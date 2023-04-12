from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

metadata = Base.metadata

class VideoGames(Base):
    __tablename__ = 'game_sales'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    platform = Column(String)
    year = Column(String)
    genre = Column(String)
    publisher = Column(String)
    na_sales = Column(Float)
    eu_sales = Column(Float)
    jp_sales = Column(Float)
    other_sales = Column(Float)
    global_sales = Column(Float)