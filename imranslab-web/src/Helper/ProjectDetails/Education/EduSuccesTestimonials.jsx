/** @format */
import { useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation, Autoplay } from "swiper/modules";
import "swiper/css";
import "swiper/css/navigation";

import { FaChevronLeft, FaChevronRight } from "react-icons/fa6";
import { EdusuccestestimonialData } from "../../../Data/EduSuccesTestimonials";

const EduSuccesTestimonials = () => {
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
    <div className="w-full max-w-9xl mx-auto space-y-8 px-4 sm:px-6 lg:px-10 py-10">
      {/* Header */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <h2 className="text-[#B3225F] text-[24px] md:text-[26px] lg:text-[30px] font-bold">
          Alumni Success Stories
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
        {EdusuccestestimonialData.map((item) => (
          <SwiperSlide key={item.id}>
            <div className="bg-[#c8edf3] p-6 rounded-xl shadow-lg hover:shadow-2xl transition duration-300 min-h-[100px] flex flex-col justify-between">
              <p className="text-[#151517] text-sm sm:text-base font-medium mb-6 leading-relaxed">
                {item.desc}
              </p>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default EduSuccesTestimonials;
