/** @format */

import PageHeader from "../Helper/PageHeader";
import { useRef } from "react";
import { motion, useInView } from "framer-motion";

const Career = () => {
  // Join team
  const joinRef = useRef(null);
  const joinInView = useInView(joinRef, { once: true, margin: "-100px" });

  // Job List
  const jobListRef = useRef(null);
  const jobListInView = useInView(jobListRef, { once: true, margin: "-100px" });

  return (
    <>
      {/* header section */}
      <PageHeader
        title="Career"
        breadcrumb={[{ label: "Home", path: "/home" }, { label: "Career" }]}
      />

      {/*  Join team */}
      <section className="p-10 bg-[#FCFCFC]" ref={joinRef}>
        <div className="flex flex-col items-center justify-between px-6 mx-auto sm:px-8 lg:px-16 md:flex-row">
          {/* Content */}
          <div className="w-full space-y-8 md:w-1/2">
            <motion.h2
              initial={{ opacity: 0, x: -50 }}
              animate={joinInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 1.2 }}
              className="text-2xl sm:text-3xl lg:text-4xl text-[#B3225F] font-bold"
            >
              Join Our Team at imranslab
            </motion.h2>
            <motion.p
              initial={{ opacity: 0, x: 50 }}
              animate={joinInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 1.2, delay: 0.6 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px]"
            >
              At imranslab, we are passionate about pushing the boundaries of
              technology, creativity, and innovation. We are constantly
              exploring new ways to solve challenges and create value for our
              clients. If you are looking for an exciting and dynamic
              environment where you can grow, learn, and make an impact,
              imranslab is the place for you!
            </motion.p>
          </div>
          {/* img */}
          <div className="w-full mt-8 md:w-1/2 md:pl-12 md:mt-0">
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={joinInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1.2 }}
              className="relative flex justify-center"
            >
              <img
                src="https://i.ibb.co.com/d0WpYYHB/Join-Our-Team-at-imranslab.jpg"
                alt="Join-Our-Team"
                className="w-[400px] sm:w-[500px] lg:w-[600px] rounded-lg z-10 hover:scale-105 transition-transform duration-300"
              />
            </motion.div>
          </div>
        </div>
      </section>

      {/* job list */}
      <section className="p-10 bg-[#FCFCFC]" ref={jobListRef}>
        <div className="grid gap-6 md:grid-cols-1 lg:grid-cols-2">
          {/*  Graphics Designer */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={jobListInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 1.2 }}
            className="p-6 transition-shadow duration-300 bg-white rounded-lg shadow-md hover:shadow-xl"
          >
            {/* img */}
            <div>
              <img
                src="https://i.ibb.co/21HBPvct/graphic.png"
                alt="Team meeting"
                className="object-cover w-full mb-4 rounded-lg h-60"
              />
            </div>
            {/* content */}
            <div className="space-y-2">
              <h2 className="text-[#151517] text-[20px] md:text-[22px] lg:text-[25px] font-bold">
                Job Title: Graphics Designer
              </h2>
              <span className="text-[#363a36] text-[16px] md:text-[18px] lg:text-[20px] font-semibold">
                Location: Remote
              </span>
              <h4 className="text-[#363a36] text-[14px] md:text-[16px] lg:text-[18px] font-semibold">
                Job Type: Part-Time
              </h4>
            </div>
            <a
              href="/graphics"
              rel="noopener noreferrer"
              className="inline-block bg-gray-900 text-white px-6 py-2.5 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300 mt-4"
            >
              More Details
            </a>
          </motion.div>

          {/* Intern Software Engineer */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={jobListInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 1.2, delay: 0.4 }}
            className="p-6 transition-shadow duration-300 bg-white rounded-lg shadow-md hover:shadow-xl"
          >
            {/* img */}
            <div>
              <img
                src="https://i.ibb.co/mrzPHyCK/software.png"
                alt="Team meeting"
                className="object-cover w-full mb-4 rounded-lg h-60"
              />
            </div>
            {/* content */}
            <div className="space-y-2">
              <h2 className="text-[#151517] text-[20px] md:text-[22px] lg:text-[25px] font-bold">
                Job Title: Intern Software Engineer
              </h2>
              <span className="text-[#363a36] text-[16px] md:text-[18px] lg:text-[20px] font-semibold">
                Location: Remote
              </span>
              <h4 className="text-[#363a36] text-[14px] md:text-[16px] lg:text-[18px] font-semibold">
                Job Type: Internship (Part-Time)
              </h4>
            </div>
            <a
              href="/software"
              rel="noopener noreferrer"
              className="inline-block bg-gray-900 text-white px-6 py-2.5 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300 mt-4"
            >
              More Details
            </a>
          </motion.div>
        </div>
      </section>
    </>
  );
};

export default Career;
