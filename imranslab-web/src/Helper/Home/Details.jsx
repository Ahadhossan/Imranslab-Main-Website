/** @format */

import { useRef } from "react";
import { motion } from "framer-motion";

const Details = ({ desc, time, isLeft }) => {
  const ref = useRef(null);

  return (
    <li
      ref={ref}
      className={`relative w-full flex flex-col md:flex-row items-center justify-between my-12 ${
        isLeft ? "md:flex-row" : "md:flex-row-reverse"
      }`}
    >
      {/* Content block */}
      <motion.div
        initial={{ y: 50, opacity: 0 }}
        whileInView={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.6, type: "spring" }}
        className="w-full md:w-[45%] text-end bg-[#FCFCFC] p-6 shadow-lg rounded-xl border border-gray-200 hover:shadow-2xl "
      >
        <h2 className="font-semibold text-lg sm:text-xl md:text-2xl lg:text-3xl text-[#151517] mb-2">
          {time}
        </h2>
        <p className="font-medium text-base sm:text-[15px] md:text-[17px] lg:text-[19px] text-[#585c58]">
          {desc}
        </p>
      </motion.div>
    </li>
  );
};

export default Details;
