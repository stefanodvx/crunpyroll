from typing import Dict, List
import json

class Object:
    def __str__(self):
        return json.dumps(
            self,
            indent=4,
            default=lambda x: x.__dict__,
            ensure_ascii=False
        )

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

class SeriesMetadata(Object):
    def __init__(self, data: dict):
        self.availability_notes: str = data.get("availability_notes")
        self.episode_count: int = data.get("episode_count")
        self.extended_description: str = data.get("extended_description")
        self.is_dubbed: bool = data.get("is_dubbed")
        self.is_mature: bool = data.get("is_mature")
        self.is_simulcast: bool = data.get("is_simulcast")
        self.is_subbed: bool = data.get("is_subbed")
        self.mature_blocked: bool = data.get("mature_blocked")
        self.maturity_ratings: List[str] = data.get("maturity_ratings", list())
        self.season_count: int = data.get("season_count")

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
        self.items: List[NewsItems] = [NewsItems(item) for item in data.get("items", list())]

class Series(Object):
    def __init__(self, data: dict):
        self.id: str = data.get("id")
        self.channel_id: str = data.get("channel_id")
        self.title: str = data.get("title")
        self.slug: str = data.get("slug")
        self.slug_title: str = data.get("slug_title")
        self.description: str = data.get("description")
        self.extended_description: str = data.get("extended_description")
        self.keywords: List[str] = data.get("keywords", list())
        self.season_tags: List[str] = data.get("season_tags", list())
        self.images: Images = data.get("images")
        self.maturity_ratings: List[str] = data.get("maturity_ratings", list())
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
        self.images: Images = data.get("images")
        self.last_public: str = data.get("last_public")
        self.linked_resource_key: str = data.get("linked_resource_key")
        self.new: bool = data.get("new")
        self.new_content: bool = data.get("new_content")
        self.promo_description: str = data.get("promo_description")
        self.promo_title: str = data.get("promo_title")
        self.search_metadata: SearchMetadata = data.get("search_metadata")
        self.series_metadata: SeriesMetadata = data.get("series_metadata")
        self.slug: str = data.get("slug")
        self.slug_title: str = data.get("slug_title")
        self.title: str = data.get("title")

class Collection(Object):
    def __init__(self, data: dict):
        self.type: str = data.get("type")
        self.total: int = data.get("total")
        self.items: List[Panel] = [Panel(item) for item in data.get("items", list())]

class NewsFeed(Object):
    def __init__(self, data: dict):
        self.top_news: News = data.get("top_news")
        self.latest_news: News = data.get("latest_news")

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
        self.keywords: List[str] = data.get("keywords", list())
        self.season_tags: List[str] = data.get("season_tags", list())
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
        self.channel: Link = data.get("episode/channel")
        self.next_episode: Link = data.get("episode/next_episode")
        self.season: Link = data.get("episode/season")
        self.series: Link = data.get("episode/series")
        self.streams: Link = data.get("streams")

class Episode(Object):
    def __init__(self, data: dict):
        self.links: EpisodeLinks = data.get("__links__")
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
        self.season_tags: List[str] = data.get("season_tags", list())
        self.available_offline: bool = data.get("available_offline")
        self.media_type: str = data.get("media_type")
        self.slug: str = data.get("slug")
        self.images: Images = data.get("images")
        self.duration_ms: int = data.get("duration_ms")
        self.is_premium_only: bool = data.get("is_premium_only")
        self.listing_id: str = data.get("listing_id")
        self.subtitle_locales: List[str] = data.get("subtitle_locales", list())
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
        self.raw: StreamData = data.get("raw")
        self.en: StreamData = data.get("en-US")
        self.es: StreamData = data.get("es-ES")
        self.es_la: StreamData = data.get("es-LA")
        self.pt_br: StreamData = data.get("pt-BR")
        self.pt: StreamData = data.get("pt-PT")
        self.fr: StreamData = data.get("fr-FR")
        self.de: StreamData = data.get("de-DE")
        self.ar: StreamData = data.get("ar-SA")
        self.it: StreamData = data.get("it-IT")
        self.ru: StreamData = data.get("ru-RU")

class Subtitles(Object):
    def __init__(self, data: dict):
        self.en: SubtitleData = data.get("en-US")
        self.es_la: SubtitleData = data.get("es-LA")
        self.es: SubtitleData = data.get("es-ES")
        self.pt_br: SubtitleData = data.get("pt-BR")
        self.pt: SubtitleData = data.get("pt-PT")
        self.fr: SubtitleData = data.get("fr-FR")
        self.de: SubtitleData = data.get("de-DE")
        self.ar: SubtitleData = data.get("ar-SA")
        self.it: SubtitleData = data.get("it-IT")
        self.ru: SubtitleData = data.get("ru-RU")

class Streams(Object):
    def __init__(self, data: dict):
        self.adaptive_dash: VideoFormat = data.get("adaptive_dash")
        self.adaptive_hls: VideoFormat = data.get("adaptive_hls")
        self.drm_adaptive_dash: VideoFormat = data.get("drm_adaptive_dash")
        self.drm_adaptive_hls: VideoFormat = data.get("drm_adaptive_hls")
        self.drm_multitrack_adaptive_hls_v2: VideoFormat = data.get("drm_multitrack_adaptive_hls_v2")
        self.multitrack_adaptive_hls_v2: VideoFormat = data.get("multitrack_adaptive_hls_v2")
        self.vo_adaptive_dash: VideoFormat = data.get("vo_adaptive_dash")
        self.vo_adaptive_hls: VideoFormat = data.get("vo_adaptive_hls")
        self.vo_drm_adaptive_dash: VideoFormat = data.get("vo_drm_adaptive_dash")
        self.vo_drm_adaptive_hls: VideoFormat = data.get("vo_drm_adaptive_hls")

class StreamsInfo(Object):
    def __init__(self, data: dict):
        self.media_id: str = data.get("media_id")
        self.audio_locale: str = data.get("audio_locale")
        self.subtitles: Subtitles = data.get("subtitles")
        self.streams: Streams = data.get("streams")
        self.bifs: List[str] = data.get("bifs", list())