from crunpyroll import types

import crunpyroll

class GetSeries:
    async def get_series(
        self: "crunpyroll.Client",
        series_id: str,
        *,
        locale: str = None,
    ) -> "types.Series":
        """
        Get informations about a series.

        Parameters:
            series_id (``str``):
                Unique identifier of the series.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`~crunpyroll.types.Series`:
                On success, series object is returned.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/series/" + series_id,
            params={
                "locale": locale or self.locale
            }
        )
        return types.Series.parse(response)