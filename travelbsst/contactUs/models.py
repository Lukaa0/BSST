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


class ContactUsPage(Page):
    templates = "contactUs/contact_us_page.html"


    page_title = models.CharField(max_length=1600, blank=False, null=True)
    sub_title = models.CharField(max_length=1600, blank=False, null=True)


    # fonts and colors
    headings_font_color = models.CharField(max_length=600, blank=False, null=True)
    headings_font_family = models.CharField(max_length=600, blank=False, null=True)
    headings_font_size = models.CharField(max_length=600, blank=False, null=True)
    paragraphs_font_color = models.CharField(max_length=600, blank=False, null=True)
    paragraphs_font_family = models.CharField(max_length=600, blank=False, null=True)
    paragraphs_font_size = models.CharField(max_length=600, blank=False, null=True)


#social media links

    social_media_links =  StreamField(
    [
        ("SocialMedia", blocks.SocialMedia()),
    ],
    null=True,
    blank=True,
    )

# content panel
    

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("page_title"),
                FieldPanel("sub_title"),
            ],
            heading="Title",
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
        verbose_name = "contact us Page"