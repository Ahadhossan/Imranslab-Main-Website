import { ArrowBigRightDash, Mail, PhoneCall } from "lucide-react";
import PageHeader from "../Helper/PageHeader";
import { useParams } from "react-router-dom";
import useUserDetail from "../hooks/useUserDetail";
import Loader from "../Helper/Loader";
import ProjectList from "../components/Project/ProjectList";
import ArticleList from "../components/Article/ArticleList";


const UserDetailsPage = () => {
    const params = useParams()
    const { user, loadingUser, errorUser } = useUserDetail(params.id)

    if (loadingUser) return <Loader />;
    return (
        <>
            {/* Header Section */}
            <PageHeader title={`${user.first_name} ${user.last_name}`} />
            {/* main content */}
            <section className="p-6 max-w-[1400px] mx-auto">
                {/* First Top */}
                <div className="flex flex-col items-start gap-8 p-4 md:flex-row">
                    <div>
                        <img
                            src={user.image}
                            alt={user.username}
                            className="object-cover transition duration-300 rounded-lg shadow-2xl h-52 w-60 md:h-64 group-hover:brightness-50"
                        />
                    </div>
                    <div className="w-full">
                        <h1 className="text-[22px] font-bold text-[#151517]">
                            <strong className="text-[#B3225F]">Name:</strong> {`${user.first_name} ${user.last_name}`}
                        </h1>
                        <h2 className="text-[19px] font-semibold text-[#151517]">
                            <strong className="text-[#B3225F]">Position:</strong> {user.position}
                        </h2>
                        <span className="text-[15px] font-medium text-[#151517]">
                            <strong className="text-[#B3225F]">Location:</strong> {user.address}
                        </span>
                        <br />
                        <div className="flex gap-4 text-[#151517] mt-2">
                            <span className="flex gap-2 text-[#B3225F]">
                                <PhoneCall />
                                <a
                                    href={`tel:${user.phone}`}
                                    className="text-[#151517] hover:border-[#15919B] hover:border-b"
                                >
                                    {user.phone}
                                </a>
                            </span>
                            |
                            <span className="flex gap-2 text-[#B3225F]">
                                <Mail />
                                <a
                                    href="mailto:"
                                    className="text-[#151517] hover:border-[#15919B] hover:border-b"
                                >
                                    {user.email}
                                </a>
                            </span>
                        </div>

                        <div className="flex gap-2 mx-auto mt-4">
                            <a href="" className="text-blue-500 ">
                                <img
                                    src="https://i.ibb.co/tPvK3GvH/linkedin.png"
                                    alt=""
                                    className="w-8 h-8"
                                />
                            </a>
                            <a href="http://" className="text-blue-500 ">
                                <img
                                    src="https://i.ibb.co/PZ4j5P9P/github.png"
                                    alt=""
                                    className="w-8 h-8"
                                />
                            </a>
                        </div>
                    </div>
                </div>

                {/* About Me */}
                <div className="mt-10">
                    <h2 className="py-2 text-[#B3225F] text-[30px] font-bold">
                        About {user.first_name}
                    </h2>
                    <p className="text-[#363a36] text-[17px]">{user.aboutme}</p>
                </div>

                <div className="w-full mx-auto my-6 border-b border-black"></div>

                {/* Core Technologies */}
               <div>
  <h2 className="py-2 text-[#B3225F] text-[30px] font-bold">Core Technologies</h2>
  <ul className="list-disc space-y-1 text-[#151517] text-[15px] font-medium">
    {user.coretechnologies?.map((tech) => (
      <li key={tech.id} className="flex gap-2 p-1 list-none"> <ArrowBigRightDash /> {tech.technology}</li>
    ))}
  </ul>
</div>

                {/* Key Contributions */}
                <div>
                    <h2 className="py-2 text-[#B3225F] text-[30px] font-bold">
                        Contributions
                    </h2>
                    <span className="text-[#151517] text-[16px] sm:text-[17px] font-medium ">
                        <strong className="text-[#15919B] font-small">
                            Key Contribution:
                        </strong>
                        {user.contributions?.map(contribution => (
                            <p key={contribution.id} className="flex gap-2 p-1">
                                <ArrowBigRightDash /> {contribution.keys}
                            </p>
                        ))}
                    </span>

                    {/* You can continue with the same structure as above for the "Key" section */}
                </div>

                <div className="w-full mx-auto my-6 border-b border-black"></div>

                {/* Projects Contributed To */}
                <div>
                    <ProjectList projects={user.projectscontributedto} />
                </div>

                <div className="w-full mx-auto my-6 border-b border-black"></div>

                {/* Articles Authored */}
                <div>
                    <ArticleList articles={user.articles} />
                </div>

                <div className="w-full mx-auto my-6 border-b border-black"></div>

                {/* Learning Journey */}
                {/* <div>
          <h2 className="py-2 text-[#B3225F] text-[30px] font-bold">
            Learning Journey
          </h2>
          <p className="flex gap-2 text-[#151517] text-[15px] font-medium">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit.
            Reprehenderit rem unde aperiam facilis. Porro nemo beatae illo atque
            mollitia voluptate ab consectetur. Ratione, facere natus sint soluta
            voluptatem sequi necessitatibus.
          </p>
        </div> */}

                {/* <div className="w-full mx-auto my-6 border-b border-black"></div> */}

                {/* Personal Interests */}
                <div>
                    <h2 className="py-2 text-[#B3225F] text-[30px] font-bold">
                        Personal Interests
                    </h2>
                    <p className="flex gap-2 text-[#151517] text-[15px] font-medium">
                        {user.personalinterests}
                    </p>
                </div>
            </section>
        </>
    )
}

export default UserDetailsPage;