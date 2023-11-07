from pydantic import BaseModel, EmailStr, Field


class SignUpModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=16)
    email: EmailStr
    password: str = Field(..., pattern="^[\S]+.*[\S]+$", min_length=8, max_length=16)
