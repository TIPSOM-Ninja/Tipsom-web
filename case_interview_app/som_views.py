from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import activate, get_language_info
from datetime import date, datetime
from django.db.models import Count,Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django_otp.decorators import otp_required
from django_otp.plugins.otp_email.models import EmailDevice
from .forms import VictimSearchForm, InterviewerSearchForm, TraffickerSearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required
def investigation_form(request):
    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    

    if(request.user.is_authenticated):
        countries = Country.objects.all().order_by('name').values()
        purposes = DataEntryPurpose.objects.all()
        languages = Language.objects.all()
        genders = Gender.objects.all()
        races = Race.objects.all()
        idtypes = IdType.objects.all()
        trafficker_orgs = TraffickerOrg.objects.all()
        investigation_statuses = InvestigationStatus.objects.all()
        roles_in_trafficking = RoleInTrafficking.objects.all()

        context = {
            "countries":countries,
            "purposes":purposes,
            "languages":languages,
            "genders":genders,
            "races":races,
            "idtypes":idtypes,
            'trafficker_orgs':trafficker_orgs,
            'investigation_statuses':investigation_statuses,
            'roles_in_trafficking':roles_in_trafficking

        }
        
        if request.GET.get('step') is not None:
            context['step'] = request.GET.get('step')
        
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

        if 'c_id' in request.session:
            context['c_id'] = request.session['c_id']
            context['victim'] = SomVictimProfile.objects.filter(case_id=request.session['c_id'])
            context['arrest'] = SomArrestInvestigation.objects.filter(case_id = request.session['c_id'])
            context['suspects'] = SomSuspectedTrafficker.objects.filter(case_id = request.session['c_id'])
            context['suspect_count'] = len(context['suspects']) if len(context['suspects'])>0 else 1
            context['suspect_add'] = 0

        context['interviewer']=interviewer
        request.session['agg'] = "1"
    

    return render(request,"som_investigation_form.html",context)

@login_required
def save_victim(request):
    if 'consent_given' not in request.session:
        messages.error(request,"Victim consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    if request.method == "POST":
        if request.POST.get('victim_id') is not None:
            # TODO: Add checks on who posted and who can edit
            # edit capability shelved for now
            #victim = VictimProfile.objects.filter(id=request.POST['victim_id']).first()
            pass
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        victim = SomVictimProfile()
        victim.case_id = request.session['c_id']
        victim.citizenship_id = request.POST['citizenship']
        victim.countryOfBirth_id = request.POST['country_of_birth']
        victim.gender_id = request.POST['gender']
        victim.race_id = request.POST['race']
        victim.last_place_of_residence_id = request.POST['last_place_of_residence']
        victim.initials = request.POST['initials']
        victim.age = request.POST['age']
        victim.interview_country_id = request.POST['interview_country']
        victim.interview_location = request.POST['interviewer_location']
        victim.interview_date = request.POST['interview_date']
        victim.additional_remarks = request.POST['additional_remarks']
        victim.approval_id = 1
        victim.consent_share_gov_patner = 1
        victim.consent_limited_disclosure = 1
        victim.consent_research = 1
        victim.consent_abstain_answer = 1
        victim.save()
        if interviewer.data_entry_purpose_id == 1:
            victim.victim_identifier = "SOM-"+victim.interview_country.two_code+"-TP-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 2:
            victim.victim_identifier = "SOM-"+victim.interview_country.two_code+"-IV-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 3:
            victim.victim_identifier = "SOM-"+victim.interview_country.two_code+"-PR-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 4:
            victim.victim_identifier = "SOM-"+victim.interview_country.two_code+"-AS-"+str(victim.id)
        victim.save()

        if request.POST.getlist('languages[]'):
            victim.languages.set(request.POST.getlist('languages[]'))
        
        if request.POST.getlist('idtypes[]'):
            victim.identification_type.set(request.POST.getlist('idtypes[]'))

        
        interviewer.som_victims.add(victim)
        request.session['agg'] = 1
        messages.success(request,"Victim successfully saved.")

    if request.GET.get('language') is not None:
        formulate_get="?step=3&language="+request.GET.get('language')
    else:
        formulate_get="?step=3"
    
    if interviewer.data_entry_purpose_id == 1:
        url = '/'+request.LANGUAGE_CODE+'/som_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 2:
        url = '/'+request.LANGUAGE_CODE+'/som_investigation_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 3:
        url = '/'+request.LANGUAGE_CODE+'/som_prosecution_form'+formulate_get
    else:
        url = '/'+request.LANGUAGE_CODE+'/som_assistance_form'+formulate_get
    return redirect(url)



@login_required
def save_multi_victim(request):
    if 'consent_given' not in request.session:
        messages.error(request,"Victim consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    if request.method == "POST":
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        victim = SomMultiVictimProfile()
        victim.case_id = request.session['c_id']
        victim.victim_count = request.POST['numberOfVictims']
        victim.interview_country_id = request.POST['interviewCountry']
        victim.interview_location = request.POST['interviewerLocation']
        victim.interview_date = request.POST['interviewDate']
        victim.additional_remarks = request.POST['additionalRemarks']
        victim.approval_id = 1
        victim.consent_share_gov_patner = 1
        victim.consent_limited_disclosure = 1
        victim.consent_research = 1
        victim.consent_abstain_answer = 1
        victim.save()

        if interviewer.data_entry_purpose_id == 1:
            victim.victim_identifier = "SOM-"+victim.interview_country.two_code+"-TP-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 2:
            victim.victim_identifier = "SOM-"+victim.interview_country.two_code+"-IV-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 3:
            victim.victim_identifier = "SOM-"+victim.interview_country.two_code+"-PR-"+str(victim.id)
        if interviewer.data_entry_purpose_id == 4:
            victim.victim_identifier = "SOM-"+victim.interview_country.two_code+"-AS-"+str(victim.id)
        victim.save()

        if request.POST.get('countries'):
            victim.countries_of_origin.set(request.POST.getlist('countries'))
        
        for key,value in request.POST.get('answers',{}).items():
            answerobj = SomVictimAnswers()
            answerobj.victim_id = victim.id
            answerobj.question_id = int(key)
            answerobj.answer = value
            answerobj.save()

        
        interviewer.som_multi_victims.add(victim)
        request.session['agg'] = 2
        messages.success(request,"Victim successfully saved.")

    if request.GET.get('language') is not None:
        formulate_get="?step=3&language="+request.GET.get('language')
    else:
        formulate_get="?step=3"
    
    if interviewer.data_entry_purpose_id == 1:
        url = '/'+request.LANGUAGE_CODE+'/som_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 2:
        url = '/'+request.LANGUAGE_CODE+'/som_investigation_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 3:
        url = '/'+request.LANGUAGE_CODE+'/som_prosecution_form'+formulate_get
    else:
        url = '/'+request.LANGUAGE_CODE+'/som_assistance_form'+formulate_get
    return redirect(url)

@login_required
def save_arrest(request):
    if 'consent_given' not in request.session:
        messages.error(request,"Victim consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    #TODO: add check for who can post about a victim
    #TODO: combine victims
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    if request.method == "POST":
        if request.POST.get("arrest_id"):
            arrest = SomArrestInvestigation.objects.filter(id = int(request.POST.get("arrest_id"))).first()
        else:
            arrest = SomArrestInvestigation()
        arrest.case_id = request.session['c_id']
        arrest.org_crime=request.POST['org_crime']
        arrest.suspects_arrested = request.POST['suspects_arrested']
        arrest.why_no_arrest=request.POST['why_no_arrest']
        arrest.investigation_done=request.POST['investigation_done']
        arrest.why_no_investigation=request.POST['why_no_investigation']
        arrest.investigation_status_id=request.POST['investigation_status']
        arrest.why_pending=request.POST['why_pending']
        arrest.withdrawn_closed_reason=request.POST['withdrawn_closed_reason']
        arrest.interviewer_id=interviewer.id
        arrest.approval_id=1
        arrest.save()
        print(request.POST)

        if request.POST.getlist('how_traffickers_org[]'):
            arrest.how_traffickers_org.set(request.POST.getlist('how_traffickers_org[]'))
        messages.success(request,"Arrest/investigation data successfully saved.")

        
    if request.GET.get('language') is not None:
        formulate_get="?step=4&language="+request.GET.get('language')
    else:
        formulate_get="?step=4"
    
    

    return redirect('/'+request.LANGUAGE_CODE+'/som_investigation_form'+formulate_get)

@login_required
def save_suspect(request):
    if 'consent_given' not in request.session:
        messages.error(request,"Victim consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    today = date.today()
    born = datetime.strptime(request.POST['dob'], '%Y-%m-%d')
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    if request.method == "POST":
        if request.POST.get("suspect_id"):
            suspect = SomSuspectedTrafficker.objects.filter(id = int(request.POST.get("suspect_id"))).first()
        else:
            suspect = SomSuspectedTrafficker()
        suspect.case_id = request.session['c_id']
        suspect.first_name = request.POST['first_name'] if request.POST.get('first_name') is not None and not request.POST.get('first_name') == '' else None
        suspect.last_name = request.POST['last_name'] if request.POST.get('last_name') is not None and not request.POST.get('last_name') == '' else None
        suspect.dob = request.POST['dob'] if request.POST.get('dob') is not None and not request.POST.get('dob') == '' else None
        suspect.gender_id = request.POST['gender'] if request.POST.get('gender') is not None and not request.POST.get('gender') == '' else None
        suspect.race_id = request.POST['race'] if request.POST.get('race') is not None and not request.POST.get('race') == '' else None
        suspect.age = age
        suspect.country_of_birth_id = request.POST['country_of_birth'] if request.POST.get('country_of_birth') is not None and not request.POST.get('country_of_birth') == '' else None
        suspect.citizenship_id = request.POST['citizenship'] if request.POST.get('citizenship') is not None and not request.POST.get('citizenship') == '' else None
        suspect.nationality_id = request.POST['nationality'] if request.POST.get('nationality') is not None and not request.POST.get('nationality') == '' else None
        suspect.id_number = request.POST['id_number'] if request.POST.get('id_number') is not None and not request.POST.get('id_number') == '' else None
        suspect.last_residence = request.POST['last_residence'] if request.POST.get('last_residence') is not None and not request.POST.get('last_residence') == '' else None
        suspect.address = request.POST['address'] if request.POST.get('address') is not None and not request.POST.get('address') == '' else None
        suspect.date_of_arrest = request.POST['date_of_arrest'] if request.POST.get('date_of_arrest') is not None and not request.POST.get('date_of_arrest') == '' else None
        suspect.traffick_from_country_id = request.POST['traffick_from_country'] if request.POST.get('traffick_from_country') is not None and not request.POST.get('traffick_from_country') == '' else None
        suspect.traffick_from_place = request.POST['traffick_from_place'] if request.POST.get('traffick_from_place') is not None and not request.POST.get('traffick_from_place') == '' else None
        suspect.traffick_to_country_id = request.POST['traffick_to_country'] if request.POST.get('traffick_to_country') is not None and not request.POST.get('traffick_to_country') == '' else None
        suspect.traffick_to_place = request.POST['traffick_to_place'] if request.POST.get('traffick_to_place') is not None and not request.POST.get('traffick_to_place') == '' else None
        suspect.interviewer_id=interviewer.id
        suspect.approval_id=1
        suspect.id_type_id = request.POST['idtypes']
        suspect.save()

        if request.POST.getlist('languages[]'):
            suspect.languages.set(request.POST.getlist('languages[]'))

        
        if request.POST.getlist('role_in_trafficking[]'):
            suspect.role_in_trafficking.add(request.POST.getlist('role_in_trafficking[]'))

    if request.GET.get('language') is not None:
        formulate_get="?step=3&language="+request.GET.get('language')
    else:
        formulate_get="?step=3"
    
    if interviewer.data_entry_purpose_id == 1:
        url = '/'+request.LANGUAGE_CODE+'/som_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 2:
        url = '/'+request.LANGUAGE_CODE+'/som_investigation_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 3:
        url = '/'+request.LANGUAGE_CODE+'/som_prosecution_form?step=3'
    else:
        url = '/'+request.LANGUAGE_CODE+'/som_assistance_form?step=2'
    
    return redirect(url)

@login_required
def save_case(request):
    if 'consent_given' not in request.session:
        messages.error(request,"Consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    if request.method == "POST":
        
        case = SomCase()
        case.date_of_arrest = request.POST['date_of_arrest']
        case.traffick_from_country_id = request.POST['traffick_from_country']
        case.traffick_from_place = request.POST['traffick_from_place']
        case.traffick_to_country_id = request.POST['traffick_to_country']
        case.traffick_to_place = request.POST['traffick_to_place']
        case.approval_id=1
        case.save()

        interviewer.som_cases.add(case)

        request.session['c_id'] = case.id
       
    if request.GET.get('language') is not None:
        formulate_get="?step=2&language="+request.GET.get('language')
    else:
        formulate_get="?step=2"
    
    if interviewer.data_entry_purpose_id == 1:
        url = '/'+request.LANGUAGE_CODE+'/som_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 2:
        url = '/'+request.LANGUAGE_CODE+'/som_investigation_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 3:
        url = '/'+request.LANGUAGE_CODE+'/som_prosecution_form?step=2'
    else:
        url = '/'+request.LANGUAGE_CODE+'/som_assistance_form?step=2'
    
    return redirect(url)


@login_required
def prosecution_form(request):
    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    
    

    if(request.user.is_authenticated):
        countries = Country.objects.all().order_by('name').values()
        purposes = DataEntryPurpose.objects.all()
        languages = Language.objects.all()
        genders = Gender.objects.all()
        races = Race.objects.all()
        idtypes = IdType.objects.all()
        roles_in_trafficking = RoleInTrafficking.objects.all()

        
        context = {
            "countries":countries,
            "purposes":purposes,
            "languages":languages,
            "genders":genders,
            "races":races,
            "idtypes":idtypes,
            'roles_in_trafficking':roles_in_trafficking
           
        }
        if request.GET.get('step') is not None:
            context['step'] = request.GET.get('step')
        
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
             
        if 'c_id' in request.session:
            context['c_id'] = request.session['c_id']
            context['victim'] = SomVictimProfile.objects.filter(case_id=request.session['c_id']).first()
            context['suspects'] = SomSuspectedTrafficker.objects.filter(case_id = request.session['c_id'])
            context['prosecutions'] = SomProsecution.objects.filter(case_id = request.session['c_id'])
            context['case_statuses'] = CaseStatus.objects.all()
            context['trial_courts'] = TrialCourt.objects.all()
            context['verdicts'] = Verdict.objects.all()
            context['guilty_reasons'] = GuiltyReason.objects.all()
            context['prosecution_outcomes'] = ProsecutionOutcome.objects.all()
            context['aquital_reasons'] = AquitalReason.objects.all()
            context['sanction_penalties'] = SanctionPenalty.objects.all()



        context['interviewer']=interviewer
        request.session['agg'] = "1"
    

    return render(request,"som_prosecution_form.html",context)


@login_required
def save_prosecution(request):
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    if 'consent_given' not in request.session:
        messages.error(request,"Victim consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    if request.method == "POST":
        prosecution = SomProsecution()
        prosecution.case_id = request.session['c_id']
        prosecution.interviewer_id = interviewer.id
        prosecution.trafficker_id = request.POST['trafficker_id']
        prosecution.status_of_case_id = request.POST['status_of_case_id']
        prosecution.trial_court_id = request.POST['trial_court_id']
        prosecution.trial_court_country_id = request.POST['trial_court_country_id']
        prosecution.court_case_no = request.POST['court_case_no']
        prosecution.verdict_id = request.POST['verdict_id']
        prosecution.guilty_verdict_reason_id = request.POST['guilty_verdict_reason_id']
        prosecution.prosecution_outcome_id = request.POST['prosecution_outcome_id']
        prosecution.aquital_reason_id = request.POST['aquital_reason_id']
        prosecution.review_appeal_outcome = request.POST['review_appeal_outcome']
        prosecution.sanction_penalty_id = request.POST['sanction_penalty_id']
        prosecution.years_imposed = request.POST['years_imposed'] if not request.POST['years_imposed'] == "" else None
        prosecution.approval_id=1
        prosecution.save()

        messages.success(request,'Prosecution details saved')
        
    return redirect('/'+request.LANGUAGE_CODE+'/som_cases')

@login_required
def som_form(request):
    if(request.user.is_authenticated):
        countries = Country.objects.all().order_by('name').values()
        purposes = DataEntryPurpose.objects.all()
        languages = Language.objects.all()
        genders = Gender.objects.all()
        races = Race.objects.all()
        idtypes = IdType.objects.all()
        
        context = {
            "countries":countries,
            "purposes":purposes,
            "languages":languages,
            "genders":genders,
            "races":races,
            "idtypes":idtypes,
           
        }
        if request.GET.get('step') is not None:
            context['step'] = request.GET.get('step')
        
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

        if 'c_id' in request.session:
            context['c_id'] = request.session['c_id']
            context['victim'] = SomVictimProfile.objects.filter(case_id=request.session['c_id'])
            context['transit'] = SomTransitRouteDestination.objects.filter(case_id = request.session['c_id'])
            context['exploitation_ages'] = ExploitationAge.objects.all()
            context['freed_methods'] = FreedMethod.objects.all()
            context['criminal_activity_types'] = CriminalActivityType.objects.all()
            context['forced_labour_industries'] = ForcedLabourIndustry.objects.all()
            context['bride_prices'] = BridePrice.objects.all()
            context['bride_price_recipients'] = BridePriceRecipient.objects.all()
            context['child_marriage_reasons'] = ChildMarriageReason.objects.all()
            context['affirm_options'] = AffirmOption.objects.all()
            context['marriage_violence_types'] = MarriageViolenceType.objects.all()
            context['military_activities'] = MilitaryActivity.objects.all()
            context['military_types'] = MilitaryType.objects.all()
            context['body_parts'] = BodyPart.objects.all()
            context['operation_locations'] = OperationLocation.objects.all()
            context['organ_paid_to'] = OrganPaidTo.objects.all()
            context['recruitment_types'] = RecruitmentType.objects.all()
            context['recruiter_relationships'] = RecruiterRelationship.objects.all()
            context['trafficking_means'] = TraffickingMean.objects.all()
            context['transport_means'] = TransportMean.objects.all()



        context['interviewer']=interviewer
        request.session['agg'] = "1"
    

    return render(request,"som_form.html",context)


@login_required
def save_transit(request):
    if 'consent_given' not in request.session:
        messages.error(request,"Victim consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    
    if request.method == "POST":
        transit = SomTransitRouteDestination()
        transit.case_id = request.session['c_id']
        transit.country_of_origin_id = int(request.POST['country_of_origin_id']) if request.POST['country_of_origin_id'].isdigit() else None
        transit.country_of_dest_id = int(request.POST['country_of_dest_id']) if request.POST['country_of_dest_id'].isdigit() else None
        transit.country_of_interception_id = int(request.POST['country_of_interception_id'])
        transit.remarks = request.POST['remarks']
        transit.interviewer_id = interviewer.id
        transit.approval_id = 1
        transit.save()

        if request.POST.get('means_of_transport[]') is not None:
            transit.transport_means.set(request.POST.getlist('means_of_transport[]'))
        
        if request.POST.get('countries_of_transit[]') is not None:
            transit.countries_of_transit.set(request.POST.getlist('countries_of_transit[]'))


        messages.success(request,'Transit route successfully saved')
        
        formulate_get="?step=3"
        return redirect('/'+request.LANGUAGE_CODE+'/som_cases')

@login_required
def assistance_form(request):

    if(request.user.is_authenticated):
        countries = Country.objects.all().order_by('name').values()
        purposes = DataEntryPurpose.objects.all()
        languages = Language.objects.all()
        genders = Gender.objects.all()
        races = Race.objects.all()
        idtypes = IdType.objects.all()
        providers = Provider.objects.all()
        community_assistance_types = CommunityAssistanceType.objects.all()
        education_levels = EducationLevel.objects.all()
        im_emmigration_statuses = ImEmmigrationStatus.objects.all()
        data_suppliers = DataSupplier.objects.all()
        family_structures = FamilyStructure.objects.all()
        living_withs = LivingWith.objects.all()
        occupations = Occupation.objects.all()
        income_project_types = IncomeProjectType.objects.all()

        
        context = {
            "countries":countries,
            "purposes":purposes,
            "languages":languages,
            "genders":genders,
            "races":races,
            "idtypes":idtypes,
            "providers":providers,
            "community_assistance_types":community_assistance_types,
            "education_levels" : education_levels,
            "im_emmigration_statuses" : im_emmigration_statuses,
            "data_suppliers" : data_suppliers,
            "family_structures" : family_structures,
            "living_withs" : living_withs,
            "occupations" : occupations,
            "income_project_types" : income_project_types,
           
        }
        if request.GET.get('step') is not None:
            context['step'] = request.GET.get('step')
        
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

        if 'c_id' in request.GET:
            case = SomCase.objects.filter(id = request.GET.get('c_id')).first()
            victim = SomVictimProfile.objects.filter(case_id = case.id)
            
            if case is None:
                messages.error(request,'Case does not exist. Please create a new case.')
            else:
                if interviewer.som_cases.filter(id = case.id).first() is not None:
                    request.session['c_id'] = case.id
                    request.session['consent_given'] = 1
                else:
                    permission = VictimPermissions.objects.filter(interviewer_id = interviewer.id, victim_id = case.id).first()
                    if permission is None:
                        if request.user.is_staff:
                            request.session['c_id'] = case.id
                            request.session['consent_given'] = 1
                        # TODO: check if permision is granted
                        # TODO: remove autopermission below
                        else:
                            messages.error(request,"You do not have access to this record. Please create a request.")
          
        if 'c_id' in request.session:
            context['c_id'] = request.session['c_id']
            context['case'] = SomCase.objects.filter(id=request.session['c_id']).first()
            context['victim'] = SomVictimProfile.objects.filter(case_id=request.session['c_id'])
            

        context['interviewer']=interviewer
        request.session['agg'] = "1"
    

    return render(request,"som_assistance_form.html",context)

@login_required
def save_assistance_types(request):
    if 'consent_given' not in request.session:
        messages.error(request,"Victim consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    
    if request.method == "POST":
        assistance = SomAssistance()
        assistance.case_id = request.session['c_id']
        assistance.interviewer_id = interviewer.id
        
        assistance.social_assistance = request.POST.get('social_assistance')
        assistance.med_rehab = request.POST.get('med_rehab')
        assistance.housing_allowance = request.POST.get('housing_allowance')
        assistance.halfway_house = request.POST.get('halfway_house')
        assistance.shelter = request.POST.get('shelter')
        assistance.vocational_training = request.POST.get('vocational_training')
        assistance.micro_ent_income = request.POST.get('micro_ent_income')
        assistance.legal_assistance = request.POST.get('legal_assistance')
        assistance.medical_assistance = request.POST.get('medical_assistance')
        assistance.financial_assistance = request.POST.get('financial_assistance')
        assistance.education_assistance = request.POST.get('education_assistance')
        assistance.im_emmigration_assistance = request.POST.get('im_emmigration_assistance')
        assistance.other_community_assistance = request.POST.get('other_community_assistance')

        # assistance.micro_ent_income_project_id = request.POST.get('micro_ent_income_project')
        # assistance.education_assistance_level_id = request.POST.get('education_assistance_level')
        # assistance.im_emmigration_assistance_status_id = request.POST.get('im_emmigration_assistance_status')
        # assistance.other_community_assistance_type_id = request.POST.get('other_community_assistance_type')
        assistance.approval_id = 1
        assistance.save()

        if request.POST.get('social_assistance_provider'):
            assistance.social_assistance_provider.set(request.POST.getlist('social_assistance_provider'))

        if request.POST.get('med_rehab_provider'):
            assistance.med_rehab_provider.set(request.POST.getlist('med_rehab_provider'))

        if request.POST.get('housing_allowance_provider'):
            assistance.housing_allowance_provider.set(request.POST.getlist('housing_allowance_provider'))

        if request.POST.get('shelter_provider'):
            assistance.shelter_provider.set(request.POST.getlist('shelter_provider'))

        if request.POST.get('vocational_training_provider'):
            assistance.vocational_training_provider.set(request.POST.getlist('vocational_training_provider'))

        if request.POST.get('micro_ent_income_provider'):
            assistance.micro_ent_income_provider.set(request.POST.getlist('micro_ent_income_provider'))

        if request.POST.get('legal_assistance_provider'):
            assistance.legal_assistance_provider.set(request.POST.getlist('legal_assistance_provider'))

        if request.POST.get('medical_assistance_provider'):
            assistance.medical_assistance_provider.set(request.POST.getlist('medical_assistance_provider'))

        if request.POST.get('financial_assistance_provider'):
            assistance.financial_assistance_provider.set(request.POST.getlist('financial_assistance_provider'))

        if request.POST.get('education_assistance_provider'):
            assistance.education_assistance_provider.set(request.POST.getlist('education_assistance_provider'))

        if request.POST.get('im_emmigration_assistance_provider'):
            assistance.im_emmigration_assistance_provider.set(request.POST.getlist('im_emmigration_assistance_provider'))

        if request.POST.get('other_community_assistance_provider'):
            assistance.other_community_assistance_provider.set(request.POST.getlist('other_community_assistance_provider'))

        messages.success(request,'Assistance data saved successfully')

        formulate_get="?step=4"
        return redirect('/'+request.LANGUAGE_CODE+'/som_assistance_form'+formulate_get)

@login_required       
def save_socio_economic(request):
    if 'consent_given' not in request.session:
        messages.error(request,"Victim consent not given")
        return redirect('/'+request.LANGUAGE_CODE+"/som_cases")
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    
    if request.method == "POST":
        socio = SomSocioEconomic()
        socio.case_id = request.session['c_id']
        socio.victim_id = request.POST.get("v_id")
        socio.family_structure_id = request.POST.get('family_structure') if request.POST.get('family_structure') is not None and not request.POST.get('family_structure') == None else None
        socio.living_with_id = request.POST.get('living_with') if request.POST.get('living_with') is not None and not request.POST.get('living_with') == None else None
        socio.violence_prior = request.POST.get('violence_prior') if request.POST.get('violence_prior') is not None and not request.POST.get('violence_prior') == None else None
        socio.violence_type = request.POST.get('violence_type') if request.POST.get('violence_type') is not None and not request.POST.get('violence_type') == None else None
        socio.education_level_id = request.POST.get('education_level') if request.POST.get('education_level') is not None and not request.POST.get('education_level') == None else None
        socio.interviewer_id = interviewer.id
        socio.approval_id = 1
        socio.save()

        if request.POST.get('last_occupation'):
            socio.last_occupation.set(request.POST.getlist('last_occupation'))

        messages.success(request,"Socio-economic situation saved")

        formulate_get="?step=4"
        return redirect('/'+request.LANGUAGE_CODE+'/som_cases')



@login_required
def process_approval(request):
    if request.user.is_staff:
        if request.POST.get("form_model") == "destination":
            oid = request.POST.get("id")
            approval_id = request.POST.get("approval")
            obj = SomTransitRouteDestination.objects.filter(id=oid).first()
            obj.approval_id = approval_id
            obj.save()
            case_id = obj.case_id
            messages.success(request,"Approval successful")

        elif request.POST.get("form_model") == "prosecution":
            oid = request.POST.get("id")
            approval_id = request.POST.get("approval")
            obj = SomProsecution.objects.filter(id=oid).first()
            obj.approval_id = approval_id
            obj.save()
            case_id = obj.case_id
            messages.success(request,"Approval successful")

        elif request.POST.get("form_model") == "suspect":
            oid = request.POST.get("id")
            approval_id = request.POST.get("approval")
            obj = SomSuspectedTrafficker.objects.filter(id=oid).first()
            obj.approval_id = approval_id
            obj.save()
            case_id = obj.case_id
            messages.success(request,"Approval successful")

        elif request.POST.get("form_model") == "arrest":
            oid = request.POST.get("id")
            approval_id = request.POST.get("approval")
            obj = SomArrestInvestigation.objects.filter(id=oid).first()
            obj.approval_id = approval_id
            obj.save()
            case_id = obj.case_id
            messages.success(request,"Approval successful")

        elif request.POST.get("form_model") == "victim":
            oid = request.POST.get("id")
            approval_id = request.POST.get("approval")
            obj = SomVictimProfile.objects.filter(id=oid).first()
            obj.approval_id = approval_id
            obj.save()
            case_id = obj.case_id
            messages.success(request,"Approval successful")

        elif request.POST.get("form_model") == "socio":
            pass
        elif request.POST.get("form_model") == "aggregate":
            pass
        
    return redirect('/'+request.LANGUAGE_CODE+'/som_case/'+str(case_id))

@login_required
def cases(request):
    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    if request.GET.get('page') is not None:
        page=request.GET.get('page')
    else:
        page=1
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    if request.user.is_staff:
        if request.GET.get('pending') is None:
            cases = SomCase.objects.filter(interviewer__id = interviewer.id).order_by('id').annotate(Count('som_assistance', distinct=True),Count('som_investigations', distinct=True),Count('som_prosecutions', distinct=True),Count('som_socio_economic', distinct=True),Count('som_traffickers', distinct=True),Count('som_transit', distinct=True))|SomCase.objects.filter(interview_country_id = interviewer.country_id).order_by('id').annotate(Count('som_assistance', distinct=True),Count('som_investigations', distinct=True),Count('som_prosecutions', distinct=True),Count('som_socio_economic', distinct=True),Count('som_traffickers', distinct=True),Count('som_transit', distinct=True))
        else:
            cases = SomCase.objects.filter(interview_country_id = interviewer.country_id,approval_id = 1).order_by('id').annotate(Count('som_assistance', distinct=True),Count('som_investigations', distinct=True),Count('som_prosecutions', distinct=True),Count('som_socio_economic', distinct=True),Count('som_traffickers', distinct=True),Count('som_transit', distinct=True))
    else:
        cases = interviewer.som_cases.order_by('id').annotate(Count('som_assistance', distinct=True),Count('som_investigations', distinct=True),Count('som_prosecutions', distinct=True),Count('som_socio_economic', distinct=True),Count('som_traffickers', distinct=True),Count('som_transit', distinct=True))

    
    paginator = Paginator(cases, per_page=12)

    page_object = paginator.get_page(page)
    if request.session.get('c_id') != None:
        del request.session['c_id']
    if request.session.get('consent_given') is not None:
        del request.session['consent_given']
    context = {
        "cases":page_object.object_list,
        "page": {

            "current": page_object.number,

            "has_next": page_object.has_next(),

            "has_previous": page_object.has_previous(),

        },
        "interviewer":interviewer
    }
    return render(request,"som-cases.html",context)

@staff_member_required
def search_view(request):
    victim_form = VictimSearchForm(request.GET or None)
    interviewer_form = InterviewerSearchForm(request.GET or None)
    trafficker_form = TraffickerSearchForm(request.GET or None)

    results = []
    current_search = 1
    if victim_form.is_valid() and 'victim_search' in request.GET:
        query = Q()
        for field, value in victim_form.cleaned_data.items():
            if value:
                query |= Q(**{field: value})
        results = SomVictimProfile.objects.filter(query)
        current_search = 1

    elif interviewer_form.is_valid() and 'interviewer_search' in request.GET:
        query = Q()
        for field, value in interviewer_form.cleaned_data.items():
            if value:
                query |= Q(**{field: value})
        results = Interviewer.objects.filter(query)
        current_search = 2
    elif trafficker_form.is_valid() and 'trafficker_search' in request.GET:
        query = Q()
        for field, value in trafficker_form.cleaned_data.items():
            if value:
                query |= Q(**{field: value})
        results = SomSuspectedTrafficker.objects.filter(query)
        current_search = 3

    page = request.GET.get('page', 1)
    paginator = Paginator(results, 10)  # Show 10 results per page
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        'victim_form': victim_form,
        'interviewer_form': interviewer_form,
        'trafficker_form': trafficker_form,
        'results': results,
        'current_search':current_search
    }
    return render(request, 'search_results.html', context)

def suspect_detail(request, suspect_id):
    # Fetch the suspect object based on the provided ID
    suspect = get_object_or_404(SomSuspectedTrafficker, pk=suspect_id)

    return render(request, 'suspect_detail.html', {'suspect': suspect})

def interviewer_detail(request, interviewer_id):
    interviewer = get_object_or_404(Interviewer, pk=interviewer_id)
    return render(request, 'interviewer_detail.html', {'interviewer': interviewer})

@login_required
def process_consent(request):
    if request.POST.get('consent_share_gov_patner') == '1' and request.POST.get('consent_limited_disclosure') == '1' and request.POST.get('consent_research') == '1' and request.POST.get('consent_abstain_answer') == '1':
        request.session['consent_given'] = 1
        messages.success(request,"Consent granted. You can proceed.")
        return redirect(request.POST.get('next'))
    else:
        messages.error(request,"Victim denied consent. You cannot add their details.")
        return redirect('/'+request.LANGUAGE_CODE+'/som_cases')

@login_required
def victim_view(request,id):
    if(request.user.is_authenticated):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    if request.user.is_staff:
        case = SomCase.objects.filter(id=id).first()
    else:
        case = interviewer.som_cases.filter(id=id).first()

    context = {
        "case":case,
        "victim":SomVictimProfile.objects.filter(case_id = id).first(),
        # "suspects":suspects
    }
    
    context['suspects'] = SomSuspectedTrafficker.objects.filter(case_id = id)
    context['arrest'] = SomArrestInvestigation.objects.filter(case_id = id).first()
    context['prosecutions'] = SomProsecution.objects.filter(case_id = id)
    context['destination'] = SomTransitRouteDestination.objects.filter(case_id = id).first()
    context['assistance'] = SomAssistance.objects.filter(case_id = id).first()
    context['socio_economic'] = SomSocioEconomic.objects.filter(case_id = id).first()

    return render(request,"som-victim-view.html",context)


@login_required
def signout(request):
    logout(request)
    return redirect('/'+request.LANGUAGE_CODE+"/")

