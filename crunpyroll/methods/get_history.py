from crunpyroll import types

import crunpyroll

class GetHistory:
    async def get_history(
        self: "crunpyroll.Client",
        *,
        locale: str = None,
    ) -> "types.HistoryQuery":
        """
        Get list of seasons from a series.

        Parameters:
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
                
        Returns:
            :obj:`~crunpyroll.types.HistoryQuery`:
                On success, query of watch history.
        """
        await self.session.retrieve()

        response_agg = []

        next_page: str = None

        while True:
            response = types.HistoryQuery.parse(await self.api_request(
                method = "GET",
                endpoint = next_page or "content/v2/" + self.session.account_id + "/watch-history",
                params={
                    "locale": locale or self.locale
                }
            ))

            response_agg += response.items

            next_page = response.next_page.lstrip('/')
            if not next_page:
                break

        return response_agg