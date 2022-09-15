# Generated by Django 3.2.15 on 2022-08-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_formfield_field_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionpagelink',
            name='category',
            field=models.CharField(choices=[('none', 'none'), ('teach', 'Lehre'), ('open', 'Offenes Angebot'), ('school', 'Schülerkurse'), ('workshop', 'Workshop'), ('extern', 'Extern'), ('event', 'FabLab Event')], default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='projectpagelink',
            name='category',
            field=models.CharField(choices=[('none', 'none'), ('teach', 'Lehre'), ('open', 'Offenes Angebot'), ('school', 'Schülerkurse'), ('workshop', 'Workshop'), ('extern', 'Extern'), ('event', 'FabLab Event')], default='none', max_length=255),
        ),
    ]