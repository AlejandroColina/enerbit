from sqlalchemy import Column, Float, Integer, String
from db.datebase import Base


class Metric(Base):
    __tablename__ = 'metrics'
    id = Column(Integer, primary_key=True)
    device = Column(Integer, nullable=False)
    consumo = Column(String(50), nullable=False)
    date = Column(Float, nullable=False)
