from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from .config import TELEGRAM_BOT_TOKEN
from .handlers.balance import show_balance
from .handlers.payments import show_payment_options, handle_payment_callback
from .handlers.auth import generate_code
from .handlers.help import show_help
from .handlers.links import show_links
from .handlers.subscriptions import show_subscriptions
from .handlers.subscriptions import activate_subscription  # если понадобится

from telegram import Update

async def start(update: Update, context):
    await update.message.reply_text(
        "Привет! Я бот для генерации кодов авторизации для приложения.\n\n"
        "Используйте кнопки меню для навигации."
    )

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("TELEGRAM_BOT_TOKEN is not set!")
        return
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex("^💰 Баланс$"), show_balance))
    application.add_handler(MessageHandler(filters.Regex("^💳 Пополнить$"), show_payment_options))
    application.add_handler(MessageHandler(filters.Regex("^🔑 Получить код$"), generate_code))
    application.add_handler(MessageHandler(filters.Regex("^❓ Помощь$"), show_help))
    application.add_handler(MessageHandler(filters.Regex("^🔗 Полезные ссылки$"), show_links))
    application.add_handler(MessageHandler(filters.Regex("^🎯 Подписки$"), show_subscriptions))
    application.add_handler(CallbackQueryHandler(handle_payment_callback, pattern="^pay_"))
    # Подписки (активация)
    from .handlers.subscriptions import handle_subscription_callback
    application.add_handler(CallbackQueryHandler(handle_subscription_callback, pattern="^sub_"))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 