from sqlalchemy.orm import Session
from sqlalchemy import text
import models, schemas

def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VideoGames).order_by(models.VideoGames.id.asc()).offset(skip).limit(limit).all()

def get_last(db: Session):
    return db.query(models.VideoGames).order_by(models.VideoGames.id.desc()).limit(1).one()

def get_games_by_name(db:Session, name:str):
    return db.query(models.VideoGames).filter(models.VideoGames.name.contains(name)).order_by(models.VideoGames.id.asc()).all()

def post_game(db:Session, game:schemas.VideoGameCreate, skip:int = 0, limit:int = 100):
    db_game = models.VideoGames(**game.dict())
    db_game.id = get_last(db).id + 1
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db.query(models.VideoGames).order_by(models.VideoGames.id.asc()).all()

def update_game(db:Session, game:schemas.VideoGame):
    db_game = db.query(models.VideoGames).filter(models.VideoGames.id == game.id).one()
    db_game.name = game.name 
    db_game.genre = game.genre
    db_game.year = game.year
    db_game.platform = game.platform
    db_game.publisher = game.publisher
    db_game.na_sales = game.na_sales
    db_game.eu_sales = game.eu_sales
    db_game.jp_sales = game.jp_sales
    db_game.other_sales = game.other_sales
    db_game.global_sales = game.global_sales
    db.commit()
    return db.query(models.VideoGames).order_by(models.VideoGames.id.asc()).all()
