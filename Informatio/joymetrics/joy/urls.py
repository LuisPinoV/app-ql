from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name = 'inicio'),
    path('grafico/', views.graficos_view, name = 'graficos'),
    path('grafico2/', views.Grafico2, name = 'grafico2'),
    path('log/', views.log, name = 'log'),
    path('registro/', views.registro, name = 'registro'),
    path('main/', views.main, name = 'main'),
    path('contacto/', views.contacto, name = 'contacto'),
    path('quienes/', views.quienes, name = 'quienes'),
]