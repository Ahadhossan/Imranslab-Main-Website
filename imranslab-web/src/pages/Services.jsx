/** @format */
import { Link } from "react-router-dom";
import PageHeader from "../Helper/PageHeader";
import { motion, useInView } from "framer-motion";
import { useRef, useState } from "react";
import ButtonFill from "../Button/ButtonFill";
import { services } from "../Data/services";

// ============== Start ServiceCard============
// Animation variants for service cards
const servicebenefitcardVariants = {
  hidden: { opacity: 0, y: 40 },
  visible: (custom) => ({
    opacity: 1,
    y: 0,
    transition: {
      delay: custom * 0.2,
      duration: 0.6,
      ease: "easeOut",
    },
  }),
};

// ServiceCard Component
const ServiceCard = ({ title, description, idx }) => {
  const ref = useRef(null);
  const inView = useInView(ref, { once: true, margin: "-100px" });

  return (
    <motion.div
      ref={ref}
      initial="hidden"
      animate={inView ? "visible" : "hidden"}
      custom={idx}
      variants={servicebenefitcardVariants}
      className="bg-[#c8edf3] w-full px-4 py-6 rounded-lg shadow-lg  hover:border hover:border-[#9de5f1]"
    >
      <div className="text-center">
        <h1 className="text-lg md:text-[22px] font-bold text-[#15919B] inline-block mt-3">
          {title}
        </h1>
        <p className="text-sm text-[#151517] pt-3">{description}</p>
      </div>
    </motion.div>
  );
};
// ============== end ServiceCard============

const Services = () => {
  // State for showing more or less projects
  const [showAllServices, setShowAllServices] = useState(false);

  // service Benifits section ref
  const servicebenefitRef = useRef(null);
  const servieisInView = useInView(servicebenefitRef, {
    once: true,
    margin: "-100px",
  });

  // service list
  const servicelistRef = useRef(null);
  const servielistisInView = useInView(servicelistRef, {
    once: true,
    margin: "-100px",
  });

  // Animation variants for service cards
  const servicelistcardVariants = {
    hidden: { opacity: 0, y: 40 },
    visible: (custom) => ({
      opacity: 1,
      y: 0,
      transition: {
        delay: custom * 0.2,
        duration: 0.6,
        ease: "easeOut",
      },
    }),
  };

  return (
    <>
      {/* header section */}
      <PageHeader
        title="Services"
        breadcrumb={[{ label: "Home", path: "/home" }, { label: "Services" }]}
      />

      {/* service  Benifits */}
      <section className="py-12 bg-[#FCFCFC]" ref={servicebenefitRef}>
        {/* Header */}
        <div className="flex flex-col w-full gap-3 px-5 mb-10 text-center md:px-16 md:gap-1">
          <motion.h1
            initial={{ opacity: 0, x: -50 }}
            animate={servieisInView ? { opacity: 1, x: 0 } : {}}
            exit={{ opacity: 0, x: 50 }}
            transition={{ duration: 0.6 }}
            className="md:text-3xl text-xl font-bold text-[#B3225F]"
          >
            Our Services
          </motion.h1>
          <div className="h-0.5 bg-blue-500 w-14 mx-auto"></div>
        </div>

        {/* Service Cards Grid */}
        <div className="grid items-center justify-between grid-cols-1 gap-5 px-12 pb-16 mx-auto md:grid-cols-2 lg:grid-cols-3 sm:px-16 lg:px-14">
          <div className="space-y-6">
            <ServiceCard
              title="Utility Management Software"
              description="At imranslab, we specialize in building intelligent, scalable, and future-ready Utility Management Software that streamlines operations, enhances efficiency, and provides actionable insights for your utility business."
              idx={0}
            />
          </div>
          <div className="space-y-6">
            <ServiceCard
              title="Custom Software Development"
              description="We build powerful, user-friendly, and scalable custom software tailored specifically to your business processes. From web apps to enterprise-grade platforms, we bring your ideas to life with quality code and modern architecture."
              idx={1}
            />
          </div>
          <div className="space-y-6">
            <ServiceCard
              title="Collaboration Opportunities"
              description="We welcome partnerships in research, software development, and AI-driven solutions. If you are interested in contributing to open-source projects or exploring innovative technologies, contact us to discuss possibilities."
              idx={2}
            />
          </div>
        </div>
      </section>

      {/* services list */}
      <section
        className="px-4 py-12 bg-[#FCFCFC] sm:px-6 lg:px-10"
        ref={servicelistRef}
      >
        <div className="mx-auto max-w-7xl">
          {/* Header */}
          <div className="px-4 mb-12 text-center sm:px-8">
            <motion.h1
              initial={{ opacity: 0, x: 50 }}
              animate={servielistisInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.6 }}
              className="text-2xl sm:text-3xl md:text-4xl font-bold text-[#B3225F]"
            >
              Choose Your Services
            </motion.h1>
            <div className="h-0.5 bg-[#15919B] w-14 mx-auto mt-2"></div>
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={servielistisInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.8 }}
              className="text-base sm:text-lg text-[#585c58] mt-4"
            >
              Explore our range of specialized services <br /> designed to meet
              your specific business needs.
            </motion.p>
          </div>

          {/* Services Grid */}
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {services
              .slice(0, showAllServices ? services.length : 6)
              .map((service, idx) => (
                <motion.div
                  key={service.id}
                  initial="hidden"
                  animate={useInView ? "visible" : "hidden"}
                  custom={idx}
                  variants={servicelistcardVariants}
                  className="p-6 transition-all duration-300 bg-[#c2dddf] rounded-lg shadow-lg hover:shadow-2xl"
                >
                  {/* Title & Icon */}
                  <div className="flex items-center mb-4">
                    <h3 className="text-[20px] sm:text-[23px] font-bold text-black  hover:text-[#15919B] cursor-pointer">
                      {service.title}
                    </h3>
                  </div>

                  {/* Description */}
                  <p className="mb-4 text-sm text-gray-700 sm:text-base">
                    {service.description}
                  </p>

                  {/* Feature Sections */}
                  <div className="mb-6 space-y-4 text-sm sm:text-base">
                    {/* Key Features */}
                    <div>
                      <h4 className="font-semibold text-[#15919B] mb-2">
                        Key Features
                      </h4>
                      <ul className="text-[#585c58] list-disc list-inside">
                        {service.features.map((feature, index) => (
                          <li key={index}>{feature}</li>
                        ))}
                      </ul>
                    </div>
                  </div>

                  {/* CTA Button */}
                  <Link to={service.page}>
                    <ButtonFill>Learn More</ButtonFill>
                  </Link>
                </motion.div>
              ))}
          </div>

          {/* Show More / Show Less Button */}
          <div className="mt-8 text-center">
            <button
              onClick={() => setShowAllServices(!showAllServices)}
              className={`px-6 py-2 text-white rounded-lg transition duration-300 ${
                showAllServices
                  ? "bg-[#15919B] hover:bg-[#0d8b83]"
                  : "bg-[#9e1c4c] hover:bg-[#B3225F]"
              }`}
            >
              {showAllServices ? "Show Less" : "Show More"}
            </button>
          </div>
        </div>
      </section>
    </>
  );
};

export default Services;
