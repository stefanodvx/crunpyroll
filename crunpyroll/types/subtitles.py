from .obj import Object

from typing import Dict

class SubtitlesStream(Object):
    def __init__(self, data: Dict):
        self.format: str = data.get("format")
        self.language: str = data.get("language")
        self.url: str = data.get("url")