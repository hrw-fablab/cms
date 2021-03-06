# Generated by Django 3.2.13 on 2022-05-19 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organisation", "0009_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="repeatEnd",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="repeatStart",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.CharField(
                blank=True, max_length=140, null=True, verbose_name="Beschreibung"
            ),
        ),
    ]
