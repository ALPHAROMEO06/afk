#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID","13191216"))
API_HASH = getenv("API_HASH","7d38e4760cb8717cd434e8f449d65b16")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","5976449311:AAFKBrj-cAZHovTxYdX8thSHDahSF9sbCEs")

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ZAID:ZAID@cluster0.8smkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "1953140355").split())
)  # Input type must be interger
