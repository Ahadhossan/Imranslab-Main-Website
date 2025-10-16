import { useState } from 'react';
import { PencilIcon, TrashIcon } from 'lucide-react';

const TechnologiesSection = ({ technologies, loading, error, onCreate, onUpdate, onDelete, showAlert }) => {
    const [editMode, setEditMode] = useState(false);
    const [newTech, setNewTech] = useState({
        technology: ''
    });
    const [editingId, setEditingId] = useState(null);

    const handleCreate = async () => {
        if (!newTech.technology.trim()) {
            showAlert('warning', 'Please enter a Technology');
            return;
        }
        try {
            await onCreate(newTech);
            setNewTech({ technology: '' });
            showAlert('success', 'Technology added successfully!');
            setEditMode(false);
        } catch (err) {
            console.error("Failed to create technology:", err);
        }
    };

    const handleUpdate = async () => {
        if (!newTech.technology.trim()) {
            showAlert('warning', 'Please enter a Technology');
            return;
        }
        try {
            await onUpdate(editingId, { technology: newTech.technology });
            showAlert('success', 'Technology successfully updated');
            setEditingId(null);
            setNewTech({ technology: '' });
            setEditMode(false); // Ensure the edit mode is reset after update
        } catch (err) {
            console.error("Failed to update technology:", err);
        }
    };

    if (loading) return <div>Loading technologies...</div>;
    if (error) return <div className="text-red-500">Error: {error.toString()}</div>;

    return (
        <div className="bg-white max-w-4xl mx-auto rounded-lg p-6 border border-gray-200">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-xl text-gray-600 font-bold">Core Technologies</h1>
                <button
                    onClick={() => {
                        setEditingId(null); // Reset editingId
                        setEditMode(!editMode); // Toggle edit mode
                    }}
                    className="bg-black text-white px-4 py-1.5 rounded-md text-sm"
                >
                    {editMode ? 'Cancel' : 'Add Technology'}
                </button>
            </div>

            {(editMode || editingId) && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg">
                    <div className="grid grid-cols-1 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Technology</label>
                            <input
                                type="text"
                                value={newTech.technology}
                                onChange={(e) => setNewTech({ ...newTech, technology: e.target.value })}
                                placeholder="e.g., React, Django, Python"
                                className="w-full p-2 text-gray-800 border border-gray-300 rounded-md"
                            />
                        </div>
                        <button
                            onClick={() => {
                                // Use handleUpdate if in edit mode, otherwise handleCreate
                                if (editingId) {
                                    handleUpdate();
                                } else {
                                    handleCreate();
                                }
                            }}
                            className="bg-blue-600 text-white px-4 py-2 rounded-md"
                        >
                            {editingId ? 'Update Technology' : 'Save Technology'}
                        </button>
                    </div>
                </div>
            )}

            <div className="space-y-4">
                {technologies.length === 0 ? (
                    <p className="text-gray-500">No technologies added yet.</p>
                ) : (
                    technologies.map(tech => (
                        <div key={tech.id} className="flex justify-between items-center p-4 border border-gray-200 rounded-lg">
                            <div>
                                <p className="font-medium text-gray-800 ">{tech.technology}</p>
                            </div>
                            <div className="flex space-x-2">
                                <button
                                    onClick={() => {
                                        // Set the technology to be edited
                                        setEditingId(tech.id);
                                        setNewTech({ technology: tech.technology });
                                        setEditMode(true); // Ensure we're in edit mode
                                    }}
                                    className="p-1 text-gray-500 hover:text-blue-600"
                                >
                                    <PencilIcon size={16} />
                                </button>
                                <button
                                    onClick={() => onDelete(tech.id)}
                                    className="p-1 text-gray-500 hover:text-red-600"
                                >
                                    <TrashIcon size={16} />
                                </button>
                            </div>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default TechnologiesSection;
