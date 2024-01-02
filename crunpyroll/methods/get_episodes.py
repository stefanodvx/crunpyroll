from crunpyroll import types

import crunpyroll

class GetEpisodes:
    async def get_episodes(
        self: "crunpyroll.Client",
        season_id: str,
        *,
        locale: str = None
    ) -> "types.EpisodesQuery":
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/seasons/" + season_id + "/episodes",
            params={
                "locale": locale or self.locale
            }
        )
        return types.EpisodesQuery.parse(response)