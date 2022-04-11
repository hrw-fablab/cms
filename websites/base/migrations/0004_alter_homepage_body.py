# Generated by Django 3.2.12 on 2022-04-11 17:16

import abstract.blocks.member
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'ul', 'link', 'document-link', 'image', 'embed']))])), ('hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(icon='media', required=False))])), ('split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ul', 'link'], required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('accent', wagtail.core.blocks.BooleanBlock(required=False))])), ('grid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('layout', wagtail.core.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('cards', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False))])), ('person', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('employment', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('since', wagtail.core.blocks.DateBlock(required=False)), ('career', wagtail.core.blocks.CharBlock(required=False)), ('responsibility', wagtail.core.blocks.CharBlock(required=False)), ('expert', wagtail.core.blocks.CharBlock(required=False)), ('projects', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False))]))]))])), ('grabber', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('layout', wagtail.core.blocks.ChoiceBlock(choices=[('news-large', 'Zeitungslayout mit einem Hauptelement'), ('news-medium', 'Zeitungslayout mit zwei Hauptelementen'), ('extrem', '1 Element pro Reihe'), ('large', '2 Elemente pro Reihe'), ('medium', '3 Elemente pro Reihe'), ('small', '4 Elemente pro Reihe')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('amount', wagtail.core.blocks.IntegerBlock(default=5)), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock()))])), ('gallery', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('contain', wagtail.core.blocks.BooleanBlock(help_text='Wenn z.B. von Logos das Seitenverhältnis beibehalten bleiben soll, sodass das Logo nicht abgeschnitten wird.', label='Cointain Aspect Ratio', required=False)), ('layout', wagtail.core.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N'), ('tiny', '5 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('cards', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtailmedia.blocks.VideoChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())]))])), ('blockquote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('cite', wagtail.core.blocks.CharBlock(required=False))])), ('spacer', wagtail.core.blocks.StructBlock([])), ('video', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(icon='media', required=False))])), ('image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('embed', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('embed', wagtail.embeds.blocks.EmbedBlock(required=False))])), ('card', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False))])), ('person', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('employment', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('since', wagtail.core.blocks.DateBlock(required=False)), ('career', wagtail.core.blocks.CharBlock(required=False)), ('responsibility', wagtail.core.blocks.CharBlock(required=False)), ('expert', wagtail.core.blocks.CharBlock(required=False)), ('projects', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False))])), ('html', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.RawHTMLBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('illustration', wagtail.core.blocks.BooleanBlock(required=False))])), ('member', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('member', abstract.blocks.member.ProjectChooserBlock(required=False))]))], blank=True),
        ),
    ]
