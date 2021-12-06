import requests, re
from typing import Optional, Dict

# Universal Authorization to access Crunchyroll Beta API
AUTHORIZATION = "Basic aHJobzlxM2F3dnNrMjJ1LXRzNWE6cHROOURteXRBU2Z6QjZvbXVsSzh6cUxzYTczVE1TY1k="

INDEX_ENDPOINT = "https://beta-api.crunchyroll.com/index/v2"
PROFILE_ENDPOINT = "https://beta-api.crunchyroll.com/accounts/v1/me/profile"
TOKEN_ENDPOINT = "https://beta-api.crunchyroll.com/auth/v1/token"
SEARCH_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/search"
STREAMS_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/videos/{}/streams"
SEASONS_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/seasons"
EPISODES_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/episodes"

config = {"data": dict()}

session = requests.Session()
session.headers = {
    "User-Agent": "Crunchyroll/3.10.0 Android/6.0 okhttp/4.9.1",
    "Content-Type": "application/x-www-form-urlencoded"
}

class Crunchyroll():
    """Crunchyroll BETA Client
    
    Parameters:
        locale (``str``, optional):
            The language to use in Crunchyroll
            E.g.: us-US, it-IT...
            Default to us-US
    """

    def __init__(self, locale="us-US") -> None:
        self.locale = locale

    def login(self, username: str, password: str) -> None:
        """Login to Crunchyroll

        Parameters:
            username (``str``):
                Email or username of the account
            password (``str``):
                Password of the account

        Returns:
            ``bool``: On success, True is returned
        """
        headers = session.headers
        headers.update({"Authorization": AUTHORIZATION})
        r = session.post(
            TOKEN_ENDPOINT,
            headers=headers,
            data = {
                "username": username,
                "password": password,
                "grant_type": "password",
                "scope": "offline_access",
            }
        )
        if r.status_code == 200:
            access_token = r.json()["access_token"]
            token_type = r.json()["token_type"]
            authorization = {"Authorization": f"{token_type} {access_token}"}

            config["data"].update(r.json())
            session.headers.update(authorization)

            # Save Streaming identifiers
            r = session.get(INDEX_ENDPOINT)
            if r.status_code == 200:
                config["data"].update(r.json())

            # Save profile's data
            r = session.get(PROFILE_ENDPOINT)
            if r.status_code == 200:
                config["data"].update(r.json())

            return True
        return False

    def search(self, query: str, n: int=6) -> Optional[Dict]:
        """Search an anime

        Parameters:
            query (``str``):
                Query to search
            n (``int``, optional):
                Number of results to return
                Default to 6

        Returns:
            ``Dict``: On success, dictionary is returned
        """
        r = session.get(
            SEARCH_ENDPOINT,
            params = {
                "q": query,
                "n": str(n),
                "locale": self.locale
            }
        )
        if r.status_code == 200:
            return r.json()["items"]
        
    def get_seasons(self, series_id: str) -> Optional[Dict]:
        """Get seasons of an anime

        Parameters:
            series_id (``str``):
                ID of the anime

        Returns:
            ``Dict``: On success, dictionary is returned
        """
        r = session.get(
            SEASONS_ENDPOINT.format(config["data"]["cms"]["bucket"]),
            params = {
                "series_id": series_id,
                "Policy": config["data"]["cms"]["policy"],
                "Signature": config["data"]["cms"]["signature"],
                "Key-Pair-Id": config["data"]["cms"]["key_pair_id"],
                "locale": self.locale
            }
        )
        if r.status_code == 200:
            return r.json()["items"]

    def get_episodes(self, season_id: str) -> Optional[Dict]:
        """Get episodes of an anime (from season)

        Parameters:
            season_id (``str``):
                ID of a season

        Returns:
            ``Dict``: On success, dictionary is returned
        """
        r = session.get(
            EPISODES_ENDPOINT.format(config["data"]["cms"]["bucket"]),
            params = {
                "season_id": season_id,
                "Policy": config["data"]["cms"]["policy"],
                "Signature": config["data"]["cms"]["signature"],
                "Key-Pair-Id": config["data"]["cms"]["key_pair_id"],
                "locale": self.locale
            }
        )
        if r.status_code == 200:
            return r.json()["items"]

    def get_streams(self, episode: Dict) -> Optional[Dict]:
        """Get streams from an episode

        Parameters:
            episode (``Dict``):
                Pass one of the items that ``get_episodes()`` returns

        Returns:
            ``Dict``: On success, dictionary is returned
        """
        stream_id = re.search(
            r"videos\/(.+?)\/streams",
            episode["__links__"]["streams"]["href"]
        ).group(1)
        r = session.get(
            STREAMS_ENDPOINT.format(
                config["data"]["cms"]["bucket"],
                stream_id
            ),
            params = {
                "Policy": config["data"]["cms"]["policy"],
                "Signature": config["data"]["cms"]["signature"],
                "Key-Pair-Id": config["data"]["cms"]["key_pair_id"],
                "locale": self.locale
            }
        )
        if r.status_code == 200:
            return r.json()
