from interactions import slash_command, SlashContext, Extension

from utils import log

class MainCommands(Extension):
    @slash_command("ping", description="Bot Ping!")
    async def ping_command(ctx:SlashContext):
        await ctx.send("Pong!")
        log(f"[{ctx.author_id}] -> /ping")