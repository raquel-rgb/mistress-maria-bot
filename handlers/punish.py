import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

PUNISHMENTS = [
    "24 horas de abstinencia total",
    "Escribirás 500 veces: 'Soy un esclavo inútil'",
    "Tributo extra de $50 por desobediencia",
    "No podrás contactarme por 48 horas (silent treatment)",
    "Arrodillado en arroz durante 30 minutos",
    "No podrás mirarte al espejo por 3 días",
    "Escribirás una carta de disculpa de 500 palabras",
    "Tributo doble durante una semana",
    "Sin redes sociales por 24 horas",
    "Harás 100 sentadillas mientras recitas 'Soy propiedad de Mistress Maria'"
]

async def punish_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if user has a stored sin from confess
    last_sin = context.user_data.get("last_sin", "desobediencia general")
    
    # Select 3-4 random punishments
    selected_punishments = random.sample(PUNISHMENTS, k=min(4, len(PUNISHMENTS)))
    punishment_text = "\n• ".join(selected_punishments)
    
    message = f"""⚡ CASTIGO ASIGNADO:

Por tu pecado de *{last_sin}*, recibirás:

• {punishment_text}

Ejecución inmediata. Reporta cumplimiento."""
    
    keyboard = [
        [InlineKeyboardButton("✅ Acepto mi castigo", callback_data="punish_accept")],
        [InlineKeyboardButton("🙏 Imploro perdón", callback_data="punish_beg")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(message, reply_markup=reply_markup, parse_mode="Markdown")

async def punish_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "punish_accept":
        await query.edit_message_text(
            query.message.text + "\n\n✅ *Castigo aceptado.* Eres un esclavo obediente... por ahora.",
            parse_mode="Markdown"
        )
    elif query.data == "punish_beg":
        await query.edit_message_text(
            query.message.text + "\n\n🙏 *¿Implorando?* Patético. Tu castigo se duplica por debilidad.",
            parse_mode="Markdown"
        )
