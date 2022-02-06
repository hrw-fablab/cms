# Generated by Django 3.2.10 on 2022-02-06 20:01

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPageLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('expire', models.DateField(blank=True, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_links', to='base.collectionpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollectionPagePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_pages', to='base.collectionpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='page',
            name='page',
        ),
        migrations.RemoveField(
            model_name='page',
            name='parent',
        ),
        migrations.AlterField(
            model_name='projectpagelink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_links', to='base.projectpage'),
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
