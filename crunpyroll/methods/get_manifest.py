import crunpyroll

class GetManifest:
    async def get_manifest(
        self: "crunpyroll.Client",
        url: str
    ) -> str:
        await self.session.retrieve()
        response = await self.manifest_request(url)
        return response