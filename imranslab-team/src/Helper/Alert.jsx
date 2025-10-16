import { useState, useEffect } from 'react';
import { CheckCircle2, XCircle, AlertCircle, Info, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion'; // Import framer-motion

const Alert = ({ type = 'info', message, onClose, duration = 5000 }) => {
    const [showAlert, setShowAlert] = useState(true);

    useEffect(() => {
        if (duration && onClose) {
            const timer = setTimeout(() => {
                setShowAlert(false);
                setTimeout(() => onClose(), 500); // Wait for the animation to finish before calling onClose
            }, duration);
            return () => clearTimeout(timer);
        }
    }, [duration, onClose]);

    const alertTypes = {
        success: {
            icon: <CheckCircle2 size={20} />,
            bg: 'bg-green-50',
            text: 'text-green-800',
            border: 'border-green-200',
        },
        error: {
            icon: <XCircle size={20} />,
            bg: 'bg-red-50',
            text: 'text-red-800',
            border: 'border-red-200',
        },
        warning: {
            icon: <AlertCircle size={20} />,
            bg: 'bg-yellow-50',
            text: 'text-yellow-800',
            border: 'border-yellow-200',
        },
        info: {
            icon: <Info size={20} />,
            bg: 'bg-blue-50',
            text: 'text-blue-800',
            border: 'border-blue-200',
        },
    };

    const { icon, bg, text, border } = alertTypes[type];

    return (
        <AnimatePresence>
            {showAlert && (
                <motion.div
                    className={`fixed top-10 right-4 z-50 flex items-start gap-3 p-4 rounded-md border ${bg} ${text} ${border} shadow-lg max-w-md`}
                    initial={{ x: 300 }} // Initial position off-screen (to the right)
                    animate={{ x: 0 }}   // Animate to original position (on-screen)
                    exit={{ x: 300 }}    // Slide out to the right when exiting
                    transition={{ type: 'spring', stiffness: 300 }} // Smooth animation
                >
                    <div className="mt-0.5">{icon}</div>
                    <div className="flex-1">
                        <p className="text-sm font-medium">{message}</p>
                    </div>
                    {onClose && (
                        <button
                            onClick={() => {
                                setShowAlert(false);
                                setTimeout(() => onClose(), 500); // Wait for the animation to finish before calling onClose
                            }}
                            className={`p-1 rounded-full hover:bg-opacity-20 hover:bg-${text.split('-')[1]}-500`}
                        >
                            <X size={16} />
                        </button>
                    )}
                </motion.div>
            )}
        </AnimatePresence>
    );
};

export default Alert;
