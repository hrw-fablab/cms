# Generated by Django 3.2.16 on 2023-02-08 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_member_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="member",
            name="image",
        ),
    ]
