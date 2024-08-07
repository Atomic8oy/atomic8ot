from interactions import BaseContext
import datetime
import logging
import json
import os

from models import DaUser
from config import ADMIN_IDS

logging.basicConfig(
    filename=f'log/{datetime.datetime.now().strftime("%Y-%m-%d")}.log',
    format='%(asctime)s %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger()

def log(message:str)-> None:
    print(f"[{datetime.datetime.now().strftime("%Y/%m/%d %I:%M:%S%p")}] {message}")
    logger.debug(message)

class CRUD():
    def __init__(self) -> None:
        pass
    
    def create(self, userID:int)-> DaUser:
        file = open(f"database/{userID}.json", 'w')
        user = DaUser()
        user.id = userID
        file.write(json.dumps(user))
        file.close()
        log(f"User {userID} Created")
        return user

    def get(self, userID:int)-> DaUser:
        try:
            file = open(f"database/{userID}.json", 'r')
            jsonRaw = file.read()
            file.close()
            log(f"User {userID} Accessed")
            return DaUser(json.loads(jsonRaw))
        except:
            log(f"[WARNING] EXCEPTION ON GET USER: {userID}")
            return self.create(userID)
        
    def update(self, userID:int, data:DaUser)-> None:
        file = open(f"database/{userID}.json", 'w')
        file.write(json.dumps(data))
        file.close()
        log(f"User {userID} Updated")

    def delete(self, userID:int)-> bool:
        if os.path.exists(f"database/{userID}.json"):
            os.remove(f"database/{userID}.json")
            return True
        else:
            return False

async def isAdmin(ctx: BaseContext)-> bool:
    if str(ctx.author_id) in ADMIN_IDS:
        return True
    else:
        return False