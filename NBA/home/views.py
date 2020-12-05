from django.shortcuts import render

from home.models import PlayerStats
from home.models import TeamStats

def home(request):
    return render(request, 'home/home.html')

def playersHome(request):
    return render(request, 'home/playersHome.html')

def teamsHome(request):
    return render(request, 'home/teamsHome.html')

def comparePlayers(request):
    return render(request, 'home/comparePlayers.html')

def compareTeams(request):
    return render(request, 'home/compareTeams.html')

def watchlist3(request):
    return render(request, 'home/watchlist3.html')

def watchlist1(request):
    return render(request, 'home/watchlist1.html')

def singleplayer(request):
    return render(request, 'home/singleplayer.html')

def singleteam(request):
    return render(request, 'home/singleteam.html')

def teamsearch(request):
    return render(request, 'home/teamsSearch.html')

def utahjazz(request):
    return render(request, 'home/utahJazz.html')  

def watchlist2(request):
    return render(request, 'home/watchlist2.html')  

def comparePlayers2(request):
    return render(request, 'home/comparePlayers2.html')

def comparePlayers3(request):
    return render(request, 'home/comparePlayers3.html')