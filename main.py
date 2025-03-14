from interactions import (
    Activity, Client, Intents, listen, slash_command, SlashContext
)
from interactions.api.events import Component

from utils import log
from config import BOT_TOKEN, ACTIVITY_TYPE, ACTIVITY_MESSAGE   

if ACTIVITY_TYPE:
    act = Activity(ACTIVITY_MESSAGE, ACTIVITY_TYPE)  
else: 
    act = None

bot = Client(
    activity=act,
    intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
    sync_interactions=True
)

@slash_command("ping", description="Bot Ping!")
async def ping_function(ctx:SlashContext):
    await ctx.send("Pong!")
    log(f"[{ctx.author_id}] -> /ping")

@listen()
async def on_startup():
    log("BOT STARTUP")

@listen()
async def on_component(event: Component):
    pass

# bot.load_extension("commands")

if BOT_TOKEN:
    bot.start(token=BOT_TOKEN)