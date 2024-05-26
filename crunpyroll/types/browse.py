from ..enums import ContentType
from ..utils import str_to_date

from .obj import Object
from .series import Series
from .episodes import Episode
from .movies import Movie

from typing import Union, List, Dict
from datetime import datetime

ITEMS_TYPING = List[Union["Series", "Episode", "Movie"]]


class BrowseQuery(Object):
    """
    Query containing browse results.

    Parameters:
        total (``int``):
            Total results returned.

        items (List of [:obj:`~crunpyroll.types.Series` | :obj:`~crunpyroll.types.Episode` | :obj:`~crunpyroll.types.Movie`]):
            List containing each result.
    """

    def __init__(self, total: int, items: List):
        self.total: int = total
        self.items: ITEMS_TYPING = items

    @classmethod
    def parse(cls, date: datetime, response: Dict):
        items = []
        for item in response["data"]:
            if str_to_date(item['last_public']).date() == date.date():
                if item["type"] == ContentType.SERIES.value:
                    items.append(Series.parse(item))
                elif item["type"] == ContentType.EPISODE.value:
                    if str_to_date(item['last_public']).date() == date.date():
                        items.append(Episode.parse(item))
                elif item["type"] == ContentType.MOVIE.value:
                    items.append(Movie.parse(item))

        return cls(len(items), items)
