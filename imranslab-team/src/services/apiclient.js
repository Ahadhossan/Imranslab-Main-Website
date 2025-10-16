import axios from "axios";

const APICLIENT = import.meta.env.VITE_APICLIENT || "https://imranslab-team.imranslab.org/"

const apiClient = axios.create({
    baseURL: APICLIENT,
    headers: {
        'Content-Type': "application/json"
    }
})

// Request Interceptor: attach access token
apiClient.interceptors.request.use((config) => {
    const access = localStorage.getItem("access");
    if (access) {
        config.headers.Authorization = `JWT ${access}`;
    }
    return config;
});

// Response Interceptor: refresh token if access token is expired
apiClient.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        // If access token expired
        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            try {
                const refresh = localStorage.getItem("refresh");

                if (refresh) {
                    const res = await apiClient.post("/auth/jwt/refresh/", { refresh })
                    const newAccess = res.data.access;

                    localStorage.setItem("access", newAccess);
                    apiClient.defaults.headers.Authorization = `JWT ${newAccess}`;
                    originalRequest.headers.Authorization = `JWT ${newAccess}`;

                    return apiClient(originalRequest);
                }
            } catch {
                localStorage.removeItem("access");
                localStorage.removeItem("refresh");
                window.location.href = "/login"; // Optional: redirect to login page
            }
        }
        return Promise.reject(error);
    }
);

export default apiClient;