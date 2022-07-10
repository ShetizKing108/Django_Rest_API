from django.urls import path

from . import views # from .views import api_home

urlpatterns = [
    path('', views.api_home)       # '' means empty path. The address here will be 127.0.0:8000/api
]