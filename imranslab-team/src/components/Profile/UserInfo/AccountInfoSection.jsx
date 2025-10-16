export const AccountInfoSection = ({ editMode, formData, handleChange }) => {
    return (
        <section className="bg-white rounded-lg p-6 border border-gray-200">
            <h2 className="text-base font-medium mb-4 text-gray-600">Account Information</h2>
            <div className="space-y-4">
                <div>
                    <label className="block text-sm text-gray-800 mb-1">First Name*</label>
                    <div className="flex items-center">
                        <div className="mr-2 text-gray-800">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                            >
                                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                                <circle cx="12" cy="7" r="4" />
                            </svg>
                        </div>
                        {editMode ? (
                            <input
                                type="text"
                                name="first_name"
                                value={formData.first_name || ''}
                                required
                                onChange={handleChange}
                                className="bg-gray-100 rounded-md px-3 py-2 text-sm w-full text-gray-800"
                            />
                        ) : (
                            <span className="text-sm text-gray-800">{formData.first_name || ''}</span>
                        )}
                    </div>
                </div>
                <div>
                    <label className="block text-sm text-gray-800 mb-1">Last Name*</label>
                    <div className="flex items-center">
                        <div className="mr-2 text-gray-800">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                            >
                                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                                <circle cx="12" cy="7" r="4" />
                            </svg>
                        </div>
                        {editMode ? (
                            <input
                                type="text"
                                name="last_name"
                                required
                                value={formData.last_name || ''}
                                onChange={handleChange}
                                className="bg-gray-100 rounded-md px-3 py-2 text-sm w-full text-gray-800"
                            />
                        ) : (
                            <span className="text-sm text-gray-800">{formData.last_name || ''}</span>
                        )}
                    </div>
                </div>
                <div>
                    <label className="block text-sm text-gray-800 mb-1">Username*</label>
                    <div className="flex items-center">
                        <div className="mr-2 text-gray-800">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                            >
                                <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2" />
                                <circle cx="12" cy="7" r="4" />
                            </svg>
                        </div>
                        {editMode ? (
                            <input
                                type="text"
                                name="username"
                                required
                                value={formData.username || ''}
                                onChange={handleChange}
                                className="bg-gray-100 text-gray-800 rounded-md px-3 py-2 text-sm w-full"
                            />
                        ) : (
                            <span className="text-sm text-gray-800">{formData.username || ''}</span>
                        )}
                    </div>
                </div>
                <div>
                    <label className="block text-sm text-gray-800 mb-1">Email*</label>
                    <div className="flex items-center">
                        <div className="mr-2 text-gray-800">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                            >
                                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                                <polyline points="22,6 12,13 2,6" />
                            </svg>
                        </div>
                        {editMode ? (
                            <input
                                type="email"
                                name="email"
                                required
                                value={formData.email || ''}
                                onChange={handleChange}
                                className="bg-gray-100 text-gray-800 rounded-md px-3 py-2 text-sm w-full"
                            />
                        ) : (
                            <span className="text-sm text-gray-800">{formData.email || ''}</span>
                        )}
                    </div>
                </div>
            </div>
        </section>
    )
}