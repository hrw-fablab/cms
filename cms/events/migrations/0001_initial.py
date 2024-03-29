# Generated by Django 4.1.7 on 2023-05-14 13:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.search.index


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                        blank=True, max_length=60, null=True, verbose_name="Titel"
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
                    models.TextField(
                        blank=True,
                        max_length=280,
                        null=True,
                        verbose_name="Beschreibung",
                    ),
                ),
                ("link", models.URLField(blank=True, null=True, verbose_name="Link")),
                ("link_text", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("none", "none"),
                            ("teach", "Lehre"),
                            ("open", "Offenes Angebot"),
                            ("student", "Schülerkurse"),
                            ("workshop", "Workshop"),
                            ("external", "Extern"),
                            ("internal", "FabLab Event"),
                        ],
                        default="none",
                        max_length=255,
                    ),
                ),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                (
                    "repeat",
                    models.CharField(
                        choices=[("0", "none"), ("1", "weekly")],
                        default="none",
                        max_length=255,
                    ),
                ),
                (
                    "repeatStart",
                    models.DateField(blank=True, null=True, verbose_name="Von"),
                ),
                (
                    "repeatEnd",
                    models.DateField(blank=True, null=True, verbose_name="Bis"),
                ),
            ],
            options={
                "verbose_name": "Termin",
                "verbose_name_plural": "Termine",
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name="Expection",
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
                ("start", models.DateField()),
                ("end", models.DateField()),
                (
                    "link",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_expection",
                        to="events.event",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
