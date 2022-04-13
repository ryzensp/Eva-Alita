from pyrogram import idle, Client, filters
from config import PREFIX
from Zect import app, LOGGER
import logging
from Zect.modules import *

app.start()
me = app.get_me()
print(f"Zect UserBot started for user {me.id}. Type {PREFIX}help in any telegram chat.")
idle()
