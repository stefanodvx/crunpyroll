from .obj import Object

class HardsubStream(Object):
    def __init__(self, data: dict):
        self.quality: str = data.get("quality")
        self.language: str = data.get("hlang")
        self.url: str = data.get("url")