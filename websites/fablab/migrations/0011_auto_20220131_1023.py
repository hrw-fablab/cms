# Generated by Django 3.2.10 on 2022-01-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fablab', '0010_auto_20220128_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='devicepage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='folderpage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='indexcategorypage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='index',
            field=models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='index', max_length=255),
        ),
    ]
