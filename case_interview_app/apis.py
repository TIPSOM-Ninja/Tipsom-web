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
from .encryption import decrypt_data
from datetime import date, datetime


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
        victim.citizenship_id = decrypt_data(request.data['citizenship'])
        victim.countryOfBirth_id = decrypt_data(request.data['countryOfBirth'])
        victim.gender_id = request.data['gender']
        victim.race_id = decrypt_data(request.data['race'])
        victim.place_of_birth = decrypt_data(request.data['placeOfBirth'])
        victim.last_place_of_residence_id = decrypt_data(request.data['lastPlaceOfResidence'])
        victim.identification_number = decrypt_data(request.data['idNumber'])
        victim.initials = decrypt_data(request.data['initials'])
        victim.age = decrypt_data(request.data['age'])
        victim.address = decrypt_data(request.data['address'])
        victim.email_address = decrypt_data(request.data['email'])
        victim.interview_country_id = decrypt_data(request.data['interviewCountry'])
        victim.interview_location = decrypt_data(request.data['interviewerLocation'])
        victim.interview_date = decrypt_data(request.data['interviewDate'])
        victim.additional_remarks = decrypt_data(request.data['additionalRemarks'])
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


class TipProsecutionAPIView(APIView):
    def get(self, request, pk = None):
        prosecution =Prosecution.objects.filter(pk = pk).first()
        serializer = ProsecutionSerializer(prosecution)
        return Response(serializer.data)

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        
        prosecution = Prosecution()
        prosecution.victim_id = request.data['v_id']
        prosecution.interviewer_id = interviewer.id
        prosecution.trafficker_id = request.data['suspectedTrafficker']
        prosecution.status_of_case_id = request.data['caseStatus']
        prosecution.trial_court_id = request.data['trialCourt']
        prosecution.trial_court_country_id = request.data['foreignCourtCountry']
        prosecution.court_case_no = request.data['courtCaseNumber']
        prosecution.verdict_id = request.data['verdict']
        prosecution.guilty_verdict_reason_id = request.data['guiltyVerdict']
        prosecution.prosecution_outcome_id = request.data['prosecutionOutcome']
        prosecution.aquital_reason_id = request.data['acquittalReason']
        prosecution.review_appeal_outcome = request.data['reviewAppealOutcome']
        prosecution.sanction_penalty_id = request.data['penalty']
        prosecution.years_imposed = request.data['yearsImposed'] if not request.data['yearsImposed'] == "" else None
        prosecution.approval_id=1
        prosecution.save()
        return Response({"message": "Prosecution details created successfully","id":prosecution.id}, status=status.HTTP_201_CREATED)

class TipSuspectAPIView(APIView):
    def get(self, request, v_id=None, pk=None ):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None):
            suspect =SuspectedTrafficker.objects.all()
            paginator = Paginator(suspect, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SuspectedTraffickerSerializer(page_object, many = True)

        elif(v_id is not None and pk is None):
            suspect =SuspectedTrafficker.objects.filter(victim_id = v_id)
            serializer = SuspectedTraffickerSerializer(suspect, many = True)
        elif pk is not None:
            suspect =SuspectedTrafficker.objects.filter(victim_id = v_id).first()
            serializer = SuspectedTraffickerSerializer(suspect)
        return Response(serializer.data)
    
    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        today = date.today()
        born = datetime.strptime(request.data['dob'], '%Y-%m-%d')
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        suspect = SuspectedTrafficker()
        suspect.victim_id = request.data['v_id']
        suspect.first_name = request.data['firstName']
        suspect.last_name = request.data['surName'] 
        suspect.dob = request.data['dob']
        suspect.gender_id = request.data['gender'] 
        suspect.race_id = request.data['race']
        suspect.age = age
        suspect.country_of_birth_id = request.data['countryOfBirth'] 
        suspect.citizenship_id = request.data['citizenship']
        suspect.nationality_id = request.data['nationality']
        suspect.id_number = request.data['idNumber']
        suspect.last_residence = request.data['lastResidence']
        suspect.address = request.data['address']
        # suspect.date_of_arrest = request.data['dateOfArrest']
        # suspect.traffick_from_country_id = request.data['traffickFromCountry']
        # suspect.traffick_from_place = request.data['traffickFromPlace']
        # suspect.traffick_to_country_id = request.data['traffickToCountry']
        # suspect.traffick_to_place = request.data['traffickToPlace']
        suspect.interviewer_id=interviewer.id
        suspect.approval_id=1
        suspect.id_type_id = request.data['idTypes']
        suspect.save()
        return Response({"message": "Suspect created successfully","id":suspect.id}, status=status.HTTP_201_CREATED)

class TipExploitationAPIView(APIView):
    def get(self, request, v_id=None, pk=None ):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None):
            exploitation =Exploitation.objects.all()
            paginator = Paginator(exploitation, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ExploitationSerializer(page_object, many = True)

        elif(v_id is not None and pk is None):
            exploitation =Exploitation.objects.filter(victim_id = v_id)
            serializer = ExploitationSerializer(exploitation, many = True)
        elif pk is not None:
            exploitation =Exploitation.objects.filter(victim_id = v_id).first()
            serializer = ExploitationSerializer(exploitation)
        return Response(serializer.data)

    def post(self, request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        exploitation = Exploitation()
        exploitation.victim_id = request.data['v_id']
        exploitation.interviewer_id = interviewer.id
        exploitation.subject_to_exploitation = request.data['subjectToExploitation']
        exploitation.intent_to_exploit = request.data['intentToExploit']
        exploitation.exploitation_length = request.data['exploitationLength']
        exploitation.exploitation_age_id = int(request.data['exploitationAge']) if request.data['exploitationAge'].isdigit() else None
        exploitation.pay_debt = request.data['paidDebt']
        exploitation.debt_amount = request.data['debtAmount']
        exploitation.freed_method_id = int(request.data['freedMethod']) if request.data['freedMethod'].isdigit() else None
        exploitation.event_description = request.data['eventDescription']
        exploitation.e_prostitution = request.data['eProstitution']
        exploitation.e_other_sexual = request.data['eOtherSexual']
        exploitation.e_other_sexual_online = request.data['eOtherSexualOnline']
        exploitation.e_online_porno = request.data['eOnlinePorno']
        exploitation.e_criminal_activity = request.data['eCriminalActivity']
        exploitation.e_forced_labour = request.data['eForcedLabour']
        exploitation.e_forced_marriage = request.data['eForcedMarriage']
        exploitation.e_victim_knew_spouse = request.data['eVictimKnewSpouse']
        exploitation.e_spouse_nationality_id = int(request.data['eSpouseNationality']) if request.data['eSpouseNationality'].isdigit() else None
        exploitation.e_bprice_paid_id = int(request.data['eBPricePaid']) if request.data['eBPricePaid'].isdigit() else None
        exploitation.e_bprice_amount_kind = request.data['eBPriceAmountKind']
        exploitation.e_child_marriage = request.data['eChildMarriage']
        exploitation.e_victim_pregnancy = request.data['eVictimPregnancy']
        exploitation.e_children_from_marriage = int(request.data['eChildFromMarriage']) if request.data['eChildFromMarriage'].isdigit() else 0
        exploitation.e_maternal_health_issues = request.data['eMaternalHealthIssues']
        exploitation.e_m_health_issues_description = request.data['eMHealthIssuesDescription']
        exploitation.e_marriage_violence_id = int(request.data['eMarriageViolence']) if request.data['eMarriageViolence'].isdigit() else None
        exploitation.e_forced_military_type_id = int(request.data['eForcedMilitaryType']) if request.data['eForcedMilitaryType'].isdigit() else None
        exploitation.e_armed_group_name = request.data['eArmedGroupName']
        exploitation.e_child_soldier = request.data['eChildSoldier']
        exploitation.e_child_soldier_age = int(request.data['eChildSoldierAge'])  if request.data['eChildSoldierAge'].isdigit() else 0
        exploitation.e_organ_removed = request.data['eOrganRemoved']
        exploitation.e_operation_location_id = int(request.data['eOperationLocation']) if request.data['eOperationLocation'].isdigit() else None
        exploitation.e_operation_country_id = int(request.data['eOperationCountry']) if request.data['eOperationCountry'].isdigit() else None
        exploitation.e_organ_sale_price = request.data['eOrganSalePrice']
        exploitation.e_organ_paid_to_id = int(request.data['eOrganPaidTo']) if request.data['eOrganPaidTo'].isdigit() else None
        exploitation.e_remarks = request.data['eRemarks']
        exploitation.e_recruitment_type_id = int(request.data['eRecruitmentType']) if request.data['eRecruitmentType'].isdigit() else None
        exploitation.e_recruiter_relationship_id = int(request.data['eRecruiterRelationship']) if request.data['eRecruiterRelationship'].isdigit() else None
        exploitation.approval_id=1
        exploitation.save()

        if request.data['eCriminalActivityType']:
            for ca in request.data('eCriminalActivityType'):
                exploitation.e_criminal_activity_type.add(ca)

        if request.data['eForcedLabourIndustry']:
            for ca in request.data['eForcedLabourIndustry']:
                exploitation.e_forced_labour_industry.add(ca)

        if request.data['eBPriceRecipient']:
            for ca in request.data['eBPriceRecipient']:
                exploitation.e_brice_recipient.add(ca)

        if request.data['eChildMarriageReason']:
            for ca in request.data['eChildMarriageReason']:
                exploitation.e_child_marriage_reason.add(ca)

        if request.data['eMarriageViolenceType']:
            for ca in request.data['eMarriageViolenceType']:
                exploitation.e_marriage_violence_type.add(ca)
        
        if request.data['eVictimMilitaryActivities']:
            for ca in request.data['eVictimMilitaryActivities']:
                exploitation.e_victim_military_activities.add(ca)
        
        if request.data['eBodyPartRemoved']:
            for ca in request.data['eBodyPartRemoved']:
                exploitation.e_body_part_removed.add(ca)
        
        if request.data['eTraffickingMeans']:
            for ca in request.data['eTraffickingMeans']:
                exploitation.e_trafficking_means.add(ca)

        return Response({"message": "Exploitation records created successfully","id":exploitation.id}, status=status.HTTP_201_CREATED)

