from datetime import datetime
from uuid import uuid4

PUBLIC_TOKEN = "b2VkYXJteHN0bGgxanZhd2ltbnE6OWxFaHZIWkpEMzJqdVY1ZFc5Vk9TNTdkb3BkSnBnbzE="

DEVICE_NAME = "RMX2170"
DEVICE_TYPE = "realme RMX2170"
DEVICE_ID = str(uuid4())

def get_api_headers(headers: dict | None) -> dict:
    return {
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Crunchyroll/3.46.2 Android/13 okhttp/4.12.0"
    } | (headers or {})

def get_date() -> datetime: 
    return datetime.utcnow()

def date_to_str(date: datetime) -> str | None: 
    try:
        return "{}-{}-{}T{}:{}:{}Z".format(
            date.year, date.month,
            date.day, date.hour,
            date.minute, date.second
        )
    except Exception:
        return

def str_to_date(string: str) -> datetime | None:
    try:
        return datetime.strptime(
            string,
            "%Y-%m-%dT%H:%M:%SZ"
        )
    except Exception:
        return