/** @format */
import { motion } from "framer-motion";
import { useState } from "react";
import { Link } from "react-router-dom";

export default function DesktopMenu({ menu }) {
  const [isHover, setIsHover] = useState(false);

  return (
    <motion.li
      className="relative group"
      onHoverStart={() => setIsHover(true)}
      onHoverEnd={() => setIsHover(false)}
      onFocus={() => setIsHover(true)}
      onBlur={() => setIsHover(false)}
      key={menu.name}
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") {
          setIsHover((prev) => !prev);
        }
      }}
      aria-expanded={isHover}
    >
      <Link
        to={menu.path}
        className="flex items-center gap-1 text-[18px] font-bold hover:bg-white/10 cursor-pointer px-3 py-1 rounded-xl focus:outline-none"
      >
        {menu.name}
      </Link>
      {/* Optional dropdown menu could go here if isHover is true */}
    </motion.li>
  );
}
