import { Navigate } from "react-router-dom";
import useAuth from './hooks/useAuth'

const PublicRoute = ({ children }) => {
    const { user } = useAuth();

    // If user is logged in, redirect to home
    if (user) return <Navigate to="/" replace />;

    return children;
};

export default PublicRoute;
