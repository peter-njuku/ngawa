from django import template
import datetime

register=template.Library()

@register.simple_tag
def current_year(): return datetime.datetime.now().year

@register.simple_tag
def copyright_years(start_year):
    current=datetime.datetime.now().year
    if current == start_year or start_year is None: return str(current) 
    else: return f'{current}'