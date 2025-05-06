# Telegram Authorization Bot

Бот для генерации кодов авторизации, управления балансом и подписками через Telegram.

## Структура проекта

```
/bot/
    __init__.py
    main.py                # Точка входа
    config.py              # Переменные окружения
    db.py                  # Подключение к MongoDB
    models.py              # Структуры данных
    keyboards.py           # Генерация клавиатур
    utils.py               # Утилиты (баланс, подписки, токены)
    handlers/
        __init__.py
        auth.py            # Генерация кода
        balance.py         # Баланс
        payments.py        # Пополнение
        subscriptions.py   # Подписки
        help.py            # Справка
        links.py           # Полезные ссылки
.env
requirements.txt
README.md
```

## Установка

1. Клонируйте репозиторий
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Создайте файл `.env` и заполните его:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
JWT_SECRET=your_jwt_secret_here
YOOKASSA_SHOP_ID=your_yookassa_id
YOOKASSA_SECRET_KEY=your_yookassa_secret
MONGODB_URI=mongodb+srv://user:pass@host/db
```

## Запуск

```bash
python3 -m bot.main
```

## Использование

- `/start` — начать работу
- Кнопки меню:
  - 💰 Баланс — посмотреть баланс
  - 💳 Пополнить — пополнить баланс
  - 🎯 Подписки — выбрать и активировать подписку
  - 🔑 Получить код — сгенерировать код авторизации
  - ❓ Помощь — справка
  - 🔗 Полезные ссылки — ссылки и контакты

## Безопасность

- Коды авторизации генерируются через JWT
- Баланс и подписки хранятся в MongoDB
- Поддержка ознакомительной подписки (1 раз на пользователя)
- Все данные пользователей защищены 