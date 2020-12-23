from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class aboutUsPage(Page):

    templates = "aboutUs/about_us_page.html"


    # banner
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    banner_title_letter1 = models.CharField(max_length=1600, blank=False, null=True)
    banner_title_text = models.CharField(max_length=1600, blank=False, null=True)


    # who we are section
    who_we_are_title = models.CharField(max_length=1600, blank=False, null=True)
    description = models.CharField(max_length=1600, blank=False, null=True)

    # why are we different section

    we_different_title = models.CharField(max_length=1600, blank=False, null=True)
    we_different_cards = StreamField(
    [
        ("aboutuscard", blocks.aboutUsBlock()),
    ],
    null=True,
    blank=True,
    )
    # community based section

    com_based_title = models.CharField(max_length=1600, blank=False, null=True)
    com_based_cards = StreamField(
    [
        ("aboutuscard", blocks.aboutUsBlock()),
    ],
    null=True,
    blank=True,
    )

    # unique experiences section

    uniq_title = models.CharField(max_length=1600, blank=False, null=True)
    uniq_cards = StreamField(
    [
        ("aboutuscard", blocks.aboutUsBlock()),
    ],
    null=True,
    blank=True,
    )

#social media links

    social_media_links =  StreamField(
    [
        ("SocialMedia", blocks.SocialMedia()),
    ],
    null=True,
    blank=True,
    )

# fonts and colors
    headings_font_color = models.CharField(max_length=600, blank=False, null=True)
    headings_font_family = models.CharField(max_length=600, blank=False, null=True)
    headings_font_size = models.CharField(max_length=600, blank=False, null=True)
    paragraphs_font_color = models.CharField(max_length=600, blank=False, null=True)
    paragraphs_font_family = models.CharField(max_length=600, blank=False, null=True)
    paragraphs_font_size = models.CharField(max_length=600, blank=False, null=True)

    # content panels

    content_panels = Page.content_panels + [

        MultiFieldPanel(
            [                
                ImageChooserPanel("banner_image"),
                FieldPanel("banner_title_letter1"),
                FieldPanel("banner_title_text"),
                

            ],
            heading="banner",
        ),

        MultiFieldPanel(
            [
                FieldPanel("who_we_are_title"),
                FieldPanel("description"),

            ],
            heading="who we are section",
        ),

        MultiFieldPanel(
            [
                FieldPanel("we_different_title"),
                StreamFieldPanel("we_different_cards"),
                

            ],
            heading="why we are different section",
        ),

        MultiFieldPanel(
            [
                FieldPanel("com_based_title"),
                StreamFieldPanel("com_based_cards"),
            ],
            heading="community based section",
        ),

        MultiFieldPanel(
            [
                FieldPanel("uniq_title"),
                StreamFieldPanel("uniq_cards"),
                

            ],
            heading="unique experiences section",
        ),


        MultiFieldPanel(
            [
                 FieldPanel("headings_font_color"),
                 FieldPanel("headings_font_family"),
                 FieldPanel("headings_font_size"),
                 FieldPanel("paragraphs_font_color"),
                 FieldPanel("paragraphs_font_family"),
                 FieldPanel("paragraphs_font_size"),

            ],
            heading="Font size/family/color ",
        ),
        MultiFieldPanel(
            [
                 StreamFieldPanel("social_media_links"),

            ],
            heading="Social Media",
        ),
    ]
    
    class Meta:
        verbose_name = "about us Page"
