export const PersonalInterests = ({ editMode, formData, handleChange }) => {
    return (
        <section className="bg-white rounded-lg p-6 border border-gray-200">
            <h2 className="text-base font-medium mb-4 text-gray-800">Personal Interests</h2>
            <div className="space-y-4">
                <div>
                    <label className="block text-sm text-gray-600 mb-1">Your Personal Interests*</label>
                    <div className="relative">
                        {editMode ? (
                            <>
                                <textarea
                                    name="personalinterests"
                                    value={formData.personalinterests || ''}
                                    onChange={handleChange}
                                    required
                                    className="bg-gray-100 text-gray-800 rounded-md px-3 py-2 text-sm w-full h-24 resize-none"
                                    placeholder="Tell us about your interests..."
                                />
                                <div className="absolute bottom-2 right-2 text-xs text-gray-500">
                                    {formData.personalinterests ? formData.personalinterests.length : 0}/100
                                </div>
                            </>
                        ) : (
                            <p className="bg-gray-100 text-gray-800 rounded-md px-3 py-2 text-sm w-full min-h-24">
                                {formData.personalinterests || 'Not specified'}
                            </p>
                        )}
                    </div>
                </div>
            </div>
        </section>
    )
}