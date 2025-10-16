import { Link } from "react-router-dom";
import { motion, useInView } from "framer-motion";
import useUsers from "../../hooks/useUsers";
import LeadershipTeamSkeleton from "./Skeleton/LeadershipTeamSkeleton";

const Leadershipteam = ({ expertRef }) => {
    const { users, loadingUsers } = useUsers({ role: 'experts' });
    const isExpertInView = useInView(expertRef, { once: true, margin: "-100px" });

    // Animation variants
    const expertCardVariants = {
        hidden: { opacity: 0, y: 40 },
        visible: (i) => ({
            opacity: 1,
            y: 0,
            transition: {
                duration: 0.7,
                delay: i * 0.3,
            },
        }),
    };
    if (loadingUsers) {
        return <LeadershipTeamSkeleton />;
    }

    return (
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
            {/* Section Header */}
            <div className="mb-16 text-center">
                <motion.h2
                    initial={{ opacity: 0, x: 50 }}
                    animate={isExpertInView ? { opacity: 1, x: 0 } : {}}
                    exit={{ opacity: 0, x: -50 }}
                    transition={{ duration: 0.6 }}
                    className="text-3xl sm:text-4xl font-bold text-[#B3225F] mb-4"
                >
                    Meet Our Expert Team
                </motion.h2>
                <div className="h-0.5 bg-blue-500 w-14 mx-auto" />
                <motion.p
                    initial={{ opacity: 0, x: -50 }}
                    animate={isExpertInView ? { opacity: 1, x: 0 } : {}}
                    exit={{ opacity: 0, x: 50 }}
                    transition={{ duration: 0.8, delay: 0.2 }}
                    className="text-lg sm:text-xl text-[#151517] pt-3"
                >
                    Passionate professionals driving innovation forward
                </motion.p>
            </div>

            {/* Leadership Cards */}
            <div className="grid grid-cols-1 gap-8 mb-16 sm:grid-cols-3 md:grid-cols-4">
                {users.map((user, id) => (
                    <motion.div
                        key={id}
                        initial="hidden"
                        animate={isExpertInView ? "visible" : "hidden"}
                        custom={id}
                        variants={expertCardVariants}
                        className="relative overflow-hidden transition duration-300 transform bg-gray-900 shadow-lg group rounded-xl hover:-translate-y-2"
                    >
                        {/* Image with dim effect */}
                        <img
                            src={user.image}
                            alt={user.username}
                            className="object-cover w-full transition duration-300 h-80 group-hover:brightness-50"
                        />

                        {/* Overlay with shadowed background */}
                        <div className="absolute inset-0 flex flex-col items-center justify-center p-6 text-center text-white transition-opacity duration-500 opacity-0 bg-black/70 backdrop-blur-sm group-hover:opacity-100">
                            {/* Name */}
                            <h3 className="text-[25px] font-semibold text-[#B3225F] group-hover:text-white transition-colors duration-300 cursor-pointer">
                                {user.first_name} {" "} {user.last_name}
                            </h3>

                            {/* Role */}
                            <p className="text-[#70dbe3] font-medium mb-2">
                                {user.position}
                            </p>

                            {/* Bio */}
                            <p className="max-w-md mb-4 text-sm text-gray-300 sm:text-base">
                                {user.bio}
                            </p>

                            {/* Details Button */}
                            <div className="mt-4">
                                <Link
                                    to={`/experts/${user.id}?role=${user.role}`}
                                    className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
                                >
                                    More Details
                                </Link>
                            </div>
                        </div>
                    </motion.div>
                ))}
            </div>
        </div>
    )
}

export default Leadershipteam;