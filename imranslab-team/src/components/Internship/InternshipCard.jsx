import { Link } from "react-router-dom";
import useUsers from "../../hooks/useUsers";
import { motion, useInView } from "framer-motion";
import InternshipSkeleton from "./Skeleton/InternshipSkeleton"

const InternshipCard = ({ internRef }) => {
    const { users, loadingUsers } = useUsers({ role: 'intern' });
    const isInternInView = useInView(internRef, { once: true, margin: "-100px" });

    // Animation variants
    const internCardVariants = {
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
        return <InternshipSkeleton />
    }


    return (
        <div className="grid grid-cols-1 gap-8 mb-16 sm:grid-cols-3 md:grid-cols-6">

            {users.map((member, index) => (

                <motion.div
                    key={index}
                    initial="hidden"
                    custom={index}
                    animate={isInternInView ? "visible" : "hidden"}
                    variants={internCardVariants}
                    className="relative overflow-hidden transition duration-300 transform bg-gray-900 shadow-lg group rounded-xl hover:-translate-y-2"
                >
                    {/* Image with dim effect */}
                    <img
                        src={member.image}
                        alt={member.name}
                        className="object-cover w-full transition duration-300 h-50 group-hover:brightness-50"
                    />

                    {/* Overlay with shadowed background */}
                    <div className="absolute inset-0 flex flex-col items-center justify-center text-center text-white transition-opacity duration-500 opacity-0 bg-black/70 backdrop-blur-sm group-hover:opacity-100">
                        {/* Name */}
                        <h3 className="text-[15px] font-semibold text-[#B3225F] group-hover:text-white transition-colors duration-300 cursor-pointer">
                            {member.first_name} {member.last_name}
                        </h3>

                        {/* Role */}
                        <p className="text-[#70dbe3] font-medium mb-2">
                            {member.position}
                        </p>

                        {/* Bio */}
                        <p className="max-w-md mb-4 text-sm text-gray-300 sm:text-base">
                            {member.bio}
                        </p>

                        {/* Details Button */}
                        <div className="mt-4">
                            <Link to={`/intern/${member.id}`}
                                className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-md hover:bg-black transition-all duration-300"
                            >
                                More Details
                            </Link>
                        </div>
                    </div>
                </motion.div>
            ))}

        </div >
    )
}

export default InternshipCard