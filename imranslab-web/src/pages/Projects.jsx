/** @format */

// import { Database, Headset, TimerIcon } from 'lucide-react';

import PageHeader from "../Helper/PageHeader";
import { useRef, useState } from "react";
import { motion, useInView } from "framer-motion";
import ScrollToTopButton from "../Helper/ScrollToTopButton";

const Projects = () => {
  // State for showing more or less projects
  const [showAllProjects, setShowAllProjects] = useState(false);

  // Benefit section ref
  const benefitRef = useRef(null);
  const isInView = useInView(benefitRef, { once: true, margin: "-100px" });

  // Animation variants
  const cardVariants = {
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

  const benefits = [
    {
      iconType: "image",
      icon: "https://i.ibb.co/C3yPFYXz/data.gif",
      title: "Increased Operational Efficiency",
      description:
        "Our software solutions optimize business operations by automating tasks, reducing manual work, and enhancing process efficiency. This leads to faster workflows, and significant time savings.",
    },
    {
      iconType: "image",
      icon: "https://i.ibb.co/5X2LLdF3/Data-Security.gif",
      title: "Data Security and Compliance",
      description:
        "Security is a core focus of our software development. We implement encryption, multi-factor authentication, and compliance with industry standards such as GDPR, HIPAA, and ISO.",
    },
    {
      iconType: "image",
      icon: "https://i.ibb.co/ycBzwvqV/time.gif",
      title: "Continuous Support and Upgrades",
      description:
        "Our team provides ongoing technical support, regular updates, and system enhancements to ensure your software remains up-to-date, secure, and fully functional in an ever-evolving tech landscape.",
    },
  ];

  // Project section ref
  const sectionRef = useRef(null);
  const isProjectInView = useInView(sectionRef, {
    once: true,
    margin: "-100px",
  });

  const projectCardVariants = {
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

  const project = [
    {
      title: "imranslab OCR Project",
      image: "https://i.ibb.co.com/rGPPdKfW/imranslab-OCR-Project.jpg",
      alt: "OCR Banner",
      description:
        "The OCR Pipeline System is a modular, scalable, and highly configurable framework for transforming scanned documents into structured, machine-readable text.",
      link: "/",
    },
    {
      title: "imranslab Education Website",
      image: "https://i.ibb.co.com/Z6TtkMpp/imranslab-Education.jpg",
      alt: "Education Website",
      description:
        "We value continuous learning, fostering growth, creativity, and skills development for a brighter future.",
      link: "https://education.imranslab.org/",
    },
    {
      title: "Clean Website",
      image: "https://i.ibb.co.com/3LmD6RZ/SR-Clean.jpg",
      alt: "Clean Website",
      description:
        "SR.Clean is a fast, affordable cleaning service for homes and offices. Flexible scheduling, trusted professionals.",
      link: "/srclean",
    },
    {
      title: "Softtech Website",
      image: "https://i.ibb.co.com/cSb3WytR/Soft-Tech-At-Soft-Tech.jpg",
      alt: "Softtech Website",
      description:
        "At SoftTech, we design and build innovative software solutions that empower businesses to grow, adapt, and succeed. From custom applications to enterprise systems, we deliver scalable, secure, and user-friendly technology tailored to your needs.",
      link: "https://soft-tech.imranslab.org/",
    },
  ];

  return (
    <>
      {/* Header section */}
      <PageHeader
        title="Our Projects"
        breadcrumb={[{ label: "Home", path: "/home" }, { label: "Projects" }]}
      />

      {/* Project Benefits Section */}
      <section className="py-12 bg-[#FCFCFC]" ref={benefitRef}>
        <div className="w-full px-5 mb-10 space-y-3 text-center md:px-16">
          <motion.h1
            className="text-xl md:text-3xl font-bold text-[#B3225F]"
            initial={{ opacity: 0, x: -50 }}
            animate={isInView ? { opacity: 1, x: 0 } : {}}
            exit={{ opacity: 0, x: 50 }}
            transition={{ duration: 0.6 }}
          >
            Project Benefits for a Software Company
          </motion.h1>
          <motion.p
            className="text-sm md:text-base w-full md:w-[70%] mx-auto text-[#585c58] font-medium"
            initial={{ opacity: 0, x: 50 }}
            animate={isInView ? { opacity: 1, x: 0 } : {}}
            exit={{ opacity: 0, x: -50 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            Investing in the right software solutions can transform business
            operations, drive efficiency, and foster innovation. Below are the
            key benefits of our services.
          </motion.p>
        </div>

        {/* Benefit Cards */}
        <div className="flex flex-col items-center justify-center gap-6 px-5 md:flex-row md:flex-wrap sm:px-10 lg:px-16">
          {benefits.map((benefit, idx) => (
            <motion.div
              key={idx}
              className="bg-[#c8edf3] w-full md:w-[48%] lg:w-[30%] rounded-lg shadow-lg px-6 py-6 transition-transform duration-300 ease-in-out hover:scale-105 cursor-pointer hover:border hover:border-[#9de5f1] "
              initial="hidden"
              animate={isInView ? "visible" : "hidden"}
              custom={idx}
              variants={cardVariants}
            >
              <div className="text-center">
                <span className="inline-block mb-4">
                  <img src={benefit.icon} alt="" className="w-12 h-12" />
                </span>
                <h2 className="text-lg md:text-[22px] font-bold text-[#15919B] hover:border-b hover:border-[#15919B] inline-block">
                  {benefit.title}
                </h2>
                <p className="text-sm text-[#151517] pt-3">
                  {benefit.description}
                </p>
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Project List Section */}
      <section className="bg-[#FCFCFC] pt-12" ref={sectionRef}>
        <div className="w-full py-2 mx-auto text-center">
          <motion.h1
            initial={{ opacity: 0, x: -50 }}
            animate={isProjectInView ? { opacity: 1, x: 0 } : {}}
            exit={{ opacity: 0, x: 50 }}
            transition={{ duration: 0.6 }}
            className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#B3225F] capitalize"
          >
            Explore Our Recent Projects
          </motion.h1>
        </div>

        {/* Project Cards */}
        <div className="px-4 py-16 space-y-16 sm:px-6 lg:px-16">
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-2">
            {project
              .slice(0, showAllProjects ? project.length : 4)
              .map((proj, index) => (
                <motion.div
                  key={proj.title}
                  className="rounded-md shadow-lg"
                  initial="hidden"
                  animate={isProjectInView ? "visible" : "hidden"}
                  custom={index}
                  variants={projectCardVariants}
                >
                  {/* Image and Hover Overlay */}
                  <div className="relative overflow-hidden rounded-md shadow-lg group aspect-w-16 aspect-h-9">
                    <img
                      src={proj.image || "/default-project.png"}
                      alt={proj.alt || "Project Image"}
                      className="object-cover w-full h-full transition duration-300 rounded-md group-hover:brightness-50"
                    />

                    {/* Hover Text Overlay */}
                    <div className="absolute inset-0 flex flex-col items-center justify-center px-4 text-center transition-opacity duration-500 opacity-0 group-hover:opacity-100 bg-black/90 backdrop-blur-sm">
                      <h1 className="text-lg sm:text-xl md:text-2xl font-semibold text-[#15919B]">
                        {proj.title}
                      </h1>
                      <p className="text-xs sm:text-sm md:text-base text-[#f3f3f3] mt-3">
                        {proj.description}
                      </p>
                      <div className="mt-4 sm:mt-6">
                        <a
                          href={proj.link}
                          rel="noopener noreferrer"
                          aria-label={`View details about ${proj.title}`}
                          className="inline-block px-4 py-2 text-xs text-white transition-all duration-300 bg-gray-900 rounded-md sm:px-6 sm:text-sm hover:bg-white hover:text-black"
                        >
                          More Details
                        </a>
                      </div>
                    </div>
                  </div>
                </motion.div>
              ))}
          </div>

          {/* Show More / Show Less Button */}
          <div className="mt-8 text-center">
            <button
              onClick={() => setShowAllProjects(!showAllProjects)}
              className={`px-6 py-2 text-white rounded-lg transition duration-300 ${
                showAllProjects
                  ? "bg-[#15919B] hover:bg-[#0d8b83]"
                  : "bg-[#9e1c4c] hover:bg-[#B3225F]"
              }`}
            >
              {showAllProjects ? "Show Less" : "Show More"}
            </button>
          </div>
        </div>
      </section>

      {/* Scroll to top */}
      <ScrollToTopButton />
    </>
  );
};

export default Projects;
