from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('polls/', views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
]