/** @format */

import { StepForward } from "lucide-react";
import PageHeader from "../Helper/PageHeader";
import { motion } from "framer-motion";
import ScrollToTopButton from "../Helper/ScrollToTopButton";

const TermsCulture = () => {
  // framer motion
  const fadeIn = {
    hidden: { opacity: 0, y: 30 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.6 } },
  };

  return (
    <>
      {/* Header Section */}
      <PageHeader
        title="Terms & Culture"
        breadcrumb={[
          { label: "Home", path: "/home" },
          { label: "Terms & Culture" },
        ]}
      />

      {/* Main Section */}
      <motion.section
        className="w-full px-4 sm:px-6 lg:px-12 py-12 bg-white"
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        variants={fadeIn}
      >
        <div className="max-w-5xl mx-auto">
          <motion.h1
            className="text-[#B3225F] text-3xl sm:text-4xl md:text-5xl font-bold text-center mb-12"
            variants={fadeIn}
          >
            Terms & Culture
          </motion.h1>

          <motion.div
            className="mb-6 flex items-center text-base text-[#111] font-semibold"
            variants={fadeIn}
          >
            <StepForward className="text-pink-700 mr-2" />
            <p>
              <strong>Effective Date:</strong> June 28, 2025
            </p>
          </motion.div>

          {/* Section: Terms */}
          <div>
            <motion.h2
              className="text-3xl font-bold text-[#151517] mb-4"
              variants={fadeIn}
            >
              1. Terms and Conditions
            </motion.h2>

            <motion.div
              className="text-[15px] text-[#6b6876] mb-6 leading-relaxed"
              variants={fadeIn}
            >
              <p>
                <strong className="text-[#15919B] font-bold">
                  Legal Entity:
                </strong>{" "}
                imranslab — Montreal, Quebec, Canada
              </p>
              <p>
                <strong className="text-[#15919B] font-bold">
                  Applies to:
                </strong>{" "}
                All visitors, users, clients, collaborators, partners, and
                third-party users of Imran’s Lab websites, applications, and
                services.
              </p>
            </motion.div>

            <motion.div
              className="text-xl font-bold text-[#151517]"
              variants={fadeIn}
            >
              <h2>i. Introduction</h2>
            </motion.div>

            <motion.div
              className="text-[15px] text-[#6b6876] mt-2 leading-relaxed"
              variants={fadeIn}
            >
              <p>
                This agreement (“Terms”) governs your access to and use of
                imranslab websites, software, mobile applications, APIs, and all
                services offered by imranslab (collectively, “Services”). By
                accessing the Services, you acknowledge that you have read,
                understood, and agreed to be legally bound by these Terms and
                our Privacy Policy. If you do not accept these Terms, you may
                not access or use the Services.
              </p>
            </motion.div>

            <motion.div
              className="text-xl font-bold text-[#151517] mt-4"
              variants={fadeIn}
            >
              <h2>ii. Definitions</h2>
            </motion.div>

            <motion.div
              className="text-[15px] text-[#6b6876] mt-2 leading-relaxed"
              variants={fadeIn}
            >
              <ul>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    “imranslab”
                  </strong>{" "}
                  refers to the operator of the Services, legally registered in
                  Montreal, Quebec, Canada.
                </li>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    “Client,” “User,” or “You”
                  </strong>{" "}
                  means any person or entity who accesses or uses the Services.
                </li>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    “Content”
                  </strong>{" "}
                  refers to any material, data, or media provided through or
                  uploaded to the Services.
                </li>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    “Authorized Use”
                  </strong>{" "}
                  means using the Services in accordance with applicable law and
                  these Terms.
                </li>
              </ul>
            </motion.div>

            <motion.div
              className="text-lg font-bold text-[#151517] mt-4"
              variants={fadeIn}
            >
              <h2>... (Content continues with sections 3 through 25)</h2>
            </motion.div>

            <motion.div
              className=" text-[#151517] leading-relaxed mt-6"
              variants={fadeIn}
            >
              <p>For questions, legal notices, or formal correspondence:</p>
              <p>
                <strong className="text-[#15919B] font-bold">imranslab</strong>
                <br />
                Montreal, Quebec, Canada
                <br />
                <div>
                  <a
                    href="mailto:contact@imranslab.imranslab.org"
                    className="hover:border-black border-b"
                  >
                    Email: contact@imranslab.imranslab.org
                  </a>
                </div>
                <div>
                  <a
                    href="tel:+1 (418) 482-0417"
                    className="hover:border-black border-b"
                  >
                    Phone: +1 (418) 482-0417
                  </a>
                </div>
              </p>
            </motion.div>
          </div>

          {/* Privacy Policy */}
          <div className="mt-8">
            <motion.h2
              className="text-3xl font-bold text-[#151517] mb-4"
              variants={fadeIn}
            >
              2. Privacy Policy
            </motion.h2>

            <motion.div
              className="text-[15px] text-[#6b6876] mb-6 leading-relaxed"
              variants={fadeIn}
            >
              <p>
                <strong className="text-[#15919B] font-bold">imranslab</strong>–
                Montreal, Quebec, Canada
              </p>
            </motion.div>

            <motion.div
              className="text-xl font-bold text-[#151517]"
              variants={fadeIn}
            >
              <h2>13. Data Breach Notification</h2>
            </motion.div>

            <motion.div
              className="text-[15px] text-[#6b6876] mt-2 leading-relaxed"
              variants={fadeIn}
            >
              <p>
                Despite our best efforts, no system is completely immune to
                security incidents. In the event of a data breach involving
                personal information, we will:
              </p>
              <ul>
                <li>
                  Notify affected users within{" "}
                  <strong className="text-[#15919B] font-bold">72 hours</strong>{" "}
                  of discovery, when legally required;
                </li>
                <li>
                  Provide details on the nature of the breach, affected data,
                  and corrective actions;
                </li>
                <li>
                  Cooperate with Canadian and, where applicable, international
                  regulatory authorities in accordance with{" "}
                  <strong className="text-[#15919B] font-bold">
                    Quebec’s Law 25
                  </strong>
                  , <strong className="text-[#15919B] font-bold">PIPEDA</strong>
                  , and{" "}
                  <strong className="text-[#15919B] font-bold">GDPR</strong>.
                </li>
              </ul>
              <p>
                If you believe your data may have been compromised, please
                contact us immediately at{" "}
                <strong className="text-[#15919B] font-bold">
                  security@imranslab.imranslab.org
                </strong>
                .
              </p>
            </motion.div>

            <motion.div
              className="text-xl font-bold text-[#151517] mt-4"
              variants={fadeIn}
            >
              <h2>14. Lawful Basis for Processing (GDPR Alignment)</h2>
            </motion.div>

            <motion.div
              className="text-[15px] text-[#6b6876] mt-2 leading-relaxed"
              variants={fadeIn}
            >
              <p>
                Where required by law (including GDPR for EU users), we process
                your personal data based on the following legal grounds:
              </p>
              <ul>
                <li>
                  <strong className="text-[#15919B] font-bold">Consent</strong>{" "}
                  – When you voluntarily provide data (e.g., contact forms,
                  sign-ups).
                </li>
                <li>
                  <strong className="text-[#15919B] font-bold">Contract</strong>{" "}
                  – When data is necessary to deliver services you've requested.
                </li>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    Legal obligation
                  </strong>{" "}
                  – When required to comply with legal or regulatory
                  requirements.
                </li>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    Legitimate interests
                  </strong>{" "}
                  – When processing supports analytics, platform performance, or
                  AI improvements in a privacy-respecting way that does not
                  override your rights.
                </li>
              </ul>
              <p>
                You may withdraw your consent at any time, subject to
                contractual or legal limits.
              </p>
            </motion.div>

            <motion.div
              className="text-xl font-bold text-[#151517] mt-4"
              variants={fadeIn}
            >
              <h2>15. Third-Party Services and Analytics Providers</h2>
            </motion.div>

            <motion.div
              className="text-[15px] text-[#6b6876] mt-2 leading-relaxed"
              variants={fadeIn}
            >
              <p>
                To improve our Services and understand usage behavior, we use
                third-party tools that may collect anonymized data via cookies
                or scripts. These may include:
              </p>
              <ul>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    Google Analytics
                  </strong>{" "}
                  – Website traffic insights
                </li>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    Firebase / Google Cloud
                  </strong>{" "}
                  – Hosting, push notifications, crash reporting
                </li>
                <li>
                  <strong className="text-[#15919B] font-bold">
                    Cloudflare
                  </strong>{" "}
                  – Security and caching
                </li>
                <li className="text-[#15919B] font-bold">
                  <strong>GitHub Pages or CDNs</strong> – Asset delivery and
                  performance monitoring
                </li>
              </ul>
              <p>
                These partners may process limited technical data in accordance
                with their own privacy policies. You can block cookies via
                browser settings or opt out where supported (e.g., Google
                Analytics Opt-out Browser Add-on).
              </p>
            </motion.div>

            <motion.div
              className="text-xl font-bold text-[#151517] mt-4"
              variants={fadeIn}
            >
              <h2>16. Transparency and User Control</h2>
            </motion.div>

            <motion.div
              className="text-[15px] text-[#6b6876] mt-2 leading-relaxed"
              variants={fadeIn}
            >
              <p>
                Although we do not yet offer a self-service privacy dashboard,
                you may:
              </p>
              <ul>
                <li>Request a copy of your data</li>
                <li>Request correction, deletion, or restriction of use</li>
                <li>Ask how your data is being processed</li>
                <li>Revoke consent for non-essential data use</li>
              </ul>
              <p>
                Send any requests to{" "}
                <strong className="text-[#15919B] font-bold">
                  privacy@imranslab.imranslab.org
                </strong>
                . We will respond within{" "}
                <strong className="text-[#15919B] font-bold">30 days</strong>{" "}
                and may require verification of identity.
              </p>
              <p>
                As we scale, we plan to offer a secure user dashboard for easier
                access and management of your data preferences.
              </p>
            </motion.div>

            <motion.div
              className="text-xl font-bold text-[#151517] mt-4"
              variants={fadeIn}
            >
              <h2>17. Data Residency and Storage Geography</h2>
            </motion.div>

            <motion.div
              className="text-[15px] text-[#6b6876] mt-2 leading-relaxed"
              variants={fadeIn}
            >
              <p>
                imranslab currently hosts data primarily in{" "}
                <strong className="text-[#15919B] font-bold">Canada</strong> and{" "}
                <strong className="text-[#15919B] font-bold">
                  the United States
                </strong>
                . Data may be mirrored or backed up in other compliant
                jurisdictions depending on third-party infrastructure providers.
              </p>
              <p>
                While we do{" "}
                <strong className="text-[#15919B] font-bold">
                  not currently support custom region-locking
                </strong>
                , we ensure that all processing follows data protection laws
                applicable in the storage region.
              </p>
              <p>
                We aim to support data residency options for enterprise clients
                in the future.
              </p>
            </motion.div>
          </div>
        </div>
      </motion.section>

      <ScrollToTopButton />
    </>
  );
};

export default TermsCulture;
