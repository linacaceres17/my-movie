from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from pydantic import BaseModel, Field
from typing import Optional , List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.movie import Movie as MovieModel


movie_router = APIRouter()


class Movie(BaseModel):
        id: Optional[int] = None
        title: str = Field(max_length=15,min_length=3)
        overview: str = Field(max_length=300,min_length=10)
        year: int = Field(le=2022)
        time: float = Field(ge=1,le=10)
        date_release : str  = Field(max_length=15,min_length=3)
        release_contry: str = Field(max_length=15,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'title': 'Avatar',
                    'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
                    'year':2002,
                    'time': 1.50,
                    'date_release':'2009',
                    'release_contry':'USA',
                }
            }



#@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@movie_router.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movies() -> Movie:
    db = Session()
    result = db.query(MovieModel).all()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.get('/movies/{id}',tags=['movies'])
def get_movie(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
    
@movie_router.get('/movies/',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movies_by_release_contry(release_contry:str = Query(min_length=3,max_length=15)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.release_contry == release_contry).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_router.post('/movies',tags=['movies'],status_code=201,response_model=dict)
def create_movie(movie:Movie)->dict:
    db = Session()
    new_movie = MovieModel(
    title=movie.title,
    overview = movie.overview,
    year = movie.year,
    time = movie.time,
    date_release = movie.date_release,
    release_contry = movie.release_contry
    )
    db.add(new_movie)
    db.commit()
    return JSONResponse(content={"message":"Se ha registrado la pelicula","status_code":201})

# @movie_router.put('/movies{id}',tags=['movies'])
# def update_movie(id:int,movie:Movie):
#     for item in movies:
#         if item['id'] == id:
#             item['title'] = movie.title
#             item['overview'] = movie.overview
#             item['year'] = movie.year
#             item['category'] = movie.category
#             item['rating'] = movie.rating
#             return JSONResponse(content={"message":"Se ha modificado la pelicula con id: {id}"})

#     return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})

@movie_router.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
        db = Session()
        result = db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        db.delete(result)
        db.commit
        return JSONResponse(content="Delete movie", status_code=200)
    