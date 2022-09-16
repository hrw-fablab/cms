from django.urls import path
from devices.views import index


urlpatterns = [path("", index, name="index")]
