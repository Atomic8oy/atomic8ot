from decouple import config
from dotenv import load_dotenv
from interactions import ActivityType

load_dotenv()

BOT_TOKEN = config("BOT_TOKEN", default=False)

match config("ACTIVITY_TYPE", default="PLAYING"):
    case "COMPETING":
        ACTIVITY_TYPE = ActivityType.COMPETING    
    case "GAME":
        ACTIVITY_TYPE = ActivityType.GAME
    case "LISTENING":
        ACTIVITY_TYPE = ActivityType.LISTENING
    case "STREAMING":
        ACTIVITY_TYPE = ActivityType.STREAMING
    case "WATCHING":
        ACTIVITY_TYPE = ActivityType.WATCHING
    case _:
        ACTIVITY_TYPE = ActivityType.PLAYING

ACTIVITY_MESSAGE = config("ACTIVITY_MESSAGE", default=None)


temp:str = config("ADMIN_IDS", default="")
if "," in temp:
    ADMIN_IDS = temp.split(",")
else:
    ADMIN_IDS = temp