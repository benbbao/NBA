from django.db import models

class PlayerStats(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=5)
    gp = models.IntegerField()
    mpg = models.FloatField()
    ftper = models.FloatField()
    ppg = models.FloatField()
    rpg = models.FloatField()
    apg = models.FloatField()
    spg = models.FloatField()
    bpg = models.FloatField()
    topg = models.FloatField()

    class Meta:
        managed = False
        db_table = 'player_stats'

class TeamStats(models.Model):
    city = models.CharField(primary_key=True, max_length=50)
    conference = models.CharField(max_length=5)
    gp = models.IntegerField()
    ppg = models.FloatField()
    papg = models.FloatField()
    sos = models.FloatField()
    wins = models.IntegerField()
    loses = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_stats'


