from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None) #Loda Lele
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://ibb.co/3cnmmJj")
START_IMG = getenv("START_IMG", "https://ibb.co/3cnmmJj")

SESSION = getenv("SESSION", None) #Lund Ka Scammer Hai Tu Vai.

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/wigglehobbit")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/F")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "13564690875").split()))


FAILED = "https://ibb.co/3cnmmJj"
