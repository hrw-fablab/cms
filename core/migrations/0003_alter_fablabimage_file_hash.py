# Generated by Django 3.2.12 on 2022-04-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fablabimage',
            name='file_hash',
            field=models.CharField(blank=True, db_index=True, editable=False, max_length=40),
        ),
    ]
