import { Link } from "react-router-dom";
import { Movie } from "../types";



export const  MovieCard: React.FC<movie: Movie> = ({movie})=>{
    <div style={{border: '1px solid #ccc', padding: '10px', borderRadius: '8px'}}>
        <img 
        src={movie.poster_path} 
        alt={movie.title}
        width='100%'
        />
        <h3>{movie.title}</h3>
        <p>Рейтинг: {movie.vote_average}</p>
        <Link to={`/movie/${movie.id}`}>Подробнее</Link>
    </div>
}