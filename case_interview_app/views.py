from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import activate, get_language_info

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
            elif(request.user.is_authenticated and (request.POST['password']!=None)):
                user = request.user
                user.set_password(request.POST['password'])
                user.save()
                messages.success(request,"Interviewer data successfully modified.")
    context['interviewer']=interviewer

    return render(request,"registration_form.html",context)

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

        context = {
            "countries":countries,
            "purposes":purposes,
            "languages":languages,
            "genders":genders,
            "races":races,
            "idtypes":idtypes,
            'trafficker_orgs':trafficker_orgs,
            'investigation_statuses':investigation_statuses
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
    
    return redirect('/investigation_form'+formulate_get)
def save_arrest(request):
    #TODO: add check for who can post about a victim
    #TODO: combine victims
    if request.method == "POST":
        arrest = ArrestInvestigation()
        arrest.victim_id =  request.POST['v_id']
        arrest.org_crime=request.POST['org_crime']
        arrest.suspect_arrested = request.POST['suspect_arrested']
        arrest.why_no_arrest=request.POST['why_no_arrest']
        arrest.victim_smuggled=request.POST['victim_smuggled']
        arrest.investigation_done=request.POST['investigation_done']
        arrest.why_no_investigation=request.POST['why_no_investigation']
        arrest.investigation_status_id=request.POST['investigation_status']
        arrest.why_pending=request.POST['why_pending']
        arrest.withdrawn_closed_reason=request.POST['withdrawn_closed_reason']
        arrest.interviewer=Interviewer.objects.filter(email_address = request.user.email).first()
        arrest.approval_id=1
        arrest.save()
    for org in request.POST['how_traffickers_org[]']:
        arrest.how_traffickers_org.add(TraffickerOrg.objects.filter(id= org).first())
        messages.success(request,"Arrest/investigation data successfully saved.")
        
    if request.GET.get('language') is not None:
        formulate_get="?step=3&language="+request.GET.get('language')
    else:
        formulate_get="?step=3"
    
    return redirect('/investigation_form'+formulate_get)

    
def cases(request):
    if request.GET.get('language') is not None:
        activate(request.GET.get('language'))
    interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    victims = interviewer.victims.all()
    context = {
        "victims":victims
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

