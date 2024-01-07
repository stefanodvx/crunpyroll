from enum import Enum

class APIHost(Enum):
    """API hosts enumeration."""
    
    WEB = "www.crunchyroll.com"
    "Universal WWW host. Mostly used on web applications."

    BETA = "beta-api.crunchyroll.com"
    "Beta-API host. Mostly used on mobile applications."

    PLAY_SERVICE = "cr-play-service.prd.crunchyrollsvc.com"
    "SVC host used for video players."

    LICENSE = "cr-license-proxy.prd.crunchyrollsvc.com"
    "SVC host used for license."