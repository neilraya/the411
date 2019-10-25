from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

def weather(request):

    url = "http://samples.openweathermap.org/data/2.5/weather"

    form = searchForm()

    querystring = {"q": "London,uk","appid":"b6907d289e10d714a6e88b30761fae22", "units": "imperial"}

    #querystring['q'] = request.POST

    headers = {
        'User-Agent': "PostmanRuntime/7.18.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "8be8b4eb-151e-4ef2-bbfb-50e6b65b6825,5909aa04-7312-4570-b457-b9d58d83d25b",
        'Accept-Encoding': "gzip, deflate",
        'Referer': "http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    template = loader.get_template('weather/index.html')


    weather = {
        'city' : response['name'],
        'temperature' : response['main']['temp'],
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon']
    }

    return HttpResponse(template.render(weather, request))
