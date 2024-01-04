from .content import Content
from .images import Images

from ..utils import str_to_date

from typing import List, Dict
from datetime import datetime
    
class Movie(Content):
    def __init__(self, data: Dict):
        self.id: str = data.get("id")
        self.title: str = data.get("title")
        self.slug: str = data.get("slug_title")
        self.duration: int = data.get("duration_ms")
        self.free_available_date: datetime = str_to_date(data.get("free_available_date"))
        self.premium_available_date: datetime = str_to_date(data.get("premium_available_date"))
        self.release_year: int = data.get("movie_release_year")
        self.description: str = data.get("description")
        self.first_movie_id: str = data.get("first_movie_id")
        self.subtitle_locales: List[str] = data.get("subtitle_locales")
        self.audio_locales: str = data.get("audio_locale")
        self.maturity_ratings: List[str] = data.get("maturity_ratings")
        self.channel_id: str = data.get("channel_id")
        self.images: "Images" = Images(data.get("images"))
        self.has_closed_captions: bool = data.get("closed_captions_available")
        self.is_available_offline: bool = data.get("available_offline")
        self.is_hd: bool = data.get("hd_flag")
        self.is_new: bool = data.get("new")
        self.is_premium: bool = data.get("is_premium_only")
        self.is_mature_blocked: bool = data.get("mature_blocked")
        self.is_subbed: bool = data.get("is_subbed")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.is_mature: bool = data.get("is_mature")
    
    @classmethod
    def parse(cls, obj: Dict):
        data = {}
        if "data" in obj:
            if isinstance(obj["data"], List):
                data.update(obj["data"][0])
            else:
                data.update(obj["data"])
        else:
            data.update(obj)
        if "movie_listing_metadata" in obj:
            data.update(obj["movie_listing_metadata"])
        return cls(data)