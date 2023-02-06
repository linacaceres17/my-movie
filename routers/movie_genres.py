from fastapi import APIRouter
from models.movie_genres import MovieGenres as MovierGenreModel 
from schemas.movie_genres import Movie_genres
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session

movie_genres_route = APIRouter()

@movie_genres_route.get('/movie_genre',tags=['movie_genres'])
def get_movie_genre():
    db = Session()
    result = db.query(MovierGenreModel).all()
    return JSONResponse(jsonable_encoder(result),status_code=200)

@movie_genres_route.post('/movie_genre',tags=['movie_genre'])
def create_movie_genre(movier_genre:Movie_genres):
    db = Session()
    return JSONResponse(content={"message":"Se registro exitosamente la pelicula"},status_code=201)