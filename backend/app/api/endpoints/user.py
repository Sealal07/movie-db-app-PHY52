from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.review import Review 
from app.models.user import User
from app.models.watchlist import Watchlist
from app.schemas.review import ReviewRead, ReviewCreate
from app.schemas.watchlist import WatchlistCreate, WatchlistRead
from typing import List


router = APIRouter()
# GET /api/watchlist 
@router.get('/watchlist', response_model=List[WatchlistRead])
def get_to_watchlist(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Watchlist).filter(Watchlist.user_id == current_user.id).all()

# POST /api/watchlist
@router.post('/watchlist', response_model=WatchlistRead)
def add_to_watchlist(
        item: WatchlistCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    existing = db.query(Watchlist).filter(
        Watchlist.user_id == current_user.id,
        Watchlist.tmdb_movie_id == item.tmdb_movie_id
    ).first()
    if existing:
        return existing
    
    new_item = Watchlist(user_id=current_user.id, tmdb_movie_id=item.tmdb_movie_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# DELETE /api/watchlist/{movie_id}
@router.delete('/watchlist/{movie_id}')
def remove_from_watchlist(
    movie_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    item = db.query(Watchlist).filter(
        Watchlist.user_id == current_user.id,
        Watchlist.tmdb_movie_id == movie_id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail='Элемент не найден')
    db.delete(item)
    db.commit()
    return {'message': 'Удалено из списка'}


# POST /api/movies/{movie_id}/reviews
@router.post('/movies/{movie_id}/reviews')
def add_review(
    movie_id: int,
    review_in: ReviewCreate,
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    review = Review(
        user_id = current_user.id,
        tmdb_movie_id=movie_id,
        rating=review_in.rating,
        content=review_in.content
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return ReviewRead(
        id=review.id,
        tmdb_movie_id=review.tmdb_movie_id, 
        rating=review.rating,
        content=review.content,
        author_username=current_user.username,
        created_at=review.created_at
    )



