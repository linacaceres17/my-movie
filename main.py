from fastapi import FastAPI, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional , List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer
from config.database import Session,engine,Base
from models.movie import Movie as MovieModel


app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)



class User(BaseModel):
    email:str
    password:str

class JWYBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="credenciales invalidas")


class Movie(BaseModel):
        id: Optional[int] = None
        title: str = Field(max_length=15,min_length=3)
        overview: str = Field(max_length=50,min_length=10)
        year: int = Field(le=2022)
        rating: float = Field(ge=1,le=10)
        category: str = Field(max_length=15,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'title': 'Avatar',
                    'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
                    'year': '2009',
                    'rating': 7.8,
                    'category': 'Acción' 
                }
            }

movies = [
    {        
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'  
    },
        {        
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'  
    },
]
@app.get('/',tags=['home'])


@app.post('/login',tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token:str = create_token(user.dict())
    return JSONResponse(status_code=200, content=token)


def message():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
def get_movies() -> Movie:
    return JSONResponse(content=movies)

@app.get('/movies/{id}',tags=['movies'])
def get_movie(id:int = Path(ge=1,le=2000)):
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse([])

@app.get('/movies/',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movies_by_category(category:str = Query(min_length=5,max_length=15)):
        data = [item for item in movies if item['category']==category]
        return JSONResponse(content=data)

@app.post('/movies',tags=['movies'],status_code=201,response_model=dict)
def create_movie(movie:Movie):
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(content={"message":"Se ha registrado la pelicula","status_code":201})

@app.put('/movies{id}',tags=['movies'])
def update_movie(id:int,movie:Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['category'] = movie.category
            item['rating'] = movie.rating
            return JSONResponse(content={"message":"Se ha modificado la pelicula con id: {id}"})

    return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})

@app.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(content={"message":"Se ha eliminado la pelicula con id: {id}"})

    return []
