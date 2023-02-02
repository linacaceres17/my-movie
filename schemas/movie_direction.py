from pydantic import BaseModel

class Movie_direction (BaseModel):
 movie_id: int
 dir_id: int

 class config:
    schema_extra = {
        "example": {
            "movie_id": 2,
            "dir_id": 2
        }
    }