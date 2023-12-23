from fastapi import APIRouter, Depends, HTTPException, status, Path
from pydantic import BaseModel, Field
from database import SessionLocal
from typing import Annotated
# from models import Playlist
from sqlalchemy.orm import Session
from models import Playlist
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]    


# @router("/playlists")
# async def take_all_playlists(db: db_dependency):
#     playlists = db.query(Playlist).all()
#     return  playlists

# @router("/plz`aylists/")
# async def add_

@router.get("/take_all_playlists")
async def take_all_songs(db: db_dependency):
    