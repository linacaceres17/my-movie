from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel, Field


actor_router = APIRouter()


class Actor(BaseModel):
        id: Optional[int] = None
        actor_frist_name: str = Field(max_length=15,min_length=3)
        actor_last_name: str = Field(max_length=15,min_length=3)
        actor_gender: str = Field(max_length=15,min_length=3)
        rol: str = Field(max_length=15,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "id": 1,
                    "actor_last_name": "Vin",
                    "actor_last_name":"Diesel",
                    "actor_gender":"M"
                }
            }
