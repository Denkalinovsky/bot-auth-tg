from telegram import Update
from telegram.ext import ContextTypes
from ..keyboards import get_keyboard

async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "📚 Справка по использованию бота:\n\n"
        "💰 Баланс - показывает ваш текущий баланс\n"
        "💳 Пополнить - пополнение баланса\n"
        "🔑 Получить код - генерация кода авторизации\n"
        "❓ Помощь - показывает это сообщение\n"
        "🔗 Полезные ссылки - важные ссылки и контакты\n\n"
    )
    await update.message.reply_text(help_text, reply_markup=get_keyboard()) 