from .obj import Object
from typing import Dict

class DRM(Object):
    def __init__(self, data: Dict):
        self.key_id: str = data.get("key_id")
        self.pssh: str = data.get("pssh")

class ContentProtection(Object):
    def __init__(self, data: Dict):
        self.widevine: "DRM" = DRM(data.get("widevine"))
        self.playready: "DRM" = DRM(data.get("playready"))