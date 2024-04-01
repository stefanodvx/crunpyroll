from .methods import Methods
from .utils import get_api_headers

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
            The locale to use in Crunchyroll.
            Default to 'en-US'
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
        proxies: Union[Dict, str] = None
    ) -> None:
        self.email: str = email
        self.password: str = password
        self.preferred_audio_language: str = preferred_audio_language
        self.locale: str = locale

        self.http = httpx.AsyncClient(proxies=proxies, timeout=15)
        self.session = Session(self)

    async def start(self):
        if self.session.is_authorized:
            raise CrunpyrollException("Client is already authorized and started.")
        return await self.session.authorize()

    @staticmethod
    def parse_response(response: httpx.Response) -> Optional[Union[Dict, str]]:
        status_code = response.status_code
        text_content = response.text
        message = f"[{status_code}] {text_content}"
        try:
            content = response.json()
        except json.JSONDecodeError:
            content = response.text
        if status_code != 200:
            raise CrunpyrollException(message)
        return content

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
        else:
            url = url
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
        return Client.parse_response(response)
    
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