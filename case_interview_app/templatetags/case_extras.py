from django import template
from case_interview_app.models import Search, Interviewer
from django.core import serializers
from django.utils.safestring import mark_safe
import json

register = template.Library()

@register.simple_tag
def lang_url(url,language):
    other_languages = ['en','fr','pt']
    # if '?' in url:
    #     if 'language' not in url:
    #         url = url+'&language='+language
    #     else:
    for other_lang in other_languages:
        if other_lang == language:
            continue
        url = url.replace(other_lang,language)     
    # else:
    #     url = url + '?language='+language
    
    return url

@register.simple_tag
def search(request):
    searches = {}
    for s in Search.objects.all():
        if s.is_admin == 1:
            if(request.user.is_staff):
                searches[s.search_text] = {
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                }
        elif s.is_technical == 1:
            if(request.user.is_staff or request.user.has_perm):
                searches[s.search_text] = {
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                }
        else:
             if(request.user.is_staff or request.user.has_perm):
                searches[s.search_text] = {
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                }
        
        
    return mark_safe(json.dumps(searches))

@register.filter()
def search_get(request):
    searches = []
    if request.user.is_authenticated:
        interviewer = Interviewer.objects.filter(email_address = request.user.email).first()
    if request.user.is_authenticated:
        for s in Search.objects.all():
            if s.data_entry_purpose_id is not None:
                if(interviewer.data_entry_purpose_id == s.data_entry_purpose_id):
                    if request.LANGUAGE_CODE == "en":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text,
                            "search_link": s.search_link,
                            "search_description": s.search_description,
                            "search_tag": s.search_tag.name
                        })
                    elif request.LANGUAGE_CODE == "fr":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text_fr,
                            "search_link": s.search_link,
                            "search_description": s.search_description_fr,
                            "search_tag": s.search_tag.name
                        })
                    elif request.LANGUAGE_CODE == "pt":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text_pt,
                            "search_link": s.search_link,
                            "search_description": s.search_description_pt,
                            "search_tag": s.search_tag.name
                        })
                else:
                    continue
            if s.is_admin == 1:
                if(request.user.is_staff):
                    if request.LANGUAGE_CODE == "en":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text,
                            "search_link": s.search_link,
                            "search_description": s.search_description,
                            "search_tag": s.search_tag.name
                        })
                    elif request.LANGUAGE_CODE == "fr":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text_fr,
                            "search_link": s.search_link,
                            "search_description": s.search_description_fr,
                            "search_tag": s.search_tag.name
                        })
                    elif request.LANGUAGE_CODE == "pt":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text_pt,
                            "search_link": s.search_link,
                            "search_description": s.search_description_pt,
                            "search_tag": s.search_tag.name
                        })
            elif s.is_technical == 1:
                if(request.user.is_staff or request.user.has_perm):
                    if request.LANGUAGE_CODE == "en":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text,
                            "search_link": s.search_link,
                            "search_description": s.search_description,
                            "search_tag": s.search_tag.name
                        })
                    elif request.LANGUAGE_CODE == "fr":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text_fr,
                            "search_link": s.search_link,
                            "search_description": s.search_description_fr,
                            "search_tag": s.search_tag.name
                        })
                    elif request.LANGUAGE_CODE == "pt":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text_pt,
                            "search_link": s.search_link,
                            "search_description": s.search_description_pt,
                            "search_tag": s.search_tag.name
                        })
            else:
                if(request.user.is_staff or request.user.has_perm):
                    if request.LANGUAGE_CODE == "en":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text,
                            "search_link": s.search_link,
                            "search_description": s.search_description,
                            "search_tag": s.search_tag.name
                        })
                    elif request.LANGUAGE_CODE == "fr":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text_fr,
                            "search_link": s.search_link,
                            "search_description": s.search_description_fr,
                            "search_tag": s.search_tag.name
                        })
                    elif request.LANGUAGE_CODE == "pt":
                        searches.append({
                            "id":s.id,
                            "search_text": s.search_text_pt,
                            "search_link": s.search_link,
                            "search_description": s.search_description_pt,
                            "search_tag": s.search_tag.name
                        })
            
        
    return mark_safe(searches)