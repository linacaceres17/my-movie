from models.director import Director as DirectorModel

class DirectorService():

    def __init__(self,db) -> None:
        self.db = db

        def get_director(self) -> DirectorModel:
          result = self.db.query(DirectorModel).all()
          return result


    def get_movie(self,id:int):
        result = self.db.query(DirectorModel).filter(DirectorModel.id == id).first()
        return result

    def get_movies_by_release_contry(self,release_contry:str):
        result = self.db.query(DirectorModel).filter(DirectorModel.release_contry == release_contry).all()
        return result        
