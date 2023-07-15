from ..enums import ImageType

class Images:
    def __init__(self, data: dict):
        self.poster_tall: "Image" = Image.from_list(data.get("poster_tall"))
        self.poster_wide: "Image" = Image.from_list(data.get("poster_wide"))
        self.promo_image: "Image" = Image.from_list(data.get("promo_image"))

class Image:
    def __init__(self, data: dict):
        self.widht: str = data.get("width")
        self.height: int = data.get("height")
        self.url: str = data.get("source")
        self.type: "ImageType" = ImageType(data.get("type"))

    @classmethod
    def from_list(cls, lst):
        return [Image(image) for image in lst]