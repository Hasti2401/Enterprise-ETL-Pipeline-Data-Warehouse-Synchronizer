from datetime import datetime

from pydantic import BaseModel, EmailStr


class StripeCustomer(BaseModel):
    id: str
    name: str | None = None
    email: EmailStr | None = None
    created: datetime | None = None