from .methods import Methods
from .utils import get_api_headers

from .session import Session
from .errors import CrunpyrollException
from .enums import APIHost
from .types.obj import Object

from mpegdash.parser import MPEGDASHParser

import httpx
import json

class Client(Object, Methods):
    """Initialize Crunchyroll Client
    
    Parameters:
        email (``str``):
            Email or username of the account
        password (``str``):
            Password of the account
        locale (``str``, optional):
            The language to use in Crunchyroll
            E.g.: en-US, it-IT...
            Default to en-US
        proxies (``dict | str``, optional):
            Proxies for Crunchyroll
            E.g.: https://0.0.0.0:8080 or {"https://": "0.0.0.0:8080"}
    """
    def __init__(
        self,
        *,
        email: str,
        password: str,
        locale: str = "en-US",
        proxies: dict | str = None
    ) -> None:
        self.email: str = email
        self.password: str = password
        self.locale: str = locale

        self.http = httpx.AsyncClient(proxies=proxies, timeout=15)
        self.session = Session(self)

    async def start(self):
        """Start Crunchyroll Client and login.

        Returns:
            ``bool``: On success, True is returned.
        """
        if self.session.is_authorized:
            raise CrunpyrollException("Client is already authorized and started.")
        return await self.session.authorize()

    @staticmethod
    def parse_response(response: httpx.Response) -> dict | str | None:
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
        params: dict = None,
        headers: dict = None,
        payload: dict = None
    ) -> dict | None:
        if not url:
            url = "https://" + host.value + "/" + endpoint
        else:
            url = url
        api_headers = get_api_headers(headers)
        if self.session.is_authorized:
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
        headers: dict = None,
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