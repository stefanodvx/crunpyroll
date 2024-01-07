from .obj import Object
from .subtitles import SubtitlesStream
from .hardsub import HardsubStream

from typing import List, Dict

class MediaStreams(Object):
    """
    Info about streams of a media content.

    Parameters:
        media_id (``str``):
            Unique identifier of the media.

        audio_locale (``str``):
            Audio language code of the media..

        url (``str``):
            Manifest URL to raw media (No subtitles)

        token (``str``):
            Token of the media. Used in license requests.

        subtitles (List of :obj:`~crunpyroll.types.SubtitlesStream`):
            List of available subtitles stream.

        hardsubs (List of :obj:`~crunpyroll.types.HardsubStream`):
            List of available hardsubs stream.
    """
    def __init__(self, data: Dict):
        self.media_id: str = data.get("media_id")
        self.audio_locale: str = data.get("audioLocale")
        self.url: str = data.get("url")
        self.token: str = data.get("token")
        self.subtitles: List["SubtitlesStream"] = data.get("subtitles")
        self.hardsubs: List["HardsubStream"] = data.get("hardsub")

    @classmethod
    def parse(cls, obj: Dict, media_id: str):
        data = {}
        data.update(obj)
        data["subtitles"] = [
            SubtitlesStream(subtitle) for
            subtitle in obj.get("subtitles").values()
        ]
        data["hardsub"] = [
            HardsubStream(video) for
            video in obj.get("hardSubs").values()
        ]
        data["media_id"] = media_id
        return cls(data)