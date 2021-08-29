import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client
from pyromod import listen


API_ID = int(os.environ.get("1677067", 0))
API_HASH = os.environ.get("0d8c8aabe36b01db6a26a7f2780fa660", None)
BOT_TOKEN = os.environ.get("1961455193:AAHtifb6YYiJjk-WII2gtU-A_Hzb_A0-roU", None)
API_KEY = os.environ.get("AAHtifb6YYiJjk-WII2gtU-A_Hzb_A0-roU", None)


def main():
    plugins = dict(root="plugins")
    app = Client("String Session",
                 bot_token=BOT_TOKEN,
                 api_id=API_ID,
                 api_hash=API_HASH,
                 plugins=plugins,
                 workers=100)

    app.run()


if __name__ == "__main__":
    main()
