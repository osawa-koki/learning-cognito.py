from pydantic import BaseModel, Field


class ChangePasswordModel(BaseModel):
    previous_password: str = Field(...,
                          pattern="^[\\S]+.*[\\S]+$",
                          min_length=8,
                          max_length=16)
    proposed_password: str = Field(...,
                        pattern="^[\\S]+.*[\\S]+$",
                        min_length=8,
                        max_length=16)
