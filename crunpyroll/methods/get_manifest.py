from crunpyroll import types

import crunpyroll

class GetManifest:
    async def get_manifest(
        self: "crunpyroll.Client",
        url: str
    ) -> "types.Manifest":
        await self.session.retrieve()
        response = await self.manifest_request(url)
        return types.Manifest.parse(response)