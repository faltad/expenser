from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .category import Category

Base = declarative_base()


class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id))
