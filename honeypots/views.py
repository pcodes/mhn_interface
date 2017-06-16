from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import mhn_api.stats as stats


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
