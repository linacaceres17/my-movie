from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel, Field


movie_cast_router = APIRouter()


class MovieCast(BaseModel):
        id: Optional[int] = None
        actor_id: int
        movie_id: int
        role: str = Field(max_length=15,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "id": 1,
                    "actor_id": 1,
                    "movie_id":1,
                    "rol":"Part of family"
                }
            }
