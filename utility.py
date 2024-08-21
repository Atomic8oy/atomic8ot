from interactions import BaseContext
from json import dumps, loads
import datetime
import logging
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
    def __init__(self, userID) -> None:
        try:
            file = open(f"database/users/{userID}.json", 'r')
            self._user = loads(file.read())
            file.close()
            log(f"User {userID} readed")
        except FileNotFoundError:
            file = open(f"database/users/{userID}.json", 'w')
            user = DaUser()
            user.id = userID
            file.write(dumps(user.get_dict()))
            file.close()
            log("User {userID} created")
            self.__init__(userID)

    def get(self)-> DaUser:
        log(f"User {self._user['id']} accessed")
        return DaUser(self._user)
        
    def update(self, data:DaUser)-> None:
        self._user = data.get_dict()
        file = open(f"database/users/{self._user['id']}.json", 'w')
        file.write(dumps(self._user))
        file.close()
        log(f"User {self._user['id']} Updated")

    def delete(self, userID:int)-> bool:
        if os.path.exists(f"database/users/{userID}.json"):
            os.remove(f"database/users/{userID}.json")
            return True
        else:
            return False

async def isAdmin(ctx: BaseContext)-> bool:
    if str(ctx.author_id) in ADMIN_IDS:
        return True
    else:
        return False