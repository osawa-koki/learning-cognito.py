from pydantic import BaseModel, EmailStr


class ForgotPasswordModel(BaseModel):
    email: EmailStr
