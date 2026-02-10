import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.tribute import tribute_handler
from handlers.task import task_handler
from handlers.confess import confess_handler, confess_callback_handler
from handlers.worship import worship_handler
from handlers.punish import punish_handler, punish_callback_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "⚠️ Un error ha ocurrido. No te atrevas a quejarte, esclavo."
        )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("tribute", tribute_handler))
    application.add_handler(CommandHandler("task", task_handler))
    application.add_handler(CommandHandler("confess", confess_handler))
    application.add_handler(CommandHandler("worship", worship_handler))
    application.add_handler(CommandHandler("punish", punish_handler))
    
    # Callback handlers
    application.add_handler(CallbackQueryHandler(confess_callback_handler, pattern="^confess_"))
    application.add_handler(CallbackQueryHandler(punish_callback_handler, pattern="^punish_"))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    logger.info("Mistress Maria Bot started - Bow down, slaves!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
