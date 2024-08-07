class DaUser():
    def __init__(self, userList: list  | None)-> None:
        self.id = userList['id'] if userList else None
        self.points = userList['points'] if userList else 0
        self.wallet = userList['wallet'] if userList else 0
        self.rank = userList['rank'] if userList else 1
        self.multiplier = userList['multiplier'] if userList else 1
 
RpsOptions = ["Rock", "Paper", "Scissors"]

Coin = ["Heads", "Tails"]

Ranks = [ "God???",
    "Bronze I", "Bronze II", "Bronze III", "Bronze IV",
    "Silver I", "Silver II", "Silver III", "Silber IV",
    "Gold I", "Gold II", "Gold III", "Gold IV",
    "Diamond I", "Diamond II", "Diamond III", "Diamond IV",
    "Obsidian I", "Obsidian II", "Obsidian III", "Obsidian IV", "Obsidian V"
    "Void"
]