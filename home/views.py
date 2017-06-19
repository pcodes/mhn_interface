from django.shortcuts import render
import mhn_api.stats as mhn_stats
import mhn_api.util as mhn_util

def index(request):
    if request.user.is_authenticated():
        user_attacks = mhn_stats.get_user_attacks(request.user.honey_id)
        top_ips = mhn_util.get_top_5(user_attacks, 'source_ip')
        top_ports = mhn_util.get_top_5(user_attacks, 'destination_port')
        recent_attacks = mhn_stats.get_user_time_attacks(24, request.user.honey_id)
        context = {"total_attacks": recent_attacks, "top_ips": top_ips, "top_ports": top_ports}

    else:
        past_24_hours = mhn_stats.get_past_time_attacks(24)
        context = {"total_attacks": past_24_hours}

    return render(request, 'pages/home.html', context)

# Create your views here.
