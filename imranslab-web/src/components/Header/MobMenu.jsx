/** @format */

import { motion } from 'framer-motion';
import {  Menu, X } from 'lucide-react';
import { useState } from 'react';

export default function MobMenu({ Menus }) {
  const [isOpen, setIsOpen] = useState(false);
  const [clicked, setClicked] = useState(null);
  const toggleDrawer = () => {
    setIsOpen(!isOpen);
    setClicked(null);
  };


  return (
    <div>
      <button className='lg:hidden z-[999] relative' onClick={toggleDrawer}>
        {isOpen ? <X /> : <Menu />}
      </button>

      <motion.div
        className='fixed left-0 right-0 top-16 overflow-y-auto h-full bg-[#0A2B42] backdrop-blur text-white p-6 pb-20'
        initial={{ x: '-100%' }}
        animate={{ x: isOpen ? '0%' : '-100%' }}>
        <ul>
          {Menus.map(({ name, path }, i) => {
            const isClicked = clicked === i;
            return (
              <li key={name} className=''>
                <span
                  className='flex-center-between p-4 hover:bg-white/5 rounded-md cursor-pointer relative'
                  onClick={() => setClicked(isClicked ? null : i)}>
                  <a href={path}>{name}</a>
                </span>
              </li>
            );
          })}
        </ul>
      </motion.div>
    </div>
  );
}
