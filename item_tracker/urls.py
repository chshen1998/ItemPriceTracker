from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="tracker-home"),
    path('recommendations/', views.recommendations, name="tracker-recommendations"),
]