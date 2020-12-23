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


class TermsOfUsePage(Page):

    templates = "termsOfUse/terms_of_use.html"


    sectionI_main_title = models.CharField(max_length=1600, blank=False, 
    null=True)
    sectionI_general_text = RichTextField()
#social media links

    social_media_links =  StreamField(
    [
        ("SocialMedia", blocks.SocialMedia()),
    ],
    null=True,
    blank=True,
    )

    # conten panels __________
    content_panels = Page.content_panels + [
        
        MultiFieldPanel(
            [
                FieldPanel("sectionI_main_title"),
                FieldPanel("sectionI_general_text"),
                
            ],
            heading="section I",
        ),
        MultiFieldPanel(
            [
                 StreamFieldPanel("social_media_links"),

            ],
            heading="Social Media",
        ),
    ]


    class Meta:
        verbose_name = "Terms of Use Page"