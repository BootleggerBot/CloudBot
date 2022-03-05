import json

from cloudbot import hook

@hook.command("duckdance", autohelp=False)
def duckdance(message):
    message("https://www.youtube.com/watch?v=anW4OZ5VnZ8");

@hook.command("ricflair", autohelp=False)
def ricflair(message):
    message("WOOOO! https://media.giphy.com/media/yUI3a7RwLhOFy/giphy.gif");

@hook.command("stitchgif", autohelp=False)
def stitchgif(message):
    message("https://gifimage.net/wp-content/uploads/2018/11/spray-water-bottle-gif-2.gif");

@hook.command("redalert", autohelp=False)
def redalert(message):
    message("https://i.imgur.com/KmzBy9G.gif");

@hook.command("repo", autohelp=False)
def repo(message):
    message("https://github.com/BootleggerBot/CloudBot");

@hook.command("dickdance", autohelp=False)
def dickdance(message):
    message("https://imgur.com/jtM3a0j - NSFW");

@hook.command("wiggle", autohelp=False)
def wiggle(message):
    message("https://i.imgur.com/z1nMKqQ.gif");

@hook.command("shake", autohelp=False)
def shake(message):
    message("https://media.giphy.com/media/4KFvJomr6nt92hCWu4/giphy.gif");
