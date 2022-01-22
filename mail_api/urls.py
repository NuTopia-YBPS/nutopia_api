from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.mail, name='mail'),
    path('reply', views.reply, name='reply'),
    path('test', views.test)
]
