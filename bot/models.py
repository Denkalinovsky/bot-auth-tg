from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Subscription:
    type: Optional[str]
    expires_at: Optional[datetime]
    is_active: bool = False

@dataclass
class User:
    id: int
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    balance: int = 0
    last_seen_version: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    banned: bool = False
    subscription: Optional[Subscription] = None
    test_subscription_used: bool = False
    auth_token: Optional[str] = None 