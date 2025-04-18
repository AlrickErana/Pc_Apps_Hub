from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    apps = App.objects.all()
    return render(request, 'home.html', {'apps': apps})

def apps(request):
    apps = App.objects.filter(category=1)
    return render(request, 'apps.html', {'apps': apps})

def games(request):
    games = App.objects.filter(category=2)
    return render(request, 'games.html', {"games": games})

def about(request):
    return render(request, 'about.html')

#wala pa nahuman
def all(request):
    return render(request, 'all.html')

def all_apps_view(request):
    apps = App.objects.all()
    return render(request, 'all_apps.html', {'apps': apps})

def app_detail(request, id):
    app = get_object_or_404(App, id=id)
    return render(request, 'app_detail.html', {'app': app})

# def all_games(request):
#     games = App.objects.filter(category=2)
#     print("🔍 Found games:", games)
#     return render(request, 'games.html', {'games': games})
# def all_games(request):
#     apps = App.objects.filter(category=2)
#     print("🎮 all_games view is being called!")
#     return render(request, 'games.html', {'games': []})

def game_detail(request, id):
    # Get the detail of a specific game
    game = get_object_or_404(App, id=id)
    return render(request, 'game_detail.html', {'game': game})