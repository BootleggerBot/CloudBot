import json

from cloudbot import hook

@hook.command("duckdance", autohelp=False)
def duckdance(message):
    message("https://www.youtube.com/watch?v=anW4OZ5VnZ8");

@hook.command("ricflair", autohelp=False)
def ricflair(message):
    message("WOOOO! https://media.giphy.com/media/yUI3a7RwLhOFy/giphy.gif");
