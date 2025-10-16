/** @format */

import { ChevronDown, ChevronUp } from "lucide-react";
import { useState } from "react";

// faqs data

const faqs = [
  {
    question: "Q1: How long does it take to develop custom software?",
    answer:
      "A1: The development timeline depends on the project scope, but typically, a custom web application takes 3-6 months, and a mobile app or enterprise solution may take 6-12 months or more. We follow Agile practices, which ensures you receive regular updates and early feedback.",
  },
  {
    question: "Q2: What technologies do you use?",
    answer:
      "A2: We use a variety of technologies including React.js, Node.js, Python, AWS, Azure, Django, Kotlin, Swift, and MongoDB. We select the best technologies based on your specific project needs.",
  },
  {
    question: "Q3: Do you offer post-launch support?",
    answer:
      "A3: Yes, we provide comprehensive post-launch support. This includes maintenance, bug fixes, and software updates to ensure your software stays up-to-date and secure.",
  },
  {
    question: "Q4: How do you ensure the quality of the software?",
    answer:
      "A4: We employ a research-driven QA process that includes manual and automated testing, performance testing, security assessments, and user acceptance testing to ensure the software meets your business needs and is free from defects.",
  },
  {
    question: "Q5: Will my software be scalable?",
    answer:
      "A5: Yes, we build software with scalability in mind, ensuring it can handle growing traffic and expanding functionalities as your business grows. We integrate cloud-based solutions to ensure seamless scalability.",
  },
];

const CustomerFaq = () => {
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

export default CustomerFaq;
