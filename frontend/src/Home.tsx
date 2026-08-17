import { useEffect, useState } from "react";
import { Movie } from './types';
import { MovieCard } from "./components/MovieCard";
import { api } from "./api/client";


export const Home: React.FC = () => {
    const [movies, setMpvies] = useState<Movie[]>([]);
    const [page, setPage] = useState(1);
    const [loading, setLoading] = useState(false);

    const fetchMovies = async () => {
        setLoading(true);
        try{
            const res = await api.get(`/movies?page=${page}`);
            setMpvies((prev)=>[...prev, ...res.data.results]);
        } catch (err){
            console.error(err);
        }finally {
            setLoading(false);
        }
    };

    useEffect(()=>{
        fetchMovies();
    },[page]);

    useEffect(()=>{
        const handleScroll = () => {
            if (window.innerHeight + document.documentElement.scrollTop + 1 >= document.documentElement.scrollHeight){
                if(!loading) setPage((prev)=> prev + 1);
            }
        };
        window.addEventListener('scroll', handleScroll);
        return ()=>window.removeEventListener('scroll', handleScroll);
    }, [loading]);

    return (
        <div style={{padding: '20px'}}>
            <h1>Новинки кино</h1>
            <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fill, mimax(200px, 1fr))', gap: '20px'}}>
                {movies.map((m, idx)=> (
                    <MovieCard key={`${m.id}-${idx}`} movie={m} />
                ))}
            </div>
            {loading && <p>Загрузка...</p>}

        </div>

    );

};