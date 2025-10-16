/** @format */
import PageHeader from "../../PageHeader";

const Softtech = () => {
  return (
    <>
      {/* Header Section */}
      <PageHeader
        title="Softtech Website"
        breadcrumb={[
          { label: "Home", path: "/home" },
          { label: "Projects", path: "/projects" },
          { label: "Softtech" },
        ]}
      />

      {/* main content */}
      <section className="p-6">
        {/* First Top */}
        <div className="py-2">
          <div>
            <img
              src="https://i.ibb.co/YBPLpbj3/softtechdetails.png"
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
        {/*SoftTech: Bridging Global Innovation from Sharjah */}
        <div className="mt-10">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            SoftTech: Bridging Global Innovation from Sharjah
          </h2>
          <div>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              SoftTech is a dynamic technology company based in Sharjah, founded
              by visionary professionals from the UAE and beyond. Our mission is
              to connect world-class clients—including Y Combinator startups,
              Big Tech, and forward-thinking organizations—with expert software
              solutions and highly personalized consulting.
            </p>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px] py-2">
              What makes SoftTech unique is our dual role: we consult directly
              with clients to understand their goals, then match them with the
              ideal technical teams to deliver modern, efficient software
              products. We stand for innovation, speed, global collaboration,
              trust, and tailored service in every project.
            </p>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              With the technical foundation live and future plans for analytics
              and enhancements, our client now has a scalable platform ready to
              support ongoing business growth.
            </p>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px] py-2">
              SoftTech’s leadership features Mr. Taimur Rana, McGill alumnus and
              former senior consultant at Deloitte, bringing both technical and
              management expertise.
            </p>

            <p className="text-[#151517] text-[17px] md:text-[19px] lg:text-[21px] py-2">
              “At SoftTech, we strive to drive innovation with advanced
              technology and a strong dedication to quality.” — Mr. Taimur Rana
            </p>
          </div>
        </div>
        <div className="w-full mx-auto my-6 border-b border-black"></div>
        {/* Use Key tech */}
        {/* <div>
          <h2 className="py-2 text-[#B3225F] text-[30px] font-bold">
            Use key tech
          </h2> */}
        {/*  React */}
        {/* <p className="text-[#151517] text-[16px] sm:text-[17px] font-medium">
            <strong className="text-[#15919B] font-bold">1.React </strong>--
            React is a JavaScript library for building user interfaces, using
            components for efficient, dynamic web apps.
          </p> */}
        {/* TailwindCSS */}
        {/* <p className="text-[#151517] text-[16px] sm:text-[17px] font-medium">
            <strong className="text-[#15919B] font-bold">2.TailwindCSS </strong>
            -- TailwindCSS is a utility-first CSS framework that allows for
            rapid, customizable, and responsive web design.
          </p> */}
        {/* React Router */}
        {/* <p className="text-[#151517] text-[16px] sm:text-[17px] font-medium">
            <strong className="text-[#15919B] font-bold">
              3.React Router{" "}
            </strong>
            -- React Router is a library for handling routing in React
            applications, enabling navigation between components without page
            reloads.
          </p> */}
        {/* JavaScript (ES6+) */}
        {/* <p className="text-[#151517] text-[16px] sm:text-[17px] font-medium">
            <strong className="text-[#15919B] font-bold">
              4.JavaScript (ES6+)
            </strong>
            -- JavaScript is a high-level, dynamic, and interpreted programming
          </p> */}
        {/* Web3Form */}
        {/* <p className="text-[#151517] text-[16px] sm:text-[17px] font-medium">
            <strong className="text-[#15919B] font-bold">5.Web3Form </strong>--
            Web3Form is a decentralized form submission tool that integrates
            blockchain for secure, transparent data processing.
          </p>
        </div> */}
        {/* <div className="w-full mx-auto my-6 border-b border-black"></div> */}

        {/* ## By the Numbers - [Placeholder: “Infographic or visual—clients
        reached, countries served, or industries impacted.”] */}

        {/* <div className="w-full mx-auto my-6 border-b border-black"></div> */}

        {/* Case Study: Delivering Real Results */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Case Study: Delivering Real Results
          </h2>
          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            “Collaborated with a leading healthcare provider to streamline their
            data management system, improving operational efficiency by 40% and
            enhancing patient data security.”
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Our Services */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Our Services
          </h2>
          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            We offer a wide range of technology solutions—from custom software
            and web development to IT consulting and digital strategy—flexibly
            adapting to client needs in an ever-evolving digital landscape.
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/*  Looking Forward */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Looking Forward
          </h2>
          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            By 2027, SoftTech aims to become the region’s premier connector for
            tech talent and business, serving clients in at least ten countries
            and building a trusted global network.
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Our Network, Your Opportunity */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Our Network, Your Opportunity
          </h2>
          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            Join our growing partner network and collaborate with innovators
            worldwide. Whether you’re looking for a trusted development partner
            or seeking new markets, SoftTech is your gateway to global
            opportunity.
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Ready to Start? */}
        <div className="container mx-auto py-10 px-6 sm:px-8 lg:px-10 mb-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 rounded-xl shadow-2xl">
          <div className="relative z-10 text-white">
            {/* Content Wrapper */}
            <div className="flex flex-col md:flex-row justify-between items-center gap-10 md:gap-16 px-6 py-8 rounded-xl shadow-lg">
              {/* Left Content */}
              <div className="text-center md:text-left max-w-lg">
                <h2 className="text-3xl sm:text-4xl font-bold mb-4 text-shadow-lg">
                  Ready to Start?
                </h2>
                <p className="text-lg sm:text-xl text-gray-100 mb-6 leading-relaxed">
                  Let’s build something exceptional together. Contact us to
                  learn how SoftTech’s innovative solutions can help you achieve
                  your business goals and drive meaningful results.
                </p>
              </div>

              {/* Buttons Section */}
              <div className="justify-center">
                <a
                  href="https://soft-tech.imranslab.org/"
                  target="_blank"
                  className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
                >
                  Contact Us
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

export default Softtech;
