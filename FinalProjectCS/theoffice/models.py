# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Season(models.Model):
    season = models.IntegerField(default=0)
    def __unicode__(self):
		return unicode(self.season)
    
class Episode(models.Model):
    season = models.ForeignKey(Season)
    episode = models.CharField(max_length=100, default='')
    description = models.TextField()
    thumbnail = models.CharField(max_length=100)
    def __unicode__(self):
		return unicode(self.episode)
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    season = models.ManyToManyField(Season)
    def __unicode__(self):
        return unicode(self.name)
		
		
		


