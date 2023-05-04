from django.urls import path
from .views import index, load, delete


urlpatterns = [path("", index, name="index"), path("load", load, name="load"), path("delete", delete, name="delete")]
