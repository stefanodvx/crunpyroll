Quick Start
===========

The next few steps serve as a quick start to see Crunpyroll in action.

Example
----------------------

Here's a quick example code. This script will login into the account, search for Attack on Titan series, and print the seasons of the show.
    
    .. code-block:: python

        import crunpyroll
        import asyncio

        client = crunpyroll.Client(
            email="email",
            password="password",
            locale="it-IT"
        )
        async def main():
            # Start client and login
            await client.start()
            # Search for Attack on Titan
            query = await client.search("Attack On Titan")
            series_id = query.items[0].id
            print(series_id)
            # Retrieve all seasons of the series
            seasons = await client.get_seasons(series_id)
            print(seasons)

        asyncio.run(main())

Enjoy the API
-------------

That was just a quick overview. In the next few pages of the introduction, we'll take a much more in-depth look of what
we have just done above.