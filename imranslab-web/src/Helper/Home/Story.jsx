/** @format */
import { useRef } from "react";
import { motion, useScroll } from "framer-motion";
import Details from "./Details";

const Story = () => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "center start"],
  });

  const experiences = [
    {
      desc: "Launched first open-source education tool",
      time: "2022",
    },
    {
      desc: "Built scalable CI/CD pipelines and AI-based OCR tools",
      time: "2023",
    },
    {
      desc: "imranslabPay platform released for secure educational transactions",
      time: "2024",
    },
    {
      desc: "Global expansion in research tools, developer training, and smart systems",
      time: "2025",
    },
  ];

  return (
    <section className="my-16 px-4 md:px-10 lg:px-16">
      <h2 className="text-center text-2xl md:text-3xl font-bold text-[#B3225F] mb-20">
        Milestones
      </h2>

      <div className="relative" ref={ref}>
        <motion.div
          style={{ scaleY: scrollYProgress }}
          className="absolute left-1/2 top-0 w-1 h-full bg-black origin-top z-0"
        />
        <ul className="relative z-10">
          {experiences.map((item, index) => (
            <Details key={index} {...item} isLeft={index % 2 === 0} />
          ))}
        </ul>
      </div>
    </section>
  );
};

export default Story;
