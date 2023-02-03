from models.movie_genres import MoviesGenres as MovieGenresModel
from schemas.movie_genres import MovieGenres

class MovieGenresService():
    def __init__(self,db) -> None:
        self.db = db

def get_movie_genres(self):
        result = self.db.query(MovieGenresModel).all()
        return result

def create_movie_genres(self,movie_genres: MovieGenresModel):
        new_direction = MovieGenresModel(
            movie_id = movie_genres.movie_id,
            gen_id = movie_genres.gen_id
        )
        self.db.add()
        self.db.commit()
        return