# Computer Security Division Annual Report 2014

NIST Special Publication 800-176  
Patrick O’Reilly, Editor  
Computer Security Division  
Information Technology Laboratory  
National Institute of Standards and Technology  

Co-Editors:  
Larry Feldman  
Greg Witte  
G2, Inc.  

This publication is available free of charge from [http://dx.doi.org/10.6028/NIST.SP.800-176](http://dx.doi.org/10.6028/NIST.SP.800-176)  
August 2015  

U.S. Department of Commerce  
Penny S. Pritzker, Secretary  

National Institute of Standards and Technology  
Dr. Willie E. May, Under Secretary of Commerce for Standards and Technology and Director  

Disclaimer: Any mention of commercial products is for information only; it does not imply NIST recommendation or endorsement, nor does it imply that the products mentioned are necessarily the best available for the purpose.  

National Institute of Standards and Technology Special Publication 800-176  
Natl. Inst. Stand. Technol. Spec. Pub., 107 pages (August 2015) CODEN: NSPUE2  

## Table of Contents
- [Welcome Letter](#welcome-letter)
- [Computer Security Division (CSD) Organization](#computer-security-division-csd-organization)
- [Introduction to CSD’s Five Groups](#introduction-to-csds-five-groups)
  - [Cryptographic Technology Group (CTG)](#cryptographic-technology-group-ctg)
  - [Security Components and Mechanisms Group (SCMG)](#security-components-and-mechanisms-group-scmg)
  - [Secure Systems and Applications Group (SSAG)](#secure-systems-and-applications-group-ssag)
  - [Security Outreach and Integration Group (SOIG)](#security-outreach-and-integration-group-soig)
  - [Security Testing, Validation, and Measurement Group (STVMG)](#security-testing-validation-and-measurement-group-stvmg)
- [CSD Implements the Federal Information Security Management Act](#csd-implements-the-federal-information-security-management-act)
- [Program and Project Achievements for FY 2014](#program-and-project-achievements-for-fy-2014)
- [NIST Responsibilities Under Executive Order 13636, Improving Critical Infrastructure Cybersecurity](#nist-responsibilities-under-executive-order-13636-improving-critical-infrastructure-cybersecurity)
- [CSD Work in National and International Standards](#csd-work-in-national-and-international-standards)
- [Federal Information Security Management Act (FISMA) Implementation Project](#federal-information-security-management-act-fisma-implementation-project)
- [Biometric Standards and Associated Conformity Assessment Testing Tools](#biometric-standards-and-associated-conformity-assessment-testing-tools)
- [Federal Cybersecurity Research & Development (R&D)](#federal-cybersecurity-research--development-rd)
- [Security Aspects of Electronic Voting](#security-aspects-of-electronic-voting)
- [Health Information Technology Security](#health-information-technology-security)
- [Supply-Chain Risk Management (SCRM) for Information and Communications Technology (ICT)](#supply-chain-risk-management-scrm-for-information-and-communications-technology-ict)
- [Nationwide Public Safety Broadband Network (NPSBN) Cybersecurity](#nationwide-public-safety-broadband-network-npsbn-cybersecurity)
- [Security of Cyber-Physical Systems (CPS)](#security-of-cyber-physical-systems-cps)
- [Smart Grid Cybersecurity](#smart-grid-cybersecurity)
- [Cybersecurity Awareness, Training, Education, and Outreach](#cybersecurity-awareness-training-education-and-outreach)
  - [National Initiative for Cybersecurity Education (NICE)](#national-initiative-for-cybersecurity-education-nice)
  - [Computer Security Resource Center (CSRC)](#computer-security-resource-center-csrc)
  - [Federal Computer Security Program Managers’ Forum](#federal-computer-security-program-managers-forum)
  - [Federal Information Systems Security Educators’ Association (FISSEA)](#federal-information-systems-security-educators-association-fissea)
  - [Information Security and Privacy Advisory Board (ISPAB)](#information-security-and-privacy-advisory-board-ispab)
  - [Small and Medium Size Business (SMB) Cybersecurity Workshop Outreach](#small-and-medium-size-business-smb-cybersecurity-workshop-outreach)
- [Cryptographic Standards Program](#cryptographic-standards-program)
  - [Hash Algorithms and the Secure Hash Algorithm-3 (SHA-3) Standard (Draft FIPS 202)](#hash-algorithms-and-the-secure-hash-algorithm-3-sha-3-standard-draft-fips-202)
  - [Random Number Generation (RNG)](#random-number-generation-rng)
  - [Block Cipher Modes of Operation](#block-cipher-modes-of-operation)
  - [Key Management](#key-management)
  - [Transport Layer Security](#transport-layer-security)
- [Cryptographic Research](#cryptographic-research)
  - [Post-Quantum Cryptography](#post-quantum-cryptography)
  - [Privacy-Enhancing Cryptography](#privacy-enhancing-cryptography)
  - [Cryptographic Standards and Guidelines Process Review](#cryptographic-standards-and-guidelines-process-review)
- [New Research Areas in Cryptographic Techniques for Emerging Applications](#new-research-areas-in-cryptographic-techniques-for-emerging-applications)
  - [Circuit Complexity Research](#circuit-complexity-research)
  - [Cryptography for Constrained Environments](#cryptography-for-constrained-environments)
  - [NIST Randomness Beacon](#nist-randomness-beacon)
  - [Wireless and Mobile Security](#wireless-and-mobile-security)
- [Validation Programs](#validation-programs)
  - [Cryptographic System Validation](#cryptographic-system-validation)
  - [Cryptographic Programs and Laboratory Accreditation](#cryptographic-programs-and-laboratory-accreditation)
  - [Automated Security Testing and Test Suite Development](#automated-security-testing-and-test-suite-development)
  - [ISO Standardization of Security Requirements for Cryptographic Modules](#iso-standardization-of-security-requirements-for-cryptographic-modules)
  - [Security Content Automation Protocol (SCAP) Validation Program](#security-content-automation-protocol-scap-validation-program)
- [Identity Management](#identity-management)
  - [Personal Identity Verification (PIV) and FIPS 201 Revision Efforts](#personal-identity-verification-piv-and-fips-201-revision-efforts)
  - [NIST Personal Identity Verification Program (NPIVP) & Revisions to FIPS 201-2 Companion Documents](#nist-personal-identity-verification-program-npivp--revisions-to-fips-201-2-companion-documents)
- [Research in Emerging Technologies](#research-in-emerging-technologies)
  - [Cloud Computing and Virtualization](#cloud-computing-and-virtualization)
  - [CSD Role in the NIST Cloud Computing Program](#csd-role-in-the-nist-cloud-computing-program)
  - [Policy Machine – Leveraging Access Control for Cloud Computing](#policy-machine--leveraging-access-control-for-cloud-computing)
  - [Virtualization Security & Leveraging Virtualization for Security](#virtualization-security--leveraging-virtualization-for-security)
- [Mobile Security](#mobile-security)
- [Strengthening Internet Security](#strengthening-internet-security)
  - [USGv6: A Technical Infrastructure to Assist IPv6 Adoption](#usgv6-a-technical-infrastructure-to-assist-ipv6-adoption)
- [Access Control and Privilege Management](#access-control-and-privilege-management)
  - [Access Control and Privilege Management Research](#access-control-and-privilege-management-research)
  - [Conformance Verification for Access-Control Policies](#conformance-verification-for-access-control-policies)
  - [Attribute-Based Access Control](#attribute-based-access-control)
- [Advanced Security Testing and Measurements](#advanced-security-testing-and-measurements)
  - [Security Automation and Continuous Monitoring](#security-automation-and-continuous-monitoring)
  - [Security Content Automation Protocol (SCAP)](#security-content-automation-protocol-scap)
  - [Continuous Monitoring](#continuous-monitoring)
  - [Security Automation Reference Data](#security-automation-reference-data)
  - [National Vulnerability Database (NVD)](#national-vulnerability-database-nvd)
  - [Computer Security Incident Coordination](#computer-security-incident-coordination)
  - [National Checklist Program (NCP)](#national-checklist-program-ncp)
  - [United States Government Configuration Baseline (USGCB) / FDCC Baselines](#united-states-government-configuration-baseline-usgcb--fdcc-baselines)
  - [Apple OS X Security Configuration](#apple-os-x-security-configuration)
- [Technical Security Metrics](#technical-security-metrics)
  - [Security Risk Analysis of Enterprise Networks Using Attack Graphs](#security-risk-analysis-of-enterprise-networks-using-attack-graphs)
  - [Algorithms for Intrusion Measurement](#algorithms-for-intrusion-measurement)
  - [Automated Combinatorial Testing](#automated-combinatorial-testing)
  - [Roots of Trust](#roots-of-trust)
- [Honors and Awards](#honors-and-awards)
- [Computer Security Division Publications](#computer-security-division-publications)
- [FY 2014 Computer Security Division Publications](#fy-2014-computer-security-division-publications)
  - [NIST Technical Series Publications − FIPS, SPs, NISTIRs, and ITL Bulletins](#nist-technical-series-publications---fips-sps-nistirs-and-itl-bulletins)
  - [Abstracts of NIST Technical Series Publications Released in FY 2014](#abstracts-of-nist-technical-series-publications-released-in-fy-2014)
- [Additional Publications by CSD Authors](#additional-publications-by-csd-authors)
  - [Journal Articles](#journal-articles)
  - [Conference Papers](#conference-papers)
  - [Books and Book Sections](#books-and-book-sections)
  - [White Papers](#white-papers)
- [Acronyms](#acronyms)
- [Opportunities to Engage with CSD and NIST](#opportunities-to-engage-with-csd-and-nist)
- [Acknowledgements](#acknowledgements)
- [Trademark Information](#trademark-information)

---

## Welcome Letter

The Computer Security Division (CSD), a component of the Information Technology Laboratory at the National Institute of Standards and Technology (NIST) is responsible for developing standards, guidelines, tests, and metrics for protection of non-national security federal information systems. NIST standards and guidelines are developed in an open, transparent, and collaborative manner that enlists broad expertise from around the world. While developed for federal agency use, these resources are voluntarily adopted by other organizations because they are effective and accepted globally.

The need for cybersecurity standards and best practices that address interoperability, usability and privacy continues to be critical for the Nation. CSD continues to align its resources to enable greater development and application of practical, innovative security technologies and methodologies that enhance our ability to address current and future computer and information security challenges. Our foundational research and applied cybersecurity programs continue to advance in many areas including cryptography, roots of trust, identity and access management, advanced security testing and measurement, cyber-physical systems, and public safety networks.

Trust is crucial to the broad adoption of our standards and guidelines, including our cryptographic standards and guidelines. To ensure that our cryptography resources have been developed according the highest standard of inclusiveness, transparency and security, NIST initiated a formal review of our cryptographic standards development efforts in 2014. We documented and solicited public comment on the principles and rigorous processes we use to engage stakeholders and experts in industry, academia, and government to develop and revise these standards. We anticipate a final report in 2015 that will serve as a basis for our future standards development and revision efforts.

Increasing the trustworthiness and resilience of the IT infrastructure is a significant undertaking that requires a substantial investment in the architectural design and development of our systems and networks. A disciplined and structured set of systems security engineering processes that starts with and builds on well-established international standards provides an important starting point. Draft Special Publication 800-160, _Systems Security Engineering: An Integrated Approach to Building Trustworthy Resilient Systems_, issued in May 2014, helps organizations to develop a more defensible and survivable information technology infrastructure. This resource, coupled with other NIST standards and guidelines, contributes to systems that are more resilient in the face of cyber attacks and other threats.

Strong partnerships with diverse stakeholders are vital to the success of our technical programs. In February 2014, NIST issued the _Framework for Improving Critical Infrastructure Cybersecurity_ as directed in Executive Order 13636. The Framework, created through collaboration between industry and government, consists of standards, guidelines, and practices to promote the protection of critical infrastructure. Its approach helps owners and operators of critical infrastructure to manage cybersecurity-related risk. Collaborations continue as NIST works with stakeholders from across the country and around the world. Working closely with standards developing organizations, industry and interagency partners, we are evolving and expanding security automation capabilities to help organizations manage and measure the security of systems and technologies.

Active engagement with diverse stakeholders continues to be critical to our success. In the federal space, this interaction is most prominent in our strengthened collaborations with the Department of Defense, the Intelligence Community, and the Committee on National Security Systems to establish a common foundation for information security across the federal government. Our cybersecurity awareness, training, and education programs also exemplify the importance of engagements with academic institutions, federal agencies, small and medium businesses and others to increase awareness and enhance the overall cybersecurity posture of the Nation.

For many years, CSD, in collaboration with our global partners across industry, academia, and government, has made great contributions to help secure the nation’s critical information and infrastructure. We look forward to strengthening these relationships as we lead the development and practical application of scalable and sustainable information security standards and practices.

To participate in any CSD research areas – whether current or future – or to learn more about our programs and activities, please visit [http://csrc.nist.gov](http://csrc.nist.gov).

Matthew Scholl  
Acting Division Chief

---

## Computer Security Division (CSD) Organization

- **MATTHEW SCHOLL** – Acting Chief and Deputy Chief, Computer Security Division
- **GROUP MANAGERS:**
  - **LILY CHEN** (Acting Group Manager) – Cryptographic Technology Group
  - **DAVID FERRAIOLO** – Secure Systems and Applications Group
  - **MARK (LEE) BADGER** – Security Outreach and Integration Group
  - **KEVIN STINE** – Security Components and Mechanisms Group
  - **MICHAEL COOPER** – Security Testing, Validation and Measurement Group

---

## Introduction to CSD’s Five Groups

The Computer Security Division’s computer scientists, mathematicians, IT specialists, support staff and others support CSD’s mission and responsibilities through five groups that are described in the following sections:
- Cryptographic Technology Group
- Security Components and Mechanisms Group
- Secure Systems and Applications Group
- Security Outreach and Integration Group
- Security Testing, Validation, and Measurement Group

### Cryptographic Technology Group (CTG)

**Mission Statement:**  
Research, develop, engineer, and standardize cryptographic algorithms, methods, and protocols.

**Overview:**  
The Cryptographic Technology Group’s (CTG) work in the field of cryptography includes researching, analyzing and standardizing cryptographic technology, such as hash algorithms, symmetric and asymmetric cryptographic techniques, key management, authentication, and random number generation. The CTG’s goal is to identify and promote methods to enhance trust in communications, data, and storage through cryptographic technology, encouraging innovative development and helping technology users to manage risk.

In FY 2014, the CTG continued to make an impact in the field of cryptography, both within and outside the Federal Government, by collaborating with national and international agencies, academic and research organizations, and standards bodies to develop interoperable security standards and guidelines. In addition, the CTG worked with industry partners to promote the use of NIST-approved cryptographic methods.

The NIST cryptographic standards’ program standardizes cryptographic primitives, algorithms, schemes, and guidelines in Federal Information Processing Standards (FIPSs), NIST Special Publications (SPs), NIST Interagency or Internal Reports (NISTIRs). The NIST standardized cryptographic tools have been adopted as standards by standards-setting organizations, such as the Internet Engineering Task Force (IETF), the Institute of Electrical and Electronics Engineers (IEEE), and the Trusted Computing Group (TCG), and have been implemented on a variety of platforms.

In FY 2014, in response to public concerns about NIST cryptographic standards -in particular, the DUAL_EC_DRBG, a deterministic random number generator specified in SP 800-90A, _Recommendation for Random Number Generation Using Deterministic Random Bit Generators_—NIST initiated a review of the cryptographic standards development process. The CTG summarized the development process for each cryptographic standard and provided materials and presentations to the NIST Visiting Committee on Advanced Technology (VCAT) and a NIST Committee of Visitors (COV), consisting of experts invited by the VCAT, to conduct the review. A summary for this review is provided in the Cryptographic Standards and Guidelines Process Review section of this annual report.

CTG researchers were highly engaged and productive in several critical cryptographic areas, such as post-quantum cryptography, elliptic curve cryptography, privacy-enhancing cryptography, and lightweight cryptographic schemes for constrained environments. The CTG has collaborated with many universities internationally, and research results were published in the major cryptography conferences and journals. The CTG also held workshops and conferences, as well as hosted guest researchers.

Several guidelines on cryptographic applications were published in various areas, such as key management, Internet protocols, and trusted platforms. The CTG contributed to other CSD cybersecurity projects, such as the Smart Grid and Personal Identity Verification (PIV) standards. The CTG also worked closely with the Security Testing, Validation, and Measurement Group of the CSD on FIPS 140-2, _Security Requirements for Cryptographic Modules_, the Cryptographic Algorithm Validation Program (CAVP), and the Cryptographic Module Validation Programs (CMVP).

**Group Manager (Acting):**  
Dr. Lily Chen  
(301) 975-6974  
lily.chen@nist.gov  

### Security Components and Mechanisms Group (SCMG)

**Mission Statement:**  
Research, develop, and standardize foundational security mechanisms, protocols, and services.

**Overview:**  
The SCMG’s security research focuses on the development and management of foundational building-block security mechanisms and techniques that can be integrated into a wide variety of mission-critical U.S. information systems. The group’s work spans the spectrum from near-term hardening and improvement of systems, to the design and analysis of next-generation, leap-ahead security capabilities. Computer security depends fundamentally on the level of trust of computer software and systems. This work, therefore, focuses strongly on assurance-building activities ranging from the analysis of software configuration settings, to advanced trust architectures, and to testing tools that identify flaws in software modules. This work also focuses significantly on increasing the applicability and effectiveness of automated techniques, wherever feasible.

The SCMG conducts collaborative research with government, industry, and academia. Outputs of this research consist of prototype systems, software tools, demonstrations, guidelines, and other documentary resources.

Collaborating extensively with government, academia, and the private sector, SCMG works on a variety of topics, such as:
- Specifications for the automated exchange of security information between systems;
- Computer-security incident-handling guidelines;
- Formulation of high-assurance software configuration settings;
- Hardware roots-of-trust for mobile devices;
- Secure Basic Input Output System (BIOS) layers;
- Combinatorial testing techniques;
- Conformity assessment of software implementing biometric standards; and
- Adoption of Internet Protocol Version 6 and Internet Protocol security extensions.

In FY 2014, collaborators and the associated collaborations have included Carnegie Mellon University (test development environment), Johns Hopkins Applied Physics Lab (practical application of combinatorial coverage measurement tool), the University of Texas at Arlington (covering array generation algorithm), Mexico’s Centro Nacional de Metrología (constraints for a testing coverage tool), National Aeronautics and Space Administration (NASA) (practical application for combinatorial coverage measurement), U.S. Air Force Test and Evaluation (a new event sequence testing method), the University of Texas Dallas and East Carolina University (safety-critical systems testing), the National Science Foundation (cybersecurity metrics and assurance building), the National Security Agency (secure software tool chain competition), and the Department of Homeland Security (incident coordination).

SCMG accomplishments include updates to the Advanced Combinatorial Testing System (ACTS) software and documentation, and the NIST Biometrics Conformance Test Software (BioCTS) 2014 biometric conformance testing tool and test assertions.

**Group Manager:**  
Mr. Mark (Lee) Badger  
(301) 975-3176  
lee.badger@nist.gov  

### Secure Systems and Applications Group (SSAG)

**Mission Statement:**  
Integrate and apply security technologies, standards and guidelines for computing platforms and information systems.

**Overview:**  
SSAG’s security research focuses on identifying emerging and high-priority technologies, and on developing security solutions that will have a high impact on the U.S. critical infrastructures. The group conducted research and development on behalf of government and industry from the earliest stages of technology development through proof-of-concept, reference and prototype implementations and demonstrations. In addition, the group worked to transfer new technologies to industry; to produce new standards and guidance for federal agencies and industry; and to develop tests, test methodologies, and assurance methods.

SSAG investigated the security concerns associated with such areas as mobile devices, cloud computing and virtualization, identity management, access control and authorization management, and software assurance.

SSAG’s research helps to meet federal information security requirements that may not be fully addressed by existing technology. The group collaborated extensively with government, academia, and private sector entities.

Example successes from this work include:
- Tools for access control policy testing;
- New concepts in access control and policy enforcement;
- Published several Personal Identity Verification documents;
- Methods for achieving comprehensive policy enforcement and data interoperability across enterprise data services; and
- Test methods for mobile device (smart phone) application security.

In particular, the SSAG released an open-source reference implementation of ANSI/INCITS 499, _Next Generation Access Control_. The group also published SP 800-162, _Attribute Based Access Control (ABAC) Definition and Considerations_, providing the first authoritative definition of ABAC. In support of the Federal Government’s mobile security initiatives, the group published SP 800-163, _Vetting the Security of Mobile Applications_, to provide agencies with guidelines on how to test mobile applications for government use. In support of the Federal Government’s cloud computing initiatives, the group led the NIST Security Working Group that published the _NIST Cloud Computing Security Reference Architecture_. In support of the recently revised FIPS 201-2, _Personal Identity Verification (PIV) of Federal Employees and Contractors_, six PIV-related 800-series SPs were revised. In addition to these, draft SP 800-157, _Guidelines for Derived Personal Identity Verification (PIV) Credentials_, was published to guide the implementation and deployment of PIV credentials for mobile devices.

To improve access to new technologies, the group also chaired, edited, and participated in the development of a wide variety of national and international security standards.

**Group Manager:**  
Mr. David Ferraiolo  
(301) 975-3046  
david.ferraiolo@nist.gov  

### Security Outreach and Integration Group (SOIG)

**Mission Statement:**  
Develop, integrate, and promote the mission-specific application of information security standards, guidelines, best practices, and technologies.

**Overview:**  
The U.S. economy, citizens, and government rely on information technology (IT), so the protection of the IT and information infrastructure is critical. SOIG leverages broad cybersecurity and risk-management expertise to develop, integrate, and promote security standards, guidelines, tools, technologies, methodologies, tests, and measurements to address cybersecurity needs in many areas of national and international importance.

The SOIG collaborates with stakeholders to address cybersecurity considerations in many diverse program areas, including the Information and Communications Technologies (ICT) supply chain, Smart Grid, Electronic Voting, Cyber Physical and Industrial Control Systems, Health Information Technology, and the National Public Safety Broadband Network. The group produces standards and guidelines through the Federal Information Security Management Act (FISMA) implementation program to help federal agencies build strong cybersecurity risk-management programs. In each of these program areas, the group extends outreach to stakeholders across federal, state, and local governments; industry; academia; small businesses; and the public. The SOIG also leads several broad cybersecurity awareness, training, education, and outreach efforts, including the National Initiative for Cybersecurity Education (NICE), the Federal Computer Security Managers’ Forum, and the Federal Information Systems Security Educators’ Association (FISSEA).

Key to the group’s success is the ability to interact with a broad constituency to ensure that SOIG’s program is consistent with national objectives related to or impacted by information security. Through open and transparent public engagement, collaboration, and cooperation, the group works to address critical cybersecurity challenges, enable greater U.S. industrial competitiveness, and facilitate the practical implementation of scalable and sustainable information security standards and practices.

**Group Manager:**  
Mr. Kevin Stine  
(301) 975-4483  
kevin.stine@nist.gov  

### Security Testing, Validation, and Measurement Group (STVMG)

**Mission Statement:**  
Advance information security testing, measurement science, and conformance.

**Overview:**  
Federal agencies, industry, and the public rely on cryptography for the protection of information and communications used in electronic commerce, critical infrastructures, and other application areas. The STVMG supports the testing and validation of cryptographic modules and the cryptographic algorithms specified in NIST standards. These cryptographic modules and algorithms enable products and systems to provide security services, such as confidentiality, integrity authentication, and source authentication. Although cryptography provides security, poor designs or weak algorithms can render a product insecure and place highly sensitive information at risk. When protecting sensitive data, Federal Government agencies require a minimum level of assurance that cryptographic products meet established security requirements and use only tested and validated cryptographic modules and algorithms.

STVMG’s testing-focused activities include validating cryptographic algorithm implementations, cryptographic modules, and Security Content Automation Protocol (SCAP)-compliant products; developing test suites and test methods; providing implementation guidance and technical support to industry forums; and conducting education, training, and outreach programs.

STVMG’s validation programs work together with independent Cryptographic and Security Testing laboratories that are accredited by the NIST National Voluntary Laboratory Accreditation Program (NVLAP). Based on the independent laboratory test report and test evidence, the Validation Program then validates the implementation under test. NIST publishes, through public websites, lists of the validations awarded.

**Group Manager:**  
Mr. Michael Cooper  
(301) 975-8077  
michael.cooper@nist.gov  

---

## The Computer Security Division Implements the Federal Information Security Management Act

The E-Government Act, Public Law 107-347, passed by the 107th Congress and signed into law by the President in December 2002, recognized the importance of information security to the economic and national security interests of the United States. Title III of the E-Government Act, entitled the Federal Information Security Management Act (FISMA) of 2002, included duties and responsibilities for the National Institute of Standards and Technology, Information Technology Laboratory, Computer Security Division (CSD). In 2014, the CSD addressed its FISMA responsibilities through the following activities:

- Issued a draft Federal Information Processing Standard (FIPS): FIPS 202, *SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions*, which specifies the Secure Hash Algorithm-3 (SHA-3) family of functions on binary data. Each of the SHA-3 functions is based on an instance of the Keccak algorithm that NIST selected as the winner of the SHA-3 Cryptographic Hash Algorithm Competition.
- Issued 23 draft and final NIST Special Publications (SPs) that provide management, operational, and technical security guidelines in areas such as application whitelisting, attribute-based access control, personal identity verification and derived credentials, key management, BIOS protection, mobile device forensics, secure communications protocol implementations, third-party mobile application vetting, supply chain risk management practices, role-based cybersecurity training, industrial control systems security, systems security engineering, and security and privacy controls assessments.
- Issued 13 draft and final NIST Interagency or Internal Reports (NISTIRs) on a variety of topics, including smart grid cybersecurity, personal identity verification, Common Vulnerability Scoring System (CVSS) implementation, cloud computing forensics, identity management in Public Safety mobile networks, replication device cybersecurity, automated access management using Secure Shell, and the development process for NIST cryptographic standards and guidelines.
- Performed research and conducted outreach on standards, practices, and technologies to enable prompt and effective computer security incident handling and coordination.
- Continued the successful collaboration with the Office of the Director of National Intelligence (ODNI), the Committee on National Security Systems (CNSS), and the Department of Defense (DOD) to establish a common foundation for information security across the Federal Government, including a structured, yet flexible approach for managing information security risk across an organization. In 2014, this collaboration produced updated guidelines for assessing security and privacy controls employed in federal information systems and organizations.
- Provided assistance to agencies and the private sector through many outreach programs, including the National Initiative for Cybersecurity Education (NICE), the Federal Information Systems Security Educators’ Association (FISSEA), and the Federal Computer Security Managers’ Forum.
- Conducted workshops, awareness briefings, and outreach to CSD customers to ensure the comprehension of standards and guidelines, to share ongoing and planned activities, and to aid in scoping guidelines in a collaborative, open, and transparent manner. CSD public workshops addressed a diverse range of information security and technology topics, including cloud and mobile technologies; cyber physical systems; cryptographic key management; safeguarding health information; secure hash algorithms; supply-chain risk management; improving critical infrastructure cybersecurity; broad computer security awareness, training, education, and outreach events; and cybersecurity innovation forums.
- Engaged with international standards bodies in a variety of areas, including promoting a broader international adoption of security automation specifications. Additionally, NIST’s CSD continued to lead the Cryptographic Module Validation Program (CMVP), in conjunction with the Government of Canada’s Communications Security Establishment. The Common Criteria Evaluation and Validation Scheme (CCEVS) and CMVP facilitate security testing of IT products usable by the Federal Government.
- Solicited recommendations of the Information Security and Privacy Advisory Board (ISPAB) on draft standards and guidelines, and on information security and privacy issues.
- Produced the CSD 2014 annual report and released it as a NIST SP. CSD annual reports from fiscal years 2003 through 2014 are available on the Computer Security Resource Center (CSRC) at [http://csrc.nist.gov/publications/PubsTC.html#AnnualReports](http://csrc.nist.gov/publications/PubsTC.html#AnnualReports).

---

## Program and Project Achievements for FY 2014

In FY 2014, CSD continued to research and develop guidance for a broad array of technical areas, including supply-chain risk management; security analytics; cloud, mobile, and privacy-enhancing technologies; hardware-enabled security; and cyber-physical and embedded systems. The staff and guest researchers within CSD have collaborated with global partners from government, industry, and academia, making significant contributions to help secure critical information and infrastructures.

The following sections describe the CSD’s programs and project achievements that include extensive research and development for high-quality, cost-effective security and privacy mechanisms, standards, guidelines, tests, and metrics that address current and future computer and information security challenges.

### NIST Responsibilities Under Executive Order 13636, “Improving Critical Infrastructure Cybersecurity”

Recognizing that the national and economic security of the United States depends on the reliable functioning of its critical infrastructure, the President issued Executive Order (EO) 13636, *Improving Critical Infrastructure Cybersecurity*, in February 2013. This EO directed NIST to work with stakeholders to develop a voluntary framework – based on existing standards, guidelines, and practices − for reducing cybersecurity risks to critical infrastructures.

The Cybersecurity Framework provides a prioritized, flexible, repeatable, performance-based, and cost-effective approach to help owners and operators of critical infrastructures and other interested entities identify, assess, and manage cybersecurity-related risk, while protecting business confidentiality, individual privacy, and civil liberties.

In FY 2014, NIST continued to work with a diverse stakeholder community to develop the Framework through an open public process. This process included:
- Preparing a Preliminary Cybersecurity Framework for official public review and comment;
- Hosting a workshop at the North Carolina State University in Raleigh, North Carolina to gather input on the Preliminary Cybersecurity Framework;
- Issuing the Cybersecurity Framework in February 2014 as directed in the Executive Order;
- Publishing a companion Cybersecurity Framework Roadmap detailing high-priority areas that should be addressed in order to improve future versions of the Framework; and
- The release of a formal Request for Information (RFI), seeking feedback on awareness, experiences with the Framework, and related activities to support the use of the Framework.

Since the release of the Framework, NIST’s primary goal has been to raise awareness of the Framework and encourage its use as a tool to help industry sectors and organizations manage cybersecurity risks. NIST has strengthened its collaboration with critical-infrastructure owners and operators, industry leaders, government partners, and other stakeholders, building on interactions over the previous year that were crucial to the Framework’s development.

In FY 2015, NIST will continue to conduct stakeholder outreach and will work collaboratively with them to further understand stakeholder needs regarding tools and resources to enable a more effective use of the Framework. NIST will conduct additional public workshops, including a forum hosted by the Florida Center for Cybersecurity (FC2) located at the University of South Florida in Tampa on October 29-30, 2014. Periodic updates will be provided and additional events announced through the Framework website.  
[http://www.nist.gov/cyberframework](http://www.nist.gov/cyberframework)

**Contacts:**  
Mr. Kevin Stine  
(301) 975-4483  
kevin.stine@nist.gov  

Mr. Adam Sedgewick  
(301) 367-4678  
adam.sedgewick@nist.gov  

---

## CSD Work in National and International Standards

The following write-ups discuss the CSD’s standards activities in conjunction with the InterNational Committee for Information Technology Standards (INCITS) Technical Processes Committee Cyber Security (CS1), where CSD’s Dan Benigni served as the Chair and U.S. Head of Delegation to subcommittee SC 27, and CSD’s Sal Francomacaro served as the CS1 Vice Chair.

### CSD’s Part in National and International ISO Security Standards Processes

Figure 1 (below) shows many of the national and international standards-developing organizations (SDOs) involved in cybersecurity standardization. CSD participates in many cybersecurity standards’ activities in many of these organizations, either in leadership positions or as editors and contributors, including the BioAPI Consortium; the Bluetooth Special Interest Group (SIG): Bluetooth Security Expert Group (BT-SEG); the International Telecommunications Union - Telecommunication Standardization Sector (ITU-T); various groups within the Institute of Electrical and Electronics Engineers (IEEE) and the Internet Engineering Task Force (IETF); the North American Security Products Organization (NASPO); the Trusted Computing Group (TCG); and Accredited Standards Committee X9, Inc. (X9) (e.g. Financial Industry Standards X9F). Many of CSD’s publications have been the basis for both national and international standards projects.

![Figure 1: SDOs involved in Cybersecurity](Image_SDOs_Cybersecurity.png)

### The International Organization for Standardization (ISO)

The International Organization for Standardization (ISO) is a network of the national standards institutes of 148 countries, with representation by one member per country. The scope of ISO covers the standardization in all fields except electrical and electronic engineering standards, which are the responsibility of the International Electrotechnical Commission (IEC).

The IEC prepares and publishes international standards for all electrical, electronic, and related technologies, including electronics, magnetics and electromagnetics, electroacoustics, multimedia, telecommunication, and energy production and distribution, as well as allied subjects.

### The American National Standards Institute (ANSI)

ANSI is a private, nonprofit (501(c)(3)) organization that administers and coordinates the U.S. voluntary standardization and conformity assessment system.

---

*(Note: The document continues further detailing additional projects, validations, honors, publications, and acronyms as listed in the Table of Contents, following the same structural fidelity principles).*

---

associated  general  disciplines,  such  as  facilitates the development of American National Standards
| terminology  | and  | symbols,  | electromagnetic  |     | compatibility,  |     |     |     |     |     |     |     |     |
| ------------ | ---- | --------- | ---------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(ANSs) by accrediting the procedures of SDOs.
measurement and performance, dependability, design and
ANSI promotes the use of U.S. standards internationally,
| development,  |     | safety,  |     | and  | the  environment.   |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | --- | ---- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
advocates U.S. policy and technical positions in international
(http://www.iec.ch/about/)
and regional standards organizations, and encourages the
Joint Technical Committee 1 (JTC 1) was formed by ISO  adoption of international standards as national standards
and IEC to be responsible for international standardization
where they meet the needs of the U.S. user community.
in the field of Information Technology (http://www.iso.org/
|     |     |     |     |     |     |     | ANSI  is  | the  sole  U.S.  | representative  |     | and  | dues-paying  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | --------------- | --- | ---- | ------------ | --- |
iso/jtc1_home.html). It develops, maintains, promotes, and  member  of  the  two  major  non-treaty  international
| facilitates  | the  | IT  standards  |     | required  | by  global  markets,  |     |            |                 |      |       |           |         |         |
| ------------ | ---- | -------------- | --- | --------- | --------------------- | --- | ---------- | --------------- | ---- | ----- | --------- | ------- | ------- |
|              |      |                |     |           |                       |     | standards  | organizations:  | ISO  | and,  | via  the  | United  | States  |
meeting business and user requirements concerning: National Committee (USNC), the IEC.
•  Design and development of IT systems and tools;
INCITS is accredited by ANSI, and serves as the ANSI
Technical Advisory Group (TAG) for ISO/IEC Joint Technical
•   Performance and quality of IT products and systems;
|     |     |     |     |     |     |     | Committee  | 1.  INCITS  | is  sponsored  |     | by  | the  Information  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | -------------- | --- | --- | ----------------- | --- |
•  Security of IT systems and information;
|     |     |     |     |     |     |     | Technology  | Industry  | (ITI)  Council,  |     | a  trade  | association  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------------- | --- | --------- | ------------ | --- |
•  Portability of application programs; representing  the  leading  U.S.  providers  of  information
•  Interoperability of IT products and systems; technology products and services.
|     |     |     |     |     |     |     | INCITS  | is  organized  | into  | Technical  | Committees  |     | that  |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | ----- | ---------- | ----------- | --- | ----- |
•  Unified tools and environments;
focus on the creation of standards for different technology
•  Harmonized IT vocabulary; and
areas. Technical committees that focus on IT security and IT
•   User-friendly and ergonomically designed user inter- security-related technologies or that may require separate
faces.
security standards include:
JTC 1 consists of a number of subcommittees (SCs) and  •  B10 – Identification Cards and Related Devices;
working groups that address specific technologies. SCs that
|     |     |     |     |     |     |     | •   CS1 – Cyber Security (Dan Benigni, NIST CSD, Chair, Sal  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
produce standards relating to IT security include:
Francomacaro, NIST CSD, Vice Chair, and NIST Principal
•   SC 06 - Telecommunications and Information Exchange  Voting Member);
Between Systems;
|     |     |     |     |     |     |     | •  E22 – Item Authentication; |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
•  SC 17 - Cards and Personal Identification;
|     |     |     |     |     |     |     | •  M1 – Biometrics (Fernando Podio, NIST CSD, Chair); |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
•  SC 27 - IT Security Techniques; and
|     |     |     |     |     |     |     | •  T3 – Open Distributed Processing (ODP); |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
•   SC 37 – Biometrics (Note: Fernando Podio, NIST CSD,
|     |     |     |     |     |     |     | •  T6 – Radio Frequency Identification (RFID) Technology; |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
served as Chair).
|     |     |     |     |     |     |     | •  GIT1 – Governance of IT; and |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
JTC 1 also has:
|     |     |     |     |     |     |     | •   DAPS38 – Distributed Application Platforms and   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
•  Technical Committee 68 – Financial Services;
Services.
•   SC 2 - Operations and Procedures, including Security;
As a technical committee of INCITS, CS1 develops United
•  SC 4 – Securities;
States, national, ANSI-accredited standards in the area of
cybersecurity. Its scope encompasses:
•   SC 6 - Financial Transaction Cards, Related Media and
Operations;
|     |     |     |     |     |     |     | •  Management of information security and systems; |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
•  SC 7 – Software and Systems Engineering, and •   Management of third-party information security service
| •   SC 38 – Distributed application platforms and services  |     |     |     |     |     |     | providers;              |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
| (DAPS).                                                     |     |     |     |     |     |     | •  Intrusion detection; |     |     |     |     |     |     |
|                                                             |     |     |     |     |     |     | •  Network security;    |     |     |     |     |     |     |
1 3
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

• Cloud computing security; All input from CS1 is processed through INCITS to ANSI,
then to SC 27. It is also a conduit for getting U.S.-based new
• Supply-chain risk management;
work item proposals and U.S.-developed national standards
• Incident handling;
into the international SC 27 standards development process.
• IT security evaluation and assurance; In its international efforts, CS1 responded to all calls for U.S.
contributions and/or voting positions on all international
• Security assessment of operational systems;
security standards projects in ISO/IEC JTC 1 SC 27 in a
• Security requirements for cryptographic modules;
consistent, efficient, and timely manner.
• Protection profiles;
NIST’s CSD contributes to many of CS1’s national
• Role-based access control; and international IT security standards efforts through
its membership on CS1, where Dan Benigni served as
• Security checklists;
the nonvoting chair and Sal Francomacaro as the NIST
• Security metrics; Principal voting member. Internationally, there are over 100
• Cryptographic and non-cryptographic techniques and published standards, and almost all have been adopted as
mechanisms, including confidentiality, entity authen- U.S. national standards. There are more than 100 current
tication, non-repudiation, key management, data international standards projects. During FY 2014, eighteen
integrity, message authentication, hash functions, and new standards were published in SC 27, and all of them have
digital signatures; been recommended by CS1 for adoption as U.S. national
standards.
• Future service and applications standards supporting
the implementation of control objectives and controls
CSD’s Role in Cybersecurity
as defined in ISO 27001, in the areas of business conti-
Standardization
nuity, and outsourcing;
CSD’s cybersecurity research also plays a direct role
• Identity management, including an identity manage- in the Cybersecurity Standardization efforts of CS1 at the
ment framework, role-based access control, and single national level. The following is a description of the national-
sign-on; and level progress achieved during FY 2014 by CSD and CS1.
• Privacy technologies, including a privacy framework, The NIST Policy Machine research and development has
privacy reference architecture, privacy infrastructure, resulted in three ongoing national standards projects in CS1
anonymity and credentials, and specific privacy-en- in the early stages of development. They include:
hancing technologies.
• Next Generation Access Control –Functional Architec-
The scope of CS1 explicitly excludes the areas of ture (NGAC-FA), project number INCITS 499-2013, was
cybersecurity standardization, which is presently under published in FY 2013 and is recently beginning an early
development in INCITS B10, M1, T3, T10, and T11, as revision;
well as other standard groups, such as the Alliance for
• Next Generation Access Control – Generic Operations
Telecommunications Industry Solutions (ATIS), the IEEE,
& Abstract Data Structures (NGAC-GOADS). Serban
the IETF, the Travel Industry Association of America (TIAA),
Gavrila, NIST CSD, is the editor. The project is assigned
and Accredited Standards Committee (ASC) X9. The CS1
project number 2195-D, and the document (planned for
scope of work includes standardization in most of the same
publication in FY 2015) is out for second public review;
cybersecurity areas as are covered in the NIST CSD.
and
As the U.S. TAG to ISO/IEC JTC 1/SC 27, CS1 contributes
• Next Generation Access Control -Implementation
to the SC 27 program of work on IT Security Techniques
Requirements, Protocols and API Definitions (NGAC-IR-
in terms of U.S. comments and contributions on SC 27
PADS). Project number is 2193-D has been assigned.
standards projects; U.S. votes on SC 27 standards documents
at various stages of development; and nominates U.S. Dan Benigni also served as cybersecurity standards
experts to work on various SC 27 projects as editors, coordinator in CSD.
co-editors, or in other SC 27 leadership positions. Currently,
over a dozen CS1 members are serving as SC 27
document editors or co-editors on various standards
projects.
1 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

During FY 2015, the INCITS B10 committee, along with
CONTACT:
the active collaboration of CSD staff, plans to:
Mr. Salvatore Francomacaro • Publish Part 3 of INCITS 504;
(301) 975-6414
• Complete the amendment process for INCITS 504 Part
salvatore.francomacaro@nist.gov
1 and 2; and
(Editor Note: Mr. Dan Benigni led this program until his • Contribute to the publication of several revisions of the
recent retirement.) ISO/IEC 7816 family of standards (all relevant to FIPS
201 specifications).
CSD staff will continue to actively support relevant ID
Identity Management Standards within
management standard initiatives, such as ISO/IEC 19286
INCITS B10 and ISO JTC1/SC17
(Integrated Circuit Card (ICC) protocols and services ensuring
CSD supports identity management standardization
privacy) and ISO/IEC 18328 (ICC managed Devices).
activities through participation in national and international
standards bodies and organizations. CSD actively CSD’s investment in these activities is motivated by new
participates in the INCITS B10 committee, which is focused technical ideas that emerge from these ISO standards. For
on the interoperability of Identification Cards and Related example, INCITS 504 is an ID platform that leverages the
Devices. CSD has contributed and provided valuable FIPS 201 infrastructure to support a larger number of
feedback to many INCITS B10 standards in the development government and enterprise initiatives. In particular, INCITS
process. In addition, CSD also participates in the B10.12 504 aims to support initiatives such as the National
committee. The B10.12 committee develops interoperable Strategy for Trusted Identities in Cyberspace (NSTIC).
standards for Integrated Circuit Cards with Contacts, and it is ISO/IEC 24727 aims to create an interoperability framework
the US TAG (Technical Advisory Group) for the international that increases the resilience and scalability of identity
ISO/IEC JTC 1 SC 17 Working Groups 4 and 11. During FY 2014, management solutions and to foster domestic and
Mr. Salvatore Francomacaro, a CSD staff member; served as international interoperability.
the U.S. Head of delegation to ISO/IEC JTC 1 SC 17 WG4 and
WG11. CONTACT:
CSD provides technical and editorial support in the
Mr. Salvatore Francomacaro
development of national and international standards.
(301) 975-6414
Specifically, a CSD staff member serves as the technical
salvatore.francomacaro@nist.gov
editor of ANSI 504-1, Generic Identity Command Set (GICS).
GICS enables PIV, PIV-Interoperable (PIV-I) and Common
Access Card (CAC) card applications, and others, to be built
from a single platform. GICS defines an open platform where
identity applications can be instantiated, deployed, and used
in an interoperable way between the credential issuers and
credential users. During FY 2014, INCITS 504 Parts 1 and 2
have started an amendment process to better align them
with the new NIST SP 800-73-4 (PIV) specifications.
CSD staff also provided significant input to standards of
major interest to U.S. government agencies and U.S. markets.
CSD played a role in the development and revision of:
• ISO/IEC 7816 (Identification Cards, Integrated Circuit
Cards);
• ISO/IEC 24727 (Identification Cards, Integrated Circuit
Card Programming Interfaces); and
• ISO/IEC 24787 (Biometrics “Match On Card” Compari-
son).
1 5
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

FEDERAL INFORMATION In FY 2014, CSD worked on the following three initiatives:
SECURITY MANAGEMENT ACT • Risk Management Guidelines: SP 800-53 Revision 4,
Security and Privacy Controls for Federal Information
(FISMA) IMPLEMENTATION
Systems and Organizations, provides organizations
PROJECT
with the security controls necessary to appropriately
strengthen their information systems and the envi-
The FISMA Implementation Project focuses on: ronments in which those systems operate, and with a
• Developing a comprehensive series of standards and process for selecting the appropriate controls, which
guidelines to help federal agencies build strong cyber- contributes to systems that are resilient in the face of
security programs, defend against increasingly sophis- attacks and other threats. This “Build It Right” strategy
ticated cyber-attacks, and demonstrate compliance to is reinforced with the May 2014 publication of the Initial
security requirements set forth in legislation, Executive Public Draft (IPD) of SP 800-160, Systems Security
Orders, Homeland Security Directives, and Office of Engineering: An Integrated Approach to Building Trust-
Management and Budget (OMB) policies; worthy Resilient Systems. The implementation of SPs
800-53 and 800-160, combined with the implementa-
• Building a common understanding and reference
tion of SP 800-37, Guide for Applying the Risk Manage-
guides for organizations applying the NIST suite of
ment Framework to Federal Information Systems, and
standards and guidelines that support the NIST Risk
SP 800-137, Information Security Continuous Monitor-
Management Framework (RMF);
ing for Federal Information Systems and Organizations,
• Developing minimum criteria and guidelines for recog- provide organizations with near real-time information
nizing security-assessment organization providers as that is essential for senior leaders making ongoing
capable of assessing information systems consistent risk-based decisions affecting their critical missions and
with NIST standards and guidelines supporting the business functions.
RMF; and
• Guidelines for a Role-Based Information Security
• Conducting FISMA outreach to public and private-sec- Training Model: SP 800-16, A Role-Based Model for
tor organizations. Federal Information Technology/Cybersecurity Train-
During FY 2014, CSD continued to strengthen its ing, describes a process for developing information
collaboration with the Department of Defense (DOD), the technology/cybersecurity role-based training. Its pri-
Intelligence Community, and the Committee on National mary focus is to provide a comprehensive, yet flexible,
Security Systems (CNSS), in partnership with the Joint methodology for the development of training courses
Task Force (JTF) Transformation Initiative. The JTF partners or modules for personnel who have been identified as
continue to develop and update key cybersecurity guidelines having significant information technology/cybersecu-
for protecting federal information and information systems rity responsibilities within agencies. Agencies can use
as part of the Unified Information Security Framework. SP 800-16 to tailor the Role-Based Security Training to
Previously, the Joint Task Force developed common meet the needs of their own organization.
security guidance in the critical areas of security controls for • FISMA Outreach Activity to Public and Private Sector
information systems and organizations, security assessment Organizations: CSD conducted cybersecurity outreach
procedures to demonstrate security control effectiveness, briefings and provided support to state and local gov-
security authorizations for risk acceptance decisions, and ernments, as well as private sector organizations, on
continuous monitoring activities to ensure that decision topics of interest, such as an effective implementation
makers receive the most up-to-date information on the of the NIST RMF. In addition, CSD conducted outreach
security state of their information systems. In addition, CSD activities with academic institutions, providing infor-
began work with the General Services Administration (GSA) mation on NIST’s security standards and guidelines,
Federal Risk and Authorization Management Program exploring new areas of cybersecurity research and
(FedRAMP) to develop a high-impact security control development, and serving on cybersecurity advisory
baseline overlay for FedRAMP cloud systems in accordance panels.
with NIST standards and guidelines.
In FY 2014, CSD completed the following activities:
• Published the IPD of SP 800-53A Revision 4,
Assessing Security and Privacy Controls in Federal
1 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Information Systems and Organizations, and began  •   Continue to support federal agencies in the effective
| public comment adjudication; | implementation of the NIST RMF. |     |     |     |     |     |     |     |
| ---------------------------- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
•   Published errata versions of SPs 800-37 Revision 1 and  http://csrc.nist.gov/groups/SMA/fisma
800-53 Revision 4 to make necessary clarifications
and ensure consistency with subsequently published/
CONTACTS:
revised NIST SPs and new/updated federal policy
| requirements; | Dr. Ron Ross    |     |     |     | Ms. Pat Toth    |     |     |     |
| ------------- | --------------- | --- | --- | --- | --------------- | --- | --- | --- |
|               | (301) 975-5390  |     |     |     | (301) 975-5140  |     |     |     |
•  P  ublished Supplemental Guidance on Ongoing Autho-
|     | ron.ross@nist.gov  |     |     |     | patricia.toth@nist.gov |     |     |     |
| --- | ------------------ | --- | --- | --- | ---------------------- | --- | --- | --- |
rization to assist federal agencies in transitioning from
the static point-in-time information system security
|     | Ms. Kelley Dempsey   |     |     |     | Ms. Peggy Himes  |     |     |     |
| --- | -------------------- | --- | --- | --- | ---------------- | --- | --- | --- |
assessment and authorization model to the dynamic,
|     | (301) 975-2827  |     |     |     | (301) 975-2489  |     |     |     |
| --- | --------------- | --- | --- | --- | --------------- | --- | --- | --- |
near real-time ongoing assessment and authorization
|     | kelley.dempsey@nist.gov   |     |     |     | peggy.himes@nist.gov |     |     |     |
| --- | ------------------------- | --- | --- | --- | -------------------- | --- | --- | --- |
model;
•   Collaborated with the Department of Homeland Securi-
ty (DHS) to develop a multiple-volume Interagency Re-
BIOMETRIC STANDARDS AND
port on Automation Support for Ongoing Assessments,
ASSOCIATED CONFORMITY
which is based on NIST standards and guidelines; and
ASSESSMENT TESTING TOOLS
•   Continued the development of a preliminary draft of SP
800-18 Revision 2, Guide for Developing Security Plans
for Federal Information Systems and Organizations. NIST’s  CSD  supports  the  development  of  biometric
|     | conformance-testing  |     | methodology  |     | standards  |     | and  | other  |
| --- | -------------------- | --- | ------------ | --- | ---------- | --- | ---- | ------ |
In FY 2015, CSD intends to:
|     | conformity-assessment  |     | efforts  |     | through  | active  | technical  |     |
| --- | ---------------------- | --- | -------- | --- | -------- | ------- | ---------- | --- |
•   Finalize SP 800-53A Revision 4, Assessing Security and  participation in the development of these standards and the
Privacy Controls in Federal Information Systems and
development of associated conformance-test architectures
Organizations;
and test suites. These test tools are developed to promote
the adoption of these standards and to support users that
•  P ublish an errata update to SP 800-53 Revision 4;
|     | require  | conformance  | to  | selected  | biometric  |     | standards,   |     |
| --- | -------- | ------------ | --- | --------- | ---------- | --- | ------------ | --- |
•   Begin the automation of the SP 800-53 revision and
product developers and testing labs. CSD’s project team
public comment process in support of more timely
|     | contributes  | to  | the  development  |     | of  biometric  |     | standards  |     |
| --- | ------------ | --- | ----------------- | --- | -------------- | --- | ---------- | --- |
updates to counter threats and keep up with techno-
|     | and  leads  | the  | InterNational  | Committee  |     | for  | Information  |     |
| --- | ----------- | ---- | -------------- | ---------- | --- | ---- | ------------ | --- |
logical advancements;
|     | Technology  | Standards  | (INCITS)  |     | Technical  |     | Committee  |     |
| --- | ----------- | ---------- | --------- | --- | ---------- | --- | ---------- | --- |
•   Finalize SP 800-16, A Role-Based Model for Federal
|     | M1  –  | Biometrics  | and  | International  |     | Organization  |     | for  |
| --- | ------ | ----------- | ---- | -------------- | --- | ------------- | --- | ---- |
Information Technology / CyberSecurity Training; Standardization (ISO) and the International Electrotechnical
•   Finalize SP 800-160, Systems Security Engineering: An  Commission  (IEC)  Joint  Technical  Committee  (JTC)  1
Integrated Approach to Building Trustworthy Resilient  Subcommittee (SC) 37 – Biometrics standards bodies. The
CSD plans to continue this work in FY 2015.
Systems;
•   Publish the IPD of SP 800-171, Protecting Controlled  The development of the two versions of the Biometric
Conformance Test Software (BioCTS) continued. “BioCTS
Unclassified Information in Nonfederal Information
Systems and Organizations; for  ANSI/NIST”  (which  targets  biometric  transactions
based on the NIST SP 500-290, and SP 500-290 Revision
•   Begin the development of SP 800-60 Revision 2, Guide
1 - Data Format for the Interchange of Fingerprint, Facial
for Mapping Types of Information and Information
& Other Biometric Information) received enhanced testing
Systems to Security Categories;
features for XML files, as well as updates to begin supporting
•   Finalize SP 800-18 Revision 2, Guide for Developing  the  revision  of  SP  500-290;  for  more  information  see:
Security Plans for Federal Information Systems and
|     | http://www.nist.gov/itl/iad/ig/ansi_standard.cfm.  |     |     |     |     |     | “BioCTS  |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- |
Organizations; for ISO/IEC” (which targets several ISO/IEC biometric data
•   Expand cybersecurity outreach to include additional  interchange formats and profiles) received updates to add
|     | additional  | conformance  | test  | suites  | (CTSs)  |     | for  selected  |     |
| --- | ----------- | ------------ | ----- | ------- | ------- | --- | -------------- | --- |
state, local, and tribal governments, as well as private
sector organizations and academic institutions; and PIV  Profiles  of  biometric  data  formats  (as  specified  in
1 7
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

SP 800-76-2), as well as support for ISO/IEC 19794-4:2011  In addition to the conformance test tools, additional
Amendment 2, which is an XML encoding for the finger  supporting tools were developed and released to benefit
image data format. The latest versions of BioCTS were  users of the test tools.  They include a Data Extractor, which
released in September 2014, together with documentation  allows users to extract data from an ANSI/NIST-ITL formatted
and sample data.  file; a Directory Hash Summary program, which allows users
to generate a SHA-256 hash value for every file within the a
| Intensive  | research  | was  | performed  |     | to  study  | the  |     |     |     |     |     |
| ---------- | --------- | ---- | ---------- | --- | ---------- | ---- | --- | --- | --- | --- | --- |
given directory recursively; and enhanced statistical features
| feasibility  | of  implementing  |     | the  | existing  | conformance- |     |     |     |     |     |     |
| ------------ | ----------------- | --- | ---- | --------- | ------------ | --- | --- | --- | --- | --- | --- |
within BioCTS for both versions of BioCTS.  In addition,
| testing  | tools  within  | a  cloud-computing  |     |     | setting.  | This  |     |     |     |     |     |
| -------- | -------------- | ------------------- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- |
advanced editing features were incorporated in BioCTS for
research was conducted on an Apache Hadoop platform,
ANSI/NIST.
| investigating  | implementation  |     | requirements,  |     | benefits  | and  |     |     |     |     |     |
| -------------- | --------------- | --- | -------------- | --- | --------- | ---- | --- | --- | --- | --- | --- |
potential applications for biometric conformance testing.
To progress the work beyond the original goal of research,
the development of a solution was performed, resulting
in a working implementation of an existing CSD BioCTS
CTS (developed in Microsoft C#) being incorporated into
| a  Linux    | and  Java-based     |     | Apache    | Hadoop  | MapReduce  |          |     |     |     |     |     |
| ----------- | ------------------- | --- | --------- | ------- | ---------- | -------- | --- | --- | --- | --- | --- |
| job.  This  | work  successfully  |     | overcame  |         | several    | initial  |     |     |     |     |     |
implementation problems, and resulted in a release package
and methodology for using BioCTS software in Apache
| Hadoop                        | (for  more  information  |               | on       | Apache    | Hadoop           | see:     |     |     |     |     |     |
| ----------------------------- | ------------------------ | ------------- | -------- | --------- | ---------------- | -------- | --- | --- | --- | --- | --- |
| https://hadoop.apache.org/).  |                          |               | The      | process,  | problems,        |          |     |     |     |     |     |
| and  methods                  | used                     | to  overcome  |          | them      | were  presented  |          |     |     |     |     |     |
| at  Global                    | Identity                 | Summit        | 2014.    | BioCTS    | Web,             | an       |     |     |     |     |     |
| ASP.NET                       | Web  application         |               | that     | runs      | existing         | BioCTS   |     |     |     |     |     |
| CTSs,                         | was  updated             | to            | support  | more      | testing          | suites.  |     |     |     |     |     |
| For  more                     | information              | on            | BioCTS   | in        | the  Cloud,      | see:     |     |     |     |     |     |

http://www.nist.gov/itl/csd/biometrics/biocts_cloud.cfm.
Figure 3: Biometric Conformance
Test Software by CSD
The BioCTS software installer files, as well the ancillary
tools and sample data can be downloaded from: http://www.
nist.gov/itl/csd/biometrics/biocta_download.cfm.
|     |     |     |     |     |     |     | A            | number  of  technical  |     | contributions       | towards  the  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------------- | --- | ------------------- | ------------- |
|     |     |     |     |     |     |     | development  | of  ANSI/NIST          |     | and  international  | standards     |
were submitted. They included technical contributions on
international biometric data interchange formats and their
|     |     |     |     |     |     |     | associated  | conformance  | testing  | methodologies,  | as  well  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | -------- | --------------- | --------- |
as on the SP 500-290 Revision 1 and the associated NIEM
XML Schema. A member of the project team, Dylan Yaga,
CSD, received the INCITS Standards Service Award for his
technical excellence, performance and dedication towards
|     |     |     |     |     |     |     | supporting  | the  development  |     | of  biometric  | standards.   |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | --- | -------------- | ------------ |
(Further details of Dylan’s award is located in the Honors
and Awards section of this annual report - page 77.)
Outreach efforts in FY 2014 in support of biometric
|     |     |     |     |     |     |     | standards  | development  | and  | conformity  | assessment  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ---- | ----------- | ----------- |
Figure 2: BioCTS in the Cloud
included contributions on the test tools to the standards
developers (in support of ongoing development projects),
and presentations on ANSI/NIST and international biometric
standards and related conformity assessment activities.  The
work included the development of technical publications,
1 8
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

the review of research papers for external publications, and monthly meetings provided an opportunity to learn and
participation in conference program committees. This effort share information about ongoing research related to the
included participation in the program development of the themes and thrusts expressed in the Strategic Plan for the
Global Identity Summit conference (previously the Biometric Federal Cybersecurity Research and Development. NIST’s
Consortium Conferences), which was held September 16- CSD briefed the IWG on initiatives in privacy engineering,
18, 2014, in Tampa, Florida. The conference included nearly combinatorial testing, android application testing, cyber-
1500 attendees from 30 countries representing government, physical systems, big data, the National Initiative for
industry, and academia. NIST’s CSD supported a booth at Cybersecurity Education (NICE), and usability.
the conference’s technical exposition and a member of the
With the NITRD CSIA Senior Steering Group, CSD
project team (Dylan Yaga) presented material regarding
participated in the dialogue and planning that resulted
the conformance test tool development project. Over 140
in the creation of the National Privacy Research Forum to
speakers participated in the program.
address concerns about privacy that were voiced in recent
Global Identity Summit conference program including President’s Council of Advisors on Science and Technology
released presentations: (PCAST) reports and to develop a strategic plan for privacy
http://www.biometrics.org/bc2014/program.pdf R&D in FY 2015.
CSD is also a regular participant in the coordination
BioCTS 2014 - Biometric Conformance Test Tool
activities of the federal Special Cyber Operations
Downloads:
Research and Engineering (SCORE) Committee. SCORE
http://www.nist.gov/itl/csd/biometrics/biocta_download.cfm
enables technology transfer through the sharing of NIST
cybersecurity expertise and output. The SCORE committee
interacts with federal leaders and reports to the National
Science & Technology Council’s Committee on Homeland &
National Security.
CONTACT:
CONTACT: Mr. Bill Newhouse
(301) 975-2869
Mr. Dylan Yaga william.newhouse@nist.gov
(301) 975-6004
dylan.yaga@nist.gov
SECURITY ASPECTS OF
(Editor Note: Mr. Fernando Podio led this program until his
ELECTRONIC VOTING
recent retirement.)
In 2002, Congress passed the Help America Vote Act
(HAVA) to encourage the upgrade of voting equipment
FEDERAL CYBERSECURITY
across the United States. HAVA established the Election
RESEARCH & DEVELOPMENT
Assistance Commission (EAC) and the Technical Guidelines
(R&D) Development Committee (TGDC), chaired by the Director of
NIST. HAVA directs NIST to provide technical support to the
The Networking and Information Technology Research EAC and TGDC in efforts related to human factors, security,
and Development (NITRD) Program provides a framework and laboratory accreditation. As part of NIST’s efforts,
in which many federal agencies come together to coordinate CSD supports the activities of the EAC related to voting
their networking and IT research and development equipment security.
(R&D) efforts. CSD remained committed to the value of In the past year, NIST continued to support the EAC in
communicating its R&D efforts to other federal colleagues finalizing changes to the Voluntary Voting System Guidelines
and identifying the opportunities to support R&D efforts (VVSG) 1.1. The security guidelines were updated in FY 2012
throughout the Federal Government. to improve the auditability of voting systems, to provide
In FY 2014, the NITRD Cyber Security and Information greater software integrity protections, to expand and
Assurance (CSIA) Interagency Working Group (IWG) improve access-control requirements, and to help ensure
1 9
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

that cryptographic security mechanisms are implemented  security tools, technologies, and methodologies that provide
properly. In addition, CSD supported the efforts of the EAC  for the security and privacy of health information.
and Federal Voting Assistance Program (FVAP) of DOD to
NIST CSD continued its HIT security outreach efforts in
improve the voting process for citizens under the Uniformed  FY 2014. NIST and the Department of Health and Human
and Overseas Citizens Voting Act (UOCAVA) by leveraging
Services’ (DHHS) Office for Civil Rights (OCR) co-hosted
electronic technologies. The team worked with the TDCG’s
|     |     |     |     |     |     |     |     | the  seventh  |     | annual  | HIPAA  | Security  |     | Rule  | conference,  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ------ | --------- | --- | ----- | ------------ |
UOCAVA Working Group to develop a risk analysis on the
|     |     |     |     |     |     |     |     | Safeguarding  |     | Health  | Information:  |     | Building  |     | Assurance  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ------------- | --- | --------- | --- | ---------- |
technologies used in current UOCAVA voting processes,
through HIPAA Security, in September 2014 in Washington,
including vote-by-mail, online voter registration, electronic  D.C.  The  conference  offered  important  sessions  that
ballot delivery, and online ballot marking.
|     |     |     |     |     |     |     |     | focused      | on  broad  |           | topics      | of  interest  |       | to  the  | healthcare  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --------- | ----------- | ------------- | ----- | -------- | ----------- |
|     |     |     |     |     |     |     |     | and  health  | IT         | security  | community.  |               | Over  | 600      | in-person   |
Finally, CSD began working with NIST’s Systems and
Software  Division  (SSD)  to  explore  applying  software  and  virtual  attendees  from  federal,  state,  and  local
|            |           |     |                 |     |         |           |      | governments,  |     | academia,  |     | HIPAA-covered  |     | entities  | and  |
| ---------- | --------- | --- | --------------- | --- | ------- | --------- | ---- | ------------- | --- | ---------- | --- | -------------- | --- | --------- | ---- |
| assurance  | concepts  |     | to  electronic  |     | voting  | systems.  | The  |               |     |            |     |                |     |           |      |
business associates, industry groups, and vendors heard
initial work in this area applies the Common Weakness
|     |     |     |     |     |     |     |     | from,  and  | interacted  |     | with,  | healthcare,  |     | security,  | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ------ | ------------ | --- | ---------- | ---- |
Enumeration (CWE) list of software weaknesses to voting
|     |     |     |     |     |     |     |     | privacy  | experts  | on  | technologies  |     | and  | methodologies   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ------------- | --- | ---- | --------------- | --- |
systems. The CWE was used to assist in the categorization
of  reported  vulnerabilities  within  voting  voting-system   for safeguarding health information and for implementing
the requirements of the HIPAA Security Rule. Presentations
| security  | security-analysis  |     |     | reports.  | Additionally,  |     | the  |             |              |     |          |     |             |     |               |
| --------- | ------------------ | --- | --- | --------- | -------------- | --- | ---- | ----------- | ------------ | --- | -------- | --- | ----------- | --- | ------------- |
|           |                    |     |     |           |                |     |      | and  panel  | discussions  |     | covered  |     | a  variety  |     | of  security  |
vulnerabilities within the CWE are being mapped to the
management and technical assurance topics, including:
| Voluntary  | Voting  | System  |     | Guidelines  | (VVSG)—both  |     | the  |     |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | --- | ----------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
current and upcoming standard. •   Updates on the OCR audit and enforcement programs;
Proposed  plans  for  FY  2015,  NIST  will  continue  •   Use of the NIST Cybersecurity Framework in the
researching the applicability of software assurance concepts  healthcare sector;
| to  electronic  |     | voting  | systems  | and  | continue  | to  | support  |                                                         |     |     |     |     |     |     |     |
| --------------- | --- | ------- | -------- | ---- | --------- | --- | -------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                 |     |         |          |      |           |     |          | •   Safeguarding data using cryptographic technologies  |     |     |     |     |     |     |     |
efforts to improve the voting process for UOCAVA voters.
and strong identity and access management;
Additionally, CSD will continue security research efforts to
|     |     |     |     |     |     |     |     | •   Strategies for engaging the executive leadership to  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
support future standards development efforts, particularly
privacy and security risks; and
| in  the  areas  | of  | risks  | to  voting  | systems  |     | and  | innovative   |     |     |     |     |     |     |     |     |
| --------------- | --- | ------ | ----------- | -------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
voting system architectures. •   Case studies on safeguarding patient information, and
lessons learned for health data breaches.
http://vote.nist.gov
Keynote addresses were delivered by Darren Dworkin,
Senior Vice President of Enterprise Information Systems
CONTACTS:
and Chief Information Officer (CIO) of Cedars-Sinai Health
Mr. Andrew Regenscheid   Mr. Joshua Franklin  System, and Daniel Solove, the John Marshall Harlan Research
Professor of Law at the George Washington University Law
| (301) 975-5155               |     |     |     | (301) 975-8463           |     |     |     |         |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| andrew.regenscheid@nist.gov  |     |     |     | joshua.franklin@nist.gov |     |     |     | School. |     |     |     |     |     |     |     |
In FY 2015, NIST CSD will continue to work with diverse
healthcare stakeholders, including partners in government
|                     |     |     |     |     |     |     |     | and  industry,  |                | to  identify  |     | opportunities  |             | to  | strengthen    |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | ------------- | --- | -------------- | ----------- | --- | ------------- |
| HEALTH INFORMATION  |     |     |     |     |     |     |     |                 |                |               |     |                |             |     |               |
|                     |     |     |     |     |     |     |     | the  sector’s   | cybersecurity  |               |     | risk           | management  |     | efforts  by   |
TECHNOLOGY SECURITY
using the NIST Cybersecurity Framework. As part of its
continued outreach efforts, NIST CSD also plans to co-
| Health  | Information  |     | Technology  |     | (HIT)  | enables  | better  |     |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ----------- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
host the eighth annual Safeguarding Health Information
patient care through the secure use and sharing of health
conference with OCR.
| information.  | HIT  | leads  | to  | improvements  |     | in  | healthcare  |     |     |     |     |     |     |     |     |
| ------------- | ---- | ------ | --- | ------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
quality, reduced medical errors, increased efficiencies in care   http://www.nist.gov/healthcare/security/
| delivery  | and  |     | administration,  |     | and  |     | improved  |     |     |     |     |     |     |     |     |
| --------- | ---- | --- | ---------------- | --- | ---- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
CONTACT:
| population  | health.    |     | Central  | to                | reaching  | these       | goals  |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | -------- | ----------------- | --------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| is  the     | assurance  | of  | the      | confidentiality,  |           | integrity,  | and    |     |     |     |     |     |     |     |     |
Mr. Kevin Stine
| availability  | of         | health  | information.  |     | CSD          | works  | with      |                 |     |     |     |     |     |     |     |
| ------------- | ---------- | ------- | ------------- | --- | ------------ | ------ | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| government,   | industry,  |         | academia,     |     | and  others  | to     | provide   | (301) 975-4483  |     |     |     |     |     |     |     |
kevin.stine@nist.gov
 2 0
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

SUPPLY-CHAIN RISK services. This lack of visibility and understanding, in turn,
has decreased the control that federal departments and
MANAGEMENT (SCRM)
agencies have with regard to the decisions impacting the
FOR INFORMATION AND
inherited risks traversing the supply chain and the ability
COMMUNICATIONS to effectively manage those risks. Figure 4 (below) shows
TECHNOLOGY (ICT) how ICT supply-chain risk may be derived from adversarial
or non-adversarial threats, as well as external or internal
vulnerabilities. The likelihood of an event and the potential
Information and communication technologies (ICT)
impact of an event are also key factors.
rely on a complex, globally distributed, and interconnected
supply-chain ecosystem that is long, has geographically This project seeks to provide federal agencies with a
diverse routes, and consists of multiple tiers of outsourcing. standardized, repeatable, and feasible toolkit of technical
In addition, Federal Government information systems have and intelligence resources to strategically manage supply-
rapidly expanded in terms of capability and number, with chain risk throughout the entire lifecycle of systems,
an increased reliance on outsourcing and commercially products and services.
available products.
In FY 2014, CSD reviewed and addressed comments
These trends have caused federal departments and from the initial public draft of SP 800-161, Supply Chain Risk
agencies to have a lack of visibility and understanding Management Practices for Federal Information Systems
throughout the supply chain of how the technology being and Organizations. This document provides guidance to
acquired is developed, integrated and deployed, as well as federal departments and agencies on identifying, assessing,
the processes, procedures, and practices used to assure the and mitigating ICT supply-chain risks at all levels in their
integrity, security, resilience, and quality of the products and organizations and utilizes and builds on existing guidance in
Figure 4: ICT Supply Chain Risk 2 1
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

the unified information security framework. A second public  NATIONWIDE PUBLIC
draft of the document was published in June 2014.
|     |     |     | SAFETY BROADBAND  |     |     |     |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
In June 2014, the University of Maryland Supply Chain
|     |     |     | NETWORK (NPSBN)  |     |     |     |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
Management Center of the R. H. Smith School of Business
CYBERSECURITY
completed the fourth phase of a multi-year research project
through a NIST grant awarded in 2013. Previous phases of
the project resulted in the development of a Cyber Risk
Portal where users can conduct ICT supply-chain risk self-
assessments and gain access to a number of resources. This
phase of the project deployed wide-scale testing of the
portal and made improvements to the security infrastructure
and applications.
NIST awarded the University of Maryland Supply Chain
Management Center an additional grant in 2014 to define an
effective engagement model that will enable representatives
of stakeholder organizations to come together in person
and online to learn how to map and manage their critical
ICT supply-chain risks using the portal-based tool set. The
project will be completed in April 2015.
Source: http://www.pscr.gov/
In FY 2015, CSD will:
•  Publish SP 800-161; In February 2012, Congress passed the Middle Class
|     |     |     | Tax  Relief  | and  | Job  | Creation  | Act.  One  | portion  | of  this  |
| --- | --- | --- | ------------ | ---- | ---- | --------- | ---------- | -------- | --------- |
•   Research and develop tools and guidance to help
|     |     |     | legislation  | calls  | for  the  | establishment  |     | of  a  | nationwide,  |
| --- | --- | --- | ------------ | ------ | --------- | -------------- | --- | ------ | ------------ |
agencies effectively conduct criticality analysis and  interoperable public-safety broadband network based on
other aspects needed to manage supply-chain risk;
the 3rd Generation Partnership Project’s (3GPP) Long-Term
•   Continue to co-chair Working Group 2 of the White  Evolution (LTE) technology. The network will be deployed
House’s Comprehensive National Cybersecurity Initia- and operated by the First Responder Network Authority
tive (CNCI) 11, Develop a Multi-Pronged Approach for  (FirstNet). The planned National Public Safety Broadband
Global Supply Chain Risk Management; and Network (NPSBN) will “create a much needed nationwide
interoperable broadband network that will help police,
•   Begin researching best practices and developing an
|     |     |     | firefighters,  |     | emergency  | medical  | service  | professionals  |     |
| --- | --- | --- | -------------- | --- | ---------- | -------- | -------- | -------------- | --- |
organizational strategy for supply-chain risk manage-
and other public safety officials stay safe and do their
ment in response to the NIST Roadmap for Improving
jobs.”(http://www.ntia.doc.gov/category/public-safety).
Critical Infrastructure Cybersecurity.
NIST is directed to establish a list of certified devices and
ICT SCRM Team email: scrm-nist@nist.gov
required components to be used by public safety officials,
vendors, and other interested parties for interacting with
CONTACTS: the nationwide network. NIST is also directed to conduct
research and development that supports the acceleration
Mr. Jon Boyens      Ms. Celia Paulsen  and advancement of the nationwide network.
| (301) 975-5549       |     | (301) 975-5981         |     |            |      |            |      |        |           |
| -------------------- | --- | ---------------------- | --- | ---------- | ---- | ---------- | ---- | ------ | --------- |
|                      |     |                        | In  | FY  2014,  | CSD  | supported  | the  | joint  | National  |
| jon.boyens@nist.gov  |     | celia.paulsen@nist.gov |     |            |      |            |      |        |           |
Telecommunications and Information Administration (NTIA)
and NIST Public Safety Communications Research (PSCR)
program (http://www.pscr.gov) with efforts in public-safety
|     |     |     | mobile-application  |     | security,  | identity  | management,  |     | and  |
| --- | --- | --- | ------------------- | --- | ---------- | --------- | ------------ | --- | ---- |
enabling cybersecurity capabilities on the PSCR 700 MHz
LTE demonstration network located in Boulder, Colorado.
In February 2014, CSD, in cooperation with the Association
|     |     |     | of  Public-Safety  |          | Communications  |         | Officials    |     | (APCO)     |
| --- | --- | --- | ------------------ | -------- | --------------- | ------- | ------------ | --- | ---------- |
|     |     |     | International      |          | and  FirstNet,  | held    | a  half-day  |     | workshop   |
|     |     |     | titled             | “Public  | Safety          | Mobile  | Application  |     | Security   |
2 2
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Requirements”. The outcome of that workshop is captured  SECURITY OF CYBER-
| in  Draft  | NISTIR  8018,  Public Safety Mobile Application  |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PHYSICAL SYSTEMS (CPS)
| Security Requirements Workshop Summary. At  |     |     |     |     | PSRC’s  |     |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Annual Public Safety Broadband Stakeholder Conference
|     |     |     |     |     |     | Cyber-Physical  |     | Systems  | (CPS)  |     | will  provide  |     | the  next  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ------ | --- | -------------- | --- | ---------- |
in June 2014, CSD organized and moderated a panel titled
|     |     |     |     |     |     | generation  | of  | “smart,”  | co-design  |     | and  | co-engineered  |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ---------- | --- | ---- | -------------- | --- |
“Mobile Applications Security for Public Safety”.
|     |     |     |     |     |     | interacting  | networks  |     | of  physical  |     | and  | computational  |     |
| --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ------------- | --- | ---- | -------------- | --- |
CSD developed Draft NISTIR 8014, Considerations for
components. CPS is commonly used in the nation’s critical
Identity Management in Public Safety Mobile Networks,
|     |     |     |     |     |     | infrastructure  |     | and  includes  | systems  |     | in  the  | electric  | grid,  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- | -------- | --- | -------- | --------- | ------ |
that provides a brief introduction to identity management,  manufacturing,  healthcare,  and  transportation  sectors.
| summarizes  | existing  guidance  |     | (including  |     | OMB-04- |           |     |                 |     |              |     |              |     |
| ----------- | ------------------- | --- | ----------- | --- | ------- | --------- | --- | --------------- | --- | ------------ | --- | ------------ | --- |
|             |                     |     |             |     |         | Composed  | of  | heterogeneous,  |     | potentially  |     | distributed  |     |
04,  E-Authentication  Guidance  for  Federal  Agencies;  components  and  systems,  CPS  provides  a  promise  of
| Homeland  | Security  Presidential  |     | Directive  | 12  | (HSPD12):  |            |             |      |              |     |          |      |           |
| --------- | ----------------------- | --- | ---------- | --- | ---------- | ---------- | ----------- | ---- | ------------ | --- | -------- | ---- | --------- |
|           |                         |     |            |     |            | increased  | efficiency  | and  | interaction  |     | between  | the  | digital   |
Policy for a Common Identification Standard for Federal
and physical worlds. However, assuring that these emerging
Employees  and  Contractors;  and  NIST  SP  800-63-2,  and  evolving  systems  are  reliable,  robust,  resilient,
Electronic Authentication Guideline), and describes possible
trustworthy, secure, and that they protect the privacy of
identity  tokens/credentials  that  could  be  supported  by   information poses a unique cybersecurity challenge.
mobile devices.
|     |     |     |     |     |     | CPS  | present  | unique  | challenges,  |     | including  | the  | need  |
| --- | --- | --- | --- | --- | --- | ---- | -------- | ------- | ------------ | --- | ---------- | ---- | ----- |
CSD participated in the standards development process  for integration with legacy components and allowance for
for LTE technology within the 3rd Generation Partnership
emerging technologies, and real-time response in support
Project (3GPP) supporting security requirements for public
of extremely high availability, predictability, and reliability.
safety that are related to Proximity Services (ProSe), Group  Cybersecurity is an important crosscutting discipline that
| Communication  | System  | Enablers  | (GCSE),  | and  | Mission  |               |     |            |                 |     |          |              |     |
| -------------- | ------- | --------- | -------- | ---- | -------- | ------------- | --- | ---------- | --------------- | --- | -------- | ------------ | --- |
|                |         |           |          |      |          | is  critical  | to  | the  safe  | and  resilient  |     | design,  | development  |     |
Critical Push-To-Talk (MCPTT). In addition, CSD broadened  and  operation  of  CPS.  Addressing  the  opportunities
its scope within the Internet Engineering Task Force (IETF)
and challenges of CPS requires a broad collaboration to
to include efforts related to public safety.
develop a common foundation to work from, including a
|     |     |     |     |     |     | consensus  | definition,  |     | vocabulary,  | reference  |     | architecture,  |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ------------ | ---------- | --- | -------------- | --- |
In FY 2015, CSD will continue representing public safety
in international standardization efforts, such as the IETF   and a shared understanding of the essential roles of timing,
cybersecurity and data interoperability. CSD is researching
| and  3GPP.  | CSD  will  work  | to  | implement  | and  | exercise  |     |     |     |     |     |     |     |     |
| ----------- | ---------------- | --- | ---------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
cybersecurity  capabilities  in  the  PSCR  700  MHz  LTE  the cybersecurity needs of the broader landscape of CPS,
demonstration  network,  conduct  research  into  mobile  by leveraging CSD’s expertise in cybersecurity in different
domains and applications of CPS (such as industrial control
authentication solutions to support the different public-
safety  disciplines,  and  investigate  mobile  application- systems,  smart  grid,  hardware-enabled  security,  and
embedded systems).
security services to support the security requirements of
| public-safety  | mobile  applications.  |     | CSD  | will  continue  | to  |     |     |     |     |     |     |     |     |
| -------------- | ---------------------- | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In June 2014, NIST established the CPS Public Working
engage the public-safety communications community by
Group (PWG), which is open to all, to foster and capture
organizing workshops and conferences; and participating  inputs  from  those  involved  in  CPS,  both  nationally  and
in events such as APCO’s Annual Meeting, PSRC’s Annual
|     |     |     |     |     |     | globally.  | CSD  | is  working  | in  | collaboration  |     | with  | NIST’s  |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ------------ | --- | -------------- | --- | ----- | ------- |
Public Safety Broadband Stakeholder Conference, and the  Engineering Laboratory (EL) Smart Grid and Cyber-Physical
International Wireless Communications Expo (IWCE).
|     |     |     |     |     |     | Systems  | Program  | Office,  | NIST’s  | Physical  |     | Measurement  |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | ------- | --------- | --- | ------------ | --- |
Laboratory Time and Frequency Division, ITL’s Software
CONTACTS: and  Systems  Division  and  ITL’s  Advanced  Networking
Technologies Division to lead a public-private working group
Ms. Sheila Frankel    Dr. Nelson Hastings  of government, academia, and industry stakeholders. The
| (301) 975-3297  |     |     | (301) 975-5237  |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CPS PWG consists of five technical subgroups:
| sheila.frankel@nist.gov  |     |     | nelson.hastings@nist.gov |     |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•  Definition, Vocabulary, and Reference Architecture;
•  Use Cases;
•  Cybersecurity and Privacy;
•  Data Interoperability; and
•  Timing and Synchronization.
2 3
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

Each subgroup consists of co-leads from academia,  SMART GRID CYBERSECURITY
| industry  and       | NIST.  | CSD      | co-leads  |     | the  Cybersecurity  |             | and    |     |     |     |     |     |     |
| ------------------- | ------ | -------- | --------- | --- | ------------------- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
| Privacy  subgroup   |        | focused  |           | on  | identifying         | strategies  |        |     |     |     |     |     |     |
| for  cybersecurity  |        | and      | privacy   | in  | CPS,  and           | will        | work   |     |     |     |     |     |     |
collaboratively with the other subgroups to ensure that
| cybersecurity  | is  | included  | as  | a  design  | principle  |     | during  |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | ---------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
development.
| In  2015,  | the  | CPS  | PWG  | will  | publish  | an  integrated  |     |     |     |     |     |     |     |
| ---------- | ---- | ---- | ---- | ----- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Framework that includes the work of the five technical
subgroups and begin work on a CPS Technology Roadmap,
which will identify opportunities for a coordinated effort
on key technical challenges. The CPS PWG deliverables will
| be  technology  |     | and  business-model  |     |     | neutral,  | and  | freely  |     |     |     |     |     |     |
| --------------- | --- | -------------------- | --- | --- | --------- | ---- | ------- | --- | --- | --- | --- | --- | --- |
available online and intended for open use by all stakeholders.
Additionally, in 2015, CSD, in conjunction with NIST’s
Engineering Laboratory, Intelligent Systems Division, will

finalize SP 800-82 Revision 2, Guide to Industrial Control
Systems Security. CSD will also continue to participate in the
International Society of Automation (ISA) 99 Committee,
Figure 5: Smart Meter
which develops and establishes standards, recommended
practices, technical reports, and related information that
The major elements of the smart grid are: information
define procedures for implementing electronically secure
|             |             |      |          |     |          |      |           | technology,  | industrial  |                 | control  | systems/operational  |      |
| ----------- | ----------- | ---- | -------- | --- | -------- | ---- | --------- | ------------ | ----------- | --------------- | -------- | -------------------- | ---- |
| industrial  | automation  | and  | control  |     | systems  | and  | security  |              |             |                 |          |                      |      |
|             |             |      |          |     |          |      |           | technology,  | and  the    | communications  |          | infrastructure.      | The  |
practices, and for assessing electronic security performance.
infrastructure is used to send command information across
http://www.nist.gov/cps/ the electric grid from generation to distribution systems, and
http://www.nist.gov/cps/cpspwg.cfm to exchange usage and billing information between utilities
|     |     |     |     |     |     |     |     | and  their  | customers.  | Key  | to  | the  successful  deployment  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ---- | --- | ---------------------------- | --- |
CONTACTS: of the smart grid infrastructure is the development of the
|     |     |     |     |     |     |     |     | cybersecurity  | strategy  | that  | includes  | cybersecurity  | as  a  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ----- | --------- | -------------- | ------ |
Ms. Victoria Yan Pillitteri    Ms. Suzanne Lightman  design consideration for new and emerging systems, and
| (301) 975-8542  |     |     |     | (301) 975-6442  |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
an approach to adding cybersecurity into existing systems.
victoria.pillitteri@nist.gov   suzanne.lightman@nist.gov The electric grid is critical to the economic and physical well-
being of the nation, and emerging cyber threats targeting
power systems highlight the need to integrate advanced
security to protect critical assets.
24
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

The Smart Grid Interoperability Panel (SGIP) became a Future activities include working with the SGIP
membership-supported organization in January 2013. The Committees, Domain Expert Working Groups, and Priority
SGIP Cybersecurity Working Group (CSWG) was renamed Action Plans to integrate cybersecurity into their work
the Smart Grid Cybersecurity Committee (SGCC), and efforts. Additionally, the SGIP SGCC will continue to
continues to be led by a NIST representative in support of collaborate with industry, academia, other working groups,
responsibilities identified in the Energy Independence and and government agencies to address the cybersecurity
Security Act of 2007. The SGCC chair is a voting member of needs for the smart grid.
the SGIP Technical Committee, and serves as an ex-officio
In FY 2015, CSD will continue to support the SGCC
Director of the Board. In addition, the SGIP SGCC continues
in the evaluation of the cryptographic methods used
to include additional leadership by a management team
in standards, practices, guidelines, and other technical
comprised of three volunteer vice-chairs (representing the
documents for inclusion in the SGIP CoS. In addition to the
Department of Energy (DOE), an electric utility, and a smart
SGIP SGCC activities, CSD will also coordinate with NIST’s
grid vendor) and a volunteer secretariat.
Engineering Laboratory (EL) and Smart Grid Program Office
In 2014, the SGCC contributed to the update of NISTIR on the development of a Cybersecurity Smart Grid Test
7628 Revision 1, Guidelines for Smart Grid Cybersecurity, Lab, part of the NIST Smart Grid Testbed Facility now under
which was published in September, following a public construction. CSD will also collaborate with ITL’s Software
comment period and comment resolution by the and Systems Division on cybersecurity research in relation
SGCC members. The revision updates and expands the to the IEEE 1588, Precision Time Protocol, a standard on time
development strategy, cryptography and key management, synchronization that is used for the electric grid and other
privacy, vulnerability classes, research and development special-purpose industrial automation and measurement
topics, standards review, and key power-system use cases networks.
to reflect changes in the smart grid environment since
http://www.nist.gov/smartgrid
2010. In addition to the revision of NISTIR 7628, the SGCC
http://www.sgip.org
have focused on developing documents to be published
through SGIP on cybersecurity risk management, a User’s
CONTACTS:
Guide for NISTIR 7628, cloud computing for the smart grid,
and a mapping between NISTIR 7628 and the Framework
Ms. Victoria Yan Pillitteri Ms. Tanya Brewer
for Improving Critical Infrastructure Cybersecurity. Work in
(301) 975-8542 (301) 975-4534
these areas is completed through SGCC subgroups, which
victoria.pillitteri@nist.gov tbrewer@nist.gov
are created and disbanded on an as-needed basis.
The SGCC also continues to support the SGIP Catalog Mr. Quynh Dang
of Standards (CoS), a compendium of standards, practices, (301) 975-3610
guidelines and other technical documents considered qdang@nist.gov
relevant for the development of a robust, secure, and
interoperable smart grid. Through the ongoing efforts of the
SGCC, these documents are reviewed for cybersecurity, and CYBERSECURITY
recommendations are made for including cybersecurity in
AWARENESS, TRAINING,
future revisions and in the implementation of the standards.
EDUCATION, AND OUTREACH
CSD supports the SGCC in assessing the security of the
cryptographic methods used in these standards, practices,
guidelines, and other technical documents. In many cases,
National Initiative for Cybersecurity
the standards bodies have taken the results of the reviews
Education (NICE)
and modified the standards or documents to address NIST
NIST has been the lead for the National Initiative for
recommendations. The SGCC has worked closely with some
Cybersecurity Education (NICE) since its inception in 2010.
of the standards bodies to ensure that the recommendations
NICE is responsive to President Obama’s declaration that
are interpreted correctly and that the mitigation strategies
the “cyber threat is one of the most serious economic
selected meet the intent of the NISTIR 7628 high-level
and national security challenges we face as a nation” and
security requirements. The result is cybersecurity “baked-in”
“America’s economic prosperity in the 21st century will
to the standards, rather than “bolted-on” after the standard
depend on cybersecurity.”
is implemented.
2 5
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

NICE  is  an  initiative  that  enhances  the  overall  integrate  the  NICE    focus  on  cybersecurity  workforce,
cybersecurity posture of the United States by accelerating  education, and training within NIST Special Publications
the  availability  of  educational  and  training  resources  and informational reports while promoting the value of
designed to improve the cybersecurity skills, and knowledge  the National Cybersecurity Workforce Framework (NCWF)
of our nation’s students and workforce. and the forthcoming Department of Defense Cyberspace
Workforce Strategy as resources that address cybersecurity
NIST’s CSD is leading the NICE initiative working from
workforce needs.
| the  strengths  |     | and  energy  | of  | more  | than  | 20  federal   |     |     |     |     |     |
| --------------- | --- | ------------ | --- | ----- | ----- | ------------- | --- | --- | --- | --- | --- |
departments  and  agencies  leveraging  each  of  their  http://www.nist.gov/nice/
relationships with academia and industry sectors to ensure
| coordination,  |     | cooperation,  | focus,  | public  |     | engagement,  |     |     |     |     |     |
| -------------- | --- | ------------- | ------- | ------- | --- | ------------ | --- | --- | --- | --- | --- |
CONTACTS:
technology transfer and sustainability. NIST will highlight
these  activities,  engage  various  stakeholder  groups  and  Mr. Bill Newhouse   Dr. Ernest McDuffie (retired)
create forums for sharing information and leveraging best  NICE Program Manager   FY 2014 NICE Lead
(301) 975-2869
practices.
william.newhouse@nist.gov
CSD is home to the NIST NICE Leadership Team that
focuses on the following activities:
Computer Security Resource Center
•   Developing planning documents and building consen-
(CSRC)
sus on the strategy and implementation activities of
| NICE; |     |     |     |     |     |     | The CSRC, CSD’s website, is one of the most visited  |                  |             |      |                 |
| ----- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | ---------------- | ----------- | ---- | --------------- |
|       |     |     |     |     |     |     | websites                                             | at  NIST.  CSRC  | encourages  | the  | broad  sharing  |
•   Utilizing a newly established public-private working
|     |     |     |     |     |     |     | of  information  | security  | tools  and  | practices,  | provides  a  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --------- | ----------- | ----------- | ------------ |
group to make progress towards NICE’s goals;
resource for information security standards and guidelines,
•   Promoting the use of data-driven initiatives within  and  identifies  and  links  key  security  web  resources  to
NICE; support  industry  and  government  users.  CSRC  is  an
•   Facilitating cross-functional cooperation among federal  integral component of all of the work that CSD conducts
and produces. It is CSD’s repository for anyone wanting to
departments and agencies by coordinating meetings,
facilitating discussions, and disseminating information; access these documents and other valuable security-related
information. During FY 2014, CSRC had more than 54 million
•   Promoting the initiative and its efforts by representing
page views and downloads.
NICE and speaking at cybersecurity events nationwide;
•   Planning and hosting an annual workshop to promote
and support the evolving issues in cybersecurity work-
force and education; and
•   Coordinating with other federal initiatives and efforts
related to NICE.
| The        | NICE     | leadership     | team  | attended     | many  | events,   |     |     |     |     |     |
| ---------- | -------- | -------------- | ----- | ------------ | ----- | --------- | --- | --- | --- | --- | --- |
| symposia,  | forums,  | competitions,  |       | educational  |       | outreach  |     |     |     |     |     |
meetings, and workshops to promote the activities within
NICE. The team continued its leadership of the Office of
| Personnel  | Management  |     | (OPM)  | Cross-Agency  |     | Priority  |     |     |     |     |     |
| ---------- | ----------- | --- | ------ | ------------- | --- | --------- | --- | --- | --- | --- | --- |
Goal: “Closing Skills Gap” for IT/Cybersecurity focused on
reducing cybersecurity workforce gaps and supported the
| goals of the White House’s Ready to Work initiative.  |            |      |                 |     |              |       |     |     |     |     |     |
| ----------------------------------------------------- | ---------- | ---- | --------------- | --- | ------------ | ----- | --- | --- | --- | --- | --- |
| In                                                    | FY  2015,  | CSD  | will  continue  |     | to  promote  | the   |     |     |     |     |     |
coordination of existing and future cybersecurity education,
training, and workforce activities. The Fifth annual NICE  Figure 6: CSRC Website Visitors For Past 5 Years
| Workshop  | will  | take  | place  on  | November  |     | 5-6,  2014  | in  |     |     |     |     |
| --------- | ----- | ----- | ---------- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
Columbia, Maryland (http://csrc.nist.gov/nice/events.html).
| The  CSD  | will  | also  identify  | opportunities  |     | to  | extend  and  |     |     |     |     |     |
| --------- | ----- | --------------- | -------------- | --- | --- | ------------ | --- | --- | --- | --- | --- |
2 6
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

CSRC is the primary gateway for gaining access to NIST Federal Computer Security Program
computer security publications, standards, and guidelines, Managers’ Forum
and serves as a vital link to CSD’s customers. Publications The Federal Computer Security Program Managers’
are organized to help users locate relevant information Forum is sponsored by NIST to promote the sharing of
quickly and are arranged by topic, relevant security control security-related information among federal agencies. The
family, and legal requirements. Forum, which serves more than 1100 members, strives to
In addition to CSRC, CSD maintains a publication provide an ongoing opportunity for managers of federal
announcement mailing list. This free e-mail list notifies information security programs to exchange information
subscribers about publications that have been posted to the security materials in a timely manner, build upon the
CSRC website, along with announcing new CSD-sponsored experiences of other programs, and reduce possible
events and important news or announcements. The e-mail duplication of effort. It provides a mechanism for NIST to
list is a valuable tool for more than 56 000 subscribers from share information directly with federal agency information
the Federal Government, industry, academia, and individuals security program managers in fulfillment of NIST’s
with a personal interest in IT security worldwide. Individuals leadership mandate under FISMA. It assists NIST in
who are interested in subscribing to this list should visit establishing and maintaining relationships with other
http://csrc.nist.gov/publications/subscribe.html for more individuals or organizations that are actively addressing
information. information security issues within the Federal Government.
NIST’s CSD serves as the Secretariat of the Forum, providing
During FY 2014, the CSRC underwent what the CSD
necessary administrative and logistical support. Patricia Toth
terms as “Quick Fixes” to the CSRC website. These “Quick
serves as the Chairperson.
Fixes” will improve the overall navigation experience on
CSRC. The CSRC homepage was streamlined by providing The Forum maintains an extensive email subscription
hot topics (these hot topics are the most popular projects/ service. Participation in the service is only open to Federal
programs that have webpages), updated references in Government employees who participate in the management
the Useful Resources section, and an improved News and of their organization’s information system security
Events section. The homepage was condensed to reduce program. The Forum also holds bimonthly meetings and an
the amount of scrolling on the page. Another improvement annual two-day conference to discuss current issues and
made to the CSRC website was the dropdown menus, developments of interest to those responsible for protecting
which appear on all pages. In previous years, the division’s sensitive (unclassified) federal systems.
projects/programs listings were placed under the division’s Topics of discussion at Forum meetings in FY 2014
group layout. Now, the projects/programs listings are under included briefings from various federal agencies on
their own category (Ex. Education & Outreach category, a Controlled Unclassified Information (CUI) Implementation
project falling under this category: Small and Medium-Sized Activities, Cross Agency Priority (CAP) Goals, Automated
Business (SMB) Outreach). The CSRC team created an A to Assessment Practicals, Automated Assessment Concepts
Z listing of the webpages for all of CSD’s projects/programs Supporting Information Security Continuous Monitoring
in order to ease the finding of a particular area. (ISCM), NIST’s Role in Ongoing Assessments, Ongoing
Plans for FY 2015 for the CSRC website will include Authorization Clarifying and Amplifying Guidance, and the
moving the CSRC website to a content management system National Cybersecurity Framework.
(CMS). Moving to a CMS is expected to improve the website’s This year’s annual two-day offsite meeting featured
functionality. updates on the computer security activities of the
Questions on the website can be sent to the CSRC Government Accountability Office (GAO), General Services
Webmaster at: webmaster-csrc@nist.gov. Administration (GSA), Bureau of the Fiscal Service,
Department of State, National Security Council, Department
of Homeland Security (DHS), and NIST. Technical sessions
CONTACTS:
included briefings on updates from NIST Computer Security
Mr. Patrick O’Reilly Ms. Judy Barnard Division (CSD), FedRAMP Overview and Security Processes,
(301) 975-4751 (301) 975-5502 Supply Chain Risk Management, Ongoing Authorization,
patrick.oreilly@nist.gov jbarnard@nist.gov Fiscal Service’s Risk-Based ISCM Strategy, Derived PIV
Credentials, Cybersecurity Training, Incident Response,
White House Initiatives, FY 2015 FISMA Metrics and recent
updates to the FISMA publications.
2 7
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

The Forum plays a valuable role in helping NIST and  The 27th Annual FISSEA Conference occurred March
other federal agencies to develop and maintain a strong,  18-20, 2014, at NIST. Approximately 180 information system
proactive stance in the identification and resolution of new  security professionals and trainers attended from federal
strategic and tactical IT security issues as they emerge. The  agencies, academia, and industry.
number of members on the email list has grown steadily and
|     |     |     |     |     |     |     | This  | year’s  theme  | was,  “Partners in Performance:  |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------------- | -------------------------------- | --- |
provides a valuable resource for federal security program
Shaping the Future of Cybersecurity Awareness, Education,
managers. To join, email your name, affiliation, address,
and Training.” The program team solicited presentations that
phone number, title, and confirmation that you are a federal
reflected current projects, trends, and future initiatives in
employee to sec-forum@nist.gov.
federal security programs. Attendees gained new techniques
http://csrc.nist.gov/groups/SMA/forum/
for developing/conducting training, cost-effective practices,
workforce development, free resources and contacts, as
CONTACTS: well as an update on National Initiative for Cybersecurity
Education (NICE) activities.
| Ms. Patricia Toth   |     |     |     | Ms. Peggy Himes  |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
Keynote presentations were given by: Dr. Ron Ross,
| Chair  |     |     |     | Administration  |     |     |     |     |     |     |
| ------ | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
NIST Fellow, CSD; Ambassador  Karen Kornbluh, Executive
| (301) 975-5140  |     |     |     | (301) 975-2489  |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
ptoth@nist.gov      peggy.himes@nist.gov Vice President of External Affairs for Nielsen, former U.S.
Ambassador to the Organization for Economic Cooperation
and Development (OECD); and Ms. Linda Cureton, Chief
Federal Information Systems Security  Executive Officer and Founder of Muse Technologies, Inc.
| Educators’ Association (FISSEA) |     |     |     |     |     |     | (former NASA CIO). |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
The Federal Information Systems Security Educators’
Presenters represented NIST, DHS, DOS, NSA, NASA,
Association (FISSEA), founded in 1987, is an organization
|     |     |     |     |     |     |     | IRS,  private  | industry  and  | academia.  Attendees  | had  an  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------------- | --------------------- | -------- |
run by NIST for information system security professionals to
opportunity to visit fifteen vendors on the second day. A
assist federal agencies in meeting their information system’s
Government Best Practice Poster and Demonstration session
security awareness, training, and education responsibilities.
was held on the third day, which provided an opportunity for
FISSEA strives to elevate the general level of information
agencies to share and tell about their specific awareness and
system security knowledge for the Federal Government and

the federal workforce. It also seeks to assist the professional

development of its members.

| FISSEA  | membership  |     | is  | open  to  information  |     | system  |     |     |     |     |
| ------- | ----------- | --- | --- | ---------------------- | --- | ------- | --- | --- | --- | --- |
security professionals, professional trainers and educators,

| and managers responsible for information system security  |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
training programs in federal agencies, as well as contractors

| of  these    | agencies      | and  | faculty     | members        | of  | accredited   |     |     |     |     |
| ------------ | ------------- | ---- | ----------- | -------------- | --- | ------------ | --- | --- | --- | --- |
| educational  | institutions  |      | who         | are  involved  | in  | information  |     |     |     |     |
| security     | training      | and  | education.  | To  become     |     | a  FISSEA    |     |     |     |     |

| member;  | all  that  | is  | required  | is  a  willingness  |     | to  share  |     |     |     |     |
| -------- | ---------- | --- | --------- | ------------------- | --- | ---------- | --- | --- | --- | --- |
products, information, and experiences. A working group

| meets monthly to administer business activities. |            |            |              |       |          |             |     |     |     |     |
| ------------------------------------------------ | ---------- | ---------- | ------------ | ----- | -------- | ----------- | --- | --- | --- | --- |
| FISSEA                                           | maintains  |            | a  website,  | a     | mailing  | list,  and  |     |     |     |     |
| participates                                     | in         | a  social  | networking   | site  | as  a    | means  of   |     |     |     |     |

communication for its members. NIST’s CSD assists FISSEA
| with its operations by providing staff support for several of  |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

its activities and by being FISSEA’s host agency.

FISSEA membership in 2014 spanned federal agencies,

industry, military, contractors, state governments, academia,

the press, and foreign organizations in a total of ten countries.

The 700 federal agency members represent 89 agencies

from the executive and legislative branches of government. 2014 FISSEA Educator of the Year Award:
Sam Maroon, FITSI Foundation / Wounded Warrior
| 2 8                                             |     |     |     |     |     |     |     | Cyber Combat Academy |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |                      |     |     |

training programs. In addition, there was a panel discussion Peers Choice Award winners voted on at the March
of former FISSEA Educator of the Year recipients - influential Conference:
leaders who have demonstrated a superior level of expertise,
• Poster Winner: Deborah Coleman – Department of
effectiveness, and dedication to the advancement of
Education OCIO Information Assurance Services;
the information system security awareness, training and
• Website Winner: Kimberly Conway, Sara Fitzgerald,
education profession. They discussed their best and worst
Steven Van Brackle – Food and Drug Administration;
ideas for improving cybersecurity programs, shared
significant activities, and answered questions. • Motivational Item Winner: Nicole Rousseau – United
Technologies Corporation;
The FISSEA Educator of the Year Award was
established to recognize and honor a contemporary who is • Newsletter Winner: Kimberly Conway, Sara Fitzgerald,
making special efforts to create, build, manage, or inspire Steven Van Brackle – Food and Drug Administration;
an information system security awareness, training, or and
education program. This year’s Educator of the Year award
• Role-Based Training Winner: Susan Farrand – Supply
was presented to Sam Maroon, Federal IT Security Institute
Chain Risk Management Resource Center, Department
(FITSI) Foundation/ Wounded Warrior Cyber Combat
of Energy.
Academy. The nomination letter recommending him for this
Attendee networking is a valuable benefit of attending
award made the following statements: “Mr. Maroon deserves
the FISSEA conference. The conference continues to be
this award for his unflagging work supporting this country’s
a valuable forum in which individuals from government,
injured servicemen and women in transitioning them to
industry, and academia who are involved with information
the cyber battlefield through the Wounded Warrior Cyber
systems/cybersecurity workforce development (awareness,
Combat Academy. … He has donated at least 300 hours
training, education, certification, and professionalization)
of his own personal time…” The full nomination letters are
learn of ongoing and planned training and education
posted on the FISSEA website.
programs and initiatives. It provides NIST the opportunity
FISSEA conference events also included announcing the
to provide assistance to departments and agencies as they
winners of FISSEA contests and awarding prize drawings.
work to meet their FISMA responsibilities.
The FISSEA Security Awareness, Training & Education
The 2015 FISSEA conference is planned for March 24-25,
Contest includes five categories from one of FISSEA’s
2015, at NIST.
three key areas of Awareness, Training, and Education.
The winner is selected from each category and awarded a http://csrc.nist.gov/fissea
certificate. The categories include: (1) awareness poster, (2) fisseamembership@nist.gov
motivational item (e.g., pens, stress relief items, t-shirts), (3)
awareness website, (4) awareness newsletter, and (5) role-
CONTACTS:
based training & education.
Ms. Patricia Toth Ms. Peggy Himes
The winners of the 2014 FISSEA Awareness, Training
(301) 975-5140 (301) 975-2489
and Education Contest are:
patricia.toth@nist.gov peggy.himes@nist.gov
• Poster Winner: Alexis Benjamin – Department of State,
Office of Computer Security;
Information Security and Privacy
• Website Winner: Emma Gilli, Daisy Karaiosifoglou, Dan
Advisory Board (ISPAB)
Acuff, and Nicole Rousseau – United Technologies
The Information Security and Privacy Advisory Board
Corporation;
(ISPAB) is a federal advisory committee with specific
• Motivational Item Winner: Kimberly Conway, Sara
statutory objectives to identify emerging managerial,
Fitzgerald, and Steven Van Brackle – Food and Drug
technical, administrative, and physical safeguard issues
Administration;
related to information security and privacy. The Board
• Newsletter Winner: Jane Moser – Employment and was originally created by the Computer Security Act of
Social Development Canada; and 1987 (P.L. 100-235) as the Computer System Security and
Privacy Advisory Board (CSSPAB) within the Department
• Role-Based Training Winner: Susan Farrand, Supply
of Commerce. The CSSPAB was chartered in May 1988 in
Chain Risk Management Resource Center, DOE.
accordance with the Federal Advisory Committee Act,
as amended, 5 U.S.C., App. In December 2002, Public
2 9
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

Law 107-347, The E-Government Act of 2002, Title III, The and guidelines developed under Section 20 of the National
Federal Information Security Management Act (FISMA) of Institute of Standards and Technology Act (15 U.S.C. 278g-3),
2002, Section 21 of the National Institute of Standards and as amended.
Technology Act (15 U.S.C. 278g-4) amended the statutory
Congress indicated the long-term need for the Board by
authority of the Board and renamed it the Information
setting the term of Board members at a minimum of four
Security and Privacy Advisory Board.
years. The charter (http://csrc.nist.gov/groups/SMA/ispab/
Since the inception of this Advisory Board in 1987, ISPAB documents/ispab_charter_2014-2016.pdf) requires that the
successfully renewed its charter with proper authority every NIST Director appoint the Chairman and all twelve members
two years. The legislative history for Public Law 100-235 and of the Board. They are selected for their preeminence in the
Public Law 107-347 underscores that Congress intended that information technology industry or related disciplines.
the Board be a continuing body. The Board plays a central
The Charter also stipulates that Board members be
and unique role in providing the government with expert
selected from three main categories, with each category
advice concerning information security and privacy issues
providing four members. Category 1 includes members
that may affect federal information systems. No other similar
from outside the Federal Government who are eminent in
group of experts meets regularly to review information
the information technology industry, at least one of whom
security issues involved in unclassified Federal Government
is representative of small or medium-sized companies in
computer systems and networks. Also, Title III of the
such industries. Category 2 also includes members from
E-Government Act of 2002 reaffirmed the need for this
outside the Federal Government and not employed by or
Board by giving it additional responsibilities: to thoroughly
representative of a producer of information, but who are
review all of the proposed information technology standards
eminent in the field of information technology, or related
3 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

disciplines. Category 3 includes experienced information information security and privacy;
system managers from the Federal Government, including
• Cybersecurity technical transfer and implementation
those with experience in information security and privacy,
interests, considering items of particular note to indi-
at least one of whom should be from the National Security
vidual industry sectors;
Agency. The categorization of Board members is intended
• Updates from the Privacy and Civil Liberties Oversight
to meet ISPAB’s statutory objectives. Federal members
Board (PCLOB);
bring a detailed understanding of the federal processing
environment; industry brings concerns and experiences • Updates from NIST’s CSD regarding cybersecurity and
regarding product development and market formation, cryptographic work;
while private computer security experts are able to bring
• Updates regarding embedded software security, in-
their experiences of commercial cost-effective security
cluding medical device security;
measures into Board discussion.
• Considerations surrounding Trusted Internet Connec-
Presently, the ISPAB Chairperson is Matt Thomlinson,
tions, DHS Enhanced Cybersecurity Services (ECS) and
Senior Vice President, Microsoft Security, who assumed
special needs for critical infrastructures;
the chair in October 2012. He is supported by the following
• Procurement and requirements to reduce supply-chain
Board members:
risk;
• Julie Boughn, (formerly from Center for Medicare &
• Cross-Agency Priority Goals (CAP Goals) for cyberse-
Medicaid, Innovation Centers for Medicare & Medicaid
curity;
Services (CMS));
• Information sharing with a focus on information securi-
• Christopher Boyer, AT&T;
ty and privacy;
• John Centafont, National Security Agency (NSA);
• Updates regarding FISMA, the related security controls
• David Cullinane, Security Starfish, LLC;
(SP 800-53), and FedRAMP; and
• Kevin Fu, The University of Michigan;
• Updates of other critical NIST publications.
• Gregory Garcia, Financial Services Sector Coordinating
In addition to the work-plan focus areas, the Board also
Council (FSSCC);
considered the following topics during FY 2014:
• Toby Levin, Retired (formerly from U.S. Department of
• Internet of Things (IOT);
Homeland Security);
• Cryptography and NIST Cryptography processes;
• Edward Roback, U.S. Department of Treasury;
• Transportation Sector and Vehicle-to-Vehicle Commu-
• Gale Stone, Social Security Administration; and
nication;
• Peter Weinberger, Google, Inc.
• GAO reports relating to information security and priva-
During FY 2014, ISPAB held three meetings, all in cy;
Washington D.C:
• Big Data and Privacy;
• December 19-20, 2013 – this meeting was to replace
• Controlled Unclassified Information (CUI) Program;
the meeting scheduled for October 10-12, 2013 that was
• Federal Cloud Credential Exchange (FCCX) and the
cancelled due to a government shutdown;
NSTIC; and
• March 12-14, 2014; and
• National Cybersecurity Center of Excellence (NCCoE)
• June 11-13, 2014.
Updates.
During the December 2013 meeting, the Board
The presenters at each Board meeting were leaders
developed a FY 2014 work plan. The resulting plan included
and experts representing private industry; academia;
the following areas of focus:
federal agency CIOs, IGs and CISOs.
• Coordination with Office of Management and Budget
Copies of the current list of members and their
(OMB), and other federal agencies, such as National
biographies, the Board’s charter and past Board activities
Security Agency (NSA) and U.S. Department of
are located at http://csrc.nist.gov/groups/SMA/ispab.
Homeland Security (DHS), on all matters relating to
Information on ISPAB Meetings is published in Federal
3 1
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

Register Notices at least 16 days prior to the meeting. Those In FY 2014, NIST, in collaboration with the FBI and the
interested in receiving meeting notices and other notices SBA, focused on implementing a three-year renewal of the
relating to NIST work in information security and privacy co-sponsorship agreement that governs this cybersecurity
may email their name, affiliation, and address to Annie Sokol workshop outreach program.
at the address below.
http://csrc.nist.gov/groups/SMA/sbc/
CONTACT:
CONTACT:
Ms. Annie Sokol
Ms. Patricia Toth
Designated Federal Officer (DFO), ISPAB
301-975-5140
(301) 975-2006
patricia.toth@nist.gov
annie.sokol@nist.gov
(Editor Note: Mr. Richard Kissel led this program until his
Small and Medium Size Business (SMB) recent retirement.)
Cybersecurity Workshop Outreach
Small business owners face a broad range of
information security issues. A computer failure or system CRYPTOGRAPHIC STANDARDS
breach could jeopardize the company’s reputation and may PROGRAM
result in significant damage and recovery cost or going
out of business. The small business owner who recognizes
the threat of computer crime and takes steps to deter Hash Algorithms and the Secure Hash
inappropriate activities is less likely to become a victim. Algorithm-3 (SHA-3) Standard (Draft
FIPS 202)
The U.S. Small Business Administration (SBA) reports
that over 27 million U.S. companies - more than 99 percent NIST opened a public competition in 2007 to develop a
of all U.S. businesses - are SMBs of 500 employees or fewer new cryptographic hash algorithm, SHA-3, to augment the
(http://www.sba.gov/sites/default/files/allprofiles12.pdf). hash algorithms specified in the Secure Hash Standard, FIPS
While the threats to individual small and medium-size 180-4. The competition ended on October 2, 2012 when NIST
businesses (SMBs) may not be significantly different from announced the selection of KeccaK as the winning algorithm
those facing larger organizations, a SMB frequently has for standardization as the new SHA-3 Standard. NIST
fewer resources available to protect systems, detect attacks, consulted with the KeccaK designers and the cryptographic
or respond to security issues. A vulnerability common to a community, and then developed a SHA-3 standardization
large percentage of SMBs could pose a threat to the nation’s plan, which was presented at numerous cryptography
information infrastructure and economic base. conferences in 2013, and posted at the NIST hash website,
indicated below, for public feedback.
To help address information security risk, these
businesses require assistance with the identification of On May 28, 2014, NIST CSD announced Draft FIPS
security mechanisms and with practical, cost-effective 202, SHA-3 Standard: Permutation-Based Hash and
training. Training helps SMB’s use their limited resources Extendable-Output Functions, in the Federal Register (79
most effectively to address relevant and serious threats. In FR 30549) and requested comments. The announcement
response to this need, NIST, the SBA, and the Federal Bureau also proposed a revision of the Applicability Clause (#6)
of Investigation (FBI) co-sponsor a series of cybersecurity of the Announcement Section of FIPS 180-4, Secure Hash
training workshops for small businesses. These workshops Standard, to allow the use of hash algorithms specified in
provide an overview of cybersecurity threats, vulnerabilities, either FIPS 180-4 or FIPS 202 for federal applications that
and corresponding protective tools and techniques, with require a cryptographic hash algorithm. The revision was
a special emphasis on information that small business necessary because the original text in FIPS 180-4 mandates
personnel can apply directly. the use of hash algorithms specified in FIPS 180-4 only. The
other sections of FIPS 180-4 remain unchanged. The ninety-
day public comment period for Draft FIPS 202 and the
revision in FIPS 180-4 ended on August 26, 2014.
3 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

The  CSD  also  hosted  a  SHA-3  workshop  at  the  800-90A in January 2012 to include additional capabilities
University of California, Santa Barbara, on August 22, 2014  identified during the development of Part 4 of ANS X9.82.
to obtain feedback on the proposed SHA-3 Standard, and
|     |     |     |     |     |     |     | In  | September  |     | 2013,  | articles  | from  | major  | news  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | --------- | ----- | ------ | ----- |
on additional modes of operation based on SHA-3 that are
|                    |     |                        |     |                |     |     | organizations,  |     | based  | on  leaked  |     | classified  | documents,  |     |
| ------------------ | --- | ---------------------- | --- | -------------- | --- | --- | --------------- | --- | ------ | ----------- | --- | ----------- | ----------- | --- |
| being  considered  |     | for  standardization.  |     | Approximately  |     | 75  |                 |     |        |             |     |             |             |     |
raised public concern that one of the DRBGs specified in
participants from around the world attended the workshop.
SP 800-90A could contain a backdoor, namely, the Dual_
The  CSD  received  much  feedback  throughout  the  EC_DRBG, which is based on the use of elliptic curves. This
year, especially during the week of the workshop. Official  weakness could allow attackers to successfully predict the
comments received on Draft FIPS 202 and on the revision  secret cryptographic keys that form the foundation for the
of the Applicability Clause of FIPS 180-4 are posted at  assurances provided by security products. CSD immediately
http://csrc.nist.gov/groups/ST/hash/sha-3/fips-202-public- published an ITL Bulletin (September 2013, visit the CSRC ITL
comments-aug2014.html. CSD is in the process of addressing  Bulletins page http://csrc.nist.gov/publications/PubsITLSB.
these comments, and incorporating them, as appropriate, in  html) that provided a high-level discussion of the issues,
the final versions of FIPS 202 and FIPS 180-4, to be approved  reopened the SP 800-90 series of publications for public
by the Secretary of Commerce. NIST will announce the final  comment, and recommended that the Dual_EC_DRBG no
approval by the Secretary in the Federal Register. longer be used, pending the resolution of the comments. In
April 2014, another public comment period was held on a
Information about the SHA-3 standardization effort is
revision of SP 800-90A that removed the Dual_EC_DRBG
available at:
http://csrc.nist.gov/groups/ST/hash/sha-3/sha-3_ from the document. An additional public comment period
|     |     |     |     |     |     |     | was  held  | in  late  | 2014  | that  | included  | additional  |     | changes  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----- | ----- | --------- | ----------- | --- | -------- |
standardization.html.
suggested during the April 2014 comment period.
|     |     |     |     |     |     |     | Two  | additional  |     | documents  |     | (SP  |     | 800-90B,  |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ---------- | --- | ---- | --- | --------- |
CONTACT:
|     |     |     |     |     |     |     | Recommendation  |     | for  | the  | Entropy  | Sources  | Used  | for   |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---- | ---- | -------- | -------- | ----- | ----- |
Ms. Shu-jen Chang  Random Bit Generation, and SP 800-90C, Recommendation
(301) 975-2940  for Random Bit Generator (RBG) Constructions) are under
shu-jen.chang@nist.gov development, and the initial drafts were made available
for public comment in 2012. SP 800-90B addresses the
|     |     |     |     |     |     |     | development  | and  | testing  | of  | entropy  | sources,  |     | including  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | -------- | --- | -------- | --------- | --- | ---------- |
Random Number Generation (RNG)
descriptions of the validation tests for NIST’s Cryptographic
Random numbers are required for the security for many
|     |     |     |     |     |     |     | Algorithm  | Validation  |     | Program  | to  | validate  | candidate  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | -------- | --- | --------- | ---------- | --- |
cryptographic algorithms. For example, random numbers
entropy sources. SP 800-90C provides basic guidance on
are used to generate the keys needed for encryption and
the construction of RBGs from entropy sources and DRBG
digital signature applications.
|     |     |     |     |     |     |     | mechanisms.  | These  | documents  |     | have  | undergone  |     | further  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ---------- | --- | ----- | ---------- | --- | -------- |
In the late 1990s, a project to develop more rigorous  changes as a result of the public comments and discussions
| requirements  |     | and  specifications  |     | for  random  | number  |     |                 |     |                   |     |          |     |         |           |
| ------------- | --- | -------------------- | --- | ------------ | ------- | --- | --------------- | --- | ----------------- | --- | -------- | --- | ------- | --------- |
|               |     |                      |     |              |         |     | with  industry  |     | representatives.  |     | Updated  |     | drafts  | will  be  |
generation (RNG) was initiated in coordination with the
provided for another public comment period in early FY
| American National Standards Institute’s (ANSI) Accredited  |            |        |           |            |           |     | 2015. |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | ---------- | ------ | --------- | ---------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Standards                                                  | Committee  | (ASC)  | X9.  The  | resulting  | standard  |     |       |     |     |     |     |     |     |     |
(American National Standard (ANS) X9.82) contains four
CONTACTS:
parts: Part 1 provides general information; Part 2, which is
nearing completion, will provide requirements for entropy
|     |     |     |     |     |     |     | Ms. Elaine Barker   |     |     |     | Mr. John Kelsey  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | ---------------- | --- | --- | --- |
sources;  Part  3  provides  specifications  for  deterministic  (301) 975-2911       (301) 975-5101
| random  | bit  generator  | (DRBG)  | mechanisms;  |     | and  | Part  4  |                         |     |     |     |                         |     |     |     |
| ------- | --------------- | ------- | ------------ | --- | ---- | -------- | ----------------------- | --- | --- | --- | ----------------------- | --- | --- | --- |
|         |                 |         |              |     |      |          | elaine.barker@nist.gov  |     |     |     | john.kelsey@nist.gov    |     |     |     |
provides guidance on constructing random bit generators
(RBGs) from entropy sources and DRBG mechanisms.
|     |     |     |     |     |     |     | Dr. Meltem Sönmez Turan   |     |     |     | Dr. Kerry McKay  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ---------------- | --- | --- | --- |
In  March  2007,  CSD  published  SP  800-90,  (301) 975-4391      (301) 975-4969
|     |     |     |     |     |     |     | meltem.turan@nist.gov  |     |     |     | kerry.mckay@nist.gov |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | -------------------- | --- | --- | --- |
Recommendation for Random Number Generation Using
Deterministic Random Bit Generators, which contained the
DRBG mechanisms in Part 3 of ANS X9.82, plus an additional
DRBG mechanism. This recommendation was revised as SP
3 3
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

Block Cipher Modes of Operation
CONTACT:
The engine for many of the techniques in NIST’s
cryptographic toolkit is a block cipher algorithm, such as Dr. Morris Dworkin
the Advanced Encryption Standard (AES) algorithm or the (301) 975-2354
Triple Data Encryption Algorithm (TDEA). A block cipher morris.dworkin@nist.gov
transforms some fixed-length binary data (i.e., a “block”)
into seemingly random data of the same length. The
Key Management
transformation is determined by the choice of some secret
NIST’s CSD continues to provide guidelines on
data called the “key.” The same key is used to reverse the
cryptographic key management for the Federal Government,
transformation and recover the original block of data. A
and to coordinate with other national and international
cryptographic technique that is constructed from a block
organizations, industry, and academia.
cipher is called a mode of operation.
SP 800-56B, Recommendation for Pair-Wise Key
NIST’s CSD is developing AES modes of operation for
Establishment Schemes Using Integer Factorization
format-preserving encryption (FPE), based on proposals
Cryptography, was first published in August 2009. This
that were submitted from the private sector. A format
publication specifies approved methods for automated
can be a sequence of decimal digits, such as a credit card
key establishment using Rivest, Shamir, Adleman (RSA)
number or a social security number (SSN); formats can
key-transport and key-agreement schemes. In an RSA key-
also be defined for other sets of characters besides decimal
transport scheme, one party (called the sender) generates
digits. FPE produces ciphertext with the same format as the
a key to be used in subsequent communications and sends
corresponding plaintext, so that, for example, an encrypted
it to another party (called the receiver), encrypted using
SSN still looks like a valid SSN. FPE is expected to facilitate
the receiver’s public key. In a key-agreement scheme, two
the retrofitting of encryption to existing applications. For
parties contribute information that is used by each party
example, FPE could be applied to database systems, so that
to compute a shared secret, which is then used to derive
the sensitive data could be targeted for encryption without
a key that is known by both parties. The 2009 version
disrupting the underlying data fields/pathways.
approved the use of 1024- and 2048-bit keys for both key-
Draft SP 800-38G, Recommendation for Block Cipher
transport and key-agreement schemes, and in the case
Modes of Operation: Methods for Format-Preserving
of the key-agreement schemes, specified two approved
Encryption, which was released for public comment in July
methods for key derivation, both using an approved hash
2013, included three methods for FPE called FF1, FF2, and
function. SP 800-56B has been revised to remove the use
FF3. These methods are modes of operation of the AES that
of 1024-bit keys because they no longer provide adequate
are intended to support a security strength of 128 bits or
protection for federal information, and to approve the use
more.
of 3072-bit keys. This revision also includes the approval of
As part of the public review of Draft SP 800-38G and additional key-derivation methods specified in SP 800-56C,
as part of its routine consultation with other agencies, NIST Recommendation for Key Derivation through Extraction-
was advised by the National Security Agency that the FF2 then-Expansion, and SP 800-135, Recommendation for
mode in the draft could not support 128 bits of security Existing Application-Specific Key Derivation Functions,
strength for some use cases. NIST independently confirmed and the use of Hash-based Message Authentication Code
this assessment, and in June 2014, NIST’s CSD announced its (HMAC), as well as a hash function, during the key-derivation
intention to remove FF2 from the document. process. HMAC is specified in FIPS 198-1, The Keyed-Hash
Message Authentication Code (HMAC). The revision of SP
The FF2 mode was designed for the payment card
800-56B was published in September 2014.
industry and submitted for NIST’s consideration in 2011 by
VeriFone Systems, Inc. NIST’s analysis does not imply any SP 800-57, Recommendation for Key Management,
practical vulnerability for the implementations of FF2 in Part 3: Application-Specific Key Management Guidance,
the payment card industry. Nevertheless, in order for FF2 was first published in 2009. This document addresses the
to meet NIST’s security requirements for other potential key-management issues of currently available cryptographic
applications, VeriFone Systems, Inc. has indicated that it will mechanisms, including the use of Public Key Infrastructures
submit a revised proposal for NIST CSD to review. Meanwhile, (PKI) and several commonly used security protocols. A
CSD expects to finalize SP 800-38G with FF1 and FF3 in FY revision of this document was provided for public comment
2015. in May 2014 that updated the guidance provided in the 2009
version, included an additional section on the Secure Shell
3 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

(SSH) protocol and removed the TLS section, which is now references to the SHA-3 hash functions and to update
being addressed in SP 800-52 Revision 1, Guidelines for the guidance on the continued use of cryptographic algo-
Selection, Configuration, and Use of Transport Layer Security rithms and key sizes by the Federal government.
(TLS) Implementations. The final version of SP 800-57, Part
http://csrc.nist.gov/groups/ST/key_mgmt
3 will be published in early 2015.
SP 800-152, A Profile for U.S. Federal Cryptographic
CONTACTS:
Key Management Systems (CKMS), is under development
to provide guidance on the CKMSs to be used by the
Ms. Elaine Barker Dr. Dustin Moody
Federal Government. This document provides refinements
(301) 975-2911 (301) 975-8136
of the requirements for CKMS designers that are specified
elaine.barker@nist.gov dustin.moody@nist.gov
in SP 800-130, A Framework for Designing Cryptographic
Key Management Systems. SP 800-152 also provides
Dr. Lily Chen Mr. Ray Perlner
requirements and recommendations for the service providers
(301) 975-6974 (301) 975-3357
of CKMSs used by federal agencies and their contractors,
lily.chen@nist.gov ray.perlner@nist.gov
as well as guidance for the federal agencies in selecting a
CKMS that supports the security and management policies
Mr. Quynh Dang
of those agencies. A draft of this document was provided
(301) 975-3610
for public comment in FY 2013, and a workshop was held
quynh.dang@nist.gov
in March 2013 to discuss the draft. A second draft has been
under development throughout FY 2014 to address the
received comments and issues raised at the workshop. This Transport Layer Security
draft will be available for public comment in December 2014. SP 800-52 Revision 1, Guidelines for the Selection,
Configuration, and Use of Transport Layer Security (TLS)
A new NIST publication is under development
Implementations, provides recommendations regarding
that provides guidance on the security strength of a
TLS server and client implementations. TLS is a widely
cryptographic key that is used to protect data (i.e., a
used cryptographic protocol that provides communication
data-protection key), given the manner in which the key
security for a variety of network applications, such as email,
was generated and handled prior to its use to protect the
e-commerce, and healthcare.
target data. This document, SP 800-158, Key Management:
Obtaining a Targeted Security Strength, involves a The first version of SP 800-52, published in 2005,
considerable amount of new research, since it is an area that was withdrawn in March 2013. In September 2013, CSD
has not been fully addressed to date. This publication will be announced Draft SP 800-52 Revision 1. Changes to the
available for public comment in FY 2015. document were made based on comments received during
the public comment period, which ended in mid-December
Additional key-management work to be conducted in
2013. The final version of SP 800-52 Revision 1 was published
FY 2015 includes revisions to the following publications:
in April 2014.
• S P 800-56A, Recommendation for Pair-Wise Key-Es-
SP 800-52 Revision 1 is a significant update to the
tablishment Schemes Using Discrete Logarithm
original guidance and includes recommendations providing
Cryptography: This revision will align SP 800-56A
higher levels of security. New recommendations include the
more closely with SP 800-56B, including the addition
support of TLS versions 1.1 and 1.2, guidance on certificate
of 3072-bit keys for the finite-field Diffie-Hellman
profiles and validation methods, TLS extensions, and support
key-agreement schemes.
for a greater variety of cryptographic algorithms.
• SP 800-57 Part 1, Recommendation for Key Man-
The Internet Engineering Task Force (IETF) is actively
agement: Part 1: General: The revision will include an
developing extensions that can be used to add functionality
update of the approved key sizes for cryptographic
to TLS. The CSD’s Cryptographic Technology Group (CTG)
algorithms, and reference the new SHA-3 hash func-
will review updates and additions to the TLS protocol in the
tions specified in FIPS 202, SHA-3 Standard: Permuta-
second half of FY 2015. If there are changes that should be
tion-Based Hash and Extendable-Output Functions.
incorporated into SP 800-52, the development of a new
• S P 800-131A, Transitions: Recommendation for Tran- revision will begin.
sitioning the Use of Cryptographic Algorithms and
Key Lengths: This document will be revised to include
3 5
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

CSD will be prepared for possible standardization efforts in
CONTACTS:
this area. The CSD will hold a workshop on cybersecurity in a
post-quantum world in March of 2015.
Dr. Lily Chen Dr. Kerry McKay
(301) 975-6974 (301) 975-4969
lily.chen@nist.gov kerry.mckay@nist.gov CONTACTS:
Email project team: pqc@nist.gov
CRYPTOGRAPHIC RESEARCH Dr. Dustin Moody Dr. Lily Chen
(301) 975-8136 (301) 975-6974
dustin.moody@nist.gov lily.chen@nist.gov
Post-Quantum Cryptography
In recent years, there has been a substantial amount of Dr. Yi-Kai Liu
research on quantum computers – machines that exploit (301) 975-6499
quantum mechanical phenomena to solve problems that are yi-kai.liu@nist.gov
difficult or intractable for conventional computers. If large-
scale quantum computers are ever built, they will be able to
Privacy-Enhancing Cryptography
break the existing infrastructure of public-key cryptography.
The privacy-enhancing cryptography project seeks to
The focus of the Post Quantum Cryptography project is
promote the use of communication protocols that do not
to identify candidate quantum-resistant systems that are
reveal unneeded private information of the communicating
secure against both quantum and classical computers, as
parties. There are many technical challenges in doing this, as
well as the impact that such post-quantum algorithms will
it is typically hard to separate private data from general data
have on current protocols and security infrastructures.
(e.g. to convert a third-party-signed date-of-birth certificate
In FY 2014, CSD researchers internally presented status
into a certificate indicating that a person is of voting age).
reports in the areas of quantum computation, coding-based
Zero-knowledge (ZK) proof techniques and their variants
cryptography, lattice-based cryptography, and multivariate
can be used to accomplish this for a large class of assertions.
cryptography, which included detailed surveys of the
These techniques allow one party to prove to another
respective fields, as well as security overviews and specific
party that a given statement is true, without conveying
results. The project members also created evaluation criteria
any additional information apart from the fact that the
to compare proposed post quantum cryptosystems with the
statement is indeed true. However, even though many such
end goal of standardization.
ZK protocols are practical, adoption by industry is slow. CSD’s
CSD staff also engaged the international cryptographic CTG is also following the progress of emerging technologies,
community with presentations and publications. such as fully homomorphic encryption (FHE). FHE could
Presentations were made at the 2014 Conference on Theory of potentially solve a large class of problems by allowing
Quantum Computation, Communication, and Cryptography, computation on encrypted data without decryption. CTG has
CRYPTO 2014, and PQCrypto 2014 Conference. CSD staff also shown that the NIST Randomness Beacon (discussed
were invited to give talks at QCrypt 2014, and at the below) can be used as a primitive in secure multi-party
PQCrypto 2014 Conference. A CSD staff member gave a computation, such as sealed-bid online auctions, in which
course on quantum algorithms. CSD staff helped organize losing bids are never opened.
the joint NIST-University of Maryland Workshop on Quantum
Team members continue to work in collaboration with
Information and Computer Science. CSD also contributed
the National Strategy for Trusted Identities in Cyberspace
to the European Telecommunications Standards Institute
(NSTIC) program and the Federal Cloud Credential
whitepaper on quantum-safe cryptography. The CSD also
Exchange (FCCX) project. In this context, CTG has served as
hosted two leading experts in the field, Dr. Jintai Ding and
evaluators and in technical support roles. Information about
Dr. Vadim Lyubashevsky, for extended visits.
NSTIC and FCCX is available at http://www.nist.gov/nstic/.
In FY 2015, the CSD will continue to explore the security
Current communication security standards are primarily
capacity of purported quantum-resistant technologies
designed for two-party communication. CTG believes that
with the ultimate goal of uncovering the fundamental
future protocols, such as those for identification, commercial
mechanisms necessary for efficient, trustworthy, and cost-
transactions, and social media, will necessitate standards
effective information assurance in the post-quantum market.
for three-party communications (e.g., two parties involved
Upon the successful completion of this phase of the project,
3 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

in a commercial transaction and a third party that serves  SP 800-38 series of block cipher modes; and the selection
as an enabler of some aspects of the transaction). This is  and status of the recommended elliptic curves in FIPS 186-
particularly important if standards are to provide privacy  4, the Digital Signature Standard. As part of the review, the
protection. CTG has developed some basic protocols for this  COV provided recommendations for process improvement,
purpose. One such protocol allows for privacy-preserving  as well as some specific technical considerations and criteria
identification with the aid of a mediator. In this protocol, the  for NIST’s cryptographic standards and processes.
issuer of an assertion, such as “John Smith is an employee
|     |     |     |     |     |     |     | Based  | on  | the  | COV’s  | recommendations,  |     |     | the  VCAT  |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---- | ------ | ----------------- | --- | --- | ---------- |
of the Department of Commerce,” does not need to know
|     |     |     |     |     |     |     | produced  | a   | report  | detailing  |     | recommendations  |     | for  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | ---------- | --- | ---------------- | --- | ---- |
who the consumer of the assertion is, yet it can encrypt the
|     |     |     |     |     |     |     | NIST’s  | cryptographic  |     | standards  |     | program.  |     | The  VCAT  |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ---------- | --- | --------- | --- | ---------- |
assertion with a key only known to that consumer (i.e. the
|     |     |     |     |     |     |     | recommendations  |     | called  |     | for  NIST  | to  | increase  | its  staff  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | --- | ---------- | --- | --------- | ----------- |
mediator cannot see the unencrypted assertion).
|          |     |     |     |     |     |     | of  cryptography                     |      | experts   |           | and   | implement  | more          | explicit   |
| -------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ---- | --------- | --------- | ----- | ---------- | ------------- | ---------- |
|          |     |     |     |     |     |     | processes                            | for  | ensuring  | openness  |       | and        | transparency  | to         |
| CONTACT: |     |     |     |     |     |     | strengthen its cryptography efforts. |      |           |           |       |            |               |            |
|          |     |     |     |     |     |     | NIST                                 | has  | posted    | the       | full  | VCAT       | report,       | including  |
Dr. René Peralta
|     |     |     |     |     |     |     | the  individual  |     | recommendations  |     |     | from  | the  COV,  | on  the  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------------- | --- | --- | ----- | ---------- | -------- |
(301) 975-8702
rene.peralta@nist.gov  NIST website, as well as the briefing documents provided to
assist in the review.
NIST CSD is working to implement the recommendations
Cryptographic Standards and
of the VCAT. In response to comments received from the
Guidelines Process Review
|     |     |     |     |     |     |     | public,  | and  the  | recommendations  |     |     | from  | the  | VCAT  and  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------------- | --- | --- | ----- | ---- | ---------- |
In September 2013, news reports about leaked classified
COV, NIST CSD is working on a revision to NISTIR 7977
documents raised concerns over the trustworthiness of the
that will provide more detailed processes and procedures.
| Dual  Elliptic  | Curve  | Deterministic  | Random  |     | Bit  Generator  |     |     |     |     |     |     |     |     |     |
| --------------- | ------ | -------------- | ------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
These additions will ensure that there is a clear record of
| (Dual_EC_DRBG),  |     | which  | is  included  | in  | SP  800-90A,  |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the contributions to NIST standards and guidelines, and
Recommendation for Random Number Generation Using
|     |     |     |     |     |     |     | will  establish  |     | a  maintenance  |     | process  |     | that  ensures  | that  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------- | --- | -------- | --- | -------------- | ----- |
Deterministic Random Bit Generators. In response to these
publications remain current.  Additionally, NIST will continue
concerns, NIST initiated an internal review, reopened public
to strengthen capabilities with new hires, guest researchers,
| comment  | on  SP  | 800-90A,  | and  invited  | an  | independent  |     |            |      |           |                 |     |     |       |               |
| -------- | ------- | --------- | ------------- | --- | ------------ | --- | ---------- | ---- | --------- | --------------- | --- | --- | ----- | ------------- |
|          |         |           |               |     |              |     | contracts  | and  | external  | collaborations  |     |     | with  | researchers,  |
review of its standards development processes.
industry and standards organizations. Finally, NIST CSD will
As a first step, NIST’s CSD solicited public comments  work with the cryptographic community to evaluate other
to obtain feedback on the following: the processes used to
technical concerns raised by the VCAT’s review and take
develop standards, and the mechanisms used to engage  appropriate remediating actions.
experts in industry, academia and government to develop
http://www.nist.gov/director/vcat/index.cfm
them. As part of this process, the team compiled information
http://www.nist.gov/director/vcat/cryptographic-standards-
about the principles, processes and procedures that drive
NIST  cryptographic  standards  development  efforts.  This  guidelines-process.cfm
supports guidance to help the public understand how such
standards are developed. This information was published  CONTACT:
in draft NISTIR 7977, NIST Cryptographic Standards and
Mr. Andrew Regenscheid
Guidelines Development Process.
(301) 975-5155
| NIST’s  | federal  | advisory  | committee,  |     | the  | Visiting  |     |     |     |     |     |     |     |     |
| ------- | -------- | --------- | ----------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
andrew.regenscheid@nist.gov
Committee on Advanced Technology (VCAT), was asked
| to  review  | NIST’s  | cryptographic  | standards  |     | program.  | The  |     |     |     |     |     |     |     |     |
| ----------- | ------- | -------------- | ---------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
VCAT formed a Committee of Visitors (COV) with invited
| experts  from  | standards  |     | organizations,  | industry,  |     | and  the  |     |     |     |     |     |     |     |     |
| -------------- | ---------- | --- | --------------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
cryptographic research community to assist in this review.
During three meetings in April and May 2014, the COV
| reviewed  | NIST’s  | cryptographic  | standards  |     | development  |     |     |     |     |     |     |     |     |     |
| --------- | ------- | -------------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
process, including the events that led up to the inclusion of
the Dual_EC_DRBG in SP 800-90A; the development of the
37
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

The complexity of such protocols largely depends on the
NEW RESEARCH AREAS IN
number of multiplications required − hence, the importance
CRYPTOGRAPHIC TECH- of expressing functions as circuit computations with few
multiplication (AND) gates. Some of the published circuits
NIQUES FOR EMERGING
are now the standard reference for benchmarking tools in
APPLICATIONS
multiparty computation.
A partial list of new results consists of:
Circuit Complexity Research
• The construction of the smallest known circuits for
Cryptographic functions, such as encryption, digital
multiplication in several small finite fields;
signatures, and hashing, are implemented as electronic
• The construction of the smallest known circuits for the
circuits for a wide class of applications. In practice, it
multiplication of polynomials of degree n over the Ga-
is important to be able to minimize the size of these
lois Field with two elements (for small values of n); and
circuits. This problem is closely related to designing small
combinational circuits. These circuits use only binary AND, • The construction of optimal circuits - with respect to
XOR and NEGATION gates, i.e. multiplication, addition, the multiplicative complexity - for all predicates on four
and “+1” in arithmetic modulo 2. A combinational circuit bits. There are 65 536 such predicates. Surprisingly, the
on four variables is depicted below. The project team has multiplicative complexity of all these functions turned
shown that finding optimal combinational circuits is MAX- out to be at most three.
SNP Complete. In practice, this means that it is necessary to
Additionally, our circuits use no more than seven non-
settle for heuristics that design “good” circuits, as opposed
linear gates (XOR, XNOR). This is quite hard. Consider the
to provably optimal circuits. The CSD’s CTG has developed
following predicate (arithmetic is modulo 2):
and implemented new heuristics for the circuit minimization
problem. Two patents have been granted related to this f = x + x + x + x + xx + xx + xx + xx +xx + xxx +
1 2 3 4 1 2 1 3 1 4 2 3 2 4 1 2 3
xxx + xxxx
work, the last one in FY 2014. These are held jointly between
1 2 4 1 2 3 4.
NIST and the University of Southern Denmark. Computing the last term requires three multiplications.
So it is quite surprising that the full expression can be
CSD’s CTG is also researching circuit-based security
computed using only three multiplications; however, this
metrics for cryptographic functions. For a function to be
secure (one-way), it must be the case that any circuit that has been shown to be the case for f and all other predicates
implements it is sufficiently complex. In particular, a function on four bits. The circuit depicted below computes f using 3
multiplications and 6 additions.
is insecure if it can be implemented by a circuit containing
too few Boolean AND gates. This security metric, namely the • A proof that the maximum multiplicative complexity
number of AND gates necessary and sufficient to implement of predicates on five bits (there are more than 4 billion
a function, is referred to as its multiplicative complexity. such predicates) is four. The proof is constructive,
Unfortunately, determining multiplicative complexity is meaning the circuits can actually be built. This result
extremely hard. Mathematicians attempted this in the 1970s, appears in the proceedings of the Third International
but the effort had been largely abandoned by the 1980s. CTG Workshop on Lightweight Cryptography for Security &
has been able to compute tight bounds for the multiplicative Privacy (Springer-Verlag).
complexity of an important class of functions: the symmetric
functions. In the process, the CTG research team developed
tools that have wide applicability for both theoretical and
applied research in security and cryptography.
Multiparty computation is a technique that allows
a group of people to compute a function of their inputs
without revealing the inputs themselves. Examples of this
are: i) holding an election; ii) conducting closed-bid auctions
in which only the winning bid is determined; iii) proving to a
third party that an entity’s encrypted attributes satisfy some
requirement, such as “over 21 and (US citizen or Canadian
citizen)”. The protocols that solve multiparty computation
problems often encrypt bits using arithmetic modulo 2. Figure 7: Combinational Boolean Circuit
3 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

The  page  http://cs-www.cs.yale.edu/homes/~peralta/ its use would be necessary in order to prevent the adoption
CircuitStuff/CMT.html contains many of our results. of a lightweight cipher where the strong protection of AES
is required.
CONTACT:
CTG is preparing a report that describes the current
|     |     |     |     |     |     |     |     | state  and  | challenges  |     | in  | target  | application  | areas,  and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | --- | ------- | ------------ | ------------ |
Dr. René Peralta
|     |     |     |     |     |     |     |     | provides  | a  survey  |     | of  lightweight  |     | primitives,  | including  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ---------------- | --- | ------------ | ---------- |
(301) 975-8702
block and stream ciphers that have been proposed for
rene.peralta@nist.gov
|     |     |     |     |     |     |     |     | constrained  | environments.  |     |     | CTG  | researchers  | also  studied  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | --- | ---- | ------------ | -------------- |
efficient implementations of the Boolean functions used in
Cryptography for Constrained  lightweight  primitives  and  published  Multiplicative
Environments Complexity of Boolean Functions on Four and Five Variables
|        |               |     |           |     |            |        |         | at  the  | Third  | International  |     | Workshop  |     | on  Lightweight  |
| ------ | ------------- | --- | --------- | --- | ---------- | ------ | ------- | -------- | ------ | -------------- | --- | --------- | --- | ---------------- |
| There  | are  several  |     | emerging  |     | areas  in  | which  | highly  |          |        |                |     |           |     |                  |
constrained  devices  are  interconnected,  typically  Cryptography for Security & Privacy (LightSec 2014).
communicating wirelessly with one another, and working in  In FY 2015, CTG will continue to analyze the resource
concert to accomplish some task. Examples of these areas  requirements  and  performance  characteristics  of
| include:  | sensor  | networks,  | healthcare,  |     | distributed  | control  |     |     |     |     |     |     |     |     |
| --------- | ------- | ---------- | ------------ | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
lightweight primitives, and study their use as building blocks
systems, the Internet of Things, cyber physical systems, and  to perform various cryptographic objectives. Additionally,
the smart grid. Security and privacy can be very important
CTG will investigate specific application areas in order to
in  all  of  these  areas.  Because  the  majority  of  current  determine functionality and resource requirements in the
cryptographic algorithms were designed for desktop/server  area of cryptography for constrained environments.
environments, many of these algorithms do not fit into the
constrained resources. If current algorithms can be made to
CONTACTS:
fit into the limited resources of constrained environments,
their performance is typically not acceptable.  Mr. Lawrence Bassham    Dr. Kerry McKay
|        |                |     |             |     |        |        |     | (301) 975-3292  |     |     |     |     | (301) 975-4969  |     |
| ------ | -------------- | --- | ----------- | --- | ------ | ------ | --- | --------------- | --- | --- | --- | --- | --------------- | --- |
| CSD’s  | Cryptographic  |     | Technology  |     | Group  | (CTG)  | is  |                 |     |     |     |     |                 |     |
studying  the  use  of  the  NIST-approved  symmetric- lawrence.bassham@nist.gov  kerry.mckay@nist.gov
| key  algorithms  |     | in  constrained  |     | environments.  |     | CTG  | has  |     |     |     |     |     |     |     |
| ---------------- | --- | ---------------- | --- | -------------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
developed  microcontroller  implementations  of  the  Dr. Meltem Sönmez Turan
(301) 975-4391
| Advanced  | Encryption  |     | Standard  | (AES)  | to  | provide  | both  |     |     |     |     |     |     |     |
| --------- | ----------- | --- | --------- | ------ | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
meltem.turan@nist.gov
confidentiality and the AES-based message authentication
code, Cipher-based Message Authentication Code (CMAC),
for authentication. Additionally, CTG has implemented the  NIST Randomness Beacon
256-bit version of the Secure Hash Algorithm (SHA-256)
NIST has implemented a source of public randomness.
| to  provide  | a  Hash-based  |     | Message  |     | Authentication  |     | Code  |     |     |     |     |     |     |     |
| ------------ | -------------- | --- | -------- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
The prototype, called the Beacon, uses two independent,
(HMAC)  for  authentication.  SHA-3,  as  specified  in  Draft  commercially available sources of randomness, each with an
FIPS 202, SHA-3 Standard: Permutation-Based Hash and
independent hardware entropy source.
| Extendable-Output Functions,  |     |     |     | and  | a  variant  | of  | KeccaK  |      |         |     |           |     |                            |     |
| ----------------------------- | --- | --- | --- | ---- | ----------- | --- | ------- | ---- | ------- | --- | --------- | --- | -------------------------- | --- |
|                               |     |     |     |      |             |     |         | The  | Beacon  | is  | designed  | to  | provide unpredictability,  |     |
using an 800-bit permutation has also been implemented.
|     |     |     |     |     |     |     |     | autonomy,  | and consistency. Unpredictability  |     |     |     |     | means  that  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------------------- | --- | --- | --- | --- | ------------ |
CTG has demonstrated that SHA-3 allows a more efficient
users cannot algorithmically predict bits before they are
construction for computing Message authentication codes
made available by the source. Autonomy means that the
(MACs) than the HMAC construction, which is required when
source is resistant to attempts by outside parties to alter the
using SHA-256. CTG has also investigated other, non-NIST-
distribution of the random bits. Consistency means that a
approved algorithms for constrained environments.
set of users can access the source in such a way that they
| CTG  | has  also  | begun  |     | to  examine  | applications  |     | in  |     |     |     |     |     |     |     |
| ---- | ---------- | ------ | --- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
are confident that they all receive the same random string.
| constrained  | environments  |     | to  | determine  |     | whether  | NIST  |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | ---------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
The Beacon posts bit-strings in blocks of 512 bits every
| should  | develop  | a  lightweight  |     | encryption  | standard.  |     | CTG  |     |     |     |     |     |     |     |
| ------- | -------- | --------------- | --- | ----------- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
60 seconds. Each such value is time-stamped and signed
has talked with industry experts to understand challenges,
by NIST, and includes the hash of the previous value to
limitations, and work from other standardization bodies in
chain the sequence of values together. This prevents all,
this area. Also, CTG has had internal discussions on additional
|     |     |     |     |     |     |     |     | even  the  | Beacon  |     | itself,  | from  retroactively  |     | changing  an  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | -------- | -------------------- | --- | ------------- |
considerations for a lightweight standard, as restrictions on
3 9
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

output packet without being detected. The Beacon keeps the proof could be mailed to a trusted third party, encrypted
all output packets and makes them available online at and signed by an application, only to be opened if needed
https://beacon.nist.gov/home. and authorized.
Tables of random numbers have probably been used for Although commercially available physical sources of
multiple purposes, at least since the Industrial Revolution. randomness are adequate as entropy sources for currently
In the digital age, algorithmic random number generators envisioned applications of the Beacon, NIST is working on
have largely replaced these tables. The NIST Randomness developing a source of verifiably random sequences. Given
Beacon expands the use of public randomness to multiple that it is impossible to construct such sequences in any
scenarios in which the latter methods cannot be used. The classical physical context, CSD is collaborating with the NIST
extra functionalities stem mainly from three features. First, Physical Measurement Laboratory (PML) to build a quantum
the Beacon-generated numbers cannot be predicted before source. The aim is to use quantum effects to generate
they are published. Second, the public, time-bound, and sequences that are guaranteed to be unpredictable, even
authenticated nature of the Beacon allows a user application if an attacker has access to the random source. For more
to prove to anybody that it used truly random numbers not information on this collaboration, see http://www.nist.gov/
known before a certain point in time. Third, this proof can be pml/div684/random_numbers_bell_test.cfm.
presented offline and at any point in the future. For example,
Figure 8: A Space-time Diagram Illustrating a Locality-loophole-free Bell Test
4 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Since the bits posted by the Beacon are public, these bits will continue to contribute to a broader scope of IEEE 802
are not to be used as secret values, such as cryptographic wireless standards.
keys or seeds for random number generators used in the
construction of cryptographic keys. NIST encourages
CONTACT:
the community-at-large to research and publish novel
ways in which this tool can be used. Some examples of Dr. Lily Chen
applications are unpredictable sampling, new authentication (301) 975-6974
mechanisms, and secure multi-party computation. To learn lily.chen@nist.gov
more about the NIST Randomness Beacon project, please
visit the project’s website at: http://beacon.nist.gov.
VALIDATION PROGRAMS
CONTACT:
Federal agencies, industry, and the public rely on many
Dr. René Peralta
of the standards and specifications supported by NIST’s CSD.
(301) 975-8702
Poor implementations of these standards or specifications
rene.peralta@nist.gov
may render a particular product insecure, potentially placing
sensitive information at risk. CSD operates several validation
Wireless and Mobile Security programs that help provide a level of assurance that products
Today, wireless networks often provide connections meet established security requirements and conform to
for mobile devices using multiple and different radio published specifications. To that end, the Security Testing,
technologies. In such a heterogeneous network, a mobile Validation, and Measurement Group (STVMG) develops test
device may switch its connection between different wireless suites and test methods; provides implementation guidance
technologies. The procedure for conducting such a switch is and technical support to industry forums; and conducts
called a “handover.” Media-independent handover (MIH) is a education, training, and outreach programs.
set of services specified in IEEE 802.21 to assist the handover.
STVMG’s validation programs work together with
When the services provided by the pervasive hetero-
independent laboratories that are accredited by the NIST
geneous networks are extended to other applications, such
National Voluntary Laboratory Accreditation Program
as Smart Grid applications, the MIH needs to be processed
(NVLAP). Based on the independent laboratory test report
by a group of wireless nodes, such as smart meters, for
and test evidence, the validation programs described
balancing the network load and for reliability. In this case,
below validate the implementation under test. The CSD
the information may need to be delivered to a group of
subsequently publishes lists of the validations awarded on
smart meters using a multicast message, which is used to
public websites.
deliver the information. That is, the message is sent from one
point-of-service (PoS) to multiple wireless nodes. In some of Cryptographic System Validation
the application environments, such as sensor networks, the Current validation programs focus on providing a known
groups are formed dynamically. That is, new nodes can be level of assurance for cryptographic algorithms and modules.
added to the group, and some nodes in the group may need These modules are used within the context of a larger system
to be removed. Such groups are managed through multicast to provide cryptographic services as a method of protecting
signals. the data within the system. As information systems continue
Amendment 2 of IEEE 802.21 provides protection to become more complex, the methods used to implement
mechanisms for unicast messages, that is, mechanisms cryptographic services have also increased in complexity.
that protect messages between a PoS and a single mobile Problems with the use of cryptography are often introduced
node. However, the protection for multicast messages and through the interaction of cryptographic components with
group management signals is critical. In FY 2014, CSD has the operating environment. This program seeks to specify
worked with IEEE 802.21 to develop security solutions for how cryptographic components are used as part of a defined
group management in Task Group D of IEEE 802.21. The cryptographic system to solve problems with a measureable
solutions, specified in IEEE 802.21 Amendment 4, include level of assurance, and to introduce automated methods of
the mechanisms to distribute group keys and for the quantifying the level of assurance that has been provided.
protection of multicast messages. A draft of Amendment 4
has been approved through sponsor ballot. In FY 2015, CSD
41
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

This program will begin the research required to Cryptographic Programs and
define a reference cryptographic systems architecture and Laboratory Accreditation
example use cases where cryptographic systems are built The Cryptographic Algorithm Validation Program
from known cryptographic components that cooperate (CAVP) and the Cryptographic Module Validation Program
through trust relationships to provide a measureable level of (CMVP) were developed in collaboration between NIST
assurance. The architecture should begin at the lowest level and the Communications Security Establishment (CSE) of
with a hardware-based root of trust, and each cryptographic Canada to support the respective federal user communities
component should be added in successive layers to for strong, independently tested, and commercially available
provide assurance in a systematic way. This should allow cryptographic algorithms and modules. Through these
the development of tests that would measure the correct programs, NIST and CSE work with international government,
implementation of cryptographic components as part of a public and private sectors as a part of the cryptographic
larger system. community to achieve standards-based security and
This program will perform research and experimentation assurance of correct implementation. The goal of these
in applicable technologies and techniques that will enable programs is to provide federal agencies with a security
the efficient testing of the cryptographic capabilities of metric to use in procuring and deploying cryptographic
each layer, and continuous monitoring capabilities of modules and promote the use of validated algorithms and
each cryptographic component, providing the necessary modules by industry and the public. The testing carried out
interfaces to establish trust relationships with other by independent third-party laboratories accredited by the
cryptographic components. Techniques could include such NIST National Voluntary Laboratory Accreditation Program
items as: (NVLAP), and the validations performed by the CAVP and
CMVP programs provide this metric. Federal agencies,
• Embedding SCAP-like data elements and standard
industry, and the public can choose cryptographic modules
interfaces to query those data elements during the de-
and/or products containing cryptographic modules from
sign and implementation of cryptographic components
the CMVP Validated Modules List and have confidence
that would enable automated testing capabilities;
in the claimed level of security and assurance of correct
• Using cryptographic techniques to embed values into implementation.
the module that would increase the verifiability and
Cryptographic algorithm and cryptographic module
assurance that the module provides; and
testing and validation are based on published NIST
• Using industry-based secure development techniques standards. As federal agencies are required to use validated
to increase the level of trust inherent in software mod- cryptographic modules for the protection of sensitive
ules starting with design and implementation. non-classified information, the validated modules and the
Research into this area of cryptographic system validated algorithms that the modules contain represent the
validation holds the promise of automating the validation of culmination and delivery of the CSD’s cryptography-based
all cryptographic components, providing a higher assurance work to the end user.
with less manual effort by using SCAP-based ideas to embed The CAVP and the CMVP are separate collaborative
data elements that instrument the test harnesses used to programs. The CAVP and the CMVP validate algorithms
validate cryptographic systems. This would also provide the and modules, respectively, that are used in a wide variety of
instrumentation that could be leveraged to enable a greater products, including Internet browsers, radios, smart cards,
level of situational awareness and security measurement, space-based communications, munitions, security tokens,
and potentially, to enable continuous monitoring of mobile phones, network and storage devices, and products
cryptographic systems. supporting the Public Key Infrastructure (PKI) and electronic
commerce. A module may be a standalone product, such
CONTACT: as a virtual private network (VPN) or smart card, or it
could be a module embedded in many products, such as a
Mr. Michael Cooper
cryptographic-based toolkit. As a result, a small number of
(301) 975-8077
modules may be incorporated within hundreds of products.
michael.cooper@nist.gov
The CAVP validates cryptographic algorithms that may be
integrated in one or more cryptographic modules.
4 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Figure 9: General Flow of FIPS 140-2 Testing and Validation
The CAVP and CMVP validation programs provide The unique position of the validation programs gives the
documented methodologies for conformance testing CAVP and CMVP the opportunity to acquire insight during
through defined sets of security requirements. For the the validation review activities and results in practical, timely,
CAVP, the validation system documents are designed for and up-to-date guidance that is needed by the testing
each FIPS-approved and NIST-recommended cryptographic laboratories and vendors to move their modules out to the
algorithm. See the website for a listing (see http://csrc.nist. user community in a timely and cost-effective manner and
gov/groups/STM/cavp/). Security requirements for the with the assurance of third-party conformance testing. This
CMVP are found in FIPS 140-2, Security Requirements for knowledge and insight provide a foundation for current and
Cryptographic Modules, and the associated test metrics future standards and tools development.
and methods in Derived Test Requirements for FIPS 140-2,
The CMVP reviews the cryptographic module validation
Security Requirements for Cryptographic Modules (DTR).
requests from the testing laboratories and, as a byproduct
The four Annexes to FIPS 140-2 reference the underlying
of the review, is attentive to emerging and/or changing
cryptographic algorithm standards or methods. The CMVP-
technologies. These insights into the evolution of operating
developed Implementation Guidance for FIPS PUB 140-2
environments and complex systems allow, the CMVP to
and the Cryptographic Validation Program (IG) provides
perform research and development on evolving test metrics
programmatic and implementation guidance across all of
and methods and future requirements for cryptographic
the referenced documents. The information provided in the
modules. This research is used to assist developers of
DTR and IG documents ensures the repeatability of tests and
cryptographic modules, testing laboratories, and the user
the equivalency in results across the testing laboratories.
community when developing new standards.
The Implementation Guidance provides clarity, consistency
of interpretation, and insight for successful conformance
testing, validation, and revalidation.
4 3
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

Figure 10: FIPS 140-1 and FIPS 140-2
Validated Modules by Calendar Year and Level
 Figure 12: CAVP Validation Status by FYs
The CAVP and the CMVP have stimulated improved
quality and security assurance of cryptographic algorithm
implementations and modules. The latest set of statistics,
| which  are  | collected  quarterly  | from  | each  of  | the  testing  |     |     |     |     |     |
| ----------- | --------------------- | ----- | --------- | ------------- | --- | --- | --- | --- | --- |
laboratories, shows that 5 % (dropped from 7 % in FY 2013)
of the cryptographic algorithms and 54 % (increased from
35 % in FY 2013) of the cryptographic modules brought in
for voluntary testing had security flaws that were corrected
| during  testing.  | By  the  | end  of  FY  | 2014,  the  | CMVP  had  |     |     |     |     |     |
| ----------------- | -------- | ------------ | ----------- | ---------- | --- | --- | --- | --- | --- |
validated and issued a total of 2258 cryptographic module
validation certificates that represent 5785 modules. These
modules have been developed by more than 475 domestic
| and  international  | vendors.  | Likewise,  | to  date,  | the  CAVP  |     |     |     |     |     |
| ------------------- | --------- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- |
has issued approximately 15 963 validations, representing  Figure 13: CAVP Validation Status for FY 2014
| the  algorithm  | validations  | of  approximately  | 17  | approved  |     |     |     |     |     |
| --------------- | ------------ | ------------------ | --- | --------- | --- | --- | --- | --- | --- |
algorithms. The  CAVP  issued  approximately  2200  algorithm
validations in FY 2014. Included in this total, is the 3000th
|     |     |     |     |     | Advanced  | Encryption  | Standard  (AES)  | validation,  | a   |
| --- | --- | --- | --- | --- | --------- | ----------- | ---------------- | ------------ | --- |
significant milestone for the CAVP. The CMVP issued 191
module validation certificates in FY 2014. The number of
algorithms and modules submitted for validation continues
to grow, representing significant growth in the number of
validations expected to be available in the future.
http://csrc.nist.gov/groups/STM
CONTACTS:
|     |     |     |     |     | CMVP Contact:  |     |   CAVP Contact:  |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | ---------------- | --- | --- |
Figure 11: FIPS 140-1 and FIPS 140-2
|     |     |     |     |     | Dr. Apostol Vassilev  |     |   Ms. Sharon Keller  |     |     |
| --- | --- | --- | --- | --- | --------------------- | --- | -------------------- | --- | --- |
Validation Certificates by Fiscal Year and Level  (301) 975-3221      (301) 975-2910
|     |     |     |     |     | apostol.vassilev@nist.gov   |     | sharon.keller@nist.gov |     |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | ---------------------- | --- | --- |
4 4
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Figure 14: CAVP Validated Implementation Actual Numbers
Automated Security Testing and Test the algorithm implementation does not function properly or
Suite Development is incomplete.
The Cryptographic Algorithm Validation Program The cryptographic algorithm validation tests designed
(CAVP), a collaborative program between NIST and the and developed by the CAVP are performed by independent
Communications Security Establishment (CSE) of Canada, third-party laboratories accredited by the NIST National
utilizes the requirements and specifications of NIST Voluntary Laboratory Accreditation Program (NVLAP). The
standards (i.e., FIPS and Special Publications), to develop laboratory works with vendors to validate their cryptographic
algorithm validation test suites and automated security algorithm implementations. The suite of validation tests for
testing. The CAVP is responsible for providing assurance that each algorithm ensures the repeatability of tests and the
the cryptographic algorithm implementations contained in equivalency in results across the testing laboratories.
cryptographic modules are implemented according to the
There are several types of validation tests, all designed
specifications in the standards. The CAVP accomplishes this
to satisfy the testing requirements of the cryptographic
by designing and developing conformance testing specific
algorithms and their specifications. These include, but are
to each cryptographic algorithm.
not limited to, Known-Answer Tests, Monte Carlo Tests,
The conformance testing consists of a suite of validation and Multi-Block Message Tests. The Known-Answer Tests
tests for each approved cryptographic algorithm. These are designed to examine the individual components of
validation tests exercise the algorithmic requirements and the algorithm by supplying known values to the variables
mathematical formulas detailed in the algorithm to assure and verifying the expected result. Negative testing is also
that the detailed specifications are implemented correctly performed by supplying known incorrect values to assure
and completely. If the implementer deviates from the that the implementation recognizes values that are not
specifications in the standard or excludes any part of these allowed. The Monte Carlo Test is designed to exercise the
specifications or requirements, the validation test will detect entire implementation under test (IUT). This test is designed
the deviations and fail. The validation testing will indicate that to detect the presence of implementation flaws that are not
4 5
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

detected with the controlled input of the Known-Answer implementation, they cannot be tested at the algorithm
Tests. The types of implementation flaws detected by level by the CAVP, but may be tested by the Cryptographic
this validation test include pointer problems, insufficient Module Validation Program (CMVP) if the requirements are
allocation of space, improper error handling, and incorrect considered applicable to the cryptographic module. However,
behavior of the IUT. The Multi-Block Message Test (MMT) some of these usage requirements may be considered to be
is designed to test the ability of the implementation to outside the scope of both the algorithm implementation
process multi-block messages, which require the chaining of and cryptographic module. In this latter case, the fulfillment
information from one block to the next. of the requirements is the responsibility of entities using,
installing, or configuring applications or protocols that use
During the last few years, the CTG has expanded
the cryptographic algorithms. For example, depending on
its publications to not only contain the algorithm’s
the design of a cryptographic module, it may not be possible
specifications, but also to include requirements on an
for the module to determine whether a specific key is used for
algorithm’s use. Many of these usage requirements do not
multiple purposes, a situation that is strongly discouraged.
fall within the scope of the CAVP because the CAVP focuses
on the correctness of the instructions within the algorithm’s The CAVP currently has algorithm validation testing for
boundary. If these additional algorithm usage requirements the following cryptographic algorithms:
are not considered applicable to the algorithm’s
CRYPTOGRAPHIC ALGORITHM/COMPONENT SPECIAL PUBLICATION OR FIPS
SP 800-67, Recommendation for the Triple Data
Encryption Algorithm (TDEA) Block Cipher, and
Triple Data Encryption Standard (TDES)
SP 800-38A, Recommendation for Block Cipher Modes of
Operation–Methods and Techniques
FIPS 197, Advanced Encryption Standard, and
Advanced Encryption Standard (AES) SP 800-38A, Recommendation for Block Cipher Modes of
Operation–Methods and Techniques
FIPS 186-2, Digital Signature Standard (DSS), with change
notice 1
Digital Signature Standard (DSS)
FIPS 186-4, Digital Signature Standard (DSS)
FIPS 186-2, Digital Signature Standard (DSS), with change
notice 1 and ANS X9.62
Elliptic Curve Digital Signature Algorithm (ECDSA)
FIPS 186-4, Digital Signature Standard (DSS), and ANS
X9.62
ANSI X9.31 and Public Key Cryptography Standards
(PKCS) #1 v2.1: RSA Cryptography Standard-2002
RSA algorithm FIPS 186-4, Digital Signature Standard (DSS), and ANSI
X9.31 and Public Key Cryptography Standards (PKCS) #1
v2.1: RSA Cryptography Standard-2002
Hashing algorithms SHA-1, SHA-224, SHA-256, SHA-384,
FIPS 180-4, Secure Hash Standard (SHS)
SHA-512, SHA-512/224, SHA-512/256
Random number generator (RNG) algorithms FIPS 186-2 Appendix 3.1 and 3.2; ANS X9.62 Appendix A.4
SP 800-90A, Recommendation for Random Number
Deterministic Random Bit Generators (DRBG)
Generation Using Deterministic Random Bit Generators
4 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Cryptographic Algorithm/Component Special Publication or FIPS
FIPS 198-1, The Keyed-Hash Message Authentication Code
Keyed-Hash Message Authentication Code (HMAC)
(HMAC)
SP 800-38C, Recommendation for Block Cipher Modes
Counter with Cipher Block Chaining-Message
of Operation: the CCM Mode for Authentication and
Authentication Code (CCM) mode
Confidentiality
Cipher-based Message Authentication Code (CMAC) Mode SP 800-38B, Recommendation for Block Cipher Modes of
for Authentication Operation: The CMAC Mode for Authentication
SP 800-38D, Recommendation for Block Cipher Modes of
Galois/Counter Mode (GCM) GMAC Mode of Operation
Operation: Galois/Counter Mode (GCM) and GMAC
SP 800-38E, Recommendation for Block Cipher Modes
XTS Mode of Operation of Operation: The XTS-AES Mode for Confidentiality on
Block-Oriented Storage Devices
SP 800-38F, Recommendation for Block Cipher Modes of
Key Wrapping
Operation: Methods for Key Wrapping
SP 800-56A, Recommendation for Pair-Wise Key
Key Agreement Schemes and Key Confirmation Establishment Schemes Using Discrete Logarithm
Cryptography, dated March 2007
SP 800-56A, Key Derivation Functions for Key Agreement
All of SP 800-56A except KDF
Schemes: All sections except Section 5.8
SP 800-56A, Section 5.7.1.2 Elliptic Curve Cryptography
SP 800-56A Section 5.7.1.2 ECC CDH function
Cofactor Diffie-Hellman (ECC CDH) Primitive Testing
SP 800-108, Recommendation for Key Derivation using
Key-Based Key Derivation functions (KBKDF)
Pseudorandom Functions
Application-Specific Key Derivation functions (ASKDF)
SP 800-135 (Revision 1) Recommendation for Existing
(includes KDFs used by IKEv1, IKEv2, TLS, ANS X9.63-
Application Specific key Derivation Functions
2001, SSH, SRTP, SNMP, and TPM)
Component test – ECDSA Signature Generation of hash
value (This component test verifies the signing of a hash- FIPS 186-4, Digital Signature Standard (DSS), and ANS
sized input. It does not verify the hashing of the original X9.62
message to be signed.)
Component test – RSA PKCS#1 1.5 Signature Generation
FIPS 186-4, Digital Signature Standard (DSS), and
of encoded message EM (This component test verifies the
Public Key Cryptography Standards (PKCS) #1 v2.1: RSA
signing of an EM. It does not verify the formatting of the
Cryptography Standard-2002
EM.)
Component test – RSA PKCS#1 PSS Signature Generation SP 800-56B, Recommendation for Pair-Wise Key
of encoded message EM (This component test verifies the Establishment Schemes Using Integer Factorization
RSASP1 function.) Cryptography, August 2009, Section 7.1.2
47
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

In FY 2015, the CAVP expects to add algorithm validation These efforts bring consistent testing of cryptographic
testing for: modules to the global community by providing ISO-
equivalent standards representing NIST FIPS 140-2, Security
• S P 800-56C, Recommendation for Key Derivation
Requirements for Cryptographic Modules and Derived
through Extraction-then-Expansion, November 2011;
Test Requirements [DTR] for FIPS PUB 140-2, Security
• S P 800-132, Recommendation for Password-Based
Requirements for Cryptographic Modules.
Key Derivation Part 1: Storage Applications, December
ISO/IEC JTC 1/SC 27 WG 3 completed and published
2010; and
revisions of ISO/IEC 19790:2006 and ISO/IEC 24759:2008,
• SP 800-56A Revision 2, Recommendation for Pair-Wise
for which Randall J. Easter of NIST’s CSD was the principal
Key Establishment Schemes Using Discrete Logarithm
editor. The revision of ISO/IEC 19790 was published
Cryptography, May 2013.
on August 15, 2012. The revision of ISO/IEC 24759 was
http://csrc.nist.gov/groups/STM/cavp published on January 31, 2014. Both ISO/IEC standards were
also adopted by the American National Standards Institute
(ANSI). The two ISO/IEC revisions were developed with
CONTACTS:
international support and the collaboration of governments,
Ms. Sharon Keller Ms. Elaine Barker industry and academia. The NIST CMVP and the NVLAP-
(301) 975-2910 (301) 975-2911 accredited testing laboratories worked closely with ISO in
sharon.keller@nist.gov elaine.barker@nist.gov the standards revision.
ISO/IEC 19790:2012 specifies the security requirements
ISO Standardization of Security for a cryptographic module utilized within a security
Requirements for Cryptographic system protecting sensitive information in computer and
telecommunication systems. This international standard
Modules
defines four security levels for cryptographic modules to
CSD has contributed to the activities of the
provide for a wide spectrum of data sensitivity (e.g. low
International Organization for Standardization/International
value administrative data, million dollar funds transfers, life-
Electrotechnical Commission (ISO/IEC), which issued
protecting data, personal identity information, and sensitive
ISO/IEC 19790, Security Requirements for Cryptographic
information used by a government) and a diversity of
Modules, on March 1, 2006, and ISO/IEC 24759, Test
application environments (e.g. a guarded facility, an office,
Requirements for Cryptographic Modules, on July 1, 2008.
Figure 15: Cryptographic Module Testing – ISO Standards
4 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

removable media, and a completely unprotected location). CSD’s contributions to the development of these
The overall security rating of a cryptographic module must international standards create a strong foundation for the
be chosen to provide a level of security appropriate for the adoption of and migration from currently used national
security requirements of the application and environment standards. In particular, this adoption will promote the
in which the module is to be utilized and for the security international harmonization for the implementation and
services that the module is to provide. testing of cryptographic algorithms and modules, while
accommodating individual country preferences in the choice
The security requirements cover areas relative to the
of approved security functions.
design and implementation of a cryptographic module.
These areas include cryptographic module specification; http://csrc.nist.gov/groups/STM/cmvp/
cryptographic module interfaces; roles, services, and
authentication; software/firmware security; the operational CONTACT:
environment; physical security; non-invasive security;
sensitive security parameter management; self-tests; life- Mr. Randy Easter
cycle assurance; and mitigation of other attacks. (301) 975-4641
randall.easter@nist.gov
CSD’s Randall J. Easter is the principal editor of the
following draft ISO/IEC documents:
Security Content Automation Protocol
• I SO/IEC 17825, Testing methods for the mitigation
of non-invasive attack classes against cryptographic (SCAP) Validation Program
modules; The SCAP Validation Program performs conformance
testing to ensure that products correctly implement
• I SO/IEC 18367, Cryptographic algorithms and security
SCAP, as defined in SP 800-126 Revision 2, The Technical
mechanisms conformance testing; and
Specification for the Security Content Automation Protocol
• ISO/IEC TS 30104, Physical Security Attacks, Mitigation (SCAP): SCAP Version 1.2. Conformance testing is necessary
Techniques and Security Requirements. because SCAP is a complex collection of eleven individual
specifications that work together to support various use
4 9
Figure 16: SCAP 1.2 Validation Process
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

cases. A single error in product implementation could result Products list at https://nvd.nist.gov/SCAP-Validated-Tools/.
in undetected vulnerabilities or policy noncompliance within
In FY 2015, the SCAP Validation Program plans to provide
an organization’s networks.
enhanced testing support and will focus on validation test
The test requirements for SCAP 1.2 are defined in NISTIR content for new operating systems. Expansion plans also
7511 Revision 3, Security Content Automation Protocol include improvements in automated testing capabilities.
(SCAP) Version 1.2 Validation Program Test Requirements.
http://scap.nist.gov/validation
In general, vendors may opt for product validation for one
or more SCAP capabilities or operating systems. Currently,
CONTACT:
the program offers testing on Microsoft Windows and Red
Hat Enterprise Linux platforms. The validation process
Ms. Melanie Cook
starts when a vendor voluntarily submits an SCAP-enabled
(301) 975-5259
product to a NVLAP-accredited laboratory. Once the lab
melanie.cook@nist.gov
completes product testing, and all validation requirements
are met, the lab submits a test report to the SCAP Validation
Program for review. NIST reviews the test report and will
IDENTITY MANAGEMENT
award a validation if all requirements have been met. Once
a validation is awarded, the SCAP Validation Record is sent
to the lab, and the newly validated product is posted on the Personal Identity Verification (PIV)
SCAP Validated Products web page. and FIPS 201 Revision Efforts
The SCAP Validation Program resources web page
(http://scap.nist.gov/validation) was introduced in FY 2013,
and was updated in FY 2014 to provide the public with a
centralized location for all resources and information
necessary for preparing products for SCAP 1.2 validation.
Resources include documentation, a list of Frequently
Asked Questions (FAQ), the SCAP validation-test content,
and tools for validating and processing SCAP data streams.
The SCAP validation-test content should be used by vendors
for quality assurance testing prior to entering formal SCAP
testing with an NVLAP accredited laboratory. The open-
source tools that are available for download may be used by
SCAP content authors for testing SCAP source content. The
SCAP Content Validation Tool (SCAPVal) may be used to
determine if the content conforms to the SCAP specification.
Open-source SCAP reference implementation tools, such as
the SCAP Reference Implementation Tool, may be used to Figure 17: Government Employees
process SCAP data streams. Use PIV Cards for Facility Access
End users may use information on the SCAP Validation
In response to Homeland Security Presidential
web page to learn about SCAP validation and find products
Directive-12 (HSPD-12), Policy for a Common Identification
that have been awarded validations. The validation records
Standard for Federal Employees and Contractors, FIPS 201,
that are posted on the SCAP Validated Products page
Personal Identity Verification (PIV) of Federal Employees
state the product version that was tested in the laboratory,
and Contractors, was developed and was approved by the
along with details about the validation, such as the tested
Secretary of Commerce in February 2005. HSPD-12 called
platforms, SCAP capabilities, the validation test suite version,
for the creation of a new identity credential for federal
and the lab that performed the product test.
employees and contractors. FIPS 201 is the technical
In FY 2014, five products successfully completed testing specification for both the PIV identity credential and the PIV
and were awarded validations. Several products are in system that produces, manages, and uses the credential.
various stages of validation testing and are expected to be Within NIST’s Information Technology Laboratory (ITL),
awarded validations in FY 2015. The current list of SCAP 1.2 this work is a collaborative effort of the Information Access
validated products may be found on the SCAP Validated
5 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Division (IAD) and CSD. CSD activities in FY 2014 directly • Prepared Draft SP 800-85A-4, PIV Card Applica-
supported the recently revised FIPS 201-2 by updating tion and Middleware Interface Test Guidelines, and
the relevant publications associated with FIPS 201-2 and published Draft SP 800-85B-4, PIV Data Model Test
by developing two new publications. CSD performed the Guidelines, in order to align these documents with FIPS
following activities during FY 2014 in support of HSPD-12: 201-2, SP 800-73-4, and SP 800-78-4.
• Published Draft NISTIR 7863, Cardholder Authentica- • As the NIST PIV Validation Authority, completed the
tion for the PIV Digital Signature Key. The document transition phase from FIPS 201-1 to FIPS 201-2 for vali-
provides clarification for the requirement in FIPS 201-2 dated PIV Card Applications and PIV Middleware.
that a PIV cardholder perform an explicit user action
• Created additional sets of test cards for the inventory
prior to each use of the digital signature key stored on
of PIV test cards. These test cards are available for
the card.
purchase and facilitate the development of applications
• Published two new draft documents to accommodate and middleware that support the PIV card (see
e-authentication with mobile devices: http://csrc.nist.gov/groups/SNS/piv/testcards.html).
− Draft SP 800-157, Guidelines for Derived Personal In FY 2015, CSD will continue to focus on updating
Identity Verification (PIV) Credentials, defines the the relevant publications associated with FIPS 201-2,
technical details for implementing and deploying including developing two new publications: SP 800-156,
derived PIV credentials on mobile devices, such Representation of PIV Chain-of-Trust for Import and Export,
as smart phones and tablets. As intended by FIPS and SP 800-166, Guidelines for Testing Derived Personal
201-2, a derived PIV credential is a PIV credential Identity Verification (PIV) Credentials. CSD will also continue
that can be provisioned directly to a mobile device to provide technical and strategic inputs to the PIV-related
to enable remote enterprise access from the initiatives.
device.
http://csrc.nist.gov/groups/SNS/piv/
− Draft NISTIR 7981, Mobile, PIV, and Authentication,
analyzes and summarizes various current and CONTACTS:
near-term options for remote authentication with
mobile devices that leverage both the investment Ms. Hildegard Ferraiolo Dr. David Cooper
in the PIV infrastructure and the unique security (301) 975-6972 (301) 975-3194
capabilities of mobile devices. hildegard.ferraiolo@nist.gov david.cooper@nist.gov
• Completed the comment resolution of Draft SP 800-
Mr. Salvatore Francomacaro Mr. Ketan Mehta
73-4, Interfaces for Personal Identity Verification, and
(301) 975-6414 (301) 975-8405
published a revised draft. The three-part SP details the
salvatore.francomacaro@nist.gov ketan.mehta@nist.gov
new PIV Card capabilities introduced in FIPS 201-2,
including a Virtual Contact Interface (VCI), a secure
channel protocol, an on-card biometric comparison NIST Personal Identity Verification
mechanism and an enforcement of a minimum PIN Program (NPIVP) & Revisions to FIPS
length of six digits.
201-2 Companion Documents
• Completed the comment resolution of Draft SP 800- The objective of the NIST Personal Identity Verification
78-4, Cryptographic Algorithms and Key Sizes for Program (NPIVP) is to validate PIV components for
Personal Identity Verification, and published a revised conformance to the specifications in FIPS 201, Personal
draft. The document has been modified to align with Identity Verification (PIV) of Federal Employees and
Draft SP 800-73-4, and includes the addition of new Contractors, and its companion documents. The two PIV
algorithms and key sizes for the secure messaging components that come under the scope of NPIVP are the
protocol and the addition of test requirements with the PIV Smart Card Application and the PIV Middleware. NPIVP
Cryptographic Algorithm Validation Program (CAVP) test facilities that perform the two types of tests are the
validation. Cryptographic and Security Testing (CST) Laboratories
that have been accredited by the NIST National Voluntary
• Published Draft SP 800-79, Guidelines for the Accredi-
Laboratory Accreditation Program (NVLAP). As of
tation of Personal Identity Verification (PIV) Card Issu-
September 2014, there were nine such facilities.
ers (PCIs). The draft document incorporates changes
required by FIPS 201-2, including a new set of issuer
controls for Derived PIV Credentials Issuers.
5 1
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

The interface specifications for the PIV Smart Card RESEARCH IN EMERGING
Application and PIV Middleware are found in a FIPS
TECHNOLOGIES
201-associated document, namely, SP 800-73 (the latest
published version SP 800-73-3) - Interfaces for Personal
Identity Verification. The conformance tests for these Cloud Computing and Virtualization
specifications are detailed in SP 800-85A (the latest The model for Cloud Computing is defined in SP 800-145,
published version is SP 800-85A-2) - PIV Card Application The NIST Definition of Cloud Computing. The foundational
and Middleware Interface Test Guidelines. To implement technology that facilitates the use of a computing
these tests and to generate conformance test reports, CSD infrastructure for cloud-computing services is virtualization.
also developed an integrated toolkit called “PIV Interface Test At the core of a virtualized infrastructure is the virtualized
Runner,” which conducts tests on both PIV Card Application host that provides an abstraction of the hardware (e.g., CPU,
and PIV Middleware products, and provides the toolkit to memory) that enables multiple computing stacks (comprised
accredited NPIVP test facilities. of the operating system, middleware, and applications) to be
run on a single physical machine. The efficiency of such a
In 2014, CSD’s activity focused on the transitioning of PIV
dynamic and distributed processing environment is counter-
Card Application and PIV Middleware products from FIPS
balanced by the interoperability, portability, and security
201-1 to FIPS 201-2 compliance. Coordinating with the test
challenges inherent to this computing environment. NIST’s
facilities, FIPS 201-1 products were identified and placed on
CSD is working in parallel on several projects (introduced
the Removed Products List (RPL). Nine PIV card application
below) that aim to accelerate the Federal Government’s
products and fifteen PIV middleware products were
adoption of secure cloud computing by collaborating
affected. With this change, there are 27 NPIVP validated PIV
with standards bodies, and public and private sectors
card application products, and five PIV Middleware products
in developing security, interoperability and portability
listed.
standards and guidance.
In addition, NPIVP is closely involved in ensuring that all
changes in PIV companion documents, such as SP 800-73-4, CSD Role in the NIST Cloud Computing
SP 800-76-2, Biometric Specifications for Personal Identity Program
Verification, and SP 800-78-4, Cryptographic Algorithms
During FY 2013, the NIST Cloud Computing Team
and Key Sizes for Personal Identity Verification, are fully
continued to promote the development of publications,
reflected in the updated versions of the conformance test
national and international standards, and specifications in
documents, SP 800-85A and SP 800-85B, as well as in the
support of the United States Government’s (USG) effective
“PIV Interface Test Runner” toolkit. Currently, the NPIVP
and secure use of cloud computing, as well as providing
team is guiding the development of the “PIV Interface Test
technical guidance to USG agencies for secure and effective
Runner” toolkit for validating PIV Card application and PIV
cloud-computing adoption. CSD supports many of the
Middleware products for conformance to the specifications
technical standards activities supported by the NIST Cloud
in SP 800-73-4, SP 800-76-2 and SP 800-78-4.
Computing Program, with a particular focus on cloud-
http://csrc.nist.gov/groups/SNS/piv/npivp computing security. Activities included the following:
• Led the development of the draft SP 500-299, NIST
Cloud Computing Security Reference Architecture
CONTACTS:
(SRA). SP 500-299 defines a modular framework that
provides a formal model and a methodology for the
Dr. Ramaswamy Chandramouli Ms. Hildegard Ferraiolo
secure adoption of cloud computing by applying a
(301) 975-5013 (301) 975-6972
Cloud-adapted Risk Management Framework (CRMF).
mouli@nist.gov hildegard.ferraiolo@nist.gov
The SRA is a security overlay to SP 500-292, NIST
Cloud Computing Reference Architecture. During FY
2014, the draft document was completed, posted for
public comments, and the received comments were
addressed.
• Co-led the development of the NISTIR 8006, Cloud
Forensics Challenges.
5 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

• Led the development of an internal draft document, • Co-Chaired the NIST Cloud Computing Interoperabil-
Cloud-adapted Risk Management Framework: Guide ity and Portability Working Group. Addressed issues
for Applying the Risk Management Framework to facing cloud computing with respect to interoperability
Cloud-based Federal Information Systems. The docu- and portability, standards, and common and functional
ment introduces a cloud customer-centric approach to terminologies. The goal is to develop guidance and
applying the risk management framework to cloud- best practices for cloud-computing interoperability and
based information systems. This internal draft has not portability that best enable business necessities, such
yet been released for public comment; it is currently as the ability to exchange, use and reuse information/
planned for future publication in the NIST SP 800 data in a cloud environment.
series.
• Co-editor for ISO/IEC AWI 19941 Information technolo-
• Led the research and development of the data that gy – Cloud computing – Interoperability and Portability.
constitutes the foundation of an internal draft docu- This is an effort to develop a standard that focuses on
ment, Security and Privacy Controls for Cloud-based defining the types of cloud-computing interoperabil-
Federal Information Systems. The document will ity and portability; the relationship and interactions
provide a cloud overlay of NIST SP 800-53 Revision between interoperability and portability; the contexts
4 security controls for cloud-based ecosystems. This where interoperability and portability are relevant in
internal draft has not yet been released for public cloud computing, with respect to the cloud-computing
comment; it is currently planned for future publication reference architecture; and the common terminology
in the NIST SP 800 series. and concepts used to describe interoperability and
portability, particularly as they relate to cloud services.
CSD staff members:
• Chair and Vice-Chair of INCITS CS1 (Cybersecurity) −
• Organized and contributed to the seventh NIST Cloud
U.S. Technical Advisory Group (TAG) to the ISO/IEC
Computing Forum and Workshop: The Intersection of
international committee JTC1/SC27 (IT Security Tech-
Cloud and Mobility Forum, March 25-27, 2014; and,
niques). This group is concerned with the development
• Organized and contributed to the first NIST Cloud
of cloud-computing taxonomy-related standards and
Computing Forensic Science Workshop, March 24,
cloud computing security standards.
2014.
CSD staff members participated in various standards
In support of USG cloud-computing mandates, CSD
development organizations, two of which are ISO/IEC JTC
staff members provided leadership for several public cloud
1 Sub Committee 38 – Distributed Application Platforms
working groups operating under the NIST Cloud Computing
and Services (SC 38) and ISO/IEC JTC 1 Sub Committee
Program. These working groups focus on meeting the
27 – IT Security Techniques (SC 27). In SC 38, CSD acts as
high priority requirements contained in SP 500-293, U.S.
the co-convener for a collaborative ISO/ITU-T initiative on
Government Cloud Computing Technology Roadmap.
cloud computing taxonomy that includes publication of
CSD staff chaired or co-chaired several significant cloud ISO/IEC 17788 – Information Technology – Cloud computing
computing efforts in 2014: – Overview and Vocabulary, and ISO/IEC 17789 Information
technology – Cloud computing – Reference Architecture.
• Co-Chaired the NIST Cloud Computing Security Work-
These standards are a joint collaborative work between ITU-T
ing Group. Led the group on the development of the
and ISO, and they are approved to be available at no charge.
SP 500-299, NIST Cloud Computing Security Reference
Notably, the genesis for this international body of work is the
Architecture; SP 800-163, Cloud-adapted Risk Manage-
widely accepted and used cloud-computing definition found
ment Framework: Guide for Applying the Risk Manage-
in SP 800-145, NIST Definition of Cloud Computing.
ment Framework to Cloud-based Federal Information
Systems; SP 800-174, Security and Privacy Controls for There are three new standards under development:
Cloud-based Federal Information Systems (all three
• ISO/IEC 19086 Information Technology - Cloud Com-
described above); and on researching cryptographic
puting - Service Level Agreement (SLA) Framework.
key-management challenges in cloud ecosystems.
This international standard has three parts, where Part 1
• Co-Chaired the NIST Cloud Computing Forensic Sci- specifies an overview of SLAs for cloud services, identi-
ence Working Group. Led the development of NISTIR fication of the relationship between the master service
8006, NIST Cloud Computing Forensics Challenges. agreement and the SLA, SLA concepts and require-
ments that can be used to build SLAs, and terms
5 3
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

and metrics commonly used in SLAs for cloud services. Additional information about the NIST Cloud Computing
This standard is for the benefit and use of both the Program is available at:
provider and customer. Part 2 specifies a model and http://www.nist.gov/itl/cloud
metrics for describing and measuring properties of the http://collaborate.nist.gov/twiki-cloud-computing/bin/
concepts and components in 19086. This standard is for view/CloudComputing/StandardsRoadmap
the benefit and use of both the provider and customer, http://collaborate.nist.gov/twiki-cloud-computing/bin/
and Part 3 specifies core conformance requirements for view/CloudComputing/CloudSecurity
SLAs for cloud services for ISO/IEC 19086. http://collaborate.nist.gov/twiki-cloud-computing/bin/
view/CloudComputing/CloudForensics
• I SO/IEC 19941 Information Technology - Cloud Comput-
ing – Interoperability and Portability. This international
standard specifies cloud-computing interoperability CONTACTS:
and portability types; the relationship and interactions
Dr. Michaela Iorga
between these two aspects; and common terminology
Chair, Cloud Computing Security Workgroup
and concepts used to discuss interoperability and por-
(301) 975-8431
tability, particularly relating to cloud services.
michaela.iorga@nist.gov
• ISO/IEC 19944 Information Technology - Cloud Com-
puting - Data and their Flow across Devices and Cloud
Ms. Annie Sokol
Services. This International Standard defines the
Co-Chair, Cloud Computing Standards Roadmap
reference architecture for mobile-to-cloud ecosystems,
(301) 975-2006
while providing the necessary structure that allows for
annie.sokol@nist.gov
data-flow transparency between portable devices and
the cloud services ecosystem.
Mr. Daniel Benigni
CSD staff members are also actively participating in 2014 Chair, INCITS CS1 (Cybersecurity) - U.S. Technical
the development of cloud-computing security standards, Advisory Group (TAG) to the ISO/IEC international
primarily through INCITS CS1, SC 27, which is responsible committee JTC1/SC27 (IT Security Techniques)
for cloud-computing security standards for ISO. CSD has (For 2015 – contact Mr. Salvatore Francomacaro – contact
provided technical contributions based on SP 500-299 information below)
and continues to advocate for secure, non-proprietary
solutions. There is a continued contribution to a number of Mr. Salvatore Francomacaro
cloud-related standards, including the recently approved Vice-Chair, INCITS CS1 (Cybersecurity) - U.S. Technical
international standard, ISO/IEC 27018, Information Advisory Group (TAG) to the ISO/IEC international
technology – Security techniques – Code of practice for committee JTC1/SC27 (IT Security Techniques)
protection of personal identifiable information (PII) in public (301) 975-6414
clouds acting as PII processors, ISO/IEC WD 27036-4, salvatore.francomacaro@nist.gov
Information technology – Information security for supplier
relationships – Part 4: Guidelines for security of Cloud Cryptographic Key Management Issues in Cloud
services, and the commencement of a study period on cloud Infrastructures
components, controls and capabilities. Dr. Ramaswamy Chandramouli Dr. Michaela Iorga
(301) 975-5013 (301) 975-8431
In FY 2014, the CSD members of the NIST cloud-
mouli@nist.gov michaela.iorga@nist.gov
computing team continued research in key areas of cloud
security, cloud interoperability and portability, cloud metrics,
cloud services, and cloud SLAs. They also presented the
results of cloud-computing research and development,
introduced the standards and specifications under
development, and provided the status of the NIST Cloud-
Computing Program in a variety of domestic and international
conferences and workshops. CSD staff continues to engage
industry and federal agencies for inputs and collaborative
work through working groups, publications, and networking.
5 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Policy Machine – Leveraging Access Project 2195–D: NGAC Generic Operations & Abstract Data
Control for Cloud Computing Structures (NGAC-GOADS), has begun the approval process,
and is expected to reach the second Public Review stage in
the summer of 2015.
In FY 2015, CSD plans to issue a new version of its open-
source distribution to reflect new features and enhanced
performance, and publish a NISTIR 7987 revision to reflect
greater consistence with NGAC’s suite of standards.
http://csrc.nist.gov/pm/
CONTACTS:
Mr. David Ferraiolo Mr. Serban Gavrila
(301) 975-3046 (301) 975-4242
david.ferraiolo@nist.gov serban.gavrila@nist.gov
Figure 18: Policy Machine Operating
Environment
Virtualization Security & Leveraging
In FY 2014, CSD continued the research and development
Virtualization for Security
of a virtualization-based, enterprise-wide controlled delivery
In FY 2014, CSD continued its research in key areas
of data services for advanced cloud computing through
of cloud and virtualization security by producing two
Access Control. This included the publication of a detailed
conference papers and one SP:
Policy Machine specification as NISTIR 7987, Policy Machine:
Features, Architecture, and Specification, in May 2014. • Conference Papers: “Analysis of Protection Options for
The team also published a description of the benefits and Virtualized Infrastructures in Infrastructure as a Service
an approach of the Policy Machine’s integration of Access Cloud ” and “Deployment-driven Security Configura-
Control and Data Services as a conference paper, On the tion for Virtual Networks;” and
Unification of Access Control and Data Service, in the
• Special Publication: SP 800-125A, Security Recom-
proceedings of the IEEE 15th International Conference of
mendations for Hypervisor Deployment (submitted for
Information Reuse and Integration, August 2014. In addition,
public comment).
CSD released its reference implementation of the Policy
The focus of research for FY 2015 in the area of Virtualized
Machine as open source (available at GitHub).
Infrastructures is two-pronged. The first approach will focus
NIST and other members of an Ad Hoc INCITS working
on identifying the security requirements for various use
group are developing a three-part Policy Machine standard,
cases involved in offering cloud services using virtualized
under the title of Next Generation Access Control (NGAC),
infrastructures and analyzing the protection options to
under three sub-projects:
meet those security requirements in terms of their features,
• P roject 2193–D: Next Generation Access Control – security strengths and architectural foundation. The second
Implementation Requirements, Protocols and API approach will focus on deriving secure configuration
Definitions; operations in a specific area of virtualized infrastructure – the
Virtual Network – leveraging state-of-the-art architectural
• P roject 2194–D: Next Generation Access Control –
paradigms, such as the Software-defined network (SDN).
Functional Architecture; and
The security recommendations for Hypervisor deployment
• P roject 2195–D: Next Generation Access Control –
will cover two areas: one based on architectural choices, and
Generic Operations & Abstract Data Structures.
the other based on configuration parameters. For developing
The Policy Machine’s architecture was the basis for the configuration parameters that form the basis of security
the NGAC work within INCITS. An initial standard from this recommendations, the following approach will be adopted:
work was published in 2013 and is now available from the
• The baseline functions of the hypervisor will be iden-
ANSI e-standards store as INCITS 499 – NGAC Functional
tified along with their associated interfaces and threat
Architecture (NGAC–FA). The standard resulting from
sources; and
5 5
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

• The protection measures against those threats will then prior to being deployed on thousands of military mobile
form the security recommendations for hypervisor de- devices for use in the current U.S. war theater, the 2013
ployment. The security recommendations will cover all Presidential Inauguration, and the 2014 Boston Marathon.
known implementations of baseline functions, making
NIST’s work in mobile security has earned the 2014
them applicable across multiple hypervisor designs.
Government Computer News (GCN) award for Information
Technology Excellence and the 2013 U.S. Department
CONTACT: of Commerce Gold Medal Award. For FY 2015, NIST will
continue to develop and transition mobile security-related
Dr. Ramaswamy Chandramouli
technologies, publish guidance on issues of mobile security,
(301) 975-5013
and provide mobile security expertise to industry and other
mouli@nist.gov
government agencies.
CONTACTS:
MOBILE SECURITY
Dr. Steve Quirolgico Dr. Jeffrey Voas
Smart phones have become both ubiquitous and (301) 975-8426 (301) 975-6622
indispensable for consumers and business people alike. steveq@nist.gov jeff.voas@nist.gov
Although these devices are relatively small and inexpensive,
they can be used for voice calls, simple text messages, Dr. Tom Karygiannis
sending and receiving emails, browsing the web, online (301) 975-4728
banking and e-commerce, social networking, and many karygiannis@nist.gov
functions once limited to laptop and desktop computers.
Smart phones and tablet devices have specialized built-in
hardware, such as photographic cameras, video cameras, STRENGTHENING INTERNET
accelerometers, Global Positioning System (GPS) receivers,
SECURITY
and removable media readers. They also employ a wide range
of wireless interfaces, including infrared, Wireless Fidelity
(Wi-Fi), Bluetooth, Near Field Communications (NFC), and USGv6: A Technical Infrastructure to
one or more types of cellular interfaces that provide network Assist IPv6 Adoption
connectivity across the globe. Naturally, just as consumers
Internet Protocol (IP) Version 6 (IPv6) is an updated
and businesses can realize productivity gains from these
version of the current Internet Protocol, IPv4. The primary
technologies, so can government agencies.
motivations for the development of IPv6 were to increase
Like any new technology, smart phones present new the number of unique IP addresses available for use and to
capabilities, but also a number of new security and privacy handle the needs of new Internet applications and devices.
challenges. As the pace of the technology life cycles In addition, IPv6 was designed with the following goals:
continues to increase, current Information Assurance increased ease of network management and configuration,
(IA) standards and processes must be updated and new expandable IP headers, improved mobility and security, and
technologies adopted to allow government users to employ the quality of service controls. IPv6 has been, and continues
the latest technologies that consumers can use without to be, developed and defined by the Internet Engineering
sacrificing privacy and security. Task Force (IETF).
NIST is conducting research in software-assurance FY 2012 was a significant year for the deployment
methodologies for smart phone software (i.e., applications, of IPv6 in the United States Government (USG). OMB’s
commonly referred to as “apps”) and is working with other Memo of September 10, 2010, Transition to IPv6, required
government agencies and industry to bridge the security all government agencies to “upgrade public/external
gaps present with today’s smart phones. For example, facing servers and services (e.g., web, email, Domain Name
NIST developed an app-vetting system and framework System (DNS), Internet Service Provider (ISP) services) to
for managing an organization’s app-vetting process with operationally use IPv6 by the end of FY 2012.” NIST worked
respect to the organization’s security and privacy policies with the USGv6 Task Force and with individual government
and requirements. This system was used by the Defense agencies to achieve this goal. NIST developed an online
Advanced Research Projects Agency (DARPA) to vet apps monitor to demonstrate which high-level government
5 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

domains have met this goal with respect to DNS services,  •   Implemented a fault-detection method for an access
email, web servers, and Domain Name System Security  control rule using Simulated Logic Circuit algorithms;
Extensions (DNSSEC). In FY 2013, NIST and OMB continued
|     |     |     |     |     |     | •   Studied formal Attribute-Based Access Control (ABAC)  |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- |
to use this monitor to measure USGv6 compliance with
models;
OMB’s requirement.
|             |      |       |               |                 |     | •   Published the SP 800-162, Guide to Attribute Based  |     |     |
| ----------- | ---- | ----- | ------------- | --------------- | --- | ------------------------------------------------------- | --- | --- |
| Additional  | OMB  | IPv6  | requirements  | were  mandated  |     |                                                         |     |     |
Access Control (ABAC) Definition and Considerations,
for FY 2014. Agencies were required to “upgrade internal
which provides information for function components,
client applications that communicate with public Internet
as well as an enterprise consideration of ABAC;
servers and supporting enterprise networks to operationally
|     |     |     |     |     |     | •   Studied an Access Control scheme for Big Data Pro- |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- |
use IPv6 by the end of FY 2014.” NIST developed online
cessing; and
diagnostic tools to help agencies verify compliance to this
requirement. •   Studied an assurance mechanism for ABAC attributes.
The  NIST  IPv6  Test  Program,  whose  goal  is  to  In FY 2015, CSD will continue the above research, and
| provide  assurance  |     | on  IPv6  | product  | conformance  | and  |     |     |     |
| ------------------- | --- | --------- | -------- | ------------ | ---- | --- | --- | --- |
present the most updated results in CSD’s CSRC website.
interoperability, continues to operate. In FY 2015, NIST will  CSD expects that this project will:
continue to manage and evolve the USGv6 Test Program
|                |          |           |          |                |      | •   Promote (or accelerate) the adoption of community  |     |     |
| -------------- | -------- | --------- | -------- | -------------- | ---- | ------------------------------------------------------ | --- | --- |
| and  to  help  | federal  | agencies  | fulfill  | OMB  mandates  | and  |                                                        |     |     |
computing that utilizes the power of shared resources
monitor compliance to those mandates. The NIST program is
and common trust-management schemes;
a collaboration between CSD and the Advanced Networking
|     |     |     |     |     |     | •   Provide guidance for implementing access control  |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
Technology Division.
models and mechanisms for standalone or enterprise
http://www.antd.nist.gov/usgv6
systems;
|     |     |     |     |     |     | •   Increase the security and safety of static (connected)  |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- |
CONTACTS:
distributed systems by applying the testing and verifi-
cation tool for the access control policies;
| Ms. Sheila Frankel  |     |     | Mr. Douglas Montgomery  |     |     |                                                             |     |     |
| ------------------- | --- | --- | ----------------------- | --- | --- | ----------------------------------------------------------- | --- | --- |
| (301) 975-3297      |     |     | (301) 975-3630          |     |     |                                                             |     |     |
|                     |     |     |                         |     |     | •   Assist system architects, security administrators, and  |     |     |
sheila.frankel@nist.gov    dougm@nist.gov security managers whose expertise is related to access
control or privilege policy in managing their systems
and in learning the limitations and practical approaches
| ACCESS CONTROL AND  |     |     |     |     |     | for their applications; and |     |     |
| ------------------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
PRIVILEGE MANAGEMENT •   Provide accurate and efficient fault detection and
correction technology for implementing access control
rules and policies.
Access Control and Privilege
See Figure 19 on next page for chart of Access Control
Management Research
and Privilege Management.
With the advance of current computing technologies
and the diverse environments in which these technologies
are used, security issues, such as situational awareness, trust  CONTACTS:
management, preservation of privacy in access control, and
|     |     |     |     |     |     | Dr. Vincent Hu  |     | Mr. David Ferraiolo  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------------------- |
privilege-management systems, are becoming increasingly
|     |     |     |     |     |     | (301) 975-4975  |     | (301) 975-3046  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- |
complex. Practical and conceptual guidance for these topics
|     |     |     |     |     |     | vhu@nist.gov  |     | david.ferraiolo@nist.gov |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------------ |
is needed.
In FY 2014, the following research was accomplished for
Mr. Rick Kuhn
| this project:                                           |     |     |     |     |     | (301) 975-3337  |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- |
| •   Enhanced the unified enforcement mechanism of data  |     |     |     |     |     | kuhn@nist.gov   |     |     |
services for use by a Policy Machine (PM) for an enter-
prise computing environment;
•   Enhanced the capabilities of the Access Control Policy
Tool (ACPT);
57
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

To address the issue, CSD researched the AC Rule Logic
Circuit Simulation (ACRLCS) technique, which enables the
AC authors to detect a fault when the fault-causing AC rule
is added to the policy, so the fix can be implemented in
real time before adding other rules that further complicate
the detecting effort. Rather than checking by retracing the
interrelations between rules after the policy is completed,
the policy author needs to only check the newly added
rule against previous “correct” ones. In ACRLCS, AC rules
are represented in a Simulated Logic Circuit (SLC). The
use of simulation may restrict ACRLCS implementation on
a physical electronic circuit; however, the concept can be
implemented and computed through simulated software. In
FY 2014, CSD accomplished the following:
Figure 19: Access Control and Privilege Management • Researched the ACRLCS, and implemented a prototype
access control rule composing system - the Access
Control Rule Logic Circuit Simulation System;
Conformance Verification for Access- • Worked with industrial and academic organizations in
Control Policies exploring new capabilities that helped to improve the
To formally and precisely capture the security properties usability of the AC tools (ACPT and ACRLCS);
that access control (AC) should adhere to, access control
• Enhanced the capability of ACPT by improving user in-
models are usually written to bridge the rather wide gap in
terfaces and adding privilege inheritance and multiple
abstraction between policy and mechanism. Thus, an access-
policy combination algorithms;
control model provides unambiguous and precise expression,
• Performed prototype testing; and
as well as a reference for design and implementation of
security requirements. Techniques are required for verifying • ACPT was downloaded by 277 users and organizations.
whether an access-control model is correctly expressed in
In FY 2015, CSD is planning to conduct further research
the access-control policies and whether the properties are
on the new capabilities and enhance performance of the
satisfied in the model.
ACPT and ACRLCS.
Most research on AC model or policy verification
techniques are focused on one particular model, and almost
all of the research is in applied methods, which require the
completed AC policies as the input for verification or test
processes to generate fault reports. Even though correct
verification is achieved, and counterexamples may be
generated when faults were found, those methods provide
no information about the source of faults that might allow
conflicts in privilege assignment, leakage of privileges, or
conflict of interest permissions. The difficulty in finding the
source of faults is increased, especially when the AC rules
are intricately covering duplicated variables to a degree of
complexity. The complexity is due to the fact that a fault
might not be caused by one particular rule. Thus, it requires
manually analyzing each rule in the policy in order to find the
correct solution for the fault.
Figure 20: Conformance Verification
5 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

This project is expected to: There has not been a comprehensive effort to formally
define or guide the implementation of ABAC within the
• Provide a generic paradigm and framework of access
Federal Government. This research provides considerations
control model/property conformance testing;
for using ABAC to improve information sharing within and
• Provide templates for specifying access control rules
among organizations, while maintaining control of that
in popular access control models, such as the Attribute
information. The research serves a two-fold purpose. First,
Based, Multilevel, and Workflow models;
it aims to provide federal agencies with a definition of ABAC
• Provide tools or services for checking the security and and a description of the functional components of ABAC.
safety of an access control implementation, policy Second, it provides planning, design, implementation, and
combination, and eXtensible Access Control Markup operational considerations for employing ABAC within a
Language (XACML) policy generation; large enterprise with the goal of improving information
sharing while maintaining control of that information.
• Promote (or accelerate) the adoption of combinatorial
In addition to the core concept (i.e. definition and
testing for large-system testing (such as an access
consideration), ABAC research includes technologies such
control system);
as attribute assurance, attribute engineering/management,
• Promote the concept of detecting AC policy faults in
identity system integration, attribute federation, situational
real time AC rule composing;
awareness (real time or contextual) mechanism, policy
• Provide an innovative method in specifying AC rules management, and natural-language policy translation to
formed by Boolean logic expressions operated on vari- digital policy.
ables of AC rules;
In FY 2014, CSD published SP 800-162, Guide to
• Provide techniques for preventing faults in enforcing Attribute Based Access Control (ABAC) Definition and
fundamental security properties, including Cyclic In- Considerations. SP 800-162 includes terminology and basic
heritance, Privilege Escalation, and Separation of Duty; understanding of ABAC; ABAC enterprise-employment
and considerations during the initiation, acquisition/development,
implementation/assessment, and operations and
• Provide new methods for composing standard man-
maintenance phases; and an example to demonstrate how
datory AC models, such as Role-Based Access Control
ABAC is implemented in a Web Information Portal. CSD also
(RBAC) and Multi-Level Security (MLS), as well as some
researched ABAC formal models; the result will be presented
fundamental security properties.
in a NISTIR that will describe a variety of characteristics
http://csrc.nist.gov/groups/SNS/acpt/ and applications of ABAC formal models. CSD also started
research on the Attribute Assurance of ABAC in partnership
CONTACTS: with the National Security Agency (NSA), the National
Strategy for Trusted Identities in Cyberspace (NSTIC), and
Dr. Vincent Hu Mr. Rick Kuhn
the National Cybersecurity Center of Excellence (NCCoE);
(301) 975-4975 (301) 975-3337
CSD developed a white paper based on the mechanism for
vhu@nist.gov kuhn@nist.gov
defining the levels of assurance of ABAC attributes, as well
as collecting use cases, current standards, and engineering
Attribute-Based Access Control experiences through a Request for Information (RFI) and
Attribute-Based Access Control (ABAC) is a logical working with ABAC user/commercial product communities.
access control methodology where an authorization to In FY 2015, CSD will continue the research of ABAC
perform a set of operations is determined by evaluating the formal models, as well as details and extended topics of
attributes associated with the subject, object, requested ABAC capabilities, such as Attribute Assurance, ABAC
operations, and, in some cases, environment conditions implementation examples, and ABAC standards. The ABAC
against policy, rules, or relationships that describe the project will pursue the following objectives:
allowable operations for a given set of attributes. ABAC
• Provide readers with the terminology and a basic un-
represents a point on the spectrum of logical access control,
derstanding of ABAC;
from simple access control lists to more capable role-based
access (RBAC), and finally, to a highly flexible method for • Provide readers with an overview of the current state
providing access based on the evaluation of attributes. of logical access control, a working definition of ABAC,
and an explanation of the core and enterprise ABAC
concepts;
5 9
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

• Assist security policy makers in establishing a busi- http://csrc.nist.gov/projects/abac/
ness case for ABAC implementation, and acquiring an
interoperable set of capabilities; CONTACTS:
• Assist ABAC developers in developing the operational
Dr. Vincent Hu Mr. David Ferraiolo
requirements and overall enterprise architecture;
(301) 975-4975 (301) 975-3046
• Assist ABAC administrators in establishing or refining
vhu@nist.gov david.ferraiolo@nist.gov
business processes to support ABAC; and
• Promote the adoption of ABAC for a more secure and Mr. Rick Kuhn
flexible method for information sharing in a standalone (301) 975-3337
or enterprise environment. kuhn@nist.gov
Figure 21: ABAC Access Control Mechanism Chart
6 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

 ADVANCED SECURITY TEST- Specification, Standards, and Guidance
| ING AND MEASUREMENTS |     |     |     |     | Development |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
To support the overarching security automation vision, it
is necessary to have specifications that describe the required
Security Automation and Continuous
|     |     |     |     |     | interactions  | between  | systems,  |     | standards  | that  document  |     |
| --- | --- | --- | --- | --- | ------------- | -------- | --------- | --- | ---------- | --------------- | --- |
Monitoring international  consensus  approaches,  and  guidance  that
IT organizations operate a diverse set of computing  informs  product  developers  and  implementers.  Through
assets that access, route, store, and process information that
|     |     |     |     |     | close  work  | with  | partners  | in  | government,  | industry,  | and  |
| --- | --- | --- | --- | --- | ------------ | ----- | --------- | --- | ------------ | ---------- | ---- |
is critical to the operations of businesses and the missions  academia, NIST CSD continues to facilitate the definition
of  government  agencies.  These  IT  environments  are  and development of security automation approaches that
frequently reconfigured, and are under constant threat of  enable organizations to understand and manage IT security
| attack. The wide variety of computing products, the speed  |     |     |     |     | risks. |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
of configuration change, and the diversity of threats require
|     |     |     |     |     | During  | FY  2014,  | CSD  | worked  | to  | build  on  | previous  |
| --- | --- | --- | --- | --- | ------- | ---------- | ---- | ------- | --- | ---------- | --------- |
organizations to maintain situational awareness over their
security automation work by:
IT assets and to utilize this information to make risk-based
decisions. •   Participating in working groups in standards develop-
ment organizations to promote international consensus
Security automation utilizes standardized data formats
around standardized approaches;
and transport protocols to enable data to be exchanged
•   Identifying and addressing gaps in the current specifi-
between business, operational, and security systems that
| support security processes by: |     |     |     |     | cations; |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
•   Evolving existing approaches to achieve greater scal-
•  Identifying IT assets;
ability and impact;
•   Providing awareness over the operational state of com-
puting devices; •   Providing additional guidance on architectural, design,
and analysis concerns; and
•   Enabling security reference data to be collected from
internal and external sources; and •   The development and maintenance of tools and refer-
ence implementations.
•   Supporting analysis processes that measure the effec-
tiveness of security controls and provide visibility into  CSD is currently working with its partners in various
|     |     |     |     |     | standards-development  |     |     | organizations,  |     | including  | the  |
| --- | --- | --- | --- | --- | ---------------------- | --- | --- | --------------- | --- | ---------- | ---- |
security risks, enabling risk-based decision making.
|     |     |     |     |     | International  | Organization  |     | for  | Standardization  | (ISO),  | the  |
| --- | --- | --- | --- | --- | -------------- | ------------- | --- | ---- | ---------------- | ------- | ---- |
Commercial solutions built using security-automation
Internet Engineering Task Force (IETF), the Forum of Incident
specifications enable the collection and harmonization of
|     |     |     |     |     | Response and  | Security Teams (FIRST), and the Trusted  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------- | ---------------------------------------- | --- | --- | --- | --- | --- |
vast amounts of operational and security data into coherent,
Computing Group (TCG), to further mature and broaden the
| comparable  | information  | streams  | to  achieve  | situational  |     |     |     |     |     |     |     |
| ----------- | ------------ | -------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
adoption of security-automation specifications, reference
awareness that allows timely and active management of
data, and techniques. This area of work is focused on evolving
diverse IT systems. Through the creation of reference data
security-automation specifications to integrate with existing
and guidance, and the international recognition of flexible,
transport protocols to provide for the secure, interoperable
| open  standards,  | the  | NIST  security-automation  |     | program  |           |                          |     |     |        |             |       |
| ----------------- | ---- | -------------------------- | --- | -------- | --------- | ------------------------ | --- | --- | ------ | ----------- | ----- |
|                   |      |                            |     |          | exchange  | of  security-automation  |     |     | data.  | Additional  | work  |
works to improve the interoperability, broad acceptance,
|                |               |                      |              |            | is  focused  | on  evolving  |     | security             | metrics  | and          | providing  |
| -------------- | ------------- | -------------------- | ------------ | ---------- | ------------ | ------------- | --- | -------------------- | -------- | ------------ | ---------- |
| and  adoption  | of            | security-automation  | solutions    | to         |              |               |     |                      |          |              |            |
|                |               |                      |              |            | consensus    | guidance      | on  | security-automation  |          | approaches.  |            |
| address        | current  and  | future  security     | challenges,  | creating   |              |               |     |                      |          |              |            |
Through the definition and adoption of security-automation
opportunities for innovation.
standards and guidelines, IT vendors will be able to provide
standardized security solutions to their customers. These
solutions support continuous monitoring and automated,
dynamic network defense capabilities based on the analysis
of data from operational and security data sources and the
collective action of security components.
61
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

Security-automation work has been focused in two In September 2012, CSD published SP 800-126
areas: the evolution and international adoption of the Revision 2, The Technical Specification for the Security
Security Content Automation Protocol (SCAP), and the Content Automation Protocol (SCAP): SCAP Version 1.2.
development of a Continuous Monitoring building block That document describes the 11 component specifications
focused on secure software asset management capabilities. composing SCAP. See Table on next page.
The following sections detail this work.
Since the release of SCAP 1.2, CSD has worked to improve
guidance around the SCAP specifications by promoting a
Security Content Automation Protocol
broader international adoption of SCAP, encouraging the
(SCAP)
integration of SCAP into other standards, and by adapting
SCAP is a multipurpose protocol that provides an
SCAP to address specific gaps and challenges. The sections
automated means to collect and assess the state of devices.
describe work activities performed during FY 2014.
SCAP supports automated vulnerability checking, verifying
the installation of patches, checking-security configuration CSD has continued its collaboration with industry
settings, verifying technical-control compliance, measuring partners in the IETF Security Automation and Continuous
security, and examining systems for indicators of a Monitoring (SACM) working group. This working group
compromise. SCAP uses the Extensible Markup Language provides a venue for advancing appropriate SCAP
(XML) to standardize the format and nomenclature by which specifications into international standards and addressing
security software products communicate information about identified gap areas. The current scope of work for SACM
software flaws, security configurations, and other aspects includes identifying and/or defining the transport protocols
of device state. SCAP enables security-automation content, and data formats needed to support the collection and
also known as “SCAP content,” to be expressed using evaluation of a device state against the expected values
standardized formats, identifiers, and scoring models. This and standards for interacting with repositories of security-
content can be used by any tool that is conformant to the automation content. Over the past twelve months, the SACM
specifications, to collect and evaluate the state of software working group has been working on identifying use cases,
installed on a device. requirements, and architectural models to inform decisions
SCAP has been widely adopted by major software about existing specifications and standards that can be
and hardware manufacturers and has become a significant referenced, required modifications or extensions to existing
component of information-security-management and specifications and standards, and any gaps that need to be
governance programs. SCAP-enabled tools are currently addressed.
being used by the U.S. Government, critical-infrastructure
The working group has been developing the following
companies, academia, and other businesses, both
Internet drafts:
domestically and internationally. Currently, CSD is leveraging
SCAP in multiple areas, both to support its own mission
and to enable other agencies and private-sector entities
to meet their goals. For CSD, SCAP is a critical component
of the SCAP Validation Program, the National Vulnerability
Database (NVD), and the National Checklist Program (NCP).
INTERNET DRAFT PURPOSE
https://datatracker.ietf.org/doc/draft-ietf-sacm- Definition of the common terminology used within a
terminology/ number of working-group documents.
Description of use cases and related capabilities to guide
https://datatracker.ietf.org/doc/draft-ietf-sacm-use-cases/ the development of requirements, architecture, and
specifications for data models and transports.
https://datatracker.ietf.org/doc/draft-ietf-sacm- Listing architectural and specification requirements for
requirements/ SACM specifications.
6 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

SCAP 1.2 SPECIFICATIONS
SPECIFICATION DESCRIPTION
Languages
Extensible Configuration Checklist Description Format Used for authoring security checklists/benchmarks and
(XCCDF) for reporting results of evaluating them
Used for representing system-configuration information,
Open Vulnerability and Assessment Language (OVAL)
assessing machine state, and reporting assessment results
Used for representing checks that collect information from
Open Checklist Interactive Language (OCIL) people or from existing data stores populated by other
data collection methods
Reporting Formats
Used to express information about assets and to define
Asset Reporting Format (ARF)
the relationships between assets and reports
Used to uniquely identify assets based on known
Asset Identification
identifiers and other asset information
Enumerations
A nomenclature and dictionary of hardware, operating
Common Platform Enumeration (CPE) systems, and applications; a method to identify
applicability to platforms
A nomenclature and dictionary of software-security
Common Configuration Enumeration (CCE)
configurations
A nomenclature and dictionary of security-related
Common Vulnerabilities and Exposures (CVE)
software flaws
Measurement and Scoring Systems
Common Vulnerability Scoring System (CVSS) Used for measuring the relative severity of software flaws
Used for measuring the relative severity of device security
Common Configuration Scoring System (CCSS)
(mis-)configuration issues
Content and Result Integrity
Guidance for using digital signatures in a common trust
Trust Model for Security Automation Data (TMSAD)
model applied to security-automation specifications
For more information, please refer to: dependency, bundling, and patch), executable and library
http://datatracker.ietf.org/wg/sacm/charter/ footprint details, and other metadata for software that they
publish. This information enhances the SCAP use cases
Additionally, CSD collaborated with industry partners
by providing authoritative information for the creation of
to revise the ISO/IEC 19770-2:2009 standard, Information
Common Platform Enumeration (CPE) names, the targeting
technology—Software asset management—Part 2: Software
of checklists, and associating software flaws to products
identification tag, which establishes a specification for
based on a defect in a software library or executable.
tagging software to support identification and management.
This software-identification (SWID) data model defines a CSD also worked with government and industry partners
mechanism for software publishers to provide authoritative in the TCG to define a number of specifications related to
identification, categorization, software relationship (e.g., the Trusted Network Connect (TNC) protocols. The first such
6 3
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

publication is the TNC SCAP Messages for IF-M specification  Continuous Monitoring
that supports carrying SCAP content and results over the
|     |     |     |     |     |     |     | In  | September  | 2010,  | the  | Department  |     | of  Homeland  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---- | ----------- | --- | ------------- | --- |
TNC protocols. The second is the TNC Enterprise Compliance  Security (DHS) released the Continuous Asset Evaluation,
Profile (ECP) and related specifications that support the  Situational  Awareness  and  Risk  Scoring  (CAESARS)
exchange of SWID data over the TNC protocols. The ECP
|     |     |     |     |     |     |     | Reference  | Architecture  |     | Report.  | This  | report  |     | identifies  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | -------- | ----- | ------- | --- | ----------- |
enables the collection of SWID data from a device for use  commonality and strengths in the custom approaches used
by external tools to provide software inventory information.
by civilian agencies to provide solutions that enable the
SCAP and SWID data collected using these mechanisms  continuous monitoring of IT systems. This report identifies
may be optionally used for network access-control decision  “essential functional components of a security risk-scoring
making, allowing the device state to be evaluated when
|     |     |     |     |     |     |     | system,  | independent  |     | of  specific  | technologies,  |     | products,  |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ------------- | -------------- | --- | ---------- | --- |
devices connect and on an ongoing basis thereafter. or vendors.” It describes the use of security-automation
For more information on these specifications, please  specifications,  such  as  the  SCAP,  to  enable  continuous
monitoring solutions.
visit: http://www.trustedcomputinggroup.org/resources/
tnc_scap_messages_for_ifm, and   In  October  2010,  the  Federal  Chief  Information
http://www.trustedcomputinggroup.org/resources/tnc_ Officer  Council’s  Information  Security  and  Identity
endpoint_compliance_profile_specification. Management  Committee’s  (ISIMC)  subcommittee  on
Finally, CSD has worked with the Forum of Incident  Continuous Monitoring and Risk Scoring saw the need to
create a technical initiative to expand upon the CAESARS
Response and Security Teams (FIRST) by participating in
two Special Interest Groups (SIG). The CVSS SIG (CVSS-SIG)  architecture to better scale it to large enterprises (e.g., the
entire U.S. Government). A team of researchers from the
focused on defining CVSS Revision 3, which is intended to
|     |     |     |     |     |     |     | NSA  Information  |     | Assurance  | Directorate  |     | (IAD),  |     | the  DHS  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | ------------ | --- | ------- | --- | --------- |
implement improvements to the scoring model, based on
community feedback. The CVSS-SIG is currently working  Federal Network Security CAESARS team, and CSD worked
|     |     |     |     |     |     |     | together  | to  respond  |     | to  this  | need.  | The  draft  | CAESARS  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --------- | ------ | ----------- | -------- | --- |
on the CVSS revision, which will be released in FY 2015. The
second SIG, the Vulnerability Reporting and Data eXchange  Framework Extension (CAESARS-FE) described by Draft
NISTIR 7756, CAESARS Framework Extension: An Enterprise
SIG (VRDX-SIG), researches and recommends methods for
Continuous Monitoring Technical Reference Architecture, is
identifying and exchanging vulnerability information across
disparate vulnerability databases. the output of this collaboration.
Draft NISTIR 7756 presents an enterprise continuous-
For more information, please visit:
http://www.first.org/global/sigs. monitoring (ConMon) technical reference architecture that
extends the framework provided by the DHS’s CAESARS
| Through  | work  | with  | international  |     | SDOs,  SCAP  | and  |     |     |     |     |     |     |     |     |
| -------- | ----- | ----- | -------------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
architecture. The primary goal of this effort is to enable
| related  | security-automation  |     | capabilities  |     | are  expected  |     |     |     |     |     |     |     |     |     |
| -------- | -------------------- | --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
enterprise ConMon by supporting the development and
to evolve and expand in support of the growing need to
|     |     |     |     |     |     |     | deployment  |     | of  capabilities  |     | that  | support  | automated,  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------------- | --- | ----- | -------- | ----------- | --- |
define and measure effective security controls, assess and
|     |     |     |     |     |     |     | enterprise-wide  |     | ConMon  | functions.  |     | The  | concepts,  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ----------- | --- | ---- | ---------- | --- |
monitor ongoing aspects of information security, remediate
|                 |     |      |               |         |          |     | workflows,  | and  | subsystems  | presented  |     | in  | this  document   |     |
| --------------- | --- | ---- | ------------- | ------- | -------- | --- | ----------- | ---- | ----------- | ---------- | --- | --- | ---------------- | --- |
| noncompliance,  |     | and  | successfully  | manage  | systems  |     | in          |      |             |            |     |     |                  |     |
can be used by organizations seeking to establish federated
| accordance  | with    | the     | Risk  Management  |                        | Framework  |     |             |                    |               |     |                  |     |               |       |
| ----------- | ------- | ------- | ----------------- | ---------------------- | ---------- | --- | ----------- | ------------------ | ------------- | --- | ---------------- | --- | ------------- | ----- |
|             |         |         |                   |                        |            |     | queries,    | an  orchestration  |               | of  | data-collection  |     | tasks,        | data  |
| described   | in  SP  | 800-37  | Revision          | 1, Guide for Applying  |            |     |             |                    |               |     |                  |     |               |       |
|             |         |         |                   |                        |            |     | analytics,  | and                | presentation  |     | and  reporting   |     | capabilities  |       |
the Risk Management Framework to Federal Information
|     |     |     |     |     |     |     | across  | a  diverse  | portfolio  | of  | security  | and  | IT  products.  |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ---------- | --- | --------- | ---- | -------------- | --- |
Systems: A Security Life Cycle Approach. Standards that are
CAESARS-FE supports IT operations and network-defense
developed and published by these SDOs will be considered
capabilities, with compliance reporting as a byproduct of
for inclusion in future revisions of SCAP.
actual security monitoring and improvement. CAESARS-
http://scap.nist.gov/ FE enables organizations to design, develop, and deploy
ConMon capabilities by leveraging their existing security and
IT tools, while minimizing custom tool-integration efforts.
CONTACT:
|     |     |     |     |     |     |     | CAESARS-FE  |     | defines  | the  requisite  |     | functionality  |     | needed  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --------------- | --- | -------------- | --- | ------- |
Mr. David Waltermire
to ensure the interoperability of vendor products, while
(301) 975-3390  continuing to encourage security-tool-vendor participation
david.waltermire@nist.gov
and innovation.
6 4
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

To advance the state-of-the-art in continuous- to determine historic vulnerable conditions in support of
monitoring capabilities and to further interoperability within incident-response and recovery processes. Finally, using
commercially available tools, CSD is working with the IETF the collected software inventory, network access can
SACM working group to develop data-model and transport be controlled, enabling the device to be connected to a
standards to support enterprise continuous monitoring. The remediation network, if necessary, so that the appropriate
CAESARS-FE reference architecture will evolve as consensus software changes can be made before allowing the device
is developed within SACM around interoperable, standards- full access to the operational network.
based approaches that enable continuous monitoring of IT
The building-block document, Continuous Monitoring
systems. CSD is working to complete an update to NISTIR
Building Block: Software Asset Management, can be viewed
7756 that provides additional guidance for the development
at http://nccoe.nist.gov/content/continuous-monitoring. In
of ConMon architectures and solutions based on ongoing
early FY 2015, the team will publish an update to the
standards activities and feedback.
building-block document and will begin work with vendors
The NIST National Cybersecurity Center of Excellence to develop a solutions demonstration. Through this process,
(NCCoE) is also working to develop a series of ConMon CSD provides publicly available descriptions of the practical
building blocks that demonstrate cybersecurity solutions steps needed to implement the technical approaches
that apply across multiple industry sectors. The first building defined by the building block.
block, currently under development, proposes a standardized
approach to software-asset management, providing an CONTACT:
organization with an integrated view of software throughout
its lifecycle. The building block will support: Mr. David Waltermire
(301) 975-3390
• Authorization and verification of software installation
david.waltermire@nist.gov
media—The ability to verify that software media is from
a trusted publisher and that the integrity of the installa-
tion media has been maintained; Security Automation Reference Data
Through the National Vulnerability Database (NVD) and
• Software-execution whitelisting—The execution envi-
the National Checklist Program (NCP), NIST is providing
ronment verifies that the software to be executed, is
relevant and important reference data in the areas of
authorized for execution, and that the executable file(s)
vulnerability and configuration management. SCAP, and
and any associated shared libraries have not been
the programs that leverage it, are moving the information
tampered with;
assurance industry towards being able to standardize
• Publication of an installed software inventory—When
communications and the collection and storage of relevant
connected to an authorized network, a device’s full
data in standardized formats, and to provide an automated
or updated software inventory is securely reported to
means for the assessment and remediation of systems for
an external configuration-management database that
both vulnerabilities and configuration compliance.
aggregates the software inventory of multiple devices
for further analysis; and National Vulnerability Database (NVD)
• Software inventory-based network access control— Security automation reference data is currently
Control access to network resources at the time of housed within the NVD. The NVD is the U.S. Government
a connect operation, based on the published, in- repository of security automation data based on security
stalled-software inventory. Access to network resourc- automation specifications. This data provides a standards-
es can be limited if software is outdated or patches are based foundation for the automation of software asset,
not installed in accordance with digital policies. vulnerability, and security configuration management;
security measurement; and compliance activities. This data
When used together, these capabilities enable the
supports security automation efforts based on the SCAP. The
enterprise-wide management of the software that is allowed
NVD includes databases of security configuration checklists
to be installed and executed. The collected information
for the NCP, listings of publicly known software flaws,
will also provide software-version information to support
product names, and impact metrics. A formal validation
license, vulnerability and patch management needs. If
program tests the ability of vendor products to use some
historic software-inventory information is maintained,
forms of security automation data, based on a product’s
retroactive analysis techniques can be applied on this data
conformance in support of specific enterprise capabilities.
6 5
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

SCAP defines the structure of standardized software and layout of the NVD to assist new users in locating
flaws and security configuration reference data, also known content, the addition of visualization options of the NVD
as SCAP content. This reference data is provided by the NVD data for security researchers, and an implementation of the
(http://nvd.nist.gov/). forthcoming release of the Common Vulnerability Scoring
System (CVSS) version 3 specifications from FIRST.
As of October 2014, the NVD contained the following
resources: http://nvd.nist.gov
• O ver 65 000 vulnerability advisories, with an average
of 40 new vulnerabilities added daily; CONTACT:
• 56 SCAP-expressed checklists containing thousands
Mr. Harold Booth
of low-level security configuration checks that can be
(301) 975-8441
used by SCAP-validated security products to perform
harold.booth@nist.gov
automated evaluations of the system state;
• 197 non-SCAP security checklists (e.g., English prose
Computer Security Incident
guidance and configuration scripts);
Coordination
• 248 U.S. Computer Emergency Readiness Team (US- Recognizing that even well-engineered and administered
CERT) alerts; 3690 US-CERT vulnerability summaries; computing systems are sometimes successfully attacked,
and 10 286 SCAP machine-readable software flaw it is important to establish and maintain processes and
checks; procedures for responding to and recovering from attacks.
• A product dictionary with over 97 000 operating sys- SP 800-61 Revision 2, Computer Security Incident Handling
tem, application, and hardware name entries; and Guide, provides guidance that helps organizations establish
and operate a Computer Security Incident Response
• 5 0 038 vulnerability advisories translated into Spanish.
Team (CSIRT). When an attack has the potential to affect
NVD is hosted and maintained by NIST and is sponsored computing systems in multiple organizations, information
by the Department of Homeland Security’s US-CERT. sharing and coordination among organizations can make it
The use of SCAP data by commercial security products, possible to reduce the impact of the attack, speed recovery
deployed in thousands of organizations worldwide, has operations, and maintain a higher level of operational
extended NVD’s effective reach. Increasing demand for NVD security.
XML data feeds (i.e., mechanisms that provide updated data CSD is working with the Department of Homeland
from data sources) and SCAP-expressed content from the Security (DHS) to develop guidance on Computer Security
NVD website demonstrates an increased adoption of SCAP. Incident Coordination (CSIC). The goal of CSIC is to help
The NVD continues to play a pivotal role in the Payment diverse collections of organizations to effectively collaborate
Card Industry (PCI) efforts to mitigate vulnerabilities in credit in the handling of computer security incidents. Effective
card systems. PCI mandates the use of NVD vulnerability collaboration raises numerous issues on how and when to
severity scores in measuring the risk to payment card share information between organizations, and in what form
servers worldwide and for prioritizing vulnerability patching. information should be shared. Because each organization
PCI’s use of NVD severity scores helps enhance credit card may have substantially different capabilities for responding
transaction security and protects consumers’ personal to attacks, diagnosing causes, and handling sensitive
information. incident-related information, guidance is needed to help
organizations interoperate despite these organizational
During FY 2014, the NVD infrastructure has been
differences.
significantly changed to improve responsiveness and
availability and to position the NVD for future improvements, The CSIC initiative is focused on the development
which will be coming soon. NVD now hosts the SP 800-53 of a Special Publication (SP) that provides guidance on
Revision 4 security controls content and will host the SP how organizations can establish information sharing and
800-53A Revision 4 content when that publication becomes coordination capabilities in advance of incidents in order
final. NVD data is substantially increasing the security of to be prepared to operate swiftly and with coordination
networks worldwide, and it is a fundamental component of during incidents. The guidance covers information sharing
CSD’s security automation infrastructure. CSD plans for the architectures; risk-informed incident response capabilities;
NVD in FY 2015 include improvements in the organization data privacy and sensitivity; data collection and retention
6 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

practices; and the use of open standards for information  responsibilities  under  the  Federal  Information  Security
exchange, redaction, and guidance on how an organization  Management Act (FISMA) of 2002, Public Law 107-347, and
can establish, participate in, and maintain coordination and  also under the Cybersecurity Research and Development
information-sharing relationships. Act, which tasks NIST to “develop, and revise as necessary,
a checklist setting forth settings and option selections that
| The  | CSIC  | guidance  | will  | help  | incident  | responders,  |     |     |     |     |     |     |     |
| ---- | ----- | --------- | ----- | ----- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
minimize the security risks associated with each computer
| network  | defenders,  |     | and  operations  |     | personnel  | consider  |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ---------------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
hardware or software system that is, or is likely to become,
what information could be shared, the circumstances under
widely used within the Federal Government.” In February
which sharing is permitted, whom it can be shared with,
2008, revised Part 39 of the Federal Acquisition Regulation
and how the information should be protected. One of the
(FAR) was published. Paragraph (d) of section 39.101 states,
key objectives of information sharing and coordination is to
“In acquiring information technology, agencies shall include
enable organizations to harness the collective knowledge
|                  |     |     |        |          |           |              |     | the  appropriate  | IT  security  | policies  | and  | requirements,  |     |
| ---------------- | --- | --- | ------ | -------- | --------- | ------------ | --- | ----------------- | ------------- | --------- | ---- | -------------- | --- |
| and  experience  |     | of  | their  | sharing  | partners  | to  enhance  |     |                   |               |           |      |                |     |
including use of common security configurations available
| protective  | measures,  |     | speed  | incident  | detection,  | augment  |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------ | --------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
from the NIST website at http://checklists.nist.gov. Agency
analysis capabilities, and enhance containment, eradication,
contracting officers should consult with the requiring official
and recovery processes.
to ensure the appropriate standards are incorporated.”
| In  early  | FY  | 2015,  | CSD  | plans  | to  release  | a  Draft  | SP  |     |     |     |     |     |     |
| ---------- | --- | ------ | ---- | ------ | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
In Memorandum M-08-22, the Office of Management
| that  provides  |     | guidance  | for  | Computer  | Security  | Incident  |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ---- | --------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
and Budget (OMB) mandated the use of SCAP-validated
| Coordination.  |     | After  | the  public  | comment  |     | period  | for  the  |     |     |     |     |     |     |
| -------------- | --- | ------ | ------------ | -------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
draft, a final version of the publication will be prepared and  products  for  continuous  monitoring  of  Federal  Desktop
Core Configuration (FDCC) compliance. The NCP strives to
released later in the fiscal year.
encourage and assist federal agencies with these mandates.
The goals of the NCP are to:
CONTACTS:
|                 |     |     |                       |     |     |     |     | •   Facilitate the development and sharing of checklists by  |     |     |     |     |     |
| --------------- | --- | --- | --------------------- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- |
| Mr. Lee Badger  |     |     | Mr. David Waltermire  |     |     |     |     |                                                              |     |     |     |     |     |
providing a formal framework for checklist developers
| (301) 975-3176  |     |     | (301) 975-3390  |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to submit checklists to NIST;
| lee.badger@nist.gov  |     |     | david.waltermire@nist.gov |     |     |     |     |                                                         |     |     |     |     |     |
| -------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
|                      |     |     |                           |     |     |     |     | •   Provide guidance to developers to help them create  |     |     |     |     |     |
standardized, high-quality checklists that conform to
Mr. Christopher Johnson
| (301) 975-3247  |     |     |     |     |     |     |     | common operation environments; |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
christopher.johnson@nist.gov •   Help developers and users by providing guidelines for
making checklists better documented and more usable;
National Checklist Program (NCP) •   Encourage software vendors and other parties to de-
| There are many threats to information technology (IT),  |     |     |     |     |     |     |     | velop checklists; |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
ranging from remotely launched network service exploits to  •   Provide a managed process for the review, update, and
malicious code spread through infected emails, websites,
maintenance of checklists;
| and  downloaded  |         | files.  | Vulnerabilities  |               | in  | IT  products  | are  |                                                          |     |     |     |     |     |
| ---------------- | ------- | ------- | ---------------- | ------------- | --- | ------------- | ---- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
|                  |         |         |                  |               |     |               |      | •   Provide an easy-to-use repository of checklists; and |     |     |     |     |     |
| discovered       | daily,  | and     | many             | ready-to-use  |     | exploitation  |      |                                                          |     |     |     |     |     |
techniques are widely available on the Internet. Because IT  •   Encourage the use of automation technologies (e.g.,
products are often intended for a wide variety of audiences,  SCAP) for checklist application.
restrictive security configuration controls are usually not
|     |     |     |     |     |     |     |     | There  are  | 253  checklists  | posted  |     | on  the  | website   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------- | ------- | --- | -------- | --------- |
enabled by default. As a result, many out-of-the box IT
(http://checklists.nist.gov); 120 of the checklists, addressing
products are immediately vulnerable. In addition, identifying
48 platforms, are SCAP-expressed and can be used with
a reasonable set of security settings that achieve balanced
|     |     |     |     |     |     |     |     | SCAP-validated  | products.  | The  majority  |     | of  the  | SCAP- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | -------------- | --- | -------- | ----- |
risk  management  is  a  complicated,  arduous,  and  time- expressed checklists have been posted in the past three
consuming task, even for experienced system administrators.
years, demonstrating continual use and adoption of this
To facilitate the development of security configuration  automated means of expressing checklist content.
| checklists  | for  | IT  products  |     | and  to  | make  | checklists  | more  |                |           |             |           |       |      |
| ----------- | ---- | ------------- | --- | -------- | ----- | ----------- | ----- | -------------- | --------- | ----------- | --------- | ----- | ---- |
|             |      |               |     |          |       |             |       | Organizations  | can  use  | checklists  | obtained  | from  | the  |
organized and usable, NIST’s CSD established the National
NCP website for automated security configuration patch
Checklist  Program  (NCP)  in  furtherance  of  its  statutory  assessment. The NCP currently hosts SCAP checklists for
67
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2014

Internet Explorer 9.0, Internet Explorer 10.0, Office 2010,
CONTACT:
Red Hat Enterprise Linux, Windows 7, Windows 8, Windows
CCC
Server 2012, and other products. Mr. Stephen Quinn
(301) 975-6967
To assist users in identifying automated checklist
stephen.quinn@nist.gov
content, NCP groups these checklists into tiers, from Tier I to
Tier IV. The NCP uses the tiers to rank checklists according
to their automation capability. Tier III and IV checklists
United States Government
include SCAP content and have been validated by the SCAP
Configuration Baseline (USGCB) /
content validation tool as conforming to the requirements
FDCC Baselines
outlined in SP 800-126, The Technical Specification for
The United States Government Configuration Baseline
the Security Content Automation Protocol (SCAP). Tier IV
(USGCB) initiative creates security configuration baselines
checklists are considered production-ready and have been
for information technology (IT) products widely deployed
validated by NIST or a NIST recognized authoritative entity
to ensure interoperability with SCAP-validated products to across the federal agencies. The project evolved from the
the maximum extent possible. Federal Desktop Core Configuration (FDCC) mandate
originally described in a March 2007 memorandum
Tier III checklists use SCAP content to document security
from the U.S. White House Office of Management and
settings and should be compatible with SCAP-validated
Budget (Memorandum M-07-11). USGCB helps to improve
products. Tier II checklists document recommended security
information security and reduce overall IT operating costs
settings in a machine-readable, nonstandard format, such
by providing commonly accepted security configurations for
as a proprietary format or a product-specific configuration
major operating systems.
script. Tier I checklists are prose-based and contain no
machine-readable content. Users can browse the checklists, Through the National Checklist Program described in
based on the checklist tier, IT product, IT product category, SP 800-70 Revision 2, National Checklist Program for IT
or authority, and through a keyword search that searches the Products: Guidelines for Checklist Users and Developers,
checklist name and summary for user specified terms. The a baseline submitter may express interest in submitting a
search results show the detailed checklist metadata and a
candidate for use in the USGCB program.
link to any SCAP content for the checklist, as well as links to
CSD provides ongoing support for the USGCB
any supporting resources associated with the checklist.
automation content, including periodic updates, assisting
To assist checklist developers, the NCP provides both
USGCB users in continuously monitoring and assessing
manual and automated interfaces to facilitate submission
security compliance of information systems. This ongoing
and maintenance processes. The manual interface consists
monitoring element supports the Risk Management
of a web application that guides the submitter through
Framework described in SP 800-37 Revision 1, Guide for
the data entry process to ensure that all of the required
Applying the Risk Management Framework to Federal
information is submitted. The submission is validated
Information Systems: A Security Life Cycle Approach. It also
upon review, and a report is returned to the submitting
supports the Core functions of the Cybersecurity Framework,
organization, verifying either acceptance or rejection, based
providing USGCB users with settings that protect digital
on the criteria requirements. For instance, Tier III and Tier
assets and enable detection of suspicious activity.
IV checklists require validation using the SCAP Content
Validation Tool (this tool is available for download via During FY 2015, the USGCB Program will continue to
http://scap.nist.gov/revision/1.2/#tools). provide ongoing maintenance of the baseline artifacts and
The NCP is defined in SP 800-70 Revision 2, National to consider additional applicable platforms.
Checklist Program for IT Products—Guidelines for The USGCB’s team email address is: usgcb@nist.gov.
Checklist Users and Developers, which can be found at
http://csrc.nist.gov/publications/PubsSPs.html.
CONTACT:
http://checklists.nist.gov
Mr. Stephen Quinn
(301) 975-6967
stephen.quinn@nist.gov
6 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Apple OS X Security Configuration During FY 2014, a majority of all proposed settings were
CSD is working with Apple Incorporated to develop scripted. The corresponding spreadsheet batches have been
secure system configuration baselines supporting different sent to Apple for feedback; approximately 230 settings are
operational environments for Apple OS X Version 10.8, now completed. Settings have also been implemented on OS
“Mountain Lion.” These configuration guidelines will assist X 10.9, when possible. Work on the draft guideline, Guide to
organizations with hardening OS X technologies and Securing Apple OS X 10.8 Systems for IT Professionals, was
provide a basis for unified controls and settings for OS X temporarily suspended while configuration setting research
workstations and for mobile system security configurations was performed, but will be resumed in FY 2015.
for federal agencies. In FY 2015, CSD plans to finish scripting the few
The configurations will be based on a collection of remaining OS X settings. The draft publication, Guide to
resources, including the existing NIST OS X configuration Securing Apple OS X 10.8 Systems for IT Professionals will
guidance, the OS X security configuration guide, the also be completed and made available for public comment.
Department of Defense (DOD) OS X Recommended Settings, One of the script’s three profiles will be deployed on select
and the Defense Information Systems Agency (DISA) OS X CSD systems to test the extended use of a system with a
Security Technical Implementation Guide (STIG). The project specific profile applied. CSD plans to continue improving the
team is aggregating 400 initial settings, determining which script after all settings are implemented.
settings will be included in the configuration baseline, and
determining appropriate values for each included setting. CONTACTS:
As the desired configuration items are established, the team
is developing shell scripts that apply the settings to an OS Mr. Mark Trapnell Mr. Lee Badger
X 10.8 system. The settings are organized into three key (301) 975-4091 (301) 975-3176
baselines, which are appropriate for different environments: mark.trapnell@nist.gov lee.badger@nist.gov
• The Enterprise baseline is appropriate for centrally
Mr. Lawrence Keys Ms. Kathy Ton-Nu
managed, networked systems.
(301) 975-5482 (301) 975-3361
• The Small Office Home Office baseline is appropriate lawrence.keys@nist.gov kathy.ton-nu@nist.gov
for systems that are deployed remotely, but need to
connect to enterprise networks.
• The Special Security Limited Functionality baseline is TECHNICAL SECURITY
appropriate for systems where security requirements
METRICS
are more stringent and where the implementation of
security safeguards is likely to reduce functionality.
Security Risk Analysis of Enterprise
SCAP, defined and discussed in other sections of this
Networks Using Attack Graphs
report, is used to express configuration settings and check
The protection of computer networks from malicious
system configuration compliance.
intrusions is critical to the economy and security of the
During FY 2013, CSD provided a block of initial settings
nation. Vulnerabilities are regularly discovered in software
to Apple and these settings were posted for the Apple
applications that are exploited to stage cyber attacks.
community on a periodic basis for public review, discussion,
System administrators need objective metrics to guide
correction and agreement. Each setting has a designated
and justify decision making as they manage the security
Common Configuration Enumeration (CCE) number, which
risk of enterprise networks. The objective of this research
aids in long-term tracking of the setting. Once these settings
is to develop a standard model for security risk analysis of
are vetted by Apple, the settings will then be tested and
computer networks. A standard model will enable NIST to
included in the configuration baselines. In addition, CSD is
answer questions such as “Are we more secure now than
producing a draft guideline, Guide to Securing Apple OS X
yesterday?” or “How does the security of one network
10.8 Systems for IT Professionals. This guidance, similar in
configuration compare with another one?” Also, having a
structure to the SP 800-68, Windows XP Security Guide, will
standard model to measure network security will allow users,
provide detailed information about the security of Apple OS
vendors, and researchers to evaluate methodologies and
X 10.8, and will provide security configuration guidelines for
products for network security in a coherent and consistent
all users of the Apple OS X 10.8 operating system.
manner.
6 9
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

CSD has approached the challenge of network security the University of Maryland. ARL’s participation helps focus
analysis by capturing vulnerability interdependencies the work on solving immediately critical problems facing
and measuring security, based on how real attackers have U.S. Government networks. However, research solutions are
penetrated networks. CSD’s methodology for security risk made publicly available and are designed to be generally
analysis is based on attack graphs. CSD analyzes attack applicable to as many environments as possible.
paths through a network, providing a probabilistic metric of
In FY 2014, the AIM project completed research
the overall system risk. Through this metric, CSD analyzes
pertaining to several stages of the detection lifecycle through
trade-offs between security costs and security benefits.
the application of graph theoretic approaches: security
Computer systems are vulnerable to both known log compression, alert aggregation, and network threat
and zero-day attacks. Handling zero-day vulnerabilities propagation. The project team accomplished the following:
is inherently difficult, due to their unpredictable nature.
• The research team enabled significantly tighter com-
In FY 2014, CSD attempted to model network diversity
pression for security logs, compared to using standard
for evaluating the resilience of networks against zero-
compression algorithms alone, and accomplished it
day attacks. CSD developed a formal model for network
using less processing time. The invention was a light-
diversity as a security metric for evaluating the robustness of
weight packing process that takes advantage of the
networks against potential zero-day attacks. CSD has
restricted semantics and regular format of certain kinds
proposed a new metric based on the least and average
of log files to render them substantially more amenable
attacking effort. CSD has authored a paper, “Modeling
to compression with standard algorithms (research
Network Diversity for Evaluating the Robustness of Networks
published by the Military Communications Conference,
against Zero- Day Attacks,” that was presented at the 19th
2014). The team achieved a reduction of compressed
European Symposium on Research in Computer Security
file sizes to as little as 21 % of that of maximally com-
(ESORICS), Wroclaw, Poland, September 7-11, 2014.
pressed files without packing, and reduced overall
In FY 2015, CSD plans to develop new techniques and compression times up to 64 %.
metrics to detect stealthy attacks on Cloud Computing using
• To aid in the human analysis of such intrusion and se-
Bayesian Networks. CSD also plans to publish the results as a
curity logs, the team designed an efficient approach to
NIST report and as white papers in conferences and journals.
visually compress groups of related logs (as opposed
http://csrc.nist.gov/groups/SNS/security-risk-analysis- to the previous work that reduced the actual size on a
enterprise-networks/ disk). The team designed a user-adjustable log aggre-
gation approach using varying Hamming distances to
CONTACT: quickly and losslessly aggregate alerts (research pub-
lished by the International Journal of Network Security
Dr. Anoop Singhal and its Applications). The result is a reduction in the
(301) 975-4432 cognitive load on analysts by minimizing the overall
anoop.singhal@nist.gov number of alerts and the number of data elements that
need to be reviewed in order for an analyst to evaluate
the set of original alerts.
Algorithms for Intrusion Measurement
The Algorithms for Intrusion Measurement (AIM) project • The research team addressed the problem of deter-
furthers measurement science in the area of the algorithms mining how far an attack may have spread in a net-
used in the field of intrusion detection. The team focuses on work when a perimeter incursion has been detected.
both new detection metrics and measurements of scalability To accomplish this, the team created metrics and an
(more formally called algorithmic complexity). This analysis algorithm for bounding the scope of network ingress
is applied to different phases of the detection lifecycle attacks using the network tainting invention (research
to include preemptive vulnerability analysis, initial attack published by IEEE Conference on Software Security
detection, alert impact, alert aggregation/correlation, and and Reliability, 2014). This approach provides an effi-
compact log storage. In performing this work, the AIM project cient means by which to stage and prioritize network
seeks to enhance the nation’s ability to defend itself from forensics examinations.
network-borne attacks. This scientific research is conducted
In FY 2015, the AIM project will work on measuring
in partnership with the Army Research Laboratory (ARL) and
Internet resilience to attacks by colluding countries, the
70
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

detection of persistent and stealthy network scanning, and Technology transfer activities included the publication
efficient representations and algorithms for modeling and of several technical papers; a presentation of the results
defending attack paths within a network. of the work with Lockheed Martin; a release of enhanced
covering array, test prioritization, and fault location tools; plus
CONTACT: seminars and lectures at several conferences, universities,
and federal agencies.
Mr. Peter Mell
Plans for FY 2015 include a follow-up project with
(301) 975-5572
the NASA IV&V Facility to investigate the integration of
peter.mell@nist.gov
combinatorial coverage measurement methods in NASA
Independent Verification and Validation (IV&V) practices;
Automated Combinatorial Testing the release of test a development environment as an open
Software developers often encounter failures that result source project (jointly with Carnegie Mellon University);
from an unexpected interaction between components. NIST lectures at conferences and research labs; and a joint
research has shown that most failures are triggered by one development of enhanced fault location tools with Johns
or two parameters, and progressively fewer by three, four, or Hopkins University Applied Physics Lab.
more parameters (see the graph below), a relationship that
http://csrc.nist.gov/groups/SNS/acts/
is called the Interaction Rule. These results have important
implications for testing. If all faults in a system can be
CONTACTS:
triggered by a combination of n or fewer parameters, then
testing all n-way combinations of parameters can provide Mr. Rick Kuhn Dr. Raghu Kacker
very strong fault detection efficiency. These methods are (301) 975-3337 (301) 975-2109
being applied to software and hardware testing for reliability, kuhn@nist.gov raghu.kacker@nist.gov
safety, and security. CSD’s focus is on empirical results and
real-world problems.
Roots of Trust
Project highlights for FY 2014 included the publication
Modern computing devices consist of various hardware,
of a report on a two-year Cooperative Research and
firmware, and software components at multiple layers of
Development Agreement (CRADA) with Lockheed Martin
abstraction. Many security and protection mechanisms are
Corporation, showing approximately a 20 % reduction in
currently rooted in software that, along with all underlying
software test development cost across a variety of projects,
components, must be trusted and not tampered with. A
with a 20 % to 50 % improvement in test coverage; the
vulnerability in any of those components could compromise
development of a parallel algorithm for fault location,
the trustworthiness of the security mechanisms that rely
demonstrated on 22 000 variables; nine invited lectures
upon those components. Stronger security assurances may
at conferences and research labs; leading (jointly with IBM
be possible by grounding security mechanisms in roots of
personnel) the IEEE Third International Conference on
trust.
Combinatorial Testing, held with the International Conference
Roots of trust are highly reliable and secure hardware,
on Software Testing; and a joint project with Carnegie Mellon
firmware, and software components that perform specific,
University developing an advanced test environment that
critical security functions. Because roots of trust are
incorporates combinatorial methods.
inherently trusted, they must be secure by their design. As
such, many roots of trust are implemented in hardware or
protected firmware so that malware cannot tamper with
the functions they provide. Roots of trust provide a firm
foundation from which to build security and trust.
NIST CSD’s work aims to encourage the use of roots of
trust in computers to provide stronger security assurances.
A focus area for this work has been securing mobile devices,
using roots of trust to provide device integrity, data and
application isolation, and protected storage. As part of this
work, CSD is revising SP 800-164, Guidelines on Hardware-
Rooted Security in Mobile Devices, based on the public
comments that were received on the draft. A revised draft
will be released in FY 2015. 7 1
Figure 22: Interaction Rule
PROGRAM AND PROJECT ACHIEVEMENTS | FY 2014

Meanwhile, the draft guideline is being used as the
basis for an effort with the National Cybersecurity Center of
Excellence (NCCoE) to encourage the adoption of stronger
security technologies in mobile devices. Using draft SP
800-164 as a foundational document, the NCCoE and
CSD developed the Mobile Device Security for Enterprises
building block, which will demonstrate commercially
available technologies that provide protection to both
organization-issued and personally owned mobile platforms.
The NCCoE will invite mobile device, operating system,
and management software vendors, as well as application
developers, to participate in this building block activity and
demonstrate how their technologies could be used together
to meet existing security requirements.
The CSD also continued its work to protect platform
firmware in FY 2014. Boot firmware, commonly known as
the Basic Input/Output System (BIOS), is a critical firmware
component, due to its unique and privileged position within
modern computing architectures. CSD has been working
with key members of the computer industry on the use of
roots of trust to improve the security of BIOS. In order to
encourage the continued adoption of BIOS protections,
The CSD submitted SP 800-147, BIOS Protection Guidelines,
to ISO for international standardization. CSD will continue
these standards efforts in FY 2015, and conduct research on
protections for other critical platform firmware.
CONTACT:
Mr. Andrew Regenscheid
(301) 975-5155
andrew.regenscheid@nist.gov
72
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

HONORS AND AWARDS
73

Department of Commerce
Gold Medal Award
Tom Karygiannis, Stephen Quirolgico, and Jeffrey Voas (CSD)
Additional recipients of this award were:
Brian Antonishek, Anthony Downs, Lisa Fronczek, Craig Schlenoff, and Brian Weiss
(all from the NIST Engineering Laboratory, Intelligent Systems Division)
From Left to Right: Secretary of Commerce Penny Pritzker, Brian Weiss, Craig Schlenoff,
Brian Antonishek, Anthony Downs, Lisa Fronczek, Stephen Quirolgico, Jeff Voas,
Tom Karygiannis, and Patrick Gallagher, NIST Director
The NIST team led a multi-organizational effort (NIST/George Mason University/DARPA) that developed
innovative methods for security, testing, and evaluation of hardware and software to securely deploy off-
the-shelf smartphones and applications in military field operations. NIST introduced software assurance
methods, power and reliability analysis techniques, and standards-based cryptographic solutions that
empowered the USG to securely deploy modified commercial solutions, reduce development costs,
enhance the combat capability of U.S. troops, and save U.S. soldiers’ lives.
74
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Department of Commerce
Gold Medal Award
Sheila Frankel (CSD)
Additional recipients of this award were:
Mark Carson, Douglas Montgomery, Stephen Nightingale, Darrin Santay,
(all from the Information Laboratory (ITL), Advanced Network Technologies Division)
From Left to Right: Secretary of Commerce Penny Pritzker, Darren Santay,
Stephen Nightingale, Mark Carson, Doug Montgomery, Sheila Frankel,
Patrick Gallagher, NIST Director
The group is recognized for technical leadership and innovation in the development and execution
of the USGv6 Program that enabled the U.S. Government to meet aggressive OMB milestones for the
adoption of IPv6 technologies. The team developed the critical standards, acquisition profiles, accredi-
tation and testing programs, test suites, procurement guides, security guides, and operational test and
measurement tools necessary to significantly improve the maturity of commercial IPv6 products and to
guide the USG in their acquisition, deployment, and secure use. The NIST USGv6 Program provided a
vital catalyst to the Internet industry and established the USG as a world leader in ensuring the contin-
ued growth and continuity of the Internet.
75
HONORS AND AWARDS | FY 2014

Department of Commerce
Bronze Medal Award
Richard Kissel, CSD
Mr. Kissel is recognized for raising small and medium-sized
business (SMB) awareness of information security threats,
vulnerabilities, and safeguards through implementation
of NIST’s SMB information security outreach program.
As the program lead, Mr. Kissel worked collaboratively
with the Small Business Administration and the FBI’s
InfraGard program to conduct information security training
workshops for small businesses with a focus on the tools
and techniques these businesses can apply directly. By
empowering SMBs, which represent over 95 percent of
all U.S. businesses, to better protect their information, the
nation’s overall information infrastructure is strengthened
to enhance innovation, competitiveness, and economic
security.
Stuart Katzke, Gallery of Distinguished Scientists,
Engineers and Administrators
Dr. Katzke was recognized for his outstanding contributions in the field of cybersecurity,
including his role as the founding director of NIST’s Computer Security Division. He was
honored as a nationally and internationally recognized leader in the development of
cybersecurity standards during his tenure at NIST ITL from 1975 through 1999, and again
during 2001 through 2008.
Naomi Lefkovitz, FierceGovernment
IT “Fierce 15” Awardee
Ms. Lefkovitz is the Senior Privacy Policy Adviser for the NIST ITL. She was recognized as an
innovator for her work in privacy and identity management, including her diligent support of
privacy considerations for the National Strategy for Trusted Identities in Cyberspace (NSTIC).
She represented the challenging and sensitive considerations to safeguard the privacy of
individuals, while supporting several important information security and risk management
initiatives, including the Framework for Improving Critical Infrastructure Cybersecurity. More
information about this award is available from:
http://www.fiercegovernmentit.com/special-reports/fiercegovernmentits-2013-fierce-15.
76
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Kevin Stine, FierceGovernment
IT “Fierce 15” Awardee
The Fierce 15 award is designed to recognize genuine groundbreaking innovation in IT. Mr.
Stine was recognized as an innovator in the Federal Government and, with Naomi Lefkovitz’s
award from previous page, demonstrated ITL’s commitment to creativity and innovation. The
award recognized those orchestrating “some of the most progressive projects underway in
government and work tirelessly to make government more efficient, service- and mission-
oriented, and accountable.” Mr. Stine was specifically awarded for his work in developing
the Framework for Improving Critical Infrastructure Cybersecurity. His leadership of a global
collaboration with public and private sector operators of critical infrastructure, and the
subsequent open public review and comment process, represent CSD’s synergistic approach.
More information about this award is available from:
http://www.fiercegovernmentit.com/special-reports/fiercegovernmentits-2013-fierce-15.
Matthew Scholl, Federal 100 Award
Matthew Scholl was recognized for his strategic direction and leadership of several initiatives,
including the Framework for Improving Critical Infrastructure Cybersecurity, Digital Government
Strategy, and Federal cross-agency priority goals on cybersecurity. Federal Computer
Week recognized his work enabling “the secure configuration of all government Windows-
based desktop computers, [increasing] security of credit card transactions worldwide, and
[establishment of] industry tools to effectively implement and monitor secure configurations.”
The Federal 100 Awards are presented to leaders who have played pivotal roles that affect
how the Federal Government acquires, develops and manages IT. Mr. Scholl was recognized as
exemplifying that spirit through his successful leadership in CSD, including efforts to transform
continuous security monitoring by expanding the use of automated tools. More information
about this recognition is available from:
http://fcw.com/articles/2014/03/10/fed100_scholl-matthew.aspx.
Dylan Yaga, 2014 InterNational Committee for
Information Technology Standards (INCITS) Service
Award
Mr. Yaga received the 2014 InterNational Committee for Information Technology Standards
(INCITS) Service Award. This is an honorary award presented to participants who have provided
outstanding service to the INCITS organization through committee work or duties. INCITS
recognized his numerous contributions to the INCITS/M1 - Biometrics standards community,
his detailed review of requirements in the biometric data interchange format standards and
associated conformance testing methodology projects. His contributions to the first and second
generation of data format standards have improved and promoted the successful development
of national and international biometric standards. More information about this award is available
from: http://www.incits.org/news-events/annual-awards.
7 7
HONORS AND AWARDS | FY 2014

COMPUTER SECURITY
DIVISION PUBLICATIONS
7 8

Computer Security Division Top 10 Most-Downloaded CSD publications in NIST
Publications Technical Series (i.e., FIPS, SP 800s, NISTIRs, and ITL
Bulletins):
During FY 2014, CSD staff
authored a significant number of • SP 800-53 Revision 4, Security and Privacy Controls for
computer/information security- Federal Information Systems and Organizations;
related guidelines, recommen-
• F IPS 201-2, Personal Identity Verification (PIV) of Fed-
dations, and research through
eral Employees and Contractors;
the NIST technical series, journal
articles, conference papers, and • SP 800-30 Revision 1, Guide for Conducting Risk As-
other published documents. sessments;
In the NIST technical series, CSD solicited public • NISTIR 7298 Revision 2, Glossary of Key Information
comments on forty draft publications, including one FIPS, 28 Security Terms;
SPs and 11 NISTIRs. The FIPS had a 90-day comment period, • F IPS 186-4, Digital Signature Standard (DSS);
while the other publications averaged 45 days. In particular,
• SP 800-82 Revision 1, Guide to Industrial Control Sys-
Draft NISTIR 7977, NIST Cryptographic Standards and
tems (ICS) Security;
Guidelines Development Process (discussed in this annual
report in the Cryptographic Standards and Guidelines • S P 800-162, Guide to Attribute Based Access Control
Process Review section), sought feedback on the NIST (ABAC) Definition and Considerations;
mechanisms used to engage experts in industry, academia • S P 800-63-2, Electronic Authentication Guideline;
and government to develop cryptographic standards.
• S P 800-165, 2012 Computer Security Division Annual
Nine SPs and four NISTIRs were issued as final Report; and
publications, including new documents, revisions or updated
• SP 800-37 Revision 1, Guide for Applying the Risk Man-
revisions. CSD also continued to have its work published
agement Framework to Federal Information Systems: A
monthly in ITL Bulletins, which summarize the various
Security Life Cycle Approach.
publications and projects occurring across CSD. Those
interested in being notified of new and draft publications Top 3 FIPS:
may visit http://csrc.nist.gov and subscribe to email alerts.
• F IPS 201-2, Personal Identity Verification (PIV) of Fed-
Seeking to expand the availability of its publications in eral Employees and Contractors;
formats besides PDFs, CSD began converting some of its
• F IPS 186-4, Digital Signature Standard (DSS); and
newer and most-downloaded publications into the .EPUB
• F IPS 140-2, Security Requirements for Cryptographic
format, which is commonly used by e-book readers on
Modules.
mobile platforms. More than 28 e-books were posted during
FY 2014 on the Computer Security Resource Center (CSRC) Top 3 NISTIRs:
publications pages, http://csrc.nist.gov/publications/.
• NISTIR 7298 Revision 2, Glossary of Key Information
Publications are available for download from CSRC Security Terms;
(http://csrc.nist.gov/), and FIPS (http://csrc.nist.gov/
• N ISTIR 7622, Notional Supply Chain Risk Management
publications/PubsFIPS.html), SPs (http://csrc.nist.gov/
Practices for Federal Information Systems; and
publications/PubsSPs.html) and NISTIRs (http://csrc.nist.
• N ISTIR 7896, Third-Round Report of the SHA-3 Cryp-
gov/publications/PubsNISTIRs.html) issued since mid-2012
tographic Hash Algorithm Competition.
have been posted on a server maintained by the NIST Library
and assigned Digital Object Identifiers (DOIs). During FY Top 3 ITL Bulletins:
2014, Google Scholar began crawling the NIST Library server,
• D ecember 2013, The National Vulnerability Database
resulting in significantly greater exposure and availability
(NVD): Overview;
of CSD’s technical series publications. The following lists
• F ebruary 2014, Framework for Improving Critical Infra-
the CSD-authored FIPS, SPs and NISTIRs that were most-
structure Cybersecurity; and
downloaded during FY 2014:
• June 2014, ITL Forensic Science Program.
7 9
CSD PUBLICATIONS | FY 2014

Additionally, CSD shares its ongoing research efforts FY 2014 COMPUTER
through other publications, such as journal articles,
SECURITY DIVISION
conference papers, books and other whitepapers. Although
PUBLICATIONS
these publications can be found through NIST’s Publications
Portal (http://www.nist.gov/publication-portal.cfm), in
FY 2014 CSD began posting a bibliography of those The Computer Security Division uses multiple NIST
documents on CSRC (http://csrc.nist.gov/publications/ Technical Series to promulgate security standards, guidelines,
articles/), including links to preprints and the final recommendations, research, and additional background
publications. During FY 2014, more than 25 such documents material. Those series include FIPS, NIST SPs, NISTIRs and
were published, and are listed in the next section (FY 2014 Information Technology Laboratory (ITL) Bulletins. Links
Computer Security Division Publications) of this annual to these publications are available at http://csrc.nist.gov/
report. Notably, the Framework for Improving Critical publications.
Infrastructure Cybersecurity, Version 1.0, described earlier Additionally, each year CSD staff author numerous
in this annual report, was downloaded more than 34 000 additional publications, including journal articles, conference
times. papers, and other papers that are widely disseminated. They
CSD also dipped into its archives and posted a new page range from basic research to high-level summaries of CSD
on CSRC, http://csrc.nist.gov/publications/history/nissc/, activities.
with full-text copies of proceedings from its 23 computer
NIST Technical Series Publications −
security conferences, held from 1979-2000 under various
FIPS, SPs, NISTIRs, and ITL Bulletins
names: National Information Systems Security Conference
(NISSC; 1995-2000), National Computer Security Conference Below are lists of NIST Technical Series publications
(NCSC; 1985-1994), DOD/NBS Computer Security Conference that CSD released as draft documents or as final publications
(1984) and Seminar on the DOD Computer Security Initiative during FY 2014 (from October 1, 2013 to September 30, 2014).
(1979-1983). Following the lists are abstracts and contact information for
each publication.
In FY 2015, besides expanding its library of available
e-books, CSD intends to greatly improve the publication
search, browse capabilities on CSRC, and provide additional
details and cross references for each publication.
CONTACT:
Mr. Jim Foti
(301) 975-8018
jfoti@nist.gov
8 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

DRAFT PUBLICATIONS
FEDERAL INFORMATION PROCESSING STANDARDS (FIPS)
Publication Number Publication Title Draft Released Date
FIPS 202 SHA-3 Standard: Permutation-Based Hash and Extendable- May 2014
Output Functions
SPECIAL PUBLICATIONS (SPs)
Publication Number Publication Title Draft Released Date
SP 800-167 Guide to Application Whitelisting August 2014
SP 800-163 Technical Considerations for Vetting 3rd Party Mobile August 2014
Applications
SP 800-161 (Second Draft) Supply Chain Risk Management Practices for Federal June 2014
Information Systems and Organizations
SP 800-160 Systems Security Engineering: An Integrated Approach to May 2014
Building Trustworthy Resilient Systems
SP 800-157 Guidelines for Derived Personal Identity Verification (PIV) March 2014
Credentials
SP 800-152 A Profile for U.S. Federal Cryptographic Key Management January 2014
Systems
SP 800-90A Revision 1 Recommendation for Random Number Generation Using April 2014
(Second Draft) Deterministic Random Bit Generators
SP 800-85B-4 PIV Data Model Conformance Test Guidelines August 2014
SP 800-82 Revision 2 Guide to Industrial Control Systems (ICS) Security May 2014
SP 800-79-2 Guidelines for the Authorization of Personal Identity June 2014
Verification Card Issuers (PCI) and Derived PIV Credential
Issuers (DPCI)
SP 800-78-4 Cryptographic Algorithms and Key Sizes for Personal Identity May 2014
Verification
SP 800-73-4 Interfaces for Personal Identity Verification May 2014
SP 800-57 Part 3, Revision 1 Recommendation for Key Management: Application-Specific May 2014
Key Management Guidance
SP 800-56B Revision 1 Guidelines for Derived Personal Identity Verification (PIV) March 2014
Credentials
(Approved as Final:
September 2014)
SP 800-53A Revision 4 Assessing Security and Privacy Controls in Federal Information July 2014
Systems and Organizations: Building Effective Assessment
Plans
SP 800-53 Revision 4, International Information Security Standards: Security Control August 2014
Appendix H Mappings for ISO/IEC 27001 and 15408
SP 800-16 Revision 1 A Role-Based Model For Federal Information Technology/
(Second Draft) CyberSecurity Training October 2013
(Third Draft) March 2014
8 1
CSD PUBLICATIONS | FY 2014

NIST INTERAGENCY OR INTERNAL REPORTS (NISTIRs)
Publication Number Publication Title Draft Released Date
NISTIR 8023 Risk Management for Replication Devices (RDs) September 2014
NISTIR 8018 Public Safety Mobile Application Security Requirements July 2014
Workshop Summary
NISTIR 8014 Considerations for Identity Management in Public Safety July 2014
Mobile Networks
NISTIR 8006 NIST Cloud Forensic Science Challenges June 2014
NISTIR 7981 Mobile, PIV, and Authentication March 2014
NISTIR 7977 NIST Cryptographic Standards and Guidelines Development February 2014
Process
NISTIR 7966 Security of Automated Access Management Using Secure August 2014
Shell (SSH)
NISTIR 7924 (Second Draft) Reference Certificate Policy May 2014
NISTIR 7863 Cardholder Authentication for the PIV Digital Signature Key December 2013
NISTIR 7628 Revision 1 Guidelines to Smart Grid CyberSecurity October 2013
(Approved as Final
September 2014)
FINAL APPROVED PUBLICATIONS
FEDERAL INFORMATION PROCESSING STANDARDS (FIPS)
NO FINAL APPROVED FIPS RELEASED DURING FY 2014.
SPECIAL PUBLICATIONS (SPs)
Publication Number Publication Title Publication Date
SP 800-170 Computer Security Division 2013 Annual Report June 2014
SP 800-168 Approximate Matching: Definition and Terminology May 2014
SP 800-162 Guide to Attribute Based Access Control (ABAC) Definition January 2014
and Considerations
SP 800-147B BIOS Protection Guidelines for Servers August 2014
SP 800-101 Revision 1 Guidelines on Mobile Device Forensics May 2014
SP 800-56B Revision 1 Guidelines for Derived Personal Identity Verification (PIV) September 2014
Credentials
SP 800-53 Revision 4 [Errata] Security and Privacy Controls for Federal Information Systems April 2013 (original
and Organizations release date);
updated January 15,
2014
8 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

SPECIAL PUBLICATIONS (SPs) (cont.)
Publication Number Publication Title Publication Date
SP 800-52 Revision 1 Guidelines for the Selection, Configuration, and Use of April 2014
Transport Layer Security (TLS) Implementations
SP 800-37 Revision 1 [Errata] Guide for Applying the Risk Management Framework to February 2010
Federal Information Systems: a Security Life Cycle Approach (original release
date); updated June
5, 2014
NIST INTERAGENCY OR INTERNAL REPORTS (NISTIRs)
Publication Number Publication Title Publication Date
NISTIR 7987 Policy Machine: Features, Architecture, and Specification May 2014
NISTIR 7946 CVSS Implementation Guidance April 2014
NISTIR 7849 A Methodology for Developing Authentication Assurance March 2014
Level Taxonomy for Smart Card-based Identity Verification
ITL BULLETINS
Publication Date Bulletin Title
September 2014 Release of NIST Interagency Report 7628 Revision 1, Guidelines for Smart Grid
Cybersecurity
August 2014 Policy Machine: Towards A General-Purpose, Enterprise-Wide Operating Environment
July 2014 Release of NIST Interagency Report 7946, CVSS Implementation Guidance
June 2014 ITL Forensic Science Program
May 2014 Small and Medium-Size Business Information Security Outreach Program
April 2014 Release of NIST SP 800-52 Revision 1, Guidelines for the Selection, Configuration, and
Use of Transport Layer Security (TLS) Implementations
March 2014 Attribute Based Access Control (ABAC) Definition and Considerations
February 2014 Framework for Improving Critical Infrastructure Cybersecurity
January 2014 A Profile of the Key Management Framework for the Federal Government
December 2013 The National Vulnerability Database (NVD): Overview
November 2013 ITL Releases Preliminary Cybersecurity Framework
October 2013 ITL Updates Federal Information Processing Standard (FIPS) for Personal Identity
Verification (PIV) of Federal Employees and Contractors
ABSTRACTS OF NIST TECHNICAL SERIES PUBLICATIONS RE-
LEASED IN FY 201
8 3
CSD PUBLICATIONS | FY 2014

| ABSTRACTS OF NIST  |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
NIST SPs
| TECHNICAL SERIES  |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- |
SP 800-170, Computer Security Division 2013 Annual
| PUBLICATIONS RELEASED  |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
Report
IN FY 2014
Title III of the E-Government Act of 2002, entitled the
Federal Information Security Management Act (FISMA) of
The following sections provide abstracts and contact
information for  the  draft and  final  FIPS, NIST  SPs,  and  2002, requires NIST to prepare an annual public report on
activities undertaken in the previous year, and planned for
security-related NISTIRs listed in the previous section. These
the coming year, to carry out responsibilities under this law.
publications are available at http://csrc.nist.gov/publications.
The primary goal of the Computer Security Division (CSD),
FIPS a component of NIST s Information Technology Laboratory
(ITL), is to provide standards and technology that protects
information systems against threats to the confidentiality,
DRAFT FIPS 202, SHA-3 Standard: Permutation-Based
|     |     |     |     | integrity,  | and  availability  | of  information  | and  services.  |
| --- | --- | --- | --- | ----------- | ------------------ | ---------------- | --------------- |
Hash and Extendable-Output Functions
During FY 2013, CSD successfully responded to numerous
  This standard specifies the Secure Hash Algorithm-3  challenges  and  opportunities  in  fulfilling  that  mission.
(SHA-3) family of functions on binary data. Each of the SHA-
Through CSD’s diverse research agenda and engagement
3 functions is based on an instance of the KeccaK algorithm  in  many  national  priority  initiatives,  high-quality,  cost-
that NIST selected as the winner of the SHA-3 Cryptographic
effective security and privacy mechanisms were developed
Hash Algorithm Competition. This Standard also specifies  and applied that improved information security across the
the  KeccaK-p  family  of  mathematical  permutations,  Federal Government and the greater information security
including the permutation that underlies KeccaK, in order to
|     |     |     |     | community.  | This  annual  | report  highlights  | the  research  |
| --- | --- | --- | --- | ----------- | ------------- | ------------------- | -------------- |
facilitate the development of additional permutation-based  agenda and activities in which CSD was engaged during FY
cryptographic functions.
2013.
The SHA-3 family consists of four cryptographic hash
functions,  called  SHA3-224,  SHA3-256,  SHA3-384,  and  CONTACTS:
| SHA3-512,  | and  two  extendable-output  |     | functions  (XOFs),  |                       |     |                    |     |
| ---------- | ---------------------------- | --- | ------------------- | --------------------- | --- | ------------------ | --- |
|            |                              |     |                     | Mr. Patrick O’Reilly  |     |   Mr. Kevin Stine  |     |
called SHAKE128 and SHAKE256.
|     |     |     |     | patrick.oreilly@nist.gov  |     |   kevin.stine@nist.gov |     |
| --- | --- | --- | --- | ------------------------- | --- | ---------------------- | --- |
Hash functions are components for many important
information security applications, including 1) the generation
SP 800-168, Approximate Matching: Definition and
and verification of digital signatures, 2) key derivation, and 3)
Terminology
pseudorandom bit generation. The hash functions specified
|     |     |     |     | Approximate  | matching  | is  a  promising  | technology  |
| --- | --- | --- | --- | ------------ | --------- | ----------------- | ----------- |
in this Standard supplement the SHA-1 hash function and
the SHA-2 family of hash functions that are specified in FIPS  for designed to identify similarities between two digital
artifacts. It is used to find objects that resemble each other
180-4, The Secure Hash Standard.
or to find objects that are contained in another object. This
Extendable-output functions are different from hash
can be very useful for filtering data for security monitoring,
functions, but it is possible to use them in similar ways, with
digital forensics, or other applications.
the flexibility to be adapted directly to the requirements
| of  individual  | applications,  | subject  | to  additional  security  |     |     |     |     |
| --------------- | -------------- | -------- | ------------------------- | --- | --- | --- | --- |
CONTACTS:
considerations.
|     |     |     |     | Mr. Douglas White  |     |     |     |
| --- | --- | --- | --- | ------------------ | --- | --- | --- |
CONTACTS:
Software and Systems Division, ITL
|                           |     |                        |     | douglas.white@nist.gov  |     |     |     |
| ------------------------- | --- | ---------------------- | --- | ----------------------- | --- | --- | --- |
| Dr. Morris Dworkin        |     |   Ms. Shu-jen Chang    |     |                         |     |     |     |
| morris.dworkin@nist.gov   |     | shu-jen.chang@nist.gov |     |                         |     |     |     |
Ms. Barbara Guttman
Software and Systems Division, ITL
barbara.guttman@nist.gov
8 4
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

DRAFT SP 800-167, Guide to Application Whitelisting SP 800-162, Guide to Attribute Based Access Control
(ABAC) Definition and Considerations
An application whitelist is a list of applications and
application components that are authorized to be used This document provides federal agencies with a definition
in an organization. Application whitelisting technologies of attribute based access control (ABAC). ABAC is a logical
use whitelists to control which applications are permitted access control methodology where authorization to perform
to execute on a host. This helps to stop the execution of a set of operations is determined by evaluating attributes
malware, unlicensed software, and other unauthorized associated with the subject, object, requested operations,
software. This publication is intended to assist organizations and, in some cases, environment conditions against policy,
in understanding the basics of application whitelisting. It rules, or relationships that describe the allowable operations
also explains planning and implementation for whitelisting for a given set of attributes. This document also provides
technologies throughout the security deployment lifecycle. considerations for using ABAC to improve information
sharing within organizations and between organizations
CONTACTS: while maintaining control of that information.
Mr. Adam Sedgewick
CONTACTS:
adam.sedgewick@nist.gov
Dr. Vincent Hu Mr. David Ferraiolo
Mr. Murugiah Souppaya vhu@nist.gov david.ferraiolo@nist.gov
murugiah.souppaya@nist.gov
Mr. Richard (Rick) Kuhn
DRAFT SP 800-163, Technical Considerations for Vetting kuhn@nist.gov
3rd Party Mobile Applications
DRAFT SP 800-161 (Second Draft), Supply Chain Risk
Today’s commercially available mobile devices (e.g.,
Management Practices for Federal Information Systems
smart phones, tablets) are handheld computing platforms
and Organizations
with wireless capabilities, geographic localization, cameras,
and microphones. Similar to computing platforms such as Federal agencies are concerned about the risks
desktops and laptops, the user experience with a mobile associated with information and communications technology
device is tied to the software apps and the tools and utilities (ICT) products and services that may contain potentially
available. The purpose of this document is to provide malicious functionality, are counterfeit, or are vulnerable due
guidance for vetting 3rd party software applications (apps) to poor manufacturing and development practices within
for mobile devices. Mobile app vetting is intended to assess the ICT supply chain. These risks are associated with the
a mobile app’s operational characteristics of secure behavior federal agencies decreased visibility into, understanding
and reliability (including performance) so that organizations of, and control over how the technology that they acquire
can determine if the app is acceptable for use in their is developed, integrated and deployed, as well as the
expected environment. processes, procedures, and practices used to assure the
integrity, security, resilience, and quality of the products and
CONTACTS: services.
This publication provides guidance to federal agencies
Dr. Jeff Voas Dr. Stephen Quirolgico
on identifying, assessing, and mitigating ICT supply chain
jeff.voas@nist.gov stephen.quirolgico@nist.gov
risks at all levels of their organizations. This publication
integrates ICT supply chain risk management (SCRM) into
federal agency risk management activities by applying a
multitiered, SCRM-specific approach, including guidance on
supply chain risk assessment and mitigation activities.
CONTACTS:
Mr. Jon Boyens Ms. Celia Paulsen
jon.boyens@nist.gov celica.paulsen@nist.gov
8 5
CSD PUBLICATIONS | FY 2014

DRAFT SP 800-160, Systems Security Engineering: An  DRAFT SP 800-152, A Profile for U. S. Federal
Integrated Approach to Building Trustworthy Resilient  Cryptographic Key Management Systems (CKMS)
Systems
|     |     |     |     |     | This  | Profile  | for  U.S.  | Federal  | Cryptographic  |     | Key  |
| --- | --- | --- | --- | --- | ----- | -------- | ---------- | -------- | -------------- | --- | ---- |
This  publication  addresses  the  actions  necessary  Management Systems (FCKMSs)  contains  requirements
for  developing  a  more  defensible  and  survivable  IT  for their design, implementation, procurement, installation,
infrastructure—including the component products, systems,  configuration,  management,  operation,  and  use  by  U.S.
and services that compose the infrastructure. It starts with  federal organizations. The Profile is based on SP 800-130, A
and builds upon well-established International Standards  Framework for Designing Cryptographic Key Management
for systems and software engineering published by the  Systems (CKMS).
| International  | Organization  | for  Standardization  |     | (ISO),  |     |     |     |     |     |     |     |
| -------------- | ------------- | --------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
International Electrotechnical Commission (IEC), and the  CONTACT:
Institute of Electrical and Electronic Engineers (IEEE), and
infuses systems security engineering techniques, methods,  Ms. Elaine Barker
elaine.barker@nist.gov
| and  practices  | into  those  | systems/software  | engineering  |     |     |     |     |     |     |     |     |
| --------------- | ------------ | ----------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
processes. The ultimate objective is to address cybersecurity
issues from a stakeholder requirements and protection needs  SP 800-147B, BIOS Protection Guidelines for Servers
perspective and to use already established organizational
|     |     |     |     |     | Modern  | computers  |     | rely  on  | fundamental  |     | system   |
| --- | --- | --- | --- | --- | ------- | ---------- | --- | --------- | ------------ | --- | -------- |
processes to ensure such requirements/needs are addressed
|     |     |     |     |     | firmware,  | commonly  | known  | as  | the  Basic  | Input/Output  |     |
| --- | --- | --- | --- | --- | ---------- | --------- | ------ | --- | ----------- | ------------- | --- |
early in the life cycle of the system. System  (BIOS),  to  facilitate  the  hardware  initialization
process and transition control to the hypervisor or operating
CONTACT:
system. Unauthorized modification of BIOS firmware by
malicious software constitutes a significant threat because
Dr. Ron Ross
of the BIOS’s unique and privileged position within the
rross@nist.gov
PC architecture. The guidelines in this document include
|     |     |     |     |     | requirements  | on  | servers  | to  mitigate  | the  | execution  | of  |
| --- | --- | --- | --- | --- | ------------- | --- | -------- | ------------- | ---- | ---------- | --- |
DRAFT SP 800-157, Guidelines for Derived Personal
|     |     |     |     |     | malicious  | or  corrupt  | BIOS  | code.  | They  | apply  | to  BIOS  |
| --- | --- | --- | --- | --- | ---------- | ------------ | ----- | ------ | ----- | ------ | --------- |
Identity Verification (PIV) Credentials
firmware stored in the BIOS flash, including the BIOS code,
This recommendation provides technical guidelines for  the cryptographic keys that are part of the Root of Trust
the  implementation  of  standards-based,  secure,  reliable,  for Update, and static BIOS data. This guide is intended to
interoperable PKI-based identity credentials that are issued  provide server platform vendors with recommendations and
by federal departments and agencies to individuals who  guidelines for a secure BIOS update process.
possess and prove control over a valid PIV Card. The scope
of this document includes requirements for initial issuance,  CONTACT:
maintenance and termination of these credentials, certificate
policies  and  cryptographic  specifications,  technical  Mr. Andy Regenscheid
andy.regenscheid@nist.gov
specifications for permitted cryptographic token types and
the command interfaces for the removable implementations
of such cryptographic tokens. SP 800-101 Revision 1, Guidelines on Mobile Device
Forensics
CONTACTS: Mobile device forensics is the science of recovering
digital evidence from a mobile device under forensically
| Ms. Hildegard (Hildy) Ferraiolo  |     | Mr. David Cooper  |     |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sound conditions using accepted methods. Mobile device
| hildegard.ferraiolo@nist.gov  |     | david.cooper@nist.gov |     |     |            |                   |     |            |          |        |              |
| ----------------------------- | --- | --------------------- | --- | --- | ---------- | ----------------- | --- | ---------- | -------- | ------ | ------------ |
|                               |     |                       |     |     | forensics  | is  an  evolving  |     | specialty  | in  the  | field  | of  digital  |
forensics. This guide attempts to bridge the gap by providing
| Mr. Salvatore Francomacaro  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
an in-depth look into mobile devices and explaining the
salvatore.francomacaro@nist.gov  technologies  involved  and  their  relationship  to  forensic
|     |     |     |     |     | procedures.  | This  | document  | covers  | mobile  | devices  | with  |
| --- | --- | --- | --- | --- | ------------ | ----- | --------- | ------- | ------- | -------- | ----- |
Mr. Andy Regenscheid
|     |     |     |     |     | features  | beyond  | simple  | voice  communication  |     |     | and  text  |
| --- | --- | --- | --- | --- | --------- | ------- | ------- | --------------------- | --- | --- | ---------- |
andrew.regednscheid@nist.gov
messaging capabilities. This guide also discusses procedures
for the validation, preservation, acquisition, examination,
analysis, and reporting of digital information.
8 6
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

CONTACT: CONTACTS:
Mr. Richard (Rick) Ayers Dr. Ramaswamy (Mouli) Chandramouli
Software and Systems Division, ITL mouli@nist.gov
richard.ayers@nist.gov
Ms. Hildegard (Hildy) Ferraiolo
DRAFT SP 800-90A Revision 1, Recommendation for hildegard.ferraiolo@nist.gov
Random Number Generation Using Deterministic Random
Bit Generators Mr. Ketan Mehta
ketan.mehta@nist.gov
This recommendation specifies mechanisms for the
generation of random bits using deterministic methods. The
methods provided are based on either hash functions, block DRAFT SP 800-82 Revision 2, Guide to Industrial Control
cipher algorithms or number theoretic problems. Systems (ICS) Security
This document provides guidance on how to secure
CONTACTS: Industrial Control Systems (ICS), including Supervisory
Control and Data Acquisition (SCADA) systems, Distributed
Ms. Elaine Barker Dr. John Kelsey Control Systems (DCS), and other control system
elaine.barker@nist.gov john.kelsey@nist.gov configurations such as Programmable Logic Controllers
(PLC), while addressing their unique performance, reliability,
DRAFT SP 800-85B-4, PIV Data Model Test Guidelines and safety requirements. The document provides an
overview of ICS and typical system topologies, identifies
FIPS 201, Personal Identity Verification (PIV) of Federal
typical threats and vulnerabilities to these systems, and
Employees and Contractors, describes a variety of data
provides recommended security countermeasures to
model components as a part of the PIV logical credentials.
mitigate the associated risks.
Such components include biometric elements in the
form of fingerprint information and facial imagery and
security elements such as electronic keys, certificates, and CONTACTS:
signatures. FIPS 201 incorporates by reference NIST SP
Mr. Keith Stouffer Ms. Suzanne Lightman
800-73-4 Interfaces for Personal Identity Verification, which
keith.stouffer@nist.go suzanne.lightman@nist.gov
specifies elements related to the PIV card interface, NIST
SP 800-76 Biometric Specifications for Personal Identity
Ms. Vicky Pillitteri
Verification, which specifies the biometric requirements, and
victoria.pillitteri@nist.gov
NIST SP 800-78 Cryptographic Algorithms and Key Sizes
for Personal Identity Verification, which specifies acceptable
cryptographic algorithms and key sizes for PIV systems. DRAFT SP 800-79-2, Guidelines for the Authorization
of Personal Identity Verification Card Issuers (PCI) and
A robust testing framework and guidelines to provide
Derived PIV Credential Issuers (DPCI)
assurance that a particular component or system is compliant
with FIPS 201 and supporting standards should exist to The purpose of this SP is to provide appropriate and
build the necessary PIV infrastructure to support common useful guidelines for assessing the reliability of issuers
unified processes and systems for government-wide use. of PIV Cards and Derived PIV Credentials. These issuers
NIST developed test guidelines in two parts. The first part store personal information and issue credentials based on
addresses test requirements for the interface to the PIV card, OMB policies and on the standards published in response
which are provided in NIST SP 800-85A PIV Card Application to HSPD-12 and therefore are the primary target of the
and Middleware Interface Test Guidelines (SP 800-73-3 assessment and authorization under this guideline. The
Compliance). The second part provides test requirements reliability of an issuer is of utmost importance when one
for the PIV data model and is provided in this document. This organization (e.g., a federal agency) is required to trust the
document specifies the derived test requirements, and the identity credentials of individuals that were created and
detailed test assertions and conformance tests for testing issued by another federal agency. This trust will only exist
the PIV data model. if organizations relying on the credentials issued by a given
organization have the necessary level of assurance that the
reliability of the issuing organization has been established
through a formal authorization process.
8 7
CSD PUBLICATIONS | FY 2014

| CONTACTS: |     |     |     |     | CONTACTS: |     |     |     |     |
| --------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
Dr. Ramaswamy (Mouli) Chandramouli    Dr. Ramaswamy (Mouli) Chandramouli
| mouli@nist.gov                   |     |     |     |     | mouli@nist.gov        |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
| Ms. Hildegard (Hildy) Ferraiolo  |     |     |     |     | Dr. David Cooper      |     |     |     |     |
| hildegard.ferraiolo@nist.gov     |     |     |     |     | david.cooper@nist.gov |     |     |     |     |
DRAFT SP 800-78-4, Cryptographic Algorithms and Key  Ms. Hildegard (Hildy) Ferraiolo
Sizes for Personal Identity Verification hildegard.ferraiolo@nist.gov
| FIPS  | 201  defines  | requirements  | for  | the  PIV  lifecycle  |     |     |     |     |     |
| ----- | ------------- | ------------- | ---- | -------------------- | --- | --- | --- | --- | --- |
Mr. Salvatore Francomacaro
activities including identity proofing, registration, PIV Card
issuance, and PIV Card usage. FIPS 201 also defines the  salvatore.francomacaro@nist.gov
structure of an identity credential that includes cryptographic
Mr. Ketan Mehta
keys. This document contains the technical specifications
needed for the mandatory and optional cryptographic keys  ketan.mehta@nist.gov
specified in FIPS 201 as well as the supporting infrastructure
specified in FIPS 201 and the related SP 800-73, Interfaces  DRAFT SP 800-57 Part 3, Revision 1, Recommendation
for Personal Identity Verification, and SP 800-76, Biometric  for Key Management: Application-Specific Key
Management Guidance
Data Specification for Personal Identity Verification, that rely
on cryptographic functions.
SP 800-57 provides cryptographic key management
guidance. It consists of three parts. Part 1 provides general
CONTACTS: guidance  and  best  practices  for  the  management  of
cryptographic keying material. Part 2 provides guidance
Mr. William (Tim) Polk    Ms. Donna Dodson  on  policy  and  security  planning  requirements  for  U.S.
| william.polk@nist.gov  |     |     | donna.dodson@nist.gov |     |             |            |           |                    |           |
| ---------------------- | --- | --- | --------------------- | --- | ----------- | ---------- | --------- | ------------------ | --------- |
|                        |     |     |                       |     | government  | agencies.  | Finally,  | Part  3  provides  | guidance  |
when using the cryptographic features of current systems.
| Ms. Hildegard Ferraiolo       |     |     | Dr. David Cooper      |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| hildegard.ferraiolo@nist.gov  |     |     | david.cooper@nist.gov |     |     |     |     |     |     |
CONTACTS:
DRAFT SP 800-73-4, Interfaces for Personal Identity  Ms. Elaine Barker     Mr. Quynh Dang
| Verification |     |     |     |     | elaine.barker@nist.gov  |     |     | quynh.dang@nist.gov |     |
| ------------ | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------- | --- |
FIPS 201 defines the requirements and characteristics
SP 800-56B Revision 1, Guidelines for Derived Personal
| of  a  government-wide  |     | interoperable  |     | identity  credential.  |     |     |     |     |     |
| ----------------------- | --- | -------------- | --- | ---------------------- | --- | --- | --- | --- | --- |
Identity Verification (PIV) Credentials
FIPS 201 also specifies that this identity credential must be
stored on a smart card. This document, SP 800-73, contains  This  recommendation  specifies  key-establishment
the  technical  specifications  to  interface  with  the  smart  schemes using integer factorization cryptography, based on
card to retrieve and use the PIV identity credentials. The
ANS X9.44, Key Establishment Using Integer Factorization
specifications reflect the design goals of interoperability and  Cryptography,  which  was  developed  by  the  Accredited
PIV Card functions. The goals are addressed by specifying  Standards Committee (ASC) X9, Inc.
| a  PIV  data  | model,  | card  edge  | interface,  | and  application  |     |     |     |     |     |
| ------------- | ------- | ----------- | ----------- | ----------------- | --- | --- | --- | --- | --- |
programming interface. Moreover, this document enumerates
CONTACTS:
requirements where the international integrated circuit card
standards include options and branches. The specifications  Ms. Elaine Barker     Dr. Lily Chen
go further by constraining implementers’ interpretations of  elaine.barker@nist.gov    lily.chen@nist.gov
the normative standards. Such restrictions are designed to
ease implementation, facilitate interoperability, and ensure  Dr. Dustin Moody
performance, in a manner tailored for PIV applications.
dustin.moody@nist.gov
8 8
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

DRAFT SP 800-53A Revision 4, Assessing Security and assurance helps to ensure that information technology
Privacy Controls in Federal Information Systems and component products and the information systems built from
Organizations: Building Effective Assessment Plans those products using sound system and security engineering
principles are sufficiently trustworthy.
This publication provides a set of procedures for
conducting assessments of security controls and privacy
CONTACT:
controls employed within federal information systems and
organizations. The assessment procedures, executed at NIST FISMA Team
various phases of the system development life cycle, are Joint Task Force Transformation Initiative
consistent with the security and privacy controls in NIST sec-cert@nist.gov
SP 800-53 Revision 4. The procedures are customizable
and can be easily tailored to provide organizations with the DRAFT SP 800-53 Revision 4 Appendix H, International
needed flexibility to conduct security control assessments Information Security Standards: Security Control
and privacy control assessments that support organizational Mappings for ISO/IEC 27001 and 15408
risk management processes and that are aligned with the
This update to Appendix H was initiated due to the
stated risk tolerance of the organization. Information on
2013 revision to ISO/IEC 27001, which occurred after the
building effective security assessment plans and privacy
final publication of SP 800-53 Revision 4. In addition to
assessment plans is also provided along with guidance on
considering the new content in ISO/IEC 27001 for the
analyzing assessment results.
mapping tables, new mapping criteria were employed in
CONTACT: conducting the mapping analysis. The new criteria are
intended to produce more accurate results—that is, to
NIST FISMA Team successfully meet the mapping criteria, the implementation
Joint Task Force Transformation Initiative of the mapped controls should result in an equivalent
sec-cert@nist.gov information security posture. While mapping exercises may
by their very nature, include a degree of subjectivity, the
SP 800-53 Revision 4 (Updated), Security and new criteria attempts to minimize that subjectivity to the
Privacy Controls for Federal Information Systems and greatest extent possible.
Organizations
CONTACT:
This publication provides a catalog of security and
privacy controls for federal information systems and NIST FISMA Team
organizations and a process for selecting controls to protect Joint Task Force Transformation Initiative
organizational operations (including mission, functions, sec-cert@nist.gov
image, and reputation), organizational assets, individuals,
other organizations, and the Nation from a diverse set of SP 800-52 Revision 1, Guidelines for the Selection,
threats including hostile cyber attacks, natural disasters, Configuration, and Use of Transport Layer Security (TLS)
structural failures, and human errors (both intentional Implementations
and unintentional). The security and privacy controls are
Transport Layer Security (TLS) provides mechanisms to
customizable and implemented as part of an organization-
protect sensitive data during electronic dissemination across
wide process that manages information security and privacy
the Internet. This SP provides guidance to the selection and
risk. The controls address a diverse set of security and
configuration of TLS protocol implementations while making
privacy requirements across the Federal Government and
effective use of FIPS and NIST-recommended cryptographic
critical infrastructure, derived from legislation, Executive
algorithms, and requires that TLS 1.1 configured with FIPS-
Orders, policies, directives, regulations, standards, and/
based cipher suites as the minimum appropriate secure
or mission/business needs. The publication also describes
transport protocol and recommends that agencies develop
how to develop specialized sets of controls, or overlays,
migration plans to TLS 1.2 by January 1, 2015. This SP also
tailored for specific types of missions/business functions,
identifies TLS extensions for which mandatory support must
technologies, or environments of operation. Finally, the
be provided and other recommended extensions.
catalog of security controls addresses security from both a
functionality perspective (the strength of security functions
CONTACTS:
and mechanisms provided) and an assurance perspective
(the measures of confidence in the implemented security
Dr. Kerry McKay Mr. Tim Polk
capability). Addressing both security functionality and
kerry.mckay@nist.gov william.polk@nist.gov
8 9
CSD PUBLICATIONS | FY 2014

SP 800-37 Revision 1 (Updated), Guide for Applying the Information Systems Security Officer (ISSO), Information
Risk Management Framework to Federal Information Assurance Manager (IAM), and Program Manager (PM).
Systems: a Security Life Cycle Approach
The purpose of SP 800-37 Revision 1 is to provide CONTACT:
guidelines for applying the Risk Management Framework
Ms. Patricia Toth
to federal information systems to include conducting
ptoth@nist.gov
the activities of security categorization, security control
selection and implementation, security control assessment,
information system authorization, and security control
NISTIRs
monitoring.
DRAFT NISTIR 8023, Risk Management for Replication
CONTACT:
Devices (RDs)
NIST FISMA Team This publication provides guidance on protecting the
Joint Task Force Transformation Initiative confidentiality, integrity, and availability of information
sec-cert@nist.gov processed, stored, or transmitted on replication devices
(RDs). It suggests appropriate countermeasures in the
context of the System Development Life Cycle. A security risk
DRAFT SP 800-16 Revision 1 (Second & Third Drafts), A
assessment template is also provided to help organizations
Role-Based Model for Federal Information Technology /
determine the risk associated with replication devices.
Cybersecurity Training
Meeting security responsibilities and providing for the
CONTACTS:
confidentiality, integrity, and availability of information in today’s
highly networked environment can be a difficult task. Each
Ms. Kelley Dempsey Ms. Celia Paulsen
individual that owns, uses, relies on, or manages information
kelley.dempsey@nist.gov celia.paulsen@nist.gov
and information technology (IT) systems must fully understand
their specific security responsibilities. This includes ownership
DRAFT NISTIR 8018, Public Safety Mobile Application
of the information and the role individuals have in protecting
Security Requirements Workshop Summary
information. Information that requires protection includes
information they own, information provided to them as part of This document captures the input received from the half-
their work and information they may come into contact with. day workshop titled “Public Safety Mobile Application Security
Requirements” organized by the Association of Public-Safety
This document describes information technology/
Communications Officials (APCO) International, in cooperation
cybersecurity role-based training for the Federal Departments
with FirstNet and the Department of Commerce and held on
and Agencies and Organizations (Federal Organizations) and
February 25, 2014. This first-of-its-kind workshop was attended
contractor support in these roles. Its primary focus is to provide
by public safety practitioners, mobile application developers,
a comprehensive, yet flexible, training methodology for the
industry experts, and government officials who contributed
development of training courses or modules for personnel
who have been identified as having significant information their experience and knowledge to provide input in identifying
technology/cybersecurity responsibilities. This document security requirements for public safety mobile applications.
is intended to be used by Federal information technology/
cybersecurity training personnel and their contractors to CONTACTS:
assist in designing role-based training courses or modules
for Federal Organizations personnel and contractors who Mr. Nelson Hastings
have been identified as having significant responsibilities nelson.hastings@nist.gov
for information technology/cybersecurity. This publication
should also be read, reviewed, or understood at a fairly high Ms. Barbara Guttman
level by several audiences including the Organizational Software and Systems Division
Heads through the leadership chain to the individual. Some barbara.guttman@nist.gov
of the titles include, but not limited to, the IT Managers,
Senior Agency Information Security Officer (SAISO), Mr. Michael Ogata
Certified Information Systems Security Officer (CISSO), Software and Systems Division
michael.ogata@nist.gov
9 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

DRAFT NISTIR 8014, Considerations for Identity NISTIR 7987, Policy Machine: Features, Architecture, and
Management in Public Safety Mobile Networks Specification
This document analyzes approaches to identity The ability to control access to sensitive data in
management for public safety networks in an effort to assist accordance with policy is perhaps the most fundamental
individuals developing technical and policy requirements for security requirement. Despite over four decades of security
public safety use. These considerations are scoped into the research, the limited ability for existing access control
context of their applicability to public safety communications mechanisms to enforce a comprehensive range of policy
networks with a particular focus on the nationwide public persists. While researchers, practitioners and policy makers
safety broadband network (NPSBN) based on the Long Term have specified a large variety of access control policies to
Evolution (LTE) family of standards. A short background address real-world security issues, only a relatively small
on identity management is provided alongside a review of subset of these policies can be enforced through off-the-
applicable federal and industry guidance. Considerations shelf technology, and even a smaller subset can be enforced
are provided for identity proofing, selecting tokens, and the by any one mechanism. This report describes an access
authentication process. While specific identity management control framework, referred to as the Policy Machine (PM),
technologies are analyzed, the document does not preclude which fundamentally changes the way policy is expressed
other identity management technologies from being used in and enforced. The report gives an overview of the PM and
public safety communications networks. the range of policies that can be specified and enacted. The
report also describes the architecture of the PM and the
CONTACTS: properties of the PM model in detail.
Mr. Nelson Hastings Mr. Joshua Franklin
CONTACTS:
nelson.hastings@nist.gov joshua.franklin@nist.gov
Mr. David Ferraiolo Mr. Serban Gavrila
DRAFT NISTIR 8006, NIST Cloud Computing Forensic david.ferraiolo@nist.gov serban.gavrila@nist.gov
Science Challenges
DRAFT NISTIR 7981, Mobile, PIV, and Authentication
This document summarizes the research performed by
the members of the NIST Cloud Computing Forensic Science The purpose of this document is to analyze various
Working Group, and aggregates, categorizes and discusses current and near-term options for remote electronic
the forensics challenges faced by experts when responding authentication from mobile devices that leverage both the
to incidents that have occurred in a cloud-computing investment in the PIV infrastructure and the unique security
ecosystem. The challenges are presented along with the capabilities of mobile devices, such as smart phones and
associated literature that references them. The immediate tablets.
goal of the document is to begin a dialogue on forensic
science concerns in cloud computing ecosystems. The long- CONTACTS:
term goal of this effort is to gain a deeper understanding
of those concerns (challenges) and to identify technologies Ms. Hildegard (Hildy) Ferraiolo Dr. David Cooper
and standards that can mitigate them. hildegard.ferraiolo@nist.gov david.cooper@nist.gov
CONTACTS: Mr. Andy Regenscheid
andrew.regenscheid@nist.gov
NIST Cloud Computing Forensic Science
Working Group (NIST) Mr. Salvatore (Sal) Francomacaro
Dr. Michaela Iorga salvatore.francomacaro@nist.gov
nistir8006@nist.gov
michaela.iorga@nist.gov
9 1
CSD PUBLICATIONS | FY 2014

DRAFT NISTIR 7977, NIST Cryptographic Standards and  NISTIR 7946, CVSS Implementation Guidance
Guidelines Development Process This NISTIR provides guidance to individuals scoring
This document describes the principles, processes and  IT vulnerabilities using the Common Vulnerability Scoring
procedures that drive cryptographic standards development  System (CVSS) Version 2.0 scoring metrics. The guidance
efforts. This draft document will be revised based on the  in  this  document  is  the  result  of  applying  the  CVSS
feedback received during the public comment period, and  specification to score over 50,000 vulnerabilities analyzed
the revised publication will serve as basis for NIST’s future  by the National Vulnerability Database (NVD). An overview
standards development efforts. It will also serve as the basis  of the CVSS base metrics is first presented followed by
for the review of NIST’s existing body of cryptographic  guidance for difficult and/or unique scoring situations. To
standards and guidelines. assist vulnerability analysts, common keywords and phrases
are identified and accompanied by suggested scores for
|     |     |     | particular  types  | of  software  | vulnerabilities.  | The  report  |
| --- | --- | --- | ------------------ | ------------- | ----------------- | ------------ |
CONTACTS:
includes a collection of scored IT vulnerabilities from the
| Dr. Lily Chen    | Mr. Andy Regenscheid  |     |     |     |     |     |
| ---------------- | --------------------- | --- | --- | --- | --- | --- |
NVD, alongside a justification for the provided score. Finally,
lily.chen@nist.gov  andrew.regenscheid@nist.gov this report contains a description of the NVD’s vulnerability
scoring process.
DRAFT NISTIR 7966, Security of Automated Access
| Management Using Secure Shell (SSH) |     |     | CONTACTS: |     |     |     |
| ----------------------------------- | --- | --- | --------- | --- | --- | --- |
Hosts must be able to access other hosts in an automated
|     |     |     | Mr. Joshua Franklin  |     | Mr. Harold Booth  |     |
| --- | --- | --- | -------------------- | --- | ----------------- | --- |
fashion, often with very high privileges, for a variety of
|     |     |     | joshua.franklin@nist.gov  |     | harold.booth@nist.gov |     |
| --- | --- | --- | ------------------------- | --- | --------------------- | --- |
reasons, including file transfers, disaster recovery, privileged
| access  management,  | software  and  | patch  management,  |     |     |     |     |
| -------------------- | -------------- | ------------------- | --- | --- | --- | --- |
DRAFT NISTIR 7924 (Second Draft), Reference Certificate
and dynamic cloud provisioning. This is often accomplished
| using the Secure Shell (SSH) protocol. The SSH protocol  |     |     | Policy |     |     |     |
| -------------------------------------------------------- | --- | --- | ------ | --- | --- | --- |
supports several mechanisms for authentication, with public  The purpose of this document is to identify a baseline
key  authentication  being  recommended  for  automated  set of security controls and practices to support the secure
access with SSH. Management of automated access requires  issuance of certificates. This baseline was developed with
proper provisioning, termination, and monitoring processes,  publicly-trusted Certificate Authorities (CAs) in mind. These
just as interactive access by normal users does. However, the  CAs, who issue the certificates used to secure websites
security of SSH-based automated access has been largely  using TLS and verify the authenticity of software, play a
ignored  to  date.  This  publication  assists  organizations  particularly important role online. This document formatted
in  understanding  the  basics  of  SSH  automated  access  as a Reference Certificate Policy (CP). We expect different
management in an enterprise, focusing on the management  applications and relying party communities will tailor this
of SSH access tokens. document based on their specific needs. It was structured
and developed so that the CP developer can fill in sections
CONTACT: specific  to  organizational  needs  and  quickly  produce  a
suitable CP. This Reference CP is consistent with the Internet
Mr. Murugiah Souppaya  Engineering  Task  Force  (IETF)  Public  Key  Infrastructure
murugiah.souppaya@nist.gov X.509  (IETF  PKIX)  Certificate  Policy  and  Certification
Practices Framework.
CONTACTS:
|     |     |     | Mr. Harold Booth       | Mr. Andy Regenscheid        |     |     |
| --- | --- | --- | ---------------------- | --------------------------- | --- | --- |
|     |     |     | harold.booth@nist.gov  | andrew.regenscheid@nist.gov |     |     |
9 2
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- |

DRAFT NISTIR 7863, Cardholder Authentication for the NISTIR 7628 Revision 1, Guidelines for Smart Grid
PIV Digital Signature Key CyberSecurity
FIPS 201-2 requires explicit user action by the Personal This three-volume report, Guidelines for Smart Grid
Identity Verification (PIV) cardholder as a condition for use Cybersecurity, presents an analytical framework that
of the digital signature key stored on the card. This document organizations can use to develop effective cybersecurity
clarifies the requirement for explicit user action to encourage strategies tailored to their particular combinations of
the development of compliant applications and middleware Smart Grid-related characteristics, risks, and vulnerabilities.
that use the digital signature key. Organizations in the diverse community of Smart Grid
stakeholders—from utilities to providers of energy
CONTACTS: management services to manufacturers of electric vehicles
and charging stations—can use the methods and supporting
Mr. William (Tim) Polk Ms. Hildegard (Hildy) Ferraiolo information presented in this report as guidance for
william.polk@nist.gov hildegard.ferraiolo@nist.gov assessing risk and identifying and applying appropriate
security requirements. This approach recognizes that the
Dr. David Cooper electric grid is changing from a relatively closed system
david.cooper@nist.gov to a complex, highly interconnected environment. Each
organization’s cybersecurity requirements should evolve
NISTIR 7849, A Methodology for Developing as technology advances and as threats to grid security
Authentication Assurance Level Taxonomy for Smart inevitably multiply and diversify.
Card-based Identity Verification
Smart cards (smart identity tokens) are now being CONTACTS:
extensively deployed for identity verification for controlling
The Smart Grid Interoperability Panel–Smart Grid
access to Information Technology (IT) resources as well as
Cybersecurity Committee
physical resources. Depending upon the sensitivity of the
resources and the risk of wrong identification, different
Ms. Tanya Brewer Ms. Vicky Pillitteri
authentication use cases are being deployed. Assignment
tanya.brewer@nist.gov vicky.pillitteri@nist.gov
of authentication strength for each of the use cases is often
based on: (a) the total number of three common orthogonal
authentication factors – What You Know, What You Have and
What You are, and (b) the entropy associated with each factor
chosen. The objective of this paper is to analyze the limitation
of this approach and present a methodology for assigning
authentication strengths based on the strength of pair wise
bindings between the five entities involved in smart card
based authentications – the card (token), the token secret,
the card holder, the card issuer, and the person identifier
stored in the card. The rationale for the methodology is based
on the following three observations: (a) The form factor of
the smart identity token introduces some threats of misuse;
(b) the common set of credentials objects provisioned to a
smart card embody bindings to address those threats and (c)
the strength of an authentication use case should therefore
be based on the number and type of binding verifications
that are performed in the constituent authentication
mechanisms. The use of the methodology for developing
an authentication assurance level taxonomy for two real
world smart identity token deployments is also illustrated.
CONTACT:
Dr. Ramaswamy (Mouli) Chandramouli
mouli@nist.gov 9 3
CSD PUBLICATIONS | FY 2014

ADDITIONAL PUBLICATIONS W. Burr, H. Ferraiolo and D. Waltermire, “NIST and Computer
Security,” IT Professional 16(2), 31-37 (March-April 2014). doi:
BY CSD AUTHORS
10.1109/MITP.2013.88.
CSD authors actively contribute to the security The U.S. NIST’s highly visible work in four key
community by authoring articles in the scholarly literature, areas—cryptographic standards, role-based access
participating in technical conferences, contributing to control, identification card standards, and security
encyclopedias and other books, and publishing other “white automation—has and continues to shape computer
papers” that fall outside the scope of NIST Technical Series and information security at both national and global
publications described in the preceding section. levels. This article is part of a special issue on NIST
contributions to IT.
The following documents were published during FY
2014. For conference papers, the contributions listed below F. Izadi, F. Khoshnam, D. Moody and A.S. Zargar, “Elliptic
were either i) accepted for a conference held during FY 2014, Curves Arising from Brahmagupta Quadrilaterals,” Bulletin
or ii) accepted for a conference held prior to FY 2014 with a of the Australian Mathematical Society 90(1), 47-56 (August
final proceeding published in FY 2014 (and not listed in an 2014). doi: 10.1017/S0004972713001172.
earlier CSD Annual Report). All NIST authors of a publication A Brahmagupta quadrilateral is a cyclic
are identified using italics. quadrilateral whose sides, diagonals, and area are
Links to the preprints and/or final publications all integer values. In this article, we characterize
of the documents below are available at the notions of Brahmagupta, introduced by
http://csrc.nist.gov/publications/articles. K. R. S. Sastry, by means of elliptic curves. Motivated
by these characterizations, we use Brahmagupta
Journal Articles quadrilaterals to construct infinite families of elliptic
curves with torsion group /2 x /2 having ranks
I. Bojanova and D.R. Kuhn, “IT Pro Conference on Information
(at least) 4, 5, and 6. Furthermore, by specializing we
Systems Governance,” IT Professional 16(4), 4-6 (July/August
give examples from these families of specific curves
2014). doi: 10.1109/MITP.2014.55.
with rank 9.
Approximately 100 IT professionals participated in
R. Kissel, “Avoiding Accidental Data Loss,” IT Professional
the 2014 IT Pro Conference on Information Systems
15(5), 12-15 (September-October 2013). doi: 10.1109/
Governance, held at NIST on May 22, 2014 (www.
MITP.2013.75.
computer.org/itproconf). Information systems
governance focuses on properly managing IT resources Does your organization have systematic procedures to
to achieve organizational goals. The conference was remove sensitive data from obsolete equipment, or do
designed to bring together IT professionals from you use a somewhat ad hoc process for the cleanup
industry, government, and academia to discuss new and disposal of old gear? Careless disposal of data
challenges in information systems and share ways of storage hardware has led to costly and embarrassing
overcoming such challenges. Sponsored by IEEE, NIST, incidents for organizations that discovered too
and Noblis, the conference featured three keynotes late that their control over media sanitization was
and 12 presentations, focusing on the following key inadequate. The guidelines presented here will help
questions: 1) How can we get the most value from IT organizations review their sanitization procedures
while still delivering successful projects and reliable and develop a more sound process if needed.
information systems and infrastructure? 2) How can
R. Marin-Lopez, F. Bernal-Hidalgo, S. Das, L. Chen and
we secure critical systems while keeping pace with
Y. Ohba, “A New Standard for Securing Media-Independent
advances in technology? and 3)What changes are on
Handover: IEEE 802.21a,” IEEE Wireless Communications
the horizon for technology and business leaders?
20(6), 82-90 (December 2013). doi: 10.1109/
R. Bryce and D.R. Kuhn, “Software Testing,” Computer MWC.2013.6704478.
(IEEE Computer) 47(2), 21-22 (February 2014). doi: 10.1109/
When enabling handover between different radio
MC.2014.45.
interfaces (e.g., handover from 3G to Wi-Fi), reducing
[Guest editor introduction to a special issue presenting network access authentication latency and securing
papers focused on important problems within the handover related signaling messages are major
Software Testing community.] challenging problems, amongst many others. The
IEEE 802 Local Area Network (LAN)/ Metropolitan
9 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Area Network (MAN) Standards committee has directing the Administration to take steps to improve
recently finished its standardization work in this area information sharing with the private sector, raise the
by defining the IEEE standard 802.21a-2012. The level of cybersecurity across our critical infrastructure,
mechanisms introduced in this standard are aimed and enhance privacy and civil liberties.” That Executive
to protect the IEEE standard 802.21-2008 messages Order, E.O. 13636, Improving Critical Infrastructure
and services and to reduce handover latency by Cybersecurity, directed the National Institute of
introducing the concept of proactive authentication. Standards and Technology (NIST) to develop a
We provide a comprehensive survey of this standard voluntary, risk-based Cybersecurity Framework
and describe how the defined mechanisms can be (“Framework”)—based on existing industry standards
used to reduce the overall latency during handover and best practices—to help organizations manage
between access networks using heterogeneous radio cybersecurity risk. The resulting Framework was
interfaces. created through a yearlong collaboration between
government and industry.
E. McDuffie and V.P. Piotrowski, “The Future of Cybersecurity
Education,” Computer (IEEE Computer) 47(8), 67-69 A.L. Roginsky, K. Christensen and M. Mostowfi, “Delay
(August 2014). doi: 10.1109/MC.2014.224. Behavior of On-Off Scheduling: Extending Idle Periods,”
Applied Mathematics & Information Sciences 7(6), 2123-2136
By fostering public-private partnerships in
(November 2013). doi: 10.12785/amis/070603.
cybersecurity education, the U.S. government is
motivating federal agencies, industry, and academia On-off scheduling of systems that have the ability
to work more closely together to defend cyberspace. to sleep can be used to extend system idle periods
and enable greater opportunities for energy savings
P. Mell and R. Harang, “Reducing the Cognitive Load
from sleeping. In this paper, we achieve a theoretical
on Analysts through Hamming Distance Based Alert
understanding of the delay behavior of on-off
Aggregation,” International Journal of Network Security &
scheduling as it may apply to communications links
Its Applications (IJNSA) 6(5), 35-50 (September 2014).
and other systems capable of sleeping. We consider
Previous work introduced the idea of grouping
a single-server coalescing queue with a scheduler
alerts at a Hamming distance of 1 to achieve alert
that schedules on-off periods for the server in order
aggregation; such aggregated meta-alerts were
to extend idle periods of the downstream link. At the
shown to increase alert interpret-ability. However,
start of an off period (duration T ) the server stops
a mean of 84 023 daily Snort alerts were reduced
serving jobs immediately if idle,
o
o
ff
r after processing
to a still formidable 14 099 meta-alerts. In this work,
a job already in service. Service of any queued and
we address this limitation by investigating several
arriving jobs begins at the start of the next on period
approaches that all contribute towards reducing the
(duration T ). On and off periods are fixed. We solve
burden on the analyst and providing timely analysis. on
for the scheduling queue behavior as a function of
We explore minimizing the number of both alerts and
T , T , interarrival time t, service time x, and time
data fields by aggregating at Hamming distances off on
of first arrival g for periodic job arrivals. Results are
greater than 1. We show how increasing bin sizes can
closed form and have both theoretical and practical
improve aggregation rates. And we provide a new
significance.
aggregation algorithm that operates up to an order
A.T. Vassilev and T.A. Hall, “The Importance of Entropy to
of magnitude faster at Hamming distance 1. Lastly, we
Information Security,” Computer (IEEE Computer) 47(2), 78-
demonstrate the broad applicability of this approach
81 (February 2014). doi: 10.1109/MC.2014.47.
through empirical analysis of Windows security alerts,
Snort alerts, netflow records, and DNS logs. The strength of cryptographic keys is an active
challenge in academic research and industrial practice.
V.Y. Pillitteri, “NIST Cybersecurity Framework Addresses
In this paper, we discuss the entropy as fundamentally
Risks to Critical Infrastructure,” ei Magazine 19 (6), 20-21
important concept for generating hard-to-guess, i.e.,
(June 2014).
strong, cryptographic keys and outline the difficulties
On February 12, 2014, President Obama issued a
in generating and estimating the available entropy
statement that, “[c]yber threats pose one the gravest
for cryptographic needs. We consider traditional
national security dangers that the United States faces.
entropy estimation in cryptographic applications and
To better defend our nation against this systemic
motivate the development of new spectral techniques
challenge, one year ago I signed an Executive Order
for estimation.
9 5
CSD PUBLICATIONS | FY 2014

L. Wang, S. Jajodia, A. Singhal, P. Cheng and S. Noel, “k-Zero Conference Papers
Day Safety: A Network Security Metric for Measuring the
R. Chandramouli, “Analysis of Protection Options for
Risk of Unknown Vulnerabilities,” IEEE Transactions on
Virtualized Infrastructures in Infrastructure as a Service
Dependable and Secure Computing 11(1), 30-44 (January-
Cloud,” Fifth International Conference on Cloud Computing,
February 2014). doi: 10.1109/TDSC.2013.24.
GRIDs, and Virtualization (CLOUD COMPUTING 2014),
By enabling a direct comparison of different security Venice, Italy, May 25-29, 2014, pp. 37-43.
solutions with respect to their relative effectiveness,
Infrastructure as a Service (IaaS) is one of the three
a network security metric may provide quantifiable
main cloud service types where the cloud consumer
evidences to assist security practitioners in securing
consumes a great variety of resources such as
computer networks. However, research on security
computing (Virtual Machines or VMs), virtual network,
metrics has been hindered by difficulties in handling
storage and utility programs (DBMS). Any large-scale
zero day attacks exploiting unknown vulnerabilities.
offering of this service is feasible only through a
In fact, the security risk of unknown vulnerabilities
virtualized infrastructure at the service provider. At the
has been considered as something unmeasurable due
minimum, this infrastructure is made up of resources
to the less predictable nature of software flaws. This
such as Virtualized hosts together with associated
causes a major difficulty to security metrics, because
virtual network and hardware/software for data
a more secure configuration would be of little value
storage An IaaS’s consumer’s total set of interactions
if it were equally susceptible to zero day attacks. In
with these resources constitute the set of use cases for
this paper, we propose a novel security metric, k-zero
IaaS cloud service. These use cases have associated
day safety, to address this issue. Instead of attempting
security requirements and these requirements are
to rank unknown vulnerabilities, the described metric
met by protection options enabled by available
counts how many such vulnerabilities would be
security solutions/technologies. The purpose of this
required for compromising network assets; a larger
paper is to analyze these protection options from
count implies more security since the likelihood
the viewpoint of: (a) Security functionality they can
of having more unknown vulnerabilities available,
provide and (b) the architecture that governs their
applicable, and exploitable all at the same time will
deployment, so that IaaS consumers can decide on
be significantly lower. We formally define the metric,
the most appropriate security configuration for their
analyze the complexity of computing the metric,
VM instances depending upon the profile of the
devise heuristic algorithms for intractable cases, and
applications running in them.
finally demonstrate through case studies that applying
the metric to existing network security practices may I. Dominguez, D.R. Kuhn, R.N. Kacker, and Y. Lei, “CCM: A
generate actionable knowledge. Tool for Measuring Combinatorial Coverage of System State
Space” [poster], 2013 ACM / IEEE International Symposium
L. Wilbanks, D.R. Kuhn and W. Chou, “IT Risks,” IT Professional
on Empirical Software Engineering and Measurement (ESEM
16(1), 20-21 (January-February 2014). doi: 10.1109/MITP.2014.7.
2013), Baltimore, Maryland, October 10-11, 2013, p. 291. doi:
Risk management is a common phrase when managing 10.1109/ESEM.2013.44.
information, from the Chief Information Security
This poster presents some measures of combinatorial
Officer (CISO) to the programmer. We acknowledge
coverage that can be helpful in estimating residual
that risk management is the identification, assessment
risk related to insufficient testing of rare interactions,
and prioritization of risks and reflects how we manage
and a tool for computing these measures.
uncertainty. These are some areas of risk that we
have come to accept, their mitigation strategies are D. Ferraiolo, S. Gavrila and W. Jansen, “On the Unification of
part of our development, part of our everyday work. Access Control and Data Services,” 15th IEEE Conference on
Most IT professionals would agree that IT is good at Information Reuse and Integration (IRI 2014), San Francisco,
identifying and managing the risks. But is that really California, August 13-15, 2014, pp. 450-457. doi: 10.1109/
the case or has risk management/mitigation become IRI.2014.7051924.
a buzz word for us? A primary objective of enterprise computing (via a
data center, cloud, etc.) is the controlled delivery of
data services (DS). Typical DSs include applications
such as email, workflow, and records management, as
well as system level features, such as file and access
9 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

control management. Although access control (AC) This poster gives an overview of the experience of eight
currently plays an important role in imposing control pilot projects, over two years, applying combinatorial
over the execution of DS capabilities, AC can be more testing in a large aerospace organization. While results
fundamental to computing than one might expect. varied across the different pilot projects, overall it was
That is, if properly designed, a single AC mechanism estimated that CT would save roughly 20 % of testing
can simultaneously implement, control, and deliver cost, with 20 % to 50 % improved test coverage.
capabilities of multiple DSs. The Policy Machine
D.R. Kuhn, R.N. Kacker and Y. Lei, “Estimating Fault Detection
(PM) is an AC framework that has been designed
Effectiveness” [poster], Third International Workshop on
with this objective in mind. This paper describes the
Combinatorial Testing (IWCT 2014), in Proceedings of the
PM features that provide a generic AC mechanism
Seventh IEEE International Conference on Software, Testing,
to implement DS capabilities, and comprehensively
Verification and Validation (ICST 2014), Cleveland, Ohio,
enforces mission tailored access control policies
March 31 - April 4, 2014, p.154. doi: 10.1109/ICSTW.2014.69.
across DSs.
A t-way covering array can detect t-way faults;
L. Ghandehari, J. Czerwonka, Y. Lei, S. Shafiee, R.N. Kacker
however, they generally include other combinations
and D.R. Kuhn, “An Empirical Comparison of Combinatorial
beyond t-way as well. For example, a particular test
and Random Testing,” Third International Workshop on
set of all 5-way combinations is shown capable of
Combinatorial Testing (IWCT 2014), in Proceedings of the
detecting all seeded faults in a test program, despite
Seventh IEEE International Conference on Software, Testing,
the fact that it contains up to 9-way faults. This
Verification and Validation (ICST 2014), Cleveland, Ohio,
poster gives an overview of methods for estimating
March 31 - April 4, 2014, pp. 68-77. doi: 10.1109/ICSTW.2014.8.
fault detection effectiveness of a test set based
Some conflicting results have been reported on the on combinatorial coverage for a class of software.
comparison between t-way combinatorial testing and Detection effectiveness depends on the distribution
random testing. In this paper, we report a new study of t-way faults, which is not known. However based
that applies t-way and random testing to the Siemens on past experience one could say for example the
suite. In particular, we investigate the stability of the fraction of 1-way faults is F = 60 %, 2-way faults F =
1 2
two techniques. We measure both code coverage 25 % F = 10 % and F = 5 %. Such information could
3 4
and fault detection effectiveness. Each program in be used in determining the required strength t. It is
the Siemens suite has a number of faulty versions. In shown that the fault detection effectiveness of a test
addition, mutation faults are used to better evaluate set may be affected significantly by the t-way fault
fault detection effectiveness in terms of both number distribution, overall, simple coverage at each level of
and diversity of faults. The experimental results t, number of values per variable, and minimum t-way
show that in most cases, t-way testing performed coverage. Using these results, we develop practical
as good as or better than random testing. There are guidance for testers.
few cases where random testing performed better,
C. Liu, A. Singhal and D. Wijesekera, “A Model Towards Using
but with a very small margin. Overall, the differences
Evidence from Security Events for Network Attack Analysis,”
between the two techniques are not as significant as
11th International Workshop on Security in Information
one would have probably expected. We discuss the
Systems (WOSIS 2014), Lisbon, Portugal, April 27, 2014. doi:
practical implications of the results. We believe that
10.5220/0004980300830095.
more studies are needed to better understand the
Constructing an efficient and accurate model from
comparison of the two techniques.
security events to determine an attack scenario for
J. Hagar, D.R. Kuhn, R.N. Kacker and T. Wissink,
an enterprise network is challenging. In this paper,
“Introducing Combinatorial Testing in a Large Organization:
we discuss how to use evidence obtained from
Pilot Project Experience Report” [poster], Third International
security events to construct an attack scenario and
Workshop on Combinatorial Testing (IWCT 2014), in
build an evidence graph. To achieve the accuracy
Proceedings of the Seventh IEEE International Conference
and completeness of the evidence graph, we use
on Software, Testing, Verification and Validation (ICST 2014),
Prolog inductive and abductive reasoning to correlate
Cleveland, Ohio, March 31 - April 4, 2014, p. 153. doi: 10.1109/
evidence by reasoning the causality, and use an anti-
ICSTW.2014.70.
forensics database and a corresponding attack graph
to find the missing evidence. In addition, because the
constructed scenario and supplied evidence might
97
CSD PUBLICATIONS | FY 2014

need to stand up in the court of law, the federal rules of 8898, Lightweight Cryptography for Security and Privacy, T.
evidence are also taken into account to predetermine Eisenbarth and E. Öztürk, eds., Berlin: Springer, 2015, pp. 21-
the admissibility of the evidence. 33. doi: 10.1007/978-3-319-16363-5_2.
P.M. Mell and R. Harang, “Limitations to Threshold Random A generic way to design lightweight cryptographic
Walk Scan Detection and Mitigating Enhancements,” 2013 primitives is to construct simple rounds using small
IEEE Conference on Communications and Network Security nonlinear components such as 4x4 S-boxes and use
(CNS), Washington, DC, October 14-16, 2013, pp. 332-340. these iteratively (e.g., PRESENT and SPONGENT).
doi: 10.1109/CNS.2013.6682723. In order to efficiently implement the primitive,
efficient implementations of its internal components
This paper discusses limitations in one of the most
are needed. Multiplicative complexity of a function
widely cited single source scan detection algorithms:
is the minimum number of AND gates required to
threshold random walk (TRW). If an attacker knows
implement it by a circuit over the basis (AND, XOR,
that TRW is being employed, these limitations
NOT). It is known that multiplicative complexity is
enable full circumvention allowing undetectable high
exponential in the number of input bits n. Thus it came
speed full horizontal and vertical scanning of target
networks from a single Internet Protocol address. To
as a surprise that circuits for all 65 536 functions on
four bits were found which used at most three AND
mitigate the discovered limitations, we provide three
gates. In this paper, we verify this result and extend it
enhancements to TRW and analyze the increased
to five-variable Boolean functions. We show that the
cost in computational complexity and memory. Even
multiplicative complexity of a Boolean function with
with these mitigations in place, circumvention is still
five variables is at most four.
possible but only through collaborative scanning
(something TRW was not designed to detect) with a L. Wang, M. Zhang, S. Jajodia, A. Singhal and M. Albanese,
significant increase in the required level of effort and “Modeling Network Diversity for Evaluating the Robustness
usage of resources. of Networks against Zero-Day Attacks,” 19th European
Symposium on Research in Computer Security (ESORICS
P.M. Mell and R. Harang, “Using Network Tainting to Bound
2014), Wroclaw, Poland, September 7-11, 2014. In Lecture
the Scope of Network Ingress Attacks,” Eighth International
Notes in Computer Science 8713, Computer Security –
Conference on Software Security and Reliability (SERE
ESORICS 2014, M. Kutyłowski and J. Vaidya, eds., Berlin:
2014), San Francisco, California, June 30-July 2, 2014, pp.
Springer, 2014, pp. 494-511. doi: 10.1007/978-3-319-11212-1_28.
206-215. doi: 10.1109/SERE.2014.34.
The interest in diversity as a security mechanism has
This research describes a novel security metric,
recently been revived in various applications, such
network taint, which is related to software taint
as Moving Target Defense (MTD), resisting worms
analysis. We use it here to bound the possible
in sensor networks, and improving the robustness
malicious influence of a known compromised node
of network routing. However, most existing efforts
through monitoring and evaluating network flows.
on formally modeling diversity have focused on a
The result is a dynamically changing defense-in-depth
single system running diverse software replicas or
map that shows threat level indicators gleaned from
variants. At a higher abstraction level, as a global
monotonically decreasing threat chains. We augment
property of the entire network, diversity and its
this analysis with concepts from the complex networks
impact on security have received limited attention.
research area in forming dynamically changing
In this paper, we take the first step towards formally
security perimeters and measuring the cardinality of
modeling network diversity as a security metric
the set of threatened nodes within them. In providing
for evaluating the robustness of networks against
this, we hope to advance network incident response
potential zero day attacks. Specifically, we first devise
activities by providing a rapid automated initial triage
a biodiversity-inspired metric based on the effective
service that can guide and prioritize investigative
number of distinct resources. We then propose two
activities.
complementary diversity metrics, based on the least
M. Sönmez Turan, R. Peralta, “The Multiplicative Complexity
and the average attacking efforts, respectively. Finally,
of Boolean Functions on Four and Five Variables,” Third
we evaluate algorithm and metrics through simulation.
International Workshop on Lightweight Cryptography
for Security & Privacy (LightSec 2014), Istanbul, Turkey,
September 1-2, 2014. In Lecture Notes in Computer Science
9 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

Books and Book Sections The white paper provides an overview of SP 800-53,
Revision 4, Security and Privacy Controls for Federal
Y. Cheng, J. Deng, J. Li, S. DeLoach, A. Singhal and X.
Information Systems and Organizations, which was
Ou, “Metrics of Security,” Cyber Defense and Situational
published April 30, 2013.
Awareness, edited by A. Knott, C. Wang and R.F. Erbacher
(Advances in Information Security 62), Berlin: Springer, 2014, “Framework for Improving Critical Infrastructure
pp. 263-295. doi: 10.1007/978-3-319-11391-3_13. Cybersecurity, Version 1.0,” NIST, Gaithersburg, Maryland,
February 12, 2014, 41 pp.
Discussion of challenges and ways of improving
Cyber Situational Awareness dominated our previous The national and economic security of the United
chapters. However, we have not yet touched on how to States depends on the reliable functioning of critical
quantify any improvement we might achieve. Indeed, infrastructure. Cybersecurity threats take advantage
to get an accurate assessment of network security of the increased complexity and connectivity of critical
and provide sufficient Cyber Situational Awareness infrastructure systems, placing the Nation’s security
(CSA), simple but meaningful metrics—the focus of at risk. To better protect these systems, the President
the Metrics of Security chapter—are necessary. The issued Executive Order 13636, Improving Critical
adage, “what can’t be measured can’t be effectively Infrastructure Cybersecurity, on February 12, 2013. The
managed,” applies here. Without good metrics and the Executive Order established that “[i]t is the Policy of
corresponding evaluation methods, security analysts the United States to enhance the security and resilience
and network operators cannot accurately evaluate of the Nation’s critical infrastructure and to maintain
and measure the security status of their networks a cyber environment that encourages efficiency,
and the success of their operations. In particular, innovation, and economic prosperity while promoting
this chapter explores two distinct issues: (i) how to safety, security, business confidentiality, privacy, and
define and use metrics as quantitative characteristics civil liberties.” In enacting this policy, the Executive
to represent the security state of a network, and (ii) Order calls for the development of a voluntary risk-
how to define and use metrics to measure CSA from a based Cybersecurity Framework—a set of industry
defender’s point of view. standards and best practices to help organizations
manage cybersecurity risks. The resulting Framework,
White Papers created through collaboration between government
and the private sector, uses a common language to
K. Dempsey, R. Ross and K. Stine, “Supplemental
address and manage cybersecurity risk in a cost-
Guidance on Ongoing Authorization: Transitioning to Near
effective way based on business needs without
Real-Time Risk Management,” NIST, Gaithersburg, Maryland,
placing additional regulatory requirements on
June 2014, 13 pp.
businesses. The Framework enables organizations—
Office of Management and Budget (OMB)
regardless of size, degree of cybersecurity risk, or
Memorandum M-14-03, Enhancing the Security
cybersecurity sophistication—to apply the principles
of Federal Information and Information Systems,
and best practices of risk management to improving
reminds federal agencies that, “our nation’s security
the security and resilience of critical infrastructure.
and economic prosperity depend on ensuring the
The Framework provides organization and structure
confidentiality, integrity and availability of federal
to today’s multiple approaches to cybersecurity by
information and information systems,” and directs
assembling standards, guidelines, and practices that
NIST to “publish guidance establishing a process and
are working effectively in industry today. Moreover,
criteria for agencies to conduct ongoing assessments
because it references globally recognized standards
and authorization.” The following guidance clarifies
for cybersecurity, the Framework can also be used by
and amplifies current NIST guidance on security
organizations located outside the United States and
authorization contained in Special Publications 800-
can serve as a model for international cooperation on
37, 800-39, 800-53, 800-53A, and 800-137.
strengthening critical infrastructure cybersecurity.
K. Dempsey, G. Witte and D. Rike, “Summary of NIST SP
800-53, Revision 4: Security and Privacy Controls for Federal
Information Systems and Organizations,” NIST, Gaithersburg,
Maryland, February 19, 2014, 13 pp.
9 9
CSD PUBLICATIONS | FY 2014

Smart Grid Interoperability Panel, Smart Grid Cybersecurity
Committee (NIST contributors include V.Y. Pillitteri and T.L.
| Brewer),  “Cybersecurity  |     |     | User’s  | Guide  to  | the  Guidelines  |
| ------------------------- | --- | --- | ------- | ---------- | ---------------- |
for Smart Grid Cybersecurity (NISTIR 7628 Vol. 1 2010),”
February 26, 2014, 30 pp.
| While        | the  NISTIR    | 7628  | document  |              | covers  many   |
| ------------ | -------------- | ----- | --------- | ------------ | -------------- |
| significant  | cybersecurity  |       | topics,   | this         | User’s  Guide  |
| is  focused  | primarily      |       | on  the   | application  | of  NISTIR     |
7628 Volume 1 in the context of an organization’s
cybersecurity risk management practices. The User’s
| Guide  | provides  | an  | end-to-end  | implementation  |     |
| ------ | --------- | --- | ----------- | --------------- | --- |
guide for an organization’s Smart Grid cybersecurity
activities, and references the Department of Energy
Electricity Subsector Cybersecurity Risk Management
Process to provide the cybersecurity risk management
| framework  | and  | organizational  |     | structure  | needed  |
| ---------- | ---- | --------------- | --- | ---------- | ------- |
before system-specific controls identified in NISTIR
7628 can be applied. The User’s Guide was developed
with significant involvement by utilities.
1 0 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

| ACRONYMS |     | CMAC  |  Cipher-based Message Authentication  |
| -------- | --- | ----- | ------------------------------------- |
Code
|       |                                     | CMVP  | Cryptographic Module Validation Program  |
| ----- | ----------------------------------- | ----- | ---------------------------------------- |
| 3GPP  | 3rd Generation Partnership Project  |       |                                          |
|       |                                     | CNCI  |  Comprehensive National Cybersecurity    |
| ABA   | American Bar Association            |       |                                          |
Initiatives
| ABAC     | Attribute Based Access Control         |          |                                         |
| -------- | -------------------------------------- | -------- | --------------------------------------- |
|          |                                        | CNSS     | Committee on National Security Systems  |
| AC       | Access Control                         |          |                                         |
|          |                                        | ConMon   | Continuous monitoring                   |
| ACPT     | Access Control Policy Tool             |          |                                         |
|          |                                        | CP       | Certificate Policy                      |
| ACRLCS   | AC Rule Logic Circuit Simulation       |          |                                         |
|          |                                        | CPE      | Common Platform Enumeration             |
| ACTS     | Advanced Combinatorial Testing System  |          |                                         |
|          |                                        | CPS      | Cyber-Physical Systems                  |
| AES      | Advanced Encryption Standard           |          |                                         |
|          |                                        | CRADA    |  Cooperative Research and Development   |
| AIM      | Algorithms for Intrusion Measurement   |          |                                         |
Agreement
| AMI   | Advanced Metering Infrastructure  |       |                                  |
| ----- | --------------------------------- | ----- | -------------------------------- |
|       |                                   | CRMF  |  Cloud-adapted Risk Management   |
| ANS   | American National Standards       |       | Framework                        |
ANSI  American National Standards Institute  CS1  Cyber Security 1
API  Application programming interface  CSD  Computer Security Division
ARF  Asset Reporting Format  CSIA  Cyber Security and Information Assurance
ARL  Army Research Laboratory  CSIC  Computer Security Incident Coordination
ASC  Accredited Standards Committee  CSIRT   Computer Security Incident Response
Team
| ATIS  |  Alliance for Telecommunications Industry  |        |                                    |
| ----- | ------------------------------------------ | ------ | ---------------------------------- |
|       | Solutions                                  | CSPs   | Critical Security Parameters       |
|       |                                            | CSRC   | Computer Security Resource Center  |
BioCTS  Biometrics Conformance Test Software  CST   Cryptographic and Security Testing
BIOS  Basic Input/Output System  CSWG  Cyber Security Working Group
|     |     | CTAs   | Conformance Test Architectures  |
| --- | --- | ------ | ------------------------------- |
CAC   Common Access Card  CTG  Cryptographic Technology Group
CAESARS    Continuous Asset Evaluation, Situational  CTSs  Conformance Test Suites
Awareness and Risk Scoring
|              |                                       | CVE    | Common Vulnerabilities and Exposures  |
| ------------ | ------------------------------------- | ------ | ------------------------------------- |
| CAESARS-FE   | CAESARS Framework Extension           |        |                                       |
|              |                                       | CVSS   | Common Vulnerability Scoring System   |
| CAs          | Certificate Authorities               |        |                                       |
| CAVP         |  Cryptographic Algorithm Validation   |        |                                       |
|              |                                       | DARPA  |  Defense Advanced Research Projects   |
Program
Agency
| CCE    | Common Configuration Enumeration            |      |                                  |
| ------ | ------------------------------------------- | ---- | -------------------------------- |
|        |                                             | DCS  | Distributed Control Systems      |
| CCEVS  |  Common Criteria Evaluation and Validation  |      |                                  |
|        |                                             | DHS  | Department of Homeland Security  |
Scheme
|        |                                      | DHHS    | Department of Health and Human Services |
| ------ | ------------------------------------ | ------- | --------------------------------------- |
| CCSS   | Common Configuration Scoring System  |         |                                         |
|        |                                      | DISA    | Defense Information Systems Agency      |
| CERT   | Computer Emergency Readiness Team    |         |                                         |
|        |                                      | DNS     | Domain Name System                      |
| CIO    | Chief Information Officer            |         |                                         |
|        |                                      | DNSSEC  | Domain Name System Security Extensions  |
| CISO   | Chief Information Security Officer   |         |                                         |
|        |                                      | DOD     | Department of Defense                   |
| CKMS   | Cryptographic Key Management System  |         |                                         |
|        |                                      | DOE     | Department of Energy                    |
1 0 1
ACRONYMS  |  FY 2014

DRBG   Deterministic random bit generator  HMAC   Hash-based Message Authentication Code
DSS  Digital Signature Standard  HSPD-12  Homeland Security Presidential Directive-12
EAC  Election Assistance Commission  IA   Information Assurance
ECDSA  Elliptic Curve Digital Signature Algorithm  IaaS  Infrastructure as a Service
ECP   Enterprise Compliance Profile  IAD   Information Access Division
EL  Engineering Laboratory  IAD   Information Assurance Directorate
EO   Executive Order  IAWG  Identity Assurance Working Group
|     | ICS   | Industrial Control Systems  |
| --- | ----- | --------------------------- |
FAQ  Frequently Asked Questions  ICT   Information and Communications Technol-
ogies
FAR   Federal Acquisition Regulation
|     | IEEE  |  Institute of Electrical and Electronics   |
| --- | ----- | ------------------------------------------ |
FBI   Federal Bureau of Investigation
Engineers
FCCX   Federal Cloud Credential Exchange
|     | INCITS   |  InterNational Committee for Information  |
| --- | -------- | ----------------------------------------- |
FDCC  Federal Desktop Core Configuration
Technology Standards
FedRAMP    Federal Risk and Authorization
|     | IP   | Internet Protocol  |
| --- | ---- | ------------------ |
Management Program
|     | IPv6  | Internet Protocol Version 6 |
| --- | ----- | --------------------------- |
FHE  fully homomorphic encryption
|     | IR  | Interagency or Internal Report  |
| --- | --- | ------------------------------- |
FIPS   Federal Information Processing Standard
|     | ISP   | Internet Service Provider  |
| --- | ----- | -------------------------- |
FIRST   Forum of Incident Response and Security
|     | IT  | information technology  |
| --- | --- | ----------------------- |
Teams
|     | ITL  | Information Technology Laboratory  |
| --- | ---- | ---------------------------------- |
FirstNet  First Responder Network Authority
|     | IUT  | Implementation under test  |
| --- | ---- | -------------------------- |
FISMA   Federal Information Security Management
| Act  | IV&V  | Independent Verification and Validation  |
| ---- | ----- | ---------------------------------------- |
FISSEA   Federal Information Systems Security   ISPAB   Information Security and Privacy Advisory
| Educators’ Association |     | Board  |
| ---------------------- | --- | ------ |
FITSI  Federal IT Security Institute  ISIMC    Information Security and Identity
Management Committee’s
FPE  format-preserving encryption
|     | ISO  |  International Organization for   |
| --- | ---- | --------------------------------- |
FVAP   Federal Voting Assistance Program
Standardization
FY  Fiscal Year
|     | ISA   | International Society of Automation  |
| --- | ----- | ------------------------------------ |
|     | ITI   | the Information Technology Industry  |
GAO  Government Accountability Office
|     | IWG  | Interagency Working Group  |
| --- | ---- | -------------------------- |
GCM  Galois/Counter Mode
GCSE  Group Communication System Enablers
|     | JTC 1  | Joint Technical Committee 1  |
| --- | ------ | ---------------------------- |
GICS  Generic Identity Command Set
GPS  Global Positioning System
|     | LTE  | Long-Term Evolution  |
| --- | ---- | -------------------- |
GSA  General Services Administration
|     | MACs   | Message authentication codes  |
| --- | ------ | ----------------------------- |
HAVA   Help America Vote Act
|     | MIH   | Media-independent handover  |
| --- | ----- | --------------------------- |
HIT  Health information technology
|     | MMT   | Multi-Block Message Test  |
| --- | ----- | ------------------------- |
1 0 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

MLS   Multi-Level Security  OPM   Office of Personnel Management
|     | OVAL  |  Open Vulnerability and Assessment   |
| --- | ----- | ------------------------------------ |
Language
NASA    National Aeronautics and Space Adminis-
tration
NCCoE   National Cybersecurity Center of Excel- PCI   Payment Card Industry
| lence  | PIV  | Personal Identity Verification  |
| ------ | ---- | ------------------------------- |
NCP  National Checklist Program
|     | PIV-I  | PIV-Interoperable  |
| --- | ------ | ------------------ |
NFC  Near Field Communications  PKI   Public Key Infrastructure
NGAC-FA   Next Generation Access Control –
|     | PKIX   | Public Key Infrastructure X.509  |
| --- | ------ | -------------------------------- |
Functional Architecture
|     | PLC  | Programmable Logic Controllers  |
| --- | ---- | ------------------------------- |
NGAC-GOADS   Next Generation Access Control – Generic
|     | PM  | Policy Machine  |
| --- | --- | --------------- |
Operations & Abstract Data Structures
|     | PML   | Physical Measurement Laboratory  |
| --- | ----- | -------------------------------- |
NGAC-IRPADS   Next Generation Access Control-Imple-
| mentation Requirements, Protocols and  | PoS   | Point of service  |
| -------------------------------------- | ----- | ----------------- |
API Definitions
|     | PSCR  | Public Safety Communications Research  |
| --- | ----- | -------------------------------------- |
NICCS   National Initiative for Cybersecurity Ca-
reers and Studies
|     | RBAC   | Role-Based Access Control  |
| --- | ------ | -------------------------- |
NICE   National Initiative for Cybersecurity Educa-
|     | RBGs   | Random bit generators  |
| --- | ------ | ---------------------- |
tion
|     | R&D   | Research and development  |
| --- | ----- | ------------------------- |
NIEM   National Information Exchange Model
|     | RFI  | Request for Information  |
| --- | ---- | ------------------------ |
NISTIR  NIST Interagency or Internal Report
|     | RFID  | Radio Frequency Identification  |
| --- | ----- | ------------------------------- |
NITRD    Networking and Information Technology
| Research and Development | RMF  | Risk Management Framework  |
| ------------------------ | ---- | -------------------------- |
NNLT   NIST NICE Leadership Team  RNG   Random number generation
NPIVP  NIST Personal Identity Verification Program  RPL  Removed Products List
NPSBN  National Public Safety Broadband Network  RSA  Rivest, Shamir, Adleman
NSA  National Security Agency
NSTIC   National Strategy for Trusted Identities in  SACM   Security Automation and Continuous
| Cyberspace  |     | Monitoring  |
| ----------- | --- | ----------- |
NTIA   National Telecommunications and
|     | SBA  | Small Business Administration  |
| --- | ---- | ------------------------------ |
Information Administration
|     | SC  | Subcommittee  |
| --- | --- | ------------- |
NVD   National Vulnerability Database
|     | SCADA  | Supervisory Control and Data Acquisition  |
| --- | ------ | ----------------------------------------- |
NVLAP   National Voluntary Laboratory
|     | SCAP  | Security Content Automation Protocol  |
| --- | ----- | ------------------------------------- |
Accreditation Program
|     | SCAPVal  | SCAP Content Validation Tool         |
| --- | -------- | ------------------------------------ |
|     | SCMG     |  Security Components and Mechanisms  |
OCIL  Open Checklist Interactive Language
Group
OCR   Office for Civil Rights
|     | SCORE  |  Special Cyber Operations Research and  |
| --- | ------ | --------------------------------------- |
ODNI   Office of the Director of National Intelli- Engineering
gence
|     | SCRM   | Supply Chain Risk Management  |
| --- | ------ | ----------------------------- |
ODP  Open Distributed Processing
|     | SDO  | Standards Developing Organizations  |
| --- | ---- | ----------------------------------- |
OMB   Office of Management and Budget
|     | SEW  | Social, Economic, and Workforce  |
| --- | ---- | -------------------------------- |
1 0 3
ACRONYMS  |  FY 2014

SGCC Smart Grid Cybersecurity Committee VPN Virtual private network
SGIP Smart Grid Interoperability Panel VRDX-SIG Vulnerability Reporting and Data eXchange
SIG
SHS Secure Hash Standard
VVSG Voluntary Voting System Guidelines
SIG Special Interest Groups
SLC Simulated Logic Circuit
Wi-Fi Wireless Fidelity
SMBs Small and medium-size businesses
SNIA Storage Networking Industry Association
XACML eXtensible Access Control Markup
SOIG Security Outreach and Integration Group
Language
SP Special Publications
XCCDF Extensible Configuration Checklist
SRA Security Reference Architecture
Description Format
SSAG Secure Systems and Applications Group
XML Extensible Markup Language
SSP Sensitive Security Parameters
STIG Security Technical Implementation Guide
STVMG Security Testing, Validation, and Measure-
ment Group
SWGDE Scientific Working Group on Digital Evi-
dence
SWID Software identification
TAG Technical Advisory Group
TCG Trusted Computing Group
TDEA Triple Data Encryption Algorithm
TGDC Technical Guidelines Development
Committee
TIAA Travel Industry Association of America
TLS Transport Layer Security
TMSAD Trust Model for Security Automation Data
TNC Trusted Network Connect
TS Technical Specification
UOCAVA Uniformed and Overseas Citizens Voting
Act
USG U.S. Government
USGCB United States Government Configuration
Baseline
USNC United States National Committee
VCI Virtual Contact Interface
VMs Virtual Machines
1 0 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014

OPPORTUNITIES TO ENGAGE
WITH CSD AND NIST
1 0 5

OPPORTUNITIES TO ENGAGE
WITH CSD AND NIST

| Guest Research Internships at NIST |     |     |     | Security Research |     |     |     |
| ---------------------------------- | --- | --- | --- | ----------------- | --- | --- | --- |
Opportunities are available at NIST for 6- to 24-month  NIST occasionally undertakes security work, primarily
internships within CSD. Qualified individuals should contact  in the area of research, funded by other agencies. Such
CSD, provide a statement of qualifications, and indicate the  sponsored  work  is  accepted  by  NIST  when  it  can  cost
area of work that is of interest. The salary costs are generally  effectively further the goals of NIST and the sponsoring
| borne by the sponsoring institution; however, in some cases,  |                        |                  |          | institution.  |     |     |     |
| ------------------------------------------------------------- | ---------------------- | ---------------- | -------- | ------------- | --- | --- | --- |
| these  guest                                                  | research  internships  | carry  a  small  | monthly  |               |     |     |     |
For further information, contact:
stipend paid by NIST.
Mr. Matthew Scholl
For further information, contact:
(301) 975-2941
| Mr. Matthew Scholl  |     |     |     | matthew.scholl@nist.gov |     |     |     |
| ------------------- | --- | --- | --- | ----------------------- | --- | --- | --- |
(301) 975-2941
matthew.scholl@nist.gov
Funding Opportunities at NIST
|     |     |     |     | NIST  funds  | industrial  and  | academic  research  | in  a  |
| --- | --- | --- | --- | ------------ | ---------------- | ------------------- | ------ |
Details at NIST for Government or  variety of ways. The Small Business Innovation Research
Military Personnel Program funds R&D proposals from small businesses; see
Opportunities are available at NIST for 6- to 24-month  www.nist.gov/sbir. CSD also offers other grants to encourage
details at NIST in CSD. Qualified individuals should contact  work in specific fields: precision measurement, fire research,
CSD, provide a statement of qualifications, and indicate the  and materials science. Grants/awards supporting research at
area of work that is of interest. Generally speaking, salary  industry, academia, and other institutions are available on a
costs are borne by the sponsoring agency; however, in some  competitive basis through several different Institute offices.
cases, agency salary costs may be reimbursed by NIST.  For general information on NIST grants programs, please
| For further information, contact: |     |     |     | contact:                    |     |     |     |
| --------------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- |
| Mr. Matthew Scholl                |     |     |     | Mr. Christopher Hunton      |     |     |     |
| (301) 975-2941                    |     |     |     | (301) 975-5718              |     |     |     |
| matthew.scholl@nist.gov           |     |     |     | christopher.hunton@nist.gov |     |     |     |
Funding opportunity information:
Federal Computer Security Program
http://www.nist.gov/director/grants/grants.cfm
Managers’ Forum (FCSPM)
The FCSPM Forum is covered in detail in the Outreach
section of this report. Membership is free and open to federal
employees.
For further information, contact:
Mr. Kevin Stine
(301) 975-4483
kevin.stine@nist.gov or sec-forum@nist.gov
Visit the FCSPM Forum website:
http://csrc.nist.gov/groups/SMA/forum/membership.html
1 0 6
| COMPUTER SECURITY DIVISION ANNUAL REPORT | 2014 |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

ACKNOWLEDGEMENTS
The editor, Patrick O’Reilly of the Computer Security
Division, wishes to thank his colleagues in the Computer Security
Division, who provided write-ups on their 2014 project highlights
and accomplishments for this annual report (their names are
mentioned after each project write-up). The editor would also
like to acknowledge Elaine Barker, Lisa Carnahan, Kevin Stine, Jim
Foti (NIST); Greg Witte and Larry Feldman (G2) for reviewing and
providing valuable feedback for this annual report.
The editor would also like to acknowledge Kristen Dill of Dill and
Company, Inc. for designing the cover and inside layout for the 2014
annual report.
TRADEMARK INFORMATION
All names are trademarks or registered trademarks of their
respective owners.
1 07
ACKNOWLEDGEMENTS | FY 2014

THIS PAGE INTENTIONALLY LEFT BLANK

THIS PAGE INTENTIONALLY LEFT BLANK

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-25", "model": "gemini-3.5-flash-lite"} -->
