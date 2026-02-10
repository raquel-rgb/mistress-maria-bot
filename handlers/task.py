import json
import random
from telegram import Update
from telegram.ext import ContextTypes

# Load tasks
with open('data/tasks.json', 'r', encoding='utf-8') as f:
    TASKS = json.load(f)

async def task_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task = random.choice(TASKS)
    
    message = f"""📋 TAREA DE HOY, ESCLAVO:

"{task}"

— Mistress Maria 👠"""
    
    await update.message.reply_text(message)
