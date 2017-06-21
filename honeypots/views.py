from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import mhn_api.stats as stats
import mhn_api.util as mhn_util


def my_honeypot(request):
    if request.user.is_authenticated():
        attacks = stats.get_user_attacks(request.user.honey_id)
        paginator = Paginator(attacks, 15)

        page = request.GET.get('page')
        try:
            attacks = paginator.page(page)
        except PageNotAnInteger:
            attacks = paginator.page(1)
        except EmptyPage:
            attacks = paginator.page(paginator.num_pages)

        context = {'attacks': attacks}
    else:
        context = {}
    return render(request, 'pages/my_honeypot.html', context)

def all_honeypots(request):
    context = {}
    return render(request, 'pages/all_honeypots.html', context)


def team_attacks(request):
    UUID = [
        '9497c654-54fd-11e7-8bca-0ad79c5b832c',
        '9812c8ba-54fd-11e7-8bca-0ad79c5b832c',
        '99f75d44-54fd-11e7-8bca-0ad79c5b832c',
        '9c1be306-54fd-11e7-8bca-0ad79c5b832c',
        'e67b19c0-54fe-11e7-8bca-0ad79c5b832c',
        'e801e170-54fe-11e7-8bca-0ad79c5b832c',
        'e9b85e4a-54fe-11e7-8bca-0ad79c5b832c',
        'eb8dc656-54fe-11e7-8bca-0ad79c5b832c'
    ]

    team_num = int(request.GET.get('team'))
    attacks = stats.get_user_attacks(UUID[team_num-1])
    paginator = Paginator(attacks, 15)

    page = request.GET.get('page')
    try:
        attacks = paginator.page(page)
    except PageNotAnInteger:
        attacks = paginator.page(1)
    except EmptyPage:
        attacks = paginator.page(paginator.num_pages)

    context = {'attacks': attacks, 'team': team_num}
    return render(request, 'pages/team.html', context)

def team_stats(request):
    UUID = [
        '9497c654-54fd-11e7-8bca-0ad79c5b832c',
        '9812c8ba-54fd-11e7-8bca-0ad79c5b832c',
        '99f75d44-54fd-11e7-8bca-0ad79c5b832c',
        '9c1be306-54fd-11e7-8bca-0ad79c5b832c',
        'e67b19c0-54fe-11e7-8bca-0ad79c5b832c',
        'e801e170-54fe-11e7-8bca-0ad79c5b832c',
        'e9b85e4a-54fe-11e7-8bca-0ad79c5b832c',
        'eb8dc656-54fe-11e7-8bca-0ad79c5b832c'
    ]

    team_num = int(request.GET.get('team'))
    attacks = stats.get_user_attacks(UUID[team_num-1])

    past_24_hours = stats.get_user_time_attacks(24, UUID[team_num-1])
    top_ips = mhn_util.get_top_5(attacks, 'source_ip')
    top_ports = mhn_util.get_top_5(attacks, 'destination_port')

    context = {"total_attacks": past_24_hours, "top_ips": top_ips, "top_ports": top_ports, "team": team_num}
    return render(request, 'pages/team_overview.html', context)
