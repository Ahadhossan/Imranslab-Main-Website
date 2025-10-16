/** @format */

import { ChevronDown, ChevronUp } from "lucide-react";
import { useState } from "react";

// faqs data

const faqs = [
  {
    question: "Q1: How long does it take to develop a mobile app?",
    answer:
      "A1: The development timeline for a custom mobile app depends on complexity. A basic app can take 3-6 months, while more complex apps with advanced features could take 6-12 months.",
  },
  {
    question: "Q2: What is the cost of developing a mobile app?",
    answer:
      "A2: The cost varies based on the complexity, platform (iOS, Android, or both), and the features required. A simple app may cost between $10,000-$50,000, while a more complex app can range from $50,000 to $200,000 or more.",
  },
  {
    question: "Q3: Do you offer both iOS and Android app development?",
    answer:
      "A3: Yes, we specialize in both iOS and Android mobile app development. We also offer cross-platform solutions like React Native and Flutter, which allow you to reach both platforms with one codebase.",
  },
  {
    question: "Q4: Do you provide post-launch support for mobile apps?",
    answer:
      "A4: Yes, we offer post-launch support to ensure your app stays bug-free, is up-to-date, and remains compatible with new OS versions.",
  },
  {
    question:
      "Q5: Can you integrate mobile apps with our existing backend systems?",
    answer:
      "A5: Yes, we offer seamless integration with your backend systems, cloud services, and third-party APIs, ensuring that your app works fluidly with your existing technology stack.",
  },
];

const MobileAppFaq = () => {
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

export default MobileAppFaq;
