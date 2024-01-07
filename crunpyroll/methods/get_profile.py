from crunpyroll import types

import crunpyroll

class GetProfile:
    async def get_profile(
        self: "crunpyroll.Client",
    ) -> "types.Profile":
        """
        Get current profile informations.

        Returns:
            :obj:`~crunpyroll.types.Profile`:
                On success, profile object is returned.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="accounts/v1/me/profile",
        )
        return types.Profile(response)