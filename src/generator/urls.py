from django.urls import path

from .views import *

app_name = 'generator'

urlpatterns = [
    path('', SendData.as_view(), name='index')
]