from .search import Search
from .get_index import GetIndex
from .get_profile import GetProfile
from .get_series import GetSeries
from .get_seasons import GetSeasons
from .get_episodes import GetEpisodes
from .get_streams import GetStreams
from .get_manifest import GetManifest
from .get_license import GetLicense

class Methods(
    Search,
    GetIndex,
    GetProfile,
    GetSeries,
    GetSeasons,
    GetEpisodes,
    GetStreams,
    GetManifest,
    GetLicense
):
    pass