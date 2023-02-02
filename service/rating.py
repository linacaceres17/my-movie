from models.rating import Rating as RatingModel
from schemas.rating import Rating

class RatingService():
    def __init__(self,db) -> None:
        self.db = db

    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result

    #crear
    def create_rating(self, rating:Rating):
        new_rating= RatingModel(
            movie_id=rating.movie_id,
            rev_id = rating.rev_id,
            rev_stars= rating.rev_stars,
            num_o_ratings=rating.num_o_ratings
        )
        self.db.add(new_rating)
        self.db.commit()
        return
 
    
    
    