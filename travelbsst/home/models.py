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


class HomePage(Page):
    max_count = 1

    templates = "home/home_page.html"

    georgia_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    ukraine_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    turkey_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    # Banner _________________________
    banner_image1 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image1_colored_text_line1 = models.CharField(max_length=1600, blank=False, null=True)
    image1_text_line1 = models.CharField(max_length=1600, blank=False, null=True)
    image1_colored_text_line2 = models.CharField(max_length=1600, blank=False, null=True)
    image1_text_line2 = models.CharField(max_length=1600, blank=False, null=True)

    banner_image2 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image2_colored_text_line1 = models.CharField(max_length=1600, blank=False, null=True)
    image2_text_line1 = models.CharField(max_length=1600, blank=False, null=True)
    image2_colored_text_line2 = models.CharField(max_length=1600, blank=False, null=True)
    image2_text_line2 = models.CharField(max_length=1600, blank=False, null=True)

    banner_image3 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    image3_colored_text_line1 = models.CharField(max_length=1600, blank=False, null=True)
    image3_text_line1 = models.CharField(max_length=1600, blank=False, null=True)
    image3_colored_text_line2 = models.CharField(max_length=1600, blank=False, null=True)
    image3_text_line2 = models.CharField(max_length=1600, blank=False, null=True)

# Video section ______________________________
    video_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    main_title = models.CharField(max_length=1600, blank=False, null=True)
    main_text = models.CharField(max_length=1600, blank=False, null=True)
    additional_text = models.CharField(max_length=1600, blank=False, null=True)

    partners_section_title = models.CharField(max_length=1600, blank=False, null=True)


# Strem fields

    content = StreamField(
    [
        ("image_and_text", blocks.LeftImageAndTextBlock()),
        ("text_and_image", blocks.RightImageAndTextBlock()),
    ],
    null=True,  
    blank=True,
    )

    partners =  StreamField(
    [
        ("partners", blocks.Partners()),
    ],
    null=True,
    blank=True,
    )

# join us pop up

    pop_up_title = models.CharField(max_length=1600, blank=False, null=True)
    
    countries =  StreamField(
    [
        ("countries", blocks.countries()),
    ],
    null=True,
    blank=True,
    )

    community_name_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    fullname_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    address_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    email_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    organisation_name_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    organisation_address_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    organisation_type_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    organisation_website_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    organisation_email_placeholder = models.CharField(max_length=1600, blank=False, null=True)

    organistaion_describtion_title = models.CharField(max_length=1600, blank=False, null=True)
    community_describtion_title = models.CharField(max_length=1600, blank=False, null=True)
    organistaion_support_describtion_title = models.CharField(max_length=1600, blank=False, null=True)
    organistaion_protect_title = models.CharField(max_length=1600, blank=False, null=True)
    organistaion_culture_describtion_title = models.CharField(max_length=1600, blank=False, null=True)

    boooking_request_title = models.CharField(max_length=1600, blank=False, null=True)
    boooking_request_subtitle = models.CharField(max_length=1600, blank=False, null=True)
    
    organisation_booking_contact_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    organisation_email_address_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    organisation_phone_placeholder = models.CharField(max_length=1600, blank=False, null=True)
    organisation_language_placeholder = models.CharField(max_length=1600, blank=False, null=True)

    finishing_text = models.CharField(max_length=1600, blank=False, null=True)
    select_email_text = models.CharField(max_length=1600, blank=False, null=True)

    
    emails =  StreamField(
    [
        ("emails", blocks.emails()),
    ],
    null=True,
    blank=True,
    )


# fonts and colors
    headings_font_color = models.CharField(max_length=1600, blank=False, null=True)
    headings_font_family = models.CharField(max_length=1600, blank=False, null=True)
    headings_font_size = models.CharField(max_length=1600, blank=False, null=True)
    paragraphs_font_color = models.CharField(max_length=1600, blank=False, null=True)
    paragraphs_font_family = models.CharField(max_length=1600, blank=False, null=True)
    paragraphs_font_size = models.CharField(max_length=1600, blank=False, null=True)

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
                PageChooserPanel('georgia_page'),

                PageChooserPanel('ukraine_page'),

                PageChooserPanel('turkey_page'),

                
            ],
            heading="Link to country",
        ),

        MultiFieldPanel(
            [
                ImageChooserPanel("banner_image1"),
                FieldPanel("image1_colored_text_line1"),
                FieldPanel("image1_text_line1"),
                FieldPanel("image1_colored_text_line2"),
                FieldPanel("image1_text_line2"),
                ImageChooserPanel("banner_image2"),
                FieldPanel("image2_colored_text_line1"),
                FieldPanel("image2_text_line1"),
                FieldPanel("image2_colored_text_line2"),
                FieldPanel("image2_text_line2"),
                ImageChooserPanel("banner_image3"),
                FieldPanel("image3_colored_text_line1"),
                FieldPanel("image3_text_line1"),
                FieldPanel("image3_colored_text_line2"),
                FieldPanel("image3_text_line2"),

            ],
            heading="Slider Images",
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("video_image"),
                FieldPanel("main_title"),
                FieldPanel("main_text"),
                FieldPanel("additional_text"),
                

            ],
            heading="Section with video",
        ),
        StreamFieldPanel("content"),
        

        MultiFieldPanel(
            [
                 FieldPanel("partners_section_title"),
                 StreamFieldPanel("partners"),

            ],
            heading="Partners section",
        ),

        MultiFieldPanel(
            [
                 FieldPanel("pop_up_title"),
                 StreamFieldPanel("countries"),
                 FieldPanel("community_name_placeholder"),
                 FieldPanel("fullname_placeholder"),
                 FieldPanel("address_placeholder"),
                 FieldPanel("email_placeholder"),
                 FieldPanel("organisation_name_placeholder"),
                 FieldPanel("organisation_address_placeholder"),
                 FieldPanel("organisation_type_placeholder"),
                 FieldPanel("organisation_website_placeholder"),
                 FieldPanel("organisation_email_placeholder"),
                 
                 FieldPanel("organistaion_describtion_title"),
                 FieldPanel("community_describtion_title"),
                 FieldPanel("organistaion_support_describtion_title"),
                 FieldPanel("organistaion_protect_title"),
                 FieldPanel("organistaion_culture_describtion_title"),
                 FieldPanel("boooking_request_title"),
                 FieldPanel("boooking_request_subtitle"),
                 FieldPanel("organisation_booking_contact_placeholder"),
                 FieldPanel("organisation_email_address_placeholder"),
                 FieldPanel("organisation_phone_placeholder"),
                 FieldPanel("organisation_language_placeholder"),
                 FieldPanel("finishing_text"),
                 FieldPanel("select_email_text"),
                 StreamFieldPanel("emails"),

            ],
            heading="join us pop up section",
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