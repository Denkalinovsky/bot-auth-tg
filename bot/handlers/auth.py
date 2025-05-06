from telegram import Update
from telegram.ext import ContextTypes
from ..db import users_collection
from ..keyboards import get_keyboard
from ..utils import generate_auth_token

async def generate_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db_user = users_collection.find_one({"id": user.id})
    if not db_user:
        users_collection.insert_one({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "balance": 0
        })
    auth_code = generate_auth_token(user.id)
    users_collection.update_one(
        {"id": user.id},
        {"$set": {"auth_token": auth_code}}
    )
    await update.message.reply_text(
        f"✅ Код успешно сгенерирован!\n\n"
        f"Ваш код авторизации:\n`{auth_code}`\n\n"
        "Скопируйте его и вставьте в приложение.",
        parse_mode='Markdown',
        reply_markup=get_keyboard()
    ) 