# Generated by Django 3.2.10 on 2022-01-31 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qu_fablab', '0014_auto_20220131_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quindexcategorypage',
            old_name='introduction',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='quindexpage',
            old_name='introduction',
            new_name='heading',
        ),
    ]