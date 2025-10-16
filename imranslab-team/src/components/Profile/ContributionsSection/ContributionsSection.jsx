import { useState } from 'react';
import { PencilIcon, TrashIcon } from 'lucide-react';

const ContributionsSection = ({ contributions, loading, error, onCreate, onUpdate, onDelete, showAlert }) => {
    const [editMode, setEditMode] = useState(false);
    const [editingId, setEditingId] = useState(null);
    const [newContribution, setNewContribution] = useState({
        keys: ''
    });

    const handleCreate = async () => {
        if (!newContribution.keys.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Contribution');
            return;
        }
        try {
            await onCreate(newContribution);
            setNewContribution({ keys: '' });
            showAlert('success', 'Contribution added successfully!');
            setEditMode(false);
        } catch (err) {
            console.error("Failed to create contribution:", err);
        }
    };

    const handleUpdate = async () => {
        if (!newContribution.keys.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Contribution');
            return;
        }
        try {
            await onUpdate(editingId, { keys: newContribution.keys });
            setEditingId(null);
            setNewContribution({ keys: '' });
            showAlert('success', 'Contribution successfully updated');
        } catch (err) {
            console.error("Failed to update contribution:", err);
        }
    };

    const handleCancelUpdate = () => {
        setEditingId(null);
        setNewContribution({ keys: '' });
        setEditMode(false);
    };

    if (loading) return <div>Loading contributions...</div>;
    if (error) return <div className="text-red-500">Error: {error.toString()}</div>;

    return (
        <div className="bg-white max-w-4xl mx-auto rounded-lg p-6 border border-gray-200">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-xl text-gray-800 font-bold">Contributions</h1>
                <button
                    onClick={() => {
                        setEditingId(null);
                        setEditMode(!editMode);
                    }}
                    className="bg-black text-white px-4 py-1.5 rounded-md text-sm"
                >
                    {editMode ? 'Cancel' : 'Add Contribution'}
                </button>
            </div>

            {(editMode || editingId) && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg">
                    <div className="grid grid-cols-1 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Contribution Details</label>
                            <textarea
                                value={newContribution.keys}
                                onChange={(e) => setNewContribution({ ...newContribution, keys: e.target.value })}
                                placeholder="Describe your contributions (comma separated)"
                                className="w-full p-2 text-gray-800 border border-gray-300 rounded-md"
                                rows={3}
                            />
                        </div>
                        <button
                            onClick={() => editingId ?
                                handleUpdate() :
                                handleCreate()}
                            className="bg-blue-600 text-white px-4 py-2 rounded-md"
                        >
                            {editingId ? 'Update Contribution' : 'Save Contribution'}
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

            <div className="grid grid-cols-1 gap-6">
                {contributions.length === 0 ? (
                    <p className="text-gray-500">No contributions added yet.</p>
                ) : (
                    contributions.map(contribution => (
                        <div key={contribution.id} className="p-4 border border-gray-200 rounded-lg shadow-md">
                            <div className="flex justify-between items-start mb-2">
                                <div>
                                    <h3 className="font-medium text-gray-800">Contribution</h3>
                                    <ul className="list-disc list-inside text-sm text-gray-800">
                                        {contribution.keys.split(',').map((key, i) => (
                                            <li key={i}>{key.trim()}</li>
                                        ))}
                                    </ul>
                                </div>
                                <div className="flex space-x-2">
                                    <button
                                        onClick={() => {
                                            setEditingId(contribution.id);
                                            setNewContribution({ keys: contribution.keys });
                                            setEditMode(false);
                                        }}
                                        className="p-1 text-gray-500 hover:text-blue-600"
                                    >
                                        <PencilIcon size={16} />
                                    </button>
                                    <button
                                        onClick={() => {
                                            onDelete(contribution.id)
                                            showAlert('info', 'Contribution deleted successfully!');
                                        }}
                                        className="p-1 text-gray-500 hover:text-red-600"
                                    >
                                        <TrashIcon size={16} />
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))
                )}
            </div>
        </div >
    );
};

export default ContributionsSection;
