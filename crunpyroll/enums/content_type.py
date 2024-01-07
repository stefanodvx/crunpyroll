from enum import Enum

class ContentType(Enum):
    """Content type enumeration."""

    MUSIC = "music"
    "Content is music."

    SERIES = "series"
    "Content is a series."

    EPISODE = "episode"
    "Content is an episode."

    MOVIE = "movie_listing"
    "Content is a movie."
