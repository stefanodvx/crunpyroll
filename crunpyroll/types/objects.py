from ..enums import ContentType

from .obj import Object
from .series import Series
from .seasons import Season
from .episodes import Episode
from .movies import Movie

from typing import Union, List, Dict

ITEMS_TYPING = List[Union["Series", "Season", "Episode", "Movie"]]

class ObjectsQuery(Object):
    """
    Query containing object structured as a search result.
    Parameters:
        total (``int``):
            Total results returned. This is always 1.
        items (List of [:obj:`~crunpyroll.types.Series` | :obj:`~crunpyroll.types.Season` | :obj:`~crunpyroll.types.Episode` | :obj:`~crunpyroll.types.Movie`]):            List containing each result.
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
        item = response['data'][0]
        item_type = item['type']
        if item_type == ContentType.SERIES.value:
            return Series.parse(item)
        if item_type == ContentType.SEASON.value:
            item['season_metadata']['series_id'] = item['season_metadata']['identifier'].split('|')[0]
            item['season_metadata']['season_number'] = int(item['season_metadata']['season_display_number'])
            return Season.parse(item)
        if item_type == ContentType.EPISODE.value: return Episode.parse(item)
        if item_type == ContentType.MOVIE.value: return Movie.parse(item)
        if item_type == 'movie':
            item['movie_listing_metadata'] = item['movie_metadata']
            return Movie.parse(item)