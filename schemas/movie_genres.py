from pydantic import BaseModel

class Movie_genres(BaseModel):

    movie_id: int
    gen_id: int 

    class Config:
        schema_extra={
            "example": {
                'movie_id': 3,
                'gen_id': 5, 
            }
        }