# Generated by Django 3.2.12 on 2022-04-18 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_person_titel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='titel',
            new_name='title',
        ),
    ]