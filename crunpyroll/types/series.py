from .images import Images
from .content import Content

from typing import List, Dict

class Series(Content):
    """
    Info about a series.

    Parameters:
        id (``str``):
            Unique identifier of the series.

        title (``str``):
            Title of the series.

        slug (``str``):
            Slug of the series.

        description (``str``):
            Number of the series.

        season_count (``int``):
            Season count of the series.

        episode_count (``int``):
            Episode count of the series.

        launch_year (``int``):
            Leanch year of the series.

        subtitle_locales (List of ``str``):
            List containing language codes of available subtitles.

        audio_locales (``str``):
            Language code of the audio.

        maturity_ratings (List of ``str``)

        is_simulcast (``bool``):
            True, if this season is simulcast (currently airing).
        
        is_subbed (``bool``):
            True, if this season got subtitles.

        is_dubbed (``bool``):
            True, if this season got dubs.

        is_mature (``bool``):
            True, if this season is NSFW.
    """
    def __init__(self, data: Dict):
        self.id: str = data.get("id")
        self.title: str = data.get("title")
        self.slug: str = data.get("slug_title")
        self.description: str = data.get("description")
        self.season_count: int = data.get("season_count")
        self.episode_count: int = data.get("episode_count")
        self.subtitle_locales: List[str] = data.get("subtitle_locales")
        self.audio_locales: List[str] = data.get("audio_locales")
        self.maturity_ratings: List[str] = data.get("maturity_ratings")
        self.launch_year: int = data.get("series_launch_year")
        self.images: "Images" = Images(data.get("images", {}))
        self.is_simulcast: bool = data.get("is_simulcast")
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
        if "series_metadata" in obj:
            data.update(obj["series_metadata"])
        return cls(data)