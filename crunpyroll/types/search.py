from ..enums import ContentType

from .obj import Object
from .series import Series
from .episodes import Episode
from .movies import Movie

from typing import Union, List, Dict

ITEMS_TYPING = Union[List["Series"], List["Episode"], List["Movie"]]

class SearchQuery(Object):
    def __init__(
        self,
        total: int,
        items: List
    ):
        self.total: int = total
        self.items: ITEMS_TYPING = items
        
    @classmethod
    def parse(cls, response: Dict):
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