import { createContext, useContext, useState, useEffect } from "react";
import { User } from "../types";
import { api } from "../api/client";

interface AuthContextType{
    user: User | null;
    loading: boolean;
    login: (credentials: any) => Promise<void>;
    register: (data: any) => Promise<void>;
    logout: () => Promise<void>;
};
    const AuthContex = createContext<AuthContextType | undefined>(undefined);

    export const AuthProvider: React.FC<{children: React.ReactNode}> = ({children})=>{
        const [user, setUser] = useState<User | null>(null);
        const [loading, setLoading] = useState(true);

        useEffect(()=>{
            api.get('/auth/me')
            .then((res)=>setUser(res.data))
            .catch(()=>setUser(null))
            .finally(()=>setLoading(false));
        },[]);

        const login = async (credentials: any) => {
            await api.post('/auth/login', credentials);
            const meRes = await api.get('/auth/me');
            setUser(meRes.data);
        };

        const register = async (data:any) =>{
            await api.post('/auth/register', data);
            await login({username: data.username, password: data.password});
        };

        const logout = async ()=>{
            await api.post('/auth/logout');
            setUser(null);
        };

        return (
            <AuthContex.Provider value={{user, loading, login, register, logout}}>
                {children}
            </AuthContex.Provider>
        );

    };

    export const useAuth = () => {
        const cx = useContext(AuthContex);
        if (!cx) throw new Error('yseAuth must be used within AuthProvider');
        return cx
    };

