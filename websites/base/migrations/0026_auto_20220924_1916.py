# Generated by Django 3.2.15 on 2022-09-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0025_auto_20220825_1146"),
    ]

    operations = [
        migrations.AddField(
            model_name="formpage",
            name="response_switch",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="formpage",
            name="response_text",
            field=models.TextField(blank=True, null=True),
        ),
    ]