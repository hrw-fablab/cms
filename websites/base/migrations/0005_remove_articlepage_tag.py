# Generated by Django 3.2.10 on 2022-02-06 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220206_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='tag',
        ),
    ]
