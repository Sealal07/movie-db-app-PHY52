export interface User {
    id: number;
    username: string;
    email: string;
    created_at: string;
}

export interface CastMember{
    id: number;
    name: string;
    character: string;
    profile_path: string | null;
}

export interface Movie{
    id:  number;
    title: string; 
    poster_path:  string | null; 
    release_date: string | null; 
    vote_average:  number;  
}

export interface Review{
    id: number;
    tmdb_movie_id: number;
    rating: number;
    content: string; 
    author_username: string; 
    created_at: string;
}

export interface MovieDetails extends Movie{
    overview: string,
    cast: CastMember[];
    reviews: Review[];
}

export interface WatchlistItem{
    id: number;
    tmdb_movie_id: number;
    added_at: string;
}
