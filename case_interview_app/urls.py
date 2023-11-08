from django.urls import path

from . import views

urlpatterns = [
    path("", views.interviewer_registration, name="interviewer_registration"),
    
]