from pydantic import BaseModel


class SignUpModel(BaseModel):
    name: str
    email: str
    password: str
