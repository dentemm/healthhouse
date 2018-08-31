from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^expo/$', views.ExpoGallery.as_view(), name='gallery_expo'),
]