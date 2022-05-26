# Generated by Django 3.2.13 on 2022-05-26 15:31

import abstract.blocks.chooser
import abstract.blocks.spacer
from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('qufablab', '0011_auto_20220519_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False))], label='Überschrift')), ('paragraph', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'ul', 'link', 'document-link', 'image', 'embed']))], label='Absatz')), ('split', wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ul', 'document-link', 'link'], required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('accent', wagtail.blocks.BooleanBlock(required=False))], label='Split')), ('grid', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('accent', wagtail.blocks.BooleanBlock(required=False)), ('cards', wagtail.blocks.StreamBlock([('card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))], label='Karte')), ('person', wagtail.blocks.StructBlock([('person', abstract.blocks.chooser.PersonChooserBlock(required=False))], label='Person'))], label='Grid Elemente'))], label='Grid')), ('grabber', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('newspaper', 'Zeitungslayout mit einem Hauptelement'), ('magazine', 'Zeitungslayout mit zwei Hauptelementen'), ('medium', '3 Element pro Reihe')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('amount', wagtail.blocks.IntegerBlock(default=5)), ('accent', wagtail.blocks.BooleanBlock(required=False)), ('pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock()))], label='Seiten Inhalte')), ('gallery', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('contain', wagtail.blocks.BooleanBlock(help_text='Wenn z.B. von Logos das Seitenverhältnis beibehalten bleiben soll, sodass das Logo nicht abgeschnitten wird.', label='Cointain Aspect Ratio', required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N'), ('tiny', '5 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('accent', wagtail.blocks.BooleanBlock(required=False)), ('cards', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtailmedia.blocks.VideoChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())]))], label='Galerie')), ('blockquote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('cite', wagtail.blocks.CharBlock(required=False))], label='Zitat')), ('spacer', abstract.blocks.spacer.SpacerBlock(label='Spacer')), ('video', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(icon='media', required=False))], label='Video')), ('image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], label='Bild')), ('embed', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('embed', wagtail.embeds.blocks.EmbedBlock(required=False))], label='Website einbetten')), ('card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))], label='Card')), ('person', wagtail.blocks.StructBlock([('person', abstract.blocks.chooser.PersonChooserBlock(required=False))], label='Person')), ('html', wagtail.blocks.StructBlock([('code', wagtail.blocks.RawHTMLBlock(required=False))], label='HTML')), ('banner', wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('illustration', wagtail.blocks.BooleanBlock(required=False))], label='Banner')), ('project', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('members', abstract.blocks.chooser.ProjectChooserBlock(label='Projektmitglieder', required=True)), ('filter', abstract.blocks.chooser.OrganisationChooserBlock(help_text='Filtert die Projektmitglieder durch die ausgewählte Organisation', label='Projektmitglieder Filter', required=False)), ('headings', wagtail.blocks.BooleanBlock(help_text='Trenne Projektrollen durch Überschriften', label='Projektrollen Überschriften', required=False))], label='Projekt Mitglieder')), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(required=False))], label='Tabelle')), ('calendar', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False))], label='Kalendar')), ('call', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.TextBlock(max_length=140, required=False)), ('link_text', wagtail.blocks.CharBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))], label='Call to Action'))], blank=True, use_json_field=None),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False))], label='Überschrift')), ('paragraph', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'ul', 'link', 'document-link', 'image', 'embed']))], label='Absatz')), ('hero', wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(required=False)), ('text', wagtail.blocks.TextBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(icon='media', required=False))], label='Hero')), ('split', wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ul', 'document-link', 'link'], required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('accent', wagtail.blocks.BooleanBlock(required=False))], label='Split')), ('grid', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('accent', wagtail.blocks.BooleanBlock(required=False)), ('cards', wagtail.blocks.StreamBlock([('card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))], label='Karte')), ('person', wagtail.blocks.StructBlock([('person', abstract.blocks.chooser.PersonChooserBlock(required=False))], label='Person'))], label='Grid Elemente'))], label='Grid')), ('grabber', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('newspaper', 'Zeitungslayout mit einem Hauptelement'), ('magazine', 'Zeitungslayout mit zwei Hauptelementen'), ('medium', '3 Element pro Reihe')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('amount', wagtail.blocks.IntegerBlock(default=5)), ('accent', wagtail.blocks.BooleanBlock(required=False)), ('pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock()))], label='Seiten Inhalte')), ('gallery', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('contain', wagtail.blocks.BooleanBlock(help_text='Wenn z.B. von Logos das Seitenverhältnis beibehalten bleiben soll, sodass das Logo nicht abgeschnitten wird.', label='Cointain Aspect Ratio', required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N'), ('tiny', '5 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('accent', wagtail.blocks.BooleanBlock(required=False)), ('cards', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtailmedia.blocks.VideoChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())]))], label='Galerie')), ('blockquote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('cite', wagtail.blocks.CharBlock(required=False))], label='Zitat')), ('spacer', abstract.blocks.spacer.SpacerBlock(label='Spacer')), ('video', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(icon='media', required=False))], label='Video')), ('image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], label='Bild')), ('embed', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('embed', wagtail.embeds.blocks.EmbedBlock(required=False))], label='Website einbetten')), ('card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))], label='Card')), ('person', wagtail.blocks.StructBlock([('person', abstract.blocks.chooser.PersonChooserBlock(required=False))], label='Person')), ('html', wagtail.blocks.StructBlock([('code', wagtail.blocks.RawHTMLBlock(required=False))], label='HTML')), ('banner', wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('illustration', wagtail.blocks.BooleanBlock(required=False))], label='Banner')), ('project', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('layout', wagtail.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('members', abstract.blocks.chooser.ProjectChooserBlock(label='Projektmitglieder', required=True)), ('filter', abstract.blocks.chooser.OrganisationChooserBlock(help_text='Filtert die Projektmitglieder durch die ausgewählte Organisation', label='Projektmitglieder Filter', required=False)), ('headings', wagtail.blocks.BooleanBlock(help_text='Trenne Projektrollen durch Überschriften', label='Projektrollen Überschriften', required=False))], label='Projekt Mitglieder')), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(required=False))], label='Tabelle')), ('calendar', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False))], label='Kalendar')), ('call', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.TextBlock(max_length=140, required=False)), ('link_text', wagtail.blocks.CharBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))], label='Call to Action'))], blank=True, use_json_field=None),
        ),
    ]
