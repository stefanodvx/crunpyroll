from crunpyroll import enums
from crunpyroll import types

import crunpyroll

class Search:
    async def search(
        self: "crunpyroll.Client",
        query: str,
        *,
        max_results: int = 6,
        locale: str = None,
        filters: list["enums.ContentType"] = [
            enums.ContentType.SERIES,
            enums.ContentType.MOVIE_LISTING,
            enums.ContentType.EPISODE,
            enums.ContentType.MUSIC,
        ]
    ) -> "types.SearchQuery":
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