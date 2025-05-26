import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, ConversationHandler, MessageHandler, filters

from bot.handlers.start import start_command
from bot.handlers.random_fact import random_command
from bot.handlers.random_fact import handle_callback as random_fact_callback
from bot.handlers.gpt_chat import gpt_start, gpt_answer, gpt_cancel, GPT_MODE

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("random", random_command))
    app.add_handler(CallbackQueryHandler(random_fact_callback))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("gpt", gpt_start)],
        states={
            GPT_MODE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, gpt_answer),
            ]
        },
        fallbacks=[
            CommandHandler("cancel", gpt_cancel)
        ]
    )
    app.add_handler(conv_handler)

    logger.info("Bot started.")
    app.run_polling()


if __name__ == "__main__":
    main()