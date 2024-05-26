from crunpyroll import enums
from crunpyroll import types
from crunpyroll.utils import get_date
from datetime import datetime
from typing import List

import crunpyroll


class Browse:
    async def browse(
            self: "crunpyroll.Client",
            sort_by: "enums.SortType" = enums.SortType.NEWLY_ADDED,
            date: datetime = get_date(),
            max_results: int = 15,
            locale: str = None,
            preferred_audio_language: str = None,
            filter: "enums.ContentType" = enums.ContentType.EPISODE
    ) -> "types.BrowseQuery":
        """
        Browse for series movies or episodes.

        Parameters:
            date: (``datetime``, *optional*):
                Get only contents release at this date
                Default date: current
            sort_by: (Value of :obj:`~crunpyroll.enums.SortType`, *optional*):
                Sort content
                Default to newly added :obj:`~crunpyroll.enums.NEWLY_ADDED`.
            max_results (``int``, *optional*):
                Max results for every content type.
                Default to 15
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
            preferred_audio_language (``str``, *optional*):
                Preferred audio language
                Default to the one used in Client.
            filter (:obj:`~crunpyroll.enums.ContentType`, *optional*):
                Content to filter. (Several filters cannot be used at the same time)
                Default to enums.ContentType.EPISODE in :obj:`~crunpyroll.enums.ContentType`.

        Returns:
            :obj:`~crunpyroll.types.BrowseQuery`:
                On success, query of results is returned.
        """
        await self.session.retrieve()

        response = await self.api_request(
            method="GET",
            endpoint="content/v2/discover/browse",
            params={
                "n": max_results,
                "locale": locale or self.locale,
                "preferred_audio_language": preferred_audio_language or self.preferred_audio_language,
                "type": filter.value,
                "sort_by": sort_by.value
            }
        )

        return types.BrowseQuery.parse(date, response)
