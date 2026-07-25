from .obj import Object
from .content import Content

from typing import List, Dict

class SeasonsQuery(Object):
    """
    Query containing seasons.

    Parameters:
        total (``int``):
            Total seasons returned.

        items (``list`` of :obj:`~crunpyroll.types.Season`):
            List containing each season.
    """
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
    """
    Info about a season.

    Parameters:
        id (``str``):
            Unique identifier of the season.

        title (``str``):
            Title of the season.

        slug (``str``):
            Slug of the season.

        season_number (``int``):
            Number of the season.

        season_sequence_number (``int``):
            Sequential number of the season.

        episode_count (``int``):
            Episode count of the season.

        description (``str``):
            Description of the season.

        series_id (``str``):
            Unique identifier of the series of this season.

        series_slug (``str``):
            Slug of the series of this season.

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
        self.season_number: int = data.get("season_number")
        self.season_sequence_number: int = data.get("season_sequence_number")
        self.episode_count: int = data.get("number_of_episodes")
        self.series_id: str = data.get("series_id")
        self.series_slug: str = data.get("series_slug_title")
        self.subtitle_locales: List[str] = data.get("subtitle_locales")
        self.audio_locales: List[str] = data.get("audio_locales")
        self.maturity_ratings: List[str] = data.get("maturity_ratings")
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