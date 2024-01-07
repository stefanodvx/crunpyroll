from .obj import Object
from .drm import ContentProtection

from ..utils import (
    WIDEVINE_UUID,
    PLAYREADY_UUID,
    parse_segments
)

from typing import List, Dict

import xmltodict

class Manifest(Object):
    """
    Info about a manifest.

    Parameters:
        video_streams (List of :obj:`~crunpyroll.types.ManifestVideoStream`):
            List of every video stream available.

        audio_streams (List of :obj:`~crunpyroll.types.ManifestAudioStream`):
            List of every audio stream available.

        content_protection (:obj:`~crunpyroll.types.ContentProtection`):
            Info about Content Protection (DRM).

        plain (``str``):
            Plain version of the manifest (XML).
            Useful for external downloader tools.
    """
    def __init__(self, data: Dict):
        self.video_streams: List["ManifestVideoStream"] = data.get("video_streams")
        self.audio_streams: List["ManifestAudioStream"] = data.get("audio_streams")
        self.content_protection: "ContentProtection" = ContentProtection(data.get("content_protection"))
        self.plain: str = data.get("plain")

    @classmethod
    def parse(cls, obj: str):
        data = {}
        data["plain"] = obj
        data["video_streams"] = []
        data["audio_streams"] = []
        data["content_protection"] = {}
        manifest = xmltodict.parse(obj)
        for aset in manifest["MPD"]["Period"]["AdaptationSet"]:
            template = aset["SegmentTemplate"]
            for drm in aset["ContentProtection"]:
                scheme_id_uri = drm["@schemeIdUri"]
                if scheme_id_uri == WIDEVINE_UUID:
                    data["content_protection"]["widevine"] = {}
                    data["content_protection"]["widevine"]["pssh"] = drm["cenc:pssh"]
                    data["content_protection"]["widevine"]["key_id"] = drm["@cenc:default_KID"]
                if scheme_id_uri == PLAYREADY_UUID:
                    data["content_protection"]["playready"] = {}
                    data["content_protection"]["playready"]["pssh"] = drm["mspr:pro"]
            for repr in aset["Representation"]:
                if repr.get("@mimeType").startswith("video"):
                    stream = ManifestVideoStream.parse(repr, template)
                    data["video_streams"].append(stream)
                elif repr.get("@mimeType").startswith("audio"):
                    stream = ManifestAudioStream.parse(repr, template)
                    data["audio_streams"].append(stream)
        return cls(data)

class ManifestVideoStream(Object):
    """
    Info about a manifest video stream.

    Parameters:
        codecs (``str``):
            Codecs of the video stream.

        width (``int``):
            Width of the video stream.

        height (``int``):
            Height of the video stream.
        
        bitrate (``int``):
            Bitrate of the video stream.

        segments (List of ``str``):
            Each segment URL of the video stream.
    """
    def __init__(self, data: Dict):
        self.codecs: str = data.get("codecs")
        self.width: int = data.get("width")
        self.height: int = data.get("height")
        self.bitrate: int = data.get("bitrate")
        self.segments: List[str] = data.get("segments")

    @classmethod
    def parse(cls, obj: Dict, template: Dict):
        data = {}
        data["codecs"] = obj["@codecs"]
        data["width"] = int(obj["@width"])
        data["height"] = int(obj["@height"])
        data["bitrate"] = int(obj["@bandwidth"])
        data["segments"] = parse_segments(obj, template)
        return cls(data)
    
class ManifestAudioStream(Object):
    """
    Info about a manifest audio stream.

    Parameters:
        codecs (``str``):
            Codecs of the audio stream.
        
        bitrate (``int``):
            Bitrate of the audio stream.

        segments (List of ``str``):
            Each segment URL of the audio stream.
    """
    def __init__(self, data: Dict):
        self.codecs: str = data.get("codecs")
        self.bitrate: int = data.get("bitrate")
        self.segments: List[str] = data.get("segments")

    @classmethod
    def parse(cls, obj: Dict, template: Dict):
        data = {}
        data["codecs"] = obj["@codecs"]
        data["bitrate"] = int(obj["@bandwidth"])
        data["segments"] = parse_segments(obj, template)
        return cls(data)