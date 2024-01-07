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
        """
        Get available streams of a media.

        Parameters:
            media_id (``str``):
                Unique identifier of the media.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`~crunpyroll.types.MediaStreams`:
                On success, streams are returned.
        """
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