from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "28243586"))
API_HASH = getenv("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

BOT_TOKEN = getenv("BOT_TOKEN", "7714254527:AAFU4rOeoaab_T4ytlf0G_TQMXZFOTDcekI")
OWNER_ID = int(getenv("OWNER_ID", "6551906246"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://madarazbotz:IMpkK5ZoxUNI89Xu@cluster0.vufqb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "vr_unreal")
DAXX_API = getenv("DAXX_API", "daxx-1490?api+key:free")
