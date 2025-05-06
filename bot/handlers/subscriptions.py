from telegram import Update
from telegram.ext import ContextTypes
from ..db import users_collection
from ..keyboards import get_subscription_keyboard, get_keyboard
from ..utils import get_subscription_price, get_user_subscription, activate_subscription, get_user_balance

async def show_subscriptions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    balance = get_user_balance(user.id)
    db_user = users_collection.find_one({"id": user.id})
    test_used = db_user.get("test_subscription_used", False)
    
    text = f"💰 Ваш баланс: {balance}₽\n\n"
    text += f"🎯 Ваша текущая подписка: {get_user_subscription(user.id)}\n\n"
    text += "Доступные подписки:\n"
    if not test_used:
        text += "• 🧪 Ознакомительная (1 час) - бесплатно (1 раз)\n"
    text += f"• Музей (час) - {get_subscription_price('museum_hour')}₽\n"
    text += f"• Музей (неделя) - {get_subscription_price('museum_weak')}₽\n"
    text += f"• Музей (месяц) - {get_subscription_price('museum_month')}₽\n"
    text += "\nВыберите подписку для активации:"
    
    await update.message.reply_text(text, reply_markup=get_subscription_keyboard(test_used))

async def handle_subscription_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    sub_type = query.data.replace("sub_", "")  # museum_hour, museum_weak, museum_month, test
    user = query.from_user
    if activate_subscription(user.id, sub_type):
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=f"✅ Подписка успешно активирована!\n"
                 f"💰 Остаток на балансе: {get_user_balance(user.id)}₽",
            reply_markup=get_keyboard()
        )
    else:
        if sub_type == "test":
            db_user = users_collection.find_one({"id": user.id})
            if db_user.get("test_subscription_used"):
                msg = "❌ Тестовая подписка уже была использована."
            else:
                msg = "❌ Не удалось активировать тестовую подписку."
        else:
            msg = "❌ Недостаточно средств на балансе!"
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=msg,
            reply_markup=get_keyboard()
        )
    await query.message.delete() 