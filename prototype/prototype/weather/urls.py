from django.urls import path

from . import views

#The pathways that sends you from login to the main page, and from main page into the search query
urlpatterns = [
    path('', views.login, name='login'),
    path('search/', views.weather, name='city'),
    path('main/', views.main),
    path('yelpSearch/', views.yelp)
]