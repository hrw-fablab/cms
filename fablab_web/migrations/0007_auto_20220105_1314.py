# Generated by Django 3.2.10 on 2022-01-05 12:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('fablab_web', '0006_auto_20220105_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.RichTextBlock(features=['h3', 'ul', 'link', 'image', 'embed']))])), ('split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_title', wagtail.core.blocks.CharBlock(required=False))])))])), ('gallery', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(required=False)))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.RichTextBlock(features=['h3', 'ul', 'link', 'image', 'embed']))])), ('hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('video', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_title', wagtail.core.blocks.CharBlock(required=False))])))])), ('articles', wagtail.core.blocks.StructBlock([('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock()))])), ('gallery', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(required=False)))]))]),
        ),
    ]
