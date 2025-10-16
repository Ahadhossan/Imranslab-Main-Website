import { useState, useRef } from "react";
import { Menus } from "../Data/utils";
import DesktopMenu from "./Header/DesktopMenu";
import MobMenu from "./Header/MobMenu";
import UserDropdown from "./UserDropdown/UserDropdown";
import useAuth from "../hooks/useAuth";
import { Link } from "react-router-dom";

const Navbar = () => {
  const { user, logout } = useAuth();
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const dropdownButtonRef = useRef(null);

  return (
    <header className="h-16 text-[15px] fixed inset-0 flex-center bg-[#0A2B42] z-50">
      <nav className="px-3.5 flex-center-between w-full max-w-7xl mx-auto">
        <div className="flex-center gap-x-3 z-[999] relative">
          <Link to={'/'}>
            <img
              src="https://i.ibb.co/DHjPqVSs/Brown-and-Black-Simple-Modern-Company-Developer-Logo-3-removebg-preview.png"
              alt="Logo"
              className="w-32 rounded-full"
            />
          </Link>
        </div>

        {/* Desktop Menu */}
        <ul className="hidden gap-x-1 md:flex-center">
          {Menus.map((menu, index) => (
            <DesktopMenu menu={menu} key={index} />
          ))}
        </ul>

        {/* Auth Buttons or User Dropdown */}
        <div className="hidden md:flex-center gap-x-5">
          {!user ? (
            <>
              <a
                href="/login"
                className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm font-bold sm:text-base rounded-md hover:bg-opacity-80 transition-all"
              >
                Log In
              </a>
            </>
          ) : (
            <div className="relative">
              <button
                ref={dropdownButtonRef}
                onClick={() => setDropdownOpen(!dropdownOpen)}
                className="flex items-center  bg-gray-200 text-white px-1 py-1 rounded-full font-semibold hover:bg-opacity-80 transition"
              >
                {user?.image ? (
                  <img
                    className="w-10 h-10 rounded-full object-cover"
                    src={user.image}
                    alt={user.username}
                  />
                ) : (
                  <div className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-white font-semibold">
                    {user?.username?.charAt(0).toUpperCase()}
                  </div>
                )}
              </button>

              {dropdownOpen && (
                <UserDropdown
                  user={user}
                  onLogout={logout}
                  closeDropdown={() => setDropdownOpen(false)}
                />
              )}
            </div>
          )}
        </div>
        {/* Mobile Menu */}
        <div className="md:hidden">
          <MobMenu Menus={Menus} />
        </div>
      </nav>
    </header>
  );
};

export default Navbar;