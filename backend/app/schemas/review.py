from datetime import datetime
from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=10)
    content: str 

class ReviewRead(BaseModel):
    id: int 
    tmdb_movie_id: int 
    rating: int 
    content: str 
    author_username: str 
    created_at: datetime

    class Config:
        from_attributes = True

