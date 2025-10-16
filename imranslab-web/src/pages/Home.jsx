/** @format */

import { useState, useRef } from "react";
import { HiArrowRight } from "react-icons/hi";
import { motion, useInView, AnimatePresence } from "framer-motion";
import ButtonFill from "../Button/ButtonFill";
import ScrollToTopButton from "../Helper/ScrollToTopButton";
import Faq from "../Helper/Home/Faq";
import { homeprojects } from "../Data/home";
import Story from "../Helper/Home/Story";
import AnimatedCanvas from "../Helper/Home/StarBackground";
import { FaDocker, FaNodeJs, FaPython, FaReact } from "react-icons/fa";

const Home = () => {
  const [submitted, setSubmitted] = useState(false);
  // hero section
  const heroRef = useRef(null);
  const heroInView = useInView(heroRef, { once: true, margin: "-100px" });
  // project section
  const sectionRef = useRef(null);
  const isInView = useInView(sectionRef, { once: true, margin: "-100px" }); // triggers when slightly in view
  // best company
  const bestCompanyRef = useRef(null);
  const companyInView = useInView(bestCompanyRef, {
    once: true,
    margin: "-100px",
  });
  // story section
  const storyRef = useRef(null);
  const storyInView = useInView(storyRef, { once: true, margin: "-100px" });
  // education section
  const educationRef = useRef(null);
  const educationInView = useInView(educationRef, {
    once: true,
    margin: "-100px",
  });
  // banner section
  // const bannerRef = useRef(null);
  // const isBannerInView = useInView(bannerRef, { once: true, margin: "-100px" });
  // newsletter section
  const newsletterRef = useRef(null);
  const isNewsletterInView = useInView(newsletterRef, {
    once: true,
    margin: "-100px",
  });

  // Project Card
  const cardVariants = {
    hidden: { opacity: 0, y: 40 },
    visible: (i) => ({
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.7,
        delay: i * 0.3,
      },
    }),
  };

  // newsletter submit from
  const onSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    formData.append("access_key", "276695ce-1e44-4cb0-bc1f-df51e6a92587");

    const object = Object.fromEntries(formData);
    const json = JSON.stringify(object);

    const res = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: json,
    }).then((res) => res.json());

    if (res.success) {
      setSubmitted(true);
      event.target.reset();
      setTimeout(() => {
        setSubmitted(false);
      }, 5000); // Auto-hide after 5 seconds
    }
  };

  // hero section

  const floatVariants = {
    initial: { y: 0 },
    animate: {
      y: [0, -10, 0],
      transition: {
        duration: 3,
        repeat: Infinity,
        ease: "easeInOut",
      },
    },
  };

  return (
    <>
      <div>
        {/* Hero Section */}
        <section
          ref={heroRef}
          className="relative min-h-[400px] pt-28 pb-12 sm:pb-16 lg:pb-20 px-4 sm:px-6 lg:px-8 overflow-hidden text-white bg-gradient-to-r from-slate-900 to-slate-700"
        >
          {/* Background */}
          <div className="absolute inset-0 z-0">
            <AnimatedCanvas />
            <div className="absolute inset-0 bg-gradient-to-t from-[#0f172a]/90 to-transparent z-10" />
          </div>

          {/* Content Wrapper */}
          <div className="relative z-30 grid items-center grid-cols-1 gap-10 mx-auto max-w-7xl lg:grid-cols-2">
            {/* Left Content */}
            <div className="flex flex-col items-start w-full space-y-8 text-start">
              {/* Subtitle */}
              <motion.span
                initial={{ opacity: 0, x: -50 }}
                animate={heroInView ? { opacity: 1, x: 0 } : {}}
                transition={{ duration: 0.8 }}
                className="inline-flex items-center gap-2 px-5 py-2 text-base font-semibold text-white bg-blue-900 rounded-lg shadow-md md:text-lg"
              >
                Explain your project!
                <img
                  src="https://i.ibb.co/qY72fV0n/hero-icon.gif"
                  alt=""
                  className="w-9 h-9"
                />
              </motion.span>

              {/* Heading */}
              <motion.h1
                initial={{ opacity: 0, y: -30 }}
                animate={heroInView ? { opacity: 1, y: 0 } : {}}
                transition={{ duration: 1.2 }}
                className="max-w-3xl text-2xl font-bold leading-snug sm:text-3xl md:text-4xl lg:text-5xl"
              >
                We Are Experts In{" "}
                <span className="text-[#B3225F]">
                  Design, App, and Developments
                </span>
              </motion.h1>

              {/* Icons near heading */}
              <motion.div
                initial={{ opacity: 0, y: 50 }}
                animate={heroInView ? { opacity: 1, y: 0 } : {}}
                exit={{ opacity: 0, y: -50 }}
                transition={{ duration: 1 }}
                className="z-30 flex flex-wrap items-start justify-start gap-6 lg:hidden"
              >
                <motion.div
                  className="text-4xl text-blue-400"
                  variants={floatVariants}
                  initial="initial"
                  animate="animate"
                >
                  <FaReact />
                </motion.div>
                <motion.div
                  className="text-3xl text-green-400"
                  variants={floatVariants}
                  initial="initial"
                  animate="animate"
                >
                  <FaNodeJs />
                </motion.div>
                <motion.div
                  className="text-3xl text-yellow-300"
                  variants={floatVariants}
                  initial="initial"
                  animate="animate"
                >
                  <FaPython />
                </motion.div>
                <motion.div
                  className="text-3xl text-cyan-400"
                  variants={floatVariants}
                  initial="initial"
                  animate="animate"
                >
                  <FaDocker />
                </motion.div>
              </motion.div>

              {/* CTA */}
              <motion.a
                href="/contact"
                initial={{ opacity: 0, y: 20 }}
                animate={heroInView ? { opacity: 1, y: 0 } : {}}
                transition={{ type: "spring", stiffness: 60, delay: 0.5 }}
                className="mt-4 inline-block bg-[#07080a] text-white px-6 py-3 text-sm sm:text-base rounded-md shadow hover:bg-black hover:scale-105 active:scale-95 transition-transform duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-[#B3225F]"
              >
                Get Started
              </motion.a>
            </div>

            {/* Right Image */}
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={heroInView ? { opacity: 1, scale: 1 } : {}}
              exit={{ opacity: 0, scale: 0.9 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="items-center justify-center hidden lg:flex"
            >
              <img
                src="https://i.ibb.co.com/67zJVdPm/hero-removebg-preview.png"
                alt="Hero"
              />
            </motion.div>
          </div>
        </section>

        {/* Best Company Section */}
        <section
          className="px-4 sm:px-6 lg:px-24 py-10 bg-[#FCFCFC]"
          ref={bestCompanyRef}
        >
          <div className="flex flex-col-reverse items-center justify-between gap-12 mx-auto md:flex-row max-w-9xl">
            {/* Left Column (Image) */}
            <motion.div
              initial={{ opacity: 0, x: -50 }}
              animate={companyInView ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.8 }}
              className="flex justify-center w-full md:w-1/2 md:justify-start"
            >
              <img
                src="https://i.ibb.co/VPpZz5X/about.png"
                alt="Team meeting"
                className="w-[300px] sm:w-[400px] md:w-[500px] lg:w-[550px] rounded-lg hover:scale-105 transition-transform duration-300 ease-in-out shadow-lg"
              />
            </motion.div>

            {/* Right Column (Text Content) */}
            <motion.div
              initial={{ opacity: 0, x: 50 }}
              animate={companyInView ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="w-full space-y-6 text-center md:w-1/2 md:text-left"
            >
              <h3 className="text-2xl md:text-3xl lg:text-4xl font-bold text-[#B3225F] leading-tight">
                Welcome imranslab!
              </h3>
              <h1 className="text-2xl md:text-3xl lg:text-4xl font-bold text-[#151517] leading-tight">
                The best software company
              </h1>
              <p className="text-[15px] md:text-[19px] text-[#585c58] max-w-xl mx-auto md:mx-0">
                Join us as we innovate, create, and build impactful software
                solutions. Explore endless opportunities for growth,
                collaboration, and professional development in a dynamic,
                forward-thinking environment. Let’s shape the future together!
              </p>
              <a
                href="https://imranslab.atlassian.net/wiki/x/uADbKg"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
              >
                More Details
              </a>
            </motion.div>
          </div>
        </section>

        {/* Our Story */}
        <section
          className="w-full bg-[#FCFCFC] py-16 px-4 sm:px-6 lg:px-8 text-center"
          ref={storyRef}
        >
          <motion.h2
            initial={{ opacity: 0, y: 30 }}
            animate={storyInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.6 }}
            className="text-2xl font-bold text-black sm:text-3xl md:text-4xl"
          >
            imranslab – Our Story
          </motion.h2>

          <motion.div
            initial={{ opacity: 0 }}
            animate={storyInView ? { opacity: 1 } : {}}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="max-w-4xl mx-auto"
          >
            <p className="text-[#585c58] text-base sm:text-lg mt-4 leading-relaxed">
              Started in 2020, imranslab began as a small group of passionate
              developers with one goal: to build meaningful, accessible, and
              powerful technology for education, innovation, and empowerment.
            </p>
            <p className="text-[#585c58] text-base sm:text-lg mt-4 leading-relaxed">
              From launching our first LMS and OCR research pipeline to
              integrating AI automation, CI/CD systems, and open-source
              contributions, we have consistently prioritized clarity, purpose,
              and curiosity—our core values.
            </p>
          </motion.div>

          <Story />
        </section>

        {/* Online Education Platform */}
        <section
          className="px-4 sm:px-6 lg:px-24 py-16 bg-[#FCFCFC]"
          ref={educationRef}
        >
          <div className="flex flex-col-reverse items-center justify-between gap-12 mx-auto md:flex-row max-w-9xl">
            <motion.div
              initial={{ opacity: 0, x: -40 }}
              animate={educationInView ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.8 }}
              className="w-full space-y-6 text-center md:w-1/2 md:text-left"
            >
              <h1 className="text-2xl md:text-3xl lg:text-4xl font-bold text-[#151517] leading-tight">
                Online Education Platform
              </h1>
              <p className="text-[15px] md:text-[19px] text-[#585c58] max-w-xl mx-auto md:mx-0">
                imranslab is an innovative online education platform offering
                skill-based learning, expert-led courses, and career-focused
                programs to empower learners worldwide.
              </p>
              <a
                href="https://education.imranslab.org/"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
              >
                More Details
              </a>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 40 }}
              animate={educationInView ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="flex justify-center w-full md:w-1/2 md:justify-start"
            >
              <img
                src="https://i.ibb.co.com/jkQq5tnz/Online-Education-Platform.jpg"
                alt="Online education presentation"
                className="w-[300px] sm:w-[400px] md:w-[500px] lg:w-[550px] rounded-lg hover:scale-105 transition-transform duration-300 ease-in-out shadow-md"
              />
            </motion.div>
          </div>
        </section>

        {/* projects Section */}
        <section className="py-10 bg-[#FCFCFC]" ref={sectionRef}>
          <div className="flex flex-col items-center justify-center w-full mb-6">
            {/* Badge */}
            <div className="flex mt-12 mb-4 justify-center gap-2 bg-[#F3E5C3] px-4 py-2 rounded-full transition-colors cursor-pointer group w-[60%] sm:w-[40%] lg:w-[20%]">
              <span className="text-sm text-[#174E4E] font-medium">
                Update Project
              </span>
            </div>

            {/* Header */}
            <div className="w-full py-2 mx-auto text-center">
              <h1 className="text-2xl font-bold text-black capitalize sm:text-3xl lg:text-4xl">
                Explore our Upcoming <br />
                <span className="text-[#B3225F]">projects</span>
              </h1>
            </div>

            {/* Project Cards Grid */}
            <div className="px-4 py-16 space-y-16 sm:px-6 lg:px-16">
              <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
                {homeprojects.map((project, index) => (
                  <motion.div
                    key={project.title}
                    className=""
                    initial="hidden"
                    animate={isInView ? "visible" : "hidden"}
                    custom={index}
                    variants={cardVariants}
                  >
                    {/* Image and Hover Overlay */}
                    <div className="relative overflow-hidden rounded-md shadow-lg group aspect-w-16 aspect-h-9">
                      <img
                        src={project.image || "/default-project.png"}
                        alt={project.alt || "Project Image"}
                        className="object-cover w-full h-full transition duration-300 rounded-md group-hover:brightness-50"
                      />

                      {/* Hover Text Overlay */}
                      <div className="absolute inset-0 flex flex-col items-center justify-center px-4 text-center transition-opacity duration-500 opacity-0 group-hover:opacity-100 bg-black/90 backdrop-blur-sm">
                        <h1 className="text-2xl sm:text-3xl font-semibold text-[#15919B]">
                          {project.title}
                        </h1>
                        <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                          {project.description}
                        </p>
                        <div className="mt-6">
                          <a
                            href={project.link}
                            target="_blank"
                            rel="noopener noreferrer"
                            aria-label={`View details about ${project.title}`}
                          >
                            <ButtonFill>Details</ButtonFill>
                          </a>
                        </div>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* faq section */}
        <Faq />

        {/* Newsletter Section */}
        <section
          ref={newsletterRef}
          className="container px-4 py-10 mx-auto sm:px-6 lg:px-8"
        >
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={isNewsletterInView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.8 }}
            className="relative overflow-hidden bg-blue-600 rounded-2xl"
          >
            <div className="absolute top-0 right-0 z-0 hidden w-1/2 h-full bg-blue-700 clip-path-slant md:block"></div>

            <div className="relative z-10 flex flex-col items-center justify-between gap-10 px-6 py-16 md:px-16 md:py-24 lg:flex-row md:gap-12">
              {/* Left Content */}
              <motion.div
                initial={{ opacity: 0, y: 40 }}
                animate={isNewsletterInView ? { opacity: 1, y: 0 } : {}}
                transition={{ duration: 0.8, delay: 0.2 }}
                className="max-w-xl text-center text-white md:text-left"
              >
                <h2 className="mb-4 text-2xl font-semibold sm:text-3xl md:text-4xl">
                  Subscribe to our newsletter
                </h2>
                <p className="text-sm text-blue-100 sm:text-base">
                  Best cooks and best delivery guys all at your service. Hot
                  tasty food delivered to you.
                </p>
              </motion.div>

              {/* Form */}
              <motion.div
                initial={{ opacity: 0, y: 40 }}
                animate={isNewsletterInView ? { opacity: 1, y: 0 } : {}}
                transition={{ duration: 0.8, delay: 0.4 }}
                className="w-full md:w-auto"
              >
                <form
                  onSubmit={onSubmit}
                  className="flex flex-col items-stretch gap-4 sm:flex-row sm:gap-0"
                >
                  <input
                    type="email"
                    name="email"
                    required
                    placeholder="Enter your email address"
                    className="w-full px-4 py-3 text-gray-900 placeholder-gray-500 bg-white sm:w-auto md:w-80 sm:px-6 sm:py-4 rounded-xl sm:rounded-l-xl sm:rounded-r-none focus:outline-none focus:ring-2 focus:ring-green-400"
                  />
                  <button
                    type="submit"
                    className="flex items-center justify-center w-full gap-2 px-6 py-3 text-white transition-colors bg-green-500 sm:w-auto hover:bg-green-600 sm:px-8 sm:py-4 rounded-xl sm:rounded-l-none sm:rounded-r-xl"
                  >
                    <span>Subscribe</span>
                    <HiArrowRight className="w-5 h-5" />
                  </button>
                </form>

                <AnimatePresence>
                  {submitted && (
                    <motion.p
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: 10 }}
                      transition={{ duration: 0.5 }}
                      className="mt-4 text-green-100"
                    >
                      ✅ Thank you for subscribing!
                    </motion.p>
                  )}
                </AnimatePresence>
              </motion.div>
            </div>
          </motion.div>

          {/* Custom Clip-path CSS */}
          <style>{`
          .clip-path-slant {
            clip-path: polygon(20% 0%, 100% 0%, 100% 100%, 0% 100%);
          }
        `}</style>
        </section>

        {/* ScrollToTopButton */}
        <ScrollToTopButton />
      </div>
    </>
  );
};

export default Home;
