from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^my_honeypot/', views.my_honeypot, name='my_honeypot'),
    url(r'^all_honeypots/', views.all_honeypots, name='all_honeypots'),
    url(r'^team', views.team_attacks, name='team_attacks')
]
