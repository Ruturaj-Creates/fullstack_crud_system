from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
url="postgresql://postgres:postgres@localhost:54320/TeluskoDB"
engine=create_engine(url)
session=sessionmaker(bind=engine,autoflush=False)

