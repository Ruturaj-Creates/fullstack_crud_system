from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine(url)
session=sessionmaker(bind=engine,autoflush=False)

