from pydantic import BaseModel, EmailStr, Field


class ResendCodeModel(BaseModel):
    email: EmailStr
