from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.review import Review 
from app.schemas.review import ReviewRead
from app.services import tmdb


router = APIRouter()

# GET /api/movies
@router.get('/')
def get_movies(page: int = Query(1, ge=1)):
    return tmdb.get_popular_movies(page=page)

# GET /api/movies/{movie_id}
@router.get('/{movie_id}')
def get_movie_detail(movie_id: int, db: Session = Depends):
    details = tmdb.get_movie_details(movie_id)
    credits_data = tmdb.get_movie_credits(movie_id)
    revies_db = db.query(Review).filter(Review.tmdb_movie_id == movie_id).all()

    reviews = [
        ReviewRead(
            id=r.id,
            tmdb_movie_id=r.tmdb_movie_id,
            ratinf=r.rating,
            content=r.content,
            author_username=r.user.username,
            created_at=r.created_at
        )
        for r in revies_db
    ]

    details['cast'] = credits_data
    details['reviews'] = reviews
    return details


