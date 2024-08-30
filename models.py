from interactions import SlashCommandChoice
from json import loads

class DaUser(): # the word User was already taken by interactions so... yeah
    def __init__(self, userList:list = None)-> None:
        self.id = userList['id'] if userList else None
        self.points = userList['points'] if userList else 0
        self.wallet = userList['wallet'] if userList else 0
        self.rank = userList['rank'] if userList else 1
        self.multiplier = userList['multiplier'] if userList else 1
        self.trivia = userList['trivia'] if userList else []

    def get_dict(self)-> dict:
        return {
            "id": self.id,
            "points": self.points,
            "wallet": self.wallet,
            "rank": self.rank,
            "multiplier": self.multiplier
        }
 
RPS_OPTIONS = ["Rock", "Paper", "Scissors"]

COIN = ["Heads", "Tails"]

_file = open("database/trivia.json", 'r')
TRIVIA:dict = loads(_file.read())
_file.close()

QUESTION_TOPICS = [ SlashCommandChoice(x.title().replace("_", " "), x) for x in TRIVIA.keys()]

RANKS = [ "God???",
    "Bronze I", "Bronze II", "Bronze III", "Bronze IV",
    "Silver I", "Silver II", "Silver III", "Silber IV",
    "Gold I", "Gold II", "Gold III", "Gold IV",
    "Diamond I", "Diamond II", "Diamond III", "Diamond IV",
    "Obsidian I", "Obsidian II", "Obsidian III", "Obsidian IV", "Obsidian V"
    "Void"
]