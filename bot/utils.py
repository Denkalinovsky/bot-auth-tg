import jwt
from datetime import datetime, timedelta, UTC
from .config import JWT_SECRET
from .db import users_collection, price_collection

def generate_auth_token(user_id: int) -> str:
    payload = {
        'user_id': user_id,
        'iat': datetime.now(UTC)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

def get_user_balance(user_id: int) -> int:
    user = users_collection.find_one({"id": user_id})
    if user:
        return user["balance"]
    return 0

def update_user_balance(user_id: int, amount: int) -> None:
    users_collection.update_one(
        {"id": user_id},
        {"$inc": {"balance": amount}}
    )

def get_subscription_price(sub_type: str) -> int:
    price_doc = price_collection.find_one()
    return price_doc.get(sub_type, 0)

def activate_subscription(user_id: int, sub_type: str) -> bool:
    user = users_collection.find_one({"id": user_id})
    if not user:
        return False
    if sub_type == "test":
        if user.get("test_subscription_used"):
            return False
        expires_at = datetime.now(UTC) + timedelta(hours=1)
        users_collection.update_one(
            {"id": user_id},
            {"$set": {
                "subscription": {
                    "type": "test",
                    "expires_at": expires_at,
                    "is_active": True
                },
                "test_subscription_used": True
            }}
        )
        return True
    price = get_subscription_price(sub_type)
    if user["balance"] < price:
        return False
    users_collection.update_one(
        {"id": user_id},
        {"$inc": {"balance": -price}}
    )
    expires_at = datetime.now(UTC) + timedelta(days=30)
    if sub_type == "museum_hour":
        expires_at = datetime.now(UTC) + timedelta(hours=1)
    elif sub_type == "museum_weak":
        expires_at = datetime.now(UTC) + timedelta(days=7)
    elif sub_type == "museum_month":
        expires_at = datetime.now(UTC) + timedelta(days=30)
    users_collection.update_one(
        {"id": user_id},
        {
            "$set": {
                "subscription": {
                    "type": sub_type,
                    "expires_at": expires_at,
                    "is_active": True
                }
            }
        }
    )
    return True

def get_user_subscription(user_id: int) -> str:
    user = users_collection.find_one({"id": user_id})
    if not user or not user.get("subscription"):
        return "Нет активной подписки"
    sub = user["subscription"]
    if not sub.get("is_active"):
        return "Нет активной подписки"
    expires_at = sub.get("expires_at")
    if expires_at:
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=UTC)
        if expires_at < datetime.now(UTC):
            users_collection.update_one(
                {"id": user_id},
                {"$set": {"subscription.is_active": False}}
            )
            return "Подписка истекла"
    sub_type = sub.get("type", "")
    if sub_type == "museum_hour":
        display_type = "Музей (час)"
    elif sub_type == "museum_weak":
        display_type = "Музей (неделя)"
    elif sub_type == "museum_month":
        display_type = "Музей (месяц)"
    elif sub_type == "test":
        display_type = "Тестовая (1 час)"
    else:
        display_type = sub_type
    if expires_at:
        expires_str = expires_at.strftime("%d.%m.%Y %H:%M")
        return f"{display_type} (до {expires_str})"
    return display_type 