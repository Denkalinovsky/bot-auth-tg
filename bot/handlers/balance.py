from telegram import Update
from telegram.ext import ContextTypes
from ..db import users_collection
from ..keyboards import get_keyboard

async def show_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db_user = users_collection.find_one({"id": user.id})
    balance = db_user["balance"] if db_user else 0
    await update.message.reply_text(
        f"💰 Ваш текущий баланс: {balance}₽\n\n"
        "Для пополнения баланса нажмите кнопку '💳 Пополнить'",
        reply_markup=get_keyboard()
    ) 