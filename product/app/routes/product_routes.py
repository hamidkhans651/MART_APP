from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from app.models.product_models import Product

router = APIRouter()


@router.post("/create-product/", response_model=Product)
def create_product(product: Annotated[Product, Depends]):
    if not product:
        raise HTTPException(
            status_code=500, detail="Some things went wrong, while creating product.")
    return product


@router.post("/add-product-images/", response_model=str)
def add_images_in_product(message: Annotated[str, Depends]):
    if not message:
        raise HTTPException(
            status_code=500, detail="Some things went wrong, while creating product.")
    return message

