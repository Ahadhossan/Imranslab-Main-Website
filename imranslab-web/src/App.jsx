import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import Footer from "./components/Footer/Footer";
import Navbar from "./components/Navbar";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Home from "./pages/Home";
import Projects from "./pages/Projects";
import Services from "./pages/Services";
import SmoothFollower from "./Helper/SmoothFollower";
// import Loader from "./Helper/Loader";
import TermsCulture from "./pages/TermsCulture";
import Errorpage from "./pages/Errorpage";
import Ocr from "./Helper/ProjectDetails/OCR/Ocr";
import SrClean from "./Helper/ProjectDetails/SrClean/SrClean";
import Softtech from "./Helper/ProjectDetails/Softtech/Softtech";
import Quality from "./Helper/ServiceDetails/Quality";
import Edu from "./Helper/ProjectDetails/Education/Edu";
import ServiceContentFrom from "./Helper/Service/ServiceContentFrom";
import CustomSoftware from "./Helper/ServiceDetails/CustomSoftware";
import Network from "./Helper/ServiceDetails/Network";
import Career from "./pages/Career";
import Graphics from "./Helper/CareerJobDetails/Graphics";
import Software from "./Helper/CareerJobDetails/Software";
import Cloud from "./Helper/ServiceDetails/Cloud";
import Devops from "./Helper/ServiceDetails/Devops";
import Security from "./Helper/ServiceDetails/Security";
import MobileApp from "./Helper/ServiceDetails/MobileApp";

export default function App() {
  // const [loading, setLoading] = useState(true);
  const [isMobile, setIsMobile] = useState(false);
  // const [progress, setProgress] = useState(0);

  // Handle loading progress
  // useEffect(() => {
  //   if (loading) {
  //     const timer = setInterval(() => {
  //       setProgress((prevProgress) => {
  //         if (prevProgress >= 100) {
  //           clearInterval(timer); // stop when 100% is reached
  //           setLoading(false); // stop loading after progress reaches 100
  //           return 100;
  //         }
  //         return prevProgress + 10; // increase progress by 5% every 300ms
  //       });
  //     }, 300);

  //     return () => clearInterval(timer); // cleanup on unmount
  //   }
  // }, [loading]);

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
      <div className="overflow-hidden App">
        {/* Smooth Transition for Loader */}
        {/* {loading ? (
          <div className="fixed top-0 left-0 flex items-center justify-center w-full h-full transition-opacity duration-1000 bg-white opacity-100">
            <Loader progress={progress} />
          </div>
        ) : ( */}
        <>
          <Navbar />
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/home" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/career" element={<Career />} />
              {/* career job Details start*/}
              <Route path="/graphics" element={<Graphics />} />
              <Route path="/software" element={<Software />} />
              {/* career job Details end*/}
              <Route path="/services" element={<Services />} />
              <Route path="/projects" element={<Projects />} />
              <Route path="/contact" element={<Contact />} />
              <Route path="/terms" element={<TermsCulture />} />
              {/* Project Details */}
              <Route path="/ocr" element={<Ocr />} />
              <Route path="/srclean" element={<SrClean />} />
              <Route path="/education" element={<Edu />} />
              <Route path="/softtech" element={<Softtech />} />
              {/* services details */}
              <Route path="/quality" element={<Quality />} />
              <Route path="/software" element={<CustomSoftware />} />
              <Route path="/network" element={<Network />} />
              <Route path="/cloud" element={<Cloud />} />
              <Route path="/devops" element={<Devops />} />
              <Route path="/security" element={<Security />} />
              <Route path="/mobile" element={<MobileApp />} />

              {/* Service Contect From */}
              <Route path="/serviceontent" element={<ServiceContentFrom />} />
              {/* Error Page for unmatched routes */}
              <Route path="*" element={<Errorpage />} />
            </Routes>
          </main>
          <Footer />
          {/* Conditionally render SmoothFollower based on screen size */}
          {!isMobile && <SmoothFollower />}
        </>
        {/* )} */}
      </div>
    </BrowserRouter>
  );
}
