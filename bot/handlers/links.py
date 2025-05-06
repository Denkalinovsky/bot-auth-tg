from telegram import Update
from telegram.ext import ContextTypes
from ..keyboards import get_links_keyboard

async def show_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 Полезные ссылки:",
        reply_markup=get_links_keyboard()
    ) 