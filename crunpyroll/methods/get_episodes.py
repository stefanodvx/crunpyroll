from crunpyroll import types

import crunpyroll

class GetEpisodes:
    async def get_episodes(
        self: "crunpyroll.Client",
        season_id: str,
        *,
        locale: str = None
    ) -> "types.EpisodesQuery":
        """
        Get list of episodes from a season.

        Parameters:
            season_id (``str``):
                Unique identifier of the season.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
                
        Returns:
            :obj:`~crunpyroll.types.EpisodesQuery`:
                On success, query of episodes is returned.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/seasons/" + season_id + "/episodes",
            params={
                "locale": locale or self.locale
            }
        )
        return types.EpisodesQuery.parse(response)