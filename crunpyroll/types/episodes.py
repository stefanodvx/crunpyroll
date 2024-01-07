from .obj import Object
from .content import Content
from .images import Images

from ..utils import str_to_date

from datetime import datetime
from typing import List, Dict

class EpisodesQuery(Object):
    """
    Query containing episodes.

    Parameters:
        total (``int``):
            Total episodes returned.

        items (``list`` of :obj:`~crunpyroll.types.Episode`):
            List containing each episode.
    """
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
    """
    Info about an episode.

    Parameters:
        id (``str``):
            Unique identifier of the episode.

        title (``str``):
            Title of the episode.

        slug (``str``):
            Slug of the episode.

        episode_number (``int``):
            Number of the episode.

        duration (``int``):
            Duration of the episode.

        free_available_date (:py:obj:`~datetime.datetime`):
            Date the episode will be released to free users.

        premium_available_date (:py:obj:`~datetime.datetime`):
            Date the episode will be released to premium users.

        air_date (:py:obj:`~datetime.datetime`):
            Date the episode aired.

        upload_date (:py:obj:`~datetime.datetime`):
            Date the episode got uploaded on Crunchyroll.

        description (``str``):
            Description of the episode.

        next_episode_title (``str``):
            Title of the next episode.

        next_episode_id (``str``):
            Unique identifier of the next episode.

        season_id (``str``):
            Unique identifier of the season of this episode.

        season_title (``str``):
            Title of the season of this episode.

        season_number (``int``):
            Number of the season of this episode.

        season_slug (``str``):
            Slug of the season of this episode.

        series_id (``str``):
            Unique identifier of the series of this episode.

        series_slug (``str``):
            Slug of the series of this episode.

        subtitle_locales (List of ``str``):
            List containing language codes of available subtitles.

        audio_locales (``str``):
            Language code of the audio.

        maturity_ratings (List of ``str``)

        images (:obj:`~crunpyroll.types.Images`):
            Images of the episode.
        
        has_closed_captions (``bool``):
            True, if this episode got closed captions.
        
        is_available_offline (``bool``):
            True, if this episode is available offline.

        is_hd (``bool``):
            True, if this episode is High Definition.

        is_premium (``bool``):
            True, if this episode is available to premium users only.

        is_simulcast (``bool``):
            True, if this episode is simulcast (currently airing).
        
        is_subbed (``bool``):
            True, if this episode got subtitles.

        is_dubbed (``bool``):
            True, if this episode got dubs.

        is_mature (``bool``):
            True, if this episode is NSFW.
    """
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
        self.season_slug: str = data.get("season_slug_title")
        self.series_id: str = data.get("series_id")
        self.series_slug: str = data.get("series_slug_title")
        self.subtitle_locales: List[str] = data.get("subtitle_locales")
        self.audio_locales: str = data.get("audio_locale")
        self.maturity_ratings: List[str] = data.get("maturity_ratings")
        self.images: "Images" = Images(data.get("images", {}))
        self.has_closed_captions: bool = data.get("closed_captions_available")
        self.is_available_offline: bool = data.get("available_offline")
        self.is_hd: bool = data.get("hd_flag")
        self.is_premium: bool = data.get("is_premium_only")
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