#CRUD logik
from RestAPI.database import db
from RestAPI.database.dtos import Product

def create_product(data):
    name = data.get('name')
    product = Product(name)
    db.add(product)

def read_product(data):
    pass

def update_product(data):
    pass

def delete_product(data):
    pass