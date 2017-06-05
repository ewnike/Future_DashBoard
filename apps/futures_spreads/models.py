# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class FutureManager(models.Manager):
    def get_or_create(self, name, symbol):
        try:
            return Future.objects.get(symbol=symbol.upper())
        except:
            return Future.objects.create(name=name, symbol=symbol.upper())

class SpreadManager(models.Manager):
    def get_or_create(self, front_id, back_id):
        try:
            return Spread.objects.get(back_id=back_id.upper(), front_id=front_id.upper())
        except:
            return Spread.objects.create(back_id=back_id.upper() ,front_id=front_id.upper())

class Future(models.Model):
    name= models.CharField(max_length = 64)
    symbol= models.CharField(max_length = 64, unique=True)
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)
    objects = FutureManager()

class Spread(models.Model):
    front=models.ForeignKey(Future, related_name = 'front_month')
    back = models.ForeignKey(Future, related_name='back_month')
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)
    objects = SpreadManager()
