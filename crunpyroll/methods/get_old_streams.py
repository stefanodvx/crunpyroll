from crunpyroll import types
from crunpyroll import errors

import crunpyroll

class GetOldStreams:
    async def get_old_streams(
        self: "crunpyroll.Client",
        media_id: str,
        *,
        locale: str = None,
    ) -> "types.OldMediaStreams":
        """
        Get available streams of a media.

        WARNING:
            It is important to note that this method relies on a deprecated endpoint,
            and there is a possibility that it may cease to function unexpectedly.
            We strongly recommend updating your code to incorporate the
            :obj:`~crunpyroll.Client.get_streams` method for
            a more reliable and sustainable solution.

        Parameters:
            media_id (``str``):
                Unique identifier of the media.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`~crunpyroll.types.OldMediaStreams`:
                On success, streams are returned.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/objects/" + media_id,
            params={
                "locale": locale or self.locale,
            }
        )
        index = await self.get_index()
        if len(response["data"]) == 0:
            raise errors.CrunpyrollException("No stream found.")
        streams_link = response["data"][0]["streams_link"]
        stream_id = streams_link.split("/")[-2]
        response = await self.api_request(
            method="GET",
            endpoint="cms/v2/IT/M3/crunchyroll/videos/" + stream_id + "/streams",
            params={
                "Policy": index.cms.policy,
                "Signature": index.cms.signature,
                "Key-Pair-Id": index.cms.key_pair_id
            }
        )
        return types.OldMediaStreams.parse(response)