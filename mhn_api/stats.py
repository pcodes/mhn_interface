import requests
import os
from django.conf import settings
import environ
from werkzeug.contrib.cache import SimpleCache
import struct
import socket
from django.conf import settings

flag_cache = SimpleCache(threshold=1000, default_timeout=300)
country_cache = SimpleCache(threshold=1000, default_timeout=300)
DEFAULT_FLAG_URL = os.path.dirname(os.getcwd()) + 'static/img/unknown.png'

def get_request(params):
    env = environ.Env

    if settings.DEBUG:
        api_key = {'api_key': os.environ.get('MHN_DEV_KEY')}
    else:
        api_key = {'api_key': env('MHN_API_KEY')}

    base_url = 'http://54.162.74.219/api/session'

    request = {**api_key, **params}

    response = requests.get(base_url, params=request).json()
    return response

def get_past_time_attacks(time):
    time_frame = {'hours_ago' : str(time)}
    past_attacks = get_request(time_frame)
    return len(past_attacks['data'])

def get_user_attacks(honeypot_id):
    id_param = {'identifier': honeypot_id}
    user_attacks = get_request(id_param)
    output = reverse_list(user_attacks['data'])
    return output

def reverse_list(input_list):
    output = []
    for x in range(0, len(input_list)):
        output.append(input_list[len(input_list) - 1 - x])
    return output

def is_RFC1918_addr(ip):
    # 10.0.0.0 = 167772160
    # 172.16.0.0 = 2886729728
    # 192.168.0.0 = 3232235520
    RFC1918_net_bits = ((167772160, 8), (2886729728, 12), (3232235520, 16))

    try:
        # ip to decimal
        ip = struct.unpack("!L", socket.inet_aton(ip))[0]

        for net, mask_bits in RFC1918_net_bits:
            ip_masked = ip & (2 ** 32 - 1 << (32 - mask_bits))
            if ip_masked == net:
                return True
    except Exception as e:
        print('Error ({}) on is_RFC1918_addr: {}'.format(e, ip))

    return False


def get_flag_ip(ipaddr):
    if is_RFC1918_addr(ipaddr):
        return DEFAULT_FLAG_URL

    flag = flag_cache.get(ipaddr)
    if not flag:
        flag = _get_flag_ip(ipaddr)
        flag_cache.set(ipaddr, flag)
    return flag

def get_country_name(ipaddr):
    if is_RFC1918_addr(ipaddr):
        return "Unknown Country"

    country = country_cache.get(ipaddr)
    if not country:
        country = _get_country_name(ipaddr)
        country_cache.set(ipaddr, country)
    return country

def _get_flag_ip(ipaddr):
    flag_path = os.path.dirname(os.getcwd()) + 'static/img/flags-iso/shiny/64/{}.png'
    geo_api = 'https://geospray.threatstream.com/ip/{}'

    try:
        r = requests.get(geo_api.format(ipaddr))
        code = r.json()['countryCode']
    except Exception:
        print("Could not determine flag for ip: {}".format(ipaddr))
        return DEFAULT_FLAG_URL

    else:
        flag = flag_path.format(code.upper())
        complete = settings.APPS_DIR.__str__() + "/" + flag

        if os.path.exists(complete):
            return flag
        else:
            return DEFAULT_FLAG_URL

def _get_country_name(ipaddr):
    geo_api = geo_api = 'https://geospray.threatstream.com/ip/{}'

    try:
        r = requests.get(geo_api.format(ipaddr))
        name = r.json()['countryName']
        return name
    except Exception:
        return "Unknown Country"

