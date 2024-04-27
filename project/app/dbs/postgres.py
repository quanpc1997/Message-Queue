from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.configs import SQLALCHEMY_DATABASE_URL
from loguru import logger


class Postgres:
    engine = None

    def __new__(cls):
        if cls.engine is None:
            cls.engine = super().__new__(cls)
            # Thiết lập kết nối tại đây
            try:
                cls.engine = create_engine(SQLALCHEMY_DATABASE_URL)
            except Exception as e:
                logger.error(e)
        return cls.engine
    
# Create declarative base meta instance
Base = declarative_base()

# Create Session for sessionmaker
SessionLocal = sessionmaker(bind=Postgres().engine, expire_on_commit=False)

async def get_db():
    db = SessionLocal()
    try:
        print(f"db1 = {db}")
        yield db
    finally:
        db.close()


