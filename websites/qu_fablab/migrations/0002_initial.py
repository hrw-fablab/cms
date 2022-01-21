# Generated by Django 3.2.10 on 2022-01-21 15:38

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qu_fablab', '0001_initial'),
        ('snippets', '0001_initial'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quprojectpage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.projectcategory'),
        ),
        migrations.AddField(
            model_name='quprojectpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='quarticlepage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.author'),
        ),
        migrations.AddField(
            model_name='quarticlepage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='quarticlepage',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.tag'),
        ),
        migrations.AddField(
            model_name='projectpagelink',
            name='locale',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
        ),
        migrations.AddField(
            model_name='projectpagelink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_link', to='qu_fablab.quprojectpage'),
        ),
        migrations.AddField(
            model_name='projectauthor',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage'),
        ),
        migrations.AddField(
            model_name='projectauthor',
            name='locale',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
        ),
        migrations.AddField(
            model_name='projectauthor',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to='qu_fablab.quprojectpage'),
        ),
        migrations.AlterUniqueTogether(
            name='projectpagelink',
            unique_together={('translation_key', 'locale')},
        ),
        migrations.AlterUniqueTogether(
            name='projectauthor',
            unique_together={('translation_key', 'locale')},
        ),
    ]