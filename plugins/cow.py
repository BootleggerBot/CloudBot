import json
import random
from typing import Any, Dict, List

from cloudbot import hook
from cloudbot.bot import CloudBot
from cloudbot.util import formatting, web

cow_gifs: Dict = {}


@hook.onload()
def load_cows(bot: CloudBot) -> None:
    """load cow gifs"""
    cow_gifs.clear()
    with open(bot.data_path / "cows.json", encoding="utf-8") as json_data:
        cow_gifs.update(json.load(json_data))


@hook.command("cowdle")
def cowdle(text, chan, action):
    index = random.randint(0, len(cow_gifs["cowdle"]) - 1)
    gif = cow_gifs["cowdle"][index]
    action(gif, chan);

@hook.command("zoomies")
def zoomies(text, chan, action):
    index = random.randint(0, len(cow_gifs["zoomies"]) - 1)
    gif = cow_gifs["zoomies"][index]
    action(gif, chan);

@hook.command("eyebleach")
def eyebleach(text, chan, action):
    index = random.randint(0, len(cow_gifs["eyebleach"]) - 1)
    gif = cow_gifs["eyebleach"][index]
    action(gif, chan);