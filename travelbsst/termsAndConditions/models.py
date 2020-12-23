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


class TermsAndConditionPage(Page):

    templates = "termsAndConditions/terms_and_conditions_page.html"
    

    main_title = models.CharField(max_length=1600, blank=False, 
    null=True)
    general_text = RichTextField()
    
    sectionA_main_title = models.CharField(max_length=1600, blank=False, 
    null=True)
    sectionA_general_text = RichTextField()

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
                FieldPanel("main_title"),
                FieldPanel("general_text"),
                
            ],
            heading="section I",
        ),
        MultiFieldPanel(
            [
                FieldPanel("sectionA_main_title"),
                FieldPanel("sectionA_general_text"),
                
            ],
            heading="section II",
        ),
        
        MultiFieldPanel(
            [
                 StreamFieldPanel("social_media_links"),

            ],
            heading="Social Media",
        ),

    ]

    class Meta:
        verbose_name = "Terms and Conditions Page"