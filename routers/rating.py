from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from service.rating import RatingService
from schemas.rating import Rating
from config.database import Session

rating_router = APIRouter()

@rating_router.get('/rating',tags=['rating'],status_code=200)
def get_ratings()-> Rating:
    db = Session()
    result = RatingService(db).get_ratings()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@rating_router.post('/rating',tags=['rating'],status_code=201)
def create_rating(rating:Rating):
    db = Session()
    RatingService(db).create_rating(rating)
    return JSONResponse(content={"message":"Se ha registrado el rating","status_code":201})
 