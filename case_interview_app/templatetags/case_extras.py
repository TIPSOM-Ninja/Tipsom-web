from django import template
from case_interview_app.models import Search
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
def search(name):
    searches = {}
    for s in Search.objects.all():
        searches[s.search_text] = {
            "search_text": s.search_text,
            "search_link": s.search_link,
            "search_description": s.search_description,
            "search_tag": s.search_tag.name
        }
    return mark_safe(json.dumps(searches))