import { useContext, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import axios from "../services/apiclient"


const useAuth = () => {
    const { user, setUser, loadingUser } = useContext(AuthContext);
    const [authLoading, setAuthLoading] = useState(false);
    const [authError, setAuthError] = useState(null);

    const login = async (username, password) => {
        setAuthLoading(true);
        setAuthError(null);
        try {
            const response = await axios.post("/auth/jwt/create/", { username, password });

            const { access, refresh } = response.data;
            localStorage.setItem("access", access);
            localStorage.setItem("refresh", refresh);

            // Get the current user info
            const userRes = await axios.get("/auth/users/me/", {
                headers: {
                    Authorization: `JWT ${access}`,
                },
            });

            setUser(userRes.data);
        } catch (error) {
            setAuthError(error.response?.data || "Login failed");
        } finally {
            setAuthLoading(false);
        }
    };

    const signup = async (username, password, email) => {
        setAuthLoading(true);
        setAuthError(null);
        try {
            await axios.post("/auth/users/", { username, password, email });

            // Auto-login after successful registration (optional)
            await login(username, password);
        } catch (error) {
            // Format the error response to be more user-friendly
            if (error.response?.data) {
                // Convert object errors to string messages
                const errorMsgs = Object.entries(error.response.data)
                    .map(([key, value]) => `${key}: ${Array.isArray(value) ? value.join(' ') : value}`)
                    .join('\n');
                setAuthError(errorMsgs);
            } else {
                setAuthError("Signup failed. Please try again.");
            }
        } finally {
            setAuthLoading(false);
        }
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
    };



    return {
        login,
        signup,
        logout,
        user,
        loadingUser,
        authLoading,
        authError,
    };
};

export default useAuth;