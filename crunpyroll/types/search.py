from ..enums import ContentType

from .obj import Object
from .series import Series
from .episodes import Episode
from .movies import Movie

from typing import Union, List, Dict

ITEMS_TYPING = List[Union["Series", "Episode", "Movie"]]

class SearchQuery(Object):
    """
    Query containing search results.

    Parameters:
        total (``int``):
            Total results returned.

        items (List of [:obj:`~crunpyroll.types.Series` | :obj:`~crunpyroll.types.Episode` | :obj:`~crunpyroll.types.Movie`]):
            List containing each result.
    """
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
                elif item["type"] == ContentType.MOVIE.value:
                    items.append(Movie.parse(item))
        return cls(len(items), items)