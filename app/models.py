from pydantic import BaseModel, EmailStr, Field
from werkzeug.security import generate_password_hash


class User(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)

    def to_dict(self):
        data = self.model_dump()
        data["password"] = generate_password_hash(data["password"])
        return data
