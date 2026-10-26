from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///dados.db"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, autocommit=False)

Base = declarative_base()