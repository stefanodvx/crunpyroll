from .content import Content
from .images import Images

from ..utils import str_to_date

from typing import List, Dict
from datetime import datetime
    
class Movie(Content):
    """
    Info about a movie.

    Parameters:
        id (``str``):
            Unique identifier of the movie.

        title (``str``):
            Title of the movie.

        slug (``str``):
            Slug of the movie.

        duration (``int``):
            Duration of the movie.

        free_available_date (:py:obj:`~datetime.datetime`):
            Date the movie will be released to free users.

        premium_available_date (:py:obj:`~datetime.datetime`):
            Date the movie will be released to premium users.

        release_year (``int``):
            Year the movie was released.

        description (``str``):
            Description of the movie.

        first_movie_id (``str``)

        subtitle_locales (List of ``str``):
            List containing language codes of available subtitles.

        audio_locales (``str``):
            Language code of the audio.

        maturity_ratings (List of ``str``)

        images (:obj:`~crunpyroll.types.Images`):
            Images of the movie.
        
        has_closed_captions (``bool``):
            True, if this movie got closed captions.
        
        is_available_offline (``bool``):
            True, if this movie is available offline.

        is_hd (``bool``):
            True, if this movie is High Definition.

        is_new (``bool``):
            True, if this movie is newly released.

        is_premium (``bool``):
            True, if this movie is available to premium users only.

        is_simulcast (``bool``):
            True, if this movie is simulcast (currently airing).
        
        is_subbed (``bool``):
            True, if this movie got subtitles.

        is_dubbed (``bool``):
            True, if this movie got dubs.

        is_mature (``bool``):
            True, if this movie is NSFW.
    """
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
        self.images: "Images" = Images(data.get("images"))
        self.has_closed_captions: bool = data.get("closed_captions_available")
        self.is_available_offline: bool = data.get("available_offline")
        self.is_hd: bool = data.get("hd_flag")
        self.is_new: bool = data.get("new")
        self.is_premium: bool = data.get("is_premium_only")
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