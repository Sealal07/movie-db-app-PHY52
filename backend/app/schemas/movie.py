from typing import List, Optional
from pydantic import BaseModel

class CastMember(BaseModel):
    id: int
    name: str
    character: str 
    profile_path: Optional[str] = None


class MovieShort(BaseModel):
    id: int 
    title: str 
    poster_path: Optional[str] = None
    release_date: Optional[str] = None
    vote_average: float 

class MovieDetail(MovieShort):
    overview: str 
    cast: List[CastMember] = [] 