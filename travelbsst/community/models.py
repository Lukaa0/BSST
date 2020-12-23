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


class CommunityPage(Page):
    template = "community/community_page.html"

    # link to coutnry
    country_name = models.CharField(max_length=1600, blank=False, 
    null=True)

    country_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    # community name and description
    community_name = models.CharField(max_length=1600, blank=False, null=True)
    community_description = models.CharField(max_length=1600, blank=False, 
    null=True)

    # included services 
    activities_cards_title = models.CharField(max_length=600, blank=False, null=True)
    activities_cards_sub_title = models.CharField(max_length=600, blank=False, null=True)


    activity_cards = StreamField(
    [
        ("activitycard", blocks.ActivityBlock()),
    ],
    null=True,
    blank=True,
    )

    # additional activities section
    additional_activities_title =  models.CharField(max_length=1600, blank=False, 
    null=True)
    additional_activities_sub_title =  models.CharField(max_length=1600, blank=False, 
    null=True)


    additional_activity_cards = StreamField(
    [
        ("additionalactivitycard", blocks.AdditionalActivityBlock()),
    ],
    null=True,
    blank=True,
    )

    # accommodation section

    accommodation_section_title =  models.CharField(max_length=1600, blank=False, 
    null=True)


    accommodation_cards = StreamField(
    [
        ("accommodationcards", blocks.AccommodationBlock()),
    ],
    null=True,
    blank=True,
    )

    # How to get there

    how_to_get_there_title =  models.CharField(max_length=1600, blank=False, 
    null=True)
    how_to_get_there_description = RichTextField()


    # meet the community section

    meet_the_community_title =  models.CharField(max_length=1600, blank=False, 
    null=True)
    meet_the_community_subtitle =  models.CharField(max_length=1600, blank=False, 
    null=True)


    member_cards = StreamField(
    [
        ("memberscards", blocks.MembersBlock()),
    ],
    null=True,
    blank=True,
    )


    # images section
    images_section_title = models.CharField(max_length=1600, blank=False, 
    null=True)
    
    images = StreamField(
    [
        ("images", blocks.ImageBlock()),
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


    # content panels

    content_panels = Page.content_panels + [
          
        MultiFieldPanel(
            [
                FieldPanel("country_name"),
                PageChooserPanel('country_page'),

                
            ],
            heading="Link to country",
        ),

        MultiFieldPanel(
            [
                FieldPanel("community_name"),
                FieldPanel("community_description"),
                

            ],
            heading="community name and description",
        ),

        MultiFieldPanel(
            [
                FieldPanel("activities_cards_title"),
                FieldPanel("activities_cards_sub_title"),
                StreamFieldPanel("activity_cards"),

            ],
            heading="activities section",
        ),

        MultiFieldPanel(
            [
                FieldPanel("additional_activities_title"),
                FieldPanel("additional_activities_sub_title"),
                StreamFieldPanel("additional_activity_cards"),

            ],
            heading="additional activities section",
        ),

        MultiFieldPanel(
            [
                FieldPanel("accommodation_section_title"),
                StreamFieldPanel("accommodation_cards"),
            ],
            heading="accommodations",
        ),

        MultiFieldPanel(
            [
                FieldPanel("how_to_get_there_title"),
                FieldPanel("how_to_get_there_description"),
            ],
            heading="how to get there",
        ),

        MultiFieldPanel(
            [
                FieldPanel("meet_the_community_title"),
                FieldPanel("meet_the_community_subtitle"),
                StreamFieldPanel("member_cards"),
                

            ],
            heading="meet the communnity",
        ),
        
        MultiFieldPanel(
            [
                FieldPanel("images_section_title"),
                StreamFieldPanel("images"),
                

            ],
            heading="images",
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
        verbose_name = "Community Page"