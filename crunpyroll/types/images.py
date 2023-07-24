from ..enums import ImageType

class Images:
    def __init__(self, data: dict):
        self.poster_tall: "Image" = Image.from_list(data.get("poster_tall"))
        self.poster_wide: "Image" = Image.from_list(data.get("poster_wide"))
        self.promo_image: "Image" = Image.from_list(data.get("promo_image"))

class Image:
    def __init__(self, data: dict):
        self.width: str = data.get("width")
        self.height: int = data.get("height")
        self.url: str = data.get("source")
        self.type: "ImageType" = ImageType(data.get("type"))

    @classmethod
    def from_list(cls, lst):
        if lst:
            return [Image(image[0]) for image in lst]