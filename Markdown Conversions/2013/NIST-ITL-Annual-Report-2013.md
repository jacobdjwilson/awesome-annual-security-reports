# NIST Special Publication 800-170: Computer Security Division 2013 Annual Report

## Table of Contents
- [Welcome Letter](#welcome-letter)
- [Computer Security Division (CSD) Management Team](#computer-security-division-csd-management-team)
- [Computer Security Division Organization](#computer-security-division-organization)
  - [Cryptographic Technology Group (CTG)](#cryptographic-technology-group-ctg)
  - [Security Components and Mechanisms Group (SCMG)](#security-components-and-mechanisms-group-scmg)
  - [Secure Systems and Applications Group (SSAG)](#secure-systems-and-applications-group-ssag)
  - [Security Outreach and Integration Group (SOIG)](#security-outreach-and-integration-group-soig)
  - [Security Testing, Validation, and Measurement Group (STVMG)](#security-testing-validation-and-measurement-group-stvmg)
- [The Computer Security Division Implements the Federal Information Security Management Act](#the-computer-security-division-implements-the-federal-information-security-management-act)
- [Program and Project Achievements for Fiscal Year 2013](#program-and-project-achievements-for-fiscal-year-2013)
  - [NIST Responsibilities Under Executive Order 13636, “Improving Critical Infrastructure Cybersecurity”](#nist-responsibilities-under-executive-order-13636-improving-critical-infrastructure-cybersecurity)
  - [Contributions to National and International Standards Development](#contributions-to-national-and-international-standards-development)
  - [Identity Management Standards within INCITS B10 and ISO JTC1/SC 17](#identity-management-standards-within-incits-b10-and-iso-jtc1sc-17)
  - [Federal Information Security Management Act (FISMA) Implementation Project](#federal-information-security-management-act-fisma-implementation-project)

---

# NIST Special Publication 800-170
## Computer Security Division
### 2013 Annual Report

**Patrick O’Reilly**, Editor  
Computer Security Division  
Information Technology Laboratory  
National Institute of Standards and Technology  

**Co-Editors:**  
- Chris Johnson (G2, Inc.)  
- Doug Rike (G2, Inc.)  
- Greg Witte (G2, Inc.)  
- Lorie Richards (Facilities Services Division, Creative and Printing Service)  

This publication is available free of charge from [http://dx.doi.org/10.6028/NIST.SP.800-170](http://dx.doi.org/10.6028/NIST.SP.800-170)  
**June 2014**  

**U.S. Department of Commerce**  
Penny S. Pritzker, Secretary  

**National Institute of Standards and Technology**  
Dr. Willie E. May, Under Secretary of Commerce for Standards and Technology and Acting Director  

> **Disclaimer:** Any mention of commercial products is for information only; it does not imply NIST recommendation or endorsement, nor does it imply that the products mentioned are necessarily the best available for the purpose.  
> National Institute of Standards and Technology Special Publication 800-170 Natl. Inst. Stand. Technol. Spec. Pub., 93 pages (June 2014) CODEN: NSPUE2  

ii  
Computer Security Division Annual Report - 2013  

---

## Welcome Letter

The Computer Security Division (CSD), a component of the Information Technology Laboratory at the National Institute of Standards and Technology (NIST) is responsible for developing standards, guidelines, tests, and metrics for protection of non-national security federal information systems. 

NIST standards and guidelines are developed in an open and transparent manner that enlists broad industry and academia expertise from around the world. While developed for federal agency use, these resources are voluntarily adopted by other organizations because they are effective and accepted throughout the world.

The need for cybersecurity standards and best practices that address interoperability, usability and privacy continues to be critical for the Nation. In Fiscal Year (FY) 2013, CSD continued to align its resources to enable greater development and application of practical, innovative security technologies and methodologies that enhance our ability to address current and future computer and information security challenges. Our foundational research and applied cybersecurity programs continue to advance in many areas including cryptography; identity and access management; cloud, virtualization, and mobile technologies; and advanced security testing and measurement.

Strong partnerships with diverse stakeholders are vital to the success of our technical programs. In February 2013, the President issued Executive Order 13636 that directed NIST to work collaboratively with industry to develop a voluntary framework - based on existing standards, guidelines, and practices - to improve critical infrastructure cybersecurity practices. NIST held several workshops, meetings, webinars, and informal sessions to gather feedback with the goals of generating content for the framework and discuss several topics that help inform and guide NIST in this effort. In August 2013, we produced a discussion draft of the preliminary framework.

Working closely with standards developing organizations, industry and interagency partners, we are evolving and expanding security automation capabilities to help organizations manage and measure the security of systems and technologies. Our cybersecurity awareness, training, and education programs also exemplify the importance of these partnerships by engaging with academic institutions, federal agencies, small and medium businesses and others to increase awareness and enhance the overall cybersecurity posture of the Nation.

Active engagement with the diverse federal community continues to be critical to our success. This interaction is most prominent in our strengthened collaborations with the Department of Defense, the Intelligence Community, and the Committee on National Security Systems to establish a common foundation for information security across the federal government. Through this partnership, NIST released Special Publication (SP) 800-53 Revision 4, _Security and Privacy Controls for Federal Information Systems and Organizations_, in April 2013. This guideline provides organizations with state-of-the-practice security controls to fundamentally strengthen their systems and the environments in which those systems operate. SP 800-53 Revision 4 and other NIST standards and guidelines contribute to systems that are more resilient in the face of cyber attacks and other threats.

Late in FY 2013, news reports about leaked classified documents caused concern from the cryptographic community about the security of NIST cryptographic standards and guidelines. Recognizing community concern regarding some specific standards, we reopened the public comment period for three Special Publications to give the public a second opportunity to view and comment on the documents. This initial step will be followed by a review of our cryptographic development process and NIST cryptographic standards and guidelines in FY 2014.

For many years, CSD, in collaboration with our global partners across industry, academia, and government, has made great contributions to help secure the nation’s critical information and infrastructure. We look forward to furthering these relationships in FY 2014 as we lead the development and practical implementation of scalable and sustainable information security standards and practices in areas such as cyber-physical and industrial control systems, privacy engineering, security automation, and mobile technologies.

To participate in any CSD research areas – whether current or future – or to learn more about our programs and activities, please visit [http://csrc.nist.gov](http://csrc.nist.gov).

**Donna Dodson**  
Chief, Computer Security Division  
& Deputy Chief Cybersecurity Advisor  

1  

---

## Computer Security Division (CSD) Management Team

- **Donna Dodson**  
  Chief, Computer Security Division, Chief Cybersecurity Advisor, and Acting Executive Director, National Cybersecurity Center of Excellence
- **Matthew Scholl**  
  Acting Associate Director & Acting Deputy Chief, Computer Security Division and Cybersecurity Advisor Office, and Acting Associate Director of Operations, National Cybersecurity Center of Excellence

### Group Managers
- **Cryptographic Technology Group:** Dr. Lily Chen (Acting)
- **Security Components and Mechanisms Group:** Mr. Mark (Lee) Badger
- **Secure Systems and Applications Group:** Mr. David Ferraiolo
- **Security Outreach and Integration Group:** Mr. Kevin Stine
- **Security Testing, Validation, and Measurement Group:** Mr. Michael Cooper

2  
Computer Security Division Annual Report - 2013  

---

## Computer Security Division Organization

The Computer Security Division’s computer scientists, mathematicians, IT specialists, administrative staff and others support CSD’s mission and responsibilities through five groups that are described in the following sections:
- Cryptographic Technology Group
- Security Components and Mechanisms Group
- Secure Systems and Applications Group
- Security Outreach and Integration Group
- Security Testing, Validation, and Measurement Group

3  

### Cryptographic Technology Group (CTG)

**Mission Statement:**  
Research, develop, engineer, and standardize cryptographic algorithms, methods, and protocols.

**Overview:**  
CTG’s work in the field of cryptography includes researching, analyzing, and standardizing cryptographic technology, such as hash algorithms, symmetric and asymmetric cryptographic techniques, key management, authentication, and random number generation. CTG’s goal is to identify and promote methods to enhance trust in communications, data, and storage through cryptographic technology, encouraging innovative development and helping technology users to manage risk.

In Fiscal Year (FY) 2013, CTG continued to make an impact in the field of cryptography, both within and outside the Federal Government, by collaborating with national and international agencies, academic and research organizations, and standards bodies to develop interoperable security standards and guidelines. In addition, CTG worked with industry partners to promote the use of NIST-approved cryptographic methods.

Federal agency collaborators include the National Security Agency (NSA), the Intelligence Advanced Research Projects Activity (IARPA), the National Telecommunications and Information Administration (NTIA), the National Strategy for Trusted Identities in Cyberspace (NSTIC), General Services Administration (GSA), the United States Postal Service (USPS), and the Election Assistance Commission (EAC).

CTG also works closely with foreign government agencies, such as the Communications Security Establishment of Canada and Australia’s Defense Signals Agency and Centrelink. Additionally, CTG is active in national and international standards bodies, including the Accredited Standards Committee (ASC) X9 (financial industry standards), the International Organization for Standardization (ISO), the Institute of Electrical and Electronics Engineers (IEEE), the Internet Engineering Task Force (IETF), the American National Standards Institute (ANSI), and the Trusted Computing Group (TCG). Industry collaborators include Intel, Microsoft, and Cisco.

Academic collaborators include Carnegie Mellon University, Yale University, University of Southern Denmark, the University of Milan, Malaga University, and the University of Lisbon. Research organizations include the Information-technology Promotion Agency (IPA)/Cryptography Research and Evaluation Committees (CRYPTREC) and the Ministry of Economy, Trade and Industry (METI) of Japan.

**Group Manager (Acting):**  
Dr. Lily Chen  
(301) 975-6974  
lily.chen@nist.gov  

---

### Security Components and Mechanisms Group (SCMG)

**Mission Statement:**  
Research, develop, and standardize foundational security mechanisms, protocols, and services.

**Overview:**  
The SCMG’s security research focuses on the development and management of foundational building-block security mechanisms and techniques that can be integrated into a wide variety of mission-critical U.S. information systems. The group’s work spans the spectrum from near-term hardening and improvement to the design and analysis of next-generation, leap-ahead security capabilities. Computer security depends fundamentally on the level of trust for computer software and systems. This work, therefore, focuses strongly on assurance building activities ranging from the analysis of software configuration settings to advanced trust architectures to testing tools that surface flaws in software modules. This work also focuses significantly on increasing the applicability and effectiveness of automated techniques, wherever feasible.

The SCMG conducts collaborative research with government, industry, and academia. Outputs of this research consist of prototype systems, software tools, demonstrations, NIST Special Publications (SP), NIST Interagency or Internal Reports (NISTIR), and conference and journal papers.

SCMG works on a variety of topics, such as specifications for the automated exchange of security information between systems, computer security incident handling guidelines, formulation of high-assurance software configuration settings, hardware roots of trust for mobile devices, secure Basic Input Output System (BIOS) layers, combinatorial testing techniques, conformity assessment of software implementing biometric standards, and adoption of Internet Protocol Version 6 and Internet Protocol security extensions. SCMG collaborates extensively with government, academia, and the private sector.

In FY 2013, collaborations have included Carnegie Mellon University (test development environment), Johns Hopkins Applied Physics Lab (practical application of combinatorial coverage measurement tool), North Carolina State University (access control policy testing), University of North Texas and University of Maryland-Baltimore County (test prioritization algorithms), University of Texas at Arlington (covering array generation algorithm), Mexico’s Centro Nacional de Metrología (constraints for testing coverage tool), National Aeronautics and Space Administration (NASA) (practical application for combinatorial coverage measurement), U.S. Air Force Test and Evaluation (a new event sequence testing method), the National Security Agency (secure software tool chain competition development), and the Department of Homeland Security (incident coordination).

SCMG accomplishments include the Advanced Combinatorial Testing System (ACTS) software and documentation, the NIST BioCTS 2013 biometric conformance testing tool and test assertions, and a security log analysis tool.

**Group Manager:**  
Mr. Mark (Lee) Badger  
(301) 975-3176  
mark.badger@nist.gov  

---

### Secure Systems and Applications Group (SSAG)

**Mission Statement:**  
Integrate and apply security technologies, standards, and guidelines for computing platforms and information systems.

**Overview:**  
SSAG’s security research focuses on the identification of emerging and high-priority technologies and on the development of security solutions that will enhance the security of U.S. critical information infrastructure. The group conducts research and development on behalf of government and industry from the earliest stages of technology development through proof-of-concept, reference and prototype implementations, and demonstrations. SSAG works to transfer new technologies to industry; to produce new standards and guidance for federal agencies and industry; and to develop tests, test methodologies, and assurance methods.

SSAG investigates topics such as mobile device security, cloud computing and virtualization, identity management, access control and authorization management, and software assurance. SSAG research helps federal agencies meet information security requirements that might not be fully addressed by existing technology. The group collaborates extensively with government, academia, and private sector entities.

Example successes from this work include tools for access control policy testing, new concepts in access control and policy enforcement, methods for achieving comprehensive policy enforcement and data interoperability across enterprise data services, and test methods for mobile device (smart phone) application security. For example, the SSAG Mobile Application Testing Portal (ATP) went operational for military use (known in the U.S. Army as PANTHR) and is in the process of transitioning to other federal agencies as open source. In support of the Federal Government’s cloud computing initiatives, SSAG led the NIST Security Working Group that published the *NIST Cloud Computing - Security Reference Architecture*. The SSAG also completed revision of Federal Information Processing Standard (FIPS) 201-2, *Personal Identity Verification (PIV) of Federal Employees and Contractors*, which was approved by the Secretary of Commerce and published in September of 2013.

To improve access to new technologies, SSAG chaired, edited, and participated in the development of a wide variety of national and international security standards.

**Group Manager:**  
Mr. David Ferraiolo  
(301) 975-3046  
david.ferraiolo@nist.gov  

---

### Security Outreach and Integration Group (SOIG)

**Mission Statement:**  
Develop, integrate, and promote the mission-specific application of information security standards, guidelines, best practices, and technologies.

**Overview:**  
The U.S. economy, citizens, and government rely on information technology (IT); so the protection of IT and information infrastructure is critical. SOIG leverages broad cybersecurity and risk management expertise to develop, integrate, and promote security standards, guidelines, tools, technologies, methodologies, tests, and measurements to address cybersecurity needs in many areas of national and international importance.

The SOIG collaborates with stakeholders to address cybersecurity considerations in many diverse program areas, including the Information and Communications Technologies (ICT) supply chain, Smart Grid, Electronic Voting, Health Information Technology, and Cyber Physical and Industrial Control Systems. The group continues to increase its efforts to research, develop, and align cybersecurity standards, practices, and testing methods necessary to foster interoperable and secure public safety communications. In our Federal Information Security Management Act (FISMA) implementation program, the group produces standards and guidelines to help federal agencies build strong cybersecurity risk management programs.

In each of these program areas, the group extends outreach to stakeholders across federal, state, and local governments; industry; academia; small businesses; and the public. The SOIG also leads several broad cybersecurity awareness, training, education, and outreach efforts, including the National Initiative for Cybersecurity Education (NICE), the Small- and Medium-Sized Business (SMB) outreach program, the Federal Computer Security Managers’ Forum, and the Federal Information Systems Security Educators’ Association (FISSEA).

Key to the group’s success is the ability to interact with a broad constituency to ensure that SOIG’s program is consistent with national objectives related to or impacted by information security. Through open and transparent public engagement, collaboration, and cooperation, the group works to address critical cybersecurity challenges, enable greater U.S. industrial competitiveness, and facilitate practical implementation of scalable and sustainable information security standards and practices.

**Group Manager:**  
Mr. Kevin Stine  
(301) 975-4483  
kevin.stine@nist.gov  

---

### Security Testing, Validation, and Measurement Group (STVMG)

**Mission Statement:**  
Advance information security testing, measurement science, and conformance.

**Overview:**  
Federal agencies, industry, and the public rely on cryptography for the protection of information and communications used in electronic commerce, critical infrastructure, and other application areas. The STVMG supports testing and validation of underlying cryptographic modules and cryptographic algorithms in consideration of established standards. These cryptographic modules and algorithms enable products and systems to provide security services, such as confidentiality, integrity, and authentication. Although cryptography provides security, poor designs or weak algorithms can render a product insecure and place highly sensitive information at risk. When protecting sensitive data, Federal Government agencies require a minimum level of assurance that cryptographic products meet established security requirements and use only tested and validated cryptographic modules.

STVMG’s testing-focused activities include validating cryptographic algorithm implementations, cryptographic modules, and Security Content Automation Protocol (SCAP)-compliant products; developing test suites and test methods; providing implementation guidance and technical support to industry forums; and conducting education, training, and outreach programs.

STVMG’s validation programs work together with independent Cryptographic and Security Testing laboratories that are accredited by the NIST National Voluntary Laboratory Accreditation Program (NVLAP). Based on the independent laboratory test report and test evidence, the Validation Program then validates the implementation under test. NIST publishes, through public websites, lists of validations awarded.

**Group Manager:**  
Mr. Michael Cooper  
(301) 975-8077  
michael.cooper@nist.gov  

---

## The Computer Security Division Implements the Federal Information Security Management Act

The E-Government Act, Public Law 107-347, passed by the 107th Congress and signed into law by the President in December 2002, recognized the importance of information security to the economic and national security interests of the United States. Title III of the E-Government Act, entitled the Federal Information Security Management Act (FISMA) of 2002, included duties and responsibilities for the National Institute of Standards and Technology, Information Technology Laboratory, Computer Security Division (CSD). In 2013, CSD addressed its assignments through the following activities:

- **Issued two final Federal Information Processing Standards (FIPS):** FIPS 186-4, _Digital Signature Standard (DSS)_, which specifies a suite of algorithms that can be used to generate digital signatures, and FIPS 201-2, _Personal Identity Verification (PIV) of Federal Employees and Contractors_, which specifies the architecture and technical requirements for a common identification standard for Federal employees and contractors.

- **Issued 25 draft and final NIST Special Publications (SP)** that provide management, operational, and technical security guidelines in areas such as personal identity verification, cryptographic key generation, cryptographic key management systems, random bit generators, transport layer security, mobile devices and mobile device forensics, hardware-rooted security in mobile devices, malware incident prevention and handling for desktops and laptops, industrial control systems security, e-authentication, security and privacy controls for federal information systems and organizations, patch management technologies, attribute based access control, and supply chain risk management practices.

- **Issued 13 draft and final NIST Interagency or Internal Reports (NISTIR)** on a variety of topics, including cryptographic key management issues and challenges in cloud services, cybersecurity in cyber-physical systems, the SHA-3 cryptographic hash algorithm competition, combinatorial coverage measurement, credential reliability and revocation model for federated identities, security automation, reference certificate policy, trusted geolocation in the cloud, and a glossary of key information security terms.

- **Performed research and conducted outreach** on standards, practices, and technologies to enable prompt and effective computer security incident handling and coordination.

- **Continued the successful collaboration** with the Office of the Director of National Intelligence (ODNI), the Committee on National Security Systems (CNSS), and the Department of Defense (DOD) to establish a common foundation for information security across the Federal Government, including a structured, yet flexible approach for managing information security risk across an organization. In 2013, this collaboration produced updated guidelines for selecting and specifying security controls, and an updated catalog of security and privacy controls for federal information systems and organizations.

- **Provided assistance to agencies and the private sector** through many outreach efforts associated with the Federal Information Systems Security Educators’ Association (FISSEA), the Federal Computer Security Managers’ Forum, the National Initiative for Cybersecurity Education (NICE), and the Small Business Information Security Corner.

- **Conducted workshops, awareness briefings, and outreach** to CSD customers to ensure comprehension of standards and guidelines, to share ongoing and planned activities, and to aid in scoping guidelines in a collaborative, open, and transparent manner. CSD public workshops addressed a diverse range of information security and technology topics, including cloud and mobile technologies, voting systems security, cyber physical systems, improving trust in the online marketplace, safeguarding health information, attribute based access control, supply chain risk management, improving critical infrastructure cybersecurity, and broad computer security awareness, training, and education forums and events.

- **Engaged with international standards bodies** in a variety of areas, including promoting broader international adoption of security automation specifications. Additionally, NIST continued to lead, in conjunction with the Government of Canada’s Communications Security Establishment, the Cryptographic Module Validation Program (CMVP). The Common Criteria Evaluation and Validation Scheme (CCEVS) and CMVP facilitate security testing of IT products usable by the Federal Government.

- **Solicited recommendations** of the Information Security and Privacy Advisory Board (ISPAB) on draft standards and guidelines, and on information security and privacy issues.

- **Produced the CSD 2013 annual report** and released it as a NIST SP. CSD annual reports from fiscal years 2003 through 2013 are available on the Computer Security Resource Center (CSRC) at [http://csrc.nist.gov/publications/PubsTC.html#Annual Reports](http://csrc.nist.gov/publications/PubsTC.html#Annual Reports).

8  
Computer Security Division Annual Report - 2013  

---

## Program and Project Achievements for Fiscal Year 2013

In FY 2013, CSD continued to research and develop guidance for a broad array of technical areas, including supply chain risk management; security analytics; cloud, mobile, and privacy-enhancing technologies; hardware-enabled security; and cyber-physical and embedded systems. The staff and guest researchers within CSD have collaborated with global partners from government, industry, and academia, making significant contributions to help secure critical information and infrastructure. The following sections describe CSD’s programs and project achievements that include extensive research and development for high-quality, cost-effective security and privacy mechanisms, standards, guidelines, tests, and metrics that address current and future computer and information security challenges.

### NIST Responsibilities Under Executive Order 13636, “Improving Critical Infrastructure Cybersecurity”

Recognizing that the national and economic security of the United States depends on the reliable functioning of critical infrastructure, the President issued Executive Order (EO) 13636, *Improving Critical Infrastructure Cybersecurity*, in February 2013. This Executive Order directed NIST to work with stakeholders to develop a voluntary framework – based on existing standards, guidelines, and practices − for reducing cybersecurity risks to critical infrastructure.

The Cybersecurity Framework will provide a prioritized, flexible, repeatable, performance-based, and cost-effective approach, including information security measures and controls to help owners and operators of critical infrastructure and other interested entities to identify, assess, and manage cybersecurity-related risk while protecting business confidentiality, individual privacy, and civil liberties. To enable technical innovation and account for organizational differences, the Cybersecurity Framework will not prescribe particular technological solutions or specifications.

In FY 2013, NIST worked with a diverse stakeholder community to develop the Framework through an open public process. This process included:
- Issuing a Request for Information (RFI) in the Federal Register in February 2013
- Conducting five open workshops to provide the public with additional opportunities to provide input. These workshops were hosted at the Department of Commerce in Washington, D.C. (April 2013), Carnegie Mellon University in Pittsburgh, Pennsylvania (May 2013), the University of California, San Diego (July 2013), the University of Texas at Dallas (September 2013), and the North Carolina State University in Raleigh, North Carolina (November 2013)
- Preparing a Preliminary Cybersecurity Framework for official public review and comment

In FY 2014, NIST will continue to conduct stakeholder outreach and will work collaboratively to further develop and issue the Cybersecurity Framework. NIST will initiate a 45-day public comment period on the Preliminary Cybersecurity Framework, review and adjudicate all public comments received, and issue a final Cybersecurity Framework (version 1.0) in February 2014 as specified in the Executive Order.

[http://www.nist.gov/cyberframework](http://www.nist.gov/cyberframework)

**Contacts:**  
Mr. Kevin Stine  
(301) 975-4483  
kevin.stine@nist.gov  

Mr. Adam Sedgewick  
(301) 367-4678  
adam.sedgewick@nist.gov  

---

### Contributions to National and International Standards Development

Figure 1 (below) shows many of the national and international Standards Developing Organizations (SDOs) involved in cybersecurity standardization. CSD participates in cybersecurity standards activities in many of these organizations, either in leadership positions or as editors and contributors. Many of CSD’s publications have been the basis for both national and international standards projects. This section discusses CSD standards activities in conjunction with InterNational Committee for Information Technology Standards (INCITS) Technical Committee Cyber Security 1 (CS1), where Dan Benigni serves as Chair and U.S. Head of Delegation to subcommittee SC 27, and Sal Francomacaro serves as CS1 Vice Chair.

![Cybersecurity Standards Development Organizations (SDO) ecosystem diagram showing interactions between national and international bodies]

*Figure 1: Cybersecurity Standards Development Organizations (SDOs)*

11  
Program and Project Achievements for FY 2013

#### The International Organization for Standardization (ISO)
The International Organization for Standardization (ISO) is a network of the national standards institutes of 148 countries, with the representation of one member per country. The scope of ISO covers standardization in all fields except electrical and electronic engineering standards, which are the responsibility of the International Electrotechnical Commission (IEC).

The IEC prepares and publishes international standards for all electrical, electronic, and related technologies, including electronics, magnetics and electromagnetics, electroacoustics, multimedia, telecommunication, and energy production and distribution, as well as associated general disciplines such as terminology and symbols, electromagnetic compatibility, measurement and performance, dependability, design and development, safety, and the environment.

Joint Technical Committee 1 (JTC 1) was formed by ISO and IEC to be responsible for international standardization in the field of information technology. It develops, maintains, promotes, and facilitates IT standards required by global markets, meeting business and user requirements concerning:
- Design and development of IT systems and tools
- Performance and quality of IT products and systems
- Security of IT systems and information
- Portability of application programs
- Interoperability of IT products and systems
- Unified tools and environments
- Harmonized IT vocabulary
- User-friendly and ergonomically designed user interfaces

JTC 1 consists of a number of subcommittees (SCs) and working groups that address specific technologies. SCs that produce standards relating to IT security include:
- SC 06 − Telecommunications and Information Exchange Between Systems
- SC 17 − Cards and Personal Identification
- SC 27 − IT Security Techniques
- SC 37 – Biometrics

JTC 1 also has:
- Technical Committee 68 – Financial Services
  - SC 2 − Operations and Procedures including Security
  - SC 4 – Securities
  - SC 6 − Financial Transaction Cards, Related Media, and Operations
- SC 7 – Software and Systems Engineering

#### The American National Standards Institute (ANSI)
ANSI is a private, nonprofit organization (501(c)(3)) that administers and coordinates the U.S. voluntary standardization and conformity assessment system and facilitates the development of American National Standards (ANS) by accrediting the procedures of SDOs.

ANSI promotes the use of U.S. standards internationally, advocates U.S. policy and technical positions in international and regional standards organizations, and encourages the adoption of international standards as national standards where they meet the needs of the user community. ANSI is the sole U.S. representative and dues-paying member of the two major non-treaty international standards organizations, ISO and, via the United States National Committee (USNC), the IEC.

INCITS is accredited by ANSI and serves as the ANSI Technical Advisory Group (TAG) for ISO/IEC Joint Technical Committee 1. INCITS is sponsored by the Information Technology Industry (ITI) Council, a trade association representing the leading U.S. providers of information technology products and services. INCITS is organized into Technical Committees that focus on the creation of standards for different technology areas. Technical committees that focus on IT security and IT security-related technologies or that may require separate security standards include:
- B10 – Identification Cards and Related Devices
- CS1 – Cyber Security (Dan Benigni, NIST, Chair; Sal Francomacaro, NIST, Vice Chair; and Richard Kissel, NIST, Principal voting member)
- E22 – Item Authentication
- M1 – Biometrics (Fernando Podio, NIST, Chair)
- T3 – Open Distributed Processing (ODP)
- T6 – Radio Frequency Identification (RFID) Technology
- GIT1 – Governance of IT
- DAPS38 – Distributed Application Platforms and Services

As a technical committee of INCITS, CS1 develops United States, national, ANSI-accredited standards in the area of cybersecurity. Its scope encompasses:
- Management of information security and systems
- Management of third-party information security service providers
- Intrusion detection
- Network security
- Cloud computing security
- Supply chain risk management
- Incident handling
- IT security evaluation and assurance
- Security assessment of operational systems
- Security requirements for cryptographic modules
- Protection profiles
- Role-based access control
- Security checklists
- Security metrics
- Cryptographic and non-cryptographic techniques and mechanisms, including confidentiality, entity authentication, non-repudiation, key management, data integrity, message authentication, hash functions, and digital signatures
- Future service and applications standards supporting the implementation of control objectives and controls as defined in ISO 27001, in the areas of business continuity and outsourcing
- Identity management, including identity management framework, role-based access control, and single sign-on
- Privacy technologies, including privacy framework, privacy reference architecture, privacy infrastructure, anonymity and credentials, and specific privacy-enhancing technologies

The scope of CS1 explicitly excludes the areas of work on cybersecurity standardization presently under way in INCITS B10, M1, T3, T10, and T11, as well as other standard groups, such as the Alliance for Telecommunications Industry Solutions (ATIS), the Institute of Electrical and Electronics Engineers, Inc. (IEEE), the Internet Engineering Task Force (IETF), the Travel Industry Association of America (TIAA), and the Accredited Standards Committee (ASC) X9. The CS1 scope of work includes standardization in most of the same cybersecurity areas as are covered in the NIST CSD.

As the U.S. TAG to ISO/IEC JTC 1/SC 27, CS1 contributes to the SC 27 program of work on IT Security Techniques in terms of U.S. comments and contributions on SC 27 standards projects; votes on SC 27 standards documents at various stages of development; and nominates U.S. experts to work on various SC 27 projects as editors, coeditors, or in other SC 27 leadership positions. Currently, over a dozen CS1 members are serving as SC 27 document editors or coeditors on various standards projects, including CSD staff Randy Easter and Richard Kissel. All input from CS1 is processed through INCITS to ANSI, then to SC 27. CS1 also serves as a conduit for getting U.S.-based new work item proposals and U.S.-developed national standards into the international SC 27 standards development process. In its international efforts, CS1 responded to all calls for U.S. contributions and/or voting positions on all international security standards projects in ISO/IEC JTC1 SC 27 in a consistent, efficient, and timely manner.

NIST contributes to many of CS1’s national and international IT security standards efforts through its membership on CS1, where Dan Benigni serves as the non-voting chair and Richard Kissel as the NIST Principal voting member. Internationally, there are over 100 published standards, and almost all have been adopted as U.S. national standards. There are more than 80 current international standards projects. During FY 2013, 29 new standards were published in SC 27, and most of them have been recommended by CS1 for adoption as U.S. national standards.

#### CSD Contributions to Cybersecurity Standardization in INCITS CS1
CSD’s cybersecurity research also plays a direct role in the Cybersecurity Standardization efforts of CS1 at the national level. Nationally during FY 2013:

- The NIST Policy Machine research and development has resulted in three ongoing national standards projects in CS1, each in the early stages of development. They include:
  - **INCITS 499-2013**, “Next Generation Access Control –Functional Architecture (NGAC-FA)”, David Ferraiolo, NIST, Editor, Published May 2013
  - “Next Generation Access Control – Generic Operations & Abstract Data Structures (NGAC-GOADS)”, Project Number: 2195-D, Serban Gavrila, NIST, Editor (Planned Publication FY 2014)
  - “Next Generation Access Control-Implementation Requirements, Protocols and API Definitions (NGAC-IRPADS)”, Project Number: 2193-D

Within CS1, liaisons are maintained with nearly 20 organizations, including:
- ABA Federated Identity Management Legal (IdM Legal) Task Force
- American Bar Association (ABA), section on Science and Technology
- Cloud Security Alliance
- Forum of Incident Response and Security Teams (FIRST)
- IEEE P1700 and P1619
- INCITS T11, M1, GIT1, DAPS38, and PL22
- Internet Security Alliance
- Kantara Initiative Identity Assurance Working Group (IAWG)
- Open Group
- SC 7 TAG 3
- Scientific Working Group on Digital Evidence (SWGDE)
- The Storage Networking Industry Association (SNIA)
- Trusted Computing Group

Dan Benigni also serves as cybersecurity standards coordinator in CSD.

**Contact:**  
Mr. Daniel Benigni  
(301) 975-3279  
benigni@nist.gov  

---

### Identity Management Standards within INCITS B10 and ISO JTC1/SC 17

CSD supports identity management standardization activities through participation in national and international standards bodies and organizations. CSD actively participates in the INCITS B10 committee, which is focused on interoperability of Identification Cards and Related Devices. CSD staff serves as Chair and Vice Chair of the B10.12 committee, which develops interoperable standards for Integrated Circuit Cards with Contacts. CSD staff also serves as the U.S. Head of delegation to ISO/IEC JTC1 SC 17 Working Groups 4 and 11.

In addition to chairing the B10.12 committee, CSD provides technical and editorial support in the development of national and international standards. Specifically, CSD staff serves as the technical editor of ANSI 504-1, Generic Identity Set (GICS). GICS enables PIV, PIV-Interoperable (PIV-I) and Common Access Card (CAC) card applications, and others, to be built from a single platform. GICS defines an open platform where identity applications can be instantiated, deployed, and used in an interoperable way between the credential issuers and credential users. CSD staff also provides significant input to standards of major interest to U.S. government agencies and U.S. markets. CSD influences the development and revision of ISO/IEC 7816 (Identification Cards, Integrated Circuit Cards), ISO/IEC 24727 (Identification Cards, Integrated Circuit Card Programming Interfaces), and ISO/IEC 24787 (Biometrics “Match On Card” Comparison).

During FY 2013, INCITS 504 Parts 1, 2, and 4 were published and ISO/IEC 7816 Part 4 was published with significant changes added per NIST’s request. CSD provides contributions and feedback on many other INCITS B10 identity management standards projects.

During the FY 2014, the INCITS B10 committee, along with the active collaboration of CSD staff, plans to publish Part 3 of INCITS 504 and contribute to the publication of several standards of the ISO/IEC 7816 family (all relevant to FIPS 201 specifications). CSD staff will continue actively supporting relevant ID management standard initiatives.

CSD’s investment in these activities is motivated by new technical ideas that emerge from these standards. For example, INCITS 504 is an ID platform that leverages the FIPS 201 infrastructure to support a larger number of government and enterprise initiatives. In particular, INCITS 504 aims to support initiatives such as the NSTIC. ISO/IEC 24727 aims to create an interoperability framework that increases the resilience and scalability of identity management solutions and fosters domestic and international interoperability.

**Contact:**  
Mr. Salvatore Francomacaro  
(301) 975-6414  
salvatore.francomacaro@nist.gov  

---

### Federal Information Security Management Act (FISMA) Implementation Project

The FISMA Implementation Project focuses on:
- Developing a comprehensive series of standards and guidelines to help federal agencies build strong cybersecurity programs, defend against increasingly sophisticated cyber attacks, and demonstrate compliance to security requirements set forth in legislation, Executive Orders, Homeland Security Command Directives, and Office of Management and Budget (OMB) policies
- Building common understanding and reference guides for organizations applying the NIST suite of standards and guidelines that support the NIST Risk Management Framework (RMF)
- Developing minimum criteria and guidelines for recognizing security assessment organization providers as capable of assessing information systems consistent with NIST standards and guidelines supporting the RMF
- Conducting FISMA outreach to public and private sector organizations

During 2013, CSD strengthened its collaboration with the Department of Defense (DoD), the Intelligence Community, and the Committee on National Security Systems (CNSS), in partnership with the Joint Task Force Transformation Initiative, which continues to develop key cybersecurity guidelines for protecting federal information and information systems the Unified Information Security Framework. Previously, the Joint Task Force developed common security guidance in the critical areas of security controls for information systems and organizations, security assessment procedures to demonstrate security control effectiveness, security authorizations for risk acceptance decisions, and continuous monitoring activities to ensure that decision makers receive the most up-to-date information on the security state of their information systems. In addition, CSD worked with the General Services Administration (GSA) Federal Risk and Authorization Management Program (FedRAMP) to identify security assessment requirements, and prototype a process for approving Third-Party Assessment Organizations (3PAOs) that demonstrate capability in assessing conformance to NIST standards and guidelines.

![Generic Risk Model with Key Risk Factors diagram showing relationships between Threat Sources, Threat Events, Vulnerabilities, Impacts, and Likelihoods]

*Figure 2: Generic Risk Model with Key Risk Factors*

In FY 2013, CSD worked on the following three initiatives:

1. **Risk Management and Risk Assessment Guidelines:** Developed a comprehensive risk assessment guideline examining the relationships among key risk factors, including threats, vulnerabilities, impact, and likelihood. Special Publication (SP) 800-53, Revision 4, *Security and Privacy Controls for Federal Information Systems and Organizations*, provides a holistic approach to information security and risk management. The publication provides organizations with security controls necessary to appropriately strengthen their information systems and the environments in which those systems operate − contributing to systems that are resilient in the face of attacks and other threats. This “Build It Right” strategy combines with a variety of security controls for “Continuous Monitoring” to give organizations near real-time information that is essential for senior leaders making ongoing risk-based decisions affecting their critical missions and business functions.

   To take advantage of the expanded set of security and privacy controls, and to give organizations greater flexibility and agility in defending their information systems, the revision introduces the concept of overlays. Overlays provide a structured approach to help organizations tailor security control baselines and develop specialized security plans for specific missions/business functions, environments of operation, and/or technologies. This specialization approach is important as the number of threat-driven controls and control enhancements in the catalog increases and organizations develop risk management strategies to address their specific protection needs within defined risk tolerances.

2. **Criteria and Guidelines for Recognizing Security Assessment Provider Organizations:** CSD updated proficiency tests and technical requirements for evaluating FedRAMP 3PAO providers’ capability to conduct security assessment of cloud-based information systems for compliance with FISMA in accordance with FedRAMP and ISO/IEC 17020 Inspection Bodies requirements. Additionally, CSD provided input to GSA requirements (including orientation and training) for private sector accreditation body of FedRAMP 3PAOs that resulted in GSA FedRAMP Program Management Office (PMO) selecting one 3PAO private sector accreditation body.

3. **FISMA Outreach Activity to Public and Private Sector Organizations:** CSD conducted cybersecurity outreach briefings and provided support to state and local governments as well as private sector organizations on topics of interest, such as effective implementation of the NIST Risk Management Framework. In addition, CSD conducted outreach activities with academic institutions, providing information on NIST’s security standards and guidelines, and exploring new areas of cybersecurity research and development.

In FY 2013, CSD completed the following outreach activities:
- Finalized SP 800-53, Revision 4
- Collaborated with the ITL Software and Systems Division and the NIST Standards Coordination Office using the International Standard ISO/IEC 17020:2008, *Conformity Assessment – Requirements for the operation of various types of bodies performing inspection*, in support of GSA in establishing a process for qualifying 3PAOs to conduct security assessments of CSPs information systems consistent with GSA requirements based on NIST standards and guidelines

In FY 2014, CSD intends to:
- Finalize SP 800-53A, Revision 4, *Guide for Assessing the Security and Privacy Controls in Federal Information Systems and Organizations*
- Finalize SP 800-60 Revision 2, *Guide for Mapping Types of Information and Information Systems to Security Categories*
- Finalize SP 800-18 Revision 2, *Guide for Developing Security Plans for Federal Information Systems and Organizations*
- Expand cybersecurity outreach to include additional state, local, and tribal governments, as well as private sector organizations and academic institutions
- Continue to support federal agencies in effective implementation of the NIST Risk Management Framework.

[http://csrc.nist.gov/sec-cert](http://csrc.nist.gov/sec-cert)

**Contacts:**  
Dr. Ron Ross  
(301) 975-5390  
ron.ross@nist.gov  

Ms. Pat Toth  
(301) 975-5140  
patricia.toth@nist.gov  

Mr. Arnold Johnson  
(301) 975-3247  
arnold.johnson@nist.gov  

Ms. Kelley Dempsey  
(301) 975-2827  
kelley.dempsey@nist.gov  

Ms. Peggy Himes  
(301) 975-2489  
peggy.himes@nist.gov

---

est Architectures (CTA)
and Conformance Test Suites (CTS) designed to test
 Developed a preliminary draft of SP 800-53A, Revision 4,
implementations of biometric standards
Guide for Assessing the Security and Privacy Controls in
Federal Information Systems and Organizations  Supporting harmonization of biometric, tokens, and
security standards
 Developed a preliminary draft of SP 800-18, Revision
16
Computer Security Division Annual Report - 2013

 Promoting biometric standards adoption In addition to previously designed CTSs (e.g., CTS for
ANSI/NIST-ITL 1-2011 [AN-2011] traditional encoding
 Promoting conformity assessment efforts
transactions and ISO/IEC biometric data interchange format
implementations), BioCTS 2013 conformance test software
To achieve these project goals, CSD continues to work in close
includes a CTS designed to test National Information Exchange
partnership with government agencies, industry partners, and
Model (NIEM) XML encoded AN-2011 implementations. The
academic institutions. CSD actively participates in a number of
functionality of this tool goes beyond the existing basic
biometric standards development projects, contributes to the
XML testing techniques, such as schema validation. CSD’s
development of biometric standards, and leads national and
project team concluded that the XML schema validation was
international biometric standards bodies. Nationally, CSD’s staff
insufficient to address full conformance testing of the AN-
leads the INCITS Technical Committee 1 (M1) – Biometrics;
2011 requirements. The team implemented over 1,200 test
international efforts include ISO JTC 1 and IEC Subcommittee
assertions beyond the schema validation (validating an XML
SC 37 - Biometrics - JTC 1/SC 37. CSD plans to continue this
file against an XSD file) for this standard, including those for
work in FY 2014.
AN-2011 Record Types 1, 4, 10, 13, 14, 15, and 17. NISTIR 7957,
During FY 2013, the development of object-oriented CTAs and
Conformance Test Architecture and Test Suite for ANSI/NIST-ITL
CTSs to test implementations of biometric standards progressed
1-2011 NIEM XML Encoded Transactions (September 2013)
at an accelerated pace. CSD developed and publicly released
and a presentation delivered at the last Biometric Consortium
two fully functional object-oriented CTAs. One CTA supports
conference discussed these test tools and provided technical
3
CTSs designed to test implementations of Extensible Markup
implementation details.
Language (XML) encoded biometric data interchange formats
BioCTS 2013 conformance test software also includes CTSs
and the other supports CTSs designed to test implementations
to test PIV profiles (e.g., finger minutia and image data formats)
of ISO/IEC data formats developed by JTC 1/SC 37 as well as
and to test implementations of the second-generation face
PIV profiles of biometric standards. CSD released these test
recognition data format developed by JTC 1/SC 37 (published
tools as “BioCTS 2013 for ANSI/NIST 1-2011” and “BioCTS
in 2011). The PIV profile of the SC 37 iris data format was
2013 for ISO/IEC” respectively. As depicted in the figure, CTA/
aligned with SP 800-76-2, Biometric Specifications for Personal
CTSs’ key features include search capabilities of the Text Log
Identity Verification. The face recognition CTS was aligned with
Outputs (very useful to debug errors in large implementations),
the associated conformance testing methodology developed by
formatted test results, and test result basic statistics (on batch
JTC 1/SC 37.
of files or individual files).
Figure 3: Biometric Conformance Test Software by NIST/ITL CSD
17
Program and Project Achievements for FY 2013

These conformance-testing tools provide significant  Keynote talks and presentations on biometric standards
functionality, usability, and performance. In addition to supplying and conformity assessment at national and international
an installer version of the CTAs, which supports new and conferences
existing CTSs with new graphical user interface enhancements,
 Related technical publications and participation in
the CSD project team extended the work to a command line
conference program committees and paper reviews
interface version for AN-2011 traditional encoding that runs
under Windows and Linux (with Mono). The test tools developed
NIST helped develop the program of the 2013 Biometric
support a Web-based environment. A prototype was developed,
Consortium Conference, which CSD’s Mr. Fernando Podio co-
tested, and demonstrated at the last Biometric Consortium
chaired. Held September 17-19, 2013, in Tampa, Florida, this
Conference.
year’s conference included nearly 1,600 attendees from 30
Based on the detailed analysis of the biometric standards countries representing government, industry, and academia.
(ISO/IEC and AN-2011) required to develop the associated
CSD supported a booth at the conference’s technical
conformance test tools, the CSD team provided technical
exposition and presented material regarding the conformance
contributions to the relevant standards bodies. In FY 2013,
test tool development project. The conference program included
these included:
sessions on Federal Government programs, advances in
 Over 200 test assertions for AN-2011 Record Type 18 – biometric technologies and standards, and Biometrics Identity
DNA Data Record and Security (BIdS) research. NIST’s session highlighted
achievements and ongoing biometric research, testing, and
 Technical contributions on the AN-2011 standard and the
standards projects. Over 140 speakers participated in the
published XML schema
program.
 Technical contributions to JTC 1/SC 37 (via INCITS M1)
ITL’s Biometric Resource Center:
on SC 37 XML namespaces, data elements, schemas,
http://www.nist.gov/biometrics
and related items; an XML-based data interchange
format framework and DNA data interchange format
BioCTS 2013 - Biometric Conformance Test Tool Downloads:
In addition to ongoing participation and management http://www.nist.gov/itl/csd/biometrics/biocta_download.
cfm#CTAdownloads
of biometric standards activities in INCITS M1 and JTC 1/
SC 37, in FY 2014, CSD plans to develop additional CTSs to
test implementations of selected international biometric Biometric Consortium website:
http://www.biometrics.org
data interchange formats specified in XML encoding (under
development in JTC 1/SC 37). The CSD team also plans to
develop conformance test assertions for selected record types Biometric Consortium 2013 conference program (released
of the 2013 version of the ANSI/NIST standard and plans presentations are linked):
http://www.biometrics.org/bc2013/program.pdf
to develop the associated CTA/CTS for traditional and XML
encoded transactions. The latest version of the ANSI/NIST
standard now incorporates extended forensics-related data,
such as a dental supplement and additional record types, such
as voice data record. The team will continue researching and
developing additional test environments support, such as web
services and tools in the cloud. The research plan expands to
technical interfaces, such as Biometric Application Programming
Interface standards specified in Object Oriented Programming Contact:
and Biometric Information Assurance Services standards. Mr. Fernando Podio
(301) 975-2947
Outreach efforts in FY 2013 in support of biometric standards
fernando.podio@nist.gov
development and conformity assessment efforts included:
 Contribution of the area editor for articles on biometric
standards for Springer’s second edition of the Biometrics
Encyclopedia (under development), where 25 papers
were reviewed and edited
18
Computer Security Division Annual Report - 2013

Cybersecurity of Cyber-Physical Systems (CPS) need to provide a common lexicon and taxonomy, a common
architectural vision to help facilitate interoperability between
Leveraging CSD’s expertise in cybersecurity for industrial elements and systems, and promotes communication across
control systems, smart grid, hardware-enabled security, the breadth of CPS stakeholders.
and embedded systems, the division is now researching
CSD, in conjunction with NIST’s Engineering Laboratory, will
cybersecurity needs of the broader landscape of cyber-
finalize the revision of SP 800-82 in FY 2014. CSD will continue
physical systems (CPS). CPS are hybrid networked cyber and
to participate in the International Society of Automation (ISA)
engineered physical elements co-designed to create adaptive
99 Committee, which develops and establishes standards,
and predictive systems that respond in real-time to enhance
recommended practices, technical reports, and related
performance with varying degrees of human interaction, and
information that define procedures for implementing
are commonly used in the nation’s critical infrastructure.
electronically secure industrial automation and control systems
Such systems control the electrical grid, provide clean water,
and security practices, and for assessing electronic security
produce chemicals, and underlie transportation systems. CPS
performance. Leveraging the initial NIST notional reference
capabilities continue to grow as a result of technological
architecture as a starting point to address the lack of an
advances, enabling future engines of growth, such as advanced
industry-wide consensus definition, reference architecture,
manufacturing, and advancements in safety initiatives, such as
and taxonomy for CPS, CSD will work in collaboration with
autonomous vehicles.
NIST’s Engineering Laboratory and ITL’s Software and Systems
Cybersecurity is an important crosscutting discipline that is division, and Advanced Networking Technologies division to
critical to safeguarding CPS and supporting communications lead a public-private working group of government, academia,
and information infrastructure. CPS presents unique challenges, and industry stakeholders. The working group will consist of 5
including the need for real-time response in support of technical subgroups: 1) Definitions and Taxonomy, 2) Reference
extremely high availability, predictability, and reliability. Despite Architecture, 3) Use Cases, 4) Cybersecurity and Privacy, and 5)
the ubiquity and criticality of CPS, additional thought is required Timing. CSD will lead the Cybersecurity and Privacy subgroup
regarding the design of secure CPS. As a result, there have been focused on identifying strategies for cybersecurity and privacy
numerous successful attacks targeting CPS for the control of in CPS, and work collaboratively with the other subgroups to
critical infrastructure (e.g., Stuxnet, Duqu, Flame, Gauss). ensure that cybersecurity is included as a design principle in
development.
In April 2013, CSD and the Cyber Security Research Alliance
(CSRA) co-hosted a 2-day workshop to explore emerging Contacts:
research needs for cybersecurity in CPS with the diverse Ms. Tanya Brewer Ms. Suzanne Lightman
cyber-physical community at large. The workshop brought (301) 975-4534 (301) 975-6442
together engineering and IT experts who have dealt with tbrewer@nist.gov suzanne.lightman@nist.gov
security issues related to CPS. Representatives from industry,
academia, and government engaged in interactive discussions Ms. Vicky Yan Pillitteri
during the workshop in the areas of supply chain, assurance, (301) 975-8542
threat information, identifying existing tools and practices to victoria.yan@nist.gov
secure CPS, security in acquisition and implementation, and
trustworthy operations. Attendees were invited to participate
Federal Cybersecurity Research & Development
in break-out sessions where the discussion topics were briefly
(R&D)
framed, allowing the attendees to explore the discussion topics
and to share their experiences with integrating security into The Networking and Information Technology Research and
existing organizations (e.g., lessons learned and examples). Development (NITRD) Program provides a framework in which
many federal agencies come together to coordinate their
CSD, in conjunction with ITL’s Advanced Network
networking and IT research and development (R&D) efforts.
Technologies division, Information Access division, and NIST’s
CSD remained committed to the value of communicating its
Engineering Laboratory, collaborated to develop an initial NIST
R&D efforts to other federal colleagues and identifying the
notional reference architecture for CPS. This notional reference
opportunities to support R&D efforts throughout the Federal
architecture was designed at such a level of abstraction that
Government.
it can be applied across the breadth of the CPS, yet provides
modularization and context for integration. The notional In FY 2013, the CSIA Interagency Working Group (IWG) monthly
CPS reference architecture was driven from a community meetings provided an opportunity to learn and share about
19
Program and Project Achievements for FY 2013

ongoing research related to the themes and thrusts expressed Guidelines (VVSG) 1.1. The security guidelines were updated
in the Strategic Plan for the Federal Cybersecurity Research and in FY 2012 to improve the auditability of voting systems, to
Development. CSD briefed the working group regarding efforts provide greater software integrity protections, to expand and
on Executive Order 13636, “Improving Critical Infrastructure improve access control requirements, and to help ensure
Cybersecurity,” under which NIST has been directed to work cryptographic security mechanisms are implemented properly.
with stakeholders to develop a voluntary framework for reducing In addition, CSD supported the efforts of the EAC and Federal
cyber risks to critical infrastructure. CSD also described Voting Assistance Program (FVAP) of DoD to improve the voting
work on the Advanced Network Technologies division’s High process for citizens under the Uniformed and Overseas Citizens
Assurance Domain project, which exists to foster development Voting Act (UOCAVA) by leveraging electronic technologies. The
and deployment of new network security technologies to team worked with the TDCG’s UOCAVA Working Group to develop
increase trust in online communications. a risk analysis on technologies used in current UOCAVA voting
processes, including vote-by-mail, online voter registration,
CSD is also a regular participant in the coordination
electronic ballot delivery, and online ballot marking.
activities of the federal Special Cyber Operations Research and
Engineering (SCORE) Committee. SCORE enables technology
In FY 2014, NIST will continue to assist the EAC in developing
transfer through the sharing of NIST cybersecurity expertise
responses to public comments and providing updates to VVSG
and output. The SCORE committee interacts with federal
1.1. Additionally, CSD will continue to support efforts for the
leaders as part of the White House’s Comprehensive National
EAC and FVAP to improve the voting process for UOCAVA voters.
Cybersecurity Initiatives (CNCI).
CSD will continue security research efforts to support future
standards development efforts, particularly in the areas of risks
Contacts: to voting systems and innovative voting system architectures.
Mr. Bill Newhouse Dr. Ernest McDuffie
CSIA IWG, CSIA SSG SEW Education Team and SCORE rep http://vote.nist.gov
(301) 975-2869 (301) 975-8897
william.newhouse@nist.gov ernest.mcduffie@nist.gov
Contacts:
Mr. Andrew Regenscheid Mr. Joshua Franklin
Security Aspects of Electronic Voting (301) 975-5155 (301) 975-8463
andrew.regenscheid@nist.gov joshua.franklin@nist.gov
Health Information Technology Security
Health information technology (HIT) enables better patient
care through secure use and sharing of health information. It
leads to improvements in healthcare quality, reduced medical
errors, increased efficiencies in care delivery and administration,
and improved population
health. Central to reaching
these goals is the assurance
of the confidentiality, integrity,
and availability of health
In 2002, Congress passed the Help America Vote Act (HAVA) to information. CSD works
encourage the upgrade of voting equipment across the United with government, industry,
States. HAVA established the Election Assistance Commission academia, and others to
(EAC) and the Technical Guidelines Development Committee provide security tools, technologies, and methodologies that
(TGDC), chaired by the Director of NIST. HAVA directs NIST to provide for the security and privacy of health information.
provide technical support to the EAC and TGDC in efforts related
to human factors, security, and laboratory accreditation. As part NIST continued its HIT security outreach efforts in FY 2013.
of NIST’s efforts, CSD supports the activities of the EAC related NIST and the Department of Health and Human Services’ (DHHS)
to voting equipment security. Office for Civil Rights (OCR) cohosted the sixth annual HIPAA
Security Rule conference, “Safeguarding Health Information:
In the past year, NIST supported the EAC by developing Building Assurance through HIPAA Security,” in May 2013 at
responses to public comments on the Voluntary Voting System
20
Computer Security Division Annual Report - 2013

the Ronald Reagan Building and International Trade Center in Supply Chain Risk Management (SCRM) for
Washington, D.C. The conference offered important sessions Information and Communications Technology
that focused on broad topics of interest to the healthcare (ICT)
and health IT security community. Over 600 in-person and
virtual attendees from federal, state, and local governments, Federal agency information systems are increasingly at risk
academia, HIPAA-covered entities and business associates, of both intentional and unintentional supply chain compromise.
industry groups, and vendors heard from, and interacted with, The management of ICT supply chain risk includes ensuring the
healthcare, security, and privacy experts on technologies and integrity, security, and resilience of the supply chain and the
methodologies for safeguarding health information and for products and services it delivers (Figure 4). Today’s ICT supply
implementing the requirements of the HIPAA Security Rule. chains have increased complexity, diversity, and scale. Federal
Presentations covered a variety of current topics including: Government information systems have rapidly expanded in
 Updates on the OCR privacy, security, and breach terms of capability and number, with an increased reliance on
notification audit program outsourcing and commercially available products. These trends
have caused federal departments and agencies to have a lack
 Patient and provider identity management, HIPAA of visibility and understanding of how acquired technology is
requirements in cloud and mobile environments developed, integrated, and deployed. Supply chain risks also
affect the processes, procedures, and practices used to assure
 HIPAA rule changes affecting breach notification and
the integrity, security, resilience, and quality of products and
HIPAA security
services. This lack of visibility and understanding, in turn,
has decreased federal departments’ and agencies’ control
 Cybersecurity Framework for improving critical
regarding decisions affecting the inherited supply chain risks
infrastructure cybersecurity
and the ability to manage those risks.
 Health IT activities at the National Cybersecurity Center
of Excellence
 Methods for managing insider threat
 Tools available to manage security settings on end-user
devices
The keynote address was delivered by Eric Dishman, Fellow
and General Manager of the Health Strategy & Solutions Group
at Intel.
In FY 2014, NIST plans to issue a
draft revision to Special Publication
(SP) 800-66, An Introductory
Figure 4: The Four Elements of ICT SCRM
Resource Guide for Implementing
the HIPAA Security Rule. As part of
its continued outreach efforts, NIST
also plans to co-host the seventh
annual Safeguarding Health
Information conference with OCR.
http://www.nist.gov/healthcare/security/
Contact:
Mr. Kevin Stine
(301) 975-4483
kevin.stine@nist.gov
21
Program and Project Achievements for FY 2013

Organizational Readiness, Best Practices and Standards,
and a composite network vulnerability map of physical
and cyber hubs and nodes, with risk ratings
 Collaboration/Crowdsourcing Portal: User-documented
ICT SCRM use/abuse cases and real-time polling about
vulnerabilities and responses
 ICT SCRM Initiatives: A dynamic matrix of current
industry and public sector ICT SCRM best practices,
standards, and policy reform initiatives that can be
updated by appropriate individuals from across industry,
academia, and government
Figure 5: ICT Supply Chain Risk  ICT SCRM Digital Library: An online repository of policy
and academic documents related to ICT SCRM
The ICT SCRM project seeks to provide federal agencies with
a toolkit of standardized, repeatable, and practical resources In FY 2014, CSD will continue its work to develop and
to strategically manage supply chain risk throughout the entire publish draft NIST SP 800-161. It will research and develop
lifecycle of systems, products, and services. tools and guidance to help agencies more effectively manage
their ICT supply chain risk. Additionally, NIST will continue to
In October 2012, NIST held a workshop with industry, co-chair Working Group 2 of the White House’s Comprehensive
academic, and government stakeholders to discuss: National Cybersecurity Initiative (CNCI) 11, Develop a Multi-
Pronged Approach for Global Supply Chain Risk Management,
 The fundamental underpinnings of ICT SCRM (terms,
and participate in national and international standards
definitions, characterizations)
activities related to supply chain risk management. Feedback
 Current and needed commercially reasonable ICT from organizations implementing ICT SCRM programs will
SCRM-related standards and practices (need, scope, and be evaluated, and best practices will be accumulated. NIST
development approach) will continue to engage stakeholders to identify needs and
opportunities for providing additional guidance regarding
 Current and needed ICT SCRM tools, technology, and
identifying and implementing supply chain protections.
techniques useful in securing the ICT supply chain
http://csrc.nist.gov/scrm/
 Current and needed research and resources
ICT SCRM Team email: scrm-nist@nist.gov
NIST used input from the workshop and additional stakeholder
Contacts:
forums to begin developing an initial public draft of NIST SP
800-161, Supply Chain Risk Management Practices for Federal Mr. Jon Boyens Ms. Celia Paulsen
Project Lead (301) 975-5549
Information Systems and Organizations, which is scheduled to
(301) 975-5981 celia.paulsen@nist.gov
be finalized in FY 2014. This document provides guidance to
jon.boyens@nist.gov
federal departments and agencies on identifying, assessing,
and mitigating ICT supply chain risks at all levels in their
organizations and utilizes and builds on existing guidance in
the unified information security framework.
Additionally in FY 2013, a grant was awarded to the University
of Maryland’s Supply Chain Management Center to support the
development and hosting of a web application with the following
capabilities:
 Enterprise Risk Assessments: A three-tier risk analysis
system based on the ICT SCRM Community Framework
Reference Architecture – A Strategic Assessment/
22
Computer Security Division Annual Report - 2013

Nationwide Public Safety Broadband Network  PSCR’s  Public  Safety  Broadband  Demonstration  Network
(NPSBN) Security located in Boulder, conduct research into identity management
technologies for mobile devices that can support the NPSBN,
|     |     |     |     |     |     | and  investigate  | ways  | to  | enhance  | the  security  | of  | mobile  |
| --- | --- | --- | --- | --- | --- | ----------------- | ----- | --- | -------- | -------------- | --- | ------- |
In February 2012, Congress passed the Middle Class Tax
Relief and Job Creation Act. One portion of this legislation calls  applications  used  by  the  public  safety  community.  CSD
|     |     |     |     |     |     | will  continue  | to  engage  |     | the  public  | safety  communications  |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | ----------- | --- | ------------ | ----------------------- | --- | --- |
for the establishment of a nationwide, interoperable public
safety broadband network based on Long-Term Evolution (LTE)  community by participating in events such as PSRC’s Annual
technology. The network will be deployed and operated by  Public Safety Broadband Stakeholder Conference.
the First Responder Network Authority (FirstNet). The planned
| National Public Safety Broadband Network (NPSBN) will “create  |     |     |     |     |     | Contacts: |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
a much needed nationwide interoperable broadband network  Ms. Sheila Frankel  Dr. Nelson Hastings
that will help police, firefighters, emergency medical service  (301) 975-3297  (301) 975-5237
|                  |             |         |                |     |     | sheila.frankel@nist.gov   |     |     | nelson.hastings@nist.gov |     |     |     |
| ---------------- | ----------- | ------- | -------------- | --- | --- | ------------------------- | --- | --- | ------------------------ | --- | --- | --- |
| professionals    | and  other  | public  | safety         |     |     |                           |     |     |                          |     |     |     |
| officials  stay  | safe  and   | do      | their  jobs.”  |     |     |                           |     |     |                          |     |     |     |
php.xedni/vog.rcsp.www//:ptth  :ecruoS egamI
(http://www.ntia.doc.gov/category/
Smart Grid Cybersecurity
| public-safety).  | NIST  | is  directed  |     | to  |     |     |     |     |     |     |     |     |
| ---------------- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
establish a list of certified devices and
required components for interacting with
the nationwide network by public safety
| officials,      | vendors,  and  | other  | interested   |     |     |     |     |     |     |     |     |     |
| --------------- | -------------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| parties.  NIST  | is  directed   |        | to  conduct  |     |     |     |     |     |     |     |     |     |
research and development that supports
the acceleration and advancement of the
nationwide network.
In FY 2013, CSD supported the joint National Telecommuni-
| cations  and    | Information     | Administration  |           | (NTIA)  | and  NIST  |     |     |     |     |     |     |     |
| --------------- | --------------- | --------------- | --------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Public  Safety  | Communications  |                 | Research  | (PSCR)  | program    |     |     |     |     |     |     |     |
(http://www.pscr.gov) efforts by developing and establishing
security-related activities to support the proposed NPSBN. CSD
presented details of the PSCR security-related activities at
Figure 6: Smart Meter
PSRC’s Annual Public Safety Broadband Stakeholder Conference
in June 2013.
The major elements of the smart grid are the information
|     |     |     |     |     |     | technology,  | the  industrial  |     | control  | systems,  | and  | the  |
| --- | --- | --- | --- | --- | --- | ------------ | ---------------- | --- | -------- | --------- | ---- | ---- |
CSD provided comments and contributed text for the security-
|     |     |     |     |     |     | communications  | infrastructure  |     | used  | to  send  | command  |     |
| --- | --- | --- | --- | --- | --- | --------------- | --------------- | --- | ----- | --------- | -------- | --- |
related aspects of the National Public Safety Telecommunications
|     |     |     |     |     |     | information  | across  | the  electric  |     | grid  from  | generation  | to  |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | -------------- | --- | ----------- | ----------- | --- |
Council (NPSTC) Public Safety Broadband High-Level Launch
|     |     |     |     |     |     | distribution  | systems,  | and  | to  exchange  | usage  | and  | billing  |
| --- | --- | --- | --- | --- | --- | ------------- | --------- | ---- | ------------- | ------ | ---- | -------- |
Requirements, published in December 2012, that describe, in
information between utilities and their customers. Key to the
increasing levels of detail, the technical requirements of the
|     |     |     |     |     |     | successful  | deployment  | of  | the  smart  | grid  infrastructure  |     | is  |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ----------- | --------------------- | --- | --- |
NPSBN infrastructure, equipment, and communications.
the development of the cybersecurity strategy that includes
cybersecurity as a design consideration for new and emerging
| CSD  began  | participating  |     | in  the  standards  |     | development  |           |          |           |             |                |     |       |
| ----------- | -------------- | --- | ------------------- | --- | ------------ | --------- | -------- | --------- | ----------- | -------------- | --- | ----- |
|             |                |     |                     |     |              | systems,  | and  an  | approach  | to  adding  | cybersecurity  |     | into  |
process for LTE technology within the 3rd Generation Partnership
existing systems. The electric grid is critical to the economic
Project (3GPP) supporting public safety’s security requirements
related to Proximity Services (ProSe) and Group Communication  and physical well-being of the nation, and emerging cyber
threats targeting power systems highlight the need to integrate
System Enablers (GCSE). In addition, CSD broadened its scope
advanced security to protect critical assets.
within the IETF to include efforts related to public safety.
In January 2013, the Smart Grid Interoperability Panel (SGIP)
In FY 2014, CSD will continue supporting NPSTC’s efforts
|     |     |     |     |     |     | became  | a  membership-supported  |     |     | organization.  | The  | SGIP  |
| --- | --- | --- | --- | --- | --- | ------- | ------------------------ | --- | --- | -------------- | ---- | ----- |
related  to  NPSBN  and  to  representing  public  safety  in   Cybersecurity Working Group (CSWG) was renamed the Smart
international standardization efforts, such as IETF and 3GPP.
Grid Cybersecurity Committee (SGCC).  All three of these groups
| CSD will work to  | incorporate  |     | security capabilities into the  |     |     |     |     |     |     |     |     |     |
| ----------------- | ------------ | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
have been led by a NIST representative since their respective
23
Program and Project Achievements for FY 2013

creations, originating with the Cybersecurity Coordination to apply the NISTIR 7628; including the identification,
Task Group (CSCTG), created by NIST in support of the Energy risk assessment and selection of the applicable security
Independence and Security Act of 2007. The SGIP SGCC includes requirements needed to secure their smart grid systems.
additional leadership by a management team, comprised of
 The Privacy subgroup identifies and describes
three volunteer vice-chairs representing the Department of
privacy risks and concerns within developed or emerging
Energy (DOE), an electric utility, and a smart grid vendor, and a
interoperability standards for the smart grid, and then
volunteer secretariat.
determines the most appropriate and feasible practices
for mitigating the risks.
 The Standards subgroup assesses cybersecurity
requirements associated with SGIP-identified smart grid
standards and other documents for the SGIP Catalog of
Standards (CoS). The subgroup has reviewed over 75
documents to date.
An example of a SGCC deliverable in 2013 is the analysis
of cybersecurity regulations relevant to electricity subsector
During the past year, members of the CSWG/SGCC worked to
stakeholders and of NIST security guidance. The analysis
revise NISTIR 7628, Guidelines for Smart Grid Cybersecurity, to
identifies the relationship, similarities, and differences among
address changes in technologies and implementations since the
NISTIR 7628, SP 800-53, and the draft North American Electric
publication’s original release. The revision updates and expands the
Reliability Corporation (NERC) Critical Infrastructure Protection
development strategy, cryptography and key management, privacy,
Standards (CIP) v5, recognizing that each document has a
vulnerability classes, research and development topics, standards
different scope and audience.
review, and key power system use cases to reflect changes in the
smart grid environment since 2010. The final version is expected to The SGCC also supports the SGIP Catalog of Standards (CoS),
be posted in FY 2014. a compendium of standards, practices, guidelines and other
technical documents considered relevant for the development
In addition to the revision of NISTIR 7628, the CSWG/
of a robust, secure, and interoperable smart grid. Through the
SGCC has focused on specific topics such as cybersecurity
ongoing efforts of the SGCC, these documents are reviewed for
risk management, security architecture, security testing and
cybersecurity, and recommendations are made for how to include
certification, Advanced Metering Infrastructure (AMI) security,
cybersecurity in future revisions and in the implementation
the development of a User’s Guide for NISTIR 7628, and cloud
of the standards. CSD supports the SGCC in assessing the
computing and privacy for the smart grid. Work in these areas
security of cryptographic methods used in these standards,
is completed through SGCC subgroups, which are created and
practices, guidelines, and other technical documents. In many
disbanded in order to meet present needs. The SGCC currently
cases, the standards bodies have taken the results of the
consist of the following subgroups:
reviews and modified the standards or documents to address
 The Architecture subgroup continues to refine the
our recommendations. The SGCC has worked closely with some
smart grid cybersecurity architecture in coordination
of the standards bodies to ensure that the recommendations
with the SGIP Smart Grid Architecture Committee on the
are interpreted correctly and that the mitigation strategies
European Union architecture harmonization effort.
selected meet the intent of the NISTIR 7628 high-level
security requirements. The result is cybersecurity “baked-in”
 The Cloud Computing subgroup is addressing
to the standards rather than “bolted-on” after the standard is
the unique cybersecurity issues of using and managing
implemented.
smart grid applications that utilize the cloud.
In FY 2014, CSD will continue to support the SGCC in the
 The High-Level Requirements subgroup
evaluation of the cryptographic methods used standards,
maintains the high-level security requirements in NISTIR
practices, guidelines, and other technical documents for
7628 and develops analyses between NISTIR 7628 and
inclusion in the SGIP CoS.
other documents, standards, and guidelines.
Future activities include working with the SGIP Committees,
 The NISTIR 7628 User’s Guide subgroup is Domain Expert Working Groups, and Priority Action Plans to
developing a User’s Guide for utilities and other entities integrate cybersecurity into their work efforts. The SGCC will
involved in implementing smart grid systems can use establish a new subgroup to produce a cybersecurity risk
24
Computer Security Division Annual Report - 2013

management process case study to accompany the Department  Raising national awareness about risks in cyberspace
of Energy Risk Management Process guideline. Members of
 Broadening the pool of individuals prepared to enter the
the committee will produce white papers on security defense
cybersecurity workforce
in depth and breadth, unique cloud computing considerations
for the smart grid, as well as a User’s Guide for NISTIR 7628.
 Cultivating a globally competitive cybersecurity
Additionally, the SGIP SCCC will continue to collaborate with
workforce
industry, academia, other working groups, and government
agencies to address the cybersecurity needs for the smart grid.
This initiative comprises four component areas:
In addition to the SGIP SGCC activities, CSD will also
 National Cybersecurity Awareness
coordinate with NIST’s Engineering Laboratory (EL) and Smart
Grid Program Office on the development of a Cybersecurity  Formal Cybersecurity Education
Smart Grid Test Lab, part of the NIST Smart Grid Testbed Facility
now under construction. CSD will also collaborate with ITL’s  Cybersecurity Workforce Structure
Software and Systems Division on cybersecurity research in
 Cybersecurity Workforce Training and Professional
relation to the IEEE 1588, Precision Time Protocol, a standard
Development
on time synchronization that is used for the electric grid and
other special-purpose industrial automation and measurement
CSD is home to the NIST NICE Leadership Team (NNLT) that
networks.
focuses on the following activities:
http://www.sgip.org  Developing planning documents and building consensus
on the strategy and implementation activities of NICE
Contacts:
 Facilitating cross-functional cooperation among NICE
Ms. Vicky Yan Pillitteri Ms. Tanya Brewer
component lead agencies
(301) 975-8542 (301) 975-4534
victoria.yan@nist.gov tbrewer@nist.gov
 Fostering communication between the component
lead agencies by coordinating meetings, facilitating
Mr. Quynh Dang discussions, and disseminating information
(301) 975-3610
qdang@nist.gov  Promoting the initiative and its efforts by representing
NICE and speaking at cybersecurity events nationwide
Cybersecurity Awareness, Training, Education,
 Planning and hosting an annual workshop to promote
and Outreach
and support the evolving issues in cybersecurity
education
ª
National Initiative for Cybersecurity  Coordinating with other federal initiatives and efforts
Education (NICE) related to NICE
 Maintaining and updating the NICE website
NIST has served as the lead for the National Initiative for
Cybersecurity Education (NICE) since 2010. NICE is responsive
to President Obama’s declaration that the “cyber threat is one In FY 2013, NIST stewarded the National Cybersecurity
of the most serious economic and national security challenges Workforce Framework (NCWF), developed within NICE’s
we face as a nation” and “America’s economic prosperity in the Cybersecurity Workforce Training and Professional
21st century will depend on cybersecurity.” Development Component, through government-wide review.
NIST also planned, organized and hosted the fourth annual NICE
The goal of NICE is to enhance the overall cybersecurity Workshop, “Navigating the National Cybersecurity Education
posture of the United States by accelerating the availability of Interstate Highway,” from September 17-19, 2013. The
educational and training resources designed to improve the workshop highlighted cybersecurity awareness, education,
cyber behavior, skills, and knowledge of every segment of the and training programs that can be adopted, copied, used, or
population, enabling a safer cyberspace for all. NICE addresses built-on by small businesses, educational institutions, industry,
this challenging goal by: and government at the state, local, tribal and federal levels to
advance the strategic goals of NICE.
25
Program and Project Achievements for FY 2013

ª
The NNLT attended more than 100 events, symposia, forums, Computer Security Division Publications
competitions, educational outreach meetings, and workshops
to promote the activities within NICE. The NNLT worked with
the Office of Personnel Management (OPM) on the OPM Cross-
Agency Priority Goal: “Closing Skills Gap” for IT/Cybersecurity
and on the OPM Special Cybersecurity Workforce Project focused
on reducing cybersecurity workforce skills gaps. The project
will allow agencies to identify and address their needs for
cybersecurity skill sets to meet their missions. In accomplishing
this project, agencies will also be updating their cybersecurity
positions with codes that revise the definitions of and taxonomy
used for cybersecurity work. In FY 2013, the NNLT supported
DHS in the launch of the National Initiative for Cybersecurity
Careers and Studies (NICCS), (http://niccs.us-cert.gov), an
online resource for cybersecurity career, education, and training
information. NICCS leverages efforts of government, industry,
and academia to provide a comprehensive, single resource to During FY 2013, CSD continued its efforts to improve
address the nation’s cybersecurity knowledge needs. the quality of information about its publications on various
NIST websites. CSD also explored new ways to make those
In FY 2014, NIST will continue to promote the coordination publications available to CSD’s customers, who access CSD’s
of existing and future cybersecurity education, training, and technical security publications in various ways: (1) directly from
awareness activities while planning the transition of NICE the CSRC website, (2) through the NIST Publications Portal, via
leadership. NIST will also identify opportunities to extend and Internet search or (3) direct links from digital content, or (4)
integrate NICE activities to raise cybersecurity awareness in the from external information providers. By the end of FY 2013, CSD
context of other sectors, and promote the NCWF as a resource had more than 270 current publications in the NIST technical
to be used to identify workforce gaps, lead bi-weekly NICE series (FIPS, Special Publications (SPs) and NISTIRs).
component meetings, and continue to conduct broad outreach
Providing accurate metadata about publications improves
on the NICE program.
users’ abilities to locate the information they are seeking. In FY
http://www.nist.gov/nice/ 2013, CSD cleaned up the NIST Publications Portal records and
PDF metadata for all of its NIST technical series publications
and for more than 100 journal articles and conference papers
Contacts: co-authored by CSD staff in recent years. By improving
Dr. Ernest McDuffie Mr. Bill Newhouse the metadata—such as title, authors, report numbers and
NICE Project Lead NICE Program Lead keywords—within the PDFs themselves, Internet searches
(301) 975-8897 (301) 975-2869
provide more informative results and make NIST’s security
ernest.mcduffie@nist.gov william.newhouse@nist.gov
publications easier to find. CSD continues to apply those
consistent metadata practices to all new publications.
Additionally, CSD expanded the dissemination of its
publications to the Association for Computing Machinery
(ACM) Digital Library (DL). ACM DL now has a “collection”
of NIST Computer Security Publications, which includes SP
800-series publications. CSD initiated an internal project to
test the feasibility of creating electronic book (e-book) editions
of its FIPS, SPs and NISTIRs, to supplement the PDF editions
currently available on CSRC. The aim is to provide a wider range
of options for CSD customers to view and use CSD’s technical
publications. The pilot project uses the EPUB file format, an open
standard for e-books from the International Digital Publication
Forum (IDPF). CSD intends to begin posting EPUB versions of
selected publications in FY 2014, which will especially benefit
users of mobile devices.
26
Computer Security Division Annual Report - 2013

In FY 2014, CSD intends to explore more ways to improve are arranged by topic, relevant security control family, and legal
the consistency of its publications and associated metadata, requirements.
enhance users’ ability to browse and search publications on
During FY 2013, the top ten most downloaded publications
CSRC, make more e-book editions available, and expand
were:
publication availability on external sites.
1. SP 800-53 Revision 4, Security and Privacy Controls for
Federal Information Systems and Organizations
http://csrc.nist.gov/publications/
2. SP 800-12, An Introduction to Computer Security: The
Contact: NIST Handbook
Mr. Jim Foti
(301) 975-8018 3. FIPS 140-2, Security Requirements for Cryptographic
jfoti@nist.gov Modules
4. FIPS 201-2, Personal Identity Verification (PIV) of Federal
ª Employees and Contractors
Computer Security Resource Center
(CSRC) 5. SP 800-100, Information Security Handbook: A Guide for
Managers
The Computer Security Resource Center (CSRC), CSD’s
website, is one of the most visited websites at NIST. CSRC 6. SP 800-30, Revision 1, Guide for Conducting Risk
encourages broad sharing of information security tools Assessments
and practices, provides a resource for information security
7. SP 800-57, Recommendation for Key Management: Part
standards and guidelines, and identifies and links key security
1: General
web resources to support industry and government users. CSRC
is an integral component of all of the work that CSD conducts
8. SP 800-53, Revision 3, Recommended Security Controls
and produces. It is CSD’s repository for anyone wanting to
for Federal Information Systems and Organizations
access these documents and other valuable security-related
information. During FY 2013, CSRC had more than 53 million 9. NISTIR 7916, Proceedings of the Cybersecurity in Cyber-
page views and downloads. Physical Systems Workshop, April 23-24, 2012
10. SP 800-123, Guide to General Server Security
In the FIPS publication series, the top three most downloaded
FIPS were:
1. FIPS 140-2, Security Requirements for Cryptographic
Modules
2. FIPS 201-2, Personal Identity Verification (PIV) of Federal
Employees and Contractors
3. FIPS 197, Advanced Encryption Standard
CSRC
CSRC
CSRC CSRC In the SP publication series, the top three most downloaded
SPs were:
1. SP 800-53 Revision 4, Security and Privacy Controls for
Figure 7: Total Number of CSRC Website Requests for 2013 Federal Information Systems and Organizations
(Oct. 1, 2012 to Sept. 30, 2013)
2. SP 800-12, An Introduction to Computer Security: The
NIST Handbook
CSRC is the primary gateway for gaining access to NIST
3. SP 800-100, Information Security Handbook: A Guide for
computer security publications, standards, and guidelines,
Managers
and serves as a vital link to CSD’s customers. Publications are
organized to help users locate relevant information quickly and
27
snoilliM
Program and Project Achievements for FY 2013

In the NISTIR publication series, the top three most Government employees who participate in the management of
downloaded NISTIRs were: their organization’s information system security program. There
are no membership dues. The Forum also holds bimonthly
1. NISTIR 7916, Proceedings of the Cybersecurity in Cyber-
meetings and an annual 2-day conference to discuss current
Physical Systems Workshop, April 23-24, 2012
issues and developments of interest to those responsible for
2. NISTIR 7250, Cell Phone Forensic Tools: An Overview and protecting sensitive (unclassified) federal systems. Participation
Analysis in Forum meetings is open to Federal Government employees,
and their designated support contractors, who participate in
3. NISTIR 7896, Third-Round Report of the SHA-3
the management of their organization’s information security
Cryptographic Hash Algorithm Competition
program.
In addition to CSRC, CSD maintains a publication
Topics of discussion at Forum meetings in FY 2013 included
announcement mailing list. This free email list notifies
briefings from various federal agencies on Preparing for
subscribers about publications that have been posted to the
and Responding to Certification Authority Compromise and
CSRC website. The email list is a valuable tool for more than
Fraudulent Certificate Issuance; Software Assurance: Enabling
28,000 subscribers from the Federal Government, industry,
Security throughout the Software Development Lifecycle; Use
academia, and individuals with a personal interest in IT security.
of Cybersecurity Function Code; Census Risk Management
Individuals who are interested in subscribing to this list should
Program Implementation; National Cybersecurity Center of
visit http://csrc.nist.gov/publications/subscribe.html for more
Excellence (NCCoE); demonstration of Trusted Geolocation in
information.
the Cloud; and Policy Machine: Enabling an Enterprise-wide,
Data Centric Computing Environment.
Questions on the website should be sent to the CSRC Webmaster at:
webmaster-csrc@nist.gov.
This year’s annual 2-day offsite meeting featured updates on
the computer security activities of the Government Accountability
Contacts: Office (GAO), General Services Administration (GSA), Bureau of
Mr. Patrick O’Reilly Ms. Judy Barnard the Fiscal Service, and NIST. Recent administration guidance
(301) 975-4751 (301) 975-5502 directing federal agencies to reduce travel and conference
patrick.oreilly@nist.gov jbarnard@nist.gov budgets significantly reduced attendance. Technical sessions
included briefings on evolving cybersecurity strategies, IT
security concerns during a consolidation (merger), supply chain
ª
Federal Computer Security Program risk management activities, the National Vulnerability Database
Managers’ Forum (NVD), SP 800-53 Revision 4, continuous monitoring, industrial
control systems security, and EO 13636.
The Federal Computer Security Program Managers’ Forum is
On August 8, 2013, a Cybersecurity and Risk Management
sponsored by NIST to promote the sharing of security-related
Training Workshop was held at the Department of Commerce
information among federal agencies. The Forum, which serves
with over 500 registrants. Attendees gained a greater
more than 1,100 members, strives to provide an ongoing
understanding of the Risk Management Framework (RMF) and
opportunity for managers of federal information security
its practical application. Dr. Ron Ross discussed SP 800-53
programs to exchange information security materials in a timely
Revision 4 and the fundamentals of continuous monitoring. Two
manner, build upon the experiences of other programs, and
afternoon panels discussed case studies regarding RMF and
reduce possible duplication of effort. It provides a mechanism
“ongoing authorization.”
for NIST to share information directly with federal agency
information security program managers in fulfillment of NIST’s
The Forum plays a valuable role in helping NIST and other
leadership mandate under FISMA. It assists NIST in establishing
federal agencies to develop and maintain a strong, proactive
and maintaining relationships with other individuals or
stance in the identification and resolution of new strategic
organizations that are actively addressing information security
and tactical IT security issues as they emerge. The number
issues within the Federal Government. NIST serves as the
of members on the email list has grown steadily and provides
Secretariat of the Forum, providing necessary administrative
a valuable resource for federal security program managers.
and logistical support. Kevin Stine serves as the Chairperson.
To join, email your name, affiliation, address, phone number,
title, and confirmation that you are a federal employee to
The Forum maintains an extensive email subscription
sec-forum@nist.gov.
service. Participation in the service is only open to Federal
28
Computer Security Division Annual Report - 2013

http://csrc.nist.gov/groups/SMA/forum/ Recent government sequestration efforts prevented some from
receiving permission to attend, which had a noticeable effect
on attendance. NIST’s Pat Toth and Peggy Himes, as well as
Contacts:
Gretchen Morris, Susan Hansche, and other members of the
Mr. Kevin Stine Ms. Peggy Himes
FISSEA Technical Working Group, were integral to the effort to
Chair Administration
(301) 975-4483 (301) 975-2489 support the conference.
kevin.stine@nist.gov peggy.himes@nist.gov
This year’s theme was, “Making Connections in Cybersecurity
and Information Security Education,” to solicit presentations
ª that reflect current projects, trends, and initiatives that provide
Federal Information Systems Security
for future solutions in federal security programs. Attendees
Educators’ Association (FISSEA)
gained new techniques for developing/conducting training,
cost-effective practices, workforce development, free resources
The Federal Information Systems Security Educators’ and contacts, as well as an update on NICE activities.
Association (FISSEA), founded in 1987, is an organization run
by and for information systems security professionals to assist NIST ITL Computer Security Division Deputy Chief, Matthew
federal agencies in meeting their information systems security Scholl, welcomed attendees. Keynote presentations were
awareness, training, and education responsibilities. FISSEA given by John J. Suess, VP of IT & CIO, University of Maryland,
strives to elevate the general level of information systems Baltimore County; Bryant Tow, Vice President, InfraGard National
security knowledge for the Federal Government and the federal Members Alliance; and Lamont Hames, Chief Development
workforce. It also seeks to assist the professional development Officer, UNCF Special Programs Corporation. Mr. Hames
of its members. presented on Expanding the Role of Minorities in Cyber Security.
FISSEA membership is open to information systems security Presenters represented NIST, DHS, DOS, DOE, NSA and the
professionals, professional trainers and educators, and Library of Congress as well as private industry and academia.
managers responsible for information systems security training Conference attendees had the opportunity to visit vendors,
programs in federal agencies, as well as contractors of these receive a government best practice poster, and attend a
agencies and faculty members of accredited educational demonstration session, which provided an opportunity for
institutions who are involved in information security training agencies to share about their specific awareness and training
and education. There are no membership fees to join FISSEA; all programs.
that is required is a willingness to share products, information,
Traditional FISSEA conference events included announcing
and experiences. A working group meets monthly to administer
the winners of FISSEA contests and awarding prize drawings.
business activities
Susan Hansche, Avaya Gov/U.S. Department of State, presented
FISSEA maintains a website, a mailing list, and participates the FISSEA Educator of the Year plaque to Mr. J. Paul Wahnish,
in a social networking site as a means of communication for its Career Technical Education Foundation, Inc., for his work in
members. NIST assists FISSEA with its operations by providing preparing the future workforce. The FISSEA Security Awareness,
staff support for several of its activities and by being FISSEA’s Training & Education Contest includes five categories from
host agency. one of FISSEA’s three key areas of Awareness, Training, and
Education. The winner is selected from each category and
FISSEA membership in 2013 spanned federal agencies, awarded a certificate. The categories include: (1) awareness
industry, military, contractors, state governments, academia, the poster, (2) motivational item (e.g., pens, stress relief items,
press, and foreign organizations to reach over 1,395 members t-shirts), (3) awareness website, (4) awareness newsletter, and
in a total of ten countries. The 700 federal agency members (5) role-based training & education.
represent 89 agencies from the executive and legislative
branches of government. The winners of the 2013 FISSEA Awareness, Training, and
Education Contest are:
The 26th Annual FISSEA Conference occurred March 19-21,
 Poster Winner: Alexis Benjamin – Department of State,
2013, at NIST. Approximately 140 information systems security
Office of Computer Security
professionals and trainers attended from federal agencies,
academia, as well as industry representatives from firms that
 Website Winner: Sara Fitzgerald and Kimberly Conway –
support federal information systems and security programs.
Food & Drug Administration (FDA)
29
Program and Project Achievements for FY 2013

ª
 Motivational Item Winner: Jennie Blizzard, Shannon Information Security and Privacy
Jones, and Shirley Clement – Federal Reserve Bank Advisory Board (ISPAB)
 Newsletter Winner: Deborah Coleman – Department of The ISPAB was originally created by the Computer Security
Education, Office of the Chief Information Officer Act of 1987 (P.L. 100-235) as the Computer System Security
and Privacy Advisory Board, and amended by Public Law
 Role-Based Training Winner: DISA, SAIC, and Carney, Inc.
107-347, The E-Government Act of 2002, Title III, The Federal
(submitted by Carmina Carper)
Information Security Management Act (FISMA) of 2002. The
statutory objectives of the Board include identifying emerging
Conference attendees selected their Peer’s Choice Awards,
managerial, technical, administrative, and physical safeguard
and they are...
issues relative to information security and privacy.
 Poster Winner: Deborah Coleman – Department of
In drafting the Computer Security Act of 1987, which
Education, Office of the Chief Information Officer
created this Advisory Board, the Congress saw a need for an
 Website Winner: Deborah Coleman – Department of independent, non-federally dominated group of computer
Education, Office of the Chief Information Officer security experts to offer its advice to senior government officials
on emerging computer security areas. The Board members,
 Motivational Item Winner: Chrisan Herrod – University of
with their individual and collective skills, responsibilities, and
Maryland University College
experiences fulfill this requirement. No other similar group of
experts meets regularly to review information security issues
 Newsletter Winner: Sara Fitzgerald and Kimberly Conway
– Food & Drug Administration (FDA) involved in unclassified Federal Government computer systems
and networks. Also, Title III of the E-Government Act of 2002
 Role-Based Training Winner: Sara Fitzgerald and reaffirmed the need for this Board by giving it additional
Kimberly Conway – Food & Drug Administration (FDA) responsibilities.
The ISPAB’s statutory purpose is to advise the Secretary of
New this year was the Pecha Kucha session on the third day.
Commerce, the Director of the NIST, and the Director of the
During Pecha Kucha (Lightning Round) speakers had 6 minutes
OMB on information security and privacy related issues. Title III
40 seconds to present a limited number of slides (20 slides at
of the E-Government Act of 2002 also mandated the Board to
most), and only 20 seconds per slide. The presentation method
thoroughly review all of the proposed information technology
is challenging for the speaker and enjoyable for audience
standards and guidelines developed under Section 20 of the
members. There were four participants and their fast-paced
National Institute of Standards and Technology Act (15 U.S.C.
talks proved to be lively and entertaining.
278g-3) as amended.
Attendee networking is a valuable benefit of attending
The charter (http://csrc.nist.gov/groups/SMA/ispab/
the FISSEA conference. The conference continues to be a
documents/ispab_charter-2012-2014.pdf) defines that the
valuable forum in which individuals from government, industry,
Board’s membership should consist of 12 members and
and academia who are involved with information systems/
a Chairperson. The Secretary of Commerce appoints the
cybersecurity workforce development (awareness, training,
Chairperson, and the Board members are selected for their
education, certification, and professionalization) learn of
preeminence in the information technology industry or related
ongoing and planned training and education programs and
disciplines. The term of office for each board member is four
initiatives. It provides NIST the opportunity to provide assistance
years.
to departments and agencies as they work to meet their FISMA
responsibilities. The Board is comprised of members from a broad range of
interested parties. There are three main categories and each
The 2014 FISSEA conference is planned for March 18-20,
category has four members. Category 1 includes members
2014, at NIST.
from outside the Federal Government eminent in the information
technology industry, at least one of whom is representative of
http://csrc.nist.gov/fissea
fisseamembership@nist.gov small or medium-sized companies in such industries. Category 2
also includes members from outside the Federal Government and
not employed by or representative of a producer of information
Contacts:
but are eminent in the field of information technology, or related
Ms. Patricia Toth Ms. Peggy Himes
disciplines. Category 3 includes experienced information
(301) 975-5140 (301) 975-2489
system managers from the Federal Government, including
patricia.toth@nist.gov peggy.himes@nist.gov
30
Computer Security Division Annual Report - 2013

From Left to Right: Tatiana Laszczak, Chris Boyer, Annie Sokol, Ed Roback, Greg Garcia, Matt Thomlinson (Chair), Peter Weinberger, John Centafont,
Toby Levin, Matt Scholl, Gale Stone.Not Present for photo: Julie Boughn
those with experience in information security and privacy, Innovation, Department of Human Health and Services,
at least one of whom should be from the National Security Centers for Medicare & Medicaid Services (DHHS/CMS)
Agency. Federal members bring a detailed understanding of
 Christopher Boyer, AT&T
the federal processing environment; industry brings concerns
and experiences regarding product development and market
 John Centafont, National Security Agency (NSA)
formation, while private computer security experts are able to
bring their experiences of commercial cost-effective security  Kevin Fu, The University of Michigan
measures into Board discussion.
 Gregory Garcia, Garcia Cyber Partners
In October 2012, Matt Thomlinson agreed to assume the
 Brian Gouker, NSA - U.S. Army War College
responsibilities of Chairperson from Dan Chenok. The Board
expressed its gratitude to Dan Chenok for his leadership and  Toby Levin, Retired
contributions to ISPAB both as a member and Chair since 2005.
Presently, ISPAB has nine members and a Chairperson. The  Edward Roback, U.S. Department of Treasury
ISPAB Board members are:
 Phyllis Schneck, (Retired from the Board in September
 Matthew Thomlinson, (Chair), Microsoft 2013), McAfee, Inc.
 Daniel Chenok (Chair – Retired from the Board in October  Gale Stone, Social Security Administration
2012), IBM Center for The Business of Government
 Peter Weinberger, Google, Inc.
 Julie Boughn, Center for Medicare and Medicaid
31
Program and Project Achievements for FY 2013

During FY 2013, ISPAB held three meetings, all held in ISPAB meeting agendas are established based on the Board’s
Washington D.C: list of emerging issues developed from previous meetings. The
meeting agenda topics also include non-work list items that
 October 10-12, 2012
are of immediate security and privacy concerns to the Board.
 February 13-15, 2013 During FY 2013, the Board provided guidance on many issues
relating to security and privacy such as:
 June 12-14, 2013
 Security and Privacy Controls
It is of particular interest to mention ISPAB’s involvement
 Digital and Mobile Security
with the EO Cybersecurity Framework and that prior to opening
the ISPAB meeting on February 15, 2013, the Board attended
 FISMA as privacy appendix on SP 800-53, metrics,
the presentation of cybersecurity policy discussion and launch
FISMA review, reduction of reporting
of the Executive Order (EO) to improve the Cybersecurity
of the U.S.’s critical infrastructure at the U.S. Department of  A130 Appendix A
Commerce. The President signed the EO and also approved the
 GAO Reports: Security and Privacy
presidential directive to improve the security and resilience of
critical infrastructure in both the cyber and physical realms.
 Medical Device Security
Dr. Patrick Gallagher, Under Secretary of Commerce for
Standards and Technology and NIST Director, provided the  Cybersecurity – Education, Training, Awareness
opening remarks on the EO. A group of distinguished panelists
presented more information:  Cross-Agency Priority (CAP) Goals
 Andy Ozment, Senior Director of Cybersecurity, Executive  Cloud Computing and Security Challenges
Office of the President
 Exploring the Future of Privacy for Federal IT
 Samara Moore, Cyber Director for Critical Infrastructure,
Executive Office of the President  IT System Performance
 Adam Sedgewick, Senior Information Technology Policy  Supply Chain and Risk Management
Advisor, National Institute of Standards and Technology
 SEC Security Breach Notification
 Bruce McConnell, Senior Counselor for Cybersecurity,
The presenters at every Board meeting were leaders and
Department of Homeland Security
experts from private industries, academia, federal agency CIOs,
 Ari Schwartz, Internet Policy Advisor, National Institute of IGs and CISOs.
Standards and Technology Copies of the current list of members and their bios, the
Board’s charter and past Board activities can be located at
 Jenny Menna, Director, Stakeholder Engagement and
http://csrc.nist.gov/groups/SMA/ispab. Information on ISPAB
Cyber Infrastructure Resilience Division, Department of
Meetings is published in Federal Register Notice at least 16
Homeland Security
days prior to the meeting. Those interested in receiving meeting
notices may email name, affiliation, and address to:
Contact:
Ms. Annie Sokol
DFO, ISPAB
(301) 975-2006
annie.sokol@nist.gov
32
Computer Security Division Annual Report - 2013

ª
Small and Medium Size Business (SMB) Cryptographic Technology
Outreach
Small business owners ª
Cryptographic Standards Program
face a broad range of
information security
issues. A computer Hash Algorithms and the Secure Hash Algorithm
failure or system breach (SHA-3) Standard (Draft FIPS 202)
could jeopardize the
In response to vulnerabilities discovered in 2005 in the
company’s reputation and may result in significant damage
and recovery cost or going out of business. The small business NIST-approved, government hash algorithm standard, SHA-1,
owner who recognizes the threat of computer crime and takes NIST opened a public competition in 2007 to develop a new
steps to deter inappropriate activities is less likely to become cryptographic hash algorithm, SHA-3, to augment the hash
a victim. algorithms specified in FIPS 180-4, Secure Hash Standard.
After 64 entries, 3 rounds of the competition, and 5 years of
The U.S. Small Business Administration (SBA) reports that intensive analysis, provided mostly by the world cryptographic
over 27 million U.S. companies - more than 99 percent of all
community, NIST announced the selection of KeccaK as the
U.S. businesses - are SMBs of 500 employees or fewer (http://
winning algorithm on October 2, 2012, and summarized its
www.sba.gov/sites/default/files/allprofiles12.pdf). While the
decision in NISTIRs after each round.
threats to individual SMBs may not be significantly different
from those facing larger organizations, a SMB frequently has After the competition had ended, NIST invited the winning
fewer resources available to protect systems, detect attacks, team to NIST in February 2013, and hosted a 2-day workshop to
or respond to security issues. A vulnerability common to a discuss the KeccaK features and options for standardization as
large percentage of SMBs could pose a threat to the nation’s the new SHA-3 hash standard. CSD developed a standardization
information infrastructure and economic base. plan and shared with the KeccaK designers and subsequently
with the cryptographic community at the 2013 RSA Conference,
To help address information security risk, these businesses
the 2013 Workshop on Cryptographic Hardware and Embedded
require assistance with identification of security mechanisms
Systems (CHES), and at the IETF 86 and 87 Workshops. In
and with practical, cost-effective training. Training helps SMB’s
addition, this standardization plan was posted at the NIST hash
use their limited resources most effectively to address relevant
website for public comment.
and serious threats. In response to this need, NIST, the SBA, and
the Federal Bureau of Investigation (FBI) co-sponsor a series A draft of the SHA-3 Permutation-based Hash Standard (Draft
of cyber security training workshops for small businesses. FIPS 202) is being finalized, and NIST is preparing a Federal
These workshops provide an overview of cyber security Register Notice to announce this draft standard. NIST expects
threats, vulnerabilities, and corresponding protective tools and to release the draft standard during FY 2014 and plans a 60-day
techniques, with a special emphasis on information that small public comment period. After the comment period closes, NIST
business personnel can apply directly. will analyze the comments, make changes to the document, as
appropriate, and propose the draft standard to the Secretary
In FY 2013, the SMB outreach team provided 15 workshops
of Commerce for approval as a FIPS. In addition to publishing
in 15 cities: Toledo, Ohio; Burlington, Vermont; Portland, Maine;
FIPS 202 in FY 2014, NIST is also considering standardizing a
Providence, Rhode Island; Lexington, Kentucky; Louisville,
generic “tree hashing” mode and other KeccaK features. NIST
Kentucky; Pittsburgh, Pennsylvania; Cleveland, Ohio; Detroit,
plans to host a workshop in FY 2014 to discuss these options.
Michigan; Portland, Oregon; Little Rock, Arkansas; Shreveport,
Louisiana; Alexandria, Louisiana; Ruston, Louisiana; and Information about the SHA-3 competition and
Monroe, Louisiana. the SHA-3 standardization effort is available at
http://www.nist.gov/hash-competition.
In collaboration with the SBA and the FBI, CSD is planning
locations for small business cyber security workshops in FY
Contact:
2014.
Ms. Shu-jen Chang
(301) 975-2940
http://sbc.nist.gov
shu-jen.chang@nist.gov
Contact:
Mr. Richard Kissel
(301) 975-5017
richard.kissel@nist.gov
33
Program and Project Achievements for FY 2013

Hash Algorithm Standards and Security Guidelines certificate profiles and validation methods, TLS extensions, and
support for a greater variety of cryptographic algorithms.
CSD’s Cryptographic Technology Group (CTG) is responsible
The final version of SP 800-52 Revision 1 will be published
for the maintenance and development of the FIPS 180-4,
in FY 2014.
Secure Hash Standard (SHS). A hash algorithm processes a
message, which can be very large, and produces a condensed
Contacts:
representation, called a message digest. A cryptographic hash
algorithm is a fundamental component of many cryptographic
Dr. Kerry McKay Dr. Lily Chen
(301) 975-4969 (301) 975-6974
functions, such as digital signature algorithms, key derivation
kerry.mckay@nist.gov lily.chen@nist.gov
functions, keyed-hash message authentication codes, and
random number generators. Cryptographic hash algorithms
are frequently used in Internet protocols and other security
Random Number Generation (RNG)
applications.
FIPS 180-4 specifies seven hash algorithms: SHA-1, SHA-224, Random numbers provide the required security for many
SHA-256, SHA-384, SHA-512, SHA-512/224 and SHA-512/256. cryptographic algorithms. For example, random numbers are
Their security properties in different cryptographic applications used to generate the keys needed for encryption and digital
are discussed in SP 800-107, Revision 1, Recommendation for signature applications.
Applications Using Approved Hash Algorithms. In the late 1990s, a project to develop more rigorous
CSD authored an article, “Changes in Federal Information requirements and specifications for random number generation
Processing Standard (FIPS) 180-4, Secure Hash Standard,” (RNG) was initiated in coordination with the American National
which was published in the January 2013 issue of the journal Standards Institute’s (ANSI) Accredited Standards Committee
Cryptologia. The article describes the rationale behind the (ASC) X9. The resulting standard (X9.82) contains four parts:
standardization of the SHA-512/224 and SHA-512/256 hash Part 1 provides general information; Part 2, which is nearing
algorithms in FIPS 180-4 and the performance advantage of completion, will provide requirements for entropy sources;
these two hash algorithms over the SHA-224 and SHA-256 hash Part 3 provides specifications for deterministic random bit
algorithms. This article was written to help the adoption of the generator (DRBG) mechanisms; and Part 4 provides guidance
two new hash algorithms in security protocols and applications on constructing random bit generators (RBGs) from entropy
to improve performance. sources and DRBG mechanisms.
In March 2007, NIST published SP 800-90, Recommendation
Contacts: for Random Number Generation Using Deterministic Random
Mr. Quynh Dang Ms. Elaine Barker Bit Generators, which contained the DRBG mechanisms in
(301) 975-3610 (301) 975-2911 Part 3 of ANS X9.82, plus an additional DRBG mechanism. This
quynh.dang@nist.gov elaine.barker@nist.gov
recommendation was revised as SP 800-90A, Recommendation
for Random Number Generation Using Deterministic Random Bit
Generators, in January 2012 to include additional capabilities
Transport Layer Security (TLS)
identified during the development of Part 4 of ANS X9.82.
Two additional documents (SP 800-90B, Recommendation for
SP 800-52, Guidelines for the Selection, Configuration,
the Entropy Sources Used for Random Bit Generation and SP
and Use of Transport Layer Security (TLS) Implementations,
800-90C, Recommendation for Random Bit Generator (RBG)
provides recommendations regarding TLS server and client
Constructions) are under development and are available for
implementations. TLS is a widely used cryptographic protocol
public comment. SP 800-90B addresses the development
that provides communication security for a variety of network
and testing of entropy sources, including descriptions of the
applications, such as email, e-commerce, and healthcare.
validation tests for NIST’s Cryptographic Algorithm Validation
The first version of SP 800-52, published in 2005, was
Program to validate candidate entropy sources. SP 800-90C
withdrawn in March 2013. A draft of SP 800-52 Revision 1
provides basic guidance on the construction of RBGs from
was issued for public review and comment in September
entropy sources and DRBG mechanisms.
2013. The revision is a substantially different document than
CSD held a workshop in December 2012 to discuss the drafts
the original and includes recommendations providing higher
of SP 800-90B and C, after which NIST began the adjudication
levels of security, both for TLS and aspects of the Public Key
of the comments received during the public comment period
Infrastructure (PKI) that TLS relies on. New recommendations
and the workshop.
include the support of TLS versions 1.1 and 1.2, guidance on
34
Computer Security Division Annual Report - 2013

In September 2013, articles from major news organizations Layer Security (TLS) section, which is now being addressed in SP
based on leaked classified documents raised public concern 800-52, Revision 1, Guidelines for the Selection, Configuration,
that one of the DRBGs specified in SP 800-90A, the Dual_EC_ and Use of Transport Layer Security (TLS) Implementations. The
DRBG, could contain a backdoor. This could allow attackers to revised SP 800-57, Part 3 will be available for public comment
successfully predict the secret cryptographic keys that form the in FY 2014.
foundation for the assurances provided by security products.
SP 800-130, A Framework for Designing Cryptographic Key
Taking these concerns seriously, NIST assured the community
Management Systems, was completed in August 2013 and
of its commitment to producing strong cryptographic standards,
provides guidance on a Cryptographic Key Management System
and took immediate steps to examine and remediate the issue.
(CKMS) framework.
Shortly after these concerns were raised, CSD published
SP 800-152, A Profile for U.S. Federal Cryptographic Key
an ITL Bulletin that provided a high-level discussion of the
Management Systems (CKMS), is under development. This
issues, reopened the SP 800-90 series of publications for
document is intended to provide refinements of the framework
public comment, and recommended that the Dual_EC_DRBG no
requirements in SP 800-130 that are appropriate for use in a
longer be used, pending the resolution of the comments. Since
CKMS employed by the Federal Government, plus guidance on
that time, NIST has released a revised draft of SP 800-90A that
its implementation, procurement, installation, configuration,
removes the questioned algorithm and addresses other issues
and operation. This document will be available for public
that were identified in the public comment process. NIST
comment in early FY 2014.
intends to finalize the revised SP800-90A publication in FY14.
A new publication will provide guidance on the security
strength of a cryptographic key that is used to protect data
Contacts:
(i.e., a data-protection key), given the manner in which the key
Ms. Elaine Barker Mr. John Kelsey
was generated and handled prior to its use to protect the target
(301) 975-2911 (301) 975-5101
elaine.barker@nist.gov john.kelsey@nist.gov data. This document, SP 800-158, Key Management: Obtaining
a Targeted Security Strength, involves a considerable amount
of new research, since it is an area that has not been fully
Key Management addressed to date. This publication will be available for public
comment in FY 2014.
NIST continues to provide guidelines on cryptographic key
management for the Federal Government, and to coordinate http://csrc.nist.gov/groups/ST/key_mgmt/
with other national and international organizations, industry,
and academia. The guidelines are available at http://csrc.nist.
Contacts:
gov/publications.
Ms. Elaine Barker Dr. Dustin Moody
SP 800-56A, Recommendation for Pair-Wise Key Establishment (301) 975-2911 (301) 975-8136
Schemes Using Discrete Logarithm Cryptography, specifies elaine.barker@nist.gov dustin.moody@nist.gov
approved methods for key establishment using Diffie-Hellman
and Menezes-Qu-Vanstone (MQV) schemes. This document was Dr. Lily Chen Mr. Ray Perlner
first published in 2006 and was revised in May 2013 to provide (301) 975-6974 (301) 975-3357
further clarification and additional methods for key derivation. lily.chen@nist.gov ray.perlner@nist.gov
SP 800-56B, Recommendation for Pair-Wise Key Establishment
Mr. Quynh Dang
Schemes Using Integer Factorization Cryptography, was first
(301) 975-3610
published in August 2009. It is under revision to provide further
quynh.dang@nist.gov
clarification and additional methods for key derivation; these
changes are consistent with those made in SP 800-56A. The
revision of SP 800-56B will be available for public comment in
Digital Signatures
FY 2014.
FIPS 186-4, Digital Signature Standard (DSS), specifies
SP 800-57, Recommendation for Key Management, Part 3:
three techniques for the generation and verification of digital
Application-Specific Key Management Guidance, was first
signatures that can be used for the protection of data: the Digital
published in 2009. A revision of this document has been under
Signature Algorithm (DSA), the Elliptic Curve Digital Signature
development. The revision will include an additional section on
Algorithm (ECDSA), and the Rivest-Shamir-Adleman (RSA)
the Secure Shell (SSH) protocol and the removal of the Transport
35
Program and Project Achievements for FY 2013

algorithm. A digital signature is represented in a computer as FPE: FF1, FF2, and FF3. These schemes were submitted for
a string of bits and is computed using a set of rules and a set NIST’s consideration in recent years under the names FFX-
of parameters that allow the identity of the signatory and the base, VAES3, and BPS; the original submission documents
integrity of the data to be verified. are available at http://csrc.nist.gov/groups/ST/toolkit/BCM/
modes_development.html, in the FFX and BPS entries under
FIPS 186, first published in 1994, has been revised several
the heading “Encryption Modes.”
times since then. In FY 2013, the Secretary of Commerce
approved the latest version of the standard, FIPS 186-4.
Contact:
Contacts: Dr. Morris Dworkin
(301) 975-2354
Ms. Elaine Barker Dr. Allen Roginsky
morris.dworkin@nist.gov
(301) 975-2911 (301) 975-3603
elaine.barker@nist.gov allen.roginsky@nist.gov
ª
Cryptographic Research
Block Cipher Modes of Operation
Post-Quantum Cryptography
The engine for many of the techniques in NIST’s cryptographic
toolkit is a block cipher algorithm, such as the Advanced
In FY 2013, NIST researchers Stephen Jordan, Yi-Kai Liu,
Encryption Standard (AES) algorithm or the Triple Data
Dustin Moody, Ray Perlner, and Daniel Smith-Tone internally
Encryption Algorithm (TDEA). A block cipher transforms some
presented status reports in the areas of quantum computation,
fixed-length binary data (i.e., a “block”) into seemingly random
coding-based cryptography, lattice-based cryptography, and
data of the same length. The transformation is determined by
multivariate cryptography, which included detailed surveys of
the choice of some secret data called the “key.” The key can
the respective fields, as well as security overviews and specific
also be used to recover the original block of data.
results. The project members also created evaluation criteria to
A method of using the block cipher to protect one or more
compare proposed post quantum cryptosystems with the end
blocks of data is called a block cipher mode of operation.
goal of standardization.
The approved modes are specified in the SP 800-38 series.
Each approved mode provides data confidentiality and/or NIST also engaged the international cryptographic community
authenticity/integrity. with presentations and publications. Daniel Smith-Tone and
Ray Perlner presented a paper at PQCrypto 2013, in addition to
In December 2012, NIST approved block cipher modes for
Dr. Smith-Tone speaking at the Joint Romanian Mathematical
key wrapping (i.e., the protection of the confidentiality and
Society, and the Quantum Cryptanalysis Seminar in Schloss
integrity of cryptographic keys). In particular, SP 800-38F,
Dagstuhl, Germany. Yi-Kai Liu presented his research at QCrypt
Recommendation for Block Cipher Modes of Operation: Methods
2013, as well as giving a talk at the European Telecommunication
for Key Wrapping, identifies existing methods that are approved
Standard Institute (ETSI) Quantum-safe Crypto Workshop. Lily
for key wrapping, and also specifies three deterministic
Chen also spoke at the ETSI Quantum-safe Crypto Workshop.
authenticated-encryption modes: the AES Key Wrap (KW) mode,
the AES Key Wrap with Padding (KWP) mode, and one TDEA Stephen Jordan delivered a keynote address at the 16th
mode, called TKW. Workshop on Quantum Information Processing on a paper that
was published in Science magazine. In FY 2013, Dr. Jordan also
Block cipher modes can also provide format-preserving
spoke about research at the Institute for Quantum Information
encryption (FPE). A format can be a sequence of decimal digits,
and Matter, the Hughes Research Laboratory, and the Lorentz
such as a credit card number or a social security number;
Center, as well as submitting some research papers for
formats can also be defined for other sets of characters besides
publication.
decimal digits. FPE is expected to be very useful because this
property facilitates the retrofitting of encryption to existing In FY 2014, NIST will continue to explore the security capacity
applications. of purported quantum-resistant technologies with the ultimate
NIST proposed the approval of three block cipher modes for goal of uncovering the fundamental mechanisms necessary for
FPE in Draft SP 800-38G, Recommendation for Block Cipher efficient, trustworthy, and cost-effective information assurance
Modes of Operation: Methods for Format-Preserving Encryption, in the post-quantum market. Upon the successful completion
which was released for a 60-day period of public comment of this phase of the project, NIST will be prepared for possible
in July 2013. This publication specifies three schemes for standardization efforts in this area. NIST will consider hosting
36
Computer Security Division Annual Report - 2013

a workshop on post-quantum cryptography to discuss practical the Beacon allows a user application to prove to anybody that
steps towards this goal. it used truly random numbers not known before a certain point
in time. Third, this proof can be presented offline and at any
Contacts: point in the future. For example, the proof could be mailed to a
Email project Team: pqc@nist.gov trusted third party, encrypted, and signed by an application, to
be opened if needed and authorized.
Dr. Dustin Moody Dr. Lily Chen Although commercially available physical sources of
(301) 975-8136 (301) 975-6974 randomness are adequate as entropy sources for currently
dustin.moody@nist.gov lily.chen@nist.gov
envisioned applications of the Beacon, NIST is working on
developing a source of verifiably random sequences. Given that
Mr. Ray Perlner Dr. Daniel Smith-Tone it is impossible to construct such sequences in any classical
(301) 975-3357 (502) 852-6010 physical context, CSD is collaborating with the NIST Physical
ray.perlner@nist.gov daniel.smith@nist.gov
Measurement Laboratory (PML) to build a quantum source.
The aim is to use quantum effects to generate sequences
Dr. Yi-Kai Liu that are guaranteed to be unpredictable, even if an attacker
(301) 975-6499
has access to the random source. For more information on this
yi-kai.liu@nist.gov
collaboration, see http://www.nist.gov/pml/div684/random_
numbers_bell_test.cfm.
As the bits posted by the Beacon are public, these are not
NIST Beacon - A Prototype Implementation of a
to be used as secret values, such as cryptographic keys or
Randomness Beacon
seeds for random number generators used in the construction
NIST has implemented a public source of randomness. of cryptographic keys. NIST encourages the community-at-
The prototype uses two independent, commercially available large to research and publish novel ways in which this tool
sources of randomness, each with an independent hardware can be used. Some examples of applications are unpredictable
entropy source. sampling, new authentication mechanisms, and secure multi-
party computation. More details are available at http://beacon.
The Beacon is designed to provide unpredictability, autonomy,
nist.gov.
and consistency. Unpredictability means that users cannot
algorithmically predict bits before they are made available
Contacts:
by the source. Autonomy means that the source is resistant
to attempts by outside parties to alter the distribution of the
Dr. Michaela Iorga Dr. René Peralta
(301) 975-8431 (301) 975-8702
random bits. Consistency means that a set of users can access
michaela.iorga@nist.gov rene.peralta@nist.gov
the source in such a way that they are confident that they all
receive the same random string.
The Beacon posts bit-strings in blocks of 512 bits every Privacy-Enhancing Cryptography Project
60 seconds. Each such value is time-stamped and signed by
NIST and includes the hash of the previous value to chain the The privacy-enhancing cryptography project seeks to promote
sequence of values together. This prevents anyone, even the the use of communication protocols that do not unnecessarily
Beacon itself, from retroactively changing an output packet reveal private information of communicating parties. There are
without being detected. The Beacon keeps all output packets many technical challenges in doing this, as it is typically hard
and makes them available online at https://beacon.nist.gov/ to separate private data from general data (e.g., to convert a
home. third-party-signed date-of-birth certificate into a certificate
that a person is of voting age). Zero-knowledge (ZK) proof
Tables of random numbers have probably been used for
techniques and their variants can be used to accomplish this
multiple purposes at least since the Industrial Revolution. In the
for a large class of assertions. These techniques allow one party
digital age, algorithmic random number generators have largely
to prove to another party that a given statement is true, without
replaced those tables. The NIST Randomness Beacon expands
conveying any additional information apart from the fact that
the use of public randomness to multiple scenarios in which
the statement is indeed true. Although many such ZK protocols
the latter methods cannot be used. The extra functionalities
are practical, adoption by industry is slow. CSD is following the
stem mainly from three features. First, the Beacon-generated
progress of emerging technologies, such as fully homomorphic
numbers cannot be predicted before they are published.
encryption (FHE). FHE could potentially solve a large class of
Second, the public, time-bound, and authenticated nature of
37
Program and Project Achievements for FY 2013

problems, by allowing computation on encrypted data without algorithms tend to be much more computational and resource-
decryption. CSD has also shown that the NIST Randomness intensive and are not easily accommodated in such constrained
Beacon (discussed in the previous section) can be used as a environments.
primitive in secure multi-party computation, such as sealed-bid
As a result, CSD is currently focusing on studying the use
online auctions in which losing bids are never opened.
of the NIST-approved symmetric-key algorithms in constrained
Team members continue to be in close collaboration with environments. Symmetric-key algorithms can perform
the NSTIC program and the Federal Cloud Credential Exchange encryption for confidentiality, and can generate message
(FCCX) project. In this context, CTG has served as evaluators authentication codes (MAC) for authenticity and integrity.
and in technical support roles. Information about NSTIC and NIST has implemented the Advanced Encryption Standard
FCCX is available at http://www.nist.gov/nstic/. (AES) to provide both confidentiality and the AES-based
message authentication code, CMAC mode, for authentication.
Current communication security standards are primarily
Additionally, CTG has implemented the 256-bit version of the
designed for two-party communication. Future protocols,
Secure Hash Algorithm (SHA-256) to provide a Hash-based
such as those for identification, commercial transactions,
Message Authentication Code (HMAC) for authentication.
and social media, will necessitate standards for three-party
communications (e.g., two parties involved in a commercial
The emerging KeccaK algorithm has also been implemented
– both the original 1600-bit permutation that won the hash
transaction and a third party that serves as an enabler of some
competition (see the SHA-3 report above) and the reduced
aspects of the transaction). This is particularly important if
standards are to provide privacy protection. NIST has developed
800-bit permutation. It has been demonstrated that the KeccaK
algorithm allows a more efficient construction for computing
some basic protocols for this purpose. One such protocol allows
MACs than SHA-256, which requires the HMAC construction.
for privacy-preserving identification with the aid of a mediator.
CTG has also investigated other, non-NIST-approved algorithms
In this protocol, the issuer of an assertion, such as “John Smith
for constrained environments.
is an employee of the Department of Commerce,” does not need
to know who the consumer of the assertion is, yet it can encrypt CTG will continue to analyze the resource requirements and
the assertion with a key only known to that consumer (i.e., the performance characteristics of these algorithms, and study
mediator does not get to see the unencrypted assertion). their use as building blocks to perform other cryptographic
functions beyond encryption.
Contact:
Dr. René Peralta Contact:
(301) 975-8702 Mr. Lawrence Bassham
rene.peralta@nist.gov (301) 975-3292
lawrence.bassham@nist.gov
Cryptography for Constrained Environments
ª
New Research Areas in Cryptographic
Pervasive computing is an emerging technical area in which
Techniques for Emerging Applications
many highly constrained devices (e.g., limited resources, such
as program space and RAM) are interconnected, typically
communicating wirelessly with one another, and working in Stream Ciphers
concert to accomplish some task. These systems apply to a
Stream ciphers are symmetric-key cryptographic primitives
wide variety of fields. Sample application areas include sensor
that encrypt plaintext bits individually using a time-varying
networks, medical devices, distributed control systems, and the
transformation. The performance advantages of dedicated
Smart Grid. Security can be very important in each of these
stream ciphers make them more attractive than block ciphers
areas. For example, an unauthorized party should not be able
in stream-cipher-type modes (e.g., AES counter mode) for
to take control of an insulin pump or the brakes on a car. There
some niche software and hardware applications. In 2004,
are also privacy concerns, particularly in the area of Health IT.
the European Network of Excellence for Cryptology (ECRYPT)
Because the majority of the current cryptographic algorithms
announced the ECRYPT Stream Cipher (eSTREAM) project with
were designed for desktop/server environments, many of these
the goal of identifying new stream ciphers that offer some
algorithms cannot operate under these constraints, or if they
performance advantages over AES. The eSTREAM portfolio,
can be made to operate in these constrained environments,
published in 2012, includes: 1) four algorithms for software
their performance is typically not acceptable. A particular
applications: HC-128, Rabbit, Salsa20/12 and Sosemanuk, and
problem is the use of asymmetric (public key) algorithms. These
38
Computer Security Division Annual Report - 2013

2) three algorithms for hardware applications: Grain, Trivium remain unanswered for the foreseeable future, even if quantum
and Mickey. computers are ever built. For example, it is unlikely that the
minimum number of gates necessary to implement the AES can
The primary focus of the project is to study the eSTREAM
be found. In the 12 years since the approval of AES, successive
candidates and other commonly used stream ciphers for
improvements have roughly cut the gate count in half. The
possible standardization. During FY 2013, three internal talks
standard reference for the smallest published circuit for AES
were given: “Stream Ciphers for Constrained Environments,”
is from a study funded by the National Security Agency. CTG
“Authenticated Encryption In Stream Ciphers,” and “Stream
improved on this work significantly by designing combinatorial
Ciphers For Software Applications.” NIST researchers Meltem
circuits that are smaller (meaning that they are likely to use
Sönmez Turan and Santanu Sarkar were two of the co-authors
less energy) and others that are of lower depth (meaning that
of “A Chosen IV Related Key Attack on Grain-128,” published
they are likely to be faster). The general technique was issued a
at the 18th Australasian Conference on Information Security
patent held jointly between NIST and the University of Southern
and Privacy, ACISP 2013. Dr. Turan also published “Related-Key
Denmark.
Slide Attacks On Block Ciphers With Secret Components” at the
Second International Lightweight Cryptography for Security and CTG is also researching circuit-based security metrics for
Privacy workshop, LightSec 2013. cryptographic functions. For a function to be secure (one-
way), it must be the case that any circuit that implements it
After comparing the security and performance of stream
is sufficiently complex. In particular, a function is insecure if
ciphers to block ciphers designed for constrained environments,
it can be implemented by a circuit containing too few Boolean
CTG observed that the gate array requirements for block and
AND gates. This security metric, namely the number of AND
stream ciphers are comparable, but stream ciphers have
gates necessary and sufficient to implement a function, is
a better throughput/area performance characteristic. CTG
referred to as its multiplicative complexity. When comparing
currently believes that well-designed lightweight block ciphers
two cryptographic functions, all other things being equal,
may be more suitable than stream ciphers for constrained
the one with higher multiplicative complexity is preferable.
environments. This determination is based upon the following
Unfortunately, determining multiplicative complexity is
factors: 1) the maturity of literature on block ciphers; 2) the
extremely hard. Mathematicians attempted this in the 1970s,
availability of better tools to analyze the security of block
but the effort had been largely abandoned by the 1980s. CTG
ciphers; 3) reduced round attacks on the stream cipher finalists;
has been able to compute tight bounds for the multiplicative
and 4) lack of flexible key sizes for stream ciphers.
complexity of an important class of functions (the symmetric
In FY 2014, NIST will continue to study the security and
functions). This theory seems to have wide applicability and
performance of software-oriented stream ciphers and block
it points to exciting directions for both theoretical and applied
ciphers designed for constrained environments.
research in security and cryptography.
A partial list of results includes:
Contacts:
Dr. Lily Chen Dr. Meltem Sönmez Turan  The construction of the smallest known circuits for
(301) 975-6974 (301) 975-4391 multiplication in several small finite fields.
lily.chen@nist.gov meltem.turan@nist.gov
 The construction of the smallest known circuits for
binary multiplication (i.e., multiplication of polynomials
Circuit Research of degree n over the Galois Field with two elements).
Cryptographic primitives, such as encryption, digital  The construction of optimal circuits – with respect to
signatures, and hashing, are implemented as electronic circuits multiplicative complexity – for all predicates on four
for a wide class of applications. A variety of metrics is relevant bits. There are 65,536 such predicates. Surprisingly, the
to designing “good” circuits. In particular, minimizing the size multiplicative complexity of all these functions turned
and maximizing the throughput of a circuit closely translate into out to be at most three.
the combinatorial problem of designing circuits with few gates
 Circuits with small multiplicative complexity can be
and short depth. The project team has shown that solving this
used to design more efficient multiparty computation
design problem, even approximately, is “MAX-SNP Complete.”
protocols. Such circuits are useful for protocols that
In practice, this means that it is necessary to settle for heuristics
use either partially homomorphic schemes or fully
that design “good” circuits, as opposed to provably optimal
homomorphic schemes. Some of the published circuits
circuits. It also means that many basic questions are likely to
are being used as benchmarking tools in those areas.
39
Program and Project Achievements for FY 2013

 Significant advances have been made in heuristics for The draft of FIPS 140-3 has had two rounds of public review.
linear circuit complexity, and this is expected to yield The resolutions to the public comments received on the second
improvements to the best-known circuits in this area for draft of FIPS 140-3 include: 1) a description of the assumed threat
years to come. models (e.g., attacker’s level of experience, expectations from
the cryptographic module) for each of the four security levels;
2) an insertion of missing definitions for terms and acronyms;
Contact:
3) changes to the Trusted Channel requirements; 4) the removal
Dr. René Peralta
of the Trusted Role; 5) the inclusion of an identity-based
(301) 975-8702
rene.peralta@nist.gov authentication mechanism that would be allowed at Security
Level (SL) 2; 6) the addition of a self-initiated cryptographic
output capability and remote control capability; 7) the inclusion
ª of additional integrity-technique requirements for the software
Applied Cryptography
components of a cryptographic module; 8) a restructure of the
annexes and enhancement of the requirements for the allowed
Development of Federal Information operator-authentication mechanisms; 9) an update of the list
Processing Standard (FIPS) 140-3, Security of the noninvasive attacks covered by the standard; and 10) an
Requirements for Cryptographic Modules update of the requirements for the allowed modifiable operating
environments.
FIPS 140-2, Security Requirements for Cryptographic
Modules, defines the security requirements for the cryptographic During the process of addressing the public comments
modules that perform cryptographic operations. This standard is received on the second draft, CSD determined that additional
applicable to all federal agencies that use cryptography-based feedback was required from the public to resolve gaps and
security systems to protect sensitive information in computer inconsistencies among the comments received for particular
and telecommunication systems (including voice systems), sections of the second draft of FIPS 140-3. As a result, CSD
as defined in Section 5131 of the Information Technology requested additional public comments in August 2012 on
Management Reform Act of 1996, Public Law 104-106, and the several clearly identified sections.
Federal Information Security Management Act of 2002, Public
During FY 2013, CSD discussed and addressed all comments
Law 107-347. The standard must be used in designing and
received on the identified issues and prepared the updated draft
implementing cryptographic modules that federal departments
FIPS 140-3 for a final internal review. The completion of the
and agencies operate, or that are operated for them under
internal review and submission for approval by the Secretary of
contract.
Commerce are expected in FY 2014.
The current version of the standard is FIPS 140-2. Draft
FIPS 140-3, a revision proposed to supersede FIPS 140-2, has http://csrc.nist.gov/groups/ST/FIPS140_3/
been developed. The draft revision of the standard adds new
security requirements for cryptographic modules to reflect the
Contact:
latest advances in technology and security and to mirror other
Dr. Michaela Iorga
new or updated standards published by NIST in the areas of
(301) 975-8431
cryptography and key management. Additionally, software and michaela.iorga@nist.gov
firmware requirements are addressed in a new topic area while
another new area specifying requirements to protect against
noninvasive attacks is also provided. Authentication
The standard provides four increasing, qualitative levels of
To support the Office of Management and Budget (OMB)
security, intended to cover a wide range of potential applications
Memorandum M-04-04, E-Authentication Guidance for Federal
and environments. The security requirements cover areas
Agencies, NIST developed SP 800-63, Electronic Authentication
related to the secure design, implementation and operation of
Guideline. Its subsequent revision, SP 800-63-1 (published
a cryptographic module. These areas include cryptographic
at the end of FY 2012) significantly expanded the range of
module specification; cryptographic module physical ports and
included technologies, such as Security Assertion Markup
logical interfaces; roles, authentication, and services; software
Language (SAML) assertions. The OMB memorandum defines
security; operating environment; physical security; physical
security – non-invasive attacks; sensitive security parameter four levels of authentication in terms of assurance about the
management; self-tests; life-cycle assurance; and mitigation of validity of an asserted identity. This recommendation covers
other attacks. remote authentication of users (such as employees, contractors,
40
Computer Security Division Annual Report - 2013

or private individuals) interacting with government IT systems NIST, therefore, plans to actively consider another incremental
over open networks. It defines technical requirements for each revision to SP 800-63-2 in response to the issues noted above
of four levels of assurance in the areas of identity proofing, and other issues that can be dealt with in time to assist in the
registration, tokens, management processes, authentication intense ongoing efforts to expand online services.
protocols and related assertions.
Contact:
As more electronic service delivery systems that require
authentication and identity management became available, Dr. Lily Chen
(301) 975-6974
large-scale enrollment and registration issues became a
lily.chen@nist.gov
significant problem for agencies, particularly for health care.
Enrollment and identity proofing result in much of the up-front
cost to agencies of implementing online service delivery and
Wireless Networks and Mobile Device Security
can be a barrier to user adoption. SP 800-63-2, a revision
with changes largely limited to identity proofing and credential
Today, wireless networks often provide connections for
issuance, was published at the end of FY 2013 and is available
mobile devices using multiple and different radio technologies.
at http://csrc.nist.gov/publications/PubsSPs.html.
In such a heterogeneous network, a mobile device may switch
SP 800-63-2 is intended to facilitate more efficient and its between different wireless technologies. The procedure
convenient user enrollment and identity proofing, mainly by of conducting such a switch is called a “handover.” Inter-
exploiting the identity proofing already done for professional technology handover has brought many challenges to existing
licensing, registration, or certification (e.g., for doctors, nurses, security solutions, such as the delays caused by access
lawyers, professional engineers). SP 800-63-2 also reduces the authentication for each handover. CSD has conducted intensive
number of cases where postal mailings are required to confirm research in the security for media-independent handover (MIH)
addresses, saving expense and making registration easier and and has worked closely with the working group of IEEE 802.21
more immediate for users. on security solutions for MIH services. The services specified
in IEEE 802.21 include information service, event service, and
In FY 2014, NIST expects its authentication work to be
command service. The security mechanisms were developed
driven by the needs of the ongoing rapid expansion of online
by Task Group A of IEEE 802.21 and specified in Amendment
service delivery, as experience accumulates and technology
2 of IEEE 802.21, which provide MIH message protection and
progresses. Efforts to develop accreditation programs for
accommodate proactive authentications.
e-authentication have revealed problem areas in the text of
the specifications, while the rapidly growing and evolving use However, the protection mechanisms specified in Amendment
of mobile devices with Internet access and new capabilities 2 of IEEE 802.21 are only applied to unicast messages; that
present both challenges and opportunities. Practical business is, the mechanisms protect messages between a point of
models for large-scale registration and credential issuance service (PoS) and a mobile node. When the services provided
seem to indicate that separate organizations should do both, by the pervasive heterogeneous networks are extended to
and NIST has been urged to make a clearer delineation of other applications, such as Smart Grid applications, the MIH
these activities in a future revision of SP 800-63. Unattended needs to be processed for a group of wireless nodes, such as
biometric authentication is considered problematic for remote smart meters, for the reliability of the services. For example,
authentication in SP 800-63-2, but the relatively high quality the information may need to be delivered to a group of smart
and online video/audio capabilities of the current mobile meters. In this case, the multicast message is used to deliver
devices, as well as the fingerprint readers in some mobile the information. That is, the message is sent from one PoS to
phones, all deserve fresh consideration. Level 4 identity multiple wireless nodes. In some of the application environments,
proofing currently requires an in-person appearance, which is such as sensor networks, the groups are formed dynamically.
often both expensive for agencies and inconvenient and time That is, new nodes can be added to the group, and some nodes
consuming for registrants, particularly in rural or remote areas. may need to be removed. Such groups are managed through
A comment received during the public review of SP 800-63-2 multicast signals. The protection for multicast messages and
urged allowing the use of secure kiosks with high-quality video, group management signals becomes critical. In FY 2013, CSD
document scanners and biometric readers that would be linked has worked with IEEE 802.21 to develop security solutions
to a human registration operator in a registration center, as for group management in Task Group D of IEEE 802.21. The
a viable solution. While this was judged to be too complex to solutions include the mechanisms to distribute group keys and
evaluate in the schedule for SP 800-63-2, the idea is intriguing for the protection of multicast messages. In FY 2014, CSD will
and deserves a detailed consideration. continue to contribute to the development of the IEEE 802.21
41
Program and Project Achievements for FY 2013

Amendment on group management.  Prepared and published a draft revision 4 of Special
Publication (SP) 800-73 (SP 800-73-4), Interfaces for
Contact: Personal Identity Verification. The update to the three-
Dr. Lily Chen part SP details the new PIV Card capabilities introduced
(301) 975-6974 in FIPS 201-2 including Virtual Contact Interface
lily.chen@nist.gov (VCI), a secure channel protocol, an on-card biometric
comparison mechanism and enforcement a minimum
PIN length of six digits.
Identity Management
 Prepared and published a draft revision 4 of SP 800-78
ª (SP 800-78-4), Cryptographic Algorithms and Key Sizes
Personal Identity Verification (PIV)
for Personal Identity Verification. The document has
and FIPS 201 Revision Efforts
been modified to align with SP 800-73-4 (Draft), and
includes the addition of new algorithms and key sizes for
the secure messaging protocol and the addition of test
requirements with the Cryptographic Algorithm Validation
Program (CAVP) validation.
 Started drafting an update to SP 800-79, Guidelines for
the Accreditation of Personal Identity Verification (PIV)
Card Issuers (PCIs), in order to incorporate changes
required by FIPS 201-2.
 Started drafting updates to SP 800-85A, PIV Card
Application and Middleware Interface Test Guidelines,
Figure 8: Personal Identity Verification (PIV)
and FIPS 201 Revision Efforts and SP 800-85B, PIV Data Model Test Guidelines, in
order to align these documents with FIPS 201-2,
In response to Homeland Security Presidential Directive-12 SP 800-73-4, and SP 800-78-4.
(HSPD-12), Policy for a Common Identification Standard for
Federal Employees and Contractors, Federal Information  To accommodate mobile devices, NIST started drafting
Processing Standard (FIPS) 201, Personal Identity Verification SP 800-157, Derived PIV Credentials. As intended by
(PIV) of Federal Employees and Contractors, was developed and FIPS 201-2, derived PIV credentials are part of the set of
was approved by the Secretary of Commerce in February 2005. PIV credentials that can be provisioned directly to mobile
HSPD-12 called for the creation of a new identity credential for devices to enable remote enterprise access from the
federal employees and contractors. FIPS 201 is the technical device.
specification for both the PIV identity credential and the PIV
In FY 2014, CSD will be focusing on updating the relevant
system that produces, manages, and uses the credential. Within
publications associated with FIPS 201-2, including developing
NIST’s Information Technology Laboratory (ITL), this work is a
a new publication, SP 800-156, Representation of PIV Chain-of-
collaborative effort of the Information Access Division (IAD) and
Trust for Import and Export. CSD will also continue to provide
CSD. CSD activities in FY 2013 directly supported the revision
technical and strategic inputs to the PIV related initiatives.
and maintenance of the FIPS 201 standard. CSD performed the
following activities during FY 2013 to revise the standard:
http://csrc.nist.gov/groups/SNS/piv/
 Drafted and published the final release version of FIPS
201-2. FIPS 201-2 reflects the disposition of more than
Contacts:
1,000 comments received from over 40 organizations on
Ms. Hildegard Ferraiolo Dr. David Cooper
the first public comment draft, and over 500 comments
(301) 975-6972 (301) 975-3194
received from 36 organizations on the second public
hildegard.ferraiolo@nist.gov david.cooper@nist.gov
comment draft. NIST coordinated with the Office of
Management and Budget (OMB), the United States
Mr. Salvatore Francomacaro Mr. Ketan Mehta
Access Board, Office of Personnel Management (OPM),
(301) 975 6414 (301) 975-8405
and other U.S. Government (USG) stakeholders before
salvatore.francomacaro@nist.gov ketan.mehta@nist.gov
incorporating changes in the final release version of
FIPS 201-2.
42
Computer Security Division Annual Report - 2013

ª ª
PIV Program Test Cards NIST Personal Identity Verification
Program (NPIVP)
To facilitate the development of applications and middleware
that support the PIV card, CSD developed a set of smart cards The objective of the NIST Personal Identity Verification
for testing. The initial work of developing the test cards was Program (NPIVP) is to validate PIV components for conformance
performed during FY 2011 and was completed during FY to specifications in FIPS 201 and its companion documents.
2012. In late FY 2012, NIST began selling the test cards as The two PIV components that come under the scope of NPIVP
NIST Special Database 33 (http://csrc.nist.gov/groups/SNS/piv/ are PIV Smart Card Application and PIV Middleware. All of the
testcards.html). tests under NPIVP are handled by third-party laboratories that
are accredited as Cryptographic and Security Testing (CST)
Over the course of FY 2013, additional sets of test cards
Laboratories by the NIST NVLAP and are called accredited
were created as the existing inventory of cards were sold.
NPIVP test facilities. As of September 2013, there were nine
In addition, CSD has maintained a mailing list that has been
such facilities.
used by individuals who have purchased the test cards to ask
questions about the cards and to exchange advice on their use. In prior years, CSD published SP 800-85A, PIV Card
Application and Middleware Interface Test Guidelines, to
For further details on the PIV project, see the Personal Identity
facilitate development of PIV Smart Card Application and PIV
Verification (PIV) and FIPS 201 Revision Efforts section.
Middleware that conform to interface specifications in SP
800-73, Interfaces for Personal Identity Verification. CSD also
http://csrc.nist.gov/groups/SNS/piv/testcards.html
developed an integrated toolkit called “PIV Interface Test
Runner” for conducting tests on both PIV Card Application and
PIV Middleware products, and provided the toolkit to accredited
NPIVP test facilities.
NPIVP validation utilized the following versions and documents
throughout FY 2013:
 SP 800-73-3, Interfaces for Personal Identity Verification
 SP 800-85A-2, PIV Card Application and Middleware
Interface Test Guidelines
In FY 2013, two new PIV card application products were
validated for conformance to SP 800-73-3 and received
certificates, bringing the total number of NPIVP validated PIV
Card application products to 36. Three PIV Middleware products
were validated for conformance to SP 800-73-3 and received
certificates, for a total number of 20 NPIVP-validated PIV
Middleware products.
Figure 9: PIV Test Card
In addition, NPIVP is closely involved in ensuring that all
changes in PIV companion documents, such as SP 800-
Contact:
73-3, SP 800-76-2, and SP 800-78-3, are fully reflected in
Dr. David Cooper
Lorie, this image was used in last yeart’hse acnonnfourmaal nrcee pteosrt td. o cGumueenst sS Py o8u00 c-8a5nA- 2u saes twhelel assa me image as used last
(301) 975-3194
subsequently in the PIV Test Runner toolkit consequent on the
david.cooper@nist.gov
year.
expected publication of FIPS 201-2.
http://csrc.nist.gov/groups/SNS/piv/npivp
Contacts:
Thanks.
Dr. Ramaswamy Chandramouli Ms. Hildegard Ferraiolo
(301) 975-5013 (301) 975-6972
mouli@nist.gov hildegard.ferraiolo@nist.gov
Pat
43
Program and Project Achievements for FY 2013

Research in Emerging Technologies interoperability, portability, and security for effective
cloud computing adoption. It is anticipated that final
versions of Volumes I and II of the SP 500-293 will be
ª
Cloud Computing and Virtualization released by the end of the first quarter, FY 2014.
Cloud computing is a model defined in the NIST SP 800-  Led the development of the draft SP 500-299, NIST
145, The NIST Definition of Cloud Computing. The foundational Cloud Computing Security Reference Architecture (SRA).
technologies that facilitate the use of a computing infrastructure It is anticipated that the final version of the document
for cloud computing services is virtualization. At the core of a will be released by the end of the second quarter, FY
virtualized infrastructure is the virtualized host that provides 2014. SP 500-299 defines a modular framework that
abstraction of the hardware (e.g., CPU, memory) enabling provides a formal model and a methodology for the
multiple computing stacks (comprised of the operating secure adoption of cloud computing by applying a Cloud-
adapted Risk Management Framework. The SRA is a
system, middleware, and applications) to be run on a single
security overlay to SP 500-292: NIST Cloud Computing
physical machine. The efficiency of such a dynamic and
Reference Architecture.
distributed processing environment is counter-balanced by the
interoperability, portability, and security challenges inherent
 Provided technical support to several Federal Chief
to this computing environment. NIST is working in parallel on
Information Officer (CIO) Council committees, including
several projects introduced below that aim to accelerate the
the Cloud Computing Executive Steering Committee,
Federal Government’s secure adoption of cloud computing by Cloud Computing Advisory Council, the Information
collaborating with standards bodies, public and private sector Security and Identity Management Workgroup, and the
in developing security, interoperability and portability standards Web 2.0 working group.
and guidance.
CSD Role in the NIST Cloud
Computing Program
During FY 2013, the NIST Cloud
Computing Team continued to promote the
development of publications, national and
international standards, and specifications
in support of the USG’s effective and secure
use of cloud computing as well as providing
technical guidance to USG agencies for
secure and effective cloud computing
adoption.. CSD supports many of the
technical standards activities supported
by the NIST Cloud Computing Program,
with a particular focus on cloud computing
security.
 Participated in the development of
a revised SP 500-291, NIST Cloud
Computing Standards Roadmap.
The document, initially published in
Figure 10: NIST Security Reference Architecture Diagram
2011, was updated in July 2013, and
was incorporated into draft SP 500-293, CSD staff members contributed significantly to several NIST-
US Government (USG) Cloud Computing Technology hosted events:
Roadmap.
 Sixth Cloud Computing Forum and Workshop: Cloud
 Participated in the update to the multi-part draft Computing and Big Data Forum, held in January 2013
document SP 500-293, US Government (USG) Cloud
 Seventh Cloud Computing Forum and Workshop: The
Computing Technology Roadmap (Vol. I, II, and III)
Intersection of Cloud and Mobility Forum, initially
that defines and prioritizes USG requirements for
scheduled for October 1-3, 2013, currently rescheduled
44
Computer Security Division Annual Report - 2013

due to USG shutdown CSD staff members are also actively participating in cloud
computing security standards, primarily through SC 27, which
 First Cloud Forensic Science Workshop, initially
is responsible for cloud computing security standards. CSD
scheduled for October 3, 2013, also rescheduled due to
has provided technical contributions based on SP 500-299 and
USG shutdown.
continues to advocate for secure, non-proprietary solutions.
In support of and advancement of USG cloud computing In FY 2013, the CSD members of the NIST cloud computing
mandates, CSD staff members provided leadership for several team also presented the results of cloud computing research
public work groups operating under the NIST Cloud Computing and development, introduced the standards and specifications
Program. Through these working groups, CSD staff led the under development, and provided status of the NIST Cloud
development of technical guidelines and recommendations that Computing Program in a variety of conferences and workshops.
considered a close collaboration with public, private, academia
and other stakeholders. Policy Machine – Leveraging Access Control for
Cloud Computing
CSD staff chaired or co-chaired several significant cloud
computing efforts in 2013:
Figure 11: Policy Machine operating environment
 Chair of the NIST Cloud Computing Security Working
Group focused the group on development of SP 500-299
(described above), and on key management research.
 Co-Chair, NIST Cloud Computing Forensic Science
Working Group, led development of Digital Forensics
Challenges in a cloud environment.
 Co-Chair, NIST Cloud Computing Standards Roadmap
Working Group, led development of SP 500291, USG
Cloud Computing Standards Roadmap (described above).
 Chair and Vice-Chair, INCITS CS1 (Cybersecurity)
− U.S. Technical Advisory Group (TAG) to the ISO/
In FY 2013, CSD continued the research and development
IEC international committee JTC1/SC27 (IT Security
of a virtualization-based, enterprise-wide controlled delivery
Techniques) − that covers cloud computing taxonomy-
of data services for advanced cloud computing through Access
related standards and cloud computing security
Control. NIST and other members of an Ad Hoc INCITS working
standards.
group are developing a three-part PM standard, under the title
CSD staff members participate in various standards of “Next Generation Access Control” (NGAC), under three sub-
development organizations, two of which are ISO/IEC JTC 1 Sub projects:
Committee 38 – Distributed Application Platforms and Services  Project 2193–D: Next Generation Access Control –
(SC 38) and ISO/IEC JTC 1 Sub Committee 27 – IT Security Implementation Requirements, Protocols and API
Techniques (SC 27). In SC 38, CSD acts as the co-convener Definitions
for a collaborative ISO/ITU-T initiative on cloud computing
taxonomy that includes work on ISO/IEC 17788 – Information  Project 2194–D: Next Generation Access Control –
Technology – Cloud computing – Overview and Vocabulary. Functional Architecture
Notably, the genesis for this international body of work is the
 Project 2195–D: Next Generation Access Control –
widely accepted and used cloud computing definition found in
Generic Operations & Abstract Data Structures
SP 800-145, NIST Definition of Cloud Computing.
ISO/IEC 17788 is closely coordinated with another standards The Policy Machine’s architecture has been adopted by
activity, ISO/IEC 17789 – Information technology – Cloud the ANSI/INCITS and is now available as ANSI INCITS 499 –
Computing – Reference Architecture, which is based on the Information technology – Next Generation Access Control –
widely used and accepted NIST publication, SP 500-292. Both Functional Architecture (NGAC–FA).
ISO/IEC 17788 and 17789 are in the final stages of international
balloting before final publication, which is anticipated in the
first quarter of calendar year 2014.
45
Program and Project Achievements for FY 2013

Cryptographic Key Management Issues Ms. Annie Sokol
in Cloud Infrastructures Co-Chair, Cloud Computing Standards Roadmap
(301) 975-2006
Many of the security capabilities associated with exercise annie.sokol@nist.gov
of cloud service rely on cryptographic operations. The key
management system (KMS) required to support cryptographic Mr. Daniel Benigni
operations for the above tasks can be complex, due to differences Chair, INCITS CS1 (Cybersecurity) - US Technical Advisory Group
(TAG) to the ISO/IEC international committee JTC1/SC27 (IT Security
in ownership and control of underlying infrastructures on
Techniques)
which the KMS and the protected resources are located. CSD
(301) 975-3279
developed NISTIR 7956, Cryptographic Key Management Issues
dbenigni@nist.gov
& Challenges in Cloud Services to discuss these critical issues.
Mr. Salvatore Francomacaro
Virtualization Security & Leveraging
Vice-Chair, INCITS CS1 (Cybersecurity) - US Technical Advisory Group
Virtualization for Security (TAG) to the ISO/IEC international committee JTC1/SC27 (IT Security
Techniques)
CSD has been researching key areas in cloud and virtualization (301) 975-6414
security producing the following papers: salvatore.francomacaro@nist.gov
“Security Assurance Requirements for Hypervisor
Deployment Feature” published as part of the proceedings of Policy Machine - Leveraging Access Control for Cloud Computing
Mr. David Ferraiolo Mr. Serban Gavrila
the 7th International Conference on Digital Society. In FY 2014,
(301) 975-3046 (301) 975-4242
CSD will consider feedback from public comments received and
david.ferraiolo@nist.gov serban.gavrila@nist.gov
publish a (yet unnumbered) Special Publication titled Secure
Management Practices for Protection of Hypervisors. In addition,
Cryptographic Key Management Issues in Cloud Infrastructures
security assurance requirements and security recommendations
Dr. Ramaswamy Chandramouli Dr. Michaela Iorga
will be developed for components of virtualized infrastructure
(301) 975-5013 (301) 975-8431
other than the hypervisor, such as the guest O/S, VM-based mouli@nist.gov michaela.iorga@nist.gov
applications, and the virtual network..
Additional information about the NIST Cloud Computing Virtualization Security & Leveraging Virtualization for Security
Program is available at: Dr. Ramaswamy Chandramouli
(301) 975-5013
mouli@nist.gov
http://www.nist.gov/itl/cloud
http://collaborate.nist.gov/twiki-cloud-computing/bin/view/ ª
CloudComputing/StandardsRoadmap Mobile Device Security
Smart phones have become both ubiquitous and indispensable
http://collaborate.nist.gov/twiki-cloud-computing/bin/view/
for consumers and business people alike. Although these
CloudComputing/CloudSecurity
devices are relatively small and inexpensive, they can be used
for voice calls, simple text messages, sending and receiving
http://collaborate.nist.gov/twiki-cloud-computing/bin/view/
emails, browsing the web, online banking and ecommerce,
CloudComputing/CloudForensics
social networking, and many functions once limited to laptop
and desktop computers. Smart phones and tablet devices have
Contacts for each project:
specialized built-in hardware, such as photographic cameras,
Computer Security Division Role in the NIST Cloud Computing video cameras, accelerometers, Global Positioning System
Program (GPS) receivers, and removable media readers. They also
Dr. Michaela Iorga
employ a wide range of wireless interfaces, including infrared,
Chair, Cloud Computing Security Workgroup
Wireless Fidelity (Wi-Fi), Bluetooth, Near Field Communications
(301) 975-8431
michaela.iorga@nist.gov (NFC), and one or more types of cellular interfaces that provide
network connectivity across the globe. Naturally, just as
consumers and business people can realize productivity gains
from these technologies, so can government agencies.
46
Computer Security Division Annual Report - 2013

Like  any  new  technology,  smart  phones  present  new  Engineering Task Force (IETF).
capabilities, but also a number of new security and privacy
FY 2012 was a significant year for the deployment of IPv6
challenges. As the pace of the technology life cycles continues  in the United States Government. OMB’s Memo of September
to increase, current Information Assurance (IA) standards and
10, 2010, Transition to IPv6, required all government agencies
processes must be updated and new technologies to allow
to “upgrade public/external facing servers and services (e.g.,
| government  | users  to  | employ  the  | latest  technologies  | that  |               |               |                 |           |          |
| ----------- | ---------- | ------------ | --------------------- | ----- | ------------- | ------------- | --------------- | --------- | -------- |
|             |            |              |                       |       | web,  email,  | Domain  Name  | System  (DNS),  | Internet  | Service  |
consumers can use without sacrificing privacy and security.
Provider (ISP) services) to operationally use native IPv6 by
NIST  is  conducting  research  in  new  software  assurance  the end of FY 2012.” NIST worked with the USGv6 Task Force
methodologies for smart phone software (i.e., apps) and is  and with individual government agencies to achieve this goal.
working  with  industry  to  bridge  the  security  gaps  present  NIST developed an online monitor to demonstrate which high-
with today’s smart phones. NIST has developed an online beta  level government domains have met this goal with respect to
Application  Testing  Portal  (ATP)  for  Android  that  examines  DNS services, email, web servers, and Domain Name System
app functionality with respect to agency security and privacy  Security Extensions (DNSSEC).  In  FY  2013, NIST and OMB
guidelines. NIST is working closely with the Defense Advanced  continued to use this monitor to measure USGv6 compliance
Research Projects Agency (DARPA) to transition this software  with OMB’s requirement.
assurance technology to other agencies and making the ATP
|     |     |     |     |     | FY  2014  | will  bring  | additional  OMB  | IPv6  requirements.   |     |
| --- | --- | --- | --- | --- | --------- | ------------ | ---------------- | --------------------- | --- |
software available to industry as open source.
|     |     |     |     |     | Agencies  | will  “upgrade  | internal  client  | applications  | that  |
| --- | --- | --- | --- | --- | --------- | --------------- | ----------------- | ------------- | ----- |
Building on this expertise in mobile app software assurance,  communicate  with  public  Internet  servers  and  supporting
NIST  researchers  are  developing  platform-independent  enterprise networks to operationally use native IPv6 by the end
techniques for identifying mobile malware by analyzing mobile  of FY 2014.” NIST is developing online diagnostic tools to help
app network behavior. NIST researchers are also developing  agencies verify compliance to this requirement.
metrics for evaluating the effectiveness of mobile app security
|     |     |     |     |     | The  NIST  | IPv6  Test  Program,  | whose  | goal  is  to  | provide  |
| --- | --- | --- | --- | --- | ---------- | --------------------- | ------ | ------------- | -------- |
test tools.
assurance on IPv6 product conformance and interoperability,
continues to operate. In FY 2014, NIST will continue to manage
Contacts:
and evolve the USGv6 Test Program.  The NIST program is a
Dr. Steve Quirolgico  Dr. Jeffrey Voas  collaboration  between  CSD  and  the  Advanced  Networking
| (301) 975-8426  |     | (301) 975-6622  |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Technology Division.
| stephen.quirolgico@nist.gov  |     | jeff.voas@nist.gov |     |     |     |     |     |     |     |
| ---------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
http://www.antd.nist.gov/usgv6
Dr. Tom Karygiannis
(301) 975-4728
| karygiannis@nist.gov |     |     |     |     | Contacts:           |     |                         |     |     |
| -------------------- | --- | --- | --- | --- | ------------------- | --- | ----------------------- | --- | --- |
|                      |     |     |     |     | Ms. Sheila Frankel  |     | Mr. Douglas Montgomery  |     |     |
|                      |     |     |     |     | (301) 975-3297      |     | (301) 975-3630          |     |     |
Strengthening Internet Security sheila.frankel@nist.gov  dougm@nist.gov
ª
USGv6: A Technical Infrastructure to
Assist IPv6 Adoption
|     |     | Internet   | Protocol         | (IP)  Version  |     |     |     |     |     |
| --- | --- | ---------- | ---------------- | -------------- | --- | --- | --- | --- | --- |
|     |     | 6  (IPv6)  | is  an  updated  | version  of    |     |     |     |     |     |
the current Internet Protocol, IPv4.
|     |     | The  primary  | motivations  | for  the  |     |     |     |     |     |
| --- | --- | ------------- | ------------ | --------- | --- | --- | --- | --- | --- |
development of IPv6 were to increase
the number of unique IP addresses
available for use and to handle the needs of new Internet
applications and devices. In addition, IPv6 was designed with
the following goals: increased ease of network management
and configuration; expandable IP headers; improved mobility
and security; and quality of service controls. IPv6 has been,
and continues to be, developed and defined by the Internet
47
Program and Project Achievements for FY 2013

Access Control and Privilege Management
ª
Access Control and Privilege
Management Research
With the advance of current computing technologies and
the diverse environments in which these technologies are
used, security issues, such as situational awareness, trust
management, preservation of privacy in access control, and
privilege management systems, are becoming increasingly
complex. Practical and conceptual guidance for these topics is
needed.
In FY 2013, the following research was accomplished for this
Figure 12: Access Control and Privilege Management
project: 1) unified enforcement mechanism of data services
for use by a Policy Machine (PM) for enterprise computing
environment, 2) enhanced the capabilities of the Access Control Contacts:
Policy Tool (ACPT), 3) researched a new fault-detection method Dr. Vincent Hu Mr. David Ferraiolo
for access control rule using Simulated Logic Circuit algorithms, (301) 975-4975 (301) 975-3046
vhu@nist.gov david.ferraiolo@nist.gov
4) researched formal ABAC models, and completed the
development of Special Publication 800-162, Guide to Attribute
Based Access Control (ABAC) Definition and Considerations, Mr. Rick Kuhn
which provides information of function components as well as (301) 975-3337
kuhn@nist.gov
enterprise consideration of ABAC.
CSD expects that this project will:
 Promote (or accelerate) the adoption of community ª
Conformance Verification for Access
computing that utilizes the power of shared resources
Control Policies
and common trust management schemes
Access control systems are among the most critical network
 Provide guidance in implementing access control models
security components. Faulty policies, misconfigurations, or flaws
and mechanisms for standalone or enterprise systems
in software implementation can result in serious vulnerabilities.
The specification of access control policies is often a challenging
 Increase the security and safety of static (connected)
problem. Often a system’s privacy and security are compromised
distributed systems by applying the testing and
due to the misconfiguration of access control policies instead
verification tool for the access control policies
of the failure of cryptographic primitives or protocols. This
 Assist system architects, security administrators, and problem becomes increasingly severe as software systems
security managers whose expertise is related to access become more and more complex and are deployed to manage a
large amount of sensitive information and resources organized
control or privilege policy in managing their systems, and
into sophisticated structures. Identifying discrepancies between
in learning the limitations and practical approaches for
policy specifications and their properties (intended function) is
their applications
crucial because correct implementation and enforcement of
 Provide accurate and efficient fault detection and policies by applications is based on the premise that the policy
correction technology for implementing access control specifications are correct. As a result, policy specifications must
rules and policies undergo rigorous verification and validation through systematic
testing to ensure that the policy specifications truly encapsulate
the desires of the policy authors.
To formally and precisely capture the security properties
that access control should adhere to, access control models
are usually written to bridge the rather wide gap in abstraction
between policy and mechanism. Thus, an access control
model provides unambiguous and precise expression as
48
Computer Security Division Annual Report - 2013

well as reference for design and implementation of security  Provide tools or services for checking the security
requirements. Techniques are required for verifying whether and safety of access control implementation, policy
an access control model is correctly expressed in the access combination, and eXtensible Access Control Markup
controls policies and whether the properties are satisfied in Language (XACML) policy generation
the model. In practice, the same access control policies may
express multiple access control models or express a single  Promote (or accelerate) the adoption of combinatorial
model in addition to extra access control constraints outside of testing for large-system (such as access control system)
the model. Ensuring the conformance of access control models testing
and policies is a nontrivial and critical task.
Started in 2009, CSD developed a prototype system, Access http://csrc.nist.gov/groups/SNS/acpt/
Control Policy Tool (ACPT), which allows a user to compose,
verify, test, and generate access control policies. Contacts:
In FY 2013, ACPT was downloaded by 190 users and Dr. Vincent Hu Mr. Rick Kuhn
organizations. CSD performed prototype testing, enhanced the (301) 975-4975 (301) 975-3337
vhu@nist.gov kuhn@nist.gov
capability of ACPT by adding privilege inheritance algorithms,
applied user cases of Attribute Based, Multi-Level, and
Workflow access control models to test ACPT’s performance,
ª
and compared to other formal method for performance and Metrics for Evaluation of Access Control
usability. CSD also produced a new user manual that explains Systems (Real-Time Access Rule Fault
new capabilities of ACPT. In addition, CSD published a research Detection)
paper related to ACPT.
Specifying correct behaviors of Access Control (AC) policies
In FY 2014, CSD will continue testing, enhance the capability
is a challenging task, especially when an AC policy includes
of ACPT by applying the tool for more complex access control
a large number of rules. Identifying discrepancies between AC
policy combinations, provide model profiles, and improve user
policies and their intended functionalities is crucial because
interfaces. CSD will also update ACPT based on user feedback
correct policy behaviors are based on the premise that the
and suggestions.
policies are correctly specified. Incorrect AC policies result in
faults that not only leak but also disable access to information,
and faults are especially difficult to detect without support of
formal embedded models such as Multi-Level Security (MLS)
and Chinese Wall.
Most research on AC model or policy verification techniques
are focused on one particular model, and almost all of the
research is in applied methods, which require the completed AC
policies as the input for verification or test processes to generate
fault reports. Even though correct verification is achieved and
counterexamples may be generated along with found faults,
those methods provide no information about the source of rule
faults that might allow conflicts in privilege assignment, leakage
of privileges, or conflict of interest permissions. The difficulty in
finding the source of faults is increased especially when the AC
rules are intricately covering duplicated variables to a degree
of complexity. The complexity is due to the fact that a fault
might not be caused by one particular rule; for example, rule x
Figure 13: Conformance Verification
grants subject/attribute s access to object/attribute o, and rule
This project is expected to: y denies the group subject/attribute g, which s is a member
of, access to object o. Such conflict can only be resolved by
 Provide generic paradigm and framework of access
removing either rule x or y, or the g membership of s from the
control model/property conformance testing
policy. But removing x or y affects other rules that depend on
 Provide templates for specifying access control rules in them (e.g., a member of subject group g k is granted access
popular access control models such as Attribute Based, to object o), and removing s’s membership in g will disable
g’s legitimate access to other objects/attributes through the
Multilevel, and Workflow models
49
Program and Project Achievements for FY 2013

membership. Thus, it requires manually analyzing each rule in Contact:
the policy in order to find the correct solution for the fault. Dr. Vincent Hu
(301) 975-4975
To address the issue, CSD researched the AC Rule Logic Circuit
vhu@nist.gov
Simulation (ACRLCS) technique, which enables the AC authors
to detect a fault when the fault-causing AC rule is added to the
policy, so the fixing can be implemented in real time before
ª
adding other rules that further complicate the detecting effort. Attribute Based Access Control
Rather than checking by retracing the interrelations between
rules after the policy is completed, the policy author needs Attribute Based Access Control (ABAC) is a logical access
only check the newly added rule against previous “correct” control methodology where authorization to perform a set of
ones. In ACRLCS, AC rules are represented in a Simulated operations is determined by evaluating attributes associated
Logic Circuit (SLC). The use of simulation may restrict ACRLCS with the subject, object, requested operations, and, in some
implementation on a physical electronic circuit; however, the cases, environment conditions against policy, rules, or
concept can be implemented and computed through simulated relationships that describe the allowable operations for a given
software. set of attributes. ABAC represents a point on the spectrum
In FY 2013, by using the Logic Circuit Simulation (LCS) of logical access control from simple access control lists to
software, CSD researched the SLC for the simulations of rule more capable role-based access (RBAC), and finally to a highly
and inheritance assignments of AC privileges, formal AC model flexible method for providing access based on the evaluation of
implementations, and multiple policy combinations. The result attributes.
is published in the conference paper, Real-Time Access Control
There has not been a comprehensive effort to formally
Rule Fault Detection Using a Simulated Logic Circuit.
define or guide the implementation of ABAC within the Federal
In FY 2014, CSD is planning to further research the Government. This research provides considerations for using
performance of the ACRLCS, and develop a basic reference ABAC to improve information sharing within and among
implementation of the algorithm. Goals for the project include: organizations while maintaining control of that information. The
 Promote the concept of detecting AC policy faults in real research serves a two-fold purpose; first, it aims to provide
time AC rule composing federal agencies with a definition of ABAC and a description of
the functional components of ABAC. Second, it provides planning,
 Provide an innovative method in specifying AC rules design, implementation, and operational considerations for
formed by Boolean logic expressions operated on
employing ABAC within a large enterprise with the goal of
variables of AC rules
improving information sharing while maintaining control of that
information.
 Provide techniques for preventing faults in enforcing
fundamental security properties including Cyclic In FY 2013, CSD completed the writing of SP 800-162,
Inheritance, Privilege Escalation, and Separation of Duty Guide to Attribute Based Access Control (ABAC) Definition
and Considerations. SP 800-162 includes terminology and
 Provide new methods for composing standard mandatory
basic understanding of ABAC; ABAC enterprise employment
AC models such as Role-Based Access Control (RBAC)
considerations during the initiation, acquisition/development,
and MLS as well as some fundamental security
implementation/assessment, and operations and maintenance
properties
phases; and example to demonstrate how ABAC is implemented
in a Web Information Portal. CSD also researched ABAC formal
models, the result will be presented in a NISTIR, which describes
a variety of characteristics and applications of ABAC formal
models.
NIST conducted an Attribute Based Access Control Workshop,
based on the SP 800-162, on July 17, 2013, in partnership
with NSA and the National Cybersecurity Center of Excellence
(NCCoE). About 100 individuals from government, industries,
and academia/research attended the event. The workshop
provided attendees an opportunity to identify, refine, and guide
the many interrelated considerations, challenges, and efforts
needed to develop ABAC guidance; CSD updated SP 800-162
Figure 14: Real-time Access Control - Circuit
from the suggestions collected at the workshop.
50
Computer Security Division Annual Report - 2013

In FY 2014, CSD will continue research of ABAC formal models http://csrc.nist.gov/projects/abac/
as well as details and extended topics of ABAC capabilities,
such as Attribute Engineering/Management, Integration with
Contacts:
Identity Management, Federation, Situation Awareness (Real
Dr. Vincent Hu Mr. David Ferraiolo
Time or Contextual) Mechanism, Policy Management, and
(301) 975-4975 (301) 975-3046
Natural Language Policy translation to Digital Policy. The ABAC vhu@nist.gov david.ferraiolo@nist.gov
project will pursue the following objectives:
 Provide readers the terminology and basic understanding Mr. Rick Kuhn
of ABAC (301) 975-3337
kuhn@nist.gov
 Provide readers with an overview of the current state of
logical access control, a working definition of ABAC, and
Advanced Security Testing and Measurements
an explanation of core and enterprise ABAC concepts
 Assist security policy makers in establishing a business ª
Security Automation and Continuous
case for ABAC implementation, and acquiring an
Monitoring
interoperable set of capabilities
IT organizations operate a diverse set of computing assets
 Assist ABAC developers in developing the operational
which access, route, store, and process information that is
requirements, and overall enterprise architecture
critical to the operations of businesses and the missions of
 Assist ABAC administrators in establishing or refining government agencies. These IT environments are frequently
business processes to support ABAC reconfigured, and are under constant threat of attack. The
wide variety of computing products, the speed of configuration
 Promote adoption of ABAC for more secure and flexible
change, and the diversity of threats require organizations to
method for information sharing in standalone or
maintain situational awareness over their IT assets and to
enterprise environment
utilize this information to make risk-based decisions.
Security automation utilizes standardized data formats
and transport protocols to enable data
to be exchanged between business,
operational, and security systems that
support security processes by:
 Identifying IT assets
 Providing awareness over the
operational state of computing
devices
 Enabling security reference data
to be collected from internal and
external sources
 Supporting analysis processes
that measure the effectiveness
of security controls and provide
visibility into security risks, enabling
risk-based decision making
Commercial solutions built using
security automation specifications enable
the collection and harmonization of vast
Figure 15: ABAC Access Control Mechanism Chart
amounts of operational and security data
into coherent, comparable information
51
Program and Project Achievements for FY 2013

streams to achieve situational awareness that informs timely to provide standardized security solutions to their customers.
and active management of diverse IT systems. Through the These solutions support continuous monitoring and automated,
creation of reference data and guidance, and the international dynamic network defense capabilities based on analysis of data
recognition of flexible, open standards, the NIST security from operational and security data sources and the collective
automation program works to improve the interoperability, action of security components.
broad acceptance, and adoption of security automation
Security automation work has been focused in two areas:
solutions to address current and future security challenges,
evolution and international adoption of the Security Content
creating opportunities for innovation.
Automation Protocol (SCAP) and development of a Continuous
Monitoring building block focused on secure software asset
Specification, Standards, and Guidance Development
management capabilities. The following sections detail this
work.
To support the overarching security automation vision, it is
necessary to have specifications that describe the required
ª
interactions between systems, standards that document Security Content Automation Protocol
international consensus approaches, and guidance that informs (SCAP)
product development and implementation. Through close
work with partners in government, industry, and academia,
NIST continues to facilitate the definition and development of SCAP is a multipurpose protocol
security automation approaches that enable organizations to that provides an automated means to
understand and manage IT security risks. collect and assess the state of devices.
SCAP supports automated vulnerability
During FY 2013, NIST worked to build on previous security
checking, verifying the installation of
automation work by:
patches, checking security configuration
 Establishing working groups in standards development
settings, verifying technical control
organizations to promote international consensus around
compliance, measuring security, and examining systems for
standardized approaches
indicators of compromise. SCAP uses the Extensible Markup
Language (XML) to standardize the format and nomenclature
 Identifying and addressing gaps in the current
by which security software products communicate information
specifications
about software flaws, security configurations, and other aspects
 Evolving existing approaches to achieve greater of device state. SCAP enables security automation content, also
scalability and impact known as “SCAP content,” to be expressed using standardized
formats, identifiers, and scoring models. This content can be
 Providing additional guidance on architectural, design,
used by any tool that is conformant to the specifications, to
and analysis concerns
collect and evaluate the state of software installed on a device.
 Development and maintenance of tools and reference SCAP has been widely adopted by major software and
implementations hardware manufacturers and has become a significant
component of information security management and governance
NIST is currently working with its partners in various standards programs. SCAP-enabled tools are currently being used by the
development organizations, including the International U.S. Government, critical infrastructure companies, academia,
Organization for Standardization (ISO), the Internet Engineering and other businesses, both domestically and internationally.
Task Force (IETF), the Forum of Incident Response and Security Currently, CSD is leveraging SCAP in multiple areas, both to
Teams (FIRST), and the Trusted Computing Group (TCG), to support its own mission and to enable other agencies and
further mature and broaden adoption of security automation private sector entities to meet their goals. For CSD, SCAP is a
specifications, reference data, and techniques. This area of critical component of the SCAP Validation Program, the National
work is focused on evolving security automation specifications Vulnerability Database (NVD), and the National Checklist
to integrate with existing transport protocols to provide for Program (NCP).
secure, interoperable exchange of security automation data.
In September 2012, NIST published SP 800-126 Revision 2,
Additional work is focused on evolving security metrics
The Technical Specification for the Security Content Automation
and providing consensus guidance on security automation
Protocol (SCAP): SCAP Version 1.2, . That document describes
approaches. Through the definition and adoption of security
the 11 component specifications composing SCAP.
automation standards and guidelines, IT vendors will be able
52
Computer Security Division Annual Report - 2013

Since the release of SCAP 1.2, NIST has worked to improve
SCAP 1.2 Specifications
guidance around the SCAP specifications by promoting broader
Specification Description
international adoption of SCAP, encouraging the integration of
Languages SCAP into other standards, and by adapting SCAP to address
Extensible Configuration Used for authoring security specific gaps and challenges. The following work activities
Checklist Description checklists/benchmarks and for were performed during FY 2013:
Format (XCCDF) reporting results of evaluating NIST released draft NISTIR 7946, CVSS Implementation
them Guidance, which guides analysts scoring IT vulnerabilities using
Open Vulnerability and Used for representing system the CVSS Version 2.0. That document is the result of applying the
Assessment Language configuration information, CVSS specification to score over 50,000 vulnerabilities analyzed
(OVAL) assessing machine state, and by the NVD. The report reviews the CVSS base metrics and
reporting assessment results provides guidance for difficult and/or unique scoring situations
and assists vulnerability analysts with scoring particular
Open Checklist Interactive Used for representing checks
types of vulnerabilities by identifying common keywords and
Language (OCIL) that collect information from
phrases that often appear in vulnerability alerts. The report
people or from existing data
includes a collection of scored IT vulnerabilities from the NVD,
stores populated by other data
a justification for each score provided, and a description of the
collection methods
NVD vulnerability scoring process.
Reporting Formats
NIST, in collaboration with industry partners in the IETF,
Asset Reporting Format Used to express information
established the Security Automation and Continuous Monitoring
(ARF) about assets and to define the
(SACM) working group, chartered in July 2013. The current
relationships between assets
scope of work for SACM includes identifying and/or defining
and reports
the transport protocols and data formats needed to support
Asset Identification Used to uniquely identify assets
the collection and evaluation of device state against expected
based on known identifiers and
values and standards for interacting with repositories of security
other asset information
automation content. The initial focus of the SACM working group
Enumerations is on identifying use cases, requirements, and architectural
Common Platform A nomenclature and dictionary models to inform decisions about existing specifications and
Enumeration (CPE) of hardware, operating systems, standards that can be referenced, required modifications or
and applications; a method extensions to existing specifications and standards, and any
to identify applicability to gaps that need to be addressed. This working group provides
platforms a venue for advancing appropriate SCAP specifications into
international standards and addressing identified gap areas.
Common Configuration A nomenclature and
Enumeration (CCE) dictionary of software security For more information, please refer to:
configurations http://datatracker.ietf.org/wg/sacm/charter/
Common Vulnerabilities A nomenclature and dictionary Additionally, NIST collaborated with industry partners to revise
and Exposures (CVE) of security-related software the ISO/IEC 19770-2:2009 standard, Information technology --
flaws Software asset management -- Part 2: Software identification
Measurement and Scoring Systems tag, which establishes a specification for tagging software
Common Vulnerability Used for measuring the relative to support identification and management. This software
Scoring System (CVSS) severity of software flaws identification (SWID) data model provides a mechanism for
software publishers to provide authoritative identification,
Common Configuration Used for measuring the relative
categorization, software relationship (e.g., dependency,
Scoring System (CCSS) severity of device security
bundling, and patch), file footprint details, and other software
(mis-)configuration issues
metadata for software they publish. This information enhances
Content and Result Integrity
SCAP use cases by providing authoritative information for
Trust Model for Security Guidance for using digital creation of CPE names, targeting of checklists, and associating
Automation Data (TMSAD) signatures in a common trust software flaws to products based on a defect in a software
model applied to security library or executable.
automation specifications
53
Program and Project Achievements for FY 2013

ª
NIST also worked with government and industry partners Continuous Monitoring
in the TCG to define a number of specifications related to
the Trusted Network Connect (TNC) protocols. The first such In September 2010, the Department of Homeland Security
publication is the TNC SCAP Messages for IF-M specification (DHS) released the Continuous Asset Evaluation, Situational
that supports carrying SCAP content and results over the TNC Awareness and Risk Scoring (CAESARS) Reference Architecture
protocols. The second is the TNC Enterprise Compliance Profile Report. This report identifies commonality and strengths in
(ECP) and related specifications that support the exchange of the custom approaches used by civilian agencies to provide
SWID data over the TNC protocols. The ECP enables collection solutions that enable the continuous monitoring of IT systems.
of SWID data from a device for use by external tools to provide This report identifies “essential functional components
software inventory information. SCAP and SWID data collected of a security risk scoring system, independent of specific
using these mechanisms may be optionally used for network technologies, products, or vendors.” It describes the use of
access control decision making, allowing device state to be security automation specifications, such as the SCAP, to enable
evaluated when devices connect and on an ongoing basis continuous monitoring solutions.
thereafter. In October 2010, the Federal Chief Information Officer
For more information on these specifications, please visit: Council’s Information Security and Identity Management
Committee’s (ISIMC) subcommittee on Continuous Monitoring
http://www.trustedcomputinggroup.org/resources/tnc_
and Risk Scoring saw the need to create a technical initiative
scap_messages_for_ifm, and
to expand upon the CAESARS architecture to better scale it to
http://www.trustedcomputinggroup.org/resources/tnc_ large enterprises (e.g., the entire U.S. Government). A team of
endpoint_compliance_profile_specification. researchers from the NSA Information Assurance Directorate
(IAD), the DHS Federal Network Security CAESARS team, and
Finally, NIST participated in two Forum of Incident Response
NIST’s Information Technology Laboratory (ITL) worked together
and Security Teams (FIRST) Special Interest Groups (SIG). The
to respond to this need. The draft CAESARS Framework
CVSS SIG (CVSS-SIG) focused on defining CVSS Revision 3,
Extension (CAESARS-FE) described by Draft NISTIR 7756,
which is intended to implement improvements to the scoring
CAESARS Framework Extension: An Enterprise Continuous
model based on community feedback. The CVSS-SIG plans to
Monitoring Technical Reference Architecture, is the output of
release a draft of the revision in early FY 2014, with a completed
this collaboration.
approved specification expected in the summer of 2014. The
second SIG, the Vulnerability Reporting and Data eXchange Draft NISTIR 7756 presents an enterprise continuous
SIG (VRDX-SIG), researches and recommends methods for monitoring (ConMon) technical reference architecture that
identifying and exchanging vulnerability information across extends the framework provided by the DHS’s CAESARS
disparate vulnerability databases. architecture. The primary goal of this effort is to enable enterprise
ConMon by supporting the development and deployment
For more information, please visit:
of capabilities that support automated, enterprise-wide
http://www.first.org/global/sigs.
ConMon functions. The concepts, workflows, and subsystems
Through work with international SDOs, SCAP and related
presented in this document can be used by organizations
security automation capabilities are expected to evolve and
seeking to establish federated queries, orchestration of data
expand in support of the growing need to define and measure
collection tasks, data analytics, and presentation and reporting
effective security controls, assess and monitor ongoing
capabilities across a diverse portfolio of security and IT
aspects of information security, remediate noncompliance,
products. CAESARS-FE supports IT operations and network
and successfully manage systems in accordance with the Risk
defense capabilities, with compliance reporting as a byproduct
Management Framework described in SP 800-37 Revision 1,
of actual security monitoring and improvement. CAESARS-FE
Guide for Applying the Risk Management Framework to Federal
enables organizations to design, develop, and deploy ConMon
Information Systems: A Security Life Cycle Approach.
capabilities by leveraging their existing security and IT tools
while minimizing custom tool integration efforts. CAESARS-
http://scap.nist.gov/
FE defines the requisite functionality needed to ensure
the interoperability of vendor products while continuing to
Contact:
encourage security tool vendor participation and innovation.
Mr. David Waltermire
To advance the state of the art in continuous monitoring
(301) 975-3390
capabilities and to further interoperability within commercially
david.waltermire@nist.gov
available tools, CSD is working within the international
54
Computer Security Division Annual Report - 2013

standards development community to establish working groups Security Automation Reference Data
and to author and comment on emerging technical standards in
Through the NVD and the National Checklist Program (NCP),
this area. The CAESARS-FE reference architecture will evolve
NIST is providing relevant and important reference data in the
as greater consensus is developed around interoperable,
areas of vulnerability and configuration management. SCAP,
standards-based approaches that enable continuous monitoring
and the programs that leverage it, are moving the information
of IT systems. In early FY 2014, CSD plans to release an
assurance industry towards being able to standardize
update to NISTIR 7756 that provides additional guidance for
communications, and the collection and storage of relevant data
development of ConMon architectures and solutions based on
in standardized formats, and provide automated means for the
ongoing standards activities and feedback.
assessment and remediation of systems for both vulnerabilities
The NIST National Cybersecurity Center of Excellence (NCCoE)
and configuration compliance.
is also working to develop a series of ConMon building blocks
that demonstrate cybersecurity solutions that apply across ª
National Vulnerability Database (NVD)
multiple industry sectors. The first building block, currently
under development, proposes a standardized approach to
Security automation reference data is currently housed
software asset management, providing an organization with
within the NVD. The NVD is the U.S. Government repository
an integrated view of software throughout its lifecycle. The
of security automation data based on security automation
building block will support:
specifications. This data provides a standards-based foundation
 Authorization and verification of software installation for the automation of software asset, vulnerability, and security
media – Verifies that the media is from a trusted configuration management; security measurement; and
software publisher and that the installation media has compliance activities. This data supports security automation
not been tampered with efforts based on the SCAP. The NVD includes databases of
security configuration checklists for the NCP, listings of publicly
 Software execution whitelisting – Verifies that the
known software flaws, product names, and impact metrics. A
software is authorized to run and has not been tampered formal validation program tests the ability of vendor products to
with use some forms of security automation data based on a product’s
conformance in support of specific enterprise capabilities.
 Publication of installed software inventory – A device
that securely communicates what software is installed to SCAP defines the structure of standardized software flaws
an organization-wide database and security configuration reference data, also known as
SCAP content. This reference data is provided by the NVD
 Software inventory-based network access control – A (http://nvd.nist.gov/).
device’s level of access to a network is determined by
The NVD is the U.S. Government repository of standards-
what software is or is not present on the device and
based vulnerability management reference data. The NVD
whether its patches are up to date
provides information regarding security vulnerabilities and
configuration settings, vulnerability impact metrics, technical
The building block document, Continuous Monitoring Building
assessment methods, and references to remediation assistance
Block: Software Asset Management, can be viewed at http://
and IT product identification data. As of October 2013, the NVD
csrc.nist.gov/nccoe/Building-Blocks/conmon.html. In FY 2014,
contained the following resources:
the team will continue to develop this building block and to work
with vendors to develop a solutions demonstration. Through this  Over 58,000 vulnerability advisories with an average of 8
process, CSD provides publically available descriptions of the new vulnerabilities added daily
practical steps needed to implement the technical approaches
 52 SCAP-expressed checklists containing thousands
defined by the building block.
of low-level security configuration checks that can be
used by SCAP-validated security products to perform
Contact:
automated evaluations of system state
Mr. David Waltermire
(301) 975-3390
 173 non-SCAP security checklists (e.g., English prose
david.waltermire@nist.gov
guidance and configuration scripts)
 248 U.S. Computer Emergency Readiness Team (US-
CERT) alerts, 2,771 US-CERT vulnerability summaries,
and 8,140 SCAP machine-readable software flaw checks
55
Program and Project Achievements for FY 2013

 Product dictionary with over 79,000 operating system, numerous organizations. When an attack has the potential to
application, and hardware name entries affect computing systems in multiple organizations, coordination
among separate CSIRTs can make it possible to limit the
 42,954 vulnerability advisories translated into Spanish
damage caused by an attack, speed recovery operations, and
maintain a higher level of operational security.
NVD is hosted and maintained by NIST and is sponsored by
the Department of Homeland Security’s US-CERT. CSD is working with the Department of Homeland Security
(DHS) to develop guidance on Computer Security Incident
The use of SCAP data by commercial security products,
Coordination (CSIC). The goal of CSIC is to help diverse
deployed in thousands of organizations worldwide, has
collections of organizations to effectively collaborate in the
extended NVD’s effective reach. Increasing demand for NVD
handling of computer security incidents. Effective collaboration
XML data feeds and SCAP-expressed content from the NVD
raises numerous issues on how and when to share information
website demonstrates increased adoption of SCAP.
between organizations, and in what form information should be
NVD continues to play a pivotal role in the Payment Card
shared. Because different organizations may have substantially
Industry (PCI) efforts to mitigate vulnerabilities in credit card
different capabilities for responding to attacks, diagnosing
systems. PCI mandates the use of NVD vulnerability severity
causes, and handling sensitive attack-related information,
scores in measuring the risk to payment card servers worldwide
guidance must provide a framework to help organizations
and for prioritizing vulnerability patching. PCI’s use of NVD
interoperate despite their organizational differences.
severity scores helps enhance credit card transaction security
This initiative will develop a NIST SP that provides guidance
and protects consumers’ personal information.
on how organizations can develop collaborative capabilities in
Throughout FY 2013, NVD continued to provide access to
advance of incidents in order to be prepared to operate swiftly
vulnerability reference data and security checklists. CSD updated
and with coordination during incidents. The guidance will
the NVD to support the latest CPE Naming specification, CPE
cover data handling considerations, such as sensitivity, data
2.3, and produces the official CPE dictionary in multiple formats.
collection and retention practices, data standards, redaction,
NVD now hosts the list of configuration items, complementing
and use of tools such as anonymization. The guidance will help
the configuration checklist data already maintained. NVD data
incident responders to understand when data can be shared,
is substantially increasing the security of networks worldwide
when it should not be shared, and when sharing is essential.
and it is a fundamental component of CSD’s security automation
A key element in the approach is the concept of an integrated,
infrastructure. CSD plans to update and improve the NVD in
functionally-composed incident response team. The objective
FY 2014 to include improvements in user navigation, addition
of a functionally-composed team is to enable each organization
of references to the SP 800-53 Revision 4 security controls
to contribute most in technical areas where that organization
content, and the ability to search, browse, and download
has higher relative levels of expertise and readiness, thus
common configuration enumeration (CCE) list data.
speeding incident detection, analysis, containment, eradication,
and recovery.
http://nvd.nist.gov
In FY 2014, CSD plans to complete a Draft Special Publication
providing guidance for Computer Security Incident Coordination
Contact:
and organize a workshop focused on the issues of incident
Mr. Harold Booth
coordination.
(301) 975-8441
harold.booth@nist.gov
Contacts:
Mr. Lee Badger Mr. David Waltermire
(301) 975-3176 (301) 975-3390
ª
Computer Security Incident Coordination lee.badger@nist.gov david.waltermire@nist.gov
Recognizing that even well-engineered and administered
computing systems are sometimes successfully attacked, it is ª
Incident Handling Automation
important to establish and maintain processes and procedures
to recover from attacks when defensive mechanisms are
In recent years, security threats to digital systems have
breached. NIST Special Publication (SP) 800-61 Revision 2,
become more prevalent and more sophisticated. While some
Computer Security Incident Handling Guide, provides guidance
security threats are generic in nature, others are targeted at
on establishing and operating a Computer Security Incident
specific organizations, assets, and missions. Although computer
Response Team (CSIRT). A wide-ranging attack may affect
56
Computer Security Division Annual Report - 2013

ª
security defenses may forestall many threats, not all can be National Checklist Program (NCP)
prevented, and organizations must therefore develop incident
handling capabilities. Incident handling encompasses a variety There are many threats to information technology (IT), ranging
of tasks ranging from preparation prior to an incident, to timely from remotely launched network service exploits to malicious
detection and analysis of an incident, to recovery and repair code spread through infected emails, websites, and downloaded
from the effects of an incident, to post-incident learning and files. Vulnerabilities in IT products are discovered daily, and
improvement. These tasks need to be performed both internally many ready-to-use exploitation techniques are widely available
within specific organizations and externally via coordination on the Internet. Because IT products are often intended for a
across teams of collaborating organizations. wide variety of audiences, restrictive security configuration
controls are usually not enabled by default. As a result, many
In the past year, NIST worked with the Department of Homeland
out-of-the box IT products are immediately vulnerable. In
Security’s United States Computer Emergency Readiness Team
addition, identifying a reasonable set of security settings that
(US-CERT) to develop Revision 2 of NIST Special Publication
achieve balanced risk management is a complicated, arduous,
800-61, Computer Security Incident Handling Guide. This
and time-consuming task, even for experienced system
document provides guidance on developing incident handling
administrators.
capabilities. The document explains the nature of incidents
and incident handling processes, the structure and operation To facilitate development of security configuration checklists
of Computer Security Incident Response Teams (CSIRT), and for IT products and to make checklists more organized and
provides guidance on handling an incident and coordinating usable, NIST established the National Checklist Program
with other organizations. (NCP) in furtherance of its statutory responsibilities under
the Federal Information Security Management Act (FISMA) of
SP 800-61 Revision 2 focuses primarily on manual (human)
2002, Public Law 107-347, and also under the Cyber Security
processes for incident handling and the effective use of human
Research and Development Act, which tasks NIST to “develop,
judgment, guided by applicable regulation and law, regarding
and revise as necessary, a checklist setting forth settings and
which incident-related information is significant and which
option selections that minimize the security risks associated
incident-related information may be shared. The growing
with each computer hardware or software system that is, or is
volume of security threats, however, is driving the need for a
likely to become, widely used within the Federal Government.”
more agile incident-handling framework that can operate at
In February 2008, revised Part 39 of the Federal Acquisition
differing scales and speeds as required.
Regulation (FAR) was published. Paragraph (d) of section 39.101
Working in concert with the DHS, NIST is expanding existing states, “In acquiring information technology, agencies shall
incident handling guidance to enable coordinated information include the appropriate IT security policies and requirements,
sharing across disparate CSIRTs operating at differing scales including use of common security configurations available
and speeds. This work will include the analysis of standardized from the NIST website at http://checklists.nist.gov. Agency
incident handling data models and the incorporation of these contracting officers should consult with the requiring official to
data models, as appropriate, into both CSIRT information sharing ensure the appropriate standards are incorporated.”
processes as well as incident/threat knowledge repositories.
In Memorandum M-08-22, the Office of Management and
This work will describe how mature CSIRTs may operate in a
Budget (OMB) mandated the use of SCAP-validated products for
diverse information-sharing network with both operational and
continuous monitoring of Federal Desktop Core Configuration
strategic CSIRTs, as well as industry knowledge repositories.
(FDCC) compliance. The NCP strives to encourage and make
This may include selective use of security automation where
simple agencies’ compliance with these mandates.
applicable.
The goals of the NCP are to:
In FY 2014, this work will develop Draft SP 800-150,
Coordinated Computer Security Incident Handling Guidance.  Facilitate development and sharing of checklists by
providing a formal framework for checklist developers to
Contacts: submit checklists to NIST
Mr. Lee Badger Mr. David Waltermire
 Provide guidance to developers to help them create
(301) 975-3176 (301) 975-3390
standardized, high-quality checklists that conform to
lee.badger@nist.gov david.waltermire@nist.gov
common operations environments
 Help developers and users by providing guidelines for
making checklists better documented and more usable
57
Program and Project Achievements for FY 2013

 Encourage software vendors and other parties to develop is submitted. The submission is validated upon review, and a
checklists report is returned to the submitting organization, verifying either
acceptance or rejection based on the criteria requirements.
 Provide a managed process for the review, update, and
For instance, Tier III and Tier IV checklists require validation
maintenance of checklists
using the SCAP Content Validation Tool (this tool is available for
download via http://scap.nist.gov/revision/1.2/#tools).
 Provide an easy-to-use repository of checklists
The NCP is defined in SP 800-70 Revision 2, National
 Encourage the use of automation technologies (e.g.,
Checklist Program for IT Products—Guidelines for
SCAP) for checklist application
Checklist Users and Developers, which can be found at
http://csrc.nist.gov/publications/PubsSPs.html.
There are 225 checklists posted on the website; 52 of the
checklists are SCAP-expressed and can be used with SCAP-
http://checklists.nist.gov
validated products. In FY 2013, a total of 16 SCAP-expressed
checklists were contributed to the NCP from other federal
Contact:
agencies and product vendors.
Mr. Stephen Quinn
Organizations can use checklists obtained from the NCP
(301) 975-6967
website for automated security configuration patch assessment.
stephen.quinn@nist.gov
NCP currently hosts SCAP checklists for Internet Explorer 9.0,
Internet Explorer 10.0, Office 2010, Red Hat Enterprise Linux,
Windows 7, Windows 8, Windows Server 2012, and other ª
United States Government Configuration
products.
Baseline (USGCB) / FDCC Baselines
To assist users in identifying automated checklist content,
NCP groups checklists into tiers, from Tier I to Tier IV. NCP The United States Government Configuration Baseline
uses the tiers to rank checklists according to their automation (USGCB) initiative creates security configuration baselines for
capability. Tier III and IV checklists include SCAP content and information technology (IT) products widely deployed across the
have been validated by the SCAP content validation tool as federal agencies. The project evolved from the Federal Desktop
conforming to the requirements outlined in SP 800-126, The Core Configuration (FDCC) mandate originally described in a
Technical Specification for the Security Content Automation March 2007 memorandum from the U.S. White House Office
Protocol (SCAP). Tier IV checklists are considered production- of Management and Budget (Memorandum M-07-11). USGCB
ready and have been validated by NIST or a NIST recognized helps to improve information security and reduce overall IT
authoritative entity to ensure, to the maximum extent possible, operating costs by providing commonly accepted security
interoperability with SCAP-validated products. configurations for major operating systems.
Tier III checklists use SCAP content to document security Through the National Checklist Program described in SP
settings and should be compatible with SCAP-validated 800-70 Revision 2, National Checklist Program for IT Products:
products. Tier II checklists document recommended security Guidelines for Checklist Users and Developers, a baseline
settings in a machine-readable, nonstandard format, such as submitter may express interest in submitting a candidate for
a proprietary format or a product-specific configuration script. use in the USGCB program.
Tier I checklists are prose-based and contain no machine-
CSD provides ongoing support for the USGCB automation
readable content. Users can browse the checklists based on
content, including the creation of patch updates, assisting
the checklist tier, IT product, IT product category, or authority,
USGCB users in continuously monitoring and assessing security
and also through a keyword search that searches the checklist
compliance of information systems. This ongoing monitoring
name and summary for user specified terms. The search results
element supports the Risk Management Framework described in
show the detailed checklist metadata and a link to any SCAP
SP 800-37 Revision 1, Guide for Applying the Risk Management
content for the checklist, as well as links to any supporting
Framework to Federal Information Systems: A Security Life
resources associated with the checklist.
Cycle Approach.
To assist checklist developers, the NCP provides both
During FY 2013, a supplemental USGCB SCAP 1.0 content for
manual and automated interfaces to facilitate submission and
Microsoft Windows XP, Vista and 7 was released to correct an
maintenance processes. The manual interface consists of a
issue with directory server performance caused by the existing
web application that guides the submitter through the data
USGCB content.
entry process to ensure that all of the required information
58
Computer Security Division Annual Report - 2013

The USGCB Program will continue in FY 2014 to provide Common Configuration Enumeration (CCE) number, which will
ongoing maintenance of the baseline artifacts and to consider aid in long-term tracking of the setting. Once these settings
additional applicable platforms. are vetted and curated by Apple, these settings will be tested
and included in the configuration baselines. In addition, CSD
Contact: is producing a draft guideline, Guide to Securing Apple OS X
Mr. Stephen Quinn 10.8 Systems for IT Professionals. This guidance, similar in
(301) 975-6967 structure to the NIST SP 800-68, Windows XP Security Guide,
stephen.quinn@nist.gov will provide detailed information about the security of Apple OS
X 10.8, and will provide security configuration guidelines for the
Apple OS X 10.8 operating system.
ª
Apple OS X Security Configuration
In FY 2014, CSD plans to complete the scripts for the
remaining initial settings and post them to the Apple community
CSD is working with Apple to develop secure system
for feedback. CSD will also continue the development of
configuration baselines supporting different operational
the draft Guide to Securing Apple OS X 10.8 Systems for IT
environments for Apple OS X, Version 10.8, Mountain Lion.
Professionals; this documentation will then be made available
These configuration guidelines will assist organizations with
for public comment.
hardening OS X technologies and provide a basis for unified
controls and settings for OS X workstations and for mobile
Contacts:
system security configurations for federal agencies.
Mr. Lee Badger Ms. Kathy Ton-Nu
The configurations will be based on a collection of resources, (301) 975-3176 (301) 975-3361
including the existing NIST OS X configuration guidance, the OS lee.badger@nist.gov kathy.ton-nu@nist.gov
X security configuration guide, the Department of Defense (DoD)
Mr. Lawrence Keys
OS X Recommended Settings, and the Defense Information
(301) 975-5482
Systems Agency (DISA) OS X Security Technical Implementation
lawrence.keys@nist.gov
Guide (STIG). Our team is aggregating appropriately 400 initial
settings, determining which settings will be included in the
configuration baseline, and determining appropriate values for Validation Programs
each included setting. As the desired configuration items are
established, our team is developing shell scripts that apply the ª
Security Content Automation Protocol
settings to an OS X 10.8 system. The settings are organized
(SCAP) Validation Program
into three key baselines, which are appropriate for different
environments:
The SCAP Validation Program performs conformance testing
 Enterprise baseline is appropriate for centrally managed, to ensure that products correctly implement SCAP as defined
networked systems. in SP 800-126 Revision 2, The Technical Specification for the
Security Content Automation Protocol (SCAP): SCAP Version 1.2.
 Small Office Home Office baseline is appropriate for
Conformance testing is necessary because SCAP is a complex
systems that are deployed remotely but need to connect
specification consisting of eleven individual specifications
to enterprise networks.
that work together to support various use cases. A single
error in product implementation could result in undetected
 Special Security Limited Functionality baseline is
vulnerabilities or policy noncompliance within agency and
appropriate for systems where security requirements are
industry networks.
more stringent and where the implementation of security
safeguards is likely to reduce functionality. In FY 2013, CSD updated the SCAP Validation Program to
support the testing of products against SCAP version 1.2. The
SCAP, defined and discussed in other sections of this report,
division published NISTIR 7511 Revision 3, Security Content
is used to express configuration settings and check system
Automation Protocol (SCAP) Version 1.2 Validation Program
configuration compliance.
Test Requirements, which introduces a modular approach
During FY 2013, CSD provided a block of initial settings with respect to the platforms that vendors may support. Public
to Apple and these settings are being posted for the Apple validation test content was published , thus providing reference
community on a periodic basis for public review, discussion, materials that support conformance testing by industry and
correction and agreement. Each setting will have a designated end users. The SCAP 1.2 public test content provides vendors
59
Program and Project Achievements for FY 2013

with the materials required for quality assurance testing prior the public can choose cryptographic modules and/or products
to entering formal SCAP testing by an NVLAP accredited SCAP containing cryptographic modules from the CMVP Validated
lab. The SCAP Validation Program resources web page was Modules List and have confidence in the claimed level of
introduced to provide the public with a centralized location for security and assurance of correct implementation.
all resources and information necessary to prepare products
Cryptographic algorithm and cryptographic module testing
for SCAP 1.2 validation. The resources provided include
and validation are based on underlying published standards .
documentation, a list of Frequently Asked Questions (FAQ),
As federal agencies are required to use validated cryptographic
the SCAP test content, and tools for validating and processing
modules for the protection of sensitive non-classified
SCAP data streams. CSD updated the SCAP Content Validation
information, the validated modules and the validated algorithms
Tool (SCAPVal), used for validating that data streams adhere to
that the modules contain represent the culmination and delivery
the SCAP specification, to include support for SCAP 1.2. The
of the division’s cryptography-based work to the end user.
update for SCAP 1.2 included open source SCAP reference
The CAVP and the CMVP are separate, collaborative
implementation tools that are used to process SCAP data
programs based on a partnership between NIST’s CSD and the
streams.
Communication Security Establishment Canada (CSEC).. The
End users may use the SCAP Validation Program resources
CAVP and the CMVP validate algorithms and modules used in
page to learn more about the validation program and download
a wide variety of products, including secure Internet browsers,
reference materials. The program currently has seven
secure radios, smart cards, space based communications,
independent laboratories accredited for SCAP 1.2 product
munitions, security tokens, mobile phones, network and storage
testing and several products are undergoing testing.
devices, and products supporting Public Key Infrastructure
The SCAP Validation Program will expand in FY 2014 to (PKI) and electronic commerce. A module may be a standalone
provide enhanced testing support and will focus on increased product, such as a virtual private network (VPN) or smart card or
test coverage by SCAP reference implementation tools. it could be a module used in several products, such as a toolkit.
Expansion plans also include improvements in automated As a result, a small number of modules may be incorporated
testing capabilities. within hundreds of products. The CAVP validates cryptographic
algorithms that may be integrated in one or more cryptographic
http://scap.nist.gov/validation/ modules.
The CAVP and CMVP validation programs provide documented
Contact: methodologies for conformance testing through defined sets
Ms. Melanie Cook of security requirements. For CAVP, the validation system
(301) 975-5259 documents are designed for each FIPS-approved and NIST-
melanie.cook@nist.gov
recommended cryptographic algorithm. See website for a
listing. Security requirements for the CMVP are found in FIPS
140-2, Security Requirements for Cryptographic Modules
ª
Cryptographic Programs and Laboratory and the associated test metrics and methods in Derived Test
Accreditation Requirements for FIPS 140-2. The four Annexes to FIPS 140-2
reference the underlying cryptographic algorithm standards or
The Cryptographic Algorithm Validation Program (CAVP) and
methods. The CMVP developed Derived Test Requirements for
the Cryptographic Module Validation Program (CMVP) were
FIPS 140-2 defines the test metrics and methods and ensures
developed by NIST to support the needs of the user community
repeatability of tests and equivalency in results across the
for strong, independently tested, and commercially available
testing laboratories.
cryptographic algorithms and modules. Through these programs,
The CMVP reviews the cryptographic modules validation
NIST works with private and governmental sectors and the
requests and, as a byproduct of the review, is attentive to
cryptographic community to achieve security, interoperability,
emerging and/or changing technologies and the evolution
and assurance of correct implementation. The goal of these
of operating environments and complex systems during the
programs is to support the use of validated algorithms, and
modules and to provide federal agencies with a security metric module validation review activities. Likewise, the CAVP reviews
to use in procuring cryptographic modules. The testing carried the cryptographic algorithm validation requests submitted by
out by independent third-party laboratories accredited by the the accredited laboratories. With these insights, the CAVP and
NIST National Voluntary Laboratory Accreditation Program CMVP can perform research and development on evolving test
(NVLAP) and the validations performed by the CMVP and CAVP metrics and methods. Based on this research, the CAVP and
programs provide this metric. Federal agencies, industry, and CMVP publish Implementation Guidance to assist vendors,
60
Computer Security Division Annual Report - 2013

General Flow of FIPS 140-2 Testing and Validation
Vendor selects a lab; Cryptographic Module
NVLAP Accredited Submits module for testing;
Module IUT Vendor
FIPS 140-2
1
CST Lab
Lab submits
questions for
guidance and Issue validation
clarification certificate
Test for conformance NIST/CSEC issue (via lab to the
To FIPS 140-2; 1a testing and vendor)
Completes test report 4 Module Implementation
Coordination Guidance 5a
Cost Recovery Fee
Received Pri or to
Validation
Module’s
Test Report 2 CST Test Report to NIST/CSEC for validation; NIST/CSEC
Module Review Pending
3
List of Validated Reviewer Assig ned
FIPS 140-2 5 F N i I n S a T l i a za d t d io s n m ; odule to Module Under R eview
Modules validated modules list at
www.nist.gov/cmvp
Figure 16: General Flow of FIPS 140-2 Testing and Validation
testing laboratories, and the user community. This guidance The CAVP and the CMVP have stimulated improved quality and
provides clarity, consistency of interpretation, and insight for security assurance of cryptographic modules. The latest set of
successful conformance testing, validation, and revalidation. statistics, which are collected quarterly from each of the testing
laboratories, shows that 7% of the cryptographic algorithms
and 35% of the cryptographic modules brought in for voluntary
testing had security flaws that were corrected during testing.
To date, over 2,004 cryptographic module validation certificates
have been issued, representing over 4,811 modules that were
validated by the CMVP. These modules have been developed by
more than 425 domestic and international vendors.
Figure 17: FIPS 140-1 and FIPS 140-2 Validated
Modules by Year and Level
The unique position of the validation programs gives the
CMVP the opportunity to acquire insight during the validation
review activities and results in practical, timely, and up-to-date
guidance that is needed by the testing laboratories and vendors
to move their modules out to the user community in a timely
Figure 18: FIPS 140-1 and FIPS 140-2 Validation
and cost-effective manner and with the assurance of third-
Certificates by Fiscal Year and Level
party conformance testing. This knowledge and insight provide
a foundation for future standards development.
61
Program and Project Achievements for FY 2013

The CAVP issued 2,288 algorithm validations and the CMVP
issued 191 module validation certificates in FY 2013. The
number of algorithms and modules submitted for validation
continues to grow, representing significant growth in the
number of validations expected to be available in the future.
http://csrc.nist.gov/groups/STM
Contacts:
CMVP Contact: CAVP Contact:
Mr. Randall J. Easter Ms. Sharon Keller
(301) 975-4641 (301) 975-2910
randall.easter@nist.gov sharon.keller@nist.gov
ª
Automated Security Testing and Test
CAVP Validation Status For FY13
Suite Development
NIST’s CAVP utilizes the requirements and specifications of
400 the algorithm FIPS and Special Publications (SPs) written by the
350
300 Cryptography Technology Group (CTG) to develop algorithm test
250
suites and automated security testing. The CAVP is responsible
200
150 for providing assurance that the algorithms contained in modules
100
are implemented correctly. The CAVP does this by designing
50
0 and developing conformance testing for implementations of
these algorithms.
62
Computer Security Division Annual Report - 2013
21'
tcO
21'
voN
21'
ceD
31'
naJ
31'
beF
31'
raM
31'
rpA
31'
yaM
31'
nuJ
31'
luJ
31'
guA
31'
peS
CAVP Validation Status By FYs
2500
2000
1500
1000
500
0
TDES
SHA
RSA
RNG
KDF
KAS
HMAC
ECDSA
DSA
DRBG
ComponentTest
AES
6991YF 8991YF 0002YF 2002YF 4002YF 6002YF 8002YF 0102YF 2102YF 4102YF
TDES
SJ
SHA
RSA
RNG
KDF
KAS
HMAC
ECDSA
DSA
DRBG
DES
Component
Test
AES
Figure 19: CAVP Validation Status by FYs
Figure 20: CAVP Validation Status for FY 2013
CAVP Validated Implementation Actual Numbers
Updated As Wednesday, November 06, 2013
FiscalYear AES Comp. DES DSA DRBGECDSAHMAC KAS KDF RNG RSA SHA SJ TDES Total
FY1996 0 0 2 0 0 0 0 0 0 0 0 0 0 0 2
FY1997 0 0 11 6 0 0 0 0 0 0 0 7 2 0 26
FY1998 0 0 27 9 0 0 0 0 0 0 0 6 0 0 42
FY1999 0 0 30 14 0 0 0 0 0 0 0 12 1 0 57
FY2000 0 0 29 7 0 0 0 0 0 0 0 12 1 28 77
FY2001 0 0 41 15 0 0 0 0 0 0 0 28 0 51 135
FY2002 30 0 44 21 0 0 0 0 0 0 0 59 6 58 218
FY2003 66 0 49 24 0 0 0 0 0 0 0 63 3 73 278
FY2004 82 0 41 17 0 0 0 0 0 28 22 77 0 70 337
FY2005 145 0 54 31 0 14 115 0 0 108 80 122 2 102 773
FY2006 131 0 3 33 0 19 87 0 0 91 63 120 1 83 631
FY2007 238 0 0 63 0 35 127 0 0 137 130 171 1 136 1038
FY2008 271 0 0 77 4 41 158 0 0 137 129 191 0 122 1130
FY2009 373 0 0 71 23 33 193 6 0 142 143 224 1 138 1347
FY2010 399 0 0 70 31 39 179 12 0 150 155 239 0 142 1416
FY2011 440 7 0 102 79 68 201 34 0 148 183 255 0 177 1694
FY2012 599 24 0 121 122 92 283 20 3 157 231 323 1 248 2224
FY2013 689 85 0 106 145 113 276 12 9 132 208 293 0 217 2285
FY2014 48 28 0 9 22 6 26 0 1 2 22 30 0 17 211
Figure 21: CAVP Validated Implementation Actual Numbers
Page 1 of 2

The conformance tests consist of a suite of validation The CAVP currently has algorithm validation testing for the
tests for each approved cryptographic algorithm. These tests following cryptographic algorithms:
exercise the mathematical formulas and the algorithmic
requirements detailed in the algorithm to assure that the
detailed specifications are implemented correctly and Cryptographic Special Publication
completely. If the implementer deviates from or excludes any Algorithm/Component or FIPS
part of these instructions or requirements, the validation test
Triple Data Encryption SP 800-67, Recommendation
will fail, indicating that the algorithm implementation does not Standard (TDES) for the Triple Data Encryption
function properly or is incomplete. Algorithm (TDEA) Block Cipher, and
SP 800-38A, Recommendation for
CAVP-developed validation tests are performed by accredited
Block Cipher Modes of Operation–
testing laboratories on a vendor’s algorithm implementation Methods and Techniques
using automated known-answer tests, which compare the result
Advanced Encryption FIPS 197, Advanced Encryption
from a cryptographic operation with a specific input against the
Standard (AES) Standard, and SP 800-38A
expected result. They provide a uniform way to assure that the
Digital Signature FIPS 186-2, Digital Signature
cryptographic algorithm implementation adheres to the detailed
Standard (DSS) Standard (DSS), with change
specifications. notice 1, dated October 5, 2001
There are several types of validation tests, all designed FIPS 186-4, Digital Signature
to satisfy the testing requirements of the cryptographic Standard (DSS), dated July 2013
algorithms and their specifications. These include, but are not Elliptic Curve FIPS 186-2, Digital Signature Standard
limited to, Known-Answer Tests, Monte Carlo Tests, and Multi- Digital Signature (DSS), with change notice 1, dated
Block Message Tests. The Known-Answer Tests are designed Algorithm (ECDSA) October 5, 2001 and ANSI X9.62
to examine the individual components of the algorithm by FIPS 186-4, Digital Signature Standard
supplying known values to the variables and verifying the (DSS), dated July 2013 and ANSI X9.62
expected result. The Monte Carlo Test is designed to exercise RSA algorithm ANSI X9.31 and Public Key
the entire IUT. This test is designed to detect the presence of Cryptography Standards (PKCS) #1
implementation flaws that are not detected with the controlled v2.1: RSA Cryptography Standard-2002
input of the Known-Answer Tests. The types of implementation FIPS 186-4, Digital Signature Standard
flaws detected by this validation test include pointer problems, (DSS), dated July 2013 and ANSI
insufficient allocation of space, improper error handling, and X9.31 and Public Key Cryptography
Standards (PKCS) #1 v2.1: RSA
incorrect behavior of the IUT. The Multi-Block Message Test
Cryptography Standard-2002
(MMT) is designed to test the ability of the implementation to
Hashing algorithms SHA- FIPS 180-4, Secure Hash Standard
process multi-block messages, which require the chaining of
1, SHA-224, SHA-256, (SHS), dated March 2012
information from one block to the next.
SHA-384, SHA-512, SHA-
During the last few years, CSD has expanded its publications 512/224, SHA-512/256
beyond only an algorithm’s specification into how an algorithm Random number FIPS 186-2 Appendix 3.1 and
should be used. Many of these requirements are outside the generator (RNG) 3.2; ANSI X9.62 Appendix A.4
scope of the algorithm boundary and therefore cannot be tested algorithms
at the algorithm level by the CAVP. Some of the requirements Deterministic Random SP 800-90A, Recommendation for
are within the scope of the CMVP while others are outside the Bit Generators (DRBG) Random Number Generation Using
scope of both the CAVP and the CMVP. In the case where the Deterministic Random Bit Generators
requirement is outside the scope of the CAVP and the CMVP, the Keyed-Hash Message FIPS 198-1, The Keyed-Hash Message
fulfillment of the requirements is the responsibility of entities Authentication Authentication Code (HMAC)
Code (HMAC)
using, installing, or configuring applications or protocols that
use the cryptographic algorithms. For example, depending on Counter with Cipher SP 800-38C, Recommendation
the design of a cryptographic module, it may not be possible Block Chaining-Message for Block Cipher Modes of
Authentication Code Operation: the CCM Mode for
for the module to determine whether a specific key is used for
(CCM) mode Authentication and Confidentiality
multiple purposes, a situation that is strongly discouraged.
Cipher-based Message SP 800-38B, Recommendation for
Authentication Code Block Cipher Modes of Operation:
(CMAC) Mode for The CMAC Mode for Authentication
Authentication
63
Program and Project Achievements for FY 2013

In FY 2014, the CAVP expects to add algorithm validation
| Galois/Counter   | SP 800-38D, Recommendation for  |     |     |     |     |
| ---------------- | ------------------------------- | --- | --- | --- | --- |
testing for:
| Mode (GCM)   | Block Cipher Modes of Operation:   |     |     |     |     |
| ------------ | ---------------------------------- | --- | --- | --- | --- |
GMAC Mode of Operation Galois/Counter Mode (GCM) and    SP 800-56C, Recommendation for Key Derivation
GMAC, dated November 2007
through Extraction-then-Expansion, November 2011
| XTS Mode of Operation | SP800-38E, Recommendation  |     |     |     |     |
| --------------------- | -------------------------- | --- | --- | --- | --- |
for Block Cipher Modes of    SP 800-132, Recommendation for Password-Based Key
Operation: The XTS-AES Derivation Part 1: Storage Applications, December 2010
Mode for Confidentiality on
Block-Oriented Storage Devices,    SP 800-38F, Recommendation for Block Cipher Modes of
dated January 2010
Operation: Methods for Key Wrapping, December 2012
| Key Agreement Schemes | SP 800-56A, Recommendation  |     |     |     |     |
| --------------------- | --------------------------- | --- | --- | --- | --- |
  SP 800-56A Revision 2, Recommendation for Pair-Wise
| and Key Confirmation | for Pair-Wise Key Establishment  |     |     |     |     |
| -------------------- | -------------------------------- | --- | --- | --- | --- |
Schemes Using Discrete Logarithm  Key Establishment Schemes Using Discrete Logarithm
Cryptography, dated March 2007
Cryptography, May 2013
| All of SP 800-56A  | SP 800-56A  All sections except Section  |     |     |     |     |
| ------------------ | ---------------------------------------- | --- | --- | --- | --- |
| except KDF         | 5.8 Key Derivation Functions for         |     |     |     |     |
http://csrc.nist.gov/groups/STM/cavp
Key Agreement Schemes
| SP 800-56A  | SP 800-56A Section 5.7.1.2 Elliptic  |     |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- | --- |
Contacts:
| Section 5.7.1.2  | Curve Cryptography Cofactor Diffie- |                    |     |                    |     |
| ---------------- | ----------------------------------- | ------------------ | --- | ------------------ | --- |
| ECC CDH function | Hellman (ECC CDH) Primitive Testing |                    |     |                    |     |
|                  |                                     | Ms. Sharon Keller  |     | Ms. Elaine Barker  |     |
Key-Based Key Derivation  SP 800-108, Recommendation for  (301) 975-2910  (301) 975-2911
|                   |                                    | sharon.keller@nist.gov  |     | elaine.barker@nist.gov |     |
| ----------------- | ---------------------------------- | ----------------------- | --- | ---------------------- | --- |
| functions (KBKDF) | Key Derivation using Pseudorandom  |                         |     |                        |     |
Functions, dated October 2009
| Application-Specific      | SP 800-135 (Revision 1)      |     |     |     |     |
| ------------------------- | ---------------------------- | --- | --- | --- | --- |
| Key Derivation functions  | Recommendation for Existing  | ª   |     |     |     |
ISO Standardization of Security
| (ASKDF) (includes KDFs   | Application Specific key Derivation  |     |     |     |     |
| ------------------------ | ------------------------------------ | --- | --- | --- | --- |
Requirements for Cryptographic Modules
| used by IKEv1, IKEv2, TLS,  | Functions, dated December 2011 |     |     |     |     |
| --------------------------- | ------------------------------ | --- | --- | --- | --- |
ANS X9.63-2001, SSH,
CSD has contributed to the activities of the International
SRTP, SNMP, and TPM)
Organization for Standardization/International Electrotechnical
| Component test – ECDSA  | FIPS 186-4, Digital Signature Standard  |     |     |     |     |
| ----------------------- | --------------------------------------- | --- | --- | --- | --- |
Commission (ISO/IEC), which issued ISO/IEC 19790, Security
| Signature Generation   | (DSS), dated July 2013 and ANSI X9.62 |     |     |     |     |
| ---------------------- | ------------------------------------- | --- | --- | --- | --- |
Requirements for Cryptographic Modules, on March 1, 2006,
of hash value (This
|     |     | and  ISO/IEC  | 24759,  Test  | Requirements  | for  Cryptographic  |
| --- | --- | ------------- | ------------- | ------------- | ------------------- |
component test verifies
the signing of a hash-  Modules, on July 1, 2008. These efforts bring consistent testing
sized input. It does not
of cryptographic modules to the global community.
verify the hashing of
ISO/IEC JTC 1/SC 27 WG 3 completed and published the
the original message
to be signed.) revisions of both ISO/IEC 19790 and ISO/IEC 24759, for which
Randall J. Easter of CSD is the editor. The revision of ISO/IEC
| Component test – RSA  | FIPS 186-4, Digital Signature Standard  |     |     |     |     |
| --------------------- | --------------------------------------- | --- | --- | --- | --- |
PKCS#1 1.5 Signature  (DSS), dated July 2013 and Public Key  19790 was published August 15, 2012. ISO/IEC 19790:2012
| Generation of encoded  | Cryptography Standards (PKCS) #1  |     |     |     |     |
| ---------------------- | --------------------------------- | --- | --- | --- | --- |
was also adopted by the American National Standards Institute
message EM (This  v2.1: RSA Cryptography Standard-2002 (ANSI). The revision of ISO/IEC 24759 was published January
component test verifies
31, 2014.
the signing of an EM.
It does not verify the  CSD’s  Randall  J.  Easter  is  the  editor  for  three  ISO/IEC
formatting of the EM.)
documents.  Work is nearing completion on the Technical Report
document, ISO/IEC 30104 “Physical Security Attacks, Mitigation
| Component test – RSA  | SP 800-56B, Recommendation  |     |     |     |     |
| --------------------- | --------------------------- | --- | --- | --- | --- |
PKCS#1 PSS Signature  for Pair-Wise Key Establishment  Techniques and Security Requirements.” A final draft of ISO/
| Generation of encoded  | Schemes Using Integer  |     |     |     |     |
| ---------------------- | ---------------------- | --- | --- | --- | --- |
IEC 30104 was completed in December 2013 and circulated for
| message EM (This  | Factorization Cryptography,  |     |     |     |     |
| ----------------- | ---------------------------- | --- | --- | --- | --- |
national body comment.
| component test verifies  | August 2009, Section 7.1.2  |     |     |     |     |
| ------------------------ | --------------------------- | --- | --- | --- | --- |
the RSASP1 function.) Work is progressing on ISO/IEC 17825 “Testing methods
|     |     | for  the  mitigation  | of  | non-invasive  attack  | classes  against  |
| --- | --- | --------------------- | --- | --------------------- | ----------------- |
cryptographic modules.” The first committee draft of ISO/IEC
17825 was completed in December 2013 and circulated for
64
Computer Security Division Annual Report - 2013

national body comment. would measure the correct implementation of cryptographic
components as part of a larger system.
Work is progressing on a new standard document, ISO/IEC
18367 “Cryptographic algorithms and security mechanisms This program will perform research and experimentation in
conformance testing.” The third working draft of ISO/IEC 18367 applicable technologies and techniques that will enable the
was completed in December 2013 and circulated for national efficient testing of the cryptographic capabilities of each layer,
body comment. and continuous monitoring capabilities of each cryptographic
component, providing the necessary interfaces to establish
National body comments for the above four documents will
trust relationships with other cryptographic components.
be addressed at the 47th SC 27 WG 3 meeting to be held in
Techniques could include such items as:
Incheon, Korea, in October 2013.
 Embedding SCAP like data elements and standard
CSD’s contributions to the development of these international
interfaces to query those data elements during design
standards create a strong foundation for the adoption of and
and implementation of cryptographic components that
migration from currently used national standards. In particular,
would enable automated testing capabilities;
this adoption will promote the international harmonization for
the implementation and testing of cryptographic algorithms and
 Using cryptographic techniques to embed values into
modules while accommodating individual country preferences
the module that would increase the verifiability and
in the choice of approved security functions.
assurance that the module provides; and
http://csrc.nist.gov/groups/STM/cmvp/  Using industry-based secure development techniques to
increase the level of trust inherent in software modules
Contact: starting with design and implementation.
Mr. Randall J. Easter
Research into this area of cryptographic system validation
(301) 975-4641
holds the promise of automating the validation of all
randall.easter@nist.gov
cryptographic components, providing a higher assurance
with less manual effort by using SCAP-based ideas to embed
ª data elements that instrument the test harnesses used to
Cryptographic System Validation
validate cryptographic systems. This would also provide the
instrumentation that could be leveraged to enable a greater
Current validation programs focus on providing a known
level of situational awareness and security measurement, and
level of assurance for cryptographic algorithms and modules.
potentially to enable continuous monitoring of cryptographic
These are used within the context of a larger system to provide
systems.
cryptographic services as a method of protecting the data
within the system. As information systems continue to become
Contact:
more complex, the methods used to implement cryptographic
Mr. Michael Cooper
services have also increased in complexity. Problems with
(301) 975-8077
the use of cryptography are often introduced through the
michael.cooper@nist.gov
interaction of cryptographic components with the operating
environment. This program seeks to specify how cryptographic
components are used as part of a defined cryptographic system Technical Security Metrics
to solve problems with a measureable level of assurance, and
to introduce automated methods of quantifying the level of
ª
assurance. Security Risk Analysis of Enterprise
Networks Using Attack Graphs
This program will begin the research required to define a
reference cryptographic systems architecture and example
Protection of computer networks from malicious intrusions is
use cases where cryptographic systems are built from known
critical to the economy and security of the nation. Vulnerabilities
cryptographic components that cooperate through trust
are regularly discovered in software applications, which are
relationships to provide a measureable level of assurance. The
exploited to stage cyber attacks. System administrators need
architecture should begin at the lowest level with a hardware
objective metrics to guide and justify decision making as they
based root of trust, and each cryptographic component should
manage the security risk of enterprise networks. The objective
be added in successive layers to provide assurance in a
of this research is to develop a standard model for security
systematic way. This should allow the development of tests that
65
Program and Project Achievements for FY 2013

ª
risk analysis of computer networks. A standard model will Algorithms for Intrusion Measurement
enable us to answer questions such as “Are we more secure
now than yesterday?” or “How does the security of one network
configuration compare with another one?” Also, having a
standard model to measure network security will allow users,
vendors, and researchers to evaluate methodologies and
products for network security in a coherent and consistent
manner.
CSD has approached the challenge of network security
analysis by capturing vulnerability interdependencies and
measuring security based on how real attackers have penetrated
networks. CSD’s methodology for security risk analysis is based
on attack graphs. CSD analyzes attack paths through a network,
providing a probabilistic metric of the overall system risk. Figure 22: Algorithms for Intrusion Measurement
Through this metric, CSD analyzes trade-offs between security
costs and security benefits. The Algorithms for Intrusion Measurement (AIM) project, newly
formed in FY 2013, furthers measurement science in the area
Computer systems are vulnerable to both known and zero
of algorithms used in the field of intrusion detection. The team
day attacks. Handling zero day vulnerabilities is inherently
focuses on both new detection metrics and measurements of
difficult due to their unpredictable nature. In FY 2013, CSD
scalability (more formally algorithmic complexity). This analysis
attempted to assess the risk of unknown attack patterns. CSD
is applied to different phases of the detection lifecycle to include
developed a new model “k-zero day safety” for zero day attacks.
pre-emptive vulnerability analysis, initial attack detection, alert
Existing algorithms for computing this metric are not scalable
as they assume that a complete zero day attack graph has impact, alert aggregation/correlation, and compact log storage.
been generated. CSD has proposed a set of polynomial time In performing this work, the AIM project seeks to enhance our
algorithms for estimating k-zero day safety. CSD has authored nation’s ability to defend itself from network-borne attacks.
a paper, “An Efficient Approach to Assessing the Risk of Zero- Much of this scientific research is conducted in partnership
Day Vulnerabilities,” that received the Best Paper Award at the with the Army Research Laboratory (ARL). ARL’s participation
tenth International Conference on Security and Cryptography helps focus the work on solving immediate critical problems
(SECRYPT 2013), in Reykjavik, Iceland. facing U.S. Government networks. However, research solutions
are made publicly available and are designed to be generally
In FY 2014, CSD plans to apply attack graphs to study the
applicable to as many environments as possible.
effect of diversity for network defense. CSD also plans to
publish the results as a NIST report and as white papers in In its first year, the AIM project initiated research in each
conferences and journals. stage of the detection lifecycle with a focus on graph theoretic
approaches; it has already obtained several major results.
http://csrc.nist.gov/groups/SNS/security-riskanalysis-enterprise-
For example, the project has advanced the state of the art
networks/
in network scan detection, discovering and then thwarting
circumvention attacks against a highly cited scan detection
Contact:
algorithm. A paper describing this approach, “Limitations
Dr. Anoop Singhal to Threshold Random Walk Scan Detection and Mitigating
(301) 975-4432
Enhancements,” was published at the First IEEE Conference on
anoop.singhal@nist.gov
Communications and Network Security. Additionally, the project
developed a hypergraph-based algorithm to use Hamming
distance to aggregate security alert logs more than an order
of magnitude faster than the previous state of the art, while
providing enhanced aggregation.
In FY 2014, the AIM project will continue its scan detection
work and publish its work on log aggregation. It will continue
emerging research on log file compression and alert impact
analysis. Newly initiated work will include investigation of
66
Computer Security Division Annual Report - 2013

known-vulnerability based metrics for comparing the attack  and  leading  (jointly  with  IBM  personnel)  the  IEEE  Second
resistance of different networks or a single network over time. International Conference on Combinatorial Testing, held with
the International Conference on Software Testing.
Contacts:
Technology transfer activities included publication of several
| Mr. Peter Mell       |     |     |     | Mr. Mark (Lee) Badger  |     |     |     |              |              |                |          |                           |     |           |
| -------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | ------------ | ------------ | -------------- | -------- | ------------------------- | --- | --------- |
|                      |     |     |     |                        |     |     |     | technical    | papers;      | participation  | in       | the  Maryland Technology  |     |           |
| (301) 975-5572       |     |     |     | (301) 975-3176         |     |     |     |              |              |                |          |                           |     |           |
|                      |     |     |     |                        |     |     |     | Development  | Corporation  |                | (TEDCO)  | Technology                |     | Transfer  |
| peter.mell@nist.gov  |     |     |     | mark.badger@nist.gov   |     |     |     |              |              |                |          |                           |     |           |
Workshop; presentation of results of the work with Lockheed
Martin; release of enhanced covering array, test prioritization,
and fault location tools; plus seminars and lectures at several
ª
Automated Combinatorial Testing
conferences, universities, and federal agencies.
Plans for FY 2014 include a second phase of a project
| Software  | developers  |     | often  | encounter  | failures  | that  | result  |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------ | ---------- | --------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
from an unexpected interaction between components. NIST  with  the  NASA  IV&V  Facility  to  investigate  integration  of
combinatorial coverage measurement methods in NASA IV&V
research has shown that most failures are triggered by one or
practices; development of new methods and tools for very large
two parameters and progressively fewer by three, four, or more
parameters (see graph below), a relationship that is called the  covering arrays (hundreds of variables); lectures at conferences
and research labs; and guiding development of a combinatorial
Interaction Rule. These results have important implications for
testing. If all faults in a system can be triggered by a combination  software test development environment by graduate students
|     |     |     |     |     |     |     |     | at  Carnegie  | Mellon  | University  | which  | will  | incorporate  | NIST  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ----------- | ------ | ----- | ------------ | ----- |
of n or fewer parameters, then testing all n-way combinations
software.
of parameters can provide very strong fault detection efficiency.
These methods are being applied to software and hardware
http://csrc.nist.gov/groups/SNS/acts/
testing for reliability, safety, and security. CSD’s focus is on
empirical results and real-world problems.
Contacts:
| Project  | highlights  | for  | FY  2013  | included  |     | completion  | of  a  |     |     |     |     |     |     |     |
| -------- | ----------- | ---- | --------- | --------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
two-year Cooperative Research and Development Agreement  Mr. Rick Kuhn  Dr. Raghu Kacker
|          |       |           |         |     |               |     |          | (301) 975-3337  |     |     | (301) 975-2109        |     |     |     |
| -------- | ----- | --------- | ------- | --- | ------------- | --- | -------- | --------------- | --- | --- | --------------------- | --- | --- | --- |
| (CRADA)  | with  | Lockheed  | Martin  |     | Corporation,  |     | showing  |                 |     |     |                       |     |     |     |
|          |       |           |         |     |               |     |          | kuhn@nist.gov   |     |     | raghu.kacker@nist.gov |     |     |     |
approximately 20% reduction in software test development
| cost  across  | a  variety         |     | of  projects;  |          | publication  | of      | the  first  |     |     |     |     |     |     |     |
| ------------- | ------------------ | --- | -------------- | -------- | ------------ | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| textbook      | on  combinatorial  |     | testing;       | release  |              | of  an  | advanced    |     |     |     |     |     |     |     |
ª
tool for measuring combinatorial coverage of test sets (jointly  Hardware Roots of Trust
| with  Centro  | Nacional  |     | de  Metrología,  |     | Mexico);  | cooperative  |     |         |            |          |          |     |          |            |
| ------------- | --------- | --- | ---------------- | --- | --------- | ------------ | --- | ------- | ---------- | -------- | -------- | --- | -------- | ---------- |
|               |           |     |                  |     |           |              |     | Modern  | computing  | devices  | consist  | of  | various  | hardware,  |
work with the National Aeronautics and Space Administration
|     |     |     |     |     |     |     |     | firmware,  | and  software  |     | components  | at  | multiple  | layers  of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ----------- | --- | --------- | ----------- |
(NASA) Independent Verification and Validation (IV&V) Facility
|     |     |     |     |     |     |     |     | abstraction.  | Many  | security  | and  protection  |     | mechanisms  | are  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --------- | ---------------- | --- | ----------- | ---- |
analyzing combinatorial coverage measurement for IV&V of
currently rooted in software that, along with all underlying
space systems; lectures at conferences and research labs;
components, must be trustworthy. A vulnerability in any of
those components could compromise the trustworthiness of
the security mechanisms that rely upon those components.
Stronger security assurances may be possible by grounding
security mechanisms in roots of trust.
Roots of trust are highly reliable hardware, firmware, and
software components that perform specific, critical security
functions. Because roots of trust are inherently trusted, they
must be secure by design. As such, many roots of trust are
|     |     |     |     |     |     |     |     | implemented  | in  hardware  |     | so  that  | malware  | cannot  | tamper  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | --------- | -------- | ------- | ------- |
with the functions they provide. Roots of trust provide a firm
foundation from which to build security and trust.
A focus area for CSD’s roots of trust research in FY 2013 was
security for mobile devices. CSD worked with government and
industry partners on guidelines on hardware-rooted security
Figure 23: Interaction Rule features in mobile devices. These guidelines focus on device
67
Program and Project Achievements for FY 2013

Cybersecurity Framework
Policy Machine
Cloud Computing
68
Computer Security Division Annual Report - 2013
Standards
yhpargotpyrC
Risk Management Framework
Biometrics
Assets
Security Practices
Security Controls
Verification
tnemeganam
ksir
niahc
ylppuS
Authorization
FISMA
Validated Products List
Mobile Devices
Continuous Monitoring
FIPS 140-2
EO
13636
integrity, isolation, and protected storage features that are
supported by roots of trust. Draft SP 800-164, Guidelines on
Hardware-Rooted Security in Mobile Devices, was released for
Roadmap
public comment in October 2012.
In FY 2014, CSD will release a revised draft of SP 800-
164, based on the feedback received during the public
comment period. In addition, CSD is working with the National
Cybersecurity Center of Excellence (NCCoE) to encourage the
adoption of stronger security technologies in mobile devices.
Using draft SP 800-164 as a basis for an NCCoE building block
activity, CSD and the NCCoE will invite mobile device, operating
system, management software vendors, and application
developers to study, demonstrate, and document how to use
hardware-backed security solutions.
In FY 2013, CSD continued its work to protect fundamental
system firmware, commonly known as Basic Input/Output
System (BIOS). CSD has been working with key members of the
computer industry on the use of roots of trust to improve the
security of BIOS.
CSD will continue its efforts to secure BIOS and other critical
firmware in FY 2014 and will finalize a Special Publication
covering BIOS protections for server-class systems. CSD will
also release an updated draft of SP 800-155, BIOS Integrity
Measurement Guidelines, which will include additional
guidelines for server-class systems and other boot firmware. In
order to encourage the continued adoption of BIOS protections,
CSD also plans to submit SP 800-147, BIOS Protection
Guidelines, to ISO for standardization.
Contact:
Mr. Andrew Regenscheid
(301) 975-5155
andrew.regenscheid@nist.gov

Cybersecurity Framework
Policy Machine
Cloud Computing
Standards
yhpargotpyrC
Risk Management Framework
Biometrics
Assets
Security Practices
Security Controls
Verification
tnemeganam
ksir
niahc
ylppuS
Authorization
FISMA
Validated Products List
Mobile Devices
Continuous Monitoring
FIPS 140-2
EO
13636
Roadmap
Honors and Awards
69

Mr. Richard Kissel Mr. Jeremy Grant
U.S. Department of Commerce Bronze Medal Federal 100 Award
Mr. Kissel received a U.S. Department Jeremy Grant is a senior executive
of Commerce Bronze Medal for raising advisor for identity management at
small and medium-sized business NIST. He leads the National Strategy for
(SMB) awareness of information security Trusted Identities in Cyberspace (NSTIC)
threats, vulnerabilities, and safeguards National Program Office, which is
through implementation of NIST’s SMB working to foster a vibrant marketplace
information security outreach program. of identity solutions—provided by
As the program lead, Mr. Kissel worked entities both private and public—that
collaboratively with the Small Business Administration and would enhance the security, convenience, and privacy of online
the FBI’s InfraGard program to conduct information security transactions. Federal Computer Week included the following
training workshops for small businesses with a focus on the description in Mr. Grant’s award: “Through his ability to facilitate
tools and techniques these businesses can apply directly. dialogue and inspire action among NSTIC’s complex and diverse
By empowering SMBs, which represent over 95% of all U.S. community of stakeholders, he has helped foster NSTIC’s vision
businesses, to better protect their information, the nation’s and principles to produce marketable solutions and advanced
overall information infrastructure is strengthened to enhance innovation.” Further details about the award are available at
innovation, competitiveness, and economic security. http://fcw.com/articles/2013/03/20/grant-jeremy.aspx.
FCW Federal 100 Awards
Three members of the Information Technology Laboratory and the Computer Security Division were
named to the 2013 list of the top 100 government, industry and academic leaders in the Federal
Government IT community. The award recognizes individuals who are making a difference in the way
technology has transformed their agency or accelerated their agency’s mission.
The Federal 100 Awards are sponsored by Federal Computer Week. Recipients are chosen by a
panel of government and industry leaders. They were formally honored at a gala on March 20, 2013.
Mr. Jon Boyens Mr. Adam Sedgewick
Federal 100 Award Federal 100 Award
Jon Boyens is a senior information Senior Information Technology Policy
technology security specialist in the Advisor Adam Sedgewick coordinates
Computer Security Division. As lead for information technology projects with
NIST’s Information and Communications NIST’s critical partners in the federal
Technology (ICT) Supply Chain Risk arena, including the Chief Information
Management (SCRM) project, he Officers’ (CIO) Council, the Office of
identifies and evaluates technologies, Management and Budget (OMB) and
tools, techniques, practices, and the National Security Staff. Federal
standards useful in managing risk to the ICT supply chain and Computer Week included the following description in Mr.
co-leads the U.S. Government’s efforts to develop ICT SCRM Sedgewick’s award: “[He] focused on government-wide impact
lifecycle processes and standards. Federal Computer Week while offering process improvements for the council’s internal
included the following description in Mr. Boyens’ award: “He operations. He added tremendous substantive expertise gleaned
led an integrated team that developed a set of standardized, from his experience as a cybersecurity and IT policy analyst on
repeatable practices to help federal agencies manage risks Capitol Hill. As senior IT policy adviser at NIST, he continues to
to their information and communications technology supply shape the government-wide dialogue on cybersecurity reform.”
chain in the face of rapid technological evolution.” Further Further details about the award are available at http://fcw.com/
details about the award are available at: http://fcw.com/ articles/2013/03/20/sedgewick-adam.aspx.
articles/2013/03/20/boyens-jon.aspx.
70
Computer Security Division Annual Report - 2013

Mr. Joshua Franklin &
Ms. Kelley Dempsey
Government Information Security
Leadership Award (GISLA)
Josh Franklin and Kelley Dempsey won the (ISC)² Government
Information Security Leadership Award (GISLA) in the Process/
Policy Improvement category for their work on the Federal
Mobile Security Baseline and the Mobile Computing Decision
Framework. According to (ISC)², the award in this category
is given to “An individual or team of senior-level U.S. federal
government personnel…whose contribution to the development
or implementation of any information security policy or process
has significantly improved the security posture of a federal
agency, department or government-wide within the last 12
months.” Source: https://www.isc2.org/gisla/Default.aspx.
Dr. Ron Ross
Inaugural Lynn F. McNulty Information
Security Leadership Tribute Award
National Institute of Standards and Technology (NIST) Fellow Ron Ross has been awarded the
inaugural Lynn F. McNulty Tribute U.S. Government Information Security Leadership Award. The (ISC)2
U.S. Government Advisory Board for Cyber Security (GABCS) announced the award on October 29,
2013, in recognition of Ross’s “key role in establishing cybersecurity requirements for federal agencies
for decades.”
The award was established last year after the death of (ISC)2 Fellow and IT security evangelist Lynn F. McNulty, CISSP. McNulty
was considered by those in the community as the “pioneer” of government information security. The Tribute Award recognizes a
member of the U.S. federal information security community who upholds McNulty’s legacy as a visionary and innovator through
outstanding service and commitment.
Ross worked with McNulty during the 1990s when McNulty was NIST’s Associate Director of Computer Security.
“Ron’s insight and leadership in producing a library of guidance publications over the past decade has greatly contributed to the
advancement of information security in government and around the world,” said Peter Gouldmann, CISSP, director of information
risk programs, Office of Information Assurance, U.S. Department of State, and member, (ISC)2 GABCS. “His highly collaborative
approach, incorporating government and industry, has resulted in products that are being adopted and adapted for use on national
security systems, transcending the unclassified and classified systems landscape.”
Sources: https://www.isc2.org/GISLA-Lynn-McNulty-Award/defalt.aspx
http://www.nist.gov/itl/csd/ross-110513.cfm
71
Honors & Awards

This page is intentionally left blank.
72
Computer Security Division Annual Report - 2013

Cybersecurity Framework
Policy Machine
Cloud Computing
Standards
yhpargotpyrC
Risk Management Framework
Biometrics
Assets
Security Practices
Security Controls
Verification
tnemeganam
ksir
niahc
ylppuS
Authorization
FISMA
Validated Products List
Mobile Devices
Continuous Monitoring
FIPS 140-2
EO
13636
Roadmap
FY 2013 Computer
Security Division
Publications
The Computer Security Division uses multiple NIST Technical Series to promulgate security standards,
guidelines, recommendations, research, and additional background material. Those series include Federal
Information Processing Standards (FIPS), NIST Special Publications (SPs), NIST Interagency or Internal
Reports (NISTIRs) and Information Technology Laboratory (ITL) Bulletins. Links to these publications are
available at http://csrc.nist.gov/publications.
Additionally, each year CSD staff authors numerous additional publications, including journal articles,
conference papers, and other papers that are widely disseminated. They range from basic research to
high-level summaries of CSD activities.
73

NIST Technical Series Publications − FIPS, Special Publications, NISTIRs, and ITL Bulletins
Below are lists of NIST Technical Series publications that CSD released as draft documents or as final publications during FY 2013
(from October 1, 2012 to September 30, 2013). Following the lists are abstracts and contact information for each publication.
DRAFT PUBLICATIONS
Draft Released
Type & Number Publication Title
Date
Federal Information Processing Standards (FIPS)
No draft FIPS were released in FY 2013.
Special Publications (SPs)
SP 800-164 Guidelines on Hardware-Rooted Security in Mobile Devices October 2012
SP 800-162 Guide to Attribute Based Access Control (ABAC) Definition and Considerations April 2013
SP 800-161 Supply Chain Risk Management Practices for Federal Information Systems and Organizations August 2013
SP 800-101 Revision 1 Guidelines on Mobile Device Forensics September 2013
SP 800-90 Series Random Bit Generators September 2013
(A Revision 1, B, and C)
A Revision 1: Recommendation for Random Number Generation Using Deterministic Random Bit Generators
B: Recommendation for the Entropy Sources Used for Random Bit Generation
C: Recommendation for Random Bit Generator (RBG) Constructions
SP 800-78-4 Cryptographic Algorithms and Key Sizes for Personal Identity Verification May 2013
SP 800-73-4 Interfaces for Personal Identity Verification (3 Parts) May 2013
Part 1- PIV Card Application Namespace, Data Model and Representation
Part 2- PIV Card Application Card Command Interface
Part 3- PIV Client Application Programming Interface
SP 800-63-2 Electronic Authentication Guideline February 2012
SP 800-53 Revision 4 Security and Privacy Controls for Federal Information Systems and Organizations February 2013
SP 800-52 Revision 1 Guidelines for the Selection, Configuration, and Use of Transport Layer Security (TLS) Implementations September 2013
SP 800-38 G Recommendation for Block Cipher Modes of Operation: Methods for Format-Preserving Encryption July 2013
NIST Interagency Reports (NISTIRs)
NISTIR 7946 CVSS Implementation Guidance September 2013
NISTIR 7924 Reference Certificate Policy April 2013
NISTIR 7904 Trusted Geolocation in the Cloud: Proof of Concept Implementation December 2012
NISTIR 7298 Revision 2 Glossary of Key Information Security Terms December 2012
74
Computer Security Division Annual Report - 2013

Final (Approved) Publications
Federal Information Processing Standards (FIPS)
Publication
Document Number Publication Title
Date
FIPS 201-2 Personal Identity Verification (PIV) of Federal Employees and Contractors August 2013
FIPS 186-4 Digital Signature Standard (DSS) July 2013
Special Publications (SPs)
Publication
Document Number Publication Title
Date
SP 800-165 Computer Security Division 2012 Annual Report June 2013
SP 800-133 Recommendation for Cryptographic Key Generation December 2012
SP 800-130 A Framework for Designing Cryptographic Key Management Systems August 2013
SP 800-124 Revision 1 Guidelines for Managing the Security of Mobile Devices in the Enterprise June 2013
SP 800-83 Revision 1 Guide to Malware Incident Prevention and Handling for Desktops and Laptops July 2013
SP 800-82 Revision 1 Guide to Industrial Control Systems (ICS) Security May 2013
SP 800-81-2 Secure Domain Name System (DNS) Deployment Guide September 2013
SP 800-76-2 Biometric Specifications for Personal Identity Verification July 2013
SP 800-63-2 Electronic Authentication Guideline August 2013
SP 800-56A Revision 2 Recommendation for Pair-Wise Key Establishment Schemes Using Discrete Logarithm Cryptography May 2013
SP 800-53 Revision 4 Security and Privacy Controls for Federal Information Systems and Organizations April 2013
SP 800-40 Revision 3 Guide to Enterprise Patch Management Technologies July 2013
SP 800-38F Recommendation for Block Cipher Modes of Operation: Methods for Key Wrapping December 2012
NIST Interagency Reports (NISTIRs)
Publication
Document Number Publication Title
Date
NISTIR 7957 Conformance Test Architecture and Test Suite for ANSI/NIST-ITL 1-2011 NIEM XML Encoded Transactions September 2013
NISTIR 7956 Cryptographic Key Management Issues & Challenges in Cloud Services September 2013
NISTIR 7933 Requirements and Conformance Test Assertions for ANSI/NIST-ITL 1-2011 Record Type 18 - DNA Record May 2013
NISTIR 7916 Proceedings of the Cybersecurity in Cyber-Physical Systems Workshop, April 23-24, 2012 February 2013
NISTIR 7896 Third-Round Report of the SHA-3 Cryptographic Hash Algorithm Competition November 2012
NISTIR 7878 Combinatorial Coverage Measurement October 2012
NISTIR 7817 A Credential Reliability and Revocation Model for Federated Identities November 2012
NISTIR 7622 Notional Supply Chain Risk Management Practices for Federal Information Systems October 2012
NISTIR 7511 Revision 3 Security Content Automation Protocol (SCAP) Version 1.2 Validation Program Test Requirements January 2013
NISTIR 7298 Revision 2 Glossary of Key Information Security Terms May 2013
75
FY 2013 Computer Security Division Publications

Final (Approved) Publications (cont.)
ITL Bulletins
| Release Date |     |     | Title of Bulletin     |     |     |     |
| ------------ | --- | --- | --------------------- | --- | --- | --- |
September 2013 NIST Opens Draft Special Publication 800-90A, Recommendation for Random Number Generation Using Deterministic
Random Bit Generators, For Review and Comment (Supplemental ITL Bulletin for September 2013)
| September 2013 |           |     | ITL Publishes Guidance on Preventing and Handling Malware Incidents |     |     |     |
| -------------- | --------- | --- | ------------------------------------------------------------------- | --- | --- | --- |
| August 2013    |           |     | ITL Publishes Guidance on Enterprise Patch Management Technologies  |     |     |     |
|                | July 2013 |     | ITL Issues Guidelines for Managing the Security of Mobile Devices   |     |     |     |
|                | June 2013 |     | ITL Updates Glossary of Key Information Security Terms              |     |     |     |
|                | May 2013  |     | ITL Publishes Security and Privacy Controls for Federal Agencies    |     |     |     |
April 2013 Security Content Automation Protocol (SCAP) Version 1.2 Validation Program Test Requirements
| March 2013 |     |     | NIST to Develop a Cybersecurity Framework to Protect Critical Infrastructure |     |     |     |
| ---------- | --- | --- | ---------------------------------------------------------------------------- | --- | --- | --- |
January 2013 Managing Identity Requirements for Remote Users of Information Systems to Protect System Security and Information Privacy
| December 2012 |     |     | Generating Secure Cryptographic Keys: A Critical Component of Cryptographic   |     |     |     |
| ------------- | --- | --- | ----------------------------------------------------------------------------- | --- | --- | --- |
Key Management and the Protection of Sensitive Information
November 2012 Practices for Managing Supply Chain Risks to Protect Federal Information Systems
October 2012 Conducting Information Security-Related Risk Assessments: Updated Guidelines for Comprehensive Risk Management Programs
Abstracts of NIST Technical Series   elements, system interfaces, and security controls required to
Publications Released in FY 2013 securely store, process, and retrieve identity credentials from
the card.
| The  | following  | sections  | provide  | abstracts  | and  | contact  |
| ---- | ---------- | --------- | -------- | ---------- | ---- | -------- |
information for the draft and final FIPS, NIST SPs, and security- Contacts:
related NISTIRs listed in the previous section.  These publications  Ms. Hildegard Ferraiolo  Dr. David Cooper
are available at http://csrc.nist.gov/publications. hildegard.ferraiolo@nist.gov   david.cooper@nist.gov
Mr. Salvatore Francomacaro  Mr. Ketan Mehta
ª
Federal Information Processing  salvatore.francomacaro@nist.gov  ketan.mehta@nist.gov
Standards (FIPS)
Ms. Annie Sokol
annie.sokol@nist.gov
FIPS 201-2, Personal Identity Verification (PIV)
of Federal Employees and Contractors
FIPS 186-4, Digital Signature Standard (DSS)
| This  | standard  | specifies  | the  | architecture  | and  | technical  |
| ----- | --------- | ---------- | ---- | ------------- | ---- | ---------- |
This standard specifies a suite of algorithms that can be used
requirements for a common identification standard for federal
to generate a digital signature. Digital signatures are used to
| employees  | and  | contractors. The  |     | overall  | goal  is  | to  achieve  |
| ---------- | ---- | ----------------- | --- | -------- | --------- | ------------ |
detect unauthorized modifications to data and to authenticate
| appropriate  | security  | assurance  |     | for  multiple  | applications  | by  |
| ------------ | --------- | ---------- | --- | -------------- | ------------- | --- |
the identity of the signatory. In addition, the recipient of signed
efficiently verifying the claimed identity of individuals seeking
data can use a digital signature as evidence in demonstrating
physical access to federally controlled government facilities
to a third party that the signature was, in fact, generated by the
and logical access to government information systems. The
claimed signatory. This is known as non-repudiation, since the
| standard  | contains  | the  minimum  |     | requirements  | for  | a  federal  |
| --------- | --------- | ------------- | --- | ------------- | ---- | ----------- |
signatory cannot easily repudiate the signature at a later time.
personal identity verification system that meets the control
| and  security  |     | objectives  | of  Homeland  | Security  |     | Presidential  |
| -------------- | --- | ----------- | ------------- | --------- | --- | ------------- |
Contact:
Directive-12 (HSPD-12), including identity proofing, registration,
Ms. Elaine Barker
and issuance. The standard also provides detailed specifications
elaine.barker@nist.gov
that will support technical interoperability among PIV systems
of federal departments and agencies. It describes the card
76
Computer Security Division Annual Report - 2013

ª
NIST Special Publications (SPs) Draft SP 800-162, Guide to Attribute Based Access
Control (ABAC) Definition and Considerations
SP 800-165, Computer Security Division This document provides federal agencies with a definition
2012 Annual Report of Attribute Based Access Control (ABAC). ABAC is a logical
access control methodology where authorization to perform
Title III of the E-Government Act of 2002, entitled the
a set of operations is determined by evaluating attributes
Federal Information Security Management Act (FISMA) of 2002,
associated with the subject, object, requested operations, and,
requires NIST to prepare an annual public report on activities
in some cases, environment conditions against policy, rules, or
undertaken in the previous year, and planned for the coming
relationships that describe the allowable operations for a given
year, to carry out responsibilities under this law. The primary
goal of the Computer Security Division (CSD), a component of set of attributes. This document also provides considerations for
NIST s Information Technology Laboratory (ITL), is to provide using ABAC to improve information sharing within organizations
standards and technology that protects information systems and between organizations while maintaining control of that
against threats to the confidentiality, integrity, and availability information.
of information and services. During FY 2013, CSD successfully
responded to numerous challenges and opportunities in fulfilling Contacts:
that mission. Through CSD’s diverse research agenda and Dr. Vincent Hu Mr. David Ferraiolo
engagement in many national priority initiatives, high-quality, vhu@nist.gov david.ferraiolo@nist.gov
cost-effective security and privacy mechanisms were developed
Mr. Rick Kuhn
and applied that improved information security across the
rkuhn@nist.gov
Federal Government and the greater information security
community. This annual report highlights the research agenda
Draft SP 800-161, Supply Chain Risk
and activities in which CSD was engaged during FY 2013.
Management Practices for Federal Information
Systems and Organizations
Contacts:
Mr. Patrick O’Reilly Mr. Kevin Stine The Information and Communications Technology (ICT) supply
patrick.oreilly@nist.gov kevin.stine@nist.gov chain is a complex, globally distributed system of interconnected
networks that are logically long, with geographically diverse
Draft SP 800-164, Guidelines on Hardware-Rooted routes and multiple tiers of outsourcing. This system of
Security in Mobile Devices networks includes organizations, people, processes, products,
and services and the infrastructure supporting the system
Many mobile devices are not capable of providing strong
development life cycle, including research and development
security assurances to end users and organizations. Current
(R&D), design, manufacturing, acquisition, delivery, integration,
mobile devices lack the hardware-based roots of trust that are
operations, and disposal/retirement of an organization’s ICT
increasingly built into laptops and other types of hosts. This
products (i.e., hardware and software) and services.
document focuses on defining the fundamental security primitives
and capabilities needed to enable more secure mobile device Today’s ICT supply chains have increased complexity, diversity,
use. This document is intended to accelerate industry efforts and scale, while Federal Government information systems have
to implement these primitives and capabilities. The guidelines been rapidly expanding in terms of capability and number, with
in this document are intended to provide a baseline of security an increased reliance on outsourcing and commercially available
technologies that can be implemented across a wide range products. These trends have caused federal departments and
of mobile devices to help secure organization-issued mobile agencies to have a lack of visibility and understanding throughout
devices as well as devices brought into an organization, such the supply chain of how the technology being acquired is
as personally-owned devices used in enterprise environments developed, integrated, and deployed, as well as the processes,
(e.g., Bring Your Own Device (BYOD)). procedures, and practices used to assure the integrity, security,
resilience, and quality of the products and services. This lack of
Contacts: visibility and understanding, in turn, has decreased the control
Dr. Lily Chen Mr. Joshua Franklin federal departments and agencies have with regard to the
lily.chen@nist.gov joshua.franklin@nist.gov decisions impacting the inherited risks traversing the supply
chain and the ability to effectively manage those risks.
Mr. Andrew Regenscheid
andrew.regenscheid@nist.gov
SP 800-161 provides guidance to federal departments and
agencies on identifying, assessing, and mitigating ICT supply
chain risks at all levels in their organizations. SP 800-161
77
FY 2013 Computer Security Division Publications

integrates ICT Supply Chain Risk Management (SCRM) into recommendations for securing mobile devices throughout their
federal agency enterprise risk management activities by applying life cycles. The scope of this publication includes securing both
a multi-tiered SCRM-specific approach, including supply chain organization-provided and personally-owned (bring your own
risk assessments and supply chain risk mitigation activities and device (BYOD)) mobile devices. [Supersedes SP 800-124.]
guidance.
Contact:
Contacts: Mr. Murugiah Souppaya
Mr. Jon Boyens Ms. Celia Paulsen murugiah.souppaya@nist.gov
jon.boyens@nist.gov celia.paulsen@nist.gov
Draft SP 800-101 Revision 1, Guidelines
SP 800-133, Recommendation for on Mobile Device Forensics
Cryptographic Key Generation
Mobile device forensics is the science of recovering digital
Cryptography is often used in an information technology evidence from a mobile device under forensically sound conditions
security environment to protect data that is sensitive, has using accepted methods. Mobile device forensics is an evolving
a high value, or is vulnerable to unauthorized disclosure or specialty in the field of digital forensics. This guide attempts to
undetected modification during transmission or while in storage. bridge the gap by providing an in-depth look into mobile devices
Cryptography relies upon two basic components: an algorithm and explaining technologies involved and their relationship to
(or cryptographic methodology) and a cryptographic key. This forensic procedures. This document covers mobile devices
Recommendation discusses the generation of the keys to be with features beyond simple voice communication and text
managed and used by the approved cryptographic algorithms. messaging capabilities. This guide also discusses procedures for
the validation, preservation, acquisition, examination, analysis,
Contacts: and reporting of digital information.
Ms. Elaine Barker Dr. Allen Roginsky
elaine.barker@nist.gov allen.roginsky@nist.gov Contact:
Mr. Richard Ayers
SP 800-130, A Framework for Designing richard.ayers@nist.gov
Cryptographic Key Management Systems
Draft SP 800-90 Series, Random Bit Generators:
This Framework for Designing Cryptographic Key Management
Systems (CKMS) contains topics that should be considered by a Draft SP 800-90A Revision 1, Recommendation
CKMS designer when developing a CKMS design specification. For for Random Number Generation Using Deterministic
each topic, there are one or more documentation requirements Random Bit Generators
that need to be addressed by the design specification. Thus, any
This Recommendation specifies mechanisms for the
CKMS that addresses each of these requirements would have a
generation of random bits using deterministic methods. The
design specification that is compliant with this Framework.
methods provided are based on hash functions, block cipher
algorithms, or number theoretic problems.
Contact:
Ms. Elaine Barker Draft SP 800-90B, Recommendation for the Entropy
elaine.barker@nist.gov Sources Used for Random Bit Generation
This Recommendation specifies the design principles and
SP 800-124 Revision 1, Guidelines for Managing the
requirements for the entropy sources used by Random Bit
Security of Mobile Devices in the Enterprise
Generators, and the tests for the validation of entropy sources.
Mobile devices, such as smart phones and tablets, typically These entropy sources are intended to be combined with
need to support multiple security objectives: confidentiality, Deterministic Random Bit Generator mechanisms that are
integrity, and availability. To achieve these objectives, mobile specified in SP 800-90A to construct Random Bit Generators, as
devices should be secured against a variety of threats. The specified in SP 800-90C.
purpose of this publication is to help organizations centrally
Draft SP 800-90C, Recommendation for Random
manage the security of mobile devices. Laptops are out of the
Bit Generator (RBG) Constructions
scope of this publication, as are mobile devices with minimal
computing capability, such as basic cell phones. This publication This Recommendation specifies constructions for the
provides recommendations for selecting, implementing, and implementation of random bit generators (RBGs). An RBG may
using centralized management technologies, and it explains the be a deterministic random bit generator (DRBG) or a non-
security concerns inherent in mobile device use and provides deterministic random bit generator (NRBG). The constructed
78
Computer Security Division Annual Report - 2013

RBGs consist of DRBG mechanisms as specified SP 800-90A and each of which contains information about a small portion of the
entropy sources as specified in SP 800-90B. domain name space. The domain name data provided by DNS
is intended to be available to any computer located anywhere
Contacts: in the Internet. This document provides deployment guidelines
for securing DNS within an enterprise. Because DNS data is
Ms. Elaine Barker Dr. John Kelsey
elaine.barker@nist.gov john.kelsey@nist.gov meant to be public, preserving the confidentiality of DNS data
is not a concern. The primary security goals for DNS are data
SP 800-83 Revision 1, Guide to Malware Incident integrity and source authentication, which are needed to ensure
Prevention and Handling for Desktops and Laptops the authenticity of domain name information and maintain the
integrity of domain name information in transit. This document
Malware, also known as malicious code, refers to a program
provides extensive guidance on maintaining data integrity and
that is covertly inserted into another program with the intent to
performing source authentication. DNS components are often
destroy data, run destructive or intrusive programs, or otherwise
subjected to denial-of-service attacks intended to disrupt
compromise the confidentiality, integrity, or availability of
access to the resources whose domain names are handled
the victim’s data, applications, or operating system. Malware
by the attacked DNS components. This document presents
is the most common external threat to most hosts, causing
guidelines for configuring DNS deployments to prevent many
widespread damage and disruption and necessitating extensive
denial-of-service attacks that exploit vulnerabilities in various
recovery efforts within most organizations. This publication
DNS components. [Supersedes SP 800-81 Revision 1.]
provides recommendations for improving an organization’s
malware incident prevention measures. It also gives extensive
Contact:
recommendations for enhancing an organization’s existing
Dr. Chandramouli (Mouli) Ramaswamy
incident response capability so that it is better prepared to handle
mouli@nist.gov
malware incidents, particularly widespread ones. [Supersedes
SP 800-83.]
Draft SP 800-78-4, Cryptographic Algorithms and
Key Sizes for Personal Identity Verification
Contact:
FIPS 201 defines requirements for the PIV lifecycle activities,
Mr. Murugiah Souppaya
murugiah.souppaya@nist.gov including identity proofing, registration, PIV Card issuance, and
PIV Card usage. FIPS 201 also defines the structure of an identity
SP 800-82 Revision 1, Guide to Industrial credential that includes cryptographic keys. This document
Control Systems (ICS) Security contains the technical specifications needed for the mandatory
and optional cryptographic keys specified in FIPS 201, as well
This document provides guidance on how to secure
as the supporting infrastructure specified in FIPS 201 and the
Industrial Control Systems (ICS), including Supervisory Control
related SP 800-73, Interfaces for Personal Identity Verification,
and Data Acquisition (SCADA) systems, Distributed Control
and SP 800-76, Biometric Data Specification for Personal Identity
Systems (DCS), and other control system configurations such
Verification, that rely on cryptographic functions.
as Programmable Logic Controllers (PLC), while addressing
their unique performance, reliability, and safety requirements.
Contacts:
The document provides an overview of ICS and typical system
Ms. Hildegard (Hildy) Ferraiolo Dr. David Cooper
topologies, identifies typical threats and vulnerabilities to these
hildegard.ferraiolo@nist.gov david.cooper@nist.gov
systems, and provides recommended security countermeasures
to mitigate the associated risks. [Supersedes SP 800-82.] Mr. William Burr Mr. Tim Polk
william.burr@nist.gov william.polk@nist.gov
Contact:
Mr. Keith Stouffer SP 800-76-2, Biometric Specifications for
keith.stouffer@nist.gov Personal Identity Verification
Homeland Security Presidential Directive HSPD-12, Policy for
SP 800-81-2, Secure Domain Name
a Common Identification Standard for Federal Employees and
System (DNS) Deployment Guide
Contractors, called for new standards to be adopted governing
The Domain Name System (DNS) is a distributed computing interoperable use of identity credentials to allow physical and
system that enables access to Internet resources by user-friendly logical access to Federal Government locations and systems.
domain names rather than IP addresses, by translating domain FIPS 201, Personal Identity Verification (PIV) of Federal
names to IP addresses and back. The DNS infrastructure is made Employees and Contractors, was developed to define procedures
up of computing and communication entities called Name Servers and specifications for issuance and use of an interoperable
79
FY 2013 Computer Security Division Publications

identity credential. This document, SP 800-76, is a companion SP 800-63-2, Electronic Authentication Guideline
document to FIPS 201. It describes technical acquisition and
This recommendation provides technical guidelines for
formatting specifications for the PIV system, including the PIV
federal agencies implementing electronic authentication and is
Card itself. It also establishes minimum accuracy specifications
not intended to constrain the development or use of standards
for deployed biometric authentication processes. The approach
outside of this purpose. The recommendation covers remote
is to enumerate procedures and formats for collection and
authentication of users (such as employees, contractors, or
preparation of fingerprint, iris, and facial data, and to restrict
private individuals) interacting with government IT systems over
values and practices included generically in published biometric
open networks. It defines technical requirements for each of four
standards. The primary design objective behind these particular
levels of assurance in the areas of identity proofing, registration,
specifications is to enable high performance and universal
tokens, management processes, authentication protocols and
interoperability. The introduction of iris and face specifications
related assertions. [Supersedes SP 800-63-1.]
into the current edition adds alternative modalities for biometric
authentication and extends coverage to persons for whom
Contacts:
fingerprinting is problematic. The addition of on-card comparison
offers an alternative to PIN-mediated card activation as well as Dr. Lily Chen Mr. William Burr
an additional authentication method. lily.chen@nist.gov william.burr@nist.gov
Contacts: SP 800-56A Revision 2, Recommendation for
Pair-Wise Key-Establishment Schemes Using
Dr. Chandramouli (Mouli) Mr. Patrick Grother
Ramaswamy patrick.grother@nist.gov Discrete Logarithm Cryptography
mouli@nist.gov
This recommendation specifies key-establishment schemes
based on the discrete logarithm problem over finite fields and
Draft SP 800-73-4, Interfaces for
elliptic curves, including several variations of Diffie-Hellman
Personal Identity Verification (3 Parts)
and Menezes-Qu-Vanstone (MQV) key establishment schemes.
Part 1- PIV Card Application Namespace, [Supersedes SP 800-56A.]
Data Model and Representation
Contacts:
Part 2- PIV Card Application Card Command Interface
Ms. Elaine Barker Dr. Lily Chen
Part 3- PIV Client Application Programming Interface elaine.barker@nist.gov lily.chen@nist.gov
FIPS 201 defines the requirements and characteristics of a
Dr. Allen Roginsky
government-wide interoperable identity credential. FIPS 201
allen.roginsky@nist.gov
also specifies that this identity credential must be stored on a
smart card. This document, SP 800-73, contains the technical
SP 800-53 Revision 4, Security and Privacy Controls for
specifications to interface with the smart card to retrieve and
Federal Information Systems and Organizations
use the PIV identity credentials. The specifications reflect the
design goals of interoperability and PIV Card functions. The This publication provides a catalog of security and privacy
goals are addressed by specifying a PIV data model, card edge controls for federal information systems and organizations
interface, and application-programming interface. Moreover, and a process for selecting controls to protect organizational
this document enumerates requirements where the international operations (including mission, functions, image, and reputation),
integrated circuit card standards [ISO7816] include options organizational assets, individuals, other organizations, and the
and branches. The specifications go further by constraining Nation from a diverse set of threats including hostile cyber-
implementers’ interpretations of the normative standards. Such attacks, natural disasters, structural failures, and human errors
restrictions are designed to ease implementation, facilitate (both intentional and unintentional). The security and privacy
interoperability, and ensure performance, in a manner tailored controls are customizable and implemented as part of an
for PIV applications. organization-wide process that manages information security
and privacy risk. The controls address a diverse set of security
Contacts: and privacy requirements across the Federal Government and
Dr. Chandramouli (Mouli) Dr. David Cooper critical infrastructure, derived from legislation, Executive Orders,
Ramaswamy david.cooper@nist.go policies, directives, regulations, standards, and/or mission/
mouli@nist.gov business needs. The publication also describes how to develop
Ms. Hildegard (Hildy) Ferraiolo Mr. Salvatore Francomacaro specialized sets of controls, or overlays, tailored for specific types
hildegard.ferraiolo@nist.gov salvatore.francomacaro@nist.gov of missions/business functions, technologies, or environments
Mr. Ketan Mehta of operation. Finally, the catalog of security controls addresses
ketan.mehta@nist.gov security from both a functionality perspective (the strength of
80
Computer Security Division Annual Report - 2013

security functions and mechanisms provided) and an assurance Contact:
perspective (the measures of confidence in the implemented Mr. Murugiah Souppaya
security capability). Addressing both security functionality murugiah.souppaya@nist.gov
and assurance helps to ensure that information technology
component products and the information systems built from SP 800-38F, Recommendation for Block Cipher Modes
those products using sound system and security engineering of Operation: Methods for Key Wrapping
principles are sufficiently trustworthy. [Supersedes SP 800-53
This publication describes cryptographic methods that
Revision 3.]
are approved for key wrapping, i.e., the protection of the
confidentiality and integrity of cryptographic keys. In addition
Contacts:
to describing existing methods, this publication specifies two
NIST FISMA Team Dr. Ron Ross
new, deterministic authenticated-encryption modes of operation
sec-cert@nist.gov rross@nist.gov
of the Advanced Encryption Standard (AES) algorithm: the AES
Mr. Arnold Johnson Ms. Kelley Dempsey Key Wrap (KW) mode and the AES Key Wrap With Padding (KWP)
kelley.dempsey@nist.gov mode. An analogous mode with the Triple Data Encryption
Algorithm (TDEA) as the underlying block cipher, called TKW, is
Draft SP 800-52 Revision 1, Guidelines for the also specified, to support legacy applications.
Selection, Configuration, and Use of Transport Layer
Security (TLS) Implementations Contact:
Dr. Morris Dworkin
Transport Layer Security (TLS) provides mechanisms to
morris.dworkin@nist.gov
protect sensitive data during electronic dissemination across
the Internet. This Special Publication provides guidance to the
Draft SP 800-38 G, Recommendation for
selection and configuration of TLS protocol implementations
Block Cipher Modes of Operation: Methods
while making effective use of FIPS and NIST-recommended
for Format-Preserving Encryption
cryptographic algorithms, and requires that TLS 1.1 configured
with FIPS-based cipher suites as the minimum appropriate This recommendation specifies three methods for format-
secure transport protocol and recommends that agencies preserving encryption, called FF1, FF2, and FF3. Each of these
develop migration plans to TLS 1.2 by January 1, 2015. This methods is a mode of operation of the AES algorithm, which is
publication also identifies TLS extensions for which mandatory used to construct a round function within the Feistel structure
support must be provided and other recommended extensions. for encryption.
Contacts: Contact:
Ms. Kerry McKay Mr. William (Tim) Polk Dr. Morris Dworkin
kerry.mckay@nist.gov william.polk@nist.gov morris.dworkin@nist.gov
SP 800-40 Revision 3, Guide to Enterprise Patch
ª
NIST Interagency Reports (NISTIRs)
Management Technologies
Patch management is the process for identifying, acquiring,
NISTIR 7957, Conformance Test Architecture
installing, and verifying patches for products and systems.
and Test Suite for ANSI/NIST-ITL 1-2011
Patches correct security and functionality problems in software
NIEM XML Encoded Transactions
and firmware. There are several challenges that complicate
patch management. If organizations do not overcome these The latest version of the ANSI/NIST-ITL standard was
challenges, they will be unable to patch systems effectively published in November 2011 (AN-2011). In addition to specifying
and efficiently, leading to easily preventable compromises. This Record Types in traditional encoding, the standard includes
publication is designed to assist organizations in understanding the specification of National Information Exchange Model
the basics of enterprise patch management technologies. It (NIEM) Extensible Markup Language (XML) encoding and an
explains the importance of patch management and examines associated schema. The Computer Security Division of NIST/ITL
the challenges inherent in performing patch management. developed a Conformance Test Architecture (CTA) and Test Suite
It provides an overview of enterprise patch management (CTS) called “BioCTS for AN-2011 NIEM XML” designed to test
technologies and it also briefly discusses metrics for measuring implementations of AN-2011 NIEM XML encoded transactions.
the technologies effectiveness and for comparing the relative Validating the XML files to a schema may indicate that the
importance of patches. [Supersedes SP 800-40 Version 2.0.] contained data is formatted correctly and individual values are
within allowable ranges, assuming that the requirements for
81
FY 2013 Computer Security Division Publications

that data have been documented in the schema file. However, Draft NISTIR 7946, CVSS Implementation Guidance
schemas are not designed to test the internal consistency of
This Interagency Report provides guidance to individuals
implementations (i.e., testing for a relationship between two
scoring IT vulnerabilities using the Common Vulnerability Scoring
elements or structures within a transaction). These shortcomings
System (CVSS) Version 2.0 scoring metrics. The guidance in this
of XML schema files for use in conformance testing necessitate
document is the result of applying the CVSS specification to score
that schemas be used only as a component of a complete
over 50,000 vulnerabilities analyzed by the National Vulnerability
testing solution. This complete solution (the test tool) ensures
Database (NVD). An overview of the CVSS base metrics is first
test coverage of requirements through a combination of schema
presented, followed by guidance for difficult and/or unique
validation and conformance tests of the data in the XML files. This
scoring situations. To assist vulnerability analysts, common
document discusses the test software design including the XML
keywords and phrases are identified and accompanied by
Data Structures used and Classes implemented. It addresses
suggested scores for particular types of software vulnerabilities.
the testing phases and the format of the test results; as well
The report includes a collection of scored IT vulnerabilities from
as the user interface and key usability features implemented in
the NVD, alongside a justification for the provided score. Finally,
this version of the test tool. Details are provided on a modified
this report contains a description of the NVD’s vulnerability
schema that was required to be used in the tool in order to fully
scoring process.
perform tests for all the requirements specified in the AN-2011
standard. Future development steps, including support for the
Contacts:
new version of the ANSI/NIST-ITL standard under development,
Mr. Joshua Franklin Mr. Harold Booth
are also discussed.
joshua.franklin@nist.gov harold.booth@nist.gov
Contacts:
NISTIR 7933, Requirements and Conformance
Mr. Fernando Podio Mr. Dylan Yaga
Test Assertions for ANSI/NIST-ITL 1-2011
fernando.podio@nist.gov dylan.yaga@nist.gov
Record Type 18 - DNA Record
Mr. Christofer McGinnis
CSD, in NIST’s Information Technology Laboratory (NIST/ITL),
christofer.mcginnis@nist.gov
develops conformance test architectures (CTA) and test suites
(CTS) to support users that require conformance to selected
NISTIR 7956, Cryptographic Key Management
biometric standards. Product developers as well as testing
Issues & Challenges in Cloud Services
laboratories can also benefit from the use of these tools. This
To interact with various services in the cloud and to store project supports the possible establishment of conformity
the data generated/processed by those services, several assessment programs for biometrics and also supports NIST/
security capabilities are required. The publication considers ITL’s Forensic Science Program by making conformance testing
a core set of features in the three common cloud services: tools available that provide developers, users, and purchasers
Infrastructure as a Service (IaaS), Platform as a Service (PaaS), with increased levels of confidence in product quality and
and Software as a Service (SaaS). The report identifies a set of increases the probability of successful interoperability of
security capabilities needed to exercise those features and the biometrics and forensic data. One of the test tools is a CTA/
cryptographic operations they entail. An analysis of the common CTS designed to test implementations of ANSI/NIST-ITL 1-2011
state of practice of the cryptographic operations that provide (AN-2011) Data Format for the Interchange of Fingerprint, Facial
those security capabilities reveals that the management of & Other Biometric Information, for selected Record Types based
cryptographic keys takes on an additional complexity in cloud on 1,200 test assertions previously developed. As part of the
environments compared to enterprise IT environments due to: process associated with the extension of the first version of
(a) difference in ownership (between cloud Consumers and BioCTS for AN-2011, NIST/ITL CSD’s staff identified over 200 test
cloud Providers) and (b) control of infrastructures on which both assertions necessary to meet the conformance requirements for
the Key Management System (KMS) and protected resources the AN-2011 Record Type 18- DNA Record. These test assertions
are located. This document identifies the cryptographic key are documented using the format specified in SP 500-295,
management challenges in the context of architectural solutions Conformance Testing Methodology for ANSI/NIST-ITL 1- 2011,
that are commonly deployed to perform those cryptographic Data Format for the Interchange of Fingerprint, Facial & Other
operations. Biometric Information (Release 1.0).
Contacts: Contacts:
Dr. Chandramouli (Mouli) Dr. Michaela Iorga Mr. Fernando Podio Mr. Dylan Yaga
Ramaswamy michaela.iorga@nist.gov fernando.podio@nist.gov dylan.yaga@nist.gov
mouli@nist.gov
Mr. Christofer McGinnis
christofer.mcginnis@nist.gov
82
Computer Security Division Annual Report - 2013

Draft NISTIR 7924, Reference Certificate Policy NISTIR 7896, Third-Round Report of the SHA-3
Cryptographic Hash Algorithm Competition
The purpose of this document is to identify a baseline set of
NIST opened a public competition on November 2, 2007 to
security controls and practices to support the secure issuance of
develop a new cryptographic hash algorithm - SHA-3, which
certificates. This baseline was developed with publicly-trusted
will augment the hash algorithms specified in FIPS 180-4,
Certificate Authorities (CA) in mind. These CAs, who issue the
Secure Hash Standard. The competition was NIST’s response
certificates used to secure websites and sign software, play a
to advances in the cryptanalysis of hash algorithms. NIST
particularly important role online. This document is formatted
received 64 submissions in October 2008, and selected 51
as a Reference Certificate Policy (CP). We expect different
first-round candidates on December 10, 2008; 14 second-
applications and relying party communities will tailor this
round candidates on July 24, 2009; and 5 third-round
document based on their specific needs. It was structured and
developed so that the CP developer can fill in sections specific
candidates - BLAKE, Grøstl, JH, KeccaK and Skein, on December
9, 2010, to advance to the final round of the competition.
to organizational needs and quickly produce a suitable CP.
Eighteen months were provided for the public review of the
This Reference CP is consistent with the Internet Engineering
finalists, and on October 2, 2012, NIST announced the winner
Task Force (IETF) Public Key Infrastructure X.509 (IETF PKIX)
Certificate Policy and Certification Practices Framework.
algorithm of the SHA-3 competition − KeccaK. This report
summarizes the evaluation of the 5 finalists, and the selection
of the SHA-3 winner.
Contacts:
Mr. Harold Booth Mr. Andrew Regenscheid Contacts:
harold.booth@nist.gov andrew.regenscheid@nist.gov
Ms. Shu-jen Chang Mr. Ray Perlner
shu-jen.chang@nist.gov ray.perlner@nist.gov
NISTIR 7916, Proceedings of the Cybersecurity in
Cyber-Physical Systems Workshop, April 23-24, 2012 Mr. William Burr Dr. Meltem Sönmez Turan
william.burr@nist.gov meltem.turan@nist.gov
This publication contains the proceeding, abstracts, and
present slides from the Cybersecurity in Cyber-Physical Systems Dr. John Kelsey Mr. Lawrence (Larry) Bassham
Workshop of April 23-24, 2012. Some of the cyber-physical john.kelsey@nist.gov lawrence.bassham@nist.gov
systems covered during the first day of the workshop included
networked automotive vehicles, networked medical devices, NISTIR 7878, Combinatorial Coverage Measurement
semi-conductor manufacturing, and cyber-physical testbeds. Combinatorial testing applies factor covering arrays to test
Dr. Farnham Jahanian, National Science Foundation, was the all t-way combinations of input or configuration state space.
keynote speaker on the first day of the workshop. Day two of the In some testing situations, it is not practical to use covering
workshop covered the electric smart grid. arrays, but any set of tests covers at least some portion of
t-way combinations up to t [less than or equal to] n. This report
Contact: describes measures of combinatorial coverage that can be
Ms. Tanya Brewer used in evaluating the degree of t-way coverage of any test
tanya.brewer@nist.gov suite, regardless of whether it was initially constructed for
combinatorial coverage.
Draft NISTIR 7904, Trusted Geolocation in the
Cloud: Proof of Concept Implementation Contact:
This publication explains selected security challenges Mr. Rick Kuhn
involving Infrastructure as a Service (IaaS) cloud computing rkuhn@nist.gov
technologies and geolocation. It then describes a proof of concept
implementation that was designed to address those challenges. NISTIR 7817, A Credential Reliability and
The publication provides sufficient details about the proof of Revocation Model for Federated Identities
concept implementation so that organizations can reproduce it if A large number of Identity Management Systems (IDMS) are
desired. The publication is intended to be a blueprint or template being deployed worldwide that use different technologies for the
that can be used by the general security community to validate population of their users. With the diverse set of technologies,
and implement the described proof of concept implementation. and the unique business requirements for organizations to
federate, there is no uniform approach to the federation process.
Contacts: Similarly, there is no uniform method to revoke credentials or
Mr. Michael Bartock Mr. Murugiah Souppaya their associated attribute(s) in a federated community. In the
michael.bartock@nist.gov murugiah.souppaya@nist.gov absence of a uniform revocation method, this document seeks to
investigate credential and attribute revocation with a particular
83
FY 2013 Computer Security Division Publications

focus on identifying missing requirements. This document first glossary includes most of the terms in the NIST publications.
introduces and analyzes the different types of digital credentials It also contains nearly all of the terms and definitions from
and recommends missing revocation-related requirements for CNSSI-4009. This glossary provides a central resource of terms
each model in a federated environment. As a second goal, and and definitions most commonly used in NIST information security
as a by-product of the analysis and recommendations, this publications and in CNSS information assurance publications.
paper suggests a credential reliability and revocation service For a given term, all definitions from NIST documents are not
that serves to eliminate the missing requirements. included − especially not from the older NIST publications.
Since draft documents are not stable, those terms/definitions
Contact: are not referenced. Each entry in the glossary points to one
Ms. Hildegard (Hildy) Ferraiolo or more source NIST publications, and/or CNSSI-4009, and/or
hildegard.ferraiolo@nist.gov supplemental sources where appropriate. The NIST publications
referenced are the most recent versions of those publications
NISTIR 7622, Notional Supply Chain Risk Management (as of the date of this document). [Supersedes NISTIR 7298
Practices for Federal Information Systems Revision 1 (February 2011)]
This publication provides a wide array of practices that, when
implemented, will help mitigate supply chain risk to federal Contact:
information systems. It seeks to equip federal departments and Mr. Richard Kissel
agencies with a notional set of repeatable and commercially richard.kissel@nist.gov
reasonable supply chain assurance methods and practices
that offer a means to obtain an understanding of, and visibility Additional Publications by CSD Authors
throughout, the supply chain.
CSD authors actively contribute to the security community
Contacts: by authoring articles in the scholarly literature, participating in
technical conferences, contributing to encyclopedias and other
Mr. Jon Boyens Ms. Celia Paulsen
books, and publishing other “white papers” that fall outside the
jon.boyens@nist.gov celia.paulsen@nist.gov
scope of NIST Technical Series publications described in the
preceding section.
NISTIR 7511 Revision 3, Security Content
Automation Protocol (SCAP) Version 1.2
The following documents were published during FY 2013. For
Validation Program Test Requirements conference papers, the contributions listed below were accepted
This report defines the requirements and associated test for conferences held during FY 2013; in some cases the final
procedures necessary for products to achieve one or more proceedings were not published until FY 2014. All NIST authors
Security Content Automation Protocol (SCAP) validations. are identified using italics.
Validation is awarded based on a defined set of SCAP capabilities
Links to the preprints and/or final publications of the documents
by independent laboratories that have been accredited for SCAP
below are available at http://csrc.nist.gov/publications.
testing by the NIST National Voluntary Laboratory Accreditation
Program (NVLAP).
ª
Contacts: Journal Articles
Mr. David Waltermire Ms. Melanie Cook
J. Boyar, P. Matthews and R.C. Peralta, “Logic Minimization
david.waltermire@nist.gov melanie.cook@nist.gov
Techniques with Applications to Cryptology,” Journal of
Mr. Stephen Quinn Cryptology 26(2), 280-312 (April 2013). doi:10.1007/s00145-
stephen.quinn@nist.gov 012-9124-7.
A new technique for combinational logic
NISTIR 7298 Revision 2, Glossary of
optimization is described. The technique is a two-step
Key Information Security Terms
process. In the first step, the non-linearity of a circuit
NIST has received numerous requests to provide a summary { as measured by the number of non-linear gates it
glossary for our publications and other relevant sources, and to contains { is reduced. The second step reduces the
make the glossary available to practitioners. As a result of these number of gates in the linear components of the
requests, this glossary of common security terms was extracted already reduced circuit. The technique can be applied
from FIPS, the SP 800 series, NISTIRs, and the Committee for to arbitrary combinational logic problems, and often
yields improvements even after optimization by
National Security Systems Instruction 4009 (CNSSI-4009). This
84
Computer Security Division Annual Report - 2013

standard methods has been performed. In this paper D. Maughan, W.D. Newhouse and T. Vagoun, “Introducing the
we show the results of our technique when applied to Federal Cybersecurity R&D Strategic Plan,” The Next Wave - The
the S-box of the Advanced Encryption Standard (FIPS National Security Agency’s Review of Emerging Technologies
197, Advanced Encryption Standard (AES), National 19(4), 3-7 (2012).
Institute of Standards and Technology, 2001).
In December 2011, the White House Office of
We also show that in the second step, one is faced Science and Technology Policy (OSTP) released the
with an NP-hard problem, the Shortest Linear Program Trustworthy Cyberspace: Strategic Plan for the Federal
(SLP) problem, which is to minimize the number of Cybersecurity Research and Development Program
linear operations necessary to compute a set of linear —a framework for a set of coordinated federal
forms. In addition to showing that SLP is NP-hard, we strategic priorities and objectives for cybersecurity
show that a special case of the corresponding decision research. The release of this strategic plan marked
problem is Max SNP-Complete, implying limits to its an important milestone by the Federal Government’s
approximability. research community. It expresses an understanding
of key causes of cybersecurity deficiencies and
Previous algorithms for minimizing the number of
presents research themes with high potential to
gates in linear components produced cancellation-
significantly improve the security of cyber systems
free straight-line programs, i.e., programs in which
and infrastructure. The strategic plan is a culmination
there is no cancellation of variables in GF(2). We show
of many efforts within the Federal Government, most
that such algorithms have approximation ratios of at
notably by the Senior Steering Group for Cybersecurity
least 3/2 and therefore cannot be expected to yield
R&D (CSIA R&D SSG), the Cyber Security and
optimal solutions to non-trivial inputs. The straight-line
Information Assurance Interagency Working Group
programs produced by our techniques are not always
(CSIA IWG) of the Federal Networking and IT R&D
cancellation-free. We have experimentally verified
(NITRD) Program, and by the Special Cyber Operations
that, for randomly chosen linear transformations, they
Research and Engineering Interagency Working Group
are significantly smaller than the circuits produced by
(SCORE IWG).
previous algorithms.
C. McLeman and D. Moody, “Class Numbers via 3-Isogenies and
Q.H. Dang, “Changes in Federal Information Processing
Elliptic Surfaces,” International Journal of Number Theory 9(1),
Standard (FIPS) 180-4, Secure Hash Standard,” Cryptologia
125-138 (February 2013). doi:10.1142/S179304211250128X.
37(1), 69-73 (2013). doi:10.1080/01611194.2012.687431.
We show that a character sum attached to a family
This paper describes the changes between FIPS
of 3-isogenies defined on the fibers of a certain
180-3 and FIPS 180-4. FIPS 180-4 specifies two new
elliptic surface over Fp relates to the class number of
secure cryptographic hash algorithms: SHA-512/224
the quadratic imaginary number field Q(\sqrt{p}). In
and SHA-512/256; it also includes a method for
this sense, this provides a higher-dimensional analog
determining initial value(s) for any future SHA-512-
of some recent class number formulas associated to
based hash algorithm(s). FIPS 180-4 also removes a
2-isogenies of elliptic curves.
requirement for the execution of the message length
encoding operation.
J.A. Montenegro, M.J. Fischer, J. Lopez and R.C. Peralta,
“Secure Sealed-Bid Online Auctions Using Discreet Cryptographic
D. Ferraiolo, S. Gavrila, and W. Jansen, “Enabling an Enterprise-
Proofs,” Mathematical and Computer Modelling 57(11-12),
wide, Data-centric Operating Environment,” Computer (IEEE)
2583-2595 (June 2013). doi:10.1016/j.mcm.2011.07.027.
46(4), 94-96 (April 2013). doi:10.1109/MC.2013.130.
This work describes the design and implementation
Although access control (AC) currently plays an
of an auction system using secure multiparty
important role in securing data services, if properly
computation techniques. Our aim is to produce a
envisaged and designed, access control can serve a
system that is practical under actual field constraints
more vital role in computing than one might expect.
on computation, memory, and communication. The
The Policy Machine (PM), a framework for AC
underlying protocol is privacy-preserving, that is, the
developed at NIST, was designed with this goal in
winning bid is determined without information about
mind. The PM has evolved beyond just a concept to a
the losing bids leaking to either the auctioneer or other
prototype implementation and is now being directed
bidders. Practical implementation of the protocol is
toward an open source project.
feasible using circuit-based cryptographic proofs
along with additively homomorphic bit commitment.
Moreover, we propose the development of a Proof
85
FY 2013 Computer Security Division Publications

Certificate standard. These certificates convey They include the work of ISO Technical Committee
sufficient information to recreate the cryptographic 68 – Financial Services – SC 2 – Security, and the
proofs and verify them offline. International Telecommunication Union - Study Group
17- Security. Due to the large international impact
and adoption, the development of the ANSI/NIST-
D. Moody and A.S. Zargar, “On Integer Solutions of x^4+y^4- ITL standards led by the Information Technology
2z^4-2w^4=0,” Notes on Number Theory and Discrete Laboratory of NIST is also addressed. Although a
Mathematics 19(1), 37-43 (2013). detailed discussion on biometric standards adoption
In this article, we study the quartic Diophantine is beyond the scope of this paper, a few examples
equation x^4+y^4-2z^4-2w^4=0. We find non-trivial of global and national biometric standards adoption
integer solutions. Furthermore, we show that when a for verification and identification applications are
solution has been found, a series of other solutions can discussed.
be derived. We do so using two different techniques.
The first is a geometric method due to Richmond,
S.M. Radack and D.R. Kuhn, “Protecting Wireless Local Area
while the second involves elliptic curves.
Networks (WLANs),” IT Professional 14(6), 59-61 (November-
December 2012). doi:10.1109/MITP.2012.110.
W.D. Newhouse, “Securing America’s Digital Infrastructure This article summarizes the information that
Through Education,” The Next Wave - The National Security was presented in the February 2012 Information
Agency’s Review of Emerging Technologies 19(4), 30-36 (2012). Technology Laboratory (ITL) bulletin, Guidelines for
This article provides an overview of the establishment Securing Wireless Local Area Networks (WLANs). The
of the National Initiative for Cybersecurity Education bulletin, which was noted by WERB in February 2012,
(NICE), its government structure, and it goals. was based on NIST Special Publication (SP) 800-153,
Parallels are drawn between the strategic R&D Guidelines for Securing Wireless Local Area Networks
thrust, Developing Scientific Foundations, described (WLANs): Recommendations of the National Institute
in “Trustworthy Cyberspace: Strategic Plan for the of Standards and Technology. The article summarizes
Federal Cybersecurity Research and Development the bulletin for a professional technical publication,
Program” published in December 2011 and NICE’s and focuses on how organizations can implement
awareness, education, and workforce efforts. sound security practices throughout the life cycles
of their WLANs. Information is provided about access
to SP 500-153, and to other NIST resources that are
F.L. Podio, “Advances in Biometric Standardisation – available to help organizations improve the security of
Addressing Global Requirements for Interoperable Biometrics,” wireless local area networks, the system development
International Journal of Biometrics 5(1), 5-19 (2013). life cycle, and the management of risks to systems.
doi:10.1504/IJBM.2013.05073.
The paper discusses the current status of biometric
M. Sönmez Turan, “On the Nonlinearity of Maximum-length
standards development activities, with a focus on
NFSR Feedbacks,” Cryptography and Communication 4(3-4),
international standards developments. Published
233-243 (December 2012). doi:10.1007/s12095-012-0067-5.
standards, as well as standards under development
or planned for the near future, are addressed. The Linear Feedback Shift Registers (LFSR) are the
work of Joint Technical Committee 1 of ISO and IEC main building block of many classical stream ciphers;
Subcommittee 37 - Biometrics who is responsible however due to their inherent linearity, most of the
for the development of a large portfolio of biometric LFSR-based designs do not offer the desired security
standards in support of interoperability and data levels. In the last decade, using Nonlinear Feedback
interchange is addressed. The work of two other Shift Registers (NFSR) in stream ciphers became
JTC 1 Subcommittees, SC 17 Cards and personal very popular. However, the theory of NFSRs is not
identification and SC 27 - IT Security techniques well-understood, and there is no efficient method
who are also developing biometric standards within that constructs a cryptographically strong feedback
their scope of work is discussed. In many cases, the function with maximum period and also, given a
development of biometric standards impacts other feedback function it is hard to predict the period. In this
standards developments including token-based, paper, we study the maximum-length NFSRs, focusing
security, and telecommunication standards. Specific on the nonlinearity of their feedback functions. First,
examples of this impact are provided. Standards we provide some upper bounds on the nonlinearity of
activities performed in standards development the maximum-length feedback functions, and then we
bodies outside of ISO/IEC JTC 1 are also addressed. study the feedback functions having nonlinearity 2 in
86
Computer Security Division Annual Report - 2013

detail. We also show some techniques to improve the around γ·2^32 (γ is a experimentally determined
nonlinearity of a given feedback function using cross- constant and it is sufficient to estimate it as 2^8)
joining. related Keys and γ·2^64 chosen IVs, it is possible
to obtain 32·γ simple nonlinear equations and solve
them to recover the Secret Key in Grain-128a.
ª
Conference Papers
J. Boyar, M. Find and R. Peralta, “Four Measures of
M. Albanese, S. Jajodia, A. Singhal and L. Wang, “An Efficient Nonlinearity,” Eighth International Conference on Algorithms
Approach to Assessing the Risk of Zero-Day Vulnerabilities,” and Complexity (CIAC 2013), Barcelona, Spain, May 22-24,
10th International Conference on Security and Cryptography 2013. In Lecture Notes in Computer Science 7878, Algorithms
(SECRYPT 2013), Reykjavik, Iceland, July 29-31, 2013.[To and Complexity, P. G. Spirakis and M. Serna, eds., Springer,
be published in a volume of Springer’s Communications in Berlin (2013) 61-72. doi:10.1007/978-3-642-38233-8_6.
Computer and Information Science series.]
Cryptographic applications, such as hashing, block
*This paper received the Best Paper Award at ciphers and stream ciphers, make use of functions
SECRYPT 2013. which are simple by some criteria (such as circuit
Computer systems are vulnerable to both known implementations), yet hard to invert almost everywhere.
and zero-day attacks. Although known attack patterns A necessary condition for the latter property is to be
can be easily modeled, thus enabling the development “sufficiently distant” from linear, and cryptographers
of suitable hardening strategies, handling zero- have proposed several measures for this distance.
day vulnerabilities is inherently difficult due to In this paper, we show that four common measures,
their unpredictable nature. Previous research has nonlinearity, algebraic degree, annihilator immunity,
attempted to assess the risk associated with unknown and multiplicative complexity, are incomparable in the
attack patterns, and a suitable metric to quantify such sense that for each pair of measures, μ1, μ2, there
risk, the k-zero-day safety metric, has been defined. exist functions f1, f2 with μ1(f1) > _μ1(f2) but μ2(f1)
However, existing algorithms for computing this metric < _μ2(f2). We also present new connections between
are not scalable, and must assume that complete two of these measures. Additionally, we give a lower
zero-day attack graphs have been generated, which bound on the multiplicative complexity of collision-
may be infeasible in practice for large networks. In free functions.
this paper, we propose a set of polynomial algorithms R. Chandramouli, “Security Assurance Requirements for
for estimating the k-zero-day safety of possibly large Hypervisor Deployment Features,” Seventh International
networks efficiently, without pre-computing the entire Conference on Digital Society (ICDS 2013), Nice, France,
attack graph. We validate our approach through February 24-March 1, 2013, L. Berntzen and C-P Rückemann,
experiments, and show that the proposed algorithms eds., Xpert Publishing Services, Wilmington, Delaware (2013)
are computationally efficient and accurate. 120-125.
Virtualized hosts provide abstraction of the
S. Banik, S. Maitra, S. Sarkar and M. Sönmez Turan, “A hardware resources (e.g., CPU, Memory) enabling
Chosen IV Related Key Attack on Grain-128a,” 18th Australasian multiple computing stacks to be run on a single
Conference on Information Security and Privacy (ACISP 2013), physical machine. The Hypervisor is the core software
Brisbane, Australia, July 1-3, 2013. In Lecture Notes in Computer that enables this virtualization and hence must be
Science 7959, Information Security and Privacy, C. Boyd and L. configured to ensure security robustness for the
Simpson, eds., Springer, Berlin (2013) 13-26. doi:10.1007/978- entire virtualization infrastructure. Among the various
3-642-39059-3_2. combination of hypervisor types and hypervisor
hardware platforms, we have chosen a reference
Due to the symmetric padding used in the stream
architecture as the basis for our set of deployment
cipher Grain v1 and Grain-128, it is possible to
features. For each deployment feature, this paper
find Key-IV pairs that generate shifted keystreams
looks at the configuration options and analyzes the
efficiently. Based on this observation, Lee et al.
security implications of the options/deployment
presented a chosen IV related Key attack on Grain v1
feature to derive a set of assurance requirements that
and Grain-128 at ACISP 2008. Later, the designers
are (a) provided by each of the configuration options or
introduced Grain-128a having an asymmetric padding.
(b) are required for that deployment feature as a whole
As a result, the existing idea of chosen IV related Key
regardless of configuration options.
attack does not work on this new design. In this paper,
we present a Key recovery attack on Grain-128a, in
a chosen IV related Key setting. We show that using
87
FY 2013 Computer Security Division Publications

P. Cheng, L. Wang, S. Jajodia and A. Singhal, “Aggregating R. Johnson, Z. Wang, A. Stavrou and J. Voas, “Exposing
CVSS Base Scores for Semantics Rich Network Security Software Security and Availability Risks For Commercial
Metrics,” 2012 IEEE 31st Symposium on Reliable Distributed Mobile Devices,” Proceedings of the Annual Reliability and
Systems (SRDS), Irvine, CA, United States, October 8-11, Maintainability Symposium, 2013 (RAMS’13), Orlando, Florida,
2012, IEEE Computer Society, Washington, DC (2012) 31-40. January 28-31, IEEE, New York (2013) 1-7. doi:10.1109/
doi:10.1109/SRDS.2012.4. RAMS.2013.6517735.
A network security metric is desirable in evaluating In this manuscript, we present our efforts towards
the effectiveness of security solutions in distributed a framework for exposing the functionality of a mobile
systems. Aggregating CVSS scores of individual application through a combination of static and
vulnerabilities provides a practical approach dynamic program analysis that attempts to explore
to network security metric. However, existing all available execution paths including libraries. We
approaches to aggregating CVSS scores usually cause verified our approach by testing a large number of
useful semantics of individual scores to be lost in the Android applications with our program to exhibit its
aggregated result. In this paper, we address this issue functionality and viability. The framework allows
through two novel approaches. First, instead of taking complete automation of the execution process so
each base score as an input, our approach drills down that no user input is required. We also discuss how
to the underlying base metric level where dependency our static analysis program can be used to inform
relationships have well-defined semantics. Second, the execution of the dynamic analysis program. The
our approach interprets and aggregates the base program can serve as an extensible basis to fulfill
metrics from three different aspects in order to other useful purposes such as symbolic execution,
preserve corresponding semantics of the individual program verification, interactive debugger, and other
scores. Finally, we confirm the advantages of our approaches that require deep inspection of an Android
approaches through simulation. application.
V. C. Hu and K. Scarfone, “Real-Time Access Control Rule Fault D.R. Kuhn, I. Dominquez Mendoza, R.N. Kacker and Y.
Detection Using a Simulated Logic Circuit,” 2013 International Lei, “Combinatorial Coverage Measurement Concepts and
Conference on Social Computing (SocialCom), Washington, DC, Applications,” International Workshop on Combinatorial Testing
September 8-14, 2013, IEEE Computer Society, Washington, DC 2013 (IWCT 2013), Luxembourg, March 22, 2013, IEEE Computer
(2013) 494-501. doi:10.1109/SocialCom.2013.76. Society, Washington, DC (2013) 352-361. doi:10.1109/
ICSTW.2013.77.
Access control (AC) policies can be implemented
based on different AC models, which are fundamentally Combinatorial testing applies factor covering arrays
composed by semantically independent AC rules in to test all t-way combinations of input or configuration
expressions of privilege assignments described by state space. In some testing situations, it is not
attributes of subjects/attributes, actions, objects/ practical to use covering arrays, but any set of tests
attributes, and environment variables of the protected covers at least some portion of t-way combinations
systems. Incorrect implementations of AC policies up to t [less than or equal to] n. This report describes
result in faults that not only leak but also disable access measures of combinatorial coverage that can be used
of information, and faults in AC policies are difficult in evaluating the degree of t-way coverage of any test
to detect without support of verification or automatic suite, regardless of whether it was initially constructed
fault detection mechanisms. This research proposes for combinatorial coverage.
an automatic method through the construction of a
simulated logic circuit that simulates AC rules in AC
policies or models. The simulated logic circuit allows C. Liu, A. Singhal and D. Wijesekera, “Mapping Evidence
real-time detection of policy faults including conflicts Graphs to Attack Graphs,” IEEE International Workshop
of privilege assignments, leaks of information, and on Information Forensics and Security 2012 (WIFS 2012),
conflicts of interest assignments. Such detection is Tenerife, Spain, December 2-5, 2012, IEEE Signal Processing
traditionally done by tools that perform verification Society, Piscataway, New Jersey (2012) 121-126. doi:10.1109/
or testing after all the rules of the policy/model are WIFS.2012.6412636.
completed, and it provides no information about Attack graphs compute potential attack paths from
the source of verification errors. The real-time fault a system configuration and known vulnerabilities of
detecting capability proposed by this research allows a system. Evidence graphs model intrusion evidence
a rule fault to be detected and fixed immediately and dependencies among them for forensic analysis.
before the next rule is added to the policy/model, thus In this paper, we show how to map evidence graphs to
requiring no later verification and saving a significant attack graphs. This mapping is useful for application
amount of fault fixing time.
88
Computer Security Division Annual Report - 2013

of attack graphs and evidence graphs for forensic have been several recent attempts at formalizing more
analysis. In addition to helping to refine attack graphs robust security arguments in this venue with varying
by comparing attack paths in both attack graphs and degrees of applicability. We present an extension
evidence graphs, important probabilistic information of one such recent measure of security against
contained in evidence graphs can be used to compute a differential adversary, which has the benefit of
or refine potential attack success probabilities being immediately applicable in a general setting on
contained in repositories like CVSS. Conversely, attack unmodified multivariate schemes.
graphs can be used to add missing evidence or remove
irrelevant evidence to build a complete evidence graph.
In particular, when attackers use anti-forensics tools M. Sönmez Turan, “Related-Key Slide Attacks on Block Ciphers
to destroy or distort evidence, attack graphs can help with Secret Components,” Second International Workshop on
investigators recover the attack scenarios and explain Lightweight Cryptography for Security and Privacy, Gebze,
the lack of evidence for missing steps. We illustrate Turkey, May 6-7, 2013. In Lecture Notes in Computer Science
the mapping using a database attack as a case study. 8162, Lightweight Cryptography for Security and Privacy,
G. Avoine and O. Kara, eds., Springer, Berlin (2013) 28-42.
doi:10.1007/978-3-642-40392-7_3.
C. Liu, A. Singhal and D. Wijesekera, “Creating Integrated
Lightweight cryptography aims to provide sufficient
Evidence Graphs for Network Forensics,” Ninth Annual IFIP WG
security with low area/power/energy requirements
11.9 International Conference on Digital Forensics, Orlando,
for constrained devices. In this paper, we focus
FL, United States, January 28-30, 2013. In IFIP Advances in
on the lightweight encryption algorithm specified
Information and Communication Technology 410, Advances in
and approved in NRS 009-6-7:2002 by Electricity
Digital Forensics IX, G. Peterson and S. Shenoi, eds., Springer,
Suppliers Liaison Committee to be used with tokens
Berlin (2013) 227-241. doi:10.1007/978-3-642-41148-9_16.
in prepayment electricity dispensing systems in South
Evidence Graphs model network intrusion evidence Africa. The algorithm is a 16-round SP network with
and their dependencies, which helps network two 4-to-4 bit S-boxes and a 64-bit permutation. The
forensics analysts collate and visualize dependencies. S-boxes and the permutation are kept secret and
In particular, probabilistic evidence graph provide provided only to the manufacturers of the system
a way to link probabilities associated with different under license conditions. We present related-key
attack paths with available evidence. Existing work in slide attacks to recover the secret key and secret
evidence graphs assume that all evidence is available components using four scenarios; (i) known S-box
as one graph. We show how to merge different evidence and permutation with 2^48 time complexity using
graphs with or without the help of attack graphs. We 2^16 + 1 chosen plaintexts; (ii) unknown S-box and
show this by providing algorithms and a case study known permutation with 2^55 time complexity using
based on attacks on a fileserver and a database server 2^22.71 + 1 chosen plaintexts; (iii) known S-box and
in a lab network environment. An integrated evidence unknown permutation with 2^48 time complexity
graphs that show all attacks launched toward a global using 2^16 + 1 chosen plaintexts and 2^12.28
network are more useful for forensics analysts and adaptively chosen plaintexts; and finally, (iv) unknown
network administrators in searching for forensic S-box and permutation, with 2^48 time complexity
evidence and safeguarding networks respectively. using 2^22.71 + 1 chosen plaintexts and 2^31.29
adaptively chosen plaintexts. We also extend these
attacks to recover the secret components in a chosen-
R. Perlner and D. Smith, “A Classification of Differential key setting with practical complexities.
Invariants for Multivariate Post-quantum Cryptosystems,”
Fifth International Workshop on Post-Quantum Cryptography ª
Books and Book Sections
(PQCrypto 2013), Limoges, France, June 4-7, 2013. In Lecture
Notes in Computer Science 7932, A Classification of Differential
D.R. Khun, R.N. Kacker and Y. Lei. Introduction to Combinatorial
Invariants for Multivariate Post-quantum Cryptosystems, P.
Testing. Boca Raton, Florida: CRC Press, 2013.
Gaborit, ed., Springer, Berlin (2013) 165-173. doi:10.1007/978-
3-642-38616-9_11. Combinatorial testing of software analyzes
interactions among variables using a very small
Multivariate Public Key Cryptography (MPKC)
number of tests. This advanced approach has
has become one of a few options for security in
demonstrated success in providing strong, low-
the quantum model of computing. Though a few
cost testing in real-world situations. Introduction
multivariate systems have resisted years of effort from
to Combinatorial Testing presents a complete self-
the cryptanalytic community, many such systems have
contained tutorial on advanced combinatorial testing
fallen to a surprisingly small pool of techniques. There
methods for real-world software.
89
FY 2013 Computer Security Division Publications

The book introduces key concepts and procedures C. Paulsen and J. Boyens, “Summary of the Workshop on
of combinatorial testing, explains how to use software Information and Communication Technologies Supply Chain Risk
tools for generating combinatorial tests, and shows Management, National Institute of Standards and Technology,
how this approach can be integrated with existing October 15-16, 2012,” National Institute of Standards and
practice. Detailed explanations and examples clarify Technology, Gaithersburg, Maryland, July 10, 2013, 21 pp.
how and why to use various techniques. Sections on
There is a great demand from federal departments
cost and practical considerations describe tradeoffs
and agencies for supply chain risk management
and limitations that may impact resources or funding.
(SCRM) guidance. This document is a summary of a
While the authors introduce some of the theory and
workshop held October 15-16, 2012 to broadly engage
mathematics of combinatorial methods, readers can
all stakeholders in an effort to set a foundation for
use the methods without in-depth knowledge of the
NIST’s future work on Information and Communication
underlying mathematics.
Technologies SCRM.
Accessible to undergraduate students and
researchers in computer science and engineering,
this book illustrates the practical application of
combinatorial methods in software testing. Giving
pointers to freely available tools and offering resources
on a supplementary website, the book encourages
readers to apply these methods in their own testing
projects.
ª
White Papers
NIST Cloud Computing Public Security Working Group [M.
Iorga], “Challenging Security Requirements for US Government
Cloud Computing Adoption,” National Institute of Standards
and Technology, Gaithersburg, Maryland, November 27, 2012,
61 pp.
The Federal Cloud Strategy, February 8, 2010,
outlines a federal cloud computing program that
identifies program objectives aimed at accelerating
the adoption of cloud computing across the Federal
Government. NIST, along with other agencies, was
tasked with a key role and specific activities in support
of that effort, including the delivery of the NIST Cloud
Computing Technology Roadmap and the publication of
other Special Publications that address the reference
architecture, definitions, and security aspects of cloud
computing. In order to achieve adoption of cloud
computing for the Federal Government, it is necessary
to address the security and privacy concerns that
federal agencies have when migrating their services
to a cloud environment. To further exacerbate the
situation, there are few documented details that
directly address how to achieve some security aspects
in a cloud environment. The purpose of this document
is to provide an overview of the high-priority security
and privacy challenges perceived by federal agencies
as impediments to the adoption of cloud computing.
The document provides descriptions of the existing
mitigations to these security and privacy impediments.
If no mitigations are listed, then ongoing efforts that
could lead to mitigations are described. In the cases
where no ongoing efforts were identified, the document
makes recommendations for possible mitigation or
references existing best practices.
90
Computer Security Division Annual Report - 2013

Cybersecurity Framework
Policy Machine
Cloud Computing
Standards
yhpargotpyrC
Risk Management Framework
Biometrics
Assets
Security Practices
Security Controls
Verification
tnemeganam
ksir
niahc
ylppuS
Authorization
FISMA
Validated Products List
Mobile Devices
Continuous Monitoring
FIPS 140-2
EO
13636
Roadmap
Opportunities to Engage
with CSD and NIST
91

ª ª
Guest Research Internships at NIST Security Research
Opportunities are available at NIST for 6- to 24-month NIST occasionally undertakes security work, primarily in the
internships within CSD. Qualified individuals should contact area of research, funded by other agencies. Such sponsored
CSD, provide a statement of qualifications, and indicate the work is accepted by NIST when it can cost effectively further
area of work that is of interest. Generally speaking, the salary the goals of NIST and the sponsoring institution. For further
costs are borne by the sponsoring institution; however, in some information, contact:
cases, these guest research internships carry a small monthly
stipend paid by NIST. For further information, contact: Ms. Donna Dodson
(301) 975-8443
donna.dodson@nist.gov
Ms. Donna Dodson Mr. Matthew Scholl
(301) 975-8443 (301) 975-2941
donna.dodson@nist.gov matthew.scholl@nist.gov
ª
Funding Opportunities at NIST
ª
Details at NIST for Government or Military NIST funds industrial and academic research in a variety of
Personnel ways. The Small Business Innovation Research Program funds
R&D proposals from small businesses; see www.nist.gov/sbir.
Opportunities are available at NIST for 6- to 24-month details CSD also offers other grants to encourage work in specific fields:
at NIST in CSD. Qualified individuals should contact CSD, precision measurement, fire research, and materials science.
provide a statement of qualifications, and indicate the area of Grants/awards supporting research at industry, academia, and
work that is of interest. Generally speaking, the salary costs other institutions are available on a competitive basis through
are borne by the sponsoring agency; however, in some cases, several different Institute offices.
agency salary costs may be reimbursed by NIST. For further
For general information on NIST grants programs, please
information, contact:
contact:
Ms. Donna Dodson Mr. Matthew Scholl
Mr. Christopher Hunton
(301) 975-8443 (301) 975-2941
(301) 975-5718
donna.dodson@nist.gov matthew.scholl@nist.gov
christopher.hunton@nist.gov
ª Funding opportunity information:
Federal Computer Security Program
Managers’ Forum (FCSPM)
http://www.nist.gov/director/ocfo/grants/grants.cfm
The FCSPM Forum is covered in detail in the Outreach
section of this report. Membership is free and open to federal
employees. For further information, contact:
Mr. Kevin Stine
(301) 975-4483
kevin.stine@nist.gov or sec-forum@nist.gov
Visit the FCSPM Forum website:
http://csrc.nist.gov/groups/SMA/forum/membership.html
92
Computer Security Division Annual Report - 2013

Cybersecurity Framework
Policy Machine
Cloud Computing
Standards
yhpargotpyrC
Risk Management Framework
Biometrics
Assets
Security Practices
Security Controls
Verification
tnemeganam
ksir
niahc
ylppuS
Authorization
FISMA
Validated Products List
Mobile Devices
Continuous Monitoring
FIPS 140-2
EO
13636
Roadmap
Acknowledgments
The editor, Patrick O’Reilly of the Computer Security Division, wishes to thank his colleagues in the
Computer Security Division, who provided write-ups on their 2013 project highlights and accomplishments
for this annual report (their names are mentioned after each project write-up). The editor would also like
to acknowledge Barbara Guttman, Kevin Stine, Jim Foti (ITL, NIST), Greg Witte, Chris Johnson and Doug
Rike (G2) for reviewing and providing valuable feedback for this annual report. The Editor also would like
to thank Lorie Richards (Facilities Services Division, Creative and Printing Service, NIST) for designing the
cover and final layout of our division’s annual report. Finally, the editor would like to thank Joshua Franklin
and Michaela Iorga (Computer Security Division, ITL, NIST) for their input with the 2013 annual report cover
design.
93

This page is intentionally left blank.
94
Computer Security Division Annual Report - 2013

Cybersecurity Framework
Access
Control
Cloud Computing
Policy Machine
yhpargotpyrC
Evaluation
Standards
Guidelines
Security Practices
Security Controls
Critical Infrastructure
Assets
Verification
Systems
krowemarF
tnemeganaM
ksiR
Biometrics
tnemeganam
ksir
niahc
ylppuS
FIPS 140-2
Validated
Products
List
FISMA
Mobile Devices
Continuous Monitoring
Authorization
Assets
EO
13636
Cybersecurity Framework
Roadmap
Computer
Security
Division
2013 Annual Report
NIST Special Publication 800-170
Access
Control
Cloud Computing
Policy Machine
yhpargotpyrC
Evaluation
Guidelines
Standards
Security Controls
Security Practices
Critical Infrastructure
Systems
Assets
Verification
krowemarF
tnemeganaM
ksiR
Biometrics
tnemeganam
ksir
niahc
ylppuS
FIPS 140-2
Validated
Products
List
FISMA
Authorization
Mobile Devices
Continuous Monitoring
EO
13636
Assets Roadmap

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-25", "model": "legacy"} -->
