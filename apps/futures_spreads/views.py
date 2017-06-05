# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . models import *
from django.db.models import Count
import re
import plotly
plotly.tools.set_credentials_file(username='ewnike', api_key='••••••••••')
EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):

    context={
        'futures':Future.objects.all(),
        'spreads':Spread.objects.all()
    }
    return render(request, 'futures_spreads/index.html', context)


def spreads(request):
    context={
        'futures':Future.objects.all(),
        'spreads':Spread.objects.all()
    }
    future_filter = {}
    unique_futures= []

    for future in Future.objects.all():
        key = future.symbol
        if key not in future_filter and len(key.strip()) > 0:
            future_filter[key] = True
            unique_futures.append(future)

    return render(request,'futures_spreads/spread.html', context)

def create_spread(request):

    if request.method== "POST":

        print request.POST
        front = Future.objects.get(id=request.POST['front'])
        back = Future.objects.get(id=request.POST['back'])
        Spread.objects.create(front=front, back=back)
    # spread={}
    # spread=Spread.objects.get_or_create(front_id=request.POST['front_id'], back_id=request.POST['back_id'])
    return redirect('futures_spreads:spreads')

def add_symbols(request):
    future={}
    future=Future.objects.get_or_create(name=request.POST['name'], symbol=request.POST['symbol'])

    return redirect('futures_spreads:index')

def add_future(request):
    context={
        'futures':Future.objects.all()
    }
    future_filter = {}
    unique_futures= []

    for future in Future.objects.all():
        key = future.symbol
        if key not in future_filter and len(key.strip()) > 0:
            future_filter[key] = True
            unique_futures.append(future)
    context['futures']=unique_futures

    return render(request, 'futures_spreads/add_future.html', context)

def make_spreads(request, future_id):
    future = Future.objects.get(id=future_id)
    front=None
    try:
        front = Spread.objects.filter(front_id= future_id)
    except:
        return redirect('futures_spreads:index')

    back=Future.objects.exclude(back_month__front=future)
    # staff__leader_id=leader_id
    context = {
        'future': future,
        'front':front,
        'back':back,
        }
    print context['back']
    print Future.objects.values("id")

    return render(request, 'futures_spreads/make_spreads.html', context )

def update_future(request, future_id):
    return redirect(reverse('futures_spreads:make_spreads', kwargs ={'future_id':future_id} ))

def assign_future(request, front_id, back_id):
    # try:
    #     Spread.objects.get(back_id=back_id, front_id=front_id)
    # except:
    #     Spread.objects.create(back_id=back_id ,front_id=front_id)
    spread={}
    spread=Spread.objects.get_or_create(front_id=front_id, back_id=back_id)
    return redirect(reverse('futures_spreads:make_spreads', kwargs={'future_id':front_id}))

def remove_future(request, front_id, back_id):
    back=Spread.objects.get(back_id=back_id ,front_id=front_id)

    back.delete()
    return redirect(reverse('futures_spreads:make_spreads', kwargs={'future_id':front_id}))
