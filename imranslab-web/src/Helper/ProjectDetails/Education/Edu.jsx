/** @format */

import PageHeader from "../../PageHeader";
import EduStoryTestimonial from "./EduStoryTestimonial";
import EduStudentTestimonial from "./EduStudentTestimonial";
import EduSuccesTestimonials from "./EduSuccesTestimonials";

const Edu = () => {
  return (
    <>
      {/* Header Section */}
      <PageHeader
        title="Education Website"
        breadcrumb={[
          { label: "Home", path: "/home" },
          { label: "Projects", path: "/projects" },
          { label: "Education Website" },
        ]}
      />

      {/* main content */}
      <section className="p-6">
        {/* First Top */}
        <div className="py-2">
          <div>
            <img
              src="https://i.ibb.co/fzXFC2H5/edudetails.png"
              alt="education"
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

        {/*imranslab Education: Shaping Futures Across Bangladesh */}
        <div className="mt-10">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            imranslab Education: Shaping Futures Across Bangladesh
          </h2>
          <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            Started in 2020, imranslab Education is the flagship training and
            talent engine of imranslab. As the only nationwide education
            provider in Bangladesh using a full-featured Learning Management
            System (LMS), we’re breaking barriers—making world-class learning,
            skill-building, and career development accessible to students and
            families in all sixty-eight districts.
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Our Mission */}
        <div className="mt-10">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Our Mission
          </h2>
          <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            We’re here to make high-quality education practical, career-focused,
            and available anywhere. Our open-source, Moodle-powered LMS and
            custom front-end let students, parents, and guardians track
            progress, check grades, and engage with courses tailored to real
            goals—from Python and Java to IELTS and school subjects like
            O-Levels and A-Levels.
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/*  By the Numbers */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            By the Numbers
          </h2>

          <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {/* Card 1 */}
              <div className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]">
                <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                  2,000+
                </h1>
                <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                  students from 68 districts
                </p>
              </div>

              {/* Card 2 */}
              <div className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]">
                <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                  150+
                </h1>
                <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                  alumni have worked with us
                </p>
              </div>

              {/* Card 3 */}
              <div className="bg-[#c8edf3] px-6 py-8 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer group text-center hover:border hover:border-[#9de5f1]">
                <h1 className="text-lg sm:text-xl md:text-2xl font-bold text-[#15919B] transition-colors duration-200">
                  95%
                </h1>
                <p className="text-sm sm:text-base text-[#151517] pt-3 leading-relaxed">
                  of imranslab tech workforce comes from this platform
                </p>
              </div>
            </div>
          </div>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Case Study: Student Success Story */}
        <div>
          <EduStoryTestimonial />
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Unique Features*/}
        <div className="mt-10">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Unique Features
          </h2>
          <p className=" text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            - Only LMS-based education provider in Bangladesh <br /> - Real-time
            dashboards for students, parents, and guardians <br />
            - Popular courses: Python, Java, Selenium, English language (IELTS,
            Basic, Intermediate) <br />
            - Built-in pathway from learning to tech careers <br />- Supported
            and developed by imranslab, ensuring world-class standards and
            continuous improvement
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Our Bold Vision */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Our Bold Vision
          </h2>

          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            By 2026, we aim to deliver O-Levels, A-Levels, and modern tech
            education to students in every rural district of Bangladesh—reaching
            even those without traditional access to quality coaching or
            instruction.
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

        {/* Student Testimonials*/}
        <div>
          <EduStudentTestimonial />
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/*  Guardian Review */}
        <div className="mb-12">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Guardian Review
          </h2>

          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            imranslab Education has been a crucial support system for my child
            academic and personal development. The dedicated mentorship and
            diverse learning resources have allowed my child to grow not just in
            knowledge but in confidence as well. We have seen a remarkable
            improvement in their approach to problem-solving and a clear path
            forward in their academic journey. I am grateful for the impact
            imranslab Education has had on their life.
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Alumni Success Stories */}
        <div>
          <EduSuccesTestimonials />{" "}
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Stay Connected */}
        <div className="mb-12">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Stay Connected
          </h2>

          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            Learning doesn’t stop with a course, and neither should your
            connection with us. We invite our alumni, parents, and mentors to
            stay involved and continue growing together. Whether it is through
            our alumni network, parent forums, or mentorship programs, there are
            endless opportunities to engage, share experiences, and support one
            another. These platforms not only provide lifelong relationships but
            also offer professional guidance and valuable insights. Join us
            today to stay connected, expand your network, and continue your
            journey with the support of a thriving community. Together, we can
            make a lasting impact!
          </p>
        </div>

        {/* Join Us */}
        <div className="container mx-auto py-10 px-6 sm:px-8 lg:px-10 mb-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 rounded-xl shadow-2xl">
          <div className="relative z-10 text-white">
            {/* Content Wrapper */}
            <div className="flex flex-col md:flex-row justify-between items-center gap-10 md:gap-16 px-6 py-8 rounded-xl shadow-lg">
              {/* Left Content */}
              <div className="text-center md:text-left max-w-lg">
                <p className="text-lg sm:text-xl text-gray-100 mb-6 leading-relaxed">
                  Whether you’re a student ready to level up, a parent seeking
                  real progress, or a school or partner interested in
                  collaboration, imranslab Education welcomes you. Together,
                  we’re shaping futures, one learner at a time.
                </p>
              </div>

              {/* Buttons Section */}
              <div className="justify-center">
                <a
                  href="https://education.imranslab.org/"
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

export default Edu;
