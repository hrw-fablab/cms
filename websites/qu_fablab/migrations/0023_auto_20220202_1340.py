# Generated by Django 3.2.10 on 2022-02-02 12:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('qu_fablab', '0022_auto_20220202_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('expire', models.DateField(blank=True, null=True)),
                ('parent', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_link', to='qu_fablab.qucollectionpage')),
            ],
        ),
        migrations.RemoveField(
            model_name='linkcollections',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='page',
            name='page',
        ),
        migrations.RemoveField(
            model_name='page',
            name='parent',
        ),
        migrations.DeleteModel(
            name='GrabberCollections',
        ),
        migrations.DeleteModel(
            name='LinkCollections',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
