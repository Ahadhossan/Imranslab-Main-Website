import { useEffect, useState } from "react";
import axios from "../services/apiclient";

const useUserDetail = (id) => {
    const [user, setUser] = useState(null);
    const [loadingUser, setLoadingUser] = useState(true);
    const [errorUser, setErrorUser] = useState(null);

    useEffect(() => {
        if (!id) return;

        const fetchUser = async () => {
            try {
                const res = await axios.get(`/users/${id}/`);
                setUser(res.data);
            } catch (err) {
                setErrorUser(err.message || "Error fetching user");
            } finally {
                setLoadingUser(false);
            }
        };

        fetchUser();
    }, [id]);

    return { user, loadingUser, errorUser };
};

export default useUserDetail;
