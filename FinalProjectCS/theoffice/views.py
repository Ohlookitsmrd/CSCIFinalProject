# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
#from django.core.context_processors import csrf
from django.shortcuts import loader, render
from django.http import HttpResponse
from .models import *
import re

# Create your views here.

def episode(request, episode):
    episode = Episode.objects.filter(episode = episode)
    t = loader.get_template('episode.html')
    c = dict({'episodeSelect': episode })
    return HttpResponse(t.render(c))

def home(request):
    season=Season.objects.all()
    t = loader.get_template('home.html')
    c = dict({'season': season })
    return HttpResponse(t.render(c))

def season(request, season):
    seasonname = str(re.sub('/season/', '', (request.path)))
    seasonobj = Season.objects.get(season = season)
    episode = Episode.objects.filter(season_id = seasonobj.id)
    season = Season.objects.filter(season=season)
    t = loader.get_template('season.html')
    c = dict({'seasonSelect': season, 'episodeSelect': episode })
    return HttpResponse(t.render(c))

def character(request, name):
    name = Character.objects.filter(character = name)
    t = loader.get_template('character.html')
    c = dict({'characterSelect': character })
    return HttpResponse(t.render(c))

def character(request):
    character=Character.objects.all()
    t = loader.get_template('character.html')
    c = dict({'characterSelect': character })
    return HttpResponse(t.render(c))