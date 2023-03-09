#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 17809227
API_HASH = "24c6288eee3e68db783afaf3df669534"
BOT_TOKEN = "5105784060:AAEuQbnUpzwHslcL_cyoArS5F1Q2IVtN_Qk"
AUTH = 1414938408
FORCESUB = "safalam_clssses"
SESSION = "BQAv3AV1FipqJcAAZ0VMwrOH-8MaBt07cSOswapa24CdPa1TcYJxRpZw1PB_K89vqpGJHMI4jl5p95-qQ7trrbpblI0scwlnZehK5h1Wfb9yKVIeh3TJaEM39nGLKEUAEh3rIaRYwOvBQNbDe-bq5-XHnakL1pF2TnL-GSv9h4sjnA-45G1OZnuoO2256k4cr45tO96K1SZr1PAeW5tqCP9w-tBGGNvBODxyh1kfJB9xRSjaGFyzq7rR9dvrOgveO6OP6TMMAdJf-aimf1SoOLt3U7LonX-jCRfhv_qYN2FW4032QVcns-qoCW3uOtZdUJRy8Ze56kPXtHXKXMXBWsJXVFY_KAA"

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
