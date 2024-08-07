from pydantic import BaseModel

class Product(BaseModel):
 name: str
 country: str
 description: str
