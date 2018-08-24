import random

from django import template

register = template.Library()

#
# TEMPLATE TAGS
#

@register.simple_tag
def random_tile():

    ext = ['', 'tile-short', 'tile-long']

    return random.choice(ext)

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
