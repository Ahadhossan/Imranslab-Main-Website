// components/ProjectList.jsx
import { useState } from "react";
import ProjectCard from "./ProjectCard";

const ProjectList = ({ projects = [] }) => {
    const [showMore, setShowMore] = useState(false);

    const visibleProjects = showMore ? projects : projects.slice(0, 3);

    return (
        <div className="mt-6">
            <h2 className="py-2 text-[#B3225F] text-[30px] font-bold">
                Projects Contributed To
            </h2>

            {projects.length === 0 ? (
                <p className="text-[#151517] text-[17px]">No projects found.</p>
            ) : (
                <>
                    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3">
                        {visibleProjects.map((project) => (
                            <ProjectCard key={project.id} project={project} />
                        ))}
                    </div>

                    {projects.length > 3 && (
                        <div className="mt-6 text-center">
                            <button
                                onClick={() => setShowMore(!showMore)}
                                className={`inline-block px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-lg text-white transition-all duration-300 ${showMore
                                        ? "bg-[#B3225F] hover:bg-[#a11745]"
                                        : "bg-[#15919B] hover:bg-[#0d8b83]"
                                    }`}
                            >
                                {showMore ? "See Less" : "See More"}
                            </button>
                        </div>
                    )}
                </>
            )}
        </div>
    );
};

export default ProjectList;
