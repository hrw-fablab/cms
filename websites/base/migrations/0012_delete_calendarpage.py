# Generated by Django 3.2.13 on 2022-04-27 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0007_add_autocreate_fields'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('base', '0011_calendarpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CalendarPage',
        ),
    ]
