from interactions import (
    Activity, Client, Intents, listen
)
from config import (
    BOT_TOKEN, ACTIVITY_TYPE, ACTIVITY_MESSAGE
)
from utility import log
import interactions

bot = Client(
    activity=Activity(ACTIVITY_MESSAGE, type=ACTIVITY_TYPE),
    intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
    sync_interactions=True
)

@listen()
async def on_startup():
    log("Bot is Online")

log("Starting the bot")
bot.load_extension("commands")
bot.start(token=BOT_TOKEN)