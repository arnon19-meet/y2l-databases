from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,price,quantity,rating):
  product_object= Product(
    name=name,
    price=price,
    quantity=quantity,
    rating=rating)
  session.add(product_object)
  session.commit()
create_product("watch",10000000000,1,10)
create_product("idk",1,1,1)
def update_product(name,rating):
  product_object=session.query(Product).filter_by(name=name).first()
  product_object.rating=rating
  session.commit()
update_product("watch",7)

def delete_product(rating):
  if price > 300:
    session.query(Product).delete()
    session.commit()


delete_product(10)

# def get_product(id):