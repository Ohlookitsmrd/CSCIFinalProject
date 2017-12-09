# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from theoffice.models import *

# Register your models here.
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('season', )

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('episode', )

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'actor', )

admin.site.register(Season, SeasonAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Character, CharacterAdmin)
