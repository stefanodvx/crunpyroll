from .obj import Object
from .content import Content
from .images import Images

from ..utils import str_to_date

from datetime import datetime
from typing import List, Dict

class EpisodesQuery(Object):
    def __init__(self, data: Dict):
        self.total: int = data.get("total")
        self.items: List["Episode"] = data.get("items")

    @classmethod
    def parse(cls, obj: Dict):
        data = {}
        data["total"] = obj["total"]
        data["items"] = [
            Episode.parse(item)
            for item in obj["data"]
        ]
        return cls(data)

class Episode(Content):
    def __init__(self, data: Dict):
        self.id: str = data.get("id")
        self.title: str = data.get("title")
        self.slug: str = data.get("slug_title")
        self.episode_number: int = data.get("episode_number")
        self.duration: int = data.get("duration_ms")
        self.free_available_date: datetime = str_to_date(data.get("free_available_date"))
        self.premium_available_date: datetime = str_to_date(data.get("premium_available_date"))
        self.air_date: datetime = str_to_date(data.get("episode_air_date"))
        self.upload_date: datetime = str_to_date(data.get("upload_date"))
        self.description: str = data.get("description")
        self.next_episode_title: str = data.get("next_episode_title")
        self.next_episode_id: str = data.get("next_episode_id")
        self.season_id: str = data.get("season_id")
        self.season_title: str = data.get("season_title")
        self.season_number: int = data.get("season_number")
        self.season_slug_title: str = data.get("season_slug_title")
        self.series_id: str = data.get("series_id")
        self.series_slug: str = data.get("series_slug_title")
        self.subtitle_locales: List[str] = data.get("subtitle_locales")
        self.audio_locales: str = data.get("audio_locale")
        self.maturity_ratings: List[str] = data.get("maturity_ratings")
        self.channel_id: str = data.get("channel_id")
        self.images: "Images" = Images(data.get("images", {}))
        self.has_closed_captions: bool = data.get("closed_captions_available")
        self.is_available_offline: bool = data.get("available_offline")
        self.is_hd: bool = data.get("hd_flag")
        self.is_premium: bool = data.get("is_premium_only")
        self.is_mature_blocked: bool = data.get("mature_blocked")
        self.is_simulcast: bool = data.get("is_simulcast")
        self.is_subbed: bool = data.get("is_subbed")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.is_mature: bool = data.get("is_mature")
    
    @classmethod
    def parse(cls, obj: Dict):
        data = {}
        data.update(obj)
        if "episode_metadata" in obj:
            data.update(obj["episode_metadata"])
        return cls(data)