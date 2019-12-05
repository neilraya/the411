from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('search/', views.weather, name='city'),
    path('main/', views.main),
    path('yelpSearch/', views.yelp)
]