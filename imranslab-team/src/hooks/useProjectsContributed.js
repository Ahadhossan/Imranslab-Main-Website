import { useEffect, useState, useCallback } from "react";
import { jwtDecode } from "jwt-decode";
import apiClient from "../services/apiclient";

const useProjectsContributed = () => {
    const [projects, setProjects] = useState([]);
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

    const fetchProjects = useCallback(async () => {
        if (!userId) return;

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.get(`/users/${userId}/projectscontributed/`);
            setProjects(response.data);
        } catch (err) {
            setError(err.response?.data || "Failed to fetch contributed projects");
        } finally {
            setLoading(false);
        }
    }, [userId]);

    const createProject = async (projectData) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        const formData = new FormData();
        Object.keys(projectData).forEach(key => {
            if (projectData[key] !== null && projectData[key] !== undefined) {
                formData.append(key, projectData[key]);
            }
        });

        setLoading(true);
        setError(null);
        try {
            const response = await apiClient.post(
                `/users/${userId}/projectscontributed/`,
                formData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'multipart/form-data',
                    },
                }
            );
            setProjects(prev => [...prev, response.data]);
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to create project");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const updateProject = async (projectId, updatedData) => {
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
                `/users/${userId}/projectscontributed/${projectId}/`,
                formData,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                        'Content-Type': 'multipart/form-data',
                    },
                }
            );
            setProjects(prev => prev.map(project =>
                project.id === projectId ? response.data : project
            ));
            return response.data;
        } catch (err) {
            setError(err.response?.data || "Failed to update project");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    const deleteProject = async (projectId) => {
        if (!userId) return;
        const access = localStorage.getItem("access");
        if (!access) return;

        setLoading(true);
        setError(null);
        try {
            await apiClient.delete(
                `/users/${userId}/projectscontributed/${projectId}/`,
                {
                    headers: {
                        'Authorization': `JWT ${access}`,
                    },
                }
            );
            setProjects(prev => prev.filter(project => project.id !== projectId));
        } catch (err) {
            setError(err.response?.data || "Failed to delete project");
            throw err;
        } finally {
            setLoading(false);
        }
    };

    return {
        userId,
        projects,
        loading,
        error,
        fetchProjects,
        createProject,
        updateProject,
        deleteProject
    };
};

export default useProjectsContributed;