from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#typeproduct aus der classe""
def add(product):
    db.session.add(product)
    db.session.commit()