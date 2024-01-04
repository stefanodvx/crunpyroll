from .obj import Object
from .subtitles import SubtitlesStream
from .hardsub import HardsubStream

from typing import List, Dict

class OldMediaStreams(Object):
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