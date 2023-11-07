from pydantic import BaseModel, EmailStr, Field


class ConfirmForgotPasswordModel(BaseModel):
    email: EmailStr
    code: str = Field(..., min_length=6, max_length=6)
    password: str = Field(..., pattern="^[\\S]+.*[\\S]+$", min_length=8, max_length=16)
