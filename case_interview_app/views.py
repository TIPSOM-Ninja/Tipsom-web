from django.shortcuts import render
from .models import *

# Create your views here.
def interviewer_registration(request):
    return render(request,"registration_form.html")
