from django import template

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