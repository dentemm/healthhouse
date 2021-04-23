import random

from django import template

from ..models.pages import HomePage

register = template.Library()

#
# TEMPLATE TAGS
#

@register.simple_tag
def random_tile():

    ext = ['', 'tile-short', 'tile-long']

    return random.choice(ext)

@register.simple_tag
def menu_items():

    return HomePage.objects.all()[0].get_children().live().in_menu()

#
# TEMPLATE FILTERS
#

@register.filter
def numberify(value):

    string_number = str(value)
    return string_number.replace(',', '.')

@register.filter
def inverse_position(value):

    if (value == 'right'):
        return 'left'
    elif (value == 'left'):
        return 'right'
    return ''

@register.filter
def startswith(text, starts):

    if isinstance(text, str):
        return text.startswith(starts)
    
    return False

@register.filter(name='split')
def split(value, key):
    return value.split(key)