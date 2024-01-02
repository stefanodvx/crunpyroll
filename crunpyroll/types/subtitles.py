from .obj import Object

class SubtitlesStream(Object):
    def __init__(self, data: dict):
        self.format: str = data.get("format")
        self.language: str = data.get("language")
        self.url: str = data.get("url")