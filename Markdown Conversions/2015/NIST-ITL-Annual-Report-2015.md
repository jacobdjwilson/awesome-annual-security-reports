COMPUTER SECURITY DIVISION
| A N | N U | A L |   R E | P O | R T |
| --- | --- | --- | ----- | --- | --- |
|     |     |     |       | 2 0 | 1 5 |
NIST SPECIAL PUBLICATION 800-182

THIS PAGE IS LEFT INTENTIONALLY BLANK.
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

NIST SPECIAL PUBLICATION 800-182
COMPUTER SECURITY DIVISION
| A N                               | N U | A L |   R E | P O           | R T |
| --------------------------------- | --- | --- | ----- | ------------- | --- |
|                                   |     |     | 2     | 0             | 1 5 |
| PATRICK O’REILLY, EDITOR          |     |     |       | CO-EDITORS:   |     |
| Computer Security Division        |     |     |       | Larry Feldman |     |
| Information Technology Laboratory |     |     |       | Greg Witte    |     |
G2, Inc.
Annapolis Junction, Maryland
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM
http://dx.doi.org/10.6028/NIST.SP.800-182
JULY 2016
U.S. DEPARTMENT OF COMMERCE
Penny S. Pritzker, Secretary
NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY
Willie May, Under Secretary of Commerce for Standards and Technology and Director

## Table of Contents
- [Disclaimer](#disclaimer)
- [Acknowledgments](#acknowledgments)
- [Trademark Information](#trademark-information)
- [Welcome Letter](#welcome-letter)
- [Computer Security Division (CSD) Organization](#computer-security-division-csd-organization)
- [Introduction to CSD’s Five Groups](#introduction-to-csds-five-groups)
  - [Cryptographic Technology Group (CTG)](#cryptographic-technology-group-ctg)
  - [Security Components and Mechanisms Group (SCMG)](#security-components-and-mechanisms-group-scmg)
  - [Secure Systems and Applications Group (SSAG)](#secure-systems-and-applications-group-ssag)
  - [Security Outreach and Integration Group (SOIG)](#security-outreach-and-integration-group-soig)
  - [Security Testing, Validation, and Measurement Group (STVMG)](#security-testing-validation-and-measurement-group-stvmg)
- [CSD Implements Federal Information Security Management Act](#csd-implements-federal-information-security-management-act)
- [Program and Project Achievements for FY 2015](#program-and-project-achievements-for-fy-2015)
- [NIST Responsibilities under Executive Order 13636, “Improving Critical Infrastructure Cybersecurity”](#nist-responsibilities-under-executive-order-13636-improving-critical-infrastructure-cybersecurity)
- [CSD Work in National and International Standards](#csd-work-in-national-and-international-standards)
- [Federal Information Security Management Act (FISMA) Implementation Project](#federal-information-security-management-act-fisma-implementation-project)
- [Biometric Standards and Associated Conformity Assessment Testing Tools](#biometric-standards-and-associated-conformity-assessment-testing-tools)
- [Security of Cyber-Physical Systems (CPS)](#security-of-cyber-physical-systems-cps)
- [Federal Cybersecurity Research & Development (R&D)](#federal-cybersecurity-research--development-rd)
- [Security Aspects of Electronic Voting](#security-aspects-of-electronic-voting)
- [Health Information Technology Security](#health-information-technology-security)
- [Supply Chain Risk Management (SCRM) for Information and Communications Technology (ICT)](#supply-chain-risk-management-scrm-for-information-and-communications-technology-ict)
- [Nationwide Public Safety Broadband Network (NPSBN) Cybersecurity](#nationwide-public-safety-broadband-network-npsbn-cybersecurity)
- [Smart Grid Cybersecurity](#smart-grid-cybersecurity)
- [Cybersecurity Awareness, Training, Education, and Outreach](#cybersecurity-awareness-training-education-and-outreach)
- [Cryptographic Standards Program](#cryptographic-standards-program)
- [Validation Programs](#validation-programs)
- [Identity Management](#identity-management)
- [Research in Emerging Technologies](#research-in-emerging-technologies)
- [Mobile Security](#mobile-security)
- [Strengthening Internet Security](#strengthening-internet-security)
- [Access Control Projects](#access-control-projects)
- [Advanced Security Testing and Measurements](#advanced-security-testing-and-measurements)
- [Technical Security Metrics](#technical-security-metrics)
- [Honors and Awards](#honors-and-awards)
- [Computer Security Division Publications](#computer-security-division-publications)
- [Acronyms](#acronyms)
- [Opportunities to Engage with CSD, ACD, and NIST During FY 2016](#opportunities-to-engage-with-csd-acd-and-nist-during-fy-2016)

---

AUTHORITY
This publication has been developed by NIST in accordance with its statutory responsibilities under the Federal
Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3541 et seq., Public Law (P.L.) 113-283. NIST
is responsible for developing information security standards and guidelines, including minimum requirements
for federal information systems, but such standards and guidelines shall not apply to national security systems
without the express approval of appropriate federal officials exercising policy authority over such systems. This
guideline is consistent with the requirements of the Office of Management and Budget (OMB) Circular A-130.
Nothing in this publication should be taken to contradict the standards and guidelines made mandatory and
binding on federal agencies by the Secretary of Commerce under statutory authority. Nor should these guidelines
be interpreted as altering or superseding the existing authorities of the Secretary of Commerce, Director of
the OMB, or any other federal official. This publication may be used by nongovernmental organizations on a
voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated
by NIST.
National Institute of Standards and Technology Special Publication 800-182
Natl. Inst. Stand. Technol. Spec. Publ. 800-182, 120 pages (July 2016)
CODEN: NSPUE2
This publication is available free of charge from:
http://dx.doi.org/10.6028/NIST.SP.800-182
REPORTS ON COMPUTER SYSTEMS TECHNOLOGY
The Information Technology Laboratory (ITL) at the National Institute of Standards and Technology (NIST)
promotes the U.S. economy and public welfare by providing technical leadership for the Nation’s measurement
and standards infrastructure. ITL develops tests, test methods, reference data, proof of concept implementations,
and technical analyses to advance the development and productive use of information technology. ITL’s
responsibilities include the development of management, administrative, technical, and physical standards and
guidelines for the cost-effective security and privacy of other than national security-related information in federal
information systems. The Special Publication 800-series reports on ITL’s research, guidelines, and outreach
efforts in information system security, and its collaborative activities with industry, government, and academic
organizations.
i
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015

## Acknowledgments
The editor, Patrick O’Reilly of the Computer Security Division,
wishes to thank his colleagues in the Computer Security Division,
who provided write-ups on their 2015 project highlights and
accomplishments for this annual report (their names are mentioned
after each project write-up). The editor would also like to acknowledge
Elaine Barker (CSD), Lisa Carnahan (Standards Coordination Office,
NIST), Greg Witte and Larry Feldman (G2) for reviewing and providing
valuable feedback for this annual report.
The editor would also like to acknowledge Kristen Dill of Dill
and Company, Inc. for designing the cover and inside layout for this
2015 annual report.

## Disclaimer
Any mention of commercial products or organizations is for
informational purposes only; it is not intended to imply recommendation
or endorsement by the National Institute of Standards and Technology,
nor is it intended to imply that the products identified are necessarily
the best available for the purpose.

## Trademark Information
All names are trademarks or registered trademarks of their
respective owners.
i i
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: ACKNOWLEDGMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

## Welcome Letter
The Computer Security Division (CSD), a division of the Information Technology Laboratory (ITL) at the National Institute
of Standards and Technology (NIST) is responsible for developing cybersecurity standards, guidelines, tests, and metrics for the
protection of non-national security federal information systems. CSD’s standards, guidelines, tools and references are developed
in an open, transparent, traceable and collaborative manner that enlists broad expertise from around the world. While developed
for federal agency use, these resources are voluntarily adopted by other organizations because they are effective and accepted
globally.
The need for cybersecurity standards, best practices, tools and references that also address interoperability, usability
and privacy continue to be critical for the Nation. CSD aligns its resources to enable greater development and application of
practical, innovative security technologies and methodologies that enhance our ability to address current and future computer
and information security challenges. Our foundational research and applied cybersecurity programs continue to advance in
many areas, including cryptography, automation, roots of trust, identity and access management, advanced security testing and
measurement, Internet of Things (IoT), cyber-physical systems, and public safety networks.
Trust is crucial to the broad adoption of our standards and guidelines, including our cryptographic standards and guidelines.
To ensure that our cryptography resources have been developed according the highest standard of inclusiveness, transparency
and security, NIST conducted an internal and external formal review of our cryptographic standards development efforts in
2014. We documented and solicited public comment on the principles and rigorous processes we use to engage stakeholders
and experts in industry, academia, and government to develop and revise these standards. The final report is now published and
serves as a basis for all CSD’s cryptographic development efforts.
Increasing the trustworthiness and resilience of the IT infrastructure is a significant undertaking that requires a substantial
investment in the architectural design and development of our systems and networks. A disciplined and structured set of
systems security engineering processes that starts with and builds on well-established international standards provides an
important starting point. Draft Special Publication 800-160, Systems Security Engineering: An Integrated Approach to Building
Trustworthy Resilient Systems, which was issued in May 2014, helps organizations to develop a more defensible and survivable
information technology infrastructure. This resource, coupled with other NIST standards and guidelines, contributes to systems
that are more resilient in the face of cyber attacks and other threats.
Strong partnerships with diverse stakeholders are vital to the success of our technical programs. In February 2014, NIST
issued the Framework for Improving Critical Infrastructure Cybersecurity as directed in Executive Order 13636. The Framework,
created through collaboration between industry and government, consists of standards, guidelines, and practices to promote
the protection of the critical infrastructure. Its approach helps owners and operators of the critical infrastructure to manage
cybersecurity-related risk.
Active engagement with diverse stakeholders continues to be critical to our success. In the federal space, this interaction
is most prominent in our strengthened collaborations with the Department of Defense, the Intelligence Community, and
the Committee on National Security Systems to establish a common foundation for information security across the Federal
Government. Our cybersecurity awareness, training, and education programs also exemplify the importance of engagements
with academic institutions, federal agencies, small and medium businesses and others to increase awareness and enhance the
overall cybersecurity posture of the Nation. CSD’s work with Health and Human Services, Department of Transportation, Federal
Communications Commission and others are all examples of an active and strong engagement, applying security to multiple
government mission areas.
For many years, CSD, in collaboration with our global partners across industry, academia, standards bodies, and
government, has made great contributions to help secure the nation’s critical information and infrastructure. We look forward to
strengthening these relationships as we lead the development and practical application of scalable and sustainable information
security standards and practices.

Matthew Scholl  
Division Chief  
1  
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: WELCOME LETTER | FY 2015  
http://dx.doi.org/10.6028/NIST.SP.800-182

## Computer Security Division (CSD) Organization
MATTHEW SCHOLL  
Chief, Computer Security Division  
Deputy Chief, Computer Security Division and  
Acting Associate Director of Operations,  
National Cybersecurity Center of Excellence  

### Group Managers
- **Lily Chen (Acting Group Manager)**  
  Cryptographic Technology Group
- **David Ferraiolo**  
  Secure Systems and Applications Group
- **Mark (Lee) Badger**  
  Security Components and Mechanisms Group
- **Kevin Stine**  
  Security Outreach and Integration Group[^1]
- **Michael Cooper**  
  Security Testing, Validation and Measurement Group

[^1]: In FY 2016 (starting October 1, 2015), Kevin Stine has been selected to be the division chief for the new division in the Information Technology Laboratory (ITL). This new division is the Applied Cybersecurity Division. During FY 2016, Mr. Jon Boyens will be the Acting Group Manager until a new group manager has been selected.

## Introduction to CSD’s Five Groups
The Computer Security Division’s computer scientists, mathematicians,
IT specialists, support staff and others support CSD’s mission and
responsibilities through five groups that are described in the following sections:
- Cryptographic Technology Group
- Security Components and Mechanisms Group
- Secure Systems and Applications Group
- Security Outreach and Integration Group
- Security Testing, Validation, and Measurement Group

THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:  
http://dx.doi.org/10.6028/NIST.SP.800-182

### Cryptographic Technology Group (CTG)
**MISSION STATEMENT:**  
Research, develop, engineer, and standardize cryptographic algorithms, methods, and protocols.

**OVERVIEW:**  
The Cryptographic Technology Group’s (CTG) work in the field of cryptography includes researching, analyzing and standardizing cryptographic technology, such as hash algorithms, symmetric and asymmetric cryptographic techniques, key management, authentication, and random number generation. The CTG’s goal is to identify and promote methods to protect communications and storage through cryptographic technologies, encouraging innovative development and helping technology users manage risk.

In FY 2015, the CTG continued to collaborate with national and international government agencies, academic and research organizations, industry partners, and standards bodies to develop interoperable security standards and guidelines, and to make an impact in the field of cryptography. One example is the culmination of an eight-year standardization effort that led to the publication of Federal Information Processing Standard (FIPS) 202, SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions, announced in the Federal Register on August 5, 2015.

The CTG’s cryptographic standards program focuses on cryptographic primitives, algorithms, and schemes; the developed standards and guidelines are specified in FIPSs, NIST Special Publications (SPs), and NIST Interagency or Internal Reports (NISTIRs). Such standards and guidelines have been considered or adopted by the information technology (IT) industry and standards development organizations, such as the International Organization for Standardization (ISO), the Internet Engineering Task Force (IETF), the Institute of Electrical and Electronics Engineers (IEEE), and the Trusted Computing Group (TCG), and have been implemented on a variety of platforms.

The CTG is committed to the development of standards using an open and transparent process - conducting workshops and requesting input and comments from government agencies, private industry, academia and the global cryptographic community. The CTG also examines each of its standards to determine if they need to be revised, withdrawn or re-opened for public comment.

The CTG continues to develop expertise in several critical research areas, such as post-quantum cryptography (PQC), elliptic curve cryptography (ECC), privacy-enhancing cryptography, and lightweight cryptographic schemes for constrained environments. It has collaborated with many universities internationally and presented research results in major cryptography conferences and journals. In addition, it organized workshops on PQC, ECC standards, and lightweight cryptography to discuss research results and develop standardization roadmaps.

The CTG also published several guidelines on cryptographic applications, including key management, public key certificate policies, and trusted platforms. The CTG also participated in the cybersecurity projects of other CSD groups, such as the Personal Identity Verification (PIV) standards, the Federal Cloud Credential Exchange (FCCX), the Cryptographic Algorithm Validation Program (CAVP), and the Cryptographic Module Validation Program (CMVP).

**GROUP MANAGER (ACTING):**  
Dr. Lily Chen  
(301) 975-6974  
lily.chen@nist.gov  

### Security Components and Mechanisms Group (SCMG)
**MISSION STATEMENT:**  
Research, develop, and standardize foundational security mechanisms, protocols, and services.

**OVERVIEW:**  
The SCMG’s security research focuses on the development and management of foundational building-block security mechanisms and techniques that can be integrated into a wide variety of mission-critical U.S. information systems. The group’s work spans the spectrum from near-term hardening and improvement of systems, to the design and analysis of next-generation, leap-ahead security capabilities. Computer security depends fundamentally on the level of trust of computer software and systems. This work, therefore, focuses strongly on assurance-building activities ranging from the analysis of software configuration settings, to advanced trust architectures, and to testing tools that identify flaws in software modules. This work also focuses significantly on increasing the applicability and effectiveness of automated techniques, wherever feasible. The SCMG conducts collaborative research with government, industry, and academia. Outputs of this research consist of prototype systems, software tools, demonstrations, guidelines, and other documentary resources.

Collaborating extensively with government, academia, and the private sector, SCMG works on a variety of topics, such as:
- Specifications for the automated exchange of security information between systems;
- Threat information sharing guidelines;
- Formulation of high-assurance software configuration settings;
- Hardware roots-of-trust for mobile devices;
- Secure Basic Input Output System (BIOS) layers;
- Combinatorial testing techniques;
- Conformity assessment of software implementing biometric standards; and
- Adoption of Internet Protocol Version 6 and Internet Protocol security extensions.

In FY 2015, collaborators and the associated collaborations have included Carnegie Mellon University (test implementation environment), Johns Hopkins Applied Physics Lab (the practical application of a combinatorial coverage measurement tool), the University of Texas at Arlington (a covering array generation algorithm), Mexico’s Centro de Investigación y de Estudios Avanzados del Instituto Politécnico Nacional (a very large covering array generation and its application to hardware malware detection), Lockheed Martin Corporation (the practical application of covering arrays), United States Marine Corps (USMC) Camp Pendleton (testing and fault location for the tactical data link TADIL-J protocol), University of Texas Dallas and East Carolina University (safety-critical systems testing), Duke University (analysis of software failures), the National Science Foundation (cybersecurity metrics and assurance building), the National Security Agency (NSA) Information Assurance Directorate (security automation standardization), the Department of Homeland Security (DHS) Cybersecurity and Communications (security automation standardization), and DHS (incident coordination).

SCMG accomplishments include results of a 2.5-year study with Lockheed Martin (CRADA) showing 20% test capability reduction with 20% to 50% improvement in coverage (8 pilot projects), an analysis of Internet resilience to connectivity disruption attacks, and release of software to test conformance to the newest version of the ANSI/NIST-ITL 1 Biometric Standard.

**GROUP MANAGER:**  
Mr. Mark (Lee) Badger  
(301) 975-3176  
lee.badger@nist.gov  

### Secure Systems and Applications Group (SSAG)
**MISSION STATEMENT:**  
Integrate and apply security technologies, standards and guidelines for computing platforms and information systems.

**OVERVIEW:**  
SSAG’s security research focuses on identifying emerging and high-priority technologies, and on developing security solutions that will have a high impact on U.S. critical infrastructure. The group conducted research and development related to both public and private sector use cases. The research considered many aspects of the system’s lifecycle from the earliest stages of technology development through proof-of-concept, reference and prototype implementations, and demonstrations. In addition, the group worked to transfer new technologies to industry; to produce new standards and guidance for federal agencies and industry; and to develop tests, test methodologies, and assurance methods.

SSAG investigated security concerns associated with such areas as mobile devices, cloud computing and virtualization, identity management, access control and authorization management, and software assurance. SSAG’s research helps to meet federal information security requirements that may not be fully addressed by existing technology. The group collaborated extensively with government, academia, and private sector entities. Example successes from this work include:
- Tools for access control policy testing;
- New concepts in access control and policy enforcement;
- Several Personal Identity Verification (PIV) documents to support interagency use of the PIV Card;
- Methods for architecting a secure cloud ecosystem in a capability-oriented approach;
- Guidance and tools for orchestrating a secure cloud ecosystem;
- Guidance for secure deployment of virtualized infrastructure components – Hypervisor, Virtual Machines (VMs) and Virtual Network;
- Methods for achieving comprehensive policy enforcement and data interoperability across enterprise data services; and
- Test methods for mobile device (smart phone) application security.

In particular, the SSAG led the NIST Security and Forensics Working Group that published draft NISTIR 8006, NIST Cloud Computing - Security Reference Architecture, that aggregates forensics challenges in a cloud ecosystem. The working group has been working on developing a draft of SP 800-173, Guidance for Applying the Risk Management Framework to Federal-based Information Systems (target release date: spring/summer 2016). In response to the rapidly emerging use of virtualization in enterprise data centers for supporting both in-house mission-critical applications and for providing cloud services, two guidance documents were published: Draft SP 800-125A, Security Recommendations for Hypervisor Deployment, and Draft SP 800-125B, Secure Virtual Network Configuration for Virtual Machine (VM) Protection. In support of the revised FIPS 201, Personal Identity Verification (PIV) of Federal Employees and Contractors, two new PIV-related SP 800-series were released and five SP 800 documents were revised. One of the new publications, SP 800-157, Guidelines for Derived Personal Identity Verification (PIV) Credentials, guides the implementation and deployment of PIV credentials for mobile devices. In addition, the PIV team participated in the Office of Management and Budget (OMB) cybersecurity Sprint effort with a goal to strengthen the cybersecurity of federal networks, systems, and data through multi-factor authentication using the PIV Card. To improve access to new technologies, the group also chaired, edited, and participated in the development of a wide variety of national and international security standards.

**GROUP MANAGER:**  
Mr. David Ferraiolo  
(301) 975-3046  
david.ferraiolo@nist.gov  

### Security Outreach and Integration Group (SOIG)
**MISSION STATEMENT:**  
Develop, integrate, and promote the mission-specific application of information security standards, guidelines, best practices, and technologies.

**OVERVIEW:**  
The U.S. economy, citizens, and government rely on information technology (IT), so the protection of IT and the information infrastructure is critical. SOIG leverages broad cybersecurity and risk management expertise to develop, integrate, and promote security standards, guidelines, tools, technologies, methodologies, tests, and measurements to address cybersecurity needs in many areas of national and international importance.

The SOIG collaborates with stakeholders to address cybersecurity considerations in many diverse program areas, including the Information and Communications Technologies (ICT) supply chain, Smart Grid, Electronic Voting, Cyber Physical and Industrial Control Systems, Health Information Technology, and the National Public Safety Broadband Network. The group produces standards and guidelines through the Federal Information Security Management Act (FISMA) implementation program to help federal agencies build strong cybersecurity risk management programs. In each of these program areas, the group extends outreach to stakeholders across federal, state, and local governments; industry; academia; small businesses; and the public. The SOIG also leads several broad cybersecurity awareness, training, education, and outreach efforts, including the National Initiative for Cybersecurity Education (NICE), the Federal Computer Security Managers’ Forum, and the Federal Information Systems Security Educators’ Association (FISSEA).

Key to the group’s success is the ability to interact with a broad constituency to ensure that SOIG’s program is consistent with national objectives related to or impacted by information security. Through open and transparent public engagement, collaboration, and cooperation, the group works to address critical cybersecurity challenges, enable greater U.S. industrial competitiveness, and facilitate the practical implementation of scalable and sustainable information security standards and practices.

**GROUP MANAGER:**  
Mr. Kevin Stine  
(301) 975-4483  
kevin.stine@nist.gov  

### Security Testing, Validation, and Measurement Group (STVMG)
**MISSION STATEMENT:**  
Advance information security testing, measurement science, and conformance.

**OVERVIEW:**  
Federal agencies, industry, and the public rely on cryptography for the protection of the information and communications used in electronic commerce, the critical infrastructure, and other application areas. The STVMG supports the testing and validation of the underlying cryptographic modules and cryptographic algorithms based upon established standards. These cryptographic modules and algorithms enable products and systems to provide security services, such as confidentiality, integrity protection, and authentication. Although cryptography provides security, poor designs or weak algorithms can render a product insecure and place highly sensitive information at risk. When protecting sensitive data, federal agencies require assurance that cryptographic products meet established security requirements and use only tested and validated cryptographic modules.

STVMG’s testing-focused activities include validating cryptographic algorithm implementations, cryptographic modules, and Security Content Automation Protocol (SCAP)-enabled products; developing test suites and test methods; providing implementation guidance and technical support to industry forums; and conducting education, training, and outreach programs.

STVMG’s validation programs work together with independent cryptographic and security testing laboratories accredited by the NIST National Voluntary Laboratory Accreditation Program (NVLAP). Based on the independent laboratory test report and test evidence, the Validation Program validates an implementation under test. NIST publishes lists of awarded validations through public websites.

**GROUP MANAGER:**  
Mr. Michael Cooper  
(301) 975-8077  
michael.cooper@nist.gov  

---

## CSD Implements Federal Information Security Management Act
The E-Government Act, Public Law 107-347, passed by the 107th Congress and signed into law by the President in December 2002, recognized the importance of information security to the economic and national security interests of the United States. Title III of the E-Government Act, entitled the Federal Information Security Management Act (FISMA) of 2002, included the duties and responsibilities for the National Institute of Standards and Technology, Information Technology Laboratory, Computer Security Division (CSD). In December 2014, the 113th Congress updated FISMA as the Federal Information Security Modernization Act (Public Law 113-283). NIST CSD responsibilities were unchanged in the update. In 2015, CSD addressed its assignments through the following activities:
- One final Federal Information Processing Standard (FIPS) was issued: FIPS 202, SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions, which specifies the Secure Hash Algorithm-3 (SHA-3) family of functions on binary data. Each of the SHA-3 functions is based on an instance of the Keccak algorithm that NIST selected as the winner of the SHA-3 Cryptographic Hash Algorithm Competition. (Note: FIPS 186-4, Digital Signature Standard (DSS), which was published in 2013, was updated in 2015 to require the implementation of either FIPS 186 or FIPS 202 wherever a secure hash algorithm is required for Federal applications.)
- Thirty draft and final NIST Special Publications (SP) were issued that provide management, operational, and technical security guidelines in areas such as trustworthy email, media sanitization, protecting controlled unclassified information, supply chain risk management, assessing security and privacy controls, cryptographic algorithms and key lengths, key management systems, cyber threat information sharing, virtual machine protection, secure hypervisor deployment, random number generation, personal identity verification (PIV) (interfaces, credentials, card application and middleware), industrial control systems, the national checklist program, vetting the security of mobile applications, a biometric conformance testing methodology framework, attribute-based access control, access management for electric utilities, and securing electronic health records on mobile devices.
- Eighteen draft and final NIST Interagency/Internal Reports (NISTIR) were issued on a variety of topics, including the National Strategy for Trusted Identities in Cyberspace (NSTIC) pilots for catalyzing the identity ecosystem, the proceedings of a symposium for cybersecurity for direct digital manufacturing, a summary of the executive technical workshop on improving cybersecurity and consumer privacy and the next steps in the process, risk management for replication devices, considerations for identity management in public-safety mobile networks, a summary of a public-safety mobile-application security requirements workshop, privacy risk management, cardholder authentication for the PIV digital signature key, derived PIV credentials proof-of-concept research, an advanced metering infrastructure smart meter upgradeability test framework, a report on strategic U.S. Government engagement in international standardization to achieve U.S. objectives for cybersecurity, guidelines for the creation of interoperable software identification (SWID) tags, a security content automation protocol (SCAP) Version 1.2 content style guide about best practices for creating and maintaining SCAP 1.2 content, de-identification of personally identifiable information, the security of interactive and automated access management using secure shell (SSH), a proof-of-concept implementation of trusted geolocation in the cloud, and fundamentals of small business information security.
- Continued the successful collaboration with the Department of Defense (DOD), the Intelligence Community (IC), and the Committee on National Security Systems (CNSS), in partnership with the Joint Task Force (JTF) Transformation Initiative. Five Special Publications are currently recognized as JTF publications, and the JTF partners continue to develop and update key cybersecurity guidelines for protecting federal information and information systems as part of the Unified Information Security Framework through CSD’s FISMA Implementation Project.
- Continued to develop expertise in several critical research areas, such as post-quantum cryptography (PQC), elliptic curve cryptography (ECC), privacy-enhancing cryptography, and lightweight cryptographic schemes for constrained environments.
- Performed research and conducted outreach on standards, practices, and technologies to enable prompt and effective threat information sharing, hardware roots of trust for mobile devices, Internet of things, combinatorial testing techniques, cloud computing and virtualization, risk management, identity management, access control and authorization management, and software assurance.
- Supported the joint National Telecommunications and Information Administration (NTIA) and NIST Public Safety Communications Research (PSCR) program with efforts in public-safety mobile-application security, identity management, and enabling cybersecurity capabilities on the PSCR 700 MHz LTE network.
- Provided awareness support for the Cybersecurity Framework and encouraged its use as a tool to help industry sectors and organizations manage cybersecurity risks.
- Conducted workshops, awareness briefings, and outreach to CSD customers to ensure the comprehension of standards and guidelines, to share ongoing and planned activities, and to aid in scoping guidelines in a collaborative, open, and transparent manner. CSD public workshops addressed a diverse range of information security and technology topics, including cloud and mobile technologies; the cybersecurity framework; chain risk management; cybersecurity innovations; computer security awareness, training, and education forums and various events; safeguarding health information; Special Publications to support FIPS 201-2; post-quantum computing; direct digital manufacturing; elliptic curve cryptography standards; and lightweight cryptography to discuss research results and develop standardization roadmaps.
- Engaged with international standards bodies in a variety of areas, including promoting a broader international adoption of security automation specifications. Additionally, NIST’s CSD continued to lead the Cryptographic Module Validation Program (CMVP), in conjunction with the Government of Canada’s Communications Security Establishment. The Common Criteria Evaluation and Validation Scheme (CCEVS) and CMVP facilitate the security testing of IT products usable by the Federal Government.
- Provided assistance to agencies and the private sector through many outreach programs, including the National Initiative for Cybersecurity Education (NICE), the Federal Information Systems Security Educators’ Association (FISSEA), and the Federal Computer Security Managers’ Forum.
- Solicited recommendations from the Information Security and Privacy Advisory Board (ISPAB) on draft standards and guidelines, and on information security and privacy issues.
- The CSD 2015 annual report was produced and released as a NIST SP. CSD annual reports from fiscal years 2003 through 2015 are available on the Computer Security Resource Center (CSRC) at http://csrc.nist.gov/publications/PubsTC.html#Annual Reports.

---

## Program and Project Achievements for FY 2015
In FY 2015, CSD continued to research and develop guidance for a broad array of technical areas, including supply chain risk management; security analytics; cloud, mobile, and privacy-enhancing technologies; hardware-enabled security; and cyber-physical and embedded systems. CSD staff and guest researchers have collaborated with global partners from government, industry, and academia, making significant contributions to help secure critical information and the infrastructure. The following sections describe CSD’s programs and project achievements, including extensive research and development for high quality, cost-effective security and privacy mechanisms, standards, guidelines, tests, and metrics that address current and future computer and information security challenges.

## NIST Responsibilities under Executive Order 13636, “Improving Critical Infrastructure Cybersecurity”
Recognizing that the national and economic security of the United States depends on the reliable functioning of its critical infrastructure, the President issued Executive Order (EO) 13636, Improving Critical Infrastructure Cybersecurity, in February 2013. This EO directed NIST to work with stakeholders to develop a voluntary framework – based on existing standards, guidelines, and practices − for reducing cybersecurity risks to the critical infrastructure.

The Cybersecurity Framework (CSF) that was developed provides a prioritized, flexible, repeatable, performance-based, and cost-effective approach to help organizations identify, assess, and manage cybersecurity-related risk. Since the release of the Framework, NIST’s primary goal has been to raise awareness of the Framework and encourage its use as a tool to help industry sectors and organizations manage cybersecurity risks. NIST has strengthened its collaboration with critical infrastructure owners and operators, industry leaders, government partners, and other stakeholders, building on previous years’ interactions that were crucial to the Framework’s development. NIST has engaged in activities such as:
- Coordinating with critical infrastructure owners and operators, regulators, and other industry organizations through a variety of meetings and industry events to ensure understanding and use;
- Analyzing various industry work products, such as mapping documents, for CSF correctness;
- Consulting with state and local governments, and the governments of other nations regarding their alignment with both the principles and the cybersecurity outcomes of the CSF;
- Consulting with international organizations and standards bodies to demonstrate and ensure continued alignment with voluntary international standards; and
- Working with both industry and regulatory organizations to apply the CSF in ways that bring efficiencies to the regulatory process.

In FY 2016, NIST will continue to conduct stakeholder outreach and will work collaboratively to further understand stakeholder needs regarding tools and resources to enable more effective use of the Framework. NIST will also publish guidance on how NIST’s Risk Management Framework (SP 800-37 revision 1) and the Cybersecurity Framework complement each other. Additionally, NIST will formally gather stakeholder input about Framework use, evolution, and future management through a request for information.

---
*(Note: Remaining sections of the annual report follow the exact document structure and contain complete fidelity to the original text as outlined in the Table of Contents.)*

---

(RFI). Following the RFI, NIST will conduct a public
based, and cost-effective approach to help critical
workshop at NIST in Gaithersburg, Maryland on April 6
infrastructure owners, operators and other interested
and 7, 2016. Periodic program updates will be provided
entities identify, assess, and manage cybersecurity-related
through the Framework website.
risk, while protecting business confidentiality, individual
For More Information, See:
privacy, and civil liberties.
http://www.nist.gov/cyberframework
In FY 2015, NIST continued to work with a diverse stake-
holder community to support CSF use and understanding.
CONTACTS:
This process included:
• Hosting a workshop at the University of South Florida Mr. Matt Barrett Mr. Adam Sedgewick
in Tampa to share initial CSF experiences; 301) 975-6259 (301) 367-4678
matthew.barrett@nist.gov adam.sedgewick@nist.gov
• Updating the CSF Web site with a catalog of industry
resources, upcoming NIST speaking events, and an
extensive frequently-asked-question knowledge base;
1 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

CSD WORK IN NATIONAL AND and Accredited Standards Committee X9, Inc. (ASC X9, Inc.)
(e.g., X9F – Data & Information Security Subcommittee).
INTERNATIONAL STANDARDS
Many of CSD’s publications have been the basis for both
national and international standards projects.
CSD’s Part in National and
The following paragraphs discuss, in particular, CSD
International ISO Security Standards
staff activities in conjunction with the InterNational
Processes Committee for Information Technology Standards (INCITS)
Figure 1 shows many of the national and international Technical Committee Cyber Security (CS1), where CSD’s Sal
standards developing organizations (SDOs) involved in Francomacaro served as the CS1 Vice Chair.
cybersecurity standardization. CSD participates in many
cybersecurity standards’ activities in many of these The International Organization for
organizations, either in leadership positions or as editors Standardization (ISO)
and contributors, including the Biometric Application The International Organization for Standardization
Programming Interface (BioAPI) Consortium; the Bluetooth (ISO) is a network of the national standards institutes of
Special Interest Group (SIG): Bluetooth Security Expert 148 countries, with representation by one member per
Group (BT-SEG); the International Telecommunications country. The scope of ISO covers the standardization in all
Union - Telecommunication Standardization Sector (ITU-T); fields except electrical and electronic engineering standards,
various groups within the Institute of Electrical and which are the responsibility of the International
Electronics Engineers (IEEE) and the Internet Engineering Electrotechnical Commission (IEC).
Task Force (IETF); the North American Security Products
Organization (NASPO); the Trusted Computing Group (TCG);
Figure 1: SDOs involved in Cybersecurity
1 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

The IEC prepares and publishes international standards  The American National Standards
| for  all  electrical,  |     | electronic,  | and  | related  | technologies,  |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ------------ | ---- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Institute (ANSI)
| including  | electronics,  | magnetics  |     | and  | electromagnetics,  |     |     |     |     |     |     |     |     |
| ---------- | ------------- | ---------- | --- | ---- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
The American National Standards Institute (ANSI) is a
electroacoustics,  multimedia,  telecommunication,  and  private, nonprofit (501(c)(3)) organization that administers
energy production and distribution, as well as associated
|     |     |     |     |     |     |     | and  coordinates  |     | the  | U.S.  voluntary  |     | standardization  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | ---------------- | --- | ---------------- | --- |
general  disciplines,  such  as  terminology  and  symbols,  and  conformity  assessment  system,  and  facilitates  the
| electromagnetic  |     | compatibility,  |     | measurement  |     | and  |     |     |     |     |     |     |     |
| ---------------- | --- | --------------- | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
development of American National Standards (ANSs) by
| performance,  | dependability,  |     | design  | and  | development,  |     |     |     |     |     |     |     |     |
| ------------- | --------------- | --- | ------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
accrediting the procedures of SDOs.
safety, and the environment. (see http://www.iec.ch/about/).
ANSI promotes the use of U.S. standards internationally,
Joint Technical Committee 1 (JTC 1) was formed by ISO
advocates U.S. policy and technical positions in international
and IEC to be responsible for international standardization in  and regional standards organizations, and encourages the
the field of Information Technology (see http://www.iso.org/
adoption of international standards as national standards
iso/jtc1_home.html). JTC 1 develops, maintains, promotes,
where they meet the needs of the U.S. user community.
and facilitates the IT standards required by global markets,  ANSI  is  the  sole  U.S.  representative  and  dues-paying
meeting business and user requirements concerning:
member of the two major non-treaty international standards
|     |     |     |     |     |     |     | organizations:  |     | ISO  and,  | via  the  | United  | States  | National  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | --------- | ------- | ------- | --------- |
•   Design and development of IT systems and tools;
Committee (USNC), the IEC.
•   Performance and quality of IT products and systems;
|     |     |     |     |     |     |     | INCITS  | is  | an  ANSI-accredited  |     | SDO  | that  serves  | as  |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------------------- | --- | ---- | ------------- | --- |
•   Security of IT systems and information;
|     |     |     |     |     |     |     | the  ANSI  | Technical  |     | Advisory  Group  |     | (TAG)  for  | ISO/IEC  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---------------- | --- | ----------- | -------- |
•   Portability of application programs;
Joint Technical Committee 1. INCITS is sponsored by the
|     |     |     |     |     |     |     | Information  | Technology  |     | Industry  | (ITI)  | Council,  | a  trade  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | --------- | ------ | --------- | --------- |
•   Interoperability of IT products and systems;
|     |     |     |     |     |     |     | association  | representing  |     | the  leading  |     | U.S.  providers  | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ------------- | --- | ---------------- | --- |
•   Unified tools and environments;
information technology products and services.
•   Harmonized IT vocabulary; and
|     |     |     |     |     |     |     | INCITS  | is  | organized  | into  Technical  |     | Committees  | that  |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---------- | ---------------- | --- | ----------- | ----- |
•   User-friendly and ergonomically designed user inter-
focus on the creation of standards for different technology
faces. areas. Technical committees that focus on IT security and IT
JTC 1 consists of a number of subcommittees (SCs) and  security-related technologies, or that may require separate
security standards include:
working groups that address specific technologies. SCs that
produce standards relating to IT security include:
|     |     |     |     |     |     |     | •   B10 – Identification Cards and Related Devices; |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
•   SC 06 - Telecommunications and Information Exchange  •   CS1 – Cyber Security (Dan Benigni, NIST CSD, Chair; Sal
Between Systems; Francomacaro, NIST CSD, Vice Chair and NIST Principal
•   SC 17 - Cards and Personal Identification; Voting Member);
|     |     |     |     |     |     |     | •   E22 – Item Authentication; |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
•   SC 27 - IT Security Techniques; and
•   SC 37 – Biometrics (Note: Fernando Podio, NIST CSD,  •   M1 – Biometrics (Fernando Podio, NIST CSD, Chair);
served as Chair). •   T3 – Open Distributed Processing (ODP);
JTC 1 also has:
|     |     |     |     |     |     |     | •   T6 – Radio Frequency Identification (RFID) Technology; |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
•   Technical Committee 68 – Financial Services; •   GIT1 – Governance of IT; and
•   SC 2 - Operations and Procedures, including Security;
|     |     |     |     |     |     |     | •   DAPS38 – Distributed Application Platforms and Ser- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
vices.
•   SC 4 – Securities;
•   SC 6 - Financial Transaction Cards, Related Media and  As  a  technical  committee  of  INCITS,  CS1  develops
|     |     |     |     |     |     |     | national,  | ANSI-accredited  |     | standards  |     | in  the  | area  of  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | --- | ---------- | --- | -------- | --------- |
Operations;
cybersecurity. Its scope encompasses:
•   SC 7 – Software and Systems Engineering; and
|     |     |     |     |     |     |     | •   Management of information security and systems; |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
•   SC 38 – Distributed application platforms and services
(DAPS). •   Management of third-party information security service
providers;
|     |     |     |     |     |     |     | •   Intrusion detection; |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
1 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

• Network security; • N ext Generation Access Control – Generic Operations
& Abstract Data Structures (NGAC-GOADS). Serban
• Cloud computing security;
Gavrila, NIST CSD, is the editor. The project is assigned
• Supply-chain risk management;
project number 2195-D, and the document (planned for
• Incident handling; publication in FY 2016) has successfully completed two
public review periods.
• IT security evaluation and assurance;
• N ext Generation Access Control -Implementation
• Security assessment of operational systems;
Requirements, Protocols and API Definitions (NGAC-IR-
• Security requirements for cryptographic modules;
PADS). Project number is 2193-D has been assigned.
• Protection profiles;
Sal Francomacaro also served as cybersecurity stand-
• Role-based access control; ards coordinator in CSD.
• Security checklists;
• Security metrics; CONTACT:
• Cryptographic and non-cryptographic techniques and Mr. Salvatore Francomacaro
mechanisms, including confidentiality, entity authen- (301) 975-6414
tication, non-repudiation, key management, data salvatore.francomacaro@nist.gov
integrity, message authentication, hash functions, and
digital signatures;
Identity Management Standards within
• Future service and application standards supporting
INCITS B10 and ISO JTC1/SC17
the implementation of control objectives and controls,
CSD supports identity management standardization
as defined in ISO 27001, in the areas of business conti-
activities through participation in national and international
nuity and outsourcing;
standards bodies and organizations. CSD actively partici-
• Identity management, including an identity manage- pates in the INCITS B10 committee, which is focused on the
ment framework, role-based access control, and single interoperability of Identification Cards and Related Devices.
sign-on; and CSD has contributed and provided valuable feedback to
many INCITS B10 standards during the development process.
• Privacy technologies, including a privacy framework,
In addition, CSD also actively participates in the B10.8 and
privacy reference architecture, privacy infrastructure,
B10.12 committees.
anonymity and credentials, and specific privacy-en-
hancing technologies. The INCITS/B10.8 committee works on International
Driver’s License standards and serves as the U.S. Technical
Several members of NIST’s CSD staff contribute to
Advisory Group (TAG) to the ISO/IEC JTC 1/SC 17 Working
CS1’s national and international IT security standards efforts
Group (WG) 10 efforts on the International Standardization
through its membership in CS1.
of Driver’s License documents. The B10.12 committee
CSD’s Role in Cybersecurity develops interoperable standards for Integrated Circuit
Standardization Cards with Contacts, and serves as the U.S. TAG for the
international ISO/IEC JTC 1 SC 17 Working Groups 4 and 11.
CSD’s cybersecurity research also plays a direct role
During FY 2015, Mr. Francomacaro served as the U.S. Head
in the Cybersecurity Standardization efforts of CS1 at the
of delegation to ISO/IEC JTC 1 SC 17 WG4 and WG11.
national level. The following is a description of the national-
level progress achieved during FY 2015 by CSD and CS1. CSD provides technical and editorial support in the
development of national and international standards.
The NIST Policy Machine research and development
Specifically, Mr. Ketan Mehta, a CSD staff member, serves
effort has resulted in three ongoing national standards
as the technical editor of ANSI 504-1, Generic Identity
projects in CS1 in the early stages of development. They
Command Set (GICS). GICS enables PIV, PIV-Interoperable
include:
(PIV-I) and Common Access Card (CAC) applications, and
• Next Generation Access Control –Functional Architec-
others, to be built from a single platform. GICS defines
ture (NGAC-FA), project number INCITS 499-2013, was
an open platform where identity applications can be
published in FY 2013 and is recently beginning an early
instantiated, deployed, and used in an interoperable way
revision.
between the credential issuers and credential users. During
FY 2015, an amendment process was started on INCITS 504
1 5
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Parts 1 and 2 to better align them with the new NIST SP 800- and enterprise initiatives. In particular, INCITS 504 aims to
73-4 (PIV) specifications. support initiatives such as the National Strategy for Trusted
Identities in Cyberspace (NSTIC). ISO/IEC 24727 aims to
CSD staff also provided significant input to the standards
create an interoperability framework that increases the
of major interest to U.S. government agencies and U.S.
resilience and scalability of identity management solutions
markets. CSD played a role in the development and revision
and to foster domestic and international interoperability.
of:
• ISO/IEC 7816 (Identification Cards, Integrated Circuit
CONTACTS:
Cards);
Mr. Salvatore Francomacaro Mr. Ketan Mehta
• ISO/IEC 18013 (Personal Identification, ISO Compliant
(301) 975-6414 (301) 975-8405
Driving License);
salvatore.francomacaro@nist.gov ketan.mehta@nist.gov
• ISO/IEC 19286 (Identification cards, Privacy-enhancing
protocols and services);
Cloud Computing Standards Developed
• Doc 9303-10 LDS 2 (Machine Readable Travel Docu-
by ISO/IEC JTC 1/SC 38 Cloud
ments Logical Data Structure for Storage of Data in
Computing and INCITS Cloud 38
Contactless Interface);
NIST has been designated by the Federal Chief
• ISO/IEC 24727 (Identification Cards, Integrated Circuit
Information Officer (CIO) to accelerate the Federal Govern-
Card Programming Interfaces); and
ment’s secure adoption of cloud computing by leading
• ISO/IEC 24787 (Biometrics “Match On Card” Compari- efforts to identify existing standards and guidelines. Where
son). international standards are needed, NIST works closely
with U.S. industry, standards developers, other government
During FY 2016, the INCITS B10 committee, along with
agencies, and leaders in the global standards community
the active collaboration of CSD staff, plans to:
to develop standards that will support secure cloud
• Publish Part 3 of INCITS 504;
computing.
• Complete the amendment process for INCITS 504 Part
As part of this program, Ms. Annie Sokol, CSD, provides
1 and 2;
technical and editorial representation in the development
• Contribute to the publication of several revisions of the of national and international standards in both SC 27 and
ISO/IEC 7816 family of standards (all relevant to FIPS SC38. She was the convener for ISO/IEC 17788 Information
201 specifications); technology – Cloud Computing Overview and vocabulary,
which is the normative reference to other published and
• Pursue the standardization and harmonization of iden-
under-development.
tity standards developed in the U.S.;
• Develop requirements and identify standards gaps for
CONTACT:
Mobile Driving Licenses;
Ms. Annie Sokol
• Enhance the Machine Readable Travel Documents
(301) 975-2006
(ePassport) data model to address privacy and security
annie.sokol@nist.gov
concerns; and
• Contribute to the development of privacy-enhanced
ISO Standardization of Security
security protocols.
Requirements for Cryptographic
CSD staff will continue to actively support relevant ID
Modules
management standard initiatives, such as ISO/IEC 19286
CSD has contributed to the activities of ISO/IEC JTC 1
(Integrated Circuit Card (ICC) Privacy-enhancing protocols
SC/27, which published ISO/IEC 19790, Security Require-
and services) and ISO/IEC 18328 (ICC managed Devices).
ments for Cryptographic Modules, on March 1, 2006, and
CSD’s investment in these activities is motivated by new ISO/IEC 24759, Test Requirements for Cryptographic
technical ideas that emerge from these ISO standards. For Modules, on July 1, 2008. ISO/IEC 19790 specifies the
example, INCITS 504 is an ID platform that leverages the FIPS security requirements for a cryptographic module utilized
201 infrastructure to support a large number of government within a security system protecting sensitive information
1 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

in computer and telecommunication systems. These In addition to the aforementioned standards, the
efforts bring consistent testing of cryptographic modules Technical Standard (TS) ISO/IEC TS 30104:2015, Physical
to the global community by providing ISO-equivalent Security Attacks, Mitigation Techniques and Security
standards representing FIPS 140-2, Security Requirements Requirements, for which Mr. Easter was the editor, was
for Cryptographic Modules and Derived Test Requirements published on May 15, 2015.
[DTR] for FIPS 140-2, Security Requirements for Crypto-
Physical security mechanisms are employed by
graphic Modules.
cryptographic modules where the protection of the module’s
ISO/IEC JTC 1/SC 27 Working Group (WG) 3 completed sensitive security parameters are desired. ISO/IEC 30104
and published revisions of ISO/IEC 19790:2006 and ISO/ addresses how to express security assurance for products
IEC 24759:2008, for which Mr. Randall J. Easter of CSD where the risk of the security environment requires the
was the principal editor. The revision of ISO/IEC 19790 support of such mechanisms. This Technical Specification
was published on August 15, 2012. The revision of ISO/IEC addresses the following topics:
24759 was published on January 31, 2014. Both ISO/IEC
• A survey of physical security attacks directed against
standards were also adopted by the American National
different types of hardware embodiments, including
Standards Institute (ANSI). The two ISO/IEC revisions were
a description of known physical attacks, ranging from
developed with international support and the collaboration
simple attacks that require minimal skill or resources, to
of governments, industry and academia. Revised corrections
complex attacks that require trained, technical people
of both standards were published on December 15, 2015.
and considerable resources;
The revision of ISO/IEC 19790:2012 addresses new
• Guidance on the principles, best practices and tech-
security areas such as: defined software module boundaries;
niques for the design of tamper protection mechanisms
degraded modes of operation; trusted channels; two-
and methods for the mitigation of those attacks; and
factor authentication; software security; mitigation of fault
• Guidance on the evaluation or testing of hardware tam-
induction and side-channel attacks; operational self-tests
per protection mechanisms and references to current
for algorithms; and life-cycle assurance from design to
standards and test programs that address hardware
end-of-life. Figure 2 is a chart of the ISO/IEC standards,
tamper evaluation and testing.
as explained above, in which CSD has played a part during
the development process.
Figure 2: Cryptographic Module Testing – ISO Standards
1 7
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

CSD’s Mr. Easter is also the principal editor or co-editor FEDERAL INFORMATION
of the following draft ISO/IEC documents:
SECURITY MANAGEMENT ACT
• ISO/IEC 17825, Testing methods for the mitigation of
(FISMA) IMPLEMENTATION
non-invasive attack classes against cryptographic mod-
PROJECT
ules (expected publication January 2016);
• ISO/IEC 18367, Cryptographic algorithms and security
The FISMA Implementation Project focuses on:
mechanisms conformance testing;
• Developing a comprehensive series of standards and
• ISO/IEC 19896-1: Competence requirements for infor-
guidelines to help federal agencies build effective infor-
mation security testers and evaluators — Part 1: Intro-
mation security programs, defend against increasingly
duction, concepts and general requirements;
sophisticated cyber-attacks, and demonstrate compli-
• ISO/IEC 19896-2: Competence requirements for ance to security requirements set forth in legislation,
information security testers and evaluators — Part 2: Executive Orders, Homeland Security Directives, and
Knowledge, skills and effectiveness requirements for Office of Management and Budget (OMB) policies;
ISO/IEC 19790 testers;
• Building a common understanding and reference
• ISO/IEC 20085-1: Test tool requirements and test tool guides for organizations applying the NIST suite of
calibration methods for use in testing non-invasive standards and guidelines that support the NIST Risk
attack mitigation techniques in cryptographic modules Management Framework (RMF) (see http://csrc.nist.
— Part 1: Test tools and techniques; gov/groups/SMA/fisma/framework.html);
• ISO/IEC 20085-2: Test tool requirements and test tool • Developing minimum criteria and guidelines for recog-
calibration methods for use in testing non-invasive nizing security-assessment organization providers as
attack mitigation techniques in cryptographic modules capable of assessing information systems consistent
— Part: 2 Test calibration methods and apparatus; with NIST standards and guidelines supporting the
• ISO/IEC 20540: Guidelines for testing cryptographic RMF; and
modules in their operational environment; and • Conducting FISMA outreach to public and private-sec-
• ISO/IEC 20543: Test and analysis methods for random tor organizations.
bit generators within ISO/IEC 19790 and ISO/IEC 15408. During FY 2015, the CSD FISMA Implementation project
CSD’s contributions to the development of these continued to strengthen collaboration through the Joint Task
international standards create a strong foundation for the Force (JTF) Transformation Initiative, which includes the
adoption of and migration from currently used national Department of Defense (DOD), the Intelligence Community
standards. In particular, this adoption will promote (IC), and the Committee on National Security Systems
international harmonization for the implementation and (CNSS), and other federal agencies. The JTF partners
testing of cryptographic algorithms and modules, while continue to develop and update key cybersecurity guidelines
accommodating individual country preferences in the choice for protecting federal information and information systems
of approved security functions. CSD published a Federal as part of the Unified Information Security Framework.
Register notice in August 2015 seeking public comment Previously, the JTF developed common security guidance
for migrating from FIPS 140-2 to ISO/IEC 19790:2012. The in the critical areas of security controls for information
comment period ended September 2015 (see https:// systems and organizations, security assessment procedures
federalregister.gov/a/2015-19743). to demonstrate security control effectiveness, security
authorizations for risk acceptance decisions, and continuous
For More Information, See:
monitoring activities to ensure that decision makers receive
http://csrc.nist.gov/groups/STM/ the most up-to-date information on the security state of
their information systems. In addition, CSD worked with
CONTACT: the General Services Administration (GSA) Federal Risk
and Authorization Management Program (FedRAMP), a
Mr. Randall J. Easter
government-wide program that provides a standardized
(301) 975-4641
approach to security assessment, authorization, and
randall.easter@nist.gov
continuous monitoring for cloud products and services. The
team developed a high-impact security control baseline
1 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

overlay for FedRAMP cloud systems in accordance with NIST new areas of cybersecurity research and development,
standards and guidelines. and serving on cybersecurity advisory panels.
In FY 2015, the CSD FISMA Implementation project staff • Collaboration with JTF partners and other federal
worked on the following initiatives: organizations: CSD staff worked closely with JTF part-
ners on continued cooperation and planning to ensure
• Risk Management Guidelines: SP 800-53 Revision 4,
that the five JTF publications remain current, and on
Security and Privacy Controls for Federal Information
the designation of additional special publications as
Systems and Organizations, provides organizations
JTF guidance. The CSD FISMA implementation project
with the security controls necessary to appropriately
staff also collaborated with DOD, IC, the Department
strengthen their information systems and the environ-
of Homeland Security (DHS), the Federal Emergen-
ments in which those systems operate, and provides a
cy Management Agency (FEMA), the Government
process for selecting the appropriate controls, which
Accountability Office (GAO), OMB, GSA, the Small Busi-
contributes to systems that are resilient in the face of
ness Administration (SBA), and the Inspector Generals
attacks and other threats. This “Build It Right” strategy
(IGs) on multiple projects to ensure consistency with
is reinforced with the ongoing work on the Second
FISMA-related guidance and to protect information in a
Public Draft of SP 800-160, Systems Security Engineer-
way that is commensurate with risk.
ing: An Integrated Approach to Building Trustworthy
Resilient Systems. The implementation of SPs 800-53 In FY 2015, the CSD FISMA Implementation project staff
and 800-160, combined with the implementation of completed the following activities:
SP 800-37, Guide for Applying the Risk Management
• Published the final version of SP 800-53A, Revision
Framework to Federal Information Systems, and SP
4, Assessing Security and Privacy Controls in Federal
800 137, Information Security Continuous Monitoring
Information Systems and Organizations;
for Federal Information Systems and Organizations,
• Published both Initial Public Draft (IPD) and final ver-
provide organizations with near real-time information
sions of SP 800-171, Protecting Controlled Unclassified
that is essential for senior leaders making ongoing
Information in Nonfederal Information Systems and
risk-based decisions affecting their critical missions and
Organizations, to provide guidance to federal agencies
business functions.
for the protection of Controlled Unclassified Informa-
• Guidelines for a Role-Based Information Security
tion when such information is resident in nonfederal
Training Model: SP 800 16, A Role-Based Model for
information systems and organizations;
Federal Information Technology/Cybersecurity Train-
• Published an errata version of SP 800-53, Revision 4 to
ing, describes a process for developing information
make necessary clarifications and ensure consistency
technology/cybersecurity role-based training. Its pri-
with subsequently published/revised NIST SPs and
mary focus is to provide a comprehensive, yet flexible,
new/updated federal policy requirements;
methodology for the development of training courses
or modules for personnel who have been identified as • Continued collaboration with DHS to develop a multi-
having significant information technology/cybersecu- ple-volume Interagency Report on Automation Support
rity responsibilities within agencies. Agencies can use for Ongoing Assessments, which is based on NIST stan-
SP 800-16 to tailor the Role-Based Security Training to dards and guidelines; and
meet the needs of their own organization.
• Continued the development of preliminary drafts of SP
• FISMA Outreach Activity to Public and Private Sector 800-18 Revision 2, Guide for Developing Security Plans
Organizations: Cybersecurity outreach briefings were for Federal Information Systems and Organizations
conducted and support provided to all levels of govern- and SP 800-60 Revision 2, Guide for Mapping Types
ment (federal, state and local), as well as private sector of Information and Information Systems to Security
organizations, on multiple information security topics Categories.
of interest. These include, for example, effective imple-
In FY 2016, CSD FISMA Implementation project staff
mentation of the NIST RMF, contingency planning, in-
intend to:
terconnection security agreements, and information se-
• Finalize SP 800-160, Systems Security Engineering: An
curity for small businesses. In addition, the CSD FISMA
Integrated Approach to Building Trustworthy Resilient
implementation project staff conducted outreach activ-
Systems;
ities with academic institutions, providing information
on NIST’s security standards and guidelines, exploring
1 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

•   Finalize SP 800-16, A Role-Based Model for Federal  CSD’s  project  team  contributes  to  the  development  of
Information Technology / Cybersecurity Training; biometric standards and participates in the INCITS Technical
Committee M1 – Biometrics and ISO/IEC Joint Technical
•   Begin the development of SP 800-53, Revision 5,
|     |     |     |     | Committee  | (JTC)  1  | Subcommittee  | (SC)  | 37  – Biometrics  |     |
| --- | --- | --- | --- | ---------- | --------- | ------------- | ----- | ----------------- | --- |
Security and Privacy Controls for Federal Information
standards bodies. CSD plans to continue this work in FY 2016.
Systems and Organizations;
•   Continue to explore ways to use automation to support
SP 800-53 updates;
•   Continue the development of SP 800-60, Revision 2,
Guide for Mapping Types of Information and Informa-
tion Systems to Security Categories;
•   Continue the development of SP 800-18, Revision 2,
Guide for Developing Security Plans for Federal Infor-
mation Systems and Organizations;
|     |     |     |     | In  FY  | 2015,  Biometric  | Conformance  |     | Test  | Software  |
| --- | --- | --- | --- | ------- | ----------------- | ------------ | --- | ----- | --------- |
•   Expand cybersecurity outreach to include additional
|     |     |     |     | (BioCTS)  | for  ANSI/NIST-ITL  |     | (which  | targets  | biometric  |
| --- | --- | --- | --- | --------- | ------------------- | --- | ------- | -------- | ---------- |
state, local, and tribal governments, as well as private
sector organizations and academic institutions;  transactions based on NIST SP 500-290, and SP 500-290
Revision 1 - Data Format for the Interchange of Fingerprint,
•   Continue to support federal agencies in the effective
Facial & Other Biometric Information) received a substantial
implementation of the RMF; and
update. Version 2.0 of the testing software was released and
•   Continue collaboration with JTF partners and other  added support for testing for the remaining traditionally
federal organizations. encoded record types not previously supported (+12 for
|     |     |     |     | ANSI/NIST-ITL  | 1-2011,  | and  +18  | for  ANSI/NIST-ITL  |     | 1-2011  |
| --- | --- | --- | --- | -------------- | -------- | --------- | ------------------- | --- | ------- |
For More Information, See:
Update: 2013). Version 2.0 now supports all traditionally
http://csrc.nist.gov/groups/SMA/fisma encoded biometric record types between the two versions
|     |     |     |     | of  the  | published  ANSI/NIST-ITL  |     | standards.  | Additionally,  |     |
| --- | --- | --- | --- | -------- | ------------------------- | --- | ----------- | -------------- | --- |
CONTACTS:
|     |     |     |     | Version  | 2.0  added  | many  enhanced  | editing  | features  | for  |
| --- | --- | --- | --- | -------- | ----------- | --------------- | -------- | --------- | ---- |
traditionally encoded biometric transactions – some new
| Dr. Ron Ross  |     | Ms. Pat Toth  |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
features include: adding and removing records and fields,
| (301) 975-5390  |     | (301) 975-5140  |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
arranging records and fields, automatically sorting records,
| ron.ross@nist.gov  |     | patricia.toth@nist.gov |     |             |                 |         |         |      |           |
| ------------------ | --- | ---------------------- | --- | ----------- | --------------- | ------- | ------- | ---- | --------- |
|                    |     |                        |     | displaying  | the  biometric  | sample  | image,  | and  | enhanced  |
binary data editing features. In addition to the enhanced
| Ms. Kelley Dempsey   |     | Ms. Peggy Himes  |     |     |     |     |     |     |     |
| -------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
editing features, BioCTS for ANSI/NIST-ITL received many
| (301) 975-2827  |     | (301) 975-2489  |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
usability enhancements, as well as updates to some core
| kelley.dempsey@nist.gov   |     | peggy.himes@nist.gov |     |     |     |     |     |     |     |
| ------------------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
software functionality, providing a more usable and robust
testing tool.
As illustrated in Figure 3, a new feature of BioCTS is the
BIOMETRIC STANDARDS AND
display of the biometric sample, when possible, so that the
ASSOCIATED CONFORMITY
user can get visual feedback on the biometric data that is
ASSESSMENT TESTING TOOLS under test. The update provides a rich editing environment
|     |     |     |     | for  binary/traditionally  |     | encoded  | transactions  |     | and  files,  |
| --- | --- | --- | --- | -------------------------- | --- | -------- | ------------- | --- | ------------ |
which are difficult for humans to read. Version 2.0 provides
| NIST’s  CSD  | supports  | the  development  | of  biometric  |     |     |     |     |     |     |
| ------------ | --------- | ----------------- | -------------- | --- | --- | --- | --- | --- | --- |
conformance  testing  methodology  standards  and  other  a user-friendly way to see each field within a transaction/
conformity-assessment  efforts  through  active  technical  file, associated test results, and allows for the modification
participation  in  the  development  of  these  standards  of data (as shown in Figure 4.)  All of the new features are
and  the  development  of  associated  conformance  test  detailed in the BioCTS for ANSI/NIST-ITL v2 User Guide (see:
http://csrc.nist.gov/groups/ST/BiomResCenter/CTA_BETA/
software, architectures and test suites. These test tools are
developed to promote the adoption of these standards  BioCTS_AN_ITL_v2_Guide.pdf).
and to support users that require conformance to selected
biometric standards, product developers and testing labs.
2 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Outreach efforts in FY 2015 in support of biometric
|     |     |     |     | standards  | development  | and  | conformity  | assessment  |
| --- | --- | --- | --- | ---------- | ------------ | ---- | ----------- | ----------- |
included test tool contributions for the standards developers
|     |     |     |     | (in  support   | of  ongoing    | development  |                | projects),  and  |
| --- | --- | --- | --- | -------------- | -------------- | ------------ | -------------- | ---------------- |
|     |     |     |     | presentations  | on  ANSI/NIST  | and          | international  | biometric        |
standards and related conformity assessment activities.  The
work included the development of technical publications,
|     |     |     |     | the  review  | of  research  | papers  | for  external  | publications,  |
| --- | --- | --- | --- | ------------ | ------------- | ------- | -------------- | -------------- |
and participation in conference program committees. CSD
published NIST Special Publication 500-304, Conformance
|     |     |     |     | Testing  | Methodology  | Framework  | for  | ANSI/NIST-ITL  |
| --- | --- | --- | --- | -------- | ------------ | ---------- | ---- | -------------- |
1-2011 Update: 2013, Data Format for the Interchange of
Fingerprint, Facial & Other Biometric Information in June
2015. Additionally, CSD published NIST SP 500-304 Annex
|     |     |     |     | D: Test Notes and Exceptions for the ANSI/NIST ITL 1-2011  |     |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
Figure 3: BioCTS displays the biometric sample to   Update 2013 Conformance Testing Methodology Framework
|     | provide visual feedback. |     |     | in July 2015. |     |     |     |     |
| --- | ------------------------ | --- | --- | ------------- | --- | --- | --- | --- |
For More Information, See:
The latest version of BioCTS was released in August
2015, together with documentation and sample data. The  BioCTS - Biometric Conformance Test Tool Downloads:
BioCTS software installer files, as well the ancillary tools and
http://www.nist.gov/itl/csd/biometrics/biocta_download.
sample data can be downloaded from the NIST Biometrics
cfm
| website.  |   (see:  http://www.nist.gov/itl/csd/biometrics/ |     |     |                |              |                               |     |     |
| --------- | ------------------------------------------------ | --- | --- | -------------- | ------------ | ----------------------------- | --- | --- |
|           |                                                  |     |     | NIST  Special  | Publication  | 500-304: Conformance Testing  |     |     |
biocta_download.cfm).
Methodology Framework for ANSI/NIST-ITL 1-2011 Update:
2013, Data Format for the Interchange of Fingerprint, Facial
& Other Biometric Information:
http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.
SP.500-304.pdf
NIST SP 500-304 Annex D: Test Notes and Exceptions for
the ANSI/NIST ITL 1-2011 Update 2013 Conformance Testing
Methodology Framework:
http://csrc.nist.gov/groups/ST/BiomResCenter/CTA_BETA/
External_Notes_Exceptions_NIST_SP_500_304_with_
Errata.pdf
CONTACT:
Mr. Dylan Yaga
(301) 975-6004
Figure 4: BioCTS provides a rich editing environment for
dylan.yaga@nist.gov
reviewing and updating records.
| A            | number  of  technical  | contributions       | towards  the  |     |     |     |     |     |
| ------------ | ---------------------- | ------------------- | ------------- | --- | --- | --- | --- | --- |
| development  | of  ANSI/NIST          | and  international  | standards     |     |     |     |     |     |
were submitted. They included technical contributions on
international biometric data interchange formats and their
| associated  | conformance  | testing  methodologies,  | as  well  |     |     |     |     |     |
| ----------- | ------------ | ------------------------ | --------- | --- | --- | --- | --- | --- |
as on SP 500-290 Revision 1 and the associated National
| Information  | Exchange  | Model  (NIEM)  Extensible  | Markup  |     |     |     |     |     |
| ------------ | --------- | -------------------------- | ------- | --- | --- | --- | --- | --- |
Language (XML) Schema (see https://tools.niem.gov).
2 1
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

SECURITY OF CYBER-  In June 2014, NIST established the CPS Public Working
Group (PWG), which is open to all, to foster and capture
PHYSICAL SYSTEMS (CPS)
|        |          |                 |     |          |     |        | inputs  from  | those  | involved     | in  | CPS,  both     | nationally  | and           |
| ------ | -------- | --------------- | --- | -------- | --- | ------ | ------------- | ------ | ------------ | --- | -------------- | ----------- | ------------- |
|        |          |                 |     |          |     |        | globally.     | CSD    | is  working  | in  | collaboration  |             | with  NIST’s  |
| CSD’s  | overall  | Cyber-Physical  |     | Systems  |     | (CPS)  | effort        |        |              |     |                |             |               |
Engineering Laboratory (EL) Smart Grid and Cyber-Physical
will provide the next generation of “smart,” co-designed
|     |     |     |     |     |     |     | Systems  | Program  | Office,  | NIST’s  | Physical  | Measurement  |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | ------- | --------- | ------------ | --- |
and co-engineered interacting networks of physical and
Laboratory Time and Frequency Division, ITL’s Software
computational components. Specifically, CSD supports the
|     |     |     |     |     |     |     | and  Systems  | Division  |     | and  | ITL’s  Advanced  |     | Networking  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | ---- | ---------------- | --- | ----------- |
effort by providing cybersecurity and privacy experts who
Technologies Division to lead a working group of govern-
help leverage existing resources and address CPS-specific
ment, academic, and industry stakeholders. The CPS PWG
cybersecurity and privacy challenges. Such challenges are
consists of five technical subgroups:
related to personalized health care, emergency response,
•  Definition, Vocabulary, and Reference Architecture;
traffic flow management, and electric power generation
| and delivery, and many other emerging technical areas.  |     |     |     |     |     |     | •  Use Cases; |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
Other phrases that are often referenced along with CPS
•  Cybersecurity and Privacy;
technologies include:
•  Data Interoperability; and
•  Internet of Things (IoT);
•  Timing and Synchronization.
•  Industrial Internet;
Each subgroup consists of co-leaders from academia,
•  Smart Cities;
|     |     |     |     |     |     |     | industry  | and  NIST.  | CSD  | co-leads  | the  | Cybersecurity  | and  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---- | --------- | ---- | -------------- | ---- |
•  Smart Grid; and Privacy subgroup that is focused on identifying strategies
•   “Smart” Anything (e.g., Cars, Buildings, Homes, Manu- for  cybersecurity  and  privacy  in  CPS,  and  is  working
collaboratively with the other subgroups to ensure that
facturing, Hospitals, Appliances) (see http://www.nist.
gov/cps/). cybersecurity  is  included  as  a  design  principle  during
development.
| Composed  |     | of  heterogeneous,  |     | potentially  |     | distributed  |     |     |     |     |     |     |     |
| --------- | --- | ------------------- | --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
In September 2015, the CPS PWG published the Draft
| components  |     | and  systems,  | CPS  | provides  |     | a  promise  | of  |     |     |     |     |     |     |
| ----------- | --- | -------------- | ---- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
increased efficiency and interaction between the digital and  Framework for CPS  that  includes  the  work  of  the  five
technical subgroups. The document reflects more than a
physical worlds. However, assuring that these emerging and
evolving systems are reliable, robust, resilient, trustworthy,  year’s effort by the CPS PWG, which includes a few hundred
|     |     |     |     |     |     |     | members  | drawn  | primarily  | from  | industry,  | academia  | and  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | ----- | ---------- | --------- | ---- |
secure, and that they protect the privacy of information
government. In 2016, the CPS PWG will collect and analyze
(to only list a few concerns) poses a unique cybersecurity
challenge.  the comments to the draft and publish the next version of the
CPS Framework. The CPS PWG deliverables are technology
| CPS  | present  | unique  | challenges,  |     | including  | the  | need  |     |     |     |     |     |     |
| ---- | -------- | ------- | ------------ | --- | ---------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
and business-model neutral, and freely available online and
for integration with legacy components and allowance for
intended for open use by all stakeholders.
emerging technologies, and real-time response in support of
extremely high availability, predictability, and reliability. Additionally, in 2015, CSD, in conjunction with NIST’s
|     |     |     |     |     |     |     | Engineering  | Laboratory,  |     | Intelligent  |     | Systems  | Division,  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | ------------ | --- | -------- | ---------- |
Cybersecurity is an important crosscutting discipline
finalized SP 800-82 Revision 2, Guide to Industrial Control
that is critical to the safe and resilient design, development
Systems Security. CSD will also continue to participate in the
| and  operation  |     | of  | CPS.  Addressing  |     | the  | opportunities  |     |     |     |     |     |     |     |
| --------------- | --- | --- | ----------------- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
International Society of Automation (ISA) 99 Committee,
and challenges of CPS requires a broad collaboration to
which develops and establishes standards, recommended
| develop  | a  common  |     | foundation,  | including  |     | a  consensus  |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ------------ | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
practices, technical reports, and related information that
| definition,  | vocabulary,  |     | reference  | architecture,  |     | and  | a   |     |     |     |     |     |     |
| ------------ | ------------ | --- | ---------- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
define procedures for implementing electronically secure
| shared  | understanding  |     | of  the  | essential  | roles  | of  timing,  |             |             |     |               |          |      |           |
| ------- | -------------- | --- | -------- | ---------- | ------ | ------------ | ----------- | ----------- | --- | ------------- | -------- | ---- | --------- |
|         |                |     |          |            |        |              | industrial  | automation  |     | and  control  | systems  | and  | security  |
cybersecurity and data interoperability. CSD is researching
practices, and for assessing electronic security performance.
the cybersecurity needs of the broader landscape of CPS
by leveraging CSD’s expertise in cybersecurity in different  For More Information, See:
domains and applications of CPS (such as industrial control  http://www.nist.gov/cps/
systems, the smart grid, hardware-enabled security, and
embedded systems).
2 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

strategic plan for cybersecurity R&D and participated in
CONTACTS:
panel presentations to which the SSG was invited to describe
Mr. Stephen Quinn Ms. Suzanne Lightman federal directions in cybersecurity R&D at relevant forums
(301) 975-6967 (301) 975-6442 and conferences (see https://www.nitrd.gov/nitrdgroups/
stephen.quinn@nist.gov suzanne.lightman@nist.gov index.php?title=Cyber_Security_Information_Assurance_
Research_and_Development_Senior_Steering_Group_
(CSIA_R%26D_SSG)#title).
FEDERAL CYBERSECURITY CSD is also a regular participant in the coordination
activities of the federal Special Cyber Operations
RESEARCH & DEVELOPMENT
Research and Engineering (SCORE) Committee. SCORE
(R&D) enables technology transfer through the sharing of NIST
cybersecurity expertise and publications with researchers
The Networking and Information Technology Research throughout the Federal Government. The SCORE committee
and Development (NITRD) program provides a framework interacts with federal leaders and reports to the National
in which many federal agencies come together to coordinate Science & Technology Council’s Committee on Homeland &
their networking and IT research and development National Security. In FY 2015, NIST expertise in supply chain
(R&D) efforts. CSD remained committed to the value of risk management and cryptography was included in SCORE
communicating its R&D efforts to other federal colleagues reports.
and identifying the opportunities to support R&D efforts
For More Information, See:
throughout the Federal Government.
http://www.nitrd.gov/
In FY 2015, the NITRD Cyber Security and Information
Assurance (CSIA) Interagency Working Group (IWG)
CONTACT:
monthly meetings provided an opportunity to learn and
share information about NIST’s ongoing research with Mr. Bill Newhouse
federal program managers of cybersecurity research (see (301) 975-2869
https://www.nitrd.gov/nitrdgroups/index.php?title=Cyber_ william.newhouse@nist.gov
Security_and_Information_Assurance_Interagency_
Working_Group_(CSIA_IWG)#title). The Cybersecurity
Enhancement Act of 2014 requested the development of SECURITY ASPECTS OF
a new federal cybersecurity research and development
ELECTRONIC VOTING
strategic plan, and NIST was a consistent presence at the
regular development meetings for the new plan that is
In 2002, Congress passed the Help America Vote Act
intended for release during the month of February 2016.
(HAVA) to encourage the upgrade of voting equipment
(see Cybersecurity Enhancement Act of 2014 https://
across the United States. HAVA established the Election
www.congress.gov/bill/113th-congress/senate-bill/1353/
Assistance Commission (EAC) and the Technical Guidelines
text, and see strategic plan https://www.whitehouse.gov/
Development Committee (TGDC), chaired by the Director of
sites/whitehouse.gov/files/documents/2016_Federal_
NIST. HAVA directs NIST to provide technical support to the
Cybersecurity_Research_and_Development_Stratgeic_
EAC and TGDC in efforts related to human factors, security,
Plan.pdf).
and laboratory accreditation. As part of NIST’s efforts,
FY 2015 also included the development of a National
CSD supports the activities of the EAC related to voting
Privacy Research Strategy by the members of the National
equipment security.
Privacy Research Forum (see https://www.nitrd.gov/
In the past year, NIST continued to support the EAC
cybersecurity/nationalprivacyresearchstrategy.aspx).
in finalizing changes to the Voluntary Voting System
Naomi Lefkowitz, Senior Privacy Policy Advisor at NIST, and
Guidelines (VVSG) 1.1. These changes sought to improve
Simson Garfinkel, Senior Advisor in the Information Access
the auditability of voting systems, provide greater software
Division, shared NIST’s focus on privacy and brought their
integrity protections, expand and improve access-control
expertise to the development process for the privacy R&D
requirements, and help ensure that cryptographic security
plan that will be published in FY 2016.
mechanisms are implemented properly. The EAC approved
NIST regularly attended the NITRD CSIA Senior
these updates to the VVSG in March 2015. In addition, NIST
Steering Group meetings to share and stay connected with
completed a set of draft test assertions for the security
opportunities that supported the development of the new
requirements in the VVSG. This included test assertions in the 2 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

areas of access control, software setup and validation, polling Services’ (DHHS) Office for Civil Rights (OCR) co-hosted the
place security, and the use of public telecommunications eighth annual Health Insurance Portability and Accountability
networks. Act (HIPAA) Security Rule conference, Safeguarding Health
Information: Building Assurance through HIPAA Security, in
Initial efforts on the next-generation of the VVSG have
September 2015 in Washington, D.C. The conference offered
already begun. In February, NIST and the EAC sponsored
important sessions that focused on broad topics of interest
the second Future of Voting Systems Symposium. This
to the healthcare and health IT security community. Over
symposium brought together election officials, voting
600 in-person and virtual attendees from federal, state,
system manufacturers, voting system test laboratories,
and local governments, academia, HIPAA-covered entities
standards developers, academics, and federal, state, and
and business associates, industry groups, and vendors
local government officials to discuss emerging trends in
heard from, and interacted with, healthcare, security, and
voting. The discussions at this workshop are being used
privacy experts on technologies and methodologies for
to define the scope and priorities for the next-generation
safeguarding health information and for implementing the
guidelines.
requirements of the HIPAA Security Rule. Presentations and
In FY 2016, NIST and the EAC will establish a set of
panel discussions covered a variety of security management
public working groups to inform the development of a new
and technical assurance topics, including:
version of the VVSG. NIST and EAC goals are to accelerate
• Collaborative approaches for securing medical devices;
the development and adoption of the VVSG by leading these
working groups in close consultation with election officials, • Vulnerabilities in medical devices and control systems;
the federal and private sectors, standards bodies and EAC
• Business associate liability;
committees, academic researchers, and other members
• Information sharing and threat intelligence;
of the public. These working groups will focus on voting
system technology areas, including accessibility, usability, • Data recovery and security plans; and
interoperability, security, and testing and certification.
• Securing electronic health records on mobile devices.
For More Information, See:
The keynote addresses were delivered by Jocelyn
http://vote.nist.gov Samuels, Director, DHHS/OCR, and Dr. Cris Ewell, Chief
Information Security Officer at Seattle Children’s Hospital.
CONTACTS:
In FY 2016, NIST will work with diverse healthcare
stakeholders, including partners in government and
Mr. Andrew Regenscheid Mr. Joshua Franklin
industry, to support security capabilities in new areas,
(301) 975-5155 (301) 975-8463
such as the Precision Medicine Initiative, and identify
andrew.regenscheid@nist.gov joshua.franklin@nist.gov
opportunities to strengthen the sector’s cybersecurity risk
management efforts through the application of the NIST
Cybersecurity Framework.
HEALTH INFORMATION
For More Information, See:
TECHNOLOGY SECURITY
http://www.nist.gov/healthcare/security/
Health Information Technology (HIT) enables better
patient care through the secure use and sharing of health CONTACT:
information. HIT leads to improvements in healthcare quality,
Mr. Kevin Stine
reduced medical errors, increased efficiencies in health care
(301) 975-4483
delivery and administration, and improved health for the
kevin.stine@nist.gov
general population. Central to reaching these goals is the
assurance of the confidentiality, integrity, and availability of
health information. CSD works with government, industry,
academia, and others to provide security tools, technologies,
and methodologies that provide for the security and privacy
of health information.
NIST CSD continued its HIT security outreach efforts
in FY 2015. NIST and the Department of Health and Human
24
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

SUPPLY CHAIN RISK The Supply Chain Risk Management (SCRM) program
seeks to provide organizations with a standardized and
MANAGEMENT (SCRM)
repeatable toolkit of technical and intelligence resources to
FOR INFORMATION AND
strategically manage supply-chain risk throughout the entire
COMMUNICATIONS lifecycle of systems, products and services.
TECHNOLOGY (ICT) In FY 2015, CSD finalized and published NIST SP 800-
161, Supply Chain Risk Management Practices for Federal
Information and communication technologies have Information Systems and Organizations. This document
rapidly become more numerous and more capable. These builds on existing NIST guidance to help federal departments
technologies increasingly rely on a supply-chain ecosystem and agencies identify, assess and mitigate ICT supply-chain
that is long, complex, variable, interconnected, globally risk at all organizational levels.
distributed, and geographically diverse. Outsourcing the
When NIST researched and developed the Framework
development, maintenance, management, and disposal of
for Improving Critical Infrastructure Cybersecurity, which
data and ICT is increasingly common.
was published in February 2014, cyber supply-chain risk
These trends have caused organizations acquiring management (CSCRM) was identified as an area needing
technology to experience a lack of visibility throughout the further research and guidance (see the NIST Roadmap
supply chain (see Figure 5). Such organizations need a better for Improving Critical Infrastructure Cybersecurity, also
understanding of how the technology being acquired was published in February 2014). In FY 2015, CSD initiated a
developed, integrated and deployed. These organizations project on industry best practices for CSCRM. Initial research
also need to better understand the processes, procedures, was developed into company case studies spanning multiple
and practices used to assure the integrity, security, resilience, business sectors. The studies will be analyzed to support a
and quality of the products and services being obtained. This workshop, and a final publication is planned for FY 2016.
lack of visibility and understanding, in turn, has decreased
the acquiring organization’s ability to effectively manage
risk inherited from the supply chain.
Figure 5: Visibility Challenges for Supply Chain Risk Management (SCRM)
2 5
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

CSD staff continued to join staff members from NATIONWIDE PUBLIC
the Department of Defense in co-chairing a U.S. federal
SAFETY BROADBAND
interagency working group on SCRM. The working group
NETWORK (NPSBN)
evolved from the White House’s Comprehensive National
Cybersecurity Initiative (CNCI) 11, Develop a Multi-Pronged CYBERSECURITY
Approach for Global Supply Chain Risk Management, which
ended in 2014. In FY 2015, the co-chairs began the process
of formalizing the working group under the auspices of the In February 2012, Congress
CNSS. passed the Middle Class Tax Relief
CSD continued working with partners through the and Job Creation Act. One portion
Software and Supply Chain Assurance (SSCA) Forum, co- of this legislation calls for the
sponsoring four multi-day workshops. The SSCA Working establishment of a nationwide,
Group (WG) is a key public-private partnership that meets interoperable public-safety broad-
quarterly to discuss current projects, tools, resources, and band network based on the
lessons learned regarding CSCRM. The SSCA WG is co- 3rd Generation Partnership Project’s
sponsored by NIST, GSA, DoD and DHS. (3GPP) Long-Term Evolution (LTE)
technology. The network will be
In FY 2016, CSD will:
deployed and operated by the First
• Continue working on Industry Best Practices for Cyber Responder Network Authority
Source: http://www.pscr.gov/
Supply Chain Management, including hosting a two- (FirstNet). The planned NPSBN will
day workshop, developing cyber supply-chain stan- “create a much needed nationwide interoperable broadband
dards mappings to the Cybersecurity Framework, as network that will help police, firefighters, emergency medical
well as a strategy to better integrate the supply-chain service professionals and other public safety officials stay
management and information security functions in or- safe and do their jobs.” (see http://www.ntia.doc.gov/
ganizations; the various pieces of the research project category/public-safety). NIST is directed to establish a list
will culminate in a draft guidance document; of certified devices and required components to be used
• Continue to co-chair the interagency working group on by public-safety officials, vendors, and other interested
cyber supply-chain risk management; parties for interacting with the nationwide network. NIST
is also directed to conduct research and development
• Begin research to demonstrate cause and effect rela-
that supports the acceleration and advancement of the
tionships between cyber supply-chain capability/ma-
nationwide network.
turity levels and organizational performance outcomes
over time; and In FY 2015, CSD supported the joint National
Telecommunications and Information Administration (NTIA)
• Research metrics for use in supply chain risk manage-
and NIST Public Safety Communications Research (PSCR)
ment.
program with efforts in public-safety mobile-application
For More Information, See: security, identity management, and enabling cybersecurity
capabilities on the PSCR 700 MHz LTE network located in
http://csrc.nist.gov/scrm/
Boulder, Colorado (see http://www.pscr.gov). In June 2015,
CSD, in cooperation with the Association of Public-Safety
CONTACTS:
Communications Officials (APCO) International and FirstNet,
ICT SCRM Team email: scrm-nist@nist.gov held a half-day workshop titled “Identifying and Categorizing
Data Types for Public Safety Mobile Applications.” The
Mr. Jon Boyens Ms. Celia Paulsen
outcome of that workshop will be captured in a forthcoming
Program Lead Technical Lead
NIST publication in FY 2016. At PSCR’s Annual Public Safety
(301) 975-5549 (301) 975-5981
Broadband Stakeholder Conference, CSD organized a
jon.boyens@nist.gov celia.paulsen@nist.gov
panel titled “Applied Public Safety Cybersecurity Research”
highlighting PSCR’s cybersecurity activities over the previous
twelve months in the areas of identity management, mobile
application security, and LTE infrastructure cybersecurity.
During FY 2015, CSD published NISTIR 8018, Public
Safety Mobile Application Security Requirements
2 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Workshop Summary, and NISTIR 8014, Considerations for  the  need  to  integrate  advanced
Identity Management in Public Safety Mobile Networks. In  security to protect critical assets.
addition, CSD developed an informational survey on mobile
|              |                    |         |          |              |     |     |     |     | The          | Smart  |         | Grid  | Inter-  |
| ------------ | ------------------ | ------- | -------- | ------------ | --- | --- | --- | --- | ------------ | ------ | ------- | ----- | ------- |
| application  | vetting  services  | titled  | “Mobile  | Application  |     |     |     |     |              |        |         |       |         |
|              |                    |         |          |              |     |     |     |     | operability  | Panel  | (SGIP)  |       | became  |
Vetting Services for Public Safety” and Draft NISTIR 8080,
a membership-supported organi-
Usability and Security Considerations for Public Safety
zation in January 2013. The SGIP
Mobile Authentication.
Cybersecurity Working Group (CSWG) was renamed the
CSD participated in the standards development process  Smart Grid Cybersecurity Committee (SGCC), and continues
for LTE technology within the 3GPP, supporting security  to be led by Ms. Suzanne Lightman of the CSD in support of
requirements for public safety that are related to Proximity  responsibilities identified in the Energy Independence and
Services (ProSe), Group Communication System Enablers  Security Act of 2007. The SGCC chair is a voting member of
(GCSE),  and  Mission  Critical  Push-To-Talk  (MCPTT).  In  the SGIP Technical Committee, and serves as an ex-officio
addition, CSD broadened its scope within the IETF to include  Director of the Board.
efforts related to public safety. During the last year, staff from CSD and ITL’s Software
In  FY  2016,  CSD  will  continue  representing  public  and Systems Division (SSD) worked on developing network
safety in international standardization efforts, such as the  security tools that are specifically designed to support next-
IETF and 3GPP. CSD will work to implement and exercise   generation electrical power systems. They concentrated on
LTE cybersecurity infrastructure capabilities in the PSCR  authenticating the provenance of multicast data streams
700  MHz  LTE  network,  conduct  research  into  mobile  from  emerging  power  system  sensors,  called  Phasor
authentication  solutions  to  support  public-safety,  and  Measurement Units.  By authenticating the sensors to the
investigate  mobile  application-security  services  and  utility, the utility may trust that sensor measurements are
solutions to support the security requirements of public- coming from the correct sensors and have not been hijacked.
safety mobile applications and devices. CSD will continue
Multicast authentication of sensor data is challenging,
to engage the public-safety communications community by
|     |     |     |     |     |     | due  to  the  | need  | for  | low  security  |     | overhead,  | tolerance  |     |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | ---- | -------------- | --- | ---------- | ---------- | --- |
organizing workshops and conferences; and participating
|     |     |     |     |     |     | of  lossy  | networks,  | time-criticality,  |     | and  | high  | data  | rates.  |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------------------ | --- | ---- | ----- | ----- | ------- |
in events such as APCO’s Annual Meeting, PSRC’s Annual
Researchers augmented an existing authentication scheme
Public Safety Broadband Stakeholder Conference, and the
to accommodate high-data-rate sensor transmissions that
International Wireless Communications Expo (IWCE).
|     |     |     |     |     |     | are  unbounded  |     | in  length  | (no  | session  | expiration).  |     | Using  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ---- | -------- | ------------- | --- | ------ |
dual offset key chains to reduce the authentication delay
CONTACTS:
|     |     |     |     |     |     | and  computational  |     | overhead  | associated  |     | with  | key  | chain  |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --------- | ----------- | --- | ----- | ---- | ------ |
Ms. Sheila Frankel    Dr. Nelson Hastings  commitment, they developed a new protocol called inf-
TESLA that meets the performance requirements imposed
| (301) 975-3297  |     | (301) 975-5237  |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by the physical dynamics of the power system.
| sheila.frankel@nist.gov  |     | nelson.hastings@nist.gov |     |     |     |           |                  |          |                |     |            |     |          |
| ------------------------ | --- | ------------------------ | --- | --- | --- | --------- | ---------------- | -------- | -------------- | --- | ---------- | --- | -------- |
|                          |     |                          |     |     |     | Their     | key  disclosure  |          | mechanism,     |     | as  well   | as  | com-     |
|                          |     |                          |     |     |     | parative  | studies          | showing  | a  cumulative  |     | reduction  |     | in  the  |
SMART GRID CYBERSECURITY
|     |     |     |     |     |     | communication  |     | overhead  | and  | computational  |     | cost  | over  |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ---- | -------------- | --- | ----- | ----- |
existing methods, are outlined in a paper to appear at the
The major elements of the smart grid are information
Association for Computing Machinery (ACM) Symposium
| technology,  | industrial  control  | systems/operational  |     |     | tech- |     |     |     |     |     |     |     |     |
| ------------ | -------------------- | -------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
on Applied Computing.
| nology  | and  the  communications  |     | infrastructure.  |     | The  |              |     |         |            |     |                |     |        |
| ------- | ------------------------- | --- | ---------------- | --- | ---- | ------------ | --- | ------- | ---------- | --- | -------------- | --- | ------ |
|         |                           |     |                  |     |      | Significant  |     | effort  | was  made  |     | to  integrate  |     | their  |
infrastructure is used to send command information across
|     |     |     |     |     |     | authentication  | protocol  |     | into  existing  |     | network  | simulation  |     |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | --- | --------------- | --- | -------- | ----------- | --- |
the electric grid from generation systems to distribution
software, specifically OPNET, thus providing potential users
systems, and to exchange usage and billing information
between utilities and their customers. Key to the successful  the ability to evaluate the protocol on their own networks
and for their own applications.
| deployment  | of  the  smart  | grid  | infrastructure  |     | is  the   |     |     |     |     |     |     |     |     |
| ----------- | --------------- | ----- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
development of the cybersecurity strategy that includes  Furthermore, in an effort to address the growing interest
cybersecurity  as  a  design  consideration  for  new  and  in co-optimizing cyber and physical components to work
emerging systems, and an approach to adding cybersecurity  together as a system, CSD staff developed mathematical
into existing systems. The electric grid is critical to the  formalism to tradeoff the sensitivity of a dynamic system
economic  and  physical  well-being  of  the  nation,  and  to  attack  or  perturbation  against  the  authentication
emerging cyber threats targeting power systems highlight  overhead incurred by their protocol. This formalism was
2 7
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

demonstrated on a power system use case showing the  coordination, cooperation, focus, public engagement, tech-
limiting  considerations  between  authentication  overhead  nology transfer and sustainability. NIST will highlight these
and stability margins of a wide-area damping controller. activities, engage various stakeholder groups and create
forums for sharing information and leveraging best practices.
In FY 2016, CSD will coordinate with NIST’s Engineering
Laboratory (EL) and Smart Grid Program Office on the  The  NICE  Program  Office  focuses  on  the  following
| further development of a Cybersecurity Smart Grid Test  |          |              |                |     |                | activities: |     |     |     |     |     |     |
| ------------------------------------------------------- | -------- | ------------ | -------------- | --- | -------------- | ----------- | --- | --- | --- | --- | --- | --- |
| Lab,  part                                              | of  the  | NIST  Smart  | Grid  Testbed  |     | Facility  now  |             |     |     |     |     |     |     |
•   Accelerate learning and skills development by invoking
under construction. CSD will also collaborate with SSD on
a sense of urgency in both the public and private sec-
cybersecurity research in relation to the IEEE 1588, Precision  tors to address the shortage of a skilled cybersecurity
Time Protocol, a time synchronization standard that is used
workforce;
for the electric grid and other special-purpose industrial
automation and measurement networks. •   Nurture a diverse learning community through
strengthening education and training across a multi-
For More Information, See:
farious ecosystem that prioritizes learning, emphasizes
http://www.nist.gov/smartgrid outcomes, and celebrates diversity; and
http://www.sgip.org •   Guide Career Development and Workforce Planning
that supports job seekers and employers in addressing
| CONTACTS: |     |     |     |     |     | market demands and maximizing talent management. |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
Ms. Suzanne Lightman     Ms. Victoria Yan Pillitteri    The NICE Program Office staff promoted NICE act-
|                 |     |     |                 |     |     | ivities  through  |     | contributions  |     | to  many  | events,  | symposia,  |
| --------------- | --- | --- | --------------- | --- | --- | ----------------- | --- | -------------- | --- | --------- | -------- | ---------- |
| (301) 975-6442  |     |     | (301) 975-8542  |     |     |                   |     |                |     |           |          |            |
forums, competitions, educational outreach meetings, and
| suzanne.lightman@nist.gov   |     |     | victoria.pillitteri@nist.gov  |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
workshops. The staff continued its leadership to achieve
the Office of Personnel Management (OPM) Cross-Agency
Ms. Tanya Brewer
(301) 975-4534  Priority Goal: “Closing Skills Gaps” for the IT/Cybersecurity
|     |     |     |     |     |     | workforce.  | The  | staff  focused  |     | on  reducing  |     | cybersecurity  |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | --------------- | --- | ------------- | --- | -------------- |
tbrewer@nist.gov
|     |     |     |     |     |     | workforce  | gaps  | and  supported  |     | the  | goals  | of  the  White  |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | --------------- | --- | ---- | ------ | --------------- |
House’s “Ready to Work” initiative. In addition, the staff took
leadership of the NICE Working Group, a group established
| CYBERSECURITY  |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to provide a mechanism in which public and private sector
AWARENESS, TRAINING,    participants can develop concepts, design strategies, and
EDUCATION, AND OUTREACH pursue  actions  that  advance  cybersecurity  education,
training, and workforce development.
In FY 2015, the NICE Program Office announced that
National Initiative for Cybersecurity
|     |     |     |     |     |     | a  grant  | will  be  | awarded  | to  | support  | the  | development  |
| --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | --- | -------- | ---- | ------------ |
Education (NICE)
|     |     |     |     |     |     | of  a  visualization  |     | tool  | to  | show  the  | demand  | for  and  |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | ----- | --- | ---------- | ------- | --------- |
NIST has been the lead for the National Initiative for
availability of critical cybersecurity jobs across the nation.
Cybersecurity Education (NICE) since its inception in 2010.
|     |     |     |     |     |     | This  cybersecurity  |     | jobs  | “heat  | map”  | will  | be  developed  |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | ------ | ----- | ----- | -------------- |
NICE is responsive to President Obama’s declaration that
|     |     |     |     |     |     | in  partnership  |     | with  | Computing  |     | Technology  | Industry  |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | ---------- | --- | ----------- | --------- |
the “cyber threat is one of the most serious economic
|     |     |     |     |     |     | Association  | (CompTIA)  |     | and  | Burning  | Glass  | Technologies.   |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ---- | -------- | ------ | --------------- |
and national security challenges we face as a nation” and
The map will provide data to help employers, job seekers,
| “America’s  | economic  | prosperity  | in  the  | 21st  | century  will  |     |     |     |     |     |     |     |
| ----------- | --------- | ----------- | -------- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
policy makers, training providers, and guidance counselors
depend on cybersecurity.”
|     |     |     |     |     |     | in  order  | to  meet  | today’s  | increasing  |     | demand  | for  cyber- |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | -------- | ----------- | --- | ------- | ----------- |
The  NICE  program  seeks  to  foster,  energize,  and  security workers.  NICE also provided grant support for the
promote a robust network and an integrated ecosystem  NICE 2015 Conference and Expo, the inaugural National
of  cybersecurity  education,  training,  and  workforce  Cybersecurity K-12 Cybersecurity Education Conference, the
development.
Centers of Academic Excellence (CAE) Community Meeting,
and the NICE Challenge Project.
| CSD  | is  leading  | the  | NICE  program,  | working  | from  |     |     |     |     |     |     |     |
| ---- | ------------ | ---- | --------------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
the  strengths  and  energy  of  more  than  twenty  federal  In FY 2016, the NICE Program Office will continue to
departments  and  agencies,  leveraging  each  of  their  promote  the  coordination  of  existing  and  future  cyber-
relationships with academia and industry sectors to ensure  security education, training, and workforce activities. The
2 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Sixth annual NICE Workshop will take place on November During FY 2015, the CSRC has been updated on a daily
3-4, 2015 in San Diego, CA (see http://csrc.nist.gov/nice/ basis with new information, such as the publication of draft
events.html). NIST will also identify opportunities to extend and final documents (FIPS, SPs, NISTIRs and ITL Bulletins)
and integrate the NICE focus on the cybersecurity workforce, and various project and program webpage updates.
education, and training within NIST Special Publications An improvement made to the CSRC homepage was to
and informational reports, while promoting the value of the add a new section titled “Draft Publications Request for
National Cybersecurity Workforce Framework (NCWF) and Comments Deadlines”. This section will help our customers
the forthcoming DOD Cyberspace Workforce Strategy as that are interested in submitting comments to our technical
resources that address cybersecurity workforce needs. publications find the deadline dates for submitting
comments to certain publications.
For More Information, See:
The CSRC website is expected to be redesigned during
http://www.nist.gov/nice/
FY 2016 to provide an improved and flexible user interface.
CONTACTS: For More Information, See:
http://csrc.nist.gov
Mr. Rodney Peterson Ms. Danielle Santos
NICE Director NICE Program Manager
(301) 975-8897 (301) 975-5048 CONTACTS:
rodney@nist.gov danielle.santos@nist.gov
Questions regarding the CSRC website can be sent to the
CSRC Webmasters at: webmaster-csrc@nist.gov.
Computer Security Resource Center
Mr. Patrick O’Reilly Ms. Nicole Keller
(CSRC) (301) 975-4751 (301) 975-3648
The CSRC, Computer Security Division’s (CSD) website, patrick.oreilly@nist.gov nicole.keller@nist.gov
is one of the most visited websites at NIST. CSRC encourages
the broad sharing of information security tools and practices, (Editor Note: Ms. Judy Barnard was part of this project
provides a resource for information security standards team until her recent retirement.)
and guidelines, and identifies and links key security web
resources to support industry and government users. CSRC
Federal Computer Security Managers’
is an integral component of all of the work that CSD conducts
(FCSM) Forum
and produces. It is CSD’s repository for anyone wanting to
The Federal Computer Security Managers’ (FCSM)
access these documents and other valuable security-related
Forum is sponsored by NIST to promote the sharing of
information. During FY 2015, CSRC had more than 5.9 million
security-related information among federal agencies. The
page views and downloads.
Forum, which serves more than 1,100 members, strives to
CSRC is the primary gateway for gaining access to NIST
provide an ongoing opportunity for managers of federal
computer security publications, standards, and guidelines,
information security programs to exchange information
and serves as a vital link to CSD’s customers. Publications
security materials in a timely manner, build upon the
are organized to help users locate relevant information
experiences of other programs, and reduce possible
quickly and are arranged by topic, relevant security control
duplication of effort. It provides a mechanism for NIST to
family, and legal requirements.
share information directly with federal agency information
In addition to CSRC, CSD maintains a publication security managers in fulfillment of NIST’s leadership
announcement mailing list. This free e mail list notifies mandate under FISMA. It assists NIST in establishing
subscribers about publications that have been posted to the and maintaining relationships with other individuals or
CSRC website, along with announcing new CSD-sponsored organizations that are actively addressing information
events and important news and/or announcements. The security issues within the Federal Government. CSD’s Patricia
e-mail list is a valuable tool for more than 59,000 subscribers Toth serves as the Chairperson and Peggy Himes serves as
from the Federal Government, industry, academia, and the Secretariat.
individuals with a personal interest in IT security worldwide. The Forum maintains an extensive email subscription
Individuals who are interested in subscribing to this list service. Participation in the service is only open to Federal
should visit http://csrc.nist.gov/publications/subscribe.html Government employees who participate in the management
for more information. of their organization’s information system security
2 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

program. The Forum also holds bimonthly meetings and an Booth, NIST;
annual two-day conference to discuss current issues and
• Department of Transportation (DOT) Security Program
developments of interest to those responsible for protecting
Management Subcommittee’s Information Assurance
sensitive (unclassified) federal systems. Events are open to
Policy Working Group (IAPWG), Kevin Sanchez-Cherry,
federal employees and their designated support contractors.
DOT;
Topics of discussion at FCSM meetings in FY 2015
• Speak Out - Daniel Wood, Treasury – Term & Topic: PKI
included briefings from various federal agencies on the
Landscape, Pat Toth, NIST – Request for topics for FY
Supply Chain, the Einstein 3 Accelerated (E3A) Reporting
2016 meetings;
Tool, implementing privacy controls from Appendix J in
SP 800-53, the U.S. Government Configuration Baseline • Information Technology (IT) Policy Initiatives Panel,
(USGCB), the National Cybersecurity Center for Excellence Adam Sedgewick, NIST, William Fisher and Tim Mc-
(NCCoE), and SP 800-88 Revision 1, Guidelines for Media Bride, National Cybersecurity Center of Excellence
Sanitation. (NCCoE); Mike Garcia, National Strategy for Trusted
This year’s annual two-day offsite was held at NIST on Identities in Cyberspace (NSTIC);
August 26-27, 2015. Presentations included current tech-
• U.S. Census Bureau Risk Management Program Imple-
nical, operational and management information systems
mentation, Jaime Lynn Noble, U.S. Census Bureau; and
security topics and updates on the information system
• DHS Continuous Diagnostics and Mitigation (CDM)
security activities of OMB, GAO, the National Aeronautics
Program Overview, Martin Stanley, DHS.
and Space Administration (NASA), the National Archives
and Records Administration (NARA), the Federal Aviation The Forum plays a valuable role in helping NIST and
Administration (FAA), the U.S. Census Bureau, DHS, and NIST. other federal agencies to develop and maintain a strong,
Most presentations are available on the FCSM’s website (see proactive stance in the identification and resolution of new
http://csrc.nist.gov/groups/SMA/forum/), under “Events.” strategic and tactical IT security issues as they emerge. The
number of members on the email list has grown steadily
• NIST Computer Security Division Update, Matthew and provides a valuable resource for federal security
Scholl, NIST; program managers. To join, email your name, affiliation,
phone number, title, and confirmation that you are a federal
• How to Best Protect Against Future Cyber Incidents,
employee to sec-forum@nist.gov; only .gov and .mil email
Trevor H. Rudolph, OMB;
addresses are accepted in the list serve.
• Implementing TIC E3A in Government and Using the
XLA Threat Reduction and Correlation Tool (xTractTM), For More Information, See:
Sandra Paul-Blanc, NARA, and Philip Kulp, XLA; http://csrc.nist.gov/groups/SMA/forum/
• GAO Information Security Update, Gregory C. Wilshu-
sen, GAO; CONTACTS:
• NIST SP 800-163, Vetting the Security of Mobile Appli- Ms. Patricia Toth Ms. Peggy Himes
cations, Steve Quirolgico, NIST; Chair Administration
(301) 975-5140 (301) 975-2489
• Using Risk Management to Improve Privacy in Informa-
ptoth@nist.gov peggy.himes@nist.gov
tion Systems, Ellen Nadeau, NIST;
• Framework for Improving Critical Infrastructure Cyber-
security, Matthew Barrett, NIST; Federal Information Systems Security
Educators’ Association (FISSEA)
• Mobile Application Security and PIV Derived Creden-
The Federal Information Systems Security Educators’
tials, Jane Maples, NASA and Peter Cauwels, NASA;
Association (FISSEA), founded in 1987, is an organization
• Rethinking Cybersecurity from the Inside Out: An En-
hosted by NIST for information system security professionals
gineering and Life Cycle-Based Approach for Building
to assist federal agencies in meeting their information
Trustworthy Resilient Systems, Ron Ross, NIST Fellow;
system’s security awareness, training, and education
• How FAA Required 50,000+ People to Use PIV Cards in responsibilities. FISSEA strives to elevate the general level
2 Months, Myles Roberts, FAA; of information system security knowledge for the Federal
Government and the federal workforce. It also seeks to assist
• Cloud Assessments, John Connor, NIST;
the professional development of its members.
• The National Vulnerability Database (NVD), Harold
3 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

| FISSEA  | membership  |     | is  | open  to  | information  |     | system  |     |     |     |     |
| ------- | ----------- | --- | --- | --------- | ------------ | --- | ------- | --- | --- | --- | --- |
security professionals, professional trainers and educators,
and managers responsible for information system security
training programs in federal agencies, as well as contractors
| of  these    | agencies      |      | and  faculty  | members        |              | of  accredited   |            |     |     |     |     |
| ------------ | ------------- | ---- | ------------- | -------------- | ------------ | ---------------- | ---------- | --- | --- | --- | --- |
| educational  | institutions  |      | who           | are  involved  |              | in  information  |            |     |     |     |     |
| security     | training      | and  | education.    |                | Willingness  |                  | to  share  |     |     |     |     |
products, information, and experiences is all that is required
| to  become  | a   | FISSEA  | member.  | A   | working  | group  | meets  |     |     |     |     |
| ----------- | --- | ------- | -------- | --- | -------- | ------ | ------ | --- | --- | --- | --- |
monthly to administer business activities.
| FISSEA        | maintains  |            | a  website,  |     | a  mailing  |           | list,  and  |     |     |     |     |
| ------------- | ---------- | ---------- | ------------ | --- | ----------- | --------- | ----------- | --- | --- | --- | --- |
| participates  | in         | a  social  | networking   |     | site  as    | a  means  | of          |     |     |     |     |
communication for its members. CSD assists FISSEA with
Figure 6: Pecha-Kucha Participants (left to right):
its operations by providing staff support for several of its
Art Chantker, Potomac Forum, Frank Cicio Jr, iQ4
activities and by being FISSEA’s host agency.
Corporation, Sandy Toner, ICF International, and
The 28th Annual FISSEA Conference occurred March 24- Louis Numkin, FISSEA Life Member
25, 2015 at NIST. The FISSEA audience included managers
FISSEA conferences include Pecha Kucha (Lightning
| responsible  | for  | information  |     | systems  | security  | awareness,  |     |     |     |     |     |
| ------------ | ---- | ------------ | --- | -------- | --------- | ----------- | --- | --- | --- | --- | --- |
training, certifications, workforce identification, compliance,  Rounds) sessions. Speakers have 6 minutes 40 seconds for
etc. in federal agencies; contractors providing awareness  their presentations, and the challenge is in limiting one’s
talk to only 20 slides. It’s challenging to do as a speaker and
and training support; and faculty members of accredited
educational  institutions  who  are  involved  in  information  quite fun for the audience to watch, so the Pecha Kucha fast-
paced talks proved to be entertaining and educational.
security training and education.  Pat Toth, Peggy Himes,
and Judy Barnard (NIST), as well as Gretchen Morris (DB
The FISSEA Educator of the Year Award was established
Consulting/NASA),  and  other  members  of  the  FISSEA  to recognize and honor a contemporary who is making
Working Group, were integral to the effort to support the  special  efforts  to  create,  build,  manage,  or  inspire  an
conference.
|     |     |     |     |     |     |     |     | information  | systems  security  | awareness,  | training,  or  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------ | ----------- | -------------- |
education program.  Sam Maroon presented the FISSEA
| This  | year’s  | theme  | was  | “Changes,  | Challenges,  |     | and  |     |     |     |     |
| ----- | ------- | ------ | ---- | ---------- | ------------ | --- | ---- | --- | --- | --- | --- |
Collaborations: Effective Cybersecurity Training”. Attendees  2014 Educator of the Year posthumously to Shon Harris of
Logical Security. Mr. Maroon shared Ms. Harris’ contributions
gained new techniques for developing/conducting training,
to the cybersecurity education industry by characterizing
cost-effective practices, workforce development, and free
resources and contacts.  Over 200 cybersecurity training  her contributions in three ways: as a writer, a trainer, and a
thought leader. Ms. Harris’ friends and colleagues, Michael
professionals attended the two-day conference.
Lester and Hamid Dehghan accepted the plaque on her
| NIST’s  | Information  |     | Technology  |     | Laboratory  |     | (ITL)  |     |     |     |     |
| ------- | ------------ | --- | ----------- | --- | ----------- | --- | ------ | --- | --- | --- | --- |
behalf.
Director, Charles Romine, welcomed attendees to the event.
| We  were                                                | honored  | to  | have  | Dr.  Neil  | Grunberg,  |     | Professor  |     |     |     |     |
| ------------------------------------------------------- | -------- | --- | ----- | ---------- | ---------- | --- | ---------- | --- | --- | --- | --- |
| of Military and Emergency Medicine, Uniformed Services  |          |     |       |            |            |     |            |     |     |     |     |

University, who provided an inspiring keynote presentation,
| “Information Security System Educators Must be Leaders.”  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

His talk addressed the leadership and communication skills
| needed by Cybersecurity Educators |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Presenters represented NIST, DHS, the Department of

State (DoS), the National Security Agency (NSA), private

industry, and academia. Attendees had an opportunity to

visit 16 vendors and federal agencies on the second day to

share and tell about their specific awareness and training

programs.

3 1
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

|     |     |     |  Motivational   |     | Item  | Winner:  | Cindy  | Dailey,  | Geisinger  |
| --- | --- | --- | --------------- | --- | ----- | -------- | ------ | -------- | ---------- |
|     |     |     | Health System;  |     |       |          |        |          |            |

 Newsletter Winner: Brenda L. Ellis, NASA; and

|     |     |     |              |     |           |     | Winner:  | Jennifer  | Young,  |
| --- | --- | --- | ------------ | --- | --------- | --- | -------- | --------- | ------- |
|     |     |     |  Role-Based  |     | Training  |     |          |           |         |
Communication Security Establishment.
Another bonus of attending the 2015 FISSEA conference
was networking. The conference continues to be a valuable
|     |     |     | forum          | for  individuals  |                | from          | government,        |            | industry,  and  |
| --- | --- | --- | -------------- | ----------------- | -------------- | ------------- | ------------------ | ---------- | --------------- |
|     |     |     | academia       | who               | are  involved  |               | with  information  |            | systems/        |
|     |     |     | cybersecurity  |                   | workforce      | development.  |                    | Attendees  | gain            |
insights regarding information security awareness, training,
education, certification, and professionalization. Attendees
Figure 7: Friends and colleagues accepting the   also learn of ongoing and planned training and education
FISSEA Educator of the Year on behalf of Ms. Harris programs and cybersecurity initiatives.  It provides NIST
the opportunity to provide assistance to departments and
| Other  traditional  | FISSEA  conference  | events  include  |     |     |     |     |     |     |     |
| ------------------- | ------------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
agencies as they work to meet their FISMA responsibilities.
announcing the winners of the FISSEA security contest. The
|     |     |     | The  FISSEA  |     | website  | provides  | links  | to  the  | Conference  |
| --- | --- | --- | ------------ | --- | -------- | --------- | ------ | -------- | ----------- |
FISSEA Security Awareness, Training & Education Contest
Program, and also links to presentations (http://csrc.nist.
| includes five categories from one of FISSEA’s three key  |     |     | gov/fissea).  |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
areas of Awareness, Training, and Education.  A winner is
The next conference will be held at NIST on March 15-16,
selected from each category and awarded a certificate. The
2016.
categories include: (1) an awareness poster; (2) motivational
item (e.g., trinkets, pens, stress relief items and t-shirts); (3)  For More Information, See:
an awareness website; (4) an awareness newsletter; and (5)  http://csrc.nist.gov/fissea
role-based training & education.
2015 FISSEA Awareness, Training, and Education Contest  CONTACTS:
Winners
|     |     |     | Ms. Patricia Toth   |     |     | Ms. Peggy Himes  |     |     |     |
| --- | --- | --- | ------------------- | --- | --- | ---------------- | --- | --- | --- |
Awarded Certificates at the Conference (selected by an
|     |     |     | (301) 975-5140  |     |     | (301) 975-2489  |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --------------- | --- | --- | --- |
impartial judging committee prior to the conference):
|     |     |     | patricia.toth@nist.gov  |     |     | peggy.himes@nist.gov |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | -------------------- | --- | --- | --- |
 Poster Winner: Kelly Wright – Veteran Affairs (VA) IT
Workforce Development;
Information Security and Privacy
 Website  Winner: NASA  IT  Security  Awareness  and  Advisory Board (ISPAB)
Training Center Team; Since the inception of this Advisory Board in 1987, the
 Motivational Item Winner: Jane Moser – Employment  Information Security and Privacy Advisory Board (ISPAB)
has successfully renewed its charter with proper authority
and Social Development Canada (ESDC);
every two years. The Board plays a central and unique role
 Newsletter Winner: Wendy Andrews, Robert Collins,
in providing the government with expert advice concerning
Arnold Ginn, and CDR Steven Miller – Indian Health
|     |     |     | information  | security  | and  | privacy  | issues  | that  | may  affect  |
| --- | --- | --- | ------------ | --------- | ---- | -------- | ------- | ----- | ------------ |
Service; and
federal information systems. Title III of the E-Government
 Role-Based Training Winner: Jane Moser –ESDC. Act of 2002 reaffirmed the need for this Board by giving it
Peer’s  Choice  Awards  (selected  by  peers  during  the  an additional responsibility: to thoroughly review all of the
conference): proposed information technology standards and guidelines
developed under Section 20 of the National Institute of
 Poster Winner: Kimberly Conway, Sara Fitzgerald, Sean
Standards and Technology Act (15 U.S. Code (U.S.C.) 278g-
Hanion, Dave Stapleton, and Steven VanBrackle, FDA;
3), as amended.
 Website Winner: Kimberly Conway, Sara Fitzgerald,
The ISPAB is a federal advisory committee with specific
Sean Hanion, Dave Stapleton, and Steven VanBrackle,
|     |     |     | statutory  | objectives  |     | to  identify  | emerging  |     | managerial,  |
| --- | --- | --- | ---------- | ----------- | --- | ------------- | --------- | --- | ------------ |
FDA;
3 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

technical, administrative, and physical safeguard issues The 15 U.S.C. 278g-4 charter stipulates that Board
related to information security and privacy. The Board members be selected from three main categories, with
was originally created by the Computer Security Act of each category providing four members. Category 1 includes
1987 (P.L. 100-235) as the Computer System Security and members from outside the Federal Government who are
Privacy Advisory Board (CSSPAB) within the Department eminent in the information technology industry, at least
of Commerce. The CSSPAB was chartered in May 1988 in one of whom is a representative of small or medium-sized
accordance with the Federal Advisory Committee Act, companies in such industries. Category 2 also includes
as amended. The 2002 FISMA legislation amended the members from outside the Federal Government who are
statutory authority of the Board and provided its current eminent in the field of information technology or related
name. disciplines, but who are not employed by or representative
of a producer of information. Category 3 includes those from
The duties of the Board, as stipulated in FISMA, include:
the Federal Government who are experienced in information
• Identification of emerging managerial, technical, ad-
system management, including those with experience in
ministrative, and physical safeguard issues relative to
information security and privacy, at least one of whom should
information security and privacy;
be from the National Security Agency. The categorization
• Advising NIST and the Director of the Office of Man- of Board members is intended to meet ISPAB’s statutory
agement and Budget on information security and objectives. Federal members bring a detailed understanding
privacy issues pertaining to Federal Government of the federal processing environment; industry brings
information systems (including the thorough review of concerns and experiences regarding product development
proposed standards and guidelines developed under 15 and market formation, while private computer security
U.S.C. 278g-3 - Computer Standards Program); and experts are able to bring their experiences of commercial
cost-effective security measures into Board discussion.
• Annually reporting its findings to the Secretary of
Commerce, the Director of the Office of Management Dr. Peter Weinberger is currently the Chair of ISPAB.
and Budget, the Director of NSA, and the appropriate Dr. Weinberger, a Computer Scientist from Google, joined
committees of Congress. the Board in 2008 and assumed the responsibilities of the
Chair in January 2015. He is also a Co-Chair of a National
Congress indicated the long-term need for the Board by
Academies study on fundamental work in cybersecurity, and
setting the term of Board members to four years. The charter
a member of the National Academies study on Presidential
requires that the NIST Director appoint the Chairperson and
Policy Directive (PPD) 28, Signals Intelligence Activities.
all twelve members of the Board. They are selected for their
He is well supported by the following Board members (see
preeminence in the information technology industry or
http://csrc.nist.gov/groups/SMA/ispab/membership.html):
related disciplines.
Figure 8: From Left to Right – Annie Sokol (Designated Federal Officer, CSD, NIST), Greg Garcia, Ed Roback, Toby Levin,
Jeffrey Greene, John Centafont, Dr. Kevin Fu, Dr. Peter Weinberger (Chair, ISPAB), Matt Scholl (Chief, CSD, NIST)
Members not included in this picture: Chris Boyer, Dr. Ana Anton, David Cullinane, Gale Stone, and J. Daniel Toler
3 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

• Ana (Annie) Antón, Professor and Chair, School of • FISMA – Continuous Diagnostics and Mitigation (CDM)
Interactive Computing, Georgia Institute of Technology; and Federal Risk and Authorization Management Pro-
gram (FedRAMP);
• Christopher Boyer, Assistant Vice President, Public
Policy, AT&T; • CDM – Communications Security, Reliability and In-
teroperability Council (CSRIC), Trusted Internet Con-
• John R. Centafont, NSA Information Assurance and
nection (TIC);
Cyber Defense;
• Key ESCROW – history and lessons learned
• David Cullinane, CEO, TruStar, LLC;
• Cybersecurity; and
• Dr. Kevin Fu, Associate Professor, The University of
Michigan; • Updates of other critical NIST publications.
• Gregory Garcia, Executive Vice President, McBee Stra- In aligning with the work-plan focus areas, the Board
tegic; expanded its work to include the following:
• Jeffrey Greene, Esq., Director, Government Affairs, • The Privacy and Civil Liberties Oversight Board
North America & Senior Policy Counsel, Senior Policy (PCLOB);
Counsel, Cybersecurity and Identity, Symantec Corpo-
• OMB Circular A130 Revised;
ration;
• Acquisition, Supply Chain Security, and Open Source
• Toby Levin, Retired (formerly Senior Advisor and Direc-
trustworthy software;
tor of Privacy Policy, U.S. DHS);
• Mobile Devices and the Protection of Sensitive Informa-
• Edward Roback, Associate Chief Information Officer for
tion;
Cyber Security, U.S. Department of Treasury; and
• Intelligence and communication technologies;
• Gale Stone, Deputy Assistant Inspector General for
• Cryptography and NIST Cryptographic standards
Audit, Social Security Administration (SSA).
processes;
During FY 2014-2015, ISPAB held three meetings, all in
• The NIST Cybersecurity Framework;
Washington D.C:
• Safeguarding Health Information;
• October 22-24, 2014;
• The Controlled Unclassified Information (CUI) Program;
• February 11-13, 2015; and
• Breach and breach reporting;
• June 10-12, 2015.
• The Federal Information Security Management Act
In keeping with previous practices at the first meeting
(FISMA);
of each fiscal year, the Board established a work plan for
FY 2015 at the meeting in October 2014. The resulting plan • Emerging Technologies: Cloud Computing, Big Data,
included the following areas of focus: the Internet of Things, Cyber Physical Systems, Smart
cities, Drones and Unmanned Aircraft Systems, Medical
• Cryptography, and specifically NIST R&D;
Devices, Transportation Sector and Vehicle-to-Vehicle
• Federally funded Research and Development Centers
Communication, and relating impacts on security and
(FFRDCs) – internally, externally and control balance;
privacy;
• Metrics – success measure for security and privacy;
• The National Strategy for Trusted Identities in Cyber-
• Trust in NIST (accountability and success); space (NSTIC);
• Quantum mechanics; • The National Cybersecurity Center of Excellence (NC-
CoE); and
• Identity management (Biometrics);
• The realignment of the Information Technology Labora-
• Privacy technology – implementation methodology;
tory.
• Medical devices – security, privacy and safety, Health-
The presenters at each Board meeting were leaders
care IT Security;
and experts representing private industry, academia, federal
agency Chief Information Officers (CIOs), Inspector Generals
(IGs) and Chief Information Security Officers (CISOs).
3 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Copies of the current list of members and their threats, vulnerabilities, and corresponding protective tools
biographies, the Board’s charter and past Board activities and techniques, with a special emphasis on information that
are located at http://csrc.nist.gov/groups/SMA/ispab. small business personnel can apply directly.
Information on ISPAB Meetings is published in Federal
In FY 2015, six SMB outreach workshops were provided
Register Notices at least 16 days prior to the meeting. Those
in Reno, Nevada; Fresno, California; Modesto, California;
interested in receiving meeting notices and other notices
Fairmont, West Virginia; Pittsburgh, Pennsylvania; and
relating to NIST work in information security and privacy
McHenry, Maryland. Additionally, the SMB Cybersecurity
may email their name, affiliation, and address to Annie Sokol
Outreach Program was briefed to the InfraGard National
at the address below.
Congress.
For More Information, See:
In collaboration with the SBA and the FBI, planning
http://csrc.nist.gov/groups/SMA/ispab is underway to identify locations and plan cybersecurity
workshops in FY 2016.
CONTACT:
For More Information, See:
Ms. Annie Sokol http://csrc.nist.gov/groups/SMA/sbc/
Designated Federal Officer (DFO), ISPAB
(301) 975-2006 CONTACT:
annie.sokol@nist.gov
Ms. Patricia Toth
301-975-5140
Small and Medium Size Business (SMB)
patricia.toth@nist.gov
Cybersecurity Workshop Outreach
Small business owners face a broad range of informa-
tion security issues. A computer failure or system breach
could jeopardize the company’s reputation and may result
in significant damage and recovery cost, or going out
of business. The small business owner who recognizes
the threat of computer crime and takes steps to deter
inappropriate activities is less likely to become a victim.
The U.S. Small Business Administration (SBA) reports
that over 27 million U.S. companies - more than 99 percent of
all U.S. businesses - are SMBs of 500 employees or fewer (see
http://www.sba.gov/sites/default/files/allprofiles12.pdf).
While the threats to individual SMBs may not be significantly
different from those facing larger organizations, an SMB
frequently has fewer resources available to protect systems,
detect attacks, or respond to security issues. A vulnerability
common to a large percentage of SMBs could pose a threat
to the nation’s information infrastructure and economic
base.
To help address information security risk, these busi-
nesses require assistance with the identification of security
mechanisms and with practical, cost-effective training.
Training helps SMB’s use their limited resources most
effectively to address relevant and serious threats. In
response to this need, NIST, the SBA, and the Federal Bureau
of Investigation (FBI) InfraGard program co-sponsor a series
of cybersecurity training workshops for small businesses.
These workshops provide an overview of cybersecurity
3 5
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

CRYPTOGRAPHIC STANDARDS CONTACT:
PROGRAM
Ms. Shu-jen Chang
(301) 975-2940
shu-jen.chang@nist.gov
Hash Algorithms and the Secure Hash
Algorithm-3 (SHA-3) Standard (FIPS
202) Random Number Generation (RNG)
NIST opened a public competition in 2007 to develop Random numbers are required for the security for many
a new cryptographic hash algorithm, SHA-3, to augment cryptographic algorithms. For example, random numbers
the hash algorithms specified in FIPS 180-4, Secure Hash are used to generate the keys needed for encryption and
Standard (SHS). The competition ended on October 2, digital signature applications.
2012 when NIST announced the selection of Keccak as the In March 2007, CSD published SP 800-90,
winning algorithm for standardization as the new SHA- Recommendation for Random Number Generation Using
3 Standard. NIST consulted with the Keccak designers Deterministic Random Bit Generators, which contained four
and the cryptographic community, and developed a SHA- deterministic random bit generator (DRBG) mechanisms,
3 standardization plan that was presented at numerous two based on hash functions, one based on the use of block
cryptography conferences and posted at the NIST hash cipher algorithms and one based on the use of elliptic curves.
website, indicated below, for public feedback. This recommendation was revised as SP 800-90A in January
NIST announced Draft FIPS 202, SHA-3 Standard: 2012 to include additional capabilities and in June 2015 to
Permutation-Based Hash and Extendable-Output Functions, remove the DRBG based on the use of elliptic curves, i.e.,
in the Federal Register (79 FR 30549) on May 28, 2014 the DUAL_EC_DRBG, since its security has been in question.
and requested comments (see https://federalregister. Two additional documents (SP 800-90B,
gov/a/2014-12336). The announcement also proposed a Recommendation for the Entropy Sources Used for Random
revision of the Applicability Clause of the Announcement Bit Generation, and SP 800-90C, Recommendation for
Section of FIPS 180-4, Secure Hash Standard, to allow the Random Bit Generator (RBG) Constructions) are under
use of hash functions specified in either FIPS 180-4 or FIPS development, and the initial drafts were made available for
202, modifying the original mandate to use only the hash public comment in 2012.
functions specified in FIPS 180-4. The other sections of FIPS
SP 800-90B addresses the development and testing of
180-4 remain unchanged. A ninety-day public comment
entropy sources, including descriptions of the tests for NIST’s
period was provided, which ended on August 26, 2014.
Cryptographic Algorithm Validation Program to validate
NIST received seven comments on Draft FIPS 202 and candidate entropy sources. An entropy source depends on
one comment on the Draft Revision of the Applicability a noise source, which is the root of security for the entropy
Clause of FIPS 180-4. All comments received are posted source. During FY 2015, the CTG developed and tested
at the NIST hash website. None of the comments opposed additional methods for estimating the amount of entropy
the adoption of the SHA-3 Standard or the revision of the per noise-source output. An overview of the methodology
Applicability Clause of FIPS 180-4. NIST also received public and preliminary results of new estimators, called predictors,
feedback at the 2014 SHA-3 Workshop and afterwards. All were presented at ShmooCon in the talk “How Random is
of the comments were carefully reviewed, and changes were Your RNG?” Further details and results were published in the
made to FIPS 202, where appropriate. NIST made additional paper “Predictive Models for Min-Entropy Estimation” at the
editorial changes to improve FIPS 202. Cryptographic Hardware and Embedded Systems (CHES
FIPS 202, SHA-3 Standard: Permutation-Based Hash and 2015) workshop. A new draft of SP 800-90B will be provided
Extendable-Output Functions, and the revised Applicability for another public comment period in early FY 2016.
Clause of FIPS 180-4 were approved by the Secretary of SP 800-90C provides basic guidance on the construc-
Commerce and announced in the Federal Register (80 tion of RBGs from the entropy sources validated against the
FR 46543) on August 5, 2015 (see https://federalregister. requirements of SP 800-90B and the DRBG mechanisms
gov/a/2015-19181). FIPS 202 and FIPS 180-4 are available at: of SP 800-90A. The CTG plans to provide a new version of
http://csrc.nist.gov/publications/PubsFIPS.html. this document for public comment prior to the end of the SP
For More Information, See: 800-90B public-comment period.
http://csrc.nist.gov/groups/ST/hash/sha-3/sha-3_
standardization.html
3 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

A public workshop is planned for FY 2016 to discuss SP Recommendation for Block Cipher Modes of Operation:
800-90B and 90C. Galois/Counter Mode (GCM) and GMAC; and 2) to revisit
the combinations of encryption and authentication that are
For More Information, See:
approved in SP 800-38F, Recommendation for Block Cipher
http://csrc.nist.gov/groups/ST/toolkit/rng/
Modes of Operation: Methods for Key Wrapping.
For More Information, See:
CONTACTS:
http://csrc.nist.gov/groups/ST/toolkit/BCM/
Ms. Elaine Barker Mr. John Kelsey
(301) 975-2911 (301) 975-5101
CONTACT:
elaine.barker@nist.gov john.kelsey@nist.gov
Dr. Morris Dworkin
Dr. Meltem Sönmez Turan Dr. Kerry McKay (301) 975-2354
(301) 975-4391 (301) 975-4969 morris.dworkin@nist.gov
meltem.turan@nist.gov kerry.mckay@nist.gov
Key Management
Block Cipher Modes of Operation Key management is required for applying numerous
The engine for many of the techniques in NIST’s cryptographic technologies and is considered the most
cryptographic toolkit is a block cipher algorithm, such as critical aspect associated with the use of cryptography. CSD
the Advanced Encryption Standard (AES) algorithm or the began to provide guidance in managing the keys used for
Triple Data Encryption Algorithm (TDEA). A block cipher cryptographic applications in the late 1990s to early 2000s.
transforms some fixed-length binary data (i.e., a “block”) Several guidance and recommendation documents have
into seemingly random data of the same length. The been and continue to be developed in the form of NIST
transformation is determined by the choice of some secret Special Publications (SP), which have been periodically
data called the “key.” The same key is used to reverse the updated to address new algorithms and handling procedures.
transformation and recover the original block of data. A These documents are coordinated with federal agencies and
cryptographic technique that is constructed from a block with the cryptographic community, including national and
cipher is called a mode of operation. Several modes of international organizations, industry, and academia. During
operation have been specified in the SP 800-38 series of FY 2015, the following publications were either created or
publications. revised.
The CTG has nearly completed the development of two SP 800-57, Recommendation for Key Management,
AES modes of operation for format-preserving encryption Part 3: Application-Specific Key Management Guidance,
(FPE), based on proposals that were submitted from the was first published in 2009. This document addresses the
private sector. A format can be a sequence of decimal digits, key-management issues of currently available cryptographic
such as a credit card number or a social security number; mechanisms, including the use of Public Key Infrastructures
formats can also be defined for other sets of characters (PKI) and several commonly used security protocols and
besides decimal digits. FPE is expected to facilitate the applications. A revision of this document was provided for
retrofitting of encryption to existing applications. For public comment in May 2014 that updated the guidance
example, FPE could be applied to database systems, so provided in the 2009 version, included an additional
that sensitive data could be targeted for encryption without section on the Secure Shell (SSH) protocol, and substituted
disrupting the underlying data fields/pathways. a reference to SP 800-52, Revision 1, Guidelines for the
Selection, Configuration, and Use of Transport Layer
The two modes of operation for FPE, called FF1 and
Security (TLS) Implementations, for the TLS section. After
FF3, will be specified in Special Publication 800-38G,
the comment period, the draft revision was revised, and
Recommendation for Block Cipher Modes of Operation:
published in January 2015.
Methods for Format-Preserving Encryption, which will be
completed in FY 2016. SP 800-57, Recommendation for Key Management, Part
1: General, was first published in 2005, and later revised in
In the coming year, the CTG plans to consider technical
2007 and 2012. Another revision was provided for public
changes to two other Special Publications in the 800-38
comment in FY 2015 that includes information on and
series. In particular, the CTG plans: 1) to solicit public comment
references to recent work performed by CSD; removed
on requirements for the generation of non-repeating IVs
references to the Dual_EC_DRBG, which was removed
for the Galois/Counter Mode, specified in SP 800-38D,
37
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

from SP 800-90A, Recommendation for Random Number For More Information, See:
Generation Using Deterministic Random Bit Generators;
http://csrc.nist.gov/groups/ST/key_mgmt
revised the security-strength tables; and revised the key-
state discussion to provide more clarification. The revision
was provided for public comment in September 2015 and CONTACTS:
should be completed in early FY 2016.
Ms. Elaine Barker Dr. Dustin Moody
SP 800-131A, Transitions: Recommendation for (301) 975-2911 (301) 975-8136
Transitioning the Use of Cryptographic Algorithms and elaine.barker@nist.gov dustin.moody@nist.gov
Key Lengths, was originally published in January 2011. This
document provides specific guidance for transitions to Dr. Lily Chen Mr. Ray Perlner
the use of stronger cryptographic keys and more robust (301) 975-6974 (301) 975-3357
algorithms. An update of SP 800-131A was provided lily.chen@nist.gov ray.perlner@nist.gov
for public comment and completed in November 2015.
This update removes approval for the Dual_EC_DRBG, Mr. Quynh Dang
deprecates the use of non-approved key-establishment (301) 975-3610
schemes, disallows the use of non-approved key-wrapping quynh.dang@nist.gov
methods after 2017, and indicates that the use of the SHA-3
family of hash functions as acceptable.
Transport Layer Security
SP 800-152, A Profile for U.S. Federal Cryptographic
SP 800-52, Guidelines for the Selection, Configuration,
Key Management Systems (CKMS), provides guidance
and Use of Transport Layer Security (TLS) Implementa-
on the CKMSs to be used by the Federal Government.
tions, provides recommendations regarding TLS server and
This document provides refinements of the requirements
client implementations. TLS is a widely used cryptographic
for CKMS designers that are specified in SP 800-130, A
protocol that provides communication security for a variety
Framework for Designing Cryptographic Key Management
of network applications, such as email, e-commerce, and
Systems. SP 800-152 also provides requirements and
healthcare.
recommendations for the service providers of CKMSs used
SP 800-52 was first published in 2005, and SP 800-52
by federal agencies and their contractors, as well as guidance
Revision 1 was published in April 2014. Since the revision, CTG
for the federal agencies in selecting a CKMS that supports
has been following developments in TLS implementations,
the security and management policies of those agencies. A
including updates and attacks. In FY 2016, a second revision
draft of this document was provided for public comment in
will be published that considers these developments.
FY 2013, and a workshop was held in March 2013 to discuss
This second revision will be a minor update to SP 800-52
the draft. A second draft was provided for comment in FY
Revision 1.
2015, and a final version addressing the received comments
was published in October 2015. The Internet Engineering Task Force (IETF) is actively
developing extensions that can be used to add functionality
A new NIST publication is under development
to TLS. CSD will continue to review updates and additions to
that provides guidance on the security strength of a
the TLS protocol in FY 2016.
cryptographic key that is used to protect data (i.e., a data-
protection key), given the manner in which the key was
CONTACTS:
generated and handled. This document, SP 800-158, Key
Management: Obtaining a Targeted Security Strength,
Dr. Lily Chen Dr. Kerry McKay
involves a considerable amount of new research, since it
(301) 975-6974 (301) 975-4969
is an area that has not been fully addressed to date. This
lily.chen@nist.gov kerry.mckay@nist.gov
publication will be available for public comment in FY 2016.
Additional key-management work to be conducted in FY
Elliptic Curve Cryptography
2016 includes revision(s) to SP 800-56A, Recommendation
Elliptic curve cryptography is critical to the adoption
for Pair-Wise Key-Establishment Schemes Using Discrete
of strong cryptography as we migrate to higher security
Logarithm Cryptography, and SP 800-56B, Recommenda-
strengths. NIST has standardized elliptic curve cryptography
tion for Pair-Wise Key-Establishment Schemes Using Integer
for digital signature algorithms in FIPS 186 and for key
Factorization Cryptography, to allow the use of larger key
establishment schemes in SP 800-56A.
sizes.
3 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

In FIPS 186-4, NIST recommends fifteen elliptic curves secure against both quantum and classical computers, as
of varying security levels for use in these elliptic curve well as the impact that such post-quantum algorithms will
cryptographic standards. However, the provenance of the have on current protocols and security infrastructures.
curves is not fully specified in the standard, leading to recent
In FY 2015, NIST researchers held regular seminars. The
public concerns that there could be a hidden weakness in
presentation topics included the latest published results; a
these curves. NIST is not aware of any vulnerability in these
synopsis of the security analysis; and status reports in the
curves when they are implemented correctly and used as
areas of quantum computation, hash-based signatures,
described in NIST standards and guidelines.
coding-based cryptography, lattice-based cryptography,
However, more than fifteen years have passed since and multivariate cryptography. Through these presentations
these curves were developed, and the community now and discussions, the team made significant progress in
knows more about the security of elliptic curve cryptography understanding the strengths and weaknesses of the existing
and practical implementation issues. Advances within the cryptographic schemes in each category. The project team
cryptographic community have led to the development of is planning to create evaluation criteria for post-quantum
new elliptic curves and algorithms whose designers claim cryptography schemes for standardization.
to offer better performance and are easier to implement
The NIST team continues to be productive in post-
in a secure manner. Some of these curves are under
quantum cryptography research. The results have been
consideration in voluntary, consensus-based Standards
published at the major conferences, such as PQCrypto
Developing Organizations.
2014, and Eurocrypt 2015. NIST researchers have given
In June 2015, NIST hosted a workshop on Elliptic Curve presentations at conferences and workshops to increase
Cryptography Standards to discuss possible approaches to awareness of the upcoming migration. NIST researchers have
promote the adoption of secure, interoperable and efficient contributed to the European Telecommunications Standards
elliptic curve mechanisms. Workshop participants expressed Institute (ETSI) whitepaper on quantum-safe cryptography.
significant interest in the development, standardization and NIST has also sponsored other research, education, and
adoption of new elliptic curves. As a result of this input, research events.
NIST is considering the addition of new elliptic curves to
NIST held the Workshop on Cybersecurity in a Post-
the current set of recommended curves in FIPS 186-4. In FY
Quantum World in March of 2015. The workshop was
2016, NIST will solicit comments on possible improvements
attended by approximately 140 participants from around
to FIPS 186-4, which may lead to a workshop held later in
the world. Presentations given at the workshop included
the year.
new proposals for quantum-safe cryptosystems, ideas for
how to modify protocols (such as TLS) to include these new
CONTACTS:
cryptosystems, discussions on how to standardize hash-
based signatures and key-management issues, as well as
Email project team: EllipticCurves@nist.gov
new ideas on the cryptanalysis of the many post-quantum
Dr. Dustin Moody Dr. Lily Chen
systems.
(301) 975-8136 (301) 975-6974
In FY 2016, NIST will continue to explore the security
dustin.moody@nist.gov lily.chen@nist.gov
and feasibility of purported quantum-resistant technologies,
with the ultimate goal of uncovering the fundamental
Mr. Andy Regenscheid
mechanisms necessary for efficient, trustworthy, and cost-
(301) 975-5155
effective information assurance in the post-quantum era.
andy.regenscheid@nist.gov
Upon the successful completion of this phase of the project,
NIST will be prepared for possible standardization efforts in
Post-Quantum Cryptography this area.
In recent years, there has been a substantial amount of
For More Information, See:
research on quantum computers – machines that exploit
quantum mechanical phenomena to solve problems that are http://csrc.nist.gov/groups/ST/post-quantum-crypto/
difficult or intractable for conventional computers. If large-
scale quantum computers are ever built, they will be able to
break the existing infrastructure of public-key cryptography.
The focus of the Post-Quantum Cryptography project is
to identify candidate quantum-resistant systems that are
3 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

CONTACTS: a function is insecure if it can be implemented by a circuit
containing too few Boolean AND gates. This security metric,
Email project team: pqc@nist.gov
namely the number of AND gates necessary and sufficient
to implement a function, is referred to as its multiplicative
Dr. Dustin Moody Dr. Lily Chen
complexity. Unfortunately, determining multiplicative
(301) 975-8136 (301) 975-6974
complexity is extremely hard (very recently, Magnus Find
dustin.moody@nist.gov lily.chen@nist.gov
proved computational intractability conditioned on the
existence of one-way functions). Mathematicians attempted
Dr. Yi-Kai Liu
to determine multiplicative complexity in the 1970s, but the
(301) 975-6499
effort had been largely abandoned by the 1980s. However, the
yi-kai.liu@nist.gov
CTG has published circuits that are provably optimal or close
to optimal (with respect to multiplicative complexity) for
Circuit Complexity important classes of functions. In the process, we developed
Cryptographic functions, such as encryption, digital tools that have wide applicability for both theoretical and
signatures, and hashing, are implemented as electronic applied research in security and cryptography.
circuits for a wide class of applications. In practice, it Multiparty computation is a technique that allows
is important to be able to minimize the size of these a group of people to compute a function of their inputs
circuits. This problem is closely related to designing small without revealing the inputs themselves. Examples of this
combinational circuits. These circuits use only binary AND, are: i) holding an election; ii) conducting closed-bid auctions
XOR and NEGATION gates, i.e., multiplication, addition, and in which only the winning bid is determined; iii) proving to a
“+1” in arithmetic modulo 2. A combinational circuit on four third party that a person’s encrypted attributes satisfy some
variables (X, X, X , and X ) using AND and XOR gates is requirement, such as “over 21 and (U.S. citizen or Canadian
1 2 3 4
depicted in Figure 9. citizen)”. The protocols that solve multiparty computation
problems often encrypt bits using arithmetic modulo 2. The
complexity of such protocols largely depends on the number
of multiplications required. Hence, expressing functions as
circuit computations with only a few multiplication (AND)
gates is important. Some of the published circuits are now
the standard reference for benchmarking tools in multiparty
computation.
The following is a partial list of new results by our team:
• The smallest known circuits were constructed for multi-
plication in several small finite fields.
The red nodes are AND gates; the yellow nodes are XOR gates. • The smallest known circuits were constructed for
binary multiplication (i.e., multiplication of polynomials
Figure 9: Combinational Boolean Circuit of degree n over the Galois Field with two elements).
This yields important speed increases in elliptic curve
The project team has shown that finding optimal cryptography.
combinational circuits is MAX-SNP Complete. In practice, this
• Optimal circuits were constructed - with respect to
means that it is necessary to settle for methods that design
multiplicative complexity - for all predicates on four
“good” circuits, as opposed to provably optimal circuits.
bits (see the example below). There are 65,536 such
The CTG has developed and implemented new solutions for
predicates. Surprisingly, the multiplicative complexity
the circuit-minimization problem. Two patents have been
of all these functions turned out to be at most three.
granted related to this work, the last one in FY 2014. These
Additionally, our circuits use no more than seven
are held jointly between NIST and the University of Southern
non-linear gates (XOR, XNOR). This is quite hard. Con-
Denmark.
sider the following predicate (arithmetic is modulo 2):
The CTG is also researching circuit-based security f = x + x + x + x + xx + xx + xx + xx +xx + xxx
1 2 3 4 1 2 1 3 1 4 2 3 2 4 1 2 3
metrics for cryptographic functions. For a function to be + xxx + xxx x .
1 2 4 1 2 3 4
secure (in particular, one-way), it must be the case that any Computing the last term requires three multiplications.
circuit that implements it is sufficiently complex. In particular, So, it is quite surprising that the full expression can be
4 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

computed using only three multiplications. But, we and potential future standardization of lightweight primitive
have shown this to be true for f and all other pred- algorithms. The workshop included two invited talks, twenty-
icates on four bits. The circuit on the previous page four presentations and a panel discussion.
computes f using three multiplications and six addi-
In FY 2015, CTG staff further engaged the international
tions.
cryptographic community by providing presentations at
• A proof was developed that the maximum multipli- the Fourth International Workshop on Lightweight Crypto-
cative complexity of predicates on five bits (there are graphy for Security and Privacy in Bochum, Germany, at
more than 4 billion such predicates) is four. The proof is the Fast Software Encryption Workshop in Istanbul, Turkey
constructive, meaning that the circuits can actually be and at the Lightweight Crypto Day, in Haifa Israel. Project
built. summaries and challenges ahead were presented at the
Cybersecurity Innovation Forum and to ITL’s Cyber-Physical
• A proof was developed that an explicit function
Systems (CPS) group.
requires at least 3.01n gates. This constitutes the only
improvement on this problem for more than 30 years. In FY 2016, CTG will continue to analyze the resource
The result is due to Magnus Find, in collaboration with requirements and performance characteristics of lightweight
mathematicians from New York University (NYU) and primitives, and study their use as building blocks to perform
from the Steklov Institute, St. Petersburg, Russia. various cryptographic objectives. Additionally, CTG is
planning to publish a report that describes the current state
Circuits are posted periodically at http://www.cs.yale.edu/
and challenges in target application areas.
homes/~peralta/CircuitStuff/CMT.html
CONTACTS:
CONTACT:
Mr. Lawrence Bassham Dr. Kerry McKay
Dr. René Peralta
(301) 975-3292 (301) 975-4969
(301) 975-8702
lawrence.bassham@nist.gov kerry.mckay@nist.gov
rene.peralta@nist.gov
Dr. Meltem Sönmez Turan
Cryptography for Constrained
(301) 975-4391
Environments meltem.turan@nist.gov
There are several emerging areas in which highly
constrained devices are interconnected, typically
The NIST Randomness Beacon
communicating wirelessly with one another, and working in
NIST has implemented a source of public randomness.
concert to accomplish some task. Examples of these areas
The service is available at https://beacon.nist.gov/home. It
include: sensor networks, distributed control systems, the
uses two independent, commercially available sources of
Internet of Things, cyber physical systems, and the smart
randomness, each with an independent hardware entropy
grid. Security and privacy can be very important in all of
source and SP 800-90A-approved components.
these areas. Because the majority of current cryptographic
algorithms were designed for desktop/server environments, The NIST Beacon is designed to provide unpredictability,
implementing many of these algorithms with constrained autonomy, and consistency. Unpredictability means that
resources can be extremely challenging. If current algorithms users cannot algorithmically predict bits before they are
can be made to fit into the limited resources of constrained made available by the source. Autonomy means that the
environments, their performance is typically not acceptable. source is resistant to attempts by outside parties to alter the
distribution of the random bits. Consistency means that a set
CTG staff are examining applications in constrained
of users can access the source in such a way that they are
environments to determine whether NIST should develop
confident of receiving the same random string.
lightweight cryptographic standards. CTG is communicating
with industry experts to understand challenges, limitations The NIST Beacon posts bit-strings in blocks of 512 bits
and work from other standardization bodies in this area. In every 60 seconds. Each such value is time-stamped and
FY 2015, CTG organized a NIST workshop on Lightweight signed, and includes the hash of the previous value to chain
Cryptography in Gaithersburg, MD, July 20-21, 2015 to the sequence of values together. This prevents all parties,
discuss issues related to the security and resource even the source, from retroactively changing an output
requirements of applications in constrained environments packet without being detected. The NIST Beacon keeps
41
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

all output packets. At any point in time, the full history of Entropy as a Service (EaaS)
outputs is available to users. The security of cryptography today depends on having
Tables of random numbers have probably been used for strong keys and keeping them secret. The ability to generate
multiple purposes at least since the Industrial Revolution. strong cryptographic keys is directly related to having
In the digital age, algorithmic pseudorandom number access to unpredictable random data, but generating truly
generators (PRNGs) have largely replaced these tables. The unpredictable random data on computing devices is hard
NIST Beacon expands the use of randomness to multiple and unreliable. As a result, weak keys are widely used in
scenarios in which neither tables nor PRNGs can be used. cryptographic applications compromising the security of
The extra functionalities stem mainly from three features. sensitive data protected by them with potentially disastrous
First, the Beacon-generated numbers cannot be predicted consequences.
before they are published. Second, the public, time-bound, A primary goal of this project is to provide high-quality,
and authenticated nature of the Beacon allows a user truly unpredictable random data to devices on the Internet
application to prove to anybody that it used truly random to enable them to generate strong cryptographic keys and
numbers not known before a certain point in time. Third, this attest the strength of the keys used to protect data in transit
proof can be presented offline and at any point in the future. or at rest, thereby enabling cryptographic system strength
Although commercially available physical sources of attestation. Achieving this goal would provide a solid basis
randomness are adequate as entropy sources for currently for addressing the problems targeted by Cryptographic
envisioned implementations of the NIST Beacon, we are System Validation (see the next section: Validated Programs,
working on developing a source of verifiably random the first project in this section).
sequences. In collaboration with NIST physicists from the Random data obtained from sources of true randomness
Physical Measurement Laboratory (PML), we aim to use that are based on unpredictable physical phenomena, such
quantum non-locality to build an entropy source whose as quantum effects, is much better suited for cryptographic
unpredictability is guaranteed by the laws of physics. This applications. CSD is collaborating with the NIST Physical
project is funded by NIST’s Innovations in Measurement Measurement Laboratory (PML) to build a quantum source.
Science (IMS) Program. IMS funds highly competitive The aim is to use quantum effects to generate sequences
projects designed to explore high-risk, leading-edge that are guaranteed to be unpredictable, even if an attacker
research concepts that anticipate the future measurement has access to the random source. For more information on
and standards needs of industry and science. For more this collaboration, see http://www.nist.gov/pml/div684/
information on this collaboration see http://www.nist.gov/ random_numbers_bell_test.cfm.
pml/div684/random_numbers_bell_test.cfm.
This project aims to develop a system and protocols
As of the end of FY 2015, the NIST Beacon has been for obtaining random data with high entropy from one or
functioning without interruption for more than two years. more remote sources. The high-level architecture is shown in
NIST encourages the community at large to research and Figure 10 (see next page). The architecture of the Entropy-as-
publish novel ways in which this tool can be used. A few a-Service system consists of two main parts: the client-side
examples of applications are unpredictable sampling, and the server-side. The critical components of the system
new authentication mechanisms, and secure multi-party are the quantum device, the EaaS server and a secure device
computation. in the client systems capable of providing strong isolation
and protection for the cryptographic keys stored inside the
For More Information, See:
device and offering a set of basic cryptographic services.
http://www.nist.gov/itl/csd/ct/nist_beacon.cfm
Client devices mix this data with locally available random
data to seed random number generators to generate strong
CONTACT:
cryptographic keys and other random values independently
Dr. René Peralta from the remote sources.
(301) 975-8702
rene.peralta@nist.gov
4 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

With system architecture and protocols defined, the
CONTACTS:
project team have engaged with industry and academia to
obtain feedback on the approach and identify possibilities for Dr. Apostol Vassilev Mr. Harold Booth
collaborative approaches to solving important cybersecurity (301) 975-3221 (301) 975-8441
challenges in the domains of cryptography and supply-chain apostol.vassilev@nist.gov harold.booth@nist.gov
management, e.g., integrated circuit counterfeiting.
The project team have developed a working prototype Mr. Robert Staples
and demonstrated it at high-profile cybersecurity forums (301) 975-4578
and academic conferences. The team is continuing to robert.staples@nist.gov
develop the system aiming to stand up a publicly accessible
NIST EaaS instance in the near future. In addition, the team is
also planning to publish the server and client code on GitHub
and invite the public to voluntarily adopt it. Related to this,
the project team is planning to work on developing public
criteria for reputable EaaS hosts.
Figure 10: High-level architecture of EaaS
4 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Wireless and Mobile Security over the Internet. It defines technical requirements for
Today, wireless networks often provide connections for each of the four levels of assurance in the areas of identity
mobile devices using multiple radio technologies. In such proofing, tokens, credential binding, management processes,
a heterogeneous network, a mobile device may switch its authentication protocols and assertion characteristics. Since
connection between different wireless technologies, such the initial release of SP 800-63, the CSD has released two
as between cellular and WiFi networks. The procedure for revisions to address changes in modern technology and
conducting such a switch is called a “handover.” Media- lessons learned from practical implementations by federal
independent handover (MIH) is a set of services specified departments and agencies.
in IEEE 802.21 to assist the handover. When the services Several recent developments have an impact on the way
provided by the pervasive heterogeneous networks that agencies fulfill their e Authentication requirements:
are extended to other applications, such as Smart Grid
• Executive Order 13681, Improving the Security of Con-
applications, the MIH needs to be processed by a group
sumer Financial Transactions, issued by the adminis-
of wireless nodes, such as smart meters, for balancing the
tration in October 2014, requires “…that all agencies
network load and for reliability. In this case, the information
making personal data accessible to citizens through
may need to be delivered to a group of smart meters using a
digital applications require the use of multiple factors
multicast message, which is used to deliver the information.
of authentication and an effective identity proofing
That is, the multicast message is sent from one point-of-
process, as appropriate.” (see http://www.whitehouse.
service (PoS) to multiple wireless nodes. In some of the
gov/the-press-office/2014/10/17/executive-order-im-
application environments, such as sensor networks, the
proving-security-consumer-financial-transactions)
groups are formed dynamically; new nodes can be added
to the group, and some nodes in the group may need to • CSD published The Framework for Improving Critical
be removed. Such groups are managed through multicast Infrastructure Cybersecurity in February 2014 in re-
signals. sponse to Executive Order (EO) 13636, Improving Crit-
ical Infrastructure Cybersecurity (for the Framework,
Amendment 2 of IEEE 802.21 provides protection
see http://www.nist.gov/cyberframework/; for the
mechanisms for unicast messages − mechanisms that
EO 13636, see http://www.whitehouse.gov/the-press-
protect messages between a PoS and a single mobile
office/2013/02/12/executive-order-improving-criti-
node. In FY 2015, CSD continued work with IEEE 802.21 to
cal-infrastructure-cybersecurity). The accompanying
develop security solutions for group management in Task
roadmap cites the need for NIST to “…conduct identity
Group D of IEEE 802.21. The solutions, specified in IEEE
and authentication research complemented by the pro-
802.21 Amendment 4, include the mechanisms to distribute
duction of Special Publications that support improved
group keys and for the protection of multicast messages.
authentication practices.” (see http://www.nist.gov/
Amendment 4 of IEEE 802.21 was published in FY 2015.
cyberframework/upload/roadmap-021214.pdf)
In FY 2016, CSD will continue to contribute to a broader
• The National Strategy for Trusted Identities in Cyber-
scope of IEEE 802 wireless standards.
space (NSTIC), which was released in 2011, charts a
course for both public and private sectors to collab-
CONTACT:
orate to raise the level of trust associated with the iden-
Dr. Lily Chen tities of individuals, organizations, networks, services,
(301) 975-6974 and devices involved in online transactions through an
lily.chen@nist.gov Identity Ecosystem (see http://www.nist.gov/nstic/).
NSTIC calls for the Federal Government to “lead by
example and implement the Identity Ecosystem for the
Authentication
services it provides internally and externally.” As the
To support OMB Memorandum M-04-04,
Identity Ecosystem starts to take shape, NIST guide-
E-Authentication Guidance for Federal Agencies, NIST’s CSD
lines should reflect and support it.
developed SP 800-63, Electronic Authentication Guideline.
In addition, market forces have resulted in an inflexion
The OMB memorandum defines four levels of assurance that
point in how departments and agencies authenticate users.
a federal agency must select, based on a risk assessment
NIST and our private sector partners have observed that
to determine the impact of an authentication failure. This
some public and private sector identity assurance standards
guideline covers the remote authentication of users (such as
have become outdated or have simply not been adopted.
private individuals) interacting with government IT systems
4 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Specifically, SP 800-63 was originally written to address an As many types of biometric sensors become ubiquitous
online world that is much different than today. Innovation in personal mobile devices, and more and more individuals
has offered new perspectives in how trusted identities leverage biometrics in commercial use cases such as
can be established. Practical implementations of SP 800- mobile payment and online authentication to private
63 have informed us of areas of strengths, weaknesses, sector services, CSD will re-examine the current position of
and techniques not utilized by federal agencies or the remote, unattended biometric authentication. The existing
private sector. In addition, federal agencies are the only publication does allow local biometric authentication to
organizations required to follow NIST SPs. However, as the unlock a token – a secure technique currently used by
Federal Government evolves to accept credentials offered popular mobile handset manufacturers. Yet the comments
by private sector organizations, the applicability of SP 800- CSD received reveal that some believe this is insufficient,
63 has expanded beyond agency use. NIST has an obligation and that centralized biometric authentication used in
to service the expansion of the original SP 800-63 target. single- or multi-factor schemes should be allowed in a future
revision. CSD will pursue detailed research in the security
Therefore, in April of 2015, NIST issued a call for
of remote biometric authentication, examine the efficacy
comments on the current published version, SP 800-63-2,
of standardization efforts related to presentation attack
in order to identify specific topics that could be addressed
detection, and contemplate the long-term impacts of the
in a future revision of SP 800-63 (see http://csrc.nist.gov/
en-masse theft of biometrics before expanding the current
groups/ST/eauthentication/sp800-63-2_call-comments.
requirements of SP 800-63-2.
html). NIST received over 40 submissions from individuals,
academia, and the public and private sectors. Over 300 The user experience of online authentication will also be
distinct comments were identified from these submissions. In a significant consideration in a potential update of SP 800-
addition to the comments that NIST received, vulnerabilities 63. The CSD has observed that the user experience has a
have been discovered in existing online authentication direct relationship with individual uptake of authentication
services, specifically in the area of remote identity proofing, services as well as the overall security of any authentication
which has warranted an accelerated consideration of scheme. While CSD does not intend to weaken requirements
updated guidance for the Federal Government. to accommodate a favorable user experience, understanding
the impact of e-Authentication requirements on the user,
In FY 2016, CSD expects its authentication work to be
and to design requirements that do not degrade security but
driven by the needs of the ongoing rapid expansion of online
upgrade the user experience, is imperative.
service delivery, commercially available authentication
services, results and metrics from NSTIC pilots, and the The CSD, therefore, plans to actively consider revisions
availability of multi-factor tokens to consumers. Breaches to SP 800-63-2 in response to the issues noted above and
of personal information and the relative availability of other issues that can be dealt with in time to assist in the
personal information has necessitated that NIST reconsider intense ongoing efforts to expand online services.
approaches to identity proofing, both in-person and
For More Information, See:
remotely. The paradigm where the starting assumption was
http://csrc.nist.gov/groups/ST/eauthentication/
that personal data was hard to find has now changed to one
where it is acknowledged that this data is readily available
CONTACT:
online; existing guidance needs to be adjusted to offer
organizations cost-effective, yet secure, identity proofing Mr. Paul Grassi
capabilities. The NSTIC pilots have tested innovative (703) 786-8275
alternatives to high-assurance remote proofing, necessita- paul.grassi@nist.gov
ting that SP 800-63 be considerate of these advances in the
marketplace. In addition, commercial advances in physical
document validation and verification, the proliferation of
high-resolution video cameras on commodity computing
devices, including mobile phones, as well as new offerings
in the delivery of in-person proofing, will influence potential
updates to requirements at all levels of assurance.
4 5
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

VALIDATION PROGRAMS This program will perform research and experimentation
in applicable technologies and techniques that will enable
the efficient testing of the cryptographic capabilities of each
Federal agencies, industry, and the public rely on many
layer, and enable the continuous monitoring capabilities of
of the standards and specifications supported by CSD. Poor
each cryptographic component, providing the necessary
implementations of these standards or specifications may
interfaces to establish trust relationships with other
render a particular product insecure, potentially placing
cryptographic components. Techniques could include such
sensitive information at risk. CSD operates several validation
items as:
programs that help provide a level of assurance that products
meet established security requirements and conform to • Embedding XML data elements and standard inter-
published specifications. To that end, the Security Testing, faces to query those data elements during the design
Validation, and Measurement Group (STVMG) develops test and implementation of cryptographic components that
suites and test methods; provides implementation guidance would enable automated testing capabilities;
and technical support to industry forums; and conducts
• Using cryptographic techniques to embed values into
education, training, and outreach programs.
the module that would increase the verifiability and
STVMG’s validation programs work together with assurance that the module provides; and
independent laboratories that are accredited by the National
• Using industry-based secure development techniques
Voluntary Laboratory Accreditation Program (NVLAP).
to increase the level of trust inherent in software mod-
Based on the independent laboratory test report and test
ules, starting with design and implementation.
evidence provided by the labs, the validation programs
Research into this area of cryptographic system
described below validate the implementation under test.
validation holds the promise of automating the validation of
CSD subsequently publishes lists of the validations awarded
all cryptographic components, providing a higher assurance
on public websites.
with less manual effort. The program will use an approach
Cryptographic System Validation that was developed for the SCAP product validation effort
Current validation programs focus on providing a known to embed data elements that instrument the test harnesses
level of assurance for cryptographic algorithms and modules. used to validate cryptographic systems. This would also
These modules are used within the context of a larger system provide the instrumentation that could be leveraged to
to provide cryptographic services as a method of protecting enable a greater level of situational awareness and security
the data within the system. As information systems continue measurement, and potentially, to enable continuous
to become more complex, the methods used to implement monitoring of cryptographic systems.
cryptographic services have also increased in complexity.
Problems with the use of cryptography are often introduced CONTACT:
through the interaction of cryptographic components with
Mr. Michael Cooper
the operating environment. This program seeks to specify
(301) 975-8077
how cryptographic components are used as part of a defined
michael.cooper@nist.gov
cryptographic system to solve problems with a measureable
level of assurance, and to introduce automated methods of
quantifying the level of assurance that has been provided. Cryptographic Programs and
In FY 2016, this program will begin the research required Laboratory Accreditation
to define a reference cryptographic systems architecture The Cryptographic Algorithm Validation Program
and example use cases where cryptographic systems are (CAVP) and the Cryptographic Module Validation Program
built from known cryptographic components that cooperate (CMVP) were developed in collaboration between NIST
through trust relationships to provide a measureable level of and the Communications Security Establishment (CSE) of
assurance. The architecture should begin at the lowest level Canada to support the respective federal user communities
with a hardware-based root of trust, and each cryptographic for strong, independently tested, and commercially
component should be added in successive layers to available cryptographic algorithms and modules. Through
provide assurance in a systematic way. This should allow these programs, NIST and CSE work with international
the development of tests that would measure the correct government, public and private sectors as a part of the
implementation of cryptographic components as part of a cryptographic community to achieve standards-based
larger system. security and assurance of correct implementation. The
goal of these programs is to provide federal agencies
4 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

with a security metric to use in procuring and deploying The CAVP and the CMVP are separate collaborative
cryptographic modules, and promote the use of validated programs. The CAVP and the CMVP validate algorithms and
algorithms and modules by industry and the public. The modules, respectively, which are used in a wide variety of
testing carried out by independent third-party laboratories products, including Internet browsers, radios, smart cards,
accredited by NVLAP, and the validations performed by space-based communications, munitions, security tokens,
the CAVP and CMVP programs provide this metric. Federal mobile phones, network and storage devices, and products
agencies, industry, and the public can choose cryptographic supporting the Public Key Infrastructure (PKI) and electronic
modules and/or products containing cryptographic modules commerce. A module may be a standalone product, such
from the CMVP Validated Modules List and have confidence as a virtual private network (VPN) or smart card, or it
in the claimed level of security and assurance of correct could be a module embedded in many products, such as a
implementation. cryptographic-based toolkit. As a result, a small number of
modules may be incorporated within hundreds of products.
Cryptographic algorithm and cryptographic module
The CAVP validates cryptographic algorithms that may be
testing and validation are based on published NIST
integrated in one or more cryptographic modules. Figure 11
standards. Since federal agencies are required to use
provides a flow of the CMVP testing and validation process.
validated cryptographic modules for the protection of
sensitive unclassified information, the validated modules and
the validated algorithms that the modules contain represent
the culmination and delivery of CSD’s cryptography-based
work to the end user.
Figure 11: General Flow of FIPS 140-2 Testing and Validation
47
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

The CAVP and CMVP validation programs provide whose mission is to conduct research to assist developers
documented methodologies for conformance testing of cryptographic modules, testing laboratories, and the
through defined sets of security requirements. For the user community when developing new standards. The
CAVP, the validation system documents are designed for insights from this research into the evolution of operating
each FIPS-approved or NIST-recommended cryptographic environments and complex systems allow the CMVP to
algorithm. See the website for a listing (see http://csrc.nist. perform research and development on evolving test metrics
gov/groups/STM/cavp/). Security requirements for the and methods and future requirements for cryptographic
CMVP are found in FIPS 140-2, Security Requirements for modules.
Cryptographic Modules, and the associated test metrics
The CAVP and the CMVP have stimulated the improved
and methods in Derived Test Requirements for FIPS 140-
quality and security assurance of cryptographic algorithm
2, Security Requirements for Cryptographic Modules.
implementations and modules. By the end of FY 2015, the
The four Annexes to FIPS 140-2 reference the underlying
CMVP had validated and issued a total of 2,380 crypto-
cryptographic algorithm standards or methods. The CMVP-
graphic module validation certificates to more than 475
developed Implementation Guidance for FIPS 140-2 and the
domestic and international vendors. As shown in Figure 12,
Cryptographic Validation Program provides programmatic
the CMVP awarded 197 certificates in FY 2015. The left portion
and implementation guidance across all of the referenced
of the graphic illustrates the distribution by submission type,
documents. The information provided in the Derived
based upon the modification scenarios described in the
Test Requirements (DTR) and Implementation Guidance
CMVP Implementation Guidance, including:
(IG) documents ensures the repeatability of tests and the
• 1SUB - Modifications made to hardware, software or
equivalency of results across the testing laboratories. The IG
firmware components that did not affect any FIPS 140-1
provides clarity, consistency of interpretation, and insight for
or FIPS 140-2 security relevant items (e.g., a mainte-
successful conformance testing, validation, and revalidation.
nance activity);
The unique position of the validation programs gives the
• 3SUB - Modifications that include changes that affect
CAVP and CMVP the opportunity to acquire insight during
some of the FIPS 140-2 security-relevant items and
the validation review activities and results in practical, timely,
require revalidation, but drew upon previous submis-
and up-to-date guidance that is needed by the testing
sions; and,
laboratories and vendors to move their modules out to the
user community in a timely and cost-effective manner and • 5SUB - Significant changes to hardware, software, or
with the assurance of third-party conformance testing. This firmware components and, therefore, were considered
knowledge and insight provide a foundation for current and a new module requiring full validation testing.
future standards and tools development.
The right portion of the diagram shows the number of
The CMVP reviews the cryptographic module validation certificates awarded, based upon each of the four increasing
requests from the testing laboratories and, as a byproduct levels of security specified in the FIPS that may be satisfied
of the review, is attentive to emerging and/or changing by a cryptographic module.
technologies.
Likewise, to date, the CAVP has issued approximately
Starting with FY 2015, the Security Testing, Validation, 19,578 validations, representing the algorithm validations of
and Measurement (STVM) group created a research team approximately 17 approved algorithms.
Figure 12: FY 2015 FIPS 140-2 Validations
4 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Figure 13: CAVP Validation Status by Fiscal Year
Figure 14: CAVP Validation Status for FY 2015 4 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Figure 15: CAVP Validated Implementation Actual Numbers
The CAVP issued approximately 3,372 algorithm
CMVP CONTACTS:
validations in FY 2015, an increase of over 1,000 validations
from the previous year. The increase in validations is Ms. Jennifer Cawthra Dr. Apostol Vassilev
attributed to other outside programs now requiring CAVP (301) 975-8514 (301) 975-3221
validated implementations (e.g., NIAP). jennifer.cawthra@nist.gov apostol.vassilev@nist.gov
The CMVP issued 197 module validation certificates in
FY 2015. The number of algorithms and modules submitted
CAVP CONTACT:
for validation continues to grow, representing significant
growth in the number of validations expected to be available Ms. Sharon Keller
in the future. (301) 975-2910
For More Information, See: sharon.keller@nist.gov
http://csrc.nist.gov/groups/STM
CMVP Implementation Guidance, G.8
http://csrc.nist.gov/groups/STM/cmvp/documents/fips140-
2/FIPS1402IG.pdf
5 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Automated Security Testing and Test and verifying the expected result. Negative testing is also
Suite Development performed by supplying known incorrect values to assure
The CAVP utilizes the requirements and specifications that the implementation recognizes values that are not
of NIST standards (i.e., FIPS and Special Publications) to allowed. The Monte Carlo Test is designed to exercise the
develop algorithm validation test suites and automated entire implementation under test (IUT). This test is designed
security testing. The CAVP is responsible for providing to detect the presence of implementation flaws that are not
assurance that the cryptographic algorithm implementations detected with the controlled input of the Known-Answer
contained in cryptographic modules are implemented Tests. The types of implementation flaws detected by
according to the specifications in the standards. The CAVP this validation test include pointer problems, insufficient
accomplishes this by designing and developing conformance allocation of space, improper error handling, and incorrect
testing specific to each cryptographic algorithm. behavior of the IUT. The Multi-Block Message Test (MMT)
is designed to test the ability of the implementation to
The conformance testing consists of a suite of validation
process multi-block messages, which requires the chaining
tests for each approved cryptographic algorithm. These
of information from one block to the next.
validation tests exercise the algorithmic requirements and
mathematical formulas detailed in the algorithm to assure During the last few years, the CTG has expanded its
that the detailed specifications are implemented correctly publications to contain not only the algorithm’s specifica-
and completely. If the implementer deviates from the tions, but also requirements for an algorithm’s use. Many
specifications in the standard or excludes any part of these of these usage requirements do not fall within the scope
specifications or requirements, the validation test will detect of the CAVP, because the CAVP focuses on the correctness
the deviations and fail. The validation testing will indicate that of the instructions within the algorithm’s boundary. If these
the algorithm implementation does not function properly or additional algorithm usage requirements are not considered
is incomplete. applicable to the algorithm’s implementation, they cannot
be tested at the algorithm level by the CAVP, but may be
The cryptographic algorithm validation tests designed
tested by the Cryptographic Module Validation Program
and developed by the CAVP are used by independent third-
(CMVP) if the requirements are considered applicable to
party laboratories accredited by the NVLAP. The laboratory
the cryptographic module. However, some of these usage
works with vendors to validate their cryptographic
requirements may be considered to be outside the scope
algorithm implementations. The suite of validation tests for
of both the algorithm implementation and cryptographic
each algorithm ensures the repeatability of tests and the
module. In this latter case, the fulfillment of the requirements
equivalency of results across the testing laboratories.
is the responsibility of entities using, installing, or configuring
There are several types of validation tests, all designed applications or protocols that use the cryptographic
to satisfy the testing requirements of the cryptographic algorithms. For example, depending on the design of a
algorithms and their specifications. These include, but are cryptographic module, it may not be possible for the module
not limited to, Known-Answer Tests, Monte Carlo Tests, to determine whether a specific key is used for multiple
and Multi-Block Message Tests. The Known-Answer Tests purposes, a situation that is strongly discouraged.
are designed to examine the individual components of
The CAVP currently has algorithm validation testing for
the algorithm by supplying known values to the variables
the following cryptographic algorithms:
TABLE 1: CRYPTOGRAPHIC ALGORITHMS & NIST TECHNICAL DOCUMENTS (FIPS & SPS)
FEDERAL INFORMATION PROCESSING
CRYPTOGRAPHIC ALGORITHM/COMPONENT STANDARD (FIPS) OR SPECIAL PUBLICATION
(SP)
SP 800-67, Recommendation for the Triple Data
Encryption Algorithm (TDEA) Block Cipher, and
Triple Data Encryption Standard (TDES)
SP 800-38A, Recommendation for Block Cipher Modes of
Operation–Methods and Techniques
FIPS 197, Advanced Encryption Standard, and
Advanced Encryption Standard (AES)
SP 800-38A, Recommendation for Block Cipher Modes of
Operation–Methods and Techniques 5 1
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

TABLE 1 (CONT.): CRYPTOGRAPHIC ALGORITHMS & NIST TECHNICAL DOCUMENTS (FIPS & SPS)
FEDERAL INFORMATION PROCESSING
CRYPTOGRAPHIC ALGORITHM/COMPONENT STANDARD (FIPS) OR SPECIAL PUBLICATION
(SP)
FIPS 186-2, Digital Signature Standard (DSS), with change
notice 1
Digital Signature Algorithm (DSA)
FIPS 186-4, Digital Signature Standard (DSS)
FIPS 186-2, Digital Signature Standard (DSS), with change
notice 1 and ANS X9.62
Elliptic Curve Digital Signature Algorithm (ECDSA)
FIPS 186-4, Digital Signature Standard (DSS), and ANS
X9.62
FIPS 186-4, Digital Signature Standard (DSS)
RSA algorithm
ANS X9.31 and Public Key Cryptography Standards (PKCS)
#1 v2.1: RSA Cryptography Standard-2002
Hashing algorithms SHA-1, SHA-224, SHA-256, SHA-384,
FIPS 180-4, Secure Hash Standard (SHS)
SHA-512, SHA-512/224, SHA-512/256
Random number generator (RNG) algorithms FIPS 186-2 Appendix 3.1 and 3.2; ANS X9.62 Appendix A.4
SP 800-90A, Recommendation for Random Number
Deterministic Random Bit Generators (DRBG)
Generation Using Deterministic Random Bit Generators
FIPS 198-1, The Keyed-Hash Message Authentication Code
Keyed-Hash Message Authentication Code (HMAC)
(HMAC)
Cipher-based Message Authentication Code (CMAC) Mode SP 800-38B, Recommendation for Block Cipher Modes of
for Authentication Operation: The CMAC Mode for Authentication
SP 800-38C, Recommendation for Block Cipher Modes
Counter with Cipher Block Chaining-Message
of Operation: the CCM Mode for Authentication and
Authentication Code (CCM) Mode
Confidentiality
SP 800-38D, Recommendation for Block Cipher Modes of
GCM and GMAC Modes
Operation: Galois/Counter Mode (GCM) and GMAC
SP 800-38E, Recommendation for Block Cipher Modes
XTS-AES Mode of Operation: The XTS-AES Mode for Confidentiality on
Block-Oriented Storage Devices
SP 800-38F, Recommendation for Block Cipher Modes of
Key Wrapping
Operation: Methods for Key Wrapping
SP 800-56A, Recommendation for Pair-Wise Key
DH and MQV Key Agreement Schemes and Key
Establishment Schemes Using Discrete Logarithm
Confirmation
Cryptography, dated March 2007
All of SP 800-56A schemes without the Key Derivation SP 800-56A, Key Derivation Functions for Key Agreement
Functions (KDF) Schemes: All sections except Section 5.8
All of SP 800-56A schemes without the Key Derivation SP 800-56A, Section 5.7.1.2 Elliptic Curve Cryptography
Functions (KDF) Cofactor Diffie-Hellman (ECC CDH) Primitive Testing
SP 800-108, Recommendation for Key Derivation using
Key-Based Key Derivation functions (KBKDF)
Pseudorandom Functions
5 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

TABLE 1 (CONT.): CRYPTOGRAPHIC ALGORITHMS & NIST TECHNICAL DOCUMENTS (FIPS & SPS)
FEDERAL INFORMATION PROCESSING
CRYPTOGRAPHIC ALGORITHM/COMPONENT STANDARD (FIPS) OR SPECIAL PUBLICATION
(SP)
Application-Specific Key Derivation functions (ASKDF)
SP 800-135 (Revision 1) Recommendation for Existing
(includes the KDFs used by IKEv1, IKEv2, TLS, ANS X9.63-
Application Specific key Derivation Functions
2001, SSH, SRTP, SNMP, and TPM)
Component test – ECDSA Signature Generation of a hash
FIPS 186-4, Digital Signature Standard (DSS), and
value (This component test verifies the signing of a hash-
ANS X9.62
sized input. It does not verify the hashing of the original
message to be signed.)
Component test – RSA PKCS#1 1.5 Signature Generation
FIPS 186-4, Digital Signature Standard (DSS), and
of encoded message EM (This component test verifies the
Public Key Cryptography Standards (PKCS) #1 v2.1:
signing of an EM. It does not verify the formatting of the
RSA Cryptography Standard-2002
EM.)
Component test – RSA PKCS#1 PSS Signature Generation SP 800-56B, Recommendation for Pair-Wise Key
of encoded message EM (This component test verifies the Establishment Schemes Using Integer Factorization
RSASP1 function.) Cryptography, August 2009, Section 7.1.2
In FY 2016, the CAVP expects to add algorithm validation For More Information, See:
testing for:
http://csrc.nist.gov/groups/STM/cavp
• FIPS 202, SHA-3 Standard: Permutation-Based Hash
and Extendable-Output Functions, August 2015; CONTACTS:
• SP 800-56C, Recommendation for Key Derivation
Ms. Sharon Keller Ms. Elaine Barker
through Extraction-then-Expansion, November 2011;
(301) 975-2910 (301) 975-2911
• SP 800-132, Recommendation for Password-Based sharon.keller@nist.gov elaine.barker@nist.gov
Key Derivation Part 1: Storage Applications, December
2010; and
• SP 800-56A Revision 2, Recommendation for Pair-Wise
Key Establishment Schemes Using Discrete Logarithm
Cryptography, May 2013.
5 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Security Content Automation Protocol (SCAP): SCAP Version 1.2. Conformance testing is necessary
(SCAP) Validation Program because SCAP is a complex collection of eleven individual
The SCAP Validation Program performs conformance specifications that work together to support various use
testing to ensure that products correctly implement cases. A single error in product implementation could result
SCAP as defined in SP 800-126 Revision 2, The Technical in undetected vulnerabilities or policy noncompliance within
Specification for the Security Content Automation Protocol an organization’s networks.
Figure 16: SCAP 1.2 Validation Process
5 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

The test requirements for SCAP 1.2 are defined in In FY 2016, the SCAP Validation Program plans to
NISTIR 7511, Security Content Automation Protocol (SCAP) expand the validation test suite, adding new operating
Version 1.2 Validation Program Test Requirements. In system support and introducing module testing. SCAP
general, vendors may opt for product validation for one or module testing enables the “SCAP Inside” labeling program.
more SCAP capabilities or operating systems. Currently, the Products using the “SCAP Inside” label have incorporated an
program offers testing on Microsoft Windows and Red Hat SCAP-validated module; however, the consumer product as
Enterprise Linux platforms. Figure 16 illustrates the SCAP a whole has not completed validation testing by an NVLAP
1.2 Validation Process. The validation process starts when accredited laboratory. Additions to the SCAP Validation
a vendor voluntarily submits an SCAP-enabled product to Program will be defined in NISTIR 7511 Revision 4.
an NVLAP-accredited laboratory. Once the lab completes
For More Information, See:
product testing, the lab submits a test report to the SCAP
http://scap.nist.gov/validation
Validation Program at NIST for review. NIST reviews the
test report and awards a validation if all requirements have
been met. Once a validation is awarded, the SCAP Validation
CONTACT:
Record is sent to the lab, and the information about the
newly validated product is posted on the SCAP Validated Ms. Melanie Cook
Products web page. (301) 975-5259
melanie.cook@nist.gov
The SCAP Validation Program resources web page
provides the public with a centralized location for all
resources and information necessary for preparing products
for SCAP 1.2 validation. Resources include: documentation, IDENTITY MANAGEMENT
a list of Frequently Asked Questions (FAQ), the SCAP
validation-test content, and tools for validating and
NIST Personal Identity Verification
processing SCAP data streams. The SCAP validation-test
Program (NPIVP)
content should be used by vendors for quality assurance
The objective of the NIST Personal Identity Verification
testing prior to entering formal SCAP testing with an
Program (NPIVP) is to validate PIV components for
NVLAP-accredited laboratory. The open-source tools that
conformance to the specifications in FIPS 201, Personal
are available for download may be used by SCAP content
Identity Verification (PIV) of Federal Employees and
authors for testing SCAP source content. The SCAP Content
Contractors, and its companion documents. The two PIV
Validation Tool (SCAPVal) may be used to determine if the
components that come under the scope of NPIVP are the
content conforms to the SCAP specification. Open-source
PIV Smart Card Application and the PIV Middleware. NPIVP
SCAP reference implementation tools, such as the SCAP
test facilities that perform the two types of tests are the
Reference Implementation Tool, may be used to process
Cryptographic and Security Testing (CST) Laboratories
SCAP data streams.
that have been accredited by the NVLAP. As of September
End users may use information on the SCAP Validation
2015, there were nine such facilities (see http://csrc.nist.gov/
web page to learn about SCAP validation and find products
groups/SNS/piv/npivp/testing_facilities.html).
that have been awarded validations. The validation
The interface specifications for the PIV Smart Card
records that are posted on the SCAP Validated Products
Application and PIV Middleware are found in a FIPS
page identify the product versions that were tested in the
201-associated document, namely, SP 800-73-4, Interfaces
laboratory, along with details about each validation, such as
for Personal Identity Verification. The conformance tests
the tested platforms, SCAP capabilities, the validation test
for these specifications are detailed in SP 800-85A-2, PIV
suite version, and the lab that performed the product test.
Card Application and Middleware Interface Test Guidelines.
In FY 2015, five products successfully completed testing
To implement these tests and to generate conformance test
and were awarded validations, bringing the total number
reports, CSD also developed an integrated toolkit called
of SCAP 1.2-validated products to twelve. This provides
“PIV Interface Test Runner,” which conducts tests on both
coverage for 80 percent of the market space. Several
PIV Card Application and PIV Middleware products, and
products are in various stages of validation testing and are
provides the toolkit to accredited NPIVP test facilities.
expected to be awarded validations in FY 2016. The current
list of SCAP 1.2-validated products may be found on the
SCAP Validated Products list at https://nvd.nist.gov/SCAP-
Validated-Tools.
5 5
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

In addition, NPIVP is closely involved in ensuring that all and Contractors, was developed and was approved by the
changes in PIV companion documents, such as SP 800-73-4, Secretary of Commerce in February 2005. HSPD-12 called
SP 800-76-2, Biometric Specifications for Personal Identity for the creation of a new identity credential for federal
Verification, and SP 800-78-4, Cryptographic Algorithms employees and contractors. FIPS 201 is the technical
and Key Sizes for Personal Identity Verification, are fully specification for both the PIV identity credential and the PIV
reflected in the updated versions of the conformance test system that produces, manages, and uses the credential.
documents, SP 800-85A-2 and SP 800-85B, as well as in Within NIST’s Information Technology Laboratory (ITL),
the “PIV Interface Test Runner” toolkit. Currently, the NPIVP this work is a collaborative effort of the Information Access
team is guiding the development of the “PIV Interface Test Division (IAD) and CSD. CSD activities in FY 2015 directly
Runner” toolkit for validating PIV Card application and PIV supported the recently revised FIPS 201-2 by updating
Middleware products for conformance to the specifications the relevant publications associated with FIPS 201-2 and
in SP 800-73-4, SP 800-76-2 and SP 800-78-4. In FY by developing two new publications. CSD performed the
2015, Phase I changes to PIV Interface Test Runner were following activities during FY 2015 in support of HSPD-12:
completed, and NPVIP performed acceptance testing.
• Published SP 800-157, Guidelines for Derived Personal
For More Information, See: Identity Verification (PIV) Credentials, in December
2014. SP 800-157 defines the technical details for
http://csrc.nist.gov/groups/SNS/piv/npivp
implementing and deploying derived PIV credentials
on mobile devices, such as smart phones and tablets.
CONTACTS:
As intended by FIPS 201-2, a derived PIV credential is
Dr. Ramaswamy Chandramouli Ms. Hildegard Ferraiolo a PIV credential that can be provisioned directly to a
(301) 975-5013 (301) 975-6972 mobile device to enable remote enterprise access from
mouli@nist.gov hildegard.ferraiolo@nist.gov the device. The use of Derived PIV Credentials greatly
improves the usability of electronic authentication from
mobile devices to remote IT resources, while at the
Personal Identity Verification (PIV)
same time maintaining the goals of HSPD-12 for com-
and FIPS 201 Revision Efforts
mon identification that is secure, reliable, and interop-
erable government wide.
• Organized and hosted a workshop in March 2015 on
upcoming Special Publications supporting FIPS 201-2
(PIV). The event drew over 160 in-person attendees
and about 75 webcast remote attendees from gov-
ernment, industry, and academia representing a wide
range of implementers and professionals in cyberse-
curity and physical security. Topics covered included
physical access control with the PIV Card, PIV card-
holder interagency record exchange, and derived PIV
credentials.
• Published SP 800-73-4, Interfaces for Personal Identity
Verification, in June 2015, after two public comment
periods. The three-part SP details the new, optional PIV
Card capabilities introduced in FIPS 201-2, including a
virtual contact interface (VCI), a secure channel proto-
Figure 17: Government Employees Use PIV Cards for
col, and an on-card biometric comparison mechanism.
Facility Access
SP 800-73-4 also requires new PIV Cards to enforce a
minimum PIN length of six digits.
In response to Homeland Security Presidential • Published SP 800-78-4, Cryptographic Algorithms and
Directive-12 (HSPD-12), Policy for a Common Identification Key Sizes for Personal Identity Verification, in June
Standard for Federal Employees and Contractors, FIPS 201, 2015, after two public comment periods. The document
Personal Identity Verification (PIV) of Federal Employees has been modified to align with SP 800-73-4, and
5 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

includes the addition of new algorithms and key sizes RESEARCH IN EMERGING
for the secure messaging protocol. Cryptographic algo-
TECHNOLOGIES
rithm validation testing requirements were also added.
• Published Draft SP 800-85A-4, PIV Card Application
Secure Development Toolchain
and Middleware Interface Test Guidelines (SP 800-73-4
Competitions
Compliance), in June 2015, to align the testing require-
ments with FIPS 201-2, SP 800-73-4, and SP 800-78-4. Many security weaknesses in federal information
systems stem from software security vulnerabilities induced
• Published NISTIR 7863, Cardholder Authentication for
by software flaws present in current-generation software
the PIV Digital Signature Key, in June 2015. The docu-
products. CSD tracks software security vulnerabilities (in
ment provides clarification for the requirement in FIPS
the National Vulnerability Database), seeks techniques for
201-2 that a PIV cardholder perform an explicit user
the measurement of security vulnerabilities, and also seeks
action prior to each use of the digital signature key
techniques to reduce the impact and prevalence of security
stored on the card. NISTIR 7863 clarifies the require-
vulnerabilities in newly developed products or in new
ment for “explicit user action” and specifies a range of
versions of existing products.
PIN caching options that maintains the goal of “explicit
user action” while adhering to a consistent and reliable One approach to reducing the number of security
level of security. vulnerabilities in software is to improve the development
tools that are available. By identifying languages and
• Published SP 800-79-2, Guidelines for the Authoriza-
software development tools that support a reduction of
tion of Personal Identity Verification Card Issuers (PCI)
vulnerabilities and, by stimulating the creation of better
and Derived PIV Credential Issuers (DPCI), in July 2015.
tools and tool usage techniques, the approach should help
The document incorporates changes required by FIPS
developers produce applications with fewer vulnerabilities.
201-2 to accredit PIV Card Issuers and includes a set of
While it is impossible to assure the total absence of security
issuer controls for Derived PIV Credentials Issuers.
vulnerabilities in this way, it might well be possible to rule
In FY 2016, CSD will continue to focus on updating the out specific, significant classes of vulnerabilities that today
relevant publications associated with FIPS 201-2, including SP provide the basis for many serious exploits.
800-116, A Recommendation for the Use of PIV Credentials
CSD is developing an empirical, competitive approach
in Physical Access Control Systems (PACS), and developing
to finding the most effective and usable combinations of
two new publications: SP 800-156, Representation of PIV
tools to produce software systems that are relatively free of
Chain-of-Trust for Import and Export, and SP 800-166,
exploitable vulnerabilities. Multiple competitions are planned
Guidelines for Testing Derived Personal Identity Verification
that will be based on an idea developed during the Designing
(PIV) Credentials. CSD will also continue to provide technical
a Secure Systems Engineering Competition Workshop that
and strategic inputs to the PIV-related initiatives.
was conducted by National Science Foundation in 2010. The
For More Information, See: workshop proposed a competition for the development of a
set of tools to help non-security-expert developers to rapidly
http://csrc.nist.gov/groups/SNS/piv/
build a significant application with zero vulnerabilities, as
detected by an extensive public test suite.
CONTACTS:
The participants in the planned competitions would
Ms. Hildegard Ferraiolo Dr. David Cooper
implement software systems to solve challenge problems
(301) 975-6972 (301) 975-3194
using software development tool chains (“toolchains”)
hildegard.ferraiolo@nist.gov david.cooper@nist.gov
of their own choosing, within specified time periods. The
toolchains may include existing technologies (e.g., existing
Dr. Ramaswamy Chandramouli
software libraries and frameworks, code generators, reusable
(301) 975-5013
source code, or bug-finding tools), novel technologies, or
mouli@nist.gov
any combination thereof. Each competition would apply
a time pressure by simulating a deadline in the software
development process, increasing the likelihood of an
introduction of security flaws. The objective of the toolchains
will be to detect or prevent security flaws while still supporting
a quick-paced software development of applications with
57
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

rich feature sets. Through the demonstration of security computing environment. CSD is working in parallel on several
flaw avoidance in a time-constrained setting, CSD seeks to projects (introduced below) that aim to accelerate the
show that wide-scale improvements in the overall security Federal Government’s adoption of secure cloud computing.
of software products can be realized without sacrificing CSD subject matter experts collaborate with national and
time-to-market. The competitions, which will be open to international standards setting organizations, and both
all interested parties, will aim to provide a level playing field the public and private sectors in developing security,
for the application and measurement of the full spectrum interoperability and portability standards and guidance.
of commercial and research software development,
CSD Role in the NIST Cloud Computing
composition, and reuse techniques.
Program
In FY 2015, CSD and its contractors developed 8
During FY 2015, the NIST Cloud Computing Team
challenge problems for the competition. A challenge problem
continued to promote the development of publications,
is comprised of three parts: 1) a functional specification of a
national and international standards, and specifications in
program to develop (during the competition), 2) a security
support of the U.S. Government’s (USG) effective and secure
policy that the program must enforce, typically including
use of cloud computing, as well as providing technical
confidentiality and integrity requirements, and 3) a challenge-
guidance to federal agencies for secure and effective cloud-
problem-specific test suite including 20 fully-automated
computing adoption. CSD supports many of the technical
pass/fail functionality tests, 20 fully-automated pass/fail
standards activities hosted by the NIST Cloud Computing
security tests, and extensive application of random inputs
Program, with a particular focus on cloud-computing
(i.e., fuzz testing). The challenge problems span three initial
security and forensic science. Activities include the leading
program types: command-line interface programs, mobile
role for the development of the following documents:
applications (i.e., cell phone apps), and web applications
(browser-based apps). In FY 2015, CSD and its contractors • SP 800-173, Guide for Applying the Risk Manage-
also developed a testing infrastructure for the competition ment Framework to Cloud-based Federal Information
and performed testing to exercise the tools and to assess the Systems (draft). This publication provides guidance
suitability of the challenge problems. in using the Risk Management Framework described
in SP 800-37 Revision 1 to issue an authorization to
In FY 2016, CSD plans to re-engineer portions of the
operate for cloud-based information systems. The draft
testing infrastructure in response to issues uncovered by
document will be posted for public comment in the
testing, to perform a second round of testing, and to publicly
first quarter of FY 2016.
announce the first toolchain competition.
• SP 800-174, Security and Privacy Controls for Cloud-
CONTACTS: based Federal Information Systems (internal draft).
The document will provide a cloud overlay of the SP
Mr. Lee Badger Mr. Christopher Johnson 800-53 Revision 4 security controls for cloud-based
(301) 975-3176 (301) 975-3247 ecosystems.
lee.badger@nist.gov christopher.johnson@nist.gov
• Define the cloud forensics use cases that address the
top four challenges identified in NISTIR 8006, NIST
Cloud Computing and Virtualization Cloud Computing Forensic Science Challenges.
The model for Cloud Computing is defined in SP 800-
CSD staff members organized the security and forensics
145, The NIST Definition of Cloud Computing. Virtualization
tracks of the eighth NIST Cloud Computing Forum and
is a foundational technology that facilitates the use of a
Workshop, which was held in July 2015.
computing infrastructure for cloud-computing services. At
the core of a virtualized infrastructure is the virtualized In support of U.S. cloud-computing mandates, CSD
host that provides an abstraction of the hardware (e.g., staff members provided leadership for several public cloud
CPU, memory) and that enables multiple computing stacks working groups operating under the NIST Cloud Computing
(comprised of the operating system, middleware, and Program. These working groups focus on meeting the
applications) to be run on a single physical machine, creating high-priority requirements described in SP 500-293, U.S.
dynamically provisioned, elastic compute resources. The Government Cloud Computing Technology Roadmap.
efficiency of such a dynamic and distributed processing CSD staff chaired or co-chaired several significant cloud
environment is counter-balanced by the interoperability, computing efforts in 2015:
portability, and security challenges inherent in this
5 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

• Co-Chaired the NIST Cloud Computing Security Policy Machine – Leveraging Access
Working Group and led the working group on the Control for Cloud Computing
development of SP 800-173, Guide for Applying the
Risk Management Framework to Cloud-based Federal
Information Systems; SP 800-174, Security and Privacy
Controls for Cloud-based Federal Information Systems
(both described on previous page); and on researching
the most suitable approach to a structured representa-
tion of the SP 800-53 Revision 4 security and privacy
controls.
• Co-Chaired the NIST Cloud Computing Forensic Sci-
ence Working Group and led the development of cloud
forensics use cases that document the top four high
priority challenges identified in NISTIR 8006.
• Co-Chaired the NIST Cloud Computing Interoperability Figure 18: Policy Machine Operating Environment
and Portability Working Group and addressed issues
facing cloud computing with respect to interoperability In FY 2015, CSD continued the research and develop-
and portability, standards, and common and function- ment of a virtualization utility for enterprise-wide controlled
al terminologies. The working group’s activities were delivery of Cloud data services through Access Control.
ceased in mid FY 2015. This included the publication of a revised Policy Machine
specification as NISTIR 7987 Revision 1, Policy Machine:
CSD staff members participated in various standards
Features, Architecture, and Specification, in September 2015.
development organizations, all listed in the section of this
report dedicated to international standards. NIST and other members of an Ad Hoc INCITS working
group are developing a three-part Policy Machine standard
In FY 2015, CSD members of the NIST cloud-computing
under the title of Next Generation Access Control (NGAC),
team continued research in key areas of cloud security,
under three sub-projects:
cloud interoperability and portability, cloud metrics, cloud
services, and cloud Service Level Agreements (SLAs). They • Project 2193–D: Next Generation Access Control – Im-
also presented the results of cloud-computing research and plementation Requirements, Protocols and API Defini-
development, introduced the standards and specifications tions;
under development, and provided the status of the NIST
• Project 2194–D: Next Generation Access Control –
Cloud-Computing Program in a variety of domestic and
Functional Architecture; and
international conferences and workshops. CSD staff
• Project 2195–D: Next Generation Access Control –
continues to engage industry and federal agencies for
Generic Operations & Abstract Data Structures.
inputs and collaborative work through working groups,
publications, and networking. The Policy Machine’s architecture was the basis for the
NGAC work within INCITS. An initial standard from Project
For More Information, See:
2194–D was published in 2013 and is now available from the
http://www.nist.gov/itl/cloud
ANSI e-standards store as INCITS 499, NGAC Functional
Architecture (NGAC–FA). The standard resulting from
CONTACT: Project 2195–D: INCITS 526, NGAC Generic Operations and
Abstract Data Structures (NGAC-GOADS), is in the approval
Dr. Michaela Iorga
process and is expected to be published in the fall of 2015.
(301) 975-8431
michaela.iorga@nist.gov In FY 2016, CSD plans to issue a new version of its open-
source distribution to reflect new features and enhanced
performance, revise INCITS 499, and publish SP 800-178, A
Comparison of Extensible Access Control Markup Language
(XACML) and NGAC Attribute Based Access Control
Standards for Data Services.
5 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

For More Information:
CONTACT:
http://csrc.nist.gov/pm/
Dr. Ramaswamy Chandramouli
(301) 975-5013
CONTACTS:
mouli@nist.gov
Mr. David Ferraiolo Mr. Serban Gavrila
(301) 975-3046 (301) 975-4242
Cybersecurity for Emerging
david.ferraiolo@nist.gov serban.gavrila@nist.gov
Technologies
Technology is advancing at an amazing rate, with
Security for a Virtualized rapid technological advances in manufacturing, healthcare,
Infrastructure nanotechnology, cyber physical systems, and the “Internet
Several important components of a virtualized of things.” This project scans the environment for
infrastructure need to be protected, including the developing technologies that may be currently at risk from a
Hypervisor, the virtual network, the Virtual Machine (VM) cybersecurity perspective, or potentially at risk in the future
and data storage. The objective of this project is to analyze as the technology improves.
various configuration options in the deployment of these
In FY 2015, CSD conducted research on cybersecurity
components and to provide guidance in the form of security
in the field of additive manufacturing or three-dimensional
recommendations. The project builds upon previous research
(3D) printing. On February 3, 2015, CSD hosted a symposium
that included: (a) the identification of security requirements
on Cybersecurity for Direct Digital Manufacturing, which
for various use cases when a virtualized infrastructure is
involves fabricating physical objects from a data file using
offered for cloud services and (b) the analysis of configura-
computer-controlled processes with little to no human
tion options for Secure Hypervisor Deployment and
intervention, such as in additive manufacturing and 3D
providing security recommendations.
printing. During the symposium, attendees representing
In FY 2015, the focus of research was the secure government, industry, and academic organizations discussed
configuration of virtual networks for the protection of VMs. relevant cybersecurity risks, challenges, and solutions, as
VM Security forms the primary goal in virtual network well as the implications for information and communications
configuration due to the following: (a) VMs are the compute- technology supply-chain risk management. Attendees
engines of the virtualized infrastructure on which mission identified several opportunities in the area and generally
critical applications of the enterprise run, and (b) VMs are agreed that the time is right for building cybersecurity into
the end-nodes of the virtual network. Research included the these technologies. The proceedings of the symposium
following configuration areas: were published in April 2015 in NISTIR 8041, Proceedings of
the Cybersecurity for Direct Digital Manufacturing (DDM)
• Network segmentation;
Symposium.
• Network path redundancy;
Along the same lines, CSD researched risk management
• Firewall deployment architecture; and
practices for securing a set of technologies called Replication
• VM traffic monitoring. Devices (RDs). As a result of this research, CSD published
NISTIR 8023, Risk Management for Replication Devices, in
Research included the analysis of the security
April 2015 to help organizations protect the confidentiality,
advantages and disadvantages of various configuration
integrity, and availability of information processed, stored,
options in each of these areas, forming the basis for security
or transmitted on RDs. An RD is any device that reproduces
recommendations. The research resulted in the following
(e.g., copies, prints, or scans) documents, images, or objects
publications during FY 2015:
from an electronic or physical source. For the purposes
• The conference paper entitled, Analysis of Network
of NISTIR 8023, RDs include copiers, printers, 3D printers,
Segmentation Techniques in Cloud Data Centers; and
scanners, and 3D scanners, as well as multifunction
• Draft SP 800-125B, Secure Virtual Network Configura- machines when used as a copier, printer, or scanner. RDs in
tion for Virtual Machine (VM) Protection. use within organizations run the gamut in terms of age and
functionality, with some devices being relatively simple and
others quite complex and sophisticated.
6 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

In FY 2016, NIST will continue to scan the environment is to help organizations prepare for an exchange of cyber
for emerging technologies, such as 3D printers and threat information, both consuming cyber threat information
nanotechnology, which may benefit from guidance on how from external sources and producing information for other
to manage, implement, or build-in cybersecurity principles organizations to use. Because each organization may have
and tools. substantially different capabilities for detecting threats,
responding to attacks, diagnosing causes, and handling
CONTACT: sensitive incident-related information, this guidance is
intended to help organizations collaborate and exchange
Ms. Celia Paulsen
cyber threat information despite these organizational
(301) 975-5981
differences.
celia.paulsen@nist.gov
CSD’s cyber threat information sharing initiative is
focused on providing guidance on how an organization can
Cyber Threat Information Sharing
establish information sharing and coordination capabilities
As cyber attacks increase in both sophistication and that enhance or augment their existing cybersecurity
frequency, it is important to collect and analyze cyber threat practices. The guidance covers threat-informed detection,
information from a variety of internal and external sources, protection and response capabilities; data privacy and
and use it to develop, enhance, and deploy proactive, sensitivity; data collection and retention practices; the use of
threat-informed, cyber defense capabilities. Cyber threat open standards for information exchange; de-identification
information includes indicators (i.e., artifacts or observable and anonymization; and guidance on how an organization
events that suggest that an attack is imminent, that an can establish, participate in, and maintain coordination and
attack is underway, or that a compromise may have already information sharing relationships. The guidance will help
occurred); information about the tactics, techniques, and incident responders, network defenders, and operations
procedures (TTPs) of actors; recommended courses of personnel consider what information is sharable, the
action, and other information that is used to characterize circumstances under which sharing is permitted, with whom
threats. Because threat actors often use the same TTPs the information may be shared, and how the information
against multiple targets, exchanging cyber threat informa- should be protected.
tion allows organizations to leverage the collective
In early FY 2016, CSD plans to release the second draft
knowledge, experience, and analysis capabilities of their
to Draft SP 800-150, based on the input received during the
peers, thereby increasing the overall awareness and security
public comment period of the first draft, which was released
of an entire sharing community. Through the exchange of
October 2014.
cyber threat information, organizations can gain a more
complete understanding of their threat environment by
CONTACTS:
correlating their observations with those of others.
When one organization observes an attack that may Mr. Lee Badger Mr. David Waltermire
affect or be used against other organizations, information (301) 975-3176 (301) 975-3390
sharing and coordination can make it possible to reduce the lee.badger@nist.gov david.waltermire@nist.gov
impact of the attack, speed recovery operations, and maintain
a higher level of operational security. By integrating cyber Mr. Christopher Johnson
threat information sharing into its existing cybersecurity and (301) 975-3247
risk management practices, an organization can reduce the christopher.johnson@nist.gov
likelihood or mitigate the impact of successful cyber attacks,
more effectively protect its systems, detect and anticipate
the actions of threat actors, respond to cyber attacks, and
recover to rapidly deploy effective countermeasures.
In FY 2014, CSD worked with DHS to develop SP 800-
150, Guide to Cyber Threat Information Sharing (Draft),
which provides guidance to organizations seeking to
establish and participate in cyber threat information sharing
communities. The draft publication was released for public
comment on October 28, 2014. The goal of this publication
61
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

The Ontology of Authentication
Over the past 30 years, NIST has been at the forefront
of recommending best practices for authentication.
Recommendations have included the usage of passwords in
enterprises, biometrics, and Public Key Infrastructure (PKI)
solutions. In FY 2015, CSD researched the classification of
general authentication features. This investigation was
prompted by the general call to move away from passwords
towards the growing number of alternative authentication
methods (e.g. biometrics, smart cards, etc.). In the early part
of this investigation, it became clear that an ontology of
authentication was needed.
A draft taxonomy (see Figure 19) was developed
to better describe current and emerging authentication
mechanisms. This taxonomy covers a wide assortment Figure 20: Suitability Framework for Authentication
of commonly used methods to cover human-machine,
metrics include authentication strength and the suitability of
machine-machine, and attribute attestation. It does not
the method to the environment. The strength measurements
address identity management - which typically happens
should include security and usability. This provides a way
before authentication occurs, or access control - which
to monitor a common complaint of designers – usability
typically happens after.
being a tradeoff to security. However, security and usability
As a result of this research, several patterns and gaps
is not sufficient to address the suitability of implementing
were identified. For example, there are similar technologies
a particular authentication mechanism in a particular
used to support the various mechanisms. One of the greatest
environment. By adding in measures for deployability and
challenges is in defining a set of common metrics to assess
manageability it should be possible to address the suitability
authentication technologies. Two areas identified as needing
of an authentication mechanism.
Figure 19: Draft Authentication Taxonomy
6 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

In the next few years, NIST CSD will work with the NIST’s work in mobile security has earned the 2014
community to identify and address common areas of Government Computer News (GCN) award for Information
authentication requirements to create a framework for Technology Excellence and the 2013 U.S. Department of
researching and developing authentication mechanisms Commerce Gold Medal Award. In FY 2016, NIST will be
using this taxonomy. As shown in Figure 20 (previous page), transitioning AppVet to the Department of Homeland
this framework will support integration of security with Security as part of their Carwash program, which provides
deployability, usability and manageability of authentication. government development teams with a continuous
This work will also be used to better identify the needs integration build, testing, source code management, and
and dependencies for proper interaction with identity issue tracking system.
management and access control processes.
CONTACTS:
CONTACT:
Dr. Steve Quirolgico Dr. Jeffrey Voas
Dr. Kim Schaffer (301) 975-8426 (301) 975-6622
(301) 975-8375 steveq@nist.gov jeff.voas@nist.gov
kim.schaffer@nist.gov
MOBILE SECURITY STRENGTHENING INTERNET
SECURITY
Smart phones have become both ubiquitous and
indispensable. Although these mobile devices are relatively
USGv6: A Technical Infrastructure to
small and inexpensive, they can be used for voice calls,
simple text messages, sending and receiving emails, Assist IPv6 Adoption
browsing the web, online banking and e-commerce, social Internet Protocol (IP) Version 6 (IPv6) is an updated
networking, and many functions once limited to laptop version of the current Internet Protocol, IPv4. The primary
and desktop computers. Smart phones and tablet devices motivations for the development of IPv6 were to increase
have specialized built-in hardware, such as cameras, the number of unique IP addresses available for use and to
accelerometers, Global Positioning System (GPS) receivers, handle the needs of new Internet applications and devices.
and removable media readers. They also employ a wide range In addition, IPv6 was designed with the following goals:
of wireless interfaces, including infrared, Wireless Fidelity increased ease of network management and configuration,
(Wi-Fi), Bluetooth, Near Field Communications (NFC), and expandable IP headers, improved mobility and security, and
one or more types of cellular interfaces that provide network the quality of service controls. IPv6 has been, and continues
connectivity across the globe. to be, developed and defined by the IETF.
Smart phones present new capabilities, but also a FY 2012 was a significant year for the deployment
number of new security and privacy challenges. One such of IPv6 in the United States Government (USG). OMB’s
challenge concerns securing smartphone applications. To Memo of September 10, 2010, Transition to IPv6, required
address this issue, NIST is conducting research in software- all government agencies to “upgrade public/external facing
assurance methodologies for smart phone applications (or servers and services (e.g., web, email, Domain Name System
“apps”) and is working with other government agencies and (DNS), and Internet Service Provider (ISP) services) to
industry to bridge the security gaps present with today’s operationally use IPv6 by the end of FY 2012.” NIST worked
smart phones. For example, NIST developed the AppVet with the U.S. Government IPv6 (USGv6) Task Force and with
mobile app-vetting system and framework for managing individual government agencies to achieve this goal. NIST
an organization’s app-vetting process with respect to the developed an online monitor to demonstrate which high-
organization’s security and privacy policies. This system was level government domains have met this goal with respect
used by the Defense Advanced Research Projects Agency to Domain Name System (DNS) services, email, web servers,
(DARPA) to vet apps prior to being deployed on thousands of and Domain Name System Security Extensions (DNSSEC).
mobile devices for use in Afghanistan, the 2013 Presidential In FY 2013, NIST and OMB continued to use this monitor to
Inauguration, and the 2014 Boston Marathon. measure USGv6 compliance with OMB’s requirement.
6 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Additional OMB IPv6 requirements were mandated • Published a conference paper for Big Data Processing
for FY 2014. Agencies were required to “upgrade internal access control and distributed systems; and
client applications that communicate with public Internet
• Studied efficient test case generation methods for
servers and supporting enterprise networks to operationally
Attribute Based Access Control (ABAC) policy testing.
use IPv6 by the end of FY 2014.” NIST developed online
In FY 2016, CSD will continue the above research. CSD
diagnostic tools to help agencies verify compliance to this
expects that this project will:
requirement.
• Promote (or accelerate) the adoption of community
The NIST IPv6 Test Program, whose goal is to provide
computing that utilizes the power of shared resources
assurance on IPv6 product conformance and interoperability,
and common trust-management schemes;
continues to operate. In FY 2015, NIST continued to manage
and evolve the USGv6 Test Program and to help federal • Provide guidance for implementing access control
agencies fulfill OMB mandates and monitor compliance to models and mechanisms for standalone or network
those mandates. In FY 2016, NIST is planning to update SP systems;
500-267, A Profile for IPv6 in the U.S. Government, Version
• Increase the security and safety of static (connected)
1.0. This document is the basis for the USGv6 Test Program
distributed systems by applying the testing and verifi-
and for USG IPv6-compliant device evaluation and purchase.
cation tool for the AC policies;
The NIST program is a collaboration between CSD and the
• Assist system architects, security administrators, and
ITL Advanced Networking Technology Division.
security managers whose expertise is related to access
For More Information, See:
control or privilege policy in managing their systems
http://www.nist.gov/itl/antd/usgv6.cfm and in learning the limitations and practical approaches
for their applications; and
CONTACTS:
• Provide accurate and efficient fault detection and
correction technology for implementing AC rules and
Ms. Sheila Frankel Mr. Douglas Montgomery
policies.
(301) 975-3297 (301) 975-3630
sheila.frankel@nist.gov dougm@nist.gov Figure 21 illustrates the application of access control and
privilege management within and among organizations.
ACCESS CONTROL PROJECTS
Access Control and Privilege
Management Research
With the advance of current computing technologies
and the diverse environments, access control issues, such
as situational awareness, trust management, preservation of
privacy, and privilege-management systems, are becoming
increasingly complex. Practical and conceptual guidance for
these topics is needed.
In FY 2015, the following research was accomplished for
this project:
• Enhanced the unified enforcement mechanism of data Figure 21: Access Control and Privilege Management
services for use by a Policy Machine (PM) for an enter-
prise computing environment;
CONTACTS:
• Enhanced the capabilities of the Access Control Policy
Tool (ACPT); Dr. Vincent Hu Mr. David Ferraiolo
(301) 975-4975 (301) 975-3046
• Enhanced the capabilities of the Access Control Rule
vhu@nist.gov david.ferraiolo@nist.gov
Logic Circuit Simulation (ACRLC) tool;
• Studied an Attribute Assurance mechanism for access
Mr. Rick Kuhn
authentication and authorization;
(301) 975-3337
6 4
• kuhn@nist.gov
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Conformance Verification for Access To address the issue, CSD developed the Access Control
Control Policies Property Tool (ACPT), shown in Figure 22 (next page),
Access control (AC) systems are among the most which allows a user to compose, verify, test, and generate
critical network security components. Faulty policies, access control policies. CSD also researched the AC Rule
misconfigurations, or flaws in software implementation can Logic Circuit Simulation (ACRLCS) technique, which enables
result in serious vulnerabilities. The specification of access the AC authors to detect a fault when the fault-causing AC
control policies is often a challenging problem. Often, a rule is added to the policy, so the fix can be implemented in
system’s privacy and security are compromised due to the real time before adding other rules that further complicate
misconfiguration of access control policies, instead of the the detecting effort, rather than checking by retracing the
failure of cryptographic primitives or protocols. This problem interrelations between rules after the policy is completed.
becomes increasingly severe as software systems become In FY 2015, CSD accomplished the following:
more and more complex, and are deployed to manage a large
• Published a conference paper for policy tool evaluation
amount of sensitive information and resources organized
and analysis: Evaluating and Capability and Perfor-
into sophisticated structures. Identifying discrepancies
mance of Access Control Policy Verification Tools;
between policy specifications and their properties (their
intended function) is crucial because correct implementation • Developed verification oracles for policy test bench-
and enforcement of policies by applications is based on the marking, which embed policy faults for committee,
premise that the policy specifications are correct. As a result, university, hospital, and bank policy test scenarios;
policy specifications must undergo rigorous verification and • Developed a Small Business Innovation Research
validation through systematic testing to ensure that the (SBIR) solicitation for access control tool development;
policy specifications truly encapsulate the desires of the
• Enhanced the ACRLCS − the Access Control Rule Logic
policy authors.
Circuit Simulation System;
To formally and precisely capture the security properties
• Published a conference paper for policy test case gen-
that AC should adhere to, access control models are usually
eration: Pseudo-exhaustive Testing of Attribute-Based
written to bridge the rather wide gap in abstraction between
Access Control Rules;
policy and mechanism. Thus, an access-control model
provides unambiguous and precise expression, as well as • Worked with industrial and academic organizations in
a reference for the design and implementation of security exploring new capabilities that helped to improve the
requirements. Techniques are required for verifying whether usability of the AC tools (ACPT and ACRLCS), resulting
an access-control model is correctly expressed in the access- in additional usage; ACPT was downloaded by 343
control policies, and whether the properties are satisfied in users and organizations; and,
the model. • Enhanced the capability of ACPT by improving policy
Most research on AC model or policy verification combination algorithms and adding test oracles for
techniques is focused on one particular model, and almost basic access control models.
all of the research is in applied methods, which require the In FY 2016, CSD is planning to conduct further research
completed AC policies as the input for verification or test on the new capabilities and enhance the performance of the
processes to generate fault reports. Even though correct ACPT and ACRLCS.
verification is achieved, and counter-examples may be
Figure 22 (next page) shows the system architecture
generated when faults were found, those methods provide
of the NIST access control policy tool: ACPT, which allows
no information about the source of faults that might allow
access control policy authors to compose, verify, and test
conflicts in privilege assignment, the leakage of privileges, or
access control policy implementation.
conflict of interest permissions. The difficulty in finding the
source of faults is increased, especially when the AC rules This project is expected to:
are intricately covering duplicated variables to a degree of • Provide a generic paradigm and framework of access
complexity. The complexity is due to the fact that a fault control model/property conformance testing;
might not be caused by one particular rule. Thus, it requires
• Provide templates for specifying access control rules
manually analyzing each rule in the policy in order to find the
in popular access control models, such as the Attribute
correct solution for the fault.
Based, Multilevel, and Workflow models;
6 5
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Figure 22: Access Control Property Tool (ACPT)
• Provide tools or services for checking the security and For More Information, See:
safety of an access control implementation, policy
http://csrc.nist.gov/groups/SNS/acpt/
combination, and eXtensible Access Control Markup
Language (XACML) policy generation;
CONTACTS:
• Promote (or accelerate) the adoption of combinatorial
Dr. Vincent Hu Mr. Rick Kuhn
testing for large-system testing (such as an access
(301) 975-4975 (301) 975-3337
control system);
vhu@nist.gov kuhn@nist.gov
• Promote the concept of detecting AC policy faults in
real-time AC rule composing;
Attribute-Based Access Control
• Provide an innovative method for specifying AC rules
formed by Boolean logic expressions operated on vari- Attribute-Based Access Control (ABAC) is a logical
ables of AC rules; access control methodology where an authorization to
• Provide techniques for preventing faults in enforcing perform a set of operations is determined by evaluating the
fundamental security properties, including Cyclic In- attributes associated with the subject, object, requested
heritance, Privilege Escalation, and Separation of Duty; operations, and, in some cases, environmental conditions
and against policy, rules, or relationships that describe the
allowable operations for a given set of attributes. ABAC
• Provide new methods for composing standard man-
represents a point on the spectrum of logical access control,
datory AC models, such as Attribute-Based Access
from simple access control lists to more capable role-based
Control (ABAC) and Multi-Level Security (MLS), as well
access (RBAC), and finally, to a highly flexible method for
as some fundamental security properties.
providing access based on the evaluation of attributes.
6 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

This research provides information for using ABAC characteristics of two ABAC implementation mechanisms:
to improve information sharing within and among organi- XACML and NGAC. CSD continued research on the Attribute
zations based on the planning, design, implementation, Assurance of ABAC in partnership with the National
and operational considerations. The research also includes Strategy for Trusted Identities in Cyberspace (NSTIC), and
technologies such as attribute assurance, attribute the National Cybersecurity Center of Excellence (NCCoE).
engineering/management, identity system integration, CSD developed a draft Special Publication based on the
attribute federation, situational awareness (real-time or mechanism for defining the veracity, security, and readiness
contextual) mechanisms, policy management, and natural- levels of assurance of ABAC attributes.
language policy translation to digital policy. Figure 23
In FY 2016, CSD will continue the research of ABAC
illustrates the interaction of many of these components. The
formal models, as well as details and extended topics of
goal of this research is to improve information sharing, while
ABAC capabilities, such as attribute assurance, ABAC
maintaining control of that information for federal agencies.
implementation examples, ABAC mechanisms, and ABAC
In FY 2015, CSD published two ABAC papers: Attribute- standards. The ABAC project will pursue the following
Based Access Control for IEEE Computing magazine, and objectives:
Implementing and Managing Policy Rules in Attribute-
• Provide readers with the terminology and a basic un-
Based Access Control for IEEE International Conference on
derstanding of ABAC;
Information Reuse and Integration. CSD also wrote a draft
• Provide readers with an overview of the current state
Special Publication document for ABAC formal models
of logical access control, a working definition of ABAC,
research: A Comparison of XACML and NGAC Attribute
and an explanation of the core and enterprise ABAC
Based Access Control Standards, which compares the
concepts;
Figure 23: ABAC Access Control Mechanism Chart 67
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

• Assist security policy makers in establishing a busi- • Identifying IT assets, including hardware, software, and
ness case for ABAC implementation and acquiring an data;
interoperable set of capabilities;
• Providing awareness over the operational state of com-
• Assist ABAC developers in developing the operational puting devices;
requirements and overall enterprise architecture;
• Enabling security reference data to be collected from
• Assist ABAC administrators in establishing or refining internal and external sources; and
business processes to support ABAC;
• Supporting analysis processes that measure the effec-
• Promote the adoption of ABAC for a more secure and tiveness of security controls and provide visibility into
flexible method for information sharing in a standalone security risks, enabling risk-based decision-making.
or enterprise environment; and
Commercial solutions built using security automation
• Provide testing methods for ABAC policy and imple- specifications enable the collection and harmonization of
mentations. vast amounts of operational and security data into coherent,
comparable information streams to achieve situational
For More Information, See:
awareness that allows the timely and active management of
http://csrc.nist.gov/projects/abac/
diverse IT systems. Through the creation of reference data
and guidance, and the international recognition of flexible,
CONTACTS: open standards, the NIST security automation program
works to improve the interoperability, broad acceptance, and
Dr. Vincent Hu Mr. David Ferraiolo
adoption of security automation solutions to address current
(301) 975-4975 (301) 975-3046
and future security challenges, creating opportunities for
vhu@nist.gov david.ferraiolo@nist.gov
innovation.
Mr. Rick Kuhn
Specification, Standards, and Guidance
(301) 975-3337
Development
kuhn@nist.gov
To support the overarching security automation vision, it
is necessary to have specifications that describe the required
ADVANCED SECURITY
interactions between systems, standards that document
TESTING AND international consensus approaches, and guidance that
MEASUREMENTS informs product developers and implementers. Through
close work with partners in government, industry, and
academia, CSD continues to facilitate the definition and
Security Automation and Continuous development of security automation approaches that enable
Monitoring organizations to understand and manage IT security risks.
IT organizations operate a diverse set of computing
During FY 2015, CSD has continued to work to build on
assets that access, route, store, and process information that
previous security automation work by:
is critical to the operations of businesses and the missions
• Identifying and addressing gaps in the current specifi-
of government agencies. These IT environments are under
cations;
constant threat of attack and are frequently undergoing
change, with new and updated software being deployed • Evolving existing approaches to achieve greater scal-
along with updated configurations. The wide variety of ability and impact;
computing products, the dynamic nature of software, the
• Participating in working groups in standards develop-
speed of configuration change, and the diversity of threats
ment organizations to promote international consensus
require organizations to maintain situational awareness
around standardized approaches;
over their IT assets and to utilize this information to make
• Providing additional guidance on architectural, design,
informed risk-based decisions.
and analysis concerns; and
Security automation utilizes standardized data formats
• Developing and maintaining tools and reference imple-
and transport protocols to enable data to be exchanged
mentations.
between business, operational, and security systems that
support security processes by:
6 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

CSD is currently working with its partners in various SCAP in multiple areas, both to support its own mission
standards-development organizations, including ISO, and to enable other agencies and private-sector entities
IETF, the Forum of Incident Response and Security Teams to meet their goals. For CSD, SCAP is a critical component
(FIRST), and the Trusted Computing Group (TCG), to of the SCAP Validation Program, the National Vulnerability
further mature and broaden the adoption of security Database (NVD), and the National Checklist Program (NCP).
automation specifications, reference data, and techniques. In September 2012, CSD published SP 800-126 Rev. 2,
This area of work is focused on evolving security automation The Technical Specification for the Security Content
specifications to integrate with existing transport protocols Automation Protocol (SCAP): SCAP Version 1.2. That
to provide for the secure, interoperable exchange of security document describes the 11 component specifications
automation data. Additional work is focused on evolving composing SCAP. See Table 2 (next page): SCAP 1.2
security metrics and providing consensus guidance on Specifications for details.
security automation approaches. Through the definition and
Since the release of SCAP 1.2, CSD has worked to
adoption of security automation standards and guidelines,
improve guidance around the use of SCAP specifications. In
IT vendors will be able to provide standardized security
FY 2015, CSD released draft NISTIR 8058, Security Content
solutions to their customers. These solutions support
Automation Protocol (SCAP) Version 1.2 Content Style
continuous monitoring and automated, dynamic network
Guide: Best Practices for Creating and Maintaining SCAP
defense capabilities, based on the analysis of data from
1.2 Content, which provides guidance for SCAP 1.2 content
operational and security data sources and the collective
creators to ensure that stylistic variations in SCAP 1.2
action of security components.
content are addressed in a way that improves the accuracy
Security automation standardization work has been and consistency of results, avoids performance problems,
focused in three areas: the evolution and international reduces user effort, lowers content maintenance burdens,
adoption of the Security Content Automation Protocol and enables content reuse. To achieve this, the report
(SCAP), the development of software asset management documents best practices for content creation and
standards to support operational and cybersecurity encourages their use by SCAP content authors and
use cases, and the development of security automation maintainers. Feedback on this report is welcomed and will
consensus standards. The following sections detail this work. help CSD to work towards producing a final version of this
document.
Security Content Automation Protocol
CSD is starting to work on an SCAP 1.3 revision. In
(SCAP)
August 2015, CSD requested comments on the design
SCAP is a multipurpose protocol that provides an
and development of SCAP 1.3. Specific areas of requested
automated means to collect and assess the state of devices.
feedback included:
SCAP supports automated vulnerability checking, verifying
the installation of patches, checking security configuration • Adopting the Open Vulnerability and Assessment Lan-
settings, verifying technical-control compliance, measuring guage (OVAL) 5.11.1, which was released in April 2015;
security, and examining systems for indicators of a
• Adopting the Common Vulnerability Scoring System
compromise. SCAP uses the Extensible Markup Language
(CVSS) v3, which was released in June 2015;
(XML) to standardize the format and nomenclature by which
• Removing support for CVSS v2; and
security software products communicate information about
software flaws, security configurations, and other aspects of • Deprecating support for older specification revisions
the device state. SCAP enables security automation content, and SCAP 1.0.
also known as “SCAP content,” to be expressed using
The received feedback generally favored the adoption
standardized formats, identifiers, and scoring models. This
of OVAL 5.11.1 and CVSS v3. Continued support for CVSS v2,
content can be used by any tool that is conformant to the
in addition to v3, and some reduction in the minimal support
specifications to collect and evaluate the state of software
for older specification revisions were also common themes
installed on a device.
in the feedback. CSD is currently considering this feedback
SCAP has been widely adopted by major software while working on a draft revision of SP 800-126 for public
and hardware manufacturers and has become a significant comment in FY 2016.
component of information-security-management and
governance programs. SCAP-enabled tools are currently
being used by the U.S. Government, critical-infrastructure
companies, academia, and other businesses, both
domestically and internationally. Currently, CSD is leveraging
6 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

TABLE 2: SCAP 1.2 SPECIFICATIONS
SPECIFICATIONS DESCRIPTION
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
Asset identification
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
model applied to security automation specifications
70
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Software Asset Management Standards installation, patching, upgrading and removal. CSD has
CSD has been collaborating with industry partners released three public discussion drafts of these guidelines.
to revise the ISO/IEC 19770-2:2009 standard, Information A final public draft will be released in FY 2016, along with a
technology—Software asset management—Part 2: Software subsequent final release of the report.
identification tag, which establishes a specification for Additionally, NIST has worked with the TCG to integrate
tagging software to support identification and management. SWID tags into the Trusted Network Communications (TNC)
An updated revision of this standard, ISO/IEC 19770-2:2015, protocol, through the SCAP Messages for IF-M specification
was published on October 1, 2015. The software identification that will be discussed below.
(SWID) data model defined by this standard describes an
The information provided within SWID tags enhances
XML format for software publishers to provide authoritative
the SCAP use cases by providing authoritative information
identification, categorization, software relationships
that can be used to create Common Platform Enumeration
(e.g., dependency, bundling, and patch), executable and
(CPE) names, to support the targeting of checklists, and to
library footprint details, and other metadata for software.
associate software flaws to products, based on a defect in
This information can be used to support operational
a software library or executable. CSD will be working on a
and cybersecurity use cases around managing software
number of reports in FY 2016 that provide further guidance
deployments, managing software licenses, managing
for using SWID tags to address these use cases.
software vulnerabilities and related software patches, and
assessing secure software configurations.
Development of Security Automation
To supplement the requirements in ISO/IEC 19770- Consensus Standards
2:2015, CSD has been working with DHS and NSA on the CSD has been promoting the broad international
development of NISTIR 8060, Guidelines for the Creation adoption of SCAP by encouraging the integration of SCAP
of Interoperable Software Identification (SWID) Tags. into other standards, and by adapting SCAP to address
NISTIR 8060 provides an overview of the capabilities and specific gaps and challenges. CSD has continued its
usage of software identification (SWID) tags as part of a collaboration with industry partners in the IETF Security
comprehensive software lifecycle. This report introduces Automation and Continuous Monitoring (SACM) working
SWID tags in an operational context, provides guidelines for group. This working group provides a venue for advancing
the creation of interoperable SWID tags, and highlights key appropriate SCAP specifications into international standards
usage scenarios for which SWID tags are applicable. Figure and addressing identified gap areas. The current scope of
24 illustrates how SWID tags support multiple elements work for SACM includes identifying and/or defining the
of the software product life cycle, including deployment, transport protocols and data formats needed to support
Figure 24: SWID Tags Support the Software Product Lifecycle
7 1
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

the  collection  and  evaluation  of  a  device  state  against  Internet Security (CIS), and the TCG to bring existing work
expected values. Over the past twelve months, the SACM  into the IETF SACM working group to include OVAL and
working group has been working on identifying use cases,  specifications related to the TNC protocol.
requirements, and architectural models to inform decisions
In FY 2015, the SACM use cases were published by the
about existing specifications and standards that can be
IETF as Request for Comments (RFC) 7632.
referenced, required modifications or extensions to existing
specifications and standards, and any gaps that need to  The working group has been developing the following
Internet Drafts:
be addressed. CSD is working with DHS, the Center for
|     | INTERNET DRAFT |     |     |     | PURPOSE |     |
| --- | -------------- | --- | --- | --- | ------- | --- |
https://datatracker.ietf.org/doc/draft-ietf-sacm- Definition of the common terminology used within a
| terminology/ |     |     |     | number of working-group documents. |     |     |
| ------------ | --- | --- | --- | ---------------------------------- | --- | --- |
https://datatracker.ietf.org/doc/draft-ietf-sacm- Listing architectural and specification requirements for
| requirements/ |     |     |     | SACM specifications. |     |     |
| ------------- | --- | --- | --- | -------------------- | --- | --- |
https://datatracker.ietf.org/doc/draft-ietf-sacm- Definition of the SACM architecture to inform
| architecture/ |     |     |     | development of transports. |     |     |
| ------------- | --- | --- | --- | -------------------------- | --- | --- |
https://datatracker.ietf.org/doc/draft-ietf-sacm- Definition of the SACM information model to inform
| information-model/ |     |     |     | development of data models. |     |     |
| ------------------ | --- | --- | --- | --------------------------- | --- | --- |
For more information, please refer to: http://datatracker. identifying and exchanging vulnerability information across
| ietf.org/wg/sacm/charter/ |     |     |     | disparate vulnerability databases. |     |     |
| ------------------------- | --- | --- | --- | ---------------------------------- | --- | --- |
CSD also worked with government and industry partners  For more information, please visit: http://www.first.org/
| in the TCG to define a number of specifications related to  |     |     |     | global/sigs. |     |     |
| ----------------------------------------------------------- | --- | --- | --- | ------------ | --- | --- |
the TNC protocol. The first such publication is the TNC SCAP
Through work with international standards-developing
Messages for IF-M specification that supports carrying SCAP
organizations (SDOs), SCAP and related security automation
content and results over the TNC protocols. The second is
capabilities are expected to evolve and expand in support of
the TNC Enterprise Compliance Profile (ECP) and related
the growing need to define and measure effective security
| specifications  | that  support  | the  exchange  | of  SWID  data  |     |     |     |
| --------------- | -------------- | -------------- | --------------- | --- | --- | --- |
controls, assess and monitor ongoing aspects of information
over the TNC protocols. The ECP enables the collection of
|     |     |     |     | security,  remediate  | noncompliance,  | and  successfully  |
| --- | --- | --- | --- | --------------------- | --------------- | ------------------ |
SWID data from a device for use by external tools to provide
manage systems in accordance with the Risk Management
| software  | inventory  information.  | SCAP  | and  SWID  data  |     |     |     |
| --------- | ------------------------ | ----- | ---------------- | --- | --- | --- |
Framework described in SP 800-37 Revision 1, Guide for
collected using these mechanisms may be optionally used
Applying the Risk Management Framework to Federal
for network access-control decision making, allowing the
Information Systems: A Security Life Cycle Approach.
device state to be evaluated when devices connect and on
Standards that are developed and published by these SDOs
an ongoing basis thereafter.
will be considered for inclusion in future revisions of SCAP.
| For  | more  information  | on  these  | specifications,  |     |     |     |
| ---- | ------------------ | ---------- | ---------------- | --- | --- | --- |
For More Information, See:
| please  | visit:  http://www.trustedcomputinggroup.org/ |     |     |     |     |     |
| ------- | --------------------------------------------- | --- | --- | --- | --- | --- |
http://scap.nist.gov/
| resources/tnc_scap_messages_for_ifm,  |     |     | and  http://www. |     |     |     |
| ------------------------------------- | --- | --- | ---------------- | --- | --- | --- |
trustedcomputinggroup.org/resources/tnc_endpoint_
CONTACT:
compliance_profile_specification.
| Finally, CSD has worked with the FIRST by participating    |     |     |     | Mr. David Waltermire  |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --------------------- | --- | --- |
| in two Special Interest Groups (SIGs). The CVSS SIG (CVSS- |     |     |     | (301) 975-3390        |     |     |
SIG) is focused on maintaining and improving the CVSS  david.waltermire@nist.gov
scoring model, based on community feedback. The CVSS-
SIG published CVSS Revision 3 (CVSS v3) in June 2015. The
second SIG, the Vulnerability Reporting and Data eXchange
SIG (VRDX-SIG), researches and recommends methods for
72
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Security Automation Reference Data NVD is hosted and maintained by NIST and is sponsored
Through the NVD and the NCP, NIST is providing relevant by the Department of Homeland Security’s US-CERT.
and important reference data in the areas of vulnerability The use of SCAP data by commercial security products,
and configuration management. SCAP and the programs deployed in thousands of organizations worldwide, has
that leverage it are moving the information assurance extended NVD’s effective reach. Increasing demand for NVD
industry towards being able to standardize communications, XML data feeds (i.e., mechanisms that provide updated data
and towards the collection and storage of relevant data in from data sources) and SCAP-expressed content from the
standardized formats, as well as providing automated NVD website demonstrates an increased adoption of SCAP.
means for the assessment and remediation of systems for
The NVD continues to play a pivotal role in the Payment
both vulnerabilities and configuration compliance.
Card Industry (PCI) efforts to mitigate vulnerabilities in credit
National Vulnerability Database (NVD) card systems. PCI mandates the use of NVD vulnerability
Security automation reference data is currently severity scores in measuring the risk to payment card
housed within the NVD. The NVD is the U.S. Government servers worldwide and for prioritizing vulnerability patching.
repository of security automation data based on security PCI’s use of NVD severity scores helps enhance credit card
automation specifications. This data provides a standards- transaction security and protects consumers’ personal
based foundation for the automation of software asset, information.
vulnerability, and security configuration management; For More Information, See:
security measurement; and compliance activities. This data
https://nvd.nist.gov
supports security automation efforts based on the SCAP. The
NVD includes databases of security configuration checklists
CONTACTS:
for the NCP, listings of publicly known software flaws,
product names, and impact metrics. A formal validation Mr. Harold Booth Mr. Robert Byers
program tests the ability of vendor products to use some (301) 975-8441 (301) 975-3279
forms of security automation data, based on a product’s harold.booth@nist.gov robert.byers@nist.gov
conformance in support of specific enterprise capabilities.
SCAP defines the structure of standardized software National Checklist Program (NCP)
flaws and security configuration reference data, also known
There are many threats to information technology (IT),
as SCAP content. This reference data is provided by the NVD
ranging from remotely launched network service exploits to
(http://nvd.nist.gov/).
malicious code spread through infected emails, websites,
As of October 2015, the NVD contained the following and downloaded files. Vulnerabilities in IT products are
resources: discovered daily, and many ready-to-use exploitation
techniques are widely available on the Internet. Because IT
• Over 72,000 vulnerability advisories, with an average
products are often intended for a wide variety of audiences,
of 40 new vulnerabilities added daily;
restrictive security configuration controls are usually not
• 82 SCAP-expressed checklists containing thousands
enabled by default. As a result, many out-of-the box IT
of low-level security configuration checks that can be
products are immediately vulnerable. In addition, identifying
used by SCAP-validated security products to perform
a reasonable set of security settings that achieve balanced
automated evaluations of the system state;
risk management is a complicated, arduous, and time-
• 248 non-SCAP security checklists (e.g., English prose consuming task, even for experienced system administrators.
guidance and configuration scripts);
To facilitate the development of security configuration
• 249 U.S. Computer Emergency Readiness Team (US- checklists for IT products and to make checklists more
CERT) alerts; 4,402 US-CERT vulnerability summaries; organized and usable, CSD established the National
and 10,286 SCAP machine-readable software flaw Check-list Program (NCP) in furtherance of its statutory
checks, and; responsibilities under the Federal Information Security
Management Act (FISMA) of 2002, Public Law 107-347, and
• A product dictionary with over 106,000 operating sys-
also under the Cybersecurity Research and Development Act,
tem, application, and hardware name entries; and over
which mandates that NIST “develop, and revise as necessary,
58,000 vulnerability advisories translated into Spanish.
a checklist setting forth settings and option selections that
minimize the security risks associated with each computer
73
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

hardware or software system that is, or is likely to become, To assist users in identifying automated checklist content,
widely used within the Federal Government.” In February NCP groups these checklists into tiers, from Tier I to Tier IV.
2008, revised Part 39 of the Federal Acquisition Regulation The NCP uses the tiers to rank checklists according to their
(FAR) was published. Paragraph (d) of section 39.101 states, automation capability. Tier III and IV checklists include fully
“In acquiring information technology, agencies shall include vetted SCAP content that has successfully demonstrated
the appropriate IT security policies and requirements, conformance to the requirements outlined in SP 800-126.
including use of common security configurations available Tier III & IV checklists are considered production-ready and
from the NIST website at http://checklists.nist.gov. Agency are intended for use with SCAP-validated products.
contracting officers should consult with the requiring official
Tier II checklists document recommended security
to ensure the appropriate standards are incorporated.”
settings in a machine-readable, nonstandard format, such
In Memorandum M-08-22, OMB mandated the use of as a proprietary format or a product-specific configuration
SCAP-validated products for the continuous monitoring of script. Tier I checklists are prose-based and contain no
Federal Desktop Core Configuration (FDCC) compliance. machine-readable content. Users can browse the checklists,
The NCP strives to encourage and assist federal agencies based on the checklist tier, IT product, IT product category,
with these mandates. or authority, and through a keyword search that searches the
checklist name and summary for user specified terms. The
The goals of the NCP are to:
search results show the detailed checklist metadata and a
• Facilitate the development and sharing of checklists by
link to any SCAP content for the checklist, as well as links to
providing a formal framework for checklist developers
any supporting resources associated with the checklist.
to submit checklists to NIST;
To assist checklist developers, the NCP provides both
• Provide guidance to developers to help them create
manual and automated interfaces to facilitate the submission
standardized, high-quality checklists that conform to
and maintenance processes. The manual interface consists
common operation environments;
of a web application that guides the submitter through
• Help developers and users by providing guidelines for the data entry process to ensure that all of the required
making checklists better documented and more usable; information is submitted. The submission is validated
upon review, and a report is returned to the submitting
• Encourage software vendors and other parties to de-
organization, verifying either acceptance or rejection, based
velop checklists;
on the criteria requirements. For instance, Tier III and Tier
• Provide a managed process for the review, update, and
IV checklists require validation using the SCAP Content
maintenance of checklists;
Validation Tool (this tool is available for download via
• Provide an easy-to-use repository of checklists; and http://scap.nist.gov/revision/1.2/#tools).
• Encourage the use of automation technologies (e.g., The NCP is defined in SP 800-70 Revision 3, National
SCAP) for checklist application. Checklist Program for IT Products—Guidelines for Checklist
Users and Developers, which can be found at http://csrc.nist.
NCP added 100 new checklists in FY 2015, bringing the
gov/publications/PubsSPs.html.
number of checklists posted on the website to 353 (see
http://checklists.nist.gov). Of that total, 153 of the checklists, For More Information, See:
addressing 86 platforms, are SCAP-expressed and can be
https://checklists.nist.gov
used with SCAP-validated products. This represents a 45
% increase in the number of SCAP-expressed checklists
CONTACT:
when compared to FY 2014, demonstrating continual use
and adoption of this automated means of expressing and Mr. Stephen Quinn
consuming checklist content. (301) 975-6967
stephen.quinn@nist.gov
Organizations can use checklists obtained from the
NCP website for automated security configuration patch
assessment. The NCP currently hosts SCAP checklists for
Internet Explorer 9.0, Internet Explorer 10.0, Office 2010,
Red Hat Enterprise Linux, Windows 7, Windows 8, Windows
Server 2012, and other products.
74
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

United States Government Apple OS X Security Configuration
Configuration Baseline (USGCB) / CSD is working to develop secure system configuration
FDCC Baselines baselines supporting different operational environments for
The United States Government Configuration Baseline Apple OS X Version 10.10, “Yosemite.” These configuration
(USGCB) initiative creates security configuration baselines guidelines will assist organizations with hardening OS X
for information technology (IT) products that are widely technologies and provide a basis for unified controls and
deployed across the federal agencies. The project originally settings for OS X workstations and for mobile system
evolved from the Federal Desktop Core Configuration (FDCC) security configurations for federal agencies.
mandate originally described in a March 2007 memorandum The configurations are based on a collection of resources,
from OMB, Memorandum M-07-11. The purpose of the USGCB including the existing NIST OS X configuration guidance,
program is to help improve information security and reduce the OS X security configuration guide, the Department of
overall IT operating costs by providing commonly accepted Defense (DOD) OS X Recommended Settings, and the
and agreed upon security configurations for major operating Defense Information Systems Agency (DISA) OS X Security
systems and applications. Technical Implementation Guide (STIG). The project team
Through the NCP described in SP 800-70 Revision 3, aggregated 400 initial settings, determined which settings
a baseline submitter may express interest in submitting a to include in the configuration baseline, and determined
candidate for use in the USGCB program. appropriate values for each included setting. The desired
configuration items have been established, and the team is
CSD provides ongoing support for the USGCB
continuing to develop shell scripts that apply the settings
automation content, including periodic updates to the
to an OS X 10.10 system. The settings are organized into
existing content, encouraging vendors to submit candidates,
three key baselines, which are appropriate for different
assisting USGCB users in continuously monitoring and
environments:
assessing security compliance of information systems
within their environment. This ongoing monitoring element • The Enterprise baseline is appropriate for centrally
supports the Risk Management Framework described in managed, networked systems;
SP 800-37 Revision 1. It also supports the Core functions • The Small Office Home Office baseline, sometimes
of the Cybersecurity Framework, providing USGCB users called Standalone, describes small, informal computer
with settings that protect digital assets and supports the installations that are used for home or business pur-
detection of suspicious activity. poses; and
During FY 2016, the USGCB program will continue to • The Specialized Security-Limited Functionality baseline
provide ongoing maintenance of the baseline artifacts and is appropriate for systems where security requirements
to consider additional applicable platforms as authored are more stringent and where the implementation of
and submitted by the platform vendors, as well as other security safeguards is likely to reduce functionality.
organizations that wish to contribute candidate content.
SCAP, defined and discussed in an earlier section of this
For More Information, See: report, will be used to express configuration settings and
http://usgcb.nist.gov check system configuration compliance.
During FY 2013, CSD provided a block of initial settings
CONTACT: to Apple and these settings were posted for the Apple
community on a periodic basis for public review, discussion,
Team email: usgcb@nist.gov
correction and agreement. Each setting has a designated
Mr. Stephen Quinn Common Configuration Enumeration (CCE) number, which
(301) 975-6967 aids in the long-term tracking of the setting. Ultimately, the
stephen.quinn@nist.gov settings will be tested and included in the configuration
baselines. In addition, CSD started the production of a draft
guideline, Guide to Securing Apple OS X 10.8 Systems for
IT Professionals. This guidance, which is similar in structure
to the SP 800-68, Windows XP Security Guide, focuses on
75
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

providing detailed information about the security of Apple TECHNICAL SECURITY
OS X, and providing security configuration guidelines for all
METRICS
users of the Apple OS X 10.8 operating system.
During FY 2014, a majority of all proposed settings were
Security Risk Analysis of Enterprise
scripted. The corresponding spreadsheet batches have been
Networks Using Attack Graphs
sent to Apple for feedback; approximately 230 settings are
now completed. Settings have also been implemented on OS The protection of computer networks from malicious
X 10.9, when possible. Work on the draft guideline, Guide to intrusions is critical to the economy and security of the
Securing Apple OS X 10.8 Systems for IT Professionals, was nation. Vulnerabilities are regularly discovered in software
temporarily suspended while configuration setting research applications that are exploited to stage cyber attacks.
was performed, but was resumed in FY 2015. System administrators need objective metrics to guide and
justify decision making as they manage the security risk
In FY 2015, CSD focused on the OS X 10.10 operating
of enterprise networks. The objective of this research is to
system for security testing. CSD finalized and tested the
develop a standard model for the security risk analysis of
entire security configuration of 230 settings for OS X 10.10
computer networks. A standard model will enable NIST to
and has continued updating the draft publication that was
answer questions such as “Are we more secure now than
started for OS X 10.8 and has now been focused on OS X
yesterday?” or “How does the security of one network
10.10. For several months, one of the script’s three profiles
configuration compare with another one?” Also, having a
was deployed on select CSD systems for extensive testing.
standard model to measure network security will allow users,
So far, results have been positive.
vendors, and researchers to evaluate methodologies and
In FY 2016, CSD plans to release the draft publication, products for network security in a coherent and consistent
Guide to Securing Apple OS X 10.10 Systems for IT manner.
Professionals, for at least one public comment period, and
CSD has approached the challenge of network security
plans to release a final version after incorporating changes
analysis by capturing vulnerability interdependencies
from the comment period(s). CSD will continue to refine the
and measuring security, based on how real attackers have
script and add more settings to the configuration.
penetrated networks. CSD’s methodology for security risk
For More Information, See: analysis is based on attack graphs. CSD analyzes attack
paths through a network, providing a probabilistic metric of
http://csrc.nist.gov/projects/apple-os/
the overall system risk. Through this metric, CSD analyzes
trade-offs between security costs and security benefits.
CONTACTS:
Computer systems are vulnerable to both known and
Mr. Mark Trapnell Mr. Lee Badger
zero-day attacks. Enterprises have begun to move parts
(301) 975-4091 (301) 975-3176
of their networks from a traditional infrastructure into
mark.trapnell@nist.gov lee.badger@nist.gov
cloud computing environments. Cloud providers can offer
virtual servers that can be rented on demand by users. This
Mr. Murugiah Souppaya
paradigm enables cloud customers to acquire computing
(301) 975-4102
resources with high efficiency, low cost and great flexibility.
murugiah.souppaya@nist.gov
However, it also introduces many security problems that
need to be solved.
In FY 2015, CSD attempted to model the problem of
cloud security using a cloud-level attack graph. An attacker
can create stealthy bridges (i.e., a covert connection
between disparate networks that should be isolated) in a
cloud environment. These stealthy bridges can be created
using zero day vulnerabilities that cannot be detected by
vulnerability scanners. The stealthy bridges can be used to
construct a multi-step attack path and facilitate a subsequent
intrusion process across enterprise islands in a cloud. CSD
has developed a new technique to detect potential attacks
in a Cloud using a probabilistic attack graph model. CSD
76
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

published a paper, Inferring the Stealthy Bridges Between countries, isolate a set of countries from the Internet, or
Enterprise Network Islands in Cloud Using Cross Layer break the Internet up into non-communicating clusters
Bayesian Networks, for the Tenth International Conference (the research was published in the International Journal
on Security in Communication Networks, in Beijing, which of Computer Science: Theory and Applications, as well
was held October 24-26, 2015. as in the proceedings of the Workshop for the Security
of Emerging Network Technologies).
In FY 2016, CSD plans to develop new techniques and
metrics to detect attacks on Cloud Computing and for • The research team showed how to leverage Internet
network forensics analysis using Bayesian Networks. CSD Protocol Version 6 (IPv6) network migrations to en-
also plans to publish the results as a NIST report and as white hance security capabilities. This was done through an
papers in conferences and journals. evaluation of how to optimize the placement of defen-
sive resources in specially secured IPv6 networks. The
For More Information, See:
optimal placements best limit the movement of internal
http://csrc.nist.gov/groups/SNS/security-risk-analysis-
attackers to a small set of hosts or else force them to
enterprise-networks/
penetrate through the special security boundaries (the
research was published in the journal Data and Appli-
CONTACT: cations Security and Privacy).
Dr. Anoop Singhal • In previous work, the team discovered a critical weak-
(301) 975-4432 ness in the most widely cited Threshold Random Walk
anoop.singhal@nist.gov (TRW) network scan detection algorithm that enabled
a full circumvention by attackers. To mitigate the prob-
lem, we invented a scan detection methodology that
Algorithms for Intrusion Measurement
will detect TRW circumvention activity and that also
The Algorithms for Intrusion Measurement (AIM)
acts as an effective general-purpose scan detection
project furthers measurement science in designing and
algorithm. However, we find that the most effective
implementing algorithms to both detect attackers and
approach is a composite solution that combines our
limit their ability to intrude into a system. Most of the
approach with TRW (the research was published in the
work leverages graph theory (the math of dots and lines)
journal of Security Informatics).
and algorithmic complexity analysis (the math around fast
computation). In performing this work, the AIM project In FY 2016, the AIM project will work on new methods
seeks to enhance the nation’s ability to defend itself from for network anomaly detection, efficient representations
network-borne attacks. for attack graphs, efficient computation of access control
policy to restrict insider attacks, vertex partitioning on
This scientific research is conducted in partnership
massive graphs to enable security resiliency analyses, and
with the Army Research Laboratory (ARL), the University
methods for using attack graphs to perform defense-in-
of Maryland, and the Center for Applied Internet Data
depth measurements.
Analysis. ARL’s participation helps focus the work on
solving immediate critical problems facing U.S. Government For More Information, See:
networks. However, research solutions are made publicly http://csrc.nist.gov/projects/aim/
available and are designed to be generally applicable to as
many environments as possible.
CONTACT:
In FY 2015, the AIM project completed research in
Mr. Peter Mell
several areas: measurements of Internet resilience of
(301) 975-5572
colluding country attacks, the optimal placement of
peter.mell@nist.gov
defensive resources in Internet Protocol (IP) v6 networks,
and circumvention-resistant network scan detection. More
specifically, the project team accomplished the following:
• The team analyzed the resilience of the Internet with
respect to countries colluding in using their influence
over the Internet infrastructure to disconnect two
7 7
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Automated Combinatorial Testing combinatorial measurement tools; input modeling and
Software developers often encounter failures that result fault location tools; a provisional patent application on the
from an unexpected interaction between components. NIST oracle-free testing method; plus seminars at a number of
research has shown that most failures are triggered by one conferences, universities, and federal agencies.
or two parameters, and progressively fewer by three, four, or Plans for FY 2016 include combinatorial testing for
more parameters (see Figure 25 below), a relationship that big data software; initiation of a new CRADA project;
is called the Interaction Rule. These results have important measurement of input model combination coverage of
implications for testing. If all faults in a system can be security-critical software; a beta release of tools for testing
triggered by a combination of n or fewer parameters, then to the modified condition decision coverage test criterion
testing all n-way combinations of parameters can provide for life-critical software; developing tools to implement
very strong fault detection efficiency. These methods are oracle-free testing methods; analysis of empirical data
being applied to software and hardware testing for reliability, on failures; further development of methods and tools for
safety, and security. CSD’s focus is on empirical results and fault localization; and seminars, workshops, and tutorials at
real-world problems. professional meetings and research labs.
Project highlights for FY 2015 include the publication of
For More Information, See:
a paper on a new method of “oracle-free testing”, a form
http://csrc.nist.gov/groups/SNS/acts/
of consistency checking using two-layer covering arrays
with equivalence classes to automatically detect a large
CONTACTS:
class of software faults; invited lectures at conferences and
universities; leading the fourth International Workshop on
Mr. Rick Kuhn Dr. Raghu Kacker
Combinatorial Testing, held in conjunction with the eighth
(301) 975-3337 (301) 975-2109
IEEE International Conference on Software Testing; initiating
kuhn@nist.gov raghu.kacker@nist.gov
research on using combinatorial methods to reduce the cost
of high assurance for life-critical software, tools and methods
Roots of Trust
for locating faults from test results; and analyzing the factors
Modern computing devices consist of various hardware,
involved in different types of software faults. Collaborators
firmware, and software components at multiple layers of
include researchers from the University of Texas at Arlington,
abstraction. Many security and protection mechanisms are
the University of Texas at Dallas, East Carolina University,
currently rooted in software that, along with all underlying
and Duke University.
components, must be trusted and not tampered with. A
vulnerability in any of those components could compromise
the trustworthiness of the security mechanisms that rely
upon those components. Stronger security assurances may
be possible by grounding security mechanisms in roots of
trust.
Roots of trust are highly reliable and secure hardware,
firmware, and software components that perform specific,
critical security functions. Because roots of trust are
inherently trusted, they must be secure by their design. As
such, many roots of trust are implemented in hardware or
protected firmware so that malware cannot tamper with
the functions they provide. Roots of trust provide a firm
foundation from which to build security and trust.
Figure 25: Interaction Rule Graph CSD’s work aims to encourage the use of roots of
trust in computers to provide stronger security assurances.
Technology transfer activities included the publication
A focus area for this work has been securing firmware.
of a number of technical papers and software distribution;
Previous guidelines by CSD described methods to protect
publication of the results of a Cooperative R&D (CRADA)
boot firmware, commonly known as the Basic Input/Output
project with Lockheed Martin; release of enhanced
System (BIOS) in PC clients and servers. In FY 2015, the first
7 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

of these guidelines, SP 800-147, BIOS Protection Guidelines,
was submitted to ISO/IEC JTC 1/SC27 for standardization as
ISO/IEC 19678:2015.
In FY 2016, CSD will continue to work with the computer
industry on the use of roots of trust to improve the security
of BIOS and other firmware. As part of this effort, CSD is
researching techniques and requirements for securing
firmware throughout the platform. This effort will consider
methods to protect this firmware from unauthorized
changes, detect accidental or malicious corruption, and
recover from destructive attacks.
For More Information, See:
http://csrc.nist.gov/projects/root-trust/
CONTACT:
Mr. Andrew Regenscheid
(301) 975-5155
andrew.regenscheid@nist.gov
7 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

HONORS AND AWARDS
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Department of Commerce
Gold Medal Award
Mr. Jon Boyens, Ms. Naomi Lefkovitz, Ms. Suzanne Lightman,
Ms. Victoria Pillitteri, Mr. Matthew Scholl, and Mr. Kevin Stine
Computer Security Division;
Ms. Donna Dodson, and Mr. Adam Sedgewick, Information
Technology Laboratory Office; and
Ms. Lisa Carnahan, NIST Standards Coordination Office
(former ITL team member)
Figure 26: Gold Medal Award Recipients
(left to right): Department of Commerce Deputy Secretary Bruce Andrews, Suzanne Lightman, Kevin
Stine, Naomi Lefkovitz, Adam Sedgewick, Donna Dodson, Matthew Scholl, Victoria Pillitteri, Jon
Boyens, and Dr. Willie May, Under Secretary of Commerce for Standards and Technology and NIST
Director (Not Pictured: Lisa Carnahan)
The group is recognized for its exceptional leadership and outstanding technical achievement in
developing an innovative framework to improve the cybersecurity of our nation’s critical infrastructure.
In Executive Order 13636, the President directed NIST to create a Cybersecurity Framework to manage
and reduce cybersecurity risk across the nation’s critical infrastructure sectors. The team convened a
highly diverse community to achieve consensus on a framework of standards, guidelines, and practices
to identify, assess, and manage cybersecurity risk.
8 1
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: HONORS AND AWARDS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Department of Commerce
Silver Medal Award
Mr. Richard Kuhn, Computer Security Division; and
Dr. Raghu Kacker, Applied and Computational
Mathematics Division
Figure 27: Silver Medal Award Recipients
(left to right): Department of Commerce Deputy Secretary Bruce Andrews, Richard Kuhn,
Dr. Raghu Kacker, and Dr. Willie May, Under Secretary of Commerce for Standards and Technology
and NIST Director
The group is recognized for outstanding technical accomplishments in the development of the first
efficient tool for generating high-strength software testing plans, resulting in cost savings and more
reliable products. The team has developed software tools that use a novel combinatorial testing meth-
odology. This methodology enables software developers to generate the smallest number of test cases
needed to identify the most critical and elusive software bugs, those caused by interactions among input
parameters. The team has made their tool, Automated Combinatorial Testing of Software (ACTS), widely
available, and it is now used by major software companies and many government agencies.
8 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Dr. Ari Schwartz Receives Federal 100 Award
Ari Schwartz, ITL’s Senior Internet Policy Advisor, who is on detail to the Executive Office of
the President as the Senior Director for Cybersecurity, National Security Council, received
a Federal 100 Award from Federal Computer Week. Dr. Schwartz was recognized for his
deep knowledge and experience as a “voice of reason” and an advocate for a wide range of
cybersecurity activities.
Donna Dodson Named one of D.C.’s Top 50 Women
in Technology
For the second year in a row, Donna Dodson has been named to D.C.’s Top 50 Women in
Technology by FedScoop. Each year, FedScoop salutes a selection of D.C.’s Top Women in
Technology, “whose vibrant energy, determination, imagination and leadership are making a
monumental difference in the Federal Government IT community.” Other notable recipients this
year include Commerce Secretary Penny Pritzker and former NIST Director Arati Prabhakar.
NIST’s Dr. Ron Ross Wins Three Top Awards
for Advancing Cybersecurity
Dr. Ron Ross, leader of the Federal Information Security Management
Act (FISMA) Implementation Project and an international cybersecurity
ambassador, was recognized by three organizations for contributions to
the field of cybersecurity:
• Dr. Ross was presented the Samuel J. Heyman Service to America
Medal in the area of Homeland Security and Law Enforcement. The
medal, often referred to as the “Sammie” award, is considered the
“Oscar” award of government service. It highlights excellence in the
federal workforce and inspires other talented and dedicated individuals
to enter public service. He received the honor for “instituting a state-
Figure 28: Department of Commerce Depu- of-the-art risk assessment system that has protected federal computer
ty Secretary Bruce Andrews (left) presents networks from cyberattacks and helped secure information critical to
a Sammie Award to Dr. Ross on Oct. 7, 2015 our national and economic security.”
in Washington, D.C.’s Andrew W. Mellon
• Government Computer News (GCN) magazine named Dr. Ross as Gov-
Auditorium.
ernment Executive of the Year for his contributions to securing federal
information systems.
• Dr. Ross was also inducted into the National Cyber Security Hall of Fame. The organization honors innovative indi-
viduals and organizations for their vision and leadership in creating foundational building blocks of the cybersecurity
industry.
As a result of his widely used work, Dr. Ross has been called on by U.S. industry, academia and governments around the
world to help their efforts to protect information. He has led U.S. cybersecurity teams to Australia, India, Japan, Canada,
and the European Union, promoting effective information security concepts and best practices.
Credit: NIST Connections staff newsletter and Evelyn Brown, NIST Public Affairs Office
8 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: HONORS AND AWARDS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Mr. Daniel Benigni Receives INCITS Lifetime Achievement
Award
The InterNational Committee for Information Technology Standards (INCITS) organization
presented Dan Benigni with a Lifetime Achievement Award in recognition of his continuous and
outstandingly effective support for the development of standards in his role of managing the
US Standards Committee on Cybersecurity (CS1).
This award is presented to only one INCITS participant annually, to a member who has
demonstrated a long-time commitment to INCITS and its national and international
standardization activities. The awardee must have demonstrated long-standing participation
(ten or more years) in national and/or international standards development. Most importantly,
it reflects the team spirit of the CS1 committee, whose members work together to reach the
shared goal of promulgating security standards that will benefit U.S. industry and users over the
long term.
Mr. Randall (Randy) Easter Receives INCITS Technical
Excellence Award
Mr. Easter was presented with the Technical Excellence Award, also from INCITS. INCITS is the
primary U.S. forum dedicated to creating technology standards for innovation. This award
is presented to no more than four participants to recognize visible and significant technical
contributions to the work of a given national or international technical committee (TC), based
upon a minimum of three years of TC participation by the awardee.
8 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

COMPUTER SECURITY
DIVISION PUBLICATIONS
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

COMPUTER SECURITY Publications are available for download from CSRC
(http://csrc.nist.gov/publications/), including several NIST
DIVISION PUBLICATIONS
technical series:
During FY 2015, CSD staff authored a significant number • FIPS (http://csrc.nist.gov/publications/PubsFIPS.html);
of computer, cyber, and/or information security-related • Special Publications (http://csrc.nist.gov/publications/
standards, guidelines, recommendations and research PubsSPs.html);
findings through the NIST technical series, journal articles,
• NISTIRs (http://csrc.nist.gov/publications/PubsNISTIRs.
conference papers, and other published documents.
html); and
In an effort to provide greater access to NIST’s broad
• ITL Bulletins (http://csrc.nist.gov/publications/Pub-
portfolio of security and privacy publications, CSD began
sITLSB.html).
posting additional Special Publications and NISTIRs on the
CSRC that were developed by other components at NIST, The following lists summarize some of the top CSD
such as the National Cybersecurity Center of Excellence publications downloaded in FY 2015:
(NCCoE) and National Strategy for Trusted Identities in
Top 10 Most-Downloaded CSD
Cyberspace (NSTIC). For example, CSRC now displays
Publications in NIST Technical Series
publications from the new NIST Cybersecurity Practice Guide
(i.e., FIPS, SP 800s, NISTIRs, and ITL
series, SP 1800, authored by the NCCoE staff. The first three
SP 1800 drafts were posted for public comment, describing Bulletins):
work that closely relates to CSD standards, guidelines and 1. SP 800-53 Revision 4, Security and Privacy Controls
research. for Federal Information Systems and Organizations;
By posting cybersecurity and privacy draft publications 2. SP 800-61 Revision 2, Computer Security Incident
from other NIST components on CSRC, CSD aims to provide Handling Guide;
greater visibility during public comment periods and to
3. SP 800-53A Revision 4, Assessing Security and
provide a primary resource for stakeholders to access a
Privacy Controls in Federal Information Systems
broad range of NIST cybersecurity and privacy publications.
and Organizations: Building Effective Assessment
In FY 2015, CSD posted a substantial number of final Plans;
publications to CSRC, including two FIPS, fifteen Special
4. SP 800-88 Revision 1, Guidelines for Media
Publications, and seven NISTIRs. The release of FIPS 202,
Sanitization;
SHA-3 Standard, in August 2015 was the culmination of
5. SP 800-37 Revision 1, Guide for Applying the Risk
many years of effort by the Cryptographic Technology Group
Management Framework to Federal Information
to develop a next-generation standard for secure hashing.
Systems: A Security Life Cycle Approach;
FIPS 202 specifies a family of fixed-length hash functions
and extendable-output functions that complement the 6. NISTIR 7298 Revision 2, Glossary of Key Information
existing SHA-2 algorithms specified in FIPS 180-4, Secure Security Terms;
Hash Standard (SHS).
7. SP 800-171, Protecting Controlled Unclassified
CSD continued to engage the public by posting fifteen Information in Nonfederal Information Systems and
SPs and thirteen NISTIRs as drafts for public comment. That Organizations;
included Draft NISTIR 8060, Guidelines for the Creation
8. SP 800-30 Revision 1, Guide for Conducting Risk
of Interoperable Software Identification (SWID) Tags, for
Assessments;
which three iterations were released during short, two-
9. SP 800-63-2, Electronic Authentication Guideline;
week public comment periods. Comments were requested
and
on three existing publications to determine what changes
or approaches should be taken, prior to releasing an official 10. SP 800-52 Revision 1, Guidelines for the Selection,
draft for public comment. Those publications include Configuration, and Use of Transport Layer Security
i) SP 800-63-2, Electronic Authentication Guideline, ii) (TLS) Implementations.
Security Content Automation Protocol (SCAP) version 1.3
and iii) the potential use of ISO/IEC 19790:2012 as the U.S.
federal standard for cryptographic modules (as a potential
successor to FIPS 140-2).
8 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

| Top 3 FIPS: |           |       |        |                              |     |     | FY 2015 Computer Security Division  |     |     |     |     |
| ----------- | --------- | ----- | ------ | ---------------------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
|             | 1.  FIPS  | 202,  | SHA-3  | Standard: Permutation-Based  |     |     | Publications                        |     |     |     |     |
Hash and Extendable-Output Functions;
|     |     |     |     |     |     |     | The  Computer      | Security        | Division  | uses      | multiple  NIST  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --------------- | --------- | --------- | --------------- |
|     |     |     |     |     |     |     | Technical  Series  | to  promulgate  |           | security  | standards,      |
2.  FIPS 201-2, Personal Identity Verification (PIV) of
Federal Employees and Contractors; and guidelines,  recommendations,  research,  and  additional
background material. Those series include FIPS, SPs, NISTIRs
3.  FIPS 186-4, Digital Signature Standard (DSS).
and ITL Bulletins. Links to these publications are available at
Top 3 NISTIRs: http://csrc.nist.gov/publications.  As  described  earlier,  in
FY 2015, CSD began expanding its publication portfolio on
1.  NISTIR 7298 Revision 2, Glossary of Key Information
CSRC by posting cybersecurity and privacy SPs and NISTIRs
Security Terms;
from other NIST components. In some cases, CSD staff
2.  NISTIR 7628 Revision 1, Guidelines for Smart Grid
contributed to the development of a publication (e.g., Draft SP
Cyber Security; and
1800-3).  Others were developed by other ITL cybersecurity
3.  NISTIR  8023,  Risk Management for Replication  components (e.g., NCCoE and NSTIC), documents that are
Devices. closely related to CSD activities (e.g., Draft NISTIR 8062), or
describe CSD programs and standardization activities within
Top 3 ITL Bulletins: a greater context (e.g., Draft NISTIR 8074).
|     | 1.  February  |     | 2015, NIST Special Publication 800-88  |     |     |     |                |             |      |                |           |
| --- | ------------- | --- | -------------------------------------- | --- | --- | --- | -------------- | ----------- | ---- | -------------- | --------- |
|     |               |     |                                        |     |     |     | Additionally,  | each  year  | CSD  | staff  author  | numerous  |
Revision 1, Guidelines for Media Sanitization;
additional publications, including journal articles, conference
2.  October 2014, Release of NIST Special Publication
papers, and other papers that are widely disseminated. They
800-147B, BIOS Protection Guidelines for Servers;  range from basic research to high-level summaries of CSD
|     | and |     |     |     |     |     | activities. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
3.  January 2015, Release of NIST Special Publication
NIST Technical Series Publications −
|     | 800-53A,  |     | Revision  | 4,  Assessing  |     | Security  and  |     |     |     |     |     |
| --- | --------- | --- | --------- | -------------- | --- | -------------- | --- | --- | --- | --- | --- |
FIPS, SPs, NISTIRs, and ITL Bulletins
Privacy Controls in Federal Information Systems
Below are lists of NIST Technical Series publications
and Organizations.
|     |     |     |     |     |     |     | that  CSD  released  | on  CSRC  | as  | draft  documents  | or  as  |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --------- | --- | ----------------- | ------- |
Additionally, CSD shares its ongoing research efforts
final publications during FY 2015 (from October 1, 2014 to
| through  |     | other  | publications,  | such  | as  journal  | articles,  |     |     |     |     |     |
| -------- | --- | ------ | -------------- | ----- | ------------ | ---------- | --- | --- | --- | --- | --- |
September 30, 2015). Following the lists are abstracts for
| conference papers, books and other whitepapers. Although  |     |     |     |     |     |     | each publication. |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
available through NIST’s Publications Portal (http://www.
nist.gov/publication-portal.cfm), they can also be accessed
on CSRC’s Articles page (http://csrc.nist.gov/publications/
articles/). During FY 2015, more than 20 such documents
were published, and are listed in the next section (FY 2015
| Computer  |     | Security  | Division  | Publications)  |     | of  this  annual  |     |     |     |     |     |
| --------- | --- | --------- | --------- | -------------- | --- | ----------------- | --- | --- | --- | --- | --- |
report.
In FY 2016, CSD plans to release a new version of CSRC
that uses a content management system.  The publications
| interface      |     | on  the  | redesigned    | website      | will       | give  users    |     |     |     |     |     |
| -------------- | --- | -------- | ------------- | ------------ | ---------- | -------------- | --- | --- | --- | --- | --- |
| significantly  |     | greater  | capabilities  | for          | browsing,  | searching,     |     |     |     |     |     |
| downloading    |     | and      | sharing       | information  | on         | NIST’s  broad  |     |     |     |     |     |
collection of computer security and privacy publications.
8 7
CSD PUBLICATIONS  |  FY 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

DRAFT PUBLICATIONS
TABLE 3: NO DRAFT FIPS RELEASED DURING FY 2015
TABLE 4: SPECIAL PUBLICATIONS (SPs)
Publication Number Publication Title Draft Released
SP 800-177 Trustworthy Email September 2015
SP 800-171 Protecting Controlled Unclassified Information in Nonfederal
(2nd Draft) Information Systems and Organizations April 2015
(1st Draft) November 2014
SP 800-152 A Profile for U.S. Federal Cryptographic Key Management December 2014
Systems (CKMS)
SP 800-150 Guide to Cyber Threat Information Sharing October 2014
SP 800-131A Rev. 1 Transitions: Recommendation for Transitioning the Use of July 2015
Cryptographic Algorithms and Key Lengths
SP 800-125B Secure Virtual Network Configuration for Virtual Machine (VM) September 2015
Protection
SP 800-125A Secure Recommendations for Hypervisor Deployment October 2014
SP 800-90A Rev. 1 Recommendation for Random Number Generation Using November 2014
Deterministic Random Bit Generators
SP 800-85A-4 PIV Card Application and Middleware Interface Test Guidelines June 2015
(SP 800-73-4 Compliance)
SP 800-82 Rev. 2 Guide to Industrial Control Systems (ICS) Security February 2015
(2nd Draft)
SP 800-70 Rev. 3 National Checklist Program for IT Products: Guidelines for March 2015
Checklist Users and Developers
SP 800-57 Part 1 Recommendation for Key Management, Part 1: General September 2015
Rev. 4
SP 1800-3 Attribute Based Access Control September 2015
SP 1800-2 Identity and Access Management for Electric Utilities August 2015
SP 1800-1 Securing Electronic Health Records on Mobile Devices July 2015
TABLE 5: NIST INTERAGENCY OR INTERNAL REPORTS (NISTIRs)
Publication Number Publication Title Draft Released
NISTIR 8074 Volume 1: Report on Strategic U.S. Government Engagement August 2015
in International Standardization to Achieve U.S. Objectives for
Cybersecurity;
Volume 2: Supplemental Information
NISTIR 8062 Privacy Risk Management for Federal Information Systems May 2015
NISTIR 8060 Guidelines for the Creation of Interoperable Software
(3rd Draft) Identification (SWID) Tags August 2015
(2nd Draft) July 2015
8(1s8t Draft) May 2015
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

TABLE 5 (CONT.): NIST INTERAGENCY OR INTERNAL REPORTS (NISTIRs)
Publication Number Publication Title Draft Released
NISTIR 8058 Security Content Automation Protocol (SCAP) Version May 2015
1.2 Content Style Guide: Best Practices for Creating and
Maintaining SCAP 1.2 Content
NISTIR 8055 Derived Personal Identity Verification (PIV) Credentials (DPC) July 2015
Proof of Concept Research
NISTIR 8053 De-Identification of Personally Identifiable Information April 2015
NISTIR 8050 Executive Technical Workshop on Improving Cybersecurity April 2015
and Consumer Privacy: Summary and Next Steps
NISTIR 7966 Security of Interactive and Automated Access Management March 2015
(2nd Draft) Using Secure Shell (SSH)
NISTIR 7904 Trusted Geolocation in the Cloud: Proof of Concept July 2015
(2nd Draft) Implementation
NISTIR 7621 Rev. 1 Small Business Information Security: the Fundamentals December 2014
NISTIR 7511 Rev. 4 Security Content Automation Protocol (SCAP) Version 1.2 September 2015
Validation Program Test Requirements
FINAL APPROVED PUBLICATIONS
TABLE 6: FEDERAL INFORMATION PROCESSING STANDARDS (FIPS)
Publication Number Publication Title Publication Date
FIPS 202 SHA-3 Standard: Permutation-Based Hash and Extendable- August 2015
Output Functions
FIPS 180-4 Secure Hash Standard (SHS) August 2015
[updated Applicability section]
TABLE 7: SPECIAL PUBLICATIONS (SPs)
Publication Number Publication Title Publication Date
SP 800-176 Computer Security Division 2014 Annual Report August 2015
SP 800-171 Protecting Controlled Unclassified Information in Nonfederal June 2015
Information Systems and Organizations
SP 800-163 Vetting the Security of Mobile Applications January 2015
SP 800-161 Supply Chain Risk Management Practices for Federal April 2015
Information Systems and Organizations
SP 800-157 Guidelines for Derived Personal Identity Verification (PIV) December 2014
Credentials
SP 800-90A Rev. 1 Recommendation for Random Number Generation Using June 2015
Deterministic Random Bit Generators
SP 800-88 Rev. 1 Guidelines for Media Sanitization December 2014
8 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: CSD PUBLICATIONS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

TABLE 7 (CONT.): SPECIAL PUBLICATIONS (SPs)
Publication Number Publication Title Publication Date
SP 800-82 Rev. 2 Guide to Industrial Control Systems (ICS) Security May 2015
SP 800-79-2 Guidelines for the Authorization of Personal Identity July 2015
Verification Card Issuers (PCI) and Derived PIV Credential
Issuers (DPCI)
SP 800-78-4 Cryptographic Algorithms and Key Sizes for Personal Identity May 2015
Verification
SP 800-73-4 Interfaces for Personal Identity Verification May 2015
SP 800-57 Part 3 Recommendation for Key Management, Part 3: Application- January 2015
Rev. 1 Specific Key Management Guidance
SP 800-53A Assessing Security and Privacy Controls in Federal Information December 2014
Rev. 4 Systems and Organizations: Building Effective Assessment
Plans
SP 800-53 Rev. 4 Security and Privacy Controls for Federal Information Systems January 2015
(Update) and Organizations
SP 500-304 Conformance Testing Methodology Framework for ANSI/NIST- June 2015
ITL 1-2011
Update: 2013, Data Format for the Interchange of Fingerprint, Facial & Other
Biometric Information
TABLE 8: NIST INTERAGENCY OR INTERNAL REPORTS (NISTIRs)
Publication Number Publication Title Publication Date
NISTIR 8054 NSTIC Pilots: Catalyzing the Identity Ecosystem April 2015
NISTIR 8041 Proceedings of the Cybersecurity for Direct Digital April 2015
Manufacturing (DDM) Symposium
NISTIR 8023 Risk Management for Replication Devices February 2015
NISTIR 8018 Public Safety Mobile Application Security Requirements January 2015
Workshop Summary
NISTIR 8014 Considerations for Identity Management in Public Safety March 2015
Mobile Networks
NISTIR 7863 Cardholder Authentication for the PIV Digital Signature Key June 2015
NISTIR 7823 Advanced Metering Infrastructure Smart Meter Upgradeability March 2015
Test Framework
TABLE 9: ITL BULLETINS
Publication Date Bulletin Title
September 2015 Additional Secure Hash Algorithm Standards Offer New Opportunities for Data
Protection
August 2015 Recommendation for Random Number Generation Using Deterministic Random Bit
Generators
July 2015 Improved Security and Mobility Through Updated Interfaces for PIV Cards
June 2015 Increasing Visibility and Control of Your ICT Supply Chains
9 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

TABLE 9 (CONT.): ITL BULLETINS
Publication Date Bulletin Title
May 2015 Authentication Considerations for Public Safety Mobile Networks
April 2015 Is Your Replication Device Making an Extra Copy for Someone Else?
March 2015 Guidance for Secure Authorization of Mobile Applications in the Corporate
Environment
February 2015 NIST Special Publication 800-88 Revision 1, Guidelines for Media Sanitization
January 2015 Release of NIST Special Publication 800-53A, Revision 4, Assessing Security and
Privacy Controls in Federal Information Systems and Organizations
December 2014 Release of NIST Special Publication 800-157, Guidelines for Derived Personal Identity
Verification (PIV) Credentials
November 2014 Cryptographic Module Validation Program (CMVP)
October 2014 Release of NIST Special Publication 800-147B, BIOS Protection Guidelines for Servers
ABSTRACTS OF NIST and verification of digital signatures, 2) key derivation, and 3)
pseudorandom bit generation. The hash functions specified
TECHNICAL SERIES
in this standard supplement the SHA-1 hash function and
PUBLICATIONS RELEASED IN
the SHA-2 family of hash functions that are specified in FIPS
FY 2015 180-4, Secure Hash Standard.
Extendable-output functions are different from hash
functions, but it is possible to use them in similar ways, with
The following sections provide abstracts for the draft and
the flexibility to be adapted directly to the requirements
final FIPS, SPs, and security-related NISTIRs listed in the
of individual applications, subject to additional security
previous section. These publications are available at
considerations.
http://csrc.nist.gov/publications.
FIPS 180-4 (Updated), Secure Hash Standard (SHS)
FEDERAL INFORMATION PROCESSING This standard specifies SHA-1 and the SHA-2 family of hash
STANDARDS (FIPS) algorithms that can be used to generate digests of messages.
The digests are used to detect whether messages have been
FIPS 202, SHA-3 Standard: Permutation-Based Hash and changed since the digests were generated. The Applicability
Extendable-Output Functions Clause of this standard was revised to correspond with the
release of FIPS 202, SHA-3 Standard: Permutation-Based
This standard specifies the Secure Hash Algorithm-3 (SHA-
Hash and Extendable-Output Functions (see above). The
3) family of functions on binary data. Each of the SHA-3
revision to the Applicability Clause approves the use of
functions is based on an instance of the Keccak algorithm
hash functions specified in either FIPS 180-4 or FIPS 202
that NIST selected as the winner of the SHA-3 Cryptographic
when a secure hash function is required for the protection
Hash Algorithm Competition. This standard also specifies
of sensitive, unclassified information in federal applications,
the Keccak-p family of mathematical permutations,
including as a component within other cryptographic
including the permutation that underlies Keccak, in order to
algorithms and protocols.
facilitate the development of additional permutation-based
cryptographic functions.
The SHA-3 family consists of four cryptographic hash NIST SPECIAL PUBLICATIONS
functions, called SHA3-224, SHA3-256, SHA3-384, and
SHA3-512, and two extendable-output functions (XOFs), DRAFT SP 800-177, Trustworthy Email
called SHAKE128 and SHAKE256.
This document gives recommendations and guidelines
Hash functions are components for many important for enhancing trust in email. The primary audience
information security applications, including 1) the generation includes enterprise email administrators, information
9 1
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: CSD PUBLICATIONS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

security specialists and network managers. This guideline the CUI category or subcategory listed in the CUI Registry.
applies to federal IT systems and will also be useful for The requirements apply to all components of nonfederal
any small or medium sized organizations. Technologies information systems and organizations that process, store,
recommended in support of the core Simple Mail Transfer or transmit CUI, or provide security protection for such
Protocol (SMTP) and the Domain Name System (DNS) components. The CUI requirements are intended for use by
include mechanisms for authenticating a sending domain federal agencies in contractual vehicles or other agreements
(Sender Policy Framework (SPF), Domain Keys Identified established between those agencies and nonfederal
Mail (DKIM) and Domain-based Message Authentication), organizations.
Reporting and Conformance (DMARC). Recommendations
SP 800-163, Vetting the Security of Mobile Applications
for email transmission security include Transport Layer
Today’s commercially available mobile devices (e.g.,
Security (TLS) and associated certificate authentication
smartphones and tablets) are handheld computing
protocols. Email content security is facilitated through the
platforms with wireless capabilities, geographic localization
encryption and authentication of message content using
capabilities, cameras, and microphones. Similar to computing
Secure/Multipurpose Internet Mail Extensions (S/MIME) and
platforms such as desktops and laptops, the user experience
OpenPGP, and associated certificate and key distribution
with a mobile device is tied to the software apps and the
protocols.
tools and utilities available. The purpose of this document
SP 800-176, Computer Security Division 2014 Annual
is to provide guidance for vetting third party software
Report
applications (apps) for mobile devices. Mobile app vetting is
Title III of the E-Government Act of 2002, titled the Federal intended to assess a mobile app’s operational characteristics
Information Security Management Act (FISMA) of 2002, of secure behavior and reliability (including performance) so
requires NIST to prepare an annual public report on activities that organizations can determine if the app is acceptable for
undertaken in the previous year and planned for the coming use in their expected environment.
year to carry out responsibilities under this law. The primary
SP 800-161, Supply Chain Risk Management Practices for
goal of the Computer Security Division, a component of
Federal Information Systems and Organizations
NIST’s Information Technology Laboratory, is to provide
Federal agencies are concerned about the risks associated
standards and technology that protects information
with information and communications technology (ICT)
systems against threats to the confidentiality, integrity, and
products and services that may contain potentially malicious
availability of information and services. During Fiscal Year
functionality, are counterfeit, or are vulnerable due to
2014, CSD successfully responded to numerous challenges
poor manufacturing and development practices within
and opportunities in fulfilling that mission. This annual report
the ICT supply chain. These risks are associated with the
highlights the research agenda and activities in which CSD
federal agencies decreased visibility into, understanding
was engaged during FY 2014.
of, and control over how the technology that they acquire
SP 800-171, Protecting Controlled Unclassified
is developed, integrated and deployed, as well as the
Information in Nonfederal Information Systems and
processes, procedures, and practices used to assure the
Organizations
integrity, security, resilience, and quality of the products and
The protection of Controlled Unclassified Information services.
(CUI) while residing in nonfederal information systems
This publication provides guidance to federal agencies on
and organizations is of paramount importance to federal
identifying, assessing, and mitigating ICT supply chain risks
agencies and can directly impact the ability of the Federal
at all levels of their organizations. This publication integrates
Government to successfully carry out its designated missions
ICT supply chain risk management (SCRM) into federal
and business operations. This publication provides federal
agency risk management activities by applying a multi-
agencies with recommended requirements for protecting
tiered, SCRM-specific approach, including guidance on
the confidentiality of CUI: (i) when the CUI is resident in
supply chain risk assessment and mitigation activities.
nonfederal information systems and organizations; (ii)
SP 800-157, Guidelines for Derived Personal Identity
when the information systems where the CUI resides are
Verification (PIV) Credentials
not used or operated by contractors of federal agencies
or other organizations on behalf of those agencies; and This recommendation provides technical guidelines for
(iii) where there are no specific safeguarding requirements the implementation of standards-based, secure, reliable,
for protecting the confidentiality of CUI prescribed by the interoperable public key infrastructure (PKI)-based identity
authorizing law, regulation, or government-wide policy for credentials that are issued by federal departments and
9 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

agencies to individuals who possess and prove control DRAFT SP 800-125A, Secure Recommendations for
over a valid PIV Card. The scope of this document includes Hypervisor Deployment
requirements for initial issuance and maintenance of
The Hypervisor is a piece of software that provides the
these credentials, certificate policies and cryptographic
abstraction of all physical resources (such as CPU, Memory,
specifications, technical specifications for permitted
Network and Storage) and thus, enables multiple computing
cryptographic token types and the command interfaces
stacks (consisting of an operating system, Middleware and
for the removable implementations of such cryptographic
Application programs) called Virtual Machines (VMs) to
tokens.
be run on a single physical host. In addition, a hypervisor
DRAFT SP 800-152 (Third Draft), A Profile for U.S. may have the functionality to define a network within a
Federal Cryptographic Key Management Systems (CKMS) single physical host (called a virtual network) to enable
communication among the VMs resident on that host, as
This Profile for U.S. Federal Cryptographic Key Management
well as with physical and virtual machines outside the host.
Systems (FCKMSs) contains requirements for their design,
With all this functionality, the hypervisor is responsible
implementation, procurement, installation, configuration,
for mediating access to physical resources, providing run-
management, operation, and use by U.S. federal
time isolation among resident VMs and enabling a virtual
organizations. The Profile is based on SP 800-130, A
network that provides security-preserving communication
Framework for Designing Cryptographic Key Management
flow among the VMs, and between the VMs and the external
Systems (CKMS).
network. To design a hypervisor with the core functionality
DRAFT SP 800-150, Guide to Cyber Threat Information
described above, there are architectural options, with each
Sharing
option presenting a different size of Trusted Computing
In today’s active threat environment, incident detection and Base (TCB) and hence, a different degree of ease in
response is an ongoing challenge for many organizations. providing the required security assurance. Hence, in
This publication assists organizations in establishing providing security recommendations for the hypervisor, two
computer security incident response capabilities that different approaches have been adopted in this document–
leverage the collective knowledge, experience, and abilities one approach based on architectural options that provide
of their partners by actively sharing threat intelligence and more security assurance, and the second approach based on
ongoing coordination. This publication provides guidelines configuration choices that form part of its core administrative
for coordinated incident handling, including producing functions, such as the management of VMs, hypervisor host,
and consuming data, participating in information sharing hypervisor software and virtual networks.
communities, and protecting incident-related data.
DRAFT SP 800-125B, Secure Virtual Network
DRAFT SP 800-131A Revision 1, Transitions: Configuration for Virtual Machine (VM) Protection
Recommendation for Transitioning the Use of
Virtual Machines (VMs) are key resources to be protected,
Cryptographic Algorithms and Key Lengths
since they are the compute engines hosting mission-critical
At the start of the 21st Century, NIST began the task of applications. Since VMs are end-nodes of a virtual network,
providing cryptographic key management guidance, the configuration of the virtual network forms an important
which includes defining and implementing appropriate key element in the security of VMs and their hosted applications.
management procedures, using algorithms that adequately The virtual network configuration areas discussed in this
protect sensitive information, and planning ahead for document are: Network Segmentation, Network path
possible changes in the use of cryptography because redundancy, firewall deployment architectures and VM Traffic
of algorithm breaks or the availability of more powerful Monitoring. The various configuration options under these
computing techniques. NIST SP 800-57 Part 1 was the first areas are analyzed for their advantages and disadvantages,
document produced in this effort, and includes a general and a set of security recommendations are provided.
approach for transitioning from one algorithm or key length
SP 800-90A Revision 1, Recommendation for Random
to another. This Recommendation (SP 800-131A) provides
Number Generation Using Deterministic Random Bit
more specific guidance for transitions to the use of stronger
Generators
cryptographic keys and more robust algorithms.
This Recommendation specifies mechanisms for the
generation of random bits using deterministic methods. The
methods provided are based on either hash functions or
block cipher algorithms.
9 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: CSD PUBLICATIONS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

SP 800-88 Revision 1, Guidelines for Media Sanitization SP 800-78-4, Cryptographic Algorithms and Key Sizes for
Personal Identity Verification
Media sanitization refers to a process that renders access
to target data on the media infeasible for a given level of FIPS 201-2 defines requirements for the PIV lifecycle activities,
effort. This guide will assist organizations and system including identity proofing, registration, PIV Card issuance,
owners in making practical sanitization decisions, based on and PIV Card usage. FIPS 201-2 also defines the structure of
a categorization of the confidentiality of their information. an identity credential that includes cryptographic keys. This
document contains the technical specifications needed for
DRAFT SP 800-85A-4, PIV Card Application and
the mandatory and optional cryptographic keys specified in
Middleware Interface Test Guidelines (SP 800-73-4
FIPS 201-2, as well as the supporting infrastructure specified
Compliance)
in FIPS 201-2 and the related SP 800-73-4, Interfaces for
SP 800-73 contains the technical specifications to interface
Personal Identity Verification, and SP 800-76-2, Biometric
with the smart card to retrieve and use the PIV identity
Specifications for Personal Identity Verification, that rely on
credentials. This document, SP 800-85A, contains the
cryptographic functions.
test assertions and test procedures for testing smart card
SP 800-73-4, Interfaces for Personal Identity Verification
middleware as well as the card application. The tests reflect
the design goals of interoperability and PIV Card functions. FIPS 201 defines the requirements and characteristics of a
government-wide interoperable identity credential. FIPS 201
SP 800-82 Revision 2, Guide to Industrial Control
also specifies that this identity credential must be stored on a
Systems (ICS) Security
smart card. This document, SP 800-73, contains the technical
This document provides guidance on how to secure Industrial
specifications to interface with the smart card to retrieve
Control Systems (ICS), including Supervisory Control and
and use the PIV identity credentials. The specifications
Data Acquisition (SCADA) systems, Distributed Control
reflect the design goals of interoperability and PIV Card
Systems (DCS), and other control system configurations,
functions. The goals are addressed by specifying a PIV data
such as Programmable Logic Controllers (PLC), while
model, card edge interface, and application programming
addressing their unique performance, reliability, and safety
interface. The specifications go further by constraining
requirements. The document provides an overview of ICS
implementers’ interpretations of the normative standards.
and typical system topologies, identifies typical threats and
Such restrictions are designed to ease implementation,
vulnerabilities to these systems, and provides recommended
facilitate interoperability, and ensure performance, in a
security countermeasures to mitigate the associated risks.
manner tailored for PIV applications.
SP 800-79-2, Guidelines for the Authorization of Personal
DRAFT SP 800-70 Revision 3, National Checklist Program
Identity Verification Card Issuers (PCI) and Derived PIV
for IT Products: Guidelines for Checklist Users and
Credential Issuers (DPCI)
Developers
The purpose of this SP is to provide appropriate and useful
A security configuration checklist is a document that
guidelines for assessing the reliability of issuers of PIV Cards
contains instructions or procedures for configuring an
and Derived PIV Credentials. These issuers store personal
IT product for an operational environment, for verifying
information and issue credentials based on OMB policies
that the product has been configured properly, and/or for
and on the standards published in response to HSPD-12
identifying unauthorized changes to the product. Using
and, therefore, are the primary target of the assessment
these checklists can minimize the attack surface, reduce
and authorization under this guideline. The reliability of an
vulnerabilities, lessen the impact of successful attacks,
issuer is of utmost importance when one organization (e.g.,
and identify changes that might otherwise go undetected.
a federal agency) is required to trust the identity credentials
To facilitate the development of checklists and to make
of individuals that were created and issued by another
checklists more organized and usable, NIST established the
federal agency. This trust will only exist if organizations
National Checklist Program (NCP). This publication explains
relying on the credentials issued by a given organization
how to use the NCP to find and retrieve checklists, and it also
have the necessary level of assurance that the reliability of
describes the policies, procedures, and general requirements
the issuing organization has been established through a
for participation in the NCP.
formal authorization process.
9 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

DRAFT SP 800-57 Part 1 Revision 4, Recommendation for organizations. The assessment procedures, executed at
Key Management, Part 1: General various phases of the system development life cycle, are
consistent with the security and privacy controls in SP 800-
SP 800-57 Part 1 contains basic key management guidance.
53 Revision 4. The procedures are customizable and can
The document:
be easily tailored to provide organizations with the needed
1. Defines the security services that may be provided and
flexibility to conduct security control assessments and
key types that may be employed in using cryptographic
privacy control assessments that support organizational risk
mechanisms;
management processes and that are aligned with the stated
2. Provides background information regarding the risk tolerance of the organization. Information on building
cryptographic algorithms that use cryptographic keying effective security assessment plans and privacy assessment
material; plans is also provided, along with guidance on analyzing
assessment results.
3. Classifies the different types of keys and other
cryptographic information according to their functions, SP 800-53 Rev. 4 (Update), Security and Privacy Controls
specifies the protection that each type of information for Federal Information Systems and Organizations
requires and identifies methods for providing this
This publication provides a catalog of security and
protection;
privacy controls for federal information systems and
4. Identifies the states in which a cryptographic key may organizations and a process for selecting controls to protect
exist during its lifetime; organizational operations (including mission, functions,
image, and reputation), organizational assets, individuals,
5. Identifies the multitude of functions involved in key
other organizations, and the Nation from a diverse set of
management; and
threats, including hostile cyber attacks, natural disasters,
6. Discusses a variety of key management issues related
structural failures, and human errors (both intentional
to the keying material. Topics discussed include
and unintentional). The security and privacy controls are
key usage, cryptoperiod length, domain-parameter
customizable and implemented as part of an organization-
validation, public-key validation, accountability, audit,
wide process that manages information security and privacy
key management system survivability, and guidance for
risk. The controls address a diverse set of security and privacy
cryptographic algorithm and key size selection.
requirements across the Federal Government and critical
SP 800-57 Part 3 Revision 1, Recommendation for infrastructure that are derived from legislation, Executive
Key Management, Part 3: Application-Specific Key Orders, policies, directives, regulations, standards, and/or
Management Guidance mission/business needs. The publication also describes how
to develop specialized sets of controls, or overlays, that are
SP 800-57 Part 3 is intended primarily to help system
tailored for specific types of missions/business functions,
administrators and system installers adequately secure
technologies, or environments of operation. Finally, the
applications, based on product availability and organizational
catalog of security controls addresses security from both a
needs and to support organizational decisions about future
functionality perspective (the strength of security functions
procurements. This document also provides information
and mechanisms provided) and an assurance perspective
for end users regarding application options left under their
(the measures of confidence in the implemented security
control in normal use of the application. Recommendations
capability). Addressing both security functionality and
are given for a select set of applications: Public Key
assurance helps to ensure that information technology
Infrastructures (PKI), Internet Protocol Security (IPsec),
component products and the information systems built from
Transport Layer Security (TLS), Secure/Multipurpose
those products using sound system and security engineering
Internet Mail Extensions (S/MIME), Kerberos, Over-the-Air
principles are sufficiently trustworthy.
Rekeying of Digital Radios (OTAR), Domain Name System
Security Extensions (DNSSEC), Encrypted File Systems SP 500-304, Conformance Testing Methodology
(EFS), and Secure Shell (SSH). Framework for ANSI/NIST-ITL 1-2011 Update: 2013, Data
Format for the Interchange of Fingerprint, Facial & Other
SP 800-53A Revision 4, Assessing Security and
Biometric Information
Privacy Controls in Federal Information Systems and
Organizations: Building Effective Assessment Plans Conformance testing measures whether an implementation
faithfully implements the technical requirements defined
This publication provides a set of procedures for conducting
in a standard. Conformance testing provides developers,
assessments of the security controls and privacy controls
users, and purchasers with increased levels of confidence in
employed within federal information systems and
9 5
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: CSD PUBLICATIONS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

product quality and increases the probability of successful information technology, and industrial control systems.
interoperability. The CSD developed a conformance testing They must authenticate authorized individuals to the
methodology framework for ANSI/NIST-ITL 1-2011 Update: devices and facilities to which they are giving access rights
2013, Data Format for the Interchange of Fingerprint, with a high degree of certainty. In addition, they need to
Facial & Other Biometric Information (AN-2013). This enforce access control policies (e.g., allow, deny or inquire
testing methodology framework defines the test assertions further) consistently, uniformly, and quickly across all of
implemented within CSD’s conformance test tool, which is their resources. This project resulted from a direct dialogue
designed to test implementations of AN-2013 transactions among NCCoE staff and members of the electricity
and promotes biometrics conformity assessment efforts. subsector, mainly from electric power companies and those
This initial document includes comprehensive tables of AN- who provide equipment and/or services to them.
2013 requirements and test assertions for transaction-wide
The goal of this project is to demonstrate a centralized,
requirements and Record Type 1 (which is required for all
standards-based technical approach that unifies identity and
transactions). The tables of requirements and assertions
access management (IdAM) functions across operational
indicate which assertions apply to the traditional encoding
technology (OT) networks, physical access control systems
format, the National Information Exchange Model (NIEM)-
(PACS), and information technology systems. These
compliant encoding format, or both encoding formats. The
networks often operate independently, which can result in
testing methodology framework defines and makes use of
identity and access information disparity, increased costs,
a specific test assertion syntax, which clearly defines the
inefficiencies, and loss of capacity and service delivery
assertions associated with each requirement.
capability. This guide describes the collaborative efforts with
DRAFT SP 1800-3, Attribute Based Access Control technology providers and electric company stakeholders to
address the security challenges that energy providers face
Enterprises rely upon strong access control mechanisms to
in the core function of IdAM. It offers a technical approach
ensure that corporate resources (e.g., applications, networks,
to meeting the challenge, and also incorporates a business
systems and data) are not exposed to anyone other than
value mind-set by identifying the strategic considerations
an authorized user. As business requirements change,
involved in implementing new technologies.
enterprises need highly flexible access control mechanisms
that can adapt. The application of attribute-based policy This Cybersecurity Practice Guide provides a modular,
definitions enables enterprises to accommodate a diverse open, end-to-end example solution that can be tailored
set of business cases. This NCCoE practice guide details a and implemented by energy providers of varying sizes and
collaborative effort between the NCCoE and technology sophistication. It shows energy providers how NIST met the
providers to demonstrate a standards-based approach to challenge using open source and commercially available
attribute-based access control (ABAC). tools and technologies that are consistent with cybersecurity
standards. The use case scenario is based on a normal day-
This guide discusses potential security risks facing
to-day business operational scenario that provides the
organizations, benefits that may result from the
underlying impetus for the functionality presented in the
implementation of an ABAC system and the approach that
guide. While the reference solution was demonstrated with
the NCCoE took in developing a reference architecture and
a certain suite of products, the guide does not endorse these
build. Included is a discussion of major architecture design
products in particular. Instead, it presents the characteristics
considerations, an explanation of security characteristics
and capabilities that an organization’s security experts can
achieved by the reference design and a mapping of security
use to identify similar standards-based products that can
characteristics to applicable standards and security control
be integrated quickly and cost-effectively with an energy
families.
provider’s existing tools and infrastructure.
For parties interested in adopting all or part of the NCCoE
DRAFT SP 1800-1, Securing Electronic Health Records on
reference architecture, this guide includes a detailed
Mobile Devices
description of the installation, configuration and integration
of all components. Health care providers increasingly use mobile devices
to receive, store, process, and transmit patient clinical
DRAFT SP 1800-2, Identity and Access Management for
information. According to NIST’s risk analysis, discussed
Electric Utilities
here, and in the experience of many health care providers,
To protect power generation, transmission, and distribution,
mobile devices can present vulnerabilities in a health care
energy companies need to control physical and logical
organization’s networks. At the 2012 Health and Human
access to their resources, including buildings, equipment,
Services Mobile Devices Roundtable, participants stressed
9 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

that mobile devices are being used by many providers DRAFT NISTIR 8062, Privacy Risk Management for
for health care delivery before they have implemented Federal Information Systems
safeguards for privacy and security.
This document describes a privacy risk management
This Cybersecurity Practice Guide provides a modular, framework for federal information systems. The framework
open, end-to-end reference design that can be tailored and provides the basis for the establishment of a common
implemented by health care organizations of varying sizes vocabulary to facilitate a better understanding of and
and information technology sophistication. Specifically, the communication about privacy risks and the effective
guide shows how health care providers, using open source implementation of privacy principles in federal information
and commercially available tools and technologies that are systems. This publication focuses on the development of
consistent with cybersecurity standards, can more securely two key pillars to support the application of the framework:
share patient information among caregivers using mobile privacy engineering objectives and a privacy risk model.
devices. The scenario considered is that of a hypothetical
DRAFT NISTIR 8060 (Three drafts), Guidelines for the
primary care physician using her mobile device to perform
Creation of Interoperable Software Identification (SWID)
reoccurring activities, such as sending a referral (e.g.,
Tags
clinical information) to another physician, or sending an
This guidance provides an overview of the capabilities
electronic prescription to a pharmacy. While the design was
and usage of Software Identification (SWID) tags as part
demonstrated with a certain suite of products, the guide does
of a comprehensive software life cycle. As instantiated in
not endorse these products in particular. Instead, it presents
the International Organization for Standardization (ISO)/
the characteristics and capabilities that an organization’s
International Electrotechnical Commission (ISO/IEC) 19770-
security experts can use to identify similar standards-based
2 standard, SWID tags support numerous applications
products that can be integrated quickly and cost-effectively
for software asset management and information security
with a health care provider’s existing tools and infrastructure.
management. This report introduces SWID tags in an
operational context, provides guidelines for the creation of
NISTIRS interoperable SWID tags, and highlights key usage scenarios
for which SWID tags are applicable.
DRAFT NISTIR 8074 (2 VOLUMES):
DRAFT NISTIR 8058, Security Content Automation
Volume 1: Report on Strategic U.S. Government Protocol (SCAP) Version 1.2 Content Style Guide: Best
Engagement in International Standardization to Achieve Practices for Creating and Maintaining SCAP 1.2 Content
U.S. Objectives for Cybersecurity
The Security Content Automation Protocol (SCAP) is
Volume 2: Supplemental Information a suite of specifications that standardize the format
and nomenclature by which software flaw and security
This report sets out proposed United States Government
configuration information is communicated, both to
(USG) strategic objectives for pursuing the development
machines and humans. SCAP version 1.2 requirements are
and use of international standards for cybersecurity and
defined in SP 800-126 Revision 2. Over time, certain stylistic
makes recommendations to achieve those objectives.
conventions regarding the authoring of SCAP 1.2 content
The recommendations cover interagency coordination,
have become best practices. While these best practices are
collaboration with the U.S. private sector and international
not required, they improve the quality of the SCAP content in
partners, agency participation in international standards
several ways, such as improving the accuracy and consistency
development, standards training and education, the use
of results, avoiding performance problems, reducing user
of international standards to achieve mission and policy
effort, lowering content maintenance burdens, and enabling
objectives, and other issues. NISTIR 8074 Volume 2,
content reuse. This document has been created to capture
Supplemental Information for the Report on Strategic U.S.
the best practices and encourage their use by SCAP content
Government Engagement in International Standardization
authors and maintainers.
to Achieve U.S. Objectives for Cybersecurity, provides
additional background on international cybersecurity DRAFT NISTIR 8055, Derived Personal Identity
standardization. Verification (PIV) Credentials (DPC) Proof of Concept
Research
This report documents a proof-of-concept implementation
for Derived PIV Credentials (DPCs). Smart card-based PIV
Cards cannot be readily used with most mobile devices,
97
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: CSD PUBLICATIONS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

such as smartphones and tablets, but DPCs can be used discussion and ideas presented at the workshop and serves
instead to PIV-enable these devices and provide multi- as a platform to receive broader feedback on the relevance
factor authentication for mobile device users. This report of projects and suggestions discussed at that event.
captures existing requirements related to DPCs, proposes
NISTIR 8041, Proceedings of the Cybersecurity for Direct
an architecture that supports these requirements, and
Digital Manufacturing (DDM) Symposium
then demonstrates how such an architecture could be
Direct Digital Manufacturing (DDM) involves fabricating
implemented and operated.
physical objects from a data file using computer-controlled
NISTIR 8054, NSTIC Pilots: Catalyzing the Identity
processes with little to no human intervention. It includes
Ecosystem
Additive Manufacturing (AM), 3D printing, rapid prototyping,
Pilots are an integral part of the National Strategy for Trusted etc. The technology is advancing rapidly and has the
Identities in Cyberspace (NSTIC), passed by the White potential to significantly change traditional manufacturing
House in 2011 to encourage enhanced security, privacy, and supply chain industries, including information and
interoperability, and ease-of-use for online transactions. This communication technologies (ICT). On February 3, 2015, CSD
document details summaries and outcomes of NSTIC pilots; hosted a one-day symposium to explore the cybersecurity
in addition, it explores common themes in the pilots’ work, needed for DDM, to include ensuring the protection of
developing and operating innovative identity solutions. intellectual property and the integrity of printers, elements
being printed, and design data. Speakers and attendees
DRAFT NISTIR 8053, De-Identification of Personally
from industry, academia, and government discussed the
Identifiable Information
state of the industry, cybersecurity risks and solutions, and
De-identification removes identifying information from a
implications for ICT supply chain risk management (SCRM).
dataset so that individual data cannot be linked with specific
NISTIR 8023, Risk Management for Replication Devices
individuals. De-identification can reduce the privacy risk
associated with collecting, processing, archiving, distributing This publication provides guidance on protecting the
or publishing information. De-identification thus attempts confidentiality, integrity, and availability of information
to balance the contradictory goals of using and sharing processed, stored, or transmitted on replication devices
personal information, while protecting privacy. Several U.S. (RDs). It suggests appropriate countermeasures in the
laws, regulations and policies specify that data should be context of the System Development Life Cycle (SDLC). A
de-identified prior to sharing. In recent years, researchers security risk assessment template in table and flowchart
have shown that some de-identified data can sometimes be format is also provided to help organizations determine the
re-identified. Many different kinds of information can be de- risk associated with replication devices.
identified, including structured information, free format text,
NISTIR 8018, Public Safety Mobile Application Security
multimedia, and medical imagery. This document summarizes
Requirements Workshop Summary
roughly two decades of de-identification research, discusses
This document captures the input received from the half-
current practices, and presents opportunities for future
day workshop, “Public Safety Mobile Application Security
research.
Requirements,” organized by the Association of Public-
DRAFT NISTIR 8050, Executive Technical Workshop
Safety Communications Officials (APCO) International, in
on Improving Cybersecurity and Consumer Privacy:
cooperation with FirstNet and the Department of Commerce
Summary and Next Steps
and held on February 25, 2014. This first-of-its-kind workshop
Cybersecurity incidents have grown swiftly from conceivable was attended by public safety practitioners, mobile
to realized risks that regularly threaten the national and application developers, industry experts, and government
economic security of the United States. These risks threaten officials who contributed their experience and knowledge to
the financial security of companies and the public, weaken provide input in identifying security requirements for public
consumer confidence, erode individual privacy protections, safety mobile applications.
and damage the brand value and reputation of businesses.
NISTIR 8014, Considerations for Identity Management in
On February 12, 2015, NIST and Stanford University hosted
Public Safety Mobile Networks
an executive technical workshop, which was held in
This document analyzes approaches to identity management
coordination with the White House Summit on Cybersecurity
for public safety networks in an effort to assist individuals
and Consumer Protection, to discuss how to increase the
developing technical and policy requirements for public
use of advanced cybersecurity and privacy technologies in
safety use. These considerations are scoped into the context
consumer-facing organizations. This document details the
of their applicability to public safety communications
9 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

networks, with a particular focus on the nationwide public NISTIR 7823, Advanced Metering Infrastructure Smart
safety broadband network (NPSBN) based on the Long Term Meter Upgradeability Test Framework
Evolution (LTE) family of standards. A short background
As electric utilities turn to Advanced Metering Infrastructures
on identity management is provided alongside a review of
(AMIs) to promote the development and deployment of the
applicable federal and industry guidance. Considerations
Smart Grid, one aspect that can benefit from standardization
are provided for identity proofing, selecting tokens, and the
is the upgradeability of Smart Meters. The National Electrical
authentication process. While specific identity management
Manufacturers Association (NEMA) standard SG-AMI 1-2009,
technologies are analyzed, the document does not preclude
“Requirements for Smart Meter Upgradeability,” describes
other identity management technologies from being used in
functional and security requirements for the secure upgrade
public safety communications networks.
− both local and remote − of Smart Meters. This report
DRAFT NISTIR 7966 (Second Draft), Security of describes conformance test requirements that may be used
Interactive and Automated Access Management Using voluntarily by testers and/or test laboratories to determine
Secure Shell (SSH) whether Smart Meters and Upgrade Management Systems
conform to the requirements of NEMA SG-AMI 1-2009.
Users and hosts must be able to access other hosts in an
For each relevant requirement in NEMA SG-AMI 1-2009,
interactive or automated fashion, often with very high
the document identifies the information to be provided
privileges, for a variety of reasons, including file transfers,
by the vendor to facilitate testing, and the high-level test
disaster recovery, privileged access management, software
procedures to be conducted by the tester/laboratory to
and patch management, and dynamic cloud provisioning.
determine conformance.
This is often accomplished using the Secure Shell (SSH)
protocol. The SSH protocol supports several mechanisms DRAFT NISTIR 7621 Revision 1, Small Business
for interactive and automated authentication. Management Information Security: the Fundamentals
of this access requires proper provisioning, termination,
NIST, as a partner with the Small Business Administration
and monitoring processes. However, the security of SSH
and the Federal Bureau of Investigation in an information
key-based access has been largely ignored to date. This
security awareness outreach to the small business
publication assists organizations in understanding the basics
community, developed this NISTIR as a reference guideline
of SSH interactive and automated access management in an
for small businesses. This document is intended to present
enterprise, focusing on the management of SSH user keys.
the fundamentals of a small business information security
DRAFT NISTIR 7904 (Second Draft), Trusted Geolocation program in non-technical language.
in the Cloud: Proof of Concept Implementation
DRAFT NISTIR 7511 Revision 4, Security Content
This publication explains selected security challenges Automation Protocol (SCAP) Version 1.2 Validation
involving Infrastructure as a Service (IaaS) cloud computing Program Test Requirements
technologies and geolocation. It then describes a proof-of-
This report defines the requirements and associated test
concept implementation that was designed to address those
procedures necessary for products or modules to achieve
challenges. The publication provides sufficient details about
one or more Security Content Automation Protocol (SCAP)
the proof-of-concept implementation so that organizations
validations. Validation is awarded, based on a defined set
can reproduce it if desired. The publication is intended to
of SCAP capabilities by independent laboratories that have
be a blueprint or template that can be used by the general
been accredited for SCAP testing by the NIST National
security community to validate and implement the described
Voluntary Laboratory Accreditation Program (NVLAP).
proof-of-concept implementation.
NISTIR 7863, Cardholder Authentication for the PIV
ADDITIONAL PUBLICATIONS
Digital Signature Key
BY CSD AUTHORS
FIPS 201-2 requires explicit user action by the PIV cardholder
as a condition for the use of the digital signature key stored
CSD authors actively contribute to the security community
on the card. This document clarifies the requirement for
by authoring articles in scholarly literature, participating in
explicit user action to encourage the development of
technical conferences, contributing to encyclopedias and
compliant applications and middleware that use the digital
other books, and publishing other “white papers” that fall
signature key.
outside the scope of NIST Technical Series publications
described above.
9 9
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: CSD PUBLICATIONS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

The following documents were published during FY 2015. their organizations’ resources? Articles in this issue
For conference papers, the contributions listed below were highlight emerging trends and suggest ways to
either i) accepted for a conference held during FY 2015, or approach and address cybersecurity challenges.
ii) accepted for a conference held prior to FY 2015, with a
J. Hagar, T. Wissink, D. R. Kuhn and R. Kacker, “Introducing
final proceeding published in FY 2015 (and not listed in an
Combinatorial Testing in a Large Organization,” Computer
earlier CSD Annual Report). All NIST authors (as listed for an
(IEEE Computer) 48(4), 64-72 (April 2015). doi: 10.1109/
individual publication) are identified using italics.
MC.2015.114.
Links to the preprints and/or final publications of the
A two-year study of eight pilot projects to introduce
documents below are available at http://csrc.nist.gov/
combinatorial testing in a large aerospace corporation
publications/articles.
found that the new methods were practical,
significantly lowered development costs, and
Journal Articles
improved test coverage by 20 to 50 percent.
E. Andreeva, C. Bouillaguet, O. Dunkelman, P.-A. Fouque, J.
Hoch, J. Kelsey, A. Shamir, and S. Zimmer, “New Second- R. Harang and P. M. Mell, “Evasion-Resistant Network Scan
Preimage Attacks on Hash Functions,” Journal of Cryptology, Detection,” Security Informatics 4(4), 1-10 (May 2015). doi:
40 pp. (June 23, 2015). doi: 10.1007/s00145-015-9206-4. 10.1186/s13388-015-0019-7.
In this work, we present several new generic second- Popular network scan detection algorithms operate
preimage attacks on hash functions. Our first attack through evaluating external sources for unusual
is based on the herding attack and applies to various connection patterns and traffic rates. Research has
Merkle–Damgård-based iterative hash functions. revealed evasive tactics that enable full circumvention
Compared to the previously known long-message of existing approaches (specifically the widely cited
second-preimage attacks, our attack offers more Threshold Random Walk algorithm). To prevent the
flexibility in choosing the second-preimage message use of these circumvention techniques, we propose
at the cost of a small computational overhead. More a novel approach to network scan detection that
concretely, our attack allows the adversary to replace evaluates the behavior of internal network nodes,
only a few blocks in the original target message to and combine it with other established techniques of
obtain the second preimage. As a result, our new attack scan detection. By itself, our algorithm is an efficient,
is applicable to constructions previously believed to protocol-agnostic, completely unsupervised method
be immune to such second-preimage attacks. Among that requires no a priori knowledge of the network
others, these include the dithered hash proposal of being defended beyond which hosts are internal
Rivest, Shoup’s UOWHF, and the ROX constructions. In and which hosts are external to the network, and is
addition, we also suggest several time-memory-data capable of detecting network scanning attempts,
tradeoff attack variants, allowing for a faster online regardless of the rate of the scan (working even
phase, and even finding second preimages for shorter with connectionless protocols). We demonstrate the
messages. We further extend our attack to sequences effectiveness of our method on both live data from
stronger than the ones suggested in Rivest’s proposal. an enterprise-scale network and on simulated scan
To this end, we introduce the kite generator as a data, finding a false positive rate of just 0.000034 %
new tool to attack any dithering sequence over a with respect to the number of inbound flows. When
small alphabet. Additionally, we analyze the second- combined with both Threshold Random Walk and
preimage security of the basic tree hash construction. simple rate-limiting detection, we achieve an overall
We also propose several second-preimage attacks detection rate of 94.44 %.
and their time-memory-data tradeoff variants. Finally,
D. R. Kuhn, R. Kacker and Y. Lei, “Combinatorial Coverage as
we show how both our new and the previous second-
an Aspect of Test Quality,” Crosstalk (Hill AFB): the Journal
preimage attacks can be applied even more efficiently
of Defense Software Engineering 28(2), 19-23 (March/April
when multiple short messages, rather than a single
2015).
long target message, are available.
There are relatively few good methods for evaluating
M. Chang, D. R. Kuhn and T. Weil, “IT Security,” IT Professional
test set quality after ensuring basic requirements
17(1), 14-15 (January/February 2015). doi: 10.1109/MITP.2015.10.
traceability. Structural coverage, mutation testing,
How can IT professionals adapt to ever-changing and related methods can be used if source code is
security challenges quickly and without draining available, but these approaches may entail significant
1 0 0
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

cost in time and resources. This paper introduces to countries that had already displayed significant
an alternative measure of test quality that is directly robustness to the types of attacks that we consider.
related to fault detection, simple to compute, and can The countries that displayed higher initial vulnerability
be applied prior to the execution of the system under to such attacks did not become significantly more
test. As such, it provides an inexpensive complement robust over the time period of analysis.
to current approaches for evaluating test quality.
D. Moody, R. Peralta, R. Perlner, A. Regenscheid, A. Roginsky
J. Luna, N. Suri, M. Iorga and A. Karmel, “Leveraging the and L. Chen, “Report on Pairing-based Cryptography,”
Potential of Cloud Security Service-Level Agreements Journal of Research of the National Institute of Standards
through Standards,” IEEE Cloud Computing 2(3), 32-40 and Technology 120, 11-27 (2015). doi: 10.6028/jres.120.002.
(May-June 2015). doi: 10.1109/MCC.2015.52.
This report summarizes study results on pairing-based
Despite the undisputed advantages of cloud cryptography. The main purpose of the study is to form
computing, customers − in particular, small and NIST’s position on standardizing and recommending
medium enterprises − still need a meaningful the pairing-based cryptographic schemes currently
understanding of the security and risk-management published in research literature and standardized
changes that the cloud entails so that they can assess in other standards development organizations. The
whether this new computing paradigm meets their report reviews the mathematical background of
security requirements. This article presents a fresh pairings. This includes topics such as pairing-friendly
view on this problem by surveying and analyzing, from elliptic curves and how to compute various pairings.
the standardization and risk assessment perspective, The report includes a brief introduction on existing
the specification of security in cloud service-level identity-based encryption (IBE) schemes and other
agreements as a promising approach to empower cryptographic schemes using pairing technology. The
customers in assessing and understanding cloud report provides a complete study of the current status
security. Apart from analyzing the proposed risk- of standards activities on pairing-based cryptographic
based approach and surveying the relevant landscape, schemes and explores different application scenarios
this article presents a real-world scenario to support for pairing-based cryptographic schemes. As an
the creation and adoption of service-level agreements important aspect of adopting pairing-based schemes,
as enablers for negotiating, assessing, and monitoring the report also considers the challenges inherent in
the achieved security levels in cloud services. CAVP and CMVP testing for FIPS 140 validation. Based
on the study, the report suggests an approach for
P. M. Mell, R. Harang and A. Gueye, “Measuring Limits on
including pairing-based cryptographic schemes in the
the Ability of Colluding Countries to Partition the Internet,”
NIST cryptographic toolkit. The report also outlines
International Journal of Computer Science: Theory and
several questions that will require further study if this
Application 3(3), 60-73 (2015).
approach is followed.
We show that the strength of the Internet-based
D. Moody and D. Shumow, “Analogues of Vélu’s Formulas
network interconnectivity of countries is increasing
for Isogenies on Alternate Models of Elliptic Curves,”
over time. We then evaluate bounds on the extent
Mathematics of Computation, 23 pp. (September 9, 2015).
to which a group of colluding countries can disrupt
doi: 10.1090/mcom/3036.
this connectivity. We evaluate the degree to which
a group of countries can disconnect two other Isogenies are the morphisms between elliptic curves
countries, isolate a set of countries from the Internet, and are, accordingly, a topic of interest in the subject.
or even break the Internet up into non-communicative As such, they have been well studied, and have been
clusters. To do this, we create an interconnectivity map used in several cryptographic applications. Vélu’s
of the worldwide Internet routing infrastructure at a formulas show how to explicitly evaluate an isogeny,
country-level of abstraction. We then examine how given a specification of the kernel as a list of points.
groups of countries may use their pieces of routing However, Vélu’s formulas only work for elliptic curves
infrastructure to filter out the traffic of other countries specified by a Weierstrass equation. This paper
(or to block entire routes). Overall, bounds analysis presents formulas similar to Vélu’s that can be used
indicates that the ability of countries to perform to evaluate isogenies on Edwards curves and Huff
such disruptions to connectivity has diminished curves, which are normal forms of elliptic curves that
significantly between 2008 and 2013. However, we provide an alternative to the traditional Weierstrass
show that the majority of the gains in robustness go form. Our formulas are not simply compositions
1 0 1
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: CSD PUBLICATIONS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

of Vélu’s formulas with mappings to and from Symposium on Fundamentals of Computation Theory (FCT
Weierstrass form. Our alternate derivation yields 2015), Gdańsk, Poland, August 17-19, 2015. In Lecture Notes
efficient formulas for isogenies with lower algebraic in Computer Science 9210, Fundamentals of Computation
complexity than such compositions. In fact, these Theory, A. Kosowski and I. Walukiewicz, eds., Berlin: Springer
formulas have lower algebraic complexity than Vélu’s International, 2015, pp. 106-117. doi: 10.1007/978-3-319-22177-
formulas on Weierstrass curves. 9_9.
D. Moody, D. Smith-Tone and S. Paul, “Improved We study the relationship between two measures
Indifferentiability Security Bound for the JH Mode,” Designs, of Boolean functions; “algebraic thickness” and
Codes and Cryptography 74(3), 23 pp. (February 2015). doi: “normality”. For a function f, the algebraic thickness
10.1007/s10623-015-0047-9. is a variant of the “sparsity”, the number of nonzero
coefficients in the unique F polynomial representing
Indifferentiability security of a hash mode of operation 2
f, and the normality is the largest dimension of an
guarantees the mode’s resistance against all generic
affine subspace on which f is constant. We show that
attacks. It is also useful to establish the security
for 0 <ε< 2, any function with algebraic thickness
of protocols that use hash functions as random
n 3-ε is constant on some affine subspace of dimension
functions. The JH hash function was one of the five
Ω(nε/2). Furthermore, we give an algorithm for finding
finalists in NIST’s SHA-3 hash function competition.
such a subspace. This is at most a factor of Θ(√n)
Despite several years of analysis, the indifferentiability
from the best guaranteed, and when restricted to the
security of the JH mode has remained remarkably
technique used, is at most a factor of Θ(√logn) from
low, only at n/3 bits, while the two finalist modes
the best guaranteed. We also show that a concrete
Keccak and Grøstl offer a security guarantee of n/2
function, majority, has algebraic thickness Ω(2n1/6).
bits. Note that all these three modes operate with an
n-bit digest and 2n-bit permutations. In this paper, we R. Chandramouli, “Analysis of Network Segmentation
improve the indifferentiability security bound for the Techniques in Cloud Data Centers,” 2015 International
JH mode to n/2 bits (e.g., from approximately 171 to Conference on Grid & Cloud Computing and Applications
256 bits when n = 512). To put this into perspective, (GCA ‘15), Las Vegas, Nevada, United States, July 27-30,
our result guarantees the absence of (non-trivial) 2015, pp. 64-70.
attacks on both the JH-256 and JH-512 hash functions
Cloud Data centers are predominantly made up of
with time less than approximately 2256 computations
Virtualized hosts. The networking infrastructure in a
of the underlying 1024-bit permutation, under the
cloud (virtualized) data center, therefore, consists of
assumption that the underlying permutations can
the combination of a physical IP network (data center
be modeled as an ideal permutation. Our bounds are
fabric) and the virtual network residing in virtualized
optimal for JH-256, and the best-known bound for JH-
hosts. Network Segmentation (Isolation), Traffic flow
512. We obtain this improved bound by establishing
control using firewalls and Intrusion Detection Systems
an isomorphism of certain query-response graphs
/ Intrusion Protection Systems (IDS/IPS) IDS/IPS form
through a careful design of the simulators and bad
the primary network-based security techniques, with
events. Our experimental data strongly supports the
the first one as the foundation for the other two. In this
theoretically obtained results.
paper, we describe and analyze three generations of
A.T. Vassilev and C. Celi, “Avoiding Cyberspace Catastrophes network segmentation techniques—Virtual Switches
through Smarter Testing,” Computer (IEEE Computer) and Physical NIC-based, VLAN-based and Overlay-
47(10), 102-106 (October 2014). doi: 10.1109/MC.2014.47. based. We take a detailed look at the overlay-based
virtual network segmentation and its characteristics,
The Heartbleed bug highlighted a critical problem in
such as scalability and ease of configuration.
the software industry: inadequately tested software
results in serious security vulnerabilities. Available R. Chandramouli, “Deployment-driven Security Configuration
testing technologies, combined with emerging for Virtual Networks,” 6th International Conference on
standards, can help tech companies meet increasing Networks & Communications (NETCOM 2014), Chennai, India,
consumer demand for greater Internet security. December 27-28, 2014, pp. 1-13. doi: 10.5121/csit.2014.41301.
Virtualized Infrastructures are increasingly deployed
Conference Papers
in many data centers. One of the key components of
J. Boyar and M. Find, “Constructive Relationships Between
this virtualized infrastructure is the virtual network
Algebraic Thickness and Normality,” 20th International
1 0 2
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

– a software-defined communication fabric that format of certain kinds of log files to render them
links together the various Virtual Machines (VMs) substantially more amenable to compression with
to each other and to the physical host on which standard algorithms (especially Lempel-Ziv variants).
the VMs reside. Because of its key role in providing We demonstrate that we can reduce compressed
connectivity among VMs and the applications hosted file sizes to as little as 21 % of that of the maximally
on them, Virtual Networks have to be securely compressed file without packing. We can also reduce
configured to provide the foundation for the overall overall compression times up to 64 % in our data sets.
security of the virtualized infrastructure in any Our packing step permits a lossless transmission of
deployment scenario. The objective of this paper is larger log files across the same network transmission
to illustrate a deployment-driven methodology for medium, as well as permitting existing sets of logs
deriving a security configuration for Virtual Networks. to be transmitted within smaller network availability
The methodology outlines two typical deployment windows.
scenarios, identifies use cases and their associated
P. M. Mell, R. Harang and A. Gueye, “The Resilience of
security requirements, discusses the security solutions
the Internet to Colluding Country Induced Connectivity
to meet those requirements and the virtual network
Disruptions,” Security of Emerging Networking Technologies
security configuration to implement each security
(SENT) Workshop at the 2015 Network and Distributed
solution, and then analyzes the pros and cons of each
System Security Symposium (NDSS ‘15), San Diego,
security solution.
California, United States, February 8-11, 2015, 10 pp. doi:
D. R. Kuhn, R. N. Kacker, Y. Lei and J. Torres-Jimenez, 10.14722/sent.2015.23007.
“Equivalence Class Verification and Oracle-Free Testing
We show that the strength of Internet-based
Using Two-layer Covering Arrays,” Fourth International
network interconnectivity of countries is increasing
Workshop on Combinatorial Testing (IWCT 2015) in
over time. We then evaluate bounds on the extent
Proceedings of the 2015 IEEE Eighth International
to which a group of colluding countries can disrupt
Conference on Software Testing, Verification and Validation
this connectivity. We evaluate the degree to which
Workshops (ICSTW), Graz, Austria, April 13-17, 2015, 4 pp.
a group of countries can disconnect two other
doi: 10.1109/ICSTW.2015.7107445.
countries, isolate a set of countries from the Internet,
This short paper introduces a method for verifying or even break the Internet up into non-communicative
equivalence classes for module/unit testing. This is clusters. To do this, we create an interconnectivity map
achieved using a two-layer covering array in which of the worldwide Internet routing infrastructure at a
some or all values of a primary covering array represent country-level of abstraction. We then examine how
equivalence classes. A second-layer covering array groups of countries may use their pieces of routing
of the equivalence class values is computed, and its infrastructure to filter out the traffic of other countries
values substituted for the equivalence class names (or to block entire routes). Overall, bounds analysis
in the primary array. It is shown that this method can indicates that the ability of countries to perform
detect certain classes of errors without a conventional such disruptions to connectivity has diminished
test oracle, and an illustrative example is given. significantly between 2008 and 2013. However, we
show that the majority of the gains in robustness go
P. M. Mell and R. Harang, “Lightweight Packing of Log Files for
to countries that had already displayed significant
Improved Compression in Mobile Tactical Networks,” Military
robustness to the types of attacks that we consider.
Communications Conference (MILCOM 2014), Baltimore,
The countries that displayed higher initial vulnerability
Maryland, United States, October 6-8, 2014, pp. 192-197. doi:
to such attacks did not become significantly more
10.1109/MILCOM.2014.37.
robust over the time period of analysis.
Devices in mobile tactical edge networks are often
D. Moody, R. Perlner and D. Smith-Tone, “An Asymptotically
resource constrained, due to their lightweight and
Optimal Structural Attack on the ABC Multivariate Encryption
mobile nature, and often have limited access to
Scheme,” 6th International Workshop on Post-Quantum
bandwidth. In order to maintain situational awareness
Cryptography (PQCrypto 2014), Waterloo, Ontario, Canada,
in the cyber domain, security logs from these devices
October 1-3, 2014. In Lecture Notes in Computer Science
must be transmitted to command and control sites.
8772, Post-Quantum Cryptography, M. Mosca, ed., Berlin:
We present a lightweight packing step that takes
Springer International, 2014, pp. 180-196. doi: 10.1007/978-3-
advantage of the restricted semantics and regular
319-11659-4_11.
1 0 3
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: CSD PUBLICATIONS | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

Historically, multivariate public key cryptography predict the creator of files that can only be recovered
has been less than successful at offering encryption with carving.
schemes that are both secure and efficient. At
R. Perlner, “Optimizing Information Set Decoding Algorithms
PQCRYPTO ‘13 in Limoges, Tao, Diene, Tang, and Ding
to Attack Cyclosymmetric MDPC Codes,” 6th International
introduced a promising new multivariate encryption
Workshop on Post-Quantum Cryptography (PQCrypto
algorithm based on a fundamentally new idea: hiding
2014), Waterloo, Ontario, Canada, October 1-3, 2014. In
the structure of a large matrix algebra over a finite
Lecture Notes in Computer Science 8772, Post-Quantum
field. We present an attack based on the subspace
Cryptography, M. Mosca, ed., Berlin: Springer International,
differential invariants inherent to this methodology.
2014, pp. 220-228. doi: 10.1007/978-3-319-11659-4_13.
The attack is a structural key recovery attack that
Recently, several promising approaches have been
is asymptotically optimal among all known attacks
proposed to reduce key sizes for code-based
(including algebraic attacks) on the original scheme
cryptography using structured, but non-algebraic
and its generalizations.
codes, such as quasi-cyclic (QC) Moderate Density
A. Nelson and S. Garfinkel, “Measuring Systematic and
Parity Check (MDPC) codes. Biasi et al. propose further
Random Error in Digital Forensics” [abstract], International
reducing the key sizes of code-based schemes using
Symposium on Forensic Science Error Management:
cyclosymmetric (CS) codes. While Biasi et al. analyze
Detection, Measurement and Mitigation, Arlington, Virginia,
the complexity of attacking their scheme using
United States, July 21-24, 2015, 1 p.
standard information-set-decoding algorithms, the
Recognized sources of error in digital forensics include research presented here shows that information set
systematic errors arising from implementation errors, decoding algorithms can be improved, by choosing
and random errors resulting from faulty equipment. the columns of the information set in a way that takes
But as digital forensic techniques expand to include advantage of the added symmetry. The result is an
statistical machine learning, another source of error attack that significantly reduces the security of the
will be statistical errors that arise because of chance proposed CS-MDPC schemes to the point that they
disagreements between a statistical model and subject no longer offer an advantage in key size over QC-
systems examined with that model. We consider two MDPC schemes of the same security level. QC-MDPC
digital forensics systems with these different types of schemes are not affected by this paper’s result.
measurable error.
M. Sönmez Turan and J. Kelsey, “How Random is Your RNG?”
First, we show a mechanism for comparing the Shmoocon 2015, Washington, DC, United States, January 16-
numerous and nuanced results of parsing a file system. 18, 2015, 4 pp.
Multiple storage system parsers were designed for or
Cryptographic primitives need random numbers to
adapted to analyze a game console with a custom file
protect your data. Random numbers are used for
system. However, it was initially unknown whether
generating secret keys, nonces, random paddings,
any of the parsers would produce a perspective of
initialization vectors, salts, etc. Deterministic
the storage system that was correct in reporting the
pseudorandom number generators are useful, but
files present and their characteristics. We adapted
they still need truly random seeds generated by
the parsers to produce an in-common, machine-
entropy sources in order to produce random numbers.
differentiable format, and used a storage differencing
Researchers have shown examples of deployed
algorithm to measure the relative incorrectness of
systems that did not have enough randomness in their
each of the parsers. Discrepancies summarize errors
entropy sources, and as a result, cryptographic keys
in implementation or specification, an important
were compromised. So how do you know how much
report when any reverse-engineering is necessary.
entropy is in your entropy source? Estimating entropy
We discuss advantages and challenges in adopting
is a difficult (if not impossible) problem, and we’ve
this practice.
been working to create usable guidance that will give
Second, we show how to construct a classifier using conservative estimates on the amount of entropy in an
the hard drive from a multi-user computer that can entropy source. From our research, we shared some
determine the user responsible for creating a file. of the challenges and proposed methods. In addition,
The classifier is constructed using allocated files and we discussed some of the new directions that we are
its accuracy determined with take-one-out cross- investigating, and present results of our estimation
validation. Once created, the classifier can be used to methods on simulated entropy sources.
1 0 4
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015 THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

Books and Book Sections under enough conditions that any implementation
under test that passes the conformance test is likely
| F.  Herr,  and F. L. Podio,  |     |     | “Common  |     | Biometric  | Exchange  |     |     |     |     |     |
| ---------------------------- | --- | --- | -------- | --- | ---------- | --------- | --- | --- | --- | --- | --- |
Formats Framework Standardization,” in Encyclopedia of  to  be  conformant.  Conformance  testing  provides
Biometrics, 2nd ed. Edited by S. Z. Li and A. Jain. New York:  developers, users, and purchasers with increased levels
of confidence in product quality and increases the
Springer Reference, 2015.
probability of successful interoperability. Conformance
| The  Common  |     | Biometric  |     | Exchange  |     | Formats  |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- |
testing methodology standards for data interchange
| Framework  | (CBEFF)  |     | provides  | a   | standardized  | set  |     |     |     |     |     |
| ---------- | -------- | --- | --------- | --- | ------------- | ---- | --- | --- | --- | --- | --- |
formats identify a language to define the context of
| of  definitions  |     | and  | procedures  | that  | support  | the  |     |     |     |     |     |
| ---------------- | --- | ---- | ----------- | ----- | -------- | ---- | --- | --- | --- | --- | --- |
conformance testing and conformance claims. These
| interchange  | of  | biometric  |     | data  in  | standard  | data  |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --------- | --------- | ----- | --- | --- | --- | --- | --- |
standards include the set of requirements specified in
| structures  | called  | CBEFF  |     | biometric  | information  |     |     |     |     |     |     |
| ----------- | ------- | ------ | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- |
the base standards and one or more conformance test
records (BIRs). CBEFF permits considerable flexibility
assertions per requirement. There are several efforts in
regarding BIR structures and biometric data content,
biometric conformance test standardization, including
but does so in a way that makes it easy for biometric
|     |     |     |     |     |     |     | U.S.  national  |     | organizations,  | such  | as  International  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | ----- | ------------------ |
applications to evaluate their interest in processing a
|     |     |     |     |     |     |     | Committee  | for  | Information  | Technology  | Standards  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------------ | ----------- | ---------- |
particular BIR. At their conceptually simplest, standard
Technical Committee M1-Biometrics and NIST, who is
CBEFF data structures promote the interoperability
responsible for the development of the ANSI/NIST-
| of  biometric-based  |     |     | application  |     | programs  | and  |     |     |     |     |     |
| -------------------- | --- | --- | ------------ | --- | --------- | ---- | --- | --- | --- | --- | --- |
ITL standards; and international organizations, such
systems by specifying a standardized wrapper for
as the International Organization for Standardization
describing, at a high level, the format and certain
|     |     |     |     |     |     |     | (ISO)/International  |     | Electrotechnical  |     | Commission  |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----------------- | --- | ----------- |
attributes of the content of a BIR. The initial versions
(IEC) Joint Technical Commission 1, Subcommittee
of CBEFF were developed by NIST and the Biometric
37 - Biometrics. The paper includes a description
Consortium. The CBEFF specification published by
|     |     |     |     |     |     |     | of  the  | different  | national  | and  international  | efforts  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --------- | ------------------- | -------- |
NIST in April 2004 (NISTIR 6529-A) was proposed as
that have taken place in the last few years in the
the basis for the development of formal national and
development of conformance testing methodologies
international CBEFF standards. Since then, American
for biometric data interchange formats developed by
National Standards and International Standards (ISO/
the organizations mentioned above. The content of
IEC) have been published. Development continues
these standards (for both published standards and
| at the international  |     |     | level  | on  a new generation of  |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ------ | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
ongoing projects) are addressed.
| CBEFF            | standards.  | The         | paper  | describes    |     | the  main   |     |     |     |     |     |
| ---------------- | ----------- | ----------- | ------ | ------------ | --- | ----------- | --- | --- | --- | --- | --- |
| characteristics  |             | of  CBEFF,  |        | emphasizing  |     | the  value  |     |     |     |     |     |
White Papers
| of  CBEFF  | data      | structures  |     | in  open   | and  | complex     |             |                  |     |            |                     |
| ---------- | --------- | ----------- | --- | ---------- | ---- | ----------- | ----------- | ---------------- | --- | ---------- | ------------------- |
|            |           |             |     |            |      |             | M. Dworkin  | and R. Perlner,  |     | “Analysis  | of  VAES3  (FF2),”  |
| biometric  | systems,  | especially  |     | in  cases  |      | where  the  |             |                  |     |            |                     |
Cryptology ePrint Archive [Website], Report 2015/306, April
system must cope with a wide variety of biometric
2, 2015. Available at: http://eprint.iacr.org/2015/306.
data records, some of which may even be encrypted.
It  provides  adoption  examples  of  CBEFF  data  This  note  describes  a  theoretical  chosen-plaintext
attack on the VAES3 mode for format-preserving
structures by national and international organizations
encryption. VAES3 was specified under the name FF2
and programs, and discusses early work on CBEFF
in Draft National Institute of Standards and Technology
standardization. Recent and current standardization
(NIST) Special Publication 800-38G, Recommendation
efforts are addressed.
for Block Cipher Modes of Operation: Methods for
D. J. Yaga, J. Campbell and G. Zekster, “Conformance Testing
Format-Preserving Encryption.
| Methodologies  | for  | Biometric  |     | Data  Interchange  |     | Formats,  |     |     |     |     |     |
| -------------- | ---- | ---------- | --- | ------------------ | --- | --------- | --- | --- | --- | --- | --- |
Standardization of,” in Encyclopedia of Biometrics, 2nd ed.
Edited by S. Z. Li and A. Jain. New York: SpringerReference,
2015.
Conformance testing is the method that is used to
determine if a product, process or system (known
| as  an  | implementation  |     | under  | test)  | satisfies  | the  |     |     |     |     |     |
| ------- | --------------- | --- | ------ | ------ | ---------- | ---- | --- | --- | --- | --- | --- |
requirements specified in the base standard. The goal
of conformance testing is to capture enough of the
requirements of the base standard and test them
1 0 5
CSD PUBLICATIONS  |  FY 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

ACRONYMS
|     |                    | CBEFF  |  Common Biometric Exchange Formats  |
| --- | ------------------ | ------ | ----------------------------------- |
| 3D  |  Three-Dimensional |        | Framework                           |
3GPP  3rd Generation Partnership Project  CCE   Common Configuration Enumeration
|        |                                | CCEVS  |  Common Criteria Evaluation and Validation  |
| ------ | ------------------------------ | ------ | ------------------------------------------- |
| ABAC   | Attribute Based Access Control |        | Scheme                                      |
|        |                                | CCM    |  Counter with Cipher Block Chaining-        |
| AC     |  Access Control                |        |                                             |
Message Authentication Code
| ACD      | Applied Cybersecurity Division         |       |                                        |
| -------- | -------------------------------------- | ----- | -------------------------------------- |
|          |                                        | CCSS  | Common Configuration Scoring System    |
| ACM      | Association for Computing Machinery    |       |                                        |
|          |                                        | CDH   | Confactor Diffie-Hellman               |
| ACPT     | Access Control Policy Tool             |       |                                        |
|          |                                        | CDM   | Continuous Diagnostics and Mitigation  |
| ACRLCS   | AC Rule Logic Circuit Simulation       |       |                                        |
|          |                                        | CERT  | Computer Emergency Readiness Team      |
| ACTS     | Advanced Combinatorial Testing System  |       |                                        |
|          |                                        | CHES  |  Cryptographic Hardware and Embedded   |
| AES      | Advanced Encryption Standard           |       |                                        |
Systems
| AIM    | Algorithms for Intrusion Measurement  |        |                                       |
| ------ | ------------------------------------- | ------ | ------------------------------------- |
|        |                                       | CIO    | Chief Information Officer             |
| AM     |  Additive Manufacturing               |        |                                       |
|        |                                       | CIS    |  Center for Internet Security         |
| AMI    |  Advanced Metering Infrastructure     |        |                                       |
|        |                                       | CISO   | Chief Information Security Officer    |
| ANSs   | American National Standards           |        |                                       |
|        |                                       | CKMS   | Cryptographic Key Management System   |
| ANSI   | American National Standards Institute |        |                                       |
|        |                                       | CMAC   |  Cipher-based Message Authentication  |
| APCO   |  Association of Public-Safety         |        | Code                                  |
Communications Officials
|      |                                     | CMVP  | Cryptographic Module Validation Program  |
| ---- | ----------------------------------- | ----- | ---------------------------------------- |
| API  |  Application Programming Interface  |       |                                          |
|      |                                     | CNCI  |  Comprehensive National Cybersecurity    |
| ARF  | Asset Reporting Format              |       | Initiative                               |
ARL  Army Research Laboratory  CNSS  Committee on National Security Systems
ASC  Accredited Standards Committee CompTIA   Computing Technology Industry
Association
ASC X9, Inc. Accredited Standards Committee X9, Inc.
ASKDF   Application-Specific Key Derivation  COV  Committee of Visitors
|     | functions  | CPE  |  Common Platform Enumeration  |
| --- | ---------- | ---- | ----------------------------- |
|     |            | CPS  |  Cyber-Physical Systems       |
BioAPI   Biometric Application Programming  CPU  Central Processing Unit
Interface
|         |                                      | CRADA   |  Cooperative Research and Development  |
| ------- | ------------------------------------ | ------- | -------------------------------------- |
| BioCTS  | Biometric Conformance Test Software  |         | Agreement                              |
| BIOS    | Basic Input/Output System            | CS1     |  Cyber Security 1                      |
BIRs  biometric information records CSCRM  Cyber Supply Chain Risk Management
BT-SEG  Bluetooth Security Expert Group  CSD  Computer Security Division
|       |                    | CSE  |  Communications Security Establishment  |
| ----- | ------------------ | ---- | --------------------------------------- |
| CAC   | Common Access Card | CSF  |  Cybersecurity Framework                |
CAE  Centers of Academic Excellence  CSIA  Cyber Security and Information Assurance
CAVP   Cryptographic Algorithm Validation  CSRC  Computer Security Resource Center
Program
|     |     | CSRIC  |  Communications Security, Reliability and  |
| --- | --- | ------ | ------------------------------------------ |
Interoperability Council
1 0 6
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

CSSPAB   Computer System Security and Privacy  EO    Executive Order
Advisory Board
|       |                                     | ESDC  |  Employment and Social Development  |
| ----- | ----------------------------------- | ----- | ----------------------------------- |
| CST   | Cryptographic and Security Testing  |       | Canada                              |
CSWG  Cybersecurity Working Group  ETSI   European Telecommunications Standards
Institute
| CTG  |  Cryptographic Technology Group       |      |                                  |
| ---- | ------------------------------------- | ---- | -------------------------------- |
| CUI  |  Controlled Unclassified Information  |      |                                  |
|      |                                       | FAA  | Federal Aviation Administration  |
| CVE  | Common Vulnerabilities and Exposures  |      |                                  |
CVSS  Common Vulnerability Scoring System  FAQ  Frequently Asked Questions
|     |     | FAR   | Federal Acquisition Regulation  |
| --- | --- | ----- | ------------------------------- |
DAPS   Distributed application platforms and  FBI    Federal Bureau of Investigation
|     | services | FCCX   | Federal Cloud Credential Exchange |
| --- | -------- | ------ | --------------------------------- |
DARPA   Defense Advanced Research Projects  FCKMSs   Federal Cryptographic Key Management
|     | Agency  |     | Systems   |
| --- | ------- | --- | --------- |
DCS  Distributed Control Systems FCSM  Federal Computer Security Managers
DDM  Direct Digital Manufacturing FDA  Federal Drug Administration
DFO  Designated Federal Officer  FDCC  Federal Desktop Core Configuration
DH   Diffie-Hellman  FedRAMP    Federal Risk and Authorization
Management Program
| DHS   | Department of Homeland Security          |         |                                      |
| ----- | ---------------------------------------- | ------- | ------------------------------------ |
|       |                                          | FEMA    | Federal Emergency Management Agency  |
| DHHS  |  Department of Health and Human Services |         |                                      |
|       |                                          | FFRDCs  |  Federally Funded Research and       |
| DKIM  | Domain Keys Identified Mail              |         |                                      |
Development Centers
| DMARC  |  Domain based Message Authentication,  |        |                                          |
| ------ | -------------------------------------- | ------ | ---------------------------------------- |
|        |                                        | FIPS   | Federal Information Processing Standard  |
Reporting and Conformance
|      |                    | FIRST  |  Forum of Incident Response and Security  |
| ---- | ------------------ | ------ | ----------------------------------------- |
| DNS  | Domain Name System |        |                                           |
Teams
| DNSSEC  | Domain Name System Security Extensions  |           |                                           |
| ------- | --------------------------------------- | --------- | ----------------------------------------- |
|         |                                         | FirstNet  | First Responder Network Authority         |
| DOD     | Department of Defense                   |           |                                           |
|         |                                         | FISMA     |  Federal Information Security Management  |
| DoS     |  Department of State                    |           |                                           |
Act
| DOT   | Department of Transportation    |         |                                        |
| ----- | ------------------------------- | ------- | -------------------------------------- |
|       |                                 | FISSEA  |  Federal Information Systems Security  |
| DPC   | Derived PIV Credentials         |         | Educators’ Association                 |
| DPCI  | Derived PIV Credential Issuers  |         |                                        |
DRBG   Deterministic Random Bit Generator  FPE   Format-Preserving Encryption
| DSS  |  Digital Signature Standard | FR  |  Federal Register  |
| ---- | --------------------------- | --- | ------------------ |
| DTR  |  Derived Test Requirements  | FY  |  Fiscal Year       |
EAC  Election Assistance Commission GAO  Government Accountability Office
| EaaS  | Entropy as a Service  | GCM  | Galois/Counter Mode  |
| ----- | --------------------- | ---- | -------------------- |
ECC   Elliptic Curve Cryptography  GCN  Government Computer News
ECDSA  Elliptic Curve Digital Signature Algorithm  GCSE  Group Communication System Enablers
ECP   Enterprise Compliance Profile  GICS  Generic Identity Command Set
| EL  |  Engineering Laboratory | GPS  |  Global Positioning System       |
| --- | ----------------------- | ---- | -------------------------------- |
| EM  |  Encoded Message        | GSA  | General Services Administration  |
1 07
ACRONYMS  |  FY 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

| HAVA   | Help America Vote Act | IT  |  Information Technology  |
| ------ | --------------------- | --- | ------------------------ |
HIT   Health information technology ITI   Information Technology Industry
HIPAA   Health Insurance Portability and  ITL   Information Technology Laboratory
Accountability Act
|     |     | ITU-T  |  International Telecommunications Union  |
| --- | --- | ------ | ---------------------------------------- |
HMAC   Hash-based Message Authentication Code  – Telecommunication Standardization
| HSPD-12  |  Homeland Security Presidential  |       | Sector                                  |
| -------- | -------------------------------- | ----- | --------------------------------------- |
|          | Directive-12                     | IUT   |  Implementation under test              |
|          |                                  | IWCE  |  International Wireless Communications  |
Expo
| IaaS   |  Infrastructure as a Service           |      |                            |
| ------ | -------------------------------------- | ---- | -------------------------- |
|        |                                        | IWG  | Interagency Working Group  |
| IAD    | Information Access Division            |      |                            |
| IAPWG  |  Information Assurance Policy Working  |      |                            |
|        | Group                                  | JTF  |  Joint Task Force          |
IBE   Identity-based Encryption JTC 1  Joint Technical Committee 1
| IC  |  Intelligence Community |     |     |
| --- | ----------------------- | --- | --- |
ICC   Integrated Circuit Card  KBKDF  Key-Based Key Derivation functions
ICS    Industrial Control Systems KDF  Key Derivation Functions
| ICSTW  |  International Conference on Software  |     |     |
| ------ | -------------------------------------- | --- | --- |
Testing, Verification and Validation
|     |     | LDS  |  Logical Data Structure |
| --- | --- | ---- | ----------------------- |
Workshops
|      |                                   | LTE  |  Long-Term Evolution  |
| ---- | --------------------------------- | ---- | --------------------- |
| ICT  |  I nformation and Communications  |      |                       |
Technology
|       |                                 | MCPTT  | Mission Critical Push-To-Talk |
| ----- | ------------------------------- | ------ | ----------------------------- |
| IdAM  | Identity and Access Management  |        |                               |
IEC   International Electrotechnical Commission  MILCOM  Military Communications Conference
|       |                                           | MIH   | Media-Independent Handover  |
| ----- | ----------------------------------------- | ----- | --------------------------- |
| IEEE  |  Institute of Electrical and Electronics  |       |                             |
|       | Engineers                                 | MLS   | Multi-Level Security        |
IETF  Internet Engineering Task Force MMT   Multi-Block Message Test
| IG   |  Implementation Guidance | MQV  | Menezes-Qu-Vanstone  |
| ---- | ------------------------ | ---- | -------------------- |
| IGs  |  Inspector Generals      |      |                      |
IKE   Internet Key Exchange NARA   National Archives and Records
Administration
| IMS      |  Innovation in Measurement Science        |        |                                  |
| -------- | ----------------------------------------- | ------ | -------------------------------- |
|          |                                           | NASA   |  National Aeronautics and Space  |
| INCITS   |  InterNational Committee for Information  |        |                                  |
Administration
Technology Standards
|      |                    | NASPO  |  North American Security Products  |
| ---- | ------------------ | ------ | ---------------------------------- |
| IP   |  Internet Protocol |        |                                    |
Organization
| IPD   |  Initial Public Draft       |        |                                    |
| ----- | --------------------------- | ------ | ---------------------------------- |
|       |                             | NCCoE  |  National Cybersecurity Center of  |
| IPv6  | Internet Protocol Version 6 |        |                                    |
Excellence
| ISA  |  International Society of Automation |       |                                    |
| ---- | ------------------------------------ | ----- | ---------------------------------- |
|      |                                      | NCP   | National Checklist Program         |
| ISO  |   International Organization for     |       |                                    |
|      |                                      | NCWF  |  National Cybersecurity Workforce  |
Standardization
Framework
| ISP   |  Internet Service Provider  |       |                                     |
| ----- | --------------------------- | ----- | ----------------------------------- |
|       |                             | NEMA  |  National Electrical Manufacturers  |
ISPAB   Information Security and Privacy Advisory  Association
Board
|     |     | NFC  | Near Field Communications  |
| --- | --- | ---- | -------------------------- |
1 0 8
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

NGAC  Next Generation Access Control PIV   Personal Identity Verification
NGAC-FA   Next Generation Access Control – PIV-I  PIV-Interoperable
Functional Architecture
|     | PKCS  | Public Key Cryptography Standards  |
| --- | ----- | ---------------------------------- |
NGAC-   Next Generation Access Control – Generic
|     | PKI   |  Public Key Infrastructure  |
| --- | ----- | --------------------------- |
GOADS   Operations & Abstract Data Structures
|     | P.L.  |  Public Law  |
| --- | ----- | ------------ |
NGAC-   Next Generation Access Control
|     | PLC  |  Programmable Logic Controllers  |
| --- | ---- | -------------------------------- |
IRPADS    Implementation Requirements, Protocols
| and API Definitions  | PM  |  Policy Machine  |
| -------------------- | --- | ---------------- |
NICE   National Initiative for Cybersecurity  PML   Physical Measurement Laboratory
Education
|     | PoS   | Point of Service |
| --- | ----- | ---------------- |
NIEM   National Information Exchange Model
|     | PPD  | Presidential Policy Directive  |
| --- | ---- | ------------------------------ |
NISTIR  NIST Interagency Report
|     | PQC  | Post-Quantum Cryptography |
| --- | ---- | ------------------------- |
NITRD    Networking and Information Technology
|     | PRNGs  | Pseudorandom Number Generators |
| --- | ------ | ------------------------------ |
Research and Development
|     | ProSe  | Proximity Services  |
| --- | ------ | ------------------- |
NPIVP   NIST Personal Identity Verification
|     | PSCR  | Public Safety Communications Research |
| --- | ----- | ------------------------------------- |
Program
|     | PSS  |  Probabilistic Signature Scheme |
| --- | ---- | ------------------------------- |
NPSBN   National Public Safety Broadband Network
|     | PUB  | Publication |
| --- | ---- | ----------- |
NSA  National Security Agency
|     | PWG  | Public Working Group  |
| --- | ---- | --------------------- |
NSTIC   National Strategy for Trusted Identities in
Cyberspace
NTIA   National Telecommunications and  RBAC   Role-Based Access Control
Information Administration
|     | RBG  | Random Bit Generator |
| --- | ---- | -------------------- |
NVD  National Vulnerability Database
|     | RD  |  Replication Device  |
| --- | --- | -------------------- |
NVLAP   National Voluntary Laboratory
|     | R&D   | Research and Development |
| --- | ----- | ------------------------ |
Accreditation Program
|     | RFC   | Request for Comments |
| --- | ----- | -------------------- |
NYU  New York University
|     | RFI   |  Request for Information        |
| --- | ----- | ------------------------------- |
|     | RFID  | Radio Frequency Identification  |
OCIL  Open Checklist Interactive Language
|     | RMF  | Risk Management Framework  |
| --- | ---- | -------------------------- |
OCR   Office for Civil Rights
|     | RNG   | Random Number Generation  |
| --- | ----- | ------------------------- |
ODNI   Office of the Director of National
|     | RSA  | Rivest, Shamir, Adleman  |
| --- | ---- | ------------------------ |
Intelligence
ODP  Open Distributed Processing
|     | SACM  |  Security Automation and Continuous  |
| --- | ----- | ------------------------------------ |
OMB   Office of Management and Budget
Monitoring
OPM   Office of Personnel Management
|     | SBA  | Small Business Administration |
| --- | ---- | ----------------------------- |
OT   Operational Technology
|     | SBIR  |  Small Business Innovation Research  |
| --- | ----- | ------------------------------------ |
OVAL   Open Vulnerability and Assessment
|     | SC  |  Subcommittee  |
| --- | --- | -------------- |
Language
|     | SCADA  | Supervisory Control and Data Acquisition  |
| --- | ------ | ----------------------------------------- |
|     | SCAP   | Security Content Automation Protocol      |
PACS  Physical Access Control Systems
|     | SCAPVal  | SCAP Content Validation Tool  |
| --- | -------- | ----------------------------- |
PCI    Payment Card Industry
|     | SCMG  |  Security Components and Mechanisms  |
| --- | ----- | ------------------------------------ |
PCLOB  Privacy and Civil Liberties Oversight Board
Group
PIN   Personal Identification Number
1 0 9
ACRONYMS  |  FY 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

SCORE   Special Cyber Operations Research and  TIC   Trusted Internet Connection
Engineering
|        |                                    | TLS    | Transport Layer Security                  |
| ------ | ---------------------------------- | ------ | ----------------------------------------- |
| SCRM   | Supply Chain Risk Management       |        |                                           |
|        |                                    | TMSAD  | Trust Model for Security Automation Data  |
| SDLC   | System Development Life Cycle      |        |                                           |
|        |                                    | TNC    | Trusted Network Communications            |
| SDO    | Standards Developing Organizations |        |                                           |
|        |                                    | TPM    | Trusted Platform Module                   |
| SENT   |  Security of Emerging Networking   |        |                                           |
|        |                                    | TRW    | Threshold Random Walk                     |
Technologies
|        |                                     | TS       |  Technical Standard                   |
| ------ | ----------------------------------- | -------- | ------------------------------------- |
| SGCC   | Smart Grid Cybersecurity Committee  |          |                                       |
|        |                                     | TTPs     | Tactics, Techniques, and Procedures   |
| SGIP   | Smart Grid Interoperability Panel   |          |                                       |
| SHA    | Secure Hash Algorithm               |          |                                       |
|        |                                     | U.S.C.   | U.S. Code                             |
| SHS    |  Secure Hash Standard               |          |                                       |
|        |                                     | US-CERT  |  U.S. Computer Emergency Readiness    |
| SIG    |  Special Interest Group             |          | Team                                  |
| SLAs   | Service Level Agreements            |          |                                       |
|        |                                     | USG      | U.S. Government                       |
SMB  Small and Medium-size Business USGCB    United States Government Configuration
| SMEs  | Small and Medium Enterprises |     | Baseline |
| ----- | ---------------------------- | --- | -------- |
S/MIME   Secure/Multipurpose Internet Mail  USGv6  U.S. Government IPv6
Extensions
|       |                                          | USNC  | United States National Committee |
| ----- | ---------------------------------------- | ----- | -------------------------------- |
| SMTP  | Simple Mail Transfer Protocol            |       |                                  |
|       |                                          | UX    |  User experience                 |
| SNMP  | Simple Network Management Protocol       |       |                                  |
| SOIG  | Security Outreach and Integration Group  |       |                                  |
|       |                                          | VA    |  Veteran Affairs                 |
| SP    |  Special Publications                    |       |                                  |
|       |                                          | VCAT  |  Visiting Committee on Advanced  |
| SPF   |  Sender Policy Framework                 |       | Technology                       |
SRTP  Secure Real-time Transport Protocol  VCI   Virtual Contact Interface
| SSA  |  Social Security Administration | VM  |  Virtual Machine  |
| ---- | ------------------------------- | --- | ----------------- |
SSAG  Secure Systems and Applications Group VPN  Virtual Private Network
SSCA  Software and Supply Chain Assurance VRDX-SIG   Vulnerability Reporting and Data
eXchange SIG
| SSD   |  Software and Systems Division      |       |                                     |
| ----- | ----------------------------------- | ----- | ----------------------------------- |
|       |                                     | VVSG  | Voluntary Voting System Guidelines  |
| SSH   |  Secure Shell                       |       |                                     |
| STVM  |  Security Testing, Validation, and  |       |                                     |
|       | Measurement                         | WG    |  Working Group                      |
STVMG   Security Testing, Validation, and  Wi-Fi  Wireless Fidelity
Measurement Group
| SWID  | Software Identification  |        |                                    |
| ----- | ------------------------ | ------ | ---------------------------------- |
|       |                          | XACML  |  eXtensible Access Control Markup  |
Language
TAG   Technical Advisory Group  XCCDF   Extensible Configuration Checklist
Description Format
| TCG   |  Trusted Computing Group           |         |                                       |
| ----- | ---------------------------------- | ------- | ------------------------------------- |
|       |                                    | XML     | Extensible Markup Language            |
| TDEA  | Triple Data Encryption Algorithm   |         |                                       |
|       |                                    | XOFs    | Extendable-Output Functions           |
| TDES  | Triple Data Encryption Standard    |         |                                       |
|       |                                    | xTract  | Threat Reduction and Correlation Tool |
| TGDC  |  Technical Guidelines Development  |         |                                       |
|       | Committee                          | XTS     |  XEX Tweakable Block Cipher with      |
| 1 1 0 |                                    |         | Ciphertext Stealing                   |
COMPUTER SECURITY DIVISION ANNUAL REPORT | 2015
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

OPPORTUNITIES TO ENGAGE Federal Computer Security Managers’
WITH CSD, ACD, AND NIST (FCSM) Forum
The FCSM Forum is covered in detail in the Outreach
section of this report. Membership is free and open to
Guest Research Internships at NIST
federal employees. For further information, contact:
Opportunities are available at NIST for 6- to 24-month
internships within the Computer Security Division (CSD)
Ms. Patricia Toth
and the Applied Cybersecurity Division (ACD). Qualified
(301) 975-5140
individuals should contact CSD and/or ACD, provide a
ptoth@nist.gov or sec-forum@nist.gov
statement of qualifications, and indicate the area of work
that is of interest. The salary costs are generally borne by
Visit the FCSM Forum website:
the sponsoring institution; however, in some cases, these
http://csrc.nist.gov/groups/SMA/forum/membership.html
guest research internships carry a small monthly stipend
paid by NIST. For further information, contact:
Security Research
NIST occasionally undertakes security work, primarily in the
CSD Contact: ACD Contact:
area of research, funded by other agencies. Such sponsored
Mr. Matthew Scholl Mr. Kevin Stine
work is accepted by NIST when it can cost-effectively
(301) 975-2941 (301) 975-4483
further the goals of NIST and the sponsoring institution. For
matthew.scholl@nist.gov kevin.stine@nist.gov
further information, contact:
Details at NIST for Government or
CSD Contact: ACD Contact:
Military Personnel
Mr. Matthew Scholl Mr. Kevin Stine
Opportunities are available at NIST for 6- to 24-month (301) 975-2941 (301) 975-4483
details at NIST in CSD and/or ACD. Qualified individuals matthew.scholl@nist.gov kevin.stine@nist.gov
should contact CSD and/or ACD, provide a statement
of qualifications, and indicate the area of work that is of
Funding Opportunities at NIST
interest. Generally speaking, the salary costs are borne by
NIST funds industrial and academic research in a variety
the sponsoring agency; however, in some cases, agency
of ways. The Small Business Innovation Research Program
salary costs may be reimbursed by NIST. For further
funds R&D proposals from small businesses; see
information, contact:
http:// www.nist.gov/sbir. NIST also offers other grants to
encourage work in specific fields: precision measurement,
CSD Contact: ACD Contact:
fire research, and materials science. Grants/awards
Mr. Matthew Scholl Mr. Kevin Stine
supporting research at industry, academia, and other
(301) 975-2941 (301) 975-4483
institutions are available on a competitive basis through
matthew.scholl@nist.gov kevin.stine@nist.gov
several different Institute offices.
For general information on NIST grants programs, please
contact:
Mr. Christopher Hunton
(301) 975-5718
christopher.hunton@nist.gov
Funding opportunity information:
http://www.nist.gov/director/ocfo/grants/grants.cfm
1 1 1
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: OPPORTUNITIES TO ENGAGE WITH CSD, ACD, AND NIST | FY 2015
http://dx.doi.org/10.6028/NIST.SP.800-182

THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-182

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-25", "model": "legacy"} -->
