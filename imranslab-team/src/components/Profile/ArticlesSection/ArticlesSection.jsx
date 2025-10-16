import { useState } from 'react';
import { PencilIcon, TrashIcon } from 'lucide-react';

const ArticlesSection = ({ articles, loading, error, onCreate, onUpdate, onDelete, showAlert }) => {
    const APICLIENT = import.meta.env.VITE_APICLIENT || "https://imranslab-team.imranslab.org/"
    const [editMode, setEditMode] = useState(false);
    const [editingId, setEditingId] = useState(null);
    const [newArticle, setNewArticle] = useState({
        title: '',
        description: '',
        articlelink: '',
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
            setNewArticle(prev => ({ ...prev, image: file }));
        }
    };

    const handleCreate = async () => {
        if (!newArticle.title.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Title');
            return;
        } else if (!newArticle.description.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Description');
            return;
        } else if (!newArticle.articlelink.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Article Link');
            return;
        }
        try {
            await onCreate(newArticle);
            setNewArticle({
                title: '',
                description: '',
                articlelink: '',
                image: null
            });
            showAlert('success', 'New Article added successfully!');
            setImagePreview(null);
            setEditMode(false);
        } catch (err) {
            console.error("Failed to create article:", err);
        }
    };

    const handleUpdate = async () => {
        if (!newArticle.title.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Title');
            return;
        } else if (!newArticle.description.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Description');
            return;
        } else if (!newArticle.articlelink.trim()) {  // Check if link is empty
            showAlert('warning', 'Please enter a Article Link');
            return;
        }
        try {
            await onUpdate(editingId, newArticle);
            setEditingId(null);
            setNewArticle({
                title: '',
                description: '',
                articlelink: '',
                image: null
            });
            showAlert('success', 'Article updated successfully!');
            setImagePreview(null);
        } catch (err) {
            console.error("Failed to update article:", err);
        }
    };

    const handleCancelUpdate = () => {
        setEditingId(null);
        setNewArticle({
            title: '',
            description: '',
            articlelink: '',
            image: null
        });
        setImagePreview(null);
        setEditMode(false);
    };

    if (loading) return <div>Loading articles...</div>;
    if (error) return <div className="text-red-500">Error: {error.toString()}</div>;

    return (
        <div className="bg-white max-w-4xl mx-auto rounded-lg p-6 border border-gray-200">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-xl text-gray-600 font-bold">Articles</h1>
                <button
                    onClick={() => {
                        setEditingId(null);
                        setEditMode(!editMode);
                    }}
                    className="bg-black text-white px-4 py-1.5 rounded-md text-sm"
                >
                    {editMode ? 'Cancel' : 'Add Article'}
                </button>
            </div>

            {(editMode || editingId) && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg">
                    <div className="grid grid-cols-1 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Title</label>
                            <input
                                type="text"
                                value={newArticle.title}
                                onChange={(e) => setNewArticle({ ...newArticle, title: e.target.value })}
                                placeholder="Article Title"
                                className="w-full p-2 text-gray-800 border border-gray-300 rounded-md"
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Description</label>
                            <textarea
                                value={newArticle.description}
                                onChange={(e) => setNewArticle({ ...newArticle, description: e.target.value })}
                                className="w-full p-2 border text-gray-800 border-gray-300 rounded-md"
                                rows={3}
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Article Link</label>
                            <input
                                type="text"
                                value={newArticle.articlelink}
                                onChange={(e) => setNewArticle({ ...newArticle, articlelink: e.target.value })}
                                placeholder="https://medium.com/your-article"
                                className="w-full text-gray-800 p-2 border border-gray-300 rounded-md"
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Featured Image</label>
                            <input
                                type="file"
                                onChange={handleImageChange}
                                className="w-full text-gray-800 p-2 border border-gray-300 rounded-md"
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
                            {editingId ? 'Update Article' : 'Save Article'}
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
                {articles.length === 0 ? (
                    <p className="text-gray-500">No articles added yet.</p>
                ) : (
                    articles.map(article => (
                        <div key={article.id} className="p-4 border border-gray-200 rounded-lg shadow-md">

                            {article.image && (
                                <div className="mb-2">
                                    <img
                                        src={APICLIENT + article.image}
                                        alt="Article"
                                        className="h-32 w-full object-cover rounded"
                                    />
                                </div>
                            )}
                            <div className="flex justify-between items-start mb-2">
                                <h3 className="font-medium text-gray-800">{article.title}</h3>
                                <div className="flex space-x-2">
                                    <button
                                        onClick={() => {
                                            setEditingId(article.id);
                                            setNewArticle({
                                                title: article.title,
                                                description: article.description,
                                                articlelink: article.articlelink,
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
                                            onDelete(article.id)
                                            showAlert('info', 'Article deleted successfully!');
                                        }}
                                        className="p-1 text-gray-500 hover:text-red-600"
                                    >
                                        <TrashIcon size={16} />
                                    </button>
                                </div>
                            </div>
                            <p className="text-sm mb-2 text-gray-800 line-clamp-3">{article.description}</p>
                            <a
                                href={article.articlelink}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="text-blue-600 text-sm"
                            >
                                Read Article
                            </a>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default ArticlesSection;
