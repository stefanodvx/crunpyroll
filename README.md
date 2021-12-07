<img src="https://i.imgur.com/y3L6XfN.png" align="right" />

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

<img src="https://static.crunchyroll.com/cxweb/assets/img/news/news_yuzu.png" align="left" />

<p>
  You can get DASH, HLS, raws, subtitles only, hardsubbed videos...
  <br>
  Just <b>explore the API yourself</b> and have fun!
  <br><br>
  <a href="https://www.buymeacoffee.com/stefanodvx" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>
