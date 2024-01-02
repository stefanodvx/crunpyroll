from ..enums import ContentType

from .obj import Object
from .series import Series
from .episodes import Episode
from .movies import Movie

class SearchQuery(Object):
    def __init__(
        self,
        total: int,
        items: list
    ):
        self.total: int = total
        self.items: list["Series"] | list["Episode"] | list["Movie"] = items
        
    @classmethod
    def parse(cls, response: dict):
        # TODO: Add support for Music
        items = []
        for sec in response["data"]:
            for item in sec["items"]:
                if item["type"] == ContentType.SERIES.value:
                    items.append(Series.parse(item))
                elif item["type"] == ContentType.EPISODE.value:
                    items.append(Episode.parse(item))
                elif item["type"] == ContentType.MOVIE_LISTING.value:
                    items.append(Movie.parse(item))
        return cls(len(items), items)