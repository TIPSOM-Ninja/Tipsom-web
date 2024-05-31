from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import apis
from . import som_views
from django.conf.urls import handler400, handler403, handler404, handler500

handler400 = 'case_interview_app.views.handler400'
handler403 = 'case_interview_app.views.handler403'
handler404 = 'case_interview_app.views.handler404'
handler500 = 'case_interview_app.views.handler500'
# Django does not support custom handlers for 502, 503, and 504 errors out of the box
#You can handle these errors at the server level. For example, if you're using Nginx or Apache, 
#you can configure these servers to show custom pages for these errors.

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

    path('api/prosecutions/', apis.TipProsecutionAPIView.as_view(), name='prosecution-api'),
    path('api/prosecutions/<int:v_id>/<int:pk>/', apis.TipProsecutionAPIView.as_view(), name='victim-prosecution-api'),
    path('api/prosecutions/<int:v_id>/', apis.TipProsecutionAPIView.as_view(), name='prosecution-detail-api'),


    path('api/suspects/', apis.TipSuspectAPIView.as_view(), name='suspect-api'),
    path('api/suspects/<int:v_id>/', apis.TipSuspectAPIView.as_view(), name='victim-suspect-api'),
    path('api/suspects/<int:v_id>/<int:pk>/', apis.TipSuspectAPIView.as_view(), name='suspect-detail-api'),

    path('api/exploitations/', apis.TipExploitationAPIView.as_view(), name='exploitation-api'),
    path('api/exploitations/<int:v_id>/', apis.TipExploitationAPIView.as_view(), name='victim-exploitation-api'),
    path('api/exploitations/<int:v_id>/<int:pk>/', apis.TipExploitationAPIView.as_view(), name='exploitation-detail-api'),

    path('api/transits/', apis.TipTransitAPIView.as_view(), name='transit-api'),
    path('api/transits/<int:v_id>/', apis.TipTransitAPIView.as_view(), name='victim-transit-api'),
    path('api/transits/<int:v_id>/<int:pk>/', apis.TipTransitAPIView.as_view(), name='transit-detail-api'),

    path('api/arrests/', apis.TipArrestAPIView.as_view(), name='arrest-api'),
    path('api/arrests/<int:v_id>/', apis.TipArrestAPIView.as_view(), name='victim-arrest-api'),
    path('api/arrests/<int:v_id>/<int:pk>/', apis.TipArrestAPIView.as_view(), name='arrest-detail-api'),

    path('api/assistances/', apis.TipAssistanceAPIView.as_view(), name='assistance-api'),
    path('api/assistances/<int:v_id>/', apis.TipAssistanceAPIView.as_view(), name='victim-assistance-api'),
    path('api/assistances/<int:v_id>/<int:pk>/', apis.TipAssistanceAPIView.as_view(), name='assistance-detail-api'),

    path('api/socios/', apis.TipSocioAPIView.as_view(), name='socio-api'),
    path('api/socios/<int:v_id>/', apis.TipSocioAPIView.as_view(), name='victim-socio-api'),
    path('api/socios/<int:v_id>/<int:pk>/', apis.TipSocioAPIView.as_view(), name='socio-detail-api'),

    path('api/aggregates/', apis.TipAggregateAPIView.as_view(), name='aggregate-api'),
    path('api/aggregates/<int:pk>/', apis.TipAggregateAPIView.as_view(), name='aggregate-details-api'),

    path('api/victim/search/', apis.VictimSearchAPIView.as_view(), name='victim-search'),

    path("som_investigation_form", som_views.investigation_form, name="som_investigation_form"),
    path("som_prosecution_form", som_views.prosecution_form, name="som_prosecution_form"),
    path("som_form", som_views.som_form, name="som_tip_form"),
    path("som_assistance_form", som_views.assistance_form, name="som_assistance_form"),

    path("som_cases", som_views.cases, name="som_cases"),
    path("som_save_case", som_views.save_case, name="som_save_case"),
    path("som_save_victim", som_views.save_victim, name="som_save_victim"),
    path("som_save_multi_victim", som_views.save_multi_victim, name="som_save_multi_victim"),
    path("som_save_arrest", som_views.save_arrest, name="som_save_arrest"),
    path("som_save_suspect", som_views.save_suspect, name="som_save_suspect"),
    path("som_save_prosecution", som_views.save_prosecution, name="som_save_prosecution"),
    path("som_save_transit", som_views.save_transit, name="som_save_transit"),
    path("som_save_assistance_types", som_views.save_assistance_types, name="som_save_assistance_types"),
    path("som_save_socio_economic", som_views.save_socio_economic, name="som_save_socio_economic"),
    path("som_process_consent", som_views.process_consent, name="som_process_consent"),
    path("som_process_approval", som_views.process_approval, name="som_process_approval"),

    path("som_case/<id>", som_views.victim_view, name="som_victim_view"),

    path('som_suspect/<int:suspect_id>/', som_views.suspect_detail, name='som_suspect_detail'),
    path('som_interviewer/<int:interviewer_id>/', som_views.interviewer_detail, name='som_interviewer_detail'),


    path('api/som/victims/', apis.SomVictimAPIView.as_view(), name='som-victim-api'),
    path('api/som/victims/<int:c_id>/', apis.SomVictimAPIView.as_view(), name='som-victim-detail-api'),
    path('api/som/victims/<int:c_id>/<int:pk>/', apis.SomVictimAPIView.as_view(), name='som-case-victim-api'),

    path('api/som/prosecutions/', apis.SomProsecutionAPIView.as_view(), name='som-prosecution-api'),
    path('api/som/prosecutions/<int:c_id>/', apis.SomProsecutionAPIView.as_view(), name='som-prosecution-detail-api'),
    path('api/som/prosecutions/<int:c_id>/<int:pk>/', apis.SomProsecutionAPIView.as_view(), name='som-case-prosecution-api'),


    path('api/som/cases/', apis.SomCaseAPIView.as_view(), name='som-case-api'),
    path('api/som/cases/<int:pk>/', apis.SomCaseAPIView.as_view(), name='som-victim-case-api'),

    path('api/som/suspects/', apis.SomSuspectAPIView.as_view(), name='som-suspect-api'),
    path('api/som/suspects/<int:v_id>/', apis.SomSuspectAPIView.as_view(), name='som-victim-suspect-api'),
    path('api/som/suspects/<int:v_id>/<int:pk>/', apis.SomSuspectAPIView.as_view(), name='som-suspect-detail-api'),

    path('api/som/transits/', apis.SomTransitAPIView.as_view(), name='som-transit-api'),
    path('api/som/transits/<int:c_id>/', apis.SomTransitAPIView.as_view(), name='som-victim-transit-api'),
    path('api/som/transits/<int:c_id>/<int:pk>/', apis.SomTransitAPIView.as_view(), name='som-transit-detail-api'),

    path('api/som/arrests/', apis.SomArrestAPIView.as_view(), name='som-arrest-api'),
    path('api/som/arrests/<int:v_id>/', apis.SomArrestAPIView.as_view(), name='som-victim-arrest-api'),
    path('api/som/arrests/<int:v_id>/<int:pk>/', apis.SomArrestAPIView.as_view(), name='som-arrest-detail-api'),

    path('api/som/assistances/', apis.SomAssistanceAPIView.as_view(), name='som-assistance-api'),
    path('api/som/assistances/<int:v_id>/', apis.SomAssistanceAPIView.as_view(), name='som-victim-assistance-api'),
    path('api/som/assistances/<int:v_id>/<int:pk>/', apis.SomAssistanceAPIView.as_view(), name='som-assistance-detail-api'),

    path('api/som/socios/', apis.SomSocioAPIView.as_view(), name='som-socio-api'),
    path('api/som/socios/<int:v_id>/', apis.SomSocioAPIView.as_view(), name='som-victim-socio-api'),
    path('api/som/socios/<int:v_id>/<int:pk>/', apis.SomSocioAPIView.as_view(), name='som-socio-detail-api'),

    path('api/som/victim/search/', apis.SomVictimSearchAPIView.as_view(), name='som-victim-search'),

    path('api/som/multi_victims/', apis.SomMultiVictimAPIView.as_view(), name='som-multivictim-api'),
    path('api/som/multi_victims/<int:c_id>/', apis.SomMultiVictimAPIView.as_view(), name='som-multivictim-detail-api'),
    path('api/som/multi_victims/<int:c_id>/<int:pk>/', apis.SomMultiVictimAPIView.as_view(), name='som-case-multivictim-api'),



    path("dashboard", views.dashboard, name="dashboard"),

]
    
if settings.DEBUG is False:   # if DEBUG is True it will be served automatically
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
