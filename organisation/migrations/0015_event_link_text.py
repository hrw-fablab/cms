# Generated by Django 3.2.13 on 2022-07-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0014_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='link_text',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]