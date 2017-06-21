from django.shortcuts import render
import mhn_api.stats as mhn_stats
import mhn_api.util as mhn_util

def index(request):
    attacks = mhn_stats.get_request('')['data']
    top_ips = mhn_util.get_top_5(attacks, 'source_ip')
    top_ports = mhn_util.get_top_5(attacks, 'destination_port')
    past_24_hours = mhn_stats.get_past_time_attacks(24)

    context = {"total_attacks": past_24_hours, "top_ips": top_ips, "top_ports": top_ports}
    return render(request, 'pages/home.html', context)

# Create your views here.
