from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('person_add/', views.person_add),
    path('person/', views.person),
]
