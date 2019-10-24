from django.shortcuts import render

def weather(request):
    import requests

    url = "http://samples.openweathermap.org/data/2.5/weather"

    querystring = {"q":request,"appid":"b6907d289e10d714a6e88b30761fae22"}

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

    response = requests.request("GET", url, headers=headers, params=querystring)

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    return render(request, 'index.html', context)
    