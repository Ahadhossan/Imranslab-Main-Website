/** @format */

import PageHeader from "../../PageHeader";
import OcrTestimonials from "./OcrTestimonials";

const Ocr = () => {
  return (
    <>
      {/* Header Section */}
      <PageHeader
        title="OCR Project"
        breadcrumb={[
          { label: "Home", path: "/home" },
          { label: "Projects", path: "/projects" },
          { label: "OCR" },
        ]}
      />

      {/* main content */}
      <section className="p-6">
        {/* First Top */}
        <div className="py-2">
          <div>
            <img
              src="https://i.ibb.co/jkD5QV5B/Ocr.png"
              alt="ocr"
              className="object-cover transition duration-300 rounded-lg shadow-2xl group-hover:brightness-50"
            />
          </div>
        </div>

        {/* update date*/}
        <div className="text-[#151517] text-[15px] md:text-[17px] lg:text-[19px] font-semibold">
          <h2>
            <strong className="text-[#15918B] font-bold">Date:</strong> 02/07/25
          </h2>
          <span>
            <strong className="text-[#15918B] font-bold">Published:</strong> by
            imranslab
          </span>
        </div>

        {/*OCR Project: Empowering Data, Empowering Talent */}
        <div className="mt-10">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            OCR Project: Empowering Data, Empowering Talent
          </h2>
          {/* 1. Solving the Real-World Challenge */}
          <div>
            <span className="py-2 text-[17px] md:text-[19px] lg:text-[21px] text-[#15919B]">
              1. Solving the Real-World Challenge
            </span>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              Most real-world documents—from books to publications—aren’t stored
              in machine-readable formats, making it tough for organizations to
              leverage their data for AI and automation. High costs and
              inflexible commercial OCR tools hold many teams back. Our OCR
              project was created to bridge this gap with an efficient,
              cost-effective, and adaptable solution.
            </p>
          </div>
          {/* 2. What Makes Our Approach Different */}
          <div>
            <span className="py-2 text-[17px] md:text-[19px] lg:text-[21px] text-[#15919B]">
              2. What Makes Our Approach Different
            </span>
            <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              We leverage open-source technologies and run our system on our own
              infrastructure, making document processing both fast and
              affordable. The current focus is on books and publications, with
              plans to handle handwritten notes for the education sector—so
              students can digitize class notes in real time.
            </p>
          </div>
          {/* 3. Modular and Adaptive by Design */}
          <div>
            <span className="py-2 text-[17px] md:text-[19px] lg:text-[21px] text-[#15919B]">
              3. Modular and Adaptive by Design
            </span>
            <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              Our OCR system is modular and robust: - It uses microservices to
              easily plug in and compare different OCR models. - AI-driven
              preprocessing adapts steps to each document’s unique
              needs—improving accuracy for everything from textbooks to notes. -
              Our approach lets us continually optimize for both accuracy and
              computational cost..
            </p>
          </div>
          {/* 4.  Learning by Building: Our Educational Mission */}
          <div>
            <span className="py-2 text-[17px] md:text-[19px] lg:text-[21px] text-[#15919B]">
              4. Learning by Building: Our Educational Mission
            </span>
            <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              This project is powered by students and junior developers,
              upskilled through real hands-on work. Supported by Eminence Lab
              Education, we continuously bring in new talent, train them in
              microservices, CI/ CD (Jenkins), and automated testing, and
              integrate their learning directly into the platform.
            </p>
          </div>
          {/* 5. Early Impact & Milestones */}
          <div>
            <span className="py-2 text-[17px] md:text-[19px] lg:text-[21px] text-[#15919B]">
              5. Early Impact & Milestones
            </span>
            <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              (i) Three developers have already gained real-world experience in
              microservices, CI/CD, and testing.
            </p>
            <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              (ii) The system is live with seamless Jenkins pipelines and robust
              test coverage.{" "}
            </p>
            <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              (iii) [Placeholder: mini case study—e.g., “Digitized a class
              textbook in hours, not days, for our team”]{" "}
            </p>
          </div>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Placeholder */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Placeholder
          </h2>

          <p className="text-[30px] text-red-600">
            [Placeholder: Visual Diagram of OCR Pipeline]
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Our Vision */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Our Vision
          </h2>
          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            We’re aiming high: making high-quality OCR affordable for schools,
            fast for businesses, and powerful enough to compete with industry
            leaders like Google and OpenAI. The platform is being built for our
            needs today, but designed to scale and serve clients of any size
            tomorrow.
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Testimonials */}
        <div>
          <OcrTestimonials />
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Placeholder */}
        <div className="mb-12">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Partner With Us!
          </h2>

          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            If you’re a business looking for cost-effective, flexible OCR
            solutions, let’s collaborate! We’re ready to help you transform your
            document processing
          </p>

          <p className="text-[30px] text-red-600">
            [Placeholder: Roadmap / future plan summary]
          </p>
        </div>

        {/* Jon Us */}
        <div className="container mx-auto py-12 px-6 sm:px-8 lg:px-16 mb-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 rounded-xl shadow-2xl">
          <div className="relative z-10 text-white">
            {/* Content Wrapper */}
            <div className="flex flex-col md:flex-row justify-between items-center gap-10 md:gap-16 px-6 py-8 rounded-xl shadow-lg">
              {/* Left Content */}
              <div className="text-center md:text-left max-w-lg">
                <p className="text-lg sm:text-xl text-gray-100 mb-6 leading-relaxed">
                  Are you a student or junior developer eager to learn and make
                  an impact? Join our team and gain real-world experience!
                </p>
              </div>

              {/* Buttons Section */}
              <div className="justify-center">
                <a
                  href="https://forms.gle/ACuiKs8wb4buHiyt8"
                  target="_blank"
                  className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
                >
                  Join Us
                </a>
              </div>
            </div>
          </div>

          {/* Custom Clip-path CSS */}
          <style>{`
                .clip-path-slant {
                  clip-path: polygon(20% 0%, 100% 0%, 100% 100%, 0% 100%);
                }
              `}</style>
        </div>
      </section>
    </>
  );
};

export default Ocr;
