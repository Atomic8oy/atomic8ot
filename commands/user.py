from interactions import (
    slash_command, slash_option, SlashContext, Extension,
    OptionType, User, Embed, EmbedFooter
)
from utility import log, CRUD
from models import Ranks, DaUser

class UserCommands(Extension):
    # PROFILE COMMAND
    @slash_command("profile", description="User profile!")
    @slash_option(
        name="user",
        description="Target user. By default its you!",
        required=False,
        opt_type=OptionType.USER
    )
    async def profile_function(self, ctx: SlashContext, user: User = None):
        log(f"[{ctx.author_id} {ctx.author.username}] /profile -> {user}")
        if user != None:
            userData:DaUser = CRUD.get(userID=user.id)
            profile = Embed(
                title= f"**{user.display_name} Profile:**",
                description= f"**ID:** {user.id}\n**Rank:** {Ranks[userData.rank]} ({userData.rank})\n**Points:** {userData.points}\n**Multiplier:** {userData.multiplier}\n**Wallet:** {userData.wallet}",
                color= 65464,
                footer= EmbedFooter(
                    text= f"{user.username}",
                    icon_url= user.display_avatar.url
                ) 
            )
        else:
            userData:DaUser = CRUD.get(ctx.author_id)
            profile = Embed(
                title= f"**{ctx.author.display_name} Profile:**",
                description= f"**ID:** {ctx.author_id}\n**Rank:** {Ranks[userData.rank]} ({userData.rank})\n**Points:** {userData.points}\n**Multiplier:** {userData.multiplier}\n**Wallet:** {userData.wallet}",
                color= 65464,
                footer= EmbedFooter(
                    text= f"{ctx.author.username}",
                    icon_url= ctx.author.display_avatar.url
                )
            )
        
        await ctx.send(content="", embed=profile)

    # RANKUP COMMAND
    @slash_command("rank_up", description="Rank up command?!")
    async def rank_up_function(self, ctx: SlashContext):
        user:DaUser = CRUD.get(ctx.author_id)

        requiredPoints = user.rank * 4 + (user.rank + 1 * 2)

        if user.points >= requiredPoints:
            user.points -= requiredPoints
            user.rank += 1
            CRUD.update(ctx.author_id, user)
            await ctx.send(f"Ranked UP!\nYour rank now: {Ranks[user.rank]} ({user.rank})")
        else:
            await ctx.send(f"You do not have enough points to rank up.\nRequired: {requiredPoints}. You need {requiredPoints-user.points} more")