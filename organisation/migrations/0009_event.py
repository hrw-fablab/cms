# Generated by Django 3.2.13 on 2022-05-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organisation", "0008_auto_20220421_2329"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Titel"
                    ),
                ),
                (
                    "adress",
                    models.CharField(
                        blank=True, max_length=60, null=True, verbose_name="Adresse"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=240,
                        null=True,
                        verbose_name="Beschreibung",
                    ),
                ),
                ("link", models.URLField(blank=True, null=True, verbose_name="Link")),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                (
                    "repeat",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Wiederholen"
                    ),
                ),
            ],
            options={
                "verbose_name": "Termin",
                "verbose_name_plural": "Termine",
            },
        ),
    ]
