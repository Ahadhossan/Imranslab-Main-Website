import { XIcon, UploadIcon } from 'lucide-react'

export const ProfilePictureSection = ({
    editMode,
    imagePreview,
    handleImageChange,
    handleRemoveImage,
    fileInputRef,
    userData
}) => {
    return (
        <section className="bg-white rounded-lg p-6 border text-gray-600">
            <h2 className="text-base font-medium mb-2">Profile Picture</h2>
            <p className="text-sm text-gray-600 mb-4">
                Upload a picture to make your profile stand out and let people recognize
                your comments and contributions easily!
            </p>
            <div className="flex items-center">
                <div className="relative w-20 h-20 mr-4">
                    {editMode ? (
                        <>
                            {imagePreview ? (
                                <img
                                    src={imagePreview}
                                    alt="Preview"
                                    className="w-full h-full rounded-md object-cover"
                                />
                            ) : userData.image ? (
                                <img
                                    src={userData.image}
                                    alt="Current Profile"
                                    className="w-full h-full rounded-md object-cover"
                                />
                            ) : (
                                <div className="w-full h-full bg-gray-200 rounded-md flex items-center justify-center">
                                    <span className="text-gray-500 text-xs">No image</span>
                                </div>
                            )}
                            {editMode && (imagePreview || userData.image) && (
                                <button
                                    type="button"
                                    onClick={handleRemoveImage}
                                    className="absolute -top-2 -right-2 bg-gray-100 rounded-full p-1"
                                >
                                    <XIcon size={14} />
                                </button>
                            )}
                        </>
                    ) : (
                        userData.image ? (
                            <img
                                src={userData.image}
                                alt="Profile"
                                className="w-full h-full rounded-md object-cover"
                            />
                        ) : (
                            <div className="w-full h-full bg-gray-200 rounded-md flex items-center justify-center">
                                <span className="text-gray-500 text-xs">No image</span>
                            </div>
                        )
                    )}
                </div>
                {editMode && (
                    <button
                        type="button"
                        onClick={() => fileInputRef.current.click()}
                        className="flex items-center bg-blue-50 text-blue-600 px-3 py-2 rounded-md text-sm"
                    >
                        <UploadIcon size={16} className="mr-2 text-gray-600" />
                        {imagePreview || userData.image ? 'Change Image' : 'Upload Image'}
                    </button>
                )}
                <input
                    type="file"
                    ref={fileInputRef}
                    onChange={handleImageChange}
                    accept="image/*"
                    className="hidden"
                />
            </div>
        </section>
    )
}