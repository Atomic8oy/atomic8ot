from commands import admin, main, user
from utility import log

def setup(bot):
    log("Importing admin commands")
    admin.AdminCommands(bot)
    log("Importing main commands")
    main.MainCommands(bot)
    log("Importing user commands")
    user.UserCommands(bot)