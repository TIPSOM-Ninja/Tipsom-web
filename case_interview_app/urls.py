from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("interviewer_registration", views.interviewer_registration, name="interviewer_registration"),
    path("investigation_form", views.investigation_form, name="investigation_form"),
    path("prosecution_form", views.prosecution_form, name="prosecution_form"),
    path("tip_form", views.tip_form, name="tip_form"),
    path("assistance_form", views.assistance_form, name="assistance_form"),


    path("cases", views.cases, name="cases"),
    # path("login", views.signin, name="signin"),
    path("logout", views.signout, name="signout"),
    path("lang/<language>",views.change_language, name="lang"),
    path("save_victim", views.save_victim, name="save_victim"),
    path("save_arrest", views.save_arrest, name="save_arrest"),
    path("save_suspect", views.save_suspect, name="save_suspect"),
    path("save_prosecution", views.save_prosecution, name="save_prosecution"),
    path("save_exploitation", views.save_exploitation, name="save_exploitation"),
    path("save_transit", views.save_transit, name="save_transit"),
    path("save_assistance_types", views.save_assistance_types, name="save_assistance_types"),
    path("save_socio_economic", views.save_socio_economic, name="save_socio_economic"),
    path("save_assistance_aggregate", views.save_assistance_aggregate, name="save_assistance_aggregate"),
    path("process_consent", views.process_consent, name="process_consent"),
    path("process_approval", views.process_approval, name="process_approval"),

    

    path("victim/<id>", views.victim_view, name="victim_view"),

    path('search/', views.search_view, name='search_view'),
    
]
    

