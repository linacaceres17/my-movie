
from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_cast import MovieCast
from models.moviecast import MovieCast as MovieCastModel
from service.genres import GenresMoldel


genres_router = APIRouter()

@genres_router.get('/genres',tags=['genres'],status_code=200)
def get_genres():
    db = Session()
    result = GenresMoldel(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)