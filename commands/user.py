from interactions import (
    slash_command, slash_option, SlashContext, Extension,
    OptionType, User, Embed, EmbedFooter, MISSING
)
from utility import log, CRUD
from models import RANKS, DaUser

class UserCommands(Extension):
    # PROFILE COMMAND
    @slash_command("profile", description="User profile!")
    @slash_option(
        name="user",
        description="Target user. By default its you!",
        required=False,
        opt_type=OptionType.USER
    )
    async def profile_function(self, ctx:SlashContext, user:User = MISSING):
        log(f"[{ctx.author_id} {ctx.author.username}] /profile -> {user}")
        if user:
            userCRUD = CRUD(user.id)
            userData:DaUser = userCRUD.get()
            profile = Embed(
                title= f"**{user.display_name} Profile:**",
                description= f"**ID:** {user.id}\n**Rank:** {RANKS[userData.rank]} ({userData.rank})\n**Points:** {userData.points}\n**Multiplier:** {userData.multiplier}\n**Wallet:** {userData.wallet}",
                color= 65464,
                footer= EmbedFooter(
                    text= f"{user.username}",
                    icon_url= user.display_avatar.url
                ) 
            )
        else:
            userCRUD = CRUD(ctx.author_id)
            userData:DaUser = userCRUD.get()
            profile = Embed(
                title= f"**{ctx.author.display_name} Profile:**",
                description= f"**ID:** {ctx.author_id}\n**Rank:** {RANKS[userData.rank]} ({userData.rank})\n**Points:** {userData.points}\n**Multiplier:** {userData.multiplier}\n**Wallet:** {userData.wallet}",
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
        userCRUD = CRUD(ctx.author_id)
        user:DaUser = userCRUD.get()

        requiredPoints = user.rank * 4 + (user.rank + 1 * 2)

        if user.points >= requiredPoints:
            user.points -= requiredPoints
            user.rank += 1
            userCRUD.update(user)
            await ctx.send(f"Ranked UP!\nYour rank now: {RANKS[user.rank]} ({user.rank})")
        else:
            await ctx.send(f"You do not have enough points to rank up.\nRequired: {requiredPoints}. You need {requiredPoints-user.points} more")