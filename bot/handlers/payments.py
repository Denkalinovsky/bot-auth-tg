from telegram import Update
from telegram.ext import ContextTypes
from ..db import users_collection
from ..keyboards import get_keyboard, get_payment_keyboard
from ..utils import get_user_balance, update_user_balance

async def show_payment_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 Выберите сумму пополнения:",
        reply_markup=get_payment_keyboard()
    )

async def handle_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    amount = int(query.data.split('_')[1])
    user = query.from_user
    update_user_balance(user.id, amount)
    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text=f"✅ Баланс успешно пополнен на {amount}₽\n"
             f"💰 Текущий баланс: {get_user_balance(user.id)}₽",
        reply_markup=get_keyboard()
    )
    await query.message.delete() 