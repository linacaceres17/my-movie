from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Rating(Base):

    __table_name__ = "rating"

    movie_id = Column(Integer,ForeignKey("movie.id"))
    rev_id = Column(Integer,ForeignKey("rev.id"))
    rev_starts = Column(Integer)
    num_o_ratings = Column(Integer)
    