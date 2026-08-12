from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Movie DB App"
    DATABASE_URL: str = "sqlite:///./movies.sqlite3"
    SECRET_KEY: str = "SUPER_SECRET_KEY"
    TMDB_API_KEY: str = "enter key!!!!!!!!!!!!!!" # KEY
    TMDB_BASE_URL: str = "https://api.themoviedb.org/3"

class Config: 
    env_file = ".env"

settings = Settings()
