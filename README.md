# Crunchyroll BETA API
## Installation ⚙️
```
pip install git+https://github.com/stefanodvx/crunchyroll@main
```

## Basic Usage ❓
### This API requires an account, and works only on Crunchyroll BETA!
### First of all, import all stuff and login
```
from crunchyroll_beta import Crunchyroll
cr = Crunchyroll()

cr.login("email", "password")
```
### To get a SERIES_ID, just use search function
```
cr.search("Demon Slayer")
```
### Check the dict it returns, and do whatever you want, like getting seasons
```
cr.get_seasons(series_id)
```
### From there get your SEASON_ID and get episodes
```
cr.get_episodes(season_id)
```
### Now let's get streams from an episode (pass the dict get_episodes() returns)
```
cr.get_streams(episode)
```
### Finally, get formats (pass the dict get_streams() returns)
```
cr.get_formats(streams)
```
## For every function, except login, you can pass
## "locale" argument (like us-US, en-ES). Default to: it-IT.
## You can only get HARDSUBS, I could change this but Im not interested
## in continuing this project for now, PRs are welcome :D
