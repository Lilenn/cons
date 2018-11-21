from django.template import Library
register = Library()
@register.filter
def reduce(value):
    return int(value) - 1
@register.filter
def add(value):
    return int(value) + 1