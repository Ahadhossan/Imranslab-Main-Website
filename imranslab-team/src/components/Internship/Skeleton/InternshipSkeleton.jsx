import { motion } from "framer-motion";

const InternshipSkeleton = () => {
    return (
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
            {/* Intern Cards Skeleton */}
            <div className="grid grid-cols-1 gap-8 mb-16 sm:grid-cols-3 md:grid-cols-6">
                {[...Array(6)].map((_, index) => (
                    <motion.div
                        key={index}
                        initial="hidden"
                        animate="visible"
                        custom={index}
                        variants={{
                            hidden: { opacity: 0, y: 40 },
                            visible: (i) => ({
                                opacity: 1,
                                y: 0,
                                transition: {
                                    duration: 0.7,
                                    delay: i * 0.1,
                                },
                            }),
                        }}
                        className="relative overflow-hidden transition duration-300 transform bg-gray-900 shadow-lg rounded-xl"
                    >
                        {/* Image skeleton with shimmer effect */}
                        <div className="w-full h-40 bg-gray-700 rounded-t-xl relative overflow-hidden">
                            <div className="absolute inset-0 -translate-x-full bg-gradient-to-r from-gray-700 via-gray-800 to-gray-700 animate-shimmer" />
                        </div>

                        {/* Overlay content skeleton */}
                        <div className="absolute inset-0 flex flex-col items-center justify-center p-4 text-center text-white opacity-100 bg-black/70 backdrop-blur-sm">
                            {/* Name skeleton */}
                            <div className="h-5 w-3/4 bg-gray-600 rounded mb-3 relative overflow-hidden">
                                <div className="absolute inset-0 -translate-x-full bg-gradient-to-r from-gray-600 via-gray-700 to-gray-600 animate-shimmer" />
                            </div>

                            {/* Role skeleton */}
                            <div className="h-4 w-1/2 bg-gray-600 rounded mb-3 relative overflow-hidden">
                                <div className="absolute inset-0 -translate-x-full bg-gradient-to-r from-gray-600 via-gray-700 to-gray-600 animate-shimmer" />
                            </div>

                            {/* Bio skeleton */}
                            <div className="space-y-2 mb-4 w-full">
                                <div className="h-3 w-full bg-gray-600 rounded relative overflow-hidden">
                                    <div className="absolute inset-0 -translate-x-full bg-gradient-to-r from-gray-600 via-gray-700 to-gray-600 animate-shimmer" />
                                </div>
                                <div className="h-3 w-5/6 bg-gray-600 rounded relative overflow-hidden">
                                    <div className="absolute inset-0 -translate-x-full bg-gradient-to-r from-gray-600 via-gray-700 to-gray-600 animate-shimmer" />
                                </div>
                                <div className="h-3 w-4/5 bg-gray-600 rounded relative overflow-hidden">
                                    <div className="absolute inset-0 -translate-x-full bg-gradient-to-r from-gray-600 via-gray-700 to-gray-600 animate-shimmer" />
                                </div>
                            </div>

                            {/* Button skeleton */}
                            <div className="h-10 w-28 bg-gray-600 rounded-md mt-2 relative overflow-hidden">
                                <div className="absolute inset-0 -translate-x-full bg-gradient-to-r from-gray-600 via-gray-700 to-gray-600 animate-shimmer" />
                            </div>
                        </div>
                    </motion.div>
                ))}
            </div>

            {/* Add CSS for shimmer animation */}
            <style>
                {`
                @keyframes shimmer {
                    0% { transform: translateX(-100%); }
                    100% { transform: translateX(100%); }
                }
                .animate-shimmer {
                    animation: shimmer 1.5s infinite;
                }
                `}
            </style>
        </div>
    );
};

export default InternshipSkeleton;