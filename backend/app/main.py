from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.sessions import engine
from app.db.base import Base
from api.endpoints import auth,movies,user


Base.metadata.create_all(bind=engine)

app = FastAPI(title='Movie DB API')
app.add_middleware(
    CORSMiddleware, 
    allow_origins=['http://localhost:5173', 'http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth.router, prefix='/api/auth', tags=['auth'])
app.include_router(movies.router, prefix='/api/movies', tags=['movies'])
app.include_router(user.router, prefix='/api', tags=['user'])