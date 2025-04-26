from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), default='')
    first_name = Column(String(50), default='')
    last_name = Column(String(50), default='')
    created_at = Column(DateTime(timezone=False), server_default=func.now())