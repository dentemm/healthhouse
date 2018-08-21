from django import template

register = template.Library()

def number_with_dots(value):
    
    return value.replace(',', '.')

register.filter('number_with_dots', number_with_dots)