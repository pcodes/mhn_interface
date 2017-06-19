from django import template
import dateutil.parser
import mhn_api.country_lookup as lookup

register = template.Library()

@register.filter(name='fdate')
def fdate(value):
    date = dateutil.parser.parse(value)
    return date.ctime()

@register.simple_tag
def get_flag_ip(ip_addr):
    return lookup.get_flag_ip(ip_addr)

@register.simple_tag
def get_country_name(ip_addr):
    return lookup.get_country_name(ip_addr)

