from fastapi import APIRouter, HTTPException, status, Response, Depends
from sqlalchemy.orm import Session
from app.db.sessions import SessionLocal
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserRead
from app.core.security import get_password_hash, verify_password


router = APIRouter() 

# POST /api/auth/register 
@router.post('/register', response_model=UserRead)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user_in.username).first():
        raise HTTPException(status_code=400, detail='Имя пользователя занято')
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail='Email уже зарегистрирован')
    
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password)
    )

    db.add(user)
    db.commit()
    db.refresh()
    return user
    
# POST /api/auth/login
@router.post('/login')
def login(user_in: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_in.username).first()
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail='Неверные учетные данные')
    
    response.set_cookie(
        key='session_user_id',
        value=str(user.id),
        httponly=True,
        samesite='lax'
    )
    return {"message": 'Успешная авторизация'}

# POST /api/auth/logout
@router.post("/logout")
def logout(response: Response):
    response.delete_cookie('session_user_id')
    return {'message': 'Успешный выход'}

# GET /api/auth/me
@router.get('/me', response_model=UserRead)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user