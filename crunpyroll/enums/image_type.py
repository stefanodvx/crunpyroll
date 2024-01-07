from enum import Enum

class ImageType(Enum):
    """Images type enumeration."""

    POSTER_TALL = "poster_tall"
    "Image is vertical."

    POSTER_WIDE = "poster_wide"
    "Image is horizontal."

    PROMO_IMAGE = "promo_image"
    "Promotional image."

    THUMBNAIL = "thumbnail"
    "Thumbnail used for episodes."