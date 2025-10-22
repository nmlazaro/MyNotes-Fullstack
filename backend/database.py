import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#load_dotenv() # Loads the DATABASE_URL from .env
#SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://admin:admin@localhost:5432/my_notes"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    except Exception as err:
        print(f'Error trying to execute get_db() -> Error: {err}')
    finally:
        db.close()