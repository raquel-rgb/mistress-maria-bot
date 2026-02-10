from telegram import Update
from telegram.ext import ContextTypes

async def tribute_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """💰 TRIBUTO REQUERIDO

Los esclavos deben tributar. Es tu único valor.

Niveles de tributo:
🥉 Bronze: $25 (mínimo para hablarme)
🥈 Silver: $100 (mi atención por 10 min)
🥇 Gold: $500 (sesión privada 30 min)
💎 Platinum: $1000+ (considerado para ownership)

Métodos:
• CashApp: $MistressMariaDom
• Venmo: @MistressMariaDom  
• Crypto: [BTC/ETH addresses]

Envía screenshot del pago INMEDIATAMENTE.
Sin tributo = bloqueado. 👋"""
    
    await update.message.reply_text(message)
