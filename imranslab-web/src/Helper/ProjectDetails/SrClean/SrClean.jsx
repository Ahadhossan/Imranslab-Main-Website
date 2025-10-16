/** @format */
import PageHeader from "../../PageHeader";

const SrClean = () => {
  return (
    <>
      {/* Header Section */}
      <PageHeader
        title="Sr Clean Website"
        breadcrumb={[
          { label: "Home", path: "/home" },
          { label: "Projects", path: "/projects" },
          { label: "Sr Clean" },
        ]}
      />

      {/* main content */}
      <section className="p-6">
        {/* First Top */}
        <div className="py-2">
          <div>
            <img
              src="https://i.ibb.co/nqx7LNrD/srcleandetails.png"
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

        {/*srclean: Practical Web Solutions, Powered by Growth */}
        <div className="mt-10">
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            srclean: Practical Web Solutions, Powered by Growth
          </h2>
          <div>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              When a leading Montreal cleaning business needed a digital
              presence to attract more clients, showcase services, and build
              trust, our team delivered a focused solution—quickly and
              collaboratively.
            </p>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px] py-2">
              We created a modern, lead-generating website using React, guided
              by real business needs. What sets this project apart isn’t just
              the technology, but the journey: a developer from our Eminence Lab
              Education program took the lead, learning React from scratch,
              contributing to our monorepo, and deploying the site through our
              automated CI/CD pipeline. This hands-on approach ensured fast
              delivery, quality, and reliability.
            </p>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              With the technical foundation live and future plans for analytics
              and enhancements, our client now has a scalable platform ready to
              support ongoing business growth.
            </p>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px] py-2">
              At imranslab, every project—big or small—is a step toward greater
              innovation. We nurture talent, focus on practical results, and lay
              the groundwork for future collaborations in AI, automation, and
              beyond.
            </p>
            <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
              Whether you’re building your first site or looking to push the
              boundaries with advanced tech, we’re here for every step of your
              digital journey.
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

        {/* Learning Journey */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Client Review!
          </h2>
          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            imranslab has been a game-changer for our business. Their expertise
            in web development and attention to detail helped us create a
            seamless, high-performing website. The team’s professionalism and
            dedication to quality are evident in every aspect of their work. I
            highly recommend imranslab for anyone seeking top-tier tech
            solutions!
          </p>
        </div>

        <div className="w-full mx-auto my-6 border-b border-black"></div>

        {/* Developer Perspective */}
        <div>
          <h2 className="py-2 text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
            Developer Perspective
          </h2>
          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px]">
            Working on the development of srclean has been an enriching
            experience. It allowed me to explore key aspects of modern web
            development, including the use of React.js, TailwindCSS, and React
            Router. I gained a deeper understanding of building responsive,
            adaptive layouts, ensuring that the application performs seamlessly
            across all devices. Implementing dynamic content and navigation
            through React Router improved my skills in creating smooth,
            user-friendly interactions.
          </p>
          <p className="text-[#363a36] text-[14px] md:text-[17px] lg:text-[18px] mt-2">
            One of the most rewarding parts of this project was refining my
            approach to clean, maintainable code. It emphasized the importance
            of efficient state management, testing, and validation. This project
            provided a great opportunity to grow as a developer, and I look
            forward to applying these lessons in future endeavors.
          </p>
        </div>
      </section>
    </>
  );
};

export default SrClean;
