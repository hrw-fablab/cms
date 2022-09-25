from django.db import models


class Device(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    model = models.CharField(max_length=250, null=True, blank=True)
    area = models.CharField(max_length=250, null=True, blank=True)
    manufacturer = models.CharField(max_length=250, null=True, blank=True)
    image = models.ForeignKey(
        "core.FablabImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
