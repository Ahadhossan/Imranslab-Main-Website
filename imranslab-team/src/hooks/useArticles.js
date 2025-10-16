import { useEffect, useState, useCallback } from "react";
import { jwtDecode } from "jwt-decode";
import apiClient from "../services/apiclient";

const useArticles = () => {
    const [articles, setArticles] = useState([]);
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

    const fetchArticles = useCallback(async () => {
        if (!userId) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.get(`/users/${userId}/article/`);
            setArticles(response.data);
        } catch (err) {
            setError(err.response?.data || "Failed to fetch articles");
        } finally {
            setLoading(false);
        }
    }, [userId]);

    const createArticle = async (articleData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        const formData = new FormData();
        Object.keys(articleData).forEach(key => {
            if (articleData[key] !== null && articleData[key] !== undefined) {
                formData.append(key, articleData[key]);
            }
        });

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.post(
                `/users/${userId}/article/`,
                formData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'multipart/form-data',
                    },
                }
            );
            setArticles(prev => [...prev, response.data]);
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to create article");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const updateArticle = async (articleId, updatedData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        const formData = new FormData();
        Object.keys(updatedData).forEach(key => {
            if (updatedData[key] !== null && updatedData[key] !== undefined) {
                formData.append(key, updatedData[key]);
            }
        });

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.patch(
                `/users/${userId}/article/${articleId}/`,
                formData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'multipart/form-data',
                    },
                }
            );
            setArticles(prev => prev.map(article =>
                article.id === articleId ? response.data : article
            ));
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to update article");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const deleteArticle = async (articleId) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            await apiClient.delete(
                `/users/${userId}/article/${articleId}/`,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                    },
                }
            );
            setArticles(prev => prev.filter(article => article.id !== articleId));
        } catch (err) {
            setError(err.response?.data || "Failed to delete article");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    return {
        userId,
        articles,
        loading,
        error,
        fetchArticles,
        createArticle,
        updateArticle,
        deleteArticle
    };
};

export default useArticles;