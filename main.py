from interactions import Client, Intents, listen
from utils import log

from config import BOT_TOKEN

bot = Client(
    intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
    sync_interactions=True
)


@listen()
async def on_startup():
    log("Bot startup", 20)

bot.load_extension("commands")

if BOT_TOKEN:
    bot.start(token=BOT_TOKEN)