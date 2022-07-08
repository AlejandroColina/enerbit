from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from os import getenv

engine = create_engine(getenv("DB_CONECTION"), echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)