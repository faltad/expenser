from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .seller import Seller

Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    seller_id = Column(Integer, ForeignKey(Seller.id))
