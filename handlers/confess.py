import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Load sins
with open('data/sins.json', 'r', encoding='utf-8') as f:
    SINS = json.load(f)

async def confess_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Pensaste en otra Domme?", callback_data="confess_thought_of_other")],
        [InlineKeyboardButton("Te tocaste sin permiso?", callback_data="confess_touched_without_permission")],
        [InlineKeyboardButton("No completaste tu tarea?", callback_data="confess_incomplete_task")],
        [InlineKeyboardButton("Fuiste desobediente?", callback_data="confess_disobedient")],
        [InlineKeyboardButton("Te masturbaste antes de tributar?", callback_data="confess_no_tribute")],
        [InlineKeyboardButton("Otro pecado...", callback_data="confess_other")],
    ]
    
    message = """😈 CONFIESA TUS PECADOS

Habla, gusano. ¿Qué has hecho mal?

1. Pensaste en otra Domme?
2. Te tocaste sin permiso?
3. No completaste tu tarea?
4. Fuiste desobediente?
5. Te masturbaste antes de tributar?

Selecciona tu pecado o escríbelo. La confesión determina tu castigo.

Confiesa ahora o serás castigado más severamente."""
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def confess_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    sin_key = query.data.replace("confess_", "")
    
    if sin_key == "other":
        await query.edit_message_text(
            "😈 Escribe tu pecado ahora mismo, gusano. No te atrevas a mentirme."
        )
    elif sin_key in SINS:
        sin_name = SINS[sin_key]
        await query.edit_message_text(
            f"😈 Has confesado: *{sin_name}*\n\n"
            f"Tu castigo será severo. Usa /punish para recibir tu sentencia.",
            parse_mode="Markdown"
        )
        # Store the sin in user data for punish command
        context.user_data["last_sin"] = sin_name
    else:
        await query.edit_message_text("⚠️ Pecado no reconocido. Intenta de nuevo, esclavo.")
