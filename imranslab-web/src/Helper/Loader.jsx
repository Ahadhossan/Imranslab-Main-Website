import { useState, useEffect } from "react";

const Loader = ({ progress }) => {
  const [percentage, setPercentage] = useState(progress);
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    if (progress >= 0 && progress <= 100) {
      setPercentage(progress);
    }

    // Update the message dynamically
    if (progress === 100) {
      setMessage("Loading Complete!");
    } else {
      setMessage(`Loading... ${progress}%`);
    }
  }, [progress]);

  // Dynamic color based on progress
  const getColor = () => {
    if (percentage < 30) return "border-red-500";
    if (percentage < 70) return "border-yellow-500";
    return "border-green-500";
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center h-screen bg-[#0A2B42]">
      <div className="relative">
        {percentage !== 100 && (
          <div
            className={`animate-spin rounded-full h-24 w-24 border-4 border-dashed ${getColor()}`}
          ></div>
        )}

        <div className="absolute inset-0 flex flex-col items-center justify-center text-center text-white">
          {percentage === 100 ? (
            <div className="text-xl font-semibold text-green-600 animate-pulse">
              {message}
            </div>
          ) : (
            <div className="text-lg font-semibold text-white">{message}</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Loader;
