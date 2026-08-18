# NIST/ITL Cybersecurity Program Annual Report 2016
Organization: NIST  
Report Title: ITL-Annual-Report  
Year: 2016  

## Table of Contents
- [Acknowledgments](#acknowledgments)
- [Disclaimer](#disclaimer)
- [Trademark Information](#trademark-information)
- [Welcome Letter](#welcome-letter)
- [Background Information of Annual Report](#background-information-of-annual-report)
- [The Information Technology Laboratory Implements the Federal Information Security Management Act](#the-information-technology-laboratory-implements-the-federal-information-security-management-act)
- [ITL Cybersecurity Program Accomplishments for Fiscal Year 2016](#itl-cybersecurity-program-accomplishments-for-fiscal-year-2016)
- [ITL Involvement with National and International IT Security Standards](#itl-involvement-with-national-and-international-it-security-standards)
  - [Focus on ISO and ANSI Standardization (ISO/IEC JTC1 SC27 IT Security)](#focus-on-iso-and-ansi-standardization-isoiec-jtc1-sc27-it-security)
  - [IT Security Techniques Standards](#it-security-techniques-standards)
  - [Next Generation Access Control Standards](#next-generation-access-control-standards)
  - [ISO Standardization of Security Requirements for Cryptographic Modules](#iso-standardization-of-security-requirements-for-cryptographic-modules)
  - [Identity Management Devices and Infrastructures Standards (JTC1 SC17 Cards and Personal Identification Devices)](#identity-management-devices-and-infrastructures-standards-jtc1-sc17-cards-and-personal-identification-devices)

---

NIST SPECIAL PUBLICATION 800-195  
NIST/ITL CYBERSECURITY PROGRAM  
2016 ANNUAL REPORT  

THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:  
http://dx.doi.org/10.6028/NIST.SP.800-195  

PATRICK O’REILLY, EDITOR | KRISTINA RIGOPOULOS, EDITOR  
Computer Security Division | Applied Cybersecurity Division  
Information Technology Laboratory | Information Technology Laboratory  

CO-EDITORS:  
Larry Feldman  
Greg Witte  
G2, Inc.  
Annapolis Junction, Maryland  

SEPTEMBER 2017  

U.S. DEPARTMENT OF COMMERCE  
Wilbur L. Ross, Jr., Secretary  

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY  
Kent Rochford, Acting Under Secretary of Commerce for Standards and Technology and Acting Director  

## Authority
This publication has been developed by NIST in accordance with its statutory responsibilities under the Federal Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3541 et seq., Public Law (P.L.) 113-283. NIST is responsible for developing information security standards and guidelines, including minimum requirements for federal information systems, but such standards and guidelines shall not apply to national security systems without the express approval of appropriate federal officials exercising policy authority over such systems. This guideline is consistent with the requirements of the Office of Management and Budget (OMB) Circular A-130.

Nothing in this publication should be taken to contradict the standards and guidelines made mandatory and binding on federal agencies by the Secretary of Commerce under statutory authority. Nor should these guidelines be interpreted as altering or superseding the existing authorities of the Secretary of Commerce, Director of the OMB, or any other federal official. This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST.

National Institute of Standards and Technology Special Publication 800-195  
Natl. Inst. Stand. Technol. Spec. Publ. 800-195, 156 pages (September 2017)  
CODEN: NSPUE2  

## Reports on Computer Systems Technology
The Information Technology Laboratory (ITL) at the National Institute of Standards and Technology (NIST) promotes the U.S. economy and public welfare by providing technical leadership for the Nation’s measurement and standards infrastructure. ITL develops tests, test methods, reference data, proof of concept implementations, and technical analyses to advance the development and productive use of information technology. ITL’s responsibilities include the development of management, administrative, technical, and physical standards and guidelines for the cost-effective security and privacy of other than national security-related information in federal information systems. The Special Publication 800-series reports on ITL’s research, guidelines, and outreach efforts in information system security, and its collaborative activities with industry, government, and academic organizations.

---

## Acknowledgments
The editors, Patrick O’Reilly of the Computer Security Division (CSD) and Kristina Rigopoulos of the Applied Cybersecurity Division (ACD), would like to thank their ITL colleagues who provided write-ups on their 2016 project highlights and accomplishments for this annual report (their names are mentioned after each project write-up). The editors would also like to acknowledge Elaine Barker (CSD), Lisa Carnahan (Standards Coordination Office, NIST), Greg Witte and Larry Feldman (G2) for reviewing and providing valuable feedback for this annual report.

The editors would also like to acknowledge Kristen Dill of Dill and Company, Inc. for designing the cover and inside layout for this 2016 annual report.

## Disclaimer
Any mention of commercial products or organizations is for informational purposes only; it is not intended to imply recommendation or endorsement by the National Institute of Standards and Technology, nor is it intended to imply that the products identified are necessarily the best available for the purpose.

## Trademark Information
All names are trademarks or registered trademarks of their respective owners.

---

## Welcome Letter
Awareness about the importance of strong cybersecurity for maintaining trust in the economy and protecting the nation is at an all-time high. So, too, are the challenges. When it comes to cybersecurity, the National Institute of Standards and Technology (NIST) has a long history of conducting path-breaking research and development, cultivating standards and best practices, and facilitating technology transitions. We rely on open, transparent, and collaborative processes that engage private and public sector participation and attract expertise from around the world. This 2016 report captures our most noteworthy accomplishments.

In 2016, NIST continued to advance fundamental research to support security and interoperability standards and guidelines. This work was led by the Computer Security Division (CSD) in the NIST Information Technology Laboratory (ITL). Among other things, CSD is responsible for developing cybersecurity standards, guidelines, tests, and metrics for the protection of non-national security federal information systems. Recognizing the agency’s need to respond to and anticipate increasing demands for its cybersecurity expertise, NIST established the Applied Cybersecurity Division (ACD) within ITL to support additional applied research and to transition effective cybersecurity technology approaches to government and business sectors nationwide. ACD helps to drive the adoption of appropriate cybersecurity solutions by government and commercial organizations – enabling solutions-oriented collaborative interactions and offering guidance on the use of research results, standards, and best practices. Other parts of NIST also are key contributors to NIST’s cybersecurity portfolio.

Strong partnerships with industry, academia and government are critical to NIST’s cybersecurity program. In 2016, NIST continued to collaborate with stakeholders from across the country and around the world to raise awareness and encourage use of the voluntary Cybersecurity Framework. In this spirit, NIST began to develop an update to the version first published in 2014. NIST also prepared a draft Cybersecurity Framework profile aligned with manufacturing sector goals and industry best practices. In addition, NIST developed the draft Baldrige Cybersecurity Excellence Builder self-assessment tool that complements the Cybersecurity Framework and helps organizations to better understand the effectiveness of their cybersecurity risk management efforts.

Looking ahead is vital in the realm of cybersecurity. Knowing that if large-scale quantum computers are ever built, they will be able to break many of the public-key cryptosystems currently in use and compromise the confidentiality and integrity of digital communication on the Internet and elsewhere, NIST is working closely with the academic community and industry to develop protective cryptographic standards that we all rely upon. Building on its successful tradition of working openly with the worldwide cryptographic community, in 2016 NIST called for submissions for quantum-resistant public-key cryptographic algorithms for standards. These algorithms must be secure against both quantum and classical computers, and should interoperate with existing communications protocols and networks. After submissions are received late in 2017, NIST plans to spend 3-5 years working with the research community and industry to analyze the candidates before selecting algorithms for standardization.

Identity management is fundamental to security management. In 2016, NIST continued to advance solutions in identity management through projects with partners who manage innovative but practical real-world solutions. Also in the past year, NIST produced an introduction to the concepts of privacy engineering and risk management for federal information systems. The goal is to help decrease privacy risks and enable organizations to make purposeful decisions about resource allocation and effective implementation of controls in information systems. NIST also initiated an update to our Digital Identity Guideline (Special Publication 800-63), which provides technical guidelines to agencies for the implementation of digital authentication. Building from these foundational resources, NIST’s efforts will focus on strengthening the security, privacy, usability and interoperability of digital identity solutions that meet an organization’s identity and access management needs throughout the system lifecycle.

During 2016, NIST’s National Cybersecurity Center of Excellence (NCCoE) moved into a new permanent facility that expanded the Center’s workspace from four to 23 separate, flexible laboratories—including two larger areas capable of safely hosting large equipment, such as automobiles. This additional space allows NCCoE to increase its collaborations and projects. In 2016, the Center published draft practice guides to support industry sectors, including healthcare, financial services, and energy; these guides are now beginning to be put to productive use. NCCoE also published draft documents to support security in key technology areas, such as cloud computing and mobile applications.

The National Initiative for Cybersecurity Education (NICE), led by NIST, is a partnership between government, academia, and the private sector that is focused on promoting a robust network and an ecosystem of cybersecurity education, training, and workforce development. In 2016, NIST released an update to the NICE Cybersecurity Workforce Framework (NCWF); it already is being used in the private and public sectors to more effectively identify, recruit, develop and maintain cybersecurity talent. The NICE framework provides a common language to categorize and describe cybersecurity work that helps organizations to build a strong staff to protect systems and data.

Our dedicated staff has accomplished a great deal in 2016, developing standards and working closely with scores of partners and drawing upon hundreds of private and public sector organizations and individuals. This is not a static endeavor. For example, NIST is fully aware of the urgent need to more aggressively address the security challenges of the Internet of Things and, more broadly, our connected world.

We welcome any and all suggestions about where and how we can better provide the nation with the kind of cybersecurity information and tools that it needs in order to advance and protect our economy and our country.

**Donna F. Dodson**,  
Chief Cybersecurity Advisor

---

## Background Information of Annual Report
This Annual Report, formerly the Computer Security Division Annual Report, has been renamed to the Information Technology Laboratory (ITL) Cybersecurity Program Annual Report. This change reflects the opportunity to describe the many cybersecurity program highlights and accomplishments from throughout the laboratory. This Annual Report is organized into several sections, each identified by a title page.

Please note: This Annual Report covers the Federal Government’s Fiscal Year (FY) 2016 from October 1, 2015 to September 30, 2016.

ITL, an operating unit under NIST, contains seven divisions. Five of these seven divisions are involved with cybersecurity efforts at NIST. Throughout this Annual Report, there are some references to particular division activities, and to work by groups within those divisions. Primarily, the authors have attributed accomplishments to ITL, since ITL staff have been involved with each cybersecurity program included in this Annual Report. At the end of each program/project write-up, one or more points of contact are provided and may be used to address questions or request for more information. Many sections also include additional references that readers may find valuable.

Below is a condensed hierarchical chart of ITL’s structure:

**INFORMATION TECHNOLOGY LABORATORY (ITL) HEADQUARTERS**  
Charles Romine, Director  
Jim St. Pierre, Deputy Director  
*(5 of the 7 divisions (identified below) are involved with the ITL Cybersecurity Program)*

- **Advanced Network Technologies Division (ANTD)**  
  Abdella Battou, Division Chief
- **Applied Cybersecurity Division (ACD)**  
  Kevin Stine, Division Chief
- **Computer Security Division (CSD)**  
  Matthew Scholl, Division Chief
- **Information Access Division (IAD)**  
  Shahram Orandi, Division Chief
- **Software and Systems Division (SSD)**  
  Ram Sriram, Division Chief

ITL’s Cybersecurity Program is very excited to share these achievements and accomplishments made during the 2016 Fiscal Year in this Annual Report.

---

## The Information Technology Laboratory Implements the Federal Information Security Management Act
This section contains a list of the major activities that were accomplished during FY 2016 by the ITL Cybersecurity Program. Detailed explanations of these activities are provided in the next section.

### Information Technology Laboratory (ITL) Cybersecurity Program Implements Federal Information Security Management Act
The E-Government Act, Public Law 107-347, passed by the 107th Congress and signed into law by the President in December 2002, recognized the importance of information security to the economic and national security interests of the United States. Title III of the E-Government Act, titled the Federal Information Security Management Act (FISMA) of 2002, included the duties and responsibilities for the National Institute of Standards and Technology, Information Technology Laboratory. There are multiple divisions within ITL that are involved with cybersecurity programs/projects. The work is being conducted collaboratively between the divisions. In December 2014, the 113th Congress updated FISMA as the Federal Information Security Modernization Act (Public Law 113-283). NIST ITL responsibilities were unchanged in the update. In 2016, the ITL Cybersecurity Program addressed its assignment through the following major activities:

- **Forty-three NIST Special Publications (SP)** (20 approved as final and 23 drafts) were issued, providing management, operational, and technical security guidelines in topic areas including:
  - The 2015 annual report; cryptography (cryptographic standards used for the Federal Government, block cipher modes of operation, related key management, random bit generator (RBG), Secure Hash Algorithm-3 (SHA-3) cryptography, and transitioning the use of cryptographic algorithms and key lengths); mobile security (enterprise telework, remote access and bring-your-own device (BYOD), mobile device security – cloud and hybrid builds): application whitelisting; cyber threat sharing; cybersecurity event recovery; data-centric system threat modeling; de-identifying government datasets; asset management – financial services; guidelines for checklist users and developers; networks of “things”; personal identification verification (PIV); protecting Controlled Unclassified Information within nonfederal information systems and organizations; securing Apple Operating System (OS) X; security content automation protocol (SCAP); systems engineering; trustworthy email; and virtual machine (VM) protection.
- **Thirty-one NIST Interagency/Internal Reports (NISTIR)** (18 approved as final and 13 drafts) were issued on a variety of topics, including:
  - Cryptography (post-quantum cryptography, lightweight cryptography, NIST cryptographic standards and guidelines development process); mobile security (mobile devices, infrastructure and platforms); attribute metadata; automation for security control assessments; catalyzing the identity ecosystem; de-identification of personal information; Long-Term Evolution (LTE) architecture overview and security analysis; PIV; policy machine (access control framework); public safety mobile applications; SCAP; security of interactive and automated access management using Secure Shell (SSH); software identification (SWID) tags; strategic U.S. Government engagement in international standardization; trusted geolocation in the cloud; and vulnerability description ontology (VDO).
- **The National Cybersecurity Center of Excellence (NCCoE)** moved into a new permanent facility:
  - This facility was made possible by the state of Maryland and Montgomery County, Maryland, and has almost 60,000 square feet of modern physical space and IT systems. The new facility expanded the Center’s workspace from four to twenty-two separate, flexible laboratories—including: two larger areas capable of safely housing large equipment (including a vehicle that will be used in an upcoming project on auto-cybersecurity issues). This additional space allows NCCoE to increase its collaboration and to undertake new projects.
- **The Strategic Plan for the National Initiative for Cybersecurity Education (NICE)** was issued:
  - With a mission of energizing and promoting a robust network and an ecosystem of cybersecurity education, training, and workforce development, this plan lays out important goals for the cybersecurity workforce. (See: `http://csrc.nist.gov/nice/about/strategicplan.html`)
- **A draft Cybersecurity Framework profile for manufacturers** was developed and issued:
  - This profile can be used as a roadmap for reducing cybersecurity risk for manufacturers and is aligned with manufacturing sector goals and industry best practices.
- **The Baldrige Cybersecurity Excellence Builder (BCEB) self-assessment tool** was developed and issued for public comment:
  - The BCEB, aligned to the Cybersecurity Framework, is a self-assessment tool to help organizations better understand the effectiveness of their cybersecurity risk management efforts. (See: `https://www.nist.gov/baldrige/products-services/baldrige-cybersecurity-initiative`)
- **Continued to research, evaluate and develop standards for Post-Quantum Cryptography (PQC):**
  - NIST announced a Call for Proposals to solicit, evaluate, and standardize quantum-resistant public key cryptography (a.k.a. post-quantum cryptography (PQC)) algorithms through a Federal Register Notice (FRN). The team solicited public comments regarding requirements and evaluation criteria, which were subsequently finalized. NIST plans to spend three to five years analyzing the submitted algorithms before selecting algorithms for standardization, during which time NIST will engage with the research community through conferences and workshops.
- **Initiated a lightweight cryptography project** to study the performance of the current NIST-approved cryptographic standards on constrained devices:
  - To better understand the need for dedicated lightweight cryptography, ITL has created a portfolio of lightweight primitives through an open process. ITL will evaluate and recommend algorithms based on profiles, which consist of a set of design goals, physical characteristics of target devices, performance characteristics imposed by the applications, and security characteristics.
- **Continued to develop expertise in several critical research areas in cryptography:**
  - ITL continues to conduct research into post-quantum cryptography (PQC), quantum algorithms, elliptic curve cryptography (ECC), privacy-enhancing cryptography, and lightweight cryptographic schemes for constrained environments.
- **A NIST/Industry joint working group** was created to study the automation of cryptographic implementation testing:
  - After working with industry on the protocol necessary to exchange cryptographic test data in an automated fashion, the development of the cryptographic algorithm testing service to be hosted at NIST was begun, with the full implementation expected to take approximately one year. (See: `http://csrc.nist.gov/projects/acvt`)
- **Continued research and reporting results in software testing:**
  - In software testing, the oracle problem refers to determining the expected output for a given set of inputs. A determination of the expected output normally requires human involvement or a mathematical model of the specification. ITL has developed an oracle-free software testing method for which NIST filed a patent application. The test settings for an input factor may represent ranges of values (called equivalence classes) for which the output is expected to remain unchanged.
- **Continued research and development of a new conformance test tool** for the ANSI/NIST-ITL Machine Readable Table (MRT) Biometric Data Formats:
  - A command-line interface was developed that tests the MRTs themselves for conformance to the specification, in addition to testing American National Standards Institute (ANSI)/NIST-ITL Transactions. An initial graphical user interface was also developed to allow an easy-to-use software suite for end users. National standard bodies were encouraged to further the advancements of biometric data interchange format standards.
- **Represented the NIST/NTIA PSCR** (Public Safety Communications Research Program), FirstNet (the US First Responders’ Network Authority), and Public Safety stakeholders in the 3GPP (Third Generation Partnership Project):
  - The International Standards Organization, which is developing the next-generation telecommunications standard, LTE (Long Term Evolution), is ensuring that features critical to Public Safety are incorporated into the standards.
- **Continued refinement and support for the USG Federal Identity Program:**
  - In continued support of Homeland Security Presidential Directive-12 (HSPD-12) and Federal Information Processing Standard 201-2 (FIPS 201-2), the NIST Personal Identity Verification (PIV) Program updated and refined several supporting documents.
- **Continued involvement, research, and development of Virtualization Guidance and Standards:**
  - As a natural follow-up to the publication of the security guidelines for hypervisor deployment for server virtualization, ITL published SP 800-125B, *Secure Virtual Network Configuration for Virtual Machine (VM) Protection*, after extensive public comments, followed by a conference paper titled “Analysis of Virtual Networking Options for Securing Virtual Machines.” ITL also submitted two Special Publications and three conference papers on Virtualization Security to ISO/IEC JTC1/SC27/WG4 as a NIST/US Contribution. The submissions have now resulted in the ISO/IEC working draft 21878.
- **Ongoing involvement and outreach support among various programs:**
  - ITL provided assistance to agencies and the private sector through many outreach programs, including the National Initiative for Cybersecurity Education (NICE), the Federal Information Systems Security Educators’ Association (FISSEA), and the Federal Computer Security Managers’ Forum.
- **Significant contributions in the design, standardization, test and measurement of technologies** to improve the security and robustness of the Internet’s global routing protocol (Border Gateway Protocol (BGP)):
  - ITL’s Internet Infrastructure Protection (IIP) program works with industry to develop the measurement science and new standards necessary to ensure the robustness, scalability, and security of the global Internet.
- **Continued research and testing with the Usability and Security project:**
  - The ITL usability team’s research focused primarily in four areas: passwords, understanding user behavior, cryptography, and privacy.
- **Continued research, developing and updating support tools, and providing resources** for the Software Assurance and Reliability, and Computer Forensics projects:
  - ITL produced reference data and test methods for computer forensics and software quality to support the needs of the software assurance, law enforcement, and forensics communities for quality and efficiency improvements.
- **Support of FISMA, ITL conducted workshops, awareness briefings, and outreach** to ITL customers:
  - These outreach activities help to ensure a clear comprehension of standards and guidelines, help share ongoing and planned activities, and help ensure that guidelines are scoped in a collaborative, open, and transparent manner.
  - ITL public workshops addressed a diverse range of information security and technology topics, including:
    - NICE National K-12 Cybersecurity Education Conference
    - NICE Annual Conference
    - Applying Measurement Science in the Identity Ecosystem Workshop
    - Federal Information Systems Security Educators’ Association (FISSEA) Annual Conference
    - Privacy Controls Workshop: Next Steps for SP 800-53 Appendix J
    - NIST Trusted Identities Group (TIG) Federated Identity in Healthcare Pilot Program
    - Cybersecurity Framework Workshop
    - Open Meeting of The Commission on Enhancing National Cybersecurity
    - NIST Cloud Computing Forum & Workshop IX
    - Information Security Privacy Advisory Board (ISPAB) Meetings
    - National Strategic Computing Initiative (NSCI): High-Performance Computing Security Workshop
    - Exploring the Dimensions of Trustworthiness: Challenges and Opportunities
    - Trustworthy Suppliers Framework Forum
    - Best Practices in Cyber Supply Chain Risk Management
    - Random Bit Generation Workshop
    - Workshop on Software Measures and Metrics to Reduce Security Vulnerabilities
    - Software Identification (SWID) Tag Implementation and Use Workshop
    - Software and Supply Chain Assurance Forums
    - Cybersecurity for Small Manufacturers webinar series
    - Retail Cybersecurity Workshop
    - Strengthening Cybersecurity in the Financial Sector with the new NIST Practice Guide
    - Cybersecurity in Retail: Trends and Challenges with Point of Sale and Payment Technologies
- **Annual Reports:**
  - The 2016 ITL Cybersecurity Program Annual Report (formerly titled Computer Security Division Annual Report) was produced and released as a NIST SP. Former CSD annual reports from fiscal years 2003 through 2015 are available on the Computer Security Resource Center (CSRC) at `https://csrc.nist.gov/Publications/Search?requestStatusList=1,3&requestSeriesList=3,1,4,2,8,13,7,9,6,5,10,11,12&requestSortOrder=7&requestDisplayOption=brief&itemsPerPage=25&requestControlFamilyType=All&requestTopicType=All&requestControlFamilyList=&requestTopicList=15`

---

## ITL Cybersecurity Program Accomplishments for Fiscal Year 2016
In FY 2016, ITL continued to research and develop guidance in a broad array of technical areas, including supply chain risk management; forensics, software, security analytics, usability and security, cloud, mobile, and privacy-enhancing technologies; hardware-enabled security; cyber-physical and embedded systems; and other projects. ITL staff and guest researchers have collaborated with global partners from government, industry, and academia, making significant contributions to help secure critical information and the infrastructure. The following sections describe ITL’s Cybersecurity Program achievements, including extensive research and development for high-quality, cost-effective security and privacy mechanisms, standards, guidelines, tests, and metrics that address current and future computer and information security challenges.

*(Editors’ Note: Acronyms used throughout this Annual Report are generally defined when first used. A complete list of Acronyms used in this report is provided in Appendix A of this Annual Report.)*

---

## ITL Involvement with National and International IT Security Standards
![SDOs involved in Cybersecurity](Image of SDOs involved in Cybersecurity)

Figure 1 shows many of the national and international standards-developing organizations (SDOs) involved in cybersecurity standardization. Various ITL staff participate in many cybersecurity standards’ activities either in leadership positions or as editors and contributors, including the American National Standards Institute (ANSI); the International Organization for Standardization (ISO); the International Electrotechnical Commission (IEC); the Biometric Application Programming Interface (BioAPI) Consortium; the Bluetooth Special Interest Group (SIG); Bluetooth Security Expert Group (BT-SEG); the International Telecommunications Union - Telecommunication Standardization Sector (ITU-T); various groups within the Institute of Electrical and Electronics Engineers (IEEE) and the Internet Engineering Task Force (IETF); the North American Security Products Organization (NASPO); the Trusted Computing Group (TCG); and Accredited Standards Committee X9, Inc. (ASC X9, Inc.) (e.g., X9F – Data & Information Security Subcommittee). Many of ITL’s publications have been the basis for both national and international standards projects.

### Focus on ISO and ANSI Standardization (ISO/IEC JTC1 SC27 IT Security)
The following paragraphs discuss ITL staff activities in conjunction with the InterNational Committee for Information Technology Standards (INCITS) Technical Committee Cybersecurity 1 (CS1), where ITL’s Sal Francomacaro serves as the CS1 Vice Chair. CS1 is the U.S. counterpart for the ISO/IEC SC27 committee for IT Security.

### IT Security Techniques Standards
ITL staff actively participate with JTC1/SC27 and its working groups to develop standards for the protection of information and Information and Communications Technology (ICT). This includes generic methods, techniques and guidelines to address both security and privacy aspects, such as:

- Management of information and ICT security; in particular, information security management systems, security processes, and security controls and services;
- Cryptographic and other security mechanisms, including but not limited to, mechanisms for protecting the accountability, availability, integrity and confidentiality of information;
- Security management support documentation, including terminology and guidelines as well as procedures for the registration of security components;
- Security aspects of identity management, biometrics and privacy;
- Conformance assessment, accreditation and auditing requirements in the area of information security management systems; and
- Security evaluation criteria and methodology.

ITL staff also engages in active liaison and collaboration with appropriate bodies to ensure the proper development and application of SC 27 standards and technical reports in relevant areas.

**CONTACT:**  
Mr. Salvatore Francomacaro  
(301) 975-6414  
salvatore.francomacaro@nist.gov  

### Next Generation Access Control Standards
ITL has continued the development of an advanced Attribute Based Access Control (ABAC) framework called the Policy Machine, which was designed to be in alignment with an emerging ANSI/INCITS standard under the title of “Next Generation Access Control” (NGAC).

The NIST Policy Machine research and development effort has resulted in three ongoing national standards projects in CS1 in the early stages of development. They include:

- **Next Generation Access Control – Functional Architecture (NGAC-FA):** Project number INCITS 499-2013, was published in FY 2013 and is currently under revision.
- **Next Generation Access Control – Generic Operations & Abstract Data Structures (NGAC-GOADS):** Serban Gavrila, ITL, is the editor. The project is assigned project number 2195-D, and the document was published during FY 2016.
- **Next Generation Access Control - Implementation Requirements, Protocols and API Definitions (NGAC-IRPADS):** Project number 2193-D has been assigned. This part will be published as a technical report in FY 2018.

**CONTACTS:**  
Mr. David Ferraiolo  
(301) 975-3046  
david.ferraiolo@nist.gov  

Mr. Serban Gavrila  
(301) 975-4343  
serban.gavrila@nist.gov  

### ISO Standardization of Security Requirements for Cryptographic Modules
ITL has contributed to the activities of ISO/IEC JTC 1 SC/27, which published ISO/IEC 19790, *Security Requirements for Cryptographic Modules*, on March 1, 2006, and ISO/IEC 24759, *Test Requirements for Cryptographic Modules*, on July 1, 2008. ISO/IEC 19790 specifies the security requirements for a cryptographic module utilized within a security system protecting sensitive information in computer and telecommunication systems. These efforts bring consistent testing of cryptographic modules to the global community by providing ISO-equivalent standards representing FIPS 140-2, *Security Requirements for Cryptographic Modules* and Derived Test Requirements [DTR] for FIPS 140-2, *Security Requirements for Cryptographic Modules*. Mr. Randall Easter (CSD) continues as the principal editor for these standards.

ISO/IEC JTC 1/SC 27 Working Group (WG) 3 completed and published revisions, followed with updated corrections, of ISO/IEC 19790:2006 and ISO/IEC 24759:2008. The revision of ISO/IEC 19790 was published on August 15, 2012. The revision of ISO/IEC 24759 was published on January 31, 2014. Both ISO/IEC standards were also adopted by the American National Standards Institute (ANSI) (see: `http://webstore.ansi.org/RecordDetail.aspx?sku=ISO%2FIEC+19790%3A2012`). The two ISO/IEC revisions were developed with international support and the collaboration of governments, industry and academia. Revised corrections of both standards were published on December 15, 2015.

The revision of ISO/IEC 19790:2012 addresses new security areas, such as defined software module boundaries, degraded modes of operation, trusted channels, two-factor authentication, software security, mitigation of fault induction and side-channel attacks, operational self-tests for algorithms, and lifecycle assurance from design to end-of-life.

![Cryptographic Module Testing – ISO Standards](Chart showing ISO/IEC standards for Cryptographic Module Testing)  
*Figure 2: Cryptographic Module Testing – ISO Standards is a chart of the ISO/IEC standards, as explained above, in which CSD has played a part during the development process.*

In addition to the aforementioned standards, International Standards ISO/IEC 17825, *Testing methods for the mitigation of non-invasive attack classes against cryptographic modules*, is expected to be published in January 2017 and ISO/IEC 18367, *Cryptographic algorithms and security mechanisms conformance testing*, is on target to be published during December 2016. Mr. Easter was the editor of both standards.

International Standard ISO/IEC 17825 specifies the non-invasive attack mitigation test metrics for determining conformance to the requirements specified in ISO/IEC 19790 for Security Levels 3 and 4. The test metrics are associated with the security functions specified in ISO/IEC 19790. Testing will be conducted at the defined boundary of the cryptographic module and using Input/Output (I/O) available at the defined boundary.

International Standard ISO/IEC 18367 describes conformance testing methods for cryptographic algorithms and security mechanisms. Conformance testing assures that an implementation of a cryptographic algorithm or security mechanism is correct whether implemented in hardware, software or firmware. It also confirms that it runs correctly in a specific operating environment. Testing may consist of known-answer or Monte Carlo testing, or a combination of test methods. Testing may be performed on the actual implementation or modeled in a simulation environment.

The test methods used by testing laboratories to test whether the cryptographic module conforms to the requirements specified in ISO/IEC 19790 and the test metrics specified in this International Standard for each of the associated security functions specified in ISO/IEC 19790 are specified in ISO/IEC 24759. The test approach employed in this International Standard is an efficient “push-button” approach: the tests are technically sound, repeatable and have moderate costs.

ITL is also the principal editor or co-editor of other ISO/IEC documents. ITL’s contributions to the development of these international standards create a strong foundation for the adoption of and migration from currently used national standards. In particular, this adoption will promote international harmonization for the implementation and testing of cryptographic algorithms and modules, while accommodating individual country preferences in the choice of approved security functions.

**FOR MORE INFORMATION, SEE:**  
`http://csrc.nist.gov/groups/STM/`  

**CONTACT:**  
Mr. Randall J. Easter  
(240) 361-8777  
randall.easter@nist.gov  

### Identity Management Devices and Infrastructures Standards (JTC1 SC17 Cards and Personal Identification Devices)
In the area of Identity Tokens and Secure elements, ITL has provided...

---

ed the technical and editorial support of Mr.
Specifically, ITL is contributing to the development of
Ketan Mehta (CSD) in the development and amendment of
passport data structure and its access control. ITL reviews
American National Standard (ANS) 504, Generic Identity
and comments on authentication protocols that are
Command Set (GICS). GICS enables Personal Identity
developed to ensure strong user authentication and to
Verification (PIV), PIV-Interoperable (PIV-I) and Common
protect personally identifiable passport data.
Access Card (CAC) applications, and others, to be built from
a single platform. GICS defines an open platform where Mobile Driver License: ITL is also participating in the
development of an ISO standard (ISO/IEC 18013) for an
identity applications can be instantiated, deployed, and used
International Mobile Driver License (DL). During 2016, ITL
in an interoperable way between the credential issuers and
gathered and discussed functional and security requirements
credential users that aligns with the last revision of the NIST
for Mobile DLs. ITL is now developing two models for the
SP 800-73-4, Interfaces for Personal Identity Verification,
Mobile DLs, namely, offline and online models. Once these
(PIV) specifications.
models are correctly defined, ITL plans to write technical
During FY 2017, ITL staff plans to:
specification for each model.
• Contribute to the publication of several revisions of
CONTACTS:
the ISO/IEC 7816 family of standards (Identification
cards - Integrated circuit cards), which are all Mr. Salvatore Francomacaro Mr. Ketan Mehta
relevant to FIPS 201, Personal Identity Verification (301) 975-6414 (301) 975-8405
(PIV) of Federal Employees and Contractors, salvatore.francomacaro@nist.gov ketan.mehta@nist.gov
specifications;
• Pursue the standardization and harmonization of
Cloud Computing Standards
identity standards developed in the U.S.;
Within ISO/IEC JTC 1/SC 38
• Develop requirements and identify standards gaps Cloud Computing and INCITS
for Mobile Driving Licenses;
Cloud 38
• Enhance the Machine-Readable Travel Documents
During FY 2016, ITL has been designated by the Federal
(ePassport) data model to address privacy and
Chief Information Officer (CIO) to accelerate the Federal
security concerns; and
Government’s secure adoption of cloud computing by
• Contribute to the development of privacy- leading efforts to identify existing standards and guidelines.
enhanced security protocols. Where standards are needed, ITL works closely with U.S.
industry, standards developers, other government agencies,
ITL staff will continue to actively support relevant ID
and leaders in the global standards community to develop
management standard initiatives, such as ISO/IEC 19286,
standards that will support secure cloud computing.
Integrated circuit card (ICC) Privacy-enhancing protocols
and services, and ISO/IEC 18328, ICC managed devices. This standardization effort supports federal agencies in
adopting and implementing cloud computing infrastructures.
Web Authentication/FIDO: ITL participates in the
This standard work includes standards development within
development of online authentication specifications.
the voluntary, consensus-based standards ecosystem and
These specifications are developed by the Fast Identities
the development of NIST standards and guidelines for
Online (FIDO) alliance, which is a consortium of private
federal agencies, as required by government mandates.
organizations. ITL also participates in the development of
The ITL staff participates in developing standards for many
similar specifications (called WebAuthn) for web browsers
aspects of cloud computing. ITL participation helps to
that are being developed by the W3C consortium. Both the
ensure the alignment of NIST standards with those of ISO/
FIDO and WebAuthn specifications enable relying parties to
IEC sub-committees, such as SC 27, SC 38 and their U.S.
create cryptographic tokens on the end-user’s device and
counterparts, ANSI/INCITS CS1 and Cloud 38. The large
subsequently use this cryptographic token to authenticate
13
number of standards being developed in SC 27 covering
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

areas (such as security, privacy, supply chain, personally RISK MANAGEMENT
identifiable information (PII) processing or virtualization
security) interweave with many cloud computing standards
Framework for Improving Critical
being developed by these subcommittees.
Infrastructure Cybersecurity
Ms. Annie Sokol is a member of ITL’s Cloud Computing
(Cybersecurity Framework)
team and the CSD representative in the standards develop-
ment program. ITL provides technical and editorial Recognizing that the national and economic security of
representation in the development of national and interna- the United States depends on the reliable functioning of its
tional standards in both SC 27 and SC38. Ms. Sokol is currently critical infrastructure, the President issued Executive Order
the co-editor of ISO/IEC 19941, Information technology– (EO) 13636, Improving Critical Infrastructure Cybersecurity,
Cloud computing–Interoperability and portability, which in February 2013. This EO directed NIST to work with
is intended to establish a common understanding of cloud stakeholders to develop a voluntary framework—based on
computing interoperability and portability. This document is existing standards, guidelines, and practices—for reducing
of interest to cloud stakeholders focusing on cloud service cybersecurity risks to critical infrastructures.
agreements concerning interoperability or portability among
The Cybersecurity Framework that was developed
cloud services. The ISO/IEC 19941 work aligns with ITL staff
provides a prioritized, flexible, repeatable, performance-based,
involvement in the SC 38 development of ISO/IEC 19086-4
and cost-effective approach to help critical infrastructure
(DIS), Information technology–Cloud computing–Service
owners and operators—as well as other interested entities—
level agreement (SLA), which has four parts. Of particular
to identify, assess, and manage cybersecurity-related risk,
interest, ISO/IEC 19086 – Part 1 was published in 2016 and
while protecting business confidentiality, individual privacy,
establishes a set of common cloud SLA building blocks (e.g.
and civil liberties.
concepts, terms, definitions, contexts) that can be used to
create cloud Service Level Agreements (SLAs). In FY 2016, ITL continued to work with a diverse
stakeholder community to support the use and understanding
CONTACT:
of the Cybersecurity Framework. This process included:
Ms. Annie Sokol • Issuing a Request for Information (RFI) to formally
(301) 975-2006 gather stakeholder input about Framework
annie.sokol@nist.gov use, evolution, and future governance of the
Framework;
Biometric Standards and • Conducting a public workshop at NIST in
Associated Conformity Gaithersburg, MD to gather input about the current
use of the Framework and the need for an update
Assessment Testing Tools
to the Framework as well as future governance of
CSD’s Biometric Standards and Associated Conformity
the Framework;
Assessment Testing Tools team contributes to the
• Releasing the draft Baldrige Cybersecurity
development of biometric standards. The team reviews
Excellence Builder, a self-assessment tool to help
standards documents, develops contributions and feedback
organizations better understand the effectiveness
and participates in technical and editorial discussions to
of their cybersecurity risk management efforts;
substantiate NIST and ITL’s goals in the biometric field. The
team participates in the International Committee for • Coordinating with critical infrastructure owners
Information Technology Standards (INCITS) Technical and operators, regulators, and other industry
Committee M1 – Biometrics standards body and related organizations through a variety of meetings and
subcommittees. The team also participates in the industry events to ensure the understanding and
International Organization for Standardization/International use of the Framework;
Electrotechnical Commission (ISO/IEC) Joint Technical
• Analyzing various industry work products
Committee (JTC) 1 Subcommittee (SC) 37 – Biometrics
(such as mapping documents) for Framework
standards body.
correctness;
CONTACT:
• Consulting with state and local governments,
and the governments of other nations regarding
Mr. Dylan Yaga
14 their alignment with both the principles and the
(301) 975-6004
cybersecurity outcomes of the Framework;
dylan.yaga@nist.gov
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

• Consulting with international organizations and Directives, and Office of Management and Budget
standards bodies to demonstrate and ensure (OMB) policies; and
continued alignment with voluntary international
• Conducting outreach to public and private-sector
standards; and
organizations to facilitate the application of the
• Working with both industry and regulatory suite of standards and guidelines that support the
organizations to apply the Framework in ways that NIST Risk Management Framework (RMF) (see
bring efficiencies to the regulatory process. http://csrc.nist.gov/groups/SMA/fisma/framework.
html).
Since the release of the Framework, NIST’s primary
goal has been to raise awareness of the Framework, and During FY 2016, the ITL FISMA Implementation project
encourage its use as a tool to help industry sectors and continued to strengthen collaboration through the Joint Task
organizations manage cybersecurity risks. Force (JTF) Transformation Initiative, which includes the
Department of Defense (DOD), the Intelligence Community
In FY 2017, ITL will continue to conduct stakeholder
(IC), and the Committee on National Security Systems
outreach and will work collaboratively to further understand
(CNSS), and various federal agencies. The JTF partners
stakeholder needs regarding tools and resources to enable
continue to develop and update key cybersecurity guidelines
more effective use of the Framework. Additionally, in early
for protecting federal information and information systems
2017, NIST will publish a minor update to the Framework
as part of the Unified Information Security Framework.
and will minimize any disruption to current Framework
Previously, the JTF developed common security guidance
users by focusing on clarification and refinement. NIST will
in the critical areas of security controls for information
also publish guidance on how Federal agencies can use
systems and organizations, security assessment procedures
the Cybersecurity Framework, particularly illustrating how
to demonstrate security control effectiveness, security
the Risk Management Framework (Special Publication (SP)
authorizations for risk acceptance decisions, and continuous
800-37 Revision 1, Guide for Applying the Risk Management
monitoring activities to ensure that decision makers receive
Framework to Federal Information Systems: A Security
the most up-to-date information on the security state of
Life Cycle Approach) and Cybersecurity Framework can
their information systems. In addition, ITL worked with
work together to help agencies develop, implement, and
the Department of Homeland Security (DHS) to develop
continuously improve their information security programs.
guidelines for automation support for security control
FOR MORE INFORMATION, SEE:
assessments on a security capability basis and in accordance
with the NIST RMF.
https://www.nist.gov/cyberframework
In FY 2016, the ITL FISMA Team worked on the following
CONTACTS: initiatives:
Team email: cyberframework@nist.gov • System Security Engineering Initiative: The
final public draft of SP 800-160, Systems Security
Mr. Matt Barrett Mr. Jeff Marron Engineering: Considerations for a Multidisciplinary
(301) 975-6259 (301) 975-3846 Approach in the Engineering of Trustworthy
matthew.barrett@nist.gov jeffrey.marron@nist.gov Secure Systems, was published to address the
engineering-driven actions necessary to develop
more defensible and survivable systems—including
Federal Information Security
the components that compose and the services
Management Act (FISMA)
that depend on those systems. To ensure that
Implementation Project
the publication provides the utmost clarity and
The FISMA Implementation Project focuses on: focus for our customers, several of the supporting
appendices from the second public draft are being
• Developing a comprehensive series of standards
recast into their own publications. SP 800-160
and guidelines to help federal and nonfederal
will become the flagship publication for the NIST
organizations build effective information
Systems Security Engineering Initiative. NIST
security programs, defend against increasingly
publications specifically addressing several key
sophisticated cyber-attacks, and demonstrate
systems security engineering considerations (i.e.,
compliance to security requirements set forth in
resilience, software assurance, and hardware
legislation, Executive Orders, Homeland Security
15
assurance) will be developed and published,
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
https://dx.doi.org/10.6028/NIST.SP.800-195

beginning in 2017. Additionally, the interaction of 1. SP 800-30, Guide for Conducting Risk
the NIST RMF with the life cycle processes in SP Assessments;
800-160, will be described in future updates to
2. SP 800-37, Guide for Applying the Risk
existing RMF standards and guidelines.
Management Framework to Federal
• Risk Management Guidelines: Work began on SP Information Systems: a Security Life Cycle
800-53 Revision 5, Security and Privacy Controls Approach;
for Systems and Organizations, with a pre-draft call
3. SP 800-39, Managing Information
for comments, adjudication of those comments,
Security Risk: Organization, Mission, and
and coordination with our JTF partners. SP
Information System View;
800-53 provides organizations with the security
and privacy controls necessary to appropriately 4. SP 800-53, Security and Privacy Controls
for Federal Information Systems and
strengthen their systems and the environments
Organizations; and
in which those systems operate, and provides a
process for selecting the appropriate controls, 5. SP 800-53A, Assessing Security and
which contributes to systems that are resilient in Privacy Controls in Federal Information
the face of attacks and other threats and protect Systems and Organizations: Building
an individual’s privacy. The implementation of SP Effective Assessment Plans.
800-53, SP 800-37, Guide for Applying the Risk
The FISMA Team also collaborated with DOD, the IC, DHS,
Management Framework to Federal Information
the National Archives and Records Administration (NARA),
Systems, and SP 800-137, Information Security
the Federal Emergency Management Agency (FEMA),
Continuous Monitoring for Federal Information
the Government Accountability Office (GAO), the Office
Systems and Organizations, provides organizations
of Management and Budget (OMB), the General Services
with near real-time information that is essential for
Administration (GSA), the Small Business Administration
senior leaders making ongoing risk-based decisions
(SBA), and the Inspectors General (IGs) on multiple projects
affecting their critical missions and business
to ensure consistency with FISMA-related guidance and to
functions.
protect information in a way that is commensurate with
• FISMA Outreach Activity to Public and Private- risk. In addition, the FISMA Team served as co-chairs on the
Sector Organizations: Cybersecurity outreach Committee on National Security Systems working groups.
briefings were conducted and support was
In FY 2016, the FISMA Team completed the following
provided to all levels of private-sector organizations
activities:
and government (including federal, state and local
• Published the final public draft of SP 800-160,
entities) on multiple information security topics of
Systems Security Engineering: Considerations for
interest. These included, for example, an effective
a Multidisciplinary Approach in the Engineering of
implementation of the NIST RMF, contingency
Trustworthy Secure Systems;
planning, interconnection security agreements,
security-focused configuration management, • Started the development of SP 800-53, Revision
and information security for small businesses. 5, Security and Privacy Controls for Systems and
In addition, the ITL FISMA Team responded to Organizations;
hundreds of inquiries from customers, served on
• Published the Initial Public Draft (IPD) of
cybersecurity advisory panels, and conducted
SP 800-171 Revision 1, Protecting Controlled
outreach activities with academic institutions,
Unclassified Information in Nonfederal Information
providing information on NIST’s security standards
Systems and Organizations, to provide guidance
and guidelines, and exploring new areas of
to federal agencies for the protection of
cybersecurity research and development.
Controlled Unclassified Information when such
• Collaboration with JTF partners and other information is resident in nonfederal systems and
federal organizations: The FISMA Team worked organizations;
closely with JTF partners to ensure that the five
• Published the IPDs of NISTIR 8011, Automation
JTF publications remain current, and to designate
Support for Ongoing Assessments, Volume
additional special publications as JTF guidance.
1 - Overview, and Volume 2 - Hardware Asset
16 The five JTF publications are:
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
https://dx.doi.org/10.6028/NIST.SP.800-195

Management, and adjudicated public comments in effective implementation of the RMF; and
partnership with DHS;
• Continue the collaboration with JTF partners and
• Started the development of a web application other federal organizations.
to automate the process for updating SP 800-
FOR MORE INFORMATION, SEE:
53 in order to keep it as current and relevant as
possible; http://csrc.nist.gov/groups/SMA/fisma
• Continued the development of SP 800-60,
CONTACTS:
Revision 2, Guide for Mapping Types of Information
and Information Systems to Security Categories, The ITL FISMA Team email is: sec-cert@nist.gov
in partnership with the National Archives and
Records Administration; and Dr. Ron Ross Mr. Nedim Goren
(301) 975-5390 (301) 975-5233
• Continued the development of the initial public
ron.ross@nist.gov nedim.goren@nist.gov
draft of SP 800-18 Revision 2, Guide for Developing
Security Plans for Federal Information Systems and Ms. Kelley Dempsey Ms. Peggy Himes
Organizations. (301) 975-2827 (301) 975-2489
In FY 2017, the FISMA Team intend to: kelley.dempsey@nist.gov peggy.himes@nist.gov
• Finalize SP 800-160, Systems Security Engineering:
Considerations for a Multidisciplinary Approach Privacy Engineering Program
in the Engineering of Trustworthy Secure
ITL research in information technology, including
Systems;
cybersecurity, cloud computing, big data, the Smart Grid and
• Finalize and publish the IPD of SP 800-53, Revision other cyber-physical systems; aims to improve the products
5, Security and Privacy Controls for Systems and and services that bring great advancements to U.S. national
Organizations, and continue the development of and economic security and the quality of life. Much of this
the final publication; research pertains to the trustworthiness of these information
technologies and the systems in which they are incorporated.
• Complete the development of a web application
Given concerns about how information technologies may
for the automated support of SP 800-53 updates
affect privacy at individual and societal levels, the ITL Privacy
and the public comment process;
Engineering Program (PEP) supports the development of
• Continue the collaboration with DHS to develop
trustworthy information systems by applying measurement
and publish additional NISTIR 8011 volumes;
science and system engineering principles to the creation of
• Finalize and publish the initial public draft of SP frameworks, risk models, guidance, tools, and standards that
800-60, Revision 2, Guide for Mapping Types protect privacy, and by extension, civil liberties. The PEP also
of Information and Information Systems to seeks to promote NIST and ITL leadership in privacy research
Security Categories in partnership with NARA and and privacy-enhancing technologies.
OMB;
The PEP was formally established as a program in FY
• Continue the development of SP 800-18, Revision 2016 as part of ACD. In 2014, the PEP team initiated research
2, Guide for Developing Security Plans for Federal with two workshops to explore the foundations of privacy
Information Systems and Organizations; engineering and risk management and published a draft
of NISTIR 8062, An Introduction to Privacy Engineering
• Finalize and publish NIST SPs 800-12 Revision 1, An
and Risk Management in Federal Systems, in May 2015 to
Introduction to Information Security, and 800-
introduce a novel set of privacy engineering objectives and a
47 Revision 1, Security Guide for Interconnecting
privacy risk assessment framework (see http://nvlpubs.nist.
Systems;
gov/nistpubs/ir/2017/NIST.IR.8062.pdf).
• Expand cybersecurity outreach to include
In FY 2016, the PEP focused resources in the following
additional state, local, and tribal governments, as
areas: developing a near-term strategic plan, finalizing
well as private-sector organizations and academic
NISTIR 8062, and coordinating with other NIST programs
institutions;
and research efforts to address and integrate privacy.
• Continue to support federal agencies in the The strategic plan is organized around the basic goals of
17
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

advancing the development of privacy engineering and risk The program also collaborated on many other projects,
management processes and the deployment of privacy- including a partnership PEP with TIG on a building block
enhancing technologies, as well as positioning NIST as a at the NIST National Cybersecurity Center of Excellence
leader in privacy research. (NCCoE) to use the new privacy engineering objectives (see
https://nccoe.nist.gov/sites/default/files/library/project-
Advancement of Privacy Engineering and Risk
descriptions/privacy-enhanced-identity-brokers-project-
Management
description-draft.pdf). There was also collaboration with
To further the development of processes for privacy CSD and NIST’s Engineering Laboratory (EL) on the big data
engineering and risk management (and inform its finalization and cyber-physical systems frameworks and related efforts,
of NISTIR 8062), the PEP team conducted outreach with and with ITL’s Information Access Division (IAD) to support
stakeholders, researched privacy assessment and risk a successful Build-the-Future proposal on de-identification,
mitigation methods, and supported the use of its Privacy Risk a process used to prevent a person’s identity from being
Assessment Methodology (PRAM) inside and outside the associated with information.
Federal Government. The PEP team also worked extensively
Figure 3: Collaboration Between PEP and Other NIST
with OMB on the revision of Circular A-130, which lays out
Programs in FY 2016 illustrates a number of projects from the
new requirements for federal agencies to address privacy risk
programs described above that PEP collaborated on in FY
in their information systems to ensure that the Circular and
2016. These projects can be categorized as applied privacy
the PEP were in alignment on privacy risk management.
projects or guidance and frameworks.
As a result of these efforts, the PEP team has revised
NIST Leadership in Privacy
NISTIR 8062 to more clearly introduce the concepts of
privacy engineering and risk management, clarify the The program worked across public and private-sector
rationale for the introduction of a set of privacy engineering organizations to advance NIST’s role in privacy. The PEP
objectives and a risk model, and include a roadmap for the team participated in the Internet Policy Task Force’s Privacy
development of comprehensive privacy risk management Working Group (see https://www.ntia.doc.gov/category/
guidance for federal agencies that parallels NIST guidance internet-policy-task-force) and now hold leadership
for information security. positions in the Federal Privacy Council (established by
Executive Order in FY 2016), and the Networking and
The PEP also co-hosted a workshop in September 2016
Information Technology Research and Development
with the Department of Transportation to gather input on
(NITRD) Program’s Privacy Research Interagency Working
changes to the privacy controls in Appendix J of NIST SP
Group, whose work included drafting the National Privacy
800-53, which is undergoing its fifth revision. The workshop
Research Strategy (see https://www.nitrd.gov/cybersecurity/
initiated the first stage of executing the guidance roadmap
nationalprivacyresearchstrategy.aspx), the Identity
that the PEP will continue in FY 2017.
Ecosystem Steering Group, and the Fast Identity Online
Coordination with Other NIST Programs
Alliance.
An important role for the PEP is a collaboration and The PEP team presented its research at major
coordination with other NIST programs and research efforts conferences, including the RSA Conference, the International
to better integrate privacy in the pursuit of more trustworthy Association of Privacy Professionals Global Summit and
systems. Privacy Academy, the Institute of Electrical and Electronics
Engineers International Workshop on Privacy Engineering,
Of particular note, the PEP put its preliminary concepts
the Privacy + Security Forum, the TRUSTe Privacy Risk
into practice with the PRAM, a set of worksheets that take an
Summit, and the Computing Community Consortium’s
organization through a privacy risk assessment of its systems.
Privacy by Design Workshop, among others.
Working with the ITL Trusted Identities Group (TIG), the PEP
team supports the TIG grant awardees’ use of the PRAM The PEP team contributed to ongoing standards and
to evaluate privacy risks and develop mitigating controls in framework development efforts in various organizations,
their pilots. The PEP team also used the PRAM for privacy including the Identity Ecosystem Steering Group, the Fast
evaluations of information systems in partnership with federal Identity Online Alliance, and the ISO.
agencies, including DHS and GSA. The lessons learned from
In FY 2017, the PEP will publish the final version of
these PRAM evaluations have been critical to the PEP team’s
NISTIR 8062, slated to be released in January 2017 (see
understanding of the practical aspects of applying privacy
http://nvlpubs.nist.gov/nistpubs/ir/2017/NIST.IR.8062.
18 risk management concepts in system development.
pdf). The PEP will also work on developing privacy risk
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 3: Collaboration Between PEP and Other NIST Programs in FY 2016
management guidance for federal agencies, beginning Cyber Supply Chain Risk
with a revision of the privacy controls in NIST SP 800-53. Management (SCRM)
The program will continue to collaborate with other NIST
Information and Communications Technology (ICT)
programs as they seek to address privacy challenges and will
relies on a complex, globally distributed, and interconnected
work with stakeholders to promote privacy engineering and
supply chain ecosystem to provide highly refined, cost-
risk management practices. The PEP team will also continue
effective, and reusable solutions. This ecosystem is composed
to seek leadership opportunities in public and private-
of various entities with multiple tiers of outsourcing, diverse
sector organizations to position NIST on the leading edge
distribution routes, assorted technologies, laws, policies,
of privacy research. Finally, The PEP will explore new areas
procedures, and practices, all of which interact to design,
for privacy research that have broad-based application and
manufacture, distribute, deploy, use, maintain, and manage
support federal agency mission-critical needs in managing
ICT products and services.
privacy risk.
The factors that allow for low-cost, interoperability,
FOR MORE INFORMATION, SEE:
rapid innovation, a variety of product features, and other
https://www.nist.gov/itl/privacy-engineering benefits, also increase the risk of a compromise to the ICT
supply chain, which may result in risks to the end user.
CONTACTS: These ICT supply chain risks may include an insertion of
counterfeits, unauthorized production, tampering, theft, and
PEP Team email: privacyeng@nist.gov
the insertion of malicious software and hardware as well as
Ms. Naomi Lefkovitz Ms. Ellen Nadeau poor manufacturing and development practices in the ICT
(301) 975-2924 (202) 306-4033 supply chain.
naomi.lefkovitz@nist.gov ellen.nadeau@nist.gov Cyber Supply Chain Risk Management (SCRM) is the
process of identifying, assessing, and mitigating the risks
(Editors’ Note: Mr. Sean Brooks was part of this project
associated with the distributed and interconnected nature
team and has since left NIST.)
of ICT product and service supply chains. It covers the 19
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

entire life cycle of a system (including design, development, further development of the Trustworthy Supplier Framework
maintenance, and destruction), as supply chain threats and by ITL in future updates to SP 800-161 and other related
and vulnerabilities may intentionally or unintentionally publications.
compromise an ICT product or service at any stage.
In FY 2017, ITL will continue to collaborate with
In FY 2016, ITL continued to research the state of Cyber stakeholders in government, industry, and academia to
SCRM in both the public and private sectors, related standards conduct research, produce needed standards and guidance,
and initiatives, effective practices, and metrics. ITL partnered and seek opportunities to create greater awareness across all
with a team composed of representatives from the Federal sectors and types and sizes of organizations. ITL will:
Government (GSA and DHS), the insurance industry (Zurich
• Conduct research and draft guidance on how
and Beecher Carlson) and academia (the University of
organizations identify critical systems and
Maryland) to begin fundamental research and build the tools
components that need additional protections;
necessary to measure and assess the actual effectiveness
• Conduct research on applicable metrics and
of cybersecurity strategies and controls. The effort will use
measures useful to cyber supply chain risk
voluntary, secure and anonymized risk assessments based
management;
on the NIST Cybersecurity Framework to begin developing
a large-scale anonymized data set that will, for the first time, • Conduct an effectiveness study with the goal of
demonstrate cause and effect relationships between cyber demonstrating cause-and-effect relationships
supply chain capability levels and organizational performance between cyber supply chain capability levels
outcomes over time. and organizational performance outcomes over
time;
Also in FY 2016, ITL co-chaired, with the Department of
Defense, the primary interagency working group on cyber • Continue to co-chair the interagency working group
SCRM to revise CNSS Directive (CNSSD) No. 505, Supply on cyber supply chain risk management, and also
Chain Risk Management, which assigns responsibilities to co-chair and sponsor the Software and Supply
and establishes minimum criteria for the development and Chain Assurance Forum;
deployment of capabilities for SCRM of National Security
• Continue to engage stakeholders in identifying
Systems. ITL also co-chaired the Software and Supply Chain
opportunities to create greater awareness about
Assurance (SSCA) Forum and Working Groups, the purpose
cyber supply chain risks and available standards,
of which is to bring together a stakeholder community of
practices, guidance and related tools; and
government, industry, and academic experts in this field.
• Continue to engage stakeholders in identifying
Meetings are held quarterly and cover a variety of subjects of
opportunities and needs for providing additional
interest to attendees.
guidance regarding identifying and implementing
In April 2016, ITL held a workshop regarding an update
supply chain protections.
to the NIST Cybersecurity Framework (CSF). During the
workshop, information was gathered in a breakout session FOR MORE INFORMATION, SEE:
regarding attendees’ views about improving how SCRM is
http://csrc.nist.gov/scrm/
covered in the CSF. Several ideas were proposed, and NIST
plans to incorporate the feedback into an updated version CONTACTS:
of the CSF.
ICT SCRM Team email: scrm-nist@nist.gov
In May 2016, ITL hosted a forum event led by the Institute
for Defense Analyses (IDA) about their Trustworthy Supplier Mr. Jon Boyens Ms. Celia Paulsen
Framework (TSF), a prototype toolbox that maps various (301) 975-5549 (301) 975-5981
existing standards and practices to the controls provided in jon.boyens@nist.gov celia.paulsen@nist.gov
NIST SP 800-161, Supply Chain Risk Management Practices
for Federal Information Systems and Organizations. The TSF
is intended to increase the utility of existing standards to
buyers and program managers making supplier selections,
while simultaneously allowing suppliers flexibility in
meeting procurement requirements. The forum provided an
opportunity for ITL to understand the needs of stakeholders
20
in this arena. The information will be used by IDA in their
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

BIOMETRIC STANDARDS AND
ASSOCIATED CONFORMITY
ASSESSMENT TESTING TOOLS
ITL supports the development of biometric
conformance testing methodology standards and other
conformity assessment efforts through active technical
participation in the development of these standards and
the development of associated conformance test software,
architectures and test suites, collectively known as Biometric
Conformance Test Software (BioCTS). These test tools are
developed to promote the adoption of these standards
and to support users, product developers, and testing labs
that require conformance to selected biometric standards.
ITL contributes to the development of biometric standards
Figure 4: ANSI/NIST-ITL Extractor Software
and participates in the INCITS Technical Committee M1
– Biometrics and related subcommittees and in ISO/IEC
The BioCTS team researched the new Machine Readable
Joint Technical Committee (JTC) 1 Subcommittee (SC) 37 –
Tables (MRTs) for the ANSI/NIST-ITL Biometric Standard
Biometrics standards bodies. ITL plans to continue this work
(AN-MRTs) to determine their suitability for integration into
in FY 2017.
conformance testing efforts. The AN-MRTs encode many
of the human-readable requirements specified in the base
ANSI/NIST-ITL Biometric Standard (and related profiles,
such as Federal Bureau of Investigation (FBI) Electronic
Biometric Transmission Specification (EBTS)) in a manner
that can be parsed and understood by software. The BioCTS
team developed software capable of parsing and testing
these tables to ensure a valid MRT format using MRT Schema
In FY 2016, the BioCTS team released refined
documents and MRT element definitions. The results of our
versions of existing software and researched the use of
tests were documented and provided to the authors of
machine-readable data to accelerate conformance test
the AN-MRTs for incorporation into future versions of the
development and increase support for profiles and user-
tables for the benefit of all MRT users. The software used
defined requirements.
to develop these results may be released in the future as
There were two updates to the BioCTS for ANSI/ a standalone tool for validating and analyzing AN-MRT
NIST-ITL (AN) software suite in FY 2016. These updates were files. The new BioCTS software will use the AN-MRTs as an
primarily focused on enhancing the underlying codebase, external resource. This will allow updates to be made to the
increasing performance, and adding more user-friendly MRTs to incorporate the latest conformance requirements,
features. The testing architecture has been updated to be correct errors, or conduct experiments without releasing an
more maintainable and more robust. The update represents updated version of BioCTS itself.
a complete overhaul of the BioCTS for AN’s initial release
An initial version of this software began development in
in 2012. A list of changes made to BioCTS for AN can be
FY 2016, and this effort is expected to continue in FY 2017.
found in the Changelog (see https://csrc.nist.gov/Projects/
FOR MORE INFORMATION, SEE:
Biometric-Conformance-Test-Software).
In addition to updates to BioCTS software, the BioCTS - Biometric Conformance Test Tools:
team released an updated ANSI/NIST-ITL Data Extractor,
https://www.nist.gov/itl/csd/biometrics/biometric-
illustrated in Figure 4: ANSI/NIST-ITL Extractor Software
conformance-test-software-biocts
which shows the internal data records within an ANSI/NIST-
ITL file. The Data Extractor allows data (images, text, etc.)
BioCTS for ANSI/NIST-ITL User Guide:
to be saved from an ANSI/NIST-ITL formatted file, as well
as providing a high-level overview of the file and its internal https://csrc.nist.gov/Projects/Biometric-Conformance-Test-
structure. Software/publications 21
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

CONTACT: interoperability. ITL is researching the cybersecurity and
privacy needs of the broader landscape of CPS by applying
Mr. Dylan Yaga their subject-matter expertise in cybersecurity and privacy
(301) 975-6004 to various instances of CPS. These instances may include
dylan.yaga@nist.gov industrial control systems, the smart grid, hardware-enabled
security, and embedded systems, to name a few.
In FY 2016, ITL provided leadership for the Cybersecurity
SECURITY OF CYBER- and Privacy subgroup of the CPS Public Working Group
PHYSICAL AND INDUSTRIAL (PWG)—which focused on identifying strategies for
cybersecurity and privacy in CPS as well as working
CONTROL SYSTEMS
collaboratively with the other subgroups to ensure the
inclusion of cybersecurity as a design principle during the
Security of Cyber Physical development processes.
Systems
After publishing a Draft Framework for CPS in
NIST’s Cyber-Physical Systems (CPS) effort will September 2015—which compiled the work of the five PWG
provide the next generation of “smart” co-designed technical subgroups—the CPS PWG published version 1.0
and co-engineered interacting networks of physical and of the Framework for Cyber-Physical Systems in May 2016.
computational components. Specifically, ITL supports the The document is the culmination of several years’ work by
effort by providing cybersecurity and privacy expertise to the CPS PWG, which includes several hundred members
address CPS-specific cybersecurity and privacy challenges. drawn primarily from industry, academia, and government.
Such challenges are related to emerging technical areas, such As a follow-on to the Framework’s release, in August 2016,
as personalized health care, emergency response, traffic-flow ITL, in collaboration with NIST’s Engineering Lab, hosted the
management, and electric power generation and delivery. Trustworthiness Launch Workshop at NIST in Gaithersburg,
Other phrases that are often referenced along with CPS MD. A key goal for the workshop was to promote interaction
technologies include: around integrated goals for trustworthy cyber-physical
systems to lay the foundation for future trustworthiness in
• Internet of Things (IoT);
science.
• Industrial Internet;
In July 2016, ITL published NIST SP 800-183, Networks
• Smart Cities; of ‘Things’, which offers an underlying and foundational
• Smart Grid; and understanding of IoT by exploring the components that
belong to most distributed systems. In FY 2017, foundational
• “Smart” Anything (e.g., Cars, Buildings, Homes,
and applied research will be conducted in the areas of CPS
Manufacturing, Hospitals, Appliances)
and IoT. ITL will also continue to participate in the International
(see http://www.nist.gov/cps/).
Society of Automation (ISA) 99 Committee, which develops
CPS aims for increased efficiency and interaction and establishes standards, recommended practices, technical
between the digital and physical worlds. Ensuring that these reports, and related information that define procedures for
emerging and evolving systems are reliable, trustworthy, implementing electronically secure industrial automation
secure, and that they protect the privacy of information poses and control systems and security practices.
a unique cybersecurity challenge. Other challenges of CPS
FOR MORE INFORMATION, SEE:
include the need for an integration with legacy components
and allowance for emerging technologies as well as real- https://www.nist.gov/cps/
time response in support of extremely high availability,
predictability, and reliability. CONTACTS:
Cybersecurity and privacy considerations are critical to Mr. Jeff Marron Ms. Suzanne Lightman
the safe and resilient design, development, and operation (301) 975-3846 (301) 975-6442
of CPS. Addressing both the opportunities and challenges jeffrey.marron@nist.gov suzanne.lightman@nist.gov
of CPS requires a broad collaboration to develop a common
foundation, including a consensus definition, vocabulary,
reference architecture, and a shared understanding of
22 the essential roles of timing, cybersecurity, and data
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Cybersecurity for Industrial performance test bed, and measuring and understanding
Control Systems the performance impacts of implemented cybersecurity
protections.
NISTs Industrial Control System (ICS) cybersecurity
effort is focused on providing guidance and insight into FOR MORE INFORMATION, SEE:
the domain of securing connected physical systems. ITL,
https://www.nist.gov/programs-projects/cybersecurity-
in collaboration with NIST’s Engineering Laboratory, is
smart-manufacturing-systems
developing and implementing guidance aimed at effectively
securing ICS—initially focusing on Smart Manufacturing http://csrc.nist.gov/cyberframework/documents/csf-
Environments. Utilizing a cybersecurity performance test manufacturing-profile-draft.pdf
bed for ICS, NIST will measure the performance of these
systems when instrumented with cybersecurity protections, http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.
in accordance with the best practices and requirements SP.800-82r2.pdf
prescribed by national and international standards and
CONTACTS:
guidelines. Examples of such standards and guidelines
include ISA/IEC-62443, Industrial Automation and Control Mr. Jeffrey Cichonski Mr. Keith Stouffer
Systems (IACS) Security, and NIST SP 800-82, Revision 2, (301) 975-3293 (301) 975-3877
Guide to Industrial Control Systems (ICS) Security. jeffrey.cichonski@nist.gov keith.stouffer@nist.gov
Industrial control systems are an essential component
in manufacturing environments; increasing reliance on
technology, communication, and the interconnectivity of ICS FEDERAL CYBERSECURITY
and IT has expanded the number of potential vulnerabilities
RESEARCH & DEVELOPMENT
and increased the potential risk to manufacturing operations.
(R&D)
While these manufacturing systems become ‘smarter’ and
increasingly connected (providing a tremendous increase
of value and efficiency), they also present a new challenge
The Networking and Information Technology Research
regarding how cybersecurity can be effectively applied to
and Development (NITRD) program provides a framework
the connected domain.
in which many federal agencies come together to coordinate
The ICS team has utilized existing standards, in
their networking and IT research and development
conjunction with the NIST Cybersecurity Framework,
(R&D) efforts. NIST remains committed to the value of
to develop a target Profile for applying cybersecurity
communicating its R&D efforts to other federal colleagues
protections within manufacturing environments. The
and identifying the opportunities to support R&D efforts
development of this profile helps establish a roadmap for
throughout the Federal Government.
reducing cybersecurity risk for manufacturers in a way that
In FY 2016, the NITRD Cybersecurity and Information
is aligned with manufacturing-sector goals and industry best
Assurance (CSIA) Interagency Working Group (IWG)
practices. The profile also tailors the existing cybersecurity
monthly meetings provided an opportunity to learn
control language to account for unique requirements in
and share information about NIST’s ongoing research.
these operational environments.
Participants also learned about connections with the
In FY 2016, leading a session during the 2016
February 2016 Federal Cybersecurity Research and
Cybersecurity Framework Workshop, the team solicited
Development Strategic Plan (see https://www.nitrd.gov/
feedback from industry partners to help advance the
cybersecurity/publications/2016_Federal_Cybersecurity_
development of the profile. The draft Cybersecurity
Research_and_Development_Strategic_Plan.pdf). With Mr.
Framework Manufacturing Profile was published as a
Bill Newhouse serving as the NIST co-chair of the CSIA IWG,
whitepaper that solicited comments from the public. The
NIST helped guide the agenda for the monthly meetings to
Profile focuses on desired cybersecurity outcomes and can
explore the defensive elements and critical elements in the
be used as a roadmap to identify opportunities for improving
R&D Strategic Plan.
the current cybersecurity posture of a manufacturing system.
In FY 2016, members of the National Privacy Research
In FY 2017, NIST will continue its research in the
Forum published a National Privacy Research Strategy,
ICS domain to include incorporating feedback and
and a new Privacy R&D Interagency Working Group
finalizing the Manufacturing Profile, implementing the 23
(IWG) was established, co-chaired by Naomi Lefkovitz,
defined cybersecurity protections onto the cybersecurity
and Simson Garfinkel (ITL), who brought their expertise
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

to the development process for the privacy R&D plan. (see In the months leading up to the November 2016 election,
https://www.nitrd.gov/Publications/PublicationDetail. NIST engaged with DHS, EAC, and the Department of
aspx?pubid=65) Justice (DOJ) to help states better identify and manage their
cybersecurity risks to election systems and voting systems
NIST is a regular participant in the coordination activities
for the upcoming election. This group ensured that election
of the federal Special Cyber Operations Research and
officials were aware of existing resources that are available to
Engineering (SCORE) Committee. SCORE enables technology
help them (including the guidelines and best practices that
transfer through the sharing of NIST cybersecurity expertise
exist for voting and other IT systems, cyber hygiene scanning
and publications with researchers throughout the Federal
services by DHS, and threat and vulnerability bulletins).
Government. The SCORE committee interacts with federal
leaders and reports to the National Science & Technology In FY 2017, the voting working group will focus its
Council’s Committee on Homeland & National Security. efforts on the next revision of the VVSG. Based on feedback
from the TGDC and election officials around the country,
FOR MORE INFORMATION, SEE:
the new revision is expected to address new technologies
http://www.nitrd.gov/ and election use cases that have become commonplace in
election systems. Additionally, the cybersecurity group plans
CONTACT: to investigate security considerations and develop guidance
in the areas of voter registration, electronic pollbooks, blank
Mr. Bill Newhouse
ballot delivery, ballot marking, auditing, and election-night
(301) 975-0232
reporting.
william.newhouse@nist.gov
FOR MORE INFORMATION, SEE:
https://vote.nist.gov
SECURITY ASPECTS OF
CONTACTS:
ELECTRONIC VOTING
Mr. Andrew Regenscheid Mr. Joshua Franklin
(301) 975-5155 (301) 975-8463
In 2002, Congress passed the Help America Vote Act andrew.regenscheid@nist.gov joshua.franklin@nist.gov
(HAVA) to encourage the upgrade of voting equipment
across the United States. HAVA established the Election
Assistance Commission (EAC) and the Technical Guidelines
SOFTWARE ASSURANCE &
Development Committee (TGDC), chaired by the Director of
RELIABILITY
NIST. HAVA directs NIST to provide technical support to the
EAC and TGDC in efforts related to human factors, security,
and laboratory accreditation. Voting security team members
Improving computer security depends on improving
from ITL conduct research and develop guidelines and best
software, that is, on reducing the number and severity of
practices for voting system security.
vulnerabilities in code. To achieve fewer vulnerabilities,
The primary objective of NIST’s work is to support the
it is essential to know what kinds of vulnerabilities and
development of the Voluntary Voting System Guidelines
weaknesses there are and to know how to find them so
(VVSG), a broad set of equipment guidelines used by the
they can be fixed. The Software Assurance Metrics and Tool
EAC to certify voting systems. The current version of these
Evaluation (SAMATE) program has two primary components:
guidelines is VVSG 1.1, which was approved by the EAC in
the Static Analysis Reference Dataset (SARD) and the Static
March 2015. Initial efforts on the next revision of the VVSG
Analysis Tool Exposition (SATE). In FY 2016, NIST produced
have already begun. Beginning in 2015, NIST established
a report on Dramatically Reducing Software Vulnerabilities
public working groups to gather input and conduct the
and a workshop report on Software Measure and Metrics to
collaborative research necessary for the development of
Reduce Security Vulnerabilities.
further guidelines/standards. These working groups consist
• The purpose of SARD is to provide users,
of three election groups and four technology groups focused
researchers, and software security assurance tool
on human factors, cybersecurity, interoperability, and
developers with a set of computer programs with
testing. The overall goal of the working groups is to lay the
known security flaws. This allows end users to
24 groundwork for a revision of the VVSG, as many jurisdictions
evaluate tools and tool developers to test their
are facing the need for a technology refresh since many
methods. The set includes “wild” (production),
voting systems are more than ten years old.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

“synthetic” (written to test or generated for COMPUTER FORENSICS
the test), and “academic” (from students) test
cases. The SARD also contains real software
applications with known bugs and vulnerabilities.
Digital evidence includes data on computers and mobile
The set is intended to encompass a wide variety
devices, including audio, video, and image files as well as
of possible vulnerabilities, languages, platforms,
software and hardware. Digital evidence can be a part of
and compilers. The SARD is a large-scale effort,
investigating most crimes, since material relevant to the
gathering test cases from many contributors. ITL
crime may be recorded in digital form. Methods for securely
has more information about the SARD, including
acquiring, storing and analyzing digital evidence quickly
goals, structure, test suite selection, etc. at https://
and efficiently are critical. ITL promotes the efficient and
samate.nist.gov/index.php/SARD.html. In FY 2016,
effective use of computer technology to investigate crimes.
the SARD was increased by approximately 40,000
The project team develops tools for testing computer
PHP (PHP is a server-side scripting language
forensic software, including test criteria and test sets. ITL
designed primarily for web development but
also maintains the National Software Reference Library
also used as a general-purpose programming
– a vast archive of published software applications that is
language) and over 30,000 C# test cases (C# is a
an important resource for both criminal investigators and
new programming language designed for building
historians.
a wide range of enterprise applications that run on
the .NET Framework).
• SATE is designed to advance research (based
on large test sets) in, and improvement of, static
analysis tools that find security-relevant defects
in source code. Participating toolmakers run their
tools on a set of programs. Researchers, led by
NIST, analyze the tool reports. The results and National Software Reference Library
experiences are reported at a workshop. The tool
The National Software Reference Library (NSRL) is
reports and analysis are made publicly available
designed to collect software from various sources and
at a later date. SATE’s purpose is NOT to evaluate
incorporate file profiles computed from this software into
nor to choose the “best” tools. Rather, it is aimed
a Reference Data Set (RDS) of information. The RDS can
at exploring the following characteristics of tools:
be used by law enforcement, government, and industry
relevance of warnings to security, their correctness,
organizations to review files on a computer by matching
and prioritization. SATE’s goals are:
file profiles in the RDS. This will help alleviate much of the
o To enable empirical research based on effort involved in determining which files are important as
large test sets, evidence on computers or file systems that have been seized
To encourage the improvement of tools, as part of criminal investigations. The NSRL also provides a
o
and research environment to promote the development of new
forensics techniques and other applications in computer
To speed the adoption of tools by
o science.
objectively demonstrating their use on real
software. In FY 2016, the NSRL published four releases of the RDS,
which continues to be the premier software resource. There
There have been five SATEs since the program
are currently 21,000 applications and 200,000,000 files.
began in 2008. The most recent exposition was
The project team completed a project with the Stanford
held in 2014. In FY 2016, planning commenced for
University Library to preserve thousands of first-generation
SATE VI.
computer packages. In FY 2017, the NSRL was expanded to
FOR MORE INFORMATION, SEE: include mobile apps.
http://samate.nist.gov
CONTACT:
Dr. Paul Black 25
(301) 975-4794
paul.black@nist.gov
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
https://dx.doi.org/10.6028/NIST.SP.800-195

|     |     |     |     | NATIONWIDE PUBLIC SAFETY  |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
BROADBAND NETWORK
(NPSBN) CYBERSECURITY

|     |     |     |     |     |     | In                                  | February  | of  2012,  | Congress  |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --------- | ---------- | --------- |
|     |     |     |     |     |     | passed the Middle Class Tax Relief  |           |            |           |
and Job Creation Act. One portion
Computer Forensics Tool Testing Project of  this  legislation  calls  for  the
|     |     |     |     |     |     | establishment  |     | of  a  | nationwide,  |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ------------ |
There is a critical need in the law enforcement community
|     |     |     |     |     |     | interoperable  |     | public-safety  |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- |
to ensure the reliability of computer forensic tools. The goal
|     |     |     |     |     |     | broadband  | network  | based  | on  the  |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | ------ | -------- |
of the Computer Forensic Tool Testing (CFTT) project at
3rd Generation Partnership Project’s
NIST is to establish a methodology for testing computer
(3GPP) Long-Term Evolution (LTE)
forensic software tools by the development of general tool
|     |     |     |     |     |     | technology.  | The  | network  | will  be  |
| --- | --- | --- | --- | --- | --- | ------------ | ---- | -------- | --------- |
specifications, test procedures, test criteria, test sets, and test
|     |     |     |     |     |     | deployed  | and  | operated  | by  the  |
| --- | --- | --- | --- | --- | --- | --------- | ---- | --------- | -------- |
Source: http://www.pscr.gov/
hardware. The project is intended to provide the information
First Responder Network Authority
necessary for toolmakers to improve tools, for users to make
(FirstNet). The planned Nationwide Public Safety Broadband
| informed  | choices  about  | acquiring  and  using  | computer  |     |     |     |     |     |     |
| --------- | --------------- | ---------------------- | --------- | --- | --- | --- | --- | --- | --- |
Network (NPSBN) will “create a much-needed nationwide
forensics tools, and for interested parties to understand the
|     |     |     |     | interoperable  | broadband  | network  | that  | will  | help  police,  |
| --- | --- | --- | --- | -------------- | ---------- | -------- | ----- | ----- | -------------- |
capabilities of the tools. A capability is required to ensure
firefighters, emergency medical service professionals and
that forensic software tools consistently produce accurate
other public safety officials stay safe and do their jobs”
and objective test results. The project team’s approach for
|     |     |     |     | (see  | http://www.ntia.doc.gov/category/public-safety).  |     |     |     |     |
| --- | --- | --- | --- | ----- | ------------------------------------------------- | --- | --- | --- | --- |
testing computer forensic tools is based on well-recognized
NIST is directed to establish a list of certified devices and
international methodologies for conformance testing and
required components to be used by public safety officials,
quality testing.
vendors, and other interested parties for interacting with
In FY 2016, the CFTT project was expanded to allow  the nationwide network. NIST is also directed to conduct
forensics testers to use the NIST testing methodology in
research and development that supports the acceleration
their own labs and to produce standardized test reports.  and advancement of the nationwide network.
Currently, the project supports disk imaging testing and
In FY 2016, CSD, ACD, and the NCCoE supported the joint
will be expanded to support hard-disk write blocking and
National Telecommunications and Information Administration
mobile forensics in 2017. The CFTT project also maintains
(NTIA) and NIST Public Safety Communications Research
| the  Forensics  | Tool  Catalog  | and  the  Computer  | Forensics  |         |          |                |                    |     |         |
| --------------- | -------------- | ------------------- | ---------- | ------- | -------- | -------------- | ------------------ | --- | ------- |
|                 |                |                     |            | (PSCR)  | program  | with  efforts  | in  public-safety  |     | mobile- |
Reference Dataset.
|     |     |     |     | application  | security,  | identity  | management,  |     | data  and  |
| --- | --- | --- | --- | ------------ | ---------- | --------- | ------------ | --- | ---------- |
FOR MORE INFORMATION, SEE:
application isolation technologies, and enabling cybersecurity
|     |     |     |     | capabilities  | on  the  | PSCR  700  | MHz  | LTE  demonstration  |     |
| --- | --- | --- | --- | ------------- | -------- | ---------- | ---- | ------------------- | --- |
http://www.nsrl.nist.gov and
network located in Boulder, Colorado (see http://www.pscr.
gov). At PSCR’s Annual Public Safety Broadband Stakeholder
http://www.cftt.nist.gov
|     |     |     |     | Conference  | in  June  | 2016,  CSD  | and  | ACD  organized  | and  |
| --- | --- | --- | --- | ----------- | --------- | ----------- | ---- | --------------- | ---- |
CONTACTS: moderated a panel called “Public Safety and Network Security
Enhancements,” led two breakout sessions on LTE Network
| Mr. Doug White  |     | Dr. Jim Lyle  |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Security, and had a booth highlighting the cybersecurity-
| (301) 975-4761  |     | (301) 975-3270  |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
related efforts of PSCR.
| doug.white@nist.gov  |     | james.lyle@nist.gov |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
26
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

SMART GRID CYBERSECURITY
|     |     |     |     |     |     |     |     |     |     |     |     | The  | major  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ |
elements of the smart
|     |     |     |     |     |     |     |     |     |     |     | grid        | are  Information  |          |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | -------- |
|     |     |     |     |     |     |     |     |     |     |     | T e         | c h n o l         | o g y ,  |
|     |     |     |     |     |     |     |     |     |     |     | industrial  |                   | control  |
systems/operational
|     |     |     |     |     |     |     |     |     |     |     | technology,  | and  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ---- |
communications
|     |     |     |     |     |     |     |     |     |     |     | infrastructure.  |     | The  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---- |

|     |     |     |     |     |     |     |     |     |     |     | infrastructure  |     | is  used  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- |
Figure 5: CSD and ACD researchers highlighting their  to  send  command
work at the June 2016 Public Safety Broadband Stake-
information across the
holder Meeting hosted by PSCR.
electric grid from the generation systems to the distribution
systems, and to exchange usage and billing information
During FY 2016, CSD and ACD published NISTIR 8080:
|     |     |     |     |     |     |     | between  | utilities  | and  their  | customers.  |     | The  key  | to  the  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----------- | ----------- | --- | --------- | -------- |
Usability and Security Considerations for Public Safety
successful deployment of the smart grid infrastructure is
| Mobile Authentication,  |     |     | and  NISTIR  | 8135:  | Identifying and  |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------------ | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
the development of a cybersecurity strategy that includes
Categorizing Data Types for Public Safety Mobile Applications
|     |     |     |     |     |     |     | cybersecurity  |     | as  a  design  | consideration  |     | for  new  | and  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | -------------- | --- | --------- | ---- |
Workshop Report. In addition, CSD and ACD released draft
emerging systems and an approach to adding cybersecurity
NISTIR 8136; Mobile Application Vetting Services for Public
into existing systems. The electric grid is critical to the
Safety - an Informal Survey, for public comment.
|      |      |      |               |     |                     |     | economic  | and  | physical  | well-being  | of  | the  nation,  | and  |
| ---- | ---- | ---- | ------------- | --- | ------------------- | --- | --------- | ---- | --------- | ----------- | --- | ------------- | ---- |
| CSD  | and  | ACD  | participated  |     | in  the  standards  |     |           |      |           |             |     |               |      |
emerging cyber threats targeting power systems highlight
development process for LTE technology within the 3rd
the need to integrate advanced security to protect critical
| Generation Partnership Project (3GPP) supporting security  |     |     |     |     |     |     | assets. |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
requirements for public safety that are related to Proximity
The Smart Grid Interoperability Panel (SGIP) became a
Services (ProSe), Group Communication System Enablers
membership-supported organization in January 2013. The
| (GCSE),  | and  Mission  |     | Critical  | Push-to-Talk  | (MCPTT).  |     | In  |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
SGIP Cybersecurity Working Group (CSWG) was renamed
addition, CSD and ACD broadened its scope within the
|     |     |     |     |     |     |     | the  Smart  | Grid  | Cybersecurity  | Committee  |     | (SGCC),  | and  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | -------------- | ---------- | --- | -------- | ---- |
Internet Engineering Task Force (IETF) to include efforts
continues to be led by a NIST representative in support of
related to public safety.
responsibilities identified in the Energy Independence and
In FY 2017, CSD and ACD will work to implement and  Security Act of 2007. The SGCC chair is a voting member of
exercise cybersecurity capabilities in the PSCR 700 MHz
the SGIP Technical Committee and serves as an ex-officio
LTE demonstration network, conduct research into mobile  Director of the Board.
authentication solutions to support the different public-
| safety  disciplines,  |             | and          | investigate    |                | mobile  application- |       |     |     |     |     |     |     |     |
| --------------------- | ----------- | ------------ | -------------- | -------------- | -------------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| security              | services    | to  support  |                | the  security  | requirements         |       |     |     |     |     |     |     |     |
| of  public-safety     |             | mobile       | applications.  |                | CSD  and  ACD        | will  |     |     |     |     |     |     |     |
| continue              | to  engage  | the          | public-safety  |                | communications       |       |     |     |     |     |     |     |     |
community by organizing workshops and conferences and
participating in events such as the Association of Public-
Safety Communications Officials (APCO) Annual Meeting,
| PSRC’s  Annual  |     | Public  | Safety  | Broadband  | Stakeholder  |     |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Conference, and the International Wireless Communications
Expo (IWCE).
CONTACTS:
| Ms. Sheila Frankel  |     |     |     | Dr. Nelson Hastings  |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
27
| (301) 975-3297            |     |     |     | (301) 975-5237           |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sheila.frankel@nist.gov   |     |     |     | nelson.hastings@nist.gov |     |     |     |     |     |     |     |     |     |
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

In FY 2016, researchers from CSD, ACD, and the Software System (GPS) is the IEEE 1588 Precision Time Protocol
and Systems Division (SSD) worked on developing security (PTP)—a time synchronization protocol that is used for the
tools for networks specifically designed to support the electric grid and other special-purpose industrial automation
next-generation electrical power systems. The researchers and measurement networks. Discussions have begun with
concentrated on authenticating the provenance of multicast the NIST Time and Frequency Division about experimental
data streams from emerging power system sensors called designs to provide a Coordinated Universal Time (UTC) scale
Phasor Measurement Units. By authenticating the sensors to that would be maintained as a NIST (UTC(NIST)) PTP service
the utility, the utility can trust that their sensor measurements over a large geographical expanse.
are coming from the correct sensors and have not been
In FY 2017, CSD will coordinate with NIST’s Engineering
hijacked.
Laboratory (EL) and Smart Grid Program Office on the
Multicast authentication of sensor data is challenging, further development of a Cybersecurity Smart Grid Test
due to the need for low-security overhead, tolerance Lab—part of the NIST Smart Grid Testbed Facility now under
of lossy networks, time-criticality, and high data rates. construction. CSD will also collaborate with the University
Researchers augmented an existing authentication scheme of New Hampshire and ITL’s Software and Systems Division
to accommodate high-data-rate sensor transmissions on cybersecurity research. The IEEE 1588 Security Working
that are unbounded in length (meaning that there is no Group is developing a new Annex to secure time distribution
session expiration). Using dual-offset key chains to reduce through (a) PTP integrated authentication and integrity
authentication delay and the computational overhead verification, (b) external transport security mechanisms, (c)
associated with key chain commitment, they developed a architecture guidance, and (d) monitoring and management
new protocol called inf-TESLA that meets the performance guidance. The research will focus on developing a full security
requirements imposed by the physical dynamics of the scheme with emphasis on PTP integrated authentication
power system. Significant effort was made to integrate their and integrity verification and monitoring/detection of the
authentication protocol into existing network simulation network’s timing performance.
software, specifically Optimized Network Engineering Tools
FOR MORE INFORMATION, SEE:
(OPNET), thus providing potential users with the ability to
evaluate the protocol on their own networks and for their http://www.nist.gov/smartgrid
own applications. http://www.sgip.org
Furthermore, in an effort to address the growing
CONTACTS:
interest in co-optimizing cyber and physical components
to work together as a system, NIST researchers developed Ms. Suzanne Lightman Ms. Victoria Yan Pillitteri
mathematical formalism to trade off the sensitivity of a (301) 975-6442 (301) 975-8542
dynamic system to attack or perturbation against the suzanne.lightman@nist.gov victoria.pillitteri@nist.gov
authentication overhead incurred by their protocol. This
formalism was demonstrated on a power system use case
showing the limiting considerations between authentication
overhead and stability margins of a wide-area damping CYBERSECURITY
controller. The project continues to be a work-in-progress AWARENESS, TRAINING,
and was presented and published at ICT Systems Security EDUCATION, AND OUTREACH
and Privacy Protection Conference 2016 in Ghent, Belgium.
Timing has also become a cyber-physical security issue
National Initiative for
with the onset of utilities detecting issues in receiving and
Cybersecurity Education (NICE)
distributing time to enable distributed real-time measurement
and control. In particular, the concern of the threat of spoofing The National Initiative for Cybersecurity Education
and jamming has led to efforts in determining redundant (NICE) is a partnership among government, academia, and
sources of traceable time. The first step is developing the private sector that is focused on cybersecurity education,
monitoring and anomaly detection capabilities. The effort training, and workforce development. The mission of NICE is
included working with the North American Synchrophasor to energize and promote a robust network and ecosystem
Initiative (NASPI) Time Synchronization Task Force to begin of cybersecurity education, training, and workforce
the effort in researching requirements and documenting development. NICE fulfills this mission by coordinating
28 guidelines for industry to provide assured timing. One with government, academic, and industry partners to build
alternative time distribution method to the Global Positioning on existing successful programs, facilitate change and
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

innovation, and bring leadership and vision to increase the  leadership in working with government partners on initiatives
number of skilled cybersecurity professionals helping to  such as the Cybersecurity National Action Plan, the Federal
keep our nation secure. Cybersecurity Workforce Strategy, and implementation of
the Federal Cybersecurity Workforce Assessment Act.
NICE is building on its current efforts based on its
Strategic  Plan—delivered  to  Congress  in  April  2016  as  In  FY  2016,  NICE  announced  grant  awards  for  five
required by the Cybersecurity Enhancement Act of 2014— Regional Alliances and Multi-stakeholder Partnerships to
which  was  written  with  engagement  and  deliberation  Stimulate (RAMPS) cybersecurity education and workforce
among NICE partners. The three primary goals of the plan  development. The RAMPS grants will bring together K-12,
are to: 1) accelerate learning and skills development, 2)  higher education, and local employers in regions across the
nurture a diverse learning community, and 3) guide career  nation  (see  https://www.nist.gov/nice/regional-alliances-
development and workforce planning. NICE partners will  and-multistakeholder-partnerships-stimulate-ramps).  NICE
continue to develop appropriate implementation strategies  also provided grant support for the 2015 NICE Conference
and metrics for this plan. and Expo, the 2015 National K-12 Cybersecurity Education
In FY 2016, the NICE team at NIST worked to set a solid  Conference,  the  Center  of  Academic  Excellence  (CAE)
Community Meeting, the National Cybersecurity Summit,
staffing foundation for future progress. They assembled
the NICE Challenge Project, and the Cybersecurity Jobs
| new  internal  | team  | members  | that  | includes  | leads  for  |     |     |     |     |     |     |
| -------------- | ----- | -------- | ----- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
Heat Map.
academic engagement, industry engagement, government
engagement, and a program manager. These, in combination  In FY 2017, NICE plans to:
with the existing NICE Director and NICE Deputy Director,
•   Support the 2016 NICE Conference on October 6-7,
completed the staffing needs for the NICE Program Office
2016;
at NIST.
•   Support the 2016 NICE Conference and Expo and
| Many  | NICE  communication  |     | mechanisms  |     | were  also  |     |     |     |     |     |     |
| ----- | -------------------- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
pre-conference seminars on October 31, 2016 –
| established  | in  FY  2016.  | These  | include  | the  | NICE  Public  |     |     |     |     |     |     |
| ------------ | -------------- | ------ | -------- | ---- | ------------- | --- | --- | --- | --- | --- | --- |
November 2, 2016;
| Working  | Group  (see  | https://www.nist.gov/itl/applied- |     |     |     |     |     |     |     |     |     |
| -------- | ------------ | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•   Launch a Cybersecurity Jobs Heat Map known as
| cybersecurity/nice/about/working-group),  |     |     |     |     | the  NICE  |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
“CyberSeek”;
| Quarterly  | eNewsletter  | (see  | https://www.nist.gov/news- |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ----- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
events/news/search/enewsletter),  and  an  increased  •   Publish a draft of the NICE Cybersecurity
presence of NICE at cybersecurity education, training, and  Workforce Framework; and
workforce development events across the country.
•   Provide a public webinar series (see
https://www.nist.gov/nice/webinars).
FOR MORE INFORMATION, SEE:
http://www.nist.gov/nice
CONTACTS:
|     |     |     |     |     |     | Mr. Rodney Petersen  |     |     | Ms. Danielle Santos      |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------------ | --- | --- |
|     |     |     |     |     |     | (301) 975-8897       |     |     | (301) 975-5048           |     |     |
|     |     |     |     |     |     | nice.nist@nist.gov   |     |     | danielle.santos@nist.gov |     |     |
Computer Security Resource
Center (CSRC)
|     |     |     |     |     |     | The  | CSRC  website  | is  a  | vast  repository  | of  | valuable  |
| --- | --- | --- | --- | --- | --- | ---- | -------------- | ------ | ----------------- | --- | --------- |

|     |     |     |     |     |     | information  | relating  | to  cybersecurity  |     | research  | by  NIST  |
| --- | --- | --- | --- | --- | --- | ------------ | --------- | ------------------ | --- | --------- | --------- |
Figure 6: The NICE Lead for Academic Engagement, Mrs.
personnel in ITL and is one of the busiest and most expansive
Davina Pruitt-Mentle, speaking with an attendee at the
websites at NIST. CSRC encourages the broad sharing of
20th Annual Colloquium for Information Systems Securi-
information security tools and practices, provides a resource
ty Education Conference in Philadelphia.
|     |     |     |     |     |     | for  information  | security  | standards  | and  | guidelines,  | and  |
| --- | --- | --- | --- | --- | --- | ----------------- | --------- | ---------- | ---- | ------------ | ---- |
In  addition  to  NICE’s  continued  coordination  with  identifies and links key security web resources to support  29
|     |     |     |     |     |     | industry  | and  government  | users.  | Several  | divisions  | within  |
| --- | --- | --- | --- | --- | --- | --------- | ---------------- | ------- | -------- | ---------- | ------- |
academic and industry partners, NICE also continued its
|     |     |     |     |     |     | ITL  rely  | on  the  CSRC  | website  | to  post  | program/project  |     |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | -------- | --------- | ---------------- | --- |
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

information, research and testing, software tools, and other Federal Computer Security
information that is essential to NIST’s customers worldwide. Managers’ (FCSM) Forum
The CSRC website is home to many of the standards,
guidelines, and other technical series documents that are
The Federal Computer Security Managers’ (FCSM) Forum
valuable to the general public. The Publications Released
is sponsored by NIST to promote the sharing of security-
in FY 2016 section of this annual report provides additional
related information among federal agencies. The Forum,
details. During FY 2016, CSRC had more than 6.2 million page
which serves more than 1,200 members, strives to provide
views and downloads.
an ongoing opportunity for managers of federal information
The CSRC team maintains a publication announcement security programs to exchange information security
mailing list with more than 73,630 subscribers from materials in a timely manner, build upon the experiences of
government, industry, and academia—as well as individuals other programs, and reduce possible duplication of effort.
with a personal interest in IT security worldwide. This free It provides a mechanism for NIST to share information
email list notifies subscribers about publications that have directly with federal agency information security managers
been posted to the CSRC website, along with announcing in fulfillment of NIST’s leadership mandate (under FISMA). It
new NIST-sponsored cybersecurity events and important also assists NIST in establishing and maintaining relationships
news and/or announcements. with other individuals or organizations that are actively
During FY 2016, the CSRC was updated daily, providing addressing information security issues within the Federal
new information such as draft and final versions of technical Government. During FY 2016, NIST’s Patricia Toth served as
series documents (e.g., FIPS, SPs, NISTIRs and ITL Bulletins) the Chairperson, and ACD served as the Secretariat of the
and updates to various program and project webpages. Forum, with administrative and logistical support from NIST’s
The CSRC team has made progress on plans for a complete Peggy Himes.
redesign of the current CSRC website, including a content The Forum maintains an extensive email subscription
management system (CMS). Updating CSRC with a CMS will service. Participation in the service is restricted to those
provide a user-friendly environment and experience. The Federal Government employees with a role in the management
first phase of the project, the publications section; has been of their organization’s information system security program.
completed. All technical and non-technical publications (e.g., The Forum conducts bi-monthly meetings and an annual
white papers, conference papers, presentations) have been two-day conference for a discussion of current issues and
successfully integrated into the new system. topics of interest to those responsible for protecting sensitive
The CSRC team has spent the last portion of FY 2016 (unclassified) federal systems. Events are open to federal
migrating the content from the current website into the CMS, employees and their designated support contractors.
and in FY 2017, a beta test site of the entire CSRC is expected Topics of discussion at FCSM meetings in FY 2016 included
to be made available. The CSRC team plans to continue briefings on: software-aided security control selection, best
testing the new website and to review feedback received, practices for privileged user personal identity verification,
with the plan for full transition to the updated site in FY 2017. the Cybersecurity Framework, the National Cybersecurity
FOR MORE INFORMATION, SEE: Center of Excellence (NCCoE) - Federally Funded Research
and Development Center (FFRDC), an update on vetting
http://csrc.nist.gov the security mobile applications, and the U.S. Government
Configuration Baselines (USGCB).
CONTACTS:
FY 2016’s annual two-day offsite was held at NIST
Questions regarding the CSRC website can be sent to the on August 16-17, 2016. Presentations included the current
CSRC Webmasters at: technical, operational and management information systems
security topics and updates on the information system
webmaster-csrc@nist.gov security activities of OMB, GAO, National Aeronautics and
Space Administration (NASA), NARA, Federal Aviation
Mr. Patrick O’Reilly Ms. Nicole Keller
Administration (FAA), Census Bureau, DHS, and NIST. Most
(301) 975-4751 (301) 975-3648
presentations are available online (see http://csrc.nist.gov/
patrick.oreilly@nist.gov nicole.keller@nist.gov
groups/SMA/forum/events.html).
The following is a list of presentations that were
30 given at the annual two-day offsite meeting (see
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

http://csrc.nist.gov/groups/SMA/forum/events.html for links Ms. Jody Jacobs
to the presentations): (301) 975-4728
jlj3@nist.gov
• Federal CIO Council update;
• Establishing a Tier 2 Information Security risk (Editors’ Note: Pat Toth worked on this initiative until she
management program: How a department-wide took another position at NIST.)
security gap analysis provided a basis for a new
security program;
Federal Information Systems
• Government Accountability Office (GAO)
Security Educators’ Association
Information Security update;
(FISSEA)
• S P 800-150, Guide to Cyber Threat Information
The Federal Information Systems Security Educators’
Sharing;
Association (FISSEA), founded in 1987, is a NIST organization
• NIST SP 800-171, Protecting Controlled Unclassified to assist federal agency professionals with meeting
Information in Nonfederal Information Systems and information system security awareness, training, and
Organizations; education responsibilities. FISSEA strives to elevate the
• Continuous Diagnostics and Mitigation (CDM); general level of information system security knowledge for
the Federal Government and the federal workforce. It also
• The new A-130 Policy;
seeks to assist the professional development of its members.
• Migrating the Federal Government to Hyper Text
FISSEA membership is open to information system
Transfer Protocol Secure (HTTPS);
security professionals, professional trainers and educators,
• Security beyond a “system” – fiscal service’s managers responsible for information system security
approach to external services; training programs in federal agencies, contractors of these
• Case study: boundary consolidation to support agencies, and faculty members of accredited educational
more efficient, effective use of resources and institutions who are involved in information security training
increased maturity in continuous monitoring; and education. All that is required to become a FISSEA
member is a willingness to share products, information, and
• Lessons learned from the Federal Risk
experiences. A working group meets monthly to administer
and Authorization Management Program
business activities.
(FedRAMP);
FISSEA communicates with its membership through a
• CDM update, interagency communications, and
website, a mailing list, and a social networking site. The ACD
agency involvement; and
staff assists FISSEA with its operations by providing staffing
• The Cybersecurity Strategy and Implementation support for several of its activities (and by acting as FISSEA’s
Plan (CSIP) and FY 2016 CIO FISMA metrics. host agency).
The Forum plays a valuable role in helping NIST (and The 29th Annual FISSEA Conference occurred March
other federal agencies) develop and maintain a strong, 15-16, 2016 at NIST, and the theme was “The Quest for the
proactive stance in the identification and resolution of new Unhackable Human: The Power of Cybersecurity Awareness
strategic and tactical IT security issues as they emerge. and Training.” The 250+ attendees were made up of
The email list of interested parties has steadily increased in managers (specifically those responsible for information
size and provides a valuable resource for federal security systems security awareness, training, certifications,
program managers. workforce identification, compliance, etc. in federal
agencies), contractors providing awareness and training
FOR MORE INFORMATION, SEE:
support, and faculty members of accredited educational
http://csrc.nist.gov/groups/SMA/forum/ institutions who are involved in information security training
and education. The attendees learned about new techniques
CONTACTS:
for developing/conducting training, cost-effective practices,
workforce development, and free resources and contacts.
Ms. Victoria Yan Pillitteri Ms. Peggy Himes
(301)975-8542 (301) 975-2489 NIST’s Pat Toth, Peggy Himes, and members of the
victoria.pillitteri@nist.gov peggy.himes@nist.gov FISSEA Technical Working Group were integral to the effort
to support the 2016 Annual Conference. NIST ITL Director, 31
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Charles Romine, opened the event as the welcoming speaker, described below, including a new section this year related to
and ten-year-old Reuben Abishai Paul, Founder and CEO of video-based training.
CyberShaolin & Prudent Games, gave the keynote address “R
In FY 2016, awarded certificates were selected by an
U #Unhackable?” Presenters at the event represented NIST,
impartial judging committee and included:
DHS, Department of State (DoS), National Security Agency
• Poster Winner: K. Rudolph, John Ippolito, G. Mark
(NSA), National Institute of Health (NIH), National Oceanic
Hardy, Andrew Ellis, and Charles A. Filius, from
and Atmospheric Administration (NOAA), Federal Housing
Native Intelligence, Inc. and friends;
Finance Agency (FHFA), private industry, and academia.
The attendees had an opportunity to visit vendors and • Website Winner: Lisa Dorr, Sarah Moffat,
federal agencies on the second day to discuss their specific Toney Rogers, and Jennifer Kimberly from U.S.
awareness and training programs, and the Pecha Kucha fast- Department of Health and Human Services (HHS),
paced talks proved to be both entertaining and educational. Office of Information Security (OIS), Governance,
Risk Management, and Compliance (GRC) –
The FISSEA Educator of the Year Award is an annual
Governance Division;
recognition to honor a contemporary individual who is
making special efforts to create, build, manage, or inspire • Motivational Item Winner: K. Rudolph from Native
an information systems security awareness, training, or Intelligence, Inc.;
education program. Susan Hansche (DHS) presented the
• Newsletter Winner: Indian Health Service (IHS),
FISSEA 2016 Educator of the Year Award to Gretchen Morris
Office of Information Technology, Division of
(DB Consulting Group/NASA). Gretchen’s vast knowledge-
Information Security;
base, strong work ethic, her dedication to the improvement
of information security awareness and training, and her • Security Training: The Employment and Social
Development Canada (ESDC) Security Training and
commitment to coordinating the annual FISSEA Security
Awareness Program Team; and
Contest made her the perfect recipient for the award.
• Video: Cheryl Seaman and Stephanie Erickson from
NIH.
Peer’s Choice Award winners were selected by peers
during the conference and included:
• Poster Winner: Katherine Martini from DoS – Office
of Cybersecurity;
• Website Winner: Lisa Dorr, Sarah Moffat, Toney
Rogers, and Jennifer Kimberly from HHS, Office
of Information Security (OIS), Governance, Risk
Management, and Compliance (GRC) – Governance
Division;
• Motivational Item Winner: K. Rudolph from Native
Intelligence, Inc.;
• Newsletter Winner: IHS Office of Information
Technology, Division of Information Security;
• Security Training: IHS Office of Information
Figure 7: Susan Hansche, DHS, presented the FISSEA 2015 Technology, Division of Information Security;
Educator of the Year Award to Gretchen Morris, DB Con- and
sulting/NASA on March 15, 2016. • Video: The ESDC Security Training and Awareness
Program Team.
Other traditional FISSEA conference events include
announcing the winners of the FISSEA Security Awareness, Another benefit of attending the 2016 FISSEA conference
Training & Education Contest, which includes six categories was the networking opportunities. The conference continues
from one of FISSEA’s three key areas: awareness, training, to be a valuable forum for attendees to learn about ongoing
and education. A winner is selected from each category and planned training and education programs and initiatives.
32 and awarded a certificate. The categories covered the topics It also provides NIST the opportunity to help departments
and agencies with fulfilling FISMA responsibilities. The 30th
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Annual FISSEA Conference will be held at NIST on March 14- the Director of the NSA, and the appropriate
15, 2017. committees of Congress.
FOR MORE INFORMATION, SEE: Congress indicated the long-term need for the Board
by setting the terms of Board members to four years. The
https://csrc.nist.gov/Projects/Federal-Info-Systems-
Board’s charter requires that the NIST Director appoint the
Security-Educators-Assoc
Chairperson and all twelve members of the Board, each of
whom is selected for her/his preeminence in the IT industry
CONTACTS:
or related disciplines.
Mr. Clarence Williams Ms. Peggy Himes
Mr. Chris Boyer took over leadership from Dr. Peter
(240) 672-8723 (301) 975-2489
Weinberger and was officially appointed by the NIST Director
clarence.williams@nist.gov peggy.himes@nist.gov
as the ISPAB Chair on May 1, 2016. Chris Boyer (Assistant Vice
President, Global Public Policy at AT&T Services Inc.) has
(Editors’ Note: Pat Toth worked on this initiative until she
been a member of the Board since June 2012. In addition to
took another position at NIST.)
his official role representing AT&T, he serves as AT&T’s point
of contact to the National Security Telecommunications
Information Security and Privacy Advisory Council (NSTAC), a federal advisory committee
Advisory Board (ISPAB) tasked with providing advice to the president on matters of
national security and emergency preparedness (NS/EP).
The Information Security and Privacy Advisory Board
(ISPAB) was initiated in 1987 and has successfully renewed The ISPAB Board currently has ten members
its charter with proper authority every two years. The supporting the Chair (see http://csrc.nist.gov/groups/
legislative history for Public Law 100-235 and Public Law SMA/ispab/membership.html). This year, the Board was
107-347 underscores that Congress intended that the Board pleased to welcome Ms. Patricia Hatter as a new member
should be a continuing body. The Board plays a central and (see https://www.nist.gov/news-events/news/2016/08/
unique role in providing the government with expert advice nists-information-security-and-privacy-advisory-board-
concerning information security and privacy issues that may adds-industry-member). The following are current Board
affect federal information systems. No other similar group of members:
experts meets regularly to review information security issues • Ana (Annie) Antón, Professor and Chair, School
involved in unclassified Federal Government computer of Interactive Computing, Georgia Institute of
systems and networks. Title III of the E-Government Act Technology;
of 2002 reaffirmed the need for this Board by giving it
• John R. Centafont, National Security Agency,
additional responsibilities: to thoroughly review all proposed
Information Assurance and Cyber Defense;
information technology standards and guidelines developed
under Section 20 of the National Institute of Standards and • David Cullinane, CEO, TruStar, LLC;
Technology Act (15 U.S.C. 278g-3), as amended.
• Gregory Garcia, Executive Vice President, McBee
The ISPAB is a federal advisory committee with specific Strategic Consulting;
statutory objectives to identify emerging managerial,
• Jeffrey Greene, Esq., Director, Government
technical, administrative, and physical safeguard issues
Affairs, North America & Senior Policy Counsel,
related to information security and privacy.
Senior Policy Counsel, Cybersecurity and Identity,
The duties of the Board, as dictated in the Act, are: Symantec Corporation;
• To identify emerging managerial, technical, • Patricia Hatter, General Manager, Professional
administrative, and physical safeguard issues Services, Intel;
relative to information security and privacy;
• Toby Levin, Retired (formerly Senior Advisor and
• To advise NIST and the Director of OMB on Director of Privacy Policy, U.S. Department of
information security and privacy issues pertaining Homeland Security);
to Federal Government information systems,
• Edward Roback, Associate Chief Information
including a thorough review of proposed standards
Officer for Cybersecurity, U.S. Department of
and guidelines developed under section 278g–3 of
Treasury;
this title; and
• Gale Stone, Deputy Assistant Inspector General for 33
• To provide an annual report of its findings to the
Audit, Social Security Administration; and
Secretary of Commerce, the Director of OMB,
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

• J. Daniel Toler, Deputy Director, Federal Network • Updates from the senior staff of federal agencies
Resilience, U.S. Department of Homeland (e.g., the Deputy Under Secretary, Cybersecurity
Security. and Communications, National Protection
Directorate, DHS, and Senate and Congressional
During FY 2016, ISPAB held three meetings that were
staff);
located at the U.S. Access Board Conference Room in
Washington, D.C: • PCLOB and the establishment of the Federal
Privacy Council;
• October 21-23, 2015;
• OMB Circular A-130 revisions;
• March 23-25, 2016; and
• National Highway Traffic Safety Administration,
• June 15-17, 2016.
autonomous vehicle technology, gaps, challenges,
The presenters at each Board meeting were leaders
security and privacy;
and experts representing private industry, academia, federal
• P rivacy, transparency, and accountability for
agency CIOs, Inspectors General, and Chief Information
commercial unmanned aircraft systems;
Security Officers.
• Cryptography and NIST cryptographic standards
In keeping with previous practices, at the first meeting of
processes;
the fiscal year, the Board established a work plan for FY 2016.
The resulting plan included the following areas of focus: • Emerging technologies: cloud computing, big data,
Internet of Things, cyber physical systems, smart
• Quantum (physics, pre-shared keys, quantum key
cities, drones and unmanned aircraft systems,
distribution, block chains);
medical devices, transportation sector and vehicle-
• Cybersecurity;
to-vehicle communication, blockchain protocol, and
• OMB topics, including Circular A-130 revisions, impacts on security and privacy;
cyber-marathon, CyberStats, measuring outcomes
• Commission on Enhancing National
for cybersecurity, and cybersecurity protections in
Cybersecurity;
Federal Government acquisitions;
• The NIST Cybersecurity Framework;
• DHS topics, including Fly-Away (Incident Response)
• Cybersecurity Information Sharing Act (CISA);
Team, Einstein, Continuous Diagnostics and
Mitigation (CDM), and outcome measurement • Information sharing and analysis;
methods;
• The DHS CDM program;
• Networking and Information Technology Research
• The Trusted Identities Group (TIG);
and Development (NITRD) and the Build-it-
• National Cybersecurity Center of Excellence
in initiative and NITRD – on how competent
(NCCoE); and
companies acquire IT;
• Realignment of IT Laboratory.
• National Highway Traffic Safety Administration
(NHTSA) and automotive cybersecurity; The Board submitted two recommendation letters based
on the Board work from each meeting in this fiscal year.
• Federal Trade Commission (FTC) – security,
Records of the submitted letters and the received responses
protecting data;
are accessible from http://csrc.nist.gov/groups/SMA/ispab/
• Facial recognition, technologies, biometrics, and
documentation.html.
users;
• At the close of the October 2015 meeting, the
• Privacy technologies;
Board submitted a recommendation letter
• Privacy and Civil Liberties Oversight Board regarding quantum computing to the NIST Director.
(PCLOB); The NIST Director responded to the Board in a letter
dated January 2016.
• Safe Harbor; and
• At the close of the March 2016 meeting, the Board
• Acquisition.
submitted a recommendation letter regarding
Aligning with work-plan focus areas, the Board
FIPS 140 and the use of ISO/IEC 19790 to the NIST
continues to monitor the following critical areas:
Director. The Board received a response from the
34
NIST Director in August 2016.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Copies of the current list of members and their response to this need, NIST, the SBA, and the FBI InfraGard
biographies, the Board’s charter, and past Board activities are program co-sponsor a series of cybersecurity training
located at https://csrc.nist.gov/Projects/ISPAB. Information workshops for small businesses. These workshops provide
on ISPAB meetings is published in Federal Register Notices an overview of cybersecurity threats, vulnerabilities, and
at least 16 days prior to the meeting. Those interested in corresponding protective tools and techniques, with a special
receiving meeting notices and other notices relating to emphasis on information that small business personnel can
NIST information security and privacy work may email their apply directly.
name, affiliation, and address to Matthew Scholl at the email
In FY 2016, SMB outreach workshops took place in:
address below.
• Minneapolis, Minnesota;
FOR MORE INFORMATION, SEE:
• McHenry, Maryland;
http://csrc.nist.gov/groups/SMA/ispab/
• Harrisonburg, Virginia;
CONTACT: • Arlington, Virginia;
• Ocala, Florida;
Mr. Matthew Scholl
(301) 975-2941 • The Villages, Florida;
matthew.scholl@nist.gov
• Orlando, Florida;
(Editors’ Note: Annie Sokol worked on this initiative until • Clermont, Florida;
she was assigned to other projects.)
• Charlestown, West Virginia; and
• Detroit, Michigan.
Small and Medium Size Business
Additionally, as part of the President’s Cybersecurity
(SMB) Cybersecurity Outreach
National Action Plan (CNAP), NIST partnered with the SBA,
Workshop
the FTC, and the Department of Energy (DoE) to develop
Small business owners face a broad range of information and provide five cybersecurity training webinars to reach
security issues. A computer failure or system breach could small businesses and small business stakeholders through
jeopardize the company’s reputation and may result in 68 SBA District Offices, nine NIST Manufacturing Extension
significant damage and recovery cost—or even business Partnership Centers, and other regional networks across the
closure. The small business owner who recognizes the threat country.
of computer crime and takes steps to deter inappropriate In collaboration with the SBA and the FBI, planning
activities is less likely to become a victim. is underway to identify locations and plan cybersecurity
The U.S. Small Business Administration (SBA) reports workshops in FY 2017.
that over 27 million U.S. companies − more than 99 % of
FOR MORE INFORMATION, SEE:
all U.S. businesses − are SMBs of 500 employees or fewer
(see http://www.sba.gov/sites/default/files/allprofiles12. https://csrc.nist.gov/Projects/Small-Business-Community
pdf). While the threats to individual small and medium-size
CONTACT:
businesses may not be significantly different from those
facing larger organizations, a SMB frequently has fewer
Mr. Jeffrey Marron
resources available to protect systems, detect attacks, or
(301) 975-3846
respond to security issues. A vulnerability common to a
Jeffrey.Marron@nist.gov
large percentage of SMBs could pose a threat to the nation’s
information infrastructure and economic base. (Editors’ Note: Pat Toth worked on this initiative until she
took another position at NIST.)
To help address information security risks, these
businesses require assistance with the identification of
security mechanisms and with practical, cost-effective
training. Training helps SMB’s use their limited resources
most effectively to address relevant and serious threats. In
35
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

CRYPTOGRAPHIC STANDARDS CONTACT:
PROGRAM
Dr. Lily Chen
(301) 975-6974
Secure Hash Algorithm-3 (SHA-3) lily.chen@nist.gov
Derived Functions (NIST SP 800-185)
(Editors’ Note: Shu-jen Chang supported this program until
NIST opened a public competition in November her recent retirement)
2007 to select a new cryptographic hash algorithm for
standardization. The “SHA-3” competition ended in October
Random Number Generation
2012. NIST standardized the winning algorithm, Keccak, in
(RNG)
FIPS 202 as the new SHA-3 Standard. Announced on August
5, 2015, FIPS 202, SHA-3 Standard: Permutation-Based Random numbers are required for the secure use of most
Hash and Extendable-Output Functions, is available at: cryptographic algorithms. For example, random numbers are
https://csrc.nist.gov/Publications/Search?requestSeriesList= used to generate the keys needed for encryption and digital
3&requestStatusList=1,3&requestDisplayOption. signature applications. The CSD Cryptographic Technology
=brief&requestSortOrder=5&itemsPerPage=All. Group (CTG) began work on the specification of random bit
generators in the late 1990s. SP 800-90, Recommendation
FIPS 202 defines four fixed-length hash functions (SHA3-
for Random Number Generation Using Deterministic Random
224, SHA3-256, SHA3-384, and SHA3-512), and two variable-
length eXtendable Output Functions (XOFs), SHAKE128 and Bit Generators, was published in 2007, and revised as SP
SHAKE256. FIPS 202 also supports a flexible scheme for 800-90A in 2012 and 2015. This document specifies several
domain separation between different functions derived from deterministic algorithms that can be used for the generation
Keccak, which ensures that different named functions will of pseudorandom bits – a sequence of bits produced by an
produce unrelated outputs. algorithm, rather than a random physical phenomenon that
produces a truly random sequence.
NIST extended this scheme to allow users to customize
their use of the function by defining a new, customizable Two additional documents (SP 800-90B and SP 800-
version of the SHAKE functions, called cSHAKE, and specifying 90C) are under development, and drafts were made available
two cSHAKE variants—cSHAKE128 and cSHAKE256—for a for public comment in 2012 and 2016.
128- and 256-bit security strength, respectively, in DRAFT
SP 800-90B, Recommendation for the Entropy Sources
SP 800-185, SHA-3 Derived Functions: cSHAKE, KMAC,
Used for Random Bit Generation:
TupleHash and ParallelHash.
SP 800-90B addresses the development and testing of
Draft SP 800-185 defines three additional SHA-3-derived
entropy sources. Figure 8: Entropy Source Model illustrates
functions that provide new functionality. They are:
the model that the Recommendation uses to describe an
• KMAC128 and KMAC256, providing pseudorandom entropy source and its components: a noise source, health
functions (PRFs) and keyed-hash functions with tests, and an optional
variable-length outputs;
• TupleHash128 and TupleHash256, providing
functions that hash tuples of input strings without
trivial collisions; and
• ParallelHash128 and ParallelHash256, providing
efficient hash functions to hash long messages in
parallel.
Published on August 4, 2016, Draft SP 800-185 is
available on the CSRC website. NIST invited the public to
review the draft and provide comments before September
30, 2016. NIST is in the process of addressing the received
comments, and will post the final version of SP 800-185 when
the comments are resolved.
FOR MORE INFORMATION, SEE:
36
http://csrc.nist.gov/groups/ST/hash/sha-3/sha-3_
standardization.html. Figure 8: Entropy Source Model
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

In Figure 8: Entropy Source Model, the noise source Figure 9: XOR-NRBG depicts the construction of one
contains the entropy-providing activity (e.g., ring oscillators); of the NRBGs – the XOR-NRBG. In this construction, each
if the activity being sampled does not produce binary data, bit output by the entropy source (as discussed in SP 800-
then the noise source includes a digitization process. Health 90B) is exclusive-ORed with a bit of output from a DRBG
tests are intended to detect whether the noise source algorithm specified in SP 800-90A.
and the entropy source (as a whole) continues to operate
as expected. The optional conditioning component is
responsible for reducing bias and/or increasing the entropy
rate of the bits to eventually be output by the entropy source.
SP 800-90B includes descriptions of the tests for NIST’s
Cryptographic Algorithm Validation Program (CAVP) to
Figure 10: DRBG and Oversampling NRBG
validate candidate entropy sources. During FY 2016, the
CTG continued the development and testing of methods for
Figure 10: DRBG and Oversampling NRBG depicts the
estimating the amount of entropy per noise-source output.
construction used for the DRBGs and the second NRBG
A draft of the document was provided for public design – the Oversampling NRBG. The difference between
comment in January 2016. A companion python code the two is the availability of the entropy source and the
package was also made available to assist reviewers in frequency of requesting output from the entropy source. For
evaluating the entropy estimation methods published in a DRBG, an entropy source is only required for seeding the
the draft (see https://github.com/usnistgov/SP800-90B_ DRBG; after the initial seeding process, further requests for
EntropyAssessment). entropy-source output depend on the implementation and
application. For the Oversampling NRBG, the entropy source
A workshop was held in May 2016 to discuss the
must always be available and is accessed whenever bits are
document, and the public comment period ended shortly
requested from the NRBG by a consuming application.
thereafter. The SP 800-90B development team has been
reviewing the comments received during the public The latest draft of SP 800-90C is available via the
comment period and plans to finalize an initial version of the Special Publications page: http://csrc.nist.gov/publications/
document in FY 2017. PubsSPs.html.
The latest draft of SP 800-90B is available via the
PLANS FOR FY 2017:
Special Publications page: http://csrc.nist.gov/publications/
PubsSPs.html. The RBG development team has the following goals for
FY 2017:
SP 800-90C, Recommendation for Random Bit
Generator (RBG) Constructions: • Complete the initial version of SP 800-90B and
post the comments received, along with their
SP 800-90C provides basic guidance on the construction
resolution. The testing of entropy sources by the
of Random Bit Generators (RBGs) from the entropy sources
CMVP will begin as soon as possible after the test
validated against the requirements of SP 800-90B and the
code is ported to another language for increased
Deterministic Random Bit Generators (DRBG) algorithms of
performance. Members of the CMVP staff have
SP 800-90A. SP 800-90C includes constructions for both
been participating in the development of SP 800-
non-deterministic random bit generators (NRBGs; also
90B to more easily prepare for such testing. Not
known as true random number generators) and deterministic
all comments received will be addressed in this
random bit generators (also known as pseudorandom
version, since the development team is anxious to
number generators). Two general models are provided in SP
begin getting feedback from the CMVP labs about
800-90C, as shown in Figures 8 and 9.
the adequacy of the tests specified in SP 800-90B.
Addressing some of the comments would result in
a significant delay in finalizing the initial version of
the document.
• Complete SP 800-90C, posting the comments
received and their resolution, along with the
document.
37
• Monitor the testing of SP 800-90B and SP 800-
90C in the CMVP labs to determine problems
Figure 9: XOR-NRBG
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

that need to be addressed in the next versions be longer than the original plaintext and may result in format
of the documents. In some cases, the problems problems when used by existing devices or software.
may be addressed by additions to the FIPS 140-
FPE modes such as FF1 and FF3 are designed for any
2 Implementation Guidance document until the
kind of data, including non-binary formats, such as credit
documents are revised. The Implementation
card numbers and social security numbers. The ciphertext
Guidance document is available at http://csrc.nist.
resulting from an FPE mode has the same length and format
gov/groups/STM/cmvp/documents/fips140-2/
as the original plaintext. Consequently, FPE modes can
FIPS1402IG.pdf.
facilitate the retrofitting of encryption technology to existing
• Consider the comments received during the public devices or software, where a conventional encryption mode
comment period for SP 800-90B that were not might not be feasible.
resolved before its publication. Also, address any
FOR MORE INFORMATION, SEE:
problems that surface during CMVP testing.
http://csrc.nist.gov/groups/ST/toolkit/BCM/
FOR MORE INFORMATION, SEE:
CONTACT:
http://csrc.nist.gov/groups/ST/toolkit/rng/
Dr. Morris Dworkin
CONTACTS:
(301) 975-2354
Ms. Elaine Barker Mr. John Kelsey morris.dworkin@nist.gov
(301) 975-2911 (301) 975-5101
elaine.barker@nist.gov john.kelsey@nist.gov
Key Management
Dr. Meltem Sönmez Turan Dr. Kerry McKay Key management is required for applying numerous
(301) 975-4391 (301) 975-4969 cryptographic technologies and is considered one of
meltem.turan@nist.gov kerry.mckay@nist.gov the most critical aspects associated with the use of
cryptography. The Cryptographic Technology Group (CTG)
began providing guidance in managing the keys used for
Block Cipher Modes of Operation
cryptographic applications in the late 1990s to early 2000s.
The engine for many of the techniques in NIST’s
NIST Special Publications have been periodically updated
cryptographic toolkit is a block cipher algorithm, such as the
to address new algorithms and handling procedures. These
Advanced Encryption Standard (AES) algorithm or the Triple
documents are coordinated with federal agencies and
Data Encryption Algorithm (TDEA). A block cipher transforms
with the cryptographic community, including national and
some fixed-length binary data (i.e., a “block”) into seemingly
international organizations, industry, and academia.
random data of the same length. The transformation is
During the development and subsequent revision of
determined by the choice of some secret data called the
these key-management documents, the development
“key.” The same key is used to reverse the transformation and
team coordinates with members of NIST’s Cryptographic
recover the original block of data. A cryptographic technique
Algorithm Validation Program (CAVP) and Cryptographic
(e.g., for encryption and/or authentication) that is constructed
Module Validation Program (CMVP) to develop validation
from a block cipher is called a ‘mode of operation.’
tests and address issues that arise during the validation
Several modes of operation have been specified in the
processes.
SP 800-38 series of publications. The latest installment in
In FY 2016, the following publications were either created
the series, Special Publication 800-38G, Recommendation
or revised:
for Block Cipher Modes of Operation: Methods for Format-
Preserving Encryption, was published in March 2016. It SP 800-57, Part 1, Recommendation for Key Management,
specifies two AES modes of operation, called FF1 and FF3, Part 1: General:
for inclusion in the “toolkit” of approved cryptographic
SP 800-57, was first published in 2005, and later revised
algorithms. FF1 and FF3 are format-preserving encryption
in 2007 and 2012. SP 800-57, Part 1 contains basic key-
(FPE) modes, based on proposals that were submitted from
management guidance, including:
the private sector.
• Defining the security services that may be obtained
Previously approved confidentiality modes are designed
using NIST-approved algorithms;
38 for binary data; ciphertext resulting from these modes may
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

• A classification of the different types of keys to be use. Many of these requirements are refinements of the
used with cryptographic algorithms, a specification requirements for CKMS designers that are specified in SP
of the protection required for each key type, 800-130: A Framework for Designing Cryptographic Key
and identification methods for providing this Management Systems. Other requirements are intended for
protection; the service providers of a CKMS used by federal agencies and
their contractors. Guidance is also provided for the federal
• A listing of the states in which a key may exist
agencies in selecting CKMSs that support the security and
during its lifetime;
management policies of those agencies.
• A discussion of a variety of key-management
This document was completed in October 2015
issues related to key management, including
and is available at http://nvlpubs.nist.gov/nistpubs/
key usage, cryptoperiods, domain-parameter
SpecialPublications/NIST.SP.800-152.pdf.
and public-key validation, backup and archiving;
and SP 800-56A: Recommendation for Pair-Wise Key
Establishment Schemes Using Discrete Logarithm
• Guidance for cryptographic algorithm and key size
Cryptography:
selection (e.g., the security strength provided by a
given algorithm with a specified key size).
SP 800-56A was originally published in 2006, and revised
Another revision of the document was completed in in 2007 and 2013. This document specifies Diffie-Hellman
January 2016 that includes information on and references (DH) and Menezes-Qu-Vanstone (MQV) key-establishment
to new and revised documents developed by the CTG (e.g., schemes, both elliptic curve and finite field versions. Key
SP 800-152, as discussed below); the removal of references establishment is a procedure that results in keying material
to the Dual_EC_DRBG, which was removed from SP 800- that is shared between the participants. A key-establishment
90A: Recommendation for Random Number Generation scheme is defined by a cryptographic algorithm, together
Using Deterministic Random Bit Generators; a revision of with an identification of other information that must be
the security-strength tables; and a revision of the key-state available by both parties when establishing keys. The
discussion to provide more clarification. schemes are intended for use in communication protocols
(e.g., Transport Layer Security (TLS), one of the protocols
SP 800-57, Part 1 is available at http://nvlpubs.nist.gov/
used by the Internet). The key-establishment schemes in SP
nistpubs/SpecialPublications/NIST.SP.800-57pt1r4.pdf.
800-56A use public key algorithms, and each participant in
SP 800-131A: Transitions: Recommendation for
a key-agreement transaction uses a pair of keys—a public
Transitioning the Use of Cryptographic Algorithms and Key
key and a private key.
Lengths:
Both key-agreement and key-transport schemes are
SP 800-131A was originally published in January 2011. specified in the document. A key-agreement scheme is a
This document provides specific guidance for transitions procedure in which both parties in a key-establishment
to the use of stronger cryptographic keys and more robust transaction contribute information that is used in generating
algorithms. An update of SP 800-131A was completed in a cryptographic key. The key-agreement process includes the
November 2015. This update removes approval for the Dual_ generation of a shared secret (which is not itself considered
EC_DRBG that was specified in SP 800-90A; deprecates the to be a cryptographic key), and the derivation of keying
use of non-approved key-establishment schemes; disallows material using the shared secret. Several key-agreement
the use of non-approved key-wrapping methods after 2017; schemes are specified in SP 800-56A. Figure 11: (See next
and indicates that the use of the SHA-3 family of hash page) Key-Agreement Example below provides a simplified
functions is acceptable, in addition to the use of the SHA-2 example of a key-agreement scheme. In this example, each
family of hash functions and some applications of SHA-1. party:
SP 800-131A is available at http://nvlpubs.nist.gov/ 1. Generates a key pair (either prior to or during
nistpubs/SpecialPublications/NIST.SP.800-131Ar1.pdf. the key-agreement transaction);
SP 800-152: A Profile for U.S. Federal Cryptographic Key 2. Obtains the public key of the other party;
Management Systems (CKMS):
3. Computes a shared secret using one’s own
SP 800-152 provides guidance on the CKMS to be keys and the other party’s public key; and
used by the Federal Government. This document contains
4. Derives one or more keys from the shared
requirements for CKMS design, implementation, procurement, 39
secret.
installation, configuration, management, operation and
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 11: Key-Agreement Example
Key transport is a key-establishment method whereby Recommendation for Block Cipher Modes of
one party selects a symmetric key and sends it securely to Operation: Methods for Key Wrapping; SP
one or more other parties. In SP 800-56A, key transport can 800-38F is available at http://nvlpubs.nist.gov/
be performed following the key-agreement process depicted nistpubs/SpecialPublications/NIST.SP.800-38F.
in Figure 11 using a key that was derived during that process. pdf);
Figure 12: Key-Transport Example provides an example of a
3. Sends the resulting ciphertext key to the other
key transport scheme. In this example,
party (i.e., the receiver); and
1. The sender (either party A or party B in Figure
4. The receiver unwraps (i.e., decrypts) the
11: Key-Agreement Example), generates a
received ciphertext key using a key derived
symmetric key;
during the key-agreement process to obtain
2. Wraps (i.e., encrypts) that key using a the original plaintext key that was generated by
key-wrapping algorithm (see SP 800-38F: the sender.
40
Figure 12: Key-Transport Example
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

The current version of SP 800-56A is available at (HMAC), and CMAC is specified for AES in SP 800-38B:
http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST. Recommendation for Block Cipher Modes of Operation:
SP.800-53Ar4.pdf. the CMAC Mode of Authentication. FIPS 198-1 is available at
http://csrc.nist.gov/publications/fips/fips198-1/FIPS-198-1_
SP 800-56A has been under revision during FY 2016.
final.pdf; SP 800-38B is available at: http://nvlpubs.nist.gov/
This revision will:
nistpubs/Legacy/SP/nistspecialpublication800-38b.pdf.
• Approve the use of additional parameter/key sizes
The current version of SP 800-56C is available
for the finite field schemes; currently, only key
at http://nvlpubs.nist.gov/nistpubs/Legacy/SP/
sizes of 2048 and 3072 bits are specified. Larger
nistspecialpublication800-56c.pdf.
key sizes will be allowed and defined in the next
version.
SP 800-56C is being revised to:
• Allow the use of pre-defined domain parameter
• Move the key derivation functions specified in SP
groups that are not currently allowed by SP 800-
800-56A into SP 800-56C as well as the references
56A. Domain parameters are used to generate
to SP 800-135: Recommendation for Existing
keys and compute the shared secret. Methods
Application-Specific Key Derivation Functions;
for generating domain parameters are specified
• Allow the use of KMAC, as specified in Draft SP
for the finite field schemes in FIPS 186-4: Digital
800-185, SHA-3 Derived Functions: cSHAKE,
Signature Standard (DSS). The revision of SP 800-
56A will allow the use of domain-parameter groups
Keccak Message Authentication Code (KMAC),
TupleHash and ParallelHash, for key derivation;
using “safe primes” that are used in the Transport
Layer Security (TLS) and Internet Key Exchange • Define additional Message Authentication Code
(IKE) protocols, which were not generated using (MAC) lengths for the new parameter-size sets
the methods in FIPS 186-4. These pre-defined that will be allowed in the revision of SP 800-56A;
groups will be listed in Annex A of FIPS 140-2. and
• Move all key-derivation functions to SP 800-56C: • Provide a formula for estimating the security
Recommendation for Key Derivation Through strength for the parameter-size sets that are
Extraction-then-Expansion. SP 800-56A currently not explicitly listed in SP 800-56A and SP 800-
specifies two versions of a single step key- 56B.
derivation function, refers to SP 800-56C for a
The revision of SP 800-56C will be available for public
two-step key-derivation procedure, and refers
comment in FY 2017.
to SP 800-135: Recommendation for Existing
Application-Specific Key Derivation Functions, for New Documents Under Development:
application-specific key-derivation functions.
A new NIST publication is under development that
The revision of SP 800-56A will be available for public provides guidance on the search resistance of a bit string
comment in FY 2017. output from an approved cryptographic algorithm (e.g.,
a cryptographic key or encrypted data). Search resistance
SP 800-56C: Recommendation for Key Derivation Through
is a (rough) measure of the amount of secrecy that can be
Extraction-then-Expansion:
provided by a bit string, given the genealogy (i.e., how it was
SP 800-56C specifies techniques for the derivation generated), handling (i.e., what happened to it after it was
of keys from a shared secret generated during a key- generated), the usage (i.e., what algorithm it will be used
establishment scheme defined in SP 800-56A and SP with), length, and any other secret values and processes
800-56B using a two-step extraction-then-expansion associated with the generation and handling of that bit
procedure. SP 800-56A is discussed above. SP 800-56B: string. When approved algorithms are used, this document
Recommendation for Pairwise Key-Establishment Schemes is intended to provide methods for determining the search
Using Integer Factorization Cryptography, is available at resistance of the bit string. This document, SP 800-158: Key
http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST. Management: The Search resistance of Bit Strings Output
SP.800-56Br1.pdf. by Cryptographic Algorithms, has involved a considerable
amount of new research, since it is an area that has not
SP 800-56C uses either HMAC or the Cipher-
been addressed to date. This publication will be available for
based Message Authentication Code (CMAC) algorithm
public comment in FY 2017.
during the two-step process. HMAC is specified in FIPS 41
198-1: The Keyed-Hash Message Authentication Code
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

A new document was started in FY 2016 on key storage testssl.sh (see https://github.com/drwetter/testssl.sh),
and recovery (e.g., key backup and archiving). This document an open-source program that tests TLS-enabled servers,
is intended to serve as a guideline for the storage and providing information about the protocols and cipher suites
recovery of cryptographic keys that are not under the direct supported, in addition to checking for some well-known
control of the entity using those keys (e.g., the owner). This flaws. In FY 2017, CTG will be contributing code to testssl.sh
includes the backup and archiving of copies of the keys and that tests a TLS server’s configuration for conformance to SP
the metadata associated with them. The document will also 800-52 Revision 2. CTG intends to make a draft version of
discuss the recovery of those keys when required (e.g., by the this code available when the draft of SP 800-52 Revision 2 is
key’s owner or the owner’s organization). posted for public comment.
Plans for FY 2017: The Internet Engineering Task Force (IETF) is actively
developing extensions that can be used to add functionality
During FY 2017, the CTG is expecting to accomplish the
to TLS. CTG will continue to review updates and additions to
following tasks:
the TLS protocol in FY 2017.
• Provide the drafts of SP 800-56A and SP 800-56C
CONTACTS:
for public comment;
Dr. Kerry McKay Dr. Lily Chen
• Begin the revision of SP 800-56B;
(301) 975-4969 (301) 975-6974
• Provide the draft of SP 800-158 for public
kerry.mckay@nist.gov lily.chen@nist.gov
comment; and
• Continue the development of the key-storage
Elliptic Curve Cryptography
document.
Elliptic curve cryptography is critical to the adoption
FOR MORE INFORMATION, SEE:
of strong cryptography as we migrate to higher security
http://csrc.nist.gov/groups/ST/key_mgmt strengths. NIST has standardized elliptic curve cryptography
for digital signature algorithms in FIPS 186: Digital Signature
CONTACTS: Standard (DSS), and for key establishment schemes in SP
800-56A: Recommendation for Pair-Wise Key Establishment
Ms. Elaine Barker Mr. Ray Perlner
Schemes Using Discrete Logarithm Cryptography.
(301) 975-2911 (301) 975-3357
elaine.barker@nist.gov ray.perlner@nist.gov In FIPS 186-4, NIST recommends fifteen elliptic curves
of varying security strengths for use in these elliptic curve
Dr. Lily Chen Dr. Allen Roginsky cryptographic standards. However, the provenance of the
(301) 975-6974 (301) 975-8136 curves is not fully specified in the standard, leading to recent
lily.chen@nist.gov allen.roginsky@nist.gov public concerns that there could be a hidden weakness in
these curves. NIST is not aware of any vulnerability in these
curves when they are implemented correctly and used as
Transport Layer Security
described in NIST standards and guidelines.
SP 800-52: Guidelines for the Selection, Configuration,
More than fifteen years have now passed since these
and Use of Transport Layer Security (TLS) Implementations,
curves were developed, and the community now knows more
provides recommendations regarding TLS server and
about the security of elliptic curve cryptography and practical
client implementations. TLS is a widely used cryptographic
implementation issues. Advances within the cryptographic
protocol that provides communication security for a variety
community have led to the development of new elliptic
of network applications, such as email, e-commerce, and
curves and algorithms whose designers claim to offer better
healthcare.
performance and are easier to implement in a secure manner.
SP 800-52 was first published in June of 2005, and Some of these curves are under consideration in voluntary,
SP 800-52 Revision 1 was published in April of 2014. Since consensus-based Standards Developing Organizations.
the revision, CTG has been following developments in TLS
In FY 2016, NIST solicited comments on possible
implementations, including updates and attacks. In FY 2016,
improvements to FIPS 186-4. In particular, comments were
a second revision began that considers these developments.
requested on the possibility of adding new elliptic curves to
This second revision will be posted for public review and
the current recommended set—as well as adding new digital
comment in FY 2017.
42 signature schemes. Throughout 2016, NIST began resolving
CTG has been contributing to the development of the comments and revising FIPS 186-4. It is expected that the
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

revised draft version of FIPS 186-5 will be available for public  issued draft submission requirements and evaluation criteria
comment in FY 2017. for public comment. (see https://www.federalregister.gov/
articles/2016/08/02/2016-18150/request-for-comments-on-
CONTACTS:
post-quantum-cryptography-requirements-and-evaluation-
| Email project team: EllipticCurves@nist.gov |     |     |     |     |     |     | criteria) |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
The NIST team also continues to be productive in post-
| Dr. Dustin Moody  |     | Dr. Lily Chen   |     |     |     |     |          |               |     |            |      |                |       |
| ----------------- | --- | --------------- | --- | --- | --- | --- | -------- | ------------- | --- | ---------- | ---- | -------------- | ----- |
|                   |     |                 |     |     |     |     | quantum  | cryptography  |     | research.  | The  | results  have  | been  |
| (301) 975-8136    |     | (301) 975-6974  |     |     |     |     |          |               |     |            |      |                |       |
published at major conferences, such as Embedded Security
| dustin.moody@nist.gov   |     | lily.chen@nist.gov  |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in Cars (ESCARS), Selected Areas in Cryptography (SAC),
Mr. Andy Regenscheid  PQCrypto,  and  Eurocrypt.  NIST  researchers  have  given
(301) 975-5155  presentations at conferences and workshops to increase
|     |     |     |     |     |     |     | awareness  | of  | the  upcoming  | migration.  |     | NIST  | has  also  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | ----------- | --- | ----- | ---------- |
andrew.regenscheid@nist.gov
sponsored other research, education, and research events.
In FY 2017, NIST will continue to explore the security
Post-Quantum Cryptography
and feasibility of purported quantum-resistant technologies,
In recent years, there has been a substantial amount of
|     |     |     |     |     |     |     | with  the  | ultimate  | goal  | of  uncovering  |     | the  fundamental  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----- | --------------- | --- | ----------------- | --- |
research on quantum computers – machines that exploit
mechanisms necessary for efficient, trustworthy, and cost-
quantum mechanical phenomena to solve problems that are
effective information assurance in the post-quantum era.
difficult or intractable for conventional computers. If large-
The Post-Quantum Standardization Process will begin in
scale quantum computers are ever built, they will be able to
early FY 2017, with the issuance of the finalized submission
break the existing infrastructure of public-key cryptography.
requirements and evaluation criteria. There will be a one-year
The focus of the Post-Quantum Cryptography project is
period during which quantum-resistant algorithms may be
to identify candidate quantum-resistant systems that are
submitted for possible standardization. After the submission
secure against both quantum and classical computers—as
period, there will be a public workshop in FY 2018, followed
well as the impact that such post-quantum algorithms will
by multiple rounds of evaluation and analysis.
have on current protocols and security infrastructures.
FOR MORE INFORMATION, SEE:
NIST researchers have held regular seminars throughout
FY 2016. The presentation topics include the latest published  https://www.nist.gov/pqcrypto
results and security analyses, as well as status reports on
CONTACTS:
| quantum  computation,  |     | hash-based     |     | signatures,    |     | coding- |     |     |     |     |     |     |     |
| ---------------------- | --- | -------------- | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| based  cryptography,   |     | lattice-based  |     | cryptography,  |     | and     |     |     |     |     |     |     |     |
Email project team: pqc@nist.gov
multivariate cryptography. Through these presentations and
discussions, the project team has made significant progress  Dr. Dustin Moody  Dr. Lily Chen
| in  understanding  | the  | strengths  | and  | weaknesses  |     | of  the  |                 |     |     |                 |     |     |     |
| ------------------ | ---- | ---------- | ---- | ----------- | --- | -------- | --------------- | --- | --- | --------------- | --- | --- | --- |
|                    |      |            |      |             |     |          | (301) 975-8136  |     |     | (301) 975-6974  |     |     |     |
existing cryptographic schemes in each category. dustin.moody@nist.gov   lily.chen@nist.gov
In April 2016, NIST published NISTIR 8105: Report on Post-
Dr. Yi-Kai Liu
Quantum Cryptography, which shared the team’s current
(301) 975-6499
| understanding  | about  | the  status  |     | of  quantum  |     | computing  |     |     |     |     |     |     |     |
| -------------- | ------ | ------------ | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
yi-kai.liu@nist.gov
and post-quantum cryptography. The report also outlined
NIST’s initial plan to move forward in this area. At Post-
Quantum Cryptography (PQCrypto) 2016, NIST announced  Circuit Complexity
| that  it  would  | begin  | the Post-Quantum Standardization  |     |     |     |     |                |     |             |       |     |              |          |
| ---------------- | ------ | --------------------------------- | --- | --- | --- | --- | -------------- | --- | ----------- | ----- | --- | ------------ | -------- |
|                  |        |                                   |     |     |     |     | Cryptographic  |     | functions,  | such  | as  | encryption,  | digital  |
Process, a thorough multi-year effort with the objective of
|     |     |     |     |     |     |     | signatures,  | and  | hashing,  | are  implemented  |     | as  | electronic  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | --------- | ----------------- | --- | --- | ----------- |
creating new quantum-resistant cryptographic standards
|                          |             |        |                  |          |             |            | circuits       | for  a  | wide  class  | of  applications.  |     | In  practice,  | it         |
| ------------------------ | ----------- | ------ | ---------------- | -------- | ----------- | ---------- | -------------- | ------- | ------------ | ------------------ | --- | -------------- | ---------- |
| for  public-key          | encryption  |        | and              | digital  | signatures  | (see       |                |         |              |                    |     |                |            |
|                          |             |        |                  |          |             |            | is  important  | to      | be  able     | to  minimize       |     | the  size      | of  these  |
| www.nist.gov/pqcrypto).  |             | These  | functionalities  |          |             | are  much  |                |         |              |                    |     |                |            |
circuits. This problem is closely related to designing small
| more  complex  | than  | AES  | or  SHA-3,  |     | and  will  | require  |     |     |     |     |     |     |     |
| -------------- | ----- | ---- | ----------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
combinational circuits. These circuits use only binary AND,
| fundamentally  | new  | techniques  | to  | address  | several  | open  |     |     |     |     |     |     |     |
| -------------- | ---- | ----------- | --- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
XOR and NEGATION gates, i.e., multiplication, addition, and
| research  questions  |     | in  this  | area  | (for  example,  |     | how  to  |     |     |     |     |     |     |     |
| -------------------- | --- | --------- | ----- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
“+1” in arithmetic modulo 2. A combinational circuit on four
measure security against quantum attacks when a quantum  43
|     |     |     |     |     |     |     | variables (X, X, X |     | , and X | ) using AND and XOR gates is  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------- | ----------------------------- | --- | --- | --- |
computer has not yet been built). In August 2016, NIST  1 2 3 4
depicted in Figure 13.
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

the standard reference for benchmarking tools in multiparty
computation.
The following is a partial list of new results by our team:
• Better recursions for Karatsuba multiplication,
which yielded the smallest known circuits for binary
multiplication (i.e., multiplication of polynomials of
degree n over the Galois Field with two elements).
This yields important speed increases in elliptic
curve cryptography and other applications.
• Optimal circuits were constructed - with respect
The red nodes are AND gates; the yellow nodes are XOR gates.
to multiplicative complexity - for all predicates on
four bits (see the example below). There are 65,536
Figure 13: Combinational Boolean Circuit
such predicates. Surprisingly, the multiplicative
The project team has shown that finding optimal
complexity of all these functions turned out to
combinational circuits is MAX SNP-complete. In practice, this
be at most three. Additionally, our circuits use no
means that it is necessary to settle for methods that design
more than seven non-linear gates (XOR, XNOR).
“good” circuits, as opposed to provably optimal circuits. f
This is quite hard. Consider the following predicate
The CTG has developed and implemented new solutions for
(arithmetic is modulo 2):
the circuit-minimization problem. Two patents have been
f = xx + xx + xx + xx +xx + xxx + xxx + xxx x
granted related to this work, the last one in FY 2014. These 1 2 1 3 1 4 2 3 2 4 1 2 3 1 2 4 1 2 3 4.
are held jointly between NIST and the University of Southern • Computing the last term requires three
Denmark. multiplications. So, it is quite surprising that the
full expression can be computed using only three
The CTG is also researching circuit-based security metrics
multiplications. But, we have shown this to be
for cryptographic functions. For a function to be secure (in
true for f and all other predicates on four bits. The
particular, one-way), it must be the case that any circuit that
circuit depicted above computes f using three
implements it is sufficiently complex. In particular, a function
multiplications and six additions.
is insecure if it can be implemented by a circuit containing
too few Boolean AND gates. This security metric, namely the • A proof was developed that the maximum
number of AND gates necessary and sufficient to implement multiplicative complexity of predicates on five bits
a function, is referred to as its multiplicative complexity. (there are more than 4 billion such predicates) is
Unfortunately, determining multiplicative complexity is four. The proof is constructive, meaning that the
extremely hard. circuits can actually be built.
The CTG has published circuits that are provably • A proof was developed that an explicit function
optimal or close to optimal (with respect to multiplicative requires at least 3.01n gates. This constitutes the
complexity) for important classes of functions. In the process, only improvement on this problem for more than
we developed tools that have wide applicability for both 30 years. The result is due to Magnus Find, in
theoretical and applied research in security and cryptography. collaboration with mathematicians from New York
University (NYU) and from the Steklov Institute, St.
Multiparty computation is a technique that allows a
Petersburg, Russia.
group of people to compute a function of their inputs without
revealing the inputs themselves. Examples of this are: i) In 2017, plans are in place to begin the implementation
holding an election; ii) conducting closed-bid auctions in of combinational circuits in ASIC (application-specific
which only the winning bid is determined; and iii) proving to a integrated circuit) hardware. The team will also map the
third party that a person’s encrypted attributes satisfy some multiplicative complexity of all functions of six variables
requirement, such as “over 21 and (U.S. citizen or Canadian and will code a new heuristic for simultaneously reducing
citizen).” The protocols that solve multiparty computation the size and depth of circuits.
problems often encrypt bits using arithmetic modulo 2. The
Circuits are posted periodically at:
complexity of such protocols largely depends on the number
of multiplications required. Hence, expressing functions as http://cs-www.cs.yale.edu/homes/~peralta/CircuitStuff/CMT.
circuit computations with only a few multiplication (AND) html
44
gates is important. Some of the published circuits are now
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

CONTACT: CONTACTS:
Dr. Rene Peralta Mr. Lawrence Bassham Dr. Kerry McKay
(301) 975-8702 (301) 975-3292 (301) 975-4969
rene.peralta@nist.gov lawrence.bassham@nist.gov kerry.mckay@nist.gov
Dr. Meltem Sönmez Turan
Lightweight Cryptography (301) 975-4391
There are several emerging areas in which highly meltem.turan@nist.gov
constrained devices are interconnected and working in
concert to accomplish a task. Examples of these areas
The NIST Randomness Beacon
include automotive systems, sensor networks, healthcare,
NIST has implemented a source of public randomness,
distributed control systems, the Internet of Things (IoT),
Figure 13: Combinational Boolean Circuit which is available at https://beacon.nist.gov/home. It
cyber-physical systems, and the smart grid. Security and
uses two independent, commercially-available sources of
The project team has shown that finding optimal privacy can be very important in these areas. Because most
randomness, each with an independent hardware entropy
combinational circuits is MAX SNP-complete. In practice, this of the modern cryptographic algorithms were designed for
source and SP 800-90A-approved components.
means that it is necessary to settle for methods that design desktop/server environments, many of these algorithms
“good” circuits, as opposed to provably optimal circuits. cannot be implemented in the constrained devices used The NIST Beacon is designed to provide unpredictability, f
The CTG has developed and implemented new solutions for by these applications. When current NIST-approved autonomy, and consistency. Unpredictability means that
the circuit-minimization problem. Two patents have been algorithms can be engineered to fit into the limited users cannot algorithmically predict bits before they are
granted related to this work, the last one in FY 2014. These resources of constrained environments, their performance made available by the source. Autonomy means that the
are held jointly between NIST and the University of Southern may not be acceptable. For these reasons, NIST started a source is resistant to attempts by outside parties to alter the
Denmark. lightweight cryptography project in 2013 that was tasked distribution of the random bits. Consistency means that a set
with determining the need and developing a strategy for the of users can access the source in such a way that they are
The CTG is also researching circuit-based security metrics
standardization of lightweight cryptographic algorithms. confident of receiving the same random string.
for cryptographic functions. For a function to be secure (in
particular, one-way), it must be the case that any circuit that CTG staff are examining applications in constrained The NIST Beacon posts bit-strings in blocks of 512 bits
implements it is sufficiently complex. In particular, a function environments to determine whether NIST should develop every 60 seconds. Each such value is time-stamped and
is insecure if it can be implemented by a circuit containing lightweight cryptographic standards. This includes signed to form a packet that also includes the hash of the
too few Boolean AND gates. This security metric, namely the communicating with industry experts to understand the previous value to chain the sequence of values together.
number of AND gates necessary and sufficient to implement challenges and limitations and following the work of This prevents all parties, even the source, from retroactively
a function, is referred to as its multiplicative complexity. other standardization bodies in this area. In FY 2015, CTG changing an output packet without being detected. The
Unfortunately, determining multiplicative complexity is organized a Lightweight Cryptography Workshop to discuss NIST Beacon keeps all output packets. At any point in time,
extremely hard. issues related to the security and resource requirements of the full history of outputs is available to users.
applications in constrained environments and potential future
The CTG has published circuits that are provably Tables of random numbers have probably been used for
standardization of lightweight primitive algorithms. Using
optimal or close to optimal (with respect to multiplicative multiple purposes at least since the Industrial Revolution.
input gathered at the workshop in FY 2016, CTG released
complexity) for important classes of functions. In the process, In the digital age, algorithmic pseudorandom number
draft NISTIR 8114, Draft Report on Lightweight Cryptography
we developed tools that have wide applicability for both generators (PRNGs) have largely replaced these tables. The
for public comments. This report provides an overview of
theoretical and applied research in security and cryptography. NIST Beacon expands the use of randomness to multiple
the lightweight cryptography project at NIST, and describes
scenarios in which neither tables nor PRNGs can be used.
Multiparty computation is a technique that allows a a plan for the standardization of lightweight cryptographic
The extra functionalities stem mainly from three features.
group of people to compute a function of their inputs without algorithms. This plan involves the creation of profiles that
First, the Beacon-generated numbers cannot be predicted
revealing the inputs themselves. Examples of this are: i) will target specific applications and requirements where
before they are published. Second, the public, time-bound,
holding an election; ii) conducting closed-bid auctions in conventional cryptography may not be suitable.
and authenticated nature of the Beacon allows a user
which only the winning bid is determined; and iii) proving to a
CTG is organizing the second NIST workshop on application to prove to anybody that it used truly random
third party that a person’s encrypted attributes satisfy some
Lightweight Cryptography, taking place at the beginning of numbers not known before a certain point in time. Third, this
requirement, such as “over 21 and (U.S. citizen or Canadian
FY 2017 to discuss the plan outlined in the draft report before proof can be presented offline and at any point in the future.
citizen).” The protocols that solve multiparty computation
it is finalized. The next steps in the plan include working with
problems often encrypt bits using arithmetic modulo 2. The Although commercially available physical sources of
industry to create an initial set of profiles and the selection
complexity of such protocols largely depends on the number randomness are adequate as entropy sources for currently
of algorithms that meet profile requirements.
of multiplications required. Hence, expressing functions as envisioned implementations of the NIST Beacon, the NIST
circuit computations with only a few multiplication (AND)
45
gates is important. Some of the published circuits are now
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Randomness Beacon project team is working on developing NIST cryptographic standards have been extensively
a source of verifiably random sequences. In collaboration with used in the wireless standards developed in the IEEE 802
NIST physicists from the Physical Measurement Laboratory community. In FY 2016, the NIST team actively worked with
(PML), the project team aims to use quantum non-locality to the IEEE 802.1 security group in using the Galois/Counter
build an entropy source whose unpredictability is guaranteed Mode (GCM) specified in NIST Special Publication 800-38D
by the laws of physics. In FY 2016, a major milestone was for Media Access Control (MAC) security (MACsec) solutions.
achieved, namely, a strong loophole-free test of local realism
In FY 2016, NIST researchers continuously collaborated
(where individual particles are governed by elements of
with the IEEE 802.21 Working Group to develop solutions
reality, even if these elements are hidden from us) (see
for multicast group key distribution and coauthored a paper
https://www.nist.gov/news-events/news/2015/11/nist-team-
titled “Security Multicast Group Key Management and Key
proves-spooky-action-distance-really-real).
Distribution in IEEE 802.21.” The paper has been accepted by
The project team has also made progress in reaching a the Security Standardization Research Conference 2016 (SSR
goal of helping other institutions set up other interoperable 2016) and will be presented on December 5-6, 2016.
sources. This is important because multiple sources can be
In FY 2017, the NIST team will continue to contribute
combined in such a way that all sources would have to be
to IEEE 802 wireless standards and provide guidance for
compromised in order to degrade the common random
NIST cryptographic standard usage in wireless and mobility
strings.
applications.
As of the end of FY 2016, the NIST Beacon has been
CONTACT:
functioning without interruption for more than three years.
During this time, the project team has received valuable input Dr. Lily Chen
from a growing community of users. As a result, the project (301) 975 -6974
team will provide an enhanced version of the service during lily.chen@nist.gov
FY 2017. The enhancements are mainly intended to enable
interoperability.
Blockchains
NIST encourages the community-at-large to research
and publish novel ways in which this tool can be used.
The Cryptographic Technology Group (CTG) began
FOR MORE INFORMATION, SEE: studying the use of blockchains, which have been suggested
as a solution for many applications. A blockchain is a
https://www.nist.gov/programs-projects/nist-randomness-
distributed database that maintains a continuously growing
beacon
list of records called blocks that are secured from revision
using a hash function. Each block contains a link to the
CONTACT:
previous block. A new block is added to the chain only when
Dr. Rene Peralta multiple parties (possibly mutually untrusting parties) agree
(301) 975-8702 to its accuracy. In essence, a blockchain is a mutually agreed-
rene.peralta@nist.gov upon record of history.
Cryptography Applications in
Wireless and Mobile Security
Today, wireless networks have been integrated into
modern communication systems that connect mobile devices
using multiple radio technologies. Such heterogeneous
networks demand integrated security solutions. The NIST
team has worked closely with different working groups in the
IEEE 802 LAN/MAN Standards Committee since 2006 and
Figure 14: Example of a Blockchain
made solid contributions to the security solutions for wireless
networks. The NIST team has been involved in the IEEE 802.11 Figure 14: Example of a Blockchain illustrates three
and IEEE 802.21 working groups to develop standards for blocks in a blockchain, where each block contains at least one
cryptographic key management schemes for the mobility transaction, a nonce and the hash value of the previous block
46 environment. in the chain.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

The most well-known example of the use of a blockchain A primary goal of this project is to provide high-quality,
is BitCoin and similar digital currencies. However, the use of truly unpredictable random data to devices on the Internet
blockchains has been proposed for other applications, such to enable them to generate strong cryptographic keys and
as smart contracts and various ledgering applications. attest the strength of the keys used to protect data in transit
or at rest, thereby enabling cryptographic system strength
Many organizations have suggested applications for the
attestation. Achieving this goal would provide a solid basis
use of blockchains, some of which may not be appropriate.
for achieving the goals of the Automated Cryptographic
The CSD is investigating the use of blockchains to determine
Validation Testing project (see http://csrc.nist.gov/projects/
which application types are appropriate for using blockchains
acvt/ ) as well as addressing the problems targeted by the
and which are not. The CTG is monitoring the proposed
Cryptographic Programs and Laboratory Accreditation (see
uses of cryptography to assure that current cryptographic
the next section: Validated Programs, the first project in that
techniques are used properly and whether new techniques
section), where entropy estimation has persisted as one of
are required.
the most difficult and labor-consuming activities, causing
During FY 2016, the CTG participated in two blockchain
problems for all parties involved: the industry, the testing
workshops: the “DC Blockchain Summit” in March and the
laboratories and the government validators.
“Blockchain and Healthcare Workshop” in September.
Random data obtained from sources of true
The CTG took an active role in the September workshop
randomness that are based on unpredictable physical
by reviewing papers and providing presentations on
phenomena, such as quantum effects, is much better
blockchains and the CTG standards that might be useful for
suited for cryptographic applications. CSD is collaborating
future blockchain work. The CSD also began testing the use
with the NIST Physical Measurement Laboratory (PML)
of several blockchain nodes.
to build a quantum source. The aim is to use quantum
During FY 2017, in addition to continuing familiarization
effects to generate sequences that are guaranteed to be
with the use of blockchains and monitoring the cryptography
unpredictable, even if an attacker has access to the random
proposed, the CTG is planning to participate in a blockchain
source. For more information on this collaboration, see
study group sponsored by American Standards Committee
https://www.nist.gov/pml/div684/random_numbers_bell_
X9, the financial services committee of the American
test.cfm/
National Standards Institute (ANSI).
This project aims to develop a system and protocols
CONTACTS:
for obtaining random data with high entropy from one or
more remote sources. The high-level architecture is shown
Ms. Elaine Barker Dr. Lily Chen
in Figure 15: (See next page) High-level Architecture of EaaS.
301-975-2911 (301) 975-6974
The architecture of the Entropy-as-a-Service system consists
ebarker@nist.gov lily.chen@nist.gov
of two main parts: the client-side and the server-side. The
Mr. John Kelsey Dr. Rene Peralta critical components of the system are the quantum device,
(301) 975-5101 (301) 975-8702john. the EaaS server and a secure device in the client systems
kelsey@nist.gov rene.peralta@nist.gov that is capable of providing strong isolation and protection
for the cryptographic keys stored inside the device and
Mr. Dylan Yaga offering a set of basic cryptographic services.
(301) 975-6004
The EaaS server is continuously fed random data from
dylan.yaga@nist.gov
the attached quantum source. The data enters a FIFO (first in,
first out)-like buffer in the server’s Random Access Memory
Entropy as a Service (EaaS) (RAM), and, when a client request arrives, the server reads
the top value from the buffer, signs and encrypts it, and then
The security of cryptography today depends on having
sends it to the requester. The FIFO buffer shifts after every
strong keys and keeping them secret. The ability to generate
request and when new data comes from the random source.
strong cryptographic keys is directly related to having
The EaaS server ensures that the FIFO buffer is erased
access to unpredictable random data, but generating truly
prior to server shutdown and never paged to disk. Open
unpredictable random data on computing devices is hard
implementations can help ensure that this occurs.
and unreliable. As a result, weak keys are widely used in
cryptographic applications, thus compromising the security The client system consists of a classic computing device
of the sensitive data protected by them − potentially with enabled with a dedicated hardware component capable of
disastrous consequences. storing secret cryptographic keys and seeds. A dedicated 47
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

software application bridges the communication between With the conceptual system architecture and protocols
EaaS and the hardware component. Examples of secure defined, the project team continues to engage with industry
hardware components are the Trusted Platform Module (TPM), and academia to obtain feedback on the approach and
TrustZone technology in Advanced Reduced Instruction Set identify possibilities for collaborative approaches to solving
Computing (RISC) Machine (ARM) processors, and Identity important cybersecurity challenges in the domains of
Protection Technology in Intel processors. If a client system cryptography and supply-chain management (e.g., integrated
or device doesn’t have a secure hardware component, it can circuit counterfeiting). The team published a peer-reviewed
still use EaaS. The presence of a hardware component simply paper on EaaS in IEEE Computer, a top professional journal,
provides further guarantees to the system or device user, in September 2016. The team also started a collaboration
when present. with a team of researchers at the University of Florida who
won a NIST research grant to explore ways to leverage
EaaS uses HTTP to transfer entropy payloads from the
EaaS in protecting against integrated circuit counterfeiting
service to clients. To secure this transmission, the server
and thereby help secure the supply chain. The University of
encrypts the data using the client’s provided public key and
Florida researchers will start their project in FY 2017.
digitally signs the payload with the server’s own private key.
The team continues to develop the system to provide
Client devices mix this data with locally available random
a publicly accessible NIST EaaS instance in FY 2017. During
data to seed random number generators to generate strong
the summer of FY 2016, the team hosted a Summer
cryptographic keys and other random values independently
Undergraduate Research Fellowship (SURF) student who
from the remote sources.
developed a sample EaaS-client implementation with a
48
Figure 15: High-level Architecture of EaaS
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

proper cryptographic mixing of random data obtained from the National Voluntary Laboratory Accreditation Program
multiple EaaS instances and local sources. The team plans (NVLAP) accredited Cryptographic and Security testing
to publish the server and client code on GitHub in FY 2017 (CST) laboratories for validation testing against the derived
and invite the public to voluntarily adopt it. Related to this, test requirements (DTR), implementation guidance (IG),
the project team is planning to work on developing public and applicable CMVP programmatic guidance. According
criteria for reputable EaaS hosts. The team succeeded to existing guidance, the CST laboratories must perform
in obtaining NIST funding to hire contractors to help with 100 % independent testing of the modules submitted by the
the implementation and hosting of the EaaS server; the vendors.
contractor team has been identified, and the project will
The structure and the rules under which the CMVP
start in FY 2017.
operates worked well for the level of the technology utilized
CONTACT: by the Federal Government when the program was created
more than two decades ago. As technology has advanced,
Dr. Apostol Vassilev
however, the module testing process no longer satisfies
(301) 975-3221
the current industry and government operational needs.
apostol.vassilev@nist.gov
Testing is exceedingly long—well beyond typical product-
development cycles across a wide range of technologies.
Automated Cryptographic The resulting validated modules often do not provide useful
interfaces for integration into IT systems to enable run-time
Validation Testing
monitoring of modules for compliance with FISMA.
The Cryptographic Module Validation Program
NIST recognizes the need to improve the efficiency and
(CMVP) was established on July 17, 1995 by NIST to
effectiveness of cryptographic module testing to reduce the
validate cryptographic modules conforming to the Federal
time and cost required for testing, while providing a high
Information Processing Standards (FIPS) 140-1, Security
level of assurance for Federal Government consumers.
Requirements for Cryptographic Modules, and other FIPS
cryptography-based standards. FIPS 140-2 was released on The principal goals of this project are to collaborate
May 25, 2001 and supersedes FIPS 140-1. with commercial or open source producers of cryptographic
capabilities and government consumers of FIPS 140-validated
The current implementation of the CMVP is shown in modules to:
Figure 16: Current Validation Flow below. The CMVP leverages
49
Figure 16: Current Validation Flow
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

• Improve the efficiency and effectiveness of the rest of algorithms currently tested by the traditional
cryptographic module testing by adopting the best Cryptographic Algorithm Validation Program (http://csrc.
practices used by industry; nist.gov/groups/STM/cavp/index.html) with the goal of
replacing it by the second quarter of 2018.
• Develop test procedures and techniques that
provide assurance of module compliance to FIPS
The project activities are structured by work areas in
140 in an automated manner, based on machine-
order for subject-matter experts to more narrowly focus and
readable artifacts or evidence (Examples of
make progress.
machine readable artifacts are Extensible Markup
1. Algorithm and Protocol Testing;
Language (XML) or JavaScript Object Notation
(JSON) files containing logs from performed tests
2. Cryptographic Module Testing,
and the corresponding results. At this stage, we
a. Hardware,
have only partially concluded the research on this
b. Software, and
and can point to examples at https://github.com/
c. Modules in cloud environments;
usnistgov/ACVP); and
and
• Identify techniques and procedures that provide 3. Positioning and relationships to other
continued assurance of operational compliance to Government Validation Programs.
FIPS 140 for cryptographic modules throughout
The project has several planned deliverables, including
their lifecycle.
the identification of prospective technical approaches that
The scope of this project is broken into multiple adopt industry best practices and produce artifacts that
phases to be performed over several years. are machine readable and map to DTR requirements, and a
selection of the best technical and feasible approaches.
PHASE 1
CONTACT:
• Identify potential approaches,
Dr. Apostol Vassilev
• Select the best technical approach or approaches
(301) 975-3221
to prototype, and
apostol.vassilev@nist.gov
• Document the technical approach.
PHASE 2
VALIDATION PROGRAMS
• Develop working prototypes, and
• Evaluate the prototypes against the principal
goals.
Federal agencies, industry, and the public rely on many
PHASE 3 of the standards and specifications supported by ITL. Poor
implementations of these standards or specifications may
• Publish a draft, provide a review period, adjudicate
render a product insecure, potentially placing sensitive
the comments, and publish the final version.
information at risk. ITL operates several validation programs
PHASE 4 that help provide a level of assurance that products meet
established security requirements and conform to published
• Integrate the final version into the operational
specifications. To that end, the CSD Security Testing,
CMVP program.
Validation, and Measurement Group (STVMG) develops test
Currently, the project is focused on completing the suites and test methods; provides implementation guidance
documentation of the technical approach for automating and technical support to industry forums; and conducts
the algorithm testing and researching the approaches education, training, and outreach programs.
for automating the software module testing. The team
STVMG’s validation programs work together with
working on this project, in collaboration with the industry,
independent laboratories that are accredited by the National
demonstrated successful automated algorithm validations
Voluntary Laboratory Accreditation Program (NVLAP). Based
at the International Cryptographic Module Conference in
on independent laboratory test reports and test evidence
May 2017 for some algorithms (see https://acvts.nist.gov/
provided by the labs, the validation programs described
50 acvp/home) and continues to develop the automation of
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

below validate the implementation-under-test. Awarded On October 1, 2015, the CMVP began using a new
validations are subsequently published on NIST websites. automated system to manage the validation workflow. The
impact to the CMVP’s efficiency was dramatic. In FY 2016,
Cryptographic Programs and the CMVP awarded 307 new certificates, 111 more than in FY
2015. Figure 17: FY 2016 CMVP Certificates by Security Level
Laboratory Accreditation
displays the number of certificates by security level for FY
Cryptographic Module Validation Program (CMVP)
2016.
The Cryptographic Module Validation Program (CMVP)
was developed to support the federal user communities for
strong, independently tested, and commercially available
cryptographic modules. Through this program, the CMVP
works with international government, public and private
sectors as a part of the cryptographic community to
achieve standards-based security and assurance of correct
implementation. The goal is to provide federal agencies
with a security metric to use in procuring and deploying
cryptographic modules, and promote the use of validated
modules by industry and the public. The testing performed
by independent third-party laboratories accredited by
the National Voluntary Laboratory Accreditation Program
(NVLAP), and the validations performed by the CMVP
program provide this metric. Federal agencies, industry,
and the public can choose cryptographic modules and/or
products containing cryptographic modules from the CMVP
Validated Modules List and have confidence in the claimed
level of security and assurance of correct implementation.
Cryptographic module testing and validation are
based on published NIST standards. Since federal agencies Figure 17: FY 2016 CMVP Certificates by Security Level
are required to use validated cryptographic modules for
The automated system tracks the status of each
the protection of sensitive unclassified information, the
submission and identifies the order in which the submissions
validated modules and the validated algorithms that the
should be reviewed, based on when each submission is
modules contain represent the culmination and delivery of
added to the CMVP queue. Automating this housekeeping
CSD’s cryptography-based work to the end user.
task significantly increased the efficiency of the validation
The CMVP validates modules that are used in a wide
process. Not only does this allow the CMVP time to focus
variety of products, including Internet browsers, radios, smart
on other tasks, it reduces the number of status messages
cards, space-based communications, munitions, security
from the laboratories that request a status for their specific
tokens, mobile phones, network and storage devices, and
submission. Status messages have dropped from 4 to 6 per
products supporting the Public Key Infrastructure (PKI) and
week to 0 to 1 per week.
electronic commerce. While a module may be a standalone
The number of submissions sitting in the CMVP queue
product (e.g., a virtual private network (VPN) or smart
and the average queue time have been reduced in part due
card), in many cases, a module (e.g., a cryptographic-based
to this automation. The number of modules in the queue has
toolkit) is embedded into many products. Because a small
dropped from an average of 120 to an average of 65. The
number of modules may be incorporated within hundreds of
average queue length (e.g., the amount of time between
products, the validation process has significant impact.
the arrival of a submission and when the review begins)
The theme for the CMVP in FY 2016 was change. The
has dropped from an average of four months to an average
CMVP is evolving to be more efficient and consistent.
of less than two months. The average amount of time to
The CMVP implemented an automated system, modified
validate a module is six months, with some validations being
workflow processes to provide better transparency and
completed within two months. In the last quarter of FY 2016,
strengthened collaboration with the Cryptographic Modules
the queue was, at times, empty.
User Forum (CMUF). 51
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

One specific area where the automated system provided laboratory finalizes the submission to CMVP. If
dramatic improvement was the NIST billing process. laboratories leverage this new capability, the
Generating an invoice was reduced from an average of three CMVP could see a further reduction in the queue
weeks to one day. Similarly, receiving a notification that an length;
invoice was paid went from an average of one week to one
• Anticipating the rollout of the new Computer
day. These are contributing factors to the reduction in the
Security Resource Center (CSRC) web site. This
queue length. This achievement was due to the cooperative
will allow the CMVP to replace the static validation
relationship between the CMVP and NIST Receivables, who
pages with an interactive capability for users, along
worked through technical challenges to allow the systems to
with other improvements for users. Following this,
exchange information.
the CMVP will begin the transition to a web-based
In May 2015, to provide greater transparency to the submission process to replace the current email-
laboratories, the CMVP began sending a weekly report based process;
to each laboratory, providing the status of each of their
• Continuing to strengthen its relationship with
submissions. Before the capability to prepare and send this
the CMUF by collaborating on new and improved
report was available, the CMVP and laboratories would, at
technical guidance and programmatic issues;
times, find that each thought the other had the next action,
and
resulting in unnecessary delays.
• Joining the International Cryptographic Module
In August 2015, to provide greater transparency to
Conference (ICMC) program committee to
users, the CMVP separated the Implementation-Under-Test
continue strengthening partnership within the
(IUT) list from the rest of the Modules-In-Process (MIP) list.
community.
Separating the lists allows the users to quickly and easily see
FOR MORE INFORMATION, SEE:
that the CMVP does not have any information on the modules
currently being tested (i.e., those listed in the IUT list). In fact,
http://csrc.nist.gov/groups/STM/cmvp/index.html
the IUT list is provided as a marketing service for vendors that
have made a commitment to achieving validation, but whose CONTACT:
module(s) are not yet in the MIP.
Ms. Jennifer Cawthra
The CMVP strengthened its relationship with the CMUF by
301-975-8514
supporting the monthly CMUF general membership meetings
jennifer.cawthra@nist.gov
and five CMUF working groups. The working groups are chaired
by a member of industry and/or by laboratory personnel.
Each working group includes a representative from the CMVP. The Cryptographic Algorithm
The current working group topics include the Security Policy Validation Program (CAVP)
Template; Testing Equivalency; Revalidation in Response to
The Cryptographic Algorithm Validation Program
Common Vulnerabilities and Exposures (CVEs); Proposed IG
(CAVP) provides federal agencies in the United States and
Integrity Testing using Random Sampling and IG Updates (IG
Canada with assurance that a cryptographic algorithm has
3.5 Documentation Requirements for Cryptographic Module
been implemented completely and correctly, as specified
Services, IG 1.20 Sub-Chip Cryptographic Subsystems, and
in its approved Federal Information Processing Standard
7.7 Key Establishment and Key Entry and Output). This CMUF
(FIPS-Approved) or NIST-recommended cryptographic
collaboration allows greater progress on technical guidance
algorithm standard. The CAVP was established in 2013 as
and incorporates differing perspectives.
a joint program in collaboration between NIST and the
For FY 2017, the CMVP team is: Communications Security Establishment (CSE) of Canada.
• Anticipating the approval of FIPS 140-3. When Prior to this date, the CAVP’s functions were included in the
approved, the CMVP will create the necessary Cryptographic Module Validation Program (CMVP). With the
documents and processes to support the transition increase in the number and complexity of FIPS-Approved
from FIPS 140-2 to FIPS 140-3; and NIST-recommended cryptographic algorithms, it was
deemed necessary to establish the CAVP as an independent
• Continuing to invest in automation to streamline the
program.
validation process and improve review consistency.
One effort that started in FY 2016 was the ability The CAVP’s goal is to provide federal agencies with a
52 for a laboratory to request an invoice while the security metric to use in validating cryptographic algorithm
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

implementations, and promote the use of validated sets of security requirements. For the CAVP, a validation
algorithms by industry and the public. The testing is carried system document is designed for each FIPS-approved
out by independent third-party laboratories accredited by or NIST-recommended cryptographic algorithm. See the
the National Voluntary Laboratory Accreditation Program website for a listing (see http://csrc.nist.gov/groups/STM/
(NVLAP), and the validations performed by the CAVP cavp/). The four Annexes to FIPS 140-2 reference the
program provide this metric. Federal agencies, industry, underlying cryptographic algorithm standards or methods.
and the public can choose validated implementations
By the end of 2016, the CAVP had issued approximately
of cryptographic algorithms from the CAVP Validated
23,559 validations, representing the algorithm validations of
Algorithms List and have confidence in the claimed level of
approximately 18 approved algorithms, including 5 modes of
security and assurance of correct implementation.
operation.
The validation of cryptographic algorithms by the
The CAVP issued approximately 4,000 algorithm
CAVP is a prerequisite to the validation of a cryptographic
validations in FY 2016, an increase of approximately 600
module by the CMVP and is also used by other programs
validations from the previous year. The increase in validations
outside of NIST as well. Since federal agencies are required
is attributed to an increase in cryptographic modules being
to use validated cryptographic modules for the protection of
validated and other outside programs now requiring CAVP
sensitive unclassified information, the validated modules and
validated implementations, e.g., the National Information
the validated algorithms that the modules contain represent
Assurance Partnership (NIAP).
the culmination and delivery of CSD’s cryptography-based
The number of algorithms submitted for validation
work to the end user.
continues to grow, representing significant growth in the
The CAVP validation program provides documented
number of validations expected to be available in the future.
methodologies for conformance testing through defined
53
Figure 18: CAVP Validation Status by Fiscal Year
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 19: CAVP Validation Status for FY 2016
54
Figure 20: CAVP Validated Implementation Actual Numbers
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

FOR MORE INFORMATION, SEE: that the implementation recognizes values that are not
allowed. The Monte Carlo Test is designed to exercise the
https://csrc.nist.gov/Projects/Cryptographic-Algorithm-
entire implementation-under-test (IUT). This test is designed
Validation-Program
to detect the presence of implementation flaws that are not
detected with the controlled input of the Known-Answer
CONTACT:
Tests. The types of implementation flaws detected by
Mr. Harold Booth this validation test include pointer problems, insufficient
(301) 975-8441 allocation of space, improper error handling, and incorrect
harold.booth@nist.gov behavior of the IUT. The Multi-Block Message Test (MMT)
is designed to test the ability of the implementation to
(Editors’ Note: Sharon Keller worked on this program until process multi-block messages, which requires the chaining
her recent retirement.) of information from one block to the next.
During the last few years, the CSD Cryptographic
Automated Security Testing and Technology Group (CTG) has expanded its publications
Test Suite Development to contain not only the algorithm’s specifications, but
also requirements for an algorithm’s use. Many of these
The CAVP utilizes the requirements and specifications
usage requirements do not fall within the scope of the
of the NIST standards (i.e., FIPS and Special Publications) to
CAVP, because the CAVP focuses on the correctness of
develop algorithm validation test suites and an automated
the instructions within the algorithm’s boundary. If these
security testing tool. The CAVP is responsible for providing
additional algorithm usage requirements are not considered
assurance that the cryptographic algorithm implementations
applicable to the algorithm’s implementation, they cannot
contained in cryptographic modules are implemented
be tested at the algorithm level by the CAVP, but may be
according to the specifications in the standards. The CAVP
tested by the CMVP if the requirements are considered
accomplishes this by designing and developing conformance
applicable to the cryptographic module. However, some of
testing specific to each cryptographic algorithm.
these usage requirements may be outside the scope of both
The conformance testing consists of a suite of validation the algorithm implementation and cryptographic module.
tests for each approved cryptographic algorithm. These In this latter case, the fulfillment of the requirements is the
validation tests exercise the algorithmic requirements responsibility of entities using, installing, or configuring
and mathematical formulas to assure that the detailed applications or protocols that use the cryptographic
specifications are implemented correctly and completely. algorithms. For example, depending on the design of a
If the implementer deviates from the specifications in the cryptographic module, it may not be possible for the module
standard or excludes any part of these specifications or to determine whether a specific key is used for multiple
requirements, the validation test will detect the deviations purposes, a situation that is strongly discouraged.
and fail. The validation testing will indicate that the algorithm
The CAVP currently has algorithm validation testing for
implementation does not function properly or is incomplete.
the following cryptographic algorithms:
The cryptographic algorithm validation tests designed
In the future, the CAVP expects to add algorithm
and developed by the CAVP are used by independent third-
validation testing for:
party laboratories accredited by NVLAP. The laboratory
works with vendors to validate their cryptographic • SP800-38G, Recommendation for Block Cipher
algorithm implementations. The suite of validation tests for Modes of Operation: Methods for Format-
each algorithm ensures the repeatability of tests and the Preserving Encryption;
equivalency of results across the testing laboratories. • SP 800-56C, Recommendation for Key Derivation
There are several types of validation tests, all designed through Extraction-then-Expansion, November
to satisfy the testing requirements of the cryptographic 2011;
algorithms and their specifications. These include, but are • SP 800-132, Recommendation for Password-
not limited to, Known-Answer Tests, Monte Carlo Tests, Based Key Derivation Part 1: Storage Applications,
and Multi-Block Message Tests. The Known-Answer Tests December 2010; and
are designed to examine the individual components of
• SP 800-56A Revision 2, Recommendation for Pair-
the algorithm by supplying known values to the variables
Wise Key Establishment Schemes Using Discrete
and verifying the expected result. Negative testing is also
55
Logarithm Cryptography, May 2013.
performed by supplying known incorrect values to assure
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

TABLE 1: CRYPTOGRAPHIC ALGORITHMS & NIST TECHNICAL DOCUMENTS (FIPS & SPS)
FEDERAL INFORMATION PROCESSING STANDARD
CRYPTOGRAPHIC ALGORITHM/COMPONENT (FIPS) OR SPECIAL PUBLICATION (SP) OR OTHER
REFERENCE DOCUMENT
SP 800-67, Recommendation for the Triple Data
Encryption Algorithm (TDEA) Block Cipher, and
Triple Data Encryption Standard (TDES)
SP 800-38A, Recommendation for Block Cipher Modes of
Operation–Methods and Techniques
FIPS 197, Advanced Encryption Standard, and
Advanced Encryption Standard (AES)
SP 800-38A, Recommendation for Block Cipher Modes of
Operation–Methods and Techniques
FIPS 186-2, Digital Signature Standard (DSS), with change
notice 1 and
Digital Signature Algorithm (DSA)
FIPS 186-4, Digital Signature Standard (DSS)
FIPS 186-2, Digital Signature Standard (DSS), with change
notice 1 and ANS X9.62 and
Elliptic Curve Digital Signature Algorithm (ECDSA)
FIPS 186-4, Digital Signature Standard (DSS), and ANS
X9.62
FIPS 186-4, Digital Signature Standard (DSS) and
RSA algorithm
ANS X9.31 and Public Key Cryptography Standards (PKCS)
#1 v2.1: RSA Cryptography Standard-2002
Hashing algorithms SHA-1, SHA-224, SHA-256, SHA-384,
FIPS 180-4, Secure Hash Standard (SHS)
SHA-512, SHA-512/224, SHA-512/256
Hashing algorithms SHA3-224, SHA3-256, SHA3-384, FIPS 202, SHA-3 Standard: Permutation-Based Hash and
SHA3-512 Extendable-Output Functions, August 2015
SHA-3 Extendable-Output Functions (XOFs) SHAKE128, FIPS 202, SHA-3 Standard: Permutation-Based Hash and
SHAKE256 Extendable-Output Functions, August 2015
Random number generator (RNG) algorithms FIPS 186-2 Appendix 3.1 and 3.2; ANS X9.62 Appendix A.4
SP 800-90A, Recommendation for Random Number
Deterministic Random Bit Generators (DRBG)
Generation Using Deterministic Random Bit Generators
Keyed-Hash Message Authentication Code (HMAC) using FIPS 198-1, The Keyed-Hash Message Authentication Code
SHA-1, SHA-2 and SHA-3 (HMAC)
Cipher-based Message Authentication Code (CMAC) Mode SP 800-38B, Recommendation for Block Cipher Modes of
for Authentication Operation: The CMAC Mode for Authentication
SP 800-38C, Recommendation for Block Cipher Modes
Counter with Cipher Block Chaining-Message
of Operation: the CCM Mode for Authentication and
Authentication Code (CCM) Mode
Confidentiality
GCM, Galois Message Authentication Code (GMAC), and SP 800-38D, Recommendation for Block Cipher Modes of
eXtended Packet Number (XPN) Modes Operation: Galois/Counter Mode (GCM) and GMAC
SP 800-38E, Recommendation for Block Cipher Modes
XTS-AES Mode of Operation: The XTS-AES Mode for Confidentiality on
Block-Oriented Storage Devices
56
Table 1: Cryptographic Algorithms & NIST Technical Documents (FIPS & SPs)
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

TABLE 1 (CONT.): CRYPTOGRAPHIC ALGORITHMS & NIST TECHNICAL DOCUMENTS
(FIPS & SPS)
FEDERAL INFORMATION PROCESSING STANDARD
CRYPTOGRAPHIC ALGORITHM/COMPONENT (FIPS) OR SPECIAL PUBLICATION (SP) OR OTHER
REFERENCE DOCUMENT
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
SP 800-56A, Section 5.7.1.2 Elliptic Curve Cryptography
SP 800-56A Section 5.7.1.2 ECC CDH function
Cofactor Diffie-Hellman (ECC CDH) Primitive Testing
SP 800-108, Recommendation for Key Derivation using
Key-Based Key Derivation functions (KBKDF)
Pseudorandom Functions
Application-Specific Key Derivation functions (ASKDF)
SP 800-135 (Revision 1) Recommendation for Existing
(includes the KDFs used by IKEv1, IKEv2, TLS, ANS X9.63-
Application-Specific key Derivation Functions
2001, SSH, SRTP, SNMP, and TPM)
Component test – ECDSA Signature Generation of a hash
value (This component test verifies the signing of a hash- FIPS 186-4, Digital Signature Standard (DSS), and ANS
sized input. It does not verify the hashing of the original X9.62
message to be signed.)
Component test – RSA PKCS#1 1.5 Signature Generation of
FIPS 186-4, Digital Signature Standard (DSS), and
encoded message (EM) (This component test verifies the
Public Key Cryptography Standards (PKCS) #1 v2.1: RSA
signing of an EM. It does not verify the formatting of the
Cryptography Standard-2002
EM.)
Component test – RSA PKCS#1 PSS Signature Generation SP 800-56B, Recommendation for Pair-Wise Key
of encoded message EM (This component test verifies the Establishment Schemes Using Integer Factorization
RSASP1 function.) Cryptography, August 2009, Section 7.1.2
FOR MORE INFORMATION, SEE: Security Content Automation
Protocol (SCAP) Validation
https://csrc.nist.gov/Projects/Cryptographic-Algorithm-
Program
Validation-Program
The SCAP Validation Program performs conformance
CONTACTS:
testing to ensure that products correctly implement
SCAP, as defined in SP 800-126 Revision 2, The Technical
Mr. Harold Booth Ms. Elaine Barker
Specification for the Security Content Automation Protocol
(301) 975-8441 (301) 975-2911
(SCAP): SCAP Version 1.2. Conformance testing is necessary
harold.booth@nist.gov elaine.barker@nist.gov
because SCAP is a complex collection of eleven individual
(Editors’ Note: Sharon Keller worked on this program until specifications that work together to support various use
her recent retirement.) cases. A single error in product implementation could result
in undetected vulnerabilities or policy noncompliance within
an organization’s networks.
The test requirements for SCAP 1.2 are defined in NISTIR
7511, Security Content Automation Protocol (SCAP) Version 57
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 21: SCAP 1.2 Validation Process
1.2 Validation Program Test Requirements. In general, vendors Questions (FAQ), the SCAP validation-test content, and
may opt for product validation for one or more SCAP tools for validating and processing SCAP data streams. The
capabilities or operating systems. Currently, the program SCAP validation-test content should be used by vendors
offers testing on Microsoft Windows and Red Hat Enterprise for quality assurance testing prior to entering formal SCAP
Linux platforms. The validation process starts when a vendor testing with an NVLAP-accredited laboratory. The open-
voluntarily submits an SCAP-enabled product to an NVLAP- source tools that are available for download may be used by
accredited laboratory. Once the lab completes product SCAP content authors for testing the SCAP source content.
testing, the lab submits a test report to the SCAP Validation The SCAP Content Validation Tool (SCAPVal) may be used to
Program at NIST for review. NIST reviews the test report and determine if the content conforms to the SCAP specification.
awards a validation if all requirements have been met. Once Open-source SCAP reference implementation tools, such as
a validation is awarded, the SCAP Validation Record is sent the SCAP Reference Implementation Tool, may be used to
to the lab, and the information about the newly validated process SCAP data streams.
product is posted on the SCAP Validated Products web page.
End users may use information on the SCAP Validation
Figure 21: SCAP 1.2 Validation Process illustrates the SCAP 1.2
web page to learn about SCAP validation and find products
Validation Process.
that have been awarded validations. The validation records
All resources and information necessary for preparing that are posted on the SCAP Validated Products page identify
products for SCAP 1.2 validation are published on the SCAP the product versions that were tested in the laboratory,
Validation Program web pages (see the url below). The most along with details about each validation, such as the tested
current NISTIR 7511 revision, as well as SCAP capabilities platforms, SCAP capabilities, the validation test suite version,
and supported platforms, are available on the home and the lab that performed the product test.
page (see http://scap.nist.gov/validation). The resources
In FY 2016, several products successfully completed
58 page includes documentation, a list of Frequently Asked
testing and were awarded validations, bringing the total
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

number of SCAP 1.2-validated products to fifteen. Most The interface specifications for the PIV Smart Card
vendors of configuration scanning products are SCAP Application and PIV Middleware are found in a FIPS 201
validated, and vendors continually pursue validation for new companion document, namely, SP 800-73-4, Interfaces for
platforms, capabilities, and versions of SCAP. The current Personal Identity Verification. The conformance tests for
list of SCAP 1.2-validated products may be found on the these specifications are detailed in SP 800-85A-4, PIV Card
SCAP Validated Products list at https://nvd.nist.gov/scap/ Application and Middleware Interface Test Guidelines. To
validated-tools. implement these tests and to generate conformance test
reports, CSD also developed and maintains an integrated
In FY 2017, NISTIR 7511 will be updated, adding
toolkit called the “PIV Interface Test Runner,” which
requirements to test products for conformance to
conducts tests on both PIV Smart Card Applications and PIV
SCAP 1.3. New capabilities include testing the ability of
Middleware products. This toolkit is provided to accredited
products to process the most recent Open Vulnerability
NPIVP test facilities for product testing and to the general
and Assessment Language (OVAL) versions and to read
public as open source software.
Software Identification (SWID) tags. The modular structure
of the SCAP Validation Program supports the addition The NPIVP team is also closely involved in activities
of these new test requirements, as well as new platforms related to the revision of specifications of the PIV companion
and capabilities, without needing to re-design the entire documents, such as SP 800-73, SP 800-76, Biometric
program. Vendors benefit from the modular structure by Specifications for Personal Identity Verification, and SP 800-
choosing the capabilities and platforms that satisfy the 78, Cryptographic Algorithms and Key Sizes for Personal
needs of their customers. Identity Verification. This ensures that specification revisions
in the PIV documents are fully reflected in the conformance
FOR MORE INFORMATION, SEE:
test documents, SP 800-85A-4 and SP 800-85B (PIV
http://scap.nist.gov/validation Data Model Conformance Test Guidelines) as well as in
the “PIV Interface Test Runner” toolkit. The changes to PIV
CONTACT: specifications in PIV companion documents necessitated
that NPIVP make a major update to the conformance
Ms. Melanie Cook
test documents and consequently to the “PIV Interface
(301) 975-5259
Test Runner” toolkit in 2016. The updated Test Runner is
melanie.cook@nist.gov
available at http://csrc.nist.gov/groups/SNS/piv/npivp/sw-
downloads.html.
The NPIVP team also maintains the Validation List for
IDENTITY AND ACCESS
PIV Smart Card Application and the PIV Middleware products
MANAGEMENT
that are PIV-conformant implementations. Updates to the
PIV Smart Card Application validation list were necessary
in 2016 to comply with the sunset date for some Random
NIST Personal Identity
Number Generators (RNGs), as outlined in SP 800-131A,
Verification Program (NPIVP)
Recommendation for Transitioning the Use of Cryptographic
The objective of the NIST Personal Identity Algorithms and Key Lengths. More information about the
Verification Program (NPIVP) is to validate PIV components sunset can be found at http://csrc.nist.gov/groups/SNS/piv/
for conformance to the specifications in FIPS 201, Personal npivp/announcements.html.
Identity Verification (PIV) of Federal Employees and
In FY 2017, the NPIVP team will continue to fine-tune its
Contractors, and its companion documents (detailed below).
toolkit and perform acceptance testing for PIV Smart Card
The two PIV components that come under the scope of NPIVP
Applications and PIV Middleware.
are the PIV Smart Card Application and the PIV Middleware.
NPIVP test facilities that perform conformance tests for FOR MORE INFORMATION, SEE:
these two components are Cryptographic and Security
https://csrc.nist.gov/Projects/NIST-Personal-Identity-
Testing (CST) Laboratories accredited by the NVLAP. As of
Verification-Program
September 2016, there were seven such facilities (see http://
csrc.nist.gov/groups/SNS/piv/npivp/testing_facilities.html).
CONTACTS:
Dr. Ramaswamy Chandramouli Ms. Hildegard Ferraiolo
59
(301) 975-5013 (301) 975-6972
mouli@nist.gov hildegard.ferraiolo@nist.gov
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Personal Identity Verification • Published SP 800-156, Representation of PIV Chain-
(PIV) and FIPS 201 Revision of-Trust for Import and Export. This document
provides the data representation of a chain-of-trust
Efforts
record for the exchange of records between issuers.
The exchanged record can be used by an agency to
personalize a PIV Card for a transferred employee,
or by a service provider to personalize a PIV Card
on behalf of client federal agencies. The data
representation is based on a common XML schema
to facilitate interoperable information sharing
and data exchange. The document also provides
support for data integrity through digital signatures
and confidentiality through encryption of chain-of-
trust data in transit and at rest.
• Published a white paper, Best Practices for
Privileged User PIV Authentication, in response
to OMB’s 30-day Cybersecurity Sprint effort
and subsequent OMB Memorandum M-16-04,
Cybersecurity Strategy and Implementation Plan
(CSIP) for the Federal Civilian Government, which
Figure 22: Government Employees Use PIV Cards for
requires federal agencies to use PIV credentials for
Facility Access
authenticating privileged users. The white paper
outlines the risks of password-based single-factor
In response to Homeland Security Presidential
authentication, and describes best practices for the
Directive-12 (HSPD-12), Policy for a Common Identification
use of multi-factor PIV-based user authentication
Standard for Federal Employees and Contractors, FIPS 201,
for privileged users.
Personal Identity Verification (PIV) of Federal Employees
and Contractors, was developed and was approved by the • Published SP 800-166, Derived PIV Application and
Secretary of Commerce in February 2005. HSPD-12 called for Data Model Test Guidelines. SP 800-166 contains
the creation of a new identity credential for federal employees the derived test requirements and test assertions
and contractors. FIPS 201 is the technical specification for for testing the Derived PIV Application and
both the PIV identity credential and the PIV system that associated Derived PIV data objects residing on a
produces, manages, and uses the credential. Within NIST’s mobile device. The tests verify the conformance of
Information Technology Laboratory (ITL), this work is a these artifacts to the technical specifications of SP
collaborative effort of the CSD and the Information Access 800-157, Guidelines for Derived Personal Identity
Division (IAD). CSD activities in FY 2016 directly supported Verification (PIV) Credentials. SP 800-157 specifies
the latest revision of FIPS 201 (i.e., FIPS 201-2) by updating standards-based, secure, reliable, interoperable
the relevant publications associated with FIPS 201-2 and by public-key infrastructure (PKI)-based identity
developing several new publications. CSD performed the credentials. SP 800-166 is targeted at vendors
following activities during FY 2016 in support of HSPD-12: of Derived PIV Applications, issuers of Derived
PIV Credentials, and entities that will conduct
• Published Draft SP 800-116 Revision 1, A
conformance tests on these applications and
Recommendation for the Use of PIV Credentials
credentials.
in Physical Access Control Systems (PACS). This
document provides best practice guidelines • Published SP 800-85A-4, PIV Card Application and
for integrating the PIV Card with the PACS that Middleware Interface Test Guidelines (SP 800-73-4
authenticate the PIV cardholders in federal facilities. Compliance), to align the testing requirements with
The document recommends a risk-based approach FIPS 2012, SP 800-73-4, and SP 800-78-4.
for selecting appropriate PIV authentication
mechanisms to manage physical access to Federal In FY 2017, CSD will continue to focus on updating
Government facilities and assets. relevant publications associated with FIPS 201-2, including
60
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

finalizing SP 800-116 Revision 1. CSD will also continue to In addition, market forces have resulted in an inflexion
provide technical and strategic inputs to the PIV-related point in how departments and agencies authenticate users.
initiatives. NIST and the private-sector partners have observed that
some public and private-sector identity assurance standards
FOR MORE INFORMATION, SEE:
have become outdated or have simply not been adopted.
http://csrc.nist.gov/groups/SNS/piv/ Specifically, SP 800-63 was originally written to address an
online world that is much different than today. Innovation
CONTACTS: has offered new perspectives in how trusted identities can
be established. Practical implementations of SP 800-63
Ms. Hildegard Ferraiolo Dr. David Cooper
have informed us of areas of strengths, weaknesses, and
(301) 975-6972 (301) 975-3194
techniques not utilized by federal agencies or the private
hildegard.ferraiolo@nist.gov david.cooper@nist.gov
sector. Note that our online adversaries are targeting user
Dr. Ramaswamy Chandramouli names and passwords as the simplest point of entry to gain
(301) 975-5013 unauthorized access to sensitive systems and data.
mouli@nist.gov
Authentication
To support Office of Management and Budget
(OMB) requirements, CSD developed SP 800-63, Electronic
Authentication Guideline. OMB defines four levels of
assurance that a federal agency must select, based on a risk
assessment to determine the impact of an authentication
failure. This guideline covers remote authentication of users
(such as private individuals) interacting with government IT
systems over the Internet. It defines technical requirements
for each of the four levels of assurance in the areas of identity
proofing, authenticators, credential binding, management
processes, authentication protocols and federation. The
newest revision underway in 2016 establishes three individual Figure 23: New SP 800-63-3 Structure
assurance categories that can map into the original OMB
levels of assurance. The categories are:
CSD, in collaboration with the ACD Trusted Identities
• Identity Assurance Level - the robustness of the
Group, hosted the two-day workshop “Applying
identity proofing process and the binding between
Measurement Science in the Identity Ecosystem” in January
an authenticator and the records pertaining to a
2016. NIST gathered critical feedback from over 200 industry,
specific individual;
academic, and public-sector stakeholders regarding new
• Authentication Assurance Level - the robustness directions that NIST should take in authentication guidance
of the authentication process itself; and, and in methods for measuring the strength of relevant
• Federation Assurance Level - the robustness technologies and processes. The workshop culminated in
of the assertion protocol utilized by a federation the release of NISTIR 8103, Advanced Identity Workshop on
to communicate authentication and attribute Applying Measurement Science in the Identity Ecosystem:
information (if applicable) to a relying party. Summary and Next Steps.
Since the initial release of SP 800-63, CSD has released In May 2016, ITL released a public preview draft of NIST
two revisions to address changes in modern technology and SP 800-63-3, with an updated name, Digital Authentication
lessons learned from practical implementations by federal Guideline. This body of work represents a significant departure
departments and agencies. from prior versions of the special publication. The guideline
has been divided into a family of standalone documents that
focus on outcomes and innovation where possible, rather
than prescriptive processes and technologies (see Figure
23). A significant number of requirements were updated 61
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

or removed, with many new requirements introduced, CONTACT:
including increased allowances for the use of biometrics in
authentication systems. SP 800-63-3, while required for Mr. Paul Grassi
federal agencies, suggests requirements for solutions often (703) 786-8275
provided by the private sector; hence, many updates were paul.grassi@nist.gov
garnered from innovation in the market, workshop feedback,
and a dialog with all sectors while the guideline was open
Access Control and Privilege
for comment. CSD and ACD also piloted a new approach
Management
to managing stakeholder feedback and document updates.
During the development of the SP 800-63 revision, drafts With the advance of current computing technologies
of the documents were made available on GitHub, an online and the diverse environments in which they are used,
version management and collaboration tool that allowed us access control issues, such as situational awareness, trust
to openly discuss comments in real time and accept edits management, the preservation of privacy, and privilege-
directly into the document from ITL stakeholders. This was management systems, are becoming increasingly complex.
the first time that an 800 series draft Special Publication was Practical and conceptual guidance for these topics is needed.
published on GitHub; the use of GitHub proved successful In FY 2016, the following activities were accomplished
and will continue to be used to manage SP 800-63-3 as the for this project:
document transitions from public preview to final version.
• Researched the requirement and capabilities
In FY 2017, CSD will publish the final SP 800-63-3 for Access Control (AC) policy composing and
revision, giving agencies an increased set of secure, privacy- verification technology;
enhancing, and user-friendly options to deliver safe digital
• Studied attribute considerations for access
services to their constituents. The final version may also serve
mechanism implementation; the results are
as a foundation for future authentication shared services
presented in the internal draft of a NIST SP,
that the government will offer, such as those directed by the
Attribute Consideration for Access Control Systems
Cybersecurity National Action Plan (CNAP).
(no publication number has been assigned to this
Work on 800-63-3 will continue after the document internal draft SP), which is scheduled to be released
becomes final. ITL will work on identifying ways to measure during FY 2017);
authentication systems in a more systematic and scientific
• Researched the AC requirements and functions for
way, allowing NIST to specify additional metrics that would
distributed systems, including Big Data, Cloud, IoT,
be required in future authentication systems, based on risk.
and the Smart Grid; and
Work on biometric authentication will capitalize on the
opportunity to enhance the authentication performance and • Published NIST SP 800-178, A Comparison of
security of a range of modalities (e.g., fingerprint, voice, or Attribute Based Access Control (ABAC) Standards
iris recognition). NIST will explore the inclusion of additional for Data Services, and worked on two internal draft
industry best practices into future revisions of SP 800-63-3. NIST SPs: 1) Draft SP 800-192: Verification and Test
NIST will also research methods to ensure that practices align Methods for Access Control Polices/Models, and
with the security and privacy demands of digital services 2) Draft SP (no number yet assigned), Attribute
offered by government. In addition to the topics described Consideration for Access Control Systems; both
above, the team will research approaches that harmonize SPs are related to access control and privilege
U.S. Government requirements on an international scale, management.
promoting easy-to-implement cross-border trusted identity
In FY 2017, CSD will continue the above research. CSD
solutions. This helps avoid challenges that result from
expects that this project will:
disparate, nationally unique authentication guidelines that
• Promote (or accelerate) the adoption of community
may disrupt international interoperability.
computing that utilizes the power of shared
FOR MORE INFORMATION, SEE: resources and common trust-management
schemes;
http://csrc.nist.gov/groups/ST/eauthentication/
• Provide guidance for implementing access control
https://pages.nist.gov/800-63-3 models and mechanisms for standalone or network
systems;
62
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

• Increase the security and safety of static misconfigurations, or flaws in software implementation can
(connected) distributed systems by applying the result in serious vulnerabilities. The specification of access
testing and verification tool for the AC policies; control policies is often a challenging problem. Often, a
system’s privacy and security are compromised due to
• Assist system architects, security administrators,
the misconfiguration of access control policies, instead of
and security managers whose expertise is related
the failure of cryptographic primitives or protocols. This
to access control or privilege policy in managing
problem becomes increasingly severe as software systems
their systems and in learning the limitations and
become more and more complex, and are deployed to
practical approaches for their applications; and
manage a large amount of sensitive information and
• Provide accurate and efficient fault detection and
resources that are organized into sophisticated structures.
correction technology for implementing AC rules
Identifying discrepancies between policy specifications and
and policies.
their properties (their intended function) is crucial because
Figure 24 (below) illustrates the application of access the correct implementation and enforcement of policies
control and privilege management within and among by applications is based on the premise that the policy
organizations. specifications are correct. As a result, policy specifications
must undergo rigorous verification and validation through
CONTACTS:
systematic testing to ensure that the policy specifications
Dr. Vincent Hu Mr. David Ferraiolo truly encapsulate the desires of the policy authors.
(301) 975-4975 (301) 975-3046
To formally and precisely capture the security properties
vhu@nist.gov david.ferraiolo@nist.gov
that AC should adhere to, access control models are usually
written to bridge the rather wide gap in abstraction between
Mr. Rick Kuhn
policy and mechanism. Thus, an access control model
(301) 975-3337
provides unambiguous and precise expression as well as
kuhn@nist.gov
a reference for the design and implementation of security
requirements. Techniques are required for verifying whether
Conformance Verification for an access control model is correctly expressed in the access
Access Control Policies control policies, and whether the properties are satisfied in
the model.
Access control (AC) systems are among the most
critical network security components. Faulty policies,
63
Figure 24: Access Control and Privilege Management
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
https://dx.doi.org/10.6028/NIST.SP.800-195

Most research on AC model or policy verification rather than checking by retracing the interrelations between
techniques is focused on one particular model, and almost rules after the policy is completed.
all of the research is in applied methods, which require
In FY 2016, CSD accomplished the following:
the completed AC policies as the input for the verification
• Funded and supported two Small Business
or test processes to generate fault reports. Even though
Innovation Research (SBIR) Phase II projects for
correct verification is achieved, and counter-examples may
access control tool developments;
be generated when faults are found, those methods provide
no information about the source of faults that might allow • Enhanced the usability and fixed bugs of the
conflicts in privilege assignment, the leakage of privileges, or ACRLCS (the Access Control Rule Logic Circuit
a conflict-of-interest in permissions. The difficulty in finding Simulation System) to provide more capability for
the source of faults is increased, especially when the AC policy fault detection;
rules are intricately covering duplicated variables to a degree
• Published a conference paper: General Methods for
of complexity. The complexity is because a fault might not
Access Control Policy Verification, and an article:
be caused by one particular access rule. Thus, it requires
Access Control Policy Verification for policy test
manually analyzing each rule in the policy to find the correct
case generation;
solution for correcting the fault.
• Worked with industrial and academic organizations
To address the issue, CSD developed the Access Control
in exploring new capabilities that helped to
Property Tool (ACPT), shown in Figure 25, which allows a user
improve the usability of the AC tools (ACPT and
to compose, verify, test, and generate access control policies.
ACRLCS), resulting in additional usage; ACPT
CSD also researched the AC Rule Logic Circuit Simulation
was downloaded by 405 users and organizations;
(ACRLCS) technique, which enables the AC authors to detect
and
a fault when the fault-causing AC rule is added to the policy,
• Enhanced the capability of ACPT by adding an
so the fix can be implemented in real time before adding
object inheritance capability for basic access
other rules that further complicate the detecting effort,
control models.
64
Figure 25: Access Control Property Tool (ACPT)
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

In FY 2017, CSD is planning to conduct further research  Attribute-Based Access Control
| on  efficient  | testing  technology,  | new  capabilities,  | and  |     |                  |     |         |          |         |     |             |
| -------------- | --------------------- | ------------------- | ---- | --- | ---------------- | --- | ------- | -------- | ------- | --- | ----------- |
|                |                       |                     |      |     | Attribute-Based  |     | Access  | Control  | (ABAC)  | is  | a  logical  |
enhance the performance of the ACPT and ACRLCS.
|     |     |     |     | access  | control  | methodology  |     | where  | an  | authorization  | to  |
| --- | --- | --- | --- | ------- | -------- | ------------ | --- | ------ | --- | -------------- | --- |
Figure  25  (See  previous  page)  shows  the  system  perform a set of operations is determined by evaluating the
architecture of the NIST Access Control Policy Tool (ACPT),  attributes associated with the subject, object, requested
which allows access control policy authors to compose,  operations, and, in some cases, environmental conditions
verify, and test access control policy implementation.
|     |     |     |     | against    | policy,     | rules,  | or   | relationships  | that  | describe         | the  |
| --- | --- | --- | --- | ---------- | ----------- | ------- | ---- | -------------- | ----- | ---------------- | ---- |
|     |     |     |     | allowable  | operations  |         | for  | a  given       | set   | of  attributes.  | For  |
This project is expected to:
example, access to a database could be restricted to users
•   Provide a generic paradigm and framework of
with particular attributes, such as membership in a group
access control model/property conformance
(e.g., employees) and other conditions (e.g., part of the
testing;
Human Resource Department). ABAC represents a point on
•   Provide templates for specifying access control  the spectrum of logical access control, from simple access
rules in popular access control models, such as  control lists to more capable role-based access (RBAC), and
the Attribute Based, Multilevel, and Workflow  finally, to a highly flexible method for providing access based
| models; |     |     |     | on the evaluation of attributes. |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
•   Provide tools or services for checking the security
CSD is conducting research that provides information
and safety of an access control implementation,  for  using  ABAC  to  improve  information  sharing  within
policy combination, and eXtensible Access Control  and among organizations based on the planning, design,
Markup Language (XACML) policy generation; implementation,  and  operational  considerations.  The
|     |     |     |     | research  | also  | includes  | technologies  |     | such  | as  | attribute  |
| --- | --- | --- | --- | --------- | ----- | --------- | ------------- | --- | ----- | --- | ---------- |
•   Promote (or accelerate) the adoption of
combinatorial testing for large-system testing  assurance,  attribute  engineering/management,  identity
|     |     |     |     | system  | integration,  |     | attribute  |     | federation,  |     | situational  |
| --- | --- | --- | --- | ------- | ------------- | --- | ---------- | --- | ------------ | --- | ------------ |
(such as an access control system);
|     |     |     |     | awareness  |     | (real-time  | or  contextual)  |     | mechanisms,  |     | policy  |
| --- | --- | --- | --- | ---------- | --- | ----------- | ---------------- | --- | ------------ | --- | ------- |
•   Promote the concept of detecting AC policy faults
|     |     |     |     | management,  |     | and  | natural-language  |     | policy  |     | translation  |
| --- | --- | --- | --- | ------------ | --- | ---- | ----------------- | --- | ------- | --- | ------------ |
in real-time AC rule composing;
to digital policy. Figure 26 (See next page) illustrates the
•   Provide an innovative method for specifying
interaction of many of these components. The goal of this
AC rules formed by Boolean logic expressions  research is to improve information sharing, while maintaining
operated on variables of AC rules; control of that information for federal agencies.
•   Provide techniques for preventing faults in  In FY 2016, the project team:
enforcing fundamental security properties,
|     |     |     |     |     | •	  | Worked on the book Attribute-Based Access  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
including Cyclic Inheritance, Privilege Escalation,
Control – Models & Deployments; publishing is
and Separation of Duty; and
planned for March 2017 by Artech House;
•   Provide new methods for composing standard
Published NIST Special Publication 800-178, A
•
mandatory AC models, such as Attribute-Based
Comparison of Attribute Based Access Control
Access Control (ABAC) and Multi-Level Security
(ABAC) Standards for Data Service Applications
(MLS) as well as some fundamental security
document; and
properties.
|     |     |     |     |     | •	  | Continued  | research,  |     | in  partnership  |     | with  the  |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---------------- | --- | ---------- |
FOR MORE INFORMATION, SEE:
Trusted Identities Group (TIG) and the National
Cybersecurity Center of Excellence (NCCoE),
http://csrc.nist.gov/groups/SNS/acpt/
on the attribute assurance of ABAC.
CONTACTS:
In FY 2017, CSD will continue the research of ABAC
formal models, as well as details and extended topics of
| Dr. Vincent Hu  |   Mr. Rick Kuhn  |     |     |     |     |     |     |     |     |     |     |
| --------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ABAC capabilities, such as attribute considerations, ABAC
| (301) 975-4975  |   (301) 975-3337  |     |     |     |     |     |     |     |     |     |     |
| --------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
implementation examples, ABAC mechanisms, and ABAC
| vhu@nist.gov   |   kuhn@nist.gov |     |     |             |     |            |          |       |         |      |            |
| -------------- | --------------- | --- | --- | ----------- | --- | ---------- | -------- | ----- | ------- | ---- | ---------- |
|                |                 |     |     | standards.  |     | The  ABAC  | project  | will  | pursue  | the  | following  |
objectives:
65
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 26: ABAC Access Control Mechanism Chart
• Provide readers with an overview of the current FOR MORE INFORMATION, SEE:
state of logical access control, a working definition
http://csrc.nist.gov/projects/abac/
of ABAC, and an explanation of the core and
enterprise ABAC concepts;
CONTACTS:
• Assist security policy makers in establishing a
Dr. Vincent Hu Mr. David Ferraiolo
business case for ABAC implementation and
(301) 975-4975 (301) 975-3046
acquiring an interoperable set of capabilities;
vhu@nist.gov david.ferraiolo@nist.gov
• Assist ABAC developers in developing the
operational requirements and overall enterprise Mr. Rick Kuhn
architecture; (301) 975-3337
kuhn@nist.gov
• Assist ABAC administrators in establishing or
refining business processes to support ABAC;
• Promote the adoption of ABAC for a more secure Trusted Identities Group (TIG)
and flexible method for information sharing in a
ACD’s Trusted Identities Group (TIG) is tasked with
standalone or enterprise environment; and
improving online identity for individuals and organizations
• Provide testing methods for ABAC policy and so they can employ solutions to access online services in
66 implementations. a manner that promotes confidence, privacy, choice, and
innovation (see http://www.nist.gov/itl/tig). The TIG focuses
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

on outcomes that meet the four guiding principles that
identity solutions be privacy-enhancing and voluntary,
secure and resilient, interoperable, cost-effective and easy
to use.
Figure 27: NIST employs four primary tactics:
Through the promotion of government and commercial
partnerships, publications, market intelligence, and
adoption of privacy-enhancing, secure, interoperable,
communications
and easy-to-use identity solutions, the TIG drives trust,
convenience, and innovation in digital identity.
Identity Ecosystem Framework. The privately-
led Identity Ecosystem Steering Group (IDESG) laid the
The TIG is a partnership model that supports the private
groundwork for better digital identity transactions with
sector, advances risk management practices, develops
the release of the Identity Ecosystem Framework (IDEF) in
and revises guidance and standards to be co-developed
early FY 2016. The IDEF lays a foundation for the Identity
with private and public stakeholders, assists agencies in
Ecosystem by providing a baseline set of requirements that
the implementation of identity solutions in their systems,
define how to execute transactions involving digital identity
promotes international interoperability of identity standards
that puts users at the center by aligning with the four
and solutions, and funds innovative projects through pilots
guiding principles, continually improving online commerce,
and other funding mechanisms.
the efficiency of digital services, and online interactions
To achieve these ends, the TIG is working to advance
(see http://www.idesg.org/News-Events/Press-Releases/
measurement science, technology, and standards adoption
ID/74/Identity-Ecosystem-Framework-Released-Creating-
in digital identity by focusing on four primary tactics:
Unprecedented-Rules-of-the-Road-for-Online-Identity).
partnerships, publications, market intelligence, and
Strategic partners. The TIG works alongside many
communications.
professional organizations, agencies, and entities in the
identity community on a daily basis. Their partnerships allow
Partnerships
them to gain stronger insights, evolve their thinking and
External Projects. The TIG funds external projects, ideas, create more robust publications, orchestrate successful
including a pilot program that impacted more than 6.7 events, participate in speaking engagements across the
million individuals in its first four years. These projects aim country, bring in outside experts to review TIG federal funding
to catalyze the marketplace to begin developing solutions opportunities, and allow for a broader reach of messaging
aligned with the guiding principles. The marketplace and announcements. Under this model, the TIG works to co-
is currently transitioning from broad market issues to develop NIST publications, creating an increasingly inclusive
targeting specific gaps and market impediments as the approach to producing the best possible documents. The
identity ecosystem matures. The pilots develop and TIG also works directly with agencies on their solutions to
deploy technology, models, and frameworks that wouldn’t provide expert advice in the risk management of identity
otherwise exist in the marketplace. In FY 2016, the pilot solutions and the implementation of those solutions.
programs made remarkable progress; the 24 projects include
Several publications were released in 2016 (many
more than 170 partner organizations across 12 sectors—
through the use of GitHub, to best ensure that the broad
including the development or deployment of 14 multi-factor
community can stay involved in their efforts and that they
authentication solutions. Over the course of the fiscal year,
are transparent and informative every step of the way).
six new pilots were launched (including five supporting state
Details are provided below; the list is current as of the end
services and one driving federated identity in healthcare)
of FY 2016. The updated publications list can be found on
(See https://www.nist.gov/itl/tig/pilot-projects).
the TIG resources page (see https://www.nist.gov/itl/tig/
resources).
67
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

• Draft SP 800-63-3: Digital Authentication Guideline Communications
(see https://pages.nist.gov/800-63-3/)
The TIG also leverages external communications to
• Draft NISTIR 8149: Developing Trust Frameworks to inform the public about its work and engage a variety of
Support Identity Federation (see https://pages.nist. audiences to collaborate on projects as well as to align
gov/NISTIR-8149/) efforts and maximize the impact of NIST’s investment in
• Publications that apply measurement science in the cybersecurity initiatives. The TIG works with government and
Identity Ecosystem: industry groups to raise public awareness of cybersecurity
tools and concepts, such as by collaborating with the
NISTIR 8103: Advanced Identity Workshop on
o National Cybersecurity Alliance on campaigns, including
Applying Measurement Science in the Identity
Lock Down Your Login, National Cybersecurity Awareness
Ecosystem: Summary and Next Steps (see
Month, and Data Privacy Day. The TIG also regularly shares
http://nvlpubs.nist.gov/nistpubs/ir/2016/NIST.
achievements and announcements via published documents,
IR.8103.pdf)
speaking engagements all over the country, webinars, their
Strength of authentication: website and blog, social media engagement and outreach,
o
and customized events for stakeholders. For instance, in FY
 Discussion Draft: Strength of Function
2016, the TIG coordinated the Advanced Identity Workshop,
for Authenticators – Biometrics (see
which brought together over 200 technology vendors,
https://pages.nist.gov/SOFA/)
cybersecurity researchers, policy makers, and other experts
 Discussion Draft: Measuring Strength of
from the public and commercial sectors.
Authentication (see https://www.nist.
In FY 2017, the TIG will continue to work to advance
gov/sites/default/files/nstic-strength-
measurement science, technology, and standards adoption
authentication-discussion-draft.pdf)
in identity management and focus on their four primary
Attribute metadata and confidence scoring:
o tactics of partnerships, publications, market intelligence,
 Draft NISTIR 8112: Attribute Metadata and communications. The TIG plans to also move on to new
(see https://pages.nist.gov/ endeavors, such as:
NISTIR-8112/)
• The identification of opportunities and
 Discussion Draft: Attribute Metadata mechanisms to complement the work of their pilot
and Confidence Scoring (see https:// programs;
www.nist.gov/sites/default/files/
• Increased work alongside federal agencies to
nstic-attribute-confidence-metadata-
address specific identity challenges through the
discussion-draft.pdf)
NCCoE;
Strength of identity proofing:
o • New research projects;
 Discussion Draft: Measuring Strength of
• Additional standards work;
Identity Proofing (see https://www.nist.
• Increased communication efforts to educate
gov/sites/default/files/nstic-strength-
audiences of all types;
identity-proofing-discussion-draft.pdf)
• Continued engagement with various NIST programs
Market Intelligence to further integrate the Identity Ecosystem into
NIST cybersecurity efforts; and,
The TIG is continuously identifying, collecting, and
analyzing metrics to gain greater insight into the development • Continued focus on industry engagement.
and adoption of TIG-aligned solutions. This work aids NIST
FOR MORE INFORMATION, SEE:
in measuring the market shift toward these solutions and
honing efforts moving forward so NIST most effectively uses https://www.nist.gov/itl/tig
program resources. This increases the likelihood that, with
CONTACTS:
each new initiative, the TIG meets the market—rather than
expecting the market to meet them.
Dr. Mike Garcia Ms. Kristina Rigopoulos
(202) 494-4122 (202) 309-4791
michael.garcia@nist.gov kristina.rigopoulos@nist.gov
68
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

RESEARCH IN EMERGING detect or prevent security flaws while still supporting the
TECHNOLOGIES quick-paced software development of applications with
rich feature sets. Through the demonstration of security-
flaw avoidance in a time-constrained setting, CSD would
Secure Development Toolchain seek to show that wide-scale improvements in the overall
Competitions security of software products could be realized without
sacrificing a time-to-market goal. The competitions, which
Many security weaknesses in federal information
would be open to all interested parties, would aim to provide
systems stem from software security vulnerabilities induced
consistent application and measurement of commercial and
by software flaws present in current-generation software
research software development, composition, and reuse
products. CSD tracks software security vulnerabilities (in
techniques.
the National Vulnerability Database), and seeks techniques
for the measurement of security vulnerabilities and In FY 2016, CSD partially reformulated the existing
techniques that reduce the impact and prevalence of toolchain testing infrastructure to mitigate test infrastructure
security vulnerabilities in newly developed products or in reliability problems uncovered by a dry run of the competition
new versions of existing products. and by subsequent inspections. A key part of this
reformulation was the consolidation of multiple operating
One approach to reducing the number of security
systems into a single operating system for all components.
vulnerabilities in software is to improve the development
Additionally, CSD developed an installation guide to assist
tools that are available. By identifying languages and
with the building, installing, and operating of the toolchain
software development tools that support a reduction of
testing infrastructure. The current infrastructure uses several
vulnerabilities, and by stimulating the creation of better
third-party components and concurrently-running virtual
tools and tool usage techniques, the approach should help
machines. The installation guide describes the required
developers produce applications with fewer vulnerabilities.
system configurations, account provisioning on local hosts,
While it is impossible to assure the total absence of security
installation and integration of third-party components
vulnerabilities in this way, it might well be possible to rule out
and packages, and the network configuration. An updated
specific, significant classes of vulnerabilities that currently
version of these elements as well as a document describing
provide the basis for many serious exploits.
the manual steps for performing simplified, script-oriented
CSD is developing an empirical, competitive approach testing in the absence of a continuous integration system
to finding the most effective and usable combinations of was also developed.
tools to produce software systems that are relatively free
In FY 2017, CSD plans to substantially simplify portions
of exploitable vulnerabilities. Multiple competitions are
of the testing infrastructure to improve reliability and
planned that will be based on an idea developed during
reproducibility, to perform a second round of testing, and to
the Designing a Secure Systems Engineering Competition
publicly announce the first toolchain competition.
Workshop that was conducted by the National Science
Foundation in 2010. The workshop proposed a competition CONTACTS:
for the development of a set of tools to help non-security-
Mr. Lee Badger Mr. Christopher Johnson
expert developers to rapidly build a significant application
(301) 975-3176 (301) 975-3247
with zero vulnerabilities, as detected by an extensive public
lee.badger@nist.gov christopher.johnson@nist.gov
test suite.
The participants in the planned competitions would
Networks of “Things”
implement software systems to solve challenge problems
using software development tool chains (“toolchains”) The Internet of Things (IoT) increasingly appears to
of their own choosing, within specified time periods. The be the next great technology revolution. It is expected to
toolchains may include existing technologies (e.g., existing impact everything from healthcare delivery, to how food is
software libraries and frameworks, code generators, reusable produced, to how we work, to all forms of transportation and
source code, or bug-finding tools), novel technologies, or any communication, and to virtually all forms of automation. IoT
combination thereof. Each competition would apply a time will impact everyone, and in multiple ways.
pressure by simulating a deadline in the software development
With a technology revolution of such large impact
process, increasing the likelihood of an introduction of
on society, it is imperative that IoT-based systems can be
security flaws. The objective of the toolchains would be to
trusted. This means that they should exhibit secure, reliable, 69
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

and private behaviors as well as many other attributes FOR MORE INFORMATION, SEE:
associated with quality (see references 2 and 4 below).
Privacy is particularly important because IoT-based systems
1 . NIST SP 800-183, Networks of ‘Things’, July 2016,
will likely produce huge amounts of data as a result of
https://doi.org/10.6028/NIST.SP.800-183.
sensing and surveillance (see references 1, 3, and 4 below).
This is the “big data” challenge associated with IoT. Therefore,
techniques, tools, and methods to mitigate the numerous 2. J. Voas and G. Hurlburt, “Third Party Software’s Trust
“trust” challenges are needed before these automated IoT- Quagmire”, IEEE Computer, December 2015.
based networks manage much of daily life.
Historically, there has been little in the way of formal, 3. J. Voas, “Demystifying IoT”, IEEE Computer, June
analytic, or even descriptive information about the building 2016.
blocks that govern the operation, trustworthiness, and life
cycle of the Internet of Things. A composability model and 4. C. Kolias, A. Stavrou, J. Voas, I. Bojanova, and R.
vocabulary that defines principles common to most, if not Kuhn, “Learning Internet of Things Security Hands-
all networks of things, was needed to address the question: On”, IEEE Security and Privacy, January 2016.
“What is the science, if any, underlying IoT?” NIST SP 800-
CONTACT:
183, Networks of ‘Things’ does exactly that – it offers an
underlying and foundational science to IoT that is based on a Dr. Jeffrey Voas
belief that IoT involves sensing, computing, communication, 301-975-6622
and actuation. The document describes five core building jeff.voas@nist.gov
blocks (called primitives): (1) sensor, (2) aggregator, (3)
communication channel, (4) eUtility, and (5) decision trigger.
Cloud Computing Security and
SP 800-183 is unique in that it uses two acronyms, IoT and
Forensics
NoT (Network of Things), extensively and interchangeably. IoT
is the outward facing acronym that most people are familiar The term cloud computing was initially coined in 1997 by
with; a NoT is an unfamiliar term, but has the advantage of Professor Ramnath Chellappa of Emory University. During his
referencing a more specific set of interconnected objects to talk, titled “Intermediaries in Cloud-Computing”, which was
which one can apply the building blocks described above. presented at the Institute for Operations Research and the
Management Sciences (INFORMS) meeting in Dallas, Texas,
The relationship between IoT and NoT is subtle—IoT is an
he referred to a cloud as an important new “computing
instantiation of a NoT, whereby IoT has its “things” tethered
paradigm where the boundaries of computing will be
to the Internet. A different type of NoT could be a Local Area
determined by economic rationale rather than technical
Network (LAN), with none of its “things” connected to the
limits alone.” The international IT literature and media later
Internet. Social media networks, sensor networks, and the
provided many definitions, models, and architectures, but it
Industrial Internet are all variants of NoTs. This differentiation
was not until 2011, when NIST published SP 800-145, The NIST
in terminology helps to separate use cases of varying vertical
Definition of Cloud Computing, that the world coalesced on
and quality domains (transportation, medical, financial,
the cloud deployment and service models, definitions and
agricultural, safety-critical, security-critical, performance-
descriptions provided in SP 800-145.
critical, and high assurance, to name a few). The distinctions
are useful since there is no singular IoT, and it is meaningless Following the December 2010 Federal Government’s
to speak of comparing one IoT to another. But one NoT can “Cloud First” policy issued as part of the 25-point plan for
be compared to another NoT – that makes this viewpoint and the U.S. Federal Government’s (USG) IT modernization
the associated definition actionable. and reform, NIST assumed a technical leadership role for
the federal agencies’ efforts related to the adoption and
Future work in this area will refine the definitions of the
development of cloud computing standards. The goal was
five core NoT building blocks. For example, instead of just
to accelerate the Federal Government’s adoption of secure
considering an all-purpose sensor, categories of sensors will
and effective cloud computing solutions to reduce costs and
be explored. This will involve a decomposition of the building
improve services.
blocks. The research team will also demonstrate how to apply
these definitions to vertical markets. In addition, the team will In addition to the initial definition of cloud computing,
present these results in Revision 1 of NIST SP 800-183, which NIST built a USG cloud computing technology roadmap
70 should be produced in late 2017 or early 2018. that focused on security, interoperability, and portability
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

requirements, and lead efforts to develop standards and be available for public comments by the end of the
guidelines in close collaboration with standards bodies, the first quarter of 2017, provides a cloud overlay of the
private sector, and other stakeholders. NIST also developed a SP 80053 Revision 4 security controls for cloud-
cloud computing reference architecture, a security reference based ecosystems.
architecture and, during 2016, focused on developing
NIST is also leading the research and development
the guidance for applying a risk-based approach to cloud
of the projects listed below:
adoption and the guidance for applying the SP 800-53
• Members of the NIST Cloud Security Working
Revision 4 security and privacy controls to cloud-based
Group, in collaboration with the Cloud Security
federal information systems.
Alliance’s members are researching the security
During FY 2016, NIST also started researching the
challenges encountered when leveraging
security challenges encountered when leveraging application
application containers and microservices for
containers and microservices for the implementation of
the implementation of cloud-based information
cloud-based federal information systems and the security
systems. Based on this research, NIST will issue
challenges encountered when implementing cloud-based
an interagency report documenting the findings
federated identity solutions, along with the impact on the
and will provide recommendations based on
system’s security posture. Some of the current work is
best practices for mitigating the identified
focusing on the development of an open security controls
challenges.
assessment language (OSCAL) that aims to revolutionize
• Members of the NIST Cloud Security Working
every step in the life cycle of a cloud-based information
Group are researching the security challenges
system and on the development of a cloud forensics
encountered when implementing cloud-based
reference architecture that is derived from the cloud security
federated identity solutions and the impact on
reference architecture mentioned above. Details regarding
the overall system’s security posture. Based
the latest projects are provided below.
on this research, NIST will issue an interagency
CSD Role in the NIST Cloud Computing
report documenting the findings and will provide
Program
recommendations based on the best practices for
mitigating the identified challenges.
During FY 2016, NIST continued to promote the
development of publications, national and international • Members of the NIST Cloud Forensic Science
standards, and specifications in support of the USG’s effective Working Group are working on defining a cloud
and secure use of cloud computing, as well as providing forensics reference architecture that leverages NIST
technical guidance to federal agencies for secure and SP 500-299: Cloud Security Reference Architecture
effective cloud-computing adoption. During FY 2016, NIST’s and NISTIR 8006, NIST Cloud Computing Forensic
cloud computing security and forensic science activities Science Challenges.
included the development of the following guidance and/or
• Members of a NIST-led Tiger Team is developing
recommendations:
an OSCAL, a hierarchical, formal language that
• NIST Draft SP 800-173, Guide for Applying the aims to support the transfer of security information
Risk Management Framework to Cloud-based in formats that are compliant with the security
Federal Information Systems. This publication controls catalog of choice.
provides guidance in using the Risk Management
In support of U.S. cloud-computing mandates, CSD
Framework described in SP 800-37 Revision
staff members provide leadership for several public
1, Guide for Applying the Risk Management
cloud working groups operating under the NIST Cloud
Framework to Federal Information Systems:
Computing Program. These working groups focus on
a Security Life Cycle Approach, to issue an
meeting the high-priority requirements described in
authorization to operate for cloud-based
NIST SP 500-293, U.S. Government Cloud Computing
information systems. The draft document will
Technology Roadmap.
be posted for public comment by December 31,
CSD staff co-chaired several significant cloud
2016.
computing efforts in 2016:
• NIST Draft SP 800-174, Security and Privacy
• Co-Chaired the NIST Cloud Computing Security
Controls for Cloud-based Federal Information
Working Group and led the working group on
Systems. This document, which is anticipated to 71
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

the development of the NIST SP 800-173, Guide are accessed by different types of applications and users.
for Applying the Risk Management Framework to The PM infrastructure is scalable and can support policies of
Cloud-based Federal Information Systems; NIST various types simultaneously while remaining manageable in
SP 800-174, Security and Privacy Controls for the face of changing technology, organizational restructuring,
Cloud-based Federal Information Systems (both and increasing amounts of data. The PM provides a framework
described above); and on researching the topics capable of supporting combinations of both current access
listed above. control approaches and newly conceived types of policy
without extension.
• Co-Chaired the NIST Cloud Computing Forensic
Science Working Group and led the development of NIST and other members of an Ad Hoc INCITS working
the cloud forensics reference architecture. group are continuing to develop a three-part NGAC standard.
This work is being conducted under three sub-projects:
• Co-Chaired the NIST Cloud Computing
Interoperability and Portability Working Group • Project 2193–D: Next Generation Access Control –
and addressed issues facing cloud computing Implementation Requirements, Protocols and API
with respect to interoperability and portability, Definitions;
standards, and common and functional
• Project 2194–D: Next Generation Access Control –
terminologies.
Functional Architecture; and
CSD staff members participated in various standards
• Project 2195–D: Next Generation Access
development organizations, all listed in the section of this
Control – Generic Operations and Abstract Data
report dedicated to international standards.
Structures.
In FY 2017, NIST will continue collaboration with the
An initial standard from this work was published
private sector, academia and other public-sector entities
in 2013 and is now available from ANSI as INCITS 499:
on developing guidance and specifications that support the
NGAC Functional Architecture (NGAC–FA). However, based
broad adoption of innovative cloud solutions. Some of the
on experience with similar efforts (e.g., Project 2193-D,
very effective frameworks for such collaborations that NIST
Project 2195-D, and the revised NISTIR 7987, Policy Machine:
is hosting are the public working groups with international
Features, Architecture, and Specification), work is underway
participation.
to update this standard.
FOR MORE INFORMATION, SEE:
In 2016, the standard for Project 2195-D was approved
and is now available from the ANSI e-standards store as
https://www.nist.gov/programs-projects/nist-cloud-
INCITS 526: NGAC Generic Operations and Abstract Data
computing-program-nccp
Structures (NGAC-GOADS).
CONTACT:
The eXtensible Access Control Markup Language
(XACML) and NGAC are very different ABAC standards with
Dr. Michaela Iorga
similar goals and objectives. What are the similarities and
(301) 975-8431
differences between these two standards? What are their
michaela.iorga@nist.gov
comparative advantages and disadvantages? To answer
these questions, in October 2016 NIST published SP 800-
Policy Machine – Next Generation 178, A Comparison of Attribute Based Access Control (ABAC)
Access Control Standards for Data Service Applications: Extensible Access
Control Markup Language (XACML) and Next Generation
CSD has continued the development of an advanced
Access Control (NGAC), to describe and compare these
Attribute Based Access Control (ABAC) framework called
standards with respect to the criteria derived from ABAC
the Policy Machine, which is designed to be in alignment with
issues or considerations identified by NIST SP 800-162, Guide
an emerging ANSI/INCITS standard under the title of “Next
to Attribute Based Access Control (ABAC) Definition and
Generation Access Control” (NGAC).
Considerations: operational efficiency, attribute and policy
The Policy Machine (PM) is a fundamental reworking of management, scope and type of policy support, and support
traditional access control into a form suited to the needs of for administrative review and resource discovery.
a modern, distributed, interconnected enterprise. The PM is
based on a flexible infrastructure that can provide access
72 control services for several different types of resources that
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

In FY 2017, CSD plans to issue a new version of the PM deployment). Recognizing the fact that VMs are the end-
through GitHub as an open source distribution to allow nodes of a virtual network, research on the secure virtual
widespread experimentation and transfer. Example data network configuration for VM protection was started in FY
services (e.g., email, file management, records management, 2015 and continued in FY 2016. The outcome of the research
workflow) are planned to be provided with the distribution. was the identification of four virtual network configuration
The new version will reflect new features and enhanced areas impacting VM security: network segmentation,
performance, and will complete (for purposes of balloting) network path redundancy, traffic control using firewalls,
the revised INCITS 499, and the Project 2193–D standard. and VM traffic monitoring. Each area was analyzed, and
the corresponding security recommendations have been
FOR MORE INFORMATION, SEE:
provided.
http://csrc.nist.gov/pm/
In FY 2016, the project team produced the following
two publications: Analysis of Virtual Networking Options
CONTACTS:
for Securing Virtual Machines which was submitted to the
Mr. David Ferraiolo Mr. Serban Gavrila Seventh International Conference on Cloud Computing,
(301) 975-3046 (301) 975-4242 GRIDs, and Virtualization (CLOUD COMPUTING 2016) (Note:
david.ferraiolo@nist.gov serban.gavrila@nist.gov The abstract to this paper can be found in the Publications
Released FY 2016 – Conference Papers section later in this
Annual Report), and SP 800-125B, Secure Virtual Network
Security for a Virtualized
Configuration for Virtual Machine (VM) Protection.
Infrastructure
In FY 2017, research on the secure configuration of
Virtualization technology has now found ubiquitous the third component of a virtualized infrastructure (i.e.,
adoption in data centers used for hosting enterprise virtualized storage) will continue. The resulting findings
applications as well as for providing cloud services. This and security recommendations will either be included as
technology has been used not only for configuring and additions to SP 800-125A, Security Recommendations for
deploying virtualized hosts (Server Virtualization) but also Hypervisor Deployment, or as a separate document.
for virtual networks (Network Virtualization) and virtualized
CONTACT:
storage (Storage Virtualization). Together, these three
components constitute the virtualized infrastructure in a
Dr. Ramaswamy Chandramouli
data center.
(301) 975-5013
The core component of a virtualized infrastructure is mouli@nist.gov
the virtualized host (i.e., a physical host running a server
virtualization product) that can support multiple computing
Cyber Threat Information Sharing
stacks (called Virtual Machines or VMs), each with a different
platform configuration (e.g., operating system (OS)) and As cyber attacks increase in both sophistication and
each with unique security needs. Application programs frequency, it is important to collect and analyze cyber threat
loaded into a VM are often valuable server programs (e.g., information from a variety of internal and external sources,
webserver, database management system) that support and use it to develop, enhance, and deploy proactive,
important business processes and generally need more threat-informed, cyber defense capabilities. Cyber threat
security protection than do other virtual hosts such as information includes indicators (i.e., artifacts or observable
workstations. Protection for application programs in a events that suggest that an attack is imminent, that an
VM (in fact for the entire VM) can be provided through a attack is underway, or that a compromise may have already
combination of the following: the secure configuration of occurred); information about the tactics, techniques, and
the virtualized host, the secure configuration of the virtual procedures (TTPs) of actors; recommended courses of
network and the secure configuration of the virtualized action; and other information that is used to characterize
storage associated with the VM. threats. Because threat actors often use the same
TTPs against multiple targets, exchanging cyber threat
Just like their physical counterparts (i.e., physical servers),
information allows organizations to leverage the collective
VMs can be protected through host-level and network-level
knowledge, experience, and analysis capabilities of their
security measures. Hence, the focus of research in FY 2014
peers, thereby increasing the overall awareness and security
and prior years was on the secure configuration of the
of an entire sharing community. Through the exchange of
virtualized hosts (specifically Hypervisor configuration and 73
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

cyber threat information, organizations can gain a more  •   Information Sharing and Analysis Centers
complete  understanding  of  their  threat  environment  by  (ISACs),
correlating their observations with those of others.
•   Information Sharing and Analysis Organizations
| CSD has established a cyber threat information sharing  |     |     |     |     |     | (ISAOs), |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
initiative, which is focused on providing guidance on how
•  Federal/State/Local agencies,
| an  organization  |     | can  establish  | information  | sharing  | and  |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------------- | ------------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
coordination  capabilities  that  enhance  or  augment  their  •  Law Enforcement,
existing cybersecurity practices. The guidance covers threat- •  Fusion Centers, and
informed detection, protection and response capabilities;
•  Sector Coordinating Councils.
data privacy and sensitivity; data collection and retention
CONTACTS:
practices; the use of open standards for information exchange;
de-identification and anonymization; and guidance on how
|     |     |     |     |     |     | Mr. Christopher Johnson  |     |     |     | Mr. Lee Badger  |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --------------- | --- | --- | --- |
an organization can establish, participate in, and maintain
|               |      |              |          |                 |      | (301) 975-3247                |     |     |     | (301) 975-3176      |     |     |     |
| ------------- | ---- | ------------ | -------- | --------------- | ---- | ----------------------------- | --- | --- | --- | ------------------- | --- | --- | --- |
| coordination  | and  | information  | sharing  | relationships.  | The  |                               |     |     |     |                     |     |     |     |
|               |      |              |          |                 |      | christopher.johnson@nist.gov  |     |     |     | lee.badger@nist.gov |     |     |     |
guidance will help incident responders, network defenders,
and  operations  personnel  consider  what  information  is  Mr. David Waltermire
sharable, the circumstances under which sharing is permitted,
(301) 975-3390
with whom the information may be shared, and how the  david.waltermire@nist.gov
information should be protected.
| As  an  | example  | of  | this  guidance,  | in  FY  2016,  | CSD  |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | ---------------- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
The Ontology of Authentication
released a second draft of SP 800-150, Guide to Cyber Threat
Over the past 30 years, NIST has been at the forefront
Information Sharing. The draft publication was released for
|     |     |     |     |     |     | of  recommending  |     |     | best  | practices  | for  | authentication.  |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ----- | ---------- | ---- | ---------------- | --- |
public comment on April 21, 2016. This publication is intended
to help organizations prepare for an exchange of cyber  Recommendations have included the usage of passwords,
biometrics, authentication hardware devices, and Public Key
threat information, both consuming cyber threat information
Infrastructure (PKI) solutions in enterprise settings. In FY
from external sources and producing information for other
2015, CSD began researching the classification of general
organizations to use. Organizations may have substantially
|     |     |     |     |     |     | authentication  |     | features.  | This  | investigation  |     | was  | prompted  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | ----- | -------------- | --- | ---- | --------- |
different capabilities for detecting threats, responding to
attacks, diagnosing causes, and handling sensitive incident- by the general call to move away from passwords toward
the growing number of alternative authentication methods
related information, but this guidance is intended to help
|                |              |     |                |        |         | (e.g.,  biometrics,  |     | smart  | cards,  | etc.).  | A   | notional  | ontology  |
| -------------- | ------------ | --- | -------------- | ------ | ------- | -------------------- | --- | ------ | ------- | ------- | --- | --------- | --------- |
| organizations  | collaborate  |     | and  exchange  | cyber  | threat  |                      |     |        |         |         |     |           |           |
of authentication was developed that included a detailed
information despite these organizational differences. CSD
|     |     |     |     |     |     | taxonomy,  | a  metrology,  |     | and  | a  framework  |     | for  | assessing  |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ---- | ------------- | --- | ---- | ---------- |
will release the final version of SP 800-150, in October 2016.
alternatives.
In FY 2017, CSD plans to continue to conduct research,
|     |     |     |     |     |     | Research  | over  | the  | past  | year  | led  to  | updates  | to  the  |
| --- | --- | --- | --- | --- | --- | --------- | ----- | ---- | ----- | ----- | -------- | -------- | -------- |
prepare guidance, and participate in standards development
|             |            |          |                |                   |     | authentication  |     | taxonomy  | (see  | Figure  | 28)  | to  encapsulate  |     |
| ----------- | ---------- | -------- | -------------- | ----------------- | --- | --------------- | --- | --------- | ----- | ------- | ---- | ---------------- | --- |
| activities  | that  are  | focused  | on  increased  | interoperability  |     |                 |     |           |       |         |      |                  |     |
current and emerging mechanisms and was the basis for
and operational tempo through near real-time cyber threat
Expanding Continuous Authentication with Mobile Devices,
information sharing, including:
which was published in the IEEE Computer magazine. The
•   Expressing cyber threat information using machine-
taxonomy now covers a wide assortment of commonly used
readable formats,
|     |     |     |     |     |     | human-machine,  |     | machine-machine,  |     |     | human-human,  |     | and  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | --- | ------------- | --- | ---- |
•   Developing automated mechanisms for exchanging  attribute attestation methods. Human-human authentication
cyber threat information, was included due to the number of systems that use human
interaction as a backup system when a user has trouble with
•   Describing automated courses of action,
a man-machine interface. In addition, the research uncovered
•   Publishing cyber threat information metadata,
|     |     |     |     |     |     | an  emerging  |     | branch  | of  | authentication  |     | –continuous  |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | --- | --------------- | --- | ------------ | --- |
and authentication – that supports user monitoring as a part of
| •   Safeguarding cyber threat information. |     |     |     |     |     | the authentication. |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
NIST will also help foster cyber threat information sharing
74 by supporting information sharing initiatives by public and
private sector organizations, including:
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 28: Draft Authentication Taxonomy
The notional authentication ontology attempts The security category is broken down into the following
to define a metrology framework that is useful for foundational areas:
better understanding, comparing, and measuring the
• Uniqueness of the relationship to the entity,
appropriateness of authentication technologies to a specific
• Protection and resilience of a token against
use-case. The measurement framework separates metrics
compromise,
into security, usability, deployability, and manageability
categories (see Figure 29). It is important to note that • Protection of a token during delivery,
each category may overlap or impact the others. Security
• Protection of metadata in storage, and
and usability are of special interest; while usability is often
• Protection / resilience of storage backup.
thought of as a tradeoff to security, both must be satisfied
for the user to support the security of the system. The usability category follows the ISO 9241-11 (1988)
areas of:
• Effectiveness,
• Efficiency, and
• Satisfaction.
Specific methods of calculating measurements in these
categories are not currently included and may be unique
to each authentication mechanism and environment. The
framework supports integration with the programmatic
categories of deployability and manageability, but
measurement areas in these categories are not currently
defined, as they are often well specified within organizations.
Future programmatic efforts will be focused toward
a NISTIR to describe the research results, encourage
Figure 29: Suitability Framework for Authentication further discussion with the community, and provide
recommendations for future standards development efforts,
with the goal of moving toward specifying independently
measurable strength requirements rather than specific
implementation requirements. 75
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

The program status was presented and well received Below is a list of NCCoE’s highlights and accomplishments
at the 2016 World eID and Cybersecurity Conference. As for FY 2016:
this program is to eventually define the future development
of standards, concerns as to the immediate adoptability
Publications
were received and will inform future research. Additional
• Draft Special Publication (SP) 1800-4, Mobile
work to identify interdependencies, such as with identity
Device Security: Cloud & Hybrid Builds Practice
management and authorization controls and requirements,
Guide: demonstrated how commercially available
should help allay these concerns.
technologies can meet an organization’s needs to
In addition, NIST CSD will work with the community in FY secure sensitive enterprise data accessed by and/
2017 to identify and address common areas of authentication or stored on employees’ mobile devices. The guide
requirements to create a framework for researching and describes approaches for securing mobile devices
developing authentication mechanisms using this ontology. in both a cloud-based architecture and also an
If a clear metrology can be established, future access control architecture using a hybrid of cloud and enterprise
process implementations should be less susceptible to architecture (see https://nccoe.nist.gov/projects/
vulnerabilities specific to individual implementations. building_blocks/mobile_device_security).
CONTACT: • Draft SP 1800-5, Financial Services IT Asset
Management Practice Guide: demonstrated how
Dr. Kim Schaffer
an organization can, in an automated fashion, gain
(301) 975-8375
customized insight into 1) what is on its network,
kim.schaffer@nist.gov
2) the status of each hardware and software
component in its environment, and 3) how to
prioritize resources to address vulnerabilities.
NATIONAL CYBERSECURITY This kind of understanding and insight can help
CENTER OF EXCELLENCE increase a financial organization’s cybersecurity
resilience by enhancing the visibility of assets,
revealing which applications are actually being
The National Cybersecurity Center of Excellence used, identifying vulnerable assets, enabling faster
(NCCoE) is a collaborative hub where industry organizations, response to security alerts, and reducing help-desk
government agencies, and academic institutions work response times (see https://nccoe.nist.gov/projects/
together to address the private sector’s most pressing use_cases/financial_services_sector/it_asset_
cybersecurity issues. As a public-private partnership, industry management
experts and technology partners—from Fortune 50 market • Wireless Medical Infusion Pumps Final Project
leaders to smaller companies specializing in IT security— Description:: examined the security of wireless
choose to work with the NCCoE to develop practical, example medical devices on an enterprise network using
cybersecurity solutions using standards, best practices, and infusion pumps as a use case (see https://nccoe.
commercially available technology. The NCCoE documents nist.gov/projects/use_cases/medical_devices).
these example solutions in the NIST Special Publication
• Domain Name System-Based Security for
1800 series, which maps technical capabilities to the NIST
Electronic Mail Final Project Description: explored
Cybersecurity Framework and details the steps needed to
a security platform that provides trustworthy email
recreate the example solution in the real world. The NCCoE
exchanges across organizational boundaries to
aims to provide practical cybersecurity solutions that are
help businesses improve the privacy and security
cost-effective, repeatable, and scalable to increase the rate of
protections of their employees’ operations (see
adoption and accelerate effective innovation across business
https://nccoe.nist.gov/projects/building_blocks/
sectors.
secured_email).
• Data Integrity: Recovering from a Destructive
Malware Attack Final Project Description:
explored methods to effectively recover operating
systems, databases, user files, applications, and
76 software/system configurations. It will also explore
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

issues of auditing and reporting (user activity • Identity and Access Management for Smart Home
monitoring, file system monitoring, database Devices Concept Paper: outlined potential project
monitoring, scanning backups/snapshots for topics for exploration, including identification,
malware, and rapid recovery solutions) to support authentication, and authorization for Internet
recovery and investigations (see https://nccoe.nist. of Things devices, specifically within the smart
gov/projects/building_blocks/data_integrity). home (see https://nccoe.nist.gov/projects/project-
concepts/idam-smart-home-devices).
• Privacy-Enhanced Identity Federation Project
Description Draft: examined how privacy-
Events
enhancing technologies that leverage market-
dominant standards can be integrated into identity NCCoE hosted several events to support project
broker solutions to meet the privacy objectives of development and receive feedback on proposed example
users and organizations (see https://nccoe.nist. solutions. Highlights include:
gov/projects/building_blocks/privacy-enhanced-
• NCCoE Building Dedication, February 8, 2016,
identity-brokers).
Rockville, MD: NCCoE hosted a ribbon cutting
• Multi-factor Authentication for e-Commerce Draft and building dedication ceremony for its new
Project Description: examined how multi-factor facility in Rockville. (see https://nccoe.nist.gov/
authentication for e-commerce transactions that news/nist-and-nccoe-celebrate-move-expanded-
are tied to existing web analytics and contextual cybersecurity-facility).
risk calculation can increase assurance in purchaser
• Protecting Consumer Data: Securing Payment
or user identity and thus help reduce the risk of
and Transaction Information Workshop, March
online identification and authentication fraud
22, 2016, University of Alabama Birmingham: The
(see https://nccoe.nist.gov/projects/use_cases/
NCCoE hosted a full-day workshop with retail
multifactor-authentication-ecommerce).
industry members and technology vendors to
• Securing Non-Credit Card, Sensitive Data Draft explore consumer-facing retail cybersecurity
Project Description: explored the implementation issues in depth. The participants recognized that
of data masking and tokenization, coupled with cybersecurity incidents affecting consumer-
fine-grained access control such as Attribute Based facing businesses threaten the financial security
Access Control, which may significantly improve of companies and the public, weakening
the security of personally identifiable information consumer confidence, eroding individual privacy
(PII) transmitted and stored during commercial protections, and damaging the brand value
payment transactions, as well as PII shared and reputation of businesses. Topics included
internally within a retail organization and externally methods to combat online fraud (e.g., through
with business partners (see https://nccoe.nist.gov/ multi-factor authentication for e-commerce
projects/use_cases/securing-sensitive-consumer- transactions) and to safeguard customer profiles
data). (e.g., through secure handling of sensitive, non-
• Mobile Application Single Sign-On Draft Project credit card consumer data). (See https://nccoe.
Description: explored the use of multi-factor nist.gov/events/consumer-facing-retail-sector-
authentication and mobile single sign-on for native workshop.)
and web applications to improve interoperability
• Pre-Workshop: Maritime and Oil & Natural Gas,
between mobile platforms, applications, and April 5, 2016, Rockville, MD: In coordination with
identity providers, irrespective of the application the NIST Cybersecurity Framework Workshop,
development platform used in their construction the NCCoE facilitated an open session with
(see https://nccoe.nist.gov/projects/use_cases/ members of the maritime and oil and natural
mobile-sso). gas industries to identify and prioritize hard
• Authentication for Law Enforcement Vehicle cybersecurity challenges that can be addressed
Systems Draft Project Description: explored jointly (see https://nccoe.nist.gov/events/pre-
implementing an integrated set of authentication workshop-maritime-and-oil-and-natural-gas-
mechanisms, improving system security, usability, open-session).
and safety (see https://nccoe.nist.gov/projects/
77
use_cases/authentication-law-enforcement-
vehicle-systems).
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 30: NCCoE Building Dedication
FRONT ROW (from left to right): Ike Leggett, Montgomery County Executive; Maryland Lt Governor Boyd Rutherford;
Senator Ben Cardin; Senator Barbara Mikulski; Commerce Secretary Penny Pritzker; Rep. John Delaney; and
Rep. John Sarbanes.
BACK ROW (from left to right): Al Grasso, President and Chief Executive Officer, MITRE; Gil Quiniones, President and
Chief Executive Officer, New York Power Authority; Michael Brown, President and Chief Executive Officer, Symantec;
Robert Caret, University System of Maryland Chancellor; Willie E. May, Director, NIST and Under Secretary of Commerce
for Standards and Technology; Amit Yoran, RSA President; and Dean Garfield, President and Chief Executive Officer,
Information Technology Industry Council. Photo credit: Joseph Andrucyk/State of Maryland Office of the Governor.
NCCoE staff were invited to speak at more than 30 • Christian Science Monitor’s Passcode
industry events and conferences. Highlights include: Conversation, October 8, 2015, Washington,
D.C.: Government leaders discussed ongoing
• RSA Conference, February 29-March 4, 2016,
cybersecurity challenges, such as how to adopt
San Francisco: Nate Lesser, NCCoE Deputy
a proactive approach to effectively defend
Director, delivered a keynote address at the State
tomorrow’s networks and how to disrupt attacks
of Maryland-hosted luncheon and presented a
upon organizational systems. Nate Lesser, NCCoE
session on the NCCoE Wireless Infusion Pumps
Deputy Director, participated in the Keynote Panel
project (see https://nccoe.nist.gov/events/rsa-
Discussion and described the center’s work in
conference-2016).
collaborating and coordinating between public and
• Healthcare Information and Management Systems
private sector.
Society (HIMSS) Conference, February 29-March
4, 2016, Las Vegas: NCCoE engineers demonstrated
the Wireless Infusion Pumps and Securing
Electronic Health Records on Mobile Devices
projects (see https://nccoe.nist.gov/events/himms-
78 conference-and-exhibition).
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 31: Gavin O’Brien (NCCoE, NIST) provided a demonstration on securing electronic health records on
mobile devices.
In FY 2017, the NCCoE plans to release six SP-1800 CONTACT:
practice guides:
Mr. Timothy McBride
• Domain Name System-Based Secured
(301) 975-0214
Email,
timothy.mcbride@nist.gov
• Situational Awareness: Secured Networking
Infrastructure for the Energy Sector,
• Wireless Medical Infusion Pumps, INTERNET INFRASTRUCTURE
• Derived Personal Identity Verification PROTECTION
Credentials,
• Data Integrity: Recovering from a Destructive
ITL’s Internet Infrastructure Protection (IIP) program, led
Malware Attack, and
by the Advanced Network Technologies Division (ANTD),
• Mobile Application Single Sign-On.
works with industry to develop the measurement science
In addition to the release of these practice guides, and new standards necessary to ensure the robustness,
NCCoE plans to attend both national and international scalability, and security of the global Internet. The research
cybersecurity conferences to present NCCoE projects and focuses on the measurement and modeling techniques
participate in panels to help increase the rate of adoption necessary to understand, predict, and control the behavior
and accelerate innovation. The NCCoE has already been of Internet-scale networked information systems. The ITL
selected to speak at the 2017 HIMSS conference. staff use these insights to guide the design, analysis, and
standardization of new technologies aimed at improving
FOR MORE INFORMATION, SEE:
the robustness of the Internet’s core infrastructure. Recent
https://nccoe.nist.gov/ efforts have focused on enhancing the security of the
Internet’s Domain Name System (DNS), the Border Gateway
Protocol (BGP), and Electronic mail (Email) and messaging
79
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

infrastructures. In addition, the IIP program addresses other In FY 2016, as technology specifications and
systemic vulnerabilities in core Internet technologies, such as implementations matured, the ITL staff began a series of
those that enable massive-scale Distributed Denial of Service outreach efforts with the networking industry to increase
(DDoS) attacks. the understanding and foster the adoption of BGP security
mechanisms. The ITL staff organized and led a workshop
In FY 2016, ITL
at the June North American Network Operators Group
staff made significant
(NANOG) meeting aimed at addressing the practical issues,
contributions to the
state of vendor support and existing operational experience
design, standardization,
with emerging BGP security technologies (see, https://www.
test and measurement
nanog.org/meetings/abstract?id=2846). The ITL staff also
of technologies to
initiated a nationwide BGP security pilot deployment project
improve the security
with the Internet2 research and education community.
and robustness of the
Internet’s global routing ITL’s High Assurance
protocol BGP. NIST staff Domains (HAD) project
were key contributors to Internet Engineering Task Force aims to leverage NIST’s
(IETF) standards to add cryptographic validation to BGP (see, previous successes in
https://tools.ietf.org/html/draft-ietf-sidr-bgpsec-protocol/), the development and
and to address the robustness issues associated with deployment of Domain
large-scale routing policy violations (see, https://www.rfc- Name System Security
editor.org/rfc/rfc7908.txt). In addition, NIST developed and Extentions (DNSSEC)
released open-source reference implementations of these technologies to enable
emerging IETF specifications, online test tools to foster their scalable solutions of long standing Internet security issues.
adoption and measurement systems to track their operational In FY 2016, the project focused on addressing the issues of
deployment. Figure 32 below is a visualization generated by Email phishing attacks and developing scalable techniques
one such monitoring tool of the emerging global structure of to enable the cryptographic protection of Email message
the Resource Public Key Infrastructure (RPKI). The RPKI has exchanges. NIST published NIST SP 800-177, Trustworthy
been designed to provide the trust infrastructure upon which Email, a comprehensive guidance on the deployment and
Internet routing security technologies can be based. use of emerging DNS-based authentication mechanisms to
combat email phishing and spam. In addition, ITL developed
and deployed online test tools to assist network operators
in the configuration and verification of their deployment of
emerging anti-phishing technologies.
The second focus area for the HAD project in FY 2016
was the advancement of specifications, implementations and
deployment of IETF DNS-based Authentication of Named
Entities (DANE) technology that leverages a secured DNS as
a ubiquitous key discovery and management infrastructure.
In FY 2016, the ITL staff contributed to the development of
IETF DANE specifications and developed distributed test and
measurement tools to assist in their adoption and use in the
global Internet. Figure 33 (See next page) shows the user
interface to the recently released NIST DANE test system
that enables product developers and network operators to
test their use of the DANE technologies to store, retrieve and
validate various types of cryptographic keying material for
end-to-end email security, and for general transport-layer
security (TLS) for web and other applications.
Figure 32: NIST Visualization of the Evolving Coverage
80
and Depth of the Internet’s Global Resource Public Key
Infrastructure for BGP security.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

In FY 2017, the major milestones for Internet Infrastructure
Program will include:
• Completing the publication of IETF standards
for BGP security and increasing outreach and
pilot deployment activities to foster commercial
deployment of these technologies;
• Continuing to develop and mature DANE
specifications and technologies for scalable key
management in the Internet and conducting
research on their applicability to emerging problem
domains, such as authentication in consumer
networks; and
• Publishing NIST guidance on current DDoS
mitigation techniques and continuing to research
Figure 33: NIST DANE Test system for Secure Email and develop new approaches based upon
emerging SDN technologies.
The HAD project staff also collaborated with the
FOR MORE INFORMATION, SEE:
NCCoE DNS-Based Secured Email project that tested and
produced detailed deployment guidance for commercial Robust Inter-Domain Routing Project:
implementations of DANE-based server-to-server security https://www.nist.gov/programs-projects/robust-inter-
for email transport (see https://nccoe.nist.gov/projects/ domain-routing
building_blocks/secured_email).
NIST RPKI Deployment Monitor and Test System:
The ITL staff in the
https://www.nist.gov/services-resources/software/nist-rpki-
Advanced Distributed
deployment-monitor-and-test-system
Denial of Service (DDoS)
Mitigation Techniques BGP Secure Routing Extension (BGP‑SRx) Prototype:
project are working https://www.nist.gov/services-resources/software/bgp-
with the community secure-routing-extension-bgp-srx-prototype
to document and
quantitatively characte- BRITE - BGPSEC / RPKI Interoperability Test & Evaluation
rize the applicability, System:
effectiveness and impact of various approaches to filtering https://www.nist.gov/services-resources/software/brite-
spoofed Internet Protocol (IP) traffic streams and develop bgpsec-rpki-interoperability-test-evaluation-system
consensus recommendations and deployment guidance that
High Assurance Domains Project:
can drive their adoption in Federal network environments and
https://www.nist.gov/programs-projects/high-assurance-
throughout the Internet industry. In FY 2016, the NIST staff
domains
developed benchmarking methodologies to characterize
the performance implications of various techniques to block
NIST SP 800-177 Trustworthy Email:
spoofed IP packets in commercial routers and developed
http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.
draft deployment guidance for these mechanisms in a
SP.800-177.pdf
variety of network interconnection scenarios.
NIST DANE Test System:
In addition to understanding the barriers to deployment
https://dane-test.had.dnsops.gov/
and adoption of existing DDoS mitigation techniques, the
ITL staff began the research and evaluation of new, scalable
Advanced DDoS Mitigation Techniques Project:
means of DDoS detection and mitigation, based upon
https://www.nist.gov/programs-projects/advanced-ddos-
Software Defined Networking (SDN) technologies.
mitigation-techniques
Software Defined Virtual Networks Project:
https://www.nist.gov/programs-projects/software-defined-
81
virtual-networks
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

CONTACT: works to improve the interoperability, broad acceptance, and
adoption of security automation solutions to address current
Mr. Doug Montgomery
and future security challenges, creating opportunities for
(301) 975-3630
innovation.
dougm@nist.gov
Specification, Standards, and Guidance
Development
ADVANCED SECURITY To support the overarching security automation vision, it
TESTING AND is necessary to have specifications that describe the required
interactions between systems, standards that document
MEASUREMENTS
international consensus approaches, and guidance for
product developers and implementers. Through close work
Security Automation and with partners in government, industry, and academia, CSD
Continuous Monitoring continues to facilitate the definition and development of
security automation approaches that enable organizations to
IT organizations operate a diverse set of computing
understand and manage IT security risks.
assets that access, route, store, and process information that
is critical to the operations of businesses and the missions During FY 2016, CSD has continued to work to build on
of government agencies. These IT environments are under previous security automation work, as follows:
constant threat of attack and are frequently undergoing • Identified and addressed gaps in the current
change, with new and updated software being deployed specifications;
along with updated configurations. The wide variety of
• Evolved existing approaches to achieve greater
computing products, the dynamic nature of software, the
scalability and impact;
speed of configuration change, and the diversity of threats
require organizations to maintain situational awareness over • Participated in working groups in standards
their IT assets and to utilize this information to make informed development organizations to promote
risk-based decisions. international consensus around standardized
approaches;
Security automation utilizes standardized data formats
and transport protocols to enable data to be exchanged • Provided additional guidance on architectural,
between business, operational, and security systems that design, and analysis concerns; and
support security processes by: • Developed and maintained tools and reference
• Identifying IT assets, including hardware, software, implementations.
and data; CSD is currently working with its partners in various
• Providing awareness over the operational state of standards-development organizations, including ISO, IETF,
computing devices; Organization for the Advancement of Structured Information
Standards (OASIS), the Forum of Incident Response and
• Enabling security reference data to be collected
Security Teams (FIRST), and the Trusted Computing Group
from internal and external sources; and
(TCG), to further mature and broaden the adoption of
• Supporting analysis processes that measure the security automation specifications, reference data, and
effectiveness of security controls and provide techniques. This area of work is focused on evolving security
visibility into security risks, enabling risk-based automation specifications to integrate with existing transport
decision making. protocols to provide for the secure, interoperable exchange
Commercial solutions built using security automation of security automation data. Additional work is focused on
specifications enable the collection and harmonization of evolving security metrics and providing consensus guidance
vast amounts of operational and security data into coherent, on security automation approaches. Through the definition
comparable information streams to achieve situational and adoption of security automation standards and
awareness that allows the timely and active management of guidelines, IT vendors will be able to provide standardized
diverse IT systems. Through the creation of reference data security solutions to their customers. These solutions support
and guidance, and the international recognition of flexible, continuous monitoring and automated, dynamic network
open standards, the NIST security automation program defense capabilities, based on the analysis of data from
82
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

operational and security data sources and the collective and to enable other agencies and private-sector entities
action of security components. to meet their goals. For CSD, SCAP is a critical component
of the SCAP Validation Program, the National Vulnerability
Additionally, CSD is working with the vulnerability
Database (NVD), and the National Checklist Program (NCP).
community to enable the automated analysis of metrics
such as the Common Vulnerability Scoring System (CVSS), In September 2012, CSD published SP 800-126
establishing a baseline of the minimum information needed Revision 2, The Technical Specification for the Security
to properly inform the vulnerability management process, Content Automation Protocol (SCAP): SCAP Version 1.2.
and facilitating the sharing of vulnerability information That document describes the 11 component specifications
across language barriers. To assist in this work, a public draft composing SCAP. See Table 2 (below): SCAP 1.2 Specifications
of NISTIR 8138, Vulnerability Description Ontology (VDO): A for details.
Framework for Characterizing Vulnerabilities, was created
Since the release of SCAP 1.2, CSD has worked to
to foster a conversation and collect feedback on the best
improve guidance around the use of SCAP specifications. In
mechanisms to improve the degree of automation within
FY 2015, CSD released draft NISTIR 8058, Security Content
vulnerability management processes. CSD is planning to
Automation Protocol (SCAP) Version 1.2 Content Style
develop this document iteratively with the vulnerability
Guide: Best Practices for Creating and Maintaining SCAP
community to ensure participation from as many
1.2 Content, which provides guidance for SCAP 1.2 content
stakeholders as possible.
creators to ensure that stylistic variations in SCAP 1.2
Security automation standardization work has been content are addressed in a way that improves the accuracy
focused in three areas: the evolution and international and consistency of results, avoids performance problems,
adoption of the Security Content Automation Protocol reduces user effort, lowers content maintenance burdens, and
(SCAP), the development of software asset management enables content reuse. To achieve this, the report documents
standards to support operational and cybersecurity best practices for content creation and encourages their use
use cases, and the development of security automation by SCAP content authors and maintainers. Feedback on
consensus standards. The following sections detail this work. this report is welcomed and will help CSD to work toward
producing a final version of this document.
Security Content Automation Protocol
(SCAP) CSD is actively working on an SCAP 1.3 revision. In July
2016, CSD posted drafts for public comment of SP 800-126
SCAP is a multipurpose protocol that provides an
Revision 3 and SP 800-126A. SP 800-126 Revision 3, is The
automated means to collect and assess the state of devices.
Technical Specification for the Security Content Automation
SCAP supports automated vulnerability checking, verifying
Protocol (SCAP): SCAP Version 1.3. SP 800-126A is SCAP 1.3
the installation of patches, checking security configuration
Component Specification Version Updates: An Annex to NIST
settings, verifying technical-control compliance, measuring
Special Publication 800-126 Revision 3. These publications
security, and examining systems for indicators of a
collectively document the draft requirements for SCAP 1.3.
compromise. SCAP uses the Extensible Markup Language
SP 800-126A is a new publication that allows SCAP 1.3 to
(XML) to standardize the format and nomenclature by which
take advantage of selected minor version updates of SCAP
security software products communicate information about
component specifications, as well as designated Open
software flaws, security configurations, and other aspects of
Vulnerability and Assessment Language (OVAL) platform
the device state. SCAP enables security automation content,
schema revisions. The SCAP 1.3 revision includes the
also known as “SCAP content,” to be expressed using
following changes:
standardized formats, identifiers, and scoring models. This
• Adoption of the Open Vulnerability and
content can be used by any tool that is conformant to the
Assessment Language (OVAL) 5.11.1, which was
specifications to collect and evaluate the state of software
released in April 2015;
installed on a device.
• Adoption of the Common Vulnerability Scoring
SCAP has been widely adopted by major software
System (CVSS) v3, which was released in June
and hardware manufacturers and has become a significant
2015;
component of information-security-management and
governance programs. SCAP-enabled tools are currently • Removal of support for CVSSv2; and
being used by the U.S. Government, critical infrastructure
• Deprecation of support for older specification
companies, academia, and other businesses, both
revisions and SCAP 1.0.
domestically and internationally. Currently, CSD is leveraging 83
SCAP in multiple areas, both to support its own mission
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

TABLE 2: SCAP 1.2 SPECIFICATIONS
SPECIFICATIONS DESCRIPTION
Languages
Extensible Configuration Checklist Description Format Used for authoring security checklists/benchmarks and
(XCCDF) 1.2 for reporting the results of evaluating them
Open Vulnerability and Assessment Language (OVAL) Used for representing system-configuration information,
5.11.1 assessing machine state, and reporting assessment results
Used for representing checks that collect information from
Open Checklist Interactive Language (OCIL) 2.0 people or from existing data stores populated by other
data collection methods
Reporting Formats
Used to express information about assets and to define
Asset Reporting Format (ARF) 1.1
the relationships between assets and reports
Used to uniquely identify assets based on known
Asset Identification 1.1
identifiers and other asset information
Identification Schemes
A nomenclature and dictionary of hardware, operating
Common Platform Enumeration (CPE) 2.3 systems, and applications; a method to identify the
applicability to platforms
A structured metadata format for describing a released
Software Identification (SWID) Tags 2015
software product
A nomenclature and dictionary of software-security
Common Configuration Enumeration (CCE) 5
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
CSD is currently considering the public feedback CSD is also starting to plan a SCAP 2.0 release. This release
received on the drafts while preparing the final versions of will further define the interfaces and use of transport protocols
these publications for release in early FY 2017. CSD is also for SCAP tools to provide component-level interoperability
working on an updated version of SCAPVal, the SCAP content between products supporting various SCAP functions.
validation tool. Once the specification revision is complete, By providing more interoperability, SCAP v2 will provide
CSD will also work to update the SCAP Validation Program to the basic software and configuration posture information
84
support SCAP 1.3. More information on SCAP 1.3 can be found needed to make and automate management decisions for
at: https://scap.nist.gov/revision/1.3/. networked devices as part of the license, vulnerability and
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 34: SWID Tags Support the Software Product Lifecycle
configuration management practices, supporting improved  software licenses, managing software vulnerabilities and
networked  device  hygiene.  Furthermore,  the  posture  related software patches, and assessing secure software
| information provided by SCAP v2 products will provide  |     |     |     |     |     |     |     | configurations. |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
much of the context needed to prevent, detect, and respond
|     |     |     |     |     |     |     |     | To  supplement  | the  requirements  | in  | ISO/IEC  | 19770- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------------ | --- | -------- | ------ |
to network attacks. This additional context will enable SCAP
2:2015, CSD collaborated with DHS, NSA, and MITRE on the
v2 information to be applied for application whitelisting, the
development of NISTIR 8060, Guidelines for the Creation
detection of anomalous behavior, the gathering and use of
|     |     |     |     |     |     |     |     | of  Interoperable  | Software  Identification  |     | (SWID)  | Tags.  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ------------------------- | --- | ------- | ------ |
indicators, the use of machine-readable threat information,
NISTIR 8060, published in April 2016, provides an overview
and orchestrating courses of action. CSD is preparing a draft
of the capabilities and usage of SWID tags as part of a
whitepaper for release in early FY 2017 that will outline an
|            |                 |     |       |              |     |      |           | comprehensive  | software  lifecycle.  | This  | report  | introduces  |
| ---------- | --------------- | --- | ----- | ------------ | --- | ---- | --------- | -------------- | --------------------- | ----- | ------- | ----------- |
| approach,  | a  development  |     | plan  | identifying  |     | the  | new  and  |                |                       |       |         |             |
SWID tags in an operational context, provides guidelines for
revised specifications that will be needed, and a transition
the creation of interoperable SWID tags, and highlights key
plan for moving from SCAP 1.x to SCAP 2.0.
usage scenarios for which SWID tags are applicable. Figure
Software Asset Management Standards 34 illustrates several types of SWID tags and how these
support multiple elements of the software product life cycle,
| CSD  | has  been  | collaborating  |     | with  | industry  |     | partners  |     |     |     |     |     |
| ---- | ---------- | -------------- | --- | ----- | --------- | --- | --------- | --- | --- | --- | --- | --- |
including deployment, installation, patching, upgrading and
| in  support  | of  | ISO/IEC’s  | revision  |     | of  standard  |     | ISO/IEC  |     |     |     |     |     |
| ------------ | --- | ---------- | --------- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- |
removal.
| 19770-2:2009,  |     | Information  |     | technology—Software  |     |     | asset  |     |     |     |     |     |
| -------------- | --- | ------------ | --- | -------------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
Additionally, NIST has worked with the TCG to integrate
| management—Part  |     | 2:  | Software  | identification  |     | tag,  | which  |     |     |     |     |     |
| ---------------- | --- | --- | --------- | --------------- | --- | ----- | ------ | --- | --- | --- | --- | --- |
SWID tags into the Trusted Network Communications (TNC)
establishes a specification for tagging software to support
protocol, through the SCAP Messages for IF-M specification.
| identification  | and  | management.  |     | An  | updated  | revision  | of  |     |     |     |     |     |
| --------------- | ---- | ------------ | --- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- |
this  standard,  ISO/IEC  19770-2:2015,  was  published  on  The information provided within SWID tags enhances
October 1, 2015. The software identification (SWID) data  the SCAP use cases by providing authoritative information
model defined by this standard describes an XML format for  that can be used to create Common Platform Enumeration
software publishers to provide authoritative identification,  (CPE) names, to support the targeting of checklists, and to
categorization,  software  relationships  (e.g.,  dependency,  associate software flaws to products, based on a defect in a
bundling,  and  patch),  executable  and  library  footprint  software library or executable. CSD is currently working on
details, and other metadata for software. This information  a SWID tag validation tool, called SWIDVal, that will validate
can be used to support operational and cybersecurity use  a SWID tag document against the ISO/IEC 19770-2:2015
cases around managing software deployments, managing  and NISTIR 8060 requirements. This tool is planned for an  85
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

early access release in FY 2017. CSD is also planning to work For more information, please refer to: http://datatracker.
on a revision of NISTIR 8060 with additional tag signature ietf.org/wg/sacm/charter/
requirements for release in late FY 2017.
Also, within the IETF, CSD has been collaborating
Development of Security Automation with the Managed Incident Lightweight Exchange (MILE)
Consensus Standards working group in order to develop the Resource-Oriented
Lightweight Information Exchange (ROLIE) specification.
CSD has been promoting the broad international adoption
This specification seeks to address the security automation
of SCAP by encouraging the integration of SCAP into other
information discovery and dissemination use cases by
standards, and by adapting SCAP to address specific gaps
defining how tools are expected to communicate with security
and challenges. CSD has continued its collaboration with
automation information repositories. ROLIE allows for the
its industry partners in the IETF Security Automation and
transport, retrieval, and storage of any security automation-
Continuous Monitoring (SACM) working group. This working
relevant information types. The ROLIE draft has undergone
group provides a venue for advancing appropriate SCAP
two major revisions, with the final draft nearing completion.
specifications into international standards and addressing
In addition, CSD has begun the process of collaborating with
identified gap areas. The current scope of work for SACM
MILE and other stakeholders to create extension drafts for
includes identifying and/or defining the transport protocols
ROLIE that address a number of information types, including
and data formats needed to support the collection and
vulnerability, configuration checklist, and software metadata
evaluation of a device state against the expected values.
information types.
The SACM working group has been working on identifying
The main ROLIE draft can be found at https://datatracker.
use cases, requirements, and architectural models to
ietf.org/doc/draft-ietf-mile-rolie/. Additional information on
provide information to facilitate decisions about existing
ROLIE and on the extension drafts can be found in the working
specifications and standards that can be referenced, required
repository on GitHub: https://github.com/CISecurity/ROLIE/.
modifications or extensions to existing specifications and
standards, and any gaps that need to be addressed. CSD is CSD also worked with its government and industry
working with DHS, the Center for Internet Security (CIS), and partners in the TCG to define a number of specifications
the TCG to bring existing work into the IETF SACM working related to the TNC protocol. The first such publication is the
group, including OVAL and specifications related to the TNC TNC SCAP Messages for IF-M specification that supports
protocol. carrying the SCAP content and results over the TNC protocols.
The second is the TNC Enterprise Compliance Profile (ECP)
The working group has been developing the following
and related specifications that support the exchange of SWID
Internet Drafts:
data over the TNC protocols. The ECP enables the collection
of SWID data from a device for use by external tools to
provide software inventory information. SCAP and SWID
data collected using these mechanisms may be optionally
used for network access control decision making, allowing
the device state to be evaluated when devices connect and
on an ongoing basis thereafter.
INTERNET DRAFT PURPOSE
https://datatracker.ietf.org/doc/draft-ietf-sacm- Definition of the common terminology used within several
terminology/ working-group documents.
https://datatracker.ietf.org/doc/draft-ietf-sacm- Listing architectural and specification requirements for
requirements/ SACM specifications.
Definition of the SACM architecture to provide information
https://datatracker.ietf.org/doc/draft-ietf-sacm-
for the development of methods to exchange security
architecture/
automation information (i.e., transports).
https://datatracker.ietf.org/doc/draft-ietf-sacm- Definition of the SACM information model to provide
86
information-model/ information for the development of data models.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

For more information on these specifications, CONTACT:
please visit: http://www.trustedcomputinggroup.org/
Mr. David Waltermire
resources/tnc_scap_messages_for_ifm, and http://www.
(301) 975-3390
trustedcomputinggroup.org/resources/tnc_endpoint_
david.waltermire@nist.gov
compliance_profile_specification.
Updated versions of the ECP and SWID related
specifications, along with a usage scenario around Security Automation Reference
vulnerability assessment are currently being worked on Data
in the SACM working group, which available through the
Through the NVD and the NCP (see below), NIST is
following locations:
providing relevant and important reference data in the areas
https://datatracker.ietf.org/doc/draft-haynes-sacm- of vulnerability and configuration management. SCAP and
ecp/ the programs that leverage it are moving the information
assurance industry toward being able to standardize
https://datatracker.ietf.org/doc/draft-coffin-sacm-nea-
communications and toward the collection and storage of
swid-patnc/
relevant data in standardized formats, as well as providing
https://datatracker.ietf.org/doc/draft-ietf-sacm-vuln-
an automated means for the assessment and remediation
scenario/
of systems for both vulnerabilities and configuration
Additionally, CSD has several members who are actively compliance.
engaged on the CVE Board, which is working to improve
the assignment of CVE identifiers for vulnerabilities, with National Vulnerability Database
the overall goal of improving the automated processing of
(NVD)
vulnerabilities and the timeliness of CVE identifier issuance.
Security automation reference data is currently housed
Finally, CSD has worked with the FIRST by participating
within the NVD. The NVD is a comprehensive cybersecurity
in two Special Interest Groups (SIGs). The CVSS SIG (CVSS-
vulnerability database that allows the tracking of vulnerability
SIG) is focused on maintaining and improving the CVSS
trends over time. This trending service allows users to assess
scoring model, based on community feedback. The CVSS-
changes in vulnerability discovery rates within specific
SIG published CVSS Revision 3 (CVSS v3) in June 2015. The
products or within specific types of vulnerabilities. NVD
second SIG, the Vulnerability Reporting and Data eXchange
data is represented using the SCAP specifications. The NVD
SIG (VRDX-SIG), researches and recommends methods for
includes databases of security configuration checklists for
identifying and exchanging vulnerability information across
the NCP, listings of publicly known software flaws, product
disparate vulnerability databases.
names, and impact metrics. A formal validation program
For more information, please visit: http://www.first.org/ tests the ability of vendor products to use some forms of
global/sigs. security automation data, based on a product’s conformance
in support of specific enterprise capabilities.
Through work with international standards-developing
organizations (SDOs), SCAP and its related security SCAP defines the structure of standardized software
automation capabilities are expected to evolve and expand flaws and security configuration reference data, also known
in support of the growing need to define and measure as SCAP content. This reference data is provided by the NVD.
effective security controls, assess and monitor ongoing
As of the end of September 2016, the NVD contained
aspects of information security, remediate noncompliance,
the following resources:
and successfully manage systems in accordance with the Risk
• Over 79,000 vulnerability advisories, with an
Management Framework described in SP 800-37 Revision
average of 30 new vulnerabilities added daily;
1, Guide for Applying the Risk Management Framework to
Federal Information Systems: A Security Life Cycle Approach. • 83 SCAP-expressed checklists containing
Standards that are developed and published by these SDOs thousands of low-level security configuration
will be considered for inclusion in future revisions of SCAP. checks that can be used by SCAP-validated
security products to perform automated
FOR MORE INFORMATION, SEE:
evaluations of the system state;
http://scap.nist.gov/
• 293 non-SCAP security checklists (e.g., English
prose guidance and configuration scripts); 87
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

• 249 U.S. Computer Emergency Readiness Team addition, identifying a reasonable set of security settings
(US-CERT) alerts; 4,458 US-CERT vulnerability that achieve balanced risk management is a complicated,
summaries; and 10,286 SCAP machine-readable arduous, and time-consuming task, even for experienced
software flaw checks; and system administrators.
• A product dictionary with over 115,000 operating To facilitate the development of security configuration
system, application, and hardware name entries; checklists for IT products and to make checklists more
and over 63,900 vulnerability advisories translated organized and usable, CSD established the National Checklist
into Spanish. Program (NCP) in furtherance of its statutory responsibilities
under the Federal Information Security Management Act
NVD is hosted and maintained by NIST and is sponsored
(FISMA) of 2002, Public Law 107-347, and also under the
by the Department of Homeland Security’s US-CERT.
Cybersecurity Research and Development Act, which
The use of SCAP data by commercial security products,
mandates that NIST “develop, and revise as necessary, a
deployed in thousands of organizations worldwide, has
checklist setting forth settings and option selections that
extended NVD’s effective reach. Increasing demand for NVD
minimize the security risks associated with each computer
XML data feeds (i.e., mechanisms that provide updated data
hardware or software system that is, or is likely to become,
from data sources) and SCAP-expressed content from the
widely used within the Federal Government.” In February
NVD website demonstrates an increased adoption of SCAP.
2008, a revision of Part 39 of the Federal Acquisition Regulation
The NVD continues to play a pivotal role in the Payment (FAR) was published. Paragraph (d) of section 39.101 states,
Card Industry (PCI) efforts to mitigate vulnerabilities in credit “In acquiring information technology, agencies shall include
card systems. The PCI mandates the use of NVD vulnerability the appropriate IT security policies and requirements,
severity scores in measuring the risk to payment card servers including use of common security configurations available
worldwide and for prioritizing vulnerability patching. The from the NIST website at http://checklists.nist.gov. Agency
PCI’s use of NVD severity scores helps enhance credit card contracting officers should consult with the requiring official
transaction security and protects consumers’ personal to ensure the appropriate standards are incorporated.”
information.
In Memorandum M-08-22, OMB mandated the use of
In the past year, the NVD began providing Common SCAP-validated products for the continuous monitoring of
Vulnerability Scoring System (CVSS) base scores following Federal Desktop Core Configuration (FDCC) compliance. The
the CVSS v3 specification and will soon include this NCP strives to encourage and assist federal agencies with
information in the data feeds (see https://www.first.org/ these mandates.
cvss/specification-document). An update of the web site is
The goals of the NCP are to:
planned to enhance the user’s experience.
• Facilitate the development and sharing of checklists
FOR MORE INFORMATION, SEE:
by providing a formal framework for checklist
developers to submit checklists to NIST;
https://nvd.nist.gov
• Provide guidance to developers to help them create
CONTACTS: standardized, high-quality checklists that conform
to common operation environments;
Mr. Harold Booth Mr. Robert Byers
(301) 975-8441 (301) 975-3279 • Help developers and users by providing guidelines
harold.booth@nist.gov robert.byers@nist.gov for making checklists better documented and more
usable;
National Checklist Program (NCP) • Encourage software vendors and other parties to
develop checklists;
There are many threats to IT, ranging from remotely
• Provide a managed process for the review, update,
launched network service exploits to malicious code spread
and maintenance of checklists;
through infected emails, websites, and downloaded files.
Vulnerabilities in IT products are discovered daily, and many • Provide an easy-to-use repository of checklists;
ready-to-use exploitation techniques are widely available on and
the Internet. Because IT products are often intended for a
• Encourage the use of automation technologies
wide variety of audiences, restrictive security configuration
(e.g., SCAP) for checklist application.
88 controls are usually not enabled by default. As a result, many
out-of-the box IT products are immediately vulnerable. In
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

At the end of FY 2016, there are a total of 367 checklists CONTACT:
posted on the NCP website (see http://checklists.nist.gov).
Mr. Stephen Quinn
Of that total, 154 of the checklists, addressing 96 platforms,
(301) 975-6967
are SCAP-expressed and can be used with SCAP-validated
stephen.quinn@nist.gov
products.
Organizations can use checklists obtained from the
NCP website for automated security configuration patch Apple OS X Security
assessment. The NCP currently provides metadata and links Configuration
to the latest operating systems and applications checklists,
CSD’s OS X security configuration team is working to
including MacOS 10.10, Windows 10, Internet Explorer 11.0,
develop secure system configuration baselines supporting
Internet Explorer 10.0, Office 2016, Red Hat Enterprise Linux,
different operational environments for Apple OS X Version
and other products.
10.10, “Yosemite.” These configuration guidelines will assist
To assist users in identifying automated checklist content, organizations with hardening OS X technologies and provide
NCP groups these checklists into tiers, from Tier I to Tier IV. a basis for unified controls and settings for OS X workstations
The NCP uses the tiers to rank checklists according to their and for mobile system security configurations for federal
automation capability. Tier III and IV checklists include fully agencies. The configurations are based on a collection of
vetted SCAP content that has successfully demonstrated resources, including the existing NIST OS X configuration
conformance to the requirements outlined in SP 800-126. guidance, the DOD OS X Recommended Settings, the
Tier III & IV checklists are considered production-ready and Defense Information Systems Agency (DISA) OS X Security
are intended for use with SCAP-validated products. Technical Implementation Guide (STIG), and the Center for
Internet Security (CIS) OS X Security Benchmark.
Tier II checklists document the recommended security
settings in a machine-readable format such as the XCCDF- The project team researched and tested 250 settings
only (i.e., no OVAL content), proprietary format, or product- for OS X 10.10. Among other collected data, each setting has
specific configuration script. Tier I checklists are prose- a designated Common Configuration Enumeration (CCE)
based and contain no machine-readable content. Users can number, which aids in long-term tracking of the setting.
browse the checklists, based on the checklist tier, IT product, Figure 35 illustrates the various categories that comprise
IT product category, or authority, and through a keyword the baselines. Note that a higher quantity of settings in a
search that searches the checklist name and summary for category does not imply greater importance over other
user-specified terms. The search results show the detailed categories.
checklist metadata and a link to any SCAP content for
The team finished developing shell scripts that apply the
the checklist, as well as links to any supporting resources
settings to an OS X 10.10 system. The settings are organized
associated with the checklist.
into three key baselines, which are appropriate for different
To assist checklist developers, the NCP provides both environments:
manual and automated interfaces to facilitate the submission
• The Standalone baseline describes small, informal
and maintenance processes. The manual interface consists
computer installations that are used for home or
of a web application that guides the submitter through the
business purposes,
data entry process to ensure that all the required information
• The Managed baseline is appropriate for centrally
is submitted. The submission is validated upon review,
managed, networked systems, and
and a report is returned to the submitting organization,
verifying either acceptance or rejection, based on the criteria • The Specialized Security-Limited Functionality
requirements. For instance, Tier III and Tier IV checklists (SSLF) baseline is appropriate for systems where
require validation using the SCAP Content Validation Tool security requirements are more stringent and
(this tool is available for download via https://scap.nist.gov/ where the implementation of security safeguards is
validation/resources.html). likely to reduce functionality.
The NCP is defined in SP 800-70 Revision 3, National In FY 2016, the security configuration was updated to
Checklist Program for IT Products—Guidelines for Checklist have 250 settings after the internal testing on select CSD
Users and Developers, which can be found at http://csrc.nist. systems was completed. In June 2016, the draft SP 800-
gov/publications/PubsSPs.html. 179, Guide to Securing Apple OS X 10.10 Systems for IT
Professionals, was published for public comment
FOR MORE INFORMATION, SEE: 89
https://checklists.nist.gov
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
https://dx.doi.org/10.6028/NIST.SP.800-195

Figure 35: Configuration Categories
(see https://csrc.nist.gov/publications/ Search?request other sections of this report. SCAP will be used to
SeriesList==1,&requestStatusList=1,3,&requestDisplay express configuration settings and check system
Option=brief&requestSortORder=5&itemsPerPage= All). configuration compliance.
FOR MORE INFORMATION, SEE:
The purpose of this document is to explain the
http://csrc.nist.gov/projects/apple-os/
settings, their security significance, and how to configure
them for the three baselines described above. All feedback
https://github.com/usnistgov/applesec
received during the comment period was addressed and
incorporated into the draft document. CONTACTS:
In FY 2017, the team plans on accomplishing the following:
Mr. Mark Trapnell Mr. Lee Badger
• Complete the final version of SP 800-179, Guide (301) 975-4091 (301) 975-3176
to Securing Apple OS X 10.10 Systems for IT mark.trapnell@nist.gov lee.badger@nist.gov
Professionals;
Mr. Murugiah Souppaya
• Continue to refine the script and add more settings
(301) 975-8443
to the configuration;
murugiah.souppaya@nist.gov
• Update the security configuration guide for MacOS
10.12; and
• Investigate translating security guidance into the
90 SCAP format, which is defined and discussed in
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

TECHNICAL SECURITY  particular, CSD has devised a biodiversity-inspired metric
based on the effective number of distinct resources. CSD
METRICS
has also proposed two complementary diversity metrics,
|     |     |     |     |     |     |     |     | based  on  | the  least  | and  | the  average  |     | attacking  | efforts,  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---- | ------------- | --- | ---------- | --------- |
Security Risk Analysis of  respectively. CSD published two papers in this area:
Enterprise Networks Using Attack
|        |     |     |     |     |     |     |     | 1.  Network Diversity: A Security Metric for Evaluating  |             |     |           |     |          |            |
| ------ | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | ----------- | --- | --------- | --- | -------- | ---------- |
| Graphs |     |     |     |     |     |     |     | the                                                      | Resilience  | of  | Networks  |     | Against  | Zero  Day  |
Attacks, IEEE Transactions on Information Forensics
The protection of computer networks from malicious
intrusions is critical to the economy and security of the  and Security, 11(5) May 2016 (see http://ieeexplore.
ieee.org/document/7378495/).
nation. Vulnerabilities are regularly discovered in software
| applications  | that  | are  exploited  |     | to  stage  | cyber  | attacks.  |     |                   |     |           |     |           |        |       |
| ------------- | ----- | --------------- | --- | ---------- | ------ | --------- | --- | ----------------- | --- | --------- | --- | --------- | ------ | ----- |
|               |       |                 |     |            |        |           |     | 2.  Diversifying  |     | Networks  |     | Services  | under  | Cost  |
System administrators need objective metrics to guide and  Constraints for Better Resilience against Unknown
justify decision making as they manage the security risk  Attacks,  30th  International  Federation  for
of enterprise networks. The objective of this research is  Information Processing (IFIP) Conference on Data
to develop a standard model for the security risk analysis  and Application Security and Privacy, Trento, Italy,
of computer networks. A standard model will enable an
|     |     |     |     |     |     |     |     | July  | 18th  | to  21st  2016  | (see  | http://ws680.nist.gov/ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --------------- | ----- | ---------------------- | --- | --- |
organization to answer questions such as “Are we more  publication/get_pdf.cfm?pub_id=920658).
secure now than yesterday?” or “How does the security of
In FY 2017, CSD plans to develop new techniques and
| one  network  | configuration  |     | compare  | with  | another  |     | one?”  |     |     |     |     |     |     |     |
| ------------- | -------------- | --- | -------- | ----- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
metrics for Cloud Computing threat modeling and network
Also, having a standard model to measure network security
forensics analysis using Bayesian networks. CSD also plans
| will  allow  | users,  | vendors,  | and  | researchers  |     | to  evaluate  |     |     |     |     |     |     |     |     |
| ------------ | ------- | --------- | ---- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
to publish the results as a NIST report and as white papers in
| methodologies  |     | and  products  |     | for  network  | security  |     | in  a  |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | ------------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
conferences and journals.
coherent and consistent manner.
FOR MORE INFORMATION, SEE:
CSD has approached the challenge of network security
analysis  by  capturing  vulnerability  interdependencies  http://csrc.nist.gov/groups/SNS/security-risk-analysis-
and measuring security, based on how real attackers have
enterprise-networks/
penetrated networks. The methodology used for security
| risk analysis is based on attack graphs. CSD analyzes attack  |     |     |     |     |     |     |     | CONTACT: |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
paths through a network, providing a probabilistic metric
Dr. Anoop Singhal
of the overall system risk. Through this metric, trade-offs
(301) 975-4432
between security costs and security benefits are analyzed.
anoop.singhal@nist.gov
Computer systems are vulnerable to both known and
zero-day attacks. Enterprises have begun to move parts
Algorithms for Intrusion
| of  their  | networks  | from  | a  traditional  |     | infrastructure  |     | into  |     |     |     |     |     |     |     |
| ---------- | --------- | ----- | --------------- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Measurement
| cloud  computing  |     | environments.  |     | Cloud  | providers  |     | offer  |     |     |     |     |     |     |     |
| ----------------- | --- | -------------- | --- | ------ | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
virtual servers that can be rented on demand by users. This
|     |     |     |     |     |     |     |     | The  | Algorithms  | for  | Intrusion  | Measurement  |     | (AIM)  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | ---- | ---------- | ------------ | --- | ------ |
paradigm enables cloud customers to acquire computing  project  furthers  measurement  science  in  designing  and
resources with high efficiency, low cost and great flexibility.
|     |     |     |     |     |     |     |     | implementing  | algorithms  |     | to  both  | detect  | attackers  | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | --------- | ------- | ---------- | ---- |
However, it also introduces many security problems that need
limit their ability to intrude into a system. Most of the
to be solved. Diversity has long been regarded as a security  work leverages graph theory (the math of dots and lines)
mechanism for improving the resilience of software and
and algorithmic complexity analysis (the math around fast
networks against various attacks. More recently, diversity has  computation).  In  performing  this  work,  the  AIM  project
found new applications in cloud computing security, moving
seeks to enhance the nation’s ability to defend itself from
target defense, and improving the robustness of network
network-borne attacks.
routing. However, most existing efforts rely on intuitive and
|     |     |     |     |     |     |     |     | This  scientific  |     | research  | is  conducted  |     | in  | partnership  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | -------------- | --- | --- | ------------ |
imprecise notions of diversity, and the few existing models
with the Army Research Laboratory (ARL), the University
of diversity are designed for a single system running diverse
|     |     |     |     |     |     |     |     | of  Maryland,  | and  | the  Center  | for  | Applied  | Internet  | Data  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ------------ | ---- | -------- | --------- | ----- |
software replicas or variants. In FY 2016, CSD has attempted
|     |     |     |     |     |     |     |     | Analysis.  | ARL’s  | participation  | helps  | focus  | the  | work  on  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | -------------- | ------ | ------ | ---- | --------- |
to formally model network diversity as a security metric by
solving immediate critical problems facing U.S. Government
91
designing and evaluating a series of diversity metrics. In
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

networks. However, research solutions are made publicly Automated Combinatorial Testing
available and are designed to be generally applicable to as
Software developers often encounter failures that result
many environments as possible.
from an unexpected interaction between components. NIST
In FY 2016, the AIM project completed research in several investigation of actual failures has shown that most failures
areas: algorithms for measuring the ease at which networks are triggered by one or two parameters, and progressively
can be broken apart, efficient representations for attack fewer by three, four, or more parameters (see Figure 36 - next
graphs, and an analysis of how to increase the robustness page); this relationship is called the Interaction Rule. These
of the African Internet. More specifically, the project team results have important implications for testing software
accomplished the following: and systems. If all faults in a system can be triggered by a
• The team discovered a linear-time algorithm to combination of n or fewer parameters, then testing all n-way
implement a heuristic for vertex partitioning that combinations of parameters with a doable number of tests
enables effective partitioning on massive graphs can provide strong fault-detection efficiency. These methods
(tested on graphs up to 34 million nodes). This are being applied to software and hardware testing for
enables one to measure the ease at which terrorist reliability, safety, and security. CSD’s focus is on empirical
activity or global conflicts can break apart large results and the impact on real-world problems.
networks, for example, the entire Internet (the Project highlights for FY 2016 include the development
research was published in the International Journal of an efficient method for testing rule-based systems using
of Computer Science: Theory and Application). covering arrays and the development of a prototype tool;
• The team discovered an efficient representation invited lectures at conferences and universities; leading the
for attack graphs that grows linearly in the number Fifth International Workshop on Combinatorial Testing, held in
of nodes, while most attack graph research uses conjunction with the eighth IEEE International Conference on
an inefficient graph representation that grows Software Testing; development of a real-time combinatorial
quadratically in the number of nodes and that coverage measurement tool; and analyzing the factors
creates unnecessary edge connections (this involved in different types of software faults. Collaborators
research was published in the proceedings of include researchers from the University of Texas at Arlington,
the Tenth International Conference on Software the University of Texas at Dallas, East Carolina University, and
Engineering Advances). Duke University.
• The team studied how to increase the robustness NIST also submitted a patent on an oracle-free testing
of the African Internet, creating the first country- method based on two-layer covering arrays (see below). In
level topology maps of Africa, and measured the software testing, the oracle problem refers to determining the
growth of Internet connectivity (this research was expected output for a given set of inputs. A determination of
a precursor to more global connectivity studies; the expected output requires expert knowledge and normally
it was published in the proceedings of the 7th cannot be automated without a mathematical model of
European Alliance for Innovation International the specification. The test settings for an input factor may
Conference on e-Infrastructure and e-Services for represent ranges of values (called equivalence classes) for
Developing Countries). which the output is expected to remain unchanged. For
example, a shipping program may charge the same rate for
In FY 2017, the AIM project will work on new methods
any package under one pound, a second rate for packages
for assuring private communication on the Internet, network
one pound to 10 pounds, and a third rate for packages over
anomaly detection, efficient graph algorithms for access
10 pounds. Values within each of these ranges are equivalent
control computations (to restrict external leakage of insider
with respect to the cost calculation. Thus, any value within an
information), and methods for using attack graphs to perform
equivalent range may be substituted for any other, and the
defense-in-depth measurements.
program output should be unchanged. Similarly, equivalent
FOR MORE INFORMATION, SEE: values for any combination of input variables will also
produce the same output.
http://csrc.nist.gov/projects/aim/
The test method works by generating two test arrays: a
CONTACT: primary array and a secondary array. The entries of a primary
array represent the names of equivalence classes of input
Mr. Peter Mell
factors. For each test row of the primary array, a second
92 (301) 975-5572
array is computed. The settings in the second array are the
peter.mell@nist.gov
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Figure 36: Interaction Rule Graph
| values from equivalence classes corresponding to the names  |     |     |     |     | CONTACTS: |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
of equivalence classes in the primary array. If the outputs
|     |     |     |     |     | Mr. Rick Kuhn  |     |   Dr. Raghu Kacker  |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | ------------------- | --- | --- |
corresponding to one row of the primary array differ, then
either the equivalence classes were defined incorrectly or  (301) 975-3337    (301) 975-2109
|     |     |     |     |     | kuhn@nist.gov   |     |   raghu.kacker@nist.gov |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | ----------------------- | --- | --- |
the code is faulty in some way. This method can detect a
large class of software faults automatically after equivalence
| classes  | have  been  defined,  | without  | a  conventional  | test  |     |     |     |     |     |
| -------- | --------------------- | -------- | ---------------- | ----- | --- | --- | --- | --- | --- |
Roots of Trust
oracle.
|     |     |     |     |     |     | Modern  | computing  | devices  | consist  of  various  |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | -------- | --------------------- |
Technology transfer activities included the publication
hardware, firmware, and software components at multiple
of a number of technical papers and software distributions;
|     |     |     |     |     | layers  | of  abstraction.  | Many  | security  | and  protection  |
| --- | --- | --- | --- | --- | ------- | ----------------- | ----- | --------- | ---------------- |
publication of the results of a Cooperative R&D (CRADA)  mechanisms are currently rooted in software that, along
| project  | with  Lockheed  | Martin;  | release  | of  enhanced  |     |     |     |     |     |
| -------- | --------------- | -------- | -------- | ------------- | --- | --- | --- | --- | --- |
with all underlying components, must be trusted and not
combinatorial  measurement  tools;  input  modeling  and  tampered with. A vulnerability in any of those components
fault location tools; a provisional patent application on the
|     |     |     |     |     | could  compromise  |     | the  | trustworthiness  | of  the  security  |
| --- | --- | --- | --- | --- | ------------------ | --- | ---- | ---------------- | ------------------ |
oracle-free testing method; and seminars at a number of
mechanisms that rely upon those components. Stronger
conferences, universities, and federal agencies. security assurances may be possible by grounding security
Plans  for  FY  2017  include  the  development  of  a  mechanisms in roots of trust.
mathematical model for the evolution of t-way faults in  Roots  of  trust  are  highly  reliable  and  secure
| software;  | combinatorial  | testing  | for  big  | data  software;  |     |     |     |     |     |
| ---------- | -------------- | -------- | --------- | ---------------- | --- | --- | --- | --- | --- |
hardware, firmware, and software components that perform
measurement  of  input  model  combination  coverage  of  specific, critical security functions. Because roots of trust
network protocol software; trial use of prototype methods
are inherently trusted, they must be secure by their design.
| and  tools  | for  oracle-free  | testing  | methods;  | analysis  of  |     |     |     |     |     |
| ----------- | ----------------- | -------- | --------- | ------------- | --- | --- | --- | --- | --- |
As such, many roots of trust are implemented in hardware
empirical data on failures; further development of methods  or protected firmware so that malware cannot tamper with
and tools for fault localization; and seminars, workshops,
the functions they provide. Roots of trust provide a firm
and tutorials at professional meetings and research labs. foundation from which to build security and trust.
FOR MORE INFORMATION, SEE:
This project aims to encourage the use of roots of trust in
computers to provide stronger security assurances. A focus
http://csrc.nist.gov/groups/SNS/acts/
area for this work has been securing firmware. Previous work
93
in this project described methods to protect boot firmware
PROGRAM AND PROJECT ACHIEVEMENTS  |  FY 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

as part of the NIST SP 800-147 series, now standardized 1. Password Research:
by ISO/IEC JTC 1/SC 27, IT Security Techniques, as ISO/
The password research included examining password
IEC 19678:2015, Information Technology – BIOS Protection
policies from two perspectives. The Password Policy
Guidelines. Building on this work in FY 2016, the project
Taxonomy project is exploring the relationship between
team researched techniques and requirements for securing
usability and security by focusing on the password policy
firmware throughout the platform. The goal of this effort is
itself and how users of a policy understand it. To tackle the
to protect platform firmware from unauthorized changes,
ambiguity inherent in many password policies, a formal
detect accidental or malicious corruption, and recover from
language for representing a password policy was previously
destructive attacks.
developed. Having clear, unambiguous policy statements
The results of this research will be documented in a new enables us to explore password policies in much greater
set of draft guidelines that are expected to be released in FY detail, discuss the relative merits of different statements,
2017. The upcoming draft guidelines will facilitate discussions compare and contrast policies, explore plain language policy
with industry, standards organizations, and consortiums over representations and user interpretations, and examine the
technologies, standards, and specifications that can support interplay between usability and security in password policies.
firmware protection, detection and recovery. A Password Policy Question-Answer System (PPQAS) was
designed, developed and tested. The system is a flexible
FOR MORE INFORMATION, SEE:
application and is designed to collect users’ interpretations
http://csrc.nist.gov/projects/root-trust/ of various password policies and map each interpretation of
a policy’s regulating statements to elements of the formal
CONTACT: language via a dynamic set of questions and answers and to
store those mappings for analysis.
Mr. Andrew Regenscheid
(301) 975-5155 The second effort examines how users interpret and
andrew.regenscheid@nist.gov apply password rules. Ambiguous terminology in password
rules affects user comprehension. This research investigated
user comprehension of ambiguous terminology in password
rules, using a combination of quantitative and qualitative
USABILITY AND SECURITY
methods in a usable security study with 60 participants.
Results showed:
Usability is an often overlooked but critical component • That manipulating password rule terminology
of cybersecurity. There is a belief that there is an inherent causes users’ interpretation of the allowed
tradeoff between cybersecurity and usability. Computers character space to shrink or expand.
can be theoretically secure but so unusable that they do • Users are confused by the terms “non-
not improve security because users are forced to perform alphanumeric,” “symbols,” “special characters,” and
in less secure ways. The opposite is true as well; systems “punctuation marks” in password rules.
that are easy to use and not secure are eventually unusable
• Additionally, users are confused by partial lists of
due to worms, viruses, and botnets. The usability principles
allowed characters using “e.g.” or “etc.”
of efficiency, effectiveness and user satisfaction must be
incorporated to ensure that it is easy for users to do the right This research provides data-driven usability guidance
thing and hard for them to do the wrong thing. NIST has been on constructing clearer language for password policies.
working to develop usability and security metrics, facilitate
the integration of usability principles into product design 2. Understanding User Behavior:
processes, and lead research projects to investigate methods
Understanding user behavior is critical to achieving
for aligning user goals with organizational security goals.
security objectives. One example of this achieving security
During FY 2016, the usability team’s research focused objectives is preventing successful phishing attacks. Phishing
primarily in four areas: passwords, understanding user is the attempt to obtain sensitive information by posing
behavior, cryptography, and privacy. as a trustworthy entity in an electronic communication,
often in the form of emails appearing to be from legitimate
parties that contains links or attachments. It is a major
94 cyber threat facing government organizations. To help
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

combat this threat, many organizations utilize some type This research on security fatigue was a popular topic
of phishing awareness training to make their staff more with users and many media outlets interested in it. According
aware of phishing threats and consequences. To ultimately to the NIST Public Affairs Office, there were:
improve awareness training, it is important to understand
• 17,550 page views of the news story on NIST.gov
why the staff do or do not fall victim to phishing attacks.
(the fourth most visited page in 2016 on the NIST
For example, an employee opening an email attachment
website);
could be a means of conducting the attack. This project
• 7.9K total views for Facebook posts on the
partnered with the NIST Office of Information Systems
story;
Management (OISM) and Office of Safety, Health and
Environment (OSHE) to better understand operational • 2,327 views of the story on Eurekalert (an online
phishing awareness training. Results showed that user news release repository operated by The American
context is the key to understanding user behavior regarding Association for the Advancement of Science
phishing attacks. For example, staff who are responsible for (AAAS));
paying bills and invoices are more likely to be victimized by
• 2,172 plays of the video on Kaltura (the platform
fake unpaid invoice emails.
hosting the video on the NIST news story page), 81
Another noteworthy program in user behavior is the shares, 51 downloads; and
research into Security Fatigue. People are repeatedly
• 918 video views on YouTube.
bombarded with messages about the dangers lurking
The news outlets included: BBC News, MSN.com,
on the Internet, about the security breaches of major
Politico, Federal News Radio, Bloomberg BNA, the Register,
corporations and the U.S. government, and about the need
and McClatchy DC, and many others included quotes by the
to be constantly attentive while online. To combat these
authors, such as: “ ‘Users are tired of being overwhelmed by
dangers and stay safe while online, users are forced to
the need to be constantly on alert…’ said the study by the
update passwords, run antivirus software programs, and
National Institute of Standards and Technology, a unit of the
accept unwieldy terms of agreements, often without a
Department of Commerce.”
clear understanding of why and to what end. The research
team interviewed 40 participants to understand their
relationships with cybersecurity. 3. Cryptography
The team’s cryptographic research is concerned with
creating a baseline understanding of the current practices
and challenges of organizations that are developing products
that use cryptography. The research team considered
the entire process, from the identification of a market
opportunity and the conceptualization of the product; the
assembling of the product team; the design, implementation
and testing of the product; and finally, the marketing, sale
and end-user support. Based on the research, ITL will use
this new understanding to help improve the assurance
of cryptographic tools and the usability of cryptographic
software and resources.
The team discovered that: The following contributions were made:
• People reach a saturation point and become inured • The research team identified opportunities to
to the issue of cybersecurity. better characterize the cryptographic practices
• People are told they need to be constantly on alert, and types of resources and standards used by
constantly doing “something,” but they are not cryptographic developers.
even sure what that something is or what might • Research offers new insights into the challenges
happen if they do or do not do it. that cryptographic implementations introduce
The team calls this “security fatigue.” This security fatigue into organizational practices, such as recruitment,
and the resignation and loss of control associated with it product lifecycle and transitions, the management
certainly presents a challenge to efforts aimed at promoting of employees, the evaluation of cryptographic
95
online security and the protection of online privacy. work, and product explanation to customers.
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: PROGRAM AND PROJECT ACHIEVEMENTS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

• The research team studied methods to quantify • Greene, K.K., and Choong, Y.Y. “Must I, Can I? I Don’t
and rank factors that developers consider Understand Your Ambiguous Password Rules.”
when evaluating the quality of a cryptographic This article was accepted on 09/12/2016 and will
implementation. appear in Issue 1 of the 2017 Volume of Journal of
Information and Computer Security.
4. Privacy • Stanton, B., Theofanos, M., Spickard Prettyman, S.,
A new area was initiated to examine privacy and de- Furman, S., “Security Fatigue”, IT Professional, Vol.
identification. A Federal Government stakeholder’s meeting 18, Issue 5, pp. 26-32, Sept.-Oct. 2016, doi:10.1109/
was organized to discuss the topic, after which NIST provided MITP.2016.84
additional guidance through multiple training sessions to • Stanton, B., Theofanos, M., Spickard Prettyman,
other federal agencies, a NIST Interagency Report, and a S., Furman, S. (2016). The Power of Qualitative
NIST Special Publication. Methods: Aha Moments in Exploring Cybersecurity
De-identification regarding private data set release, and Trust. User Experience Magazine, 16(5).
or the release of other information about a private data set Retrieved from http://uxpamagazine.org/the-
(such as summarizing statistics), is a class of procedures power-of-qualitative-methods/
intended to restrict or limit the ability of a recipient of • Steves, M., Theofanos, M., (2016) “What’s in your
such a release to re-identify a particular individual in the policy? Do your users know?” National Institute
data set and infer potentially sensitive information about of Standards and Technology Interagency Report
the individual (whether in an absolute, or in a probabilistic (NISTIR) that was submitted to IEEE Security and
sense). De-identification is a collection of methods with Privacy.
the goal of protecting the privacy of the individual, while
• Garfinkle, S., Theofanos, M. and Choong,Y.Y., “Secure
simultaneously preserving the utility of the released data (or
and Usable Enterprise Authentication: Lessons from
other summarizing statistics).
the Field,” to appear in IEEE Security & Privacy,
ITL researchers are evaluating differentially private September/October 2016, a special issue on usable
algorithms, a subset of de-identification techniques. The team security.
is considering the possible tradeoffs between protecting the
The proposed plans for FY 2017 for this project consist
privacy of individuals and the usefulness of information, such
of the following activities:
as might occur when a research database with de-identified
personal information is released. • Examine users in healthcare and their behaviors
and perceptions of security;
The following are the publications that were released for
the Usability and Security project during FY 2016: • Complete interviews with companies that develop
cryptographic products;
• N ISTIR 8080, Usability and Security Considerations
for Public Safety Mobile Authentication. (July 2016) • Perform usability testing on a password policy
(see http://nvlpubs.nist.gov/nistpubs/ir/2016/NIST. tool;
IR.8080.pdf) • Finalize usability chapters for the revision of 800-
• N ISTIR 8150, Government Data De-Identification 63, Digital Identity Guidelines;
Stakeholder’s Meeting, Meeting Report. (September • Extend the password rules comprehension
2016) (see http://nvlpubs.nist.gov/nistpubs/ir/2016/ research; and
NIST.IR.8150.pdf)
• Develop test methods for de-identification
• Choong, Y. Y., & Greene, K. K. (2016, September). algorithms.
What’s a Special Character Anyway? Effects
FOR MORE INFORMATION, SEE:
of Ambiguous Terminology in Password Rules.
Published in the Proceedings of the Human Factors https://csrc.nist.gov/Projects/Usability-Of-Security
and Ergonomics Society Annual Meeting (Vol. 60,
No. 1, pp. 760-764). Sage CA: Los Angeles, CA: CONTACTS:
SAGE Publications.
Ms. Mary Theofanos Mr. Brian Stanton
• Theofanos, M., Garfinkel, S. and Choong, Y.Y., (2016).
(301) 975-5889 (301) 975-2103
96 Secure and Usable Enterprise Authentication: maryt@nist.gov brian.stanton@nist.gov
Lessons from the Field. IEEE Security &
Privacy, 14(5), pp.14-21.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
https://dx.doi.org/10.6028/NIST.SP.800-195

HONORS AND AWARDS
This section recognizes ITL staff who have received honors and/or awards for
their cybersecurity accomplishments.
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Department of Commerce
Gold Medal Award
Leah Kauffman, Nathan Lesser, Timothy McBride, Gavin O’Brien, Lucy Salah, and
Karen Waltermire (Applied Cybersecurity Division, National Cybersecurity Center
of Excellence (NCCoE)); Murugiah Souppaya (Computer Security Division); Kevin
Kimball (NIST Director’s Office); Keith Bubar (Acquisition Management Division);
and Lauren Didiuk (Department of Commerce, Office of General Counsel).
Front Row (Left/Right): Waltermire, Salah, Kauffman
Back Row Left/Right: Lesser, Kimball, O’Brien, McBride
Absent: Bubar, Souppaya, and Didiuk
The group is recognized for establishing the National Cybersecurity Center of Excellence (NCCoE) to accelerate the
adoption of cybersecurity standards and best practices. With industry partnerships, the NCCoE builds practical security
reference designs that can be rapidly applied to the real challenges that businesses face today. This achievement includes
the Department’s first Federally Funded Research and Development Center (FFRDC) and the Nation’s first FFRDC devoted
wholly to cybersecurity.
98
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Department of Commerce
Silver Medal Award
Elaine Barker, Lawrence Bassham, Shu-jen Chang, Lily Chen, Quynh Dang, Morris
Dworkin, John Kelsey, Rene Peralta, Ray Perlner and Andrew Regenscheid (All work
for the Computer Security Division, Information Technology Laboratory)
(Left/Right): Regenscheid; Dang; Barker; Kelsey; Chang; Bassham; Dworkin; Chen; Perlner; Peralta
The group is recognized for exceptional technical innovation in leading a global effort to develop Federal Information
Processing Standard (FIPS) 202, the “SHA-3” hash function standard. Cryptographic hash functions are critical components
of the technologies (e.g., digital signatures and message authentication) that secure global communications, international
electronic commerce and more. Advances in cryptanalysis in 2004-2007 weakened the security of many widely used hash
functions, broadly threatening cybersecurity. SHA-3 is intended to provide security for decades.
99
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: HONORS AND AWARDS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Department of Commerce
Bronze Medal Award
Bill Fisher and Jerome “Jay” Thomson (Applied Cybersecurity Division, National
Cybersecurity Center of Excellence (NCCoE)); Beth Bly and Deana Ramsburg
(Customer Access and Support Division); Alex Folk (Information Technology
Laboratory Office); Robert Densock (Information Technology Security & Networking
Division); Lynn Flanagan (Department of Commerce, Office of General Counsel);
Jatin Patel (Gaithersburg Design and Construction Division, Facilities Improvement
Group); Kevin Conrad and Cheri Smith (Emergency Services Office, Security
Systems and Access Control Group).
Group Photo: (Left/Right) (front) Bly; Smith; Ramsburg;
(back) Folk; Thomson; Conrad; Densock; Fisher;
Individual Photo Top/Bottom: Flanagan; Patel
The team is recognized for outstanding leadership and teamwork in coordinating the design and construction of the
facility housing the National Cybersecurity Center of Excellence. In 12 months, this team transformed a 65,000-square-foot
biotech facility into a state-of-the-art cybersecurity research center that is home to 28 laboratories and other workspaces
for collaboration among government, academia and industry. During this time, this high-performing team brought
together the necessary leadership skills, team-building techniques, contracting and procurement expertise, project
management discipline, physical security methods, construction knowledge, and attention to detail required to complete
this high-priority effort.
100
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

Ms. Donna Dodson Nominated 1 of the 11 Most
Influential Women in Government IT for 2016
The United Nations adopted February 11th as an International Day of Women and Girls in
Science. This day celebrates the impact and importance of women in science, technology,
engineering and management, also known as STEM, and focuses on the significance of
encouraging women of all ages to enter STEM fields. Within the Federal Government, there
have been many women over the years that have made significant, influential, and positive
impacts on Information Technology.
One of the eleven Women in the Federal Government chosen to receive this great honor
is Ms. Donna Dodson of the National Institute of Standards and Technology (NIST). Donna
works in the Information Technology Laboratory (ITL) as the Associate Director Chief
Cybersecurity Advisor, and she is also the Director of the National Cybersecurity Center
of Excellence (NCCoE), a program at NIST. Donna manages the lab’s research and development; she also has a key role in
developing relationships with academia, industry, and government agencies to analyze and improve cybersecurity best
practices.
Dr. Ron Ross is the recipient of 5 awards during 2016
National Cybersecurity Hall of Fame: Class of 2015
Dr. Ron Ross was inducted into the National Cybersecurity Hall of Fame. The Hall of Fame
is a national program that describes its mission as honoring “the innovative individuals
and organizations which had the vision and leadership to create the foundational building
blocks for the Cybersecurity industry.” Dr. Ross was honored as a key pioneer of the Federal
Information Security Management Act (FISMA) security standards and his role as one of
the world’s leading experts on cybersecurity. His induction recognized his leadership as the
principal architect of the NIST Risk Management Framework and lead developer of the first
set of unified cybersecurity standards for the Federal Government.
(See Source: http://www.cybersecurityhalloffame.com)
Service to America Medal for Homeland Security and Law Enforcement
Dr. Ross was awarded a Service to America Medal for his work having “instituted a state-of-the-art risk assessment system
that has protected federal computer networks from cyber attacks and helped secure information critical to our national
and economic security.” The Samuel J. Heyman Service to America Medals honor members of the Federal workforce,
highlighting the work of employees who significantly contribute to the governance of the United States.
(See Source: https://servicetoamericamedals.org/honorees/view_profile.php?profile=409)
Government Executive of the Year Award
Dr. Ross was also recognized, as part of the Government Computer News (GCN) Annual Awards, as the Government
Executive of the Year. The award honored Dr. Ross’ contributions to securing federal information systems. GCN’s editor in
chief, Troy Schneider, stated that “there is virtually no corner of federal IT in 2015 that doesn’t need to take cybersecurity
into account, and there is probably no government executive more central to those security efforts than Ron Ross.”
(See Source: https://gcn.com/articles/2015/10/07/ron-ross-nist.aspx?m=1)
Federal 100 Award
For the third time, Dr. Ross was recognized as one of Federal Computer Week’s Federal 100 awardees. The Federal 100
Awards recognize government and industry leaders who have played pivotal roles in the Federal Government IT community.
101
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: HONORS AND AWARDS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

Ross personally has been a critical driver for getting
agencies − and many other key stakeholders − to move
beyond checklist-based security. He spent much of 2015
evangelizing in the federal community, making sure that
both NIST Special Publication 800-160 on systems security
engineering and the Risk Management Framework that he
developed were put to good use.
(See Source: https://fcw.com/articles/2016/03/28/fed100_
ross-ron.aspx?m=1)
2015 Presidential Rank Award
Dr. Ron Ross was awarded the 2015 Presidential Rank
Award. The Civil Service Reform Act of 1978 established the
Presidential Rank Awards Program to recognize a select
group of career members of the Senior Executive Service
(SES) for exceptional performance over an extended period.
Later, the Rank Award statute was amended to extend
eligibility to senior career employees with a sustained record
of exceptional professional, technical, and/or scientific achievement at a national or international level.
(See Source: https://www.opm.gov/policy-data-oversight/senior-executive-service/presidential-rank-awards/presidential-
rank-awards-2015-full-list.pdf)
102
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

ITL CYBERSECURITY PROGRAM
PUBLICATIONS RELEASED IN FY 2016
This section provides a compiled list of ITL cybersecurity publications that were
released during FY 2016 (from October 1, 2015 to September 30, 2016). The first
portion provides a list of the technical documents. The second portion provides
abstracts that represent a brief summary of each document (technical and non-
technical).
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

DRAFT PUBLICATIONS
TABLE 3: NO DRAFT FIPS RELEASED DURING FY 2016
TABLE 4: SPECIAL PUBLICATIONS (SPs)
PUBLICATION NUMBER PUBLICATION TITLE DRAFT RELEASED
SP 800-188 De-Identifying Government Datasets August 2016
SP 800-185 SHA-3 Derived Functions: cSHAKE, KMAC, TupleHash, and August 2016
ParallelHash
SP 800-184 Guide for Cybersecurity Event Recovery June 2016
SP 800-180 NIST Definition of Microservices, Application Containers and February 2016
System Virtual Machines
SP 800-179 Guide to Securing Apple OS X 10.10 Systems for IT June 2016
Professionals: A NIST Security Configuration Checklist
SP 800-177 (2nd Draft) Trustworthy Email March 2016
SP 800-175A Guideline for Using Cryptographic Standards in the Federal April 2016
Government: Directives, Mandates and Policies
SP 800-175B Guideline for Using Cryptographic Standards in the Federal March 2016
Government: Cryptographic Mechanisms
SP 800-171 Rev. 1 Protecting Controlled Unclassified Information in Nonfederal August 2016
Information Systems and Organizations
SP 800-166 Derived PIV Application and Data Model Test Guidelines February 2016
SP 800-160 (Final Public Draft) Systems Security Engineering Guideline: An Integrated September 2016
(2nd Draft) Approach to Building Trustworthy Resilient Systems May 2016
SP 800-156 Representation of PIV Chain-of-Trust for Import and Export December 2015
SP 800-154 Guide to Data-Centric System Threat Modeling March 2016
SP 800-150 (2nd Draft) Guide to Cyber Threat Information Sharing April 2016
SP 800-126 Rev. 3 The Technical Specification for the Security Content July 2016
Automation Protocol (SCAP): SCAP Version 1.3
SP 800-126A SCAP 1.3 Component Specification Version Updates: An Annex July 2016
to NIST Special Publication 800-126 Revision 3
SP 800-116 Rev. 1 A Recommendation for the Use of PIV Credentials in Physical December 2015
Access Control Systems (PACS)
SP 800-114 Rev. 1 User's Guide to Telework and Bring Your Own Device (BYOD) March 2016
Security
SP 800-90C (2nd Draft) Recommendation for Random Bit Generator (RBG) April 2016
Constructions
SP 800-90B (2nd Draft) Recommendation for the Entropy Sources Used for Random January 2016
Bit Generation
SP 800-46 Rev. 2 Guide to Enterprise Telework, Remote Access, and Bring Your March 2016
Own Device (BYOD) Security
104
SP 1800-5 IT Asset Management: Financial Services October 2015
SP 1800-4 Mobile Device Security: Cloud and Hybrid Builds November 2015
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

TABLE 5: NIST INTERAGENCY OR INTERNAL REPORTS (NISTIRs)
PUBLICATION NUMBER PUBLICATION TITLE DRAFT RELEASED
NISTIR 8144 Assessing Threats to Mobile Devices and Infrastructure: The September 2016
TABLE 3: NO DRAFT FIPS RELEASED DURING FY 2016 Mobile Threat Catalogue
NISTIR 8138 Vulnerability Description Ontology (VDO): A Framework for September 2016
Characterizing Vulnerabilities
NISTIR 8136 Mobile Application Vetting Services for Public Safety June 2016
NISTIR 8114 Report on Lightweight Cryptography August 2016
NISTIR 8112 Attribute Metadata August 2016
NISTIR 8105 Report on Post-Quantum Cryptography for Public Comment February 2016
NISTIR 8103 Advanced Identity Workshop on Applying Measurement February 2016
Science in the Identity Ecosystem: Summary and Next Steps
NISTIR 8085 Forming Common Platform Enumeration (CPE) Names from December 2015
Software Identification (SWID) Tags
NISTIR 8080 Usability and Security Considerations for Public Safety Mobile November 2015
Authentication
NISTIR 8071 LTE Architecture Overview and Security Analysis April 2016
NISTIR 8063 Primitives and Elements of Internet of Things (IoT) February 2016
[final version published as Trustworthiness
SP 800-183]
NISTIR 8060 Guidelines for the Creation of Interoperable Software December 2015
(Final Public Draft) Identification (SWID) Tags
NISTIR 8011 Automation Support for Security Control Assessments February 2016
Volumes 1 & 2 Volume 1: Overview
Volume 2: Hardware Asset Management
FINAL APPROVED PUBLICATIONS
TABLE 6: NO FIPS PUBLISHED IN FY 2016
105
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: ITL CYBERSECURITY PUBLICATIONS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

TABLE 7: FINAL - SPs
PUBLICATION NUMBER PUBLICATION TITLE RELEASE DATE
SP 800-183 Networks of ‘Things’ July 2016
SP 800-182 Computer Security Division 2015 Annual Report July 2016
SP 800-177 Trustworthy Email September 2016
SP 800-175A Guideline for Using Cryptographic Standards in the Federal August 2016
Government: Directives, Mandates and Policies
SP 800-175B Guideline for Using Cryptographic Standards in the Federal August 2016
Government: Cryptographic Mechanisms
SP 800-171 (update) Protecting Controlled Unclassified Information in Nonfederal January 2016
Information Systems and Organizations
SP 800-167 Guide to Application Whitelisting October 2015
SP 800-166 Derived PIV Application and Data Model Test Guidelines June 2016
SP 800-156 Representation of PIV Chain-of-Trust for Import and Export May 2016
SP 800-152 A Profile for U.S. Federal Cryptographic Key Management October 2015
Systems
SP 800-131A Rev. 1 Transitions: Recommendation for Transitioning the Use of November 2015
Cryptographic Algorithms and Key Lengths
SP 800-125B Secure Virtual Network Configuration for Virtual Machine (VM) March 2016
Protection
SP 800-114 Rev. 1 User's Guide to Telework and Bring Your Own Device (BYOD) July 2016
Security
SP 800-85A-4 PIV Card Application and Middleware Interface Test Guidelines April 2016
(SP 800-73-4 Compliance)
SP 800-73-4 (update) Interfaces for Personal Identity Verification February 2016
SP 800-70 Rev. 3 National Checklist Program for IT Products: Guidelines for December 2015
Checklist Users and Developers
SP 800-57 Part 1 Rev. 4 Recommendation for Key Management, Part 1: General January 2016
SP 800-46 Rev. 2 Guide to Enterprise Telework, Remote Access, and Bring Your July 2016
Own Device (BYOD) Security
SP 800-38G Recommendation for Block Cipher Modes of Operation: March 2016 (and
Methods for Format-Preserving Encryption updated August
2016)
SP 500-316 Framework for Cloud Usability December 2015
106
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

TABLE 8: FINAL - NISTIRs
PUBLICATION NUMBER PUBLICATION TITLE RELEASE DATE
NISTIR 8150 Government Data De-Identification Stakeholder’s Meeting, September 2016
Meeting Report
NISTIR 8135 Identifying and Categorizing Data Types for Public Safety May 2016
Mobile Applications: Workshop Report
NISTIR 8113 SATE V Ockham Sound Analysis Criteria March 2016
NISTIR 8105 Report on Post-Quantum Cryptography for Public Comment March 2016
NISTIR 8103 Advanced Identity Workshop on Applying Measurement September 2016
Science in the Identity Ecosystem: Summary and Next Steps
NISTIR 8101 A Rational Foundation for Software Metrology January 2016
NISTIR 8080 Usability and Security Considerations for Public Safety Mobile July 2016
Authentication
NISTIR 8074 Volume 1: Report on Strategic U.S. Government Engagement December 2015
Volumes 1 & 2 in International Standardization to Achieve U.S. Objectives for
Cybersecurity
Volume 2: Supplemental Information
NISTIR 8060 Guidelines for the Creation of Interoperable Software April 2016
Identification (SWID) Tags
NISTIR 8055 Derived Personal Identity Verification (PIV) Credentials (DPC) January 2016
Proof of Concept Research
NISTIR 8054 (update) NSTIC Pilots: Catalyzing the Identity Ecosystem March 2016
NISTIR 8053 De-Identification of Personal Information October 2015
NISTIR 8040 Measuring the Usability and Security of Permuted Passwords April 2016
on Mobile Platforms
NISTIR 7987 Rev. 1 Policy Machine: Features, Architecture, and Specification October 2015
NISTIR 7977 NIST Cryptographic Standards and Guidelines Development March 2016
Process
NISTIR 7966 Security of Interactive and Automated Access Management October 2015
Using Secure Shell (SSH)
NISTIR 7904 Trusted Geolocation in the Cloud: Proof of Concept December 2015
Implementation
NISTIR 7511 Rev. 4 Security Content Automation Protocol (SCAP) Version 1.2 January 2016
Validation Program Test Requirements
107
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: ITL CYBERSECURITY PUBLICATIONS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

TABLE 9: ITL BULLETINS
PUBLICATION DATE BULLETIN TITLE
September 2016 Demystifying the Internet of Things
August 2016 NIST Updates Personal Identity Verification (PIV) Guidelines
July 2016 Improving Security and Software Management Through the Use of SWID Tags
June 2016 Extending Network Security into Virtualized Infrastructure
May 2016 Combinatorial Testing for Cybersecurity and Reliability
April 2016 New NIST Security Standard Can Protect Credit Cards, Health Information
March 2016 Updates to the NIST SCAP Validation Program and Associated Test Requirements
February 2016 Implementing Trusted Geolocation Services in the Cloud
January 2016 Securing Interactive and Automated Access Management Using Secure Shell (SSH)
December 2015 Stopping Malware and Unauthorized Software through Application Whitelisting
November 2015 Tailoring Security Controls for Industrial Control Systems
October 2015 Protection of Controlled Unclassified Information
Other NIST Publications
NIST released other publications in FY 2016, as “White Papers,” and as Concept Papers and Project Descriptions from
NCCoE.
TABLE 10: OTHER NIST PUBLICATIONS (CONCEPT PAPERS, PROJECT DESCRIPTIONS, AND
WHITE PAPERS) POSTED FOR PUBLIC COMMENT
PUBLICATION TYPE PUBLICATION TITLE RELEASE DATE
Concept Paper (Draft) Identity and Access Management for Smart Home Devices June 2016
Project Description (Draft) Authentication for Law Enforcement Vehicle Systems September 2016
Project Description (Final) Data Integrity: Recovering from a Destructive Malware Attack May 2016
(Draft) December 2015
Project Description (Final) Domain Name System-Based Security for Electronic Mail March 2016
Project Description (Draft) Mobile Application Single Sign-on: for Public Safety and First July 2016
Responders
Project Description (Draft) Multifactor Authentication for e-Commerce: Online May 2016
Authentication for the Retail Sector
Project Description (Draft) Securing Non-Credit Card, Sensitive Consumer Data: May 2016
Consumer Data Security for the Retail Sector
White Paper (Draft) Baldrige Cybersecurity Excellence Builder (BCEB): Key September 2016
questions for improving your organization’s cybersecurity
performance
White Paper (Final) Best Practices for Privileged User PIV Authentication April 2016
(Draft) February 2016
White Paper (Draft) Cybersecurity Framework Manufacturing Profile September 2016
108
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

ITL CYBERSECURITY Two significant efforts to revise major publications were
PROGRAM RELATED begun. ACD solicited public input to develop preliminary
drafts of SP 800-63-3, Digital Authentication Guideline,
PUBLICATIONS
during a “Public Preview” phase that enabled stakeholders
to provide dynamic, interactive feedback. A subseries
During FY 2016, the ITL staff authored a significant
of documents that will revise the current SP 800-63-2,
number of standards, guidelines, recommendations and
Electronic Authentication Guideline, will be posted for public
other research papers. These were published as NIST technical
comment as official public drafts in early FY 2017 (see https://
series documents (e.g., Federal Information Processing
pages.nist.gov/800-63-3/). Meanwhile, CSD posted a call for
Standards (FIPS), Special Publications (SP), NIST Internal or
comments on SP 800-53 Revision 4, Security and Privacy
Interagency Reports (NISTIRs), and Information Technology
Controls for Federal Information Systems and Organizations,
Laboratory (ITL) Bulletins), other NIST publications, or
to begin preparing for the release of a draft of Revision 5 for
as externally-published documents (e.g., journal articles,
public comment in FY 2017.
conference papers, books, and other papers).
The ITL Cybersecurity Framework team worked closely
Additionally, the NCCoE began posting public drafts of
with the Baldrige Performance Excellence Program to
documents in two new series: Concept Papers and Project
develop the Baldrige Cybersecurity Excellence Builder
Descriptions. Concept Papers identify potential project
(BCEB): Key questions for improving your organization’s
topics for NCCoE to explore with stakeholders and
cybersecurity performance, which was posted for public
technology collaborators. After reviewing public comments
comment on the Baldridge Cybersecurity Initiative website
on a draft Concept Paper, NCCoE can better understand
(see https://www.nist.gov/baldrige/products-services/
specific challenges and needs, and may possibly draft
baldrige-cybersecurity-initiative). The BCEB is a voluntary
a Project Description. Formerly issued as “Building
self-assessment tool that enables organizations to better
Blocks” and “Use Cases,” Project Descriptions describe a
understand the effectiveness of their cybersecurity risk
particular problem that is relevant across a sector. Through
management efforts.
collaboration with community members and vendors of
cybersecurity solutions, NCCoE will develop a reference
design that can be used by sector organizations to address Top Downloads
that challenge.
Publications are available for download from CSRC
In FY 2016, ITL published 20 NIST Special Publications, 18 (see http://csrc.nist.gov/publications/), the NCCoE website
NISTIRs and 12 ITL Bulletins in the areas of cybersecurity and (see https://nccoe.nist.gov/library) and the main NIST
privacy. Additionally, ITL continued to engage stakeholders Publications site (see https://www.nist.gov/publications/).
by posting numerous draft documents for public comment, The following lists summarize the most-downloaded ITL
including 23 Special Publications, 13 NISTIRs, 6 NCCoE publications for FY 2016, using weblog data (and excluding
Project Descriptions, 1 NCCoE Concept Paper, and 3 NIST traffic from spiders and web crawlers):
“white papers.” ITL research was also published externally, as
18 journal articles and 18 conference papers. They are listed Top 10 Most-Downloaded
below, with abstracts and full text links, under (External Publications (with estimated
Publications).
number of downloads):
In the October 19, 2015 Federal Register, NIST
1. SP 800-53 Revision 4, Security and Privacy Controls
announced the withdrawal of six FIPS that had become
for Federal Information Systems and Organizations
obsolete: FIPS 181, 185, 188, 190, 191, and 196. NIST had
(303,162);
received only one comment in response to a January 16,
2015 Federal Register Notice requesting public feedback 2. SP 800-145, The NIST Definition of Cloud Computing
on their proposed withdrawal. (The titles of the withdrawn (235,191);
FIPS are: 181 - Automated Password Generator (APG), 185 3. Framework for Improving Critical Infrastructure
- Escrowed Encryption Standard, 188 - Standard Security Cybersecurity, version 1.0 (180,163);
Label for Information Transfer, 190 - Guideline for the Use
4. SP 800-61 Revision 2, Computer Security Incident
of Advanced Authentication Technology Alternatives,
Handling Guide (153,723);
191 - Guideline for The Analysis of Local Area Network
Security, and 196 - Entity Authentication Using Public Key 5. SP 800-30 Revision 1, Guide for Conducting Risk
Cryptography.) Assessments (116,991); 109
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: ITL CYBERSECURITY PUBLICATIONS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

6. SP 800-37 Revision 1, Guide for Applying the Risk FY 2017 Plans
Management Framework to Federal Information
ITL will continue to publish its research in the publication
Systems: A Security Life Cycle Approach (112,104);
series mentioned here. Additionally, ITL is developing a new
7. FIPS 197, Advanced Encryption Standard (AES) version of CSRC—planned for release in FY 2017—that will
(108,162); significantly improve information about its cybersecurity and
8. SP 800-122, Guide to Protecting the Confidentiality privacy publications, including features such as advanced
of Personally Identifiable Information (PII) (81,887); searching and filtering; abstracts, keywords, and authors;
links to superseding/superseded versions of publications;
9. SP 800-12, An Introduction to Computer Security:
and a significantly more robust taxonomy of topical
the NIST Handbook (81,768); and
headings to help users easily find related content (including
10. SP 800-171, Protecting Controlled Unclassified publications) on the CSRC website. More publication-related
Information in Nonfederal Information Systems and features will be added incrementally after the website’s
Organizations (80,960). initial rollout.
FOR MORE INFORMATION, SEE:
Top 3 FIPS:
http://csrc.nist.gov/publications/
1. FIPS 197, Advanced Encryption Standard (AES)
(108,162);
CONTACTS:
2. FIPS 140-2, Security Requirements for Cryptographic
Mr. Jim Foti Mr. Patrick O’Reilly
Modules (79,565); and
(301) 975-8018 (301) 975-4751
3. FIPS 199, Standards for Security Categorization
james.foti@nist.gov patrick.oreilly@nist.gov
of Federal Information and information Systems
(70,846).
NIST Technical Series
Top 3 NISTIRs: Publications and Other NIST
Publications
1. NISTIR 7298 Rev. 2, Glossary of Key Information
Security Terms (36,110); The following tables list NIST Technical Series
publications and other NIST publications released by ITL on
2. NISTIR 7316, Assessment of Access Control Systems
CSRC—either as draft or final publications—during FY 2016
(19,902); and
(from October 1, 2015 to September 30, 2016). Abstracts and
3. NISTIR 8053, De-Identification of Personal Infor-
links to the full text of these publications are provided in the
mation (17,970).
sections that follow.
Top 3 ITL Bulletins:
1. The System Development Life Cycle (SDLC), April
2009 (46,298);
2. Cloud Computing: A Review of Features, Benefits,
and Risk, and Recommendations for Secure,
Efficient Implementations, June 2012 (7,309); and
3. New NIST Security Standard Can Protect Credit
Cards, Health Information, April 2016 (6,150).
110
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

ABSTRACTS OF PUBLICATIONS   provide  sufficient  functionality  for  performing  de-
identification. This document also includes an extensive
RELEASED IN FY 2016
list of references, a glossary, and a list of specific de-
identification tools, although the mention of these tools
The following sections provide abstracts of NIST SPs,  is only to be used to convey the range of tools currently
security-related NISTIRs, and other NIST publications listed  available, and is not intended to imply recommendation
in the previous section. If a publication was released as a  or endorsement by NIST.
draft and final publication during FY 2016, only the final
SP 800-185 (DRAFT)
publications are listed below. Any updated publications with
|     |     |     |     |     |     |     |    SHA-3 Derived Functions: cSHAKE, KMAC,   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
minor technical or editorial changes, identified in the tables
TupleHash, and ParallelHash
above as “updates,” are not listed below. Technical reports
are listed in reverse numerical order by report number; other
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-185
documents are listed alphabetically by title.
This Recommendation specifies four SHA-3-derived
functions: cSHAKE, KMAC, TupleHash, and ParallelHash.
NIST SPs
cSHAKE is a customizable variant of the SHAKE functions
|     |     |     |     |     |     |     | defined         | in  FIPS  | 202.   | KMAC  |                     | (for  Keccak  |          | Message  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | ------ | ----- | ------------------- | ------------- | -------- | -------- |
|     |     |     |     |     |     |     | Authentication  |           | Code)  | is    | a  variable-length  |               | message  |          |
SP 800-188 (DRAFT)  authentication code algorithm based on Keccak; it can
  De-Identifying Government Datasets  also be used as a pseudorandom function. TupleHash
|     |     |     |     |     |     |     | is a variable-length hash function that is designed to  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-188 hash tuples of input strings unambiguously. ParallelHash
is a variable-length hash function that can hash non-
| De-identification  |     | removes  | identifying  |     | information  |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
overlapping subsets of very long messages in parallel.
from a dataset so that the remaining data cannot be
linked with specific individuals. Government agencies  SP 800-184 (DRAFT)
|           |                    |     |             |     |               |       |   Guide for Cybersecurity Event Recovery  |     |     |     |     |     |     |     |
| --------- | ------------------ | --- | ----------- | --- | ------------- | ----- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| can  use  | de-identification  |     | to  reduce  |     | the  privacy  | risk  |                                           |     |     |     |     |     |     |     |

| associated  | with  | collecting,  | processing,  |     |     | archiving,  |     |     |     |     |     |     |     |     |
| ----------- | ----- | ------------ | ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-184
distributing or publishing government data. Previously,
NIST published NISTIR 8053, “De-Identifying Personal
In light of an increasing number of cybersecurity
Data,” which provided a survey of de-identification and
|                    |     |              |       |           |     |           | events,  | organizations  |     | can  | improve  |     | resilience  | by  |
| ------------------ | --- | ------------ | ----- | --------- | --- | --------- | -------- | -------------- | --- | ---- | -------- | --- | ----------- | --- |
| re-identification  |     | techniques.  | This  | document  |     | provides  |          |                |     |      |          |     |             |     |
ensuring that their risk management processes include
specific guidance to government agencies that wish to   comprehensive  recovery  planning.  Identifying  and
| use  de-identification.  |         |           | Before  using   |           | de-identification,  |             |               |               |      |            |            |           |                  |         |
| ------------------------ | ------- | --------- | --------------- | --------- | ------------------- | ----------- | ------------- | ------------- | ---- | ---------- | ---------- | --------- | ---------------- | ------- |
|                          |         |           |                 |           |                     |             | prioritizing  | organization  |      |            | resources  | helps     | to               | guide   |
| agencies                 | should  | evaluate  | their           | goals     |                     | in  using   |               |               |      |            |            |           |                  |         |
|                          |         |           |                 |           |                     |             | effective     | plans         | and  | realistic  |            | test      | scenarios.       | This    |
| de-identification        |         | and       | the  potential  |           | risks               | that        |               |               |      |            |            |           |                  |         |
|                          |         |           |                 |           |                     |             | preparation   | enables       |      | rapid      | recovery   |           | from  incidents  |         |
| de-identification        |         | might     | create.         | Agencies  |                     | should      |               |               |      |            |            |           |                  |         |
|                          |         |           |                 |           |                     |             | when  they    | occur         | and  | helps      | to         | minimize  | the              | impact  |
decide  upon  a  de-identification  release  model,  such  on the organization and its constituents. Additionally,
as publishing de-identified data, publishing synthetic
|     |     |     |     |     |     |     | continually  | improving  |     | recovery  |     | planning  | by  | learning  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | --------- | --- | --------- | --- | --------- |
data based on identified data, and providing a query
|            |     |                  |       |       |                |     | lessons         | from  | past   | events,  | including  |      | those  of   | other  |
| ---------- | --- | ---------------- | ----- | ----- | -------------- | --- | --------------- | ----- | ------ | -------- | ---------- | ---- | ----------- | ------ |
| interface  | to  | the  identified  | data  | that  | incorporates   |     |                 |       |        |          |            |      |             |        |
|            |     |                  |       |       |                |     | organizations,  |       | helps  | to       | ensure     | the  | continuity  | of     |
de-identification. Agencies can use a Disclosure Review
important mission functions. This publication provides
Board to oversee the process of de-identification; they   tactical and strategic guidance regarding the planning,
| can  also   | adopt        | a  de-identification  |          |          | standard  | with      |           |              |     |           |     |                   |     |     |
| ----------- | ------------ | --------------------- | -------- | -------- | --------- | --------- | --------- | ------------ | --- | --------- | --- | ----------------- | --- | --- |
|             |              |                       |          |          |           |           | playbook  | developing,  |     | testing,  |     | and  improvement  |     | of  |
| measurable  | performance  |                       | levels.  | Several  |           | specific  |           |              |     |           |     |                   |     |     |
recovery planning. It also provides an example scenario
| techniques  | for  | de-identification  |     |     | are  | available,  |                     |     |     |           |      |              |     |          |
| ----------- | ---- | ------------------ | --- | --- | ---- | ----------- | ------------------- | --- | --- | --------- | ---- | ------------ | --- | -------- |
|             |      |                    |     |     |      |             | that  demonstrates  |     |     | guidance  | and  | informative  |     | metrics  |
including de-identification by removing identifiers and
|     |     |     |     |     |     |     | that  may  | be  | helpful  | for  | improving  | resilience  |     | of  the  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ---- | ---------- | ----------- | --- | -------- |
transforming  quasi-identifiers  and  the  use  of  formal   information systems.
| de-identification  |                    | models  | that  | rely  upon  | Differential  |     |     |     |     |     |     |     |     |     |
| ------------------ | ------------------ | ------- | ----- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Privacy.           | De-identification  |         | is    | typically   | performed     |     |     |     |     |     |     |     |     |     |
with software tools that may have multiple features;
111
however, not all tools that mask personal information
ITL CYBERSECURITY PUBLICATIONS  |  FY 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

| SP 800-183  |     |     |     |     |     |     | SP 800-180 (DRAFT)  |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
  Networks of ‘Things’     NIST Definition of Microservices, Application
|     |     |     |     |     |     |     | Containers and System Virtual Machines |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
https://doi.org/10.6028/NIST.SP.800-183
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-180
   [This was originally released for public comment
as draft NISTIR 8063, Internet of Things (IoT)
|     |     |     |     |     |     |     | Many  | variations  | and  | definitions  | of  | application  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ---- | ------------ | --- | ------------ |
Trustworthiness, in February 2016.]
|     |     |     |     |     |     |     | containers  | exist  | in  industry,  | causing  |     | considerable  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | -------------- | -------- | --- | ------------- |
confusion among those who attempt to explain what
| System  | primitives  |     | allow  | formalisms,  | reasoning,  |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------ | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
simulations, and reliability and security risk-tradeoffs  a container is. This document provides a NIST-standard
definition to application containers, microservices that
to be formulated and argued. In this work, five core
reside in application containers and operating system
primitives belonging to most distributed systems are
virtual machines. Furthermore, this document explains
| presented.   | These    | primitives  |            | apply  well  | to  | systems    |                    |     |                   |          |     |              |
| ------------ | -------- | ----------- | ---------- | ------------ | --- | ---------- | ------------------ | --- | ----------------- | -------- | --- | ------------ |
|              |          |             |            |              |     |            | the  similarities  |     | and  differences  | between  |     | a  Services  |
| with  large  | amounts  |             | of  data,  | scalability  |     | concerns,  |                    |     |                   |          |     |              |
heterogeneity  concerns,  temporal  concerns,  and  Oriented Architecture (SOA) and Microservices, as well
as the similarities and differences between Operating
elements of unknown pedigree with possible nefarious
System Virtual Machines and Application Containers.
intent. These primitives are the basic building blocks
for a Network of ‘Things’ (NoT), including the Internet  SP 800-179 (DRAFT)
of Things (IoT). This document offers an underlying     Guide to Securing Apple OS X 10.10 Systems for
| and  foundational  |     | understanding  |     | of  | IoT  based  | on  |     |     |     |     |     |     |
| ------------------ | --- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
IT Professionals: A NIST Security Configuration
| the realization that IoT involves sensing, computing,  |     |     |     |     |     |     | Checklist |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
communication, and actuation. The material presented
here is generic to all distributed systems that employ  http://csrc.nist.gov/publications/PubsSPs.html#SP-800-179
| IoT  technologies  |     | (i.e.,  | ‘things’  | and  | networks).  | The  |     |     |     |     |     |     |
| ------------------ | --- | ------- | --------- | ---- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
This publication assists IT professionals in securing
expected audience is computer scientists, IT managers,
Apple OS X 10.10 (i.e., Yosemite) desktop and laptop
| networking  | specialists,  |     | and  | networking  | and  | cloud  |     |     |     |     |     |     |
| ----------- | ------------- | --- | ---- | ----------- | ---- | ------ | --- | --- | --- | --- | --- | --- |
systems within various environments. It provides detailed
computing software engineers.
information about the security features of OS X 10.10
SP 800-182  and security configuration guidelines. The publication
   Computer Security Division 2015 Annual Report recommends and explains tested, secure settings with
the objective of simplifying the administrative burden of
https://doi.org/10.6028/NIST.SP.800-182
improving the security of OS X 10.10 systems in three
|     |     |     |     |     |     |     | types  of  | environments:  | Standalone,  |     | Managed,  | and  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ------------ | --- | --------- | ---- |
Title III of the E-Government Act of 2002, entitled
Specialized Security-Limited Functionality.
| the  Federal                                         | Information  |     | Security  | Management  |     | Act  |             |     |     |     |     |     |
| ---------------------------------------------------- | ------------ | --- | --------- | ----------- | --- | ---- | ----------- | --- | --- | --- | --- | --- |
| (FISMA) of 2002, requires NIST to prepare an annual  |              |     |           |             |     |      | SP 800-177  |     |     |     |     |     |
public report on activities undertaken in the previous
|     |     |     |     |     |     |     |    Trustworthy Email |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
year, and those planned for the coming year, to carry
https://doi.org/10.6028/NIST.SP.800-177
out responsibilities under this law. The primary goal of
the Computer Security Division (CSD), a component
|             |              |     |             |             |     |         | This  | document  | gives  | recommendations  |     | and  |
| ----------- | ------------ | --- | ----------- | ----------- | --- | ------- | ----- | --------- | ------ | ---------------- | --- | ---- |
| of  NIST’s  | Information  |     | Technology  | Laboratory  |     | (ITL),  |       |           |        |                  |     |      |
guidelines for enhancing trust in email. The primary
is to provide standards and technology that protects
|              |          |     |          |          |     |           | audience  | includes  | enterprise  | email  | administrators,  |     |
| ------------ | -------- | --- | -------- | -------- | --- | --------- | --------- | --------- | ----------- | ------ | ---------------- | --- |
| information  | systems  |     | against  | threats  | to  | the  con- |           |           |             |        |                  |     |
information security specialists and network managers.
fidentiality, integrity, and availability of information and
This guideline applies to federal IT systems and will
services. During FY 2015, CSD successfully responded to
also be useful for small or medium-sized organizations.
numerous challenges and opportunities in fulfilling that
Technologies recommended in support of core Simple
mission. Through CSD’s diverse research agenda and
Mail Transfer Protocol (SMTP) and the Domain Name
engagement in many national priority initiatives, high-
System (DNS) include mechanisms for authenticating
quality, cost-effective security and privacy mechanisms
|     |     |     |     |     |     |     | a  sending  | domain:  | Sender  | Policy  | Framework  | (SPF),  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------- | ------- | ---------- | ------- |
were developed and applied that improved information
Domain Keys Identified Mail (DKIM) and Domain-based
security across the Federal Government and the greater
Message Authentication, Reporting and Conformance
| information  | security  |     | community.  | This  | annual  | report  |           |                  |     |      |        |               |
| ------------ | --------- | --- | ----------- | ----- | ------- | ------- | --------- | ---------------- | --- | ---- | ------ | ------------- |
|              |           |     |             |       |         |         | (DMARC).  | Recommendations  |     | for  | email  | transmission  |
112
highlights the research agenda and activities in which
|     |     |     |     |     |     |     | security  | include  | the  Transport  | Layer  | Security  | (TLS)  |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------------- | ------ | --------- | ------ |
CSD was engaged during FY 2015.
protocols and the associated certificate authentication
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

protocols. Recommendations for email content security requirements for protecting the confidentiality of CUI:
include the encryption and authentication of message (i) when the CUI is resident in nonfederal information
content using S/MIME (Secure/Multipurpose Internet systems and organizations; (ii) when the information
Mail Extensions) and the associated certificate and key systems where the CUI resides are not used or operated
distribution protocols. by contractors of federal agencies or other organizations
on behalf of those agencies; and (iii) where there are
SP 800-175A
no specific safeguarding requirements for protecting
Guideline for Using Cryptographic Standards in
the confidentiality of CUI prescribed by the authorizing
the Federal Government: Directives, Mandates and
law, regulation, or government-wide policy for the CUI
Policies
category or subcategory listed in the CUI Registry. The
https://doi.org/10.6028/NIST.SP.800-175A requirements apply to all components of nonfederal
information systems and organizations that process,
This document is part of a series intended to
store, or transmit CUI, or provide security protection for
provide guidance to the Federal Government for using
such components. The CUI requirements are intended
cryptography and NIST’s cryptographic standards to
for use by federal agencies in contractual vehicles or
protect sensitive, but unclassified digitized information
other agreements established between those agencies
during transmission and while in storage. SP 800-175A
and nonfederal organizations.
provides guidance on the determination of requirements
SP 800-167
for using cryptography. It includes a summary of laws
Guide to Application Whitelisting
and regulations concerning the protection of the Federal
Government’s sensitive information, guidance regarding
https://doi.org/10.6028/NIST.SP.800-167
the conduct of risk assessments to determine what
needs to be protected and how best to protect that An application whitelist is a list of applications and
information, and a discussion of the relevant security- application components that are authorized for use in an
related documents (e.g., various policy and practice organization. Application whitelisting technologies use
documents). whitelists to control which applications are permitted
to be executed on a host. This helps to stop the
SP 800-175B
execution of malware, unlicensed software, and other
Guideline for Using Cryptographic Standards in the
unauthorized software. This publication is intended
Federal Government: Cryptographic Mechanisms
to assist organizations in understanding the basics of
https://doi.org/10.6028/NIST.SP.800-175B application whitelisting. It also explains planning and
implementation for whitelisting technologies throughout
This document is intended to provide guidance to
the security deployment lifecycle.
the Federal Government for using cryptography and
SP 800-166
NIST’s cryptographic standards to protect sensitive, but
Derived PIV Application and Data Model Test
unclassified digitized information during transmission
Guidelines
and while in storage. The cryptographic methods and
services to be used are discussed.
https://doi.org/10.6028/NIST.SP.800-166
SP 800-171 Revision 1 (DRAFT)
SP 800-157 contains technical guidelines for the
Protecting Controlled Unclassified Information in
implementation of standards-based, secure, reliable,
Nonfederal Information Systems and Organizations
interoperable PKI-based identity credentials that are
http://csrc.nist.gov/publications/PubsSPs.html#SP-800- issued for mobile devices by federal departments and
171-Rev-1 agencies to individuals who possess and prove control
over a valid PIV Card. This document, SP 800-166,
The protection of Controlled Unclassified Information
contains the requirements and test assertions for testing
(CUI) while residing in nonfederal information systems
the Derived PIV Application and associated Derived
and organizations is of paramount importance to
PIV data objects implemented on removable hardware
federal agencies and can directly impact the ability
tokens and within mobile devices. The tests reflect the
of the Federal Government to successfully carry out
design goals of interoperability and interface functions.
its designated missions and business operations. This
publication provides federal agencies with recommended 113
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: ITL CYBERSECURITY PUBLICATIONS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

SP 800-160 (2 Drafts) processes. The general methodology provided by
Systems Security Engineering Guideline: An the publication is not intended to replace existing
Integrated Approach to Building Trustworthy methodologies, but rather to define fundamental
Resilient Systems principles that should be part of any sound data-centric
system threat modeling methodology.
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-160
SP 800-152
This publication addresses the engineering- A Profile for U. S. Federal Cryptographic Key
driven actions necessary to develop more defensible Management Systems (CKMS)
and survivable systems—including the components
https://doi.org/10.6028/NIST.SP.800-152
that compose and the services that depend on those
systems. It starts with and builds upon a set of well-
This Profile for U. S. Federal Cryptographic Key
established International Standards for systems and
Management Systems (FCKMSs) contains requirements
software engineering published by the International
for their design, implementation, procurement,
Organization for Standardization (ISO), the International
installation, configuration, management, operation, and
Electrotechnical Commission (IEC), and the Institute of
use by U. S. federal organizations. The Profile is based on
Electrical and Electronics Engineers (IEEE), and infuses
SP 800-130, A Framework for Designing Cryptographic
systems security engineering techniques, methods, and
Key Management Systems (CKMS).
practices into those systems and software engineering
SP 800-150 (2nd Draft)
processes. The ultimate objective is to address security
Guide to Cyber Threat Information Sharing
issues from the perspective of stakeholder requirements
and protection needs and to use established engineering
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-150
processes to ensure that such requirements and needs
are addressed with appropriate fidelity and rigor early Cyber threat information is any information that
and in a sustainable manner throughout the life cycle of can help an organization identify, assess, monitor, and
the system. respond to cyber threats. Cyber threat information
includes indicators of compromises; tactics, techniques,
SP 800-156
and procedures used by threat actors; suggested actions
Representation of PIV Chain-of-Trust for Import and
to detect, contain, or prevent attacks; and the findings
Export
from the analyses of incidents. Organizations that share
https://doi.org/10.6028/NIST.SP.800-156 cyber threat information can improve their own security
postures as well as those of other organizations. This
This document provides a common XML-based data
publication provides guidelines for establishing and
representation of a chain-of-trust record to facilitate the
participating in cyber threat information-sharing
exchange of PIV Card enrollment data. The exchanged
relationships. This guidance helps organizations
record is the basis for personalizing a PIV Card for a
establish information sharing goals, identify cyber
transferred employee and, also for service providers
threat information sources, scope information sharing
to personalize a PIV Card on behalf of client federal
activities, develop rules that control the publication and
agencies.
distribution of threat information, engage with existing
SP 800-154 (DRAFT) sharing communities, and make effective use of threat
Guide to Data-Centric System Threat Modeling information in support of their overall cybersecurity
practices.
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-154
SP 800-131A Revision 1
Threat modeling is a form of risk assessment Transitions: Recommendation for Transitioning the
that models aspects of the attack and defense sides Use of Cryptographic Algorithms and Key Lengths
of a particular logical entity, such as a piece of data,
https://doi.org/10.6028/NIST.SP.800-131Ar1
an application, a host, a system, or an environment.
This publication examines data-centric system threat
At the start of the 21st century, NIST began the task
modeling, which is threat modeling that is focused on
of providing cryptographic key management guidance,
protecting particular types of data within systems. The
which includes defining and implementing appropriate
publication provides information on the basics of data-
114 key management procedures, using algorithms that
centric system threat modeling so that organizations
adequately protect sensitive information, and planning
can successfully use it as part of their risk management
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

ahead for possible changes in the use of cryptography SP 800-125B
because of algorithm breaks or the availability of more Secure Virtual Network Configuration for Virtual
powerful computing techniques. SP 800-57, Part 1 was Machine (VM) Protection
the first document produced in this effort, and includes
https://doi.org/10.6028/NIST.SP.800-125B
a general approach for transitioning from one algorithm
or key length to another. This Recommendation (SP 800-
Virtual machines (VMs) are key resources to be
131A) provides more specific guidance for transitions to
protected, since they are the compute engines hosting
the use of stronger cryptographic keys and more robust
mission-critical applications. Since VMs are the end
algorithms.
nodes of a virtual network, the configuration of the
SP 800-126 Revision 3 (DRAFT) virtual network is an important element in the security
The Technical Specification for the Security Content of the VMs and their hosted applications. The virtual
Automation Protocol (SCAP): SCAP Version 1.3 network configuration areas discussed in this document
are network segmentation, network path redundancy,
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-
traffic control using firewalls, and VM traffic monitoring.
126-Rev-3
This document analyzes the configuration options
under these areas and presents a corresponding
The Security Content Automation Protocol (SCAP)
set of recommendations for secure virtual network
is a suite of specifications that standardize the format
configuration for VM protection.
and nomenclature by which software flaw and security
configuration information is communicated, both to SP 800-116 Revision 1 (DRAFT)
machines and humans. This publication defines the A Recommendation for the Use of PIV Credentials in
technical composition of SCAP version 1.3 in terms of its Physical Access Control Systems (PACS)
component specifications, their interrelationships and
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-
interoperation, and the requirements for SCAP content.
116-Rev.%201
SP 800-126A (DRAFT)
SCAP 1.3 Component Specification Version Updates: This recommendation provides a technical guideline
An Annex to NIST Special Publication 800-126 to use Personal Identity Verification (PIV) Cards in
Revision 3 physical access control systems (PACS), enabling federal
agencies to operate as government-wide interoperable
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-
enterprises. This recommendation covers the risk-
126A
based strategy to select appropriate PIV authentication
mechanisms as expressed within Federal Information
The Security Content Automation Protocol (SCAP) is
Processing Standard (FIPS) 201-2.
a multi-purpose framework of component specifications
that support automated configuration, vulnerability, and SP 800-114 Revision 1
patch checking, security measurement, and technical User’s Guide to Telework and Bring Your Own Device
control compliance activities. The SCAP version 1.3 (BYOD) Security
specification is defined by the combination of SP 800-
https://doi.org/10.6028/NIST.SP.800-114r1
126 Revision 3 and this document. This document allows
the use of particular minor version updates to SCAP 1.3
Many people telework, and they use a variety
component specifications and the use of particular Open
of devices, such as desktop and laptop computers,
Vulnerability and Assessment Language (OVAL) core
smartphones, and tablets, to read and send email, access
schema and platform schema versions. Allowing the
websites, review and edit documents, and perform many
use of these updates and schemas provides additional
other tasks. Each telework device is controlled by the
functionality for SCAP 1.3 without causing any loss of
organization, a third party (such as the organization’s
existing functionality.
contractors, business partners, and vendors), or the
teleworker; the latter is known as bring your own device
(BYOD). This publication provides recommendations
for securing BYOD devices used for telework and
remote access, as well as those directly attached to the
enterprise’s own networks.
115
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: ITL CYBERSECURITY PUBLICATIONS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

SP 800-90B (2nd Draft) Using these checklists can minimize the attack surface,
Recommendation for the Entropy Sources Used for reduce vulnerabilities, lessen the impact of successful
Random Bit Generation attacks, and identify changes that might otherwise go
undetected. To facilitate the development of checklists
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-
and to make checklists more organized and usable, NIST
90-B
established the National Checklist Program (NCP). This
publication explains how to use the NCP to find and
This Recommendation specifies the design
retrieve checklists, and it also describes the policies,
principles and requirements for the entropy sources
procedures, and general requirements for participation
used by Random Bit Generators, and the tests for the
in the NCP.
validation of entropy sources. These entropy sources are
intended to be combined with Deterministic Random SP 800-57 Part 1 Revision 4
Bit Generator mechanisms that are specified in SP 800- Recommendation for Key Management, Part 1:
90A to construct Random Bit Generators, as specified General
in SP 800-90C.
https://doi.org/10.6028/NIST.SP.800-57pt1r4
SP 800-90C (2nd Draft)
Recommendation for Random Bit Generator (RBG) This publication provides general cryptographic
Constructions key management guidance and is the first of three
parts. Part 1 defines cryptographic security services
http://csrc.nist.gov/publications/PubsSPs.html#SP-800-
that may be provided, provides background information
90-C
regarding the NIST-approved cryptographic algorithms,
classifies keys and other cryptographic information
This Recommendation specifies constructions for
according to their functions, specifies the protections
the implementation of random bit generators (RBGs).
required for each key type, identifies the functions
An RBG may be a deterministic random bit generator
involved in key management and discusses a variety of
(DRBG) or a non-deterministic random bit generator
key management issues related to the use of keys. Part
(NRBG). The constructed RBGs consist of DRBG
2 provides guidance on policy and security planning
mechanisms, as specified in SP 800-90A, and entropy
requirements for U.S. government agencies, and Part
sources, as specified in SP 800-90B.
3 provides guidance when using the cryptographic
SP 800-85A-4 features of current systems.
PIV Card Application and Middleware Interface Test
SP 800-46 Revision 2
Guidelines (SP 800-73-4 Compliance)
Guide to Enterprise Telework, Remote Access, and
https://doi.org/10.6028/NIST.SP.800-85A-4 Bring Your Own Device (BYOD) Security
SP 800-73 contains the technical specifications https://doi.org/10.6028/NIST.SP.800-46r2
to interface with the smart card to retrieve and use
For many organizations, their employees,
the PIV identity credentials. This document, SP 800-
contractors, business partners, vendors, and/or
85A, contains the test assertions and test procedures
others use enterprise telework or remote access
for testing smart card middleware as well as the card
technologies to perform work from external locations.
application. The tests reflect the design goals of
All components of these technologies, including
interoperability and PIV Card functions.
organization-issued BYOD client devices, should be
SP 800-70 Revision 3 secured against expected threats as identified through
National Checklist Program for IT Products: threat models. This publication provides information
Guidelines for Checklist Users and Developers on security considerations for several types of remote
access solutions, and it makes recommendations for
https://doi.org/10.6028/NIST.SP.800-70r3
securing a variety of telework, remote access, and BYOD
A security configuration checklist is a document that technologies. It also gives advice on creating related
contains instructions or procedures for configuring an security policies.
IT product for an operational environment, for verifying
that the product has been configured properly, and/or
116
for identifying unauthorized changes to the product.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

SP 800-38G utilization and security. This NIST Cybersecurity Practice
Recommendation for Block Cipher Modes of Guide provides a reference build of an ITAM solution.
Operation: Methods for Format-Preserving Encryption The build contains descriptions of the architecture, all
products used in the build and their individual
https://doi.org/10.6028/NIST.SP.800-38G
configurations. Additionally, this guide provides
a mapping of each product to multiple relevant
This Recommendation specifies two methods,
security standards. While the reference solution was
called FF1 and FF3, for format-preserving encryption
demonstrated with a certain suite of products, the
(FPE). Both of these methods are modes of operation
guide does not endorse these specific products. Instead,
for an underlying, approved symmetric-key block cipher
it presents the characteristics and capabilities of the
algorithm. FPE transforms data that is formatted as
products that an organization’s security experts can use
a sequence of symbols (e.g., a sequence of decimal
to identify similar standards-based products that can be
numbers) so that the encrypted form of the data has
integrated quickly and cost-effectively with a financial
the same format and length as the original plaintext
service company’s existing tools and infrastructure.
data. Thus, an FPE-encrypted Social Security Number
would be a sequence of nine decimal digits, rather than a SP 1800-4 (DRAFT)
sequence of symbols that may not be decimal numbers Mobile Device Security: Cloud and Hybrid Builds
and would very likely be longer than the original plaintext,
http://csrc.nist.gov/publications/PubsSPs.html#SP-1800-4
as is the case for other encryption modes.
SP 500-316 This document proposes a reference design on how
Framework for Cloud Usability to architect enterprise-class protection for mobile devices
accessing an organization’s resources. The example
https://doi.org/10.6028/NIST.SP.500-316
solutions presented here can be used by any organization
implementing an enterprise mobility management
Organizations are increasingly adopting cloud-
solution. This project contains two distinct builds: cloud
based services to meet their business needs. However,
and hybrid. The cloud build uses cloud-based services
due to the complexity and diversity of cloud systems it
and solutions, while the hybrid build achieves the same
is important to evaluate the user experience using within
functionality, but hosts at least some of the data and
a framework that encompasses the characteristics that
services within an enterprise’s own infrastructure. The
define the user experience. In this paper, we propose
example solutions and architectures presented here are
a cloud usability framework to provide a structure to
based on open standards and commercially available
evaluate the key attributes of the cloud user experience.
products.
The framework includes five attributes and 19 elements
that characterize this user experience. Generally these
NISTIRs
describe the consumer’s expectations of the cloud. The
framework can be the foundation for developing usability
metrics for organizations interested in measuring the
user experience when adopting the cloud. NISTIR 8150
Government Data De-Identification Stakeholder’s
SP 1800-5 (DRAFT)
Meeting, Meeting Report
IT Asset Management: Financial Services
https://doi.org/10.6028/NIST.IR.8150
http://csrc.nist.gov/publications/PubsSPs.html#SP-1800-5
The first Government Data De-Identification
While a physical asset management system can
Stakeholder’s Meeting was held at the National Institute
tell you the location of a computer, it cannot answer
of Standards and Technology on June 29, 2016. This
questions like, “What operating systems are our laptops
meeting featured 80 participants from 67 different
running?” and “Which devices are vulnerable to the
government agencies. Following the keynote, five panels
latest threat?” An effective IT asset management (ITAM)
discussed agency case studies, agency needs, available
solution can tie together physical and virtual assets and
solutions, governance, and evaluation of de-identification
provide management with a complete picture of what,
techniques. Eighteen presenters from eleven agencies
where, and how assets are being used. ITAM enhances
spoke for 10-minutes each. After each speaker’s
visibility for security analysts, which leads to better asset
presentation, audience members asked questions and 117
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: ITL CYBERSECURITY PUBLICATIONS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

elaborated on points that the speakers made. Overall, it responders with a modern array of network devices.
was the sense of the attendees that there is a need for Mobile applications stand to be an important resource
collaboration and the sharing of techniques for the de- that will be utilized by this network. However, current
identification of government data. mobile application developers may not be equipped
with the unique needs and requirements that must
NISTIR 8144 (DRAFT)
be met for operation on FirstNet’s network. It would
Assessing Threats to Mobile Devices & Infrastructure:
benefit the public safety community to leverage the
the Mobile Threat Catalogue
mobile application vetting services and infrastructures
http://csrc.nist.gov/publications/PubsNISTIRs.html#NIST- that already exist. These services currently target the
IR-8144 general public and enterprise markets. The purpose of
this document is to be an overview of existing mobile
Mobile devices pose a unique set of threats, yet
application vetting services, the features these services
typical enterprise protections fail to address the larger
provide and how they relate to public safety’s needs. This
picture. To fully address the threats presented by mobile
document is intended to aid public safety organizations
devices, a wider view of the mobile security ecosystem
when selecting mobile application vetting services for
is necessary. This document discusses the Mobile Threat
use in analyzing mobile applications.
Catalogue, which describes, identifies, and structures
NISTIR 8135
the threats posed to mobile information systems.
Identifying and Categorizing Data Types for Public
NISTIR 8138 (DRAFT)
Safety Mobile Applications: Workshop Report
Vulnerability Description Ontology (VDO): a
Framework for Characterizing Vulnerabilities https://doi.org/10.6028/NIST.IR.8135
http://csrc.nist.gov/publications/PubsNISTIRs.html#NIST- The Association of Public-Safety Communications
IR-8138 Officials (APCO), in cooperation with FirstNet and the
Department of Commerce held a half-day workshop on
This document aims to describe a more effective
June 2, 2015, “Identifying and Categorizing Data Types
and efficient methodology for characterizing the
for Public Safety Mobile Applications.” The goal of this
vulnerabilities found in various forms of software and
workshop was to begin identifying different types of
hardware implementations, including, but not limited
data that will flow through applications that operate
to, information technology systems, industrial control
on the National Public Safety Broadband Network
systems or medical devices to assist in the vulnerability
(NPSBN). A diverse group of first responders, industry
management process. The primary goal of the described
leaders, and government representatives attended
methodology is to enable automated analysis using
the workshop. This document describes the workshop
metrics such as the Common Vulnerability Scoring
and captures the input received from the workshop
System (CVSS). Additional goals include establishing
attendees.
a baseline of the minimum information needed to
NISTIR 8114 (DRAFT)
properly inform the vulnerability management process,
Report on Lightweight Cryptography
and facilitating the sharing of vulnerability information
across language barriers.
http://csrc.nist.gov/publications/PubsNISTIRs.html#NIST-
NISTIR 8136 (DRAFT) IR-8114
Mobile Application Vetting Services for Public Safety:
NIST-approved cryptographic standards are
an Informal Survey
designed to perform well using general-purpose
http://csrc.nist.gov/publications/PubsNISTIRs.html#NIST- computers. In recent years, there has been an
IR-8136 increased deployment of small computing devices
that have limited resources with which to implement
The Middle Class Tax Relief Act of 2012 mandated
cryptography. When current NIST-approved algorithms
the creation of the Nation’s first nationwide, high-speed
can be engineered to fit into the limited resources of
communications network dedicated for public safety.
constrained environments, their performance may
The law instantiated a new federal entity, the Federal
not be acceptable. For these reasons, NIST started
Responder Network Authority (FirstNet), to build,
a lightweight cryptography project that was tasked
118 maintain, and operate a new Long Term Evolution (LTE)
with learning more about the issues and developing
network. This network has the potential to equip first
a strategy for the standardization of lightweight
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2016
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM:
http://dx.doi.org/10.6028/NIST.SP.800-195

cryptographic algorithms. This report provides an supporting an organization’s risk-informed authorization
overview of the lightweight cryptography project at policies and evaluation.
NIST, and describes plans for the standardization of
NISTIR 8105
lightweight cryptographic algorithms.
Report on Post-Quantum Cryptography
NISTIR 8113
https://doi.org/10.6028/NIST.IR.8105
SATE V Ockham Sound Analysis Criteria
In recent years, there has been a substantial amount
https://doi.org/10.6028/NIST.IR.8113
of research on quantum computers – machines that
Static analyzers examine the source or executable exploit quantum mechanical phenomena to solve
code of programs to find problems. Many static analyzers mathematical problems that are difficult or intractable
use some heuristics or approximations to handle for conventional computers. If large-scale quantum
programs up to millions of lines of codes. We established computers are ever built, they will be able to break many
the Ockham Sound Analysis Criteria to recognize static of the public-key cryptosystems currently in use. This
analyzers whose findings are always correct. In brief would seriously compromise the confidentiality and
the criteria are (1) the analyzer’s findings are claimed to integrity of digital communications on the Internet and
always be correct, (2) it produces findings for most of a elsewhere. The goal of post-quantum cryptography (also
program, and (3) even one incorrect finding disqualifies called quantum-resistant cryptography) is to develop
an analyzer. This document begins by explaining the cryptographic systems that are secure against both
background and requirements of the Ockham Criteria in quantum and classical computers, and can interoperate
more detail. In Static Analysis Tool Exposition (SATE) V, with existing communications protocols and networks.
one tool, Frama-C, examined pertinent parts of the Juliet This Internal Report shares NIST’s current understanding
1.2 test suite to participate. We reviewed eight classes about the status of quantum computing and post-
of warnings, including improper buffer access, NULL quantum cryptography, and outlines NIST’s initial plan to
pointer dereference, integer overflow, and others. This move forward in this space. The report also recognizes
document details the many technical and theoretical the challenge of moving to new cryptographic
challenges we addressed to classify and review the infrastructures and, therefore, emphasizes the need for
warnings against the Criteria. It also reports anomalies, agencies to focus on crypto agility.
our observations, and interpretations. Frama-C reports
NISTIR 8103
led to the discovery of three unintentional, systematic
Advanced Identity Workshop on Applying
flaws in the Juliet test suite involving 416 test cases. Our
Measurement Science in the Identity Ecosystem:
conclusion is that Frama-C satisfied the SATE V Ockham
Summary and Next Steps
Sound Analysis Criteria.
https://doi.org/10.6028/NIST.IR.8103
NISTIR 8112 (DRAFT)
Attribute Metadata
On January 12-13, 2016, ACD hosted a workshop
on “Applying Measurement Science in the Identity
http://csrc.nist.gov/publications/PubsNISTIRs.html#NIST-
Ecosystem” to discuss the application of measurement
IR-8112
science to digital identity management. This document
This NIST Internal Report contains a metadata summarizes the concepts and ideas presented at the
schema for attributes that may be asserted about an workshop and serves as a platform to receive feedback
individual during an online transaction. The schema on the major themes discussed at that event.
can be used by relying parties to enrich access control
NISTIR 8101
policies, as well as during runtime evaluation of an
A Rational Foundation for Software Metrology
individual’s ability to access protected resources.
Attribute metadata could also create the possibility for https://doi.org/10.6028/NIST.IR.8101
data sharing permissions and limitations on individual
Much software research and practice involves
data elements. There are other possible applications of
ostensible measurements of software, yet little progress
attribute metadata, such as the evaluation and execution
has been made on an SI-like metrological foundation for
of business logic in decision support systems; however,
those measurements since the work of Gray, Hogan, et al.
the metadata contained in this document is focused on
in 1996-2001. Given a physical object, one can determine 119
THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM: ITL CYBERSECURITY PUBLICATIONS | FY 2016
http://dx.doi.org/10.6028/NIST.SP.800-195

physical properties using measurement principles and be deployed and used. Although first responders work
express measured values using standard quantities that in a variety of disciplines, this report is focused on the
have concrete realizations. In contrast, most software Fire Service, Emergency Medical Services (EMS), and
metrics are simple counts that are used as indicators Law Enforcement. This report describes the constraints
of complex, abstract qualities. In this report we revisit presented by their personal protective equipment (PPE),
software metrology from two directions: first, top specialized gear, and unique operating environments
down, to establish a theory of software measurement; and how such constraints may interact with mobile
second, bottom up, to identify specific purposes for authentication requirements. The overarching goal of
which software measurements are needed, quantifiable this work is analyzing which authentication solutions
properties of software, relevant units, and objects of are the most appropriate and usable for first responders
measurement. Although there are structural obstacles using mobile devices in operational scenarios in the field.
to realizing the vision of software metrology that works
NISTIR 8074 (2 volumes)
like physical metrology for all desired measurands,
Volume 1: Report on Strategic U.S. Government
progress is possible if we start with a rational foundation.
Engagement in International Standardization to
NISTIR 8085 (DRAFT) Achieve U.S. Objectives for Cybersecurity
Forming Common Platform Enumeration (CPE)
https://doi.org/10.6028/NIST.IR.8074v1
Names from Software Identification (SWID) Tags
This interagency report sets out proposed U.S.
http://csrc.nist.gov/publications/PubsNISTIRs.html#NIST-
Government strategic objectives for pursuing the
IR-8085
development and use of international standards
This report describes the association between for cybersecurity and makes recommendations to
the use of SWID Tags and the Common Platform achieve those objectives. The recommendations cover
Enumeration (CPE) specifications. The publication is interagency coordination, collaboration with the U.S.
intended as a supplement to NIST Internal Report 8060, private

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-25", "model": "gemini-3.5-flash-lite"} -->
