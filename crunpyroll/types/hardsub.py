from .obj import Object

from typing import Dict

class HardsubStream(Object):
    """
    Info about an hardsub stream.

    Parameters:
        quality (``str``):
            Quality of the video stream.

        language (``str``):
            Language of the subtitles.

        url (``str``):
            URL to DASH/HLS manifest.
    """
    def __init__(self, data: Dict):
        self.quality: str = data.get("quality")
        self.language: str = data.get("hlang", data.get("hardsub_locale"))
        self.url: str = data.get("url")