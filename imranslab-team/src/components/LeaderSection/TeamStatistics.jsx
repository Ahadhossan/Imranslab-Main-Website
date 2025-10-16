import { teamStats } from "../../Data/expert";
import { motion, useInView } from "framer-motion";

const TeamStatistics = ({ teamRef }) => {
    const isTeamInView = useInView(teamRef, { once: true, margin: "-100px" });
    // Animation variants
    const teamcardVariants = {
        hidden: { opacity: 0, y: 40 },
        visible: (i) => ({
            opacity: 1,
            y: 0,
            transition: {
                delay: i * 0.2,
                duration: 0.6,
                ease: "easeOut",
            },
        }),
    };
    return (
        <div className="grid grid-cols-2 gap-6 md:grid-cols-4">
            {teamStats.map((stat, index) => (
                <motion.div
                    key={index}
                    className="bg-[#c8edf3] w-full p-6 rounded-lg shadow-lg transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-2xl hover:border hover:border-[#9de5f1] cursor-pointer"
                    initial="hidden"
                    animate={isTeamInView ? "visible" : "hidden"}
                    custom={index}
                    variants={teamcardVariants}
                >
                    <h1 className="text-xl sm:text-2xl md:text-3xl font-bold text-[#15919B]">
                        {stat.count}
                    </h1>
                    <p className="text-sm sm:text-base md:text-lg text-[#151517] pt-2 leading-relaxed">
                        {stat.label}
                    </p>
                </motion.div>
            ))}
        </div>
    )
}

export default TeamStatistics