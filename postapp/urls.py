from django.urls import  path
from .import views

urlpatterns  = [
    path('index', views.index, name='index'),
    path('post/<int:pk>', views.post, name='post')
]