import { motion } from "framer-motion";

const LeadershipTeamSkeleton = () => {
    return (
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
            {/* Section Header Skeleton */}
            <div className="mb-16 text-center">
                <motion.div
                    initial={{ opacity: 0.6 }}
                    animate={{ opacity: 1 }}
                    transition={{
                        duration: 1.2,
                        repeat: Infinity,
                        repeatType: "reverse",
                        ease: "easeInOut"
                    }}
                    className="h-10 w-1/3 bg-gray-300 rounded mx-auto mb-4"
                />
                <div className="h-0.5 bg-gray-300 w-14 mx-auto" />
                <motion.div
                    initial={{ opacity: 0.6 }}
                    animate={{ opacity: 1 }}
                    transition={{
                        duration: 1.2,
                        repeat: Infinity,
                        repeatType: "reverse",
                        ease: "easeInOut",
                        delay: 0.2
                    }}
                    className="h-6 w-2/3 bg-gray-300 rounded mx-auto pt-3"
                />
            </div>

            {/* Leadership Cards Skeleton */}
            <div className="grid grid-cols-1 gap-8 mb-16 sm:grid-cols-3 md:grid-cols-4">
                {[...Array(4)].map((_, index) => (
                    <motion.div
                        key={index}
                        initial={{ opacity: 0.6 }}
                        animate={{ opacity: 1 }}
                        transition={{
                            duration: 1.2,
                            repeat: Infinity,
                            repeatType: "reverse",
                            ease: "easeInOut",
                            delay: index * 0.1
                        }}
                        className="relative overflow-hidden transition duration-300 transform bg-white shadow-lg group rounded-xl"
                    >
                        {/* Image skeleton */}
                        <div className="w-full h-80 bg-gray-300 rounded-t-xl"></div>

                        {/* Overlay content skeleton */}
                        <div className="absolute inset-0 flex flex-col items-center justify-center p-6 text-center text-white opacity-100 bg-transparent">
                            {/* Name skeleton */}
                            <div className="h-7 w-3/4 bg-gray-400 rounded mb-2"></div>

                            {/* Role skeleton */}
                            <div className="h-5 w-1/2 bg-gray-400 rounded mb-4"></div>

                            {/* Bio skeleton */}
                            <div className="space-y-2 mb-4 w-full">
                                <div className="h-3 w-full bg-gray-400 rounded"></div>
                                <div className="h-3 w-5/6 bg-gray-400 rounded"></div>
                                <div className="h-3 w-4/6 bg-gray-400 rounded"></div>
                            </div>

                            {/* Button skeleton */}
                            <div className="h-10 w-32 bg-gray-400 rounded-md mt-4"></div>
                        </div>
                    </motion.div>
                ))}
            </div>
        </div>
    );
};

export default LeadershipTeamSkeleton;