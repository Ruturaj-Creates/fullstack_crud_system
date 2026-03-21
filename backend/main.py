from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware 
from models import Products
from database import session, engine
import db_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_models.Base.metadata.create_all(bind=engine)

products = [
    Products(id=1, name="phone", description="budget phone", price=999, quantity=13),
    Products(id=2, name="laptop", description="gaming laptop", price=20000, quantity=5),
    Products(id=3, name="pen", description="blue ink pen", price=20, quantity=100),
    Products(id=4, name="notebook", description="single line notebook", price=30, quantity=50)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(db_models.Products).count()  # ✅ FIXED: Added ()
    if count == 0:
        for product in products:
            db.add(db_models.Products(**product.model_dump()))
        db.commit()
    db.close()

init_db()

# GET all products
@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(db_models.Products).all()

# GET single product by ID
@app.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Products).filter(db_models.Products.id == id).first()
    if db_product:
        return db_product
    return {"error": "product not found"}

# CREATE product
@app.post("/products")
def add_product(product: Products, db: Session = Depends(get_db)):
    db_product = db_models.Products(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # ✅ FIXED: Refresh to get DB instance
    return db_product

# UPDATE product
@app.put("/products/{id}")  # ✅ FIXED: {id} in path
def update_product(id: int, product: Products, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Products).filter(db_models.Products.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        db.refresh(db_product)  # ✅ FIXED: Refresh after update
        return db_product
    return {"error": "No product found"}

# DELETE product
@app.delete("/products/{id}")  # ✅ FIXED: {id} in path
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(db_models.Products).filter(db_models.Products.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "product deleted successfully"}
    return {"error": "product not found"}