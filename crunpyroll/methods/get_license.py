from crunpyroll import types
from crunpyroll import enums

import crunpyroll

class GetLicense:
    async def get_license(
        self: "crunpyroll.Client",
        media_id: str,
        *,
        challenge: bytes,
        token: str,
    ) -> "types.MediaStreams":
        await self.session.retrieve()
        response = await self.api_request(
            method="POST",
            endpoint="v1/license/widevine",
            params={"specConform": True},
            headers={
                "Content-Type": "application/octet-stream",
                "X-Cr-Content-Id": media_id,
                "X-Cr-Video-Token": token,
            },
            host=enums.APIHost.LICENSE,
            payload=challenge,
        )
        return response