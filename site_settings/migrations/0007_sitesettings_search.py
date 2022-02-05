# Generated by Django 3.2.10 on 2022-02-05 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('site_settings', '0006_sponsor_logo_alt_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='search',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
    ]
