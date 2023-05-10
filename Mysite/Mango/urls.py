from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('services', views.services, name = 'services'),
    path('upload', views.uploadImage, name = 'uploadImage'),
    path('BgRemove', views.BgRemove, name = 'Image'),
]