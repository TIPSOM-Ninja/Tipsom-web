from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("interviewer_registration", views.interviewer_registration, name="interviewer_registration"),
    path("investigation_form", views.investigation_form, name="investigation_form"),
    path("prosecution_form", views.prosecution_form, name="prosecution_form"),
    path("tip_form", views.tip_form, name="tip_form"),

    path("cases", views.cases, name="cases"),
    path("login", views.signin, name="signin"),
    path("logout", views.signout, name="signout"),
    path("lang/<language>",views.change_language, name="lang"),
    path("save_victim", views.save_victim, name="save_victim"),
    path("save_arrest", views.save_arrest, name="save_arrest"),
    path("save_suspect", views.save_suspect, name="save_suspect"),
    path("save_prosecution", views.save_prosecution, name="save_prosecution"),
    path("save_exploitation", views.save_exploitation, name="save_exploitation"),

    path("victim/<id>", views.victim_view, name="victim_view"),
    

    


    
]