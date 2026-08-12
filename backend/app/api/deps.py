from typing import Generator
from fastapi import Request, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.db.sessions import SessionLocal
from app.models.user import User

def get_db()->Generator:
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


def get_current_user(request: Request, db: Session=Depends(get_db))->User:
    user_id = request.cookies.get("session_user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Пользователь не найден'
        )
    return user