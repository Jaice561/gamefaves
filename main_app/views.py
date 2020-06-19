from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Game
# Create your views here.

def home(request):
    return render(request, 'home.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', { 'game': game })

class GameCreate(CreateView):
  model = Game
  fields = ['name', 'genre']
  success_url = '/games/'
