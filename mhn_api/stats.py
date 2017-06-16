import requests
import os
from django.conf import settings
import environ

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
