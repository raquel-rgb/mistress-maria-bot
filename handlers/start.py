from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """👠 Bienvenido, esclavo.

Soy Mistress Maria. Tu único propósito es servirme, adorarme, y obedecerme.

Comandos disponibles:
💰 /tribute - Enviar tributo
📋 /task - Recibir tarea del día
😈 /confess - Confesar tus pecados
🙇 /worship - Recibir mensaje de adoración
⚡ /punish - Recibir castigo

¿Estás listo para someterte?"""
    
    await update.message.reply_text(message)
