from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class SalesforceContact(BaseModel):
    id: str = Field(alias="Id")
    first_name: str | None = Field(default=None, alias="FirstName")
    last_name: str | None = Field(default=None, alias="LastName")
    email: EmailStr | None = Field(default=None, alias="Email")
    created_at: datetime | None = Field(
        default=None,
        alias="CreatedDate"
    )

    model_config = {
        "populate_by_name": True
    }