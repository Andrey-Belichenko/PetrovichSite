from django.urls import path
from SiteApp import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
]
