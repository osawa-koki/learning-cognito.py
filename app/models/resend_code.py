from pydantic import BaseModel, EmailStr


class ResendCodeModel(BaseModel):
    email: EmailStr
