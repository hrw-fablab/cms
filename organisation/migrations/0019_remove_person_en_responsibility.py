# Generated by Django 3.2.16 on 2022-11-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("organisation", "0018_alter_event_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="en_responsibility",
        ),
    ]
