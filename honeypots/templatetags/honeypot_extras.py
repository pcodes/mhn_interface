from django import template
import dateutil.parser
import mhn_api.stats as stats

register = template.Library()

@register.filter(name='fdate')
def fdate(value):
    date = dateutil.parser.parse(value)
    return date.ctime()

@register.simple_tag
def get_flag_ip(ip_addr):
    return stats.get_flag_ip(ip_addr)

@register.simple_tag
def get_country_name(ip_addr):
    return stats.get_country_name(ip_addr)

