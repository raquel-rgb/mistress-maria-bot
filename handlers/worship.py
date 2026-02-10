import json
import random
from telegram import Update
from telegram.ext import ContextTypes

# Load worship messages
with open('data/worship_messages.json', 'r', encoding='utf-8') as f:
    WORSHIP_MESSAGES = json.load(f)

async def worship_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = random.choice(WORSHIP_MESSAGES)
    
    message = f"""🙇 ADORA:

"{message_text}"

— Tu Diosa 👑"""
    
    await update.message.reply_text(message)
