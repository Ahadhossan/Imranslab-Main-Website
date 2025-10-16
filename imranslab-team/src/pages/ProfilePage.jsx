import { useState, useEffect, useRef } from 'react';
import Sidebar from "../components/Profile/Sidebar";
import { ProfileContent } from "../components/Profile/ProfileContent";
import useUserInfo from "../hooks/useUserInfo";
import useSocialMediaLinks from "../hooks/useSocialMediaLinks";
import useCoreTechnologies from "../hooks/useCoreTechnologies";
import useProjectsContributed from "../hooks/useProjectsContributed";
import useArticles from "../hooks/useArticles";
import useContributions from "../hooks/useContributions";
import Loader from '../Helper/Loader';
import Alert from '../Helper/Alert';

import SocialLinksSection from '../components/Profile/SocialLinksSection/SocialLinksSection';
import TechnologiesSection from '../components/Profile/TechnologiesSection/TechnologiesSection';
import ProjectsSection from '../components/Profile/ProjectsSection/ProjectsSection';
import ArticlesSection from '../components/Profile/ArticlesSection/ArticlesSection';
import ContributionsSection from '../components/Profile/ContributionsSection/ContributionsSection';
import { useActiveTab } from '../context/ActiveTabContext';


const ProfilePage = () => {
    const { activeTab, setActiveTab } = useActiveTab();
    const [editMode, setEditMode] = useState(false);
    const [formData, setFormData] = useState({});
    const [imagePreview, setImagePreview] = useState(null);
    const fileInputRef = useRef(null);
    const [alert, setAlert] = useState(null);
    const {
        userId,
        userData,
        loading: userLoading,
        error: userError,
        fetchUser,
        updateUser
    } = useUserInfo();

    const {
        links: socialLinks,
        loading: linksLoading,
        error: linksError,
        fetchLinks,
        createLink,
        updateLink,
        deleteLink
    } = useSocialMediaLinks();

    const {
        technologies,
        loading: techLoading,
        error: techError,
        fetchTechnologies,
        createTechnology,
        updateTechnology,
        deleteTechnology
    } = useCoreTechnologies();

    const {
        projects,
        loading: projectsLoading,
        error: projectsError,
        fetchProjects,
        createProject,
        updateProject,
        deleteProject
    } = useProjectsContributed();

    const {
        articles,
        loading: articlesLoading,
        error: articlesError,
        fetchArticles,
        createArticle,
        updateArticle,
        deleteArticle
    } = useArticles();

    const {
        contributions,
        loading: contributionsLoading,
        error: contributionsError,
        fetchContributions,
        createContribution,
        updateContribution,
        deleteContribution
    } = useContributions();

    useEffect(() => {
        if (userData) {
            setFormData(userData);
            if (userData.image) {
                setImagePreview(userData.image);
            }
        }
    }, [userData]);

    useEffect(() => {
        if (userId) {
            fetchUser();
            fetchLinks();
            fetchTechnologies();
            fetchProjects();
            fetchArticles();
            fetchContributions();
        }
    }, [userId, fetchUser, fetchLinks, fetchTechnologies, fetchProjects, fetchArticles, fetchContributions]);

    // Add this function to show alerts
    const showAlert = (type, message, duration = 5000) => {
        setAlert({ type, message });
        if (duration) {
            setTimeout(() => setAlert(null), duration);
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
    };

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setImagePreview(reader.result);
            };
            reader.readAsDataURL(file);
            setFormData(prev => ({ ...prev, image: file }));
        }
    };

    const handleRemoveImage = () => {
        setImagePreview(null);
        setFormData(prev => ({ ...prev, image: null }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        // List of fields that cannot be empty
        const requiredFields = [
            'first_name',
            'last_name',
            'personalinterests',
            'aboutme',
            'email',
            'position',
            'address',
            'phone'
        ];

        // Check for empty required fields
        const emptyFields = requiredFields.filter(field => {
            const value = formData[field];
            return !value || (typeof value === 'string' && value.trim() === '');
        });

        if (emptyFields.length > 0) {
            showAlert('error', `These fields cannot be empty: ${emptyFields.join(', ')}`);
            return;
        }

        // Validate email format
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
            showAlert('error', 'Please enter a valid email address');
            return;
        }

        // Validate phone number format (adjust regex as needed)
        if (!/^[\d\s\-()+]{10,20}$/.test(formData.phone)) {
            showAlert('error', 'Please enter a valid phone number (10-20 digits)');
            return;
        }

        // Prepare form data for submission
        const formDataToSend = new FormData();

        Object.keys(formData).forEach(key => {
            if (formData[key] !== null && formData[key] !== undefined) {
                if (key === 'image') {
                    if (formData[key] instanceof File || formData[key] === null) {
                        formDataToSend.append(key, formData[key]);
                    }
                } else {
                    // Trim string values before sending
                    const value = typeof formData[key] === 'string'
                        ? formData[key].trim()
                        : formData[key];
                    formDataToSend.append(key, value);
                }
            }
        });

        try {
            await updateUser(formDataToSend);
            setEditMode(false);
            fetchUser();
            showAlert('success', 'Profile updated successfully!');
        } catch (err) {
            console.error("Update failed:", err);
            showAlert('error', 'Failed to update profile. Please try again.');
        }
    };


    const isLoading = userLoading || linksLoading || techLoading || projectsLoading || articlesLoading || contributionsLoading;

    if (isLoading) return <Loader />;
    if (userError) return <div className="text-red-500 p-4">Error: {userError.toString()}</div>;

    return (
        <div className="w-full bg-gray-50 pt-16">
            {alert && (
                <Alert
                    type={alert.type}
                    message={alert.message}
                    onClose={() => setAlert(null)}
                />
            )}
            <div className="flex flex-col md:flex-row flex-1 mx-auto">
                <Sidebar
                    userData={userData}
                    activeTab={activeTab}
                    setActiveTab={setActiveTab}
                />
                <main className="flex-1 p-4 md:p-6">
                    {activeTab === 'profile' && (
                        <ProfileContent
                            editMode={editMode}
                            setEditMode={setEditMode}
                            formData={formData}
                            handleChange={handleChange}
                            handleSubmit={handleSubmit}
                            imagePreview={imagePreview}
                            handleImageChange={handleImageChange}
                            handleRemoveImage={handleRemoveImage}
                            fileInputRef={fileInputRef}
                            userData={userData}
                        />
                    )}
                    {activeTab === 'social' && (
                        <SocialLinksSection
                            links={socialLinks}
                            loading={linksLoading}
                            error={linksError}
                            onCreate={createLink}
                            onUpdate={updateLink}
                            onDelete={deleteLink}
                            showAlert={showAlert}
                        />
                    )}
                    {activeTab === 'technologies' && (
                        <TechnologiesSection
                            technologies={technologies}
                            loading={techLoading}
                            error={techError}
                            onCreate={createTechnology}
                            onUpdate={updateTechnology}
                            onDelete={deleteTechnology}
                            showAlert={showAlert}
                        />
                    )}
                    {activeTab === 'projects' && (
                        <ProjectsSection
                            projects={projects}
                            loading={projectsLoading}
                            error={projectsError}
                            onCreate={createProject}
                            onUpdate={updateProject}
                            onDelete={deleteProject}
                            showAlert={showAlert}
                        />
                    )}
                    {activeTab === 'articles' && (
                        <ArticlesSection
                            articles={articles}
                            loading={articlesLoading}
                            error={articlesError}
                            onCreate={createArticle}
                            onUpdate={updateArticle}
                            onDelete={deleteArticle}
                            showAlert={showAlert}
                        />
                    )}
                    {activeTab === 'contributions' && (
                        <ContributionsSection
                            contributions={contributions}
                            loading={contributionsLoading}
                            error={contributionsError}
                            onCreate={createContribution}
                            onUpdate={updateContribution}
                            onDelete={deleteContribution}
                            showAlert={showAlert}
                        />
                    )}
                </main>
            </div>
        </div>
    );
};

export default ProfilePage;
