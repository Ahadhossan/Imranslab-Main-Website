const JobPosition = ({ editMode, formData, handleChange }) => {
    return (
        <section className="bg-white rounded-lg p-6 border border-gray-200">
            <h2 className="text-base font-medium mb-4 text-gray-600">Job Position</h2>
            <div className="space-y-4">
                <div>
                    <label htmlFor="position" className="block text-sm text-gray-800 mb-1">Position*</label>
                    <div className="flex items-center">
                        <div className="mr-2 text-gray-800">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="24"
                                height="24"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                className="lucide lucide-briefcase-business-icon lucide-briefcase-business"
                            >
                                <path d="M12 12h.01" />
                                <path d="M16 6V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2" />
                                <path d="M22 13a18.15 18.15 0 0 1-20 0" />
                                <rect width="20" height="14" x="2" y="6" rx="2" />
                            </svg>
                        </div>
                        {editMode ? (
                            <input
                                id="position"
                                type="text"
                                name="position"
                                value={formData.position || ''}
                                required
                                onChange={handleChange}
                                className="bg-gray-100 rounded-md px-3 py-2 text-sm w-full text-gray-800"
                            />
                        ) : (
                            <span className="text-sm text-gray-800">{formData.position || 'N/A'}</span>
                        )}
                    </div>
                </div>
            </div>
        </section>
    );
};

export default JobPosition;
