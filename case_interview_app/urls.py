from django.urls import path

from . import views

urlpatterns = [
    path("", views.interviewer_registration, name="interviewer_registration"),
    path("investigation_form", views.investigation_form, name="investigation_form"),
    path("cases", views.cases, name="cases"),
    path("login", views.signin, name="signin"),
    path("logout", views.signout, name="signout"),
    path("lang/<language>",views.change_language, name="lang"),
    
]