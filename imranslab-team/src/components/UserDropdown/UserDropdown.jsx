import PropTypes from "prop-types";
import { Link, useNavigate } from "react-router-dom";
import { useEffect, useRef } from "react";

const UserDropdown = ({ user, onLogout, closeDropdown }) => {
    const navigate = useNavigate();
    const dropdownRef = useRef(null);

    // Handle click outside
    useEffect(() => {
        const handleClickOutside = (event) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
                closeDropdown();
            }
        };

        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, [closeDropdown]);

    return (
        <div
            ref={dropdownRef}
            className="absolute right-0 mt-2 bg-white border border-gray-200 rounded-lg shadow-lg w-52 z-50 overflow-hidden transition-all duration-300 transform origin-top"
        >
            {/* User Profile Section */}
            <div className="flex items-center px-4 py-3 border-b border-gray-100 bg-gray-50">
                <div className="flex-shrink-0">
                    {user?.image ? (
                        <img
                            className="w-10 h-10 rounded-full object-cover"
                            src={user.image}
                            alt={user.username}
                        />
                    ) : (
                        <div className="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center text-white font-semibold">
                            {user?.username?.charAt(0).toUpperCase()}
                        </div>
                    )}
                </div>
                <div className="ml-3">
                    <p className="text-sm font-medium text-gray-900">{`${user.first_name} ${user.last_name}`}</p>
                    <p className="text-xs text-gray-500">{user?.email}</p>
                </div>
            </div>

            {/* Dropdown Items */}
            <Link
                to={"/profile"}
                className="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-100 transition-colors duration-200"
            >
                Profile
            </Link>

            <button
                onClick={() => {
                    onLogout();
                    closeDropdown();
                    navigate("/login");
                }}
                className="w-full text-left px-4 py-2.5 text-sm text-red-600 hover:bg-gray-100 transition-colors duration-200"
            >
                Logout
            </button>
        </div>
    );
};

UserDropdown.propTypes = {
    user: PropTypes.object,
    onLogout: PropTypes.func.isRequired,
    closeDropdown: PropTypes.func.isRequired,
};

export default UserDropdown;