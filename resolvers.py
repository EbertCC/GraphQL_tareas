def resolve_welcome(obj, info):
    return "Bienvenido a nuestra tienda de productos!"

products_db = {
    "1": {"id": "1", "name": "Laptop", "price": 1000},
    "2": {"id": "2", "name": "Smartphone", "price": 600},
    "3": {"id": "3", "name": "Tablet", "price": 400},
}

def resolve_get_all_products(obj, info):
    return list(products_db.values())

def resolve_get_product(obj, info, id):
    return products_db.get(id)
