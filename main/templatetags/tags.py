## tags.py
from django import template

register = template.Library()

@register.simple_tag
def is_active(request , pattern):
    import re
    if pattern != "/" and request.path != "/" :
        if re.search(pattern , request.path): 
            return 'active'
    else:
        if pattern == "/" and request.path == "/":
            return 'active'
    return ''