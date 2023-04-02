from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_URL = "sqlite:///./blog.db"
engin = create_engine(SQLALCHEMY_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engin, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
