from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('playersHome/', views.playersHome, name='players-homepage'),
    path('teamsHome/', views.teamsHome, name='teams-homepage'),
    path('comparePlayers/', views.comparePlayers, name='compare-players'),
    path('compareTeams/', views.compareTeams, name='compare-teams'),
    path('watchlist3/', views.watchlist3, name='watchlist3'),
    path('steven-adams/', views.singleplayer, name='steven'),
    path('milwaukee-bucks/', views.singleteam, name='bucks'),
    path('miami-heat/', views.teamsearch, name='heat'),
    path('watchlist1/', views.watchlist1, name='watchlist1'),
    path('utah-jazz/', views.utahjazz, name='jazz'),
    path('watchlist2/', views.watchlist2, name='watchlist2'),
    path('comparePlayers2/', views.comparePlayers2, name='compare-players2'),
    path('comparePlayers3/', views.comparePlayers3, name='compare-players3'),
]