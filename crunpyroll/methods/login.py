import crunpyroll

class Login:
    async def login(
        client: "crunpyroll.Client",
    ) -> bool | None:
        return await client.session.authorize()