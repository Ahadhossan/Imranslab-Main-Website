// components/ProjectCard.jsx

const ProjectCard = ({ project }) => {
    const APICLIENT = import.meta.env.VITE_APICLIENT || "https://imranslab-team.imranslab.org/"
    const {
        projectlink,
        technologies,
        description,
        image,
        created_at,
    } = project;

    const formattedDate = new Date(created_at).toLocaleDateString("en-GB");

    return (
        <div className="bg-[#cfe9e4] rounded-lg shadow-lg">
            <img
                src={APICLIENT + image}
                alt="Project"
                className="object-cover w-full h-40 rounded-md"
            />
            <div className="p-4">
                <span className="mt-4 text-[20px] text-[#151517] font-semibold">
                    {technologies}
                </span>
                <p className="mt-2 text-[15px] text-gray-700 line-clamp-3">{description}</p>
                <div className="flex flex-wrap items-center justify-between mt-4">
                    <div className="mb-4 sm:mb-0">
                        <a
                            href={projectlink}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-block bg-gray-900 text-white px-6 sm:px-8 py-2.5 sm:py-3 text-sm sm:text-base rounded-lg hover:bg-black transition-all duration-300"
                        >
                            Link
                        </a>
                    </div>
                    <div>
                        <span className="inline-block text-[16px] sm:text-[20px] font-medium text-[#15919B] tracking-wide">
                            {formattedDate}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ProjectCard;
