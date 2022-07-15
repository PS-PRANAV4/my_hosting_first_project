from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('author',views.authors),
    path('mark/<int:id>',views.mark),
    path('result/<str:name>',views.report),


    ] 