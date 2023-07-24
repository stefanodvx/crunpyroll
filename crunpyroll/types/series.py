from .images import Images

class Series:
    def __init__(self, data: dict):
        self.is_mature: bool = data.get("is_mature")
        self.seo_title: str = data.get("seo_title")
        self.availability_notes: str = data.get("availability_notes")
        self.audio_locales: list[str] = data.get("audio_locales")
        self.content_provider: str = data.get("content_provider")
        self.season_count: int = data.get("season_count")
        self.id: str = data.get("id")
        self.title: str = data.get("title")
        self.slug_title: str = data.get("slug_title")
        self.media_count: int = data.get("media_count")
        self.episode_count: int = data.get("episode_count")
        self.maturity_ratings: list[str] = data.get("maturity_ratings")
        self.is_simulcast: bool = data.get("is_simulcast")
        self.series_launch_year: str = data.get("series_launch_year")
        self.channel_id: str = data.get("channel_id")
        self.slug: str = data.get("slug")
        self.extended_description: str = data.get("extended_description")
        self.season_tags: str = data.get("season_tags")
        self.images: "Images" = Images(data.get("images"))
        self.mature_blocked: bool = data.get("mature_blocked")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.subtitle_locales: list[str] = data.get("subtitle_locales")
        self.keywords: str = data.get("keywords")
        self.is_subbed: bool = data.get("is_subbed")
        self.description: str = data.get("description")

    @classmethod
    def parse(cls, data: dict):
        if "series_metadata" in data:
            data.update(data["series_metadata"])
            data.pop("series_metadata")
        return cls(data)