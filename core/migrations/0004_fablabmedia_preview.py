# Generated by Django 3.2.16 on 2023-02-05 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_fablabimage_file_hash"),
    ]

    operations = [
        migrations.AddField(
            model_name="fablabmedia",
            name="preview",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="core.fablabimage",
            ),
        ),
    ]