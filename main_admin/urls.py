from django.urls import path
from .views import *

urlpatterns = [
    path('', get_mro, name='get_mro')
]
