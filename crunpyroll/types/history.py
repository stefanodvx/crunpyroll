from .obj import Object
from .content import Content
from .episodes import Episode

from ..utils import str_to_date

from datetime import datetime
from typing import List, Dict

class HistoryQuery(Object):
    """
    Query containing watch history.

    Parameters:
        total (``int``):
            Total episodes returned.

        items (``list`` of :obj:`~crunpyroll.types.History`):
            List containing each episode.

        next_page (``str```):
            URL for next page of results
    """
    def __init__(self, data: Dict):
        self.total: int = data.get("total")
        self.items: List["History"] = data.get("items")
        self.next_page: str = data.get("next_page")

    @classmethod
    def parse(cls, obj: Dict):
        data = {}
        data["total"] = obj["total"]
        data["next_page"] = obj["meta"]["next_page"]
        data["items"] = [
            History.parse(item)
            for item in obj["data"]
        ]
        return cls(data)

class History(Content):
    """
    Info about watch episode.

    Parameters:
        id (``str``):
            Unique identifier of the episode.

        date_played :py:obj:`~datetime.datetime`):
            Date the episode was watched.
        
        fully_watched (``bool``):
            True, if this episode was fully watched.

        episode (:obj:`~crunpyroll.types.Episode`):
            Episode metadata.
        
    """
    def __init__(self, data: Dict):
        self.id: str = data.get("id")
        self.date_played: datetime = str_to_date(data.get("date_played"))
        self.fully_watched: bool = data.get("fully_watched")
        self.episode: "Episode" = Episode(data.get("episode"))

    @classmethod
    def parse(cls, obj: Dict):
        data = {}
        data["id"] = obj["id"]
        data["date_played"] = obj["date_played"]
        data["fully_watched"] = obj["fully_watched"]
        data["episode"] = obj.get("panel",{})
        if "episode_metadata" in data["episode"]:
            data["episode"].update(data["episode"]["episode_metadata"])
            data["episode"].pop("episode_metadata", None)
        return cls(data)