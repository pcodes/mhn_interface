from django.db import models

class Honeypot(models.Model):
    team_id = models.IntegerField(default=-1)
    honey_id = models.CharField(max_length=200)
