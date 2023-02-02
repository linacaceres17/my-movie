from pydantic import BaseModel, Field
from typing import Optional

class Genres(BaseModel):
    id:Optional[int]=None 
    title: str= Field(max_length=20, min_length=3)

    class Config:
        schema_extra={
            "example":{
                'id':2,
                'title': 'Fantasy',
            }
        }