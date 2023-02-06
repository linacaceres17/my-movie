from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship


from config.database import Base

class Director(Base):
    
    __tablename__='director'

    id=Column(Integer, primary_key=True)
    fname=Column(String)
    lname= Column(String)