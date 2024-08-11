from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models, schemas, database

app = FastAPI()

@app.get("/check")
async def read_root():
    return{"hellow":"this is email api"}


@app.post("/food-items/", response_model=schemas.FoodItem)
def create_food_item(food_item: schemas.FoodItemCreate, db: Session = Depends(database.get_db)):
    db_food_item = models.FoodItem(**food_item.dict())
    db.add(db_food_item)
    db.commit()
    db.refresh(db_food_item)
    return db_food_item
