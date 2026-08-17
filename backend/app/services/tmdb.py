import requests
from fastapi import HTTPException
from app.core.config import settings 

def get_popular_movies(page: int = 1) -> dict:
    url = f"{settings.TMDB_BASE_URL}/movie/now_playing"
    params ={
        "api_key": settings.TMDB_API_KEY,
        "page": page,
        "language": "ru-RU"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Ошибка при запросе к TMDB API")
    return response.json()



def  get_movie_details(movie_id: int) -> dict:
    url = f"{settings.TMDB_BASE_URL}/movie/{movie_id}"
    params ={
        "api_key": settings.TMDB_API_KEY,
        "language": "ru-RU"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail='Фильм не найден')
    return response.json()

def get_movie_credits(movie_id: int):
    url = f"{settings.TMDB_BASE_URL}/movie/{movie_id}/credits"
    params ={
        "api_key": settings.TMDB_API_KEY,
        "language": "ru-RU"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []
    cast = response.json().get('cast', [])
    return [
        {
            "id": member['id'],
            "name": member['name'],
            "character": member['character'],
            "profile_path": member['profile_path'] 
        }
        for member in cast[:10]
    ]