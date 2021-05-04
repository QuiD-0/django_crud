from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', app_main, name='app_main'),
    path('foods/', app_menu, name='app_menu'),
    path('foods/<str:food>/', food_detail),
]
