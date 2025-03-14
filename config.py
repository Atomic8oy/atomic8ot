from decouple import config
from dotenv import load_dotenv

from exceptions import InvalidVariable

load_dotenv()

BOT_TOKEN = config("BOT_TOKEN", default=None)

if not BOT_TOKEN:
    raise InvalidVariable("BOT_TOKEN CAN NOT BE EMPTY")


activity_type = config("ACTIVITY_TYPE", default=None)

if activity_type:
    if activity_type.isnumeric() and int(activity_type) not in [0,1,2,3,5]:
        ACTIVITY_TYPE = 0
        raise InvalidVariable("ACTIVITY_TYPE IS INVALID") # BROKEN?
    else:
        ACTIVITY_TYPE = activity_type


ACTIVITY_MESSAGE = config("ACTIVITY_MESSAGE", default=None)


temp:str = config("ADMIN_IDS", default="")
if "," in temp:
    ADMIN_IDS = temp.split(",")
else:
    ADMIN_IDS = temp