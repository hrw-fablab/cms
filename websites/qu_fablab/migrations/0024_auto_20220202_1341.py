# Generated by Django 3.2.10 on 2022-02-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qu_fablab', '0023_auto_20220202_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='link',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
