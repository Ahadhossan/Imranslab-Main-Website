/** @format */

// import { Link } from "react-router-dom";

const PageHeader = ({ title }) => {
  return (
    <div className="w-full header-bg h-[210px] bg-gradient-to-r from-[#0f172a] to-[#334155] bg-cover bg-center flex flex-col items-center justify-center p-12 lg:px-12 text-center pb-0">
      {/* Title */}
      <div>
        <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold text-[#649EC5] uppercase">
          {title}
        </h1>
      </div>

      {/* Breadcrumb */}
      {/* <div className="flex flex-wrap justify-center items-center gap-3 mt-6 text-base sm:text-lg text-[#D7FCFF] font-medium">
        {breadcrumb.map((item, index) => (
          <span key={index} className="flex items-center gap-2">
            {item.path ? (
              <Link
                to={item.path}
                className="hover:border-b border-[#47A1C4] text-[#B3225F] hover:text-[#47A1C4] transition duration-200"
              >
                {item.label}
              </Link>
            ) : (
              <span className="text-white">{item.label}</span>
            )}
            {index < breadcrumb.length - 1 && (
              <span className="text-[#B3225F]">|</span>
            )}
          </span>
        ))}
      </div> */}
    </div>
  );
};

export default PageHeader;
