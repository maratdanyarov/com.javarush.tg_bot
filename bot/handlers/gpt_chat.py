from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters
from bot.utils.gpt import ask_gpt
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
GPT_MODE = 1


async def gpt_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("Entering gpt_start()")
    chat_id = update.effective_chat.id

    with open("../../resources/images/bot.png", "rb") as image:
        await context.bot.send_photo(chat_id, photo=image)
    logger.info("Sending an image")

    await update.message.reply_text(
        "I am connected to ChatGPT. Please write your question, and I will ask it.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Finish", callback_data="start")]
        ])
    )
    logger.info("Sending instructions to user.")
    return GPT_MODE


async def gpt_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_text = update.message.text
    logger.info(f"Received user text: {user_text}")
    response = await ask_gpt(user_text)
    logger.info(f"Received response: {response}")
    await update.message.reply_text(response)
    logger.info("Sending GPT answer to user")
    return GPT_MODE


async def gpt_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("The conversation was finished. Type /gpt to start the conversation again.")
    return ConversationHandler.END