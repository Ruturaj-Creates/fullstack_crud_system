from sqlalchemy.orm import declarative_base
from sqlalchemy import String,Integer,Float,Column

Base=declarative_base()

class Products(Base):
    __tablename__ ='product'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)

