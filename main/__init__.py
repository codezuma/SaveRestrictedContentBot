#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables

API_ID = "17809227"
API_HASH = "24c6288eee3e68db783afaf3df669534"
BOT_TOKEN = "5105784060:AAEuQbnUpzwHslcL_cyoArS5F1Q2IVtN_Qk"
SESSION = "BQC08BE0IT1IBIQ-R4apX0wND9vVaD3DP4dUHCUTtqd1mrvrkl1tzorC8zeZahm9i49Pc1z2hy0TDuI3fxiuEhpMmVMfv5eKTszx5ulY2utyRycBSCV0oTgynTKNQBsMgcsQyjyDzBq8n_IiaWj4YaLebtDQsje9YNMsu6jzcH1D3TBSwSqY8vjThMkGh_vFc4yH4TgwKR8vVocORkWfzBftfGePM_iDpjcTJqVwfVkwxoDnVGL3yhpsbioVzkwPNnEfLlGlyweYP5IHBhX1xwPTkzL3Urpl4m_orIcWfrEQs4t5qZOLNYFK3DhGDpw8XB35iO4lxN9Q8XvQoYtFbrTXVFY_KAA"
FORCESUB = "Marvel_movies_hindi_fhd"
AUTH = "1414938408"

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)


bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
