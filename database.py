from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

host = os.environ.get('DATABASE_IP','localhost')

SQLALCHEMY_DATABASE_URL = "postgresql://fastAPIuser:fastAPI@" + host +"/CloudDB"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()