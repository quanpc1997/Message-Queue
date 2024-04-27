from sqlalchemy import Column, UUID, String, DateTime, Boolean
from uuid import uuid4

from app.dbs.postgres import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=uuid4())
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
