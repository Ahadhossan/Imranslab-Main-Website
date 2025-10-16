import { useState } from 'react';
import { PencilIcon, TrashIcon } from 'lucide-react';

const ProjectsSection = ({ projects, loading, error, onCreate, onUpdate, onDelete, showAlert }) => {
    const APICLIENT = import.meta.env.VITE_APICLIENT || "https://imranslab-team.imranslab.org/"
    const [editMode, setEditMode] = useState(false);
    const [editingId, setEditingId] = useState(null);
    const [newProject, setNewProject] = useState({
        technologies: '',
        description: '',
        projectlink: '',
        role: 'intern',
        image: null
    });
    const [imagePreview, setImagePreview] = useState(null);

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setImagePreview(reader.result);
            };
            reader.readAsDataURL(file);
            setNewProject(prev => ({ ...prev, image: file }));
        }
    };

    const handleCreate = async () => {
        if (!newProject.technologies.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Technologies');
            return;
        } else if (!newProject.description.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Description');
            return;
        } else if (!newProject.projectlink.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Project Link');
            return;
        }
        try {
            await onCreate(newProject);
            setNewProject({
                technologies: '',
                description: '',
                projectlink: '',
                role: 'intern',
                image: null
            });
            showAlert('success', 'New Project added successfully!');
            setImagePreview(null);
            setEditMode(false);
        } catch (err) {
            console.error("Failed to create project:", err);
        }
    };

    const handleUpdate = async () => {
        if (!newProject.technologies.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter Technologies');
            return;
        } else if (!newProject.description.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Description');
            return;
        } else if (!newProject.projectlink.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Project Link');
            return;
        }
        try {
            await onUpdate(editingId, newProject);
            setEditingId(null);
            setNewProject({
                technologies: '',
                description: '',
                projectlink: '',
                role: 'intern',
                image: null
            });
            showAlert('success', ' Project Update successfully!');
            setImagePreview(null);
        } catch (err) {
            console.error("Failed to update project:", err);
        }
    };

    const handleCancelUpdate = () => {
        setEditingId(null);
        setNewProject({
            technologies: '',
            description: '',
            projectlink: '',
            role: 'intern',
            image: null
        });
        setImagePreview(null);
    };

    if (loading) return <div>Loading projects...</div>;
    if (error) return <div className="text-red-500">Error: {error.toString()}</div>;

    return (
        <div className="bg-white max-w-4xl mx-auto rounded-lg p-6 border border-gray-200">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-xl text-gray-600 font-bold">Projects Contributed To</h1>
                <button
                    onClick={() => {
                        setEditingId(null);
                        setEditMode(!editMode);
                    }}
                    className="bg-black text-white px-4 py-1.5 rounded-md text-sm"
                >
                    {editMode ? 'Cancel' : 'Add Project'}
                </button>
            </div>

            {(editMode || editingId) && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg">
                    <div className="grid grid-cols-1 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Technologies</label>
                            <input
                                type="text"
                                value={newProject.technologies}
                                onChange={(e) => setNewProject({ ...newProject, technologies: e.target.value })}
                                placeholder="React, Django, PostgreSQL"
                                className="w-full p-2 border border-gray-300 text-gray-800 rounded-md"
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Description</label>
                            <textarea
                                value={newProject.description}
                                onChange={(e) => setNewProject({ ...newProject, description: e.target.value })}
                                className="w-full p-2 border text-gray-800 border-gray-300 rounded-md"
                                rows={3}
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Project Link</label>
                            <input
                                type="text"
                                value={newProject.projectlink}
                                onChange={(e) => setNewProject({ ...newProject, projectlink: e.target.value })}
                                placeholder="https://github.com/your-project"
                                className="w-full text-gray-800 p-2 border border-gray-300 rounded-md"
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Role</label>
                            <select
                                value={newProject.role}
                                onChange={(e) => setNewProject({ ...newProject, role: e.target.value })}
                                className="w-full text-gray-800  p-2 border border-gray-300 rounded-md"
                            >
                                <option value="intern">Intern</option>
                                <option value="developer">Developer</option>
                                <option value="contributor">Contributor</option>
                            </select>
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Project Image</label>
                            <input
                                type="file"
                                onChange={handleImageChange}
                                className="w-full p-2 text-gray-800 border border-gray-300 rounded-md"
                                accept="image/*"
                            />
                            {imagePreview && (
                                <div className="mt-2">
                                    <img src={imagePreview} alt="Preview" className="h-20 w-auto rounded" />
                                </div>
                            )}
                        </div>

                        <button
                            onClick={() => editingId ? handleUpdate() : handleCreate()}
                            className="bg-blue-600 text-white px-4 py-2 rounded-md"
                        >
                            {editingId ? 'Update Project' : 'Save Project'}
                        </button>
                        {editingId && (
                            <button
                                onClick={handleCancelUpdate}
                                className="bg-gray-500 text-white px-4 py-2 rounded-md ml-2"
                            >
                                Cancel Update
                            </button>
                        )}
                    </div>
                </div>
            )}

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {projects.length === 0 ? (
                    <p className="text-gray-500">No projects added yet.</p>
                ) : (
                    projects.map(project => (
                        <div key={project.id} className="p-4 border border-gray-200 rounded-lg shadow-md">
                            <div className="flex justify-between items-start mb-2">
                                <div>
                                    <p className="text-md font-semibold text-gray-600">{project.technologies}</p>
                                </div>
                                <div className="flex space-x-2">
                                    <button
                                        onClick={() => {
                                            setEditingId(project.id);
                                            setNewProject({
                                                technologies: project.technologies,
                                                description: project.description,
                                                projectlink: project.projectlink,
                                                role: project.role,
                                                image: null
                                            });
                                            setEditMode(false);
                                        }}
                                        className="p-1 text-gray-500 hover:text-blue-600"
                                    >
                                        <PencilIcon size={16} />
                                    </button>
                                    <button
                                        onClick={() => {
                                            onDelete(project.id)
                                            showAlert('info', 'Project Deleted successfully')
                                        }}
                                        className="p-1 text-gray-500 hover:text-red-600"
                                    >
                                        <TrashIcon size={16} />
                                    </button>
                                </div>
                            </div>
                            {project.image && (
                                <div className="mb-2">
                                    <img
                                        src={APICLIENT + project.image}
                                        alt="Project"
                                        className="h-32 w-full object-cover rounded"
                                    />
                                </div>
                            )}
                            <p className="text-sm mb-2 text-gray-800 line-clamp-3">{project.description}</p>
                            <a
                                href={project.projectlink}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="text-blue-600 text-sm"
                            >
                                View Project
                            </a>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default ProjectsSection;
