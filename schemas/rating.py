from pydantic import BaseModel


class Rating(BaseModel):
    movie_id: int
    rev_id: int
    rev_stars: int
    num_o_ratings: int

    class config:
        schema_extra = {
            "example":{
                "movie_id": 1,
                "rev_id":1,
                "rev_starts":2,
                "num_o_ratings":3
            }
        }
