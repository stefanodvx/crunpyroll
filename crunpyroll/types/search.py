from ..enums import ContentType

from .series import Series

class SearchResult:
    def __init__(
        self,
        total: int,
        items: list
    ):
        self.total: int = total
        self.items: list = items
        
    @classmethod
    def parse(cls, response: dict):
        items = []
        if "data" not in response:
            raise Exception("Invalid response.")
        for sec in response["data"]:
            for item in sec["items"]:
                if item["type"] == ContentType.SERIES.value:
                    items.append(Series(item))
        return cls(len(items), items)