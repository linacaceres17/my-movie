from fastapi import APIRouter
from models.director import Director as DirectorModel
from schemas.director import Director
from typing import List
from config.database import Session
from service.director import DirectorService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


director_router = APIRouter()


@director_router.get('/director',tags=['director'], response_model=List[Director],status_code=200)
def get_director() -> Director: 
    db = Session()
    result = DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)
