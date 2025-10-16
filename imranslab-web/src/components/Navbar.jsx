/** @format */

import { Menus } from "../Data/utils";
import DesktopMenu from "./Header/DesktopMenu";
import MobMenu from "./Header/MobMenu";

const Navbar = () => {
  return (
    <header className="h-16 text-[15px] fixed inset-0 flex-center bg-[#0A2B42] z-50">
      <nav className="px-3.5 flex-center-between w-full max-w-7xl mx-auto">
        <div className="flex-center gap-x-3 z-[999] relative">
          <a href="/">
            <img
              src="https://i.ibb.co/Z0BSXrf/logo.jpg"
              alt="Logo"
              className="w-12 rounded-full"
            />
          </a>
        </div>

        {/* Desktop Menu */}
        <ul className="gap-x-1 lg:flex-center hidden">
          {Menus.map((menu, index) => (
            <DesktopMenu menu={menu} key={index} />
          ))}
        </ul>

        <div className="flex-center gap-x-5">
          <a
            href="/contact"
            className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm font-bold sm:text-base rounded-md hover:bg-opacity-80 transition-all"
          >
            Contact
          </a>

          {/* Mobile Menu */}
          <div className="lg:hidden">
            <MobMenu Menus={Menus} />
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
