from app.models.product_models import ProductsBase

_ProductsBase = [
    ProductsBase(product_name = "olivia",
                 product_description =  "best hair color for color your hair",
                 product_type= "hair color",
                )
]
def get_all()-> list[ProductsBase]:
    """return  the all productsbase"""
    return ProductsBase

def get_one(name:str) -> ProductsBase | None:
    for _product in _product:
        if _product.name == name:
            return _product
    return None


def create(product: ProductsBase) -> ProductsBase:
    "add products"
    return product

