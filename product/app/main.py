from fastapi import FastAPI
import uvicorn
from app.routes import  product_routes

app = FastAPI(
    title="Product and Category Service",
    description="API for managing products",
    version="1.0.0",

    openapi_tags=[
        {"name": "Products", "description": "Operations with products."}
    ]
)


@app.get("/")
def home():
    return "Welcome to Product service"



app.include_router(router=product_routes.router,
                   prefix="/api/v1/product", tags=["Products"])


if __name__ == "__main__":
 uvicorn.run("main:app", reload=True)
