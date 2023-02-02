from models.movie_direction import Movie_direction as MovieDirectionModel
from schemas.movie_direction import Movie_direction

class MovieDirectionService():
    def __init__(self,db) -> None:
        self.db = db

def get_movie_direction(self):
        result = self.db.query(MovieDirectionModel).all()
        return result

def create_movie_direction(self,movie_direction: MovieDirectionModel):
        new_direction = MovieDirectionModel(
            movie_id = movie_direction.movie_id,
            dir_id = movie_direction.dir_id
        )
        self.db.add(new_direction)
        self.db.commit()
        return