from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from django_otp.plugins.otp_email.models import EmailDevice
from django.shortcuts import get_object_or_404
from django.db.models import Count,Q
from django.utils.translation import activate, get_language_info
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class InterviewerRegistrationAPIView(APIView):
    def get(self, request, pk=None):
        if pk==0:
            if request.user.is_authenticated:
                interviewer = Interviewer.objects.filter(email_address=request.user.username).first()
            else:   
                interviewer = get_object_or_404(Interviewer, pk=pk)
            serializer = InterviewerSerializer(interviewer)
        else:
            if request.user.is_staff:
                interviewers = Interviewer.objects.all()
                serializer = InterviewerSerializer(interviewers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = InterviewerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email_address']

            # Optionally create a user account
            if 'password' in request.data:
                user, created = User.objects.get_or_create(username=email, email=email)
                if created:
                    user.set_password(request.data['password'])
                    user.save()
                    # Set up email device for two-factor authentication
                    EmailDevice.objects.create(user=user, name="default", confirmed=True)
                    return Response({"message": "Interviewer and user account created successfully"}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Interviewer created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        interviewer = get_object_or_404(Interviewer, pk=pk)
        serializer = InterviewerSerializer(interviewer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Interviewer updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CasesWithCountsAPIView(APIView):
    def get(self, request):
        if request.GET.get('language') is not None:
            activate(request.GET.get('language'))
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()

        if request.user.is_staff:
            if request.GET.get('pending') is None:
                victims = VictimProfile.objects.filter(interviewer__id = interviewer.id).order_by('id').annotate(Count('assistance', distinct=True),Count('exploitation', distinct=True),Count('investigations', distinct=True),Count('prosecutions', distinct=True),Count('socio_economic', distinct=True),Count('traffickers', distinct=True),Count('destinations', distinct=True))|VictimProfile.objects.filter(interview_country_id = interviewer.country_id).order_by('id').annotate(Count('assistance', distinct=True),Count('exploitation', distinct=True),Count('investigations', distinct=True),Count('prosecutions', distinct=True),Count('socio_economic', distinct=True),Count('traffickers', distinct=True),Count('destinations', distinct=True))
            else:
                victims = VictimProfile.objects.filter(interview_country_id = interviewer.country_id,approval_id = 1).order_by('id').annotate(Count('assistance', distinct=True),Count('exploitation', distinct=True),Count('investigations', distinct=True),Count('prosecutions', distinct=True),Count('socio_economic', distinct=True),Count('traffickers', distinct=True),Count('destinations', distinct=True))
        else:
            victims = interviewer.victims.order_by('id').annotate(Count('assistance', distinct=True),Count('exploitation', distinct=True),Count('investigations', distinct=True),Count('prosecutions', distinct=True),Count('socio_economic', distinct=True),Count('traffickers', distinct=True),Count('destinations', distinct=True))


        paginator = Paginator(victims, per_page=12)
        page_object = paginator.get_page(page)

        if request.session.get('v_id') is not None:
            del request.session['v_id']
        if request.session.get('consent_given') is not None:
            del request.session['consent_given']

        # Serialize the data using the custom serializer
        serializer = VictimProfileWithCountsSerializer(page_object, many=True)
        interviewer_serializer = InterviewerSerializer(interviewer)
        context = {
            "victims": serializer.data,
            "page": {
                "current": page_object.number,
                "has_next": page_object.has_next(),
                "has_previous": page_object.has_previous(),
            },
            "interviewer": interviewer_serializer.data
        }

        return Response(context)
    
class TipVictimAPIView(APIView):
    def get(self, request, pk=None):
        victim =VictimProfile.objects.filter(pk = pk).annotate(Count('assistance', distinct=True),Count('exploitation', distinct=True),Count('investigations', distinct=True),Count('prosecutions', distinct=True),Count('socio_economic', distinct=True),Count('traffickers', distinct=True),Count('destinations', distinct=True)).first()
        serializer = VictimProfileWithRelatedSerializer(victim)
        return Response(serializer.data)
    def post(self,request):
        print(request.POST)
        print("+++++++")
        print(request.data)
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        victim = VictimProfile()
        victim.citizenship_id = request.data['citizenship']
        victim.countryOfBirth_id = request.data['countryOfBirth']
        victim.gender_id = request.data['gender']
        victim.race_id = request.data['race']
        victim.place_of_birth = request.data['placeOfBirth']
        victim.last_place_of_residence_id = request.data['lastPlaceOfResidence']
        victim.identification_number = request.data['idNumber']
        victim.initials = request.data['initials']
        victim.age = request.data['age']
        victim.address = request.data['address']
        victim.email_address = request.data['email']
        victim.interview_country_id = request.data['interviewCountry']
        victim.interview_location = request.data['interviewerLocation']
        victim.interview_date = request.data['interviewDate']
        victim.additional_remarks = request.data['additionalRemarks']
        victim.approval_id = 1
        victim.consent_share_gov_patner = 1
        victim.consent_limited_disclosure = 1
        victim.consent_research = 1
        victim.consent_abstain_answer = 1
        victim.save()
        if interviewer.data_entry_purpose_id == 1:
            victim.victim_identifier = victim.citizenship.two_code+"-TP-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 2:
            victim.victim_identifier = victim.citizenship.two_code+"-IV-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 3:
            victim.victim_identifier = victim.citizenship.two_code+"-PR-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 4:
            victim.victim_identifier = victim.citizenship.two_code+"-AS-"+str(victim.id)
        victim.save()
        for lang in request.data['languages']:
            victim.languages.add(Language.objects.filter(id= lang).first())
        
        for idt in request.data['idType']:
            victim.identification_type.add(IdType.objects.filter(id = idt).first())

        
        interviewer.victims.add(victim)
        return Response({"message": "Victim created successfully","id":victim.id}, status=status.HTTP_201_CREATED)

           