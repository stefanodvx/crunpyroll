import crunpyroll

from ..enums import SearchFilter

class Search:
    async def search(
        self: "crunpyroll.Client",
        query: str,
        max_results: int = 6,
        ratings: bool = True,
        preferred_audio_language: str = None,
        locale: str = None,
        filters: list["SearchFilter"] = [
            SearchFilter.EPISODE,
            SearchFilter.MOVIE_LISTING,
            SearchFilter.MUSIC,
            SearchFilter.SERIES,
            SearchFilter.TOP_RESULTS
        ]
    ):
        await self.session.retrieve()
        filters_string = ",".join(
            filter.value for filter in filters
            if isinstance(filter, SearchFilter)
        )
        response = await self.api_request(
            "POST", "content/v2/discover/search",
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