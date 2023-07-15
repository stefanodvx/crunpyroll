from datetime import datetime, timedelta
from .utils import (
    get_date,
    PUBLIC_TOKEN,
    DEVICE_NAME,
    DEVICE_TYPE,
    DEVICE_ID
)

import crunpyroll

class Session:
    def __init__(
        self,
        client: "crunpyroll.Client"
    ):
        self._client: crunpyroll.Client = client

        self.access_token: str = None
        self.refresh_token: str = None
        self.expiration: datetime = None

    @property
    def is_authorized(self):
        return (self.access_token and self.refresh_token)
    
    async def retrieve(self) -> None:
        if not self.is_authorized:
            await self.authorize()
        date = get_date()
        if date >= self.expiration:
            await self.refresh()
    
    async def authorize(self) -> bool | None:
        response = await self._client.api_request(
            method="POST",
            endpoint="auth/v1/token",
            headers={
                "Authorization": f"Basic {PUBLIC_TOKEN}"
            },
            payload={
                "username": self._client.email,
                "password": self._client.password,
                "grant_type": "password",
                "scope": "offline_access",
                "device_id": DEVICE_ID,
                "device_name": DEVICE_NAME,
                "device_type": DEVICE_TYPE
            }
        )
        self.access_token = response.get("access_token")
        self.refresh_token = response.get("refresh_token")
        self.expiration = get_date() + timedelta(
            seconds=response.get("expires_in")
        )
        return True
    
    async def refresh(self) -> bool | None:
        response = await self._client.api_request(
            method="POST",
            endpoint="auth/v1/token",
            headers={
                "Authorization": f"Bearer {self.access_token}"
            },
            payload={
                "refresh_token": self.refresh_token,
                "grant_type": "refresh_token",
                "scope": "offline_access",
                "device_id": DEVICE_ID,
                "device_name": DEVICE_NAME,
                "device_type": DEVICE_TYPE
            }
        )
        self.access_token = response.get("access_token")
        self.refresh_token = response.get("refresh_token")
        self.expiration = get_date() + timedelta(
            seconds=response.get("expires_in")
        )
        return True
