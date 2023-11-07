from pydantic import BaseModel


class UpdateAttributesModel(BaseModel):
    comment: str
