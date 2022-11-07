import requests
import re

from datetime import timedelta
from typing import Optional, List, Dict
from requests.models import Response

from .utils import *
from .types import *

from .errors import CrunchyrollError, LoginError

class Crunchyroll:
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
            E.g.: {"http": ...}
    """
    def __init__(
        self,
        email: str,
        password: str,
        locale: str="en-US",
        proxy: dict=None
    ) -> None:
        self.http = requests.Session()
        if proxy:
            self.http.proxies.update(proxy)
        self.email: str = email
        self.password: str = password
        self.locale: str = locale
        self.account_data: AccountData = AccountData(dict())
        self.api_headers: Dict = headers()

    def start(self):
        self._create_session()

    def _get_json(self, r: Response) -> Optional[Dict]:
        code: int = r.status_code
        r_json: Dict = r.json()
        if "error" in r_json:
            error_code = r_json.get("error")
            if error_code == "invalid_grant":
                raise LoginError(f"[{code}] Invalid login credentials.")
        elif "message" in r_json and "code" in r_json:
            message = r_json.get("message")
            raise CrunchyrollError(f"[{code}] Error occured: {message}")
        if code != 200:
            raise CrunchyrollError(f"[{code}] {r.text}")
        return r_json

    def _create_session(self, refresh=False):
        headers = {"Authorization": AUTHORIZATION}
        if not refresh:
            data = {
                "username": self.email,
                "password": self.password,
                "grant_type": "password",
                "scope": "offline_access",
            }
        elif refresh:
            data = {
                "refresh_token": self.account_data.refresh_token,
                "grant_type": "refresh_token",
                "scope": "offline_access",
            }

        r = self.http.request(
            method="POST",
            url=TOKEN_ENDPOINT,
            headers=headers,
            data=data
        )
        r_json = self._get_json(r)

        self.api_headers.clear()
        self.account_data = AccountData({})

        access_token = r_json["access_token"]
        token_type = r_json["token_type"]
        account_auth = {"Authorization": f"{token_type} {access_token}"}
        
        account_data = dict()
        account_data.update(r_json)
        self.account_data = AccountData({})
        self.api_headers.update(account_auth)

        r = self._make_request(
            method="GET",
            url=INDEX_ENDPOINT
        )
        account_data.update(r)

        r = self._make_request(
            method="GET",
            url=PROFILE_ENDPOINT
        )
        account_data.update(r)

        account_data["expires"] = date_to_str(get_date() + timedelta(seconds=account_data["expires_in"]))
        self.account_data = AccountData(account_data)

    def _make_request(
        self,
        method: str,
        url: str,
        headers: Dict=dict(),
        params: Dict=dict(),
        data=None
    ) -> Optional[Dict]:
        if self.account_data:
            if expiration := self.account_data.expires:
                current_time = get_date()
                if current_time > str_to_date(expiration):
                    self._create_session(refresh=True)
            params.update({
                "Policy": self.account_data.cms.policy,
                "Signature": self.account_data.cms.signature,
                "Key-Pair-Id": self.account_data.cms.key_pair_id
            })
        headers.update(self.api_headers)
        r = self.http.request(
            method,
            url,
            headers=headers,
            params=params,
            data=data
        )
        return self._get_json(r)

    def search(
        self,
        query: str,
        max_results: int=6,
        raw_json=False
    ) -> Optional[List[Collection]]:
        """Search series

        Parameters:
            query (``str``):
                Query to search
            max_results (``int``, optional):
                Number of results to return
                Default to 6

        Returns:
            ``List``: On success, list of ``Collection`` is returned
        """
        r = self._make_request(
            method="GET",
            url=SEARCH_ENDPOINT,
            params = {
                "q": query,
                "n": str(max_results),
                "locale": self.locale
            }
        )
        return [Collection(collection) for collection in r.get("items")] if not raw_json else r

    def get_series(
        self,
        series_id: str,
        raw_json=False
    ) -> Optional[Series]:
        """Get info about a series

        Parameters:
            series_id (``str``):
                ID of the series

        Returns:
            ``Series``: On success, ``Series`` object is returned
        """
        r = self._make_request(
            method="GET",
            url=SERIES_ENDPOINT.format(self.account_data.cms.bucket, series_id),
            params = {"locale": self.locale}
        )
        return Series(r) if not raw_json else r
        
    def get_seasons(
        self,
        series_id: str,
        raw_json=False
    ) -> Optional[List[Season]]:
        """Get seasons of a series

        Parameters:
            series_id (``str``):
                ID of the series

        Returns:
            ``List``: On success, list of ``Season`` is returned
        """
        r = self._make_request(
            method="GET",
            url=SEASONS_ENDPOINT.format(self.account_data.cms.bucket),
            params = {
                "series_id": series_id,
                "locale": self.locale
            }
        )
        return [Season(season) for season in r.get("items")] if not raw_json else r

    def get_episodes(
        self,
        season_id: str,
        raw_json=False
    ) -> Optional[List[Episode]]:
        """Get episodes of a series (from season)

        Parameters:
            season_id (``str``):
                ID of a season

        Returns:
            ``List``: On success, list of ``Episode`` is returned
        """
        r = self._make_request(
            method="GET",
            url=EPISODES_ENDPOINT.format(self.account_data.cms.bucket),
            params = {
                "season_id": season_id,
                "locale": self.locale
            }
        )
        return [Episode(episode) for episode in r.get("items")] if not raw_json else r

    def get_streams(
        self,
        episode: Episode,
        raw_json=False
    ) -> Optional[StreamsInfo]:
        """Get streams from an episode

        Parameters:
            episode (``Episode``):
                Pass one of the items that ``get_episodes()`` returns

        Returns:
            ``StreamsInfo``: On success, ``StreamsInfo`` object is returned
        """
        stream_id = re.search(r"videos\/(.+?)\/streams", episode.links.streams.href).group(1)
        r = self._make_request(
            method="GET",
            url=STREAMS_ENDPOINT.format(self.account_data.cms.bucket, stream_id),
            params = {"locale": self.locale}
        )
        
        # Fix empty key in video streams
        fixup(r)
    
        return StreamsInfo(r) if not raw_json else r

    def get_similar(
        self,
        series_id: str,
        max_results: int=6,
        raw_json=False
    ) -> Optional[List[Panel]]:
        """Get similar series

        Parameters:
            series_id (``str``):
                ID of the series
            max_results (``int``, optional):
                Number of results to return
                Default to 6

        Returns:
            ``List``: On success, list of ``Panel`` is returned
        """
        r = self._make_request(
            method="GET",
            url=SIMILAR_ENDPOINT.format(self["account_id"]),
            params = {
                "guid": series_id,
                "n": str(max_results),
                "locale": self.locale
            }
        )
        return [Panel(panel) for panel in r.get("items")] if not raw_json else r

    def news_feed(
        self,
        max_results: int=6,
        raw_json=False
    ) -> Optional[NewsFeed]:
        """Get news feed

        Parameters:
            n (``int``, optional):
                Number of results to return
                Default to 6

        Returns:
            ``NewsFeed``: On success, ``NewsFeed`` object is returned
        """
        r = self._make_request(
            method="GET",
            url=NEWSFEED_ENDPOINT,
            params = {
                "n": str(max_results),
                "locale": self.locale
            }
        )
        return NewsFeed(r) if not raw_json else r

    def browse(
        self,
        sort_by: str = "newly_added",
        max_results: int=6,
        raw_json=False
    ) -> Optional[List[Panel]]:
        """Browse Crunchyroll catalog

        Parameters:
            sort_by (``str``, optional):
                Sort by ``newly_added``, ``popularity`` or ``alphabetical``
                Default to ``newly_added``
            max_results (``int``, optional):
                Number of results to return
                Default to 6

        Returns:
            ``List``: On success, list of ``Panel`` is returned
        """
        r = self._make_request(
            method="GET",
            url=BROWSE_ENDPOINT,
            params = {
                "sort_by": sort_by,
                "n": str(max_results),
                "locale": self.locale
            }
        )
        return [Panel(panel) for panel in  r.get("items")] if not raw_json else r

    def get_formats(self, url: str) -> Optional[List[PlaylistItem]]:
        """Get formats in a playlist

        Parameters:
            url (``str``):
                URL of the m3u8 playlist

        Returns:
            ``List``: On success, list of ``PlaylistItem`` is returned
        """
        formats = list()
        r = self.http.get(url)
        lines = r.text.split("\n")
        for i, line in enumerate(lines, 1):
            regesp = re.match(PLAYLIST_REG, line.strip())
            if regesp:
                formats.append({
                    "url": lines[i].strip(),
                    "bandwidth": int(regesp.group(1)),
                    "width": int(regesp.group(2)),
                    "height": int(regesp.group(3))
                })
        return [PlaylistItem(frmt) for frmt in formats]
