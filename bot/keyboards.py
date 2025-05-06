from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton("💰 Баланс"), KeyboardButton("💳 Пополнить")],
        [KeyboardButton("🎯 Подписки"), KeyboardButton("🔑 Получить код")],
        [KeyboardButton("❓ Помощь"), KeyboardButton("🔗 Полезные ссылки")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_payment_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("100₽", callback_data="pay_100"),
            InlineKeyboardButton("300₽", callback_data="pay_300"),
            InlineKeyboardButton("500₽", callback_data="pay_500")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_links_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("📱 Скачать приложение", url="https://t.me/+TPCuwQN7a_YxNTIy")],
        [InlineKeyboardButton("📚 Документация", url="https://t.me/+TPCuwQN7a_YxNTIy")],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_subscription_keyboard(test_used: bool) -> InlineKeyboardMarkup:
    keyboard = []
    if not test_used:
        keyboard.append([
            InlineKeyboardButton("🧪 Ознакомительная (1 час)", callback_data="sub_test")
        ])
    keyboard.append([
        InlineKeyboardButton("🎯 Музей (час)", callback_data="sub_museum_hour"),
    ])
    keyboard.append([
        InlineKeyboardButton("🎯 Музей (неделя)", callback_data="sub_museum_weak"),
    ])
    keyboard.append([
        InlineKeyboardButton("🎯 Музей (месяц)", callback_data="sub_museum_month")
    ])
    return InlineKeyboardMarkup(keyboard) 