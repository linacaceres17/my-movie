from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Reviewer(Base):

    __table_name__ = "reviewer"

    rev_id = Column(Integer,ForeignKey("rev.id"))
    rev_name=Column(Integer)