from crunpyroll import types

import crunpyroll

class GetManifest:
    async def get_manifest(
        self: "crunpyroll.Client",
        url: str
    ) -> "types.Manifest":
        """
        Retrieve and parse manifest.

        Parameters:
            url (``str``):
                URL of the manifest.

        Returns:
            :obj:`~crunpyroll.types.Manifest`:
                On success, parsed manifest is returned.

        """
        await self.session.retrieve()
        response = await self.manifest_request(url)
        return types.Manifest.parse(response)