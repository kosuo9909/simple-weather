import math
from datetime import datetime

from django.shortcuts import render
import requests


def index(request):
    API_ID = 'eaca8af8aeb337cfa1ff34aa3f670179'
    URL_GEO = 'http://api.openweathermap.org/geo/1.0/direct'
    URL_WEATHER = 'https://api.openweathermap.org/data/2.5/weather'

    city = request.POST.get('city')
    # GET GEO LOCATION
    PARAMS_GEO = {
        'q': 'Sofia' if not city else city,
        'state code': '',
        'appid': API_ID,
        'units': 'metric',
    }

    r_geo = requests.get(url=URL_GEO, params=PARAMS_GEO)
    result_geo = r_geo.json()

    lat = result_geo[0]['lat']
    lon = result_geo[0]['lon']

    PARAMS_WEATHER = {
        'lat': lat,
        'lon': lon,
        'appid': API_ID,
        'units': 'metric',
    }
    r_weather = requests.get(url=URL_WEATHER, params=PARAMS_WEATHER)
    result_weather = r_weather.json()

    name = result_weather['name']
    # TODAY
    weather_main = result_weather['weather'][0]['main']
    weather_description = result_weather['weather'][0]['description']
    weather_icon = result_weather['weather'][0]['icon']

    temperature = result_weather['main']['temp']
    feels_like = result_weather['main']['temp']

    context = {
        'result': result_weather,
        'city': city,
        'weather_main': weather_main,
        'weather_desc': weather_description,
        'weather_icon': weather_icon,
        'temperature': math.ceil(temperature),
        'feels_like': feels_like,
        'name': name,
        'date': datetime.now(),
    }
    return render(request, 'index.html', context=context)
