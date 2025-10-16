/** @format */

import { footerLinks } from "../../Data/utils";
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
      <div className="px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-24">
        {/* Brand Column */}
        <motion.div
          initial={{ opacity: 0, x: -30 }}
          whileInView={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true, margin: "-100px" }}
          className="lg:col-span-4"
        >
          <div className="flex items-center gap-2 mb-6">
            <img
              src="https://i.ibb.co/Z0BSXrf/logo.jpg"
              alt="imranslab logo"
              className="w-10 h-10 rounded-full"
            />
            <span className="text-2xl sm:text-3xl font-bold text-[#B3225F]">
              imranslab
            </span>
          </div>
          <p className="text-white text-[15px] leading-relaxed">
            imranslab is a platform that provides comprehensive resources and
            tools for developers, designers, and tech enthusiasts. From
            tutorials and articles to forums and showcases, we empower your tech
            journey.
          </p>

          {/* Social Icons */}
          <motion.nav
            aria-label="Social media"
            className="flex mt-6 gap-4 justify-start"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-100px" }}
            variants={{
              visible: {
                transition: {
                  staggerChildren: 0.2,
                },
              },
            }}
          >
            {[
              {
                href: "https://www.facebook.com/imranslab.dev",
                label: "Facebook",
                image: "https://i.ibb.co/1YpZV3Yd/facebook.png",
              },
              {
                href: "http://www.youtube.com/@imranslab7742",
                label: "YouTube",
                image: "https://i.ibb.co/pjNZkBdV/youtube.png",
              },
              {
                href: "https://www.linkedin.com/company/imranslab/",
                label: "LinkedIn",
                image: "https://i.ibb.co/yFM5n4m8/linkedin.png",
              },
            ].map(({ href, label, image }, i) => (
              <motion.a
                key={label}
                href={href}
                target="_blank"
                rel="noopener noreferrer"
                aria-label={label}
                className={`w-10 h-10 rounded-full flex items-start justify-start transition-transform transform hover:scale-150 hover:rotate-12`}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 * i }}
              >
                <img
                  src={image}
                  alt={label}
                  className="w-8 h-8"
                  loading="lazy"
                />
              </motion.a>
            ))}
          </motion.nav>
        </motion.div>

        {/* Footer Links */}
        <motion.div
          className="lg:col-span-8"
          initial={{ opacity: 0, x: 30 }}
          whileInView={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true, margin: "-100px" }}
        >
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-8">
            {Object.entries(footerLinks).map(([category, links]) => (
              <div key={category}>
                <h3 className="text-[20px] sm:text-[22px] font-bold text-[#B3225F] mb-4">
                  {category}
                </h3>
                <ul className="space-y-3 text-[16px] sm:text-[17px] text-white">
                  {links.map((link, index) => (
                    <li key={index}>
                      <a
                        href={link.href}
                        className="hover:text-[#B3225F] hover:border-b border-[#B3225F] transition"
                      >
                        {link.name}
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </motion.div>
      </div>

      <motion.div
        className="border-t border-gray-300 mt-6 pt-6 text-center text-white text-[17px] sm:text-[19px] px-4 sm:px-6 lg:px-8"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
        <p className="flex justify-center items-center gap-1 flex-wrap">
          © {new Date().getFullYear()} — Created by{" "}
          <span className="text-[#B3225F] font-bold">imranslab Team</span>
          <img
            src="https://i.ibb.co/LXFNfHgv/boy.png"
            alt="Developer emoji"
            className="w-10 h-10 inline-block align-middle"
          />
        </p>
      </motion.div>
    </motion.footer>
  );
};

export default Footer;
