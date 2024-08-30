from interactions import (
    Activity, Client, Intents, listen, ButtonStyle, ActionRow
)
from interactions.api.events import Component
from config import (
    BOT_TOKEN, ACTIVITY_TYPE, ACTIVITY_MESSAGE
)
from utility import log

bot = Client(
    activity=Activity(ACTIVITY_MESSAGE, type=ACTIVITY_TYPE),
    intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
    sync_interactions=True
)

@listen()
async def on_startup():
    log("Bot is Online")

@listen()
async def on_component(event: Component):
    ctx = event.ctx
    compDT = ctx.custom_id.split("|")

    if compDT[0] == "trivia":
        finComps = ActionRow()
        if compDT[2] == "0":

            for compDict in ctx.message.components[0].to_dict()['components']:
                if compDict['custom_id'] == ctx.custom_id:
                    compDict['style'] = ButtonStyle.GREEN
                else:
                    compDict['style'] = ButtonStyle.GRAY
                compDict['disabled'] = True

                finComps.add_component(compDict)
            
            await ctx.send("Correct!")
        else:
            for compDict in ctx.message.components[0].to_dict()["components"]:
                if compDict['custom_id'] == ctx.custom_id:
                    compDict['style'] = ButtonStyle.RED
                elif compDict['custom_id'].split("|")[2] == '0':
                    compDict['style'] = ButtonStyle.GREEN
                compDict['disabled'] = True

                finComps.add_component(compDict)
                
            await ctx.send("Wrong.")
        
        await ctx.message.edit(content=ctx.message.content, components=finComps)

log("Starting the bot")
bot.load_extension("commands")
bot.start(token=BOT_TOKEN)