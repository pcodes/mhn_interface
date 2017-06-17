from django import template
import dateutil.parser

register = template.Library()

@register.filter(name='fdate')
def fdate(value):
    date = dateutil.parser.parse(value)
    return date.ctime()

