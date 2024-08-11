from pydantic import BaseModel

class FoodItemBase(BaseModel):
    name: str
    description: str
    price: int

class FoodItemCreate(FoodItemBase):
    pass

class FoodItem(FoodItemBase):
    id: int

    class Config:
        orm_mode = True
