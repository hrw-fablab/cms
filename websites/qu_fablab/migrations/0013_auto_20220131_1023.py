# Generated by Django 3.2.10 on 2022-01-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qu_fablab', '0012_auto_20220128_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarticlepage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='quflexpage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='qufolderpage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='quhomepage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='quindexcategorypage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='quindexpage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='quprojectpage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
    ]