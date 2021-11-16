import requests, re
from typing import Optional, List, Dict

ACCESS_TOKEN = "aHJobzlxM2F3dnNrMjJ1LXRzNWE6cHROOURteXRBU2Z6QjZvbXVsSzh6cUxzYTczVE1TY1k="

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

    def login(self, username: str, password: str) -> None:
        headers = session.headers
        headers.update({"Authorization": f"Basic {ACCESS_TOKEN}"})
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

    def search(self, query: str, n: int=6, locale: str="it-IT") -> Optional[Dict]:
        r = session.get(
            SEARCH_ENDPOINT,
            params = {
                "q": str(query),
                "n": str(n),
                "locale": locale
            }
        )
        if r.status_code == 200:
            return r.json()["items"]
        
    def get_seasons(self, series_id: str, locale: str="it-IT") -> Optional[Dict]:
        r = session.get(
            SEASONS_ENDPOINT.format(config["data"]["cms"]["bucket"]),
            params = {
                "series_id": series_id,
                "Policy": config["data"]["cms"]["policy"],
                "Signature": config["data"]["cms"]["signature"],
                "Key-Pair-Id": config["data"]["cms"]["key_pair_id"],
                "locale": locale
            }
        )
        if r.status_code == 200:
            return r.json()["items"]

    def get_episodes(self, season_id: str, locale: str="it-IT") -> Optional[Dict]:
        r = session.get(
            EPISODES_ENDPOINT.format(config["data"]["cms"]["bucket"]),
            params = {
                "season_id": season_id,
                "Policy": config["data"]["cms"]["policy"],
                "Signature": config["data"]["cms"]["signature"],
                "Key-Pair-Id": config["data"]["cms"]["key_pair_id"],
                "locale": locale
            }
        )
        if r.status_code == 200:
            return r.json()["items"]

    def get_streams(self, episode: Dict, locale: str="it-IT") -> Optional[Dict]:
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
                "locale": locale
            }
        )
        if r.status_code == 200:
            return r.json()

    def get_formats(self, streams: Dict) -> Optional[List]:
        video_url = streams["streams"]["adaptive_hls"]["it-IT"]["url"]
        hls_streams = requests.get(video_url).text
        items = hls_streams.split("#EXT-X-STREAM")
        formats = []
        # Parse formats in m3u8
        for item in items:
            if "RESOLUTION" in item:
                resolution = re.search(
                    r"RESOLUTION=(?:\d+)x(\d+)",
                    item
                ).group(1)
                formats.append({"url": item.split("\n")[1], "height": int(resolution)})
        return formats