from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import activate, get_language_info
from datetime import date, datetime

def index(request):
    countries = Country.objects.all().order_by('name').values()
    context = {
        "countries":countries,
     
    }
    return render(request,"index.html",context)
def change_language(request,language):
    activate(language)
    return redirect(request.META.get('HTTP_REFERER'))

# Create your views here.
def interviewer_registration(request):

    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    countries = Country.objects.all()
    purposes = DataEntryPurpose.objects.all()

    context = {
        "countries":countries,
        "purposes":purposes
    }
    if(request.user.is_authenticated):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    else:
        interviewer=None
    if request.method == "POST":
        
        if (not request.user.is_authenticated) and (Interviewer.objects.filter(email_address = request.POST['email_address']).first()!=None):
            messages.error(request,"Please login first to complete the action.")
        else:
            if(interviewer == None):
                interviewer = Interviewer()
            interviewer.first_name = request.POST['first_name']
            interviewer.last_name = request.POST['last_name']
            interviewer.position = request.POST['position']
            interviewer.organization = request.POST['organization']
            interviewer.address = request.POST['address']
            interviewer.email_address = request.POST['email_address'] if not request.user.is_authenticated else request.user.email
            interviewer.country_id = request.POST['country']
            interviewer.data_entry_purpose_id = request.POST['purpose']
            interviewer.save()
            if not request.user.is_authenticated:
                user = User.objects.create_user(request.POST['email_address'],request.POST['email_address'],request.POST['password'])
                user.first_name = request.POST['first_name']
                user.last_name =  request.POST['last_name']
                user.groups.add(1)
                user.save()
                login(request,user)
                messages.success(request,"Welcome "+interviewer.first_name+". Interviewer successfully created.")
                if interviewer.data_entry_purpose_id==1:
                    return redirect('/cases')
                else:
                    return redirect('/cases')
            elif request.user.is_authenticated:
                if (request.POST['password'] is not None and not request.POST['password'] == ""):
                    user = request.user
                    user.set_password(request.POST['password'])
                    user.save()
                    login(request,user)
                    messages.success(request,"Credentials successfully modified.")
                messages.success(request,"Interviewer data successfully modified.")
            interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

    context['interviewer']=interviewer

    return render(request,"registration_form.html",context)
def victim_view(request,id):
    if(request.user.is_authenticated):
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    victim = interviewer.victims.filter(id=id ).first()
    context = {
        "victim":victim,
        # "suspects":suspects
    }
    context['suspects'] = SuspectedTrafficker.objects.filter(victim_id = id,interviewer_id=interviewer.id)
    context['arrest'] = ArrestInvestigation.objects.filter(victim_id = id,interviewer_id=interviewer.id).first()
    context['prosecutions'] = Prosecution.objects.filter(victim_id = id)
    return render(request,"victim-view.html",context)


def investigation_form(request):
    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    

    if(request.user.is_authenticated):
        countries = Country.objects.all()
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
        if request.GET.get('step') and 'v_id' in request.session:
            context['v_id'] = request.session['v_id']
            context['victim'] = VictimProfile.objects.filter(id=request.session['v_id']).first()
            context['arrest'] = ArrestInvestigation.objects.filter(victim_id = request.session['v_id'],interviewer_id=interviewer.id).first()
            context['suspects'] = SuspectedTrafficker.objects.filter(victim_id = request.session['v_id'],interviewer_id=interviewer.id)
            context['suspect_count'] = len(context['suspects']) if len(context['suspects'])>0 else 1
            context['suspect_add'] = 0

        context['interviewer']=interviewer
    else:
        return redirect("/login")

    return render(request,"investigation_form.html",context)
def save_victim(request):
    
    if request.method == "POST":
        if request.POST.get('victim_id') is not None:
            # TODO: Add checks on who posted and who can edit
            # edit capability shelved for now
            #victim = VictimProfile.objects.filter(id=request.POST['victim_id']).first()
            pass
        
        victim = VictimProfile()
        victim.citizenship_id = request.POST['citizenship']
        victim.countryOfBirth_id = request.POST['country_of_birth']
        victim.gender_id = request.POST['gender']
        victim.race_id = request.POST['race']
        victim.place_of_birth = request.POST['place_of_birth']
        victim.last_place_of_residence_id = request.POST['last_place_of_residence']
        victim.identification_number = request.POST['id_number']
        victim.initials = request.POST['initials']
        victim.age = request.POST['age']
        victim.address = request.POST['address']
        victim.email_address = request.POST['email_address']
        victim.interview_location = request.POST['interviewer_location']
        victim.interview_date = request.POST['interview_date']
        victim.additional_remarks = request.POST['additional_remarks']
        victim.approval_id = 1
        victim.save()
        for lang in request.POST['languages[]']:
            victim.languages.add(Language.objects.filter(id= lang).first())
        
        for idt in request.POST['idtypes[]']:
            victim.identification_type.add(IdType.objects.filter(id = idt).first())

        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        interviewer.victims.add(victim)
        messages.success(request,"Victim successfully saved.")

        request.session['v_id'] = victim.id

    if request.GET.get('language') is not None:
        formulate_get="?step=2&language="+request.GET.get('language')
    else:
        formulate_get="?step=2"
    
    if interviewer.data_entry_purpose_id == 1:
        url = '/investigation_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 2:
        url = '/investigation_form'+formulate_get
    elif interviewer.data_entry_purpose_id == 3:
        url = '/prosecution_form'+formulate_get
    else:
        url = '/investigation_form'+formulate_get
    return redirect(url)
def save_arrest(request):
    #TODO: add check for who can post about a victim
    #TODO: combine victims
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    if request.method == "POST":
        arrest = ArrestInvestigation()
        arrest.victim_id =  request.POST['v_id']
        arrest.org_crime=request.POST['org_crime']
        arrest.suspect_arrested = request.POST['suspects_arrested']
        arrest.why_no_arrest=request.POST['why_no_arrest']
        arrest.victim_smuggled=request.POST['victim_smuggled']
        arrest.investigation_done=request.POST['investigation_done']
        arrest.why_no_investigation=request.POST['why_no_investigation']
        arrest.investigation_status_id=request.POST['investigation_status']
        arrest.why_pending=request.POST['why_pending']
        arrest.withdrawn_closed_reason=request.POST['withdrawn_closed_reason']
        arrest.interviewer=interviewer.id
        arrest.approval_id=1
        arrest.save()
        print(request.POST)
        for org in request.POST['how_traffickers_org[]']:
            arrest.how_traffickers_org.add(TraffickerOrg.objects.filter(id= org).first())
            messages.success(request,"Arrest/investigation data successfully saved.")
        
    if request.GET.get('language') is not None:
        formulate_get="?step=3&language="+request.GET.get('language')
    else:
        formulate_get="?step=3"
    
    

    return redirect('/investigation_form'+formulate_get)

def save_suspect(request):
    today = date.today()
    born = datetime.strptime(request.POST['dob'], '%Y-%m-%d')
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if request.method == "POST":
        suspect = SuspectedTrafficker()
        suspect.victim_id = request.session['v_id']
        suspect.first_name = request.POST['first_name']
        suspect.last_name = request.POST['last_name']
        suspect.dob = request.POST['dob']
        suspect.gender_id = request.POST['gender']
        suspect.race_id = request.POST['race']
        suspect.age = age
        suspect.country_of_birth_id = request.POST['country_of_birth']
        suspect.citizenship_id = request.POST['citizenship']
        suspect.nationality_id = request.POST['nationality']
        suspect.id_number = request.POST['id_number']
        suspect.last_residence = request.POST['last_residence']
        suspect.address = request.POST['address']
        suspect.date_of_arrest = request.POST['date_of_arrest']
        suspect.traffick_from_country_id = request.POST['traffick_from_country']
        suspect.traffick_from_place = request.POST['traffick_from_place']
        suspect.traffick_to_country_id = request.POST['traffick_to_country']
        suspect.traffick_to_place = request.POST['traffick_to_place']
        suspect.interviewer=Interviewer.objects.filter(email_address = request.user.email).first()
        suspect.approval_id=1
        suspect.id_type_id = request.POST['idtypes']
        suspect.save()

        for lang in request.POST['languages[]']:
            suspect.languages.add(Language.objects.filter(id= lang).first())

        
        for rl in request.POST['role_in_trafficking[]']:
            suspect.role_in_trafficking.add(RoleInTrafficking.objects.filter(id = rl).first())

    if request.GET.get('language') is not None:
        formulate_get="?step=3&language="+request.GET.get('language')
    else:
        formulate_get="?step=3"
    
    return redirect('/investigation_form'+formulate_get)

def prosecution_form(request):
    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    
    

    if(request.user.is_authenticated):
        countries = Country.objects.all()
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

        if request.GET.get("v_id") is not None:
            victim = VictimProfile.objects.filter(id = request.GET.get("v_id")).first()
            if victim is None:
                messages.error('Victim does not exist. Please create a new victim.')
            else:
                if interviewer.victims.filter(id = victim.id).first() is not None:
                    request.session['v_id'] = victim.id
                else:
                    permission = VictimPermissions.objects.filter(interviewer_id = interviewer.id, victim_id = victim.id).first()
                    if permission is None:
                        messages.error("You do not have access to this record. Please create a request.")
                    else:
                        # TODO: check if permision is granted
                        # TODO: remove autopermission below
                        request.session['v_id'] = victim.id
             
        if 'v_id' in request.session:
            context['v_id'] = request.session['v_id']
            context['victim'] = VictimProfile.objects.filter(id=request.session['v_id']).first()
            context['suspects'] = SuspectedTrafficker.objects.filter(victim_id = request.session['v_id'])
            context['prosecution'] = Prosecution.objects.filter(interviewer_id = interviewer.id, victim_id = request.session['v_id']).first()
            context['case_statuses'] = CaseStatus.objects.all()
            context['trial_courts'] = TrialCourt.objects.all()
            context['verdicts'] = Verdict.objects.all()
            context['guilty_reasons'] = GuiltyReason.objects.all()
            context['prosecution_outcomes'] = ProsecutionOutcome.objects.all()
            context['aquital_reasons'] = AquitalReason.objects.all()
            context['sanction_penalties'] = SanctionPenalty.objects.all()



        context['interviewer']=interviewer
    else:
        return redirect("/login")

    return render(request,"prosecution_form.html",context)



def save_prosecution(request):
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()

    if request.method == "POST":
        prosecution = Prosecution()
        prosecution.victim_id = request.session['v_id']
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
        prosecution.save()

        messages.success(request,'Prosecution details saved')
        
    return redirect('/cases')
    



def cases(request):
    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    victims = interviewer.victims.all()
    if request.session.get('v_id') != None:
        del request.session['v_id']
    context = {
        "victims":victims,
        "interviewer":interviewer
    }
    return render(request,"cases.html",context)
def signin(request):
    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("/cases")
        else:
            messages.error(request,"Wrong credentials.")
    return render(request,"login.html")

def signout(request):
    logout(request)
    return redirect("/login")

