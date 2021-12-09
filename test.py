from crunchyroll_beta import Crunchyroll
import json

cr = Crunchyroll("it-IT")

cr.login("wrekage12@gmail.com", "craftastic12")
# GY5P48XEY

r = cr.get_episodes("GR3VC2P74")[0].id

print(r)