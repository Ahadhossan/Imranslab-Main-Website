/** @format */

import PageHeader from "../Helper/PageHeader";
import { useRef } from "react";
import { motion, useInView } from "framer-motion";
import ScrollToTopButton from "../Helper/ScrollToTopButton";
import ButtonFill from "../Button/ButtonFill";
import { interbenefits, InternTeam } from "../Data/intern";

const IntershipPage = () => {
  return (
    <>
      {/* Header Section */}
      <PageHeader title="Your Career" />

      {/* Search box */}
      <h1>Search box[Job Type, Location, etc.]</h1>
      <p>Example: Software Engineer, Data Scientist, etc.</p>

      {/* Job List section  */}
      <section className=" bg-[#FCFCFC]" ref={internRef}>
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <div className="bg-[#F3E5C3] w-full p-6 rounded-lg shadow-lg transition-all duration-300 ease-in-out transform hover:scale-105 hover:shadow-2xl hover:border hover:border-[#9de5f1] cursor-pointer group">
            <h3 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
              Software Engineer
            </h3>
            <p>Location: Dhaka, Bangladesh</p>
            <p>Salary: 100,000 - 150,000 BDT</p>
            <p>Experience: 2-5 years</p>
            <p>Job Type: Full-time</p>
            <p>
              Job Description: We are looking for a Software Engineer with 2-5
              years of experience in software development. The ideal candidate
              will have a strong understanding of software development
              principles and a passion for building high-quality software.
            </p>
            <p>
              Requirements: Bachelor's degree in Computer Science or a related
              field. 2-5 years of experience in software development. Strong
              understanding of software development principles. Passion for
              building high-quality software.
            </p>
          </div>
          <div className="bg-[#F3E5C3] w-full p-6 rounded-lg shadow-lg transition-all duration-300 ease-in-out transform hover:scale-105 hover:shadow-2xl hover:border hover:border-[#9de5f1] cursor-pointer group">
            <h3 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
              Software Engineer
            </h3>
            <p>Location: Dhaka, Bangladesh</p>
            <p>Salary: 100,000 - 150,000 BDT</p>
            <p>Experience: 2-5 years</p>
            <p>Job Type: Full-time</p>
            <p>
              Job Description: We are looking for a Software Engineer with 2-5
              years of experience in software development. The ideal candidate
              will have a strong understanding of software development
              principles and a passion for building high-quality software.
            </p>
            <p>
              Requirements: Bachelor's degree in Computer Science or a related
              field. 2-5 years of experience in software development. Strong
              understanding of software development principles. Passion for
              building high-quality software.
            </p>
          </div>
        </div>
      </section>

      <ScrollToTopButton />
    </>
  );
};

export default IntershipPage;
