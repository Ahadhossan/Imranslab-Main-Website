/** @format */

import PageHeader from "../Helper/PageHeader";
import { benefits } from "../Data/expert";
import { useRef } from "react";
import { motion, useInView } from "framer-motion";
import ScrollToTopButton from "../Helper/ScrollToTopButton";
import LeaderSection from "../components/LeaderSection/LeaderSection";
import Leadershipteam from "../components/LeaderSection/Leadershipteam"
import TeamStatistics from "../components/LeaderSection/TeamStatistics";

const HomePage = () => {
  // choose section ref
  const choseRef = useRef(null);
  const isInView = useInView(choseRef, { once: true, margin: "-100px" });
  // Animation variants
  const choosecardVariants = {
    hidden: { opacity: 0, y: 40 },
    visible: (i) => ({
      opacity: 1,
      y: 0,
      transition: {
        delay: i * 0.2,
        duration: 0.6,
        ease: "easeOut",
      },
    }),
  };
  // CEO section ref
  const ceoRef = useRef(null);
  // Experts section ref
  const expertRef = useRef(null);
  // Team Statistics
  const teamRef = useRef(null);
  return (
    <>
      {/* Header Section */}
      <PageHeader
        title="Our Experts"
        breadcrumb={[{ label: "Home", path: "/home" }, { label: "Experts" }]}
      />

      {/* why choose us */}
      <section className="py-6 bg-[#FCFCFC]" ref={choseRef}>
        <div className="w-full px-5 mb-10 text-center md:px-16">
          <motion.h1
            initial={{ opacity: 0, x: -50 }}
            animate={isInView ? { opacity: 1, x: 0 } : {}}
            exit={{ opacity: 0, x: 50 }}
            transition={{ duration: 0.6 }}
            className="text-xl sm:text-2xl md:text-3xl font-bold text-[#B3225F]"
          >
            Why Choose Us
          </motion.h1>
        </div>
        <div className="grid gap-8 px-5 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 sm:px-8 md:px-12">
          {benefits.map((benefit, index) => (
            <motion.div
              key={index}
              className="bg-[#c8edf3] w-full p-6 rounded-lg shadow-lg transition-all duration-300 ease-in-out transform hover:scale-105 hover:shadow-2xl hover:border hover:border-[#9de5f1] cursor-pointer group"
              initial="hidden"
              animate={isInView ? "visible" : "hidden"}
              custom={index}
              variants={choosecardVariants}
            >
              {benefit.iconType === "image" ? (
                <img
                  src={benefit.icon}
                  alt={benefit.title}
                  className="w-12 h-12"
                />
              ) : (
                <i className={`${benefit.icon} mb-4`}></i>
              )}
              <h3 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                {benefit.title}
              </h3>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                {benefit.description}
              </p>
            </motion.div>
          ))}
        </div>
      </section>
      {/* leader section */}
      <section className="py-20 bg-[#FCFCFC]" ref={ceoRef}>
        <LeaderSection ceoRef={ceoRef} />
      </section>
      <div className="w-[90%] mx-auto border-b border-black my-6"></div>
      {/* leadershipteam section */}
      <section className=" bg-[#FCFCFC]" ref={expertRef}>
        <Leadershipteam expertRef={expertRef} />
      </section>
      <div className="w-[80%] mx-auto border-b border-black my-6"></div>
      {/* Team Statistics section  */}
      <section className="w-full px-5 py-16 text-center md:px-16" ref={teamRef}>
        {/* Team Statistics */}
        <TeamStatistics teamRef={teamRef} />
      </section>
      <ScrollToTopButton />
    </>
  );
};

export default HomePage;
