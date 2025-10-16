/** @format */
import { useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation, Autoplay } from "swiper/modules";
import "swiper/css";
import "swiper/css/navigation";

import { FaChevronLeft, FaChevronRight, FaStar } from "react-icons/fa6";
import { testimonialData } from "../../Data/testimonial";

const Testimonials = () => {
  const [isBeginning, setIsBeginning] = useState(true);
  const [isEnd, setIsEnd] = useState(false);

  const handleSwiperEvents = (swiper) => {
    setIsBeginning(swiper.isBeginning);
    setIsEnd(swiper.isEnd);
  };

  const breakpointsResponsive = {
    0: { slidesPerView: 1, spaceBetween: 10 },
    640: { slidesPerView: 2, spaceBetween: 20 },
    1024: { slidesPerView: 3, spaceBetween: 30 },
  };

  return (
    <div className="w-full max-w-7xl mx-auto space-y-8 px-4 sm:px-6 lg:px-12 py-16">
      {/* Header */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <h2 className="text-2xl sm:text-3xl font-semibold text-[#151517]">
          Testimonials
        </h2>

        <div className="flex items-center gap-4">
          <button
            className={`custom-prev bg-blue-600 hover:bg-blue-700 text-white p-2 rounded-full transition transform hover:scale-105 ${
              isBeginning ? "opacity-50 cursor-not-allowed" : "cursor-pointer"
            }`}
            disabled={isBeginning}
          >
            <FaChevronLeft size={18} />
          </button>
          <button
            className={`custom-next bg-blue-600 hover:bg-blue-700 text-white p-2 rounded-full transition transform hover:scale-105 ${
              isEnd ? "opacity-50 cursor-not-allowed" : "cursor-pointer"
            }`}
            disabled={isEnd}
          >
            <FaChevronRight size={18} />
          </button>
        </div>
      </div>

      {/* Swiper Carousel */}
      <Swiper
        slidesPerView={1}
        spaceBetween={10}
        autoplay={{ delay: 5000, disableOnInteraction: false }}
        navigation={{
          nextEl: ".custom-next",
          prevEl: ".custom-prev",
        }}
        breakpoints={breakpointsResponsive}
        onSlideChange={handleSwiperEvents}
        onInit={handleSwiperEvents}
        modules={[Navigation, Autoplay]}
        className="w-full"
      >
        {testimonialData.map((item) => (
          <SwiperSlide key={item.id}>
            <div className="bg-[#c8edf3] p-6 rounded-xl shadow-lg hover:shadow-2xl transition duration-300 min-h-[200px] flex flex-col justify-between">
              <p className="text-[#151517] text-sm sm:text-base font-medium mb-6 leading-relaxed">
                {item.desc}
              </p>

              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <img
                    src={item.img}
                    alt={item.name}
                    className="w-12 h-12 object-cover rounded-full border"
                  />
                  <div>
                    <p className="text-sm font-bold text-[#151517]">
                      {item.name}
                    </p>
                    <p className="text-xs text-[#151517]">
                      {item.role} at {item.company}
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-1 bg-yellow-500/10 px-2 py-1 rounded-full">
                  <FaStar className="text-yellow-600 text-sm" />
                  <p className="text-xs text-yellow-600 font-semibold">
                    {item.rating}
                  </p>
                </div>
              </div>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default Testimonials;
