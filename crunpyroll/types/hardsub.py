from .obj import Object

from typing import Dict

class HardsubStream(Object):
    def __init__(self, data: Dict):
        self.quality: str = data.get("quality")
        self.language: str = data.get("hlang", data.get("hardsub_locale"))
        self.url: str = data.get("url")