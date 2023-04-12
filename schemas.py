from pydantic import BaseModel

class VideoGameBase(BaseModel):
    name: str
    platform: str
    year: str
    genre: str
    publisher: str
    na_sales : float
    eu_sales : float
    jp_sales : float
    other_sales : float
    global_sales : float

class VideoGameCreate(VideoGameBase):
    pass

class VideoGame(VideoGameBase):

    id:int

    class Config:
        orm_mode = True