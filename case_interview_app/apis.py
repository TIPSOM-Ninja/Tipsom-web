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

    def put(self, request, pk=None):
        victim = VictimProfile.objects.filter(pk=pk).first()
        if not victim:
            return Response({"error": "Victim not found"}, status=status.HTTP_404_NOT_FOUND)

        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        victim.citizenship_id = decrypt_data(request.data.get('citizenship')) if request.data.get('citizenship') else victim.citizenship_id
        victim.countryOfBirth_id = decrypt_data(request.data.get('countryOfBirth')) if request.data.get('countryOfBirth') else victim.countryOfBirth_id
        victim.gender_id = decrypt_data(request.data.get('gender')) if request.data.get('gender') else victim.gender_id
        victim.race_id = decrypt_data(request.data.get('race')) if request.data.get('race') else victim.race_id
        victim.place_of_birth = decrypt_data(request.data.get('placeOfBirth')) if request.data.get('placeOfBirth') else victim.place_of_birth
        victim.last_place_of_residence_id = decrypt_data(request.data.get('lastPlaceOfResidence')) if request.data.get('lastPlaceOfResidence') else victim.last_place_of_residence_id
        victim.identification_number = decrypt_data(request.data.get('idNumber')) if request.data.get('idNumber') else victim.identification_number
        victim.initials = decrypt_data(request.data.get('initials')) if request.data.get('initials') else victim.initials
        victim.age = decrypt_data(request.data.get('age')) if request.data.get('age') else victim.age
        victim.address = decrypt_data(request.data.get('address')) if request.data.get('address') else victim.address
        victim.email_address = decrypt_data(request.data.get('email')) if request.data.get('email') else victim.email_address
        victim.interview_country_id = decrypt_data(request.data.get('interviewCountry')) if request.data.get('interviewCountry') else victim.interview_country_id
        victim.interview_location = decrypt_data(request.data.get('interviewerLocation')) if request.data.get('interviewerLocation') else victim.interview_location
        victim.interview_date = decrypt_data(request.data.get('interviewDate')) if request.data.get('interviewDate') else victim.interview_date
        victim.additional_remarks = decrypt_data(request.data.get('additionalRemarks')) if request.data.get('additionalRemarks') else victim.additional_remarks
        victim.approval_id = 1
        victim.consent_share_gov_patner = 1
        victim.consent_limited_disclosure = 1
        victim.consent_research = 1
        victim.consent_abstain_answer = 1
        victim.save()

        if request.data.get('languages'):
            victim.languages.set(request.data.get('languages'))
        
        if request.data.get('idType'):
            victim.identification_type.set(request.data.get('idType'))

        return Response({"message": "Victim updated successfully","id":victim.id}, status=status.HTTP_201_CREATED)


class TipProsecutionAPIView(APIView):
    def get(self, request, v_id = None,pk=None):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None and pk is None):
            prosecution =Prosecution.objects.all()
            paginator = Paginator(prosecution, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ProsecutionSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            prosecution =Prosecution.objects.filter(victim_id = v_id)
            paginator = Paginator(prosecution, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ProsecutionSerializer(page_object,many = True)
        else:
            prosecution =Prosecution.objects.filter(pk = pk).first()
            serializer = ProsecutionSerializer(prosecution)
        return Response(serializer.data)
        

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        
        prosecution = Prosecution()
        prosecution.victim_id = request.data['v_id']
        prosecution.interviewer_id = interviewer.id
        prosecution.trafficker_id = request.data['suspectedTrafficker'] if not request.data['suspectedTrafficker'] == ""  else None
        prosecution.status_of_case_id = request.data['caseStatus'] if not request.data['caseStatus']  == "" else None
        prosecution.trial_court_id = request.data['trialCourt'] if not request.data['trialCourt']  == "" else None
        prosecution.trial_court_country_id = request.data['foreignCourtCountry'] if not request.data['foreignCourtCountry']  == "" else None
        prosecution.court_case_no = request.data['courtCaseNumber']
        prosecution.verdict_id = request.data['verdict'] if not request.data['verdict']  == "" else None
        prosecution.guilty_verdict_reason_id = request.data['guiltyVerdict'] if not request.data['guiltyVerdict']  == "" else None
        prosecution.prosecution_outcome_id = request.data['prosecutionOutcome'] if not request.data['prosecutionOutcome']  == "" else None
        prosecution.aquital_reason_id = request.data['acquittalReason'] if not request.data['acquittalReason']  == "" else None
        prosecution.review_appeal_outcome = request.data['reviewAppealOutcome']
        prosecution.sanction_penalty_id = request.data['penalty'] if not request.data['penalty']  == "" else None
        prosecution.years_imposed = int(request.data['yearsImposed']) if request.data['yearsImposed'].isdigit() else None
        prosecution.approval_id=1
        prosecution.save()
        return Response({"message": "Prosecution details created successfully","id":prosecution.id}, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None):
        prosecution = Prosecution.objects.filter(pk=pk).first()
        if not prosecution:
            return Response({"error": "Prosecution not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Update prosecution object with the provided data
        prosecution.victim_id = request.data.get('v_id', prosecution.victim_id)
        prosecution.trafficker_id = request.data.get('suspectedTrafficker', prosecution.trafficker_id) if request.data.get('suspectedTrafficker') != "" else None
        prosecution.status_of_case_id = request.data.get('caseStatus', prosecution.status_of_case_id) if request.data.get('caseStatus') != "" else None
        prosecution.trial_court_id = request.data.get('trialCourt', prosecution.trial_court_id) if request.data.get('trialCourt') != "" else None
        prosecution.trial_court_country_id = request.data.get('foreignCourtCountry', prosecution.trial_court_country_id) if request.data.get('foreignCourtCountry') != "" else None
        prosecution.court_case_no = request.data.get('courtCaseNumber', prosecution.court_case_no)
        prosecution.verdict_id = request.data.get('verdict', prosecution.verdict_id) if request.data.get('verdict') != "" else None
        prosecution.guilty_verdict_reason_id = request.data.get('guiltyVerdict', prosecution.guilty_verdict_reason_id) if request.data.get('guiltyVerdict') != "" else None
        prosecution.prosecution_outcome_id = request.data.get('prosecutionOutcome', prosecution.prosecution_outcome_id) if request.data.get('prosecutionOutcome') != "" else None
        prosecution.aquital_reason_id = request.data.get('acquittalReason', prosecution.aquital_reason_id) if request.data.get('acquittalReason') != "" else None
        prosecution.review_appeal_outcome = request.data.get('reviewAppealOutcome', prosecution.review_appeal_outcome)
        prosecution.sanction_penalty_id = request.data.get('penalty', prosecution.sanction_penalty_id) if request.data.get('penalty') != "" else None
        prosecution.years_imposed = int(request.data.get('yearsImposed', prosecution.years_imposed)) if request.data.get('yearsImposed') != "" and request.data.get('yearsImposed').isdigit() else None
        prosecution.save()
        
        return Response({"message": "Prosecution details updated successfully"}, status=status.HTTP_200_OK)

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
        suspect.race_id = int(request.data['race']) if request.data['race'].isdigit() else None
        suspect.age = age
        suspect.country_of_birth_id = int(request.data['countryOfBirth']) if request.data['countryOfBirth'].isdigit() else None 
        suspect.citizenship_id = int(request.data['citizenship']) if request.data['citizenship'].isdigit() else None
        suspect.nationality_id = int(request.data['nationality']) if request.data['nationality'].isdigit() else None
        suspect.id_number = request.data['idNumber']
        suspect.last_residence = request.data['lastPlaceOfResidence']
        suspect.address = request.data['address']
        suspect.date_of_arrest = request.data['dateOfArrest']
        suspect.traffick_from_country_id = request.data['countryFrom']
        suspect.traffick_from_place = request.data['placeFrom']
        suspect.traffick_to_country_id = request.data['countryTo']
        suspect.traffick_to_place = request.data['placeTo']
        suspect.interviewer_id=interviewer.id
        suspect.approval_id=1
        suspect.id_type_id = request.data['idType']
        suspect.save()

        for lang in request.data['languages']:
            suspect.languages.add(Language.objects.filter(id= lang).first())

        
        for rl in request.data['roleInTrafficking']:
            suspect.role_in_trafficking.add(RoleInTrafficking.objects.filter(id = rl).first())

        return Response({"message": "Suspect created successfully","id":suspect.id}, status=status.HTTP_201_CREATED)

    def put(self, request, v_id = None, pk=None):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        suspect = SuspectedTrafficker.objects.filter( pk=pk).first()
        if not suspect:
            return Response({"error": "Suspect not found"}, status=status.HTTP_404_NOT_FOUND)

        today = date.today()
        born = datetime.strptime(request.data.get('dob',suspect.dob), '%Y-%m-%d')
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        # Update suspect object with the provided data
        suspect.first_name = request.data.get('firstName', suspect.first_name)
        suspect.last_name = request.data.get('surName', suspect.last_name)
        suspect.dob = request.data.get('dob', suspect.dob)
        suspect.gender_id = request.data.get('gender',suspect.gender_id)
        suspect.race_id = int(request.data.get('race')) if request.data.get('race') else suspect.race_id
        suspect.age = age
        suspect.country_of_birth_id = int(request.data.get('countryOfBirth')) if request.data.get('countryOfBirth') and request.data.get('countryOfBirth').isdigit() else suspect.country_of_birth_id 
        suspect.citizenship_id = int(request.data.get('citizenship')) if request.data.get('citizenship') and request.data.get('citizenship').isdigit() else suspect.citizenship_id
        suspect.nationality_id = int(request.data.get('nationality')) if request.data.get('nationality') and request.data.get('nationality').isdigit() else suspect.nationality_id
        suspect.id_number = request.data.get('idNumber',suspect.id_number)
        suspect.last_residence = request.data.get('lastPlaceOfResidence',suspect.last_residence)
        suspect.address = request.data.get('address',suspect.address)
        suspect.date_of_arrest = request.data.get('dateOfArrest',suspect.date_of_arrest)
        suspect.traffick_from_country_id = request.data.get('countryFrom',suspect.traffick_from_country_id)
        suspect.traffick_from_place = request.data.get('placeFrom',suspect.traffick_from_place)
        suspect.traffick_to_country_id = request.data.get('countryTo',suspect.traffick_to_country_id)
        suspect.traffick_to_place = request.data.get('placeTo',suspect.traffick_to_place)
        suspect.interviewer_id=interviewer.id
        suspect.approval_id=1
        suspect.id_type_id = request.data.get('idType',suspect.id_type_id)
        suspect.save()

        if request.data.get('languages'):
            suspect.languages.set(request.data.get('languages'))

        
        if request.data.get('roleInTrafficking'):
            suspect.role_in_trafficking.set(request.data.get('roleInTrafficking'))

        return Response({"message": "Suspect details updated successfully"}, status=status.HTTP_200_OK)

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

    def put(self, request, v_id=None, pk=None):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        exploitation = Exploitation.objects.filter( pk=pk).first()
        if not exploitation:
            return Response({"error": "Exploitation record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update exploitation object with the provided data
        exploitation.subject_to_exploitation = request.data.get('subjectToExploitation', exploitation.subject_to_exploitation)
        exploitation.intent_to_exploit = request.data.get('intentToExploit', exploitation.intent_to_exploit)
        exploitation.exploitation_length = request.data.get('exploitationLength', exploitation.exploitation_length)
        exploitation.exploitation_age_id = int(request.data.get('exploitationAge')) if request.data.get('exploitationAge') is not None and str(request.data.get('exploitationAge')).isdigit() else exploitation.exploitation_age_id
        exploitation.pay_debt = request.data.get('paidDebt',exploitation.pay_debt)
        exploitation.debt_amount = request.data.get('debtAmount',exploitation.debt_amount)
        exploitation.freed_method_id = int(request.data.get('freedMethod',exploitation.freed_method_id)) if request.data.get('freedMethod') is not None else exploitation.freed_method_id
        exploitation.event_description = request.data.get('eventDescription',exploitation.event_description)
        exploitation.e_prostitution = request.data.get('eProstitution',exploitation.e_prostitution)
        exploitation.e_other_sexual = request.data.get('eOtherSexual',exploitation.e_other_sexual)
        exploitation.e_other_sexual_online = request.data.get('eOtherSexualOnline',exploitation.e_other_sexual_online)
        exploitation.e_online_porno = request.data.get('eOnlinePorno',exploitation.e_online_porno)
        exploitation.e_criminal_activity = request.data.get('eCriminalActivity',exploitation.e_criminal_activity)
        exploitation.e_forced_labour = request.data.get('eForcedLabour',exploitation.e_criminal_activity)
        exploitation.e_forced_marriage = request.data.get('eForcedMarriage',exploitation.e_forced_marriage)
        exploitation.e_victim_knew_spouse = request.data.get('eVictimKnewSpouse',exploitation.e_victim_knew_spouse)
        exploitation.e_spouse_nationality_id = int(request.data.get('eSpouseNationality',exploitation.e_spouse_nationality_id)) if request.data.get('eSpouseNationality') is not None and str(request.data['eSpouseNationality']).isdigit() else exploitation.e_spouse_nationality_id
        exploitation.e_bprice_paid_id = int(request.data.get('eBPricePaid',exploitation.e_bprice_paid_id)) if request.data.get('eBPricePaid') is not None and str(request.data['eBPricePaid']).isdigit() else exploitation.e_bprice_paid_id
        exploitation.e_bprice_amount_kind = request.data.get('eBPriceAmountKind',exploitation.e_bprice_amount_kind)
        exploitation.e_child_marriage = request.data.get('eChildMarriage',exploitation.e_child_marriage)
        exploitation.e_victim_pregnancy = request.data.get('eVictimPregnancy',exploitation.e_victim_pregnancy)
        exploitation.e_children_from_marriage = int(request.data.get('eChildFromMarriage',exploitation.e_children_from_marriage)) if  request.data.get('eChildFromMarriage') is not None and str(request.data['eChildFromMarriage']).isdigit() else exploitation.e_children_from_marriage
        exploitation.e_maternal_health_issues = request.data.get('eMaternalHealthIssues',exploitation.e_maternal_health_issues)
        exploitation.e_m_health_issues_description = request.data.get('eMHealthIssuesDescription',exploitation.e_m_health_issues_description)
        exploitation.e_marriage_violence_id = int(request.data.get('eMarriageViolence',exploitation.e_marriage_violence_id)) if request.data.get('eMarriageViolence') is not None and str(request.data['eMarriageViolence']).isdigit() else exploitation.e_marriage_violence_id
        exploitation.e_forced_military_type_id = int(request.data.get('eForcedMilitaryType',exploitation.e_forced_military_type_id)) if request.data.get('eForcedMilitaryType') is not None and str(request.data['eForcedMilitaryType']).isdigit() else exploitation.e_forced_military_type_id
        exploitation.e_armed_group_name = request.data.get('eArmedGroupName',exploitation.e_armed_group_name)
        exploitation.e_child_soldier = request.data.get('eChildSoldier',exploitation.e_child_soldier)
        exploitation.e_child_soldier_age = int(request.data.get('eChildSoldierAge',exploitation.e_child_soldier_age))  if request.data.get('eChildSoldierAge') is not None and str(request.data['eChildSoldierAge']).isdigit() else exploitation.e_child_soldier_age
        exploitation.e_organ_removed = request.data.get('eOrganRemoved',exploitation.e_organ_removed)
        exploitation.e_operation_location_id = int(request.data.get('eOperationLocation',exploitation.e_operation_location_id)) if request.data.get('eOperationLocation') is not None and str(request.data['eOperationLocation']).isdigit() else exploitation.e_operation_location_id
        exploitation.e_operation_country_id = int(request.data.get('eOperationCountry',exploitation.e_operation_country_id)) if request.data.get('eOperationCountry') is not None and str(request.data['eOperationCountry']).isdigit() else exploitation.e_operation_country_id
        exploitation.e_organ_sale_price = request.data.get('eOrganSalePrice',exploitation.e_organ_sale_price)
        exploitation.e_organ_paid_to_id = int(request.data.get('eOrganPaidTo',exploitation.e_organ_paid_to_id)) if request.data.get('eOrganPaidTo') is not None and str(request.data['eOrganPaidTo']).isdigit() else exploitation.e_organ_paid_to_id
        exploitation.e_remarks = request.data.get('eRemarks',exploitation.e_remarks)
        exploitation.e_recruitment_type_id = int(request.data.get('eRecruitmentType',exploitation.e_recruitment_type_id)) if request.data.get('eRecruitmentType') is not None and str(request.data['eRecruitmentType']).isdigit() else exploitation.e_recruitment_type_id
        exploitation.e_recruiter_relationship_id = int(request.data.get('eRecruiterRelationship',exploitation.e_recruiter_relationship_id)) if request.data.get('eRecruiterRelationship') is not None and str(request.data['eRecruiterRelationship']).isdigit() else exploitation.e_recruiter_relationship_id
        exploitation.approval_id=1
        exploitation.save()

        if request.data.get('eCriminalActivityType'):
            exploitation.e_criminal_activity_type.set(request.data.get('eCriminalActivityType'))

        if request.data.get('eForcedLabourIndustry'):
            exploitation.e_forced_labour_industry.set(request.data.get('eForcedLabourIndustry'))

        if request.data.get('eBPriceRecipient'):
            exploitation.e_brice_recipient.set(request.data.get('eBPriceRecipient'))

        if request.data.get('eChildMarriageReason'):
            exploitation.e_child_marriage_reason.set(request.data.get('eChildMarriageReason'))

        if request.data.get('eMarriageViolenceType'):
            exploitation.e_marriage_violence_type.set(request.data.get('eMarriageViolenceType'))
        
        if request.data.get('eVictimMilitaryActivities'):
            exploitation.e_victim_military_activities.set(request.data.get('eVictimMilitaryActivities'))
        
        if request.data.get('eBodyPartRemoved'):
            exploitation.e_body_part_removed.set(request.data.get('eBodyPartRemoved'))
        
        if request.data.get('eTraffickingMeans'):
            exploitation.e_trafficking_means.set(request.data.get('eTraffickingMeans'))

        return Response({"message": "Exploitation record updated successfully"}, status=status.HTTP_200_OK)
    

class TipTransitAPIView(APIView):
    def get(self, request, v_id=None, pk=None ):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None and pk is None):
            transit =TransitRouteDestination.objects.all()
            paginator = Paginator(transit, per_page=12)
            page_object = paginator.get_page(page)
            serializer = TransitRouteDestinationSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            transit =TransitRouteDestination.objects.filter(victim_id = v_id)
            paginator = Paginator(transit, per_page=12)
            page_object = paginator.get_page(page)
            serializer = TransitRouteDestinationSerializer(page_object,many = True)
        else:
            transit =TransitRouteDestination.objects.filter(pk = pk).first()
            serializer = TransitRouteDestinationSerializer(transit)
        return Response(serializer.data)

    def post(self, request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        transit = TransitRouteDestination()
        transit.victim_id = request.data['v_id']
        transit.country_of_origin_id = int(request.data['countryOfOrigin']) if request.data['countryOfOrigin'].isdigit() else None
        transit.country_of_dest_id = int(request.data['countryOfDestination']) if request.data['countryOfDestination'].isdigit() else None
        transit.city_village_of_dest = request.data['cityVillageOfDest']
        transit.city_village_of_origin = request.data['cityVillageOfOrigin']
        transit.remarks = request.data['remarks']
        transit.interviewer_id = interviewer.id
        transit.approval_id = 1
        transit.save()

        if request.data('meansOfTransportation') is not None:
            for item in request.data('meansOfTransportation'):
                transit.transport_means.add(int(item))
        return Response({"message": "Transit record created successfully","id":transit.id}, status=status.HTTP_201_CREATED)

    def put(self, request, v_id=None, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        transit = TransitRouteDestination.objects.filter( pk=pk).first()
        if not transit:
            return Response({"error": "Transit record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update transit object with the provided data
        transit.country_of_origin_id = int(request.data.get('countryOfOrigin',transit.country_of_origin_id)) if request.data.get('countryOfOrigin') and request.data.get('countryOfOrigin').isdigit() else transit.country_of_origin_id
        transit.country_of_dest_id = int(request.data.get('countryOfDestination',transit.country_of_dest_id)) if request.data.get('countryOfDestination') and request.data.get('countryOfDestination').isdigit() else transit.country_of_dest_id
        transit.city_village_of_dest = request.data.get('cityVillageOfDest',transit.city_village_of_dest)
        transit.city_village_of_origin = request.data.get('cityVillageOfOrigin',transit.city_village_of_origin)
        transit.remarks = request.data['remarks']
        transit.interviewer_id = interviewer.id
        transit.approval_id = 1
        # Save the updated transit object
        transit.save()

        if request.data.get('meansOfTransportation'):
            transport_means = request.data.get('meansOfTransportation',[])
            transit.transport_means.set(transport_means)

        return Response({"message": "Transit record updated successfully"}, status=status.HTTP_200_OK)

class TipArrestAPIView(APIView):
    def get(self, request, v_id = None, pk = None):
        if request.GET.get('page') is not None:
                page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None and pk is None):
            arrest =ArrestInvestigation.objects.all()
            paginator = Paginator(arrest, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ArrestInvestigationSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            arrest =ArrestInvestigation.objects.filter(victim_id = v_id)
            paginator = Paginator(arrest, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ArrestInvestigationSerializer(page_object,many = True)
        else:
            arrest =ArrestInvestigation.objects.filter(pk = pk).first()
            serializer = ArrestInvestigationSerializer(arrest)
        return Response(serializer.data)

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        
        arrest = ArrestInvestigation()
        arrest.victim_id = request.data['v_id']
        arrest.org_crime=request.data['organizedCrime']
        arrest.suspects_arrested = request.data['suspectArrested']
        arrest.why_no_arrest=request.data['whyNoArrest']
        arrest.victim_smuggled=request.data['victimSmuggled']
        arrest.investigation_done=request.data['investigationDone']
        arrest.why_no_investigation=request.data['whyNoInvestigation']
        arrest.investigation_status_id= int(request.data['investigationStatus']) if request.data['investigationStatus'].isdigit() else None
        arrest.why_pending=request.data['whyPending']
        arrest.withdrawn_closed_reason=request.data['withdrawnClosedReason']
        arrest.interviewer_id = interviewer.id
        arrest.approval_id=1
        arrest.save()
        for org in request.POST.get('howTraffickersOrg'):
            arrest.how_traffickers_org.add(TraffickerOrg.objects.filter(id= org).first())

        return Response({"message": "Arrest details created successfully","id":arrest.id}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        arrest = ArrestInvestigation.objects.filter(pk=pk).first()
        if not arrest:
            return Response({"error": "Arrest record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update arrest object with the provided data
        arrest.org_crime = request.data.get('organizedCrime', arrest.org_crime)
        arrest.suspects_arrested = request.data.get('suspectArrested', arrest.suspects_arrested)
        arrest.why_no_arrest = request.data.get('whyNoArrest', arrest.why_no_arrest)
        arrest.victim_smuggled = request.data.get('victimSmuggled', arrest.victim_smuggled)
        arrest.investigation_done = request.data.get('investigationDone', arrest.investigation_done)
        arrest.why_no_investigation = request.data.get('whyNoInvestigation', arrest.why_no_investigation)
        arrest.investigation_status_id = int(request.data.get('investigationStatus', arrest.investigation_status_id)) if request.data.get('investigationStatus') else arrest.investigation_status_id
        arrest.why_pending = request.data.get('whyPending', arrest.why_pending)
        arrest.withdrawn_closed_reason = request.data.get('withdrawnClosedReason', arrest.withdrawn_closed_reason)
        arrest.interviewer_id = interviewer.id
        arrest.approval_id = 1
        arrest.save()

        # Update many-to-many relationship
        # arrest.how_traffickers_org.clear()
        if request.data.get('howTraffickersOrg'):
            arrest.how_traffickers_org.set(request.data.get('howTraffickersOrg'))

        return Response({"message": "Arrest details updated successfully"}, status=status.HTTP_200_OK)
    
class TipAssistanceAPIView(APIView):
    def get(self, request, v_id=None, pk = None):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

        if(v_id is None and pk is None):
            assistance =Assistance.objects.all()
            paginator = Paginator(assistance, per_page=12)
            page_object = paginator.get_page(page)
            serializer = AssistanceSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            assistance =Assistance.objects.filter(victim_id = v_id)
            paginator = Paginator(assistance, per_page=12)
            page_object = paginator.get_page(page)
            serializer = AssistanceSerializer(page_object,many = True)
        else:
            assistance =Assistance.objects.filter(pk = pk).first()
            serializer = AssistanceSerializer(assistance)
        return Response(serializer.data)

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        assistance = Assistance()
        assistance.victim_id = request.data['v_id']
        assistance.interviewer_id = interviewer.id
        if request.POST.get('socialAssistanceDurationType') == '1':
            assistance.social_assistance_days = int(request.data["socialAssistanceDuration"]) if request.data['socialAssistanceDuration'].isdigit() else None
        elif request.POST.get('socialAssistanceDurationType') == '0':
            assistance.social_assistance_months = int(request.data["socialAssistanceDuration"]) if request.data['socialAssistanceDuration'].isdigit() else None
        if request.POST.get('medicalRehabilitationAssistanceDurationType') == '1':
            assistance.med_rehab_days = int(request.data["medicalRehabilitationAssistanceDuration"]) if request.data['medicalRehabilitationAssistanceDuration'].isdigit() else None
        elif request.POST.get('medicalRehabilitationAssistanceDurationType') == '0':
            assistance.med_rehab_months = int(request.data["medicalRehabilitationAssistanceDuration"]) if request.data['medicalRehabilitationAssistanceDuration'].isdigit() else None
        if request.POST.get('housingAllowanceDurationType') == '1':
            assistance.housing_allowance_days = int(request.data["housingAllowanceDuration"]) if request.data['housingAllowanceDuration'].isdigit() else None
        elif request.POST.get('housingAllowanceDurationType') == '0':
            assistance.housing_allowance_months = int(request.data["housingAllowanceDuration"]) if request.data['housingAllowanceDuration'].isdigit() else None
        if request.POST.get('halfwayHouseDurationType') == '1':
            assistance.halfway_house_days = int(request.data["halfwayHouseDuration"]) if request.data['halfwayHouseDuration'].isdigit() else None
        elif request.POST.get('halfwayHouseDurationType') == '0':
            assistance.halfway_house_months = int(request.data["halfwayHouseDuration"]) if request.data['halfwayHouseDuration'].isdigit() else None
        if request.POST.get('shelterDurationType') == '1':
            assistance.shelter_days = int(request.data["shelterDuration"]) if request.data['shelterDuration'].isdigit() else None
        elif request.POST.get('shelterDurationType') == '0':
            assistance.shelter_months = int(request.data["shelterDuration"]) if request.data['shelterDuration'].isdigit() else None
        if request.POST.get('vocationalTrainingDurationType') == '1':
            assistance.vocational_training_days = int(request.data["vocationalTrainingDuration"]) if request.data['vocationalTrainingDuration'].isdigit() else None
        elif request.POST.get('vocationalTrainingDurationType') == '0':
            assistance.vocational_training_months = int(request.data["vocationalTrainingDuration"]) if request.data['vocationalTrainingDuration'].isdigit() else None
        if request.POST.get('incomeGeneratingProjectDurationType') == '1':
            assistance.micro_ent_income_days = int(request.data["incomeGeneratingProjectDuration"]) if request.data['incomeGeneratingProjectDuration'].isdigit() else None
        elif request.POST.get('incomeGeneratingProjectDurationType') == '0':
            assistance.micro_ent_income_months = int(request.data["incomeGeneratingProjectDuration"]) if request.data['incomeGeneratingProjectDuration'].isdigit() else None
        if request.POST.get('legalAssistanceDurationType') == '1':
            assistance.legal_assistance_days = int(request.data["legalAssistanceDuration"]) if request.data['legalAssistanceDuration'].isdigit() else None
        elif request.POST.get('legalAssistanceDurationType') == '0':
            assistance.legal_assistance_months = int(request.data["legalAssistanceDuration"]) if request.data['legalAssistanceDuration'].isdigit() else None
        if request.POST.get('medicalAssistanceDurationType') == '1':
            assistance.medical_assistance_days = int(request.data["medicalAssistanceDuration"]) if request.data['medicalAssistanceDuration'].isdigit() else None
        elif request.POST.get('medicalAssistanceDurationType') == '0':
            assistance.medical_assistance_months = int(request.data["medicalAssistanceDuration"]) if request.data['medicalAssistanceDuration'].isdigit() else None
        if request.POST.get('financialAssistanceDurationType') == '1':
            assistance.financial_assistance_days = int(request.data["financialAssistanceDuration"]) if request.data['financialAssistanceDuration'].isdigit() else None
        elif request.POST.get('financialAssistanceDurationType') == '0':
            assistance.financial_assistance_months = int(request.data["financialAssistanceDuration"]) if request.data['financialAssistanceDuration'].isdigit() else None
        if request.POST.get('educationAssistanceDurationType') == '1':
            assistance.education_assistance_days = int(request.data["educationAssistanceDuration"]) if request.data['educationAssistanceDuration'].isdigit() else None
        elif request.POST.get('educationAssistanceDurationType') == '0':
            assistance.education_assistance_months = int(request.data["educationAssistanceDuration"]) if request.data['educationAssistanceDuration'].isdigit() else None
        if request.POST.get('immEmmigrationAssistanceDurationType') == '1':
            assistance.im_emmigration_assistance_days = int(request.data["immEmmigrationAssistanceDuration"]) if request.data['immEmmigrationAssistanceDuration'].isdigit() else None
        elif request.POST.get('immEmmigrationAssistanceDurationType') == '0':
            assistance.im_emmigration_assistance_months = int(request.data["immEmmigrationAssistanceDuration"]) if request.data['immEmmigrationAssistanceDuration'].isdigit() else None
        if request.POST.get('communityBasedAssistanceDurationType') == '1':
            assistance.other_community_assistance_days = int(request.data["communityBasedAssistanceDuration"]) if request.data['communityBasedAssistanceDuration'].isdigit() else None
        elif request.POST.get('communityBasedAssistanceDurationType') == '0':
            assistance.other_community_assistance_months = int(request.data["communityBasedAssistanceDuration"]) if request.data['communityBasedAssistanceDuration'].isdigit() else None
        assistance.approval_id = 1
        assistance.save()
        for it in request.data['socialAssistanceProvider']:
            assistance.social_assistance_provider.add(it)

        for it in request.data['medRehabProvider']:
            assistance.med_rehab_provider.add(it)

        for it in request.data['housingAllowanceProvider']:
            assistance.housing_allowance_provider.add(it)

        for it in request.data['halfwayHouseProvider']:
            assistance.halfway_house_providers.add(it)

        for it in request.data['shelterProvider']:
            assistance.shelter_provider.add(it)

        for it in request.data['vocationalTrainingProvider']:
            assistance.vocational_training_provider.add(it)

        for it in request.data['incomeGeneratingProjectProvider']:
            assistance.micro_ent_income_provider.add(it)

        for it in request.data['legalAssistanceProvider']:
            assistance.legal_assistance_provider.add(it)

        for it in request.data['medicalAssistanceProvider']:
            assistance.medical_assistance_provider.add(it)

        for it in request.data['financialAssistanceProvider']:
            assistance.financial_assistance_provider.add(it)

        for it in request.data['educationAssistanceProvider']:
            assistance.education_assistance_provider.add(it)

        for it in request.data['immEmmigrationAssistanceProvider']:
            assistance.im_emmigration_assistance_provider.add(it)

        for it in request.data['communityBasedAssistanceProvider']:
            assistance.other_community_assistance_provider.add(it)

        return Response({"message": "Arrest details created successfully","id":assistance.id}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        assistance = Assistance.objects.filter(pk=pk).first()
        if not assistance:
            return Response({"error": "Assistance record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update assistance object with the provided data
        assistance.victim_id = request.data.get('v_id', assistance.victim_id)
        assistance.interviewer_id = interviewer.id
        if request.POST.get('socialAssistanceDurationType') == '1':
            assistance.social_assistance_days = int(request.data.get('socialAssistanceDuration')) if request.data.get('socialAssistanceDuration') and request.data['socialAssistanceDuration'].isdigit() else assistance.social_assistance_days
        elif request.POST.get('socialAssistanceDurationType') == '0':
            assistance.social_assistance_months = int(request.data["socialAssistanceDuration"]) if request.data.get('socialAssistanceDuration') and request.data['socialAssistanceDuration'].isdigit() else assistance.social_assistance_months
        if request.POST.get('medicalRehabilitationAssistanceDurationType') == '1':
            assistance.med_rehab_days = int(request.data["medicalRehabilitationAssistanceDuration"]) if request.data.get('medicalRehabilitationAssistanceDuration') and request.data['medicalRehabilitationAssistanceDuration'].isdigit() else assistance.med_rehab_days
        elif request.POST.get('medicalRehabilitationAssistanceDurationType') == '0':
            assistance.med_rehab_months = int(request.data["medicalRehabilitationAssistanceDuration"]) if request.data.get('medicalRehabilitationAssistanceDuration') and request.data['medicalRehabilitationAssistanceDuration'].isdigit() else assistance.med_rehab_months
        if request.POST.get('housingAllowanceDurationType') == '1':
            assistance.housing_allowance_days = int(request.data["housingAllowanceDuration"]) if request.data.get('housingAllowanceDuration') and request.data['housingAllowanceDuration'].isdigit() else assistance.housing_allowance_days
        elif request.POST.get('housingAllowanceDurationType') == '0':
            assistance.housing_allowance_months = int(request.data["housingAllowanceDuration"]) if request.data.get('housingAllowanceDuration') and request.data['housingAllowanceDuration'].isdigit() else assistance.housing_allowance_months
        if request.POST.get('halfwayHouseDurationType') == '1':
            assistance.halfway_house_days = int(request.data["halfwayHouseDuration"]) if request.data.get('halfwayHouseDuration') and request.data['halfwayHouseDuration'].isdigit() else assistance.halfway_house_days
        elif request.POST.get('halfwayHouseDurationType') == '0':
            assistance.halfway_house_months = int(request.data["halfwayHouseDuration"]) if request.data.get('halfwayHouseDuration') and request.data['halfwayHouseDuration'].isdigit() else assistance.halfway_house_months
        if request.POST.get('shelterDurationType') == '1':
            assistance.shelter_days = int(request.data["shelterDuration"]) if request.data.get('shelterDuration') and request.data['shelterDuration'].isdigit() else assistance.shelter_days
        elif request.POST.get('shelterDurationType') == '0':
            assistance.shelter_months = int(request.data["shelterDuration"]) if request.data.get('shelterDuration') and request.data['shelterDuration'].isdigit() else assistance.shelter_months
        if request.POST.get('vocationalTrainingDurationType') == '1':
            assistance.vocational_training_days = int(request.data["vocationalTrainingDuration"]) if request.data.get('vocationalTrainingDuration') and request.data['vocationalTrainingDuration'].isdigit() else assistance.vocational_training_days
        elif request.POST.get('vocationalTrainingDurationType') == '0':
            assistance.vocational_training_months = int(request.data["vocationalTrainingDuration"]) if request.data.get('vocationalTrainingDuration') and request.data['vocationalTrainingDuration'].isdigit() else assistance.vocational_training_months
        if request.POST.get('incomeGeneratingProjectDurationType') == '1':
            assistance.micro_ent_income_days = int(request.data["incomeGeneratingProjectDuration"]) if request.data.get('incomeGeneratingProjectDuration') and request.data['incomeGeneratingProjectDuration'].isdigit() else assistance.micro_ent_income_days
        elif request.POST.get('incomeGeneratingProjectDurationType') == '0':
            assistance.micro_ent_income_months = int(request.data["incomeGeneratingProjectDuration"]) if request.data.get('incomeGeneratingProjectDuration') and request.data['incomeGeneratingProjectDuration'].isdigit() else assistance.micro_ent_income_months
        if request.POST.get('legalAssistanceDurationType') == '1':
            assistance.legal_assistance_days = int(request.data["legalAssistanceDuration"]) if request.data.get('legalAssistanceDuration') and request.data['legalAssistanceDuration'].isdigit() else assistance.legal_assistance_days
        elif request.POST.get('legalAssistanceDurationType') == '0':
            assistance.legal_assistance_months = int(request.data["legalAssistanceDuration"]) if request.data.get('legalAssistanceDuration') and request.data['legalAssistanceDuration'].isdigit() else assistance.legal_assistance_months
        if request.POST.get('medicalAssistanceDurationType') == '1':
            assistance.medical_assistance_days = int(request.data["medicalAssistanceDuration"]) if request.data.get('medicalAssistanceDuration') and request.data['medicalAssistanceDuration'].isdigit() else assistance.medical_assistance_days
        elif request.POST.get('medicalAssistanceDurationType') == '0':
            assistance.medical_assistance_months = int(request.data["medicalAssistanceDuration"]) if request.data.get('medicalAssistanceDuration') and request.data['medicalAssistanceDuration'].isdigit() else assistance.medical_assistance_months
        if request.POST.get('financialAssistanceDurationType') == '1':
            assistance.financial_assistance_days = int(request.data["financialAssistanceDuration"]) if request.data.get('financialAssistanceDuration') and request.data['financialAssistanceDuration'].isdigit() else assistance.financial_assistance_days
        elif request.POST.get('financialAssistanceDurationType') == '0':
            assistance.financial_assistance_months = int(request.data["financialAssistanceDuration"]) if request.data.get('financialAssistanceDuration') and request.data['financialAssistanceDuration'].isdigit() else assistance.financial_assistance_months
        if request.POST.get('educationAssistanceDurationType') == '1':
            assistance.education_assistance_days = int(request.data["educationAssistanceDuration"]) if request.data.get('educationAssistanceDuration') and request.data['educationAssistanceDuration'].isdigit() else assistance.education_assistance_days
        elif request.POST.get('educationAssistanceDurationType') == '0':
            assistance.education_assistance_months = int(request.data["educationAssistanceDuration"]) if request.data.get('educationAssistanceDuration') and request.data['educationAssistanceDuration'].isdigit() else assistance.education_assistance_months
        if request.POST.get('immEmmigrationAssistanceDurationType') == '1':
            assistance.im_emmigration_assistance_days = int(request.data["immEmmigrationAssistanceDuration"]) if request.data.get('immEmmigrationAssistanceDuration') and request.data['immEmmigrationAssistanceDuration'].isdigit() else assistance.im_emmigration_assistance_days
        elif request.POST.get('immEmmigrationAssistanceDurationType') == '0':
            assistance.im_emmigration_assistance_months = int(request.data["immEmmigrationAssistanceDuration"]) if request.data.get('immEmmigrationAssistanceDuration') and request.data['immEmmigrationAssistanceDuration'].isdigit() else assistance.im_emmigration_assistance_months
        if request.POST.get('communityBasedAssistanceDurationType') == '1':
            assistance.other_community_assistance_days = int(request.data["communityBasedAssistanceDuration"]) if request.data.get('communityBasedAssistanceDuration') and request.data['communityBasedAssistanceDuration'].isdigit() else assistance.other_community_assistance_days
        elif request.POST.get('communityBasedAssistanceDurationType') == '0':
            assistance.other_community_assistance_months = int(request.data["communityBasedAssistanceDuration"]) if request.data.get('communityBasedAssistanceDuration') and request.data['communityBasedAssistanceDuration'].isdigit() else assistance.other_community_assistance_months
        assistance.approval_id = 1

        # Your existing code to update the fields based on request data

        assistance.approval_id = 1
        assistance.save()

        # Update many-to-many relationships
        assistance.social_assistance_provider.set(request.data.get('socialAssistanceProvider'))
        assistance.med_rehab_provider.set(request.data.get('medRehabProvider'))
        assistance.housing_allowance_provider.set(request.data.get('housingAllowanceProvider'))
        assistance.halfway_house_providers.set(request.data.get('halfwayHouseProvider'))
        assistance.shelter_provider.set(request.data.get('shelterProvider'))
        assistance.vocational_training_provider.set(request.data.get('vocationalTrainingProvider'))
        assistance.micro_ent_income_provider.set(request.data.get('incomeGeneratingProjectProvider'))
        assistance.legal_assistance_provider.set(request.data.get('legalAssistanceProvider'))
        assistance.medical_assistance_provider.set(request.data.get('medicalAssistanceProvider'))
        assistance.financial_assistance_provider.set(request.data.get('financialAssistanceProvider'))
        assistance.education_assistance_provider.set(request.data.get('educationAssistanceProvider'))
        assistance.im_emmigration_assistance_provider.set(request.data.get('immEmmigrationAssistanceProvider'))
        assistance.other_community_assistance_provider.set(request.data.get('communityBasedAssistanceProvider'))

        return Response({"message": "Assistance details updated successfully"}, status=status.HTTP_200_OK)

class TipSocioAPIView(APIView):
    def get(self, request, v_id = None,pk=None):
        if request.GET.get('page') is not None:
                page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None and pk is None):
            socia =SocioEconomic.objects.all()
            paginator = Paginator(socia, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SocioEconomicSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            socia =SocioEconomic.objects.filter(victim_id = v_id)
            paginator = Paginator(socia, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SocioEconomicSerializer(page_object,many = True)
        else:
            socia =SocioEconomic.objects.filter(pk = pk).first()
            serializer = SocioEconomicSerializer(socia)
        return Response(serializer.data)

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        
        socio = SocioEconomic()
        socio.victim_id = request.session["v_id"]
        socio.family_structure_id = int(request.data['familyStructure']) if request.data['familyStructure'].isdigit() else None
        socio.living_with_id = int(request.data['livingWith']) if request.data['livingWith'].isdigit() else None
        socio.violence_prior = request.data['violencePrior']
        socio.violence_type = request.data['violenceType']
        socio.education_level_id = int(request.data['educationLevel']) if request.data['educationLevel'].isdigit() else None
        socio.interviewer_id = interviewer.id
        socio.approval_id = 1
        socio.save()

        for it in request.data['lastOccupation']:
            socio.last_occupation.add(it)
        
        return Response({"message": "Arrest details created successfully","id":socio.id}, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        socio = SocioEconomic.objects.filter(pk=pk).first()
        if not socio:
            return Response({"error": "SocioEconomic record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update socio object with the provided data
        socio.victim_id = request.session.get("v_id", socio.victim_id)
        socio.family_structure_id = int(request.data.get('familyStructure', socio.family_structure_id)) if request.data.get('familyStructure').isdigit() else socio.family_structure_id
        socio.living_with_id = int(request.data.get('livingWith', socio.living_with_id)) if request.data.get('livingWith').isdigit() else socio.living_with_id
        socio.violence_prior = request.data.get('violencePrior', socio.violence_prior)
        socio.violence_type = request.data.get('violenceType', socio.violence_type)
        socio.education_level_id = int(request.data.get('educationLevel', socio.education_level_id)) if request.data.get('educationLevel').isdigit() else socio.education_level_id
        socio.interviewer_id = interviewer.id
        socio.approval_id = 1
        socio.save()

        # Update many-to-many relationships
        socio.last_occupation.set(request.data.get('lastOccupation'))

        return Response({"message": "SocioEconomic details updated successfully"}, status=status.HTTP_200_OK)


class TipAggregateAPIView(APIView):
    def get(self, request, pk = None):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

        if(pk == None):
            aggregate =AssistanceAggregateData.objects.filter(interviewer_id = interviewer.id)
            paginator = Paginator(aggregate, per_page=12)
            page_object = paginator.get_page(page)
            serializer = AssistanceAggregateDataSerializer(page_object,many = True)
        else:
            aggregate =AssistanceAggregateData.objects.filter(pk = pk).first()
            serializer = AssistanceAggregateDataSerializer(aggregate)
        return Response(serializer.data)

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

        assistance_aggregate = AssistanceAggregateData()
        assistance_aggregate.data_supplier_id = int(request.data['dataSupplier']) if request.data['dataSupplier'].isdigit() else None
        assistance_aggregate.total_tip_annually = int(request.data['totalTip']) if request.data['totalTip'].isdigit() else None
        assistance_aggregate.total_service = int(request.data['totalVictim']) if request.data['totalVictim'].isdigit() else None
        assistance_aggregate.eligible_family_service = int(request.data['totalFamily']) if request.data['totalFamily'].isdigit() else None
        assistance_aggregate.total_anon_contacts = int(request.data['totalAnon']) if request.data['totalAnon'].isdigit() else None
        assistance_aggregate.interviewer_id = interviewer.id
        assistance_aggregate.approval_id = 1
        assistance_aggregate.save()

        return Response({"message": "Aggregate details created successfully","id":assistance_aggregate.id}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        assistance_aggregate = AssistanceAggregateData.objects.filter(pk=pk).first()
        if not assistance_aggregate:
            return Response({"error": "AssistanceAggregateData not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update assistance_aggregate object with the provided data
        assistance_aggregate.data_supplier_id = int(request.data.get('dataSupplier', assistance_aggregate.data_supplier_id)) if request.data.get('dataSupplier').isdigit() else assistance_aggregate.data_supplier_id
        assistance_aggregate.total_tip_annually = int(request.data.get('totalTip', assistance_aggregate.total_tip_annually))
        assistance_aggregate.total_service = int(request.data.get('totalVictim', assistance_aggregate.total_service))
        assistance_aggregate.eligible_family_service = int(request.data.get('totalFamily', assistance_aggregate.eligible_family_service))
        assistance_aggregate.total_anon_contacts = int(request.data.get('totalAnon', assistance_aggregate.total_anon_contacts))
        assistance_aggregate.interviewer_id = interviewer.id
        assistance_aggregate.approval_id = 1
        assistance_aggregate.save()

        return Response({"message": "Aggregate details updated successfully"}, status=status.HTTP_200_OK)


class VictimSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract query params
        query_params = request.query_params
        initials = query_params.get('initials', None)
        age = query_params.get('age', None)
        gender_id = query_params.get('gender', None)
        race_id = query_params.get('race', None)
        email = query_params.get('email', None)
        citizenship_id = query_params.get('citizenship', None)
        idNumber = query_params.get('idNumber', None)
        address = query_params.get('address', None)
        last_place_of_residence_id = query_params.get('lastPlaceOfResidence', None)
        interview_date = query_params.get('interviewDate', None)
        interviewer_location = query_params.get('interviewerLocation', None)
        date_start = query_params.get('dateStart', None)
        date_end = query_params.get('dateEnd', None)
        # Build query
        filters = Q()
        if initials:
            filters &= Q(initials__icontains=initials)
        if age:
            filters &= Q(age=age)
        if gender_id:
            filters &= Q(gender__id=gender_id)
        if race_id:
            filters &= Q(race__id=race_id)
        if email:
            filters &= Q(email_address__icontains=email)
        if citizenship_id:
            filters &= Q(citizenship__id=citizenship_id)
        if idNumber:
            filters &= Q(identification_number__icontains=idNumber)
        if address:
            filters &= Q(address__icontains=address)
        if last_place_of_residence_id:
            filters &= Q(last_place_of_residence__id=last_place_of_residence_id)
        if interview_date:
            filters &= Q(interview_date=interview_date)
        if interviewer_location:
            filters &= Q(interview_location__icontains=interviewer_location)
        if date_start and date_end:
            filters &= Q(interview_date__range=[date_start, date_end])
        # Execute query
        victims = VictimProfile.objects.filter(filters)
        serializer = VictimProfileSerializer(victims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    
class SomVictimAPIView(APIView):
    def get(self, request, c_id = None, pk=None):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if(c_id is None and pk is None):
            victim =SomVictimProfile.objects.all()
            paginator = Paginator(victim, per_page=12)
            page_object = paginator.get_page(page)
            serializer = VictimProfileWithRelatedSerializer(page_object,many = True)
        elif(c_id is not None and pk is None):
            victim =SomVictimProfile.objects.filter(case_id = c_id)
            paginator = Paginator(victim, per_page=12)
            page_object = paginator.get_page(page)
            serializer = VictimProfileWithRelatedSerializer(page_object,many = True)
        else:
            victim =SomVictimProfile.objects.filter(pk = pk).annotate(Count('som_assistance', distinct=True),Count('som_investigations', distinct=True),Count('som_prosecutions', distinct=True),Count('som_socio_economic', distinct=True),Count('som_traffickers', distinct=True),Count('som_destinations', distinct=True)).first()
            serializer = VictimProfileWithRelatedSerializer(victim)
        
        return Response(serializer.data)
    def post(self,request):
        print(request.POST)
        print("+++++++")
        print(request.data)
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        victim = SomVictimProfile()
        victim.citizenship_id = decrypt_data(request.data['citizenship'])
        victim.countryOfBirth_id = decrypt_data(request.data['countryOfBirth'])
        victim.case_id = request.data['case_id']
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

        
        interviewer.som_victims.add(victim)
        return Response({"message": "Victim created successfully","id":victim.id}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        victim = SomVictimProfile.objects.filter(pk=pk).first()
        if not victim:
            return Response({"error": "Victim not found"}, status=status.HTTP_404_NOT_FOUND)

        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        victim.citizenship_id = decrypt_data(request.data.get('citizenship')) if request.data.get('citizenship') else victim.citizenship_id
        victim.countryOfBirth_id = decrypt_data(request.data.get('countryOfBirth')) if request.data.get('countryOfBirth') else victim.countryOfBirth_id
        victim.gender_id = decrypt_data(request.data.get('gender')) if request.data.get('gender') else victim.gender_id
        victim.race_id = decrypt_data(request.data.get('race')) if request.data.get('race') else victim.race_id
        victim.place_of_birth = decrypt_data(request.data.get('placeOfBirth')) if request.data.get('placeOfBirth') else victim.place_of_birth
        victim.last_place_of_residence_id = decrypt_data(request.data.get('lastPlaceOfResidence')) if request.data.get('lastPlaceOfResidence') else victim.last_place_of_residence_id
        victim.identification_number = decrypt_data(request.data.get('idNumber')) if request.data.get('idNumber') else victim.identification_number
        victim.initials = decrypt_data(request.data.get('initials')) if request.data.get('initials') else victim.initials
        victim.age = decrypt_data(request.data.get('age')) if request.data.get('age') else victim.age
        victim.address = decrypt_data(request.data.get('address')) if request.data.get('address') else victim.address
        victim.email_address = decrypt_data(request.data.get('email')) if request.data.get('email') else victim.email_address
        victim.interview_country_id = decrypt_data(request.data.get('interviewCountry')) if request.data.get('interviewCountry') else victim.interview_country_id
        victim.interview_location = decrypt_data(request.data.get('interviewerLocation')) if request.data.get('interviewerLocation') else victim.interview_location
        victim.interview_date = decrypt_data(request.data.get('interviewDate')) if request.data.get('interviewDate') else victim.interview_date
        victim.additional_remarks = decrypt_data(request.data.get('additionalRemarks')) if request.data.get('additionalRemarks') else victim.additional_remarks
        victim.approval_id = 1
        victim.consent_share_gov_patner = 1
        victim.consent_limited_disclosure = 1
        victim.consent_research = 1
        victim.consent_abstain_answer = 1
        victim.save()

        if request.data.get('languages'):
            victim.languages.set(request.data.get('languages'))
        
        if request.data.get('idType'):
            victim.identification_type.set(request.data.get('idType'))

        return Response({"message": "Victim updated successfully","id":victim.id}, status=status.HTTP_201_CREATED)


class SomProsecutionAPIView(APIView):
    def get(self, request, v_id = None,pk=None):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None and pk is None):
            prosecution =SomProsecution.objects.all()
            paginator = Paginator(prosecution, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ProsecutionSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            prosecution =SomProsecution.objects.filter(victim_id = v_id)
            paginator = Paginator(prosecution, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ProsecutionSerializer(page_object,many = True)
        else:
            prosecution =SomProsecution.objects.filter(pk = pk).first()
            serializer = ProsecutionSerializer(prosecution)
        return Response(serializer.data)
        

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        
        prosecution = SomProsecution()
        prosecution.victim_id = request.data['v_id']
        prosecution.interviewer_id = interviewer.id
        prosecution.trafficker_id = request.data['suspectedTrafficker'] if not request.data['suspectedTrafficker'] == ""  else None
        prosecution.status_of_case_id = request.data['caseStatus'] if not request.data['caseStatus']  == "" else None
        prosecution.trial_court_id = request.data['trialCourt'] if not request.data['trialCourt']  == "" else None
        prosecution.trial_court_country_id = request.data['foreignCourtCountry'] if not request.data['foreignCourtCountry']  == "" else None
        prosecution.court_case_no = request.data['courtCaseNumber']
        prosecution.verdict_id = request.data['verdict'] if not request.data['verdict']  == "" else None
        prosecution.guilty_verdict_reason_id = request.data['guiltyVerdict'] if not request.data['guiltyVerdict']  == "" else None
        prosecution.prosecution_outcome_id = request.data['prosecutionOutcome'] if not request.data['prosecutionOutcome']  == "" else None
        prosecution.aquital_reason_id = request.data['acquittalReason'] if not request.data['acquittalReason']  == "" else None
        prosecution.review_appeal_outcome = request.data['reviewAppealOutcome']
        prosecution.sanction_penalty_id = request.data['penalty'] if not request.data['penalty']  == "" else None
        prosecution.years_imposed = int(request.data['yearsImposed']) if request.data['yearsImposed'].isdigit() else None
        prosecution.approval_id=1
        prosecution.save()
        return Response({"message": "Prosecution details created successfully","id":prosecution.id}, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None):
        prosecution = SomProsecution.objects.filter(pk=pk).first()
        if not prosecution:
            return Response({"error": "Prosecution not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Update prosecution object with the provided data
        prosecution.victim_id = request.data.get('v_id', prosecution.victim_id)
        prosecution.trafficker_id = request.data.get('suspectedTrafficker', prosecution.trafficker_id) if request.data.get('suspectedTrafficker') != "" else None
        prosecution.status_of_case_id = request.data.get('caseStatus', prosecution.status_of_case_id) if request.data.get('caseStatus') != "" else None
        prosecution.trial_court_id = request.data.get('trialCourt', prosecution.trial_court_id) if request.data.get('trialCourt') != "" else None
        prosecution.trial_court_country_id = request.data.get('foreignCourtCountry', prosecution.trial_court_country_id) if request.data.get('foreignCourtCountry') != "" else None
        prosecution.court_case_no = request.data.get('courtCaseNumber', prosecution.court_case_no)
        prosecution.verdict_id = request.data.get('verdict', prosecution.verdict_id) if request.data.get('verdict') != "" else None
        prosecution.guilty_verdict_reason_id = request.data.get('guiltyVerdict', prosecution.guilty_verdict_reason_id) if request.data.get('guiltyVerdict') != "" else None
        prosecution.prosecution_outcome_id = request.data.get('prosecutionOutcome', prosecution.prosecution_outcome_id) if request.data.get('prosecutionOutcome') != "" else None
        prosecution.aquital_reason_id = request.data.get('acquittalReason', prosecution.aquital_reason_id) if request.data.get('acquittalReason') != "" else None
        prosecution.review_appeal_outcome = request.data.get('reviewAppealOutcome', prosecution.review_appeal_outcome)
        prosecution.sanction_penalty_id = request.data.get('penalty', prosecution.sanction_penalty_id) if request.data.get('penalty') != "" else None
        prosecution.years_imposed = int(request.data.get('yearsImposed', prosecution.years_imposed)) if request.data.get('yearsImposed') != "" and request.data.get('yearsImposed').isdigit() else None
        prosecution.save()
        
        return Response({"message": "Prosecution details updated successfully"}, status=status.HTTP_200_OK)

class SomCaseAPIView(APIView):
    def get(self, request, pk=None ):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if (pk is None):
            som_case =SomCase.objects.filter(interviewer__id = interviewer.id)
            paginator = Paginator(som_case, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SomCaseSerializer(page_object, many = True)

        elif pk is not None:
            som_case =SomCase.objects.filter(pk = pk).first()
            serializer = SomCaseSerializer(som_case)

        return Response(serializer.data)
    
    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        
        case = SomCase()
        case.date_of_arrest = request.data['dateOfArrest']
        case.traffick_from_country_id = request.data['countryFrom']
        case.traffick_from_place = request.data['placeFrom']
        case.traffick_to_country_id = request.data['countryTo']
        case.traffick_to_place = request.data['placeTo']
        case.approval_id=1
        case.save()

        interviewer.som_cases.add(case)
        return Response({"message": "Suspect created successfully","id":case.id}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        case = SomCase.objects.filter( pk=pk).first()
        if not case:
            return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

        
        # Update suspect object with the provided data
       
        case.date_of_arrest = request.data.get('dateOfArrest')
        case.traffick_from_country_id = request.data.get('countryFrom')
        case.traffick_from_place = request.data.get('placeFrom')
        case.traffick_to_country_id = request.data.get('countryTo')
        case.traffick_to_place = request.data.get('placeTo')
        case.interviewer_id=interviewer.id
        case.approval_id=1
        case.save()


        return Response({"message": "Suspect details updated successfully"}, status=status.HTTP_200_OK)

class SomSuspectAPIView(APIView):
    def get(self, request, v_id=None, pk=None ):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None):
            suspect =SomSuspectedTrafficker.objects.all()
            paginator = Paginator(suspect, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SuspectedTraffickerSerializer(page_object, many = True)

        elif(v_id is not None and pk is None):
            suspect =SomSuspectedTrafficker.objects.filter(victim_id = v_id)
            serializer = SuspectedTraffickerSerializer(suspect, many = True)
        elif pk is not None:
            suspect =SomSuspectedTrafficker.objects.filter(victim_id = v_id).first()
            serializer = SuspectedTraffickerSerializer(suspect)
        return Response(serializer.data)
    
    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        today = date.today()
        born = datetime.strptime(request.data['dob'], '%Y-%m-%d')
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        suspect = SomSuspectedTrafficker()
        suspect.case_id = request.data['case_id']
        suspect.first_name = request.data['firstName']
        suspect.last_name = request.data['surName'] 
        suspect.dob = request.data['dob']
        suspect.gender_id = request.data['gender']
        suspect.race_id = int(request.data['race']) if request.data['race'].isdigit() else None
        suspect.age = age
        suspect.country_of_birth_id = int(request.data['countryOfBirth']) if request.data['countryOfBirth'].isdigit() else None 
        suspect.citizenship_id = int(request.data['citizenship']) if request.data['citizenship'].isdigit() else None
        suspect.nationality_id = int(request.data['nationality']) if request.data['nationality'].isdigit() else None
        suspect.id_number = request.data['idNumber']
        suspect.last_residence = request.data['lastPlaceOfResidence']
        suspect.address = request.data['address']
        suspect.date_of_arrest = request.data['dateOfArrest']
        suspect.traffick_from_country_id = request.data['countryFrom']
        suspect.traffick_from_place = request.data['placeFrom']
        suspect.traffick_to_country_id = request.data['countryTo']
        suspect.traffick_to_place = request.data['placeTo']
        suspect.interviewer_id=interviewer.id
        suspect.approval_id=1
        suspect.id_type_id = request.data['idType']
        suspect.save()

        for lang in request.data['languages']:
            suspect.languages.add(Language.objects.filter(id= lang).first())

        
        for rl in request.data['roleInTrafficking']:
            suspect.role_in_trafficking.add(RoleInTrafficking.objects.filter(id = rl).first())

        return Response({"message": "Suspect created successfully","id":suspect.id}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        suspect = SomSuspectedTrafficker.objects.filter( pk=pk).first()
        if not suspect:
            return Response({"error": "Suspect not found"}, status=status.HTTP_404_NOT_FOUND)

        today = date.today()
        born = datetime.strptime(request.data.get('dob'), '%Y-%m-%d')
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        # Update suspect object with the provided data
        suspect.first_name = request.data.get('firstName', suspect.first_name)
        suspect.last_name = request.data.get('surName', suspect.last_name)
        suspect.dob = request.data.get('dob', suspect.dob)
        suspect.gender_id = request.data.get('gender',suspect.gender_id)
        suspect.race_id = int(request.data.get('race')) if request.data.get('race') else suspect.race_id
        suspect.age = age
        suspect.country_of_birth_id = int(request.data.get('countryOfBirth')) if request.data.get('countryOfBirth') and request.data.get('countryOfBirth').isdigit() else suspect.country_of_birth_id 
        suspect.citizenship_id = int(request.data.get('citizenship')) if request.data.get('citizenship') and request.data.get('citizenship').isdigit() else suspect.citizenship_id
        suspect.nationality_id = int(request.data.get('nationality')) if request.data.get('nationality') and request.data.get('nationality').isdigit() else suspect.nationality_id
        suspect.id_number = request.data.get('idNumber',suspect.id_number)
        suspect.last_residence = request.data.get('lastPlaceOfResidence',suspect.last_residence)
        suspect.address = request.data.get('address',suspect.address)
        suspect.date_of_arrest = request.data.get('dateOfArrest',suspect.date_of_arrest)
        suspect.traffick_from_country_id = request.data.get('countryFrom',suspect.traffick_from_country_id)
        suspect.traffick_from_place = request.data.get('placeFrom',suspect.traffick_from_place)
        suspect.traffick_to_country_id = request.data.get('countryTo',suspect.traffick_to_country_id)
        suspect.traffick_to_place = request.data.get('placeTo',suspect.traffick_to_place)
        suspect.interviewer_id=interviewer.id
        suspect.approval_id=1
        suspect.id_type_id = request.data.get('idType')
        suspect.save()

        if request.data.get('languages'):
            suspect.languages.set(request.data.get('languages'))

        
        if request.data.get('roleInTrafficking'):
            suspect.role_in_trafficking.set(request.data.get('roleInTrafficking'))

        return Response({"message": "Suspect details updated successfully"}, status=status.HTTP_200_OK)

class SomTransitAPIView(APIView):
    def get(self, request, c_id=None, pk=None ):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        if(c_id is None and pk is None):
            transit =SomTransitRouteDestination.objects.all()
            paginator = Paginator(transit, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SomTransitRouteDestinationSerializer(page_object,many = True)
        elif(c_id is not None and pk is None):
            transit =SomTransitRouteDestination.objects.filter(case_id = c_id)
            paginator = Paginator(transit, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SomTransitRouteDestinationSerializer(page_object,many = True)
        else:
            transit =SomTransitRouteDestination.objects.filter(pk = pk).first()
            serializer = SomTransitRouteDestinationSerializer(transit)
        return Response(serializer.data)

    def post(self, request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        transit = SomTransitRouteDestination()
        transit.case_id = request.data['case_id']
        transit.country_of_origin_id = int(request.data['countryOfOrigin']) if request.data['countryOfOrigin'].isdigit() else None
        transit.country_of_dest_id = int(request.data['countryOfDestination']) if request.data['countryOfDestination'].isdigit() else None
        transit.country_of_interception_id = int(request.data['countryOfInterception']) if request.data['countryOfInterception'].isdigit() else None
        transit.remarks = request.data['remarks']
        transit.interviewer_id = interviewer.id
        transit.approval_id = 1
        transit.save()

        if request.data.get('meansOfTransportation'):
            for item in request.data.get('meansOfTransportation'):
                transit.transport_means.add(int(item))
        
        if request.data.get('countriesOfTransit'):
            for item in request.data.get('countriesOfTransit'):
                transit.countries_of_transit.add(int(item))

        return Response({"message": "Transit record created successfully","id":transit.id}, status=status.HTTP_201_CREATED)

    def put(self, request, c_id=None, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        transit = SomTransitRouteDestination.objects.filter( pk=pk).first()
        if not transit:
            return Response({"error": "Transit record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update transit object with the provided data

        transit.country_of_origin_id = int(request.data['countryOfOrigin']) if request.data.get('countryOfOrigin') and request.data.get('countryOfOrigin').isdigit() else transit.country_of_origin_id
        transit.country_of_dest_id = int(request.data['countryOfDestination']) if request.data.get('countryOfDestination') and request.data.get('countryOfDestination').isdigit() else transit.country_of_dest_id
        transit.country_of_interception_id = int(request.data['countryOfInterception']) if request.data.get('countryOfInterception') and request.data.get('countryOfInterception').isdigit() else transit.country_of_interception_id
        transit.remarks = request.data.get('remarks',transit.remarks)
        transit.interviewer_id = interviewer.id
        transit.approval_id = 1
        # Save the updated transit object
        transit.save()

        if request.data.get('meansOfTransportation'):
            tr = request.data.get('meansOfTransportation',[])
            transit.transport_means.set(tr)
        if request.data.get('countriesOfTransit'):
            ct = request.data.get('countriesOfTransit')
            transit.countries_of_transit.set(ct)

                
        return Response({"message": "Transit record updated successfully"}, status=status.HTTP_200_OK)

class SomArrestAPIView(APIView):
    def get(self, request, v_id = None, pk = None):
        if request.GET.get('page') is not None:
                page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None and pk is None):
            arrest =SomArrestInvestigation.objects.all()
            paginator = Paginator(arrest, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ArrestInvestigationSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            arrest =SomArrestInvestigation.objects.filter(victim_id = v_id)
            paginator = Paginator(arrest, per_page=12)
            page_object = paginator.get_page(page)
            serializer = ArrestInvestigationSerializer(page_object,many = True)
        else:
            arrest =SomArrestInvestigation.objects.filter(pk = pk).first()
            serializer = ArrestInvestigationSerializer(arrest)
        return Response(serializer.data)

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        
        arrest = SomArrestInvestigation()
        arrest.case_id = request.data['case_id']
        arrest.org_crime=request.data['organizedCrime']
        arrest.suspects_arrested = request.data['suspectArrested']
        arrest.why_no_arrest=request.data['whyNoArrest']
        arrest.victim_smuggled=request.data['victimSmuggled']
        arrest.investigation_done=request.data['investigationDone']
        arrest.why_no_investigation=request.data['whyNoInvestigation']
        arrest.investigation_status_id= int(request.data['investigationStatus']) if request.data['investigationStatus'].isdigit() else None
        arrest.why_pending=request.data['whyPending']
        arrest.withdrawn_closed_reason=request.data['withdrawnClosedReason']
        arrest.interviewer_id = interviewer.id
        arrest.approval_id=1
        arrest.save()
        for org in request.POST.get('howTraffickersOrg'):
            arrest.how_traffickers_org.add(TraffickerOrg.objects.filter(id= org).first())

        return Response({"message": "Arrest details created successfully","id":arrest.id}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        arrest = SomArrestInvestigation.objects.filter(pk=pk).first()
        if not arrest:
            return Response({"error": "Arrest record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update arrest object with the provided data
        arrest.org_crime = request.data.get('organizedCrime', arrest.org_crime)
        arrest.suspects_arrested = request.data.get('suspectArrested', arrest.suspects_arrested)
        arrest.why_no_arrest = request.data.get('whyNoArrest', arrest.why_no_arrest)
        arrest.victim_smuggled = request.data.get('victimSmuggled', arrest.victim_smuggled)
        arrest.investigation_done = request.data.get('investigationDone', arrest.investigation_done)
        arrest.why_no_investigation = request.data.get('whyNoInvestigation', arrest.why_no_investigation)
        arrest.investigation_status_id = int(request.data.get('investigationStatus', arrest.investigation_status_id)) if request.data.get('investigationStatus') else arrest.investigation_status_id
        arrest.why_pending = request.data.get('whyPending', arrest.why_pending)
        arrest.withdrawn_closed_reason = request.data.get('withdrawnClosedReason', arrest.withdrawn_closed_reason)
        arrest.interviewer_id = interviewer.id
        arrest.approval_id = 1
        arrest.save()

        # Update many-to-many relationship
        arrest.how_traffickers_org.clear()
        if request.data.get('howTraffickersOrg'):
            arrest.how_traffickers_org.set(request.data.get('howTraffickersOrg'))

        return Response({"message": "Arrest details updated successfully"}, status=status.HTTP_200_OK)
    
class SomAssistanceAPIView(APIView):
    def get(self, request, v_id=None, pk = None):
        if request.GET.get('page') is not None:
            page = request.GET.get('page')
        else:
            page = 1
        
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

        if(v_id is None and pk is None):
            assistance =SomAssistance.objects.all()
            paginator = Paginator(assistance, per_page=12)
            page_object = paginator.get_page(page)
            serializer = AssistanceSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            assistance =SomAssistance.objects.filter(victim_id = v_id)
            paginator = Paginator(assistance, per_page=12)
            page_object = paginator.get_page(page)
            serializer = AssistanceSerializer(page_object,many = True)
        else:
            assistance =SomAssistance.objects.filter(pk = pk).first()
            serializer = AssistanceSerializer(assistance)
        return Response(serializer.data)

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        assistance = SomAssistance()
        assistance.victim_id = request.data['v_id']
        assistance.social_assistance = request.data['socialAssistance']
        assistance.med_rehab = request.data['medRehab']
        assistance.housing_allowance = request.data['housingAllowance']
        assistance.halfway_house = request.data['halfwayHouse']
        assistance.shelter = request.data['shelter']
        assistance.vocational_training = request.data['vocationalTraining']
        assistance.micro_ent_income = request.data['incomeGeneratingProject']
        assistance.legal_assistance = request.data['legalAssistance']
        assistance.medical_assistance = request.data['medicalAssistance']
        assistance.financial_assistance = request.data['financialAssistance']
        assistance.education_assistance = request.data['educationAssistance']
        assistance.im_emmigration_assistance = request.data['immEmmigrationAssistance']
        assistance.other_community_assistance = request.data['communityBasedAssistance']
        assistance.interviewer_id = interviewer.id
        assistance.approval_id = 1
        assistance.save()
        for it in request.data['socialAssistanceProvider']:
            assistance.social_assistance_provider.add(it)

        for it in request.data['medRehabProvider']:
            assistance.med_rehab_provider.add(it)

        for it in request.data['housingAllowanceProvider']:
            assistance.housing_allowance_provider.add(it)

        for it in request.data['halfwayHouseProvider']:
            assistance.halfway_house_providers.add(it)

        for it in request.data['shelterProvider']:
            assistance.shelter_provider.add(it)

        for it in request.data['vocationalTrainingProvider']:
            assistance.vocational_training_provider.add(it)

        for it in request.data['incomeGeneratingProjectProvider']:
            assistance.micro_ent_income_provider.add(it)

        for it in request.data['legalAssistanceProvider']:
            assistance.legal_assistance_provider.add(it)

        for it in request.data['medicalAssistanceProvider']:
            assistance.medical_assistance_provider.add(it)

        for it in request.data['financialAssistanceProvider']:
            assistance.financial_assistance_provider.add(it)

        for it in request.data['educationAssistanceProvider']:
            assistance.education_assistance_provider.add(it)

        for it in request.data['immEmmigrationAssistanceProvider']:
            assistance.im_emmigration_assistance_provider.add(it)

        for it in request.data['communityBasedAssistanceProvider']:
            assistance.other_community_assistance_provider.add(it)

        return Response({"message": "Arrest details created successfully","id":assistance.id}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        assistance = SomAssistance.objects.filter(pk=pk).first()
        if not assistance:
            return Response({"error": "Assistance record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update assistance object with the provided data
        assistance.victim_id = request.data.get('v_id', assistance.victim_id)
        assistance.social_assistance =  request.data.get('socialAssistance',assistance.social_assistance)
        assistance.med_rehab =  request.data.get('medRehab',assistance.med_rehab)
        assistance.housing_allowance =  request.data.get('housingAllowance',assistance.housing_allowance)
        assistance.halfway_house =  request.data.get('halfwayHouse',assistance.halfway_house)
        assistance.shelter =  request.data.get('shelter',assistance.shelter)
        assistance.vocational_training =  request.data.get('vocationalTraining',assistance.vocational_training)
        assistance.micro_ent_income =  request.data.get('incomeGeneratingProject',assistance.micro_ent_income)
        assistance.legal_assistance =  request.data.get('legalAssistance',assistance.legal_assistance)
        assistance.medical_assistance =  request.data.get('medicalAssistance',assistance.medical_assistance)
        assistance.financial_assistance =  request.data.get('financialAssistance',assistance.financial_assistance)
        assistance.education_assistance =  request.data.get('educationAssistance',assistance.education_assistance)
        assistance.im_emmigration_assistance =  request.data.get('immEmmigrationAssistance',assistance.im_emmigration_assistance)
        assistance.other_community_assistance =  request.data.get('communityBasedAssistance',assistance.other_community_assistance)
        assistance.interviewer_id = interviewer.id
        assistance.approval_id = 1

        # Your existing code to update the fields based on request data

        assistance.approval_id = 1
        assistance.save()

        # Update many-to-many relationships
        assistance.social_assistance_provider.set(request.data.get('socialAssistanceProvider'))
        assistance.med_rehab_provider.set(request.data.get('medRehabProvider'))
        assistance.housing_allowance_provider.set(request.data.get('housingAllowanceProvider'))
        assistance.halfway_house_providers.set(request.data.get('halfwayHouseProvider'))
        assistance.shelter_provider.set(request.data.get('shelterProvider'))
        assistance.vocational_training_provider.set(request.data.get('vocationalTrainingProvider'))
        assistance.micro_ent_income_provider.set(request.data.get('incomeGeneratingProjectProvider'))
        assistance.legal_assistance_provider.set(request.data.get('legalAssistanceProvider'))
        assistance.medical_assistance_provider.set(request.data.get('medicalAssistanceProvider'))
        assistance.financial_assistance_provider.set(request.data.get('financialAssistanceProvider'))
        assistance.education_assistance_provider.set(request.data.get('educationAssistanceProvider'))
        assistance.im_emmigration_assistance_provider.set(request.data.get('immEmmigrationAssistanceProvider'))
        assistance.other_community_assistance_provider.set(request.data.get('communityBasedAssistanceProvider'))

        return Response({"message": "Assistance details updated successfully"}, status=status.HTTP_200_OK)

class SomSocioAPIView(APIView):
    def get(self, request, v_id = None,pk=None):
        if request.GET.get('page') is not None:
                page = request.GET.get('page')
        else:
            page = 1
        if(v_id is None and pk is None):
            socia =SomSocioEconomic.objects.all()
            paginator = Paginator(socia, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SocioEconomicSerializer(page_object,many = True)
        elif(v_id is not None and pk is None):
            socia =SomSocioEconomic.objects.filter(victim_id = v_id)
            paginator = Paginator(socia, per_page=12)
            page_object = paginator.get_page(page)
            serializer = SocioEconomicSerializer(page_object,many = True)
        else:
            socia =SomSocioEconomic.objects.filter(pk = pk).first()
            serializer = SocioEconomicSerializer(socia)
        return Response(serializer.data)

    def post(self,request):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        
        socio = SomSocioEconomic()
        socio.case_id = request.data.get("case_id")
        socio.victim_id = request.data.get("v_id")
        socio.family_structure_id = int(request.data['familyStructure']) if request.data.get('familyStructure') and request.data['familyStructure'].isdigit() else None
        socio.living_with_id = int(request.data['livingWith']) if request.data.get('livingWith') and request.data['livingWith'].isdigit() else None
        socio.violence_prior = request.data['violencePrior']
        socio.violence_type = request.data['violenceType']
        socio.education_level_id = int(request.data['educationLevel']) if request.data.get('educationLevel') and request.data['educationLevel'].isdigit() else None
        socio.interviewer_id = interviewer.id
        socio.approval_id = 1
        socio.save()

        for it in request.data['lastOccupation']:
            socio.last_occupation.add(it)
        
        return Response({"message": "Arrest details created successfully","id":socio.id}, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk=None):
        interviewer = Interviewer.objects.filter(email_address=request.user.email).first()
        socio = SomSocioEconomic.objects.filter(pk=pk).first()
        if not socio:
            return Response({"error": "SocioEconomic record not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update socio object with the provided data
        socio.victim_id = request.data.get("v_id", socio.victim_id)
        socio.family_structure_id = int(request.data.get('familyStructure', socio.family_structure_id)) if request.data.get('familyStructure') and request.data.get('familyStructure').isdigit() else socio.family_structure_id
        socio.living_with_id = int(request.data.get('livingWith', socio.living_with_id)) if request.data.get('livingWith') and request.data.get('livingWith').isdigit() else socio.living_with_id
        socio.violence_prior = request.data.get('violencePrior', socio.violence_prior)
        socio.violence_type = request.data.get('violenceType', socio.violence_type)
        socio.education_level_id = int(request.data.get('educationLevel', socio.education_level_id)) if request.data.get('educationLevel') and request.data.get('educationLevel').isdigit() else socio.education_level_id
        socio.interviewer_id = interviewer.id
        socio.approval_id = 1
        socio.save()

        # Update many-to-many relationships
        socio.last_occupation.set(request.data.get('lastOccupation'))

        return Response({"message": "SocioEconomic details updated successfully"}, status=status.HTTP_200_OK)

class SomVictimSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract query params
        query_params = request.query_params
        initials = query_params.get('initials', None)
        age = query_params.get('age', None)
        gender_id = query_params.get('gender', None)
        race_id = query_params.get('race', None)
        email = query_params.get('email', None)
        citizenship_id = query_params.get('citizenship', None)
        idNumber = query_params.get('idNumber', None)
        address = query_params.get('address', None)
        last_place_of_residence_id = query_params.get('lastPlaceOfResidence', None)
        interview_date = query_params.get('interviewDate', None)
        interviewer_location = query_params.get('interviewerLocation', None)
        date_start = query_params.get('dateStart', None)
        date_end = query_params.get('dateEnd', None)
        # Build query
        filters = Q()
        if initials:
            filters &= Q(initials__icontains=initials)
        if age:
            filters &= Q(age=age)
        if gender_id:
            filters &= Q(gender__id=gender_id)
        if race_id:
            filters &= Q(race__id=race_id)
        if email:
            filters &= Q(email_address__icontains=email)
        if citizenship_id:
            filters &= Q(citizenship__id=citizenship_id)
        if idNumber:
            filters &= Q(identification_number__icontains=idNumber)
        if address:
            filters &= Q(address__icontains=address)
        if last_place_of_residence_id:
            filters &= Q(last_place_of_residence__id=last_place_of_residence_id)
        if interview_date:
            filters &= Q(interview_date=interview_date)
        if interviewer_location:
            filters &= Q(interview_location__icontains=interviewer_location)
        if date_start and date_end:
            filters &= Q(interview_date__range=[date_start, date_end])
        # Execute query
        victims = SomVictimProfile.objects.filter(filters)
        serializer = SomVictimProfileSerializer(victims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

