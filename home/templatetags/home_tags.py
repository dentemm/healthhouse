from django import template

register = template.Library()

def number_with_dots(value):
    
    return value.replace(',', '.')

register.filter('number_with_dots', number_with_dots)

def inverse_image_position(value):

    if (value == 'right'):
        return 'left'
    elif (value == 'left'):
        return 'right'
    return ''

register.filter('inverse_position', inverse_image_position)