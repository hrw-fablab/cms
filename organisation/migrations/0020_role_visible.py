# Generated by Django 3.2.16 on 2022-11-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organisation", "0019_remove_person_en_responsibility"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="visible",
            field=models.BooleanField(default=True),
        ),
    ]
