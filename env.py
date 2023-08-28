import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "27477919").strip()
API_HASH = os.getenv("API_HASH", "b25cce1727f6d33d41d9e00e3ed62583").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6644469889:AAHMW1W1ESZvMFW8ij7-13vMmXGcMNXO3-8").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/def_Zoka")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
