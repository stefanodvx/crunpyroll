from dataclasses import dataclass
from datetime import datetime

@dataclass
class Session:
    access_token: str
    refresh_token: str
    expiration: datetime