import { useEffect, useState, useCallback } from "react";
import { jwtDecode } from "jwt-decode";
import apiClient from "../services/apiclient";

const useContributions = () => {
    const [contributions, setContributions] = useState([]);
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

    const fetchContributions = useCallback(async () => {
        if (!userId) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.get(`/users/${userId}/contribution/`);
            setContributions(response.data);
        } catch (err) {
            setError(err.response?.data || "Failed to fetch contributions");
        } finally {
            setLoading(false);
        }
    }, [userId]);

    const createContribution = async (contributionData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.post(
                `/users/${userId}/contribution/`,
                contributionData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'application/json',
                    },
                }
            );
            setContributions(prev => [...prev, response.data]);
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to create contribution");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const updateContribution = async (contributionId, updatedData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.patch(
                `/users/${userId}/contribution/${contributionId}/`,
                updatedData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'application/json',
                    },
                }
            );
            setContributions(prev => prev.map(contribution =>
                contribution.id === contributionId ? response.data : contribution
            ));
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to update contribution");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const deleteContribution = async (contributionId) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            await apiClient.delete(
                `/users/${userId}/contribution/${contributionId}/`,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                    },
                }
            );
            setContributions(prev => prev.filter(contribution => contribution.id !== contributionId));
        } catch (err) {
            setError(err.response?.data || "Failed to delete contribution");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    return {
        userId,
        contributions,
        loading,
        error,
        fetchContributions,
        createContribution,
        updateContribution,
        deleteContribution
    };
};

export default useContributions;