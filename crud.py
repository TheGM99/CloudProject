from sqlalchemy.orm import Session
from sqlalchemy import text
import models, schemas

def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VideoGames).order_by(models.VideoGames.id.asc()).offset(skip).limit(limit).all()

def get_last(db: Session):
    return db.query(models.VideoGames).order_by(models.VideoGames.id.desc()).limit(1).one()

def get_games_by_name(db:Session, name:str):
    return db.query(models.VideoGames).filter(models.VideoGames.Name.contains(name)).order_by(models.VideoGames.id.asc()).all()

def post_game(db:Session, game:schemas.VideoGameCreate, skip:int = 0, limit:int = 100):
    db_game = models.VideoGames(**game.dict())
    db_game.id = get_last(db).id + 1
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db.query(models.VideoGames).order_by(models.VideoGames.id.asc()).all()

def update_game(db:Session, game:schemas.VideoGame):
    db_game = db.query(models.VideoGames).filter(models.VideoGames.id == game.id).one()
    db_game.Name = game.Name 
    db_game.Genre = game.Genre
    db_game.Year = game.Year
    db_game.Platform = game.Platform
    db_game.Publisher = game.Publisher
    db_game.NA_Sales = game.NA_Sales
    db_game.EU_Sales = game.EU_Sales
    db_game.JP_Sales = game.JP_Sales
    db_game.Other_Sales = game.Other_Sales
    db_game.Global_Sales = game.Global_Sales
    db.commit()
    return db.query(models.VideoGames).order_by(models.VideoGames.id.asc()).all()
