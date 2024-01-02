from crunpyroll import types

import crunpyroll

class GetProfile:
    async def get_profile(
        self: "crunpyroll.Client",
    ) -> "types.Profile":
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="accounts/v1/me/profile",
        )
        return types.Profile(response)