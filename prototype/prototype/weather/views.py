from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from weather.forms import searchForm
import requests
import yelpapi

passwords = {}
with open("prototype/passwords.txt") as f:
    for line in f:
        (key, val) = line.split()
        passwords[key] = val

def login(request):
    return render(request, "weather/login.html")

def main(request):
    return render(request, "weather/main.html")
    
def yelp(request):
    yelp = yelpapi.YelpAPI(passwords['YELP_API_KEY'])
    response = yelp.search_query(location=request.POST['cname'],
                                 price="1")
    temperature = weather(request)
    print(response)
    return render(request, "weather/yelpSearch.html", {"response":response, "temperature":temperature})
    
def weather(request):

    url = "http://api.openweathermap.org/data/2.5/weather"

    querystring = {"q":request.POST['cname'],"APPID":passwords['WEATHER_API_KEY']}

    headers = {
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "6e50db66-a2e8-4b9f-b8ef-fd00cbf8d955,ebe1363c-f7d7-4316-a683-ea6064efbf56",
        'Host': "api.openweathermap.org",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.get(url, headers=headers, params=querystring).json()

    #template = loader.get_template('weather/login.html')

    #print(response)

    #weatherres = {
    #    'city' : response['name'],
    #    'temperature' : response['main']['temp'],
    #    'description' : response['weather'][0]['description'],
    #    'icon' : response['weather'][0]['icon']
    #}

    #return HttpResponse(template.render(weather, request))
    #return render(request, "weather/main.html", {"weather":weather})#, "searchform":template, })
    return response['main']['temp']
