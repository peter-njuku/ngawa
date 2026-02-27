import base64
from django import template

register = template.Library()

@register.filter
def to_b64(value):
    return base64.b64encode(value.encode()).decode()