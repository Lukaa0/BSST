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


class AccommodationPage(Page):
    template = "accommodation/accommodation_page.html"

    # link to commuity
    community_name = models.CharField(max_length=1600, blank=False, 
    null=True)
  
    community_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    # images section _____________
    images_section_title = models.CharField(max_length=1600, blank=False, 
    null=True)
    images_section_subtitle = models.CharField(max_length=1600, blank=False, 
    null=True)
    
    images = StreamField(
    [
        ("images", blocks.ImgsBlock()),
    ],
    null=True,
    blank=True,
    )

    # booking form ____________


    booking_form_title = models.CharField(max_length=1600, blank=False, 
    null=True)

    breakfast_price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)

    flat_fees = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)
    
    per_person_charges = models.DecimalField(max_digits=5, decimal_places=2,blank=False, null=True)

    administration_charge = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)

    

    administration_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)

    community_fund = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)

    room_types_available = models.BooleanField(default=True)

    room_options = StreamField(
    [
        ("RoomOptions", blocks.RoomOptions()),
    ],
    null=True,
    blank=True,
    )

    room_option_prices = StreamField(
    [
        ("RoomOptionPrices", blocks.RoomOptionPrices()),
    ],
    null=True,
    blank=True,
    )


   


    # amenities section _____________
    amenities_section_title = models.CharField(max_length=1600, blank=False, 
    null=True)


    amenities = StreamField(
    [
        ("amenities", blocks.AmenityBlock()),
    ],
    null=True,
    blank=True,
    )

    # accommodation description
    description_title = models.CharField(max_length=1600, blank=False, 
    null=True)
    description_text = models.CharField(max_length=1600, blank=False, 
    null=True)

    # included services
    included_services_title = models.CharField(max_length=1600, blank=False, 
    null=True)
    included_services_subtitle = models.CharField(max_length=1600, blank=False, 
    null=True)

    l1 = models.CharField(max_length=1600, blank=False, 
    null=True)
    l2 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l3 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l4 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l5 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l6 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l7 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l8 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l9 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l10 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l11 = models.CharField(max_length=1600, blank=True, 
    null=True)
    l12 = models.CharField(max_length=1600, blank=True, 
    null=True)


    tour_content_change_warning =  models.CharField(max_length=1600, blank=False, 
    null=True)

    # not included services
    not_included_services_title = models.CharField(max_length=1600, blank=False, 
    null=True)

    ll1 = models.CharField(max_length=1600, blank=False, 
    null=True)
    ll2 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll3 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll4 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll5 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll6 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll7 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll8 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll9 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll10 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll11 = models.CharField(max_length=1600, blank=True, 
    null=True)
    ll12 = models.CharField(max_length=1600, blank=True, 
    null=True)

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
    # conten panels __________
    content_panels = Page.content_panels + [
        
        MultiFieldPanel(
            [
                FieldPanel("community_name"),
                PageChooserPanel('community_page'),

                
            ],
            heading="Link to community",
        ),
        MultiFieldPanel(
            [
                FieldPanel("images_section_title"),
                FieldPanel("images_section_subtitle"),
                StreamFieldPanel("images"),
            ],
            heading="images section",
        ),

        MultiFieldPanel(
            [
                FieldPanel("booking_form_title"),
                FieldPanel("breakfast_price"),
                FieldPanel("flat_fees"),
                FieldPanel("per_person_charges"),
                FieldPanel("administration_charge"),
                FieldPanel("administration_fee"),
                FieldPanel("community_fund"),
                FieldPanel("room_types_available"),
                StreamFieldPanel("room_options"),
                StreamFieldPanel("room_option_prices"),
            ],
            heading="booking form",
        ),


        MultiFieldPanel(
            [
                FieldPanel("amenities_section_title"),
                StreamFieldPanel("amenities"),
            ],
            heading="amenities section",
        ),

        MultiFieldPanel(
            [
                FieldPanel("description_title"),
                FieldPanel("description_text"),
            ],
            heading="accommodation description",
        ),

        MultiFieldPanel(
            [
                FieldPanel("included_services_title"),
                FieldPanel("included_services_subtitle"),
                FieldPanel("l1"),
                FieldPanel("l2"),
                FieldPanel("l3"),
                FieldPanel("l4"),
                FieldPanel("l5"),
                FieldPanel("l6"),
                FieldPanel("l7"),
                FieldPanel("l8"),
                FieldPanel("l9"),
                FieldPanel("l10"),
                FieldPanel("l11"),
                FieldPanel("l12"),
            ],
            heading="included services",
        ),

        MultiFieldPanel(
            [
                FieldPanel("tour_content_change_warning"),
                
            ],
            heading="tour content change warning",
        ),

            
        MultiFieldPanel(
            [
                FieldPanel("not_included_services_title"),
                FieldPanel("ll1"),
                FieldPanel("ll2"),
                FieldPanel("ll3"),
                FieldPanel("ll4"),
                FieldPanel("ll5"),
                FieldPanel("ll6"),
                FieldPanel("ll7"),
                FieldPanel("ll8"),
                FieldPanel("ll9"),
                FieldPanel("ll10"),
                FieldPanel("ll11"),
                FieldPanel("ll12"),
            ],
            heading="not included services",
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
        verbose_name = "Accomodation Page"