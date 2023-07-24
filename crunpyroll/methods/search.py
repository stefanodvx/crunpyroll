import crunpyroll

from crunpyroll import enums
from crunpyroll import types

class Search:
    async def search(
        self: "crunpyroll.Client",
        query: str,
        max_results: int = 6,
        ratings: bool = True,
        preferred_audio_language: str = None,
        locale: str = None,
        filters: list["enums.ContentType"] = [
            enums.ContentType.EPISODE,
            enums.ContentType.MOVIE_LISTING,
            enums.ContentType.MUSIC,
            enums.ContentType.SERIES,
            enums.ContentType.TOP_RESULTS
        ]
    ) -> "types.SearchResult":
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
                "ratings": ratings,
                "preferred_audio_language": preferred_audio_language or self.locale,
                "locale": locale or self.locale,
                "type": filters_string
            }
        )
        return types.SearchResult.parse(response)