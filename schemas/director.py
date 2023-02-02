from pydantic import BaseModel, Field
from typing import Optional


class Director(BaseModel):

    id: Optional[int] = None
    fname: str = Field(max_length=20, min_length=3)
    lname: str = Field(max_length=20, min_length=3)

    class Config:
        schema_extra = {
            "example":{
                'id':1,
                'fname': 'Martin',
                'lname': 'Scorsese'

            }
        }