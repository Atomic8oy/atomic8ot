from datetime import datetime
from logging import basicConfig, getLogger, getLevelName

basicConfig(
    filename=f'log/{datetime.datetime.now().strftime("%Y-%m-%d")}.log',
    format='%(asctime)s %(message)s',
    level=10
)

logger = getLogger()

def log(message: str, level:int = 10)-> None:
    """level: DEBUG = 10, INFO = 20, WARNING = 30, ERROR = 40, CRITICAL = 50"""

    print(f"[{datetime.now().strftime("%Y/%m/%d %I:%M:%S%p")}] [{getLevelName(level)}] {message}")
    logger.log(level, message)