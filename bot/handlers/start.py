from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hey! I am bot with ChatGPT. "
                                    "Type /random to get an interesting fact."
                                    "Type /gpt to answer any question to ChatGPT")
