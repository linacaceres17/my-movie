from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.genres import Genres as GenresModel
from config.database import Session
from service.genres import GenresService
from fastapi.responses import JSONResponse

genres_router = APIRouter()

@genres_router.get('/genres',tags=['genres'],status_code=200)
def get_genres():
    db = Session()
    result = db.query(GenresModel).all()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@genres_router.get('/genre_by_id',tags=['genres'],status_code=200)
def get_genre_by_id(id:int):
    db = Session()
    result = GenresService(db).get_genre_by_id(id)
    if not result:
        return JSONResponse(status_code=400,content={"message":"No found director with that id"})
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.get('/genre_by_title',tags=['genres'],status_code=200)
def get_genre_for_title(genre:str):
    db = Session()
    result = GenresService(db).get_genre_by_title(genre)
    if not result:
        return JSONResponse(status_code=400,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result),status_code=200)