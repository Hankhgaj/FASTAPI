from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#'postgresql://usuario:contraseña@localhost:puerta/BaseDeDatos'
SQLALCHEMY_DATABASE_URL = 'postgresql://firmadigital:firmadigital@localhost:5432/Sistema'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()