from decouple import config
from dotenv import load_dotenv
from interactions import ActivityType

load_dotenv()

BOT_TOKEN = config("BOT_TOKEN", default=False)

temp = config("ACTIVITY_TYPE", default="PLAYING")
if temp == "COMPETING":
    ACTIVITY_TYPE = ActivityType.COMPETING
elif temp == "GAME":
    ACTIVITY_TYPE = ActivityType.GAME
elif temp == "LISTENING":
    ACTIVITY_TYPE = ActivityType.LISTENING
elif temp == "STREAMING":
    ACTIVITY_TYPE = ActivityType.STREAMING
elif temp == "WATCHING":
    ACTIVITY_TYPE = ActivityType.WATCHING
else:
    ACTIVITY_TYPE = ActivityType.PLAYING

ACTIVITY_MESSAGE = config("ACTIVITY_MESSAGE", default=None)


temp:str = config("ADMIN_IDS", default="")
if "," in temp:
    ADMIN_IDS = temp.split(",")
else:
    ADMIN_IDS = temp