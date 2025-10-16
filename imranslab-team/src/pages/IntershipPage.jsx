/** @format */

import PageHeader from "../Helper/PageHeader";
import { useRef } from "react";
import { motion, useInView } from "framer-motion";
import ScrollToTopButton from "../Helper/ScrollToTopButton";
import ButtonFill from "../Button/ButtonFill";
import { interbenefits } from "../Data/intern";
import InternshipCard from "../components/Internship/InternshipCard";

const IntershipPage = () => {
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

  // Intern section ref
  const internRef = useRef(null);
  const isInternInView = useInView(internRef, { once: true, margin: "-100px" });

  // career section
  const careerRef = useRef(null);
  const isCareerInView = useInView(careerRef, { once: true, margin: "-100px" });

  return (
    <>
      {/* Header Section */}
      <PageHeader title="Our Intership" />

      {/* why choose us */}
      <section className="py-16 bg-[#FCFCFC]" ref={choseRef}>
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
          {interbenefits.map((benefit, index) => (
            <motion.div
              key={index}
              className="bg-[#c8edf3] w-full p-6 rounded-lg shadow-lg transition-all duration-300 ease-in-out transform hover:scale-105 hover:shadow-2xl hover:border hover:border-[#9de5f1] cursor-pointer group"
              initial="hidden"
              animate={isInView ? "visible" : "hidden"}
              custom={index}
              variants={choosecardVariants}
            >
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

      <div className="w-[80%] mx-auto border-b border-black my-6"></div>

      {/* Intern section */}
      <section className=" bg-[#FCFCFC]" ref={internRef}>
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
          {/* Section Header */}
          <div className="mb-16 text-center">
            <motion.h2
              initial={{ opacity: 0, x: 50 }}
              animate={isInternInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.6 }}
              className="text-3xl sm:text-4xl font-bold text-[#B3225F] mb-4"
            >
              Internship Member
            </motion.h2>
            <div className="h-0.5 bg-blue-500 w-14 mx-auto" />
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={isInternInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="text-lg sm:text-xl text-[#151517] pt-3"
            >
              Corporate intern members gain professional experience, mentorship,
              and career development opportunities.
            </motion.p>
          </div>

          <InternshipCard internRef={internRef} />
        </div>
      </section>

      {/* Career Section */}
      <section
        className="py-10 px-4 sm:px-6 lg:px-20 bg-[#FCFCFC]"
        ref={careerRef}
      >
        <motion.div
          initial={{ opacity: 0, y: 60 }}
          animate={isCareerInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.8 }}
          className="flex flex-col-reverse items-center justify-between gap-12 md:flex-row"
        >
          {/* Left Text */}
          <motion.div
            initial={{ opacity: 0, x: -40 }}
            animate={isCareerInView ? { opacity: 1, x: 0 } : {}}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="w-full space-y-8 text-center md:w-1/2 md:text-left"
          >
            <div className="flex items-center justify-center md:justify-start gap-2 bg-[#F3E5C3] w-fit px-4 py-2 rounded-full hover:bg-[#FCDFC5] transition-colors cursor-pointer group mx-auto md:mx-0">
              <span className="text-lg text-blue-600 transition-transform group-hover:scale-110">
                ★
              </span>
              <span className="text-sm text-[#174E4E] hover:text-[#E84F5E] font-medium">
                Online Career Opportunities
              </span>
            </div>

            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-[#141414] leading-tight">
              Start your career at
              <span className="text-[#B3225F]"> imranslab Company</span>
            </h1>

            <p className="text-[#585C58] text-[17px] md:text-[19px] max-w-2xl mx-auto md:mx-0 leading-relaxed">
              Begin your career at imranslab Software Company, where innovation
              meets opportunity. Collaborate with passionate professionals,
              build real-world solutions, and grow your skills in a supportive,
              forward-thinking environment.
            </p>

            <ButtonFill>
              <a href="https://forms.gle/ACuiKs8wb4buHiyt8" target="_blank">
                Apply
              </a>
            </ButtonFill>
          </motion.div>

          {/* Right Image */}
          <motion.div
            initial={{ opacity: 0, x: 40 }}
            animate={isCareerInView ? { opacity: 1, x: 0 } : {}}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="flex justify-center w-full md:w-1/2"
          >
            <img
              src="https://i.ibb.co.com/nNpYVzpQ/Start-your-career-at-imranslab.jpg"
              alt="Career"
              className="object-contain w-full max-w-md md:max-w-lg"
            />
          </motion.div>
        </motion.div>
      </section>

      <ScrollToTopButton />
    </>
  );
};

export default IntershipPage;
