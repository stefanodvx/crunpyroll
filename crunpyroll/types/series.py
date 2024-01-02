from .images import Images
from .content import Content

class Series(Content):
    def __init__(self, data: dict):
        self.id: str = data.get("id")
        self.title: str = data.get("title")
        self.slug: str = data.get("slug_title")
        self.description: str = data.get("description")
        self.season_count: int = data.get("season_count")
        self.episode_count: int = data.get("episode_count")
        self.subtitle_locales: list[str] = data.get("subtitle_locales")
        self.audio_locales: list[str] = data.get("audio_locales")
        self.maturity_ratings: list[str] = data.get("maturity_ratings")
        self.launch_year: str = data.get("series_launch_year")
        self.channel_id: str = data.get("channel_id")
        self.images: "Images" = Images(data.get("images", {}))
        self.is_mature_blocked: bool = data.get("mature_blocked")
        self.is_simulcast: bool = data.get("is_simulcast")
        self.is_subbed: bool = data.get("is_subbed")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.is_mature: bool = data.get("is_mature")

    @classmethod
    def parse(cls, obj: dict):
        data = {}
        if "data" in obj:
            if isinstance(obj["data"], list):
                data.update(obj["data"][0])
            else:
                data.update(obj["data"])
        else:
            data.update(obj)
        if "series_metadata" in obj:
            data.update(obj["series_metadata"])
        return cls(data)