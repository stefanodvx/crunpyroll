from .methods import Methods
from .utils import (
    get_api_headers,
    API_DOMAIN
)

from .session import Session
from .errors import CrunchyrollError

import ssl
import json
import httpx

class Client(Methods):
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
        proxy (``str``, dict):
            Proxy for Crunchyroll
            E.g.: {"https://": "0.0.0.0:8080"}
    """
    def __init__(
        self,
        email: str,
        password: str,
        locale: str = "en-US",
        proxies: dict = None
    ) -> None:
        self.email: str = email
        self.password: str = password
        self.locale: str = locale

        self.http = httpx.AsyncClient(
            proxies=proxies,
            verify=ssl.create_default_context(),
        )

        self.session = Session(self)

    @staticmethod
    def parse_response(response: httpx.Response) -> dict | None:
        status_code = response.status_code
        text_content = response.text
        try:
            json_content = response.json()
        except json.JSONDecodeError:
            raise CrunchyrollError(f"[{status_code}] {text_content}")
        if status_code != 200:
            raise CrunchyrollError(f"[{status_code}] {text_content}")
        return json_content

    async def api_request(
        self,
        method: str,
        endpoint: str,
        params: dict = None,
        headers: dict = None,
        payload: dict = None
    ) -> dict | None:
        url = API_DOMAIN + endpoint
        api_headers = get_api_headers(headers)
        print(url, api_headers)
        response = await self.http.request(
            method=method,
            url=url,
            params=params,
            headers=api_headers,
            data=payload
        )
        return Client.parse_response(response)