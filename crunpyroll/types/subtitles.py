from .obj import Object

from typing import Dict

class SubtitlesStream(Object):
    """
    Info about a subtitles stream.

    Parameters:
        format (``str``):
            File format for subtitles (ass, srt, ...).

        language (``str``):
            Language code of the subtitles.    
        
        url (``str``):
            Direct URL to subtitles.
    """
    def __init__(self, data: Dict):
        self.format: str = data.get("format")
        self.language: str = data.get("language")
        self.url: str = data.get("url")