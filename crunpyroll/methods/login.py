from crunpyroll import Crunchyroll

from crunpyroll.types import Session
from crunpyroll.utils import (
    get_date,
    PUBLIC_TOKEN,
    DEVICE_NAME,
    DEVICE_TYPE,
    DEVICE_ID
)

from datetime import timedelta

class Login:
    async def login(
        client: "Crunchyroll",
    ) -> bool | None:
        response = await client.api_request(
            method="POST",
            endpoint="auth/v1/token",
            headers={
                "Authorization": f"Basic {PUBLIC_TOKEN}"
            },
            payload={
                "username": client.email,
                "password": client.password,
                "gran_type": "password",
                "scope": "offline_access",
                "device_id": DEVICE_ID,
                "device_name": DEVICE_NAME,
                "device_type": DEVICE_TYPE
            }
        )
        
        access_token = response.get("access_token")
        refresh_token = response.get("refresh_token")
        expires_in = response.get("expires_in")
        expiration = get_date() + timedelta(seconds=expires_in)

        client.session = Session(
            access_token=access_token,
            refresh_token=refresh_token,
            expiration=expiration
        )

        return True