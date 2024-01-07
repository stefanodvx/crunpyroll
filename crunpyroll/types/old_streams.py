from .obj import Object
from .subtitles import SubtitlesStream
from .hardsub import HardsubStream

from typing import List, Dict

class OldMediaStreams(Object):
    """
    Info about streams of a media content.

    Parameters:
        media_id (``str``):
            Unique identifier of the media.

        audio_locale (``str``):
            Audio language code of the media..

        dash_url (``str``):
            DASH Manifest URL to raw media (No subtitles)

        hls_url (``str``):
            HLS Manifest URL to raw media (No subtitles)

        subtitles (List of :obj:`~crunpyroll.types.SubtitlesStream`):
            List of available subtitles stream.

        hardsub_dash (List of :obj:`~crunpyroll.types.HardsubStream`):
            List of available DASH hardsubs stream.

        hardsub_hls (List of :obj:`~crunpyroll.types.HardsubStream`):
            List of available HLS hardsubs stream.
    """
    def __init__(self, data: Dict):
        self.media_id: str = data.get("media_id")
        self.audio_locale: str = data.get("audioLocale")
        self.dash_url: str = data.get("dash_url")
        self.hls_url: str = data.get("hls_url")
        self.subtitles: List["SubtitlesStream"] = data.get("subtitles")
        self.hardsub_hls: List["HardsubStream"] = data.get("hardsub_hls")
        self.hardsub_dash: List["HardsubStream"] = data.get("hardsub_dash")

    @classmethod
    def parse(cls, obj: Dict):
        data = {}
        data.update(obj)
        adaptive_dash_stream = obj["streams"].get("adaptive_dash", {}).pop("", {})
        adaptive_hls_stream = obj["streams"].get("adaptive_hls", {}).pop("", {})
        data["dash_url"] = adaptive_dash_stream.get("url")
        data["hls_url"] = adaptive_hls_stream.get("url")
        data["subtitles"] = [
            SubtitlesStream(subtitle) for
            subtitle in obj.get("subtitles").values()
        ]
        data["hardsub_dash"] = [
            HardsubStream(video) for
            video in obj["streams"].get("adaptive_dash", {}).values()
        ]
        data["hardsub_hls"] = [
            HardsubStream(video) for
            video in obj["streams"].get("adaptive_hls", {}).values()
        ]
        return cls(data)