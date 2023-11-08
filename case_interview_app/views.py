from django.shortcuts import render
from .models import *

# Create your views here.
def interviewer_registration(request):
    countries = Country.objects.all()
    purposes = DataEntryPurpose.objects.all()
    return render(request,"registration_form.html")
