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

class FlexPage(Page):
    template = "flex/flex_page.html"

# banner _________________________
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )    

    image_colored_text_word1 = models.CharField(max_length=600, blank=False, null=True)
    image_text_word1 = models.CharField(max_length=600, blank=False, null=True)
    image_colored_text_word2 = models.CharField(max_length=600, blank=False, null=True)
    image_text_word2 = models.CharField(max_length=600, blank=False, null=True)


# country name and description____________
    country_name = models.CharField(max_length=600, blank=False, null=True)
    country_description = models.CharField(max_length=1600, blank=False, null=True)

    # cards _______________

    cards = StreamField(
    [
        ("card", blocks.CardBlock()),
    ],
    null=True,
    blank=True,
    )

    # map section
    center_lat = models.CharField(max_length=600, blank=False, null=True)
    center_lng = models.CharField(max_length=600, blank=False, null=True)

    markers = StreamField(
    [
        ("marker", blocks.CommunityMarker()),
    ],
    null=True,
    blank=True,
    )

    # service description _____________________

    service_info_title = models.CharField(max_length=600, blank=False, null=True)
    service_info = models.CharField(max_length=600, blank=False, null=True)

# images section ____________________
    images_section_title = models.CharField(max_length=600, blank=False, null=True)

    images = StreamField(
    [
        ("card", blocks.ImageBlock()),
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


#social media links

    social_media_links =  StreamField(
    [
        ("SocialMedia", blocks.SocialMedia()),
    ],
    null=True,
    blank=True,
    )



# content panels _______________
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("banner_image"),
                FieldPanel("image_colored_text_word1"),
                FieldPanel("image_text_word1"),
                FieldPanel("image_colored_text_word2"),
                FieldPanel("image_text_word2"),
                

            ],
            heading="banner",
        ),
        MultiFieldPanel(
            [
                FieldPanel("country_name"),
                FieldPanel("country_description"),
            ],
            heading="country name and description",
        ),

        MultiFieldPanel(
            [
                FieldPanel("center_lat"),
                FieldPanel("center_lng"),
                StreamFieldPanel("markers"),
            ],
            heading="map",
        ),
        StreamFieldPanel("cards"),

        MultiFieldPanel(
            [
                FieldPanel("service_info_title"),
                FieldPanel("service_info"),
            ],
            heading="service description",
        ),
        MultiFieldPanel(
            [
                FieldPanel("images_section_title"),
                StreamFieldPanel("images"),
            ],
            heading="images section",
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

# Meta class ____________
    class Meta:
        verbose_name = "Country Page"