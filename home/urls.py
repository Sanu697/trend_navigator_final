from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('search/',search,name='search'),
    path('upload/',upload,name='upload'),
]