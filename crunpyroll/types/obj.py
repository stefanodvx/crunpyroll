from datetime import datetime
from enum import Enum

import json
import typing

class Object:
    @staticmethod
    def default(obj: "Object"):
        if isinstance(obj, bytes):
            return repr(obj)
        if isinstance(obj, typing.Match):
            return repr(obj)
        if isinstance(obj, Enum):
            return str(obj)
        if isinstance(obj, datetime):
            return str(obj)
        return {
            attr: (
                "*" * 9 if attr in (
                    "refresh_token",
                    "access_token",
                    "password"
                )
                else getattr(obj, attr)
            )
            for attr in filter(
                lambda x: getattr(obj, x) != None,
                obj.__dict__
            )
        }

    def __str__(self) -> str:
        return json.dumps(
            self,
            indent=4,
            default=Object.default,
            ensure_ascii=False
        )