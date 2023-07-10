from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
