import { ProfilePictureSection } from './UserInfo/ProfilePictureSection'
import { AccountInfoSection } from './UserInfo/AccountInfoSection'
import { ContactInformation } from './UserInfo/ContactInformation'
import { AboutSection } from './UserInfo/AboutSection'
import { PersonalInterests } from './UserInfo/PersonalInterests'
import JobPosition from './UserInfo/JobPosition'

export const ProfileContent = ({
    editMode,
    setEditMode,
    formData,
    handleChange,
    handleSubmit,
    imagePreview,
    handleImageChange,
    handleRemoveImage,
    fileInputRef,
    userData
}) => {
    return (
        <div className="max-w-4xl mx-auto">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-xl text-gray-600 font-bold">Profile</h1>
                {editMode ? (
                    <div className="space-x-2">
                        <button
                            type="button"
                            onClick={() => setEditMode(false)}
                            className="bg-red-200 text-gray-800 px-4 py-1.5 rounded-md text-sm"
                        >
                            Cancel
                        </button>
                        <button
                            type="button"
                            onClick={handleSubmit}
                            className="bg-green-700 text-white px-4 py-1.5 rounded-md text-sm"
                        >
                            Save
                        </button>
                    </div>
                ) : (
                    <button
                        type="button"
                        onClick={() => setEditMode(true)}
                        className="bg-gray-700 text-white px-4 py-1.5 rounded-md text-sm"
                    >
                        Edit
                    </button>
                )}
            </div>
            <form onSubmit={handleSubmit} className="space-y-8">
                <ProfilePictureSection
                    editMode={editMode}
                    imagePreview={imagePreview}
                    handleImageChange={handleImageChange}
                    handleRemoveImage={handleRemoveImage}
                    fileInputRef={fileInputRef}
                    userData={userData}
                />
                <AccountInfoSection
                    editMode={editMode}
                    formData={formData}
                    handleChange={handleChange}
                />
                <JobPosition
                    editMode={editMode}
                    formData={formData}
                    handleChange={handleChange}
                />
                <ContactInformation
                    editMode={editMode}
                    formData={formData}
                    handleChange={handleChange}
                />
                <AboutSection
                    editMode={editMode}
                    formData={formData}
                    handleChange={handleChange}
                />
                <PersonalInterests
                    editMode={editMode}
                    formData={formData}
                    handleChange={handleChange}
                />
            </form>
            <div className="flex justify-between items-center my-6">
                <h1 className="text-xl text-gray-600 font-bold"></h1>
                {editMode ? (
                    <div className="space-x-2">
                        <button
                            type="button"
                            onClick={() => setEditMode(false)}
                            className="bg-gray-200 text-gray-800 px-4 py-1.5 rounded-md text-sm"
                        >
                            Cancel
                        </button>
                        <button
                            type="button"
                            onClick={handleSubmit}
                            className="bg-black text-white px-4 py-1.5 rounded-md text-sm"
                        >
                            Save
                        </button>
                    </div>
                ) : (
                    <div></div>
                )}
            </div>

        </div>
    )
}