from django.urls import path
from . import views


urlpatterns = [
    path('register', views.reply, name='reply'),
]
