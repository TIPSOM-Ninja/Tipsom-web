from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import InterviewerSerializer, VictimProfileWithCountsSerializer
from .models import *
from django_otp.plugins.otp_email.models import EmailDevice
from django.shortcuts import get_object_or_404
from django.db.models import Count,Q
from django.utils.translation import activate, get_language_info
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class InterviewerRegistrationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
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