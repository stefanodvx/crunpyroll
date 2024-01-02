from crunpyroll import types

import crunpyroll

class GetSeries:
    async def get_series(
        self: "crunpyroll.Client",
        series_id: str,
        *,
        locale: str = None,
    ) -> "types.Series":
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/series/" + series_id,
            params={
                "locale": locale or self.locale
            }
        )
        return types.Series.parse(response)