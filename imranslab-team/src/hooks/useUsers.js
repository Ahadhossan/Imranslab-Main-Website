import { useEffect, useState } from "react";
import axios from "../services/apiclient"


const useUsers = ({ role }) => {
    const [users, setUsers] = useState([]);
    const [loadingUsers, setLoadingUsers] = useState(true);
    const [errorUsers, setErrorUsers] = useState(null);

    useEffect(() => {
        const fetchUsers = async () => {
            setLoadingUsers(true)
            try {
                const res = await axios.get("/users/", {
                    params: role ? { role } : {}
                }); // baseURL is already set
                setUsers(res.data.results || []); // safe fallback
            } catch (err) {
                setErrorUsers(err.message || "Error fetching users");
                setLoadingUsers(false);
            } finally {
                setLoadingUsers(false);
            }
        };

        fetchUsers();
    }, [role]);

    return { users, loadingUsers, errorUsers };
};

export default useUsers;