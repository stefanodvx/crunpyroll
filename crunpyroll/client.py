from .methods import Methods
from .utils import (
    get_api_headers,
    DEVICE_ID,
    DEVICE_NAME,
    DEVICE_TYPE
)

from .session import Session
from .errors import CrunpyrollException
from .enums import APIHost
from .types.obj import Object

from typing import (
    Union, Optional,
    Dict
)

import httpx
import json

class Client(Object, Methods):
    """Initialize Crunchyroll Client
    
    Parameters:
        email (``str``):
            Email or username of the account.
        password (``str``):
            Password of the account.
        preferred_audio_language (``str``, *optional*):
            The audio language to use in Crunchyroll.
            Default to 'ja-JP'
        locale (``str``, *optional*):
            The language to use in Crunchyroll.
            Default to 'en-US'
        device_id (``str``, *optional*):
            The device identifier to use, in string form, e.g. '01234567-89AB-CDEF-0123-456789ABCDEF' where the 32 hexadecimal digits represent the UUID.
            Default to a random UUID
        device_name (``str``, *optional*):
            The device name to use (Crunchyroll app uses [About phone → Device name] field).
        device_type (``str``, *optional*):
            The device type to use (Crunchyroll app uses Manufacturer + Model).
        proxies (``str`` | ``dict``, *optional*):
            Proxies for HTTP requests.
            Default to None
    """
    def __init__(
        self,
        *,
        email: str,
        password: str,
        preferred_audio_language: str = "ja-JP",
        locale: str = "en-US",
        device_id: str = DEVICE_ID,
        device_name: str = DEVICE_NAME,
        device_type: str = DEVICE_TYPE,
        proxies: Union[Dict, str] = None,
        public_token: str = None
    ) -> None:
        self.email: str = email
        self.password: str = password
        self.preferred_audio_language: str = preferred_audio_language
        self.locale: str = locale
        self.device_id: str = device_id
        self.device_name: str = device_name
        self.device_type: str = device_type
        self.public_token = public_token

        self.http = httpx.AsyncClient(proxies=proxies, timeout=15)
        self.session = Session(self)

    async def start(self):
        if self.session.is_authorized:
            raise CrunpyrollException("Client is already authorized and started.")
        return await self.session.authorize()

    @staticmethod
    def parse_response(
        response: httpx.Response,
        *,
        method: str = "GET",
    ) -> Optional[Union[Dict, str]]:
        status_code = response.status_code
        text_content = response.text
        message = f"[{status_code}] {text_content}"
        try:
            content = response.json()
        except json.JSONDecodeError:
            content = response.text
        if status_code == 200:
            return content
        if status_code == 204 and method in {"PUT", "DELETE"}:
            return content
        raise CrunpyrollException(message)

    async def api_request(
        self,
        method: str,
        endpoint: str,
        host: APIHost = APIHost.BETA,
        url: str = None,
        params: Dict = None,
        headers: Dict = None,
        payload: Dict = None,
        include_session: bool = True,
    ) -> Optional[Dict]:
        if not url:
            url = "https://" + host.value + "/" + endpoint
        api_headers = get_api_headers(headers)
        if self.session.is_authorized and include_session:
            api_headers.update(self.session.authorization_header)
        response = await self.http.request(
            method=method,
            url=url,
            params=params,
            headers=api_headers,
            data=payload
        )
        return Client.parse_response(response, method=method)
    
    async def manifest_request(
        self,
        url: str,
        headers: Dict = None,
    ) -> str:
        api_headers = get_api_headers(headers)
        if self.session.is_authorized:
            api_headers.update(self.session.authorization_header)
        response = await self.http.request(
            method="GET",
            url=url,
            headers=api_headers,
        )
        return Client.parse_response(response)