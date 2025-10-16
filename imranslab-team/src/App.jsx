import { BrowserRouter, Routes, Route } from "react-router-dom";
import Footer from "./components/Footer/Footer";
import Navbar from "./components/Navbar";
import Contact from "./pages/Contact";
import HomePage from "./pages/HomePage";
import SmoothFollower from "./Helper/SmoothFollower";
import Loader from "./Helper/Loader";
import IntershipPage from "./pages/IntershipPage";
import useAuth from "./hooks/useAuth";
import PublicRoute from "./PublicRoute";
import PrivateRoute from "./PrivateRoute";
import Login from "./Helper/Login";
import SignUp from "./Helper/Signup";
import UserDetailsPage from "./pages/UserDetailsPage";
import ProfilePage from "./pages/ProfilePage";
import { useState, useEffect } from "react";
import { ActiveTabProvider } from './context/ActiveTabContext.jsx'

export default function App() {
  const [isMobile, setIsMobile] = useState(false);
  const { loadingUser, authLoading } = useAuth();

  // Handle mobile detection and screen resize
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth <= 768) {
        setIsMobile(true); // If screen width is 768px or less, it's a mobile device
      } else {
        setIsMobile(false);
      }
    };

    // Initial check
    handleResize();

    // Add event listener on window resize
    window.addEventListener("resize", handleResize);

    // Cleanup the event listener
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);


  return (
    <BrowserRouter>
      <ActiveTabProvider>
        <div className="App overflow-hidden">
          {loadingUser || authLoading ? (
            <Loader />
          ) : (
            <>
              <div className="min-h-screen flex flex-col">
                <Navbar />
                <main className="flex-grow">
                  <Routes>
                    {/* Landing pages */}
                    <Route path="/" element={<HomePage />} />
                    <Route path="/intern" element={<IntershipPage />} />
                    <Route path="/contact" element={<Contact />} />

                    {/* ExpertDetails page */}
                    <Route path="/experts/:id" element={<UserDetailsPage />} />
                    {/* internship deatils */}
                    <Route path="/intern/:id" element={<UserDetailsPage />} />

                    {/* user Proficepage */}
                    <Route path="/profile" element={
                      <PrivateRoute>
                        <ProfilePage />
                      </PrivateRoute>
                    } />
                    {/* Log in and Sign Up */}
                    <Route
                      path="/login"
                      element={
                        <PublicRoute>
                          <Login />
                        </PublicRoute>
                      }
                    />
                    <Route
                      path="/signup"
                      element={
                        <PublicRoute>
                          <SignUp />
                        </PublicRoute>
                      }
                    />
                  </Routes>
                </main>
                <Footer />
                {/* Conditionally render SmoothFollower based on screen size */}
                {!isMobile && <SmoothFollower />}
              </div>
            </>
          )}
        </div>
      </ActiveTabProvider >
    </BrowserRouter >
  );
}
