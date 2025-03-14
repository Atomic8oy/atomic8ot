from datetime import datetime

# TODO: ADD LOGGING
def log(message:str):
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S%p")
    print(f"[{time}] {message}")