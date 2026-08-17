import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import type React from 'react';


export const Navbar: React.FC = () => {
    const {user, logout} = useAuth();

    return (
        <nav style={{padding: '1rem', background: '#333', display: 'flex', gap: '1rem'}}>
            <Link to='/' style={{color: '#fff'}}>Главная</Link>
            {user ? (
                <>
                <Link to='/watchlist' style={{color: '#fff'}}>Буду смотреть</Link>
                <span>Привет, {user.username}</span>
                <button onClick={logout}>Выйти</button>
                </>
            ): (
                <>
                <Link to='/login' style={{color: '#fff'}}>Вход</Link>
                <Link to='/register' style={{color: '#fff'}}>Регистрация</Link>
                </>
            )}
        </nav>
    );
};


