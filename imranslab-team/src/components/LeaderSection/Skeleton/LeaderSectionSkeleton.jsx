import { motion } from "framer-motion";

const LeaderSectionSkeleton = () => {
    return (
        <div className="px-4 mx-auto max-w-[1440px] sm:px-6 lg:px-8">
            <div className="grid gap-6 mb-16 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3">
                {[...Array(3)].map((_, index) => (
                    <motion.div
                        key={index}
                        className="relative flex flex-col overflow-hidden transition duration-300 transform bg-gray-900 shadow-lg group rounded-xl"
                        initial={{ opacity: 0.6 }}
                        animate={{ opacity: 1 }}
                        transition={{
                            duration: 1.2,
                            repeat: Infinity,
                            repeatType: "reverse",
                            ease: "easeInOut"
                        }}
                    >
                        {/* Image Section Skeleton */}
                        <div className="w-full">
                            <div className="aspect-w-16 aspect-h-9 md:aspect-w-1 md:aspect-h-1">
                                <div className="object-cover w-full h-80 bg-gray-400 rounded-lg"></div>
                            </div>
                        </div>

                        {/* Content Section Skeleton */}
                        <div className="p-6 md:w-1/2">
                            <div className="h-7 w-3/4 bg-gray-700 rounded mb-2"></div>
                            <div className="h-5 w-1/2 bg-gray-700 rounded mb-4"></div>
                            <div className="space-y-2 mb-4">
                                <div className="h-4 w-full bg-gray-700 rounded"></div>
                                <div className="h-4 w-5/6 bg-gray-700 rounded"></div>
                                <div className="h-4 w-4/6 bg-gray-700 rounded"></div>
                            </div>

                            {/* Social links skeleton */}
                            <div className="flex items-center gap-3 mb-4">
                                {[...Array(3)].map((_, i) => (
                                    <div key={i} className="w-6 h-6 bg-gray-700 rounded-full"></div>
                                ))}
                            </div>

                            {/* Button skeleton */}
                            <div className="h-10 w-24 bg-gray-700 rounded-md"></div>
                        </div>
                    </motion.div>
                ))}
            </div>
        </div>
    );
};

export default LeaderSectionSkeleton;