from crunpyroll import types

import crunpyroll

class GetSeasons:
    async def get_seasons(
        self: "crunpyroll.Client",
        series_id: str,
        *,
        locale: str = None,
    ) -> "types.SeasonsQuery":
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/series/" + series_id + "/seasons",
            params={
                "locale": locale or self.locale
            }
        )
        return types.SeasonsQuery.parse(response)