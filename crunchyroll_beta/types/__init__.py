from typing import Dict, List
from datetime import datetime
from json import dumps

class Meta(type, metaclass=type("", (type,), {"__str__": lambda _: "~hi"})):
    def __str__(self):
        return f"<class 'pyrogram.types.{self.__name__}'>"

class Object(metaclass=Meta):
    @staticmethod
    def default(obj: "Object"):
        return {
            "_": obj.__class__.__name__,
            **{
                attr: (
                    "*" * 5
                    if attr in ("access_token", "refesh_token")
                    else getattr(obj, attr)
                )
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) not in (None, datetime)
            }
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Object.default, ensure_ascii=False)

class CMS(Object):
    def __init__(self, data: dict):
        self.bucket: str = data.get("bucket")
        self.policy: str = data.get("policy")
        self.signature: str = data.get("signature")
        self.key_pair_id: str = data.get("key_pair_id")
    
class AccountData(Object):
    def __init__(self, data: dict):
        self.access_token: str = data.get("access_token")
        self.refresh_token: str = data.get("refresh_token")
        self.expires_in: int = data.get("expires_in")
        self.expires: datetime = data.get("expires")
        self.token_type: str =  data.get("token_type")
        self.scope: str = data.get("scope")
        self.contry: str = data.get("country")
        self.account_id: str = data.get("account_id")
        self.cms: CMS = CMS(data.get("cms", {}))
        self.service_available: bool = data.get("service_available")
        self.avatar: str = data.get("avatar")
        self.has_beta: bool = data.get("cr_beta_opt_in")
        self.email_verified: bool = data.get("crleg_email_verified")
        self.email: str = data.get("email")
        self.maturity_rating: str = data.get("maturity_rating")
        self.account_language: str = data.get("preferred_communication_language")
        self.default_subtitles_language: str = data.get("preferred_communication_language")
        self.username: str = data.get("username")

class PlaylistItem(Object):
    def __init__(self, data: dict):
        self.url: str = data.get("url")
        self.bandwidth: int = data.get("bandwidth")
        self.width: int = data.get("width")
        self.height: int = data.get("height")
        self.framerate: str = data.get("framerate")
        self.codecs: str = data.get("codecs")

class Image(Object):
    def __init__(self, data: dict):
        self.width: int = data.get("width")
        self.height: int = data.get("height")
        self.type: str = data.get("type")
        self.source: str = data.get("source")

class Images(Object):
    def __init__(self, data: dict):
        self.poster_tall: List[Image] = [Image(item) for item in data.get("poster_tall", [[]])[0]]
        self.poster_wide: List[Image] = [Image(item) for item in data.get("poster_wide", [[]])[0]]
        self.thumbnail: List[Image] = [Image(item) for item in data.get("thumbnail", [[]])[0]]

class SearchMetadata(Object):
    def __init__(self, data: dict):
        self.score: int = data.get("score")

class Link(Object):
    def __init__(self, data: dict):
        self.href: str = data.get("href")

class NewsItems(Object):
    def __init__(self, data: dict):
        self.title: str = data.get("title")
        self.link: str = data.get("link")
        self.image: str = data.get("image")
        self.creator: str = data.get("creator")
        self.publish_date: str = data.get("publish_date")
        self.description: str = data.get("description")

class News(Object):
    def __init__(self, data: dict):
        self.total: int = data.get("total")
        self.items: List[NewsItems] = [NewsItems(item) for item in data.get("items", [])]

class Series(Object):
    def __init__(self, data: dict):
        self.id: str = data.get("id")
        self.channel_id: str = data.get("channel_id")
        self.title: str = data.get("title")
        self.slug: str = data.get("slug")
        self.slug_title: str = data.get("slug_title")
        self.description: str = data.get("description")
        self.extended_description: str = data.get("extended_description")
        self.keywords: List[str] = data.get("keywords", [])
        self.season_tags: List[str] = data.get("season_tags", [])
        self.images: Images = Images(data.get("images", {}))
        self.maturity_ratings: List[str] = data.get("maturity_ratings", [])
        self.episode_count: int = data.get("episode_count")
        self.season_count: int = data.get("season_count")
        self.media_count: int = data.get("media_count")
        self.content_provider: str = data.get("content_provider")
        self.is_mature: bool = data.get("is_mature")
        self.mature_blocked: bool = data.get("mature_blocked")
        self.is_subbed: bool = data.get("is_subbed")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.is_simulcast: bool = data.get("is_simulcast")
        self.seo_title: str = data.get("seo_title")
        self.seo_description: str = data.get("seo_description")
        self.availability_notes: str = data.get("availability_notes")

class Panel(Object):
    def __init__(self, data: dict):
        self.channel_id: str = data.get("channel_id")
        self.description: str = data.get("description")
        self.external_id: str = data.get("external_id")
        self.id: str = data.get("id")
        self.type: str = data.get("type")
        self.images: Images = Images(data.get("images", {}))
        self.last_public: str = data.get("last_public")
        self.linked_resource_key: str = data.get("linked_resource_key")
        self.new: bool = data.get("new")
        self.new_content: bool = data.get("new_content")
        self.promo_description: str = data.get("promo_description")
        self.promo_title: str = data.get("promo_title")
        self.search_metadata: SearchMetadata = SearchMetadata(data.get("search_metadata", {}))
        self.slug: str = data.get("slug")
        self.slug_title: str = data.get("slug_title")
        self.title: str = data.get("title")

class Collection(Object):
    def __init__(self, data: dict):
        self.type: str = data.get("type")
        self.total: int = data.get("total")
        self.items: List[Panel] = [Panel(item) for item in data.get("items", [])]

class NewsFeed(Object):
    def __init__(self, data: dict):
        self.top_news: News = News(data.get("top_news", {}))
        self.latest_news: News = News(data.get("latest_news", {}))

class Season(Object):
    def __init__(self, data: dict):
        self.id: str = data.get("id")
        self.channel_id: str = data.get("channel_id")
        self.title: str = data.get("title")
        self.slug_title: str = data.get("slug_title")
        self.series_id: str = data.get("series_id")
        self.season_number: int = data.get("season_number")
        self.is_complete: bool = data.get("is_complete")
        self.description: str = data.get("description")
        self.keywords: List[str] = data.get("keywords", [])
        self.season_tags: List[str] = data.get("season_tags", [])
        self.images: Dict = data.get("images")
        self.is_mature: bool = data.get("is_mature")
        self.mature_blocked: bool = data.get("mature_blocked")
        self.is_subbed: bool = data.get("is_subbed")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.is_simulcast: bool = data.get("is_simulcast")
        self.seo_title: str = data.get("seo_title")
        self.seo_description: str = data.get("seo_description")
        self.availability_notes: str = data.get("availability_notes")

class EpisodeLinks(Object):
    def __init__(self, data: dict):
        self.channel: Link = Link(data.get("episode/channel", {}))
        self.next_episode: Link = Link(data.get("episode/next_episode", {}))
        self.season: Link = Link(data.get("episode/season", {}))
        self.series: Link = Link(data.get("episode/series", {}))
        self.streams: Link = Link(data.get("streams", {}))

class Episode(Object):
    def __init__(self, data: dict):
        self.links: EpisodeLinks = EpisodeLinks(data.get("__links__", {}))
        self.id: str = data.get("id")
        self.channel_id: str = data.get("channel_id")
        self.series_id: str = data.get("series_id")
        self.series_title: str = data.get("series_title")
        self.season_id: str = data.get("season_id")
        self.season_title: str = data.get("season_title")
        self.season_number: int = data.get("season_number")
        self.episode: str = data.get("episode")
        self.episode_number: int = data.get("episode_number")
        self.sequence_number: int = data.get("sequence_number")
        self.production_episode_id: str = data.get("production_episode_id")
        self.title: str = data.get("title")
        self.slug_title: str = data.get("slug_title")
        self.description: str = data.get("description")
        self.next_episode_id: str = data.get("next_episode_id")
        self.next_episode_title: str = data.get("next_episode_title")
        self.hd_flag: bool = data.get("hd_flag")
        self.is_mature: bool = data.get("is_mature")
        self.mature_blocked: bool = data.get("mature_blocked")
        self.episode_air_date: str = data.get("episode_air_date")
        self.is_subbed: bool = data.get("is_subbed")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.is_clip: bool = data.get("is_clip")
        self.seo_title: str = data.get("seo_title")
        self.seo_description: str = data.get("seo_description")
        self.season_tags: List[str] = data.get("season_tags", [])
        self.available_offline: bool = data.get("available_offline")
        self.media_type: str = data.get("media_type")
        self.slug: str = data.get("slug")
        self.images: Images = Images(data.get("images", {}))
        self.duration_ms: int = data.get("duration_ms")
        self.is_premium_only: bool = data.get("is_premium_only")
        self.listing_id: str = data.get("listing_id")
        self.subtitle_locales: List[str] = data.get("subtitle_locales", [])
        self.playback: str = data.get("playback")
        self.availability_notes: str = data.get("availability_notes")

class StreamData(Object):
    def __init__(self, data: dict):
        self.hardsub_locale: str = data.get("hardsub_locale")
        self.url: str = data.get("url")

class SubtitleData(Object):
    def __init__(self, data: dict):
        self.locale: str = data.get("locale")
        self.url: str = data.get("url")
        self.format: str = data.get("format")

class VideoFormat(Object):
    def __init__(self, data: dict):
        self.raw: StreamData = StreamData(data.get("raw", {}))
        self.en: StreamData = StreamData(data.get("en-US", {}))
        self.es: StreamData = StreamData(data.get("es-ES", {}))
        self.es_la: StreamData = StreamData(data.get("es-LA", {}))
        self.pt_br: StreamData = StreamData(data.get("pt-BR", {}))
        self.pt: StreamData = StreamData(data.get("pt-PT", {}))
        self.fr: StreamData = StreamData(data.get("fr-FR", {}))
        self.de: StreamData = StreamData(data.get("de-DE", {}))
        self.ar: StreamData = StreamData(data.get("ar-SA", {}))
        self.it: StreamData = StreamData(data.get("it-IT", {}))
        self.ru: StreamData = StreamData(data.get("ru-RU", {}))

class Subtitles(Object):
    def __init__(self, data: dict):
        self.en: SubtitleData = SubtitleData(data.get("en-US", {}))
        self.es_la: SubtitleData = SubtitleData(data.get("es-LA", {}))
        self.es: SubtitleData = SubtitleData(data.get("es-ES", {}))
        self.pt_br: SubtitleData = SubtitleData(data.get("pt-BR", {}))
        self.pt: SubtitleData = SubtitleData(data.get("pt-PT", {}))
        self.fr: SubtitleData = SubtitleData(data.get("fr-FR", {}))
        self.de: SubtitleData = SubtitleData(data.get("de-DE", {}))
        self.ar: SubtitleData = SubtitleData(data.get("ar-SA", {}))
        self.it: SubtitleData = SubtitleData(data.get("it-IT", {}))
        self.ru: SubtitleData = SubtitleData(data.get("ru-RU", {}))

class Streams(Object):
    def __init__(self, data: dict):
        self.adaptive_dash: VideoFormat = VideoFormat(data.get("adaptive_dash", {}))
        self.adaptive_hls: VideoFormat = VideoFormat(data.get("adaptive_hls", {}))
        self.drm_adaptive_dash: VideoFormat = VideoFormat(data.get("drm_adaptive_dash", {}))
        self.drm_adaptive_hls: VideoFormat = VideoFormat(data.get("drm_adaptive_hls", {}))
        self.drm_multitrack_adaptive_hls_v2: VideoFormat = VideoFormat(data.get("drm_multitrack_adaptive_hls_v2", {}))
        self.multitrack_adaptive_hls_v2: VideoFormat = VideoFormat(data.get("multitrack_adaptive_hls_v2", {}))
        self.vo_adaptive_dash: VideoFormat = VideoFormat(data.get("vo_adaptive_dash", {}))
        self.vo_adaptive_hls: VideoFormat = VideoFormat(data.get("vo_adaptive_hls", {}))
        self.vo_drm_adaptive_dash: VideoFormat = VideoFormat(data.get("vo_drm_adaptive_dash", {}))
        self.vo_drm_adaptive_hls: VideoFormat = VideoFormat(data.get("vo_drm_adaptive_hls", {}))

class StreamsInfo(Object):
    def __init__(self, data: dict):
        self.media_id: str = data.get("media_id")
        self.audio_locale: str = data.get("audio_locale")
        self.subtitles: Subtitles = Subtitles(data.get("subtitles", {}))
        self.streams: Streams = Streams(data.get("streams", {}))
        self.bifs: List[str] = data.get("bifs", [])