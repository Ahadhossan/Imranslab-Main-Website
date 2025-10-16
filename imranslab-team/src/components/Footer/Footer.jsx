/** @format */

import { motion } from "framer-motion";

const Footer = () => {
  return (
    <motion.footer
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      viewport={{ once: true, margin: "-100px" }}
      className="bg-[#202b5b] w-full"
    >
      <motion.div
        className="mt-6 pt-6 px-4 sm:px-6 lg:px-8 text-white text-[15px] sm:text-[17px]"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
        {/* Footer Links */}
        <div className="flex flex-wrap justify-center gap-6 px-6 py-6">
          <a href="#">About</a>|<a href="#">Our Experts</a>|
          <a href="#">Our Internship</a>|<a href="#">Help & FAQs</a>|
          <a href="/contact">Contact Us</a>|
        </div>

        {/* Footer Text */}
        <div className="text-center">
          <p className="flex flex-wrap items-center justify-center gap-1 text-sm sm:text-base">
            © {new Date().getFullYear()} — Created by{" "}
            <span className="text-[#B3225F] font-bold">imranslab Team</span>
            <img
              src="https://i.ibb.co/LXFNfHgv/boy.png"
              alt="Developer emoji"
              className="inline-block w-8 h-8 align-middle sm:w-10 sm:h-10"
            />
          </p>
        </div>
      </motion.div>
    </motion.footer>
  );
};

export default Footer;
