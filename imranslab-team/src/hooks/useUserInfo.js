import { useEffect, useState, useCallback } from "react";
import { jwtDecode } from "jwt-decode";
import apiClient from "../services/apiclient";

const useUserInfo = () => {
    const [userData, setUserData] = useState({
        first_name: "",
        last_name: "",
        role: "",
        personalinterests: "",
        aboutme: "",
        email: "",
        position: "",
        address: "",
        phone: "",
        birth_date: "",
        image: ""
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [userId, setUserId] = useState(null);

    // Get user ID from JWT token on hook initialization
    useEffect(() => {
        const token = localStorage.getItem("access");
        if (token) {
            try {
                const decoded = jwtDecode(token);
                if (decoded.user_id) {
                    setUserId(decoded.user_id);
                }
            } catch (err) {
                console.error("Failed to decode token:", err);
                setError("Failed to authenticate user");
            }
        }
    }, []);

    // Fetch user data
    const fetchUser = useCallback(async () => {
        if (!userId) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.get(`/users/${userId}/`);
            setUserData(response.data);
        } catch (err) {
            setError(err.response?.data || "Failed to fetch user data");
        } finally {
            setLoading(false);
        }
    }, [userId]);

    // Update partial user data
    const updateUser = async (partialData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;
        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.put(`/users/${userId}/`, partialData, {
                headers: {
                    'Authorization': `JWT ${access}`,
                    'Content-Type': 'multipart/form-data',
                },
            });
            setUserData(prev => ({ ...prev, ...response.data }));
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to update user data");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    // Delete user
    const deleteUser = async () => {
        if (!userId) return;

        setLoading(true);
        setError(null);
        try {
            await apiClient.delete(`/users/${userId}/`);
            setUserData({
                first_name: "",
                last_name: "",
                role: null,
                personalinterests: "",
                aboutme: "",
                email: "",
                position: "",
                address: "",
                phone: "",
                birth_date: null,
                image: null
            });
        } catch (err) {
            setError(err.response?.data || "Failed to delete user");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    return {
        userId,
        userData,
        loading,
        error,
        fetchUser,
        updateUser,
        deleteUser
    };
};

export default useUserInfo;
