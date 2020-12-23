from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock

# home page 
class LeftImageAndTextBlock(blocks.StructBlock):

    image = ImageChooserBlock()
    header_text = blocks.TextBlock(required=True, help_text="text to the right")
    main_text = blocks.TextBlock(required=True, help_text="text to the right")
    additional_text = blocks.TextBlock(required=True)

    class Meta:  # noqa
        template = "streams/leftImage_and_text_block.html"
        icon = "edit"
        label = "Image & Text"

class RightImageAndTextBlock(blocks.StructBlock):

    image = ImageChooserBlock()
    header_text = blocks.TextBlock(required=True)
    main_text = blocks.TextBlock(required=True)
    additional_text = blocks.TextBlock(required=True)

    class Meta:  # noqa
        template = "streams/rightImage_and_text_block.html"
        icon = "edit"
        label = "Text & Image"


class Partners(blocks.StructBlock):

    image = ImageChooserBlock()
    button_url = blocks.URLBlock(required=False)


    class Meta:  # noqa
        template = "streams/partners.html"
        icon = "placeholder"
        label = "Text & Image"

class countries(blocks.StructBlock):

    country_name = blocks.TextBlock(required=True)

    class Meta:  # noqa
        template = "streams/countries.html"
        icon = "placeholder"
        label = "country"


class emails(blocks.StructBlock):

    country = blocks.TextBlock(required=True)
    email =  blocks.TextBlock(required=True)
    class Meta:  # noqa
        template = "streams/emails.html"
        icon = "placeholder"
        label = "email"



class SocialMedia(blocks.StructBlock):

    icon = blocks.TextBlock(required=True)
    social_media_url = blocks.URLBlock(required=False)


    class Meta:  # noqa
        template = "streams/socialMedia.html"
        icon = "placeholder"
        label = "icon & link"

# flex page

class CommunityMarker(blocks.StructBlock):
    
    community_name = blocks.TextBlock(required=True)
    community_link = blocks.PageChooserBlock(required=False)
    Latitude = blocks.TextBlock(required=True)
    Longitude = blocks.TextBlock(required=True)
    
    class Meta:  # noqa
        template = "streams/community_marker_block.html"
        icon = "placeholder"
        label = "community markers"

class CardBlock(blocks.StructBlock):
    
    page_link = blocks.PageChooserBlock(required=False)
    price_text = blocks.TextBlock(required=True)
    community_name = blocks.TextBlock(required=True)
    community_description = blocks.TextBlock(required=True)
    image = ImageChooserBlock()
    
    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Community Cards"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    class Meta:  # noqa
        template = "streams/image_block.html"
        icon = "image"
        label = "Image"

# community page

class ActivityBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.TextBlock(required=True)
    l1 = blocks.TextBlock(required=True)
    l2 = blocks.TextBlock(required=False)
    l3 = blocks.TextBlock(required=False)
    l4 = blocks.TextBlock(required=False)
    
    class Meta:  # noqa
        template = "streams/activity_block.html"
        icon = "placeholder"
        label = "Activity Cards"

class AdditionalActivityBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    image = ImageChooserBlock()
    activity_description = blocks.TextBlock(required=True)
    availability = blocks.TextBlock(required=True)
    group_size = blocks.TextBlock(required=True)
    price_per_person = blocks.TextBlock(required=True)

    
    class Meta:  # noqa
        template = "streams/additional_activity_block.html"
        icon = "placeholder"
        label = "Additional Activity Cards"


class AccommodationBlock(blocks.StructBlock):

    image = ImageChooserBlock()

    page_link = blocks.PageChooserBlock(required=False)

    accommodation_name = blocks.TextBlock(required=True)
    accommodation_price = blocks.TextBlock(required=True)

    attribute1_title = blocks.TextBlock(required=True)
    attribute1_text = blocks.TextBlock(required=True)
    attribute2_title = blocks.TextBlock(required=True)
    attribute2_text = blocks.TextBlock(required=True)
    attribute3_title = blocks.TextBlock(required=True)
    attribute3_text = blocks.TextBlock(required=True)
    
    class Meta:  # noqa
        template = "streams/accommodation_block.html"
        icon = "placeholder"
        label = "Accommodation Cards"
        

class RoomOptionPrices(blocks.StructBlock):

    price = blocks.TextBlock(required=True)
    

    class Meta:  # noqa
        template = "streams/room_option_prices.html"
        icon = "edit"
        label = "Room Prices"

class RoomOptions(blocks.StructBlock):

    room_option = blocks.TextBlock(required=True)
    

    class Meta:  # noqa
        template = "streams/room_options.html"
        icon = "edit"
        label = "Room Options"

class MembersBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    name = blocks.TextBlock(required=True)
    surname = blocks.TextBlock(required=True)
    person_info = blocks.TextBlock(required=True)

    class Meta:  # noqa
        template = "streams/members_block.html"
        icon = "placeholder"
        label = "Community Member Cards"

# accommodation page ________________
class AmenityBlock(blocks.StructBlock):
    icon_class = blocks.TextBlock(required=True)
    icon_name = blocks.TextBlock(required=True)

    class Meta:  # noqa
        template = "streams/amenity_block.html"
        icon = "tick-inverse"
        label = "Amenity Cards"


class ImgsBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    class Meta:  # noqa
        template = "streams/img_block.html"
        icon = "image"
        label = "Image"

# about us page

class aboutUsBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    description = blocks.TextBlock(required=True)

    class Meta:  # noqa
        template = "streams/aboutUs_block.html"
        icon = "placeholder"
        label = "Community Member Cards"
