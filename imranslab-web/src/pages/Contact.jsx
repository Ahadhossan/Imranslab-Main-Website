/** @format */

import { useRef, useState } from "react";
import PageHeader from "../Helper/PageHeader";
import { motion, useInView } from "framer-motion";
import ScrollToTopButton from "../Helper/ScrollToTopButton";
import PhoneInput from "react-phone-input-2";
import "react-phone-input-2/lib/style.css";
import ButtonFill from "../Button/ButtonFill";
import { Mail, Phone } from "lucide-react";

const Contact = () => {
  // Form state
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    message: "",
  });
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState("");

  // Regex
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  const validate = () => {
    const newErrors = {};

    if (!formData.name.trim()) newErrors.name = "Name is required.";
    if (!formData.email.trim()) newErrors.email = "Email is required.";
    else if (!emailRegex.test(formData.email))
      newErrors.email = "Invalid email format.";
    if (!formData.phone || formData.phone.replace(/\D/g, "").length < 10)
      newErrors.phone = "Valid international phone number is required.";
    if (!formData.message.trim()) newErrors.message = "Message is required.";
    else if (formData.message.length < 10)
      newErrors.message = "Message must be at least 10 characters.";

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    setErrors({ ...errors, [e.target.name]: "" });
  };

  const onSubmit = async (event) => {
    event.preventDefault();
    if (!validate()) return;

    setLoading(true);

    const formDataObj = new FormData();
    formDataObj.append("access_key", "276695ce-1e44-4cb0-bc1f-df51e6a92587");
    formDataObj.append("name", formData.name);
    formDataObj.append("email", formData.email);
    formDataObj.append("phone", formData.phone);
    formDataObj.append("message", formData.message);

    const response = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      body: formDataObj,
    });

    const result = await response.json();

    if (result.success) {
      setSuccess("✅ Message sent successfully!");
      setFormData({ name: "", email: "", phone: "", message: "" });
    } else {
      setSuccess("❌ Failed to send message. Please try again.");
    }

    setLoading(false);
  };

  // framer motion
  // location
  const locationRef = useRef(null);
  const locationInView = useInView(locationRef, {
    once: true,
    margin: "-100px",
  });

  return (
    <>
      <PageHeader
        title="Get In Touch"
        breadcrumb={[{ label: "Home", path: "/home" }, { label: "Contact" }]}
      />

      {/* Main Content */}
      {/* Country address */}
      <section
        className="px-4 py-10 bg-white sm:px-6 lg:px-12"
        ref={locationRef}
      >
        <motion.h2
          initial={{ opacity: 0, x: 50 }}
          animate={locationInView ? { opacity: 1, x: 0 } : {}}
          exit={{ opacity: 0, x: -50 }}
          transition={{ duration: 0.6 }}
          className="text-center text-[#B3225F] text-[27px] sm:text-[30px] md:text-[32px] lg:text-[36px] py-6 sm:py-8 md:py-10"
        >
          Global Networks imranslab
        </motion.h2>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {/* BD card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/wr4bmmz5/bangladesh.png"
                    alt="bangladesh"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  Bangladesh
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  House 41, Road 14, Block D, Section 12, Dhaka 1216
                </p>
                <div className="mt-4 flex gap-2">
                  <Phone />
                  <a
                    href="tel:+880 4182-0417"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    +880 4182-0417
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3649.8050123696407!2d90.3707393744262!3d23.825531785889595!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3755c188b7204ee9%3A0x68239ece58591201!2simranslab!5e0!3m2!1sen!2sbd!4v1751118431535!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Imran's Lab Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* UAE card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/C35pZQgj/united-arab-emirates.png"
                    alt="united-arab-emirates"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  UAE
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  Al Nahda Street, Al Majaz, Sharjah, UAE
                </p>
                <div className="mt-4 flex gap-2">
                  <Mail />
                  <a
                    href="mailto:uae@imranslab.org"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    mailto:uae@imranslab.org
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3607.1017813680023!2d55.37727987447702!3d25.30078422749888!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f5c748f6a7b0b%3A0x846c45bc69ef1809!2sAl%20Nahda%20St%20-%20Sharjah%20-%20United%20Arab%20Emirates!5e0!3m2!1sen!2sbd!4v1751122897672!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Imran's Lab Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* UK card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 0.4 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/sJKRdmVM/united-kingdom.png"
                    alt="united-kingdom"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  United Kingdom
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  2210 Baker Steet, London, NW1 6XE
                </p>
                <div className="mt-4 flex gap-2">
                  <Mail />
                  <a
                    href="mailto:uk@imranslab.org"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    uk@imranslab.org
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2482.599328483272!2d-0.1593790241219901!3d51.5205664097423!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761ace9a2e67d7%3A0xd458de8d0fdc498e!2sBaker%20St%2C%20London%2C%20UK!5e0!3m2!1sen!2sbd!4v1751123139328!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="united-kingdom Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* Pak card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 0.6 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/21YmCGRx/pakistan.png"
                    alt="pakistan"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  Pakistan
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  House 12, Street 45, Gulberg III,Lahare,Pakistan
                </p>
                <div className="mt-4 flex gap-2">
                  <Mail />
                  <a
                    href="mailto:pakistan@imranslab.com"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    pakistan@imranslab.com
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3402.5923224046683!2d74.38295757472451!3d31.48039894911736!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391905e1b996c16d%3A0xae1b76829ca066cd!2sStreet%2045%2C%20Lahore%2C%20Pakistan!5e0!3m2!1sen!2sbd!4v1751123713078!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Imran's Lab Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* Canada card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 0.8 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/1tjk3KNX/canada.png"
                    alt="canada"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  Canada
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  7077 Rue Birnam, Montréal, QC H3N 2S8, Canada
                </p>
                <div className="mt-4 flex gap-2">
                  <Phone />
                  <a
                    href="tel:+1 (47) 428-0032"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    +1 (47) 428-0032
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2795.273610634132!2d-73.6248102!3d45.5246993!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cc9190a134730ff%3A0xf5056fb7d1a161d3!2s7077%20Rue%20Birnam%2C%20Montr%C3%A9al%2C%20QC%20H3N%202S8%2C%20Canada!5e0!3m2!1sen!2sbd!4v1751125721811!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="canada Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* Senegal card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 1 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/KjtwFbdL/senegal.png"
                    alt="Senegal"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  Senegal
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  Rue Carrot, Dakar, Senegal
                </p>
                <div className="mt-4 flex gap-2">
                  <Mail />
                  <a
                    href="mailto:senegal@imranslab.org"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    senegal@imranslab.org
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3858.803120213925!2d-17.47977212226145!3d14.72372024145081!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xec16d003cf4bc0f%3A0x669efd32559d1d08!2sRue!5e0!3m2!1sen!2sbd!4v1751125962401!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Senegal Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* Sweden card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 1.2 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/GvTBC63R/sweden.png"
                    alt="Sweden"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  Sweden
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  Sveavägen 34, 111 34 Stockholm, Sweden
                </p>
                <div className="mt-4 flex gap-2">
                  <Mail />
                  <a
                    href="mailto:sweden@imranslab.org"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    sweden@imranslab.org
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2034.796154491645!2d18.058662484668538!3d59.33635705436813!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x465f9d6781640001%3A0x79eaee68e0b2679c!2sSveav%C3%A4gen%2034%2C%20111%2034%20Stockholm%2C%20Sweden!5e0!3m2!1sen!2sbd!4v1751126187883!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Sweden Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* US card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 1.4 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/JWN3g3k8/united-states.png"
                    alt="bangladesh"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  United States
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  123 Madison Ave, New York, NY 10016, USA
                </p>
                <div className="mt-4 flex gap-2">
                  <Mail />
                  <a
                    href="mailto:usa@imranslab.org"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    usa@imranslab.org
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.7578178988533!2d-73.98699532480471!3d40.745354235574354!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c259a7e012f549%3A0x1f4b74f64db7d437!2s123%20Madison%20Ave%2C%20New%20York%2C%20NY%2010016%2C%20USA!5e0!3m2!1sen!2sbd!4v1751127643264!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="USA Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* Moroco card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 1.6 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/WWRK0k7d/morocco.png"
                    alt="Moroco"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  Moroco
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  77 Rue Doukkala, Casablanca, Morocco
                </p>
                <div className="mt-4 flex gap-2">
                  <Phone />
                  <a
                    href="tel:+212 5220-98765"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    +212 5220-98765
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3322.955157913509!2d-7.632279225177688!3d33.60646794113854!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xda7d261cf1d0381%3A0x5ec8699ce30b5643!2s77%20Rue%20de%20Doukkala%2C%20Casablanca%2C%20Morocco!5e0!3m2!1sen!2sbd!4v1751127938463!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Morocco Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* US card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 1.8 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/JWN3g3k8/united-states.png"
                    alt="bangladesh"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  United States
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  456 Elm St, San Diego, CA 9102
                </p>
                <div className="mt-4 flex gap-2">
                  <Phone />
                  <a
                    href="tel:+46 (8) 1233 456 78"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    +46 (8) 1233 456 78
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d26853.543130276626!2d-117.13722110744094!3d32.72078747176145!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80d9537775f33751%3A0xd6c62e2f331f7ffa!2sSan%20Diego%2C%20CA%2092102%2C%20USA!5e0!3m2!1sen!2sbd!4v1751127069348!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="USA Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* San Diego card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 2 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/JWN3g3k8/united-states.png"
                    alt="bangladesh"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  San Diego
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  456 Elm St, San Diego, CA 92102
                </p>
                <div className="mt-4 flex gap-2">
                  <Phone />
                  <a
                    href="tel:+1 (619) 555-0267"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    +1 (619) 555-0267
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d26853.543130276626!2d-117.13722110744094!3d32.72078747176145!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80d9537775f33751%3A0xd6c62e2f331f7ffa!2sSan%20Diego%2C%20CA%2092102%2C%20USA!5e0!3m2!1sen!2sbd!4v1751127069348!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="San Diego Location Map"
                />
              </div>
            </div>
          </motion.div>
          {/* Oshowa card */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={locationInView ? { opacity: 1, y: 0 } : {}}
            exit={{ opacity: 0, y: -50 }}
            transition={{ duration: 0.6, delay: 2.2 }}
          >
            {/* Image and Hover Overlay */}
            <div className="relative group overflow-hidden rounded-md shadow-lg aspect-w-16 aspect-h-9">
              {/* Hover Text Overlay */}
              <div className="absolute inset-0 flex flex-col justify-center items-start text-start px-4 opacity-100 group-hover:opacity-0 transition-opacity duration-500 bg-black/90 backdrop-blur-sm">
                <h1 className="text-xl sm:text-2xl font-semibold text-[#15919B] flex justify-center text-center gap-2">
                  <img
                    src="https://i.ibb.co/1tjk3KNX/canada.png"
                    alt="canada"
                    border="0"
                    className="h-8 w-8"
                  />{" "}
                  Oshowa
                </h1>
                <p className="text-[17px] sm:text-[19px] text-[#f3f3f3] mt-3">
                  89 King St W, Oshawa, ONLH1A2
                </p>
                <div className="mt-4 flex gap-2">
                  <Mail />
                  <a
                    href="mailto:canada@imranslab.org"
                    className="text-[#15919B] hover:text-white hover:border-blue-50 hover:border-b"
                  >
                    canada@imranslab.org
                  </a>
                </div>
              </div>

              {/* Hover Location Map */}
              <div
                className="overflow-hidden"
                style={{ width: "100%", height: "200px" }}
              >
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2875.0253944333444!2d-78.87187402164741!3d43.89674077276889!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d51ce3e6913b57%3A0xab72361b2accda34!2s89%20King%20St%20W%2C%20Oshawa%2C%20ON%20L1H%208W7%2C%20Canada!5e0!3m2!1sen!2sbd!4v1751126816749!5m2!1sen!2sbd"
                  width="100%"
                  height="100%"
                  style={{ border: "0" }}
                  allowFullScreen=""
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Oshowa Location Map"
                />
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      <div className="w-full mx-auto border-b border-black my-10"></div>

      {/* contact from */}
      <section className="px-4 py-6 bg-white sm:px-6 lg:px-12">
        <div className="mx-auto max-w-7xl">
          <div className="grid items-start grid-cols-1 md:grid-cols-2 bg-[#FCFCFC] shadow-2xl border-2 border-[#15919B]">
            {/* Contact Info */}
            <motion.div
              initial={{ opacity: 0, x: -40 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true, margin: "-100px" }}
              className="space-y-8"
            >
              <img
                src="https://i.ibb.co/ymb6H3Wk/pexels-ann-h-45017-4672950.jpg"
                alt=""
                className="w-full h-[400px] md:h-[500px] lg:h-[585px] object-cover"
              />
            </motion.div>

            {/* Contact Form */}
            <motion.div
              initial={{ opacity: 0, x: 40 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true, margin: "-100px" }}
            >
              <div className="p-8 bg-white">
                {success && (
                  <p className="mb-4 font-semibold text-center text-green-600">
                    {success}
                  </p>
                )}

                <h3 className="text-xl font-semibold text-[#B3225F] mb-3">
                  Have Questions? Let’s Talk.
                </h3>
                <p className="text-[#151517] mb-6">
                  We’ve got the answers to your questions.
                </p>

                <form onSubmit={onSubmit} className="space-y-6">
                  {/* name and email */}
                  <div className="grid gap-4 md:grid-cols-2">
                    {/* Name */}
                    <div>
                      <label
                        htmlFor="name"
                        className="block mb-1 font-medium text-gray-700"
                      >
                        Name
                      </label>
                      <input
                        id="name"
                        name="name"
                        type="text"
                        value={formData.name}
                        onChange={handleChange}
                        className={`w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950 ${
                          errors.name ? "border-red-500" : ""
                        }`}
                        placeholder="Your Name"
                      />
                      {errors.name && (
                        <p className="mt-1 text-sm text-red-500">
                          {errors.name}
                        </p>
                      )}
                    </div>

                    {/* Email */}
                    <div>
                      <label
                        htmlFor="email"
                        className="block mb-1 font-medium text-gray-700"
                      >
                        Email
                      </label>
                      <input
                        id="email"
                        name="email"
                        type="email"
                        value={formData.email}
                        onChange={handleChange}
                        className={`w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950 ${
                          errors.email ? "border-red-500" : ""
                        }`}
                        placeholder="Your Email"
                      />
                      {errors.email && (
                        <p className="mt-1 text-sm text-red-500">
                          {errors.email}
                        </p>
                      )}
                    </div>
                  </div>

                  {/* Phone */}
                  <div>
                    <label
                      htmlFor="phone"
                      className="block mb-1 font-medium text-gray-700"
                    >
                      Phone
                    </label>
                    <PhoneInput
                      country={"ca"}
                      value={formData.phone}
                      onChange={(phone) =>
                        setFormData((prev) => ({ ...prev, phone }))
                      }
                      inputProps={{
                        name: "phone",
                        required: true,
                        autoFocus: false,
                      }}
                      inputClass="!w-full !text-black shadow-lg rounded-lg"
                      specialLabel=""
                      containerClass="w-full text-black"
                    />
                    {errors.phone && (
                      <p className="mt-1 text-sm text-red-500">
                        {errors.phone}
                      </p>
                    )}
                  </div>

                  {/* Message */}
                  <div>
                    <label
                      htmlFor="message"
                      className="block mb-1 font-medium text-gray-700"
                    >
                      Message
                    </label>
                    <textarea
                      id="message"
                      name="message"
                      value={formData.message}
                      onChange={handleChange}
                      className={`w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950 resize-none ${
                        errors.message ? "border-red-500" : ""
                      }`}
                      placeholder="Your Message"
                      rows={5}
                    />
                    {errors.message && (
                      <p className="mt-1 text-sm text-red-500">
                        {errors.message}
                      </p>
                    )}
                  </div>

                  {/* Submit */}
                  <ButtonFill type="submit" disabled={loading}>
                    {loading ? "Sending..." : "Send Message"}
                  </ButtonFill>
                </form>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      <ScrollToTopButton />
    </>
  );
};

export default Contact;
