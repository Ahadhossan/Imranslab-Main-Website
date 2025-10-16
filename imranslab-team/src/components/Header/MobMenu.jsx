/** @format */

import { motion } from 'framer-motion';
import { Menu, X } from 'lucide-react';
import { useState } from 'react';
import useAuth from '../../hooks/useAuth';
import { useActiveTab } from '../../context/ActiveTabContext';
import { Link, useNavigate } from 'react-router-dom';
import {
  UserIcon,
  LogOutIcon,
  Share2Icon,
  CpuIcon,
  BookOpenIcon,
  GitPullRequestIcon,
} from 'lucide-react';

export default function MobMenu({ Menus }) {
  const [isOpen, setIsOpen] = useState(false);
  const [clicked, setClicked] = useState(null);
  const { activeTab, setActiveTab } = useActiveTab();

  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const toggleDrawer = () => {
    setIsOpen(!isOpen);
    setClicked(null);
  };
  const handleTabChange = (tab) => {
    setActiveTab(tab);
    toggleDrawer();
    navigate('/profile'); // Navigate to profile page when a tab is selected
  };
  return (
    <div>
      <button className='lg:hidden z-[999] relative' onClick={toggleDrawer}>
        {isOpen ? <X /> : <Menu />}
      </button>

      <motion.div
        className='fixed left-0 right-0 top-16 overflow-y-auto h-full bg-[#0A2B42] backdrop-blur text-white p-6 pb-20 z-[998]'
        initial={{ x: '-100%' }}
        animate={{ x: isOpen ? '0%' : '-100%' }}
        transition={{ type: 'spring', stiffness: 300, damping: 30 }}
      >
        {/* User Profile Section */}
        {user && (
          <div className="space-y-2">
            <div className="flex items-center mb-6 p-4 bg-white/10 rounded-lg">
              <div className="w-10 h-10 rounded-full bg-gray-200 overflow-hidden mr-3">
                {user.image ? (
                  <img
                    src={user.image}
                    alt="Profile"
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
                <h3 className="font-medium text-white text-sm">{`${user.first_name} ${user.last_name}`}</h3>
                <Link to={'/profile'} className="text-xs text-gray-300">
                  @{user.username}
                </Link>
              </div>
            </div>
            {/* Sidebar Navigation Items */}
            <div className="space-y-2">
              {/* Profile Section */}
              <button
                onClick={() => handleTabChange('profile')}
                className={`flex items-center w-full px-4 py-3 rounded-md ${activeTab === 'profile' ? 'bg-white/20' : 'hover:bg-white/10'}`}
              >
                <UserIcon size={16} className="mr-3 text-gray-300" />
                <span className="text-sm">Profile Information</span>
              </button>

              {/* Social Links Section */}
              <button
                onClick={() => handleTabChange('social')}
                className={`flex items-center w-full px-4 py-3 rounded-md ${activeTab === 'social' ? 'bg-white/20' : 'hover:bg-white/10'}`}
              >
                <Share2Icon size={16} className="mr-3 text-gray-300" />
                <span className="text-sm">Social Links</span>
              </button>

              {/* Technologies Section */}
              <button
                onClick={() => handleTabChange('technologies')}
                className={`flex items-center w-full px-4 py-3 rounded-md ${activeTab === 'technologies' ? 'bg-white/20' : 'hover:bg-white/10'}`}
              >
                <CpuIcon size={16} className="mr-3 text-gray-300" />
                <span className="text-sm">Core Technologies</span>
              </button>

              {/* Contributions Section */}
              <button
                onClick={() => handleTabChange('contributions')}
                className={`flex items-center w-full px-4 py-3 rounded-md ${activeTab === 'contributions' ? 'bg-white/20' : 'hover:bg-white/10'}`}
              >
                <GitPullRequestIcon size={16} className="mr-3 text-gray-300" />
                <span className="text-sm">Contributions</span>
              </button>

              {/* Projects Section */}
              <button
                onClick={() => handleTabChange('projects')}
                className={`flex items-center w-full px-4 py-3 rounded-md ${activeTab === 'projects' ? 'bg-white/20' : 'hover:bg-white/10'}`}
              >
                <GitPullRequestIcon size={16} className="mr-3 text-gray-300" />
                <span className="text-sm">Projects</span>
              </button>

              {/* Articles Section */}
              <button
                onClick={() => handleTabChange('articles')}
                className={`flex items-center w-full px-4 py-3 rounded-md ${activeTab === 'articles' ? 'bg-white/20' : 'hover:bg-white/10'}`}
              >
                <BookOpenIcon size={16} className="mr-3 text-gray-300" />
                <span className="text-sm">Articles</span>
              </button>
            </div>
          </div>

        )}




        <ul className="mt-6 pt-4 border-t border-white/20">
          {Menus.map(({ name, path }, i) => {
            const isClicked = clicked === i;
            return (
              <li key={name} >
                <span
                  className='flex-center-between p-4 hover:bg-white/5 rounded-md cursor-pointer'
                  onClick={() => setClicked(isClicked ? null : i)}
                >
                  <a href={path}>{name}</a>
                </span>
              </li>
            );
          })}
        </ul>

        <div className="mt-6 border-t border-white/20 pt-4">
          {!user ? (
            <div className="space-y-3">
              <button
                onClick={() => {
                  toggleDrawer();
                  navigate('/login');
                }}
                className="w-full px-4 py-2 rounded bg-white text-[#0A2B42] font-semibold hover:bg-gray-200"
              >
                Log In
              </button>
              <button
                onClick={() => {
                  toggleDrawer();
                  navigate('/signup');
                }}
                className="w-full px-4 py-2 rounded border border-white text-white font-semibold hover:bg-white/10"
              >
                Sign Up
              </button>
            </div>
          ) : (
            <div className="relative">
              <button
                onClick={() => {
                  logout();
                  toggleDrawer();
                  navigate('/login');
                }}
                className="flex items-center w-full px-4 py-3 rounded-md text-red-400 hover:bg-white/10"
              >
                <LogOutIcon size={16} className="mr-3" />
                <span className="text-sm">Log out</span>
              </button>

            </div>
          )}
        </div>
      </motion.div>
    </div>
  );
}
