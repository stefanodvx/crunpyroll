from crunpyroll import types
from crunpyroll import enums

import crunpyroll

class GetStreams:
    async def get_streams(
        self: "crunpyroll.Client",
        media_id: str,
        *,
        locale: str = None,
    ) -> "types.MediaStreams":
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="v1/" + media_id + "/android/phone/play",
            params={
                "locale": locale or self.locale,
                "queue": False
            },
            host=enums.APIHost.PLAY_SERVICE
        )
        return types.MediaStreams.parse(response, media_id)