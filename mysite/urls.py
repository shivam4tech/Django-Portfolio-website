from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact', views.contact, name="contact"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('door_unlock', views.door_unlock, name="door_unlock"),
    path('index', views.index, name='index'),
    path('aqua_tank', views.aqua_tank, name='aqua_tank'),
]