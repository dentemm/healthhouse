from django import template

from ..models import Menu

register = template.Library()

@register.simple_tag()
def get_menu(identifier):
  return Menu.objects.filter(identifier=identifier).first()