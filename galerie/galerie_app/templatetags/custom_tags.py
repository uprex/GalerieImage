from django import template

register = template.Library()
from galerie_app.models import Post


@register.simple_tag
def incremente(var):
    return var +1;