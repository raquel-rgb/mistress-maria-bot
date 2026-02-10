import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("MISTRESS_BOT_TOKEN", "")

if not BOT_TOKEN:
    raise ValueError("MISTRESS_BOT_TOKEN not set in environment variables!")

# Bot metadata
BOT_NAME = "Mistress Maria"
BOT_USERNAME = "@MistressMariaDomme"

# Tribute levels
TRIBUTE_LEVELS = {
    "bronze": {"name": "Bronze", "amount": "$25", "description": "mínimo para hablarme"},
    "silver": {"name": "Silver", "amount": "$100", "description": "mi atención por 10 min"},
    "gold": {"name": "Gold", "amount": "$500", "description": "sesión privada 30 min"},
    "platinum": {"name": "Platinum", "amount": "$1000+", "description": "considerado para ownership"}
}

# Payment methods
PAYMENT_METHODS = {
    "cashapp": "$MistressMariaDom",
    "venmo": "@MistressMariaDom",
    "btc": "bc1q...",
    "eth": "0x..."
}
