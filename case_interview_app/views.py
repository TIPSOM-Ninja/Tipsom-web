from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def interviewer_registration(request):

    
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
            elif(request.user.is_authenticated and (request.POST['password']!=None)):
                user = request.user
                user.set_password(request.POST['password'])
                user.save()
                messages.success(request,"Interviewer data successfully modified.")
    context['interviewer']=interviewer

    return render(request,"registration_form.html",context)

def investigation_form(request):
    
    if(request.user.is_authenticated):
        countries = Country.objects.all()
        purposes = DataEntryPurpose.objects.all()
        context = {
            "countries":countries,
            "purposes":purposes
        }
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
        context['interviewer']=interviewer
    else:
        return redirect("/login")

    return render(request,"investigation_form.html",context)

def signin(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request,"Wrong credentials.")
    return render(request,"login.html")

def signout(request):
    logout(request)
    return redirect("/login")

