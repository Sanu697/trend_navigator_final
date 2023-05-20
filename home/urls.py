from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('',index, name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('search/',search,name='search'),
]