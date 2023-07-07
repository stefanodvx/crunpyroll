from datetime import datetime
from uuid import uuid4

API_DOMAIN = "https://beta-api.crunchyroll.com/"
PUBLIC_TOKEN = "ZGE4NWw0aWZxaXZucTEtanJ4d2Y6UVlRX0xoY3M4LVgtTlFadnNOWW0zRGlEbHV5ejQwaWo="

DEVICE_NAME = "RMX2170"
DEVICE_TYPE = "realme RMX2170"
DEVICE_ID = str(uuid4())

def base_api_headers() -> dict:
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Crunchyroll/3.35.0 Android/10 okhttp/4.9.2"
    }
    return headers

def get_date() -> datetime: 
    return datetime.utcnow()

def date_to_str(date: datetime) -> str: 
    return "{}-{}-{}T{}:{}:{}Z".format(
        date.year, date.month,
        date.day, date.hour,
        date.minute, date.second
    )

def str_to_date(string: str) -> datetime: 
    return datetime.strptime(string, "%Y-%m-%dT%H:%M:%SZ")