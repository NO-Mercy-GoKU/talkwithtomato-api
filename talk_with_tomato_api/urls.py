from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('reply/', views.reply, name='Reply'),
]
