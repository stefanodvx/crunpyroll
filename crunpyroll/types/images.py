from ..enums import ImageType

from .obj import Object

from typing import List, Dict

class Images(Object):
    """
    Images of a series, episode or movie.

    Parameters:
        poster_tall (List of :obj:`~crunpyroll.types.Image`):
            Images of the content (vertical).

        poster_wide (List of :obj:`~crunpyroll.types.Image`):
            Images of the content (horizontal).

        promo_image (List of :obj:`~crunpyroll.types.Image`):
            Promotional images of the content.

        thumbnail (List of :obj:`~crunpyroll.types.Image`):
            Thumbnails of the content. Mostly used for episodes.
    """
    def __init__(self, data: Dict):
        self.poster_tall: List["Image"] = Image.from_list(data.get("poster_tall"))
        self.poster_wide: List["Image"] = Image.from_list(data.get("poster_wide"))
        self.promo_image: List["Image"] = Image.from_list(data.get("promo_image"))
        self.thumbnail: List["Image"] = Image.from_list(data.get("thumbnail"))

class Image(Object):
    """
    Info about an image.

    Parameters:
        width (``str``):
            Width of the image.

        height (``str``):
            Height of the image.

        url (``str``):
            Direct URL to the image source.

        type (:obj:`~crunpyroll.enums.ImageType`):
            Type of image (tall, wide, promo...)
    """
    def __init__(self, data: Dict):
        self.width: str = data.get("width")
        self.height: int = data.get("height")
        self.url: str = data.get("source")
        self.type: "ImageType" = ImageType(data.get("type"))

    @classmethod
    def from_list(cls, lst: List) -> List:
        if lst:
            return [
                Image(image) for obj
                in lst for image in obj
            ]