from django.shortcuts import render
from django.http import HttpResponse
import requests

url = "http://api.weatherapi.com/v1/forecast.json"
api_key = "5e619981755b4c10a41180919241601"

parameter = {
    "key": api_key,
    "q" : "Bangladesh"
}

fetched_weather_data = requests.get(url, params=parameter)

# Create your views here.
def weather(request):
    return HttpResponse(fetched_weather_data)