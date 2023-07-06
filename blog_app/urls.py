from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
# 
# router = DefaultRouter()
# router.register("blogs", home.as_view(), basename="home")
# 
# urlpatterns = [] +router.urls

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
