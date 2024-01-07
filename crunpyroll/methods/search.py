from crunpyroll import enums
from crunpyroll import types

from typing import List

import crunpyroll

class Search:
    async def search(
        self: "crunpyroll.Client",
        query: str,
        *,
        max_results: int = 6,
        locale: str = None,
        filters: List["enums.ContentType"] = [
            enums.ContentType.SERIES,
            enums.ContentType.MOVIE,
            enums.ContentType.EPISODE,
            enums.ContentType.MUSIC,
        ]
    ) -> "types.SearchQuery":
        """
        Search for series, movies or episodes.

        Parameters:
            query (``str``):
                Query string to search.
            max_results (``int``, *optional*):
                Max results for every content type.
                Default to 6
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
            filters (List of :obj:`~crunpyroll.enums.ContentType`, *optional*):
                Content to filters.
                Default to every value in :obj:`~crunpyroll.enums.ContentType`.

        Returns:
            :obj:`~crunpyroll.types.SearchQuery`:
                On success, query of results is returned.
        """
        await self.session.retrieve()
        filters_string = ",".join(
            filter.value for filter in filters
            if isinstance(filter, enums.ContentType)
        )
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/discover/search",
            params={
                "q": query,
                "n": max_results,
                "locale": locale or self.locale,
                "type": filters_string
            }
        )
        return types.SearchQuery.parse(response)