from django.shortcuts import render
import mhn_api.stats as mhn_stats

def index(request):
    past_24_hours = mhn_stats.get_past_time_attacks(24)

    context = {"total_attacks" : past_24_hours}

    return render(request, 'pages/home.html', context)

# Create your views here.
