export const ContactInformation = ({ editMode, formData, handleChange }) => {
    return (
        <section className="bg-white rounded-lg p-6 border border-gray-200">
            <h2 className="text-base font-medium mb-4 text-gray-600">Contact Information</h2>
            <div className="space-y-4">
                <div>
                    <label className="block text-sm text-gray-800 mb-1">Phone*</label>
                    <div className="flex items-center">
                        <div className="mr-2 text-gray-800">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"
                                className="lucide lucide-phone-call-icon lucide-phone-call">
                                <path d="M13 2a9 9 0 0 1 9 9" />
                                <path d="M13 6a5 5 0 0 1 5 5" />
                                <path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384" />
                            </svg>
                        </div>
                        {editMode ? (
                            <input
                                type="text"
                                name="phone"
                                value={formData.phone || ''}
                                required
                                onChange={handleChange}
                                className="bg-gray-100 rounded-md px-3 py-2 text-sm w-full text-gray-800"
                            />
                        ) : (
                            <span className="text-sm text-gray-800">{formData.phone || 'Not specified'}</span>
                        )}
                    </div>
                </div>
                <div>
                    <label className="block text-sm text-gray-800 mb-1">Address*</label>
                    <div className="flex items-center">
                        <div className="mr-2 text-gray-800">
                            <svg
                                width="16"
                                height="16"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                className="lucide lucide-map-pin-icon lucide-map-pin">
                                <path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0" />
                                <circle cx="12" cy="10" r="3" />
                            </svg>
                        </div>
                        {editMode ? (
                            <input
                                type="text"
                                name="address"
                                required
                                value={formData.address || ''}
                                onChange={handleChange}
                                className="bg-gray-100 rounded-md px-3 py-2 text-sm w-full text-gray-800"
                            />
                        ) : (
                            <span className="text-sm text-gray-800">{formData.address || 'Not specified'}</span>
                        )}
                    </div>
                </div>
                <div>
                    <label className="block text-sm text-gray-800 mb-1">Birth Date</label>
                    <div className="flex items-center">
                        <div className="mr-2 text-gray-800">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                className="lucide lucide-calendar-icon lucide-calendar">
                                <path d="M8 2v4" /><path d="M16 2v4" />
                                <rect width="18" height="18" x="3" y="4" rx="2" /><path d="M3 10h18" />
                            </svg>
                        </div>
                        {editMode ? (
                            <input
                                type="date"
                                name="birth_date"
                                value={formData.birth_date || ''}
                                onChange={handleChange}
                                className="bg-gray-100 text-gray-800 rounded-md px-3 py-2 text-sm w-full"
                            />
                        ) : (
                            <span className="text-sm text-gray-800">{formData.birth_date || 'Not specified'}</span>
                        )}
                    </div>
                </div>
            </div>
        </section>
    )
}