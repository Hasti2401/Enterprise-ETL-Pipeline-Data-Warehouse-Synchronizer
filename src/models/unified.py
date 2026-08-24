from datetime import datetime

from pydantic import BaseModel, EmailStr


class UnifiedCustomer(BaseModel):
    source: str
    source_id: str
    full_name: str | None = None
    email: EmailStr | None = None
    created_at: datetime | None = None
