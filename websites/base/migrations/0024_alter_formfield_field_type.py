# Generated by Django 3.2.14 on 2022-07-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0023_formpage_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formfield",
            name="field_type",
            field=models.CharField(
                choices=[
                    ("singleline", "Single line text"),
                    ("multiline", "Multi-line text"),
                    ("email", "Email"),
                    ("number", "Number"),
                    ("url", "URL"),
                    ("checkbox", "Checkbox"),
                    ("checkboxes", "Checkboxes"),
                    ("dropdown", "Drop down"),
                    ("multiselect", "Multiple select"),
                    ("radio", "Radio buttons"),
                    ("date", "Date"),
                    ("datetime", "Date/time"),
                    ("hidden", "Hidden field"),
                    ("pageParam", "Page Parameter"),
                ],
                max_length=16,
                verbose_name="field type",
            ),
        ),
    ]
