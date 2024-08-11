from pydantic import BaseModel


class post(BaseModel):
    title: str
    id: str
    published : bool =True