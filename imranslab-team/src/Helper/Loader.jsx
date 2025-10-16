/** @format */

const Loader = () => {
  return (
    <div className="fixed inset-0 flex items-center justify-center h-screen bg-darkBg z-50">
      <div className="animate-spin rounded-full h-16 w-16 border-4 border-dashed border-primary"></div>
    </div>
  );
};

export default Loader;
