# Generated by Django 4.1.7 on 2023-04-17 18:57

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomFormSubmission",
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
                    "form_data",
                    models.JSONField(
                        encoder=django.core.serializers.json.DjangoJSONEncoder
                    ),
                ),
                (
                    "submit_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="submit time"),
                ),
                ("date", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "form submission",
                "verbose_name_plural": "form submissions",
                "abstract": False,
            },
        ),
    ]