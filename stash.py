from config import config
from .stashapi import log
from .stashapi.stashapp import StashInterface

# TODO: ENV VARS
SCHEMA='https'
DOMAIN='stash'
PORT=''

stash = StashInterface({
    "scheme": config['stash']['schema'],
    "domain":config['stash']['domain'],
    "port": config['stash']['port'],
    "logger": log
})