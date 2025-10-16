/** @format */

import ServiceForm from "./serviceFrom";
import { motion, useInView } from "framer-motion";
import { useRef } from "react";

const ServiceContentFrom = () => {
  // service From
  const servicefromRef = useRef(null);
  const serviefromisInView = useInView(servicefromRef, {
    once: true,
    margin: "-100px",
  });

  return (
    <>
      {/* service From */}
      <section
        className="px-4 py-12 bg-[#FCFCFC] sm:px-6 lg:px-12 mt-24"
        ref={servicefromRef}
      >
        <div className="mx-auto max-w-7xl">
          <div className="mb-12 text-center px-4">
            <motion.h2
              initial={{ opacity: 0, x: -50 }}
              animate={serviefromisInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.6 }}
              className="text-xl sm:text-2xl md:text-3xl lg:text-4xl font-bold text-[#B3225F] mb-4"
            >
              Service Contact Us
            </motion.h2>
            <motion.p
              initial={{ opacity: 0, x: 50 }}
              animate={serviefromisInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.8 }}
              className="text-base sm:text-[13px] md:text-[15px] lg:text-[20px] text-[#585c58] leading-relaxed"
            >
              Looking for a technology partner that understands{" "}
              <br className="hidden md:block" />
              your business and delivers high-quality digital solutions?
            </motion.p>
          </div>

          <div className="grid items-start grid-cols-1 md:grid-cols-2 bg-[#FCFCFC] shadow-2xl border-2 border-[#15919B]">
            {/* Contact Img */}
            <motion.div
              initial={{ opacity: 0, x: -40 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true, margin: "-100px" }}
              className="space-y-8"
            >
              <img
                src="https://i.ibb.co/v618sxQJ/pexels-yankrukov-8867258.jpg"
                alt=""
                className="w-full h-[400px] md:h-[500px] lg:h-[585px] object-cover"
              />
            </motion.div>

            {/* Contact Form */}
            <div>
              <motion.div
                initial={{ opacity: 0, x: 40 }}
                whileInView={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.6 }}
                viewport={{ once: true, margin: "-100px" }}
                className="p-8 bg-white"
              >
                <ServiceForm />
              </motion.div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default ServiceContentFrom;
