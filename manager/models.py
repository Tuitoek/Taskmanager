# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import time 
# Create your models here.

class Start(models.Model):
    time = models.CharField(max_length=20)
    color = models.CharField(max_length =20)
    started_at = models.DateTimeField(auto_now_add=True)
    servers= models.CharField(max_length =15)

class Stop(models.Model):
    time = models.CharField(max_length=20)
    color = models.CharField(max_length =20)
    started_at = models.DateTimeField(auto_now_add=True)
    servers= models.CharField(max_length =15)

class Report(models.Model):
    time = models.CharField(max_length=20)
    colors = models.CharField(max_length =20)
    started_at = models.DateTimeField(auto_now_add=True)
    servers= models.CharField(max_length =15)    