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
def number_with_dots(value):
    
    return value.replace(',', '.')

@register.filter
def inverse_image_position(value):

    if (value == 'right'):
        return 'left'
    elif (value == 'left'):
        return 'right'
    return ''
