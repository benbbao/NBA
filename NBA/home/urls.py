from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('playersHome/', views.playersHome, name='players-homepage'),
    path('teamsHome/', views.teamsHome, name='teams-homepage'),
    path('comparePlayers/', views.comparePlayers, name='compare-players'),
    path('compareTeams/', views.compareTeams, name='compare-teams'),
    path('watchlist/', views.watchlist, name='watchlist'),
]