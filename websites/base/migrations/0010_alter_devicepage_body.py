# Generated by Django 3.2.13 on 2022-04-24 09:53

import abstract.blocks.chooser
import abstract.blocks.spacer
from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_auto_20220423_1242"),
    ]

    operations = [
        migrations.AlterField(
            model_name="devicepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "heading",
                        wagtail.core.blocks.StructBlock(
                            [("title", wagtail.core.blocks.CharBlock(required=False))],
                            label="Überschrift",
                        ),
                    ),
                    (
                        "paragraph",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "text",
                                    wagtail.core.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "h3",
                                            "ul",
                                            "link",
                                            "document-link",
                                            "image",
                                            "embed",
                                        ]
                                    ),
                                ),
                            ],
                            label="Absatz",
                        ),
                    ),
                    (
                        "split",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                                (
                                    "text",
                                    wagtail.core.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "ul",
                                            "document-link",
                                            "link",
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "page",
                                    wagtail.core.blocks.PageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "accent",
                                    wagtail.core.blocks.BooleanBlock(required=False),
                                ),
                            ],
                            label="Split",
                        ),
                    ),
                    (
                        "grid",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "layout",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("extrem", "1 x N"),
                                            ("large", "2 x N"),
                                            ("medium", "3 x N"),
                                            ("small", "4 x N"),
                                        ],
                                        help_text="Die Anzahl an Elementen in einer Horizontalen Reihe",
                                    ),
                                ),
                                (
                                    "cards",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            (
                                                "card",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.core.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "text",
                                                            wagtail.core.blocks.TextBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "page",
                                                            wagtail.core.blocks.PageChooserBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                    ],
                                                    label="Karte",
                                                ),
                                            ),
                                            (
                                                "person",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "person",
                                                            abstract.blocks.chooser.PersonChooserBlock(
                                                                required=False
                                                            ),
                                                        )
                                                    ],
                                                    label="Person",
                                                ),
                                            ),
                                        ],
                                        label="Grid Elemente",
                                    ),
                                ),
                            ],
                            label="Grid",
                        ),
                    ),
                    (
                        "gallery",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "contain",
                                    wagtail.core.blocks.BooleanBlock(
                                        help_text="Wenn z.B. von Logos das Seitenverhältnis beibehalten bleiben soll, sodass das Logo nicht abgeschnitten wird.",
                                        label="Cointain Aspect Ratio",
                                        required=False,
                                    ),
                                ),
                                (
                                    "layout",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("extrem", "1 x N"),
                                            ("large", "2 x N"),
                                            ("medium", "3 x N"),
                                            ("small", "4 x N"),
                                            ("tiny", "5 x N"),
                                        ],
                                        help_text="Die Anzahl an Elementen in einer Horizontalen Reihe",
                                    ),
                                ),
                                (
                                    "cards",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(),
                                            ),
                                            (
                                                "video",
                                                wagtailmedia.blocks.VideoChooserBlock(),
                                            ),
                                            (
                                                "embed",
                                                wagtail.embeds.blocks.EmbedBlock(),
                                            ),
                                        ]
                                    ),
                                ),
                            ],
                            label="Galerie",
                        ),
                    ),
                    ("spacer", abstract.blocks.spacer.SpacerBlock(label="Spacer")),
                    (
                        "video",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "video",
                                    wagtailmedia.blocks.VideoChooserBlock(
                                        icon="media", required=False
                                    ),
                                ),
                            ],
                            label="Video",
                        ),
                    ),
                    (
                        "image",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                            ],
                            label="Bild",
                        ),
                    ),
                    (
                        "embed",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "embed",
                                    wagtail.embeds.blocks.EmbedBlock(required=False),
                                ),
                            ],
                            label="Website einbetten",
                        ),
                    ),
                    (
                        "html",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "code",
                                    wagtail.core.blocks.RawHTMLBlock(required=False),
                                )
                            ],
                            label="HTML",
                        ),
                    ),
                    (
                        "table",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "table",
                                    wagtail.contrib.table_block.blocks.TableBlock(
                                        required=False
                                    ),
                                )
                            ],
                            label="Tabelle",
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
    ]
