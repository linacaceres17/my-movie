from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class MoviesGenres(Base):

    __table_name__ = "movie_genres" 

    movie_id = Column(Integer, ForeignKey("movie.id"))
    gen_id = Column(Integer, ForeignKey("genres.id"))
