from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='imageclassification'),
    url(r'^classify_images', views.classify_images, name='classify_images'),
]
