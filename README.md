<img src="https://camo.githubusercontent.com/1ef79a2b6f8fa7a4007849fd65448ca5a15146bad6ff47661c2d0f82984f1df1/68747470733a2f2f7374617469632e6372756e636879726f6c6c2e636f6d2f63787765622f6173736574732f696d672f6e6577732f6c65616e696e675f68696d652e706e67" align="right" />

## Crunchyroll BETA API
### Installation ⚙️
```bash
pip install git+https://github.com/stefanodvx/crunchyroll@main
```

### Example Code ❓
This API **requires an account**, and works only on Crunchyroll BETA!
```python3
from crunchyroll_beta import Crunchyroll
cr = Crunchyroll()

cr.login("email", "password")
series_id = "GY5P48XEY" # cr.search("Demon Slayer")
season_id = cr.get_seasons(series_id)[2]["id"]
episodes = cr.get_episodes(season_id)
streams = cr.get_streams(episodes[0])
url = streams["streams"]["adaptive_hls"]["en-US"]["url"] # m3u8 url
```

You can get DASH, HLS, raws, subtitles only, hardsubbed videos... Just **explore the API yourself** and have fun!
