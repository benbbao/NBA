from django.shortcuts import render

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

def watchlist(request):
    return render(request, 'home/watchlist.html')