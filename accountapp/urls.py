from django.urls import path

from accountapp import views

urlpatterns = [
    path('hello_world/', views.hello_world),
    path('hello_world_drf/', views.hello_world_drf),
]
