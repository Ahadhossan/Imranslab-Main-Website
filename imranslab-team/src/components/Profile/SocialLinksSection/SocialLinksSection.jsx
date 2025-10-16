import { useState } from 'react';
import { PencilIcon, TrashIcon, SaveIcon, XIcon } from 'lucide-react';

const SocialLinksSection = ({ links, loading, error, onCreate, onUpdate, onDelete, showAlert }) => {
    const [editMode, setEditMode] = useState(false);
    const [newLink, setNewLink] = useState({ link: '', socialmediachoice: 'github' });
    const [editingLinkId, setEditingLinkId] = useState(null);
    const [editedLink, setEditedLink] = useState({});

    const handleCreate = async () => {
        if (!newLink.link.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a URL');
            return;
        }
        try {
            await onCreate(newLink);
            setNewLink({ link: '', socialmediachoice: 'github' });
            showAlert('success', 'Social link added successfully!');
            setEditMode(false);
        } catch (err) {
            console.error("Failed to create link:", err);
        }
    };

    const handleUpdate = async () => {
        if (!editedLink.link.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a URL');
            return;
        }

        try {
            await onUpdate(editingLinkId, editedLink);
            showAlert('success', 'Social link successfully updated');
            setEditingLinkId(null);
            setEditedLink({});
        } catch (err) {
            console.error("Failed to update link:", err);
        }
    };

    if (loading) return <div>Loading social links...</div>;
    if (error) return <div className="text-red-500">Error: {error.toString()}</div>;

    return (
        <div className="bg-white rounded-lg max-w-4xl mx-auto p-6 border border-gray-200">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-xl text-gray-600 font-bold">Social Media Links</h1>
                <button
                    onClick={() => setEditMode(!editMode)}
                    className="bg-black text-white px-4 py-1.5 rounded-md text-sm"
                >
                    {editMode ? 'Cancel' : 'Add Link'}
                </button>
            </div>

            {editMode && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg">
                    <div className="grid grid-cols-1 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Platform</label>
                            <select
                                value={newLink.socialmediachoice}
                                onChange={(e) =>
                                    setNewLink({ ...newLink, socialmediachoice: e.target.value })
                                }
                                className="w-full text-gray-800 p-2 border border-gray-300 rounded-md"
                            >
                                <option value="github">GitHub</option>
                                <option value="linkedin">LinkedIn</option>
                                <option value="facebook">Facebook</option>
                                <option value="x">X (Twitter)</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">URL</label>
                            <input
                                type="text"
                                value={newLink.link}
                                onChange={(e) =>
                                    setNewLink({ ...newLink, link: e.target.value })
                                }
                                placeholder="https://example.com"
                                className="w-full p-2 border text-gray-800 border-gray-300 rounded-md"
                            />
                        </div>
                        <button
                            onClick={handleCreate}
                            className="bg-blue-600 text-white px-4 py-2 rounded-md"
                        >
                            Save Link
                        </button>
                    </div>
                </div>
            )}

            <div className="space-y-4">
                {links.length === 0 ? (
                    <p className="text-gray-500">No social links added yet.</p>
                ) : (
                    links.map((link) => {
                        const isEditing = editingLinkId === link.id;
                        return (
                            <div
                                key={link.id}
                                className="flex justify-between items-center p-4 border border-gray-200 rounded-lg"
                            >
                                <div className="w-full">
                                    {isEditing ? (
                                        <div className="grid grid-cols-1 gap-2">
                                            <select
                                                value={editedLink.socialmediachoice}
                                                onChange={(e) =>
                                                    setEditedLink({
                                                        ...editedLink,
                                                        socialmediachoice: e.target.value,
                                                    })
                                                }
                                                className="text-gray-800 p-2 border border-gray-300 rounded-md"
                                            >
                                                <option value="github">GitHub</option>
                                                <option value="linkedin">LinkedIn</option>
                                                <option value="facebook">Facebook</option>
                                                <option value="x">X (Twitter)</option>
                                                <option value="other">Other</option>
                                            </select>
                                            <input
                                                type="text"
                                                value={editedLink.link}
                                                onChange={(e) =>
                                                    setEditedLink({ ...editedLink, link: e.target.value })
                                                }
                                                className="p-2 border border-gray-300 rounded-md text-gray-800 "
                                            />
                                        </div>
                                    ) : (
                                        <div>
                                            <p className="font-medium capitalize text-gray-800">
                                                {link.socialmediachoice}
                                            </p>
                                            <a
                                                href={link.link}
                                                target="_blank"
                                                rel="noopener noreferrer"
                                                className="text-blue-600 text-sm"
                                            >
                                                {link.link}
                                            </a>
                                        </div>
                                    )}
                                </div>
                                <div className="flex space-x-2 ml-4">
                                    {isEditing ? (
                                        <>
                                            <button
                                                onClick={handleUpdate}
                                                className="p-1 text-green-600 hover:text-green-800"
                                            >
                                                <SaveIcon size={16} />
                                            </button>
                                            <button
                                                onClick={() => {
                                                    setEditingLinkId(null);
                                                    setEditedLink({});
                                                }}
                                                className="p-1 text-gray-500 hover:text-red-600"
                                            >
                                                <XIcon size={16} />
                                            </button>
                                        </>
                                    ) : (
                                        <>
                                            <button
                                                onClick={() => {
                                                    setEditingLinkId(link.id);
                                                    setEditedLink(link);
                                                }}
                                                className="p-1 text-gray-500 hover:text-blue-600"
                                            >
                                                <PencilIcon size={16} />
                                            </button>
                                            <button
                                                onClick={() => {
                                                    onDelete(link.id)
                                                    showAlert('info', 'SocialMedia  Links Deleted successfully')
                                                }
                                                }
                                                className="p-1 text-gray-500 hover:text-red-600"
                                            >
                                                <TrashIcon size={16} />
                                            </button>
                                        </>
                                    )}
                                </div>
                            </div>
                        );
                    })
                )}
            </div>
        </div>
    );
};

export default SocialLinksSection;
