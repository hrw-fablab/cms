# Generated by Django 3.2.10 on 2022-01-11 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0007_rename_adress_footer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer',
            old_name='place',
            new_name='city',
        ),
    ]
