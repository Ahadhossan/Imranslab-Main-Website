/** @format */

import { motion, useInView } from "framer-motion";
import PageHeader from "../Helper/PageHeader";
import { useRef } from "react";
import Testimonials from "../Helper/About/Testimonials";

const About = () => {
  // about section
  const aboutRef = useRef(null);
  const aboutInView = useInView(aboutRef, { once: true, margin: "-100px" });
  // Other section
  const otherRef = useRef(null);
  const otherInView = useInView(otherRef, { once: true, margin: "-100px" });

  // vision
  const visionRef = useRef(null);
  const visionInView = useInView(visionRef, { once: true, margin: "-100px" });

  // testimonial section
  const testimonialRef = useRef(null);
  const isTestimonialInView = useInView(testimonialRef, {
    once: true,
    margin: "-100px",
  });

  // mission
  const missionRef = useRef(null);
  const missionInView = useInView(missionRef, { once: true, margin: "-100px" });

  // core section
  const coreRef = useRef(null);
  const coreInView = useInView(coreRef, { once: true, margin: "-100px" });

  // Culture
  const cultureRef = useRef(null);
  const cultureInView = useInView(cultureRef, { once: true, margin: "-100px" });

  // Global
  const globalRef = useRef(null);
  const globalInView = useInView(globalRef, { once: true, margin: "-100px" });

  // How We Grow Together
  const growRef = useRef(null);
  const growInView = useInView(growRef, { once: true, margin: "-100px" });

  //The Road Ahead
  const roadRef = useRef(null);
  const roadInView = useInView(roadRef, { once: true, margin: "-100px" });

  // cta
  const ctaRef = useRef(null);
  const ctaInView = useInView(ctaRef, { once: true, margin: "-100px" });

  return (
    <>
      {/* header section */}
      <PageHeader
        title="About Us"
        breadcrumb={[{ label: "Home", path: "/home" }, { label: "About" }]}
      />

      {/* Who We Are Section */}
      <section ref={aboutRef} className="bg-[#FCFCFC] py-10 sm:py-12 lg:py-16">
        {/* About info */}
        <div className="flex flex-col items-center justify-between px-6 mx-auto sm:px-8 lg:px-16 md:flex-row">
          {/* Left Column */}
          <div className="w-full space-y-8 md:w-1/2">
            <motion.h1
              initial={{ opacity: 0, x: -50 }}
              animate={aboutInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 1.2 }}
              className="text-2xl sm:text-3xl lg:text-4xl text-[#B3225F] font-bold leading-tight"
            >
              Who We Are
            </motion.h1>

            <motion.p
              initial={{ opacity: 0, x: 50 }}
              animate={aboutInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 1.2, delay: 0.6 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px]"
            >
              At <strong className="text-[#151517] font-bold">imranslab</strong>
              , we are more than just a software company—we’re a{" "}
              <strong className="text-[#151517] font-bold">
                global catalyst for innovation
              </strong>
              . From our headquarters in{" "}
              <strong className="text-[#151517] font-bold">Montreal</strong>,
              Canada, and a strong presence in{" "}
              <strong className="text-[#151517] font-bold">Dhaka</strong>,
              Bangladesh, we deliver
              <strong className="text-[#151517] font-bold">
                {" "}
                scalable
              </strong>,{" "}
              <strong className="text-[#151517] font-bold">accessible</strong>,
              and{" "}
              <strong className="text-[#151517] font-bold">
                purpose-driven solutions
              </strong>{" "}
              to help businesses and individuals achieve their goals.
            </motion.p>

            <motion.p
              initial={{ opacity: 0, x: 50 }}
              animate={aboutInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 1.2, delay: 0.8 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px]"
            >
              We believe that{" "}
              <strong className="text-[#151517] font-bold">
                technology can change the world
              </strong>
              , and we’re on a mission to make that vision a reality, with every
              product we build and every client we support. Our team is united
              by a shared purpose: to{" "}
              <strong className="text-[#151517] font-bold">
                empower individuals
              </strong>{" "}
              and{" "}
              <strong className="text-[#151517] font-bold">
                transform industries
              </strong>{" "}
              through the power of technology.
            </motion.p>
          </div>

          {/* Right Column - Images */}
          <div className="w-full mt-8 md:w-1/2 md:pl-12 md:mt-0">
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={aboutInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1.2 }}
              className="relative flex justify-center"
            >
              <img
                src="https://i.ibb.co/wjNp3p1/imranslab.png"
                alt="Team meeting"
                className="w-[400px] sm:w-[500px] lg:w-[600px] rounded-lg z-10 hover:scale-105 transition-transform duration-300"
              />
            </motion.div>
          </div>
        </div>
      </section>

      {/*  Other sidle */}
      <section className="p-12 bg-[#FCFCFC]" ref={otherRef}>
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {/* Card 1 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 0.6 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <div className="inline-block mb-4">
                <img
                  src="https://i.ibb.co/Kj77dZTb/project.gif"
                  alt=""
                  className="w-12 h-12"
                />
              </div>
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                05+
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                Projects completed
              </p>
            </motion.div>

            {/* Card 2 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 0.8 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <div className="inline-block mb-4">
                <img
                  src="https://i.ibb.co/mC2Rdqrz/like.gif"
                  alt=""
                  className="w-12 h-12"
                />
              </div>
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                20k+
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                Pepole Trust Us
              </p>
            </motion.div>

            {/* Card 3 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <div className="inline-block mb-4">
                <img
                  src="https://i.ibb.co/Ps51d0hM/checkbox.gif"
                  alt=""
                  className="w-12 h-12"
                />
              </div>
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                95%
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                Results Guaranteed
              </p>
            </motion.div>

            {/* Card 4 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1.2 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <div className="inline-block mb-4">
                <img
                  src="https://i.ibb.co/JMR4Fpw/files.gif"
                  alt=""
                  className="w-12 h-12"
                />
              </div>
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                03+
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                Upcoming Project
              </p>
            </motion.div>
          </div>
        </div>
      </section>

      {/* mission*/}
      <section
        ref={missionRef}
        className="px-4 py-10 sm:px-6 lg:px-16 bg-[#FCFCFC]"
      >
        <div className="flex flex-col items-center gap-12 mx-auto max-w-9xl md:flex-row">
          {/* Left Column - Image */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={missionInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 1.2 }}
            className="flex justify-center w-full md:w-1/2 md:justify-start"
          >
            <img
              src="https://i.ibb.co.com/0yhXhQTd/Our-Mission.jpg"
              alt="Team meeting"
              className="w-[350px] sm:w-[450px] lg:w-[550px] rounded-lg hover:scale-105 transition-transform duration-300 shadow-md"
            />
          </motion.div>

          {/* Right Column - Content */}
          <div className="w-full space-y-6 text-start md:w-1/2 md:text-left">
            <motion.h3
              initial={{ opacity: 0, x: 50 }}
              animate={missionInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.9 }}
            >
              <span className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#B3225F]">
                Our Mission
              </span>
            </motion.h3>
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={missionInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.9, delay: 0.6 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px] mx-auto md:mx-0 text-start"
            >
              To empower individuals and businesses with innovative, efficient,
              and accessible technology solutions—driving progress and enhancing
              lives around the world. Our mission is what drives us every day.{" "}
              <strong className="text-[#151517] font-bold">imranslab</strong>{" "}
              isn’t just about writing code or creating digital products—it’s
              about making a{" "}
              <strong className="text-[#151517] font-bold">real impact</strong>.
              We focus on delivering{" "}
              <strong className="text-[#151517] font-bold">
                tailored solutions
              </strong>{" "}
              that meet the{" "}
              <strong className="text-[#151517] font-bold">unique needs</strong>{" "}
              of our clients, from{" "}
              <strong className="text-[#151517] font-bold">
                AI-powered systems
              </strong>{" "}
              to{" "}
              <strong className="text-[#151517] font-bold">
                cloud-based innovations
              </strong>
              . Everything we do is fueled by our commitment to technology as a
              force for good. We are here to empower, educate, and create
              solutions that{" "}
              <strong className="text-[#151517] font-bold">change lives</strong>{" "}
              for the better.
            </motion.p>
            <a
              href="https://imranslab.atlassian.net/wiki/x/uADbKg"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
            >
              More Details
            </a>
          </div>
        </div>
      </section>

      <div className="w-[90%] mx-auto border-b border-black my-6"></div>

      {/* vision*/}
      <section
        className="px-4 py-10 sm:px-6 lg:px-16 bg-[#FCFCFC]"
        ref={visionRef}
      >
        <div className="flex flex-col items-center gap-12 mx-auto max-w-7xl md:flex-row">
          {/* left Column - Content */}
          <div className="w-full space-y-6 md:w-1/2 md:text-left text-start">
            <motion.h3
              initial={{ opacity: 0, x: 50 }}
              animate={visionInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.9 }}
            >
              <span className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#B3225F]">
                Our vision
              </span>
            </motion.h3>
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={missionInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.9, delay: 0.6 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px] mx-auto"
            >
              To become a global catalyst for innovation—designing accessible,
              scalable, and purpose-driven technology that transforms
              industries, empowers individuals, and shapes a better future. Our
              vision is{" "}
              <strong className="text-[#151517] font-bold">
                future-focused
              </strong>
              , <strong className="text-[#151517] font-bold">ambitious</strong>,
              and{" "}
              <strong className="text-[#151517] font-bold">
                transformative
              </strong>
              . As a company, we are not just building for today—we are
              preparing for the future. We aim to be a leader in the{" "}
              <strong className="text-[#151517] font-bold">
                global tech landscape
              </strong>
              , providing solutions that are{" "}
              <strong className="text-[#151517] font-bold">accessible</strong>{" "}
              to all, scalable to grow with industries, and purpose-driven to
              ensure a better future for all of humanity. We believe that{" "}
              <strong className="text-[#151517] font-bold">innovation</strong>{" "}
              should not only{" "}
              <strong className="text-[#151517] font-bold">
                solve problems
              </strong>{" "}
              but should{" "}
              <strong className="text-[#151517] font-bold">
                reshape the world for the better
              </strong>
              , making it more{" "}
              <strong className="text-[#151517] font-bold">
                inclusive, efficient
              </strong>
              , and{" "}
              <strong className="text-[#151517] font-bold">sustainable</strong>.
            </motion.p>
            <a
              href="https://imranslab.atlassian.net/wiki/x/uADbKg"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
            >
              More Details
            </a>
          </div>

          {/* right Column - Image */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={visionInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 1.2 }}
            className="flex justify-center w-full md:w-1/2 md:justify-start"
          >
            <img
              src="https://i.ibb.co.com/XZHhHgY4/Our-vision.jpg"
              alt="Team meeting"
              className="w-[400px] md:w-[500px] lg:w-[550px] rounded-lg hover:scale-105 transition-transform duration-300 shadow-md"
            />
          </motion.div>
        </div>
      </section>

      <div className="w-[90%] mx-auto border-b border-black my-6"></div>

      {/*  Core Value */}
      <section className="p-6 bg-[#FCFCFC]" ref={coreRef}>
        <div className="px-4 mx-auto max-w-9xl sm:px-6 lg:px-8">
          {/* header content */}
          <div className="px-4 text-center sm:px-6 md:px-8 lg:px-16">
            <motion.h2
              initial={{ opacity: 0, x: 50 }}
              animate={coreInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.6 }}
              className="text-[25px] md:text-[30px] lg:text-[35px] text-[#B3225F] font-bold"
            >
              Core Values
            </motion.h2>
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={coreInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.6 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px] p-6 mx-auto max-w-5xl md:max-w-3xl"
            >
              At <strong className="text-[#151517] font-bold">imranslab</strong>
              , our{" "}
              <strong className="text-[#151517] font-bold">core values</strong>{" "}
              shape everything we do. They guide our{" "}
              <strong className="text-[#151517] font-bold">decisions</strong>,{" "}
              <strong className="text-[#151517] font-bold">actions</strong>, and{" "}
              <strong className="text-[#151517] font-bold">
                relationships
              </strong>{" "}
              with our clients, teams, and partners. These values are at the
              heart of our{" "}
              <strong className="text-[#151517] font-bold">
                company culture
              </strong>{" "}
              and are the key to our continued success.
            </motion.p>
          </div>

          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {/* Card 1 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={coreInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 0.6 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Purpose Over Hype
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                We solve real problems that matter. We don’t follow trends—we
                set standards.
              </p>
            </motion.div>

            {/* Card 2 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 0.8 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Build with Clarity
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                We believe in transparency and clear communication. Every
                product we design, every code we commit, reflects clarity of
                purpose.
              </p>
            </motion.div>

            {/* Card 3 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Learn Relentlessly
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                Every project is an opportunity to grow and level up. We
                encourage constant learning and self-improvement.
              </p>
            </motion.div>

            {/* Card 4 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1.2 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Own What You Build
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                We take full responsibility for every product and project we
                deliver, from design to deployment and beyond.
              </p>
            </motion.div>

            {/* Card 5 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1.4 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Challenge with Curiosity
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                We question assumptions, explore new ideas, and challenge the
                status quo. Innovation comes from curiosity.
              </p>
            </motion.div>

            {/* Card 6 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1.6 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Move with Urgency
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                We prioritize momentum over perfection. Progress is what drives
                us.
              </p>
            </motion.div>

            {/* Card 7 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 1.8 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Design for Everyone
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                Technology should be inclusive, designed with empathy and equity
                in mind.
              </p>
            </motion.div>

            {/* Card 8 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 2 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Embrace Diverse Thinking
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                We value diversity in all forms—different perspectives create
                better ideas.
              </p>
            </motion.div>

            {/* Card 9 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              animate={otherInView ? { opacity: 1, y: 0 } : {}}
              exit={{ opacity: 0, y: -50 }}
              transition={{ duration: 2.2 }}
              className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]"
            >
              <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                Work with Empathy
              </h1>
              <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                We treat each other with respect and kindness. Every decision
                and action is rooted in empathy for our team, clients, and the
                communities we serve.
              </p>
            </motion.div>
          </div>
        </div>
      </section>

      <div className="w-[90%] mx-auto border-b border-black my-6"></div>

      {/*  Our Culture */}
      <section className="p-6 bg-[#FCFCFC]" ref={cultureRef}>
        <div className="px-4 mx-auto max-w-9xl sm:px-6 lg:px-8">
          {/* header content */}
          <div className="px-4 text-start md:text-center sm:px-6 md:px-8 lg:px-16">
            <motion.h2
              initial={{ opacity: 0, x: 50 }}
              animate={cultureInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.6 }}
              className="text-[25px] md:text-[30px] lg:text-[35px] text-[#B3225F] font-bold"
            >
              Our Culture
            </motion.h2>
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={coreInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px] py-4 mx-auto max-w-5xl md:max-w-3xl"
            >
              At <strong className="text-[#151517] font-bold">imranslab</strong>
              , our culture is at the core of everything we do. We don’t just
              work hard—we work smart. Every team member is encouraged to take{" "}
              <strong className="text-[#151517] font-bold">ownership</strong> of
              their work and contribute to the{" "}
              <strong className="text-[#151517] font-bold">
                company’s growth
              </strong>
              . We foster a{" "}
              <strong className="text-[#151517] font-bold">
                high-performance culture
              </strong>{" "}
              where innovation is expected, speed is respected, and
              collaboration is at the heart of everything we build. Our team
              members are encouraged to be{" "}
              <strong className="text-[#151517] font-bold">curious</strong>,{" "}
              <strong className="text-[#151517] font-bold">innovative</strong>,
              and{" "}
              <strong className="text-[#151517] font-bold">accountable</strong>.
              We embrace{" "}
              <strong className="text-[#151517] font-bold">diversity</strong>{" "}
              and value the different perspectives each individual brings. We
              believe in{" "}
              <strong className="text-[#151517] font-bold">
                continuous learning
              </strong>{" "}
              and{" "}
              <strong className="text-[#151517] font-bold">
                self-improvement
              </strong>
              , encouraging team members to grow alongside the company.{" "}
              <strong className="text-[#151517] font-bold">
                Collaboration
              </strong>{" "}
              and <strong className="text-[#151517] font-bold">feedback</strong>{" "}
              are at the core of how we work—every idea, feature, and project
              benefits from the collective input of our diverse team.
            </motion.p>
            <a
              href="https://imranslab.atlassian.net/wiki/x/uADbKg"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
            >
              More Details
            </a>
          </div>
        </div>
      </section>

      <div className="w-[90%] mx-auto border-b border-black my-6"></div>

      {/* Global Presence*/}
      <section
        className="px-4 py-10 bg-[#FCFCFC] sm:px-6 lg:px-16"
        ref={globalRef}
      >
        <div className="flex flex-col items-center gap-12 mx-auto max-w-9xl md:flex-row">
          {/* Left Column - Text Content & Cards */}
          <div className="w-full space-y-6 md:w-1/2 md:text-left text-start">
            <motion.h1
              initial={{ opacity: 0, x: 50 }}
              animate={globalInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.8 }}
              className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#B3225F]"
            >
              Global Presence
            </motion.h1>
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={globalInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px] mx-auto"
            >
              Our vision has no boundaries. We are proud to have a{" "}
              <strong className="text-[#151517] font-bold">
                global footprint
              </strong>
              , serving clients and building solutions across continents. With
              offices in{" "}
              <strong className="text-[#151517] font-bold">Montreal</strong>,{" "}
              <strong className="text-[#151517] font-bold">Dhaka</strong>,{" "}
              <strong className="text-[#151517] font-bold">Sharjah</strong>,{" "}
              <strong className="text-[#151517] font-bold">London</strong>,{" "}
              <strong className="text-[#151517] font-bold">Lahore</strong>,{" "}
              <strong className="text-[#151517] font-bold">Sengal</strong>,{" "}
              <strong className="text-[#151517] font-bold">Sweden</strong>,{" "}
              <strong className="text-[#151517] font-bold">New York</strong>,{" "}
              <strong className="text-[#151517] font-bold">Morocco</strong>,{" "}
              <strong className="text-[#151517] font-bold">San Diego</strong>,
              and <strong className="text-[#151517] font-bold">Oshawa</strong>
              —we are positioned to deliver results wherever our clients need
              us. Our{" "}
              <strong className="text-[#151517] font-bold">
                global presence
              </strong>{" "}
              ensures that we can offer support and solutions across time zones,
              bringing diverse perspectives and expertise to every project.
            </motion.p>
          </div>

          {/* Right Column - Image */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={globalInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 1.2 }}
            className="flex justify-center w-full md:w-1/2 md:justify-start"
          >
            <img
              src="https://i.ibb.co.com/670KLDJT/Global-Presence.jpg"
              alt="Team meeting"
              className="w-[400px] md:w-[500px] lg:w-[550px] rounded-lg hover:scale-105 transition-transform duration-300 shadow-md"
            />
          </motion.div>
        </div>
      </section>

      <div className="w-[90%] mx-auto border-b border-black my-6"></div>

      {/* How We Grow Together*/}
      <section className="p-10 bg-[#FCFCFC]" ref={growRef}>
        <div className="px-4 mx-auto max-w-9xl sm:px-6 lg:px-8">
          {/* header content */}
          <div className="px-4 text-center sm:px-8 md:px-12">
            <motion.h2
              initial={{ opacity: 0, x: 50 }}
              animate={growInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.6 }}
              className="text-[25px] md:text-[30px] lg:text-[35px] text-[#B3225F] font-bold"
            >
              How We Grow Together
            </motion.h2>
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={growInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px] py-4 mx-auto max-w-5xl md:max-w-3xl"
            >
              At <strong className="text-[#151517] font-bold">imranslab</strong>
              , growth is a shared effort. We are committed to supporting each
              other, challenging assumptions, and{" "}
              <strong className="text-[#151517] font-bold">empowering</strong>{" "}
              our team members to reach their full potential.{" "}
              <strong className="text-[#151517] font-bold">Innovation</strong>{" "}
              comes from collaboration, and{" "}
              <strong className="text-[#151517] font-bold">curiosity</strong>{" "}
              drives our exploration. We{" "}
              <strong className="text-[#151517] font-bold">learn</strong> from
              every project,{" "}
              <strong className="text-[#151517] font-bold">adapt</strong> to new
              challenges, and{" "}
              <strong className="text-[#151517] font-bold">scale</strong> as
              individuals and as a company.
            </motion.p>
          </div>
        </div>
      </section>

      <div className="w-[90%] mx-auto border-b border-black my-6"></div>

      {/* The Road Ahead */}
      <section
        className="px-4 py-10 bg-[#FCFCFC] sm:px-6 lg:px-16"
        ref={roadRef}
      >
        <div className="flex flex-col items-center gap-12 mx-auto max-w-9xl md:flex-row">
          {/* left Column - Image */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={roadInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 1.2 }}
            className="flex justify-center w-full md:w-1/2 md:justify-start"
          >
            <img
              src="https://i.ibb.co/YsHGTBh/Roadmap.png"
              alt="Team meeting"
              className="w-[400px] md:w-[500px] lg:w-[550px] rounded-lg hover:scale-105 transition-transform duration-300 shadow-md"
            />
          </motion.div>

          {/* right Column - Text Content & Cards */}
          <div className="w-full space-y-6 text-start md:w-1/2 md:text-left">
            <motion.h1
              initial={{ opacity: 0, x: 50 }}
              animate={roadInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.8 }}
              className="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#B3225F]"
            >
              The Road Ahead
            </motion.h1>
            <motion.p
              initial={{ opacity: 0, x: -50 }}
              animate={roadInView ? { opacity: 1, x: 0 } : {}}
              exit={{ opacity: 0, x: 50 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="text-[#363a36] text-[15px] sm:text-[17px] lg:text-[19px] mx-auto"
            >
              We’re just getting started, but every step we take brings us
              closer to realizing our{" "}
              <strong className="text-[#151517] font-bold">vision.</strong> As
              we grow, our focus remains clear—to build innovative, scalable
              solutions that have a{" "}
              <strong className="text-[#151517] font-bold">
                lasting impact
              </strong>{" "}
              on industries and communities around the world. We will continue
              to{" "}
              <strong className="text-[#151517] font-bold">
                push the boundaries of technology
              </strong>
              , develop{" "}
              <strong className="text-[#151517] font-bold">
                new solutions
              </strong>{" "}
              and expand our presence globally all while maintaining our
              commitment to{" "}
              <strong className="text-[#151517] font-bold">ethics</strong>,{" "}
              <strong className="text-[#151517] font-bold">purpose</strong>, and{" "}
              <strong className="text-[#151517] font-bold">inclusivity.</strong>
            </motion.p>
          </div>
        </div>
      </section>

      <div className="w-[90%] mx-auto border-b border-black my-6"></div>

      {/* Testimonials */}
      <section className="bg-[#FCFCFC]" ref={testimonialRef}>
        <motion.div
          initial={{ opacity: 0, x: 50 }}
          animate={isTestimonialInView ? { opacity: 1, x: 0 } : {}}
          transition={{ duration: 0.8 }}
          className="w-full px-4 mx-auto max-w-7xl sm:px-6 lg:px-8"
        >
          <Testimonials />
        </motion.div>
      </section>

      {/* Cta section */}
      <section
        ref={ctaRef}
        className="container px-6 py-12 mx-auto mb-4 shadow-2xl sm:px-8 lg:px-16 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 rounded-xl"
      >
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          animate={ctaInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.8 }}
          className="relative z-10 text-white"
        >
          {/* Content Wrapper */}
          <div className="flex flex-col items-center justify-between gap-10 px-6 py-8 shadow-lg md:flex-row md:gap-16 rounded-xl">
            {/* Left Content */}
            <motion.div
              initial={{ opacity: 0, y: 40 }}
              animate={ctaInView ? { opacity: 1, y: 0 } : {}}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="max-w-lg text-center md:text-left"
            >
              <h2 className="mb-4 text-3xl font-bold sm:text-4xl text-shadow-lg">
                Ready to make an impact?
              </h2>
              <p className="mb-6 text-lg leading-relaxed text-gray-100 sm:text-xl">
                Whether you are interested in our services, looking for
                collaboration, or want to join our innovative team, we’re here
                to help.
              </p>
            </motion.div>

            {/* Buttons Section */}
            <div className="flex flex-col justify-center gap-6 sm:flex-row sm:gap-8">
              <a
                href="/services"
                className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
              >
                Explore Our Services
              </a>
              <a
                href="https://forms.gle/ACuiKs8wb4buHiyt8"
                target="_blank"
                className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
              >
                Join Us
              </a>
              <a
                href="/contact"
                className="inline-block px-6 py-2 text-sm text-white transition-all duration-300 bg-gray-900 rounded-md sm:px-4 sm:py-3 sm:text-base hover:bg-black"
              >
                Contact Us
              </a>
            </div>
          </div>
        </motion.div>

        {/* Custom Clip-path CSS */}
        <style>{`
        .clip-path-slant {
          clip-path: polygon(20% 0%, 100% 0%, 100% 100%, 0% 100%);
        }
      `}</style>
      </section>
    </>
  );
};

export default About;
