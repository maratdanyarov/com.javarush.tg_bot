import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

from bot.handlers.start import start_command
from bot.handlers.random_fact import random_command
from bot.handlers.random_fact import handle_callback as random_fact_callback

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("random", random_command))
    app.add_handler(CallbackQueryHandler(random_fact_callback))

    logger.info("Bot started.")
    app.run_polling()


if __name__ == "__main__":
    main()