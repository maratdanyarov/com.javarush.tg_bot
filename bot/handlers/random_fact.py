from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.utils.gpt import ask_gpt

PROMPT = "Tell an interesting fact, to amaze a person!"

keyboard = [
    [InlineKeyboardButton("Tell me another fact", callback_data="random")],
    [InlineKeyboardButton("Finish", callback_data="start")],
]

markup = InlineKeyboardMarkup(keyboard)

async def random_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    with open("../../resources/images/bot.png", "rb") as photo:
        await context.bot.send_photo(chat_id=chat_id, photo=photo)

    fact = await ask_gpt(PROMPT)
    await context.bot.send_message(chat_id=chat_id, text=fact, reply_markup=markup)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "random":
        await random_command(update, context)
    elif query.data == "start":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You returned to the beginning. Type /random to know another interesting fact."
        )