from interactions import (
    slash_command, slash_option, SlashContext, Extension,
    OptionType, SlashCommandChoice
)
from utility import log, CRUD
from models import RpsOptions, Coin
from random import randint

class MainCommands(Extension):

    # PING COMMAND
    @slash_command("ping", description="Testing if the bot works")
    async def ping_function(self, ctx:SlashContext):
        log(f"[{ctx.author_id} {ctx.author.username}] - /ping")
        await ctx.send("Pong!")

    # RANDOM COMMAND
    @slash_command("random", description="Generate a random number in provided range.")
    @slash_option(
        name="min",
        description="Minimum number in range.",
        required=True,
        opt_type=OptionType.INTEGER,
        argument_name="minNum"
    )
    @slash_option(
        name="max",
        description="Maximum number in range.",
        required=True,
        opt_type=OptionType.INTEGER,
        argument_name="max"
    )
    async def random_function(self, ctx: SlashContext, minNum: int, max: int):
        if max > minNum:
            outNum = randint(minNum, max)
            log(f"[{ctx.author_id} {ctx.author.username}] /random -> {outNum}")
            await ctx.send(outNum)
        else:
            await ctx.send("Entered values are not valid!", delete_after=5.0)

    # RPS COMMAND
    @slash_command("rps", description="Rock, Paper, Scissors")
    @slash_option(
        name="user",
        description="Your choice",
        required=True,
        opt_type=OptionType.INTEGER,
        choices=[
            SlashCommandChoice("Rock", 0),
            SlashCommandChoice("Paper", 1),
            SlashCommandChoice("Scissors", 2)
        ]
    )
    async def rps_function(self, ctx: SlashContext, user: int):
        code = randint(0,2)
        status = 2 # USER WON 0 / CODE WON 1 / TIED 2
        if user == code:
            status = 2
        elif user == 0 and code == 1:
            status = 1
        elif user == 0 and code == 2:
            status = 0
        elif user == 1 and code == 0:
            status = 0
        elif user == 1 and code == 2:
            status = 1
        elif user == 2 and code == 0:
            status = 1
        elif user == 2 and code == 1:
            status = 0
        else:
            log(f"[{ctx.author_id} {ctx.author.username}] /RPS -> {user} - {code} (wtf???)")
            status = 2
        
        log(f"[{ctx.author_id} {ctx.author.username}] /RPS -> {user} - {code}")

        if status == 0:
            userData = CRUD.get(ctx.author_id)
            userData['points'] += userData['multiplier']
            CRUD.update(ctx.author_id, userData)
            await ctx.send(f"You Won! {RpsOptions[user]} - {RpsOptions[code]}\nYou earned {userData['multiplier']} points. Total: {userData['points']}")
        elif status == 1:
            await ctx.send(f"You Lost! {RpsOptions[user]} - {RpsOptions[code]}")
        elif status == 2:
            await ctx.send(f"We got tied! {RpsOptions[user]} - {RpsOptions[code]}")

    # GUESS COMMAND
    @slash_command("guess", description="Guess the number!")
    @slash_option(
        name="max",
        description="Maximum number to guess (from 0 to this number)",
        required=True,
        opt_type=OptionType.INTEGER,
        choices=[
            SlashCommandChoice("10", value=10),
            SlashCommandChoice("100", value=100),
            SlashCommandChoice("1000", value=1000),
            SlashCommandChoice("10000", value=10000)
        ]
    )
    @slash_option(
        name="guess",
        description="Your guessed number",
        required=True,
        opt_type=OptionType.INTEGER
    )
    async def guess_function(self, ctx: SlashContext, max: int, guess: int):
        if guess < 0 or guess > max:
            log(f"[{ctx.author_id} {ctx.author.username}] /random {max}, {guess} -> (INVALID)")
            await ctx.send(f"Guessed number is not in range (should be between 0-{max})")
            return None

        number = randint(0 , max)

        log(f"[{ctx.author_id} {ctx.author.username}] /random {max}, {guess} -> {number}")

        if number == guess:
            user = CRUD.get(ctx.author_id)
            earned  = int(user['multiplier'] * (max / 10))
            user['points'] += earned
            CRUD.update(ctx.author_id, user)
            await ctx.send(f"YOU WON!!!\nAnd you got {earned} points. Your Total points: {user['points']}")

        else:
            await ctx.send(f"Better luck next time.\nThe number was {number}")

    # COIN FLIP COMMAND
    @slash_command("coin", description="Flip a coin!")
    async def coin_function(self, ctx: SlashContext):
        pos = randint(0,1)
        log(f"[{ctx.author_id} {ctx.author.username}] /coin -> {pos}")
        await ctx.send(Coin[pos])