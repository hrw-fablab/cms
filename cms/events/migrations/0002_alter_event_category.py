# Generated by Django 4.1.7 on 2023-03-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.CharField(
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
    ]