import { Navigate } from "react-router-dom";
import useAuth from './hooks/useAuth'

const PrivateRoute = ({ children }) => {
    const { user } = useAuth();
    // If user is logged in, redirect to home
    if (!user) return <Navigate to="/login" replace />;

    return children;

}

export default PrivateRoute