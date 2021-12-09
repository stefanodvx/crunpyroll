# Crunchyroll BETA API
## Installation ⚙️
```
pip install git+https://github.com/stefanodvx/crunchyroll@main
```

## Example Code ❓
### This API requires an account, and works only on Crunchyroll BETA!
### First of all, import all stuff and login
```
from crunchyroll_beta import Crunchyroll
cr = Crunchyroll()

cr.login("email", "password")
series_id = "GY5P48XEY" # cr.search("Demon Slayer")
season_id = cr.get_seasons(series_id)[2].id
episode = cr.get_episodes(season_id)[0]

# m3u8 url
url = cr.get_streams(episode).streams.adaptive_hls.en.url
```

### You can get DASH, HLS,
### raws, subtitles only, hardsubbed videos...
### Just explore the API yourself and have fun!