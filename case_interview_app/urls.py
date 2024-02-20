from django.urls import path

from . import views
from . import apis
from . import som_views

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
    path('suspect/<int:suspect_id>/', views.suspect_detail, name='suspect_detail'),
    path('interviewer/<int:interviewer_id>/', views.interviewer_detail, name='interviewer_detail'),

    path('api/interviewers/', apis.InterviewerRegistrationAPIView.as_view(), name='interviewer-list-api'),
    path('api/interviewer/<int:pk>/', apis.InterviewerRegistrationAPIView.as_view(), name='interviewer-detail-api'),
    path('api/cases/', apis.CasesWithCountsAPIView.as_view(), name='cases-api'),
    path('api/victims/', apis.TipVictimAPIView.as_view(), name='victim-api'),
    path('api/victims/<int:pk>/', apis.TipVictimAPIView.as_view(), name='victim-detail-api'),




    path("som_interviewer_registration", som_views.interviewer_registration, name="som_interviewer_registration"),
    path("som_investigation_form", som_views.investigation_form, name="som_investigation_form"),
    path("som_prosecution_form", som_views.prosecution_form, name="som_prosecution_form"),
    path("som_form", som_views.tip_form, name="som_tip_form"),
    path("som_assistance_form", som_views.assistance_form, name="som_assistance_form"),

    path("som_cases", som_views.cases, name="som_cases"),
    path("som_save_victim", som_views.save_victim, name="som_save_victim"),
    path("som_save_arrest", som_views.save_arrest, name="som_save_arrest"),
    path("som_save_suspect", som_views.save_suspect, name="som_save_suspect"),
    path("som_save_prosecution", som_views.save_prosecution, name="som_save_prosecution"),
    path("som_save_exploitation", som_views.save_exploitation, name="som_save_exploitation"),
    path("som_save_transit", som_views.save_transit, name="som_save_transit"),
    path("som_save_assistance_types", som_views.save_assistance_types, name="som_save_assistance_types"),
    path("som_save_socio_economic", som_views.save_socio_economic, name="som_save_socio_economic"),
    path("som_save_assistance_aggregate", som_views.save_assistance_aggregate, name="som_save_assistance_aggregate"),
    path("som_process_consent", som_views.process_consent, name="som_process_consent"),
    path("som_process_approval", som_views.process_approval, name="som_process_approval"),

    path("som_victim/<id>", som_views.victim_view, name="som_victim_view"),

    path('som_suspect/<int:suspect_id>/', som_views.suspect_detail, name='som_suspect_detail'),
    path('som_interviewer/<int:interviewer_id>/', som_views.interviewer_detail, name='som_interviewer_detail'),
]
    

