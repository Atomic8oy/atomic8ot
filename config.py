from decouple import config
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = config("BOT_TOKEN", default=None)

if not BOT_TOKEN:
    raise InvalidVariable("BOT_TOKEN CAN NOT BE EMPTY")
