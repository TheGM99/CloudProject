from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import crud, models, schemas
from database import SessionLocal, engine
import os 
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
front = os.environ.get('FRONTEND_IP',"localhost")
origins = [
    "http://" + front,
    "http://"+front+":8080",
    "http://"+front+":5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/games",response_model=list[schemas.VideoGame])
def get_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games

@app.get("/games/{game_name}",response_model=list[schemas.VideoGame])
def get_games_by_name(game_name:str, db: Session = Depends(get_db)):
    games = crud.get_games_by_name(db, name = game_name)
    if games is None:
        raise HTTPException(status_code=404, detail="User not found")
    return games

@app.post("/games",response_model=list[schemas.VideoGame])
def post_game(game:schemas.VideoGameCreate,db: Session = Depends(get_db)):
    return crud.post_game(db=db, game=game)

@app.put("/games",response_model=list[schemas.VideoGame])
def put_game(game:schemas.VideoGame, db: Session = Depends(get_db)):
    return crud.update_game(db=db,game=game)


if __name__ == "__main__":
    uvicorn.run(app, port=5000, log_level="info")