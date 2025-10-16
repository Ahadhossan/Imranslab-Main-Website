/** @format */

import { ChevronDown, ChevronUp } from "lucide-react";
import { useState } from "react";

// faqs data

const faqs = [
  {
    question: "Q1: What is network design?",
    answer:
      "A1: Network design is the process of creating a customized network architecture that meets your business needs, ensuring it is secure, fast, and scalable.",
  },
  {
    question: "Q2: How do you optimize network performance?",
    answer:
      "A2: We optimize network performance by managing bandwidth, optimizing traffic flow, and reducing latency. This helps ensure your network is fast and efficient.",
  },
  {
    question: "Q3: What are the benefits of load balancing?",
    answer:
      "A3: Load balancing ensures that no single server is overwhelmed with too much traffic. It helps distribute traffic evenly, ensuring high availability and better performance.",
  },
  {
    question: "Q4: How do you ensure network security?",
    answer:
      "A4: We implement firewall configurations, VPN solutions, and intrusion detection systems to secure your network from potential threats and ensure your data is protected.",
  },
];

const NetworkFaq = () => {
  const [activeQuestion, setActiveQuestion] = useState(null);

  return (
    <>
      {/* FAQ Section */}
      <section className="py-10 bg-white">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          {/* Header */}
          <h2 className="text-3xl sm:text-4xl font-bold text-center text-[#B3225F] mb-12">
            Frequently Asked Questions
          </h2>

          {/* FAQ List */}
          <div className="space-y-6">
            {faqs.map((faq, index) => (
              <div
                key={`faq-${index}-${faq.question
                  .substring(0, 10)
                  .replace(/\s+/g, "-")}`}
                className="border-b border-gray-900 pb-6"
              >
                <button
                  className="w-full flex justify-between items-center text-left py-3 px-4 rounded-md focus:outline-none transition-all duration-300 hover  hover:bg-slate-300"
                  onClick={() =>
                    setActiveQuestion(activeQuestion === index ? null : index)
                  }
                >
                  <span className="text-lg font-semibold text-gray-900 ">
                    {faq.question}
                  </span>
                  <div
                    className={`transition-transform duration-300 ${
                      activeQuestion === index ? "rotate-180" : ""
                    }`}
                  >
                    {activeQuestion === index ? (
                      <ChevronUp className="text-[#0066cc]" />
                    ) : (
                      <ChevronDown className="text-[#0066cc]" />
                    )}
                  </div>
                </button>
                {activeQuestion === index && (
                  <p className="mt-2 text-base  text-[#585c58]">{faq.answer}</p>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
};

export default NetworkFaq;
