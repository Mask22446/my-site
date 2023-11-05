from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('polls/', views.index, name='index'),
    path('polls/details/<slug:slug>', views.details, name='details'),
]