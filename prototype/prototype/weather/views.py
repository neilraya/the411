from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from weather.forms import searchForm
from .models import SearchHistory
import requests
import yelpapi

#Gives access to our local passwords for the API's and facebook login
passwords = {}
with open("prototype/passwords.txt") as f:
    for line in f:
        (key, val) = line.split()
        passwords[key] = val

#Loads up the login screen
def login(request):
    return render(request, "weather/login.html")
    
 
#Loads up main page after login is successful
def main(request):
    return render(request, "weather/main.html")
    
    
#Accesses the yelp API after the user searches
def yelp(request):
    
    #Database saving search history
    search_history = SearchHistory()
    search_history.CityName = request.POST['cname']
    search_history.save()


    #Changing kelvin to Farenheit
    temperature =  round(((9*(weather(request) - 273))/5) +32)
    
    #Icon is the sun to represent warm weather and snowflake for cold
    #color is red for sun and blue for cold
    #out is a boolean that helps filter out utdoor events in cold weather
    icon = ""
    color=""
    out = True
    if(temperature > 50):
        icon = "fa fa-sun-o fa-3x"
        color = "#FF0000;"
    else:
        icon = "fa fa-snowflake-o fa-3x"
        color = "#0000FF;"
        out = False 
    
    
    yelp = yelpapi.YelpAPI(passwords['YELP_API_KEY'])
    
    #Yelp event filter
    response = yelp.search_query(location=request.POST['cname'],
                                 price=request.POST['value'],
                                 outdoor = out,
                                 limit=10)
    
    #Sends the JSON of filtered events to the yelpSearch html page
    return render(request, "weather/yelpSearch.html", {"response":response, "temperature":temperature, "icon":icon, "color":color})
    
    
#weather function that gets info from the weather api and sends it back to the yelp function
#to help filter out events
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
    
    
    #temperature of the target city
    return response['main']['temp']
