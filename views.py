from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse_lazy 
from .models import squirrel
from .forms import SquirrelForm
import json
import random

def sighting(request):
    Squirrels = squirrel.objects.all()
    context = {
            'squirrels':Squirrels,
            'fields':data,
            }
    return render(request,'Sightings/sight.html', context)


def update_squirrel(request,uniqueID):
    Squirrel = squirrel.objects.get(UniqueID=uniqueID)
    form = SquirrelForm(instance=Squirrel)
    context={
              'form':form,
               'squirrel':Squirrel
                }
    return render(request,'Sightings/update_squirrel.html', context)



def add_squirrel(request):
    form = SquirrelForm()
    context = {'form': form,}
    return render(request, 'Sightings/add_squirrel.html', context)


def stats(request):
    running_count = Squirrel.objects.values('Running').order_by('Running').annotate(running_count=Count('Running'))
    chasing_count = Squirrel.objects.values('Chasing').order_by('Chasing').annotate(chasing_count=Count('Chasing'))
    climbing_count = Squirrel.objects.values('Climbing').order_by('Climbing').annotate(climbing_count=Count('Climbing'))
    approaches_count = Squirrel.objects.values('Approaches').order_by('Approaches').annotate(approaches_count=Count('Approaches'))
    foraging_count = Squirrel.objects.values('Foraging').order_by('Foraging').annotate(foraging_count=Count('Foraging'))
    running = running_count[2]['running_count']
    chasing = chasing_count[2]['chasing_count']
    climbing = climbing_count[2]['climbing_count']
    approaches = approaches_count[2]['approaches_count']
    foraging = foraging_count[2]['foraging_count']

    context = {
        'Running': running,
        'Chasing': chasing,
        'Climbing': climbing,
        'Approaches': approaches,
        'Foraging': foraging,
            }
    return render(request, 'Sightings/stats.html',context)

def map (request):
    Squirrels = squirrel.objects.all()[:70]
    context = {
            'Squirrels': Squirrels
            }
    return render (request, 'Sightings/map.html', context)