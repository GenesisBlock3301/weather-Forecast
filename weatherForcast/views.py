from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from . import weather_service


def index(request:HttpRequest):
     cities = ['dhaka','chittagong','sylhet','christchurch']
     return render(request, 'index.html', context={
        'weather_updates': [weather_service.get_weather(city) for city in cities ]
    })