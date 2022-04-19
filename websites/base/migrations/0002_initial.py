# Generated by Django 3.2.12 on 2022-04-18 13:18

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('organisation', '0001_initial'),
        ('core', '0001_initial'),
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='projectpagelink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_links', to='base.projectpage'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organisation.projectcategory'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='folderpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='devicepage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organisation.devicecategory'),
        ),
        migrations.AddField(
            model_name='devicepage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='devicepage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='deviceindexpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='collectionpagepage',
            name='grabber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='collectionpagepage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_pages', to='base.collectionpage'),
        ),
        migrations.AddField(
            model_name='collectionpagelink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_links', to='base.collectionpage'),
        ),
        migrations.AddField(
            model_name='collectionpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organisation.person'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='organisation.organisation'),
        ),
    ]