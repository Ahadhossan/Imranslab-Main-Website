import { useEffect, useState, useCallback } from "react";
import { jwtDecode } from "jwt-decode";
import apiClient from "../services/apiclient";

const useSocialMediaLinks = () => {
    const [links, setLinks] = useState([]);
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

    // Fetch all social media links
    const fetchLinks = useCallback(async () => {
        if (!userId) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.get(`/users/${userId}/socialmedialinks/`);
            setLinks(response.data);
        } catch (err) {
            setError(err.response?.data || "Failed to fetch social media links");
        } finally {
            setLoading(false);
        }
    }, [userId]);

    // Create a new social media link
    const createLink = async (linkData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.post(
                `/users/${userId}/socialmedialinks/`,
                linkData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'application/json',
                    },
                }
            );
            setLinks(prev => [...prev, response.data]);
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to create social media link");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    // Update a social media link
    const updateLink = async (linkId, updatedData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.patch(
                `/users/${userId}/socialmedialinks/${linkId}/`,
                updatedData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'application/json',
                    },
                }
            );
            setLinks(prev => prev.map(link =>
                link.id === linkId ? response.data : link
            ));
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to update social media link");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    // Delete a social media link
    const deleteLink = async (linkId) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            await apiClient.delete(
                `/users/${userId}/socialmedialinks/${linkId}/`,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                    },
                }
            );
            setLinks(prev => prev.filter(link => link.id !== linkId));
        } catch (err) {
            setError(err.response?.data || "Failed to delete social media link");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    return {
        userId,
        links,
        loading,
        error,
        fetchLinks,
        createLink,
        updateLink,
        deleteLink
    };
};

export default useSocialMediaLinks;