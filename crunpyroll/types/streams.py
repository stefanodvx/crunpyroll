from .obj import Object
from .subtitles import SubtitlesStream
from .hardsub import HardsubStream

class MediaStreams(Object):
    def __init__(self, data: dict):
        self.media_id: str = data.get("media_id")
        self.audio_locale: str = data.get("audioLocale")
        self.url: str = data.get("url")
        self.token: str = data.get("token")
        self.subtitles: list["SubtitlesStream"] = data.get("subtitles")
        self.hardsubs: list["HardsubStream"] = data.get("hardsub")

    @classmethod
    def parse(cls, obj: dict, media_id: str):
        data = {}
        data.update(obj)
        data["subtitles"] = [
            SubtitlesStream(subtitle) for
            subtitle in obj.get("subtitles").values()
        ]
        data["hardsub"] = [
            HardsubStream(subtitle) for
            subtitle in obj.get("hardSubs").values()
        ]
        data["media_id"] = media_id
        return cls(data)