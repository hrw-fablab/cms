from django.db import models


class Device(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    model = models.CharField(max_length=250, null=True, blank=True)
    area = models.CharField(max_length=250, null=True, blank=True)
