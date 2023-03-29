from pydantic import BaseModel

class VideoGameBase(BaseModel):
    Name: str
    Platform: str
    Year: str
    Genre: str
    Publisher: str
    NA_Sales : float
    EU_Sales : float
    JP_Sales : float
    Other_Sales : float
    Global_Sales : float

class VideoGameCreate(VideoGameBase):
    pass

class VideoGame(VideoGameBase):

    id:int

    class Config:
        orm_mode = True