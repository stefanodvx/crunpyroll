from .obj import Object

from typing import Dict

class Profile(Object):
    def __init__(self, data: Dict):
        self.avatar: str = data.get("avatar")
        self.beta: bool = data.get("cr_beta_opt_in")
        self.email_verified: bool = data.get("crleg_email_verified")
        self.email: str = data.get("email")
        self.maturity_rating: str = data.get("maturity_rating")
        self.preferred_language: str = data.get("preferred_communication_language")
        self.preferred_subtitle_language: str = data.get("preferred_content_subtitle_language")
        self.profile_name: str = data.get("profile_name")
        self.username: str = data.get("username")