# Generated by Django 3.2.12 on 2022-04-11 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0005_alter_member_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='body',
        ),
    ]