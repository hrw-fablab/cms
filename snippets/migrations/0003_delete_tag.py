# Generated by Django 3.2.10 on 2022-02-06 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20220206_1804'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
