# Generated by Django 3.2.13 on 2022-07-04 19:15

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0015_event_link_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='link_text',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Expection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('link', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_expection', to='organisation.event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
