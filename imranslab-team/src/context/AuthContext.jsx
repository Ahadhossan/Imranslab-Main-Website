/* eslint-disable react-refresh/only-export-components */
import { createContext, useState, useEffect } from "react";
import axios from "../services/apiclient"

export const AuthContext = createContext()

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loadingUser, setLoadingUser] = useState(true);

    useEffect(() => {
        const fetchUser = async () => {
            const access = localStorage.getItem("access");
            if (access) {
                try {
                    const res = await axios.get("/auth/users/me/", {
                        headers: {
                            Authorization: `JWT ${access}`,
                        },
                    });
                    setUser(res.data);
                } catch (err) {
                    console.error("Error loading user", err);
                }
            }
            setLoadingUser(false);
        };

        fetchUser();
    }, []);

    return (
        <AuthContext.Provider value={{ user, setUser, loadingUser }}>
            {children}
        </AuthContext.Provider>
    )
}

