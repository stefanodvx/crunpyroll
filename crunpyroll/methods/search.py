import crunpyroll

from crunpyroll import enums

class Search:
    async def search(
        self: "crunpyroll.Client",
        query: str,
        max_results: int = 6,
        ratings: bool = True,
        preferred_audio_language: str = None,
        locale: str = None,
        filters: list["enums.SearchFilter"] = [
            enums.SearchFilter.EPISODE,
            enums.SearchFilter.MOVIE_LISTING,
            enums.SearchFilter.MUSIC,
            enums.SearchFilter.SERIES,
            enums.SearchFilter.TOP_RESULTS
        ]
    ):
        await self.session.retrieve()
        filters_string = ",".join(
            filter.value for filter in filters
            if isinstance(filter, enums.SearchFilter)
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
        return response