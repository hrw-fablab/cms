# Generated by Django 3.2.10 on 2022-02-06 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepage',
            options={'verbose_name': 'Artikel'},
        ),
        migrations.AlterModelOptions(
            name='devicepage',
            options={'verbose_name': 'Gerät'},
        ),
        migrations.AlterModelOptions(
            name='folderpage',
            options={'verbose_name': 'Ordner'},
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Startseite'},
        ),
        migrations.AlterModelOptions(
            name='projectpage',
            options={'verbose_name': 'Projekt'},
        ),
        migrations.AlterModelOptions(
            name='searchpage',
            options={'verbose_name': 'Suche'},
        ),
    ]
