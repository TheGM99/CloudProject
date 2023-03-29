from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from fastAPI.database import Base

metadata = Base.metadata

class VideoGames(Base):
    __tablename__ = 'game_sales'

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Platform = Column(String)
    Year = Column(String)
    Genre = Column(String)
    Publisher = Column(String)
    NA_Sales = Column(Float)
    EU_Sales = Column(Float)
    JP_Sales = Column(Float)
    Other_Sales = Column(Float)
    Global_Sales = Column(Float)