from models.genres import Genres as GenresMoldel

class GenresService():
    def __init__(self,db) -> None:
        self.db = db

    def get_genres(self):
        result = self.db.query(GenresMoldel).all()
        return result

    # def create_actor(self,actor:ActorMoldel):
    #     new_actor = ActorMoldel(
    #     actor_first_name = actor.actor_first_name ,
    #     actor_last_name = actor.actor_last_name,
    #     actor_gender = actor.actor_gender,    
    #     )
    #     self.db.add(new_actor)
    #     self.db.commit()
    #     return