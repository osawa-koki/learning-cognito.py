from pydantic import BaseModel, EmailStr, Field


class SignInModel(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)
