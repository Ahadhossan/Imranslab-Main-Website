/* eslint-disable react-refresh/only-export-components */
// contexts/ActiveTabContext.js
import { createContext, useContext, useState } from 'react';

const ActiveTabContext = createContext();

export const ActiveTabProvider = ({ children }) => {
    const [activeTab, setActiveTab] = useState('profile');

    return (
        <ActiveTabContext.Provider value={{ activeTab, setActiveTab }}>
            {children}
        </ActiveTabContext.Provider>
    );
};

export const useActiveTab = () => {
    return useContext(ActiveTabContext);
};