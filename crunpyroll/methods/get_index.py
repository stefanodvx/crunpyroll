from crunpyroll import types

import crunpyroll

class GetIndex:
    async def get_index(
        self: "crunpyroll.Client",
    ) -> "types.Index":
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="index/v2",
        )
        return types.Index(response)