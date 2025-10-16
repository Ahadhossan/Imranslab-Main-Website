import { Link, useNavigate } from 'react-router-dom'
import {
    UserIcon,
    LogOutIcon,
    Share2Icon,
    CpuIcon,
    BookOpenIcon,
    GitPullRequestIcon,
} from 'lucide-react'
import useAuth from '../../hooks/useAuth'

const Sidebar = ({ userData, activeTab, setActiveTab }) => {
    const { logout } = useAuth()
    const navigate = useNavigate()

    return (
        <aside className="hidden md:flex md:w-72 h-screen bg-white border-r border-gray-200">
            <div className="p-4">
                <div className="flex items-center mb-4">
                    <div className="w-10 h-10 rounded-full bg-gray-200 overflow-hidden mr-3">
                        {userData.image ? (
                            <img
                                src={userData.image}
                                alt="Current Profile"
                                className="w-full h-full rounded-md object-cover"
                            />
                        ) : (
                            <img
                                src="https://avatars.githubusercontent.com/u/1000000?v=4"
                                alt="Profile"
                                className="w-full h-full object-cover"
                            />
                        )}
                    </div>
                    <div>
                        <h3 className="font-medium text-gray-800 text-sm">{`${userData.first_name} ${userData.last_name}`}</h3>
                        <Link to={'/profile'}>
                            <p className="text-xs text-gray-600">@{userData.username}</p>
                        </Link>
                    </div>
                </div>
                <div className="space-y-6">
                    {/* Profile Section */}
                    <div>
                        <div className="mb-2">
                            <button
                                onClick={() => setActiveTab('profile')}
                                className={`flex items-center w-full px-2 py-1.5 rounded-md ${activeTab === 'profile' ? 'bg-gray-100' : ''}`}
                            >
                                <UserIcon size={16} className="mr-2 text-gray-600" />
                                <span className="text-sm text-gray-800">Profile Information</span>
                            </button>
                        </div>
                    </div>

                    {/* Social Links Section */}
                    <div>
                        <button
                            onClick={() => setActiveTab('social')}
                            className={`flex items-center w-full px-2 py-1.5 rounded-md ${activeTab === 'social' ? 'bg-gray-100' : ''}`}
                        >
                            <Share2Icon size={16} className="mr-2 text-gray-600" />
                            <span className="text-sm text-gray-800">Social Links</span>
                        </button>
                    </div>

                    {/* Technologies Section */}
                    <div>
                        <button
                            onClick={() => setActiveTab('technologies')}
                            className={`flex items-center w-full px-2 py-1.5 rounded-md ${activeTab === 'technologies' ? 'bg-gray-100' : ''}`}
                        >
                            <CpuIcon size={16} className="mr-2 text-gray-600" />
                            <span className="text-sm text-gray-800">Core Technologies</span>
                        </button>
                    </div>

                    {/* Contributions Section */}
                    <div>
                        <button
                            onClick={() => setActiveTab('contributions')}
                            className={`flex items-center w-full px-2 py-1.5 rounded-md ${activeTab === 'contributions' ? 'bg-gray-100' : ''}`}
                        >
                            <GitPullRequestIcon size={16} className="mr-2 text-gray-600" />
                            <span className="text-sm text-gray-800">Contributions</span>
                        </button>
                    </div>


                    {/* Projects Section */}
                    <div>
                        <button
                            onClick={() => setActiveTab('projects')}
                            className={`flex items-center w-full px-2 py-1.5 rounded-md ${activeTab === 'projects' ? 'bg-gray-100' : ''}`}
                        >
                            <GitPullRequestIcon size={16} className="mr-2 text-gray-600" />
                            <span className="text-sm text-gray-800">Projects</span>
                        </button>
                    </div>

                    {/* Articles Section */}
                    <div>
                        <button
                            onClick={() => setActiveTab('articles')}
                            className={`flex items-center w-full px-2 py-1.5 rounded-md ${activeTab === 'articles' ? 'bg-gray-100' : ''}`}
                        >
                            <BookOpenIcon size={16} className="mr-2 text-gray-600" />
                            <span className="text-sm text-gray-800">Articles</span>
                        </button>
                    </div>


                    {/* Logout Section */}
                    <div className="pt-4 mt-4 border-t border-gray-200">
                        <button onClick={() => {
                            logout();
                            navigate("/login");
                        }} className="flex items-center px-2 py-1.5 ">
                            <LogOutIcon size={16} className="mr-2 text-gray-500" />
                            <span className="text-sm text-gray-600 hover:text-red-600">Log out</span>
                        </button>
                    </div>
                </div>
            </div>
        </aside>
    )
}

export default Sidebar;