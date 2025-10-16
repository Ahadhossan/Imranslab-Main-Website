import { useEffect, useState, useCallback } from "react";
import { jwtDecode } from "jwt-decode";
import apiClient from "../services/apiclient";

const useCoreTechnologies = () => {
    const [technologies, setTechnologies] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [userId, setUserId] = useState(null);

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

    const fetchTechnologies = useCallback(async () => {
        if (!userId) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.get(`/users/${userId}/coretechnologies/`);
            setTechnologies(response.data);
        } catch (err) {
            setError(err.response?.data || "Failed to fetch core technologies");
        } finally {
            setLoading(false);
        }
    }, [userId]);

    const createTechnology = async (techData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.post(
                `/users/${userId}/coretechnologies/`,
                techData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'application/json',
                    },
                }
            );
            setTechnologies(prev => [...prev, response.data]);
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to create core technology");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const updateTechnology = async (techId, updatedData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.patch(
                `/users/${userId}/coretechnologies/${techId}/`,
                updatedData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'application/json',
                    },
                }
            );
            setTechnologies(prev => prev.map(tech =>
                tech.id === techId ? response.data : tech
            ));
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to update core technology");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const deleteTechnology = async (techId) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            await apiClient.delete(
                `/users/${userId}/coretechnologies/${techId}/`,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                    },
                }
            );
            setTechnologies(prev => prev.filter(tech => tech.id !== techId));
        } catch (err) {
            setError(err.response?.data || "Failed to delete core technology");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    return {
        userId,
        technologies,
        loading,
        error,
        fetchTechnologies,
        createTechnology,
        updateTechnology,
        deleteTechnology
    };
};

export default useCoreTechnologies;