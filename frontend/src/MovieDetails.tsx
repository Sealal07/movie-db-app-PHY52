import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { MovieDetails as IMovieDetails } from "./types";
import { api } from "./api/client";
import { useAuth } from "./context/AuthContext";


export const MovieDetails: React.FC = () => {
    const {id} = useParams<{id: string}>();
    const {user} = useAuth();
    const [movie, setMovie] = useState<IMovieDetails | null>(null);
    const [rating, setRating] = useState(10);
    const [content, setContent] = useState('');

    const loadData = async () => {
        const res = await api.get(`/movies/${id}`);
        setMovie(res.data);
    };

    useEffect(()=> {loadData();}, [id]);

    const handleWatchlist = async () => {
        await api.post('/watchlist', {tmdb_movie_id: Number(id)});
        alert('Добавлено!');
    };

    const handleReviewSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        await api.post(`/movies/${id}/reviews`, {rating, content});
        setContent('');
        loadData();
    };

    if (!movie) return <div>Загрузка...</div>

    return (
        <>
        </>
    );
}