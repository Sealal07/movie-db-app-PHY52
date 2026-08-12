from datetime import datetime
from pydantic import BaseModel 


class WatchlistCreate(BaseModel):
    tmdb_movie_id: int 

class WatchlistRead(BaseModel):
    id: int
    tmdb_movie_id: int
    added_at: datetime 

    class Config:
        from_attributes = True