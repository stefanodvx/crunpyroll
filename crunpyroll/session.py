from datetime import datetime, timedelta

from .utils import (
    get_date,
    PUBLIC_TOKEN
)

from .errors import ClientNotAuthorized

from typing import Optional

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
        self.account_id: str = None

    @property
    def is_authorized(self):
        return bool(self.access_token and self.refresh_token)
    
    @property
    def authorization_header(self):
        return {"Authorization": f"Bearer {self.access_token}"}
    
    async def retrieve(self) -> None:
        if not self.is_authorized:
            raise ClientNotAuthorized("Client is not authorized yet.")
        date = get_date()
        if date >= self.expiration:
            await self.refresh()
    
    async def authorize(self) -> Optional[bool]:
        response = await self._client.api_request(
            method="POST",
            endpoint="auth/v1/token",
            headers={
                "Authorization": f"Basic {self._client.public_token or PUBLIC_TOKEN}"
            },
            payload={
                "username": self._client.email,
                "password": self._client.password,
                "grant_type": "password",
                "scope": "offline_access",
                "device_id": self._client.device_id,
                "device_name": self._client.device_name,
                "device_type": self._client.device_type
            }, include_session=False
        )
        self.access_token = response.get("access_token")
        self.refresh_token = response.get("refresh_token")
        self.expiration = get_date() + timedelta(
            seconds=response.get("expires_in")
        )
        self.account_id = response.get("account_id")
        return True
    
    async def refresh(self) -> Optional[bool]:
        response = await self._client.api_request(
            method="POST",
            endpoint="auth/v1/token",
            headers={
                "Authorization": f"Basic {self._client.public_token or PUBLIC_TOKEN}"
            },
            payload={
                "refresh_token": self.refresh_token,
                "grant_type": "refresh_token",
                "scope": "offline_access",
                "device_id": self._client.device_id,
                "device_name": self._client.device_name,
                "device_type": self._client.device_type
            }, include_session=False
        )
        self.access_token = response.get("access_token")
        self.refresh_token = response.get("refresh_token")
        self.expiration = get_date() + timedelta(
            seconds=response.get("expires_in")
        )
        return True
