<img src="https://i.imgur.com/y3L6XfN.png" align="right" />

## Crunpyroll 2.0 is HERE!
- Fully async ([httpx](https://www.python-httpx.org/))
- Python 3.11 support
- Clean and modern code
- Updated to latest Crunchyroll API
### Installation ⚙️
```bash
pip install git+https://github.com/stefanodvx/crunpyroll@main
```

### Example Code ❓
```py3
import crunpyroll
import asyncio

client = crunpyroll.Client(
    email="email",
    password="password",
    locale="it-IT"
)
async def main():
    # Start client and login
    await client.start()
    # Search for Attack on Titan
    query = await client.search("Attack On Titan")
    series_id = query.items[0].id
    print(series_id)
    # Retrieve all seasons of the series
    seasons = await client.get_seasons(series_id)
    print(seasons)

with asyncio.Runner() as runner:
    runner.run(main())
```
### Downloading content 🔑
Crunchyroll has recently integrated the **Widevine Digital Rights Management (DRM)** system, resulting in challenges for certain users attempting to download content from the platform. Subsequently, the following provides an illustrative example of obtaining decryption keys through the utilities of the [pywidevine](https://github.com/devine-dl/pywidevine) library and an L3 Content Decryption Module (CDM).
```py3
from pywidevine.cdm import Cdm
from pywidevine.pssh import PSSH
from pywidevine.device import Device
...
device = Device.load("l3cdm.wvd")
cdm = Cdm.from_device(device)
# Get streams of the episode/movie
streams = await client.get_streams("GRVDQ1G4R")
# Get manifest of the format you prefer
manifest = await client.get_manifest(streams.hardsubs[0].url)
# print(manifest)
# Get Widevine PSSH from manifest
pssh = PSSH("AAAAoXBzc2gAAAAA7e.........")
session_id = cdm.open()
challenge = cdm.get_license_challenge(session_id, pssh)
license = await client.get_license(
    streams.media_id,
    challenge=challenge,
    token=streams.token
)
cdm.parse_license(session_id, license)
for key in cdm.get_keys(session_id, "CONTENT"):
    print(f"{key.kid.hex}:{key.key.hex()}")
cdm.close(session_id)
```
##### Output:
```bash
056ec1ca849e350181753cacc9bd404b:2307a188ecd8de3859b71b30791f171d
```
###### Decryption keys are universally applicable to both video and audio streams, maintaining consistency across all available formats.

### TODO 📄
- Add support for token login
- Add support for visitor view (authless)
- Add support for Music
- Add missing documentation
- Add missing API methods