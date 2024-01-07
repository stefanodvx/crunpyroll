from .obj import Object

from typing import Dict

class Profile(Object):
    """
    Info about current profile.

    Parameters:
        avatar (``str``):
            Avatar of the account.

        email_verified (``bool``):
            True, if email is verified.

        email (``str``):
            Email of the account.

        maturity_rating (``str``):
            Maturity rating of the account.

        preferred_language (``str``):
            Preferred language for communication.

        preferred_subtitle_language (``str``):
            Preferred subtitles language for content.

        profile_name (``str``):
            Name of the profile.

        username (``str``):
            Username of the account.
    """
    def __init__(self, data: Dict):
        self.avatar: str = data.get("avatar")
        self.email_verified: bool = data.get("crleg_email_verified")
        self.email: str = data.get("email")
        self.maturity_rating: str = data.get("maturity_rating")
        self.preferred_language: str = data.get("preferred_communication_language")
        self.preferred_subtitle_language: str = data.get("preferred_content_subtitle_language")
        self.profile_name: str = data.get("profile_name")
        self.username: str = data.get("username")