from interactions import (
    slash_command, slash_option, SlashContext, Extension,
    OptionType, User, check
)

from utility import log, isAdmin, CRUD
from models import DaUser

class AdminCommands(Extension):
    # GIVE_POINTS COMMAND
    @slash_command("give_points", description="Admin command to give someone points")
    @slash_option(
        name="target",
        description="User to give points",
        required=True,
        opt_type=OptionType.USER
    )
    @slash_option(
        name="points",
        description="Points to give",
        required=True,
        opt_type=OptionType.INTEGER
    )
    @check(isAdmin)
    async def add_points_function(self, ctx:SlashContext, target:User, points:int):
        userCRUD = CRUD(target.id)
        user = userCRUD.get()
        user.points += points
        userCRUD.update(user)
        log(f"[{ctx.author_id} {ctx.author.username}] Added {points} to [{target.id} {target.username}]")
        await ctx.send(f"Added {points} to {target.display_name}!")

