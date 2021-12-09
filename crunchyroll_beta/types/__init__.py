from typing import Dict, List
from pydantic import BaseModel, Field

class Image(BaseModel):
    width: int
    height: int
    type: str
    source: str

class Images(BaseModel):
    poster_tall: List[List[Image]] = Field(default=None)
    poster_wide: List[List[Image]] = Field(default=None)
    thumbnail: List[List[Image]] = Field(default=None)

class SeriesMetadata(BaseModel):
    availability_notes: str
    episode_count: int
    extended_description: str
    is_dubbed: bool
    is_mature: bool
    is_simulcast: bool
    is_subbed: bool
    mature_blocked: bool
    maturity_ratings: List[str]
    season_count: int

class SearchMetadata(BaseModel):
    score: int

class Link(BaseModel):
    href: str

class NewsItems(BaseModel):
    title: str
    link: str
    image: str
    creator: str
    publish_date: str
    description: str

class News(BaseModel):
    total: int
    items: List[NewsItems]

class Series(BaseModel):
    id: str
    channel_id: str
    title: str
    slug: str
    slug_title: str
    description: str
    extended_description: str
    keywords: List[str]
    season_tags: List[str]
    images: Images
    maturity_ratings: List[str]
    episode_count: int
    season_count: int
    media_count: int
    content_provider: str
    is_mature: bool
    mature_blocked: bool
    is_subbed: bool
    is_dubbed: bool
    is_simulcast: bool
    seo_title: str
    seo_description: str
    availability_notes: str

class Panel(BaseModel):
    channel_id: str
    description: str
    external_id: str
    id: str
    type: str
    images: Images
    linked_resource_key: str
    new: bool
    new_content: bool
    promo_description: str
    promo_title: str
    search_metadata: SearchMetadata
    series_metadata: SeriesMetadata = Field(default=None)
    slug: str
    slug_title: str
    title: str

class Collection(BaseModel):
    type: str
    total: int
    items: List[Panel]

class NewsFeed(BaseModel):
    top_news: News
    latest_news: News

class Season(BaseModel):
    id: str
    channel_id: str
    title: str
    slug_title: str
    series_id: str
    season_number: int
    is_complete: bool
    description: str
    keywords: List[str]
    season_tags: List[str]
    images: Dict
    is_mature: bool
    mature_blocked: bool
    is_subbed: bool
    is_dubbed: bool
    is_simulcast: bool
    seo_title: str
    seo_description: str
    availability_notes: str

class EpisodeLinks(BaseModel):
    channel: Link = Field(alias="episode/channel")
    next_episode: Link = Field(alias="episode/next_episode")
    season: Link = Field(alias="episode/season")
    series: Link = Field(alias="episode/series")
    streams: Link

class Episode(BaseModel):
    links: EpisodeLinks = Field(alias="__links__")
    id: str
    channel_id: str
    series_id: str
    series_title: str
    season_id: str
    season_title: str
    season_number: int
    episode: str
    episode_number: int
    sequence_number: int
    production_episode_id: str
    title: str
    slug_title: str
    description: str
    next_episode_id: str
    next_episode_title: str
    hd_flag: bool
    is_mature: bool
    mature_blocked: bool
    episode_air_date: str
    is_subbed: bool
    is_dubbed: bool
    is_clip: bool
    seo_title: str
    seo_description: str
    season_tags: List[str]
    available_offline: bool
    media_type: str
    slug: str
    images: Images
    duration_ms: int
    is_premium_only: bool
    listing_id: str
    subtitle_locales: List[str]
    playback: str
    availability_notes: str

class StreamData(BaseModel):
    hardsub_locale: str
    url: str

class SubtitleData(BaseModel):
    locale: str
    url: str
    format: str

class VideoFormat(BaseModel):
    raw: StreamData = Field(default=None)
    en: StreamData = Field(default=None, alias="en-US")
    es: StreamData = Field(default=None, alias="es-ES")
    es_la: StreamData = Field(default=None, alias="es-LA")
    pt_br: StreamData = Field(default=None, alias="pt-BR")
    pt: StreamData = Field(default=None, alias="pt-PT")
    fr: StreamData = Field(default=None, alias="fr-FR")
    de: StreamData = Field(default=None, alias="de-DE")
    ar: StreamData = Field(default=None, alias="ar-SA")
    it: StreamData = Field(default=None, alias="it-IT")
    ru: StreamData = Field(default=None, alias="ru-RU")

class Subtitles(BaseModel):
    en: SubtitleData = Field(default=None, alias="en-US")
    es_la: SubtitleData = Field(default=None, alias="es-LA")
    es: SubtitleData = Field(default=None, alias="es-ES")
    pt_br: SubtitleData = Field(default=None, alias="pt-BR")
    pt: SubtitleData = Field(default=None, alias="pt-PT")
    fr: SubtitleData = Field(default=None, alias="fr-FR")
    de: SubtitleData = Field(default=None, alias="de-DE")
    ar: SubtitleData = Field(default=None, alias="ar-SA")
    it: SubtitleData = Field(default=None, alias="it-IT")
    ru: SubtitleData = Field(default=None, alias="ru-RU")

class Streams(BaseModel):
    adaptive_dash: VideoFormat
    adaptive_hls: VideoFormat
    drm_adaptive_dash: VideoFormat
    drm_adaptive_hls: VideoFormat
    drm_multitrack_adaptive_hls_v2: VideoFormat
    multitrack_adaptive_hls_v2: VideoFormat
    vo_adaptive_dash: VideoFormat
    vo_adaptive_hls: VideoFormat
    vo_drm_adaptive_dash: VideoFormat
    vo_drm_adaptive_hls: VideoFormat

class StreamsInfo(BaseModel):
    media_id: str
    audio_locale: str
    subtitles: Subtitles
    streams: Streams
    bifs: List[str]