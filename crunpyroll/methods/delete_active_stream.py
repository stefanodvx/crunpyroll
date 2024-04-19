from crunpyroll import enums

import crunpyroll

class DeleteActiveStream:
    async def delete_active_stream(
        self: "crunpyroll.Client",
        media_id: str,
        *,
        token: str,
    ) -> str:
        """
        Delete an active stream.

        Parameters:
            media_id (``str``):
                Unique identifier of the media.
            token (``str``):
                Token of the stream.

        Returns:
            ``str``:
                On success, ??? is returned.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="DELETE",
            endpoint="v1/token/" + media_id + "/" + token,
            host=enums.APIHost.PLAY_SERVICE
        )
        return response