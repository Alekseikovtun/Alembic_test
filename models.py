import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

if __name__ == '__models__':
    class UserModel(Base):
        __tabelname__ = 'user'

        id = Column(Integer, primary_key=True)
        first_name = Column(String, nullable=False)
        last_name = Column(String, nullable=False)
        birth = Column(DateTime)
        created = Column(DateTime, default=datetime.utcnow)
