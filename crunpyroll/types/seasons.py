from .obj import Object
from .content import Content

from typing import List, Dict

class SeasonsQuery(Object):
    def __init__(self, data: Dict):
        self.total: int = data.get("total")
        self.items: List["Season"] = data.get("items")

    @classmethod
    def parse(cls, obj: Dict):
        data = {}
        data["total"] = obj["total"]
        data["items"] = [
            Season.parse(item)
            for item in obj["data"]
        ]
        return cls(data)

class Season(Content):
    def __init__(self, data: Dict):
        self.id: str = data.get("id")
        self.title: str = data.get("title")
        self.slug: str = data.get("slug_title")
        self.description: str = data.get("description")
        self.season_number: int = data.get("season_number")
        self.episode_count: int = data.get("number_of_episodes")
        self.series_id: str = data.get("series_id")
        self.series_slug: str = data.get("series_slug_title")
        self.subtitle_locales: List[str] = data.get("subtitle_locales")
        self.audio_locales: List[str] = data.get("audio_locales")
        self.maturity_ratings: List[str] = data.get("maturity_ratings")
        self.channel_id: str = data.get("channel_id")
        self.is_mature_blocked: bool = data.get("mature_blocked")
        self.is_simulcast: bool = data.get("is_simulcast")
        self.is_subbed: bool = data.get("is_subbed")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.is_mature: bool = data.get("is_mature")

    @classmethod
    def parse(cls, obj: Dict):
        data = {}
        data.update(obj)
        if "season_metadata" in obj:
            data.update(obj["season_metadata"])
        return cls(data)