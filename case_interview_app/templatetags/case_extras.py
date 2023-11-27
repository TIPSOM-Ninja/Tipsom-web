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
def search(user):
    searches = {}
    for s in Search.objects.all():
        if s.is_admin == 1:
            if(user.is_staff):
                searches[s.search_text] = {
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                }
        elif s.is_technical == 1:
            if(user.is_staff or user.has_perm):
                searches[s.search_text] = {
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                }
        else:
             if(user.is_staff or user.has_perm):
                searches[s.search_text] = {
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                }
        
        
    return mark_safe(json.dumps(searches))

@register.filter()
def search_get(user):
    searches = []
    if user.is_authenticated:
        interviewer = Interviewer.objects.filter(email_address = user.email).first()
    if user.is_authenticated:
        for s in Search.objects.all():
        if s.data_entry_purpose_id is not None:
            if(interviewer.data_entry_purpose_id == s.data_entry_purpose_id):
                searches.append({
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                })
            else:
                continue
        if s.is_admin == 1:
            if(user.is_staff):
                searches.append({
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                })
        elif s.is_technical == 1:
            if(user.is_staff or user.has_perm):
                searches.append({
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                })
        else:
             if(user.is_staff or user.has_perm):
                searches.append({
                    "id":s.id,
                    "search_text": s.search_text,
                    "search_link": s.search_link,
                    "search_description": s.search_description,
                    "search_tag": s.search_tag.name
                })
        
        
    return mark_safe(searches)