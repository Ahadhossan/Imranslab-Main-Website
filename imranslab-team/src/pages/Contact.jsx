/** @format */

import { useState } from "react";
import PageHeader from "../Helper/PageHeader";
import { motion } from "framer-motion";
import ScrollToTopButton from "../Helper/ScrollToTopButton";
import PhoneInput from "react-phone-input-2";
import "react-phone-input-2/lib/style.css";
import ButtonFill from "../Button/ButtonFill";

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

  return (
    <>
      <PageHeader title="Get In Touch" />

      {/* Main Content */}

      {/* contact from */}
      <section className="px-4 py-12 bg-white sm:px-6 lg:px-12">
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
              <div className="p-8 bg-white border shadow-md rounded-xl">
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
                      country={"ca"} // Default to US/Canada; can change to 'bd' for Bangladesh
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
                      className={`w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950  resize-none ${
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
