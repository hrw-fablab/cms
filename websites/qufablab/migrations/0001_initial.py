# Generated by Django 3.2.10 on 2022-02-10 14:19

from django.db import migrations, models
import django.db.models.deletion
import wagtail.admin.forms.choosers
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailcache.cache
import wagtailmedia.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='wagtailcore.page')),
                ('index', models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=255)),
                ('og_image_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('og_type', models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='website', max_length=255)),
                ('tw_size', models.CharField(choices=[('summary_large_image', 'summary_large_image'), ('summary', 'summary'), ('player', 'player')], default='summary_large_image', max_length=255)),
                ('og_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage')),
            ],
            options={
                'verbose_name': 'Suche',
                'abstract': False,
            },
            bases=(wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='wagtailcore.page')),
                ('index', models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=255)),
                ('og_image_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('og_type', models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='website', max_length=255)),
                ('tw_size', models.CharField(choices=[('summary_large_image', 'summary_large_image'), ('summary', 'summary'), ('player', 'player')], default='summary_large_image', max_length=255)),
                ('heading', models.CharField(blank=True, max_length=255)),
                ('og_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage')),
            ],
            options={
                'verbose_name': 'Index Seite',
                'abstract': False,
            },
            bases=(wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='wagtailcore.page')),
                ('index', models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=255)),
                ('og_image_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('og_type', models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='website', max_length=255)),
                ('tw_size', models.CharField(choices=[('summary_large_image', 'summary_large_image'), ('summary', 'summary'), ('player', 'player')], default='summary_large_image', max_length=255)),
                ('body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'ul', 'link', 'document-link', 'image', 'embed']))])), ('hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(icon='media', required=False))])), ('split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ul'], required=False)), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(required=False))])), ('grid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('layout', wagtail.core.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('cards', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))], required=False))])), ('person', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.core.blocks.CharBlock(required=False)), ('employment', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('since', wagtail.core.blocks.DateBlock(required=False)), ('career', wagtail.core.blocks.CharBlock(required=False)), ('responsibility', wagtail.core.blocks.CharBlock(required=False)), ('expert', wagtail.core.blocks.CharBlock(required=False)), ('projects', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False))]))]))])), ('grabber', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock()))])), ('gallery', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('contain', wagtail.core.blocks.BooleanBlock(help_text='Wenn z.B. von Logos das Seitenverhältnis beibehalten bleiben soll, sodass das Logo nicht abgeschnitten wird.', label='Cointain Aspect Ratio', required=False)), ('cards', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtailmedia.blocks.VideoChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())]))])), ('blockquote', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('cite', wagtail.core.blocks.CharBlock(required=False))])), ('spacer', wagtail.core.blocks.StructBlock([])), ('video', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(icon='media', required=False))])), ('image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('embed', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('embed', wagtail.embeds.blocks.EmbedBlock(required=False))])), ('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))], required=False))])), ('person', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.core.blocks.CharBlock(required=False)), ('employment', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('since', wagtail.core.blocks.DateBlock(required=False)), ('career', wagtail.core.blocks.CharBlock(required=False)), ('responsibility', wagtail.core.blocks.CharBlock(required=False)), ('expert', wagtail.core.blocks.CharBlock(required=False)), ('projects', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False))])), ('html', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.RawHTMLBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], blank=True)),
                ('og_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage')),
            ],
            options={
                'verbose_name': 'QuFabLab Startseite',
            },
            bases=(wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='FolderPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='wagtailcore.page')),
                ('index', models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=255)),
                ('og_image_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('og_type', models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='website', max_length=255)),
                ('tw_size', models.CharField(choices=[('summary_large_image', 'summary_large_image'), ('summary', 'summary'), ('player', 'player')], default='summary_large_image', max_length=255)),
                ('og_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage')),
            ],
            options={
                'verbose_name': 'Ordner',
                'abstract': False,
            },
            bases=(wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='wagtailcore.page')),
                ('index', models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=255)),
                ('og_image_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('og_type', models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='website', max_length=255)),
                ('tw_size', models.CharField(choices=[('summary_large_image', 'summary_large_image'), ('summary', 'summary'), ('player', 'player')], default='summary_large_image', max_length=255)),
                ('body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False))])), ('paragraph', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'ul', 'link', 'document-link', 'image', 'embed']))])), ('blockquote', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('cite', wagtail.core.blocks.CharBlock(required=False))])), ('split', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ul'], required=False)), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(required=False))])), ('grid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('layout', wagtail.core.blocks.ChoiceBlock(choices=[('extrem', '1 x N'), ('large', '2 x N'), ('medium', '3 x N'), ('small', '4 x N')], help_text='Die Anzahl an Elementen in einer Horizontalen Reihe')), ('cards', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))], required=False))])), ('person', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.core.blocks.CharBlock(required=False)), ('employment', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('since', wagtail.core.blocks.DateBlock(required=False)), ('career', wagtail.core.blocks.CharBlock(required=False)), ('responsibility', wagtail.core.blocks.CharBlock(required=False)), ('expert', wagtail.core.blocks.CharBlock(required=False)), ('projects', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False))]))]))])), ('grabber', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock()))])), ('spacer', wagtail.core.blocks.StructBlock([])), ('gallery', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('contain', wagtail.core.blocks.BooleanBlock(help_text='Wenn z.B. von Logos das Seitenverhältnis beibehalten bleiben soll, sodass das Logo nicht abgeschnitten wird.', label='Cointain Aspect Ratio', required=False)), ('cards', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtailmedia.blocks.VideoChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())]))])), ('video', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(icon='media', required=False))])), ('image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('embed', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('embed', wagtail.embeds.blocks.EmbedBlock(required=False))])), ('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))], required=False))])), ('person', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('name', wagtail.core.blocks.CharBlock(required=False)), ('employment', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('since', wagtail.core.blocks.DateBlock(required=False)), ('career', wagtail.core.blocks.CharBlock(required=False)), ('responsibility', wagtail.core.blocks.CharBlock(required=False)), ('expert', wagtail.core.blocks.CharBlock(required=False)), ('projects', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False))])), ('html', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.RawHTMLBlock(required=False))])), ('banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], blank=True)),
                ('og_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage')),
            ],
            options={
                'verbose_name': 'Flexible Seite',
                'abstract': False,
            },
            bases=(wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='wagtailcore.page')),
                ('index', models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=255)),
                ('og_image_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('og_type', models.CharField(choices=[('website', 'website'), ('article', 'article'), ('profile', 'profile')], default='website', max_length=255)),
                ('tw_size', models.CharField(choices=[('summary_large_image', 'summary_large_image'), ('summary', 'summary'), ('player', 'player')], default='summary_large_image', max_length=255)),
                ('date', models.DateField()),
                ('introduction', models.CharField(max_length=150)),
                ('body', wagtail.core.fields.RichTextField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.author')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage')),
                ('og_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.fablabimage')),
            ],
            options={
                'verbose_name': 'Artikel',
                'abstract': False,
            },
            bases=(wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page'),
        ),
    ]
