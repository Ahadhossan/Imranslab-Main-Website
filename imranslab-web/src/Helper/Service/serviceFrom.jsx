/** @format */

import { useEffect, useState } from "react";
import PhoneInput from "react-phone-input-2";
import "react-phone-input-2/lib/style.css";
import ButtonFill from "../../Button/ButtonFill";

const ServiceForm = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    service: "",
    number: "",
    message: "",
    budget: "",
  });

  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    setErrors((prev) => ({ ...prev, [name]: "" }));
  };

  const validate = () => {
    const newErrors = {};

    if (formData.name.trim().length < 2)
      newErrors.name = "Name must be at least 2 characters long.";

    if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(formData.email))
      newErrors.email = "Invalid email address.";

    if (!formData.service) newErrors.service = "Please select a service.";

    if (!formData.number || formData.number.replace(/\D/g, "").length < 10)
      newErrors.number = "Valid phone number required.";

    if (formData.message.length > 500)
      newErrors.message = "Message cannot exceed 500 characters.";

    if (!formData.budget) newErrors.budget = "Please select a budget.";

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    if (!validate()) return;

    setLoading(true);

    const data = new FormData();
    data.append("access_key", "276695ce-1e44-4cb0-bc1f-df51e6a92587");
    Object.entries(formData).forEach(([key, value]) => data.append(key, value));

    try {
      const res = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        body: data,
      });

      const result = await res.json();

      if (result.success) {
        setSuccess("Message sent successfully!");
        setFormData({
          name: "",
          email: "",
          service: "",
          number: "",
          message: "",
          budget: "",
        });
      } else {
        setSuccess("Failed to send message. Please try again.");
      }
    } catch {
      setSuccess("Network error. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (success) {
      const timer = setTimeout(() => setSuccess(""), 4000);
      return () => clearTimeout(timer);
    }
  }, [success]);

  return (
    <div className="p-6">
      {success && (
        <p
          className={`text-center text-sm font-medium ${
            success.includes("successfully") ? "text-green-500" : "text-red-500"
          }`}
        >
          {success}
        </p>
      )}

      <form onSubmit={onSubmit} className="space-y-4">
        {/* Name & Email */}
        <div className="flex flex-col gap-6 sm:flex-row">
          <div className="w-full sm:w-1/2">
            <input
              type="text"
              name="name"
              placeholder="Your Name"
              className="w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950"
              value={formData.name}
              onChange={handleChange}
            />
            {errors.name && (
              <p className="text-sm text-red-500">{errors.name}</p>
            )}
          </div>

          <div className="w-full sm:w-1/2">
            <input
              type="email"
              name="email"
              placeholder="Email"
              className="w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950"
              value={formData.email}
              onChange={handleChange}
            />
            {errors.email && (
              <p className="text-sm text-red-500">{errors.email}</p>
            )}
          </div>
        </div>

        {/* International Phone Input */}
        <div>
          <PhoneInput
            country={"ca"}
            value={formData.number}
            onChange={(phone) =>
              setFormData((prev) => ({ ...prev, number: phone }))
            }
            inputProps={{
              name: "phone",
              required: true,
              autoFocus: false,
            }}
            inputClass="!w-full !text-black px-4 py-2"
            specialLabel=""
            containerClass="w-full text-black"
          />
          {errors.number && (
            <p className="mt-1 text-sm text-red-500">{errors.number}</p>
          )}
        </div>

        {/* Service Dropdown */}
        <div>
          <select
            name="service"
            value={formData.service}
            onChange={handleChange}
            className="w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-black bg-white"
          >
            <option value="">Select your best service</option>
            <option value="Custom Software Development">
              Custom Software Development
            </option>
            <option value="Web Applications">Web Applications</option>
            <option value="Mobile Solutions">Mobile Solutions</option>
            <option value="UX, Product and Design">
              UX, Product and Design
            </option>
            <option value="Backend Development Services">
              Backend Development Services
            </option>
            <option value="Frontend Development Services">
              Frontend Development Services
            </option>
            <option value="QA and Software Testing">
              QA and Software Testing
            </option>
            <option value="DevOps">DevOps</option>
          </select>
          {errors.service && (
            <p className="mt-1 text-sm text-red-500">{errors.service}</p>
          )}
        </div>

        {/* Message */}
        <div>
          <label className="block mb-1 text-sm font-medium text-gray-500">
            Please describe your service
          </label>
          <textarea
            name="message"
            className="w-full p-2 px-4 py-2 text-black border-2 rounded-lg shadow-lg resize-none focus:outline-blue-950"
            placeholder="Details?"
            value={formData.message}
            onChange={handleChange}
          />
          {errors.message && (
            <p className="text-sm text-red-500">{errors.message}</p>
          )}
        </div>

        {/* Budget Dropdown */}
        <div>
          <input
            type="number"
            name="budget"
            placeholder="Your price"
            value={formData.budget}
            onChange={handleChange}
            className="w-full px-4 py-2 text-black border-2 rounded-lg shadow-lg focus:outline-blue-950"
          ></input>
          {errors.budget && (
            <p className="mt-1 text-sm text-red-500">{errors.budget}</p>
          )}
        </div>

        {/* Submit Button */}
        <ButtonFill type="submit" disabled={loading}>
          {loading ? "Sending..." : "Submit"}
        </ButtonFill>
      </form>
    </div>
  );
};

export default ServiceForm;
