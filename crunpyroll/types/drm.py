from .obj import Object
from typing import Dict

class DRM(Object):
    """
    Info about DRM.

    Parameters:
        key_id (``str``)

        pssh (``str``)
    """
    def __init__(self, data: Dict):
        self.key_id: str = data.get("key_id")
        self.pssh: str = data.get("pssh")

class ContentProtection(Object):
    """
    List of Content Protection (DRM) used by Crunchyroll.

    Parameters:
        widevine (:obj:`~crunpyroll.types.DRM`):
            Info about Widevine DRM.

        playready (:obj:`~crunpyroll.types.DRM`):
            Info about PlayReady DRM.
    """
    def __init__(self, data: Dict):
        self.widevine: "DRM" = DRM(data.get("widevine"))
        self.playready: "DRM" = DRM(data.get("playready"))