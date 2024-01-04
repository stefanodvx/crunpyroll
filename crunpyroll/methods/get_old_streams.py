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