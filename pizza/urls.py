"""
URL configuration for shpak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('order', views.order, name='order'),
    path('drop_position', views.drop_position, name='drop_position'),
    path('add_to_basket', views.add_to_basket, name='add_to_basket'),
    path('basket/', views.basket, name='basket'),
    path('check/', views.check, name='check'),
    path('parse/', views.parse, name='parse'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.redir_to_index, name='logout'),
    path('registration/', views.Enter.as_view(), name='registration'),
    path('bind_TG/', views.bind_TG, name='bind_TG')
]
