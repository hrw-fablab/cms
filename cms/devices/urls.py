from django.urls import path
from .views import index, load


urlpatterns = [path("", index, name="index"), path("load", load, name="load")]
