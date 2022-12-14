import datetime

from sqlalchemy import Column, DateTime, Integer, String
from models.base import Base


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.datetime.utcnow)
