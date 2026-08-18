## Table of Contents
- [Welcome Letter](#welcome-letter)
- [Background Information of Annual Report](#background-information-of-annual-report)
- [Information Technology Laboratory (ITL) Cybersecurity Program Implements Federal Information Security Management Act](#information-technology-laboratory-itl-cybersecurity-program-implements-federal-information-security-management-act)
- [ITL Cybersecurity Program and Projects](#itl-cybersecurity-program-and-projects)
- [ITL Involvement with International IT Security Standards](#itl-involvement-with-international-it-security-standards)

# 2017 ANNUAL REPORT
## NIST/ITL CYBERSECURITY PROGRAM
### NIST SPECIAL PUBLICATION 800-203

THIS PAGE IS INTENTIONALLY LEFT BLANK

## ANNUAL REPORT 2017
### NIST/ITL CYBERSECURITY PROGRAM
**PATRICK O’REILLY, EDITOR** | **KRISTINA RIGOPOULOS, EDITOR**  
Computer Security Division | Applied Cybersecurity Division  
Information Technology Laboratory | Information Technology Laboratory  

**CO-EDITORS:**  
Larry Feldman  
Greg Witte  
G2, Inc.  
Annapolis Junction, Maryland  

THIS PUBLICATION IS AVAILABLE FREE OF CHARGE FROM  
https://doi.org/10.6028/NIST.SP.800-203  

**JULY 2018**  

**U.S. DEPARTMENT OF COMMERCE**  
Wilbur L. Ross, Jr., Secretary  

**NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY**  
Walter Copan, NIST Director and Under Secretary of Commerce for Standards and Technology  

---

### AUTHORITY
This publication has been developed by the National Institute of Standards and Technology (NIST) in accordance with its statutory responsibilities under the Federal Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3541 et seq., Public Law (P.L.) 113-283. NIST is responsible for developing information security standards and guidelines, including minimum requirements for federal information systems, but such standards and guidelines shall not apply to national security systems without the express approval of appropriate federal officials exercising policy authority over such systems. This guideline is consistent with the requirements of the Office of Management and Budget (OMB) Circular A-130.

Nothing in this publication should be taken to contradict the standards and guidelines made mandatory and binding on federal agencies by the Secretary of Commerce under statutory authority. Nor should these guidelines be interpreted as altering or superseding the existing authorities of the Secretary of Commerce, Director of the OMB, or any other federal official. This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST.

National Institute of Standards and Technology Special Publication 800-203  
Natl. Inst. Stand. Technol. Spec. Publ. 800-203, 175 pages (July 2018)  
CODEN: NSPUE2  

This publication is available free of charge from:  
https://doi.org/10.6028/NIST.SP.800-203  

### REPORTS ON COMPUTER SYSTEMS TECHNOLOGY
The Information Technology Laboratory (ITL) at NIST promotes the U.S. economy and public welfare by providing technical leadership for the Nation’s measurement and standards infrastructure. ITL develops tests, test methods, reference data, proof of concept implementations, and technical analyses to advance the development and productive use of information technology. ITL’s responsibilities include the development of management, administrative, technical, and physical standards and guidelines for the cost-effective security and privacy of other than national security-related information in federal information systems. The Special Publication 800-series reports on ITL’s research, guidelines, and outreach efforts in information system security, and its collaborative activities with industry, government, and academic organizations.

I  
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

---

### ACKNOWLEDGMENTS
The editors, Patrick O’Reilly of the Computer Security Division (CSD) and Kristina Rigopoulos of the Applied Cybersecurity Division (ACD), would like to thank their ITL colleagues who provided write-ups on their project highlights and accomplishments for this annual report (their names are mentioned after each project write-up). The editors would also like to acknowledge Elaine Barker (CSD) and Lisa Carnahan (Standards Coordination Office, NIST), for reviewing and providing valuable feedback for this annual report.

The editors would also like to acknowledge Natasha Hanacek (Graphic Designer, NIST Public Affairs Office) for designing the cover and inside layout for this annual report.

### DISCLAIMER
Any mention of commercial products or organizations is for informational purposes only; it is not intended to imply recommendation or endorsement by the National Institute of Standards and Technology, nor is it intended to imply that the products identified are necessarily the best available for the purpose.

### TRADEMARK INFORMATION
All names are trademarks or registered trademarks of their respective owners.

II  
ACKNOWLEDGMENTS | FY 2017

---

## TABLE OF CONTENTS
- [WELCOME LETTER](#welcome-letter)
- [ITL INVOLVEMENT WITH INTERNATIONAL IT SECURITY STANDARDS](#itl-involvement-with-international-it-security-standards)
- [RISK MANAGEMENT](#risk-management)
- [BIOMETRIC STANDARDS AND ASSOCIATED CONFORMITY ASSESSMENT TESTING TOOLS](#biometric-standards-and-associated-conformity-assessment-testing-tools)
- [CYBERSECURITY APPLICATIONS](#cybersecurity-applications)
- [SOFTWARE ASSURANCE & QUALITY](#software-assurance--quality)
- [FEDERAL CYBERSECURITY RESEARCH AND DEVELOPMENT (R&D)](#federal-cybersecurity-research-and-development-rd)
- [COMPUTER FORENSICS](#computer-forensics)
- [CYBERSECURITY AWARENESS, TRAINING, EDUCATION, AND OUTREACH](#cybersecurity-awareness-training-education-and-outreach)
- [CRYPTOGRAPHIC STANDARDS PROGRAM](#cryptographic-standards-program)
- [VALIDATION PROGRAMS](#validation-programs)
- [IDENTITY AND ACCESS MANAGEMENT](#identity-and-access-management)
- [RESEARCH IN EMERGING TECHNOLOGIES](#research-in-emerging-technologies)
- [NATIONAL CYBERSECURITY CENTER OF EXCELLENCE (NCCoE)](#national-cybersecurity-center-of-excellence-nccoe)
- [INTERNET INFRASTRUCTURE PROTECTION](#internet-infrastructure-protection)
- [ADVANCED SECURITY TESTING AND MEASUREMENTS](#advanced-security-testing-and-measurements)
- [TECHNICAL SECURITY METRICS](#technical-security-metrics)
- [USABILITY AND SECURITY](#usability-and-security)
- [ITL CYBERSECURITY PROGRAM RELATED PUBLICATIONS](#itl-cybersecurity-program-related-publications)
- [ITL PUBLICATIONS RELEASED DURING FY 2017](#itl-publications-released-during-fy-2017)
- [APPENDICES](#appendices)

III  
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

THIS PAGE IS INTENTIONALLY LEFT BLANK  
IV  
TABLE OF CONTENTS | FY 2017

---

## WELCOME LETTER

If recent events involving the security of information and operations have taught us anything, it is that cybersecurity, and the way cybersecurity risks are managed, are no longer solely the domain of the information technology specialist. Cybersecurity risk management issues are becoming increasingly familiar topics in executive management offices and boardrooms. That is as true for businesses as it is for federal and other government organizations.

No doubt that is because every year brings more troubling reports of organizations experiencing financial and reputational damage from both novel and well-known threats and vulnerabilities. But what does not get nearly as much attention are the impressive advances that so many organizations have been making in thoughtfully and successfully securing their information and processes and the systems upon which those organizations, their leaders, and their customers depend.

That’s where the cybersecurity work of the National Institute of Standards and Technology (NIST) comes into play. For nearly 50 years, we have been helping organizations to succeed in building the strategies and in employing the tools needed to better recognize, anticipate, and manage cybersecurity risks. Our diverse cybersecurity activities are an essential ingredient in carrying out the NIST Information Technology Laboratory’s mission: to cultivate trust in information and technology. We do that by conducting foundational and applied cybersecurity research to produce and advance cybersecurity standards, best practices, measurements, and reference resources. While NIST has an explicit statutory mission to focus on federal government agencies, our work can and is being heavily leveraged by large and small businesses, state and local agencies, and other organizations. Ultimately, this benefits taxpayers, investors, consumers, our digital economy, and our national security.

However, we don’t work alone. To the contrary, all cybersecurity efforts at NIST are based on input from, and often in cooperation with, the private sector and other government agencies.

We also don’t work in the dark. NIST prides itself on being transparent, open, and collaborative. When we actively engage the private and public sectors, we rely on and use experts from around the country – and around the globe – to complement the talents of our own staff. Exposing our thinking to others helps to improve the quality, relevance, and likely use of the end product.

This report features some of our most significant accomplishments during Fiscal Year (FY) 2017 in risk management, cryptography, identity and access management, vulnerability management, education and workforce development, and internet and communications infrastructure, as well as our efforts to transition our work into common practice. Below are just a few highlights of the work carried out in 2017.

- In recent years, there has been a substantial amount of research on quantum computers – machines that exploit quantum mechanical phenomena to solve problems that are difficult or intractable for conventional computers. If large-scale quantum computers are ever built, they will be able to break the existing infrastructure of public-key cryptography. Employing NIST’s proven approach of worldwide open competitions, in 2016 we solicited submissions for quantum-resistant public-key cryptographic algorithms for standards. These algorithms must be secure against both quantum and classical computers and should interoperate with existing communications protocols and networks. We now are engaging the cryptographic community in the difficult work of determining how the 69 submissions we received in 2017 meet the competition’s exacting requirements.
- In instances where many devices are interconnected and working in concert to accomplish some task, security and privacy can be very important but hard to achieve due to limited capabilities available to handle modern cryptographic algorithms. This includes automotive systems, sensor networks, healthcare, distributed control systems, the smart grid, and cyber-physical systems and the Internet of Things (IoT). Recognizing this special challenge and in order to gain greater awareness and involvement with the cryptographic community, NIST shared its findings in this area (known as lightweight cryptography) and presented our plans to address standardization issues for community feedback.
1  
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

- NIST improved two widely used guidelines that provide senior leaders with the information they need to make risk-based decisions affecting critical mission and business functions. We proposed revisions to Security and Privacy Controls for Information Systems and Organizations (Special Publication (SP) 800-53) and Risk Management Framework for Information Systems and Organizations (SP 800-37). The latter provides a closer link between risk management processes and activities at various organizational levels. It demonstrates how the Cybersecurity Framework can be implemented using established Risk Management Framework processes. Both publications will be finalized in 2018.
- Reflecting a growing recognition of the link between cybersecurity and privacy risk management, we collaborated with internal and external partners to integrate privacy requirements and considerations into SP 800-53 and SP 800-37 risk management guidelines as well as our latest version of NIST’s Digital Identity Guidelines (SP 800-63-3), which covers digital identity from the initial risk assessment to the deployment of federated identity solutions. These guidelines build the foundation needed to make privacy and security equal, quality attributes in trustworthy systems. We focused on encouraging the adoption of trusted identities through digital identity standards for federal agencies and internationally.
- The supply chain that provides the information and operational technology (IT/OT) upon which we all depend has evolved into a complex, globally distributed, dynamic ecosystem enabling the development of highly refined, sophisticated, cost-effective, and reusable solutions. In FY 2017, we published a proposed process model providing a method to identify and prioritize IT/OT systems and components. The approach aims to increase an organization’s ability to make cost-effective risk decisions by determining the systems and components that have the greatest impact on the organization and that would potentially cause the most harm if compromised.
- As NIST continues to collaborate with stakeholders to raise awareness and encourage the use of the voluntary Cybersecurity Framework, we solicited public comments on a draft update of the first (2014) version and hosted a widely attended workshop that charted progress and shared issues to which NIST now has given additional attention. In May 2017, the President’s Executive Order 13800 directed federal agency heads to use the Cybersecurity Framework to manage cybersecurity risk. In response, NIST released draft guidance on how the Risk Management Framework and Cybersecurity Framework can work together to help agencies develop, implement, and continuously improve their information security programs. After incorporating public comments, NIST released the Baldrige Cybersecurity Excellence Builder, a self-assessment tool based in part on the Cybersecurity Framework, to help organizations better understand the effectiveness of their cybersecurity risk management efforts.
- In FY 2017, NIST’s National Cybersecurity Center of Excellence (NCCoE) began taking full advantage of its expanded, more capable facilities to accelerate the adoption of standards-based, security technologies. Healthcare and financial services were two areas that had notable progress, including the development of new draft practice guides on securing wireless infusion pumps and on managing access rights for the financial sector. NCCoE also leveraged industry partners’ expertise to produce a guide on how organizations can develop strategies to recover operating systems, user files, applications, and other IT assets from data corruption events such as ransomware. The guide also offers insights on auditing, reporting, and investigations following a company’s discovery of such destructive security incidents. Other guides addressed the authentication of mobile device users with personal identity verification credentials and how organizations can use attribute-based access controls to better manage employee access to data and networks. 
2  
WELCOME LETTER | FY 2017

- The NIST-led National Initiative for Cybersecurity Education (NICE) made noteworthy strides in FY 2017 to foster, energize, and promote a robust network and an integrated ecosystem of cybersecurity education, training, and workforce development. We published the NICE Cybersecurity Workforce Framework, establishing a taxonomy and common lexicon to describe all cybersecurity work and workers, irrespective of where or for whom the work is performed. NICE launched “CyberSeek,” an online tool that provides a visualization of the demand for and the supply of cybersecurity workers across the country as well as career pathways in cybersecurity. Via NICE, NIST served as the Commerce Department’s lead, working with the Department of Homeland Security (DHS) to analyze U.S. cybersecurity workforce issues and offer recommendations in response to the President’s May 2017 Executive Order.

Looking ahead - with full knowledge that new challenges are constantly emerging - we are moving towards collaborating with industry, government agencies, and others who use NIST’s cybersecurity research, standards, and guides. For example, in FY 2018 NIST is assigning higher priority to the cybersecurity and privacy aspects of the Internet of Things (IoT). Researchers in our Cybersecurity for IoT program are working with industry to produce guidance and best practices, as well as to perform research and coordinate standards within and across sectors in the digital economy. We are reviewing international standards-based approaches to the IoT challenges and ramping up our IoT-related identity work. NIST is also launching a project to provide organizations with practical guidance to reduce the vulnerability of IoT devices to botnets and other automated distributed threats, while also limiting the utility of compromised devices to malicious actors. Such efforts are paving the way toward more secure IoT devices in the future.

In addition to the work in IoT, NIST has embarked on a project to automate much of the testing required under the cryptographic validation programs. We expect that automated cryptographic algorithm testing will be complete in 2018, and we will then begin developing methods to automate the testing of cryptographic modules. These efforts in automation are intended to provide a higher trust in the assurance claims made by the product developers, but do so in an efficient, and cost-effective manner that allows the vendors’ conformance efforts to keep pace with the changing IT landscape. By investing in a more robust testing infrastructure, NIST hopes that product vendors will take advantage of this service by validating their products more often, which will produce more secure products.

In reporting on our accomplishments, NIST welcomes all suggestions about how we can improve our work. We do this so that we can provide the nation with the kind of cybersecurity information and tools needed to cultivate trust in information and technology while advancing and protecting our economy and our nation.

All projects in this report include contact information for the key NIST contacts. Let us hear from you.

Donna F. Dodson,  
NIST Chief Cybersecurity Advisor  
3  
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

---

## BACKGROUND INFORMATION OF ANNUAL REPORT

This Annual Report provides the opportunity to describe the many cybersecurity program highlights and accomplishments from throughout the NIST Information Technology Laboratory (ITL). The report is organized into several sections, each section is identified by a title page.

Please note: This Annual Report covers the Federal Government’s Fiscal Year (FY) 2017, from October 1, 2016 to September 30, 2017.

ITL, an operating unit under NIST, contains seven divisions. Cybersecurity work is conducted by each, and is the sole focus of the Applied Cybersecurity and Computer Security Divisions. Throughout this Annual Report, there are references to particular division activities, and often to work by groups within those divisions. Primarily, the authors of each segment of the report have attributed accomplishments to ITL, since the ITL staff have been involved with each cybersecurity program included in this Annual Report. At the end of each program/project write-up, one or more points of contact are provided and may be used to address questions or requests for more information. Many sections also include additional references that readers may find valuable.

Below is a condensed hierarchical chart of ITL’s structure:

**INFORMATION TECHNOLOGY LABORATORY (ITL) OFFICE**  
Charles Romine, Director  
Jim St. Pierre, Deputy Director  

- **Applied Cybersecurity Division (ACD)**  
  Kevin Stine, Division Chief  
- **Computer Security Division (CSD)**  
  Matthew Scholl, Division Chief  
- **Applied and Computational Mathematics Division (ACMD)**  
  Ronald F. Boisvert, Division Chief  
- **Advanced Network Technologies Division (ANTD)**  
  Abdella Battou, Division Chief  
- **Information Access Division (IAD)**  
  Shahram Orandi, Division Chief  
- **Software and Systems Division (SSD)**  
  Ram Sriram, Division Chief  

ITL’s Cybersecurity Program is pleased to share these achievements and accomplishments made during the 2017 Fiscal Year in this Annual Report.  
4  
INTRODUCTION | FY 2017

---

## THE INFORMATION TECHNOLOGY LABORATORY IMPLEMENTS THE FEDERAL INFORMATION SECURITY MANAGEMENT ACT

This section contains a list of the major activities that were accomplished during FY 2017 by the ITL Cybersecurity Program. Detailed explanations of these activities are provided in the next section.  
5  
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

---

## INFORMATION TECHNOLOGY LABORATORY (ITL) CYBERSECURITY PROGRAM IMPLEMENTS FEDERAL INFORMATION SECURITY MANAGEMENT ACT

The E-Government Act, Public Law 107-347, passed by the 107th Congress and signed into law by the President in December 2002, recognized the importance of information security to the economic and national security interests of the United States. Title III of the E-Government Act, titled the Federal Information Security Management Act (FISMA) of 2002, included the duties and responsibilities for the National Institute of Standards and Technology, Information Technology Laboratory (ITL). There are multiple divisions within ITL that are involved with cybersecurity programs and projects. The work is being conducted collaboratively between the divisions. In December 2014, the 113th Congress updated FISMA as the Federal Information Security Modernization Act (Public Law 113-283). NIST ITL responsibilities were unchanged in the update. In FY 2017, the ITL Cybersecurity Program addressed its assignment through the following major activities:

- **Forty-one NIST Special Publications (SP)** (20 approved as final and 21 drafts) were issued, providing management, operational, and technical security guidelines in a variety of topic areas, including:
  The 2016 Annual Report, the National Initiative for Cybersecurity Education (NICE) Cybersecurity Workforce Framework, attribute-based access control and access control standards and policies, application container security, Secure Hash Algorithm-3 (SHA-3) derived functions, cybersecurity event recovery, data integrity, recovering from ransomware and other destructive events, securing Apple OS X 10.10 systems, protecting controlled unclassified information in nonfederal information systems and organizations, systems security engineering, cyber threat information sharing, bluetooth security, the National Checklist Program, digital identity guidelines, block cipher modes of operation, the Cipher-Based Message Authentication Code (CMAC) - a Mode for Authentication, an introduction to information security, a report of the workshop on software measures and metrics to reduce security vulnerabilities, platform firmware resiliency, fog computing, de-identifying government datasets, Long Term Evolution (LTE) security, trustworthy email, security recommendations for hypervisor deployment, the Triple Data Encryption Algorithm (TDEA) Block Cipher, key-derivation methods in key-establishment schemes, pair-wise key-establishment schemes using discrete logarithm cryptography, security and privacy controls, a risk management framework for information systems and organizations, personal identity verification (PIV) credentials, access rights management for the financial services sector, securing wireless infusion pumps in healthcare delivery organizations, situational awareness for electric utilities, and domain name systems-based electronic mail security.
- **Fifteen NIST Interagency/Internal Reports (NISTIR)** (10 approved as final and 5 drafts) were issued on a variety of topics, including:
  A criticality analysis process model, security assurance challenges for container deployment, the cybersecurity framework for federal agencies, a cybersecurity framework manufacturing profile, dramatically reducing software vulnerabilities, code complexity on software analysis, identifying uniformity with entropy and divergence, enhancing resilience of the Internet and communications ecosystem, mobile application vetting services for public safety, lightweight cryptography, privacy engineering and risk management in federal systems, automation support for security control assessments, and small business information security.
- **Formally Launched a Post-Quantum Cryptography (PQC) Standardization Process:**
  The research community has actively responded to the NIST Call for Proposals to solicit, evaluate, and standardize quantum-resistant public key cryptography (also known as post-quantum cryptography (PQC)) algorithms. Upon the submission deadline, NIST received 82 submissions from 26 countries and 6 continents, among which 69 submissions are considered as complete and proper. The NIST Post-Quantum Cryptography team has worked closely with the submitters and the research community to evaluate and analyze the first-round candidates.
6  
ITL IMPLEMENTS THE FISMA ACTIVITIES | FY 2017

- **Lightweight Cryptography Standards for the Internet of Things (IoT):**
  The Internet of Things (IoT) tethers heterogeneous “things” together. Some of the “things” are resource constrained. Lightweight cryptography provides critical tools for IoT security. To better understand the need for dedicated lightweight cryptography, the NIST team released a white paper in 2017 to specify two major portfolios for lightweight cryptography primitives. NIST will announce a call for proposals on lightweight cryptography primitives in 2018.
- **A NIST / Industry joint working group continued the development of automated cryptographic implementation testing:**
  After working with industry on the protocol necessary to exchange cryptographic test data in an automated fashion, the development of the cryptographic algorithm testing service to be hosted at NIST is fully under way, with the full implementation expected in FY 2018. (See: http://csrc.nist.gov/projects/acvt).
- **Published an Initial Public Draft of Special Publication (SP) 800-53, Revision 5:**
  NIST SP 800-53 Revision 5, Security and Privacy Controls for Information Systems and Organizations, is a comprehensive set of safeguarding measures that are applicable to all types of computing platforms, including traditional IT systems, cloud and mobile systems, industrial/process control systems, and Internet of Things (IoT) devices. The safeguarding measures in the update to this publication include a full integration of security and privacy controls to protect the operations and assets of organizations and the personal privacy of individuals. Additionally, this update promotes the integration with different risk management and cybersecurity approaches and lexicons, including the Cybersecurity Framework. The Initial Public Comment period resulted in over 3000 comments from over 115 different stakeholders representing the public and private sectors, and academia.
- **Published a Discussion Draft of SP 800-37, Revision 2:**
  This update to NIST SP 800-37 Revision 2, Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy, responds to the call by the Defense Science Board, the President’s Executive Order on Strengthening the Cybersecurity of Federal Networks and Critical Infrastructure, and the Office of Management and Budget Memorandum M-17-25, to develop the next-generation Risk Management Framework (RMF) for systems and organizations. This update provides linkage and communication between the risk management processes and activities at the executive and operational levels of the organization; demonstrates how the Cybersecurity Framework can be implemented using the established NIST risk management processes (i.e., developing a Federal use case); and integrates privacy concepts into the RMF. This discussion draft was issued to inform a public workshop for RMF stakeholders and featured discussions on the risk management methodologies used in various sectors and potential opportunities to improve the RMF.
- **The Cyber Supply Chain Risk Management (C-SCRM) program continued to work with stakeholders to develop and improve FISMA-related guidance on C-SCRM:**
  C-SCRM controls were significantly modified in a draft of NIST SP 800-53, Security and Privacy Controls for Information Systems and Organizations, to better align with other guidance. A working group co-chaired by NIST and the Department of Defense
7  
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

completed a revision of Committee On National Security Systems Directives (CNSSD) Number 505, Supply Chain Risk Management, which assigns responsibilities and establishes minimum criteria for the development and deployment of supply chain risk management capabilities for national security systems. Also, NIST collaborated with over 3,000 stakeholders through the Software and Supply Chain Assurance (SSCA) Forum and email list service. The effort, initiated in 2003, is co-led by NIST, the Department of Homeland Security (DHS), the Department of Defense (DOD) and the U.S. General Services Administration (GSA) and provides a venue for government, industry, and academic participants from around the world to discuss cyber supply chain risks, effective practices and mitigation strategies, tools and technologies, and any gaps related to the people, processes, or technologies involved.
- **The goal of the ITL’s Usable Security and Privacy project team is to provide guidance for policymakers, system engineers and security professionals so that they can make better decisions that enhance the usability of cybersecurity in their organizations:**
  The Usable Security and Privacy team contributed usability chapters to SP 800-63, Digital Identity Guidelines, marking the first time there were dedicated usability chapters in this flagship NIST security publication. In addition, the usability team also completed a long-term operational phishing evaluation, demonstrating the importance of individual user context in explaining phishing email click decisions.
- **Method developed for efficient automated testing of systems used in Artificial Intelligence (AI) applications:**
  NIST developed a method of automatically testing and verifying rule-based systems to a high degree of assurance. The method uses a mathematical construct known as a covering array to exhaustively test all components of rules used in many classes of artificial intelligence applications, for a large subset of such applications. The method was incorporated into a proof-of-concept software tool that is freely available.
- **Final Draft of a NIST Special Publication providing guidance on how to securely configure Apple OS X systems:**
  NIST developed this publication to assist IT professionals in securing Apple OS X 10.10 desktop and laptop systems within various environments. It provides detailed information about the security features of OS X 10.10 and security configuration guidelines. The publication recommends and explains tested, secure settings with the objective of simplifying the administrative burden of improving the security of OS X 10.10 systems in three types of environments: Standalone, Managed, and Specialized Security-Limited Functionality.
- **Began the integration of privacy into the Risk Management Framework documents:**
  A July 2016 update to Office of Management and Budget (OMB) Circular A-130 requires federal agencies to apply the Risk Management Framework to privacy programs - managing privacy risk beyond compliance with privacy laws, regulations and policies. In alignment with this policy, the Privacy Engineering Program in ITL has been working to integrate privacy into the Risk Management Framework documents, providing one unified security and privacy approach – as seen in the initial draft of SP 800-53rev5 and the discussion draft of SP 800-37rev2.
- **Introduced concepts for privacy engineering and risk management as the foundation for the integration of privacy into the Risk Management Framework documents:**
  The Privacy Engineering Program in ACD published NISTIR 8062, An Introduction to Privacy Engineering and Risk Management in Federal Systems. This publication establishes the basis for a common vocabulary to facilitate better understanding and communication of privacy risk within federal systems, and the effective implementation of privacy principles. It introduces two key components to support the application of 8  
ITL IMPLEMENTS THE FISMA ACTIVITIES | FY 2017

privacy engineering and risk management: privacy engineering objectives and a privacy risk model. These concepts lay the foundation for the integration of privacy into the Risk Management Framework (as seen in the latest revisions of SP 800-53 and SP 800-37).
- **Comprehensive Security Guidance for Virtualized Infrastructures and Contributions to Standards Development:**
  A set of security recommendations for server virtualization were updated in the publication of SP 800-125A, Security Recommendations for Hypervisor Deployment on Servers, including emerging use cases. NIST security guidance for this technology now covers hardware, hypervisor (the core server virtualization software), virtual network and management modules. The active participation of NIST in the editorial team for the International Organization For Standardization/International Electrotechnical Commission (ISO/IEC) 21878, Security guidelines for design and implementation of virtualized servers, has advanced the standard from a working draft in October 2016 to a Draft International Standard (DIS) in October 2017. In the area of OS virtualization, the potential solutions for security countermeasures outlined in SP 800-190, Application Container Security Guide, were examined, and security assurance requirements for each solution were developed to guide actual security configurations. These security assurance requirements were published in NISTIR 8176, Security Assurance Requirements for Linux Application Container Deployments, for the open source Linux platform where application containers are ubiquitously developed and deployed.
- **Established the NIST Cybersecurity Program for the Internet of Things (IoT):**
  ITL created a program for IoT cybersecurity that supports the development and application of standards, guidelines, and related tools to improve IoT cybersecurity. Program establishment included creating an inventory of NIST-wide efforts related to IoT 9 cybersecurity, coordinating among NIST IoT cybersecurity efforts, and convening a team of subject-matter experts to begin drafting guidance on managing IoT cybersecurity and privacy risks.
- **The IoT Program convened cross-sector stakeholders to inform IoT cybersecurity efforts:**
  The IoT Cybersecurity Program coordinated outreach to a range of public and private-sector stakeholders to inform them of NIST’s IoT cybersecurity work and collect feedback to inform future work. This included sessions at the Cybersecurity Framework Workshop in 2017, the Industrial Internet Consortium (IIC) quarterly meeting, and planning a colloquium with industry, government, and academic participants.
- **The National Initiative for Cybersecurity Education (NICE) program provided numerous communication channels and maintained a visible high-level presence in supporting its mission to the cybersecurity workforce and education fields:**
  The NICE program published three eNewsletters; launched an updated and refreshed the NICE Website to better meet the needs of the NICE Community and visitors; produced 3 new one-page reports and updated the content of three others; produced two ITL Science Day posters; established a LinkedIn presence and hashtag for Tweets from the @NISTCyber twitter account; developed a NICE Multimedia page; participated in seven conference exhibit displays; and hosted ten webinar sessions.
- **The NICE Program also developed and published two NIST publications to support the Cybersecurity Workforce:**
  During FY 2017, the NICE Program published NIST Special Publication 800-181, National Initiative for Cybersecurity Education (NICE) Cybersecurity Workforce Framework, and the Draft NIST Interagency Report (NISTIR) 8193, National Initiative for Cybersecurity Education (NICE) Framework Work Role Capability Indicators: Indicators for Performing Work Roles. The national need for a common lexicon to describe and organize the cybersecurity workforce and the requisite knowledge, skills, and abilities (KSAs) led to the creation of the NICE Cybersecurity Workforce Framework (NICE Framework). The NICE Framework defines the spectrum of cybersecurity work as well as tasks for over 50 common Work Roles. While the Work Roles have made the NICE Framework easier to associate with specific positions, they do not provide organizations with guidance on how to determine if a cybersecurity worker can perform a Work Role. NISTIR 8193 is intended to help organizations address this challenge by identifying capability indicators or recommended education, certification, training, experiential learning, and continuous learning that could signal an increased ability to perform a given Work Role.
- **The NICE program provided strategic outreach and engagement with stakeholders throughout FY 2017:**
  The NICE Program increased its outreach efforts to include new academic, industry, and government organizations, including international stakeholders through various meetings and collaborative efforts including the NICE Working Group and NICE Interagency Coordinating Council.
- **Seven NIST National Cybersecurity Center of Excellence (NCCoE) Special Publications (SP) 1800 Series Practice Guides (one revised draft and six new drafts) were issued, providing management, operational, and technical security guidelines in topic areas including:**
  Attribute Based Access Control, Domain Name Systems-Based Email Security, Situational Awareness for the Electric Utilities, Securing Wireless Infusion Pumps in Healthcare Delivery Organizations, Managing Access Rights in the Financial Services Sector, Data Integrity: Recovering from Ransomware and Other Destructive Events, and Derived Personal Identity Verification (PIV) Credentials.
- **The ITL Software Assurance and Quality Program researched and improved how to assess a tool’s ability to detect and identify**
10  
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

code problems in the Software Assurance Metrics And Tool Evaluation (SAMATE) program:
The SAMATE program has three primary components: the Software Assurance Reference Dataset (SARD), the Static Analysis Tool Exposition (SATE), and the Bugs Framework (BF). Mobile applications and test cases used in former Static Analysis Tool Expositions were added to SARD. In 2017, the sixth instance of SATE began.
- **ITL’s Computer Forensics Team researched ways to improve the methods for securely acquiring, storing and analyzing digital evidence quickly and efficiently:**
  ITL promoted the efficient and effective use of computer technology to investigate crimes. The project team developed tools for testing computer forensic software, including test criteria and test sets. ITL also maintains the National Software Reference Library (NSRL) – a vast archive of published software applications that is an important resource for both criminal investigators and historians. The NSRL published four releases of the Reference Data Set (RDS) that continues to be the premier software resource. The NSRL was expanded to include mobile apps and to include the profiles obtained from installing and exercising applications.
- **Ongoing involvement and outreach support among various programs:**
  ITL provided assistance to agencies and the private sector through many outreach programs, including the National Initiative for Cybersecurity Education (NICE), the Federal Information Systems Security Educators’ Association (FISSEA), and the Federal Computer Security Managers’ Forum.
- **Continued support and involvement of the Information Security and Privacy Advisory Board (ISPAB):**
  NIST solicited recommendations from the Information Security and Privacy Advisory Board (ISPAB) on draft standards and guidelines regarding information security and privacy issues. 11  
ITL IMPLEMENTS THE FISMA ACTIVITIES | FY 2017

- **In support of FISMA activities, ITL conducted workshops, awareness briefings, webinars, and various outreach to ITL customers:**
  The ITL Cybersecurity Program hosted or provided at least 55 different cybersecurity events throughout FY 2017. These outreach activities were open to the public or for federal agencies. These events covered various Cybersecurity topics – to see the complete list of these events, please see Appendix B at the back of this Annual Report for further details. If a website URL is available for these events – the URLs have been provided.
- **Annual Reports:**
  The ITL Fiscal Year 2017 Cybersecurity Program Annual Report (formerly titled Computer Security Division Annual Report) was produced and released as a NIST SP. This report, and previously released CSD annual reports from fiscal years 2003 through 2017, are available on the Computer Security Resource Center (CSRC) website at https://csrc.nist.gov/publications/search?topics-lg=3363%7Cannual+reports  
11  
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

---

## ITL CYBERSECURITY PROGRAM AND PROJECTS

The next section describes accomplishments that were achieved during FY 2017 (covering the time frame October 1, 2016 to September 30, 2017) for the NIST ITL Cybersecurity Program.

*(Editors’ Note: Acronyms used throughout this Annual Report are generally defined when first used. A complete list of Acronyms used in this report is provided in Appendix A of this Annual Report.)*  
12  
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

---

## ITL INVOLVEMENT WITH INTERNATIONAL IT SECURITY STANDARDS

### ITL Involvement with National and International IT Security Standards Work

The following paragraphs discuss ITL staff activities in conjunction with the InterNational Committee for Information Technology Standards (INCITS) Technical Committee Cybersecurity 1 (CS1), where ITL’s Mr. Sal Francomacaro serves as the CS1 Vice Chair. CS1 is the U.S. counterpart for the ISO/IEC SC27 committee for IT Security.

The ITL staff actively participate with JTC1/SC27 and its working groups to develop standards for the protection of information and communications technology (ICT). This includes generic methods, techniques and guidelines to address both security and privacy aspects, such as:
- Management of information and ICT security; in particular, information security management systems, security processes, and security controls and services;
- Cryptographic and other security mechanisms, including but not limited to, mechanisms for protecting the accountability, availability, integrity and confidentiality of information;
- Security management support documentation, including terminology and guidelines as well as procedures for the registration of security components;
- Security aspects of identity management, biometrics and privacy;
- Conformance assessment, accreditation and auditing requirements in the area of information security management systems; and
- Security evaluation criteria and methodology.

The ITL staff also engages in active liaison and collaboration with appropriate bodies to ensure the proper development and application of SC 27 standards and technical reports in relevant areas.

**CONTACT:**  
Mr. Salvatore Francomacaro  
(301) 975-6414  
salfra@nist.gov  

### NIST Cybersecurity Framework – International Standardization

The NIST/ITL staff actively participate with JTC1/SC27 and its working groups to support the NIST Cybersecurity Framework International Standardization strategy.

(BT-SEG); the International Telecommunications Union - Telecommunication Standardization Sector (ITU-T); various groups within the Institute of Electrical and Electronics Engineers (IEEE) and the Internet Engineering Task Force (IETF); the North American Security Products Organization (NASPO); the Trusted Computing Group (TCG); and Accredited Standards Committee X9, Inc. (ASC X9, Inc.) (e.g., X9F – Data & Information Security Subcommittee). Many of ITL’s publications have been the basis for both national and international standards projects.

![SDOs involved in Cybersecurity](Figure 1: SDOs involved in Cybersecurity)

### Focus on ISO and ANSI Standardization (ISO/IEC JTC1 SC27 IT Security)

The main focus for FY 2017 was the development of a Technical Specification based on ISO/IEC 27101 – Guidelines for developing cybersecurity frameworks. This Technical Specification (TS) represents the work done by a U.S. group on NIST Cybersecurity Framework and should serve as a guideline for other organizations considering creating a new cybersecurity framework.

The NIST staff was also active in the definition of another ISO Technical Specification: Cybersecurity Overview and Concepts. This TS should target any user concerned with cybersecurity, but is particularly targeted toward decision makers. It should cover, among other things, what cybersecurity IS and IS NOT, how it applies to existing standards, and how it fits in with the other ISO/IEC 27000 series of standards.

The NIST staff will increase participation and effort on these activities during FY 2018.

**CONTACT:**  
Mr. Matt Barrett  
(301) 975-6259  
matthew.barrett@nist.gov  

### ISO Standardization of Security Requirements for Cryptographic Modules

ITL is also the principal editor, co-editor, and contributor to many ISO/IEC documents by the ISO/IEC International Organization for Standardization. ITL’s contributions to the development of these international standards help to create a strong foundation for the adoption of and migration from currently used national standards. In particular, this adoption promotes international harmonization for the implementation and testing of cryptographic algorithms and modules, while accommodating individual country preferences in the choice of approved security functions.

ITL has contributed to the activities of ISO/IEC JTC 1 SC/27, which published ISO/IEC 19790, Security Requirements for Cryptographic Modules, on March 1, 2006, and ISO/IEC 24759, Test Requirements
14  
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

for Cryptographic Modules, on July 1, 2008. ISO/IEC 19790 specifies the security requirements for a cryptographic module utilized within a security system protecting sensitive information in computer and telecommunication systems. These efforts bring consistent testing of cryptographic modules to the global community by providing ISO-equivalent standards representing Federal Information Processing Standard (FIPS) 140-2, Security Requirements for Cryptographic Modules. Mr. Randall Easter (CSD) continues as the principal editor for these standards.

ISO/IEC JTC 1/SC 27 Working Group (WG) 3 completed and published revisions, updated corrections, of ISO/IEC 19790:2006 and ISO/IEC 24759:2008. The second revision of ISO/IEC 19790 was published on August 15, 2012. The second revision of ISO/IEC 24759 was published on January 31, 2014 and the third revision was published March 2017. Both ISO/IEC standards are available through the American National Standards Institute (ANSI) (see: http://webstore.ansi.org/RecordDetail.aspx?sku=ISO%2FIEC+19790%3A2012). The two ISO revisions were developed with international support and the collaboration of governments, industry and academia.

The revision of ISO/IEC 19790:2012 addresses new security areas, such as defined software module boundaries, degraded modes of operation, trusted channels, two-factor authentication, software security, mitigation of fault induction and side-channel attacks, operational self-tests for algorithms, and lifecycle assurance from design to end-of-life.

In addition to the aforementioned standards, International Standards ISO/IEC 17825, Testing methods for the mitigation of non-invasive attack classes against cryptographic modules, was published on January 15, 2016 and ISO/IEC 18367, Cryptographic algorithms and security mechanisms conformance testing, was published on December 15, 2016. Mr. Easter was the editor of both standards.

International Standard ISO/IEC 17825 specifies the non-invasive attack mitigation test metrics for determining conformance to the requirements specified in ISO/IEC 19790 for Security Levels 3 and 4. The test metrics are associated with the security functions specified in ISO/IEC 19790. Testing will be conducted at the defined boundary of the cryptographic module and using Input/Output (I/O) available at the defined boundary.

---

ion
19790:2012
|                   |                           |         | First Edition            |             |         |                       |     | 24759:2014  |                |     | (Published 05-15-2015)  |                      |       |     |     |
| ----------------- | ------------------------- | ------- | ------------------------ | ----------- | ------- | --------------------- | --- | ----------- | -------------- | --- | ----------------------- | -------------------- | ----- | --- | --- |
|                   |                           | ( P u b | l i s h e d   0 1 -1 5 - | 2 0 1 6 )   | S e c o | n d   E d i t i o n   |     |             |                |     | P h y s                 | i c a l  S e c u r i | t y   |     |     |
| T e s t t o o l   | r e q u i r e m e n t s   |         |                          |             |         |                       |     | T h i r     | d   E d i t io | n   |                         |                      |       |     |     |
a n d   t e s t t o o l   c a l i b r a t i o n   T e s t i n g   m e t h o d s   f o r   t h e   ( P u b l i s h e d   0 8 - 1 5 - 2 0 1 2 )   A t t a c k s ,   M it i g a t i o n
|                   |                                    | m   | i t i g a t i o n   o f   n | o n ­ |                 |                               |     | ( P u bl i s h | e d   0 3 - 0 1 - 2 | 0 1 7 )  | T e c | h n i q u e s   a n d |     |     |     |
| ----------------- | ---------------------------------- | --- | --------------------------- | ----- | --------------- | ----------------------------- | --- | -------------- | ------------------- | -------- | ----- | --------------------- | --- | --- | --- |
| m e t h o d s   f | o r   u s e   i n   t e s t i n g  |     |                             |       | ( C o r r e c t | e d   1 2 - 1 5 - 2 0 1 5 )   |     | T e s t   r e  | q u ir e m e        | n t s    |       |                       |     |     |     |
n o n - i n v a s i v e   a t t a c k   i n v a s i v e   a t t a c k   c l a s s e s   S e c u ri t y   Se c u r i ty   R e q u i r e m e n t s
|                         |     | against cryptographic  |          |     |                   |     |     |                | for  |     |     |     |     |     |     |
| ----------------------- | --- | ---------------------- | -------- | --- | ----------------- | --- | --- | -------------- | ---- | --- | --- | --- | --- | --- | --- |
| mitigation techniques   | in  |                        |          |     | requirements for  |     |     |                |      |     |     |     |     |     |     |
| cryptographic modules - |     |                        | modules  |     |                   |     |     | cryptographic  |      |     |     |     |     |     |     |
cryptographic
| Part 1: Test tools and  |     |     |     |     | modules  |     |     | modules  |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
techniques
| Testtool      | requirements  | 18367:2016  |                |     |     |     |     |     |     |     |                     |               |     |                      |             |
| ------------- | ------------- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ------------- | --- | -------------------- | ----------- |
|               |               |             |                |     |     |     |     |     |     |     | TS 20540            |               |     | 20543                |             |
| and testtool  | calibration   |             | First Edition  |     |     |     |     |     |     |     |                     |               |     |                      |             |
|               |               |             |                |     |     |     |     |     |     |     | U n d e r d e v e l | o p m e n t   | U   | n d e r  d e v e l o | p m e n t   |
methods for use in testing  (Published 12-15-2016)  Competence  G ui d e li n e s   f o r   Te s t i ng  T e s t  a n d   a n a l ys i s
| n o n - i n v | a s i v e   a t t a c k   |     | C r y p t o g ra p h i | c   | C o m | p e t e n c e   |     |                  |                 |     |                       |                  |     |                       |               |
| ------------- | ------------------------- | --- | ---------------------- | --- | ----- | --------------- | --- | ---------------- | --------------- | --- | --------------------- | ---------------- | --- | --------------------- | ------------- |
|               |                           |     |                        |     |       |                 |     | r e q u i re m e | n t s   f o r   | Cr  | y p t o g r a p h i c |   M o d u l e s  | m   | e t h o d s   f o r   | r a n d o m   |
m i t i g a t i o n   t e c h n i q u e s   i n  al g o r i t h m s   a n d   s e c u r it y  r e q u i r e m e n t s   f o r   i n  t h e i r   O p e ra t i o n a l
c r y p t o g r a p h i c   m o d u l e s   - m e c h a n i s m s   i n f o r m a t i o n   s e c u r i t y   i n f o r m a t i o n   s e c u r i t y   b it   g e n e r a t o r s   w it h i n
|                  |                                |       |                         |          |                    |                           | te  | s t e r s   a n d   | e v a l u a t o r s   |     | E n v i r o n | m e n t   | 1   | S 0 / I E C   1 9 7 9 | 0   a n d   |
| ---------------- | ------------------------------ | ----- | ----------------------- | -------- | ------------------ | ------------------------- | --- | ------------------- | --------------------- | --- | ------------- | --------- | --- | --------------------- | ----------- |
| P a r t :   2  T | e s t   c a li b r a t i o n   | c o n | f o r m a n c e   t e s | t i ng   | te s t e r s   a n | d   e v a l u a t o r s   |     |                     |                       |     |               |           |     |                       |             |
methods and apparatus  - Part 1: Introduction,  - Part 2: Knowledge,  1S0/IEC 15408
skills and effectiveness
concepts and general
|     |     |     |     |     | requirements  |     |     | requirements  | for  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- |
1S0/IEC 19790 testers
Figure 2: Cryptographic Module Testing – ISO Standards
15
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

International Standard ISO/IEC 18367 describes INCITS 499-2013, was published in FY 2013
conformance testing methods for cryptographic and is currently under revision.
algorithms and security mechanisms. Conformance
• Next Generation Access Control – Generic
testing assures that an implementation of a
Operations & Abstract Data Structures
cryptographic algorithm or security mechanism is
(NGAC-GOADS). Serban Gavrila, ITL, is the
correct whether implemented in hardware, software
editor. The project is assigned project number
or frmware. It also confrms that it runs correctly
2195-D, and the document was published
in a specifc operating environment. Testing may
during FY 2016.
consist of known-answer or Monte Carlo testing,
or a combination of test methods. Testing may be
• Next Generation Access Control –
performed on the actual implementation or modeled
Implementation Requirements, Protocols
in a simulation environment.
and API Defnitions (NGAC-IRPADS). Project
number 2193-D has been assigned. This part
The test methods used by testing laboratories to
will be published in FY 2018.
test whether the cryptographic module conforms to
the requirements specifed in ISO/IEC 19790 and the
CONTACTS:
test metrics specifed in this International Standard
Mr. David Ferraiolo Mr. Serban Gavrila
for each of the associated security functions specifed
(301) 975-3046 (301) 975-4343
in ISO/IEC 19790 are specifed in ISO/IEC 24759. The
david.ferraiolo@nist.gov serban.gavrila@nist.gov
test approach employed in this International Standard
is an efcient “push-button” approach: the tests are
technically sound, repeatable and have moderate Identity Management Devices and
costs.
Standards
FOR MORE INFORMATION, SEE:
In the area of Identity Tokens and Secure
https://csrc.nist.gov/Projects/Cryptographic-Mod-
elements, ITL has provided the technical and editorial
ule-Validation-Program
support of Mr. Ketan Mehta (CSD) in the development
and amendment of American National Standard
CONTACT:
(ANS) 504, Generic Identity Command Set (GICS).
Mr. Randall J. Easter
GICS enables Personal Identity Verifcation (PIV),
(240) 361-8777
PIV-Interoperable (PIV-I) and Common Access Card
randall.easter@nist.gov
(CAC) applications, and others, to be built from a
single platform. GICS defnes an open platform where
Next Generation Access Control identity applications can be instantiated, deployed,
and used in an interoperable way between the
Standards
credential issuers and credential users that aligns with
the last revision of the NIST SP 800-73-4, Interfaces
ITL has continued the development of an advanced
for Personal Identity Verifcation, (PIV) specifcations.
Attribute Based Access Control (ABAC) framework
called the Policy Machine, which was designed to be
During FY 2017, the ITL staf:
in alignment with an emerging ANSI/INCITS standard
under the title of “Next Generation Access Control” • Contributed to the publication of several
(NGAC). revisions of the ISO/IEC 7816 family of
standards (Identifcation cards - Integrated
The NIST Policy Machine research and
circuit cards), which are all relevant to FIPS
development efort has resulted in three ongoing
201, Personal Identity Verifcation (PIV)
national standards projects in CS1 that are in the early
of Federal Employees and Contractors,
stages of development. They include:
specifcations;
• Next Generation Access Control – Functional
16
Architecture (NGAC-FA). Project number
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

• Pursued the standardization and 18013) for an International Mobile Driver License (DL).
harmonization of identity standards that were ITL gathered and discussed functional and security
developed in the U.S.; requirements for Mobile DLs, and is now developing
two models: ofine and online. Once these models are
• Developed requirements and identifed
fully defned, ITL plans to write technical specifcations
standards gaps for Mobile Driving Licenses;
for each model.
• Actively participated in the development of a
CONTACTS:
standards for Mobile Driving Licenses;
Mr. Salvatore Francomacaro Mr. Ketan Mehta
• Enhanced the Machine-Readable Travel (301) 975-6414 (301) 975-8405
Documents (ePassport) data model to salvatore.francomacaro@nist.gov ketan.mehta@nist.gov
address privacy and security concerns; and
• Contributed to the development of a standard Identity Management International
for privacy-enhanced security protocols for
Standardization with ISO/IEC SC27
secure elements.
During FY 2017, NIST ACD’s Trusted Identities
The ITL staf will continue to actively support
Group (TIG) collaborated with representatives from
relevant ID management standard initiatives, such as
the United Kingdom (U.K.) Cabinet Ofce and the
ISO/IEC 19286, Integrated circuit card (ICC) Privacy-
Canadian Treasury Board to identify commonalities
enhancing protocols and services, and ISO/IEC 18328,
and work to align the digital identity standards and
ICC managed devices.
requirements among the respective national digital
Web Authentication/FIDO: ITL participates in the identity programs, particularly SP 800-63-3 for
development of online authentication specifcations. the U.S. and the U.K. Good Practice Guides (GPG).
These specifcations are developed by the Fast The goal in these eforts is to promote a vibrant
Identities Online (FIDO) alliance, which is a consortium market of internationally viable identity services and
of private organizations. ITL also participates in advance the secure exchange of digital identities
the development of similar specifcations (called while protecting the privacy of the subjects of those
WebAuthn) for web browsers that are being developed identities for cross-border transactions and mutual
by the World Wide Web Consortium (W3C). Both the recognition. While primarily focused on developing a
FIDO and WebAuthn specifcations enable relying framework that would facilitate the establishment of
parties to create cryptographic tokens on the end- a common set of requirements and standards across
user’s device and subsequently use this cryptographic the three national programs, there was increasing
token to authenticate the end user. These specifcations interest from other national programs and industry
provide multi-factor authentication directives, and in the work products and methodologies developed
they are designed to mitigate common threat vectors by this collaborative work. As a result, the group
for Internet communications, such as phishing, man- provided this work to the international community as
in-the-middle, and replay attacks. a series of aligned joint contributions for international
standardization.
ePassport: ITL participates in the development
of an ISO/IEC standard (ISO/IEC 7501) for electronic The TIG contributions, in collaboration with their
Passports. Specifcally, ITL is contributing to the British and Canadian partners, were focused on
development of passport data structure and its access establishing a synchronized core set of international
control. ITL reviews and comments on authentication identity management standards within the scope of
protocols that are developed to ensure strong user the activities of ISO/IEC JTC 1/SC 27/WG 5, which
authentication and to protect personally identifable oversees the development of international standards
passport data. for identity management and privacy. The team
provided contributions to synchronize and align the
Mobile Driver License: ITL is also participating
following ISO/IEC standards with the U.K., Canadian,
17 in the development of an ISO standard (ISO/IEC
and U.S. harmonization work:
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

•   ISO/IEC 29115 Information Technology —  blockchain technologies and architectures. NIST has
Security techniques — Entity authentication  been participating in these activities via the national
assurance framework – a major revision is  mirror committee within the InterNational Committee
required to align with SP 800-63 B and GPG  for Information Technology Standards (INCITS). ISO/
| 44;  |     |     |     | TC 307 will meet in November 2017, where the reports  |     |     |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
on these topics will be reviewed and new work will be
•   ISO/IEC 29003 Information technology —
established.
Security techniques — Identity proofng;
CONTACTS:
•   ISO 31000 Risk management framework
|     |     |     |     | Mr. Dylan Yaga        |                Dr. Lily Chen  |     |     |
| --- | --- | --- | --- | --------------------- | ----------------------------- | --- | --- |
applied to identity-related risk, a new work
|     |     |     |     | (301)-975-6004  |     |  (301) 975-6974  |     |
| --- | --- | --- | --- | --------------- | --- | ---------------- | --- |
project for a new international standard that
|     |     |     |     | dylan.yaga@nist.gov    |     |   lily.chen@nist.gov  |     |
| --- | --- | --- | --- | ---------------------- | --- | --------------------- | --- |
will be aligned with the risk management
section of NIST SP 800-63-3;
Internet of Things (IoT)
•   Identity related standards landscape, a new
work project to establish a clear and aligned
|     |     |     |     | NIST/ITL  | has  contributed  | to  | standardization  |
| --- | --- | --- | --- | --------- | ----------------- | --- | ---------------- |
landscape for ISO/IEC identity standards and  activities  for  the  IoT  architecture  and  vocabulary
administrative processes and to establish rules
during FY 2017 in three primary areas:
for how the development and maintenance
of an aligned set of identity management  •   The Industrial Internet Consortium (IIC);
standards could be coordinated and managed
•   ISO/IEC SC41, Internet of Things and related
within ISO/IEC WG5; and
technologies; and
•   Identity assurance framework, a new work
•   IEEE P2413, Standard for an Architectural
project for a new international standard that
Framework for the Internet of Things (IoT).
will be aligned with the identity assurance
components of SP 800-63A and the U.K. GPG  Focus was on the architecture, vocabulary, and
| 45.  |     |     |     | recently, edge computing. In addition to working on  |     |     |     |
| ---- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
standards related to these areas, NIST staf member
CONTACT:
|     |     |     |     | Eric  Simmon  | is  the  chair  | of  the  | IIC  commenting  |
| --- | --- | --- | --- | ------------- | --------------- | -------- | ---------------- |
Mr. David Temoshok
working group for reviewing the IEEE p2413 draft
(202) 482-5475
standard and is the liaison between ISO/IEC SC41-
david.temoshok@nist.gov
ISO/IEC SC38 (cloud computing).
The NIST staf has also participated to the activities
Blockchains
in ISO/IEC SC27 relative to IoT Security. This activity
During FY 2017, NIST participated in standards  will be further developed during FY 2018.
| activities  | exploring  | blockchain  | technologies,  |     |     |     |     |
| ----------- | ---------- | ----------- | -------------- | --- | --- | --- | --- |
CONTACTS:
| architectures,  | and                | use  cases.  | These  included  |                       |     |                          |     |
| --------------- | ------------------ | ------------ | ---------------- | --------------------- | --- | ------------------------ | --- |
|                 |                    |              |                  | Mr. Eric Simmon       |     | Ms. Katerina Megas       |     |
| participation   | in  a  new         | blockchain   | study  group     |                       |     |                          |     |
|                 |                    |              |                  | (301) 975-3956        |     | (202) 441-1147           |     |
| sponsored       | by  the  American  | Standards    | Committee        |                       |     |                          |     |
|                 |                    |              |                  | eric.simmon@nist.gov  |     | katerina.megas@nist.gov  |     |
X9, the fnancial services committee of the American
National Standards Institute (ANSI), and continued
| work  in  | the  International  | Standards  | Organization  |     |     |     |     |
| --------- | ------------------- | ---------- | ------------- | --- | --- | --- | --- |
Cloud Computing Standards
| (ISO)  Technical  | Committee  | (TC)  | for  Blockchains  |     |     |     |     |
| ----------------- | ---------- | ----- | ----------------- | --- | --- | --- | --- |
Developed Within ISO/IEC JTC 1
and Distributed Ledger Technologies (ISO/TC 307).
Established in 2016, the initial objectives of ISO/TC 307
ITL is actively engaged with several key players
include defning key terms and concepts, exploring
|     |     |     |     | in  the  Federal  | Government  | which  | look  broadly  at  |
| --- | --- | --- | --- | ----------------- | ----------- | ------ | ------------------ |
reference architectures, investigating use cases, and
questions of IT standards, how to infuence them, and  18
identifying identity and privacy implications within
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

|     |     |     |     |     |     |     |     | of  ISO/IEC  | 19941,  Information  |     | technology–Cloud  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------------- | --- | ----------------- | --- |
how to use them. These participants include the Ofce
of Management and Budget (OMB) E-Gov Ofce and  computing–Interoperability  and  portability,  which
Ofce  of  Information  and  Regulatory  Afairs,  the  is  expected  to  be  published  by  the  end  of  2017.
federal Chief Information Ofcers (CIO) Council, the  The document is intended to establish a common
Interagency Council on Standards Policy (ICSP), and  understanding  of  cloud  computing  interoperability
the General Services Administration (GSA) Ofce of  and portability. Both interoperability and portability
Government-wide  Policy.  Our  goal  in  chairing  the  ofer  more  choices  to  cloud  users  by  limiting  the
Standards Working Group is to solicit requirements  efects of being locked-in to any cloud service or cloud
from federal agencies, fnd the appropriate voluntary  service provider. ISO/IEC 19941 joins many published
standards  committee  that  is  addressing  these  cloud computing standards that were developed from
NIST publications, such as:
requirements and encourage participation to ensure
the government requirements are being adequately
•   ISO/IEC 17788, Information technology --
| met.  Where  |     | standards  |     | are  needed,  |     | ITL  | works  |     |     |     |     |     |
| ------------ | --- | ---------- | --- | ------------- | --- | ---- | ------ | --- | --- | --- | --- | --- |
Cloud computing -- Overview and vocabulary;
| closely         | with  | U.S.  industry,  |             | standards  |            | development  |      |     |     |     |     |     |
| --------------- | ----- | ---------------- | ----------- | ---------- | ---------- | ------------ | ---- | --- | --- | --- | --- | --- |
| organizations,  |       | other            | government  |            | agencies,  |              | and  |     |     |     |     |     |
•   ISO/IEC 17789, Information technology --
leaders in the global standards community to develop
Cloud computing -- Reference architecture;
standards that will support secure cloud computing.
and,
ITL participation helps to ensure the alignment
•   ISO/IEC 19086, Information technology --
of NIST standards with those of ISO/IEC JTC 1 sub-
Cloud computing -- Service level agreement
committees, such as SC 27 IT Security techniques,  (SLA) framework.
SC 38 Cloud Computing and Distributed Platforms,
| and  their  | U.S.  | counterparts,  |     | ANSI/  | INCITS  |     | Cyber  | CONTACT:  |     |     |     |     |
| ----------- | ----- | -------------- | --- | ------ | ------- | --- | ------ | --------- | --- | --- | --- | --- |
Security 1 (CS 1) and Cloud 38. The large number of  Ms. Annie Sokol
standards being developed in SC 27 covering areas
(301) 975-2006
such as security, cryptography, privacy, supply chain,
annie.sokol@nist.gov
| personally  | identifable  |     | information  |     | (PII)  | processing  |     |     |     |     |     |     |
| ----------- | ------------ | --- | ------------ | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- |
or virtualization security, harmonize with many cloud
| computing  | standards  |     | being  | developed  |     | by  | these  |     |     |     |     |     |
| ---------- | ---------- | --- | ------ | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- |
RISK MANAGEMENT
subcommittees.
The focus of implementing cloud computing is
even more critical since the White House released  Framework for Improving Critical
an IT Modernization Report in September 2017 that  Infrastructure Cybersecurity
| includes  | recommendations  |     |     | for  | agencies  | to  | take  |     |     |     |     |     |
| --------- | ---------------- | --- | --- | ---- | --------- | --- | ----- | --- | --- | --- | --- | --- |
(Cybersecurity Framework)
steps to secure and modernize federal IT networks.
| Those  | steps  | for  | modernizing  |     | and  | consolidating  |     |              |       |                |     |                |
| ------ | ------ | ---- | ------------ | --- | ---- | -------------- | --- | ------------ | ----- | -------------- | --- | -------------- |
|        |        |      |              |     |      |                |     | Recognizing  | that  | the  national  |     | and  economic  |
networks point to cloud computing, modernization of
security of the United States depends on the reliable
government-hosted applications, and better security
functioning of its critical infrastructure, the President
| for  legacy  | systems.  |     | Federal  | modernization  |     |     | eforts,  |     |     |     |     |     |
| ------------ | --------- | --- | -------- | -------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
issued Executive Order (EO) 13636: Improving Critical
| such  as  | those  | connected  |     | with  | the  | Modernizing  |     |     |     |     |     |     |
| --------- | ------ | ---------- | --- | ----- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
Infrastructure Cybersecurity, in February of 2013. This
| Government  |     | Technology  |     | Act,  may  | further  |     | enable  |     |     |     |     |     |
| ----------- | --- | ----------- | --- | ---------- | -------- | --- | ------- | --- | --- | --- | --- | --- |
EO directed NIST to work with stakeholders to develop
agencies to accelerate investments in cloud and other
a voluntary framework – based on existing standards,
new technologies.
guidelines, and practices − for reducing cybersecurity
risks to critical infrastructures.
| Ms.  | Annie  | Sokol  | is  | a  member  | of  | ITL’s  | Cloud  |     |     |     |     |     |
| ---- | ------ | ------ | --- | ---------- | --- | ------ | ------ | --- | --- | --- | --- | --- |
Computing team and is the CSD representative in
|                 |     |              |     |           |     |                |     | The  | Cybersecurity  | Framework  |     | that  was  |
| --------------- | --- | ------------ | --- | --------- | --- | -------------- | --- | ---- | -------------- | ---------- | --- | ---------- |
| the  standards  |     | development  |     | program.  |     | ITL  provides  |     |      |                |            |     |            |
developed provides a prioritized, fexible, repeatable,
| technical  | and  | editorial  |     | representation  |     |     | in  the  |     |     |     |     |     |
| ---------- | ---- | ---------- | --- | --------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
performance-based, and cost-efective approach to
development of national and international standards
| 19  |     |     |     |     |     |     |     | help critical infrastructure owners and operators—as  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
in both SC 27 and SC 38. Ms. Sokol is the co-editor
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

well as other interested entities—identify, assess, and the Framework;
manage cybersecurity-related risk while protecting
• Consulting with international organizations
business confdentiality, individual privacy, and civil
and standards bodies to demonstrate and
liberties.
ensure continued alignment with voluntary
In FY 2017, NIST continued to work with a diverse international standards; and
stakeholder community to support the use and
• Working with both industry and regulatory
understanding of the Cybersecurity Framework. This
organizations to apply the Framework in
process included:
ways that bring efciencies to the regulatory
• Publication of a draft Framework 1.1 to clarify, process.
refne, and enhance the Cybersecurity
Since the release of the Framework, NIST’s primary
Framework, drawing upon comments received
goal has been to raise awareness of the Framework
from a public review process launched in
and encourage its use as a tool to help industry
January 2017;
sectors and organizations manage cybersecurity risks.
• Conducting a public workshop at NIST in NIST has strengthened its collaboration with critical
Gaithersburg, MD to gather input about the infrastructure owners and operators, industry leaders,
current use of the Framework and feedback government partners, and other stakeholders—
regarding the initial public draft; building on previous years’ interactions that were
crucial to the Framework’s development.
• Releasing the 1.0 version of the Baldrige
Cybersecurity Excellence Builder, a self- In May 2017, Executive Order 13800 was released,
assessment tool to help organizations directing federal agency heads to use the Framework
better understand the efectiveness of their to manage agencies’ cybersecurity risk. NIST released
cybersecurity risk-management eforts; draft NISTIR 8170, The Cybersecurity Framework:
Implementation Guidance for Federal Agencies, to
• Updates to the Framework website with a
provide information on how Federal agencies can use
catalog of industry resources, upcoming NIST
the Cybersecurity Framework—and in particular, how
speaking events, and an extensive frequently-
the Risk Management Framework and Cybersecurity
asked-question knowledge base;
Framework work together to help agencies
develop, implement, and continuously improve their
• Provision of outreach for small- and medium-
information security programs.
sized businesses (SMBs), including guidance
provided by the Applied Cybersecurity
In FY 2018, NIST will continue to conduct
Division (ACD) in NIST Interagency Report
stakeholder outreach and will work collaboratively
(NISTIR) 7621 Rev. 1, Small Business
to further understand stakeholder needs regarding
Information Security: The Fundamentals;
tools and resources to enable more efective use
of the Framework. Version 1.1 of the Framework is
• Coordinating with critical infrastructure
expected to be published, and NIST will continue to
owners and operators, regulators, and other
identify ways for the Framework to contribute to risk
industry organizations through a variety of
management initiatives.
meetings and industry events to ensure the
understanding and use of the Framework;
FOR MORE INFORMATION, SEE:
• Analyzing various industry work products https://www.nist.gov/cyberframework
(such as mapping documents) for Framework
CONTACTS:
correctness;
Mr. Matt Barrett Mr. Jef Marron
• Consulting with state and local governments, (301) 975-6259 (301) 975-3846
and the governments of other nations matthew.barrett@nist.gov jefrey.marron@nist.gov
regarding their alignment with both the 20
principles and the cybersecurity outcomes of
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

Federal Information Security • System Security Engineering Initiative:
The fnal version of Special Publication (SP)
Management Act (FISMA)
800-160, Systems Security Engineering:
Implementation Project
Considerations for a Multidisciplinary
Approach in the Engineering of Trustworthy
The FISMA Implementation Project focuses on:
Secure Systems, was published to address
the engineering-driven actions necessary
• Developing a comprehensive series of
to develop more defensible and survivable
standards and guidelines to help federal
systems—including the components that
and nonfederal organizations build efective
compose and the services that depend on
information security programs, defend against
those systems. To ensure that the publication
increasingly sophisticated cyber-attacks,
provides the utmost clarity and focus for
and demonstrate compliance to security
our customers, several of the supporting
requirements set forth in legislation, Executive
appendices from the second public draft are
Orders, Homeland Security Directives, and
being recast into their own publications. SP
OMB policies; and
800-160 is the fagship publication for the
• Conducting outreach to public and NIST Systems Security Engineering Initiative.
private-sector organizations to facilitate NIST publications specifcally addressing
the application of the suite of standards several key systems security engineering
and guidelines that support the NIST Risk considerations (i.e., resilience, software
Management Framework (RMF) (see https:// assurance, and hardware assurance) will be
csrc.nist.gov/Projects/Risk-Management). developed and published, beginning in 2018.
Additionally, the interaction of the NIST RMF
During FY 2017, the ITL FISMA Implementation
with the life cycle processes in SP 800-160,
project continued to strengthen collaboration through
will be described in future updates to existing
the Joint Task Force (JTF) Transformation Initiative,
RMF standards and guidelines.
which includes the Department of Defense (DoD),
the Intelligence Community (IC), the Committee on • Risk Management Guidelines: Work
National Security Systems (CNSS), and various federal continued on SP 800-53 Revision 5, Security
agencies. The JTF partners continue to develop and and Privacy Controls for Information Systems
update key cybersecurity guidelines for protecting and Organizations. The initial public draft
federal information and information systems as was published after collaboration with a
part of the Unifed Information Security Framework. federal interagency working group, the OMB,
Previously, the JTF developed common security NIST, other agency privacy professionals,
guidance in the critical areas of security controls and our JTF partners. SP 800-53 provides
for information systems and organizations, security organizations with the security and privacy
assessment procedures to demonstrate security controls necessary to appropriately strengthen
control efectiveness, security authorizations for risk their systems and the environments in
acceptance decisions, and continuous monitoring which those systems operate, and provides
activities to ensure that decision makers receive the a process for selecting the appropriate
most up-to-date information on the security state of controls, which contributes to systems that
their information systems. In addition, ITL continued are resilient in the face of attacks and other
to work with the Department of Homeland Security threats and protect an individual’s privacy.
(DHS) to develop guidelines for automation support The FISMA Team, in conjunction with the
for security control assessments on a security same group of collaborators, also published
capability basis and in accordance with the NIST RMF a discussion draft of SP 800-37 Revision 2,
as well as on developing guidance and a security Risk Management Framework for Information
controls overlay to protect federal high value assets. Systems and Organizations. SP 800-37
Revision 2 provides a closer link between risk
21 In FY 2017, the ITL FISMA Team worked on the
following initiatives:
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

management processes and activities at the 1. SP 800-30, Guide for Conducting Risk
executive level of the organization, with risk Assessments;
management activities at the system and
2. SP 800-37, Guide for Applying the Risk
operational level; institutionalizes enterprise-
Management Framework to Federal
wide risk management preparatory activities
Information Systems: a Security Life Cycle
to facilitate a more efcient and cost-
Approach;
efective execution of the Risk Management
Framework at the system and operational
3. SP 800-39, Managing Information
level; demonstrates how the Cybersecurity
Security Risk: Organization, Mission, and
Framework can be implemented using the
Information System View;
established Risk Management Framework
processes; and integrates privacy concepts 4. SP 800-53, Security and Privacy Controls
into the Risk Management Framework. The for Federal Information Systems and
implementation of SP 800-53, SP 800-37, and Organizations; and
SP 800-137, Information Security Continuous
5. SP 800-53A, Assessing Security and
Monitoring for Federal Information Systems
Privacy Controls in Federal Information
and Organizations, provides organizations
Systems and Organizations: Building
with near real-time information that is
Efective Assessment Plans.
essential for senior leaders making ongoing
risk-based decisions afecting their critical
The FISMA Team also collaborated with DoD,
missions and business functions.
the IC, DHS, the National Archives and Records
Administration (NARA), the Federal Emergency
• FISMA Outreach Activity to Public and
Management Agency (FEMA), the Government
Private-Sector Organizations: Cybersecurity
Accountability Ofce (GAO), the OMB, the General
outreach briefngs were conducted and
Services Administration (GSA), the Small Business
support was provided to all levels of private-
Administration (SBA), and the Inspectors General
sector organizations and government
(IGs) on multiple projects to ensure consistency with
(including federal, state and local entities) on
FISMA-related guidance and to protect information in
multiple information security topics of interest.
a way that is commensurate with risk. In addition, the
These included, for example, an efective
FISMA Team served as co-chairs on the CNSS working
implementation of the NIST RMF, contingency
groups.
planning, interconnection security
agreements, security-focused confguration
In FY 2017, the FISMA Team completed the
management, and information security for
following activities:
small businesses. In addition, the ITL FISMA
Team responded to hundreds of inquiries from • Published the fnal version of SP 800-160,
customers, served on cybersecurity advisory Systems Security Engineering: Considerations
panels, conducted outreach activities with for a Multidisciplinary Approach in the
academic institutions, provided information on Engineering of Trustworthy Secure Systems;
NIST’s security standards and guidelines, and
• Published the initial public draft of SP 800-53
explored new areas of cybersecurity research
Revision 5, Security and Privacy Controls for
and development.
Systems and Organizations;
• Collaboration with JTF partners and
• Published the discussion draft of SP 800-37
other federal organizations: The FISMA
Revision 2, Risk Management Framework for
Team worked closely with JTF partners to
Federal Information Systems: A System Life
ensure that the fve JTF publications remain
Cycle Approach for Security and Privacy;
current, and to designate additional Special
Publications as JTF guidance. The fve JTF
• Published the fnal version of SP 800-171
publications are: 22
Revision 1, Protecting Controlled Unclassifed
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

Information in Nonfederal Information Systems A System Life Cycle Approach for Security and
and Organizations, to provide guidance Privacy;
to federal agencies for the protection of
• Complete the development of and
Controlled Unclassifed Information when such
operationalize the web application for the
information is resident in nonfederal systems
automated support of SP 800-53 updates and
and organizations;
the public comment process;
• Published fnal versions of NIST Interagency
• Continue the collaboration with DHS to
Report (NISTIR) 8011, Automation Support for
develop and publish additional NISTIR 8011
Ongoing Assessments, Volume 1 - Overview,
volumes;
and Volume 2 - Hardware Asset Management,
and adjudicated public comments in
• Finalize and publish the initial public draft
partnership with DHS;
of SP 800-60 Revision 2, Guide for Mapping
Types of Information and Information Systems
• Published the fnal version of An Introduction
to Security Categories, in partnership with
to Information Security;
NARA and OMB;
• Continued the development of a web
• Publish the initial public draft and fnal version
application to automate the process for
of SP 800-53A, Assessing Security and
updating SP 800-53 in order to keep it as
Privacy Controls in Information Systems and
current and relevant as possible;
Organizations;
• Continued the development of SP 800-
• Publish the initial public draft and fnal version
60, Revision 2, Guide for Mapping Types
of SP 800-171A, Assessing Security Controls in
of Information and Information Systems to
Nonfederal Systems;
Security Categories, in partnership with the
National Archives and Records Administration
• Continue the development of SP 800-18
(NARA);
Revision 2, Guide for Developing System
Security and Privacy Plans;
• Continued the development of the initial
public draft of SP 800-18 Revision 2, Guide for
• Finalize and publish SP 800-47 Revision
Developing System Security and Privacy Plans;
1, Information Exchange and System
and
Connections;
• Continued the development of the
• Update the RMF online course to Hypertext
initial public draft of SP 800-47 Revision
Markup Language version 5 (HTML5) and
1, Information Exchange and System
verify consistency with SP 800-37 Revision 2;
Connections.
• Expand cybersecurity outreach to include
In FY 2018, the FISMA Team intends to:
additional state, local, and tribal governments,
as well as private-sector organizations and
• Continue work on SP 800-160 companion
academic institutions;
publications;
• Continue to support federal agencies in the
• Finalize and publish the fnal version of SP
efective implementation of the RMF; and
800-53 Revision 5, Security and Privacy
Controls for Information Systems and
• Continue the collaboration with JTF partners
Organizations;
and other federal organizations.
• Finalize and publish the fnal version of
SP 800-37 Revision 2, Risk Management
FOR MORE INFORMATION, SEE:
Framework for Federal Information Systems:
23 https://csrc.nist.gov/projects/risk-management
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

CONTACTS:  by  the  OMB’s  July  2016  update  to  Circular
|     |     |     |     |     | A-130,  |     | which  | emphasized  |     | federal  | agencies’  |     |
| --- | --- | --- | --- | --- | ------- | --- | ------ | ----------- | --- | -------- | ---------- | --- |
The ITL FISMA Team email is: sec-cert@nist.gov
|     |     |     |     |     | responsibilities  |     | to  | manage  |     | privacy  | risk,  | not  just  |
| --- | --- | --- | --- | --- | ----------------- | --- | --- | ------- | --- | -------- | ------ | ---------- |
Dr. Ron Ross  Ms. Victoria Pillitteri  compliance risk, and now requires them to apply the
NIST Risk Management Framework to their privacy
| (301) 975-5390  |     | (301) 975-8542  |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
programs.
| ron.ross@nist.gov  |     | victoria.pillitteri@nist.gov  |     |     |              |     |     |          |              |     |      |       |
| ------------------ | --- | ----------------------------- | --- | --- | ------------ | --- | --- | -------- | ------------ | --- | ---- | ----- |
|                    |     |                               |     |     | Advancement  |     | of  | Privacy  | Engineering  |     | and  | Risk  |
| Mr. Nedim Goren    |     | Ms. Jody Jacobs               |     |     |              |     |     |          |              |     |      |       |
Management
| (301) 975-5233        |     | (301) 975-4728        |     |     |     |              |        |     |           |          |     |        |
| --------------------- | --- | --------------------- | --- | --- | --- | ------------ | ------ | --- | --------- | -------- | --- | ------ |
| nedim.goren@nist.gov  |     | jody.jacobs@nist.gov  |     |     |     |              |        |     |           |          |     |        |
|                       |     |                       |     |     |     | In  January  | 2017,  |     | the  PEP  | reached  | a   | major  |
milestone in advancing the development of privacy
Ms. Kelley Dempsey
engineering and risk management processes with the
(301) 975-2827
fnalization of NISTIR 8062, An Introduction to Privacy
kelley.dempsey@nist.gov  Engineering and Risk Management in Federal Systems
|     |     |     |     |     | (see  | https://doi.org/10.6028/NIST.IR.8062).  |     |     |     |     |     | NISTIR  |
| --- | --- | --- | --- | --- | ----- | --------------------------------------- | --- | --- | --- | --- | --- | ------- |
Editor’s Note: Ms. Peggy Himes worked on this
|     |     |     |     |     | 8062  | introduces  |     | the  concept  |     | of  applying  |     | systems  |
| --- | --- | --- | --- | --- | ----- | ----------- | --- | ------------- | --- | ------------- | --- | -------- |
project until her recent retirement.
|     |     |     |     |     | engineering  |     | practices  |     | to  privacy  | and  | provides  | a   |
| --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ------------ | ---- | --------- | --- |
new model for conducting privacy risk assessments
Privacy Engineering Program  on federal systems. It also presents the PEP’s initial
roadmap (See Figure 3) for guidance development to
The  NIST  Privacy  Engineering  Program  (PEP)  help agencies more efectively meet new obligations
supports the development of trustworthy information  under the revised Circular A-130.
systems by applying measurement science and system
|     |     |     |     |     |     | In  FY  | 2017,  | the  PEP  | team  | collaborated  |     | with  |
| --- | --- | --- | --- | --- | --- | ------- | ------ | --------- | ----- | ------------- | --- | ----- |
engineering principles to the creation of frameworks,
internal and external partners to successfully integrate
| risk  models,  | guidance,  | tools,  | and  standards  | that  |     |     |     |     |     |     |     |     |
| -------------- | ---------- | ------- | --------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
privacy requirements and considerations into SP 800-
protect privacy and, by extension, civil liberties.
63-3, Digital Identity Guidelines. The PEP team also
In  FY  2017,  the  PEP  focused  on  advancing  collaborated to integrate privacy into the draft revisions
the  development  of  privacy  engineering  and  risk  of  SPs  800-53,  Revision  5,  Security  and  Privacy
management  processes  and  the  deployment  Controls for Information Systems and Organizations,
of  privacy-enhancing  technologies  (as  well  as  and 800-37, Revision 2, Risk Management Framework
positioning  NIST  as  a  leader  in  privacy  research).  for Information Systems and Organizations, building
Many of the PEP’s eforts in FY 2017 were fueled  the foundation of making privacy and security equal
|     |     | SP 800-18       | SP 800-30    | SP 800-37     |     | SP 800-39      |     | SP 800-53      |     |     |     |     |
| --- | --- | --------------- | ------------ | ------------- | --- | -------------- | --- | -------------- | --- | --- | --- | --- |
|     |     |                 |              | Guide for     |     | Managing       |     | Security       |     |     |     |     |
|     |     | Guide for       |              | Applying the  |     |                |     |                |     |     |     |     |
|     |     |                 |              |               |     | Information    |     | and Privacy    |     |     |     |     |
|     |     | Developing      | Guide for    | Risk          |     | Security Risk- |     | Controls for   |     |     |     |     |
|     |     | Security Plans  | Conducting   | Management    |     |                |     |                |     |     |     |     |
|     |     |                 |              |               |     | Organization,  |     | Federal        |     |     |     |     |
|     |     | for Federal     | Risk         | Framework to  |     |                |     |                |     |     |     |     |
|     |     | Information     | Assessments  | Federal       |     | Mission, and   |     | Information    |     |     |     |     |
|     |     |                 |              |               |     | Information    |     | Systems and    |     |     |     |     |
|     |     | Systems         |              | Information   |     |                |     |                |     |     |     |     |
|     |     |                 |              | Systems       |     | System View    |     | Organizations  |     |     |     |     |
|     |     | SP 800-53A      | SP 800-60    | SP 800-63-3   |     | SP 800-122     |     | SP 800-160     |     |     |     |     |
Vol. I; Guide for
|     |     | Guide for           | Mappir,g Types              |                         |     | Guide to  |                        |          |              |     |     |     |
| --- | --- | ------------------- | --------------------------- | ----------------------- | --- | --------- | ---------------------- | -------- | ------------ | --- | --- | --- |
|     |     | Assessing the       | of Information and          |                         |     |           |                        |          |              |     |     |     |
|     |     |                     | In fo r m a t i o n  S y    | s t em s                |     | Pr o      | t e c tin g  t h e     |          |              |     |     |     |
|     |     | Security            | 1 0  S e cu r i t y  c a    | t e g or ie s  Digital  |     | C o       | n f id e n tia li ty   | Systems  |              |     |     |     |
|     |     | C o n tr o l s  in  | a n d   V o l.  I I :  A pp | e n d i c es  Identity  |     |           |                        | S e      | c u r it y   |     |     |     |
of Personally
|     |     | F e d e r a l   | lo   G u l de   f o r  M | a p p lr, g          |     |        |                      | E n | g in e e r ing  |     |     |     |
| --- | --- | --------------- | ------------------------ | -------------------- | --- | ------ | -------------------- | --- | --------------- | --- | --- | --- |
|     |     | Information     | T y p e s  o f   In fo r | m ation  Guidel;;;/  |     | I d e  | n t ifi a b le       |     |                 |     |     |     |
|     |     |                 | an d   I nf o r m a ti   | o n                  |     | I n fo | r m a t io n  (PII)  |     |                 |     |     |     |
|     |     | Systems         | Systems to Security      |                      |     |        |                      |     |                 |     |     |     |
categories
Figure 3: PEP guidance roadmap for integrating privacy risk management into NIST SPs, featuring
24
integrations underway during FY 2017 (highlighted in green).
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

quality attributes in trustworthy systems. The PEP NIST Leadership in Privacy
team also contributed privacy concepts to the Trusted
The PEP team built upon NIST’s leadership role
Identities Group (TIG) measurement science efort,
in privacy by serving in leadership positions and
draft NISTIR 8112, Attribute Metadata.
contributing to privacy expertise organizations across
The PEP team also contributed to ongoing the public and private sectors. These leadership
standards and framework development eforts in positions included: the chair of the Federal Privacy
the International Organization for Standardization Council’s Risk Management Task Force and co-chair of
(ISO), Institute of Electrical and Electronics Engineers the Networking and Information Technology Research
(IEEE), and the Fast Identity Online (FIDO) Alliance. and Development (NITRD) Program’s Privacy
Specifcally, the PEP team worked on ISO/IEC 27552, Research and Development (R&D) Interagency
which is a privacy-focused sector-specifc extension Working Group. The PEP team also participated in the
of the information security-focused ISO/IEC 27001, Internet Policy Task Force’s Privacy Working Group,
and ISO/IEC 27550, a technical report on privacy the FIDO Alliance’s Privacy and Public Policy Working
engineering. The PEP team also supported the Group, and the Identity Ecosystem Steering Group.
development of IEEE P7002, an efort in its early
stages that also addresses privacy engineering. The
Looking Forward
PEP team also engaged with FIDO to help develop
privacy-enhancing authentication specifcations. In FY 2018, the PEP team will continue developing
privacy risk management guidance for agencies,
Continuing the ongoing series of NIST workshops
including fnalizing SP 800-53 Revision 5, and SP
on privacy engineering and risk management,
800-37 Revision 2. The PEP team will also collaborate
building of the concepts introduced in NISTIR 8062,
with internal and external stakeholders to kick of
the PEP team hosted the June 2017 workshop,
the integration of privacy guidance into SP 800-53A
“Privacy Risk Assessment: A Prerequisite for Privacy
Revision 5, Assessing Security and Privacy Controls
Risk Management” (see https://www.nist.gov/news-
in Federal Information Systems and Organizations,
events/events/2017/06/privacy-risk-assessment-
and implement the provisions of other documents
prerequisite-privacy-risk-management). Feedback
laid out in the guidance roadmap. The PEP team will
received included the need for further integration of
continue supporting the development of international
privacy into risk management and security guidance,
standards focused on privacy engineering and risk
a privacy-specifc risk assessment model, and a toolset
management.
to manage privacy risk. These takeaways aligned well
with the PEP team’s ongoing eforts and goals for The PEP team will place a greater focus on
future work. its goal of advancing the deployment of privacy-
enhancing technologies. The PEP team has already
In support of a privacy-specifc risk assessment
begun exploring whether stakeholders see a need
tool, the PEP team continued socializing the use of
for an online space where collaborators can discuss,
its Privacy Risk Assessment Methodology (PRAM)
learn about, and improve upon tools, solutions, and
inside and outside the Federal Government. As of
processes that support privacy engineering and
FY 2017, more than 30 public- and private-sector
risk management. The PEP team will also explore
organizations have used or are using the PRAM,
the management of privacy risk in leading-edge
including participants in NIST’s trusted identities
domains, such as the internet of things (IoT) and
pilots and a few federal agencies.
artifcial intelligence (AI). Specifcally, the PEP team
The PEP team also collaborated on projects at the will collaborate with NIST’s Cybersecurity for the IoT
National Cybersecurity Center of Excellence (NCCoE), program to tackle IoT-specifc privacy challenges
including the Privacy-Enhancing Identity Federation through workshops and guidance.
building block, which demonstrates the use of the
The PEP team will continue to seek leadership
NIST privacy engineering objectives (see https://
opportunities in public- and private-sector organizations
nccoe.nist.gov/projects/building-blocks/privacy-
25 to strengthen NIST’s position as a leader in privacy.
enhanced-identity-brokers).
Finally, the PEP team will continue working with a
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

variety of organizations to manage privacy risk using Cyber Supply Chain Risk Management (C-SCRM)
the PRAM, such as using it in the NCCoE’s Mobile lies at the intersection of information security, supply
Device Security building block. chain management, and enterprise risk management
(Figure 4); it is the process of identifying, assessing,
FOR MORE INFORMATION, SEE:
and mitigating the risks associated with the distributed
https://www.nist.gov/itl/privacy-engineering and interconnected nature of IT/OT product and
service supply chains. C-SCRM covers the entire life
CONTACTS:
cycle of a system (including design, development,
PEP Team email: privacyeng@nist.gov maintenance, and destruction), as supply chain threats
and vulnerabilities may intentionally or unintentionally
Ms. Naomi Lefkovitz Ms. Ellen Nadeau compromise an IT/OT product or service at any
(301) 975-2924 (202) 306-4033 stage. These cyber supply chain risks may include
naomi.lefkovitz@nist.gov ellen.nadeau@nist.gov the use of counterfeits, unauthorized production,
tampering, theft, and insertion of malicious software
Ms. Katie Boeckl and hardware, as well as poor manufacturing and
(240) 753-9674 development practices. As shown in Figure 5, C-SCRM
kaitlin.boeckl@nist.gov is concerned with and involves a range of subjects,
including safety, integrity, quality, reliability, and
others, all within an overall environment of awareness.
Cyber Supply Chain Risk
Management (C-SCRM)
Figure 4: C-SCRM Disciplines
Figure 5: C-SCRM Aspects
Over the last several years, providing information
In FY 2017, NIST drafted NISTIR 8179, Criticality
and operational technology (IT/OT) for a supply chain
Analysis Process Model, a method for identifying
has evolved into a complex, globally distributed,
and prioritizing IT/OT systems and components. This
dynamic ecosystem enabling the development of
model is intended to increase an organization’s ability
highly refned, sophisticated, cost-efective, and
to make cost-efective risk decisions by determining
reusable solutions. This ecosystem is composed of
the systems and components that have the most
assorted entities with multiple tiers of outsourcing,
impact on the organization and that would potentially
global distribution routes, diverse technologies, and
cause the most harm if compromised. Figure 6 shows
varying laws, policies, procedures, and practices, all of
an overview of the model, which includes separate
which interact throughout the life cycle of a system.
analyses at the program, system, and component
Factors that allow for low-cost products, rapid
level, and then a trace-back exercise to complete the
innovation, and other benefts also increase the risk
analysis. NIST will fnalize this publication in FY 2018
that the supply chain may be compromised in a way
and will begin to research and write guidance that
that results in risks to the end user and reduce the
overall competitiveness of U.S. companies. builds on this model to identify critical suppliers and 26
service providers.
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

. Define & Scope
_____________
...._.,_ _____________________ _
•
...
13. Program-Level I ~II C. System-Level I II D. Componen -Level
Analysis I Analysis I ~ II Analysis
I II.!-::::::::::,-'==.-====~ • ~ ,
L----------------------- ...- ------------·
E. Traceback
Figure 6: Criticality Analysis Process Overview
During 2017, NIST continued to research the state of establishes minimum criteria for the development
C-SCRM in both the public and private sectors, related and deployment of supply chain risk management
standards and initiatives, efective practices, and capabilities for national security systems. In FY 2017,
metrics. NIST joined with the GSA and the University the group completed the revision of CNSSD 505 and
of Maryland under a contract and grant awarded in developed a self-assessment tool to help agencies
FY 2016 to conduct cyber analytics research on the measure their capabilities and compare those
efectiveness of various risk management practices. capabilities to those of other agencies.
The efort neared conclusion in FY 2017 and found
NIST also sponsored the Software and Supply
correlations between certain practices and publicly
Chain Assurance (SSCA) Forum and Working Groups,
disclosed data breaches. A report on the research will
the purpose of which is to bring together a stakeholder
be published in FY 2018.
community of government, industry, and academic
Similarly, NIST began research in FY 2017 experts in this feld. Meetings are held three to four
to identify metrics that are currently used in times a year and cover a variety of subjects of interest
organizations to measure information security risks. to attendees (see the website at https://csrc.nist.gov/
This research included a review of over 200 published scrm/ssca).
standards, academic papers, organizational white-
NIST began working in FY 2017 to integrate
papers, and other documents and interviews with a
C-SCRM into existing risk management programs and
dozen industry experts on the state of metrics in this
processes. The draft Cybersecurity Framework v1.1
feld. The research will be continued and published in
and Draft SP 800-53 Revision 5 were both updated
FY 2018.
to better include up-to-date C-SCRM guidance. In
NIST continued to co-chair a working group FY 2018, NIST will continue this work by including
with the DoD to revise CNSSD 505, Supply Chain or updating existing C-SCRM concepts in other
Risk Management, which assigns responsibilities and publications as they are developed.
27
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

In FY 2018, NIST will continue to collaborate with of career professionals, including government ofcials,
stakeholders in government, industry, and academia chief information security ofcers, those in academia
to conduct research, produce needed standards and with cybersecurity and supply chain specialties,
guidance, and seek opportunities to create greater system administrators, engineers, consultants,
awareness across all sectors and types and sizes of vendors, software developers, managers, analysts,
organizations. NIST will: specialists in IT and cybersecurity, and many more
felds. The SSCA Forum meets two to three times per
• Update SP 800-161 based on the fnal
year and is free and open to all interested participants,
publication of SP 800-53 Revision 5,
both nationally and internationally.
• Continue developing industry supply chain
While the general intent is to share information,
risk management case studies,
the SSCA Forum also ofers government and
private-sector participants an opportunity to openly
• Develop a draft NISTIR on SCRM “principles”,
collaborate by presenting and receiving feedback on
• Develop a NISTIR on Supply Chain current and potential future work. Most events are two
Interdependency Analysis, and to three days long and contain a mixture of discussion
and presentation. To encourage open interaction,
• Continue research and work on metrics and
SSCA Forum meetings operate under the Chatham
cyber risk analytics.
House Rule, meaning “participants are free to use
the information received, but neither the identity nor
FOR MORE INFORMATION, SEE:
the afliation of the speaker(s), nor that of any other
https://scrm.nist.gov
participant, may be revealed,” though most speakers
allow NIST to post their presentations.
CONTACTS:
Cyber SCRM Team email: scrm-nist@nist.gov The SSCA Forum also maintains an extensive
email subscription service. To receive information
Ms. Celia Paulsen Mr. Jon Boyens about upcoming meetings and related publications
(301) 975-5981 (301) 975-5549 and activities, please sign up for the SSCA Forum
celia.paulsen@nist.gov jon.boyens@nist.gov mailing list, operated by NIST, by sending a blank
email to sw.assurance-join@nist.gov.
Software and Supply Chain FOR MORE INFORMATION, SEE:
Assurance Forum https://csrc.nist.gov/Projects/Supply-Chain-Risk-
Management/SSCA
Cyber supply chain risk management (hardware
CONTACTS:
and software assurance and assured services) has
become a topic of core strategic concern for business
Ms. Celia Paulsen Mr. Jon Boyens
and government leaders worldwide and is an essential
(301) 975-5981 (301) 975-5549
component of an enterprise risk management
celia.paulsen@nist.gov jon.boyens@nist.gov
strategy. The Software and Supply Chain Assurance
(SSCA) Forum provides a venue for government,
industry, and academic participants from around
the world to share their knowledge and expertise
regarding cyber supply chain risks, efective practices
and mitigation strategies, tools and technologies,
and any gaps related to the people, processes, or
technologies involved.
The efort, initiated in 2003, is co-led by NIST,
DHS, DoD and GSA, and serves approximately 3,000
28
stakeholders. Participants represent a diverse group
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

BIOMETRIC STANDARDS AND  was then required to code each of the assertions listed
|     |     |     |     |     |     |     |     | in  the  | CTM  | documentation.  | This  | process  | required  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------------- | ----- | -------- | --------- | --- |
ASSOCIATED CONFORMITY
|     |     |     |     |     |     |     |     | a  large  | amount  | of  development  |     | time  | after  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------------- | --- | ----- | ------ | ---- |
ASSESSMENT TESTING TOOLS  publication of the standard and related CTM, and often
resulted in long delays in the release of conformance
tools. This approach also defned conformance tests
statically, meaning that:
| ITL  | supports  |     | the  | development  | of  | biometric  |     |     |     |     |     |     |     |     |
| ---- | --------- | --- | ---- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
conformance  testing  methodology  standards  and  •   End users with domain-specifc requirements
other conformity assessment eforts through active  or user-defned felds were not able to modify
technical participation in the development of these
the conformance tests or parsing rules.
| standards  | and  | the  | development  |     | of  | associated  |     |     |     |     |     |     |     |     |
| ---------- | ---- | ---- | ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
•   Any modifcation to the base standard
| conformance  |     | test  | software,  | architectures  |     | and  | test  |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ---------- | -------------- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
suites, collectively known as Biometric Conformance  requirements or subsequent revision of the
Test Software (BioCTS). These test tools are developed  standard required a new release of BioCTS
applications.
| to  promote  |         | the  adoption  |          | of  these    | standards  |               | and  |     |            |        |               |      |          |     |
| ------------ | ------- | -------------- | -------- | ------------ | ---------- | ------------- | ---- | --- | ---------- | ------ | ------------- | ---- | -------- | --- |
| to  support  | users,  |                | product  | developers,  |            | and  testing  |      |     |            |        |               |      |          |     |
|              |         |                |          |              |            |               |      | To  | alleviate  | these  | issues,  the  | new  | version  | of  |
labs that require conformance to selected biometric
BioCTS was designed to allow a modifcation of test
| standards.  | ITL  | contributes  |     | to  the  | development  |     | of  |     |     |     |     |     |     |     |
| ----------- | ---- | ------------ | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assertions and parsing rules. This approach required
biometric standards and participates in the INCITS
a confguration fle to specify requirements and allow
| Technical  | Committee  |     | M1  | –  Biometrics  |     | and  related  |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
the software to respond to the needs of the end user.
| subcommittees  |     | and  | in  | ISO/IEC  | Joint  | Technical  |     |     |     |     |     |     |     |     |
| -------------- | --- | ---- | --- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Committee (JTC) 1 Subcommittee (SC) 37 –  Biometrics   BioCTS AN MRT had two releases in FY 2017.
standards bodies.
The frst release included a command line interface
(CLI) as well as a graphical user interface (GUI). It
|     |     |     |     |      |     |     |     | supported  | Level-1  | testing,  | fle  format  |     | testing  | that  |
| --- | --- | --- | --- | ---- | --- | --- | --- | ---------- | -------- | --------- | ------------ | --- | -------- | ----- |
| Bi  |     |     |     | CTS  |     |     |     |            |          |           |              |     |          |       |
checks for the allowed content, length, and value for
fve diferent standards and profles specifed within
the AN MRTs. Since the MRT fles can be combined
to support multiple standards, updates and profles,
BioCTS AN MRT was designed to allow users to test
against multiple standards during a single test.
In early 2017, a suite of BioCTS applications was
released to support user-defned requirements and
profles  for  ANSI/NIST-ITL  (AN-ITL)  specifcations.  _, llooCTSfDrl.NS!mm.ffl.Madw.a-iabll!lelti(fndibonalandNlt.MXMlfnn~
|     |     |     |     |     |     |     |     | filt  Help  |     | -·'  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | --- | --- | --- | --- |
These applications make use of confguration fles to
| dynamically generate parsing rules and conformance  |     |     |     |     |     |     |     |     |     |     | ''"""  |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
requirements for nearly any version or profle of the
|     |     |     |     |     |     |     |     |                     |                             |     | C C . " lf O ~    r                                 | t :u .  ~ \U U : :   , r : t :,nl- | D  N l tl '! • Xl'tt. !:ncod:no  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --------------------------- | --- | --------------------------------------------------- | ---------------------------------- | -------------------------------- | --- |
|     |     |     |     |     |     |     |     | ...a • >l   l ...20 | • 1h     dib • 10     ~ h   |     | lo~o 'P. t, <a iuf l : t~ tcA ! t 'I i C uc: C 1. ' |  ;  T I ) fn . : . t  :            | c: .i. " 1 11                    |     |
AN-ITL  standard.  The  confguration  fles  utilize  an  r ) ', ,b,ocol,trur~\AN~1 \T.-.diu  , 1 H ;  ru t
|             |         |     |           |              |     |         |     | ✓•   | ✓   "  0 : \t , ,,          | o( b \t r " " "\ D .i. ~l \ 2 011\f,.i-t\  | l!.=-e ~t~:  .Dli•O,•!?  | n:?3:i3Z  | n.,:c,11 l~ma: l!ll  | ~   |
| ----------- | ------- | --- | --------- | ------------ | --- | ------- | --- | ---- | --------------------------- | ------------------------------------------ | ------------------------ | --------- | -------------------- | --- |
|             |         |     |           |              |     |         |     |      | r  r   ~ ~ \ A              | M I N l 5 1 U O U V it i M                 | I                        |           |                      |     |
| Extensible  | Markup  |     | Language  | (XML)-based  |     | format  |     |      | •                           |                                            |                          |           |                      |     |
|             |         |     |           |              |     |         |     | ✓    | ✓  ~~\AN$lNtS'1\l'011\Ntt:M |                                            | I                        |           |                      |     |
called ANSI/NIST-ITL Machine Readable Tables (MRTs)  O·\b«b\tr""~~f\2013\1,.o,to
|     |     |     |     |     |     |     |     |     | D;\b,,,;,m\lnri.\DMa~l0.0..5\  |     | P'Ltc Vi'U:SclT"u t:  tl:\111.:.:t,.\tni:.ll\tl1t,1 | \.ul.t~ttf\.2                          | C1-1\11Ilbi:aa.\:111l-a  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --------------------------------------------------- | -------------------------------------- | ------------------------ | --- |
|     |     |     |     |     |     |     |     |     |                                |     | fltlx i ltlunir:IeU :  T I iet ~!                   | . 1 1  ~1U-c.•l~: leiU ~;  ~ l : ilt   | K U l 'l, V l ! U l'O    |     |
(see Figure 7 for an example output). The BioCTS AN- ~~Vt~T\t~110.o .si;  • i4   ,  J •i 'J • .:. !  !- ~ ~   , t ~ • A?lU ~tr-tn ~:
0.,1,b,,offl\tr"""•,DeuWISP,ltSl\itbblOJ)J\ tatlX :SV.ttllailt4.r' t-121,1u: 1.utl!Jo.--ao o:uliUu .•lllto -.:K.uuubo oV1a1lu}-0l'~O1 1.ttt1'-co:ut
|     |     |     |     |     |     |     |     |     |     |     | i);,  Ib t  ! !u ~  ' , | , 'l l i ;u   ~ .4t~ : : : i:   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | ------------------------------- | --- | --- |
ITL applications that use MRTs are collectively referred  Th 1c  ,~ 1 e  ti : . .: : l e r  !Ht   ~ . , u h . V1.1ue l'...1~Cle.1-~!:.e ::iata t\!I
to as BioCTS AN MRT.
.tdll!ur.'tllkrlut :
|     |     |     |     |     |     |     |     |     | .   |     | ;l!\tl~ tJ\t=k | \~ \!11CO$_;;ta_!o!ill\!11c,,;t$_),N__Ki(I\t'  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------------------------------------- | --- | --- |
The  development  of  BioCTS  applications  ---------------------------------..-.- S   \ - ,  - •  ----·tcti1!
traditionally relied on the publication of Conformance
| Testing   | Methodology  |       | (CTM)       | documentation,  |           |             | which  |     |     |     |     |     |     |     |
| --------- | ------------ | ----- | ----------- | --------------- | --------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| specifed  | the          | test  | assertions  |                 | required  | to  assess  |        |     |     |     |     |     |     |     |
Figure 7 - BioCTS AN MRT Testing Multiple
conformance to requirements found in the related
| 29          |                                        |     |     |     |     |     |     |     | Standards Within Single Test  |     |     |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
| biometric   | standard. Manual software development  |     |     |     |     |     |     |     |                               |     |     |     |     |     |
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

The second release included further refnements EAC and TGDC in eforts related to human factors,
of the existing tools, and expanded the testing security, and laboratory accreditation.
capabilities to include Level-2 testing, or the testing
NIST and the EAC established a set of public
of inter-feld as well as inter-record relationships,
working groups to inform the development of a new
checking data between two or more related data
version of the Volunary Voting Systems Guidelines
felds. The current release of BioCTS AN MRT supports
(VVSG). The NIST and EAC goals are to accelerate
all Level-1 and Level-2 tests defned by the MRTs.
the development and adoption of the VVSG by
Work on BioCTS AN MRT continued through FY leading these working groups in close consultation
2017, and an additional release that supports expanded with election ofcials, voting system manufacturers,
character sets, as well as additional enhancements, is standards bodies, academic researchers, and other
expected to be released in FY 2018. members of the public. These working groups focus
on multiple voting system technology areas, including
FOR MORE INFORMATION, SEE:
accessibility, usability, interoperability, security, testing
BioCTS - Biometric Conformance Test Tool and certifcation.
Homepage:
The cybersecurity public working group designed
https://www.nist.gov/itl/csd/biometrics/biometric- principles and guidelines to form the basis for the
conformance-test-software-biocts security requirements in the new version of the VVSG.
Although 15 principles exist, the security-related
BioCTS AN MRT:
principles include auditability, ballot secrecy, physical
https://www.nist.gov/itl/csd/biometrics/biocts- security, access control, system integrity, detection
machine-readable-tables and monitoring, and data protection. Many of these
principles are already included in previous iterations
BioCTS AN MRT Changelog: of the federal standards, whereas others are new
areas of focus (e.g., system integrity). These principles
https://www.nist.gov/fle/384611
and guidelines were presented to, and adopted by, the
BioCTS AN MRT User Guide: Technical Guidelines and Development Committee
(TGDC).
https://www.nist.gov/fle/384606
In FY 2018, NIST will continue leading the public
working groups to inform the development of
CONTACT:
voting system requirements based on the principles
Mr. Dylan Yaga
and guidelines. Additionally, test assertions will be
(301) 975-6004
developed to improve the quality and consistency
dylan.yaga@nist.gov
of testing activities by accredited voting system test
laboratories (VSTLs).
FOR MORE INFORMATION, SEE:
CYBERSECURITY APPLICATIONS https://vote.nist.gov
CONTACTS:
Security Aspects of Electronic Voting Mr. Joshua Franklin Ms. Gema Howell
(301) 975-8463 (301) 975-6299
In 2002, Congress passed the Help America joshua.franklin@nist.gov gema.howell@nist.gov
Vote Act (HAVA) to encourage the upgrade of
voting equipment across the United States. HAVA Mr. Andrew Regenscheid
established the Election Assistance Commission (301) 975-5155
(EAC) and the Technical Guidelines Development andrew.regenenscheid@nist.gov
Committee (TGDC), chaired by the Director of NIST.
30
HAVA directs NIST to provide technical support to the
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

Nationwide Public Safety Broadband  be  shared  between  public  safety  ofcials  as  each
individual goes on and of duty. Furthermore, there will
Network (NPSBN) Cybersecurity
be a need for fexible distribution and credentialing of
devices and users in situations where multiple public
safety organizations are called into action. To facilitate
| ...P...S  |     |     |     | CR  |     |     |                   |     |                 |           |         |      |             |
| --------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------------- | --------- | ------- | ---- | ----------- |
|           |     |     |     |     |     |     | these  needs      |     | NIST,  through  | the       | NCCoE,  |      | piloted  a  |
|           |     |     |     |     |     |     | proof-of-concept  |     | single          | sign  on  | (SSO)   | for  | mobile      |
applications on iOS and Android.
t
SECURITY
Due to the vital nature of frst responder activities,
the mobile applications that will serve public safety
|     |     |     |     |     |     |     | in  their  | mission  | will  require  |     | more  | scrutiny  | when  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | -------------- | --- | ----- | --------- | ----- |
 Source: https://www.pscr.gov/  evaluated  for  software  bugs  and  vulnerabilities
than applications targeted at the public. In FY 2017,
|     |     |     |     |     |     |     | NIST  continued  |     | to  expand  | its  | expertise  | in  | mobile  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ---- | ---------- | --- | ------- |
In February 2012, Congress passed the Middle
Class Tax Relief and Job Creation Act. One portion  application vetting tools and practices. In addition
of  this  legislation  calls  for  the  establishment  of  a  to publishing NISTIR 8136, An Overview of Mobile
Application Vetting Services for Public Safety, ACD, in
| nationwide,  | interoperable  |     | public-safety  |     |     | broadband  |     |     |     |     |     |     |     |
| ------------ | -------------- | --- | -------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
network  based  on  the  3rd  Generation  Partnership  conjunction with NIST Software and System’s Division
Project’s  (3GPP)  Long  Term  Evolution  (LTE)  (SSD), expanded the Static Analysis Tool Exposition
technology.  The  network  will  be  deployed  and  (SATE) to include mobile application analysis for the
operated by the First Responder Network Authority  frst time. This exposition seeks to improve methods
(FirstNet).  The  planned  Nationwide  Public  Safety  for measuring the efectiveness of mobile application
| Broadband  | Network  |     | (NPSBN)  | will  | “create  | a  much  | vetting tools.  |     |     |     |     |     |     |
| ---------- | -------- | --- | -------- | ----- | -------- | -------- | --------------- | --- | --- | --- | --- | --- | --- |
needed nationwide interoperable broadband network
|     |     |     |     |     |     |     | ITL  continued  |     | to  participate  |     | in  | the  standards  |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------------- | --- | --- | --------------- | --- |
that will help police, frefghters, emergency medical
development process for LTE technology within the
service professionals and other public safety ofcials
3rd Generation Partnership Project (3GPP), supporting
stay safe and do their jobs” (see https://www.ntia.
security requirements for public safety that are related
doc.gov/category/public-safety). NIST is directed to
to Proximity Services (ProSe), Group Communication
| conduct  | research  | and  | development  |     | that  | supports  |     |     |     |     |     |     |     |
| -------- | --------- | ---- | ------------ | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
System Enablers (GCSE), and Mission Critical Push-To-
the acceleration and advancement of the nationwide
Talk (MCPTT). NIST also broadened its participation
network.
in 3GPP’s 5th Generation Mobile Networks (5G). In
In FY 2017, CSD, ACD, and the NCCoE continued  addition, researchers broadened their scope within
the Internet Engineering Task Force (IETF) to include
| to  support  | the  | joint  | National  | Telecommunications  |     |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------ | --------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and  Information  Administration  (NTIA)  and  NIST  eforts related to public safety.
| Public  Safety                            |                     | Communications  |     |     | Research   | (PSCR)     |             |         |               |      |       |           |         |
| ----------------------------------------- | ------------------- | --------------- | --- | --- | ---------- | ---------- | ----------- | ------- | ------------- | ---- | ----- | --------- | ------- |
|                                           |                     |                 |     |     |            |            | In  FY      | 2018,   | CSD  and      | ACD  | will  | continue  | to      |
| program (see  https://www.pscr.gov) with  |                     |                 |     |     |            | eforts in  |             |         |               |      |       |           |         |
|                                           |                     |                 |     |     |            |            | strengthen  | NIST’s  | relationship  |      | with  | both      | public  |
| public-safety                             | mobile-application  |                 |     |     | security,  | identity   |             |         |               |      |       |           |         |
safety and commercial telecom stakeholders. Work
| management,    |     | data      | and       | application  |      | isolation  |             |         |              |     |          |      |        |
| -------------- | --- | --------- | --------- | ------------ | ---- | ---------- | ----------- | ------- | ------------ | --- | -------- | ---- | ------ |
|                |     |           |           |              |      |            | concerning  | mobile  | application  |     | vetting  | and  | cyber  |
| technologies,  |     | wearable  | devices,  |              | and  | broadband  |             |         |              |     |          |      |        |
security will continue to evolve as NIST refnes both
standards. The PSCR’s Annual Public Safety Broadband
its methods for tool evaluation as well as its corpus
Stakeholder Conference, held in June 2017, continued
|     |     |     |     |     |     |     | of  test  | cases  | used  in  those  |     | evaluations.  |     | PSCR  is  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---------------- | --- | ------------- | --- | --------- |
to be a valuable venue for ITL to provide updates on
working diligently to fund grants and prize challenges
each of our ongoing projects. The conference also
to both solve current problems and fll future gaps
provided a venue to directly interface with the public
in public safety broadband technology. In FY 2018,
safety and frst responder communities.
ITL will also take on a crucial role in this work by
The mobile devices that will operate on the NPSBN  providing cybersecurity expertise and guidance in the
will be utilized in unique ways when compared to their  administration of these awards.
31
| public  counterparts.  |     | The  | same  | device(s)  |     | will  likely  |     |     |     |     |     |     |     |
| ---------------------- | --- | ---- | ----- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

CONTACTS:  The  ICS  cybersecurity  team  has  used  existing
standards, in conjunction with the NIST Framework
| Mr. Michael Ogata  |     |         Dr. Nelson Hastings  |     |     |     |     |     |     |
| ------------------ | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
for Improving Critical Infrastructure Cybersecurity, to
| (301) 975-6993   |     |         (301) 975-5237  |     |     |     |     |     |     |
| ---------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
michael.ogata@nist.gov        nelson.hastings@nist.gov  develop a target profle for applying cybersecurity
protections within manufacturing environments. The
development of this profle helps establish a roadmap
Cybersecurity for Industrial Control
|     |     |     |     | for  reducing  | cybersecurity  | risk  | for  manufacturers  |     |
| --- | --- | --- | --- | -------------- | -------------- | ----- | ------------------- | --- |
that is aligned with manufacturing sector goals and
Systems
|     |     |     |     | industry  best  | practices.  | The  profle  | tailors  | existing  |
| --- | --- | --- | --- | --------------- | ----------- | ------------ | -------- | --------- |
NIST’s  Industrial  Control  System  (ICS)  cybersecurity control language to be more aligned
cybersecurity efort is focused on providing guidance  with operational technology environments, focusing
and insights into the domain of securing connected  on  desired  cybersecurity  outcomes  to  identify
physical  systems.  ACD  is  supporting  the  NIST  opportunities for improving the current cybersecurity
Engineering Laboratory’s (EL) efort to develop and  posture of a manufacturing system. Through a session
implement  guidance  aimed  at  efectively  securing  during the 2016 Cybersecurity Framework Workshop
ICS,  initially  focusing  on  Smart  Manufacturing  and two public comment periods, the team solicited
Environments. Using an ICS cybersecurity testbed,  feedback from industry partners to help solidify the
a portion of which is shown in Figure 8, NIST will  content in the profle. The Cybersecurity Framework
measure the network and operational performance of  Manufacturing Profle  was published as NISTIR 8183
these systems when instrumented with cybersecurity  (see  https://nvlpubs.nist.gov/nistpubs/ir/2017/NIST.
| protections, in accordance with the best practices  |             |     |               | IR.8183.pdf).  |     |     |     |     |
| --------------------------------------------------- | ----------- | --- | ------------- | -------------- | --- | --- | --- | --- |
| and  requirements                                   | prescribed  |     | by  national  | and            |     |     |     |     |
In 2018, NIST will continue the process of applying
international standards and guidelines. Examples of
the guidance presented in the Manufacturing Profle
such standards and guidelines include International
|     |     |     |     | by  implementing  | the  recommended  |     | cybersecurity  |     |
| --- | --- | --- | --- | ----------------- | ----------------- | --- | -------------- | --- |
Society of Automation (ISA) standard ISA/IEC-62443
|     |     |     |     | controls  within  | the  ICS  | cybersecurity  |     | testbed.  |
| --- | --- | --- | --- | ----------------- | --------- | -------------- | --- | --------- |
and SP 800-82 Revision 2, Guide to Industrial Control
|     |     |     |     | This  application  | of  cybersecurity  |     | controls  | in  an  |
| --- | --- | --- | --- | ------------------ | ------------------ | --- | --------- | ------- |
Systems (ICS) Security (see https://nvlpubs.nist.gov/
nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf).  ICS  environment  will  enable  the  measuring  and
|     |     |     |     | understanding  | of  the  | network  | and  | operational  |
| --- | --- | --- | --- | -------------- | -------- | -------- | ---- | ------------ |
Industrial  Control  Systems  are  an  essential  performance impacts that cybersecurity protections
component  in  manufacturing  environments.  have  on  these  systems.  In  addition  to  providing
Increasing  reliance  on  technology,  communication,  performance  data,  this  project  will  produce
and the interconnectivity of ICS and IT has expanded  documentation  relating  to  the  implementation
the  potential  vulnerabilities  and  increased  the  intricacies  and  special  requirements  presented  by
potential  risk  to  manufacturing  operations.  While  these non-traditional environments.
these manufacturing systems become smarter and
FOR MORE INFORMATION, SEE:
| increasingly  | connected,  | providing  | a  tremendous  |     |     |     |     |     |
| ------------- | ----------- | ---------- | -------------- | --- | --- | --- | --- | --- |
https://www.nist.gov/itl/privacy-engineering
increase in value and efciency, they also present
a new challenge: “How is cybersecurity efectively
CONTACTS:
applied to this connected domain?”
|     |     |     |     | Mr. Jefrey Cichonski     |           Mr. Keith Stoufer (EL)  |     |     |     |
| --- | --- | --- | --- | ------------------------ | --------------------------------- | --- | --- | --- |
|     |     |     |     | (301) 975-3293           |           (301) 975-3877          |     |     |     |
jefrey.cichonski@nist.gov       keith.stoufer@nist.gov
Smart Grid Cybersecurity
In December 2007, Congress passed the Energy
Independence and Security Act (EISA) that gave NIST
a leading role in the coordination and acceleration of
Figure 8: Collaborative robotics portion of the ICS  32
smart grid interoperability and security standards in
cybersecurity testbed
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

|     |     |     |     |     |     |     | opportunities  | to  collaborate  | with  | the  National  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------- | ----- | -------------- | --- |
collaboration with the private sector. The NIST Smart
Grid program is led by the Engineering Laboratory  Renewable Energy Laboratory (NREL) about smart
(EL) with support from the Physical Measurement and  grid cybersecurity.
Information Technology Laboratories. The objective
FOR MORE INFORMATION, SEE:
| of  the  | program  | is  | to  advance  | the  | measurement  |     |     |     |     |     |     |
| -------- | -------- | --- | ------------ | ---- | ------------ | --- | --- | --- | --- | --- | --- |
science  that  will  increase  asset  utilization  and  https://www.nist.gov/engineering-laboratory/smart-
| efciency, improve grid reliability, and enable greater  |     |     |     |     |     |     | grid   |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
use of renewable energy sources in the grid through  https://www.nist.gov/programs-projects/
research, standardization, testing and implementation  cybersecurity-smart-grid-systems
https://sepapower.org
of the NIST Smart Grid Interoperability Framework.
| In the Spring of 2017, the Smart Grid Interoperability  |     |     |     |     |     |     | CONTACT:  |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
Panel (SGIP) merged with the Smart Electric Power
Dr. Nelson Hastings
| Alliance  | (SEPA).  | SEPA’s  | Smart  | Grid  | Cybersecurity  |     |     |     |     |     |     |
| --------- | -------- | ------- | ------ | ----- | -------------- | --- | --- | --- | --- | --- | --- |
(301) 975-5237
Committee (SGCC) is led by an ITL representative.
nelson.hastings@nist.gov
| The  SGCC  | conducts  |     | regular  | outreach  | regarding  |     |     |     |     |     |     |
| ---------- | --------- | --- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- |

| cybersecurity                                          |     | issues  | related  | to  the  | smart  | grid,  |     |     |     |     |     |
| ------------------------------------------------------ | --- | ------- | -------- | -------- | ------ | ------ | --- | --- | --- | --- | --- |
| including such topics as identity and key management.  |     |         |          |          |        |        |     |     |     |     |     |
Examples of this outreach include bi-weekly calls and
SOFTWARE ASSURANCE &
support to the SEPA Grid Evolution Summit held on
QUALITY
July 25-27, 2017 in Washington, D.C., where the SGCC
held its annual face-to-face meeting and included a
presentation on the public key infrastructure by ACD’s
Tim Polk. In addition to participating in SEPA’s SGCC,  Outstanding  computer  security  is  based  on
CSD and ACD personnel are participating in SEPA’s
|     |     |     |     |     |     |     | software  | implementations  | that  minimize  |     | the  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | --------------- | --- | ---- |
OpenFMB working groups to support cybersecurity
|     |     |     |     |     |     |     | existence  | of  vulnerabilities.  | To  develop  | processes  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------- | ------------ | ---------- | --- |
capabilities.
that deliver high-quality software, it is vital to be able
to fnd, characterize, and categorize vulnerabilities,
| In  FY  | 2017,  | researchers  |     | from  | ITL  worked  | on  |     |     |     |     |     |
| ------- | ------ | ------------ | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
weaknesses, and faults that appear in code. Processes
defning a grid edge experiment to understand the
can then be improved to preclude these faults, detect
| performance  |     | impact  | of  | cybersecurity  | capabilities  |     |     |     |     |     |     |
| ------------ | --- | ------- | --- | -------------- | ------------- | --- | --- | --- | --- | --- | --- |
them earlier, or build in mitigations for them. The
on resource-constrained components of the grid. In
NIST Software Assurance Metrics And Tool Evaluation
addition, researchers explored how to leverage and
|              |                |     |     |                   |     |       | (SAMATE)  | program  promotes  | efective  | software  |     |
| ------------ | -------------- | --- | --- | ----------------- | --- | ----- | --------- | ------------------ | --------- | --------- | --- |
| incorporate  | cybersecurity  |     |     | risk  management  |     | into  |           |                    |           |           |     |
assurance processes and also evaluates methods for
the next version of the Smart Grid Interoperability
automated tools to provide confdence that software
Framework. ITL experts supported the Department
is free from vulnerabilities. The SAMATE program has
| of  Energy  | (DoE)  | Cyber  |     | Resilient  | Energy  | Delivery  |     |     |     |     |     |
| ----------- | ------ | ------ | --- | ---------- | ------- | --------- | --- | --- | --- | --- | --- |
three primary components: the Software Assurance
Consortium (CREDC) program by participating in their
Reference Dataset (SARD), the Static Analysis Tool
Annual Industry Workshop in Tempe, AZ and program
Exposition (SATE), and the Bugs Framework (BF).
peer review held in Washington, D.C. Through a grant
to the University of New Hampshire, NIST supported  SARD  is  a  public  repository  of  hundreds  of
research into adding security mechanisms to the IEEE
thousands of computer programs with known security
1588 Precision Time Protocol (PTP).
|     |     |     |     |     |     |     | faws  | (see  https://samate.nist.gov/SARD).  |     |     | The  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------------------------------- | --- | --- | ---- |
programs are primarily in fve computer languages,
In FY 2018, ITL will continue to coordinate with EL
C, C++, Java, PHP, and C#, and include synthetic test
and the Smart Grid Program in the development of the
cases (small programs written as tests), open-source
next version of the NIST Smart Grid Interoperability
production programs, and production programs with
Framework 2.0 and in an execution of the grid edge
vulnerabilities injected. See Figure 9 for a graph of the
| experiment  | on  | the  | NIST  | Smart  Grid  | Testbed.  | ITL  |     |     |     |     |     |
| ----------- | --- | ---- | ----- | ------------ | --------- | ---- | --- | --- | --- | --- | --- |
size, type, and languages of the test cases. This rich
will continue to chair SEPA’s SGCC and support the
33
collection allows software developers to assess tools
DoE CREDC program, and will look for and explore
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

and helps tool developers to refne their techniques. Research Projects Activity (IARPA), academia, and
SARD includes contributions from government industry. In FY 2017, mobile applications and test
organizations, such as the Defense Advanced cases used in former Static Analysis Tool Expositions
Research Project Agency (DARPA), the National were added to SARD.
Security Agency (NSA), the Intelligence Advanced
SYN
~ ~ D
Bar height is log number of test cases '?
c::=::=ii PRO
D
(not to scale) ,oo~ INJ
D
C#
Java
 D ~
0)
m
:::l nr:==7
0)
PHP D
Cm
_J
•
C++
C • • •
5 10 100 1000 10000 100000
Number of lines of code
Figure 9: Graph of Size, Type, and Languages Of Test Cases in SARD
The sixth instance of SATE began in FY 2017. reports and publicly reported their experiences at a
The SAMATE prepares test cases to measure the workshop. The purpose of SATE is to understand the
strengths of tools in fnding source code that may state of technology and society’s justifed confdence
lead to serious breaches. More than a dozen tool in software. SATE VI has three tracks: the classic track,
makers will run their software analysis tools on these a track to assess mobile application vetting services,
test cases. NIST researchers, aided by others in the and the Ockham track for sound analysis. For more
software assurance community, analyzed the tool information, see https://samate.nist.gov/SATE.html.
34
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

Just as the medical profession has vocabulary to  4.   Faulty Operation (FOP)–integer overfow,
precisely indicate anatomy, symptoms, and diseases,  divide by zero, etc.;
the BF seeks to improve the science of secure software
5.   Memory Allocation (MAL)–double free,
by providing orthogonal, unambiguous language for
use after free, etc.;
software professionals. The BF comprises classes of
software faults, including their attributes, causes, and
6.   Encryption (ENC)–including decryption,
consequences. Figure 10 illustrates the causal graph
for bufer overfow (BOF) faults. FY 2017 updates  7.   Verifcation (VRF), and
include eight classes (including three cryptography
8.   Key Management (KMN).
classes):
Defnitions, examples, and causal graphs of these
1.   Injection (INJ)–SQL, OS, etc.;
|     |     | classes  and  | links  to  | publications  | are  available  | at  |
| --- | --- | ------------- | ---------- | ------------- | --------------- | --- |
2.   Control of Interaction Frequency (CIF);  https://samate.nist.gov/BF.
3.   Bufer Overfow (BOF);
|     | CAUSES  | ATTRIBUTES  |     | CONSEQUENCES  |     |     |
| --- | ------- | ----------- | --- | ------------- | --- | --- |
Access:
✓ Read
✓Write
Incorrect Results
Boundary:
✓ Below
|     |      | ✓ Above    | Program Crash  |     |     |     |
| --- | ---- | ---------- | -------------- | --- | --- | --- |
|     | ARC  | Location:  |                |     |     |     |
✓ Heap
System Crash
|     | Result Fault:  | ✓ Stack  |     |     |     |     |
| --- | -------------- | -------- | --- | --- | --- | --- |
Magnitude:
✓ Overflow
|        | ✓ Underflow   | ✓ Small     |     |     |     |     |
| ------ | ------------- | ----------- | --- | --- | --- | --- |
|        | ✓ Undefined   | ✓ Moderate  |     |     |     |     |
| r::'\  | ✓ Truncation  | ✓ Far       |     |     |     |     |
|        | Operator:     | Data Size:  |     |     |     |     |
✓ Little
~ Operand Error:
|     | Types:  | ✓ Some  |     |     |     |     |
| --- | ------- | ------- | --- | --- | --- | --- |
✓ Huge
Excursion:
|     |     | ✓ Continuous  ACI  |     |     |     |     |
| --- | --- | ------------------ | --- | --- | --- | --- |
✓ Discrete
Incorrect Conversion

Figure 10: Causal Graph for Bufer Overfow
CONTACT:
Dr. Paul E. Black
(301) 975-4794
paul.black@nist.goV
35
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

FEDERAL CYBERSECURITY S&T Education and Research (FASTER) Community
of Practice (CoP). Barry I. Schneider is co-chair of
RESEARCH AND DEVELOPMENT
High End Computing (HEC) IWG. Chris Greer and Al
(R&D) Wavering from NIST’s Engineering Laboratory co-
chair NITRD’s Cyber Physical Systems (CPS) IWG and
the High Confdence Software and Systems (HCSS)
IWG, respectively.
Networking and Information Technology
Research and Development (NITRD) program Tim Polk is the principal NIST participant in the bi-
provides a framework in which many federal agencies weekly coordination activities of the federal Special
come together to coordinate their networking and Cyber Operations Research and Engineering (SCORE)
IT research and development (R&D) eforts. NIST Committee. SCORE enables technology transfer
remained committed to the value of communicating through the sharing of NIST cybersecurity expertise
its R&D eforts to other federal colleagues and and publications with researchers throughout the
identifying the opportunities to support R&D eforts Federal Government. The SCORE committee interacts
throughout the Federal Government. with federal leaders and reports to the National
Science and Technology Council’s Committee on
NIST is a consistent presence at the monthly
Homeland and National Security.
cybersecurity meetings with Bill Newhouse, National
Cybersecurity Center of Excellence (NCCoE) Security All the NIST leaders for interagency coordination
Engineer and the National Initiative for Cybersecurity leverage these working groups and committees to
Education (NICE) Deputy Director, as the co-chair communicate powerfully about NIST’s research,
of the Cyber Security and Information Assurance frameworks, and publications and bring back insights
Interagency Working Group (CSIA IWG). During and activities relevant to NIST’s work.
FY 2017, NIST provided updates to the CSIA IWG
describing the updates to the NIST Cybersecurity FOR MORE INFORMATION, SEE:
Framework, SP 800-53, Security and Privacy Controls https://www.nitrd.gov
for Information Systems and Organizations, and the
CONTACT:
NICE program.
Mr. Bill Newhouse
Naomi Lefkowitz, Senior Privacy Policy Advisor
(301) 975-0232
at NIST, co-chairs the Privacy R&D IWG, which
william.newhouse@nist.gov
coordinates the multidisciplinary research and
development conducted by NITRD agencies that seek
to produce knowledge and technologies that identify
and mitigate emerging risks to our privacy, and that
COMPUTER FORENSICS
enables individuals, companies, and the government
to beneft from technological advancements while
being able to efectively balance the resulting benefts
with resulting risks to privacy. The activity involves Digital evidence includes software, hardware,
research into and development of methods for and data on computers and mobile devices (e.g.,
characterizing privacy expectations, understanding audio, video, and image fles). Digital evidence can
privacy violations, engineering privacy-protecting be a part of investigating most crimes, since material
systems, recovering from privacy violations, and the relevant to the crime may be recorded in digital form.
impact of privacy on public policy and of public policy Methods for securely acquiring, storing and analyzing
on privacy. digital evidence quickly and efciently are critical. ITL
promotes the efcient and efective use of computer
Ram Sriram is the co-chair of NITRD’s Software
technology to investigate crimes. The project team
Productivity, Sustainability, and Quality (SPSQ)
develops tools for testing computer forensic software,
Interagency Working Group (IWG). Robert B. Bohn
including test criteria and test sets. ITL also maintains 36
is the co-chair of NITRD’s Faster Administration of
the National Software Reference Library (NSRL) – a
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

vast archive of published software applications that is Tool Testing (CFTT) project at NIST is to establish
an important resource for both criminal investigators a methodology for testing computer forensic
and historians. software tools by the development of general tool
specifcations, test procedures, test criteria, test sets,
and test hardware. The project is intended to provide
the information necessary for toolmakers to improve
tools, for users to make informed choices about
acquiring and using computer forensics tools, and
for interested parties to understand the capabilities
of the tools. The project team’s approach for testing
computer forensic tools is based on well-recognized
National Software Reference Library
international methodologies for conformance testing
The NSRL is designed to collect software and quality testing that ensures that forensic software
from various sources and incorporate fle profles tools consistently produce accurate and objective test
computed from this software into a Reference Data results.
Set (RDS) of information. The RDS can be used by law
In FY 2016, the CFTT project expanded to allow
enforcement, government, and industry organizations
forensics testers to use the NIST testing methodology
to review fles on a computer by matching fle profles
in their own labs and to produce standardized test
in the RDS. This will help alleviate much of the efort
reports for disk imaging forensic tools. In FY 2017,
involved in determining which fles are important as
federated testing was further expanded with three
evidence on computers or fle systems that have been
major updates: a revision to disk-imaging testing, the
seized as part of criminal investigations. The NSRL
addition of mobile device tool testing and hardware
also provides a research environment to promote the
write-blocker testing. In FY 2018, the project will be
development of new forensics techniques and other
expanded to support string searching and forensic
applications in computer science.
media preparation. The forensic community is
The RDS continues to be the premier software beginning to use federated testing to test tools and
resource and, in FY 2017, the NSRL published four share test reports. The CFTT project also maintains the
releases. There are currently 23,000 microcomputer Forensics Tool Catalog and the Computer Forensics
applications and 160,000 mobile device applications Reference Data Sets (CFReDS). The Tool Catalog
yielding a combined total of 326 million fles. In FY website is a community-sourced catalog of forensic
2017, the NSRL was expanded to include mobile tools aided by a taxonomy of forensic tools. The Tool
applications and to include the profles obtained from Catalog grew by 17 tools in FY 2017. The CFReDS data
installing and exercising applications. sets are used in a variety of settings, such as university
classes, to try out forensics tools on known data.
FOR MORE INFORMATION, SEE:
https://www.nsrl.nist.gov,
https://toolcatalog.nist.gov,
https://www.cfreds.nist.gov. and
https://www.cftt.nist.gov
CONTACTS:
Mr. Doug White Dr. Jim Lyle
Computer Forensics Tool Testing Project (301) 975-4761 (301) 975-3270
doug.white@nist.gov james.lyle@nist.gov
There is a critical need in the law enforcement
community to ensure the reliability of computer
37 forensic tools. The goal of the Computer Forensic
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

|     |     | OPERATE  |     |     | OVERSEE  |     | PROTECT  |     |     | COLLECT  |     |     |
| --- | --- | -------- | --- | --- | -------- | --- | -------- | --- | --- | -------- | --- | --- |
SECURELY
|            |     |           | AND  |     | AND     |     |         | AND  |          |          | INVESTIGATE  |     |
| ---------- | --- | --------- | ---- | --- | ------- | --- | ------- | ---- | -------- | -------- | ------------ | --- |
| PROVISION  |     |           |      |     |         |     |         |      | ANALYZE  | AND      |              |     |
|            |     | MAINTAIN  |      |     | GOVERN  |     | DEFEND  |      |          | OPERATE  |              |     |
Figure 11: The Seven Categories of the NICE Framework
CYBERSECURITY AWARENESS,  In support of goal 3, NICE published SP 800-181,
The NICE Framework, in August 2017 (see https://
TRAINING, EDUCATION, AND
|     |     |     |     |     |     |     |     | nist.gov/nice/framework).  |     | The  NICE  | Framework  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | ---------- | ---------- | --- |
OUTREACH  establishes  a  taxonomy  and  common  lexicon  that
is to be used to describe all cybersecurity work and
workers, irrespective of where or for whom the work
National Initiative for Cybersecurity  is performed. Figure 11 shows the seven categories of
the NICE Framework. These categories further break
Education (NICE)
down into Specialty Areas, Work Roles, Tasks, and
Knowledge, Skills, and Abilities (KSAs).
| Since          | 2010       | NIST’s     |     | National       |          | Initiative  | for      |     |     |     |     |     |
| -------------- | ---------- | ---------- | --- | -------------- | -------- | ----------- | -------- | --- | --- | --- | --- | --- |
| Cybersecurity  |            | Education  |     | (NICE)         | seeks    | to          | foster,  |     |     |     |     |     |
| energize,      | and        | promote    | a   | robust         | network  | and         | an       |     |     |     |     |     |
| integrated     | ecosystem  |            | of  | cybersecurity  |          | education,  |          |     |     |     |     |     |
training, and workforce development. NICE has been
focusing on eforts to achieve this by aligning to three
goals: 1) accelerate learning and skills development, 2)
nurture a diverse learning community, and 3) guide
career development and workforce planning.
In support of goal 1, in November 2016, CyberSeek
| was  launched  |           | to      | provide  | a  visualization   |     |          | of  the  |     |     |     |     |     |
| -------------- | --------- | ------- | -------- | ------------------ | --- | -------- | -------- | --- | --- | --- | --- | --- |
| demand         | for  and  | supply  |          | of  cybersecurity  |     | workers  |          |     |     |     |     |     |
across the nation (see http://cyberseek.org). At its
launch, the tool also provided a visualization of career
pathways in cybersecurity. The data from this tool, in
part, has helped NICE develop an executive overview
Figure 12: Clarence Williams, Lead for Government
white paper on Cybersecurity Workforce Demand. In
Engagement at NICE, and Rodney Petersen,
FY 2017, NICE also supported goal one through the
Director of NICE, speak with an attendee at the
| development  |     | of  a  | paper  | regarding  |     | Cybersecurity  |     |     |     |     |     |     |
| ------------ | --- | ------ | ------ | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
CyberSecureGov Conference in Washington, D.C.
Apprenticeships. This report and other white papers
developed by NICE authors are available at https://
NICE continued its coordination with academic,
www.nist.gov/itl/applied-cybersecurity/nice/
|     |     |     |     |     |     |     |     | industry  | and  government  | partners  | throughout  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | --------- | ----------- | ---- |
resources/one-pagers.
year at various meetings, workshops and events. In
August 2017, NICE held a workshop in Chicago, Illinois.
In support of goal 2, NICE hosted a Veterans in
Cybersecurity Workshop in March 2017. This workshop  This workshop, along with a Request for Information
|     |     |     |     |     |     |     |     | that  NICE  | issued,  provided  | information  | to  | inform  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------ | ------------ | --- | ------- |
convened approximately 40 representatives of federal
work and to prepare a report to the President on the
| and  state  | government,  |     |     | branches  | of  | the  military,  |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
industry, and workforce development organizations  fndings and recommendations about supporting the
growth and sustainment of the nation’s cybersecurity
| to  explore  | issues,  |     | discuss  | initiatives  |     | and  | better  |     |     |     |     |     |
| ------------ | -------- | --- | -------- | ------------ | --- | ---- | ------- | --- | --- | --- | --- | --- |
workforce in the public and private sectors.
understand the gaps that exist in helping our veterans
transition to careers in cybersecurity.
38
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

In FY 2018, NICE will continue to promote and  organized around several primary content types to
coordinate annual NICE activities such as the NICE  make information easier to fnd and maintain: projects,
Quarterly eNewsletter; the NICE Webinar Series; the  publications, news, events and presentations. A new
NICE Conference to be held on November 7-8, 2017  taxonomy of topics is used to tag content site-wide,
in  Dayton,  Ohio;  and  the  NICE  K-12  Cybersecurity  and  an  online,  searchable  glossary  of  information
Education Conference to be held December 4-5, 2017  security terminology expands on the terms identifed
in Nashville, Tennessee. NICE will also kick of the  in NISTIR 7298 Revision 2. One of the most noticeable
frst annual National Cybersecurity Career Awareness  changes is a vastly improved publications section, in
Week  on  November  13-18,  2017  to  focus  local,  terms of content, searchability, and browsing. At the
regional, and national interest to inspire, educate, and  end of FY 2017, the site provided detailed information
engage children through adults to pursue careers in  about more than 1,200 of NIST’s current and historical
| cybersecurity.  |     |     |     |     |     |     | information security publications.  |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
FOR MORE INFORMATION, SEE:  The  CSRC  Redesign  Team  designed  the  site’s
|     |     |     |     |     |     |     | architecture  | and  | interface  | to  | signifcantly  |     | improve  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ---------- | --- | ------------- | --- | -------- |
https://www.nist.gov/itl/applied-cybersecurity/nice
site navigation, search, and the ability of ITL staf to
CONTACTS:  maintain and contribute content. The site also uses
Mr. Rodney Petersen      Ms. Danielle Santos  responsive design to greatly improve CSRC’s usability
|                 |     |                    |     |     |     |     | on  mobile  | devices.  |     | More  than  | 21,000  | individual  |     |
| --------------- | --- | ------------------ | --- | --- | --- | --- | ----------- | --------- | --- | ----------- | ------- | ----------- | --- |
| (301) 975-8897  |     |    (301) 975-5048  |     |     |     |     |             |           |     |             |         |             |     |
content items were transferred from the legacy site,
| rodney@nist.gov   |     |     danielle.santos@nist.gov  |     |     |     |     |          |           |        |                    |     |           |     |
| ----------------- | --- | ----------------------------- | --- | --- | --- | --- | -------- | --------- | ------ | ------------------ | --- | --------- | --- |
|                   |     |                               |     |     |     |     | and  in  | February  | 2017,  | ITL  successfully  |     | launched  | a   |
beta version of the new site. Feedback from beta-
Computer Security Resource Center  site users over seven months was incorporated by
| (CSRC)  |     |     |     |     |     |     | the  CSRC  | Redesign  |     | Team  to  | fx  bugs,  | implement  |     |
| ------- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --------- | ---------- | ---------- | --- |
enhancements, and refne the site’s look and feel. The
For more than 20 years, the CSRC website has  team considered all comments it received, and made
provided  stakeholders  with  signifcant  information  every efort to implement those suggestions. After
about  ITL’s  cybersecurity  research  and  testing  making signifcant, gradual improvements to the beta
site, NIST launched the new CSRC on September 18,
| programs.  | Consistently  |     | one  of  | the  | most-visited  |     |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | -------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
websites  at  NIST,  CSRC  is  used  by  several  ITL  2017, while simultaneously retiring the legacy site.
divisions to communicate information about NIST’s
In FY 2018, the CSRC Redesign Team will continue
| cybersecurity  | and  | privacy  | programs  |     | and  | projects,  |     |     |     |     |     |     |     |
| -------------- | ---- | -------- | --------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
to enhance the content, functionality and usability of
research, validation testing, software tools, and other
the new site, striving to provide a better and more
areas of interest to NIST’s customers in government,
useful experience to site users.
industry, academia and elsewhere, both within the
U.S. and globally.
The CSRC team maintains an email subscription
list with more than 78,000 subscribers worldwide.
| The  | CSRC  website  |     | serves  | as  a  | primary  | NIST  |     |     |     |     |     |     |     |
| ---- | -------------- | --- | ------- | ------ | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Subscribers receive notifcations when news updates,
| repository  | of  cybersecurity  |     | and  | privacy  | standards,  |     |     |     |     |     |     |     |     |
| ----------- | ------------------ | --- | ---- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
event details, and publication information—including
| guidelines,  | and  technical  |     | documents.  |     | Refer  | to  the  |     |     |     |     |     |     |     |
| ------------ | --------------- | --- | ----------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
the release of draft publications for public comment—
| Publications  | Released  | in  | FY  2017   | section  |     | of  this  |              |     |        |             |      |            |        |
| ------------- | --------- | --- | ---------- | -------- | --- | --------- | ------------ | --- | ------ | ----------- | ---- | ---------- | ------ |
|               |           |     |            |          |     |           | are  posted  | to  | CSRC.  | To  review  | the  | available  | lists  |
annual report for details about the ITL Cybersecurity
and subscribe, visit https://csrc.nist.gov/ and in the
Program’s publications released in FY 2017.
|     |     |     |     |     |     |     | page  footer  | click  | either  | the  | envelope  | icon  | or  the  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ------- | ---- | --------- | ----- | -------- |
CSRC’s  most  signifcant  event  occurred  in  “Subscribe to CSRC Updates” link. Additional NIST/ITL
Cybersecurity topics are available including: Federal
| September  | 2017,  with  | the  | launch  | of  | a  completely  |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ---- | ------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
redesigned,  content  management  system-based  Information Security Management Act (FISMA) news;
website. In addition to aligning with the main NIST  Cybersecurity  Framework;  National  Initiative  for
Cybersecurity Education (NICE); ITL’s Trusted Identity
website’s look and feel, the new CSRC website is
Group (TIG), and several lists for the NCCoE.
39
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

FOR MORE INFORMATION, SEE: The Forum conducts quarterly meetings and an
annual two-day conference for a discussion of current
https://csrc.nist.gov
issues and topics of interest to those responsible for
CONTACTS: supporting the information security programs of
federal agencies.
Questions regarding the CSRC website can be sent
to the CSRC Webmasters at:
Discussion topics at the quarterly FCSM meetings
webmaster-csrc@nist.gov
in FY 2017 included briefngs on:
Mr. Patrick O’Reilly Ms. Nicole Keller • The National Cybersecurity Center of
(301) 975-4751 (301) 975-3648 Excellence (NCCoE) - Federally Funded
patrick.oreilly@nist.gov nicole.keller@nist.gov Research and Development Center (FFRDC),
• Developing an information security continuous
Federal Computer Security Managers’
monitoring (ISCM) Assessment Methodology,
(FCSM) Forum
• Security Automation and Continuous
The Federal Computer Security Managers’ Forum Monitoring,
(the Forum) is sponsored by NIST to promote the
• Demonstration of a Continuous Diagnostic
sharing of security-related information among federal
Monitoring Instance,
agencies. The Forum, which serves more than 1,000
members, strives to provide an ongoing opportunity • Guidance for Assigning New Cybersecurity
for managers of federal information security Codes to Positions with IT/Cybersecurity/
programs to exchange information security materials Cyber-related Functions and the New
in a timely manner, build upon the experiences of Cybercareers.gov Site,
other programs, and to reduce possible duplication
of eforts. It provides a mechanism for NIST to share • Using Risk Management to Improve Privacy in
information directly with federal agency information Federal Systems,
security managers in fulfllment of NIST’s leadership
• National Cybersecurity and Communications
mandate under FISMA. The Forum also assists NIST
Integration Center (NCCIC) 101, and
in establishing and maintaining relationships with
other individuals and organizations that are actively • Creating a Cybersecurity Scorecard for a
addressing information security issues within the Federal Agency.
Federal Government. During FY 2017, CSD’s Victoria
Pillitteri and Jody Jacobs served as Co-Chairs, and FY 2017’s annual two-day meeting was held at
Peggy Himes from ACD served as the Secretariat of NIST on June 20-21, 2017 with over 220 attendees.
the Forum, providing administrative and logistical Presentations included the current technical,
support. Additionally, during FY 2017, the FCSM operational and management information systems
webpage was signifcantly restructured and updated security topics and updates on the information
to ensure that presentation information, both current system security activities of OMB, General Services
and archived, is delivered as efciently and efectively Administration (GSA), Department of Homeland
as possible. Security (DHS), Department of Health and Human
Services (HHS), NARA, Internal Revenue Service (IRS),
The Forum maintains an extensive email National Weather Service (NOAA), Ofce of Personnel
subscription service/listserv. Participation in the Management (OPM), and NIST. A frst ever “ask the
service is restricted to those Federal and State experts” panel was held where attendees could ask
Government employees and their designated support subject matter experts on security, privacy, and
contractors with a role in the management of their procurement-related questions. Most presentations
organization’s information system security program. from the two-day ofsite and monthly meetings are
The email listserv ofers an open forum for information available online (see https://csrc.nist.gov/Projects/
40
sharing of best practices and recommendations, and Forum/Archived-Events-and-Presentations).
serves as a resource for this community of interest.
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

The following is a list of presentations that were Federal Information Systems Security
given at the annual two-day meeting:
Educators’ Association (FISSEA)
• Overview of SP 800-184, Guide for
The Federal Information Systems Security
Cybersecurity Event Recovery
Educators’ Association (FISSEA), founded in 1987, is
• FedRAMP Tailored an organization hosted by NIST for information system
security professionals to assist federal agencies in
• Overview of the Software Quality Assurance
meeting their information system’s security awareness,
Project and Software Assurance Marketplace
training, and education responsibilities. FISSEA strives
to elevate the general level of information system
• Applying the Cybersecurity Framework in
security knowledge for the Federal Government
Federal Agencies: Presentation and Panel
and the federal workforce. It also seeks to assist the
Discussion
professional development of its members.
• Top Down vs. Bottom Up Governance of Risk,
FISSEA membership is open to information system
What’s Best?
security professionals, professional trainers and
• Cybersecurity Dashboard on a Shoestring educators, and managers responsible for information
Budget system security training programs in federal agencies,
as well as contractors of these agencies and faculty
• High Vulnerability Asset Overlay
members of accredited educational institutions who
are involved in information security training and
• Pushing Computers to the Edge: Next
education. Willingness to share products, information,
Generation Security and Privacy Controls for
and experiences is all that is required to become a
Systems and IoT Devices
FISSEA member. A working group meets monthly to
• Infusing Cybersecurity into the Government administer business activities.
Acquisition Process
FISSEA maintains a website and a mailing list, and
• Government Accountability Ofce Update participates in a social networking site as a means of
communication for its members. CSD assists FISSEA
• “Ask the Experts” Panel
with its operations by providing staf support for
several of its activities and by being FISSEA’s host
• NIST Interagency Report 8011, Automation
agency.
Support for Security Control Assessments
The 30th Annual FISSEA Conference occurred on
The Forum plays a valuable role in helping NIST
June 19, 2017 at NIST. The FISSEA audience included
and other federal agencies develop and maintain
managers responsible for information systems
a strong, proactive stance in the identifcation and
security awareness, training, certifcations, workforce
resolution of new strategic and tactical IT security
identifcation, compliance, etc. in federal agencies;
issues as they emerge. The email list of interested
contractors providing awareness and training support;
parties has steadily increased in size and provides
and faculty members of accredited educational
a valuable resource for Federal and State security
institutions who are involved in information security
program managers.
training and education. Clarence Williams, Peggy
FOR MORE INFORMATION, SEE: Himes, Gretchen Morris (DB Consulting Group/NASA),
and other members of the FISSEA Working Group,
https://csrc.nist.gov/Projects/Forum
were integral to the efort to support the conference.
CONTACTS:
This year’s theme was “Securing the Future to
Ms. Victoria Pillitteri Ms. Jody Jacobs
Infnity and Beyond: Improving Cybersecurity through
(301) 975-8542 (301) 975-4728
Awareness, Training, and Education”. Attendees
victoria.pillitteri@nist.gov jody.jacobs@nist.gov
gained new techniques for developing/conducting
41
training, cost-efective practices, considerations for
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

compliance, and free resources and contacts. Over Rosenberg, Andrew Ellis, John Ippolito, & Sam
150 cybersecurity training professionals attended the Carter, Native Intelligence, Inc. and Friends
one-day conference.
• Website: The Security Training and Awareness
NIST’s ITL Director, Charles Romine, welcomed Program Team, Employment and Social
attendees to the event. FISSEA Lifetime Member, Development Canada (ESDC).
Louis Numkin, provided a historical timeline of
• Motivational Item: K Rudolph, Native
FISSEA, recognizing 30 years of providing a platform
Intelligence, Inc.
for security specialists to collaborate, network, and
learn.
• Newsletter: IHS Policy & Security Awareness
Team, Indian Health Service
Presenters represented NIST, DHS, DoD, HHS,
private industry, and academia. Attendees had an
• Security Training Scenarios: Division of
opportunity to share about their specifc awareness
Information Security; Policy & Security
and training programs throughout the conference.
Awareness Team, Ofce of Information
Technology, Indian Health Service
The FISSEA Educator of the Year Award was
established to recognize and honor a contemporary
• Video: Rita John, John Creery, Chelsea O’Hara,
who is making special eforts to create, build, manage,
Nellie MacNeil, Kyle Bachan, Tim Herman,
or inspire an information systems security awareness,
Rosanne Trudel, & Sapna Kalhan, IFDS Canada
training, or education program. Gretchen Morris, 2015
FISSEA Educator of the Year, presented the 2016 Publicly available YouTube video Uniform Resource
FISSEA Educator of the Year Award to Professor Locator (URL): https://youtu.be/KBJCO6F4r2g
Sushil Jajodia of George Mason University. Mrs. Morris
Peer’s Choice Awards (selected by peers during
shared Mr. Jajodia’s contributions to the cybersecurity
the conference):
education industry by characterizing his contributions
in three ways: as an educationist, a researcher, and a
• Poster: K Rudolph, G. Mark Hardy, Niomi
thought leader. Professor Jajodia was presented with
Rosenberg, Andrew Ellis, John Ippolito, & Sam
a plaque as recognition of his achievements in the
Carter, Native Intelligence, Inc. and Friends
security community.
• Website: Valerie Hayward, InfoSight, Inc.
Other traditional FISSEA conference events
included announcing the winners of the FISSEA • Motivational Item: K Rudolph, Native
security contest. The FISSEA Security Awareness, Intelligence, Inc.
Training & Education Contest includes fve categories
• Newsletter: Kim Brumley, Margaret
from one of FISSEA’s three key areas of Awareness,
McDermott, Hiyan Sisson & Robert
Training, and Education. A winner is selected from each
Cunningham, Department of Veterans Afairs
category and awarded a certifcate. The categories
include: (1) an awareness poster; (2) an awareness
• Security Training Scenarios: K Rudolph,
website; (3) a motivational item (e.g., trinkets, pens,
Niomi Rosenberg & Sam Carter, Native
stress relief items and t-shirts); (4) an awareness
Intelligence, Inc. and Friends
newsletter; (5) an interactive scenario/exercise; and
(6) an awareness video • Video: TIE Rita John, John Creery, Chelsea
O’Hara, Nellie MacNeil, Kyle Bachan,
2017 FISSEA Awareness, Training, and Education
Tim Herman, Rosanne Trudel, & Sapna
Contest Winners
Kalhan, IFDS Canada and Cheryl Seaman &
Stephanie Erickson, The National Institutes of
Awarded Certifcates at the Conference (selected
Health
by an impartial judging committee prior to the
conference):
42
• Poster: K Rudolph, G. Mark Hardy, Niomi
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

FISSEA attendees have reported that social safeguard issues related to information security
interaction and networking at the conference are and privacy. The Board was originally created by
benefcial. The conference continues to be a valuable the Computer Security Act of 1987 (P.L. 100-235)
forum for individuals from government, industry, as the Computer System Security and Privacy
and academia who are involved with developing, Advisory Board (CSSPAB) within the Department of
maintaining, and/or supporting security programs. Commerce. The CSSPAB was chartered in May 1988 in
Attendees gain insights regarding information security accordance with the Federal Advisory Committee Act,
awareness, training, education, certifcation, and as amended. The 2002 FISMA legislation amended
professionalization. Attendees also learn of ongoing the statutory authority of the Board and provided its
and planned training and education programs and current name.
cybersecurity initiatives. The conference provides
The duties of the Board, as stipulated in FISMA,
NIST with the opportunity to provide assistance to
include:
departments and agencies as they work to meet their
FISMA responsibilities. The FISSEA website provides
• Identifcation of emerging managerial,
links to the conference program and presentations
technical, administrative, and physical
(seehttps://csrc.nist.gov/Projects/Federal-Info
safeguard issues relative to information
Systems-Security-Educators-Assoc.)
security and privacy;
The next conference will be held at NIST on March
• Advising NIST, DHS and the Director of the
14-15, 2018.
OMB on information security and privacy
issues pertaining to Federal Government
FOR MORE INFORMATION, SEE:
information systems (including the thorough
https://csrc.nist.gov/Projects/Federal-Info-Sys-
review of proposed standards and guidelines
tems-Security-Educators-Assoc
developed under 15 U.S.C. 278g-3 - Computer
Standards Program); and
CONTACTS:
Mr. Clarence Williams Ms. Rae’chell Finch • Annually reporting its fndings to the
(240) 672-8723 (202) 482-0935 Secretary of Commerce, the Director of the
clarence.williams@nist.gov raechell.fnch@nist.gov OMB, the Director of NSA, and the appropriate
committees of Congress.
Information Security and Privacy
Congress indicated the long-term need for the
Advisory Board (ISPAB)
Board by setting the term of Board members to four
years. The charter requires that the NIST Director
Since the inception of this Advisory Board in 1987,
appoint the Chairperson and all 12 members of the
the Information Security and Privacy Advisory Board
Board. They are selected for their preeminence in the
(ISPAB) has successfully renewed its charter with
information technology industry or related disciplines.
proper authority every two years. The Board plays a
central and unique role in providing the government The charter stipulates that Board members
with expert advice concerning information security be selected from three main categories, with each
and privacy issues that may afect federal information category providing four members. Category 1 includes
systems. Title III of the E-Government Act of 2002 members from outside the Federal Government who
reafrmed the need for this Board by giving it an are eminent in the information technology industry,
additional responsibility: to thoroughly review all at least one of whom is a representative of small
of the proposed information technology standards or medium-sized companies in such industries.
and guidelines developed under Section 20 of the Category 2 also includes members from outside the
National Institute of Standards and Technology Act Federal Government who are eminent in the feld
(15 U.S. Code (U.S.C.) 278g-3), as amended. of information technology or related disciplines,
but who are not employed by or representative of a
The ISPAB is a federal advisory committee with
43 producer of information. Category 3 includes those
specifc statutory objectives to identify emerging
from the Federal Government who are experienced
managerial, technical, administrative, and physical
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

in information system management, including those • Updates of other critical NIST publications.
with experience in information security and privacy,
In aligning with the work-plan focus areas, the
at least one of whom should be from the National
Board expanded its work to include the following:
Security Agency. The diversity of these categories
helps the Board to meet its statutory objectives.
• Acquisition, Supply Chain Security, and Open
Federal members bring a detailed understanding
Source trustworthy software;
of the federal processing environment; industry
brings concerns and experiences regarding product • Mobile Devices and the Protection of Sensitive
development and market formation, while private Information;
computer security experts are able to bring their
• Machine Learning and Artifcial Intelligence;
experiences of commercial cost-efective security
measures into Board discussions.
• The NIST Cybersecurity Framework;
Chris Boyer is currently the Chair of ISPAB. Mr.
• The Federal Information Security Management
Boyer, the Assistant Vice President for Global Public
Act (FISMA);
Policy at AT&T, joined the Board in 2012 and assumed
the responsibilities of the Chair in January 2016 (see • Emerging Technologies; and
list of Board members https://csrc.nist.gov/Projects/
ISPAB/Members). • The National Cybersecurity Center of
Excellence (NCCoE).
During FY 2017, ISPAB held three meetings, all in
Washington, D.C.: The presenters at each Board meeting were
leaders and experts representing private industry,
• June 28-30, 2017; academia, federal agency Chief Information Ofcers
(CIOs), Inspector Generals (IGs) and Chief Information
• March 29-31, 2017; and
Security Ofcers (CISOs).
• October 26-28, 2016.
Copies of the current list of members and their
In keeping with previous practices at the frst biographies, the Board’s charter and past Board
meeting of each fscal year, the Board established a activities are located at https://csrc.nist.gov/Projects/
work plan for FY 2017. The resulting plan included the ISPAB. Information on ISPAB meetings is published in
following areas of focus: Federal Register Notices at least 16 days prior to the
meeting. Those interested in receiving meeting notices
• Cryptography, and specifcally NIST R&D; and other notices relating to NIST work in information
security and privacy may email their name, afliation,
• Metrics – success measures for security and
and address to Matthew Scholl at the address below.
privacy;
FOR MORE INFORMATION, SEE:
• Trust in NIST (accountability and success);
https://csrc.nist.gov/Projects/ISPAB
• Quantum-resistant encryption;
CONTACT:
• Identity management;
Mr. Matthew Scholl
(301) 975-2941
• Privacy engineering;
matthew.scholl@nist.gov
• FISMA – Continuous Diagnostics and
Mitigation (CDM) and Federal Risk and Small and Medium Size Business
Authorization Management Program
(SMB) Cybersecurity Outreach
(FedRAMP);
Program
• High-Value Asset cybersecurity;
Small- and medium-sized businesses (SMBs)— 44
• Cybersecurity; and
representing approximately 95% of all businesses—
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

are the backbone of the U.S. economy. SMBs cannot FOR MORE INFORMATION, SEE:
always justify an extensive security program or even
https://www.nist.gov/programs-projects/small-busi-
full-time staf devoted to information security. Faced
ness-corner-sbc
with limited resources and budgets, SMBs need
practical solutions and training that enable them to CONTACTS:
cost-efectively address their cybersecurity risks. NIST
Email: smallbizsecurity@nist.gov
has partnered with other federal agencies and public-
Dr. Nelson Hastings Ms. Marian Merritt
private organizations to help address these needs.
(301) 975-5237 (240) 338-2033
During FY 2017, the Small Business Outreach nelson.hastings@nist.gov marian.merritt@nist.gov
Program accomplished the following:
Mr. Jef Marron Mr. Matthew Barrett
• Partnered with other federal agencies to (301) 975-3846 (301) 975-3267
catalog and evaluate existing cybersecurity jefrey.marron@nist.gov matthew.barrett@nist.gov
educational materials designed for SMB use;
• Collaborated with federal partners, led by the
Small Business Administration (SBA) and the
CRYPTOGRAPHIC STANDARDS
Department of Homeland Security (DHS),
on the development of the Small Business PROGRAM
Development Center Cyber Strategy;
• Reviewed available SMB training programs
Cryptographic Hash Algorithms
from federal partners and the National Cyber
Security Alliance (NCSA);
Cryptographic hash functions, which transform
• Evaluated existing NIST SMB-focused arbitrarily long input data into a fxed-length output,
educational materials such as reports, are a fundamental tool for information security, e.g.,
presentations, and online content; digital signatures, pseudorandom functions, and key
derivation.
• Updated the Small Business Corner website
to refect program updates and simplify SMB NIST has standardized two families of Secure
contact with NIST; Hash Algorithms (SHA): SHA-1 and SHA-2 in Federal
Information Processing Standard (FIPS) 180, and
• Initiated the development of the NIST
SHA-3 in FIPS 202.
strategic plan for small business outreach,
refecting requirements in new Congressional
The SHA-1 function—which was published in the
legislation; and
original version of FIPS 180 in 1995, and which is still
specifed along with the SHA-2 family in FIPS 180-4—
• Published Revision 1 of NISTIR 7621,
has been deprecated for many years, because it could
Small Business Information Security: The
no longer be relied upon to provide the important
Fundamentals. This publication presents
property of “collision resistance.” In fact, in 2017 a
cybersecurity fundamentals for SMBs in
SHA-1 collision (diferent inputs with the same output)
straightforward, non-technical language (see
was published by researchers at Centrum Wiskunde
https://www.nist.gov/publications/small-
& Informatica (CWI) Institute of Amsterdam and
business-information-security-fundamentals).
Google, based on the seminal cryptanalysis in 2005
In FY 2018, the Small Business Outreach Program by Xiaoyun Wang of Shandong University.
will continue to collaborate with federal and other
partners to understand the cybersecurity needs of Wang’s research was the main impetus to the
SMBs and identify and/or develop materials and development of SHA-3 through a public competition,
45 training to meet those needs. which NIST initiated in 2007. The winning algorithm,
KECCAK, was chosen in part because its components
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

could easily be adapted to provide a variety of Triple Data Encryption Algorithm
functionalities.
(TDEA)
FIPS 202 realized some of this potential by
SP 800-67: Recommendation for the Triple Data
including two eXtendable Output Functions (XOFs),
Encryption Algorithm (TDEA) Block Cipher:
which allow variable-length outputs, in addition to its
four hash functions. The two XOFs are called SHAKE128 The TDEA algorithm is specifed in SP 800-67
and SHAKE256; the numerical sufx indicates the Revision 1. This publication includes a specifcation of
supported security strength. FIPS 202 also supports the Data Encryption Algorithm (DEA) engine that was
a fexible scheme for “domain separation” between originally specifed in FIPS 46, The Data Encryption
diferent functions, which ensures that diferent Standard, in 1977 and was withdrawn as an approved
named functions will produce unrelated outputs. algorithm in 2005.
In December 2016, NIST further expanded the A security analysis and practical demonstration
uses of KECCAK with the publication SP 800-185, SHA- of attacks on TDEA in several real-world protocols
3 Derived Functions: cSHAKE, KMAC, TupleHash and was posted in FY 2017 by Karthikeyan Bhargavan
ParallelHash. It provides four new types of functions, and Gaëtan Leurent of Inria (Paris) and is available at
as indicated in the title, each with the same two https://sweet32.info/. This article provides evidence
supported security strengths: that the collision attack on TDEA represents a serious
security vulnerability for many common uses of
• cSHAKE128 and cSHAKE256 are XOFs that these protocols — including the Hyper Text Transfer
can be “customized” for individual users or Protocol Secure (HTTPS) protocol for secure Internet
applications, so that their outputs would be connections. Moreover, the analysis shows that the
unrelated to any other SHAKE variants; security vulnerability remains serious unless more
stringent limits are imposed on the amount of data
• KMAC128 and KMAC256 are keyed-hash
that can be encrypted under a single three-key bundle
functions with variable-length outputs, i.e.,
than the current data limit recommended by NIST in
pseudorandom functions (PRFs);
SP 800-67, Revision 1.
• TupleHash128 and TupleHash256 are hash
In response to this article, NIST posted a notice
functions on tuples of input strings; and
announcing plans to reduce the maximum amount
• ParallelHash128 and ParallelHash256 are hash of plaintext allowed to be encrypted under a single
functions that can exploit parallel processing TDEA three-key bundle from 232 to 220 (64-bit) blocks,
to efciently hash long messages. and to revise SP 800-67 accordingly. In addition, NIST
plans to disallow TDEA for TLS, IPsec and possibly
NIST is currently considering the development other protocols (see https://csrc.nist.gov/News/2017/
of a parallelizable hashing mode and XOF mode for Update-to-Current-Use-and-Deprecation-of-TDEA
generic hash functions (e.g., SHA-2). These modes for the announcement).
would allow the SHA-2 family to achieve some of the
functionality of the SHA-3 family. In late FY 2017, a revision of SP 800-67 was
provided for public comment that included the above
FOR MORE INFORMATION, SEE: restriction on the usage of TDEA for each three-key
https://csrc.nist.gov/projects/hash-functions/ TDEA key bundle. SP 800-67 Rev 2 will be published
sha-3-standardization in early FY 2018.
CONTACT: CONTACT:
Dr. Morrie Dworkin Ms. Elaine Barker
(301) 975-2354 (301) 975-2911
morris.dworkin@nist.gov elaine.barker@nist.gov
46
(Editors’ Note: Ms. Shu-jen Chang supported this
program until her recent retirement)
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

Random Bit Generation  In Figure 13, the noise source contains the entropy-
providing activity (e.g., the output of ring oscillators);
Random  bits are required for the secure use  if the activity being sampled does not produce binary
| of  most  | cryptographic  |     | algorithms.  |     | For  example,  |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
data, then the noise source includes a digitization
random bits are used to generate the keys needed  process. Health tests are intended to detect whether
for  encryption  and  digital  signature  applications.  the noise source and the entropy source (as a whole)
| CSD  began  | work  | on  | the  | specifcation  | of  random  |            |     |          |     |            |      |           |
| ----------- | ----- | --- | ---- | ------------- | ----------- | ---------- | --- | -------- | --- | ---------- | ---- | --------- |
|             |       |     |      |               |             | continues  | to  | operate  | as  | expected.  | The  | optional  |
bit generators in the late 1990s. Information on the  conditioning component is responsible for reducing
Random Bit Generation project is available at https://  bias and/or increasing the entropy rate of the bits to
csrc.nist.gov/projects/random-bit-generation.  eventually be output by the entropy source.
This  project  consists  of  the  development  of  SP 800-90B includes descriptions of the tests for
three NIST Special Publications (SPs). SP 800-90A,   NIST’s Cryptographic Algorithm Validation Program
| Recommendation  |     | for  | Random  | Number  | Generation  |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
(CAVP) and Cryptographic Module Validation Program
Using  Deterministic  Random  Bit  Generators,  was  (CMVP) to validate candidate entropy sources. During
initially published in 2007 and last revised in 2015. It  FY 2017, CSD fnalized the test descriptions for the
specifes  several  deterministic  algorithms  that  can  initial publication of SP 800-90B, which is expected
be used for the generation of pseudorandom bits –
to be published in early FY 2018. CSD will begin a
a sequence of bits produced by an algorithm, rather  revision of the document in FY 2018 to address issues
than a random physical phenomenon that produces a  that were not included in the initial version of the
truly random sequence. Two additional documents (SP
document and any lessons learned during validation
800-90B and SP 800-90C) are under development,  testing by the CAVP and CMVP labs.
and the latest drafts were made available for public
comment in 2016 via the Special Publications page:  The initial version of SP 800-90B will be available
https://csrc.nist.gov/publications/PubsSPs.html.  via  the  Special  Publications  page:  https://csrc.nist.
gov/publications/PubsSPs.html.
| SP  | 800-90B,  |     | Recommendation  |     | for  the  |     |     |     |     |     |     |     |
| --- | --------- | --- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Entropy Sources Used for Random Bit Generation,  In May 2017, a presentation “A Tale of Two Entropy
|     |     |     |     |     |     | Source  | Validation  | Approaches:  |     | NIST  | 800  | 90B  vs.  |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | ------------ | --- | ----- | ---- | --------- |
addresses the development and testing of entropy
BSI AIS 31” was provided by Meltem Sönmez Turan
| sources.  | Figure  | 13  illustrates  |     | the  | model  that  the  |     |     |     |     |     |     |     |
| --------- | ------- | ---------------- | --- | ---- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Recommendation uses to describe an entropy source  at  the  ICMC17  International  Cryptographic  Module
and its components: a noise source, health tests, and  Conference held in Washington D.C.
an optional conditioning component.
|     |     |     |     |     |     | SP               | 800-90C,  |         | Recommendation     |                 | for      | Random    |
| --- | --- | --- | --- | --- | --- | ---------------- | --------- | ------- | ------------------ | --------------- | -------- | --------- |
|     |     |     |     |     |     | Bit  Generator   |           | (RBG)   |                    | Constructions,  |          | provides  |
|     |     |     |     |     |     | basic  guidance  |           | on      | the  construction  |                 | of       | Random    |
|     |     |     |     |     |     | Bit  Generators  |           | (RBGs)  | from               | the             | entropy  | sources   |
validated against the requirements of SP 800-90B
and the Deterministic Random Bit Generators (DRBG)
Digital Noise  algorithms  of  SP  800-90A.  SP  800-90C  includes
c__ ____  ---1------------"  Source  constructions  for  both  non-deterministic  random
--------------------1
Health Tests  bit generators (NRBGs; also known as true random
Raw data
|     |     |     |     |     |     | number  | generators)  |     | and  deterministic  |     |     | random  bit  |
| --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------------------- | --- | --- | ------------ |
generators (DRBGs; also known as pseudorandom
(optional)
Conditioning  number generators). Two general models are provided
in SP 800-90C, as shown in Figure 14 and Figure 15.
Entropy Source
|     |     | Output  |     |     | Error message  |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |

47
Figure 13: Entropy Source Model
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

last public comment period, along with their
DRBG resolutions. The testing of entropy sources
Algorithm
by the CAVP and CMVP will begin as soon as
possible after publication.
RBG Output
• Monitor the testing of SP 800-90B in the
CAVP and CMVP labs to determine problems
Figure 14: XOR-NRBG that need to be addressed in the next
version of SP 800-90B. In some cases, the
Figure 14 depicts the construction of one of the problems may be addressed by additions
NRBGs – the XOR-NRBG. In this construction, each to the FIPS 140-2 Implementation Guidance
bit output by the entropy source (as discussed in SP document until SP 800-90B is revised. The
800-90B) is exclusive-ORed with a bit of output from Implementation Guidance document is
a DRBG algorithm specifed in SP 800-90A. available at https://csrc.nist.gov/groups/STM/
cmvp/documents/fps140-2/FIPS1402IG.pdf.
• Begin a revision of SP 800-90B to address
issues not included in the initial version of SP
Entropy RBG
800-90B, as well as any issues that surface
Source Input output
during CAVP and CMVP entropy source
validation.
• Finalize and publish 800-90C, posting the
Figure 15: DRBG and Oversampling NRBG
comments received and their resolution, along
with the document.
Figure 15 depicts the construction used for
the DRBGs and the second NRBG design – the
• Complete plans for testing SP 800-90C.
Oversampling NRBG. In this construction. the entropy
source repeatedly provides input to the DRBG FOR MORE INFORMATION, SEE:
algorithm to produce the requested output.
https://csrc.nist.gov/projects/random-bit-generation
The diference between DRBGs and NRBGs is the
CONTACTS:
availability of the entropy source and the frequency
Ms. Elaine Barker Mr. John Kelsey
of requesting output from the entropy source. For a
(301) 975-2911 (301) 975-5101
DRBG, an entropy source is only required for seeding
the DRBG; after the initial seeding process, further elaine.barker@nist.gov john.kelsey@nist.gov
requests for entropy-source output depend on the
implementation and application. For the Oversampling Dr. Meltem Sönmez Turan Dr. Kerry McKay
NRBG, the entropy source must always be available (301) 975-4391 (301) 975-4969
and is accessed whenever bits are requested from the meltem.turan@nist.gov kerry.mckay@nist.gov
NRBG by a consuming application.
The NIST Randomness Beacon
The latest draft of SP 800-90C is available via
the Special Publications page: https://csrc.nist.gov/
NIST has implemented a source of public
publications/PubsSPs.html.
randomness, which is available at https://beacon.nist.
gov/home. It uses two independent, commercially
Plans for FY 2018:
available sources of randomness, each with an
The RBG development team has the following independent hardware entropy source and SP
goals for FY 2018: 800-90A-approved components.
• Publish the initial version of SP 800-90B The NIST Beacon is designed to provide
48
and post the comments received during the unpredictability, autonomy, and consistency.
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

Unpredictability means that users cannot The project team has also made progress in
algorithmically predict bits before they are made helping other institutions set up interoperable sources.
available by the source. Autonomy means that the This is important because multiple sources can be
source is resistant to attempts by outside parties to combined in such a way that all sources would have
alter the distribution of the random bits. Consistency to be compromised in order to degrade the common
means that a set of users can access the source in random strings. It is expected that the University
such a way that they are confdent of receiving the of Chile will start operating their own randomness
same random string. beacon during FY 2018.
The NIST Beacon posts bit-strings in blocks of As of the end of FY 2017, the NIST Beacon has
512 bits every 60 seconds. Each such value is time- been functioning without major interruptions for more
stamped and signed to form a packet that also includes than four years. During this time, the project team has
the hash of the previous value to chain the sequence received valuable input from a growing community
of values together. This prevents all parties, even the of users. As a result, the project team has redesigned
source, from retroactively changing an output packet the Application Programming Interface (API) and the
without being detected. The NIST Beacon keeps all architecture. The changes provide higher security and
output packets. At any point in time, the full history of availability, as well as better interoperability. Version
outputs is available to users. 2.0 of the NIST Beacon is scheduled to be deployed
during November 2017.
Tables of random numbers have probably
been used for multiple purposes at least since the NIST encourages the community of users to
Industrial Revolution. In the digital age, algorithmic research and publish novel ways in which this tool can
pseudorandom number generators (PRNGs) have be used.
largely replaced these tables. The NIST Beacon
FOR MORE INFORMATION, SEE:
expands the use of randomness to multiple scenarios
in which neither tables nor PRNGs can be used. The https://www.nist.gov/programs-projects/nist-
extra functionalities stem mainly from three features. randomness-beacon
First, the Beacon-generated numbers cannot be
CONTACT:
predicted before they are published. Second, the
public, time-bound, and authenticated nature of the Dr. René Peralta
(301) 975-8702
Beacon allows a user application to prove to anybody
rene.peralta@nist.gov
that it used truly random numbers not known before a
certain point in time. Third, this proof can be presented
ofine and at any point in the future. Entropy as a Service (EaaS)
Although commercially available physical sources The security of cryptography today depends
of randomness are adequate as entropy sources for on having strong keys and keeping them secret.
currently envisioned implementations of the NIST The ability to generate strong cryptographic keys
Beacon, the NIST Randomness Beacon project team is is directly related to having access to unpredictable
working on developing a source of verifably random random data, but generating truly unpredictable
sequences. In collaboration with NIST physicists random data on common computing devices is hard
from the Physical Measurement Laboratory (PML), and unreliable. As a result, weak keys are widely used
the project team aims to use quantum non-locality in cryptographic applications, thus compromising the
to build an entropy source whose unpredictability security of the sensitive data protected by them -
is guaranteed by the laws of physics. In FY 2016, potentially with disastrous consequences.
a major milestone was achieved, namely, a strong
A primary goal of this project is to provide
loophole-free test of local realism (where individual
high quality, truly unpredictable random data to
particles are governed by elements of reality, even
devices on the Internet to enable them to generate
if these elements are hidden) (see https://www.nist.
strong cryptographic keys and attest the strength
49 gov/news-events/news/2015/11/nist-team-proves-
of the keys used to protect data in transit or at rest,
spooky-action-distance-really-real).
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

thereby enabling cryptographic system strength source. The EaaS server ensures that the FIFO bufer
attestation. Achieving this goal would provide a is erased prior to server shutdown and never copied
solid basis for achieving the goals of the Automated to disk. Open implementations can help ensure that
Cryptographic Validation Testing project (see https:// this occurs.
csrc.nist.gov/projects/acvt) as well as addressing the
The client system consists of a classic computing
problems targeted by the Cryptographic Programs
device enabled with a dedicated hardware
and Laboratory Accreditation (see the next section:
component capable of storing secret cryptographic
Validated Programs), where entropy estimation
keys and seeds. A dedicated software application
has persisted as one of the most difcult and labor-
bridges the communication between EaaS and the
consuming activities, causing problems for all parties
hardware component. Examples of secure hardware
involved: the industry, the testing laboratories and the
components are the Trusted Platform Module
government validators.
(TPM), TrustZone technology in Advanced Reduced
Random data obtained from sources of true Instruction Set Computing (RISC) Machine (ARM)
randomness that are based on unpredictable physical processors, and Identity Protection Technology in
phenomena, such as quantum efects, is much Intel processors. Recently, an alternative innovative
better suited for cryptographic applications. CSD is technology has emerged that allows extracting
collaborating with the NIST Physical Measurement unique cryptographic keys from the imperfections of
Laboratory (PML) to build a quantum source. The memory Static Random Access Memory (SRAM) cells
aim is to use quantum efects to generate sequences used in common computers. The idea behind this
that are guaranteed to be unpredictable, even technology is to extract PUF-like unique data from the
if an attacker has access to the random source. SRAM chip, which is then used to construct a unique
(For more information on this collaboration, see key. This technology is quite interesting for EaaS
https://www.nist.gov/pml/div684/random_ applications on the client side because it eliminates
numbers_bell_test.cfm). the need to provision an initial key for accessing
EaaS. If a client system or device does not have a
This EaaS project aims to develop a system and
secure hardware component, it can still use EaaS. The
protocols for obtaining random data with high entropy
presence of a hardware component simply provides
from one or more remote sources. The high-level
further guarantees to the system or device user, when
architecture is shown in Figure 16. The architecture
present.
of the Entropy-as-a-Service system consists of two
main parts: the client-side and the server-side. The EaaS uses the Hyper Text Transfer Protocol (HTTP)
critical components of the system are the quantum to transfer entropy payloads from the server to clients.
device, the EaaS server and a secure device in the To secure this transmission, the server encrypts the
client systems that is capable of providing strong data using the client’s public key and digitally signs
isolation and protection for the cryptographic keys the payload with the server’s own private key.
stored inside the device and ofering a set of basic
Client devices mix this data with locally available
cryptographic services.
random data to seed random number generators to
The EaaS server is continuously fed random data generate strong cryptographic keys and other random
from the attached quantum source. The data enters values independently from the remote sources.
a frst in, frst out (FIFO)-like bufer in the server’s
Random Access Memory (RAM), and, when a client
request arrives, the server reads the top value from
the bufer, signs and encrypts it, and then sends it
to the requester. The FIFO bufer shifts after every
request and when new data comes from the random
50
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

NIST NIST
Quantum
/ device
R/•d=
HashlHSM~
Quantum~1
EaaS server
/ ERROR: Halt
Requester's
network public key
capability, proxy
i.e. device Q.!1t he r
loT
/r -
R(s.,!
,,. H/W Root of Trust
chip; Continuous
TrueRBG
BEST,i f available, to health
hold a provisioned monitor
key pair. (SP 800-90B
it:ed  tests)
HHh[EaiiS:a..,. ., Otherwise, a
EaaS,111 local];
protected memory/
Key;;;
ORBG(,eed) file location may be
used
NOTE: EaaS1, ••• , EaaS, above indicate data from n
different EaaS server instances;
local Indicates locally available random data, If any
Figure 16: High-level Architecture of EaaS
With the conceptual system architecture and against integrated circuit counterfeiting and thereby
protocols defned, the project team continues help secure a supply chain. The University of Florida
to engage with industry and academia to obtain researchers working on this grant obtained interesting
feedback on the approach and identify possibilities security results that identifed security vulnerabilities
for collaborative approaches to solving important in widely used protocols for intellectual property
cybersecurity challenges in the domains of protection in integrated circuit manufacturing and
cryptography and supply-chain management (e.g., resulted in proposals for new secure protocols that
integrated circuit counterfeiting). A published paper eliminated these vulnerabilities.
on EaaS in IEEE Computer magazine generated a lot
The team continues to develop the system to
of interest among the public, including companies
provide a publicly accessible NIST EaaS instance
from the U.S. and Canada who approached the team
in FY 2018. The team succeeded in establishing a
and asked for assistance in implementing and hosting
non-disclosure agreement and a collaboration with
their own EaaS servers. The team started a technology
Intrinsic ID, Inc. – a company with complementing
transfer efort to help with this. The team also continues
technology for constructing the initial key on the
the collaboration with a team of researchers at the
client side by extracting it from SRAM memory cells.
University of Florida who work under a NIST research
The team also established a collaborative relationship
51 grant to explore ways to leverage EaaS in protecting
with Crypto4A and 2Keys Corp. from Canada on
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

developing a common protocol for EaaS. The team  uniqueness of the “nonce” input; CSD plans to seek
coordinated with the research team working on the  public comment on how to best update the guidance
NIST  Beacon  for  developing  common  back-end  for achieving this property.
components for the two services. The team plans to
FOR MORE INFORMATION, SEE:
leverage these common components in the NIST EaaS
implementation.  https://csrc.nist.gov/projects/block-cipher-
techniques
CONTACT:
CONTACT:
Dr. Apostol Vassilev
| (301) 975-3221             |     |     |     |     |     | Dr. Morris Dworkin   |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
| apostol.vassilev@nist.gov  |     |     |     |     |     | (301) 975-2354       |     |     |     |     |     |     |
morris.dworkin@nist.gov
Block Cipher Modes of Operation
Key Management
The engine for many of the techniques in CSD’s
cryptographic  toolkit  is  a  block  cipher  algorithm,  Key  management  is  required  for  applying
such as the Advanced Encryption Standard (AES)  numerous  cryptographic  technologies  and  is
algorithm.  A  block  cipher  transforms  some  fxed- considered one of the most critical aspects associated
length  binary  data  (i.e.,  a  “block”  of  data)  into  with  the  use  of  cryptography.  The  CSD  began
seemingly  random  data  of  the  same  length.  The  providing guidance in managing the keys used for
transformation is determined by the choice of some  cryptographic applications in the late 1990s to early
secret data called the “key.” The same key is used to  2000s. Information on the CSD’s key management
project is available at https://csrc.nist.gov/projects/
reverse the transformation and recover the original
block of data. A cryptographic technique (e.g., for  key-management.
encryption and/or authentication) that is constructed
|     |     |     |     |     |     | SP  | 800-56A,  | Recommendation  |     |     | for  | Pair- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | --- | --- | ---- | ----- |
from a block cipher is called a “mode of operation.”
|     |     |     |     |     |     | Wise  Key  | Establishment  |     | Schemes  | Using  |     | Discrete  |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | -------- | ------ | --- | --------- |
Several modes of operation have been specifed  Logarithm Cryptography:
in the SP 800-38 series of publications. The latest
In FY 2017, SP 800-56A was revised. SP 800-
| installment           | in  the  series,  | Special     | Publication  |        | 800- |           |             |            |     |            |      |      |
| --------------------- | ----------------- | ----------- | ------------ | ------ | ---- | --------- | ----------- | ---------- | --- | ---------- | ---- | ---- |
|                       |                   |             |              |        |      | 56A  was  | originally  | published  |     | in  2006,  | and  | was  |
| 38G,  Recommendation  |                   | for  Block  | Cipher       | Modes  | of   |           |             |            |     |            |      |      |
previously revised in 2007 and 2013. This document
Operation: Methods for Format-Preserving Encryption,
|     |     |     |     |     |     | specifes  | Dife-Hellman  |     | (DH)  | and  | Menezes-Qu- |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ----- | ---- | ----------- | --- |
was published in 2016. It specifes two AES modes of
|     |     |     |     |     |     | Vanstone  | (MQV)  | key-agreement  |     | schemes,  |     | both  |
| --- | --- | --- | --- | --- | --- | --------- | ------ | -------------- | --- | --------- | --- | ----- |
operation, called FF1 and FF3, for “format-preserving
elliptic curve and fnite feld versions. Key agreement
| encryption”  | (FPE),  | based  on  | proposals  | that  | were  |     |     |     |     |     |     |     |
| ------------ | ------- | ---------- | ---------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
results in keying material that is shared between the
submitted from the private sector, specifcally, the
participants. A key-agreement scheme is a procedure
payments industry.
|     |     |     |     |     |     | in  which  | both  parties  |     | contribute  | information  |     | that  |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ----------- | ------------ | --- | ----- |
Recently,  two  academic  researchers,  Vaudenay  is used in generating a cryptographic key. A key-
|              |            |                   |     |         |     | agreement  | scheme  | is  | defned  | by  a  | cryptographic  |     |
| ------------ | ---------- | ----------------- | --- | ------- | --- | ---------- | ------- | --- | ------- | ------ | -------------- | --- |
| and  Dürak,  | developed  | a  cryptanalytic  |     | attack  | on  |            |         |     |         |        |                |     |
the  FF3  mode.  On  April  12,  2017,  CSD  posted  an  algorithm, together with other information that must
announcement  that  summarizes  the  attack  and  be available by both parties when establishing keys.
outlines CSD’s plans to revise FF3 in a new draft of  The schemes are intended for use in communication
SP  800-38G  in  FY  2018;  see   protocols (e.g., Transport Layer Security (TLS), one
|     |     |     |   https://csrc.nist.gov/  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
News/2017/Recent-Cryptanalysis-of-FF3.  of  the  protocols  used  by  the  Internet).  The  key-
|     |     |     |     |     |     | establishment  | schemes  |     | in  SP  | 800-56A  | use  | public  |
| --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ------- | -------- | ---- | ------- |
In FY 2018, CSD also plans to revisit SP 800-38D,  key  algorithms,  and  each  participant  in  a  key-
which specifes the Galois/Counter Mode (GCM) for
agreement transaction uses a pair of keys—a public
authenticated encryption. In particular, the security
key and a private key. The key-agreement process
of GCM depends critically on the requirement for the  includes the generation of a shared secret (which is  52
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

not itself considered to be a cryptographic key), and • Added the KECCAK Message Authentication
the derivation of keying material using the shared Code (KMAC) to the list of approved MAC
secret. Several key-agreement schemes are specifed functions; KMAC is specifed in SP 800-185,
in SP 800-56A. Figure 17 below provides a simplifed SHA-3 Derived Functions: cSHAKE, KMAC,
example of one of the key-agreement schemes. In this TupleHash and ParallelHash.
example, each party:
• The elliptic curves to be used in the elliptic
1. Generates a key pair (either prior to or curve Dife-Hellman and MQV schemes will
during the key-agreement transaction); henceforward be specifed in SP 800-186, a
new publication under development that will
2. Obtains the public key of the other party;
include the elliptic curves currently specifed
in FIPS 186-4, Digital Signature Standard
3. Computes a shared secret using one’s own
(DSS), along with additional approved
keys and the other party’s public key; and
elliptic curves for key agreement and digital
4. Derives one or more keys from the shared signatures.
secret.
• The key-derivation functions were moved
A revision of SP 800-56A was provided for public to SP 800-56C: Recommendation for
comment in FY 2017 as a draft of SP 800-56A Rev. 3. Key-Derivation Methods in Key-Derivation
This revision includes the following changes: Schemes (see below).
Party A (Communications) Party B
1 :~
Generate ·- Generate
Key Pair Exchange Public Keys -· Key Pair
~-
l l
' ,
Compute Shared Secret Compute Shared Secret
! !
Derive Key(s) . Derive Key(s)
Figure 17: Key-Agreement Example
• Encourages the use of pre-defned domain A more complete list of changes is provided in an
parameter groups for the fnite feld Dife- appendix of SP 800-56A Rev. 3. SP 800-56A Rev. 3
Hellman and MQV schemes. Domain will be published in early FY 2018 and will be available
parameters are used to generate keys and via the CSD publications page at https://csrc.nist.
compute the shared secret. The domain- gov/publications. This web page may also be used to
parameter groups include the “safe primes” access FIPS 186-4, SP 800-185, and (eventually) SP
that are used in the Transport Layer Security 800-186.
(TLS) and Internet Key Exchange (IKE)
protocols.
53
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

Information about SP 800-56A is also available at will be published in early FY 2018 and will be available
https://csrc.nist.gov/publications/detail/sp/800-56a/ via the CSD publications page at https://csrc.nist.gov/
rev-3/draft. publications. SP 800-135 and SP 800-185 are also
available using that address.
SP 800-56C: Recommendation for Key-
Derivation Methods in Key-Establishment Information on SP 800-56C is also available at
Schemes: https://csrc.nist.gov/publications/detail/sp/800-56c/
rev-1/draft.
SP 800-56C specifes techniques for the derivation
of keys from a shared secret generated during a key- New Key Management Publications Under
establishment scheme defned in SP 800-56A and SP Development:
800-56B. SP 800-56A is discussed above. SP 800-
A new document was started in FY 2016 on key
56B: Recommendation for Pairwise Key-Establishment
storage and recovery by an organization (e.g., key
Schemes Using Integer Factorization Cryptography, is
backup and archiving). This document is intended
available via https://csrc.nist.gov/publications.
to serve as a guideline for the storage and recovery
SP 800-56C had included only one method of cryptographic keys that are not under the direct
for key derivation - a two-step key-derivation control of the entity using those keys (e.g., the owner).
procedure that used either the Keyed-Hash Message This includes the backup and archiving of copies of
Authentication Code (HMAC) or the Cipher-based the keys and the metadata associated with them. The
Message Authentication Code (CMAC) algorithm document will also discuss the recovery of those keys
during the process. HMAC is specifed in FIPS 198- when required (e.g., by the key’s owner or the owner’s
1: The Keyed-Hash Message Authentication Code organization).
(HMAC), and CMAC is specifed for AES in SP 800-
Plans for FY 2018:
38B: Recommendation for Block Cipher Modes of
Operation: the CMAC Mode of Authentication. These
During FY 2018, the CSD is expecting to accomplish
documents are available via https://csrc.nist.gov/
the following key management tasks:
publications.
• Publish the revisions of SP 800-56A and SP
A revision of SP 800-56C was provided for public
800-56C.
comment in FY 2017 as a draft of SP 800-56C Rev. 1.
This revision includes the following changes: • Begin the revision of SP 800-56B and post it
for public comment.
• The single-step key derivation functions
specifed in SP 800-56A and SP 800-56B • Begin revisions of SP 800-131A, Transitions:
were moved into SP 800-56C, as well as the Recommendation for Transitioning the Use of
references to SP 800-135: Recommendation Cryptographic Algorithms and Key Lengths,
for Existing Application-Specifc Key to address the use of Triple Data Encryption
Derivation Functions. Note that the relevant Algorithm (TDEA), SP 800-56A, SP 800-56B,
changes to SP 800-56B (i.e., to remove the KMAC and other SHA-3 derived functions
key derivation functions from the document) specifed in SP 800-185. A statement about
have not been performed yet; those changes the advent of quantum-resistant algorithms
will be initiated in FY 2018 (see below). will also be included.
• KMAC, as specifed in Draft SP 800-185, SHA-3 • Begin revisions of SP 800-57, Part 2,
Derived Functions: cSHAKE, KECCAK Message Recommendation for Key Management,
Authentication Code (KMAC), TupleHash and Part 2: Best Practices for Key Management
ParallelHash, is allowed for the single-step key Organization, to update the guidance.
derivation functions.
• Revise SP 800-57, Part 3, Recommendation for
Changes to the document are discussed in an Key Management, Part 3: Application-Specifc
54
appendix of SP 800-56C Rev. 1. SP 800-56A Rev. 3 Key Management Guidance, to provide revised
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

guidance on the use of the Internet Protocol CSD has been contributing to the development
Security (IPsec) protocol. of testssl.sh (see https://github.com/drwetter/testssl.
sh), an open-source program that tests TLS-enabled
• Continue the development of the
servers, providing information about the protocols
organizational key-storage and recovery
and cipher suites supported, in addition to checking
publication.
for some well-known faws. In FY 2018, CSD will be
contributing code to testssl.sh that adds support for
• Resume work on SP 800-71, Recommendation
TLS version 1.3. When the draft of SP 800-52 Revision
for Key Establishment Using Symmetric Block
2 is posted for public comment, CSD intends to make a
Ciphers.
draft version of this code available that includes some
FOR MORE INFORMATION, SEE: checks for conformance to SP 800-52 Revision 2.
https://csrc.nist.gov/projects/key-management/
CONTACTS:
cryptographic-key-management-systems
Dr. Kerry McKay Dr. David Cooper
CONTACTS: (301) 975-4969 (301) 975-3194
kerry.mckay@nist.gov david.cooper@nist.gov
Ms. Elaine Barker Mr. Quynh Dang
(301) 975-2911 (301) 975-3610
elaine.barker@nist.gov quynh.dang@nist.gov Cryptographic Recommendations for
the Internet Protocol Security (IPsec)
Dr. Lily Chen Dr. Allen Roginsky
(301) 975-6974 (301) 975-8136 and Internet Key Exchange (IKE)
lily.chen@nist.gov allen.roginsky@nist.gov
IPsec is a suite of protocols for securing Internet
communications at the network layer and operates
Transport Layer Security
within the Internet Protocol (IP). It is frequently used
to establish Virtual Private Networks (VPNs), requiring
SP 800-52 Guidelines for the Selection,
both parties to share keying material, which can be
Confguration, and Use of Transport Layer Security
established using the Internet Key Exchange (IKE)
(TLS) Implementations, provides recommendations
protocol, and enabling telecommuters or travelers to
regarding TLS server and client implementations.
gain secure access to their enterprise networks. IPsec
TLS is a widely used cryptographic protocol that
provides the cryptographic security functions for both
provides communication security for a variety of
versions of the Internet Protocol, IPv4 and IPv6.
network applications, such as email, e-commerce, and
healthcare. CSD has provided cryptographic guidance for
using IPsec and IKE in SP 800-57 part 3, Section 3:
SP 800-52 was frst published in June of 2005,
Internet Protocol Security (IPsec). From the beginning
and SP 800-52 Revision 1 was published in 2014.
of FY 2017, CSD has been working on a revision of
Since the frst revision, CSD has been following
the section and plans to publish it as a standalone
developments in TLS implementations, including
Special Publication. This SP will update and expand
updates and attacks. In FY 2016, a second revision
the existing cryptographic guidelines. The important
was initiated that updates TLS recommendations to
technical updates include disallowing Triple DES and
include mitigations for recent attacks, synchronizes
recommending AES-GCM authenticated encryption
cryptographic algorithm recommendations with
instead of the CipherBlock Chaining (CBC) mode.
other NIST Special Publications, and provides more
fexibility to system administrators in choosing which CSD expects to release the draft SP in FY 2018 for
TLS features they should support. There is also public comments. The SP will be harmonized with an
guidance for implementations of TLS version 1.3, a upcoming revision of SP 800-77, Guide to IPsec VPNs.
signifcant update to TLS. SP 800-52 Revision 2 will
be posted for public review and comment in FY 2018.
55
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

CONTACTS: signature schemes will be included in FIPS 186. It is
expected that the revised draft version of FIPS 186-5
Ms. Elaine Barker Mr. Quynh Dang
(and SP 800-186) will be available for public comment
(301) 975-2911 (301) 975-3610
in early FY 2018.
elaine.barker@nist.gov quynh.dang@nist.gov
CONTACTS:
Elliptic Curve Cryptography
Email project team: EllipticCurves@nist.gov
Elliptic curve cryptography is critical to the
Dr. Dustin Moody Dr. Lily Chen
adoption of strong cryptography during the
(301) 975-8136 (301) 975-6974
migration to higher security strengths. One of the
dustin.moody@nist.gov lily.chen@nist.gov
main advantages of elliptic curve cryptography is that
users can achieve the same level of security as other
Mr. Andrew Regenscheid
systems, but with a much shorter key length. NIST has
(301) 975-5155
standardized elliptic curve cryptography for digital
andrew.regenscheid@nist.gov
signature algorithms in FIPS 186: Digital Signature
Standard (DSS), and for key establishment schemes
in SP 800-56A: Recommendation for Pair-Wise Key Post-Quantum Cryptography
Establishment Schemes Using Discrete Logarithm
Cryptography. In recent years, there has been a substantial
amount of research on quantum computers – machines
In FIPS 186-4, NIST recommends 15 elliptic
that exploit quantum mechanical phenomena to
curves of varying security strengths for use in these
solve problems that are difcult or intractable for
elliptic curve cryptographic standards. However, the
conventional computers. If large-scale quantum
provenance of the curves is not fully specifed in the
computers are ever built, they will be able to break
standard, leading to recent public concerns that there
the existing infrastructure of public-key cryptography
could be a hidden weakness in these curves. NIST is
(see Table 1). The focus of the Post-Quantum
not aware of any vulnerability in these curves when
Cryptography (PQC) project is to identify candidate
they are implemented correctly and used as described
quantum-resistant systems that are secure against
in NIST standards and guidelines.
both quantum and classical computers—as well as the
impact that such post-quantum algorithms will have
More than 15 years have now passed since these
on current protocols and security infrastructures.
curves were developed, and the community now
knows more about the security of elliptic curve
NIST researchers have held regular seminars
cryptography and practical implementation issues. throughout FY 2017. The presentation topics included
Advances within the cryptographic community have the latest published results and security analyses, as
led to the development of new elliptic curves and well as status reports on quantum computation, hash-
algorithms whose designers claim to ofer better based signatures, coding-based cryptography, lattice-
performance and are easier to implement in a secure based cryptography, and multivariate cryptography.
manner. Some of these curves are under consideration Through these presentations and discussions, the
in voluntary, consensus-based Standards Developing project team has made signifcant progress in
Organizations. understanding the strengths and weaknesses of the
existing cryptographic schemes in each category.
In FY 2017, NIST utilized feedback received to revise
and improve FIPS 186-4. In particular, NIST plans to The NIST team also continues to be productive
add new elliptic curves to the current recommended in post-quantum cryptography research. The results
set. The entire collection of recommended curves and have been published at major conferences, such as
their specifcation will be moved to a new publication Real World Cryptography, Number Theory Methods in
SP 800-186: Recommendations for Discrete- Cryptography, Selected Areas in Cryptography, Post-
Logarithm Based Cryptography: Elliptic Curve Domain Quantum Cryptography (PQCrypto), and AsiaCrypt.
Parameters. In addition, new deterministic digital NIST researchers have given many presentations at 56
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

TABLE 1: IMPACT OF QUANTUM COMPUTING ON COMMON
CRYPTOGRAPHIC ALGORITHMS
IMPACT FROM
CRYPTOGRAPHIC
|     |     |     |     | TYPE  |     |     | PURPOSE  |     | LARGE-SCALE  |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | -------- | --- | ------------ | --- | --- | --- |
ALGORITHM
QUANTUM COMPUTER
AES  Symmetric key  Encryption  Larger key sizes likely needed
SHA-2, SHA-3  --------------- Hash functions  Larger output likely needed
Signatures, key
| RSA  |     |     | Public Key  |     |     |     |     | No longer secure  |     |     |     |     |
| ---- | --- | --- | ----------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
establishment
ECDSA, ECDH
Signatures, key
| (Elliptic Curve       |     |     | Public key  |     |     |     |     | No longer secure  |     |     |     |     |
| --------------------- | --- | --- | ----------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
exchange
Cryptography)
DSA, DH
Signatures, key
| (Finite Field           |     |     | Public key  |     |     |     |     | No longer secure  |     |     |     |     |
| ----------------------- | --- | --- | ----------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
exchange
Cryptography)
venues,  such  as  the  European  Telecommunication  received several proposals, and the fnal submission
Standardisation  Institute  (ETSI)  Quantum-Safe  deadline is in November 2017.
Workshop, to increase awareness of the upcoming
|            |                     |     |     |                |            |          | In  FY  2018,  | NIST         | will  continue  | to         | explore  | the  |
| ---------- | ------------------- | --- | --- | -------------- | ---------- | -------- | -------------- | ------------ | --------------- | ---------- | -------- | ---- |
| migration  | to  post-quantum    |     |     | cryptography,  |            | and  to  |                |              |                 |            |          |      |
|            |                     |     |     |                |            |          | security  and  | feasibility  | of              | purported  | quantum- |      |
| engage     | with  stakeholders  |     | in  | the            | U.S.  and  | other    |                |              |                 |            |          |      |
resistant technologies submitted to the Post-Quantum
countries. NIST has also sponsored other research,
|     |     |     |     |     |     |     | Standardization  | Process.  | NIST  | will  hold  | a   | public  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --------- | ----- | ----------- | --- | ------- |
education, and research events.
workshop in April 2018, co-located with the PQCrypto
In  2016,  NIST  published  NISTIR  8105:  Report  conference in Florida, during which submitters will be
on Post-Quantum Cryptography, which shared the  invited to present their algorithms. The Post-Quantum
team’s  current  understanding  about  the  status  of  Standardization Process will proceed with multiple
quantum computing and post-quantum cryptography.  rounds of public evaluation and analysis, with the goal
Shortly  thereafter,  NIST  began  the  Post-Quantum  of selecting algorithms for standardization by NIST
Standardization  Process,  a  thorough  multi-year  after three to fve years of analysis.
efort with the objective of creating new quantum-
FOR MORE INFORMATION, SEE:
| resistant  | cryptographic  |     | standards  |     | for  public-key  |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
encryption and digital signatures (see https://www.  https://www.nist.gov/pqcrypto
| nist.gov/pqcrypto).  |     | These  | functionalities  |     | are  | much  |     |     |     |     |     |     |
| -------------------- | --- | ------ | ---------------- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- |
CONTACTS:
more complex than AES or SHA-3, and will require
fundamentally  new  techniques  to  address  several  Email project team: pqc@nist.gov
open research questions in this area (for example, how
|     |     |     |     |     |     |     | Dr. Dustin Moody   |     |     | Dr. Lily Chen  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | -------------- | --- | --- |
to measure security against quantum attacks when a
|     |     |     |     |     |     |     | (301) 975-8136    |     |     | (301) 975-6974  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --------------- | --- | --- |
quantum computer has not yet been built). Submitters
|                    |      |                |      |          |                |     | dustin.moody@nist.gov    |     |     | lily.chen@nist.gov  |     |     |
| ------------------ | ---- | -------------- | ---- | -------- | -------------- | --- | ------------------------ | --- | --- | ------------------- | --- | --- |
| from  around       | the  | world          | are  | invited  | to  propose    |     |                          |     |     |                     |     |     |
| quantum-resistant  |      | cryptosystems  |      | for      | consideration  |     |                          |     |     |                     |     |     |
Dr. Yi-Kai Liu
by NIST as part of the PQC standardization process.
(301) 975-6499
| In  December  | 2016,  | after  | resolving  |     | and  assessing  |     |     |     |     |     |     |     |
| ------------- | ------ | ------ | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
yi-kai.liu@nist.gov
57  public comments, NIST issued the fnal submission
| requirements  | and  | evaluation  |     | criteria.  | NIST  | has  |     |     |     |     |     |     |
| ------------- | ---- | ----------- | --- | ---------- | ----- | ---- | --- | --- | --- | --- | --- | --- |
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

Circuit Complexity  CSD  is  also  researching  circuit-based  security
metrics for cryptographic functions. For a function
Cryptographic  functions,  such  as  those  used  to be secure (in particular, one-way), it must be the
for encryption, digital signatures, and hashing, are
case that any circuit that implements it is sufciently
implemented as electronic circuits for a wide class of  complex. In particular, a function is insecure if it can be
applications. In practice, it is important to be able to  implemented by a circuit containing too few Boolean
reduce the size and depth of these circuits. Size impacts
AND gates. This security metric — the number of AND
energy consumption and power requirements. Depth  gates necessary and sufcient to implement a function
largely determines the speed at which the functions  — is called multiplicative complexity. Unfortunately,
are evaluated by the circuit. This reduction problem  determining  multiplicative  complexity  is  extremely
is closely related to designing small (and low-depth)
hard. In previous years, the CSD was able to determine
combinational  circuits,  which  contain  only  logical  the multiplicative complexity of all Boolean functions
gates (i.e., no registers are used, and there is no clock).  on up to fve input bits. This year the team was able
Figure 18 below shows one such circuit, for performing
to do the same for all functions on six inputs (there
inversion in GF(24).  are 264 such functions). ITL was able to exhibit specifc
functions on n bits which are impossible to calculate
Finding optimal combinational circuits is MAX-
with fewer than n AND gates. Also as a result of
| SNP  | Complete.  | In  practice,  |     | this  means  | that  | it  is  |     |     |     |     |     |     |
| ---- | ---------- | -------------- | --- | ------------ | ----- | ------- | --- | --- | --- | --- | --- | --- |
this classifcation, it was possible to determine the
necessary to settle for methods that design “good”
multiplicative complexity of the symmetric function
circuits, as opposed to provably optimal circuits. CSD
S(8,4) – problems that had remained unresolved for
has developed and implemented new solutions for
many years.
the circuit-minimization problem. There is a tradeof
between the size and depth of circuits. Heuristics that  Secure multi-party computation is a technique
do well with respect to one of these metrics tend to do
that allows a group of people to compute a function of
so at the expense of the other one. In cooperation with  their inputs without revealing the inputs themselves.
colleagues at the University of Southern Denmark,  Examples  of  this  are:  1)  holding  an  election;  2)
CSD developed a new heuristic that simultaneously  conducting  closed-bid  auctions  in  which  only  the
reduces size and depth.
winning bid is determined; 3) proving to a third party
|     |     |     |     |     |     |     | that  a  person’s  |     | encrypted  | attributes  | satisfy  | some  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------- | ----------- | -------- | ----- |
|     | x0  | x1  | x2  | x3  |     |     |                    |     |            |             |          |       |
requirement, such as being “over 21 and (U.S. citizen

or Canadian citizen)”. The protocols that solve secure
s1    	x0 ⊕
|     |     |     |     |     | 	=  | x1  | multi-party  | computation  |     | problems  | often  | encrypt  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | --------- | ------ | -------- |
t1  	=	x0
	⊼	x3
NAND  AND NAND  t2    x0    bits using arithmetic modulo 2. The complexity of
|     | XOR  |     |     | XOR     | 	=	    | 	∧	 x2  |                                                  |     |     |     |     |     |
| --- | ---- | --- | --- | ------- | ------ | ------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
|     | s1   | t1  | t2  | t3  s2  |        |      2  |                                                  |     |     |     |     |     |
|     |      |     |     |         | t3	 =	 | x1	 ⊼	x | such protocols largely depends on the number of  |     |     |     |     |     |
	x2⊕
|     |     |     |     |     | s2	= | x3  | multiplications required. Hence, expressing functions  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |      1 | as a circuit with only a few multiplication (AND) gates  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | -------------------------------------------------------- | --- | --- | --- | --- | --- |
t4	 =	 s1	 ∧	t
s3    x1⊕
AND  XOR XOR  AND  	= 	 t2 is important. Some of the circuits published are now
|     | t4  |     | s4  | t5  | s4  	=	t2 ⊕ |   	x3    |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- |

a standard reference for the benchmarking of secure
|     |     | s3  |     |     | t5 	=	 | t3	 ∧	 s2 |                                     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --------- | ----------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |        |           | multi-party computation protocols.  |     |     |     |     |     |
    s1   4
t6	 =	 	∧	s
s5  	=	t2 ⊕	     t5
|     |      |      |     |      |     |     | The  | results  | on  circuit  | size  and  | depth,  | and  on  |
| --- | ---- | ---- | --- | ---- | --- | --- | ---- | -------- | ------------ | ---------- | ------- | -------- |
|     | AND  | AND  |     | XOR  |     |     |      |          |              |            |         |          |
t6  t7  s5  t7	 =	 s3 	∧	s 2 multiplicative complexity were presented at the 2nd

|     |     |     |     |     | s6  |   t4 ⊕	  2 | International Workshop on Boolean Functions and  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
	=	 t
s7    t6 ⊕	  1
|     |     |     |     |     | 	=	 | x   | their  Applications  |     | (Bergen,  | Norway).  | Circuits  | are  |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --------- | --------- | --------- | ---- |
t7⊕
s8	 =	 x3
XOR  XOR  XOR      periodically posted at https://csrc.nist.gov/Projects/
|     | s6  |     | s7  | s8  | y0  |     | Circuit-Complexity/Circuit-Problems.  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
	=	 s5
y1
	=	s8
y2  	=	s6
CONTACT:
|     | y0  | y1  | y2  | y3  | y3	=	s7 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Dr. René Peralta
(301) 975-8702   58
|     | Figure 18: Inversion in GF(24)  |     |     |     |     |     | rene.peralta@nist.gov  |     |     |     |     |     |
| --- | ------------------------------- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

| Lightweight Cryptography  |     |     |     |     |     |     | FOR MORE INFORMATION, SEE:  |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- |
https://www.nist.gov/programs-projects/lightweight-
| There  | are  | several  | emerging  |     | areas  | in  which  |     |     |     |     |
| ------ | ---- | -------- | --------- | --- | ------ | ---------- | --- | --- | --- | --- |
cryptography
| highly  | constrained  |     | devices  | are  interconnected  |     | and  |     |     |     |     |
| ------- | ------------ | --- | -------- | -------------------- | --- | ---- | --- | --- | --- | --- |
https://csrc.nist.gov/publications/detail/itl-
working in concert to accomplish a task. Examples
bulletin/2017/06/toward-standardizing-lightweight-
of these areas include automotive systems, sensor
cryptography/fnal
| networks,                                              | healthcare,  |     | distributed  |     | control  | systems,  |            |     |     |     |
| ------------------------------------------------------ | ------------ | --- | ------------ | --- | -------- | --------- | ---------- | --- | --- | --- |
| the Internet of Things (IoT), cyber-physical systems,  |              |     |              |     |          |           | CONTACTS:  |     |     |     |
and the smart grid. Security and privacy can be very  Mr. Lawrence Bassham    Dr. Kerry McKay
important in these areas. Because most of the modern  (301) 975-3292      (301) 975-4969
cryptographic algorithms were designed for desktop/
|         |                |     |       |            |             |     | lawrence.bassham@nist.gov    |     | kerry.mckay@nist.gov   |     |
| ------- | -------------- | --- | ----- | ---------- | ----------- | --- | ---------------------------- | --- | ---------------------- | --- |
| server  | environments,  |     | many  | of  these  | algorithms  |     |                              |     |                        |     |
cannot be implemented in the constrained devices  Dr. Meltem Sönmez Turan
| used  by  | these  | applications.  |     | When  | current  | NIST- |     |     |     |     |
| --------- | ------ | -------------- | --- | ----- | -------- | ----- | --- | --- | --- | --- |
(301) 975-4391
approved algorithms can be engineered to ft into  meltem.turan@nist.gov
| the limited resources of constrained environments,  |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
their performance may not be acceptable. For these
Cryptography Applications in
| reasons,  | NIST  | started  | a  lightweight  |     | cryptography  |     |     |     |     |     |
| --------- | ----- | -------- | --------------- | --- | ------------- | --- | --- | --- | --- | --- |
project in 2013 that was tasked with determining the  Wireless and Mobile Security
need and developing a strategy for the standardization
of lightweight cryptographic algorithms.  Today,  wireless  networks  have  been  integrated
|     |     |     |     |     |     |     | into  modern  | communication  | systems  that  | connect  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | -------------- | -------- |
In October 2016, CSD held the Second Lightweight  mobile devices using multiple radio technologies. Such
Cryptography  Workshop  for  representatives  from  heterogeneous networks demand integrated security
government, industry, and academia. The workshop led
|     |     |     |     |     |     |     | solutions.  | CSD  has  | worked  closely  with  | diferent  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------------------- | --------- |
to the publication of NISTIR 8114, Report on Lightweight  working groups in the IEEE 802 LAN/MAN Standards
Cryptography. This report provides an overview of  Committee since 2006 and made solid contributions
| the  lightweight  |     | cryptography  |     | project  | at  | NIST,  and  |     |     |     |     |
| ----------------- | --- | ------------- | --- | -------- | --- | ----------- | --- | --- | --- | --- |
to the security solutions for wireless networks. The
describes a plan for the standardization of lightweight  NIST team has been involved in the IEEE 802.11 and
cryptographic algorithms. A draft whitepaper, Profles  IEEE  802.21  working  groups  to  develop  standards
for  the  Lightweight  Cryptography  Standardization  for cryptographic key management schemes for the
Process, was released for public comment in order
mobility environment. NIST cryptographic standards
to receive community feedback on the goals for the  have been extensively used in the wireless standards
frst set of NIST lightweight cryptography standards.  developed in the IEEE 802 community.
The functionality that will be requested for this frst
set of standards are authenticated encryption with  In  FY  2017,  NIST  researchers  continuously
|             |       |         |       |           |           |     | collaborated  | with  the  | IEEE  802.21  Working  | Group.  |
| ----------- | ----- | ------- | ----- | --------- | --------- | --- | ------------- | ---------- | ---------------------- | ------- |
| associated  | data  | (AEAD)  | with  | optional  | hashing.  | A   |               |            |                        |         |
IEEE 802.21 “Media Independent Handover Services
| call  for  | algorithm  |     | submissions  | for  | the  lightweight  |     |     |     |     |     |
| ---------- | ---------- | --- | ------------ | ---- | ----------------- | --- | --- | --- | --- | --- |
cryptography portfolio will be announced in FY 2018,  Framework” was published, and IEEE 802.21.1 “Media
Independent Services” was fnalized for publication.
along with details of the selection process.
These new standards address the future connectivity
NISTIR  8114  and  the  Lightweight  Cryptography  and management requirements of Smart Grid, IoT and
project were featured in the June 2017 ITL bulletin,
|     |     |     |     |     |     |     | Smart  | Home  networks,  | where  multimode  | wireless  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------------- | ----------------- | --------- |
and CSD presented a poster on the project during  devices and smart end nodes incorporate diferent
ITL Science Day in October 2016. The Lightweight  wireless interfaces, and need to switch among the
Cryptography project was presented at several venues
networks during an ongoing communication session,
in FY 2017, including Real World Crypto, HighLight:  while  maintaining  the  same  security  posture.  IEEE
High Security Lightweight Cryptography, and the rump  802.21 and IEEE 802.21.1 adopted NIST standardized
sessions of the Eurocrypt and Crypto conferences.  cryptographic algorithms, such as ECDSA, as specifed
59
in FIPS 186-4, and AES-CCM, as specifed in SP 800-
38C.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

The recently revealed KRACK attack on the IEEE  Figure 19  illustrates three blocks in a blockchain,
802.11 wireless network leads to generating the same  where each block contains at least one transaction, a
key stream in the case of AES-CCM, or recovering the  nonce and the hash value of the previous block in the
| authentication key, in the case of AES-GCM through  |     |     |         |             |             |     | chain.  |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | ------- | ----------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| a  man-in-the-middle                                |     |     | attack  | to  create  | a  counter  |     |         |     |     |     |     |     |     |
The most well-known example of the use of a
reset condition. The KRACK attack confrms that it is
blockchain is BitCoin and similar digital currencies.
essential to make sure that the special features and
However, the use of blockchains has been proposed
assumptions for using each cryptographic algorithm
for other applications, such as smart contracts and
| are  considered  |     | in  | the  protocol  | design  | so  that  | the  |     |     |     |     |     |     |     |
| ---------------- | --- | --- | -------------- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
various ledgering applications.
requirements are satisfed to assure security in any
circumstance.  Many organizations have suggested applications
for the use of blockchains, some of which may not
In FY 2018, CSD will continue to contribute to IEEE
|     |     |     |     |     |     |     | be  appropriate.  |     | CSD  | is  investigating  |     | the  | use  of  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | ------------------ | --- | ---- | -------- |
802 wireless standards. CSD will work with the IEEE
blockchains to determine which application types are
802.11 working group to develop countermeasures for
appropriate for using blockchains and which are not.
the KRACK attack.
CSD is monitoring the proposed uses of cryptography
CONTACT:  to  assure  that  current  cryptographic  techniques
are used properly and whether new techniques are
Dr. Lily Chen
required.
(301) 975 -6974
lily.chen@nist.gov
During FY 2017, NIST participated in standards
|     |     |     |     |     |     |     | activities  | exploring  |     | blockchain  |     | technologies,  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ----------- | --- | -------------- | --- |
Blockchains
|        |        |           |            |          |               |      | architectures,  |     | and         | use  cases.  |     | These  included  |        |
| ------ | ------ | --------- | ---------- | -------- | ------------- | ---- | --------------- | --- | ----------- | ------------ | --- | ---------------- | ------ |
|        |        |           |            |          |               |      | participation   |     | in  a  new  | blockchain   |     | study            | group  |
| CSD    | began  | studying  | the        | use  of  | blockchains,  |      |                 |     |             |              |     |                  |        |
|        |        |           |            |          |               |      | sponsored       | by  | American    | Standards    |     | Committee        | X9,    |
| which  | have   | been      | suggested  | as  a    | solution      | for  |                 |     |             |              |     |                  |        |
|        |        |           |            |          |               |      | the  fnancial   |     | services    | committee    | of  | the  American    |        |
many applications. A  blockchain  is a distributed
National Standards Institute (ANSI), and continued
| database  | that  | maintains  | a   | continuously  | growing  |     |           |      |                |            |     |               |     |
| --------- | ----- | ---------- | --- | ------------- | -------- | --- | --------- | ---- | -------------- | ---------- | --- | ------------- | --- |
|           |       |            |     |               |          |     | work  in  | the  | International  | Standards  |     | Organization  |     |
list of records called blocks that are secured from
|             |     |              |        |          |            |     | (ISO)  Technical  |     | Committee  |     | (TC)  | for  Blockchains  |     |
| ----------- | --- | ------------ | ------ | -------- | ---------- | --- | ----------------- | --- | ---------- | --- | ----- | ----------------- | --- |
| undetected  |     | modifcation  | using  | a  hash  | function.  |     |                   |     |            |     |       |                   |     |
and Distributed Ledger Technologies (ISO/TC 307).
Each block contains a link to the previous block. A
Established in 2016, the initial objectives of ISO/TC 307
new block is added to the chain only when multiple
include defning key terms and concepts, exploring
parties (possibly mutually untrusted parties) agree
reference architectures, investigating use cases, and
to its accuracy. In essence, a blockchain is a mutually
identifying identity and privacy implications within
agreed-upon record of history.
blockchain technologies and architectures. NIST has
|     |     |     | Tlmestamp  |     |     |     | Tlmestamp  |     |     |     | T1mestamp  |        |     |
| --- | --- | --- | ---------- | --- | --- | --- | ---------- | --- | --- | --- | ---------- | ------ | --- |
|     |     |     | Nonce      |     |     |     | Nonce      |     |     |     |            | Nonce  |     |
Time
60
Figure 19: Example of a Blockchain
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

been participating in these activities via the national  specifcations. To that end, the CSD develops test
mirror committee within the InterNational Committee  suites  and  test  methods;  provides  implementation
for Information Technology Standards (INCITS). ISO/  guidance and technical support to industry forums;
TC 307 will meet in November 2017, where the reports  and  conducts  education,  training,  and  outreach
|     | on these topics will be reviewed and new work will be  |     |     |     |     | programs.  |     |     |     |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
established.
|     |     |     |     |     |     | CSD’s  | validation  | programs  |     | work  | together  | with  |
| --- | --- | --- | --- | --- | --- | ------ | ----------- | --------- | --- | ----- | --------- | ----- |
During FY 2017, CSD established the NIST Internal  independent laboratories that are accredited by the
Blockchain Workbench to support internal research  National Voluntary Laboratory Accreditation Program
exploring  blockchain  technologies  and  use  cases.  (NVLAP).  Based  on  independent  laboratory  test
The workbench itself is hosted on internal servers,  reports and test evidence provided by the labs, the
and is currently running two blockchains – the frst
|     |     |     |     |     |     | validation  | programs  | described  |     | below  | validate  | the  |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------- | --- | ------ | --------- | ---- |
is a permissioned blockchain utilizing the MultiChain  implementation-under-test. Awarded validations are
blockchain  platform;  the  second  is  Ethereum,  subsequently published on NIST websites.
which has been confgured to run only within the
workbench. In addition to the blockchain software  Cryptographic  Algorithm  Validation
itself, the workbench has demonstration applications
Program (CAVP)
with source code, software development tools and
several diagnostic tool suites available for researchers
The Cryptographic Algorithm Validation Program
to utilize. NIST/ITL plans to continue advancing the  (CAVP) provides federal agencies in the United States
capabilities  of  the  workbench  and  expanding  the  and  Canada  with  assurance  that  a  cryptographic
types of blockchains available in FY 2018.
|     |     |     |     |     |     | algorithm  | has  | been  | implemented  |     | completely  |     |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ----- | ------------ | --- | ----------- | --- |
and correctly, as specifed in its approved Federal
CONTACTS:
|     |                     |     |                   |     |     | Information           | Processing  |     | Standard       | (FIPS-Approved)  |            |     |
| --- | ------------------- | --- | ----------------- | --- | --- | --------------------- | ----------- | --- | -------------- | ---------------- | ---------- | --- |
|     | Ms. Elaine Barker   |     | Mr. John Kelsey   |     |     |                       |             |     |                |                  |            |     |
|     |                     |     |                   |     |     | or  NIST-recommended  |             |     | cryptographic  |                  | algorithm  |     |
|     | (301) 975-2911      |     |   (301) 975-5101  |     |     |                       |             |     |                |                  |            |     |
standard. The CAVP was established in 2013 as a
|     | ebarker@nist.gov   |     | john.kelsey@nist.gov    |     |     |                      |     |                    |     |                |       |        |
| --- | ------------------ | --- | ----------------------- | --- | --- | -------------------- | --- | ------------------ | --- | -------------- | ----- | ------ |
|     |                    |     |                         |     |     | joint  program       |     | in  collaboration  |     | between        | NIST  | and    |
|     |                    |     |                         |     |     | the  Communications  |     | Security           |     | Establishment  |       | (CSE)  |
|     | Dr. René Peralta   |     | Mr. Andrew Regenscheid  |     |     |                      |     |                    |     |                |       |        |
of Canada. Prior to this date, the CAVP’s functions
|     | (301) 975-8702    |     | (301) 975-5155  |     |     |     |     |     |     |     |     |     |
| --- | ----------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
were included in the Cryptographic Module Validation
|     | rene.peralta@nist.gov   |     | andrew.regenscheid@nist.gov  |     |     |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Program (CMVP). With the increase in the number and
complexity of FIPS-Approved and NIST-recommended
Mr. Dylan Yaga
cryptographic algorithms, it was deemed necessary
(301) 975-6004
to establish the CAVP as an independent program.
dylan.yaga@nist.gov
The CAVP’s goal is to provide federal agencies with

a security metric list to use in validating cryptographic

|     |     |     |     |     |     | algorithm  | implementations,  |     | and  | promote  |     | the  use  |
| --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | ---- | -------- | --- | --------- |
of validated algorithms by industry and the public.
VALIDATION PROGRAMS
|     |     |     |     |     |     | The  testing         | is  | carried     | out  by  | independent  |         | third-   |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ----------- | -------- | ------------ | ------- | -------- |
|     |     |     |     |     |     | party  laboratories  |     | accredited  |          | by  the      | NVLAP,  | and      |
|     |     |     |     |     |     | the  validations     |     | performed   | by       | the  CAVP    |         | program  |
Federal agencies, industry, and the public rely on
provide this metric. Federal agencies, industry, and
many of the standards and specifcations supported
|     |                    |       |                  |             |                   | the  public        | can  | choose      | validated  | implementations  |      |       |
| --- | ------------------ | ----- | ---------------- | ----------- | ----------------- | ------------------ | ---- | ----------- | ---------- | ---------------- | ---- | ----- |
|     | by  ITL.           | Poor  | implementations  | of          | these  standards  |                    |      |             |            |                  |      |       |
|     |                    |       |                  |             |                   | of  cryptographic  |      | algorithms  |            | from             | the  | CAVP  |
|     | or  specifcations  |       | may  render      | a  product  | insecure,         |                    |      |             |            |                  |      |       |
Validated Algorithms List and have confdence in the
potentially placing sensitive information at risk. ITL
claimed level of security and assurance of correct
operates several validation programs that help provide
implementation.
a level of assurance that products meet established
| 61  | security  | requirements  | and  | conform  | to  published  |      |             |     |                |     |             |     |
| --- | --------- | ------------- | ---- | -------- | -------------- | ---- | ----------- | --- | -------------- | --- | ----------- | --- |
|     |           |               |      |          |                | The  | validation  | of  | cryptographic  |     | algorithms  |     |
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

by the CAVP is a prerequisite to the validation of a through defned sets of security requirements. For
cryptographic module by the CMVP and is also used by the CAVP, a validation system document is designed
other programs outside of NIST as well. Since federal for each FIPS-approved or NIST-recommended
agencies are required to use validated cryptographic cryptographic algorithm. See the website for a listing
modules for the protection of sensitive unclassifed (see https://csrc.nist.gov/groups/STM/cavp/). The
information, the validated modules and the validated four Annexes to FIPS 140-2 reference the underlying
algorithms that the modules contain represent the cryptographic algorithm standards or methods.
culmination and delivery of CSD’s cryptography-
By the end of FY 2017, the CAVP had issued
based work to the end user.
approximately 28,710 validations, representing the
The CAVP validation program provides algorithm validations of approximately 18 approved
documented methodologies for conformance testing algorithms, including 5 modes of operation.
CAVP Validation Status By FYs
6000
5000
4000
3000
2000
1000
0
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017
6991YF 8991YF 0002YF 2002YF 4002YF 6002YF 8002YF 0102YF 2102YF 4102YF 6102YF
Figure 20: CAVP Validation Status by Fiscal Year
62

CA VP Validation Status For FYI 7

TOES
1400

SHA3
1200 
SHA

1000 RSA

KDF
800

KAS
600
DH.MAC

400 ECDSA
ODSA
200
DDRBG
0  ComponentTest
~.. . ~ ~. r . - -- r . - -- r . - -- r . - -- . r- -- r . - -- r . - -- r . - -- r . - --  AES
~ ~ ~ ~ ~ ~ ~ ~ ~ - ~ ~ ~
0 (.I
z~
Q
(
~
.I
~
i ,
~
.
~
Q
~
"
~
' "
-
"=
<
'"-
~
>
~
,
~
§
~ -
b=
<
Jl
0
=
~ 0
-
Figure 21: CAVP Validation Status for FY 2017
CAVP Validated Implementation Actual Numbers
Updated As: Friday, November 03, 2017
FiscalYear AES Comp. DES DSA DRBG ECDSAHMAC KAS KDF RNG RSA SHA SJ TDES Total
FY1996 0 0 2 0 0 0 0 0 0 0 0 0 0 0 2
FY1997 0 0 11 6 0 0 0 0 0 0 0 7 2 0 26
FY1998 0 0 27 9 0 0 0 0 0 0 0 6 0 0 42
FY1999 0 0 30 14 0 0 0 0 0 0 0 12 1 0 57
FY2000 0 0 29 7 0 0 0 0 0 0 0 12 1 28 77
FY2001 0 0 41 15 0 0 0 0 0 0 0 28 0 51 135
FY2002 30 0 44 21 0 0 0 0 0 0 0 59 6 58 218
FY2003 66 0 49 24 0 0 0 0 0 0 0 63 3 73 278
FY2004 82 0 41 17 0 0 0 0 0 28 22 77 0 70 337
FY2005 145 1 54 31 0 14 115 0 0 108 80 122 2 102 774
FY2006 131 1 3 33 0 19 87 0 0 91 63 120 1 83 632
FY2007 238 5 0 63 0 35 127 0 0 137 130 171 1 136 1043
FY2008 271 7 0 77 4 41 158 0 0 137 129 191 0 122 1137
FY2009 373 2 0 71 23 33 193 6 0 142 143 224 1 138 1349
FY2010 406 2 0 70 31 39 179 12 0 150 155 239 0 142 1425
FY2011 476 11 0 102 79 68 201 34 0 148 183 255 0 177 1734
FY2012 654 24 0 121 122 92 283 20 3 157 231 323 1 248 2279
FY2013 778 88 0 106 145 113 276 12 9 132 208 293 0 217 2377
FY2014 595 223 0 95 167 96 276 14 23 63 225 314 0 196 2287
FY2015 1179 226 0 99 320 164 355 32 35 80 243 396 0 258 3387
FY2016 1357 329 0 125 339 214 422 50 32 23 305 463 0 303 3967
FY2017 1786 503 0 170 426 271 508 88 52 0 391 547 0 371 5147
Total 8567 1422 331 1276 1656 1199 3180 268 154 1396 2508 3922 19 2773 28710
63
Figure 22: Validated Implementation Actual Numbers
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

The CAVP issued approximately 5,000 algorithm Validated Modules List and have confdence in the
validations in FY 2017, an increase of approximately claimed level of security and assurance of correct
100 validations from the previous year. The increase in implementation.
validations is attributed to an increase in cryptographic
Cryptographic module testing and validation are
modules being validated and other outside programs
based on published NIST standards. Since federal
now requiring CAVP validated implementations,
agencies are required to use validated cryptographic
e.g., the National Information Assurance Partnership
modules for the protection of sensitive unclassifed
(NIAP).
information, the validated modules and the validated
The number of algorithms submitted for validation algorithms that the modules contain represent the
continues to grow, representing signifcant growth in culmination and delivery of the CSD’s cryptography-
the number of validations expected to be available in based work to the end user.
the future.
The CMVP validates modules that are used in a
FOR MORE INFORMATION, SEE: wide variety of products, including Internet browsers,
radios, smart cards, space-based communications,
https://csrc.nist.gov/groups/computer-security-
munitions, security tokens, mobile phones, network
division/security-testing-validation-and-
and storage devices, and products supporting
measurement
the Public Key Infrastructure (PKI) and electronic
CONTACT:
commerce. A module may be a standalone product,
Mr. Harold Booth such as a virtual private network (VPN) or smart card,
(301) 975-8441 or it could be a module embedded in many products,
harold.booth@nist.gov such as a cryptographic-based toolkit. As a result, a
small number of modules may be incorporated within
(Editors’ Note: Sharon Keller worked on this hundreds of products.
program until her recent retirement.)
The theme for FY 2017 was modernization. As part
of the launch of the new Computer Security Resource
Cryptographic Module Validation Center (CSRC) web site, the CMVP web pages were
Program (CMVP) redesigned and now have a new look with additional
functionality. The CMVP was automated to improve
The Cryptographic Module Validation Program its validation processes, the Cryptographic Validation
(CMVP) was developed to support the federal user Program (CVP) Certifcation Exam was developed, and
communities for strong, independently tested, and collaboration was continued with the Cryptographic
commercially available cryptographic modules. Modules User Forum (CMUF) to publish new CMVP
Through this program, the CMVP works with Implementation Guidance (IG).
international government, public and private sectors
The CMVP uses an automation system to manage
as a part of the cryptographic community to achieve
the validation workfow. This automation continues to
standards-based security and assurance of correct
reduce the administrative overhead for the program
implementation. The goal is to provide federal
allowing the staf to focus on addressing the technical
agencies with a security metric list to use in procuring
needs of the community. The automated system tracks
and deploying validated cryptographic modules, and
the status of each submission and identifes the order
promote the use of those modules by industry and
that the submission should be reviewed, based on
the public. The testing performed by independent
when the submission was added to the CMVP queue.
third-party laboratories accredited by NVLAP, and the
In FY 2017, the CMVP awarded 271 new certifcates.
validations performed by the CMVP program provide
Figure 23 displays the number of certifcates that
this metric. Federal agencies, industry, and the public
were issued by security level.
can choose cryptographic modules and/or products
containing cryptographic modules from the CMVP
64
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

In February 2017, the CMVP adopted the fve
FY 2017 CMVP Certificates
year Validation Sunsetting Policy that moved all
271 Total FIPS 140-1 validation entries and all validations that
were completed prior to February 1, 2012 from the
2, 1%
28, 10% Active Validation List to the Historical Validation
List. This was done to ensure that modules on the
Active Validation List are compliant with the latest
standards and guidance. In January 2018, the CMVP
will drop modules to the historical list that have not
138, 51%
103, 38% been validated within two years of report or billing
submission, whichever occurred frst. This is to
encourage the completion of projects and to ensure
that the MIP list refects modules that are actively in
the validation process.
• Level 1 • Level 2 • Level 3 • Level 4 In order to demonstrate profciency in the
technical areas addressed by Handbook 150-17,
NVLAP Cryptographic and Security Testing, the
Figure 23: FY 2017 CMVP
CMVP activated the CVP Certifcation Exam in July
Certifcates by Security Level
2017. This exam is now required as part of the initial
and renewal accreditation process. The profciency
Initially, this system automated the creation and
testing was previously handled by the NVLAP/
transmittal of billing invoices, but then was further
CMVP technical assessors at the onsite audit, but is
enhanced to allow laboratories to submit those
now being managed through a third-party testing
invoices in advance of the report submission. For
facility. Each laboratory must have a minimum of two
laboratories and vendors who elect to take advantage
testers who pass the exam to be eligible for initial or
of this, the amount of time that submissions wait in
renewal accreditation. The certifcation will remain
the queue prior to being assigned has been reduced,
with the individual tester making it easier to access
which in turn lessens the overall time to validation.
the laboratory’s overall competency, as its staf may
This enhancement provides signifcant time savings
change over time. In support of this efort, the CMVP
and was achieved due to the continued collaborative
also created a web site and user’s guide that provides
efort between the CMVP and NIST Receivables.
information on this new certifcation process.
In order to provide a greater transparency to
In September 2017, the NIST CSRC launched a new
the laboratories, the CMVP sends a weekly report to
website. In support of that efort, the CMVP updated
each laboratory providing a status of each of their
its web pages to include both basic and advanced
submissions. The CMVP provides those reports to
search capabilities. The basic search results in the list
apprise the laboratories of the current state of each
of all active validated modules. The more advanced
submission along with their respective payment
search allows the user to search on specifc felds
status. This has mitigated the number of status
and to retrieve historical and revoked certifcates. For
requests that need to be addressed by the CMVP.
each validation, there are links provided to related
Since August 2015, the CMVP produces a separate fles that direct the user to the module’s security
Implementation Under Test (IUT) list from the policy and to the applicable consolidated certifcate.
Modules In Process (MIP) list. The IUT list is merely The consolidated certifcates are generated once a
provided as a marketing service for vendors. However, month and include the individual validations that
to encourage this list to be kept up to date, the CMVP were completed within that particular month. The
implemented a new policy to drop IUT entries that are posting of the most current CMVP IG document was
greater than 18 months old. The MIP list continues to also separated from the archived versions that are still
refect the status of the current work that is actively in accessible for historical reference.
65 the validation process.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

The CMVP has maintained the relationship with CONTACT:
the CMUF by supporting the monthly CMUF general
Ms. Beverly Trapnell
membership meetings and the CMUF working
(301) 975-6745
groups. The working groups are chaired by a member
beverly.trapnell@nist.gov
of industry and/or laboratory personnel. Each
working group includes a representative from the
Automated Cryptographic Validation
CMVP. The current working group tasks include the
Revalidation and Response to Common Vulnerabilities (ACV) Testing
and Exposures (CVEs), ROM Integrity Testing in
Constrained Devices, and Testing Equivalency. The Cryptographic Module Validation Program
Working groups are dissolved once discussions on (CMVP) was established on July 17, 1995 by NIST to
the topics are completed, and guidance is typically validate cryptographic modules for conformance to
published. the Federal Information Processing Standards (FIPS)
140-1, Security Requirements for Cryptographic
In order to provide predicable support for
Modules, and other FIPS cryptography-based
vendors and laboratories needing guidance, the
standards. FIPS 140-2 was released on May 25, 2001
CMVP implemented a quarterly IG release process.
and supersedes FIPS 140-1.
New draft IGs and revisions to currently posted IGs
are sent out once a month to the laboratories for The current implementation of the CMVP is shown
comments. Vendors are encouraged to provide their in Figure 24 below. The CMVP leverages the National
feedback, so draft IGs are also posted on the CMUF Voluntary Laboratory Accreditation Program (NVLAP)
Forum. The comments are adjudicated by the CMVP, accredited Cryptographic and Security Testing (CST)
and the fnalized IGs are incorporated into the main laboratories for validation testing against the Derived
IG document, which is posted quarterly on the CMVP Test Requirements (DTR), Implementation Guidance
web site. (IG), and applicable CMVP programmatic guidance.
According to existing guidance, the CST laboratories
For FY 2018, the CMVP is anticipating the approval
must perform 100 % independent testing of the
of FIPS 140-3. When approved, the CMVP will create
modules submitted by the vendors.
the necessary documents and processes to support
the transition from FIPS 140-2 to FIPS 140-3. The The structure and the rules under which the CMVP
CMVP will continue to: operates worked well for the level of the technology
utilized by the Federal Government when the
• Invest in automation to streamline the
program was created more than two decades ago. As
validation process and improve review
technology progresses and cryptography becomes
consistency,
ubiquitous in the federal IT infrastructure, the plethora
of cryptographic module validations has proven
• Strengthen its relationship with the CMUF by
to outstrip available human resources for vendors,
collaborating on new and improved technical
third-party testing laboratories and federal validators
guidance and programmatic issues, and
alike. As the number and complexity of modules to
• Support the ICMC committee to continue be validated increases, the existing methodologies
strengthening the relationship with vendors face a limit on their ability to catch and eliminate all
and laboratories. possible defects that could compromise the security.
Testing is exceedingly long — well beyond typical
FOR MORE INFORMATION, SEE:
product-development cycles across a wide range of
https://csrc.nist.gov/projects/cryptographic-module- technologies — yet costly and inefective. The resulting
validation-program/module-validation-lists validated modules often do not provide useful
https://wsr.pearsonvue.com/nist-cmvp interfaces for integration into IT systems to enable
run-time monitoring of modules for compliance with
FISMA.
66
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

|     | Accredit | ed  |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- |
IUT
|     | Cryp1t10gr~p h le i!!ind  | • vendor reques.fSM ald a oo al lmpleiromiatlon  |     |              |                     |      |
| --- | ------------------------- | ------------------------------------------------ | --- | ------------ | ------------------- | ---- |
|     | 5'                        | i  • subm rs the modlll                          |     | fortes  118  |                     |      |
|     | uri yTes.ti               |                                                  |     |              | Cryp •osra p        | i,c  |
|     | Laboratory                |                                                  |     |              | Modu I!' vl!'nd or  |      |
IVT
cvlcw-
•  La!bp erforms
|     | conform  :et es- |     |     |     | • WIM!nI s ln•roicek  p,ald,  |          |
| --- | ---------------- | --- | --- | --- | ----------------------------- | -------- |
|     |                  |     |     |     | cwo CMVP rel/le               | ers a e  |
•  P!1lparl?'Stl-:'f.t
|     | report  |     |     |     | a99i.!lneadn d r~ili'l't the  |     |
| --- | ------- | --- | --- | --- | ----------------------------- | --- |
submitted documients
|     |     |     |     |     | • CMVPP OCi s ~ne,cl  | tu  |
| --- | --- | --- | --- | --- | --------------------- | --- |
n  nage t!Mc! oordlnaoon
phas.e
|     | Crypto  rap hie  |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- |
and . 40-2 Cry-ptogra ph le
Mo-dule  Test.
Ri!!!prot  Module5-Li.st
|     |     |     |     | ltttp;f/<= ,ri st.ii<'Y/'1:ro\lP~Tl\1f,::nmi/d~140-1/1dl]y  |     | all,h  |
| --- | --- | --- | --- | ----------------------------------------------------------- | --- | ------ |
Figure 24: Current Validation Flow
NIST recognizes the need to improve the efciency  The scope of this project is broken into multiple
and efectiveness of cryptographic module testing  phases to be performed over several years:
| to  reduce  | the  time  and  | cost  required  | for  testing,  |     |     |     |
| ----------- | --------------- | --------------- | -------------- | --- | --- | --- |
Phase 1
while providing a high level of assurance for Federal
Government consumers.
•   Identify potential approaches,
The  principal  goals  of  this  project  are  to  •   Select the best technical approach or
collaborate with commercial or open source producers
approaches to prototype, and
| of  cryptographic  | capabilities  | and  | government  |     |     |     |
| ------------------ | ------------- | ---- | ----------- | --- | --- | --- |
consumers of FIPS 140-validated modules to:  •   Document the technical approach.
| •   Improve the efciency and efectiveness of  |     |     |     | Phase 2  |     |     |
| --------------------------------------------- | --- | --- | --- | -------- | --- | --- |
cryptographic module testing by adopting the
•   Develop working prototypes, and
best practices used by industry;
•   Evaluate the prototypes against the principal
•   Develop test procedures and techniques that
goals.
provide assurance of module compliance
to FIPS 140 in an automated manner, based
Phase 3
on machine-readable artifacts or evidence
(examples of machine readable artifacts are  •   Publish a draft, provide a review period,
XML or JavaScript Object Notation (JSON)  adjudicate the comments, and publish the
fles containing logs from performed tests and  fnal version.
the corresponding results – see examples at
Phase 4
https://github.com/usnistgov/ACVP); and
•   Integrate the fnal version into the operational
•   Identify techniques and procedures that
CMVP program.
provide continued assurance of operational
compliance to FIPS 140 for cryptographic  The new structure of the CMVP is shown in Figure
modules throughout their lifecycle.
25. It leverages automation through computer analysis
67
of test results.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

Proxy/Validation Authority Architecture
Automated Cryptographic Validation System
|     |     |     |     |     |     |     |     |     |     | s:t::-t•o  | r•s•-  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | --- |
ACV Protocol
5
----
esponses
Device Under Test
' Vendor ACV Server
I
NIST ACV Server
Figure 25: Updated CMVP Structure Leveraging Automation
b.   Modules in cloud environments,
Currently, the project is focused on completing
| the  documentation  |     | of  | the  | technical  | approach  | for  |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ---- | ---------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
c.   Hardware; and
| automating  |     | the  algorithm  |     | testing  | and  | fnalizing  |     |     |     |     |     |     |     |
| ----------- | --- | --------------- | --- | -------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
3.   Positioning and relationships to other
| the  implementation  |     |     | of  the  | automated  |     | algorithm  |     |     |     |     |     |     |     |
| -------------------- | --- | --- | -------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
government validation programs.
| testing      | server.  | The              | team  | is  also  | working     | on   |      |          |      |          |          |                |     |
| ------------ | -------- | ---------------- | ----- | --------- | ----------- | ---- | ---- | -------- | ---- | -------- | -------- | -------------- | --- |
| researching  |          | the  approaches  |       | for       | automating  | the  |      |          |      |          |          |                |     |
|              |          |                  |       |           |             |      | The  | project  | has  | several  | planned  | deliverables,  |     |
software module testing. The team working on this
including the identifcation of prospective technical
| project,  | in  collaboration  |     | with  | industry,  |     | established  |     |     |     |     |     |     |     |
| --------- | ------------------ | --- | ----- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
a  demonstration  algorithm  testing  server  that  is  approaches that adopt industry best practices and
produce artifacts that are machine readable and map
currently capable of testing over 30 algorithms (see
to FIPS 140 DTR requirements, and a selection of the
| https://demo.acvts.nist.gov/acvp/home).  |     |     |     |     |     | The  work  |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
is progressing, and new algorithms are added to it  best technical and feasible approaches.
on an ongoing basis. Eventually, this demonstration
CONTACT:
functionality will be transferred into the production
server  for  algorithm  validation  testing.  The  team  Dr. Apostol Vassilev
| developed criteria for participation in the automated  |     |     |     |     |     |     | (301) 975-3221   |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
apostol.vassilev@nist.gov
testing for commercial companies wishing to validate
their cryptographic algorithm implementations. The
criteria are positioned as an annex to NIST Handbook  Automated Security Testing and Test
| 150-17,  NVLAP  |     | Cryptographic  |     | and  | Security  | Testing,  |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | --- | ---- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Suite Development
| which  NVLAP  |     | uses  | to  accredit  |     | laboratories.  | This  |     |     |     |     |     |     |     |
| ------------- | --- | ----- | ------------- | --- | -------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
criteria will be used, beginning in FY 2018, to establish
|     |     |     |     |     |     |     | The  | CAVP  | utilizes  |     | the  requirements  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --------- | --- | ------------------ | --- | ---- |
a new testing scope for algorithm testing.  specifcations of the NIST standards (i.e., FIPS and
Special Publications) to develop algorithm validation
The project activities are structured by work areas
test suites and an automated security testing tool.
in order for subject-matter experts to more narrowly
|     |     |     |     |     |     |     | The  CAVP  | is  | responsible  |     | for  providing  | assurance  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | --- | --------------- | ---------- | --- |
focus on program needs and develop solutions:
|     |     |     |     |     |     |     | that  the  | cryptographic  |     | algorithm  | implementations  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ---------- | ---------------- | --- | --- |
1.   Algorithm and Protocol Testing;  contained in cryptographic modules are implemented
according to the specifcations in the standards. The
2.   Cryptographic Module Testing,
CAVP accomplishes this by designing and developing
a.   Software,  conformance testing specifc to each cryptographic  68
algorithm.
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

The conformance testing consists of a suite of  During  the  last  few  years,  CSD  has  expanded
validation  tests  for  each  approved  cryptographic  its publications to contain not only the algorithm’s
algorithm.  These  validation  tests  exercise  the  specifcations, but also requirements for an algorithm’s
algorithmic  requirements  and  mathematical  use. Many of these usage requirements do not fall
formulas to assure that the detailed specifcations  within the scope of the CAVP, because the CAVP
are  implemented  correctly  and  completely.  If  the  focuses on the correctness of the instructions within
implementer deviates from the specifcations in the  the algorithm’s boundary. If these additional algorithm
standard or excludes any part of these specifcations  usage  requirements  are  not  considered  applicable
or requirements, the validation test will detect the  to the algorithm’s implementation, they cannot be
deviations and fail. The validation testing will indicate  tested at the algorithm level by the CAVP, but may be
tested by the CMVP if the requirements are considered
that the algorithm implementation does not function
properly or is incomplete.  applicable  to  the  cryptographic  module.  However,
some of these usage requirements may be outside
| The  | cryptographic  |     | algorithm  | validation  |     | tests  |             |                |            |                 |     |
| ---- | -------------- | --- | ---------- | ----------- | --- | ------ | ----------- | -------------- | ---------- | --------------- | --- |
|      |                |     |            |             |     |        | the  scope  | of  both  the  | algorithm  | implementation  |     |
designed and developed by the CAVP are used by
and cryptographic module. In this latter case, the
independent third-party laboratories accredited by
fulfllment of the requirements is the responsibility of
NVLAP. The laboratory works with vendors to validate
entities using, installing, or confguring applications or
their cryptographic algorithm implementations. The  protocols that use the cryptographic algorithms. For
suite of validation tests for each algorithm ensures the
example, depending on the design of a cryptographic
repeatability of tests and the equivalency of results
module, it may not be possible for the module to
across the testing laboratories.  determine whether a specifc key is used for multiple
purposes, a situation that is strongly discouraged.
| There  | are  | several  | types  | of  validation  |     | tests,  all  |     |     |     |     |     |
| ------ | ---- | -------- | ------ | --------------- | --- | ------------ | --- | --- | --- | --- | --- |
designed to satisfy the testing requirements of the
|     |     |     |     |     |     |     | The  | CAVP  currently  | has  algorithm  |     | validation  |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------------- | --------------- | --- | ----------- |
cryptographic  algorithms  and  their  specifcations.  testing for the following cryptographic algorithms:
| These  | include  | Known-Answer  |     | Tests,  | Monte  | Carlo  |     |     |     |     |     |
| ------ | -------- | ------------- | --- | ------- | ------ | ------ | --- | --- | --- | --- | --- |
Tests, and Multi-Block Message Tests. The Known-
| Answer Tests are designed to examine the individual  |     |     |     |     |     |     |     | -\' 0  |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
components of the algorithm by supplying known
|                                                     |           |            |     |           |             |       |     | ·.         | .     | SHA..f      |          |
| --------------------------------------------------- | --------- | ---------- | --- | --------- | ----------- | ----- | --- | ---------- | ----- | ----------- | -------- |
| values to the variables and verifying the expected  |           |            |     |           |             |       |     |            |       |             | ~        |
| result.                                             | Negative  | testing    |     | is  also  | performed   | by    |     |            |       |             |          |
|                                                     |           |            |     |           |             |       |     | ~.·.       |       | /           | SHA-224  |
| supplying                                           | known     | incorrect  |     | values    | to  assure  | that  |     |            |       |             |          |
|                                                     |           |            |     |           |             |       |     | ..~,   ~·  | Q  J  | •  (SHA-2)  |          |
the implementation recognizes values that are not
allowed. The Monte Carlo Test is designed to exercise  ~-f-1  SHA-256
|     |     |     |     |     |     |     |     | "•  ,  | ,  •  | -   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- |
the entire implementation-under-test (IUT). This test  1  .  (SHA-2)
is designed to detect the presence of implementation
faws that are not detected with the controlled input of
the Known-Answer Tests. The types of implementation
faws detected by this validation test include pointer
problems, insufcient allocation of space, improper
| error  handling,  |     | and      | incorrect  | behavior     | of  | the  IUT.  |     |     |     |     |     |
| ----------------- | --- | -------- | ---------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
| The  Multi-Block  |     | Message  |            | Test  (MMT)  | is  | designed   |     |     |     |     |     |
Credit: Shutterstock/Olivier Le Moal
to test the ability of the implementation to process
multi-block messages, which requires the chaining of  Various Types of SHAs
information from one block to the next.
69
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

TABLE 2: CRYPTOGRAPHIC ALGORITHMS & NIST TECHNICAL DOCUMENTS (FIPS & SPs)
FEDERAL INFORMATION PROCESSING
CRYPTOGRAPHIC
STANDARD (FIPS), SPECIAL PUBLICATION
ALGORITHM/COMPONENT
(SP) OR OTHER REFERENCE DOCUMENT
SP 800-67, Recommendation for the Triple Data
Encryption Algorithm (TDEA) Block Cipher, and
Triple Data Encryption Standard (TDES)
SP 800-38A, Recommendation for Block Cipher
Modes of Operation–Methods and Techniques
FIPS 197, Advanced Encryption Standard, and
Advanced Encryption Standard (AES)
SP 800-38A, Recommendation for Block Cipher
Modes of Operation–Methods and Techniques
FIPS 186-2, Digital Signature Standard (DSS), with
change notice 1 and
Digital Signature Algorithm (DSA)
FIPS 186-4, Digital Signature Standard (DSS)
FIPS 186-2, Digital Signature Standard (DSS), with
Elliptic Curve Digital Signature Algorithm change notice 1 and ANS X9.62 and
(ECDSA) FIPS 186-4, Digital Signature Standard (DSS) and
ANS X9.62
FIPS 186-4, Digital Signature Standard (DSS) and
RSA Algorithm
ANS X9.31 and Public Key Cryptography Standards
(PKCS) #1 v2.1: RSA Cryptography Standard-2002
Hashing algorithms SHA-1, SHA-224, SHA-256, SHA-
FIPS 180-4, Secure Hash Standard (SHS)
384, SHA-512, SHA-512/224, SHA-512/256
Hashing algorithms SHA3-224, SHA3-256, SHA3-384, FIPS 202, SHA-3 Standard: Permutation-Based Hash
SHA3-512 and Extendable-Output Functions, August 2015
SHA-3 Extendable-Output Functions (XOFs) FIPS 202, SHA-3 Standard: Permutation-Based Hash
SHAKE128, SHAKE256 and Extendable-Output Functions, August 2015
FIPS 186-2 Appendix 3.1 and 3.2; ANS X9.62
Random Number Generator (RNG) algorithms
Appendix A.4
SP 800-90A, Recommendation for Random
Deterministic Random Bit Generators (DRBG) Number Generation Using Deterministic Random Bit
Generators
Keyed-Hash Message Authentication Code (HMAC) FIPS 198-1, The Keyed-Hash Message Authentication
using SHA-1, SHA-2 and SHA-3 Code (HMAC)
SP 800-38B, Recommendation for Block Cipher
Cipher-based Message Authentication Code (CMAC)
Modes of Operation: The CMAC Mode for 70
Mode for Authentication
Authentication
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

TABLE 2 (CONT): CRYPTOGRAPHIC ALGORITHMS & NIST TECHNICAL DOCUMENTS
(FIPS & SPs)
FEDERAL INFORMATION PROCESSING
CRYPTOGRAPHIC
STANDARD (FIPS), SPECIAL PUBLICATION
ALGORITHM/COMPONENT
(SP) OR OTHER REFERENCE DOCUMENT
SP 800-38C, Recommendation for Block
Counter with Cipher Block Chaining-Message
Cipher Modes of Operation: the CCM Mode for
Authentication Code (CCM) Mode
Authentication and Confdentiality
SP 800-38D, Recommendation for Block Cipher
GCM, Galois Message Authentication Code (GMAC), and
Modes of Operation: Galois/Counter Mode (GCM)
eXtended Packet Number (XPN) Modes
and GMAC
SP 800-38E, Recommendation for Block Cipher
XTS-AES Mode XOR–encrypt–XOR (XEX) Tweakable
Modes of Operation: The XTS-AES Mode for
Block Cipher with Ciphertext Stealing mode
Confdentiality on Block-Oriented Storage Devices
SP 800-38F, Recommendation for Block Cipher
Key Wrapping
Modes of Operation: Methods for Key Wrapping
SP 800-56A, Recommendation for Pair-Wise Key
DH and MQV Key Agreement Schemes and Key
Establishment Schemes Using Discrete Logarithm
Confrmation
Cryptography, dated March 2007
SP 800-56A, Key Derivation Functions for Key
All of SP 800-56A schemes without the Key Derivation
Agreement Schemes: All sections except Section
Functions (KDF)
5.8
SP 800-56A, Section 5.7.1.2 Elliptic Curve
SP 800-56A Section 5.7.1.2 ECC CDH function Cryptography Cofactor Dife-Hellman (ECC CDH)
Primitive Testing
SP 800-108, Recommendation for Key Derivation
Key-Based Key Derivation functions (KBKDF)
using Pseudorandom Functions
Application-Specifc Key Derivation functions (ASKDF)
(includes the KDFs used by Internet Key Exchange (IKE)
v1, IKEv2, Transport Layer Security (TLS), American SP 800-135 (Revision 1) Recommendation for
National Standard (ANS) X9.63-2001, Secure Shell (SSH), Existing Application-Specifc key Derivation
Secure Real-time Transport Protocol (SRTP), Simple Functions
Network Management Protocol (SNMP), and Trusted
Platform Module (TPM)
Component test – ECDSA Signature Generation of a hash
value (This component test verifes the signing of a hash- FIPS 186-4, Digital Signature Standard (DSS), and
sized input. It does not verify the hashing of the original ANS X9.62
message to be signed.)
Component test – RSA PKCS#1 1.5 Signature Generation
FIPS 186-4, Digital Signwature Standard (DSS),
of encoded message (EM) (This component test verifes
and Public Key Cryptography Standards (PKCS) #1
the signing of an EM. It does not verify the formatting of
v2.1: RSA Cryptography Standard-2002
the EM.)
SP 800-56B, Recommendation for Pair-Wise
Component test – RSA PKCS#1 Probabilistic Signature
Key Establishment Schemes Using Integer
Scheme (PSS) Signature Generation of encoded message
71 Factorization Cryptography, August 2009, Section
EM (This component test verifes the RSASP1 function.)
7.1.2
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

In the future, the CAVP expects to add algorithm The test requirements for SCAP 1.2 are defned
validation testing for: in NISTIR 7511, Security Content Automation
Protocol (SCAP) Version 1.2 Validation Program
• SP 800-38G, Recommendation for Block
Test Requirements. In general, vendors may opt for
Cipher Modes of Operation: Methods for
product validation for one or more SCAP capabilities
Format-Preserving Encryption;
or operating systems. Currently, the program ofers
testing on Microsoft Windows, Red Hat Enterprise
• SP 800-56C, Recommendation for Key
Linux, and Apple Mac OS platforms. The validation
Derivation through Extraction-then-Expansion;
process starts when a vendor voluntarily submits
• SP 800-132, Recommendation for Password- an SCAP-enabled product to an NVLAP-accredited
Based Key Derivation Part 1: Storage laboratory. Once the lab completes product testing,
Applications; and the lab submits a test report to the SCAP Validation
Program at NIST for review. NIST reviews the test
• SP 800-56A Revision 2, Recommendation for
report and awards a validation if all requirements
Pair-Wise Key Establishment Schemes Using
have been met. Once a validation is awarded, the
Discrete Logarithm Cryptography.
SCAP Validation Record is sent to the lab, and the
information about the newly validated product is
FOR MORE INFORMATION, SEE:
posted on the SCAP Validated Products web page.
https://csrc.nist.gov/projects/cryptographic-
Figure 26 illustrates the SCAP 1.2 Validation Process.
algorithm-validation-program
CONTACTS:
Mr. Harold Booth Ms. Elaine Barker
(301) 975-8441 (301) 975-2911
harold.booth@nist.gov elaine.barker@nist.gov
(Editors’ Note: Sharon Keller worked on this program
until her recent retirement.)
Security Content Automation
Protocol (SCAP) Validation Program
The SCAP Validation Program performs
conformance testing to ensure that products correctly
implement SCAP, as defned in SP 800-126 Revision 2,
Credit: Shutterstock/Rawpixel.com
The Technical Specifcation for the Security Content
Automation Protocol (SCAP): SCAP Version 1.2.
Computer monitor displaying
Conformance testing is necessary because SCAP is a
that a product has been tested.
complex collection of eleven individual specifcations
that work together to support various use cases. A
single error in product implementation could result
in undetected vulnerabilities or policy noncompliance
within an organization’s networks.
72
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

|     |     |             |     |     | SCAP 1.2 Validation  |                          |     |     | Process  |     |                           |     |     |
| --- | --- | ----------- | --- | --- | -------------------- | ------------------------ | --- | --- | -------- | --- | ------------------------- | --- | --- |
|     |     | ----------F |     |     |                      | 2  Vendor selects a lab  |     |     |          |     |                           |     |     |
|     |     |             |     |     |                      |                          |     |     |          |     | 3  Lab tests product for  |     |     |
and submits the
conformance to SCAP
|     |     |     | SCAP Product  |     |     | product for testing.  |     | NVLAP Accredited  |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --------------------- | --- | ----------------- | --- | --- | --- | --- | --- |
1.2 using the derived
|     |     |     | Vendor  |     |     |     |     |     | SCAP Lab  |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
test  requirements in
NIST IR 7511 and
(D
|     |     |     | Vendor develops SCAP  |     |     |     |     |     |     |     | completes a test  |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- |
report .
|     |     |     | enabled  | product and  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
uses the publicly
|     |     |     | available validation  |     |     | Lab submits the test  |          |     |                      |     |     |     |     |
| --- | --- | --- | --------------------- | --- | --- | --------------------- | -------- | --- | -------------------- | --- | --- | --- | --- |
|     |     |     | test content during   |     |     | reportto              | NISTfor  |     |                      |     |     |     |     |
|     |     |     | quality assurance     |     |     | validation.           |          |     |                      |     |     |     |     |
|     |     |     | testing.              |     |     |                       |          |     | of validation award  |     |     |     |     |
and sends the
validation record.
|     |     | ®   |                         |     |     |           |     | 0   |                        |     |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | --------- | --- | --- | ---------------------- | --- | --- | --- | --- |
|     |     |     | NI ST reviews the test  |     |     |           |     |     | NISTa dds the product  |     |     |     |     |
|     |     |     | report and awards       |     |     | NISTSCAP  |     |     |                        |     |     |     |     |
to the SCAP Validated
validation for products
|     |     |     |     |     |     | Validation  | Program  |     | Product list.  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | -------------- | --- | --- | --- | --- |
meeting the
requirements defined
in NIST IR 7511.
Figure 26: SCAP 1.2 Validation Process
All  resources  and  information  necessary  for  and fnd products that have been awarded validations.
preparing  products  for  SCAP  1.2  validation  are  The validation records that are posted on the SCAP
published on the SCAP Validation Program web page  Validated Products page identify the product versions
(see https://scap.nist.gov/validation). The most current  that were tested in the laboratory, along with details
NISTIR 7511 revision, as well as SCAP capabilities and  about each validation, such as the tested platforms,
supported platforms, are available on the home page  SCAP capabilities, the validation test suite version,
(see  https://scap.nist.gov/validation).  The  resources  and the lab that performed the product test.
|     | page  includes  |            | documentation,  |      | a  list  | of  Frequently   |     |     |            |         |       |               |     |
| --- | --------------- | ---------- | --------------- | ---- | -------- | ---------------- | --- | --- | ---------- | ------- | ----- | ------------- | --- |
|     |                 |            |                 |      |          |                  |     | In  | FY  2017,  | NISTIR  | 7511  | was  updated  | in  |
|     | Asked           | Questions  | (FAQ),          | the  | SCAP     | validation-test  |     |     |            |         |       |               |     |
preparation for testing conformance to SCAP 1.3,
|     | content,  | and  | tools  for  | validating  |     | and  processing  |     |     |     |     |     |     |     |
| --- | --------- | ---- | ----------- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
and the validation test content was updated to
SCAP data streams. The SCAP validation-test content
include test coverage for SCAP 1.3 and support for
|     | should  | be  used  | by  | vendors  | for  | quality  assurance  |     |     |     |     |     |     |     |
| --- | ------- | --------- | --- | -------- | ---- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
new platforms. Support for Microsoft Windows 10
testing prior to entering formal SCAP testing with an
and Mac OS 10.11 was released in FY 2017; updates
NVLAP-accredited laboratory. The open-source tools
for SCAP 1.3 will be released in FY 2018.
that are available for download may be used by SCAP
content authors for testing the SCAP source content.  Vendors continued to beneft from the openly
The SCAP Content Validation Tool (SCAPVal) may  available  SCAP  validation  test  suite  reference
material. Access to the validation test suite enables
be used to determine if the content conforms to the
SCAP  specifcation.  SCAP  validated  products  may  vendors to test products during development and
provides a means for verifying SCAP conformance
be used to process SCAP data streams for use cases
after operational products are patched. Through the
such as checking compliance of target systems to a
use of the reference materials, vendors that market
confguration checklist.
|     |     |     |     |     |     |     |     | their  | products  | to  federal  | agencies  | may  | better  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------------ | --------- | ---- | ------- |
End  users  may  use  information  on  the  SCAP  prepare for formal validation testing with NVLAP
| 73  |     |     |     |     |     |     |     | accredited  | laboratories.  |     | Vendors  | focused  | on  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | -------- | -------- | -------- |
Validation web page to learn about SCAP validation
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

critical infrastructure, and for which formal validation Contractors. There are three companion technical
testing may not be required, have access to reference documents:
material that ensures that scanning products are
1. SP 800-73, Interfaces for Personal Identity
correctly processing SCAP content. Approximately
Verifcation;
86 % of confguration scanning products are SCAP-
validated, and SCAP product vendors continue to
2. SP 800-76, Biometric Specifcations for
engage with the SCAP Validation Program on new
Personal Identity Verifcation; and
releases of the validation test content. The current list
of SCAP 1.2-validated products may be found on the 3. SP 800-78, Cryptographic Algorithms and Key
SCAP Validated Products list at https://nvd.nist.gov/ Sizes for Personal Identity Verifcation.
scap/validated-tools.
The two main products are: the PIV Card
In FY 2018, NISTIR 7511 for SCAP 1.3 and the Application and the PIV Middleware. The guidelines for
associated validation test suite reference material will performing the conformance tests for these products
be released. In addition, the program will continue to are themselves outlined in two technical documents
add support for new platforms (i.e., Windows Server (SP 800-85A, PIV Card Application and Middleware
2016 and Mac OS 10.12). The program will continue Interface Test Guidelines (SP 800-73-4 Compliance),
to collaborate with vendors, laboratories, and the and SP 800-85B, PIV Data Model Test Guidelines);
Security Automation team on updating validation they specify a two-step process that frst involves
resources in a meaningful way that meets the needs the development of Derived Test Requirements
of federal agencies and the critical infrastructure. (DTRs) and then the actual test procedures. To
Coordination with the Security Automation team implement these tests and to generate conformance
ensures that validation resources are developed and test reports, CSD also developed test modules for
released in conjunction with new releases of SCAP. testing the PIV card application and PIV middleware.
These modules were provided to NPIVP test facilities
FOR MORE INFORMATION, SEE:
for testing and certifying the vendor submissions in
https://scap.nist.gov/validation/ the two PIV product categories. NPIVP test facilities
are Cryptographic and Security Testing (CST)
CONTACT:
Laboratories that were accredited by the NVLAP.
Mr. Michael Cooper NPIVP also assisted NVLAP in the accreditation
(301) 975-8077 of laboratories by developing technology-focused
michael.cooper@nist.gov assessment criteria. An additional software module to
perform conformance testing for the PIV data model
(Editors’ Note: Melanie Cook supported this program was also developed by CSD to enable GSA to provide
until her recent departure from NIST.) a toolkit to agencies for testing fully personalized PIV
cards prior to card issuance.
FIPS 201 specifes the architecture and technical
IDENTITY AND ACCESS
requirements for the PIV cards. Since the start of the
MANAGEMENT NPIVP, FIPS 201 has undergone two revisions and the
companion technical documents even more revisions.
The two test guidelines documents have also been
NIST Personal Identity Verifcation updated to be consistent with the specifcation
documents. The NPIVP team was fully involved in the
Program (NPIVP)
review, analysis and development of these revisions
The objective of the NIST Personal Identity of specifcation documents and have also ensured
Verifcation Program (NPIVP) is to validate Personal that these revisions are fully refected in the two test
Identity Verifcation (PIV) products for conformance guidelines documents as well as in the test software
to the specifcations in FIPS 201, Personal Identity modules. The latest versions of all documents (as of
Verifcation (PIV) of Federal Employees and September 2017) with their URLs, as well as the URL 74
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

for the list of accredited NPIVP labs are given below: and inconsistencies in software codes performing
the same functionality and to make the maintenance
Specifcation Documents:
of the overall toolkit much easier. Further tests
pertaining to diferent card interfaces (Contact,
• FIPS 201-2, Personal Identity Verifcation (PIV)
Contactless, Secure Messaging and Virtual Contact)
of Federal Employees and Contractors – (see
for the same command were grouped together for
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.
easy accessibility. The redesigned test toolkit (now
FIPS.201-2.pdf)
called the SP 800-73-4 PIV Test Runner for PIV
Card Applications, Middleware and Data Model) has
• SP 800-73-4 Parts 1-3, Interfaces for
been made freely available to the public and can be
Personal Identity Verifcation (see https://doi.
downloaded at https://csrc.nist.gov/Projects/NIST-
org/10.6028/NIST.SP.800-73-4)
Personal-Identity-Verifcation-Program/Software-
• SP 800-76-2, Biometric Specifcations for Downloads.
Personal Identity Verifcation (see https://doi.
NPIVP’s PIV Card Application Validation List
org/10.6028/NIST.SP.800-76-2)
is available at https://csrc.nist.gov/Projects/NIST-
• SP 800-78-4, Cryptographic Algorithms and Personal-Identity-Verifcation-Program/Validation-
Key Sizes for Personal Identity Verifcation Lists/PIV-Card-Application-Validation-List.
(see https://doi.org/10.6028/NIST.
The PIV Middleware Validation List is available at
SP.800-78-4)
https://csrc.nist.gov/Projects/NIST-Personal-Identity-
Test Guidelines Documents: Verifcation-Program/Validation-Lists/SP-800-73-4-
PIV-Middleware-Validation-List.
• SP 800-85A-4, PIV Card Application and
Middleware Interface Test Guidelines (SP During FY 2017, fve PIV card application products
800-73-4 Compliance) (see https://doi. were certifed and validated.
org/10.6028/NIST.SP.800-85A-4)
FOR MORE INFORMATION, SEE:
• Draft SP 800-85B-4, PIV Data Model Test
https://csrc.nist.gov/Projects/NIST-Personal-Identity-
Guidelines (see https://csrc.nist.gov/CSRC/
Verifcation-Program
media/Publications/sp/800-85b/4/draft/
documents/sp800_85b-4_draft.pdf) CONTACTS:
Dr. Ramaswamy Chandramouli
List of Accredited NPIVP Labs
(301) 975-5013
mouli@nist.gov
As of September 2017, there are six accredited
NPIVP labs (see https://csrc.nist.gov/projects/nist-
Ms. Hildegard Ferraiolo
s-personal-identity-verifcation-program/testing-
(301) 975-6972
facilities).
hildegard.ferraiolo@nist.gov
During FY 2017, NPIVP did a major redesign of the
test software modules. The three software modules
for PIV card application conformance testing, PIV
Middleware conformance testing and PIV data model
conformance testing were all integrated into a single
comprehensive toolkit to eliminate redundancies
75
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

Personal Identity Verifcation (PIV) issuance and use of PIV Credentials on mobile
devices using commercial technologies. For
more information visit https://nccoe.nist.gov/
projects/building-blocks/piv-credentials.
• Coordinated cybersecurity-related updates
with vendors, departments and agencies to
ease migration to stronger cryptography for
identity credentials and for a PIV system that
produces, manages, and uses the credential
-- to include the sunset of the Triple Data
Encryption Algorithm (TDEA), the upgrade
to Deterministic Random Number Generator
(DRBG).
In FY 2018, CSD will continue to focus on updating
the relevant publications associated with FIPS 201-2,
including fnalizing SP 800-116 Revision 1. CSD will also
Figure 27: Government Employees Use
continue to provide technical and strategic inputs to
PIV Cards for Facility Access
the PIV-related initiatives.
In response to Homeland Security Presidential FOR MORE INFORMATION, SEE:
Directive-12 (HSPD-12), Policy for a Common
https://csrc.nist.gov/projects/piv
Identifcation Standard for Federal Employees
and Contractors, the following NIST standard was CONTACTS:
developed, FIPS 201, Personal Identity Verifcation
Dr. Ramaswamy Chandramouli
(PIV) of Federal Employees and Contractors. FIPS
(301) 975-5013
201 was approved by the Secretary of Commerce in
mouli@nist.gov
February 2005. HSPD-12 called for the creation of a
new identity credential for federal employees and
Ms. Hildegard Ferraiolo
contractors. FIPS 201 is the technical specifcation for
(301) 975-6972
both the PIV identity credential and the PIV system
hildegard.ferraiolo@nist.gov
that produces, manages, and uses the credential.
Within NIST’s ITL, this work is a collaborative efort of
the CSD and the IAD. CSD activities in FY 2017 directly Access Control and Privilege
supported the latest revision of FIPS 201 (i.e., FIPS 201- Management
2) by updating the relevant publications associated
with FIPS 201-2 and by initiating implementations With the advance of the current computing
of the credential on mobile devices. CSD performed technologies and the diverse environments in which
the following activities during FY 2017 in support of they are used, access control issues, such as situational
HSPD-12: awareness, trust management, the preservation
of privacy, and privilege-management systems,
• Coordinated with the revision team in the
are becoming increasingly complex. This project is
ACD to update SP 800-63, titled The Digital
intended to provide practical and conceptual guidance
Identity Guidelines, and ensured close
for these issues.
alignment with the PIV Standard in areas of
enrollment, identity proofng, authentication In FY 2017, the following activities were
and credential lifecycle management. accomplished:
• With industry CRADA partners, built sample • Published a conference paper: Access Control
solutions at the NCCoE to demonstrate the for Distributed Processing Systems: Use Cases 76
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

and General Considerations, which discussed  of shared resources and common trust-
fundamental requirements as well as some  management schemes;
general access control implementations for
•   Provide guidance for implementing AC
distributed system environments.
models and mechanisms for standalone or
•   Continued working on attribute considerations  network systems;
for access mechanism implementation; the
•   Increase the security and safety of static
results will be presented in the internal draft of
(connected) distributed systems by applying
a NIST SP, Attribute Consideration for Access
the testing and verifcation tool for the AC
Control Systems (no publication number has
policies;
been assigned to this internal draft SP), which
is scheduled to be released during FY 2018).
•   Assist system architects, security
administrators, and security managers whose
•   Added new functions in NIST’s Access Control
expertise is related to AC or privilege policy
Policy Tool (ACPT) for efciently combining
in managing their systems and in learning the
access control policies for systems that require
limitations and practical approaches for their
multi-policy access control.
applications; and
•   Researched a general Access Control (AC)
•   Provide accurate and efcient fault detection
framework for distributed systems, including
and correction technology for implementing
Big Data, Cloud, IoT, and the Smart Grid.
AC rules and policies.
In FY 2018, CSD will continue the above research.
|     |     |     | Figure  28   | illustrates  | the  | application  | of  AC  |
| --- | --- | --- | ------------ | ------------ | ---- | ------------ | ------- |
CSD expects that this project will:
|                                              |     |     | and  privilege  | management  | within  | and  | among  |
| -------------------------------------------- | --- | --- | --------------- | ----------- | ------- | ---- | ------ |
| •   Promote (or accelerate) the adoption of  |     |     | organizations.  |             |         |      |        |
community computing that utilizes the power
| Gov'tOrg.A     | Gov'tOrg.B     | Gov'tOrg.C     |     |     |     | Environmental  |     |
| -------------- | -------------- | -------------- | --- | --- | --- | -------------- | --- |
| Authoritative  | Authoritative  | Authoritative  |     |     |     | Conditions     |     |
| Attribute      | Attribute      | Attribute      |     |     |     |                |     |
| Store          | Store          | Store          |     |     |     |                |     |
Policy
Decision
|     |     |     |     | Web  | Point (PDP)  |     |     |
| --- | --- | --- | --- | ---- | ------------ | --- | --- |
lnformaton
Portal Sevrer
Responseto  ResourcRe equesrA
Rtsponst to Rtsourct Rtqutst 8
| Aurlioriud Access to Rtsourct  |                                    |                                     |     |     | Policy Enforcement  |     |     |
| ------------------------------ | ---------------------------------- | ----------------------------------- | --- | --- | ------------------- | --- | --- |
|                                | Autllori7edA ccesst o Rl'"-O(JKf'  | Respomf' to Rt'i.ourceR eq,~'i.t C  |     |     |                     |     |     |
|                                |                                    | Autlwrized Acc,m to Resource        |     |     | Point (PEP)         |     |     |
| Gov'tOrg . A                   | Gov'tOrg . B                       | Gov't Org.C                         |     |     |                     |     |     |
| User Terminals                 | User Terminals                     | User Terminals                      |     |     |                     |     |     |
| Integrated w/ Web              | Integrated w / Web                 | Integrated w/ Web                   |     |     |                     |     |     |
Resource
| Information Portal  | Information Portal  | Information Portal  |     |     |     |     |     |
| ------------------- | ------------------- | ------------------- | --- | --- | --- | --- | --- |
| GUI/Client          | GUI/Client          | GUI/Client          |     |     |     |     |     |
| Application         | Application         | Application         |     |     |     |     |     |
|                     | ResourceR equtstB   | Refoutce RequtstC   |     |     |     |     |     |
ResourceR equesrA
77
Figure 28: Access Control and Privilege Management
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

CONTACTS: the verifcation or test processes to generate fault
reports. Even though correct verifcation is achieved,
Dr. Vincent Hu Mr. David Ferraiolo
and counter-examples may be generated when faults
(301) 975-4975 (301) 975-3046
are found, those methods provide no information
vhu@nist.gov david.ferraiolo@nist.gov
about the source of faults that might allow conficts
in privilege assignment, the leakage of privileges, or
Mr. Rick Kuhn
(301) 975-3337 a confict-of-interest in permissions. The difculty in
kuhn@nist.gov fnding the source of faults is increased, especially
when the AC rules are intricately covering duplicated
variables to a degree of complexity. The complexity is
Conformance Verifcation for Access
because a fault might not be caused by one particular
Control Policies access rule but by multiple rules that confict. Thus, it
requires manually analyzing each rule in the policy to
Access control (AC) systems are among the
fnd the correct solution for correcting the fault.
most critical network security components. Faulty
policies, misconfgurations, or faws in software To address the issue, CSD developed the ACPT,
implementation can result in serious vulnerabilities. shown in Figure 29, which allows a user to compose,
The specifcation of AC policies is often a challenging verify, test, and generate access control policies. CSD
problem. Often, a system’s privacy and security also researched the AC Rule Logic Circuit Simulation
are compromised due to the misconfguration of (ACRLCS) technique, which enables the AC authors to
AC policies, instead of the failure of cryptographic detect a fault when the fault-causing AC rule is added
primitives or protocols. This problem becomes to the policy, so the fx can be implemented in real
increasingly severe as software systems become time before adding other rules that further complicate
more and more complex, and are deployed to the detecting efort, rather than checking by retracing
manage a large amount of sensitive information the interrelations between rules after the policy is
and resources that are organized into sophisticated completed.
structures. Identifying discrepancies between policy
In FY 2017, CSD accomplished the following:
specifcations and their intended properties is crucial
because the correct implementation and enforcement
• Published SP 800-192, Verifcation and Test
of policies by applications is based on the premise that
Methods for Access Control Policies/Models,
the policy specifcations are correct. As a result, policy
an article, Access Control Policy Verifcation
specifcations must undergo rigorous verifcation and
in IEEE Computer, and a conference paper,
validation through systematic testing to ensure that
Diferentiation Non-Isomorphic Graphs for
the policy specifcations truly encapsulate the desires
Graph Analytics;
of the policy authors.
• Enhanced the capability of ACPT by including
To formally and precisely capture the security
additional functions for the specifcations
properties that AC should adhere to, access control
of subject inheritance, separation of duty
models are usually written to bridge the rather wide
requirements, and better user interfaces for
gap in abstraction between policy and mechanism.
policy model specifcation;
Thus, an AC model provides unambiguous and precise
expression as well as a reference for the design and • Enhanced the usability and fxed bugs of the
implementation of security requirements. Techniques ACRLCS (the Access Control Rule Logic Circuit
are required for verifying whether an AC model is Simulation System) to provide more policy
correctly expressed in the AC policies, and whether composing and user interface capability for
the properties are satisfed in the model. policy fault detection;
Most research on AC model or policy verifcation • Supported two Small Business Innovation
techniques is focused on one particular model, and Research (SBIR) Phase II projects for the
almost all of the research is in applied methods, which access control tool and embeded function 78
require the completed AC policies as the input for developments; and
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

GU/allows
specificatfon of users,
user attributes,
actions, resources,
Access Control Policy Tool resources attributes,
.-----------------+-------....-.-.-..-..
and properties
---
GUI
Templates indude.­
ABAC, World/ow, and
Multi-Level
Generates encoded
AC Model Templates Model XACML policy
......................................0...i.ns.ta. .n.ce. ....
Validates models Model Checker LJ
against properties
~-------~ Generates test
swtes
Generates -- -+--+-• Combinatorial {~~
combinatorial test Array Generator ~--~_:_~t_e sr_~;__!e_r_~ ·································· I
array
Figure 29: Access Control Policy Tool (ACPT)
• Worked with industrial and academic Figure 29 shows the system architecture of the
rganizations in exploring new capabilities that NIST ACPT, which allows access control policy authors
helped to improve the usability of the AC tools to compose, verify, and test access control policy
(ACPT and ACRLCS), resulting in additional implementation.
usage; ACPT was downloaded by 475 users
Figure 30 provides an example of access control
and organizations.
rule implementation in ACRLCS, which allows the
In FY 2018, CSD is planning to conduct further online detection of access control rule composition
research on efcient testing technology, develop new faults.
capabilities, and to enhance the performance of the
ACPT and ACRLCS.
Tu
In
To
In
Top Secret Permission
So
In
Cu
In
Read
In
Co
In
Confidential Permission
79
Figure 30: Access Control Rule Implementation
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

This project is expected to: to perform a set of operations is determined by
evaluating the attributes associated with the subject,
• Provide a generic paradigm and framework of
object, requested operations, and, in some cases,
access control model/property conformance
environmental conditions against policy, rules, or
testing;
relationships that describe the allowable operations
for a given set of attributes. For example, access to a
• Provide templates for specifying access
database could be restricted to users with particular
control rules in popular access control models,
attributes, such as membership in a group (e.g.,
such as the Attribute Based, Multi-level, and
employees) and other conditions (e.g., part of the
Workfow models;
Human Resource Department). ABAC represents a
• Provide tools or services for checking the point on the spectrum of logical access control, from
security and safety of an access control simple access control lists to more capable Role Based
implementation, policy combination, and Access Control (RBAC), and fnally, to a highly fexible
eXtensible Access Control Markup Language method for providing access based on the evaluation
(XACML) policy generation; of attributes.
• Promote (or accelerate) the adoption of CSD is conducting research that provides
combinatorial testing for large-system testing information for using ABAC to improve information
(such as an access control system); sharing within and among organizations based on the
planning, design, implementation, and operational
• Promote the concept of detecting AC policy
considerations. The research also includes technologies
faults in real-time AC rule composing;
such as attribute assurance, attribute engineering/
management, identity system integration, attribute
• Provide an innovative method for specifying
federation, situational awareness (real-time or
AC rules formed by Boolean logic expressions
contextual) mechanisms, policy management, and
operated on variables of AC rules;
natural-language policy translation to digital policy.
• Provide techniques for preventing faults in Figure 31 illustrates the interaction of many of these
enforcing fundamental security properties, components.
including Cyclic Inheritance, Privilege
The goal of this research is to improve information
Escalation, and Separation of Duty; and
sharing, while maintaining control of that information
• Provide new methods for composing standard for federal agencies.
mandatory AC models, such as Attribute
In FY 2017, the project team:
Based Access Control (ABAC) and Multi-Level
Security (MLS) as well as some fundamental
• Published the book Attribute-Based Access
security properties.
Control by Artech House. The book contains
discussions covering almost all aspects of
FOR MORE INFORMATION, SEE:
ABAC;
https://csrc.nist.gov/projects/access-control-policy-
tool • Published a conference paper: Verifcation of
Resilience Policies that Assist Attribute Based
CONTACTS:
Access Control. The paper presents research
Dr. Vincent Hu Mr. Rick Kuhn results of access privilege blocking and
(301) 975-4975 (301) 975-3337 privilege leaking; and
vhu@nist.gov kuhn@nist.gov
• Worked with government, industry and
academic organizations in exploring diverse
Attribute Based Access Control
models (e.g., Next Generation Access Control
- NGAC) and applications (e.g., distributed
Attribute Based Access Control (ABAC) is a logical
systems: Cloud, Bigdata, IoT applications) of 80
access control methodology where an authorization
ABAC.
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

Enterprise Access Control
|     |                          | ~ Enterprise         |                       |                              | Policy Repository          |        |
| --- | ------------------------ | -------------------- | --------------------- | ---------------------------- | -------------------------- | ------ |
|     | ....v ~                  | olicy Manager        | LocalA ccessC ontrol  |                              |                            |        |
|     | ~                        |                      |                       |                              | ~------                    |        |
|     |                          | ,                    | PolicyR               | epository  , ,               |                            |        |
|     |                          | I                    |                       | ,,  ,                        |                            |        |
|     |                          | ~                    |                       | ~,,'  Hierarchical Policy    | Enterprise Access Control  |        |
|     |                          |                      |                       | Pushed to Subordinate        | Policy Administration      | Point  |
|     |                          | Optional Enterprise  |                       | <-_ _ ---Or-ga-niz-at-ion-s  |                            |        |
|     | Policy Decision Service  |                      |                       |                              | ---                        |        |
~-------
|     | Enterprise Identity/  |     |     |     |     | 1   |
| --- | --------------------- | --- | --- | --- | --- | --- |
I
|     | Credential Manager  |     | '   |              |                              |     |
| --- | ------------------- | --- | --- | ------------ | ---------------------------- | --- |
|     |                     |     | '   |              | Local Access Control Policy  | 1   |
|     |                     |     |     | Environment  | Administration  Point        |     |
\
|     | \   | Credenital lnssuance  |     | Conditions  |     |     |
| --- | --- | --------------------- | --- | ----------- | --- | --- |
\
Subject  \
\  Object
Attribute Issuance  \
\  -----+
\
\
A  Optional Enterprise
\  1
|     | \   | Subject  |     |     | :  Object Attribute Binding  |     |
| --- | --- | -------- | --- | --- | ---------------------------- | --- |
|     | \   |          |     |     | V I  and Validation Service  |     |
ABAC"
|     | ~                   |     |          |     | i i   |     |
| --- | ------------------- | --- | -------- | --- | ----- | --- |
|     |                     |     | Access   |     | ~     |     |
|     | Enterprise Subject  |     | Control  |     |       |     |
I,:.,,~
|     | Attribute             |                        | Mechanism  |                 |                     |     |
| --- | --------------------- | ---------------------- | ---------- | --------------- | ------------------- | --- |
|     | Administration Point  |                        |            |                 | ~                   |     |
|     | Enterprise Subject    |                        |            |                 | Enterprise Object   |     |
|     | Attribute  Sharing    |                        |            |                 |                     |     |
|     |                       |                        |            |                 | Attribute  Manager  |     |
|     |                       | ,. , ,7 LocalS ubject  |            | Object  '{",,,  |                     |     |
|     |                       | '  Attribute           |            | Attribute       |                     |     |
Set of Available
|     |     | Repository  |           | Repository    |     |     |
| --- | --- | ----------- | --------- | ------------- | --- | --- |
|     |     |             | Attribute | s for Policy  |     |     |
Development
|     |     |     |     | I   | Local Object Attribute  |     |
| --- | --- | --- | --- | --- | ----------------------- | --- |
Local Subject Attribute  ____________________A_d_m_in_is_tr_at_io_n_ _P_oi_nt_ _
JI
Administration Point
Figure 31: ABAC Access Control Mechanism Chart
In FY 2018, CSD will continue the research of ABAC  •   Assist ABAC administrators in establishing or
formal models, as well as the details and extended  refning business processes to support ABAC;
| topics  | of  ABAC  capabilities,  | such  | as  attribute  |     |     |     |
| ------- | ------------------------ | ----- | -------------- | --- | --- | --- |
•   Promote the adoption of ABAC for a more
| considerations,  | ABAC  implementation  |     | examples,  |     |     |     |
| ---------------- | --------------------- | --- | ---------- | --- | --- | --- |
secure and fexible method for information
ABAC mechanisms, and ABAC standards. The ABAC
sharing in a standalone or enterprise
project will pursue the following objectives:
environment; and
•   Provide readers with an overview of the
•   Provide testing methods for ABAC policy and
current state of logical access control,
implementations.
a working defnition of ABAC, and an
explanation of the core and enterprise ABAC
FOR MORE INFORMATION, SEE:
concepts;
https://csrc.nist.gov/projects/abac/
•   Assist security policy makers in establishing a
CONTACTS:
business case for ABAC implementation and
acquiring an interoperable set of capabilities;  Dr. Vincent Hu     Mr. David Ferraiolo
|     |     |     |     | (301) 975-4975    | (301) 975-3046   |     |
| --- | --- | --- | --- | ----------------- | ---------------- | --- |
•   Assist ABAC developers in developing  vhu@nist.gov      david.ferraiolo@nist.gov
the operational requirements and overall
| enterprise architecture;  |     |     |     | Mr. Rick Kuhn   |     |     |
| ------------------------- | --- | --- | --- | --------------- | --- | --- |
(301) 975-3337
81
kuhn@nist.gov
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

Trusted Identities Program and to align with international standards. One of
the most signifcant updates is replacing levels of
By promoting the government and commercial assurance with three individual components of the
adoption of privacy-enhancing, secure, interoperable, digital identity fow for more fexibility in design and
and easy-to-use digital identity solutions, ACD works operations: the identity, authenticator, and federation
alongside its partners to drive trust, convenience, and assurance levels. Identity proofng was also updated
innovation in the marketplace of identity solutions to further mitigate the potential for mass breaches of
(see https://www.nist.gov/itl/tig). ACD is committed personal information.
to advancing measurement science, technology, and
Over the course of a year, the document evolved
standards adoption to improve digital identity for
with the help of the community. For this revision,
individuals and organizations alike.
GitHub was used to interact in near-real-time with
In FY 2017, the Trusted Identities Program was a the community and received a tremendous response:
key participant and driving force in the digital identity over 1,400 comments were submitted, and the web
arena for NIST’s National Cybersecurity Center of version of the publication drew over 74,000 unique
Excellence (NCCoE). Many identity-related projects visitors between May 2016 and May 2017. ACD will
initiated at the NCCoE leveraged the technical continue to use this approach in the future during the
expertise and experiences of, and the foundational development of new volumes and document revisions.
guidelines and practices issued by, ACD and NIST’s
broader identity program.
International Standards Alignment
Through these collaborative eforts, projects
this year focused on driving the adoption of trusted ACD, the United Kingdom Cabinet Ofce, and the
identities through digital identity standards, including Canada Treasury Board have been collaborating to
for federal agencies. NIST also engaged the community compare national frameworks for identity assurance
on standards and guidelines development, including with the intention of creating a broad and competitive
issuing SP 800-63-3, Digital Identity Guidelines, global market for identity solutions and enabling
collaborating with other countries to advance high- cross-border credential interoperability. Building on
assurance online identity standards, and participating recent updates to guidance documents like NIST’s
in the OpenID Foundation and Fast Identity Online SP 800-63-3 and the UK’s Good Practice Guides,
(FIDO) Alliance. the group made several recommendations for the
International Organization for Standardization’s
ACD also focused on building trust in digital
(ISO’s) suite of identity standards. These
identity technologies by advancing measurement
recommendations included the development of a new
science in the identity space—which included
standard that provides an overall approach to identity
measuring the strength of authenticators and
and authentication risk management and assurance;
evaluating attribute metadata. The team also
organizations could leverage this when developing
continued work with numerous external partners
their models for assessing and managing identity-
through trusted identities pilots, seeding the market
based risks and threats.
with innovative technologies and providing solutions.
The group also recommended refocusing ISO/IEC
29115, Entity Authentication Assurance Framework, to
address authentication threats and risks exclusively.
Updated Digital Identity Guidelines
These updates should contain a threat model, controls
In June of 2017, ACD fnalized the latest revision and mitigations, and guidance on how these can
to SP 800-63-3, which covers digital identity from be combined to achieve defned risk management
initial risk assessment to deployment of federated outcomes for authentication events.
identity solutions. Digital identity in both agencies
NIST staf members served as the Federal
and the market place have changed dramatically
Government lead for all activities in the (Fast IDentity
since the publication’s last revision in 2013; the latest
82
Online) FIDO Alliance, which focuses on creating
update was designed to give agencies more options
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

strong authentication specifcations to create an ACD has advanced trusted digital identity
identity ecosystem. During 2017, ACD participation solutions by building partnerships that stem from
included active membership and contribution in the trusted identities pilots. These pilots develop
technical and privacy working groups, as well as and deploy technology, models, and frameworks
international plenary participation in Hong Kong, that would not otherwise exist in the marketplace,
Vancouver, Madrid, and Sydney. and have impacted more than 8.8 million individuals
to date. In FY 2017, the pilots made remarkable
Additionally, ACD supported standardization
progress: the 24 projects now involve more than 190
eforts including iGov (see https://openid.net/wg/
partner organizations across 12 sectors — including
igov). The iGov is working toward an OpenID Connect
the development or deployment of 16 multi-factor
specifcation that will enable users to authenticate and
authentication solutions.
share consented attribute information with public-
sector services across the globe. The resulting profle In FY 2018, NIST, through the NCCoE, will fully
will enable standardized integration with public-sector integrate identity management standards, best
relying parties (RPs) in multiple jurisdictions. practices, and technical approaches into projects that
are foundational to the work of the NCCoE and many
of its stakeholders and projects, including the Internet
Authenticator Strength of Function of Things. The project will also continue to advance
the digital identity marketplace by collaborating with
NIST is working to produce a framework
partners on measurement science, technology, and
for evaluating and comparing the strength of
standards adoption, and develop guidance to meet
authentication solutions, starting with the Strength of
today’s digital identity needs.
Function for Authenticators – Biometrics (SOFA-B).
The team began with a focus on biometrics, due to FOR MORE INFORMATION, SEE:
the increased availability of biometric solutions in the
https://www.nist.gov/itl/tig
consumer space and the need for improved security
guidance regarding the use of those solutions as CONTACTS:
authenticators. The end goal is a framework to
Dr. Nelson Hastings
assess and combine authentication technologies, as
(301) 975-5237
well as to compare biometrics’ efectiveness to that
nelson.hastings@nist.gov
of passwords and other authenticators. Using the
SOFA-B framework, RPs will be able to determine
Ms. Kristina Rigopoulos
the overall strength of biometric authentication, (202) 309-4791
considering matching performance, presentation
kristina.rigopoulos@nist.gov
attack detection, and the efort required to break – or
spoof – a system.
(Editors’ Note: Paul Grassi supported this program
until his recent departure from NIST.)
With the draft of NISTIR 8112: A Proposed Schema
for Evaluating Federated Attributes, the TIG aims to
give RPs greater insight into how attributes assist
with risk-based business decision-making. RPs can RESEARCH IN EMERGING
examine this metadata and determine if they have
TECHNOLOGIES
the confdence they need in the attribute value before
making an authorization decision. This NISTIR is being
treated like an implementers’ draft, an approach
Secure Development Toolchain
focused on real-world implementation results and
lessons learned before fnalizing the document. ACD Competitions
plans to advance SOFA-B and attribute metadata
eforts to their next stages in FY 2018. Many security weaknesses in federal information
systems stem from software security vulnerabilities
83
Innovative Digital Identity Solutions induced by software faws present in current-
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

generation software products. CSD tracks software sets. Through the demonstration of security-faw
security vulnerabilities (in the National Vulnerability avoidance in a time-constrained setting, CSD will seek
Database), and seeks techniques for the measurement to show that wide-scale improvements in the overall
of security vulnerabilities and techniques that reduce security of software products can be realized without
the impact and prevalence of security vulnerabilities sacrifcing a time-to-market goal. The competitions,
in newly developed products or in new versions of which will be open to all interested parties, will aim
existing products. to provide consistent application and measurement
of commercial and research software development,
One approach to reducing the number of
composition, and reuse techniques.
security vulnerabilities in software is to improve the
development tools that are available. By identifying In FY 2017, CSD personnel documented the
languages and software development tools that Toolchain Infrastructure (TCI) in a collection of
support a reduction of vulnerabilities, and by documents that included a concept of operations,
stimulating the creation of better tools and tool system design specifcation, and administrator’s
usage techniques, the approach has the potential and users guides. These documents helped inform
to help developers produce applications with fewer the development of a python-based prototype of
vulnerabilities. While it is impossible to assure the the TCI. The prototype development efort included
total absence of security vulnerabilities in this way, it automated unit test scripts for the TCI and the
might well be possible to rule out specifc, signifcant confguration and deployment of the TCI hardware.
classes of vulnerabilities that currently provide the The team also refned a selected challenge problem
basis for many serious exploits. by updating the problem descriptions, requirements,
and test cases; and developed an exemplar challenge
CSD is developing an empirical, competitive
problem solution in python.
approach to fnding the most efective and usable
combinations of tools to produce software systems In FY 2018, CSD plans to complete the
that are relatively free of exploitable vulnerabilities. development and testing of the TCI prototype. The
Multiple competitions are planned that will be based team will enhance the prototype to further improve
on an idea developed during the Designing a Secure its reliability and reproducibility, perform extensive
Systems Engineering Competition Workshop that was testing of the TCI, and publicly announce the frst
conducted by the National Science Foundation in toolchain competition.
2010. The workshop proposed a competition for the
CONTACTS:
development of a set of tools to help non-security-
expert developers to rapidly build a signifcant Mr. Lee Badger Mr. Christopher Johnson
application with zero vulnerabilities, as detected by (301) 975-3176 (301) 975-3247
an extensive public test suite. lee.badger@nist.gov christopher.johnson@nist.gov
The participants in the planned competitions
Networks of Things
will implement software systems to solve challenge
problems using software development tool chains
The Internet of Things (IoT) increasingly appears
(“toolchains”) of their own choosing, within specifed
to be the next great technology revolution. It is
time periods. The toolchains will be free to include
expected to impact everything from healthcare
existing technologies (e.g., existing software libraries
delivery, to how food is produced, to how we work, to
and frameworks, code generators, reusable source
all forms of transportation and communication, and
code, or bug-fnding tools), novel technologies, or
to virtually all forms of automation. IoT will impact
any combination thereof. Each competition will apply
everyone, and in multiple ways.
time pressure by simulating a deadline in the software
development process, increasing the likelihood of
With a technology revolution of such large impact
an introduction of security faws. The objective of
on society, it is imperative that IoT-based systems
the toolchains will be to detect or prevent security
can be trusted. This means that they should exhibit
faws while still supporting the quick-paced software secure, reliable, and private behaviors as well as many 84
development of applications with rich feature
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

other attributes associated with quality. Privacy is Operations Research and the Management Sciences
particularly important because IoT-based systems (INFORMS) meeting in Dallas, Texas, he referred to
will likely produce huge amounts of data as a result a cloud as an important new “computing paradigm
of sensing and surveillance. This is the “big data” where the boundaries of computing will be determined
challenge associated with IoT. Therefore, techniques, by economic rationale rather than technical limits
tools, and methods to mitigate the numerous “trust” alone.” The international IT literature and media later
challenges are needed before these automated IoT- provided many defnitions, models, and architectures,
based networks manage much of daily life. but it was not until 2011, when NIST published SP 800-
145, The NIST Defnition of Cloud Computing, that the
In July 2016, NIST released SP 800-183, Networks
world coalesced on the cloud deployment and service
of ‘Things’, which addressed the question: “What is the
models, defnitions and descriptions provided in SP
science, if any, underlying IoT?” After releasing that
800-145.
document, NIST has begun to look at how to apply
the principles in the document in a practical setting, Following the December 2010 Federal
with a focus on healthcare. NIST has also looked at Government’s “Cloud First” policy issued as part of
the security and privacy of virtual assistants, and how the 25-point plan for the U.S. Federal Government’s
a network of things with low inherent testability can (USG) IT modernization and reform, NIST assumed
be tested. a technical leadership role for the federal agencies’
eforts related to the adoption and development of
Future work in this area will refne the defnitions
cloud computing standards. The goal was to accelerate
of the fve core networks of things building blocks
the Federal Government’s adoption of secure and
as presented in SP 800-183. For example, instead of
efective cloud computing solutions to reduce costs
considering all temperature sensors as equal, NIST will
and improve services.
create categories of sensors for various applications
and vertical domains. Furthermore, a small IoT lab In addition to the initial defnition of cloud
to test “low-energy” devices is being architected. computing, NIST built a USG cloud computing
In addition, NIST plans to present these results in technology roadmap that focused on security,
Revision 1 of SP 800-183, which are expected to be interoperability, and portability requirements, and
produced in by the end of 2018. lead eforts to develop standards and guidelines in
close collaboration with standards bodies, the private
FOR MORE INFORMATION, SEE:
sector, and other stakeholders. NIST also developed
SP 800-183, Networks of ‘Things’, a cloud computing reference architecture, a security
https://dx.doi.org/10.6028/NIST.SP.800-183 reference architecture and, during 2017, focused on
https://www.nist.gov/topics/internet-things-iot developing the guidance for applying a risk-based
approach to cloud adoption and the guidance for
CONTACT: leveraging the NIST Cybersecurity Framework in the
process of architecting a cloud-based system secured
Dr. Jefrey Voas
with SP 800-53 Revision 4 security and privacy
(301) 975-6622
controls.
jef.voas@nist.gov
During FY 2017, NIST also researched the security
challenges encountered when leveraging application
Cloud Computing Security and
containers and microservices for the implementation
Forensics
of cloud-based federal information systems, along
with the impact on the system’s security posture.
The term “cloud computing” was initially coined
Details regarding the latest projects are provided
in 1997 by Professor Ramnath Chellappa of Emory
below.
University. During his talk, Intermediaries in Cloud-
Computing, which was presented at the Institute for
85
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

CSD Role in the NIST Cloud NIST is also leading the research and development
of the projects listed below:
Computing Program
• Members of the NIST Cloud Security Working
During FY 2017, NIST continued to promote the
Group, in collaboration with the Cloud Security
development of publications, national and international
Alliance’s members, researched the security
standards, and specifcations in support of the USG’s
challenges encountered when leveraging
efective and secure use of cloud computing, as well
application containers and microservices
as providing technical guidance to federal agencies
for the implementation of cloud-based
for secure and efective cloud-computing adoption.
information systems. Based on this research,
During FY 2017, NIST’s cloud computing security and
ITL will publish (in early FY 2018) the NIST
forensic science activities included the development
Interagency Report (NISTIR) documenting the
of the following guidance and/or recommendations:
fndings and will provide recommendations
based on the best practices for mitigating the
• NIST Draft SP 800-173, Guide for Applying the
identifed challenges.
Risk Management Framework to Cloud-based
Federal Information Systems. This publication
• Members of the NIST Cloud Security Working
initially focused on providing guidance in
Group are researching the security challenges
using the Risk Management Framework
encountered when implementing cloud-based
described in SP 800-37 Revision 1, Guide for
federated identity solutions and the impact
Applying the Risk Management Framework to
on the overall system’s security posture.
Federal Information Systems: a Security Life
Based on this research, NIST will issue an
Cycle Approach, to issue an authorization to
interagency report documenting the fndings
operate for cloud-based information systems.
and will provide recommendations based on
As SP 800-37 underwent revision in late FY
the best practices for mitigating the identifed
2017, and is anticipated to be fnalized in
challenges.
early FY 2018, the draft of SP 800-173 will be
updated to refect all changes incorporated • Members of the NIST Cloud Forensic Science
in the SP 800-37 Rev. 2 and will be posted for Working Group are working on defning
public comment after publication of SP 800- a cloud forensics reference architecture
37 Rev. 2. that leverages SP 500-299: Cloud Security
Reference Architecture and NISTIR 8006,
• NIST Draft SP 800-174, Security and
NIST Cloud Computing Forensic Science
Privacy Controls for Cloud-based Federal
Challenges. In support of U.S. cloud-
Information Systems. This document provides
computing mandates, CSD staf members
a methodology that leverages the NIST
provide leadership for several public cloud
Cybersecurity Framework (CSF) to architect
working groups operating under the NIST
a cloud-based information system and to
Cloud Computing Program. These working
identify security controls deemed necessary
groups focus on meeting the high-priority
to implement in order to secure the system.
requirements described in SP 500-293, U.S.
The document will be available for public
Government Cloud Computing Technology
comment in the frst quarter of FY 2018. The
Roadmap.
document will be accompanied by a tool,
Cloud Security Architecture Tool (CSAT), that CSD staf co-chaired several signifcant cloud
implements the methodology described in SP computing eforts in 2017:
800-174 and allows users to customize their
• Co-Chaired the NIST Cloud Computing
data and tailor their security controls. The tool
Security Working Group and led the working
repository is available at: https://github.com/
group on the development of the NIST
usnistgov/CloudSecurityArchitectureTool.
research on Application Containers and
Microservices – security challenges and 86
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

best practices. The result of this efort will  (IoT) devices in a manner that ensures minimal latency
materialize in FY 2018 into the development of  across a distributed and decentralized model.
a NIST Interagency Report and a NIST Special
Researchers working with system and network
Publication.
|     |     |     |     |     | engineers  | are  | continually  |     | developing  |     | innovative  |
| --- | --- | --- | --- | --- | ---------- | ---- | ------------ | --- | ----------- | --- | ----------- |
•   Co-Chaired the NIST Cloud Computing  solutions to fll the technological gaps. Many of these
Forensic Science Working Group and led the  solutions or computational paradigms have begun
development of SP 800-201, Cloud Forensics  to be referred to as fog computing, mist computing,
Reference Architecture, which is currently in  cloudlets,  or  edge  computing.  Lacking  broad
progress.  consensus on the distinction among these concepts,
NIST facilitated an efort to better defne these topics
•   Co-Chaired the NIST Cloud Computing
|     |     |     |     |     | to  help  | facilitate  | meaningful  |     | conversations  |     | among  |
| --- | --- | --- | --- | --- | --------- | ----------- | ----------- | --- | -------------- | --- | ------ |
Interoperability and Portability Working
practitioners and researchers.
Group and addressed issues facing cloud
computing with respect to interoperability  During FY 2017, NIST collaborated with the IoT
and portability, standards, and common and  community to develop SP 500-325, Fog Computing
functional terminologies. CSD staf members  Conceptual  Model.  This  publication   provides  the
participated in various standards development  conceptual model of fog computing and its subsidiary
organizations, all listed in the section of this  concept,  mist  computing,  and  identifes  these
report dedicated to international standards.  concepts in relation to cloud computing, cloudlets,
| In FY 2018, NIST will continue collaboration  |     |     |     |     | and edge computing.  |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
with the private sector, academia and other
The fog computing research will continue in FY
public-sector entities on developing guidance
2018 with the development of the draft of SP 800-
and specifcations that support the broad
|     |     |     |     |     | 199,  Security  |     | and  Privacy  |     | Controls  | for  | Fog-based  |
| --- | --- | --- | --- | --- | --------------- | --- | ------------- | --- | --------- | ---- | ---------- |
adoption of innovative cloud solutions. Some
Information Systems. This document, also referred to
of the very efective frameworks for such
as the fog computing overlay, will identify the security
collaborations that NIST is hosting are the
|     |     |     |     |     | and  privacy  |     | controls  | specifc  | to  | fog  | computing  |
| --- | --- | --- | --- | --- | ------------- | --- | --------- | -------- | --- | ---- | ---------- |
public working groups, with international
|     |     |     |     |     | ecosystems,  | allowing  |     | users  | of  this  | computational  |     |
| --- | --- | --- | --- | --- | ------------ | --------- | --- | ------ | --------- | -------------- | --- |
participation.
model to build resilient and survivable standalone
FOR MORE INFORMATION SEE:  fog computing environments that are more resistant
https://www.nist.gov/itl/cloud   to penetration attacks and are capable of limiting the
damage from attacks when they occur.
CONTACT:
CONTACTS:
Dr. Michaela Iorga
|     |     |     |     |     | Dr. Michaela Iorga  |     |     |     |      Mr. Ned Goren  |     |     |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | ------------------- | --- | --- |
(301) 975-8431
|     |     |     |     |     | (301) 975-8431   |     |     |          (301) 975-5233  |     |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | ------------------------ | --- | --- | --- |
michaela.iorga@nist.gov
michaela.iorga@nist.gov         nedim.goren@nist.gov
Fog Computing
NIST Cybersecurity for IoT Program
Ubiquitous deployment of smart, interconnected
NIST’s Cybersecurity for IoT Program develops
devices is estimated to reach as high as 50 billion
and applies standards, guidelines, and related tools
| units  by  | 2020.  This  exponential  |     | increase  | is  fueled  |     |     |     |     |     |     |     |
| ---------- | ------------------------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
to improve the cybersecurity of connected devices
by the proliferation of mobile devices (e.g., mobile
and the environments in which they are deployed. By
phones and tablets), smart sensors serving diferent
collaborating among stakeholders across government,
vertical markets (e.g., smart power grids, autonomous
|                  |                  |            |        |            | industry,    | international  |          | bodies,    | and          | academia,  | the         |
| ---------------- | ---------------- | ---------- | ------ | ---------- | ------------ | -------------- | -------- | ---------- | ------------ | ---------- | ----------- |
| transportation,  | industrial       | controls,  | smart  | cities,    |              |                |          |            |              |            |             |
|                  |                  |            |        |            | program      | aims           | to       | cultivate  | trust        | and        | foster  an  |
| wearables,       | etc),  wireless  | sensors    | and    | actuators  |              |                |          |            |              |            |             |
|                  |                  |            |        |            | environment  | that           | enables  |            | innovation.  | (see       | https://    |
networks. New concepts and technologies are needed
| 87  |     |     |     |     | www.nist.gov/programs-projects/nist-cybersecurity- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
to manage this growing feet of Internet of Things
iot-program).
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

| In        | FY  2017,  | during  |          | the  nascent  |     | phase     | of  the  | CONTACTS:  |     |     |     |     |     |     |
| --------- | ---------- | ------- | -------- | ------------- | --- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
| Program,  | the        | team    | focused  |               | on  | engaging  | and      |            |     |     |     |     |     |     |
Ms. Kat Megas
collaborating with stakeholders across government,
(202) 441-1147
industry,  international  bodies,  and  academia  to  katerina.megas@nist.gov
understand the IoT threat landscape and determine
whether there is stakeholder interest in NIST guidance
Mr. Ben Piccarreta
for securing their IoT ecosystems. To this end, the  (202) 802-1861
| Program  | hosted  | the  | IoT  | Cybersecurity  |     | Colloquium  |     |     |     |     |     |     |     |     |
| -------- | ------- | ---- | ---- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
benjamin.piccarreta@nist.gov
| in  Gaithersburg  |            | to    | better  | understand  |     | the   | overall  |     |     |     |     |     |     |     |
| ----------------- | ---------- | ----- | ------- | ----------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
| threat            | landscape  | from  |         | the  point  | of  | view  | of  the  |     |     |     |     |     |     |     |
Policy Machine – Next Generation
| community  | (see  | https://www.nist.gov/news-events/  |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ----- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
events/2017/10/iot-cybersecurity-colloquium).  The  Access Control
presenters discussed specifc security and privacy risks
|     |     |     |     |     |     |     |     | CSD  | has  | continued  | the  | development  |     | of  an  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---------- | ---- | ------------ | --- | ------- |
and NIST’s role in supporting these areas. The team
is currently drafting a NISTIR on the presentations,  advanced  Attribute  Based  Access  Control  (ABAC)
themes, and community feedback.  framework  called  the  Policy  Machine,  which  is
designed to be in alignment with an emerging ANSI/
Additionally, NIST and DHS co-chair the IoT Task  INCITS standard under the title of “Next Generation
Group of the Interagency International Cybersecurity
Access Control” (NGAC).
| Standardization  |     | Working  |     | Group   | (IICS  | WG).  | The  |      |         |          |       |     |                 |     |
| ---------------- | --- | -------- | --- | ------- | ------ | ----- | ---- | ---- | ------- | -------- | ----- | --- | --------------- | --- |
|                  |     |          |     |         |        |       |      | The  | Policy  | Machine  | (PM)  | is  | a  fundamental  |     |
IICS WG established the Task Group to determine
the present state of international IoT cybersecurity  reworking of traditional access control into a form
standards. The Task Group has 54 federal employee  suited  to  the  needs  of  a  modern,  distributed,
|               |     |               |     |     |           |      |       | interconnected  |     | enterprise.  |     | The  PM  | is  based  | on  a  |
| ------------- | --- | ------------- | --- | --- | --------- | ---- | ----- | --------------- | --- | ------------ | --- | -------- | ---------- | ------ |
| participants  |     | representing  |     | 13  | agencies  | and  | will  |                 |     |              |     |          |            |        |
convene in early FY 2018 to determine the next steps  fexible infrastructure that can provide access control
for its draft report. If approved, NIST is prepared to  services for several diferent types of resources that
are accessed by diferent types of applications and
take this document through the NISTIR process in FY
|     |     |     |     |     |     |     |     | users.  The  | PM  | infrastructure  |     | is  scalable  |     | and  can  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | --- | ------------- | --- | --------- |
2018 to collect industry input on specifc areas, such
as market adoption and challenges associated with  support  policies  of  various  types  simultaneously
while remaining manageable in the face of changing
the adoption of existing standards.
|     |     |     |     |     |     |     |     | technology,  |     | organizational  |     | restructuring,  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | --- | --------------- | --- | ---- |
In FY 2018, the Cybersecurity for IoT Program
|     |     |     |     |     |     |     |     | increasing  | amounts  |     | of  data.  | The  | PM  provides  | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ---------- | ---- | ------------- | --- |
will continue collaborating with stakeholders as NIST
|     |     |     |     |     |     |     |     | framework  | capable  |     | of  supporting  |     | combinations  | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | --------------- | --- | ------------- | --- |
begins drafting guidance for IoT security and privacy.  both current access control approaches and newly
As part of the drafting process, the team will hold  conceived types of policy without extensions.
town-hall meetings for input on discussion drafts. The
NIST and other members of an Ad Hoc INCITS
document is intended to educate federal agencies
working group are continuing to develop a three-part
| on  common  |     | high-level  |     | security  | and  | privacy  | risks  |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | --- | --------- | ---- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
for IoT, and to introduce practical risk management  NGAC standard. This work is being conducted under
considerations for IoT product selection, deployment,  three sub-projects:
protection, and operation.
•   Project 2193–D: Next Generation Access
Additional  information  regarding  the  broad  Control – Implementation Requirements,
Protocols and API Defnitions;
portfolio of NIST activities for supporting secure IoT
can be found on our program website.
•   Project 2194–D: Next Generation Access
FOR MORE INFORMATION, SEE:  Control – Functional Architecture; and
https://www.nist.gov/programs-projects/nist- •   Project 2195–D: Next Generation Access
cybersecurity-iot-program
Control – Generic Operations and Abstract
Data Structures.  88
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

|     |     |     |     |     |     |     |     | authentication  | (if  feasible)  |     | and  | some  | sample  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------------- | --- | ---- | ----- | ------- |
An initial standard from this work was published
in 2013 and is now available from ANSI as INCITS  applications  (e.g.,  email,  fle  management,  records
499: NGAC Functional Architecture (NGAC-FA) (see  management, document editor, workfow, etc.).
http://www.techstreet.com/standards/incits/499_
In FY 2018, CSD will continue improving the Web
| draft?product_id=1827386).  |     |     |     | However,  |     | based  | on  |           |                   |         |          |     |          |
| --------------------------- | --- | --- | --- | --------- | --- | ------ | --- | --------- | ----------------- | ------- | -------- | --- | -------- |
|                             |     |     |     |           |     |        |     | services  | version  of  the  | Policy  | Machine  | to  | include  |
experience with similar eforts (e.g., Project 2193-D,
|     |     |     |     |     |     |     |     | the  remaining  | NGAC  | functionalities  |     | and  | more  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | ---------------- | --- | ---- | ----- |
Project 2195-D, and the revised NISTIR 7987, Policy
applications to provide diferent use cases to support
Machine: Features, Architecture, and Specifcation).
the community’s use of the Policy Machine.
| This  standard  |     | has  been  |     | updated  | and  | was  | in  the  |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | -------- | ---- | ---- | -------- | --- | --- | --- | --- | --- | --- |
process of formal publication at the end of FY 2017.
FOR MORE INFORMATION, SEE:
In addition, as of the end of FY 2017, the work on  https://csrc.nist.gov/projects/policy-machine/
Project 2193-D had been submitted to ANSI as INCITS
CONTACTS:
525: NGAC Implementation Requirements, Protocols
and API Defnitions (NGAC-IRPADS), for approval for  Mr. David Ferraiolo           Ms. Gopi Katwala
an initial public review.  (301) 975-3046             (301) 975-6182
david.ferraiolo@nist.gov        gopi.katwala@nist.gov
The standard for Project 2195-D has been approved
and is now available from the ANSI e-standards store
Security for a Virtualized
as INCITS 526: NGAC Generic Operations and Abstract
| Data Structures (NGAC-GOADS).  |             |     |         |     |          |         |     | Infrastructure  |     |     |     |     |     |
| ------------------------------ | ----------- | --- | ------- | --- | -------- | ------- | --- | --------------- | --- | --- | --- | --- | --- |
| The                            | eXtensible  |     | Access  |     | Control  | Markup  |     |                 |     |     |     |     |     |
The objective of this project is to focus on security
| Language  | (XACML)  |     | and  | NGAC  are  | very  | diferent  |     |           |                     |              |     |      |          |
| --------- | -------- | --- | ---- | ---------- | ----- | --------- | --- | --------- | ------------------- | ------------ | --- | ---- | -------- |
|           |          |     |      |            |       |           |     | concerns  | in  virtualization  | technology;  |     | the  | project  |
ABAC standards with similar goals and objectives.  was started at a time when the technology was just
| What  are  | the  | similarities  |     | and  diferences  |     | between  |     |     |     |     |     |     |     |
| ---------- | ---- | ------------- | --- | ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
beginning to gain traction in data centers used for
these two standards?  What are  their comparative
supporting enterprise IT applications as well as for
| advantages  |     | and  disadvantages?  |     |     | To  answer  |     | these  |     |     |     |     |     |     |
| ----------- | --- | -------------------- | --- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
providing cloud services. An IT infrastructure can be
questions, in October 2016 NIST published SP 800-
looked upon as having fve components or resources:
178, A Comparison of Attribute Based Access Control
Hardware, Operating System (OS), and Applications
| (ABAC)  | Standards  |     | for  Data  | Service  |     | Applications:  |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ---------- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
that collectively form a compute node, together with
Extensible Access Control Markup Language (XACML)  network and storage components that provide the
| and  Next     |     | Generation    |     | Access  | Control    | (NGAC),  |       |                  |                      |      |            |      |          |
| ------------- | --- | ------------- | --- | ------- | ---------- | -------- | ----- | ---------------- | -------------------- | ---- | ---------- | ---- | -------- |
|               |     |               |     |         |            |          |       | function         | of  interconnecting  | the  | computing  |      | nodes    |
| to  describe  |     | and  compare  |     | these   | standards  |          | with  |                  |                      |      |            |      |          |
|               |     |               |     |         |            |          |       | and  supporting  | a  persistent        |      | medium     | for  | storing  |
respect to the criteria derived from ABAC issues or  data respectively. Any of these fve resources can be
| considerations  |     | identifed  |     | by  SP  800-162,  |     | Guide  | to  |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | ----------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
virtualized by building an abstraction layer on top of
| Attribute  | Based  | Access  |     | Control  (ABAC)  |     | Defnition  |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | --- | ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
it, facilitating efcient utilization of that resource by
and Considerations: operational efciency, attribute  other components or resources as well as providing a
and policy management, scope and type of policy
degree of isolation among the utilizing components.
support, and support for administrative review and
resource discovery.  The  earliest  component  to  be  virtualized  was
|     |     |     |     |     |     |     |     | the  hardware  | (ubiquitously  | referred  |     | to  | as  Server  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------------- | --------- | --- | --- | ----------- |
In FY 2017, CSD issued the frst version of the
Virtualization) through an abstraction layer (software
| Policy  | Machine  | Web  | Services  | through  |     | GitHub  | as  |          |                           |     |       |       |           |
| ------- | -------- | ---- | --------- | -------- | --- | ------- | --- | -------- | ------------------------- | --- | ----- | ----- | --------- |
|         |          |      |           |          |     |         |     | module)  | called  the  Hypervisor.  |     | This  | gave  | rise  to  |
an open-source distribution to support widespread  an  architecture  where  multiple  computing  stacks
| experimentation  |     | of  | web-based  |     | applications.  |     | The  |     |     |     |     |     |     |
| ---------------- | --- | --- | ---------- | --- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
(called Virtual Machines or VMs) each with a diferent
current version of the web services supports most
OS can be run on a single physical host (called a
NGAC functionality. In order to provide an example
virtualized host). To connect the various VMs residing
of web-based clients, CSD is planning to issue an  in a single physical host, an approach to networking
| administrative  |     | interface  |     | for  policy  | management,   |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(called the Virtual Network) had to be implemented.
89
| which  | will  also  | include  |     | a  user  interface  |     | with  | PIV  |     |     |     |     |     |     |
| ------ | ----------- | -------- | --- | ------------------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- |
The Virtual Network used the software analogs of
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

hardware network devices such as network interface  stack with all these new components is shown in
cards (NICs) and switches. Thus, the Virtual Network  Figure 32 as the Container Technology stack.
| (which  | was  later  | extended  | to  connect  | virtualized  |       |      |             |           |                  |
| ------- | ----------- | --------- | ------------ | ------------ | ----- | ---- | ----------- | --------- | ---------------- |
|         |             |           |              |              | With  | the  | increasing  | adoption  | of  application  |
hosts themselves in addition to VMs inside a single
container technology for deploying, managing and
virtualized host) became an integral part of the server
maintaining applications, NIST identifed threats to
virtualization infrastructure. From FY 2014 to FY 2016,
components involved in supporting containers as well
this project focused on providing guidelines for the
secure confguration and deployment of hypervisors  as the security countermeasures to mitigate the efect
|     |     |     |     |     | of  those  | threats  | through  | SP  800-190,  | Application  |
| --- | --- | --- | --- | --- | ---------- | -------- | -------- | ------------- | ------------ |
and virtual networks.
|     |     |     |     |     | Container  | Security  | Guide  | (see  https://nvlpubs.nist.  |     |
| --- | --- | --- | --- | --- | ---------- | --------- | ------ | ---------------------------- | --- |
The next component to be virtualized was the OS  gov/nistpubs/SpecialPublications/NIST.SP.800-190.
| itself. The application component of the computing  |           |       |           |                 | pdf).  |     |     |     |     |
| --------------------------------------------------- | --------- | ----- | --------- | --------------- | ------ | --- | --- | --- | --- |
| stack  was                                          | packaged  | into  | multiple  | self-contained  |        |     |     |     |     |
In FY 2017, building on the information in SP 800-
| lightweight  | software  | elements  |     | called  Application  |     |     |     |     |     |
| ------------ | --------- | --------- | --- | -------------------- | --- | --- | --- | --- | --- |
Containers.  The  abstraction  of  the  OS  itself  was  190, this project examined potential security solutions
that provide the necessary countermeasures as well as
| enabled  | by  a  software  |     | module  | called  “Container  |     |     |     |     |     |
| -------- | ---------------- | --- | ------- | ------------------- | --- | --- | --- | --- | --- |
the kind of security assurance requirements that each
| Runtime”.  | This  form  | of  | virtualization  | brought  in  |     |     |     |     |     |
| ---------- | ----------- | --- | --------------- | ------------ | --- | --- | --- | --- | --- |
solution should satisfy in accordance with NISTIR 8176,
| several  | new  technology  |     | components  | involved  in  |     |     |     |     |     |
| -------- | ---------------- | --- | ----------- | ------------- | --- | --- | --- | --- | --- |
Security Assurance Requirements for Linux Application
| building  | containers,  | storing  | them  | in  repositories  |     |     |     |     |     |
| --------- | ------------ | -------- | ----- | ----------------- | --- | --- | --- | --- | --- |
Container Deployments (see https://nvlpubs.nist.gov/
(called registries) and deploying and managing them
|     |     |     |     |     | nistpubs/ir/2017/NIST.IR.8176.pdf).  |     |     |     | Because  security  |
| --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | ------------------ |
(through a process called orchestration) as logical
solutions for containers vary signifcantly based on
| groups  | (called  clusters).  |     | The  resulting  | computing    |             |     |     |     |     |
| ------- | -------------------- | --- | --------------- | ------------ | ----------- | --- | --- | --- | --- |
|         |                      |     |                 | Application  | Scheduling  |     |     |     |     |
Container Scheduling
Service Discovery
Container Cluster Management
Container Networking
.g;;;,;;;
|     |     |                        | Container Runtime  |     |     | Container Runtime      |               |     |     |
| --- | --- | ---------------------- | ------------------ | --- | --- | ---------------------- | ------------- | --- | --- |
|     |     |                        | Container OS       |     |     |                        | Container OS  |     |     |
|     |     | Physical Host (or VM)  |                    |     |     | Physical Host (or VM)  |               |     |     |
DevOps Tools
90
Figure 32: Container Technology Stack
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

the OS component (shown as Container OS in Figure capabilities. Cyber threat information includes
32) and because of their ubiquitous usage in container indicators (i.e., artifacts or observable events that
deployments, NISTIR 8176 focused on Linux OS- suggest that an attack is imminent, that an attack is
based environments. This decision enabled detailed underway, or that a compromise may have already
security assurance requirements to be defned. occurred); information about the tactics, techniques,
Furthermore, the team recognized that there are and procedures (TTPs) of actors; recommended
multiple hypervisor products for server virtualization courses of action; and other information that is used to
in current infrastructures. This observation led the characterize threats. Because threat actors often use
team to modify previous security recommendations to the same TTPs against multiple targets, exchanging
improve countermeasures against potential threats to cyber threat information allows organizations to
the hypervisor. These countermeasures are agnostic leverage the collective knowledge, experience, and
to any specifc architecture of the hypervisor platform. analysis capabilities of their peers, thereby increasing
The modifed recommendations were published the overall awareness and security of an entire
for public comment in the second draft of SP 800- sharing community. Through the exchange of cyber
125A, Security Recommendations for Hypervisor threat information, organizations can gain a more
Deployment (see https://csrc.nist.gov/publications/ complete understanding of their threat environment
detail/sp/800-125a/draft). by correlating their observations with those of others.
NIST contributed signifcant material that led CSD has established a cyber threat information-
to the creation of ISO/IEC Committee Draft 21878, sharing initiative, which is focused on providing
Security Guidelines for Design and Implementation guidance on how an organization can establish
of Virtualized Servers, in April 2017. The draft was co- information sharing and coordination capabilities
edited by a CSD computer scientist and drew from that enhance or augment their existing cybersecurity
information in seven NIST conference papers and practices. The guidance covers threat-informed
four technical publications regarding security for the detection, protection and response capabilities; data
virtualized infrastructure. privacy and sensitivity; data collection and retention
practices; the use of open standards for information
NIST recognizes that application container
exchange; de-identifcation and anonymization;
technology is being increasingly used to develop
and guidance on how an organization can establish,
applications with microservices-based architectures.
participate in, and maintain coordination and
In FY 2018, this project plans to focus on security issues
information-sharing relationships. The guidance will
arising from technology components involved in that
help incident responders, network defenders, and
architecture. Developments in virtual networking
operations personnel consider what information is
and virtual storage technologies will be monitored
sharable, the circumstances under which sharing is
to update our security recommendations for secure
allowed, with whom the information may be shared,
deployment of these technologies.
and how the information should be protected.
CONTACT:
In October 2016, CSD published SP 800-150, Guide
Dr. Ramaswamy Chandramouli to Cyber Threat Information Sharing. This publication
(301) 975-5013 helps organizations prepare for an exchange of
mouli@nist.gov cyber threat information, both consuming cyber
threat information from external sources and
producing information for other organizations to
Cyber Threat Information Sharing
use. Organizations may have diferent capabilities for
detecting threats, responding to attacks, diagnosing
As cyber attacks increase in both sophistication
causes, and handling sensitive incident-related
and frequency, it is important to collect and analyze
information, but this guidance is intended to help
cyber threat information from a variety of internal
organizations collaborate and exchange cyber threat
and external sources, and use it to develop, enhance,
information despite these organizational diferences.
and deploy proactive, threat-informed, cyber defense
91
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

In May 2017, NIST conducted a Threat Intelligence  •   Law Enforcement,
| Working  | Session  | as  part  | of  the  | Cybersecurity  |     |     |     |     |     |     |     |     |
| -------- | -------- | --------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
•   Fusion Centers, and
Framework Workshop. The working session provided
an opportunity for attendees to provide comments on
•   Sector Coordinating Councils.
the use of cyber threat intelligence in the Framework,
| to help shape future enhancements to the Framework,  |     |     |     |     |     | CONTACTS:  |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
and to share experiences regarding the use of cyber  Mr. Christopher Johnson   Mr. Lee Badger
threat intelligence in the Framework. NIST used the
|           |           |         |                |     |           | (301) 975-3247                 |     |     | (301) 975-3176       |     |     |     |
| --------- | --------- | ------- | -------------- | --- | --------- | ------------------------------ | --- | --- | -------------------- | --- | --- | --- |
| feedback  | received  | during  | the  workshop  |     | and  the  |                                |     |     |                      |     |     |     |
|           |           |         |                |     |           | christopher.johnson@nist.gov   |     |     | lee.badger@nist.gov  |     |     |     |
public review process as input when updating the
Cybersecurity Framework Version 1.1 and its roadmap.  Mr. David Waltermire
(301) 975-3390
| Throughout  |     | the  year,  | CSD  | engaged  | with  |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | ---- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
david.waltermire@nist.gov
| government,  |     | industry,  and  | academia  | to  | research  |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
protocols, data models, and standards that enable
The Ontology of Authentication
cyber threat information sharing and support near
real-time cybersecurity decision-making and security
Over the past 30 years, NIST recommendations
operations.
have included the usage of passwords, biometrics,
|     |     |     |     |     |     | authentication  |     | hardware  | devices,  | and  | Public  |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --------- | ---- | ------- | --- |
In FY 2018, CSD plans to continue to conduct
|            |          |            |      |       |           | Key  Infrastructure  |     | (PKI)  | solutions  | for  | enterprise  |     |
| ---------- | -------- | ---------- | ---- | ----- | --------- | -------------------- | --- | ------ | ---------- | ---- | ----------- | --- |
| research,  | prepare  | guidance,  | and  | take  | part  in  |                      |     |        |            |      |             |     |
standards development activities that foster greater  authentication  applications.  Recently,  CSD  began
interoperability and increase the operational tempo  researching  general  authentication  features.  This
investigation was prompted by the general call to
| through  | near  | real-time  | cyber  threat  | information  |     |             |       |            |     |              |          |     |
| -------- | ----- | ---------- | -------------- | ------------ | --- | ----------- | ----- | ---------- | --- | ------------ | -------- | --- |
|          |       |            |                |              |     | move  away  | from  | passwords  |     | toward  the  | growing  |     |
sharing, including:
number of alternative authentication methods (e.g.,
•   Expressing cyber threat information using  biometrics, smart cards, etc.). A notional ontology
machine-readable formats,  of authentication is in development that includes a
detailed taxonomy and an assessment approach to
•   Developing automated mechanisms for
aid in defnitively comparing alternatives.
exchanging cyber threat information,
As the research matures, it is possible to draft
•   Describing automated courses of action,
|     |     |     |     |     |     | a  concept  | map  | (see  Figure  |     | 33)  to  highlight  |     | key  |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | ------------- | --- | ------------------- | --- | ---- |
components. There are many intertwining aspects of
•   Publishing cyber threat information metadata,
authentication, such as the relationships with Identity
and
|     |     |     |     |     |     | Management  | and  | Authorization.  |     | As  more  | of  | the  |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | --------------- | --- | --------- | --- | ---- |
•   Safeguarding cyber threat information.  aspects of authentication are identifed and defned,
|     |     |     |     |     |     | better  development  |     | and  | use  | of  authentication  |     | is  |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ---- | ---- | ------------------- | --- | --- |
NIST will also help foster cyber threat information
expected.
sharing by supporting information-sharing initiatives
by public and private-sector organizations, including:  The  structure  of  the  authentication  taxonomy
(see Figure 34) to encapsulate current and emerging
•   Information Sharing and Analysis Centers
mechanisms continues to be refned as recent updates
(ISACs),
expand the diversity of mechanisms. The taxonomy
includes entity authentication as a wide assortment of
•   Information Sharing and Analysis
Organizations (ISAOs),  commonly used human-machine, machine-machine,
and human-human methods, all of which are termed
•   Federal/State/Local agencies,  confrmation. Attestation is the term used for afrming
expectations of objects.
92
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

- -
.. -
-
..,


....~ .
Hi\1111:

- HH-
 ii+
• - ...
 &M+

• - -
lib-
Figure 33: Draft Authentication Concept Map
The notional authentication ontology attempts may overlap or impact the others. Security and
to defne an assessment framework that is useful for usability are of special interest; while usability is often
better understanding, comparing, and determining thought of as a tradeof to security, both must be
the appropriateness of authentication technologies satisfed for the user to support the security of the
to a specifc use-case. The assessment framework system. To state the issue another way, there appears
separates attributes into security, usability, to be a relation between how much we must ask of the
deployability, and manageability categories (see operator and how willing the operator is to support
Figure 35). It is important to note that each category security rather than (mis)manage it.
Authentication
Taxonomy
93 Figure 34: Draft Authentication Taxonomy
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

Cognitive-based Approach to System
Security Assessment (CASSA)
The increase in information systems’ complexity,
Deployability
due to the aggregation of broader-spectrum services
|     |     |     |     |     |     |     |     | and  functionality  |     | within  | one  system,  | challenges  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------- | ------------- | ----------- |
security professionals  that are required to plan, analyze,
design, implement and maintain systems compliant to
Usability  Manageability  various regulatory requirements supported by diverse
sets of security controls, processes and procedures. For
example, Veteran Afairs’ hospital systems are often
required to meet FISMA, Payment Card Industry (PCI)
and Health Insurance Portability and Accountability
Figure 35: Suitability Framework for Authentication  Act (HIPAA) requirements simultaneously. Assessing
and maintaining the security posture of such complex
| Specifc  |     | methods  | of  | assessment  |     | in  | these    |              |          |          |         |             |
| -------- | --- | -------- | --- | ----------- | --- | --- | -------- | ------------ | -------- | -------- | ------- | ----------- |
|          |     |          |     |             |     |     |          | information  | systems  | through  | manual  | procedures  |
categories are not developed and are expected to  leveraging  paper-driven  approaches  is  colossal,
| be  unique  | to  | each  | authentication  |     | mechanism  |     | and  |     |     |     |     |     |
| ----------- | --- | ----- | --------------- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- |
inefcient, and often unreliable.
| dependent  | on  | the  | environment.  |     | The  | assessment  |     |     |     |     |     |     |
| ---------- | --- | ---- | ------------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
framework  also  includes  integration  with  the  NIST is researching methodologies for enhancing
|               |     |             |     |     |                |     |      | the  security  | assessment  |     | and  the  | near-real-time  |
| ------------- | --- | ----------- | --- | --- | -------------- | --- | ---- | -------------- | ----------- | --- | --------- | --------------- |
| programmatic  |     | categories  |     | of  | deployability  |     | and  |                |             |     |           |                 |
manageability. What is known is that these are unlikely  monitoring of complex systems. The team is leveraging
to be reduced to a single value, but will have to be  cognitive approaches to provide continuous feedback
by highlighting relevant threats, rendering security
assessed across several independent constructs.
enhancements, or augmenting solutions to maintain/
| Future  | programmatic  |     |     | eforts  | will  | be  | focused  |     |     |     |     |     |
| ------- | ------------- | --- | --- | ------- | ----- | --- | -------- | --- | --- | --- | --- | --- |
increase systems’ security postures.
| toward     | a  NISTIR  | to          | describe  | the   | research  |             | results,  |         |     |              |            |                 |
| ---------- | ---------- | ----------- | --------- | ----- | --------- | ----------- | --------- | ------- | --- | ------------ | ---------- | --------------- |
|            |            |             |           |       |           |             |           | During  | FY  | 2017,  NIST  | completed  | a  feasibility  |
| encourage  | further    | discussion  |           | with  | the       | community,  |           |         |     |              |            |                 |
and provide recommendations for future standards  assessment and created the project’s research plan,
development  eforts.  The  goal  is  to  move  toward  identifying milestones and deliverables. In FY 2018
and subsequent years, the team will continue the
| specifying  | independent  |     |     | strength  |     | requirements  |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
rather  than  specifc  implementation  requirements.  Cognitive-based  Approach  to  Security  Controls
Upon completion of the NISTIR, work will begin on a  Assessment (CASSA) by researching methods to:
suitability matrix that will aid the user in determining
•   Identify the relationships between
| how  best  | to  | apply  | and  | assess  | the  | assessment  |     |     |     |     |     |     |
| ---------- | --- | ------ | ---- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
implemented security and privacy controls for
| framework.  | Concerns  |     | as  | to  the  | adoptability  |     | of  |     |     |     |     |     |
| ----------- | --------- | --- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
a targeted information system;
| this  approach  |     | will  | be  addressed.  |     | Additional  |     | work  |     |     |     |     |     |
| --------------- | --- | ----- | --------------- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
to  identify  interdependencies  among  identity  •   Analyze the implementation of the security
| management  |     | and  | authorization  |     | controls  |     | and  |     |     |     |     |     |
| ----------- | --- | ---- | -------------- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- |
and privacy controls, providing, as feedback,
requirements should aid in unifying the approach. As
a rendered set of suggestions to enhance the
a clear assessment approach is defned, future identity  security posture of the system;
| management,  |     | authentication,  |     |     | and  | authorization  |     |     |     |     |     |     |
| ------------ | --- | ---------------- | --- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
process implementations can address vulnerabilities  •   Identify documented and undocumented
vulnerabilities relevant to the system;
of individual or combined solutions.
| CONTACT:  |     |     |     |     |     |     |     | •   Identify the minimum-resistance penetration  |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
path into the system, providing, as feedback,
Dr. Kim Schafer
rendered recommendations for mitigating the
(301) 975-8375
risk; and
kim.schafer@nist.gov
94
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

•   Perform continuous monitoring and analysis  and a healthcare institution (with Health Insurance
of the system, factoring in the above steps  Portability  and  Accountability  Act  (HIPAA)
while providing rendered suggestions for  requirements)  that  has  credit  card  transactions
system enhancements.  (with requirements specifed in the Payment Card
Industry Data Security Standard (PCI DSS)). There is
CONTACTS:
no shortage of requirements for some organizations
Dr. Michaela Iorga              Dr. Dmitry Cousin   that have multiple regulatory frameworks. Assessing
(301) 975-8431              (301) 975-5727   a plethora of security controls rooted on diferent
michaela.iorga@nist.gov         dmitry.cousin@nist.gov  standards  with  diferent  formatting  is  a  complex
process that is currently largely manual or leverages
proprietary, specifcally customized approaches and
Open Security Controls Assessment
tools.
Language (OSCAL)
|     |     |     |     |     |     |     |     | OSCAL  | attempts  |     | to  standardize  |     | how  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ---------------- | --- | ---- |
NIST is proposing the development of the Open  security  controls  are  represented,  how  a  control
Security Controls Assessment Language, or OSCAL,  implementation for a given system is represented,
a  hierarchical,  formatted,  XML-based  (and  JSON  and how that information is best used. It supports
translation)  schema  that  provides  a  standard  for  the generation of standardized reports that can be
representing  diferent  categories  of  information  used  by  both  humans  and  machines.  That  means
pertaining to the publication, implementation, and  that formats are needed that can be generated by
assessment of security controls.
machines for communicating with other machines,
but can also be easily reformatted so that humans
| OSCAL       | is      | attempting  | to  | address   | a    | number    | of  |            |                    |     |     |                |      |
| ----------- | ------- | ----------- | --- | --------- | ---- | --------- | --- | ---------- | ------------------ | --- | --- | -------------- | ---- |
|             |         |             |     |           |      |           |     | can  read  | the  information.  |     | By  | standardizing  | the  |
| challenges  | around  | security    |     | controls  | and  | security  |     |            |                    |     |     |                |      |
representation of this information, OSCAL information
| controls  | assessment.  |     | The  core  | challenge,  |     | and  | one  |          |                |          |     |                     |     |
| --------- | ------------ | --- | ---------- | ----------- | --- | ---- | ---- | -------- | -------------- | -------- | --- | ------------------- | --- |
|           |              |     |            |             |     |      |      | can  be  | interoperable  | because  |     | of  a  well-defned  |     |
of the primary reasons for creating OSCAL, is that
specifcation with information that’s going to be used,
| concepts  | like  | security  | controls  |     | and  profles  |     | are  |     |     |     |     |     |     |
| --------- | ----- | --------- | --------- | --- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
imported, and subsquently used for security control
| represented  | today  | largely  |     | in  proprietary  |     | ways.  | In  |     |     |     |     |     |     |
| ------------ | ------ | -------- | --- | ---------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
assessments. The goal is to keep OSCAL as simple as
many cases they are written in prose documents that
possible and provide extensive automation for tools
are imprecise, lead to diferences in interpretation,
it uses.
| and  are  | not  | machine-readable,  |     | meaning  |     | that  | the  |     |     |     |     |     |     |
| --------- | ---- | ------------------ | --- | -------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- |
prose instructions require someone to do data entry  During  FY  2017,  NIST  focused  on  developing
into a tool in order for the tool to use the information.  the control catalog schema and the profle schema,
focusing on addressing a large number of user stories
Organizations are also struggling with information
that describe features, attributes or characteristics.
systems that have many diferent components, and
The team validated the approach with use cases from
some components require the use of diferent profles
SP 800-53 Rev. 4, SP 800-53 Rev. 5 (draft), ISO/IEC
per component, which is commonly the case with
27001 and 27002, and COBIT 5.
| cloud  | environments.  |     | Also,  | the  cloud  | environments  |     |     |     |     |     |     |     |     |
| ------ | -------------- | --- | ------ | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
can  be  multitenant  or  have  mixed  ownership  of  In   the   next   year,  NIST  will  continue  the
components. We need to be able to assess the security  development of the other schemas pertaining to the
of these systems against a number of requirements,  project (e.g., the framework schema, implementation
owners, etc.—to do this simultaneously and provide  schema and System Security Plan (SSP) representation,
| these views to stakeholders.                      |        |                |          |            |             |             |     | assessment schema, etc.).  |     |                             |     |     |     |
| ------------------------------------------------- | ------ | -------------- | -------- | ---------- | ----------- | ----------- | --- | -------------------------- | --- | --------------------------- | --- | --- | --- |
| In addition, there are situations where a single  |        |                |          |            |             |             |     | CONTACTS:                  |     |                             |     |     |     |
| system                                            | needs  | to             | support  | multiple   |             | regulatory  |     |                            |     |                             |     |     |     |
|                                                   |        |                |          |            |             |             |     | Dr. Michaela Iorga         |     |       Mr. David Waltermire  |     |     |     |
| frameworks.                                       |        | For  example,  |          | the  U.S.  | Department  |             | of  |                            |     |                             |     |     |     |
|                                                   |        |                |          |            |             |             |     | (301) 975-8431             |     |       (301) 975-3390        |     |     |     |
Veterans Afairs is a federal agency (with Federal
michaela.iorga@nist.gov     david.waltermire@nist.gov
| Information  |     | Security  | Modernization  |     | Act  | (FISMA)  |     |     |     |     |     |     |     |
| ------------ | --- | --------- | -------------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
95
| and  NIST  | Cybersecurity  |     | Framework  |     | requirements)  |     |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

NATIONAL CYBERSECURITY in a NIST SP 1800 series, a three-volume
document that provides applicable guidance
CENTER OF EXCELLENCE
for executives, CISOs or IT directors, and IT
staf.
Types of Collaborators & Partnerships
The National Cybersecurity Center of Excellence
(NCCoE), established in 2012 by NIST in partnership
Vendors, industry stakeholders, academic experts
with the State of Maryland and Montgomery County,
and others participate in the center through a variety
Md., is a collaborative hub – convening experts from
of collaborative mechanisms as described below:
industry, academia, and government to work on critical
problems in cybersecurity. The NCCoE’s collaborations • Communities of Interest: A Community of
focus on providing practical guidance to technical, Interest (COI) is a group of professionals and
real-world cybersecurity challenges using standards- advisors that share business insights, technical
based, commercially available technologies. expertise, challenges, and perspectives to
guide NCCoE projects. The NCCoE relies on
Project Lifecycle this robust collaboration with experts and
innovators to provide real-world cybersecurity
To help accelerate businesses’ adoption of
challenges and inform the reference
standards-based, secure technologies, the NCCoE
designs for standards-based cybersecurity
works collaboratively with stakeholders to:
integrations that address business needs.
• Defne and articulate: The NCCoE works
• Technology Collaborators: Vendors
with industry stakeholders, cybersecurity
who would like to participate in a center
professionals, academic experts, government
project reply to a Federal Register call for
agencies, and others to identify and defne
participation. Vendors who are chosen to
pressing cybersecurity issues.
participate sign a CRADA and contribute
• Organize and engage: The NCCoE then their expertise, hardware, or software to the
collaborates with stakeholders to refne a reference design for a specifc problem.
project’s scope and develop detailed technical
• National Cybersecurity Excellence
descriptions of the problem. The NCCoE also
Partnership (NCEP): The NCCoE also works
engages technology vendors via an open
with technology vendors via the NCEP
call through the Federal Register, to build a
program, wherein vendors sign MOUs to
potential example solution.
establish a deeper partnership with the
• Implement and test: The NCCoE works with NCCoE. NCEPs can provide hardware,
technology vendors that have standards- software, knowledge, personnel, and can
based, commercially available products designate guest researchers to work at the
that can be used as part of the example center in person or remotely. The NCCoE
implementation. These vendors sign a currently has 31 NCEPs, from Fortune
Cooperative Research and Development 50 market leaders to smaller companies
Agreement (CRADA) and help build a specializing in IT security.
reference design, identify gaps in the build;
For more information on NCCoE Partnerships, see
and refne the example implementation
https://nccoe.nist.gov/partners.
until there is a practical, usable, repeatable
reference design that addresses the business
SP 1800 Series: Practical Cybersecurity
problem.
Guidance
• Publish and transfer: The NCCoE provides NCCoE projects result in a NIST Special Publication
details of the reference design, standards
(SP) 1800 document – a three-volume practice guide,
mapping, lab implementation, and more which is a complement to NIST’s SP 800 series 96
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

intentionally or otherwise, can expose a healthcare
documents. SP 1800 documents contain an Executive
Summary for business executives, a second volume  delivery  organization  to  serious  risks,  including
for security program managers that details security  breaches  of  protected  health  information,  loss  or
approaches and maps security capabilities to the NIST  disruption  of  healthcare  services,  damage  to  an
Cybersecurity Framework as well as other relevant  organization’s reputation, productivity, and revenue,
standards, and a third volume for the cybersecurity  or even loss of life.
implementation staf that details the steps needed
The NCCoE worked with a community-of-interest
for another entity to recreate the NCCoE’s example
made up of various components of the healthcare
solution.
ecosystem to defne the challenge of using wireless
In FY 2017, the center published seven practice  infusion pumps securely, identify relevant standards
guides (up from two in FY 2016 and three in FY 2015)  and  best  practices,  and  create  a  representative
| that provide practical guidance, including a reference  |                      |           |                | architecture.  |     |     |     |
| ------------------------------------------------------- | -------------------- | --------- | -------------- | -------------- | --- | --- | --- |
| design                                                  | and  implementation  | details,  | on  standards- |                |     |     |     |
The NCCoE then developed a lab implementation
based secure technologies:
to demonstrate how healthcare delivery organizations
1.   SP 1800-3, Revision 2, Attribute Based  can  use  standards-based,  commercially  available
Access Control;  cybersecurity  technologies  and  industry  best
|      |                                           |     |     | practices.      | Working  with  | fve  major       | infusion  pump       |
| ---- | ----------------------------------------- | --- | --- | --------------- | -------------- | ---------------- | -------------------- |
| 2.   | SP 1800-6, DNS-Based Email Security;      |     |     |                 |                |                  |                      |
|      |                                           |     |     | manufacturers,  | which          | accounted        | for  85  %  of  the  |
|      |                                           |     |     | market          | in  America,   | and  innovative  | cybersecurity        |
| 3.   | SP 1800-7, Situational Awareness for the  |     |     |                 |                |                  |                      |
|      |                                           |     |     | technology      | vendors,       | the  NCCoE       | helped  highlight    |
Electric Utilities;
where security capabilities could be built into the
4.   SP 1800-8, Securing Wireless Infusion  pumps to strengthen the cybersecurity of the devices,
pump ecosystem, and healthcare enterprise. This has
Pumps in Healthcare Delivery
Organizations;  led  to  multiple  pump  manufacturers  incorporating
security capabilities into the next generation versions
| 5.   | SP 1800-9, Managing Access Rights in the  |     |     |     |     |     |     |
| ---- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
of their pumps.
Financial Services Sector;
Collaborating Across Government
| 6.   | SP 1800-11, Data Integrity: Recovering  |     |     |     |     |     |     |
| ---- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
from Ransomware and Other Destructive  The NCCoE’s Work for Others (WFO) Program,
Events; and  governed  by  the  NCCoE’s  Program  Management
|      |                                        |     |     | Ofce  | (PMO),  facilitates  | the  engagement  | of  other  |
| ---- | -------------------------------------- | --- | --- | ----- | -------------------- | ---------------- | ---------- |
| 7.   | SP 1800-12, Derived Personal Identity  |     |     |       |                      |                  |            |
agencies with NIST’s National Cybersecurity Federally
Verifcation (PIV) Credentials.  Funded Research and Development Center (FFRDC).
Since 2015, the WFO program has continuously grown
For more information about NCCoE projects, visit
|     |     |     |     | and  currently  | has  several  | interagency  | agreements  |
| --- | --- | --- | --- | --------------- | ------------- | ------------ | ----------- |
https://nccoe.nist.gov/projects.
in place, which support projects for the U.S. Coast
Guard, the U.S. Department of Transportation, the U.S.
Example: Impact of Guidance on Wireless Infusion
Air Force, and the Department of Homeland Security.
Pumps
Medical devices like infusion pumps were once  Example of Government Collaboration: U.S. Coast
Guard and Sector CSF Profles
| standalone  | instruments.  | Today,  | infusion  pumps  |     |     |     |     |
| ----------- | ------------- | ------- | ---------------- | --- | --- | --- | --- |
connect wirelessly to a variety of healthcare systems,
In early FY 2017, the U.S. Coast Guard (USCG) and
| networks,  | and  other  | devices.  Connecting  | infusion  |     |     |     |     |
| ---------- | ----------- | --------------------- | --------- | --- | --- | --- | --- |
industry representatives worked with NIST to develop
| pumps       | to  point-of-care  | medication             | systems  and  |                |                |           |                |
| ----------- | ------------------ | ---------------------- | ------------- | -------------- | -------------- | --------- | -------------- |
|             |                    |                        |               | the  Maritime  | Bulk  Liquids  | Transfer  | Cybersecurity  |
| electronic  | health             | records  can  improve  | healthcare    |                |                |           |                |
Framework (CSF) Profle. This profle template helps
delivery processes, but it also increases cybersecurity
organizations in the complex and sophisticated supply
risks that could afect operations or safety. Tampering
chain of the oil and natural gas industry assess and
97
with the wireless infusion pump ecosystem, whether
monitor their cybersecurity risk (see https://www.dco.
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

uscg.mil/Portals/9/CG-FAC/Documents/Maritime_  stakeholders to improve the resilience of the internet
BLT_CSF.pdf?ver=2017-07-19-070544-223).  Building  and communications ecosystem and to encourage
on the success of this CSF profle, the USCG asked for  collaboration with the goal of dramatically reducing
two more profles to be completed: Mobile Of-Shore  threats  perpetrated  by  automated  and  distributed
Drilling Units and Passenger Vessels.  attacks (e.g., botnets).” The workshop was designed
to allow stakeholders to explore a range of current
The goal of these profles is to provide maritime
|     |     |     |     |     | and  emerging  |     | solutions  | addressing  | automated,  |     |
| --- | --- | --- | --- | --- | -------------- | --- | ---------- | ----------- | ----------- | --- |
sub-sectors  with  guidance  for  applying  the  CSF,  distributed  threats  in  an  open  and  transparent
| leveraging  | the  framework  | to  create  | a  sub-sector  |     |     |     |     |     |     |     |
| ----------- | --------------- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
manner. The workshop’s proceedings were detailed
profle that individual companies can tailor and use to
in NISTIR 8192, published in FY 2017 (see https://csrc.
prioritize resources and identify cybersecurity gaps.
nist.gov/publications/detail/nistir/8192/fnal). Beyond
This project has helped showcase how the NCCoE
NISTIR 8192, the workshop led to the launch of two
can apply standards and best practices to real-world
new NCCoE projects: Mitigating IoT Based Automated
industry challenges to help companies more easily
|     |     |     |     |     | Distributed  | Threats  | and  | TLS  | Server  Certifcate  |     |
| --- | --- | --- | --- | --- | ------------ | -------- | ---- | ---- | ------------------- | --- |
take advantage of existing guidance.
Management.
Workshops & Events
Additionally, the regularly held NCCoE Speaker
|     |     |     |     |     | Series  showcases  |     | thought  | leaders  | that  highlight  |     |
| --- | --- | --- | --- | --- | ------------------ | --- | -------- | -------- | ---------------- | --- |
critical cybersecurity issues of national importance
|     |     |     |     |     | across  | various  | industries.  | The  | Speaker  Series  | is  |
| --- | --- | --- | --- | --- | ------- | -------- | ------------ | ---- | ---------------- | --- |
jointly hosted by the NCCoE, Maryland Department
of Commerce, and Montgomery County Department
of Economic Development in collaboration with the
Maryland Tech Council. This year, the NCCoE hosted
four Speaker Series events, whose topics ranged from
how small businesses can utilize the NIST CSF, to
cybersecurity threats in the hospitality sector, to the
psychology behind insider threats.
|     |     |     |     |     | The        | NCCoE            | also          | hosted    | multiple  in-person  |      |
| --- | --- | --- | --- | --- | ---------- | ---------------- | ------------- | --------- | -------------------- | ---- |
|     |     |     |     |     | workshops  | with             | its  NCEP     | partners  | –  in  February      |      |
|     |     |     |     |     | at  the    | RSA  Conference  |               | and       | in  September        | at   |
|     |     |     |     |     | Juniper    | Networks’        | headquarters  |           | in  Sunnyvale,       | CA.  |
Figure 36: The Enhancing Resilience of the Internet
|     |     |     |     |     | The  workshops  |     | brought  | together  | dozens  | of  top  |
| --- | --- | --- | --- | --- | --------------- | --- | -------- | --------- | ------- | -------- |
and Communications Ecosystem Workshop  cybersecurity  experts  from  nearly  all  the  partner
|             |            |             |         |      | organizations  |     | to  discuss  | critical  | cybersecurity  |     |
| ----------- | ---------- | ----------- | ------- | ---- | -------------- | --- | ------------ | --------- | -------------- | --- |
| Throughout  | FY  2017,  | the  NCCoE  | hosted  | and  |                |     |              |           |                |     |
challenges, from identity to artifcial intelligence, that
participated in numerous workshops to defne, refne,
may beneft from NCCoE guidance.
| and  provide  | guidance  | on  technical  | cybersecurity  |     |     |     |     |     |     |     |
| ------------- | --------- | -------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
challenges facing businesses today.
Learn more about the NCCoE’s events at https://
nccoe.nist.gov/events.
For example, the NCCoE hosted NIST’s Workshop
| on  “Enhancing  | Resilience  | of  the  | Internet  | and  |     |     |     |     |     |     |
| --------------- | ----------- | -------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
Looking Ahead
Communications Ecosystem,” which brought together
over a hundred cybersecurity technologists, vendors,  Building on the robust stakeholder engagement
seen in FY 2017, the NCCoE expects to accelerate the
researchers, and subject matter experts. Executive
Order  13800,  “Strengthening  the  Cybersecurity  of  number of projects undertaken in FY 2018, reinforcing
Federal Networks and Critical Infrastructure,” required  the importance of the Healthcare, Financial Services,
the Secretaries of Commerce and Homeland Security  and Energy industries as well as expanding work in
to  “jointly  lead  an  open  and  transparent  process  identity  and  access  management,  the  Internet  of
to  identify  and  promote  action  by  appropriate  Things, and Internet infrastructure.  98
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

FOR MORE INFORMATION SEE:  Internet. The research focuses on the development
of measurement and modeling techniques necessary
https://nccoe.nist.gov
to understand, predict, and control the behavior of
CONTACTS:  Internet-scale  networked  information  systems.  The
ITL staf use these techniques to guide the design,
Ms. Donna Dodson         Mr. Tim Polk
|     |     |     | analysis,  | and  | standardization  | of  | new  technologies  |     |
| --- | --- | --- | ---------- | ---- | ---------------- | --- | ------------------ | --- |
(301) 975-3669                 (301) 975-3348
donna.dodson@nist.gov      william.polk@nist.gov  aimed at improving the robustness of the Internet’s
core infrastructure. Recent eforts have focused on
enhancing the security of several of the foundational
Mr. Tim McBride         Ms. KarenWaltermire
(301) 975-0214          (301) 975-0221   routing and communications protocols - the Internet’s
timothy.mcbride@nist.gov karen.waltermire@nist.gov  Domain  Name  System  (DNS),  Border  Gateway
|     |     |     | Protocol   | (BGP),            | and  Electronic  |     | mail  (Email)  | and       |
| --- | --- | --- | ---------- | ----------------- | ---------------- | --- | -------------- | --------- |
|     |     |     | messaging  | infrastructures.  |                  | In  | addition,      | the  IIP  |
program addresses other systemic vulnerabilities in
core Internet technologies such as those that enable
INTERNET INFRASTRUCTURE
massive scale Distributed Denial of Service (DDoS)
| PROTECTION  |     |     | attacks.  |     |     |     |     |     |
| ----------- | --- | --- | --------- | --- | --- | --- | --- | --- |
The Robust Inter-Domain Routing (RIDR) project
|        |     |         | aims  to  | remedy  | serious  | security  | and  | robustness  |
| ------ | --- | ------- | --------- | ------- | -------- | --------- | ---- | ----------- |
| ITL’s  |     | (IIP)   |           |         |          |           |      |             |
Internet  Infrastructure  Protection  vulnerabilities  in  the  Internet’s  global  BGP  routing
program, led by the Advanced Network Technologies  system. In FY 2017, the ITL staf, working with its
Division (ANTD), works with industry to develop the  Internet  Engineering  Task  Force  (IETF)  partners,
measurement science and new standards necessary
|     |     |     | completed  | the  | design  | and  standardization  |     | of  the  |
| --- | --- | --- | ---------- | ---- | ------- | --------------------- | --- | -------- |
to ensure the resilience and security of the global  BGPsec  Protocol  Specifcation  (RFC8205)  and
ROUTER  SECURITY
•
|     |     |     |     |     |     | -   | Forged  | BGP  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- |
•
|     |     |     |     |     |     |     | Route       | to  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
|     |     |     |     |     |     | '   | Enterprise  | A   |
- -
.
|     |     |     |     |     | .   |     |     | '   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
' '  '
BGPt  ............  '
:., .
| Legitimate  |     |     |     |     | .   | ',  |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
I
Route  to
Enterprise  A
|     | Data Traffic        | to  Enterprise  | A ---­      |     |     |     |     |     |
| --- | ------------------- | --------------- | ----------- | --- | --- | --- | --- | --- |
|     | HJacked to Attacker |                 | 's Network  |     |     |     |     |     |
99
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

supporting specifcations. BGPsec provides the ability  deployment. Figure 37 is a visualization generated by
to use digital signatures to prevent both malicious  one such monitoring tool that shows the current state
and accidental unauthorized routing messages from  of Route Origin Authorizations (ROAs) in the global
efecting Internet global routing operations.  Resource Public Key Infrastructure (RPKI). The RPKI
has been designed to provide the trust infrastructure
upon which Internet routing security technologies can
be based.
|     |     |     |     | In  FY         | 2017,  | as  BGPsec       | and  | RPKI  | technology  |      |
| --- | --- | --- | --- | -------------- | ------ | ---------------- | ---- | ----- | ----------- | ---- |
|     |     |     |     | specifcations  | and    | implementations  |      |       | matured,    | ITL  |
shifted its eforts to focus on technology transition
|     |     |     |     | and  operational  |            | issues           | associated  |          | with  the  | new       |
| --- | --- | --- | --- | ----------------- | ---------- | ---------------- | ----------- | -------- | ---------- | --------- |
|     |     |     |     | secure  routing   |            | technologies.    | The         | ITL      | staf       | and  its  |
|     |     |     |     | collaborators     | published  |                  | research    | results  | on         | high-     |
|     |     |     |     | speed  BGPsec     |            | implementations  |             | that     | attempt    | to        |
In  addition  to  standards  development,  NIST  minimize  the  operational  performance  impact  of
developed and released an open source reference  routing  security.  Figure  38  illustrates  a  prototype
implementation  of  emerging  IETF  BGPsec  model for investigating and validating the emerging
specifcations, on-line test tools to foster their adoption  BGP security extensions and supporting protocols.
and measurement systems to track their operational
|     |     | Global: 25 Autonomous  | Systems  |     |     |     |     |     |     |     |
| --- | --- | ---------------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
with the most Prefixes VALID by RPKI
|                           |     |                    |         |     |        |     |                                         |                       |       |     |
| ------------------------- | --- | ------------------- | -------- | --- | ------ | --- | --------------------------------------- | --------------------- | ----- | --- |
|                           |     | Valid  D Not-fow1d  | Invalid  |     |        |     |                                         |                       |       |     |
| AS                        |     |                     |          |     |        |     | OrgName                                 |                       |       |     |
| 8551                      |     |                     |          |     | 3,589  |     | BEZEQ--INTERNATIONAL-AS Bezeqint lntE   |                       |       |     |
| 10620                     |     |                     |          |     |        |     | TernexColo                              | bia S.A., CO          |       |     |
| 11830                     |     |                     | 2 267    |     |        |     | lnstttuto Costarrioense                 | de Electricidad y T,  |       |     |
| 7303                      |     | 1258  255 -l,517    |          |     |        |     | Telecom Argentina S.A., AR              |                       |       |     |
| 3816                      |     |                     |          |     |        |     | COLOMBIA TELECOMUNICAOIONES S.A.        |                       |       |     |
| 6147                      |     |                     |          |     |        |     | Telefonica del Peru SAA.                |                       | , PE  |     |
| 27738                     |     |                     |          |     |        |     | Eouac!ortelecom S.A., EC                |                       |       |     |
| 31148                     |     |                     |          |     |        |     | FREENET-AS, UA                          |                       |       |     |
| 8866                      |     |                     |          |     | +      |     | BTC-AS BULGARIA, BG                     |                       |       |     |
| 13489                     |     |                     |          |     |        |     | EPMTelooornunicaciones S.A. E.S.P., CO  |                       |       |     |
| 55430                     |     | 664 -l,263          |          |     |        |     | STARHUBINTERNET-AS-SNGNBN Startiub      |                       |       |     |
| 6057 1-==;;;;;;;;~i,';;;~ |     | -----=-=--"         |          |     |        |     |                                         |                       |       |     |
Adrninistracion Nacional de Teleoornunica
| 6830       | 328 B5i  |           |     |     |     |     | LG'-'UPC formerly known as UPC Broadba    |                            |     |     |
| ---------- | -------- | --------- | --- | --- | --- | --- | ----------------------------------------- | -------------------------- | --- | --- |
| 3215  521  | 282      | -851      |     |     |     |     | AS3215, FR                                |                            |     |     |
| 21826      |          |           |     |     |     |     | Corporaaion Telernic C.A., VE             |                            |     |     |
| 28006      |          |           |     |     |     |     | CORPORACION NACIONAL DE TELECOMl          |                            |     |     |
| 9541       |          |           |     |     |     |     | CYB ERN ET-AP Cyber Internet Services (F  |                            |     |     |
| 18101      |          | 474 '916  |     |     |     |     | RELIANCE-COMMUNICATIONS-IN' Refia.nCE     |                            |     |     |
| 50710      |          |           |     |     |     |     | EARTHLINK-AS, IQ                          |                            |     |     |
| 9299       |          | I         |     |     |     |     | IPG-AS-A P P,                             | pp·ne Long Distance Telep  |     |     |
| 8048       |          |           |     |     |     |     | CANTV Servicios, Venezuela, VE            |                            |     |     |
| 19429      |          |           |     |     |     |     | ETB -Colombia, CO                         |                            |     |     |
| 52228      |          |           |     |     |     |     | Cable Tica, CR                            |                            |     |     |
47524
TURKSAT-AS, TR
4760 l====="'===============================J  HKTIMS-AP PCCW l.Jirnited, HK
| 0   | 500  | 1,000  1,500  | 2,000  2,500  | 3,000  | 3,500  | 4,000  |     |     |     |     |
| --- | ---- | ------------- | ------------- | ------ | ------ | ------ | --- | --- | --- | --- |
Prefix Count
| NIST RPKI Monitor | : 201&-05-31  |     |     |     |     |     |     |     |     |     |
| ----------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 37: Measurement of global networks with most BGP announcements protected by RPKI.  100
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

Software Suite
https://bgpsrx.antd.nist.gov
•  RPKI-RTR-SVR
•  QuaggaSRx (QSRx)
•  RPKI Validation Cache Simulator
|     | •  RPKI/  BGPsecR  | outer  |     |     |     |
| --- | ------------------ | ------ | --- | --- | --- |
•  BGPSEC-10 (BIO)
|     | •  SRx Server/  | Proxy (SRxSnP)  |     |                      |        |
| --- | --------------- | --------------- | --- | -------------------- | ------ |
|     |                 |                 |     | •  BGPsecTrafficGene | rator  |
•  RPKI/  BGPsecValidation Server
•  SRxCryptoAPI (SCA)
|                 | •  Crypto Module for QSRx&  |     |  SRxSnP  |     |             |
| --------------- | --------------------------- | --- | -------- | --- | ----------- |
| BGPsecT raffic  |                             |     |          |     | ROA Script  |
RFC8210
10.0.0.0/8 , 10 20 30 65530  RPKI-RTR-SRV  add 10.0.0.0/8  16 65530
| 10.10.0.0/16 30 65530  |     |     |     | Cache  | add 10.10.0.0/16 24 65530  |
| ---------------------- | --- | --- | --- | ------ | -------------------------- |
10.20.0.0/16  100 200 65531  Test Harness  add 10.20.0.0/16  24 65531
|     |     |     | Process BGP Validation          | Requests  |     |
| --- | --- | --- | ------------------------------- | --------- | --- |
|     |     |     | Process BGPsec Path Validation  | Requests  |     |
Some BGPsec Router
RFC 8205
Figure 38: NIST BGPsec prototypes and test tools
To further facilitate technology transition, a new

NCCoE Secure Inter-Domain Routing (SIDR) project
Robust Inter-Domain Routing Project
| was  initiated  | with  industry  | partners  | to  conduct  a  |     |     |
| --------------- | --------------- | --------- | --------------- | --- | --- |
https://www.nist.gov/programs-projects/robust-in-
proof-of-concept evaluation of the current state of
ter-domain-routing
secure routing technologies in realistic deployment
| settings.  |     |     | NCCoE Secure-Inter-Domain Routing Project  |     |     |
| ---------- | --- | --- | ------------------------------------------ | --- | --- |
https://nccoe.nist.gov/projects/building-blocks/se-
A second thrust of ITL’s RIDR project is addressing
cure-inter-domain-routing
| the  wide-spread  | problem  | of  BGP  “route  | leaks”  –  |     |     |
| ----------------- | -------- | ---------------- | ---------- | --- | --- |
CONTACTS:
accidental routing policy violations that often result in
large-scale outages in global Internet routing. The ITL
Mr. Doug Montgomery      Dr. Kotikalapudi Sriram
staf have lead the development of IETF specifcations  (301) 975-3630        (301) 975-3973
that defne the problem space (see RFC 7809, Problem  dougm@nist.gov        ksriram@nist.gov
Defnition and Classifcation of BGP Route Leaks) and
the corresponding proposed mitigation techniques.
FOR MORE INFORMATION:
NIST RPKI monitor
https://rpki-monitor.antd.nist.gov/
101
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

ADVANCED SECURITY TESTING  acceptance,  and  adoption  of  security  automation
|     |     |     |     |     |     |     |     | solutions  | to  address  current  | and  | future  | security  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------- | ---- | ------- | --------- | --- |
AND MEASUREMENTS
challenges, creating opportunities for innovation.
Security Automation and Continuous  Specifcation, Standards, and
| Monitoring  |     |     |     |     |     |     |     | Guidance Development  |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
IT  organizations  operate  a  diverse  set  of  To support the overarching security automation
computing  assets  that  access,  route,  store,  and  vision,  it  is  necessary  to  have  specifcations  that
process information that is critical to the operations of  describe the required interactions between systems,
businesses and the missions of government agencies.  standards  that  document  international  consensus
These IT environments are under constant threat of  approaches, and guidance for product developers and
attack and are frequently undergoing change, with  implementers. Through close work with partners in
government, industry, and academia, CSD continues
| new  and  | updated  | software  |     | being  | deployed  |     | along  |     |     |     |     |     |     |
| --------- | -------- | --------- | --- | ------ | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
with  updated  confgurations.  The  wide  variety  of  to facilitate the defnition and development of security
computing products, the dynamic nature of software,  automation approaches that enable organizations to
the speed of confguration change, and the diversity  understand and manage IT security risks.
of threats require organizations to maintain situational
During FY 2017, CSD has continued to build on
| awareness  | over  | their  | IT  | assets  | and  to  | utilize  | this  |     |     |     |     |     |     |
| ---------- | ----- | ------ | --- | ------- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
previous security automation work, as follows:
information to make informed risk-based decisions.
•   Identifed and addressed gaps in the current
| Security  | automation  |     |     | utilizes  | standardized  |     | data  |     |     |     |     |     |     |
| --------- | ----------- | --- | --- | --------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
specifcations;
formats and transport protocols to enable data to
be  exchanged  between  business,  operational,  and  •   Evolved existing approaches to achieve
security systems that support security processes by:
greater scalability and impact;
•   Identifying IT assets, including hardware,
•   Participated in working groups in standards
| software, and data;  |     |     |     |     |     |     |     | development organizations to promote  |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
international consensus around standardized
•   Providing awareness over the operational
approaches;
state of computing devices;
•   Provided additional guidance on architectural,
•   Enabling security reference data to be
design, and analysis concerns; and
collected from internal and external sources;
| and  |     |     |     |     |     |     |     | •   Developed and maintained tools and reference  |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
implementations.
•   Supporting analysis processes that measure
the efectiveness of security controls and
CSD is currently working with its partners in various
provide visibility into security risks, enabling  standards-development  organizations,  including
risk-based decision making.
|             |     |            |     |        |        |           |     | ISO,  IETF,     | the  Organization       | for  the   | Advancement  |        |     |
| ----------- | --- | ---------- | --- | ------ | ------ | --------- | --- | --------------- | ----------------------- | ---------- | ------------ | ------ | --- |
|             |     |            |     |        |        |           |     | of  Structured  | Information             | Standards  | (OASIS),     | the    |     |
| Commercial  |     | solutions  |     | built  | using  | security  |     |                 |                         |            |              |        |     |
|             |     |            |     |        |        |           |     | Forum           | of  Incident  Response  | and        | Security     | Teams  |     |
automation specifcations enable the collection and
(FIRST), and the Trusted Computing Group (TCG), to
harmonization of vast amounts of operational and
further mature and broaden the adoption of security
security data into coherent, comparable information
|     |     |     |     |     |     |     |     | automation  | specifcations,  | reference  | data,  | and  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ---------- | ------ | ---- | --- |
streams to achieve situational awareness that allows
techniques. This area of work is focused on evolving
| the  timely  | and  | active  | management  |     | of  | diverse  | IT  |     |     |     |     |     |     |
| ------------ | ---- | ------- | ----------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
security automation specifcations to integrate with
| systems.  | Through  | the  | creation  |     | of  reference  |     | data  |     |     |     |     |     |     |
| --------- | -------- | ---- | --------- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
existing transport protocols to provide for the secure,
| and  guidance  |     | and  the  | international  |     | recognition  |     | of  |     |     |     |     |     |     |
| -------------- | --- | --------- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
interoperable exchange of security automation data.
fexible, open standards, the NIST security automation
|     |     |     |     |     |     |     |     | Additional  | work  is  focused  | on  evolving  |     | security  | 102  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------ | ------------- | --- | --------- | ---- |
program works to improve the interoperability, broad
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

metrics and providing consensus guidance on security  security software products communicate information
automation  approaches.  Through  the  defnition  about  software  faws,  security  confgurations,  and
and  adoption  of  security  automation  standards  other  aspects  of  the  device  state.  SCAP  enables
and guidelines, IT vendors will be able to provide  security automation content, also known as “SCAP
standardized security solutions to their customers.  content,”  to  be  expressed  using  standardized
These solutions support continuous monitoring and  formats, identifers, and scoring models. This content
automated,  dynamic  network  defense  capabilities,  can be used by any tool that is conformant to the
based on the analysis of data from operational and  specifcations  to  collect  and  evaluate  the  state  of
security  data  sources  and  the  collective  action  of  software installed on a device.
security components.
Additionally, CSD is working with the vulnerability
| community  | to  | enable  | the  | automated  |     | analysis  | of  |     |     |     |     |     |     |
| ---------- | --- | ------- | ---- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
metrics such as the Common Vulnerability Scoring
| System  | (CVSS),  | establishing  |     | a   | baseline  | of  | the  |     |     |     |     |     |     |
| ------- | -------- | ------------- | --- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- |
minimum information needed to properly inform the
vulnerability management process, and facilitating the
sharing of vulnerability information across language
barriers. To assist in this work, a public draft of NISTIR
| 8138,  Vulnerability  |      | Description     |     | Ontology          |     | (VDO):  | A    |     |     |     |     |     |     |
| --------------------- | ---- | --------------- | --- | ----------------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- |
| Framework             | for  | Characterizing  |     | Vulnerabilities,  |     |         | was  |     |     |     |     |     |     |
created to foster a conversation and collect feedback
| on  the         | best  | mechanisms  |                | to  improve  | the         | degree  |     |     |     |     |     |     |     |
| --------------- | ----- | ----------- | -------------- | ------------ | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| of  automation  |       | within      | vulnerability  |              | management  |         |     |     |     |     |     |     |     |
processes. CSD is planning to develop this document
iteratively by releasing additional drafts in FY 2018 to
Credit: Shutterstock/Den Rise
ensure participation from as many stakeholders in the
vulnerability community as possible.  SCAP  has  been  widely  adopted  by  major
|                |     |             |                  |                |            |          |      | software  | and            | hardware  | manufacturers  |             | and  has         |
| -------------- | --- | ----------- | ---------------- | -------------- | ---------- | -------- | ---- | --------- | -------------- | --------- | -------------- | ----------- | ---------------- |
| Security       |     | automation  | standardization  |                |            | work     | has  |           |                |           |                |             |                  |
|                |     |             |                  |                |            |          |      | become    | a  signifcant  |           | component      |             | of  information  |
| been  focused  |     | in  three   | areas:           | the            | evolution  |          | and  |           |                |           |                |             |                  |
|                |     |             |                  |                |            |          |      | security  | management     |           | and            | governance  | programs.        |
| international  |     | adoption    | of               | the  Security  |            | Content  |      |           |                |           |                |             |                  |
SCAP-enabled tools are currently being used by the
| Automation  | Protocol  |             | (SCAP),  | the        | development  |              | of  |                    |     |           |                 |     |             |
| ----------- | --------- | ----------- | -------- | ---------- | ------------ | ------------ | --- | ------------------ | --- | --------- | --------------- | --- | ----------- |
|             |           |             |          |            |              |              |     | U.S.  Government,  |     | critical  | infrastructure  |     | companies,  |
| software    | asset     | management  |          | standards  |              | to  support  |     |                    |     |           |                 |     |             |
academia, and other businesses, both domestically
operational  and  cybersecurity  use  cases,  and  the  and  internationally.  Currently,  CSD  is  leveraging
| development  |     | of  security  |     | automation  |     | consensus  |     |           |           |         |       |              |           |
| ------------ | --- | ------------- | --- | ----------- | --- | ---------- | --- | --------- | --------- | ------- | ----- | ------------ | --------- |
|              |     |               |     |             |     |            |     | SCAP  in  | multiple  | areas,  | both  | to  support  | its  own  |
standards. The following sections detail this work.
mission and to enable other agencies and private-
sector entities to meet their goals. For CSD, SCAP is
a critical component of the SCAP Validation Program,
Security Content Automation
the National Vulnerability Database (NVD), and the
Protocol (SCAP)
National Checklist Program (NCP).
SCAP is a multipurpose protocol that provides
In September 2012, CSD published SP 800-126
an automated means to collect and assess the state
Revision 2, The Technical Specifcation for the Security
of devices. SCAP supports automated vulnerability
Content Automation Protocol (SCAP): SCAP Version
| checking,  | verifying  |               | the  | installation  | of  | patches,   |     |             |           |     |            |      |                |
| ---------- | ---------- | ------------- | ---- | ------------- | --- | ---------- | --- | ----------- | --------- | --- | ---------- | ---- | -------------- |
|            |            |               |      |               |     |            |     | 1.2.  That  | document  |     | describes  | the  | 11  component  |
| checking   | security   | confguration  |      | settings,     |     | verifying  |     |             |           |     |            |      |                |
specifcations composing SCAP. See Table 3 for details.
technical-control compliance, measuring security, and
examining systems for indicators of a compromise.  Since the release of SCAP 1.2, CSD has worked
SCAP uses the Extensible Markup Language (XML) to  to improve guidance for using SCAP specifcations.
103
standardize the format and nomenclature by which  In FY 2015, CSD released draft NISTIR 8058, Security
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

Content Automation Protocol (SCAP) Version 1.2 Scoring System (CVSS) v3, which was
Content Style Guide: Best Practices for Creating released in June 2015;
and Maintaining SCAP 1.2 Content, which provides
• Removal of support for CVSSv2; and
guidance for SCAP 1.2 content creators to ensure that
stylistic variations in SCAP 1.2 content are addressed
• Deprecation of support for older specifcation
in a way that improves the accuracy and consistency
revisions and SCAP 1.0.
of results, avoids performance problems, reduces
user efort, lowers content maintenance burdens, and CSD is currently working to publish the fnal
enables content reuse. To achieve this, NISTIR 8058 versions of the publications described above in
documents best practices for content creation and early FY 2018. CSD has published a beta release of
encourages their use by SCAP content authors and an updated version of SCAPVal, the SCAP content
maintainers. Feedback on this document is welcomed validation tool. A fnal version of this tool will be
and will help CSD to work toward producing a fnal provided after the SP 800-126 documents have been
version of this NISTIR 8058. fnalized. CSD is also working to update the SCAP
Validation Program to support SCAP 1.3, with an
update to NISTIR 5711 to be posted in early FY 2018.
More information on SCAP 1.3 can be found at: https://
csrc.nist.gov/Projects/Security-Content-Automation-
Protocol/SCAP-Releases/SCAP-1-3.
CSD is also starting to plan an SCAP 2.0 release
(SCAP v2). This release will further defne the
interfaces and use of transport protocols for SCAP
tools to provide component-level interoperability
between products supporting various SCAP
functions. By providing more interoperability, SCAP
v2 will provide the basic software and confguration
posture information needed to make and automate
management decisions for networked devices as
Credit: Shutterstock/Titima Ongkantong
part of the license, vulnerability and confguration
CSD is actively working on an SCAP 1.3 revision. In management practices, supporting improved
July 2016, CSD posted drafts for public comment of networked device hygiene. Furthermore, the posture
SP 800-126 Revision 3 and SP 800-126A. SP 800-126 information provided by SCAP v2 products will provide
Revision 3, is The Technical Specifcation for the Security much of the context needed to prevent, detect, and
Content Automation Protocol (SCAP): SCAP Version respond to network attacks. This additional context
1.3. SP 800-126A is SCAP 1.3 Component Specifcation will enable SCAP v2 information to be applied for
Version Updates: An Annex to NIST Special Publication application whitelisting, the detection of anomalous
800-126 Revision 3. These publications collectively behavior, the gathering and use of indicators, the
document the draft requirements for SCAP 1.3. SP use of machine-readable threat information, and for
800-126A is a new publication that allows SCAP 1.3 to orchestrating courses of action. CSD is preparing a
take advantage of selected minor version updates of draft whitepaper for release in early FY 2018 that will
SCAP component specifcations, as well as designated outline an approach, a development plan identifying
Open Vulnerability and Assessment Language (OVAL) the new and revised specifcations that will be
platform schema revisions. The SCAP 1.3 revision needed, and a transition plan for moving from SCAP
includes the following changes: 1.x to SCAP 2.0. A discussion draft of the SCAP 2.0
specifcation addressing software asset management
• Adoption of the Open Vulnerability and
and vulnerability management use cases will also
Assessment Language (OVAL) 5.11.1, which
be published in FY 2018 as a way to start a broader
was released in April 2015;
conversation with the SCAP community about where
104
to focus next on the development of SCAP 2.0.
• Adoption of the Common Vulnerability
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

TABLE 3: SCAP 1.2 SPECIFICATIONS
SPECIFICATIONS DESCRIPTION
Languages
Extensible Confguration Checklist Description Used for authoring security checklists/benchmarks
Format (XCCDF) 1.2 and for reporting the results of evaluating them
Used for representing system-confguration
Open Vulnerability and Assessment Language
information, assessing machine state, and reporting
(OVAL) 5.11.2
assessment results
Used for representing checks that collect information
Open Checklist Interactive Language (OCIL) 2.0 from people or from existing data stores populated
by other data collection methods
Reporting Formats
Used to express information about assets and to
Asset Reporting Format (ARF) 1.1
defne the relationships between assets and reports
Used to uniquely identify assets based on known
Asset Identifcation 1.1
identifers and other asset information
Identifcation Schemes
A nomenclature and dictionary of hardware,
Common Platform Enumeration (CPE) 2.3 operating systems, and applications; a method to
identify the applicability to platforms
A structured metadata format for describing a
Software Identifcation (SWID) Tags 2015
released software product
A nomenclature and dictionary of software-security
Common Confguration Enumeration (CCE) 5
confgurations
A nomenclature and dictionary of security-related
Common Vulnerabilities and Exposures (CVE)
software faws
Measurement and Scoring Systems
Used for measuring the relative severity of software
Common Vulnerability Scoring System (CVSS)
faws
Used for measuring the relative severity of device
Common Confguration Scoring System (CCSS)
security (mis-)confguration issues
Content and Result Integrity
Guidance for using digital signatures in a common
Trust Model for Security Automation Data (TMSAD) trust model applied to security automation
105
specifcations
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

Software Asset Management  and related software patches, and assessing secure
software confgurations.
Standards
|                |              |                |                      |       |              | To             | supplement  |      | the  requirements  |       | in      | ISO/IEC  |
| -------------- | ------------ | -------------- | -------------------- | ----- | ------------ | -------------- | ----------- | ---- | ------------------ | ----- | ------- | -------- |
| CSD            | has  been    | collaborating  |                      | with  | industry     |                |             |      |                    |       |         |          |
|                |              |                |                      |       |              | 19770-2:2015,  |             | CSD  | collaborated       | with  | DHS,    | NSA,     |
| partners       | to  promote  | the            | adoption             |       | of  ISO/IEC  |                |             |      |                    |       |         |          |
|                |              |                |                      |       |              | and  MITRE     | on          | the  | development        | of    | NISTIR  | 8060,    |
| 19770-2:2015,  | Information  |                | technology—Software  |       |              |                |             |      |                    |       |         |          |
Guidelines for the Creation of Interoperable Software
| asset  management—Part  |     |     | 2:  Software  |     | identifcation  |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Identifcation (SWID) Tags. NISTIR 8060, published in
| tag,  which  | establishes  | a   | specifcation  |     | for  tagging  |     |     |     |     |     |     |     |
| ------------ | ------------ | --- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
April 2016, provides an overview of the capabilities
software to support identifcation and management.
and usage of SWID tags as part of a comprehensive
| The  software  | identifcation  |     | (SWID)  |     | data  model  |           |             |     |               |             |     |       |
| -------------- | -------------- | --- | ------- | --- | ------------ | --------- | ----------- | --- | ------------- | ----------- | --- | ----- |
|                |                |     |         |     |              | software  | lifecycle.  |     | This  report  | introduces  |     | SWID  |
defned by this standard describes an XML format
tags in an operational context, provides guidelines
| for  software  | publishers  |     | to  provide  |     | authoritative  |           |           |     |                |       |     |             |
| -------------- | ----------- | --- | ------------ | --- | -------------- | --------- | --------- | --- | -------------- | ----- | --- | ----------- |
|                |             |     |              |     |                | for  the  | creation  | of  | interoperable  | SWID  |     | tags,  and  |
identifcation, categorization, software relationships
highlights key usage scenarios for which SWID tags
| (e.g.,  | dependency,  | bundling,  |     | and  | patching),  |     |     |     |     |     |     |     |
| ------- | ------------ | ---------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
are applicable. Figure 39 illustrates several types of
| executable  | and  library  | footprint  |     | details,  | and  other  |     |     |     |     |     |     |     |
| ----------- | ------------- | ---------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
SWID tags (as indicated in the legend) and how these
metadata for software. This information can be used
support multiple elements of the software product
to support operational and cybersecurity use cases
life cycle, including deployment, installation, patching,
around managing software deployments, managing
upgrading and removal.
software licenses, managing software vulnerabilities
LEGEND
| ~   | CORPUS   |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ~   | PRIMARY  |     |     |     |     |     |     |     |     |     |     |     |
~ SUPPLEMENTAL
| ~   | PATCH  |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 39: SWID Tags Support the Software Product Lifecycle
Additionally, in FY 2017, NIST has worked with  based collection of software inventory information
the IETF to integrate SWID tags into the Network  using SWID tag information.
Endpoint Assessment (NEA) protocol, through the
|     |     |     |     |     |     | The  | information  |     | provided  | within  | SWID  | tags  |
| --- | --- | --- | --- | --- | --- | ---- | ------------ | --- | --------- | ------- | ----- | ----- |
Software Inventory Message and Attributes (SWIMA)
|     |     |     |     |     |     | enhances  | the  | SCAP  | use  | cases  | by  | providing  |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ----- | ---- | ------ | --- | ---------- |
for PA-TNC specifcation (see https://datatracker.ietf.
authoritative information that can be used to create
| org/doc/draft-ietf-sacm-nea-swima-patnc/).  |     |     |     |     | This  |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
draft Request for Comments (RFC) will be published  Common  Platform  Enumeration  (CPE)  names,  to
support the targeting of checklists, and to associate
soon, describing a method for the automated, event- 106
|     |     |     |     |     |     | software  | faws  | to  products,  | based  |     | on  a  | defect  in  |
| --- | --- | --- | --- | --- | --- | --------- | ----- | -------------- | ------ | --- | ------ | ----------- |
ITL CYBERSECURITY PROGRAM AND PROJECTS  |  FY 2017

a  software  library  or  executable.  In  FY  2017,  CSD  automation-relevant  information  types.  The  ROLIE
published a SWID tag validation tool (see https://  draft has undergone two major revisions, with the
scap.nist.gov/specifcations/swid/),  called  SWIDVal,  fnal draft nearing completion. In addition, CSD has
that can validate a SWID tag document against the  begun the process of collaborating with MILE and
ISO/IEC 19770-2:2015 and NISTIR 8060 requirements.  other  stakeholders  to  create  extension  drafts  for
ROLIE that address a number of information types,
|     |     |     |     |     |     |     | including  | vulnerability,  |     | confguration  |     |     | checklist,  | and  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------------- | --- | --- | ----------- | ---- |
Development of Security Automation
software metadata information types.
Consensus Standards
The main ROLIE draft can be found at https://
CSD has been promoting the broad international  datatracker.ietf.org/doc/draft-ietf-mile-rolie/.
adoption of SCAP by encouraging the integration of  Additional information on ROLIE and on the extension
SCAP into other standards, and by adapting SCAP  drafts can be found in the working repository on
to address specifc gaps and challenges. CSD has  GitHub: https://github.com/CISecurity/ROLIE/.
continued its collaboration with its industry partners
|             |                 |     |             |         |      |                | CSD                | also      | worked   | with  | its      | government  |          | and     |
| ----------- | --------------- | --- | ----------- | ------- | ---- | -------------- | ------------------ | --------- | -------- | ----- | -------- | ----------- | -------- | ------- |
| in  the     | IETF  Security  |     | Automation  |         | and  | Continuous     |                    |           |          |       |          |             |          |         |
|             |                 |     |             |         |      |                | industry           | partners  | in       | the   | TCG      | to  defne   | a        | number  |
| Monitoring  | (SACM)          |     | working     | group.  |      | This  working  |                    |           |          |       |          |             |          |         |
|             |                 |     |             |         |      |                | of  specifcations  |           | related  |       | to  the  | Trusted     | Network  |         |
group provides a venue for advancing appropriate
Connect (TNC) protocol. The frst such publication
SCAP specifcations into international standards and
|     |     |     |     |     |     |     | is  the  TNC  | SCAP  | Messages  |     | for  | IF-M  | specifcation  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --------- | --- | ---- | ----- | ------------- | --- |
addressing identifed gap areas. The current scope of
that supports carrying the SCAP content and results
work for SACM includes identifying and/or defning
over the TNC protocols. IF-M is a messaging protocol
| the  transport  |     | protocols  |     | and  data  | formats  | needed  |              |              |     |     |              |     |              |     |
| --------------- | --- | ---------- | --- | ---------- | -------- | ------- | ------------ | ------------ | --- | --- | ------------ | --- | ------------ | --- |
|                 |     |            |     |            |          |         | that  helps  | communicate  |     |     | measurement  |     | information  |     |
to support the collection and evaluation of details
|            |     |           |        |          |     |                | about  | endpoints  | for  | evaluation  |     | against  |     | security  |
| ---------- | --- | --------- | ------ | -------- | --- | -------------- | ------ | ---------- | ---- | ----------- | --- | -------- | --- | --------- |
| regarding  | a   | device’s  | state  | against  |     | the  expected  |        |            |      |             |     |          |     |           |
policy. The second is the TNC Endpoint Compliance
values. The SACM working group has been working on
Profle (ECP) and related specifcations that support
identifying use cases, requirements, and architectural
the exchange of SWID data over the TNC protocols.
models to provide information to facilitate decisions
The ECP enables the collection of SWID data from a
about existing specifcations and standards that can
device for use by external tools to provide software
be referenced, required modifcations or extensions
inventory information. SCAP and SWID data collected
to existing specifcations and standards, and any gaps
using these mechanisms may be optionally used for
that need to be addressed. CSD is working with DHS,
network access control decision making, allowing the
the Center for Internet Security (CIS), and the TCG
device state to be evaluated when devices connect
to bring existing work into the IETF SACM working
and on an ongoing basis thereafter.
group, including OVAL and specifcations related to
the Trusted Network Connect (TNC) protocol.
|      |       |               |     |         |        |               | For     | more    | information                        |     | on  | this  | specifcation,  |     |
| ---- | ----- | ------------- | --- | ------- | ------ | ------------- | ------- | ------- | ---------------------------------- | --- | --- | ----- | -------------- | --- |
|      |       |               |     |         |        |               | please  | visit:  | http://www.trustedcomputinggroup.  |     |     |       |                |     |
| For  | more  | information,  |     | please  | refer  | to:  http://  |         |         |                                    |     |     |       |                |     |
org/resources/tnc_endpoint_compliance_profle_
datatracker.ietf.org/wg/sacm/charter/.
specifcation.
Also, within the IETF, CSD has been collaborating
Updated versions of the ECP and SWID-related
| with  the  | Managed  |     | Incident  | Lightweight  |     | Exchange  |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | --------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
specifcations, along with a usage scenario around
| (MILE)  | working  | group  |     | in  order  | to  | develop  the  |     |     |     |     |     |     |     |     |
| ------- | -------- | ------ | --- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
vulnerability assessment, are currently being worked
Resource-Oriented Lightweight Information Exchange
on in the SACM and MILE working groups, which are
| (ROLIE)  | specifcation.  |     |     | This  | specifcation  | seeks  |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | --- | ----- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
available through the locations indicated in Table 4.
| to  address  | the  | security  |     | automation  |     | information  |     |     |     |     |     |     |     |     |
| ------------ | ---- | --------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
discovery and dissemination use cases by defning
The SACM and MILE working groups have been
how tools are expected to communicate with security
developing the following related Internet Drafts:
automation information repositories. ROLIE allows for
the transport, retrieval, and storage of any security
107
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

INTERNET DRAFT PURPOSE
A Concise Binary Object Representation (CBOR)
https://datatracker.ietf.org/doc/draft-ietf-sacm-
[RFC7049] based specifcation for representing
coswid/
SWID tag for use with constrained IoT devices.
Specifes the Endpoint Compliance Profle (ECP),
that describes the use of IETF and TNC protocols
and interfaces to support the ongoing assessment
https://datatracker.ietf.org/doc/draft-ietf-sacm-ecp/
of endpoint posture and the controlled exposure of
collected posture information to authorized security
applications.
Extends the PA-TNC specifcation [RFC5792] to
https://datatracker.ietf.org/doc/draft-ietf-sacm-nea- provide specifc attributes and message exchanges
swima-patnc/ allowing endpoints to report their installed software
inventory information to a NEA server.
The ROLIE protocol supporting a resource-oriented
https://datatracker.ietf.org/doc/draft-ietf-mile-rolie/ approach for security automation information
publication, discovery, and sharing.
https://datatracker.ietf.org/doc/draft-ietf-sacm-rolie- An extension to ROLIE to support the exchange of
softwaredescriptor/ SWID-based software information.
https://datatracker.ietf.org/doc/draft-ietf-sacm- Defnition of the common terminology used within
terminology/ several working-group documents.
Additionally, CSD has several members who are For more information, please visit: http://www.
actively engaged on the CVE Board, which is working frst.org/global/sigs.
to improve the assignment of CVE identifers for
Through work with international standards-
vulnerabilities, with the overall goal of improving
developing organizations (SDOs), SCAP and its
the automated processing of vulnerabilities and the
related security automation capabilities are expected
timeliness of CVE identifer issuance.
to evolve and expand in support of the growing need
Finally, CSD has worked with FIRST by to defne and measure efective security controls,
participating in two Special Interest Groups (SIGs). assess and monitor ongoing aspects of information
The CVSS SIG (CVSS-SIG) is focused on maintaining security, remediate noncompliance, and successfully
and improving the CVSS scoring model, based on manage systems in accordance with the Risk
community feedback. The CVSS-SIG published CVSS Management Framework described in SP 800-37
Revision 3 (CVSS v3) in June 2015. The second SIG, Revision 1, Guide for Applying the Risk Management
the Vulnerability Reporting and Data eXchange SIG Framework to Federal Information Systems: A Security
(VRDX-SIG), researches and recommends methods for Life Cycle Approach. Standards that are developed
identifying and exchanging vulnerability information and published by these SDOs will be considered for
across disparate vulnerability databases. inclusion in future revisions of SCAP. 108
ITL CYBERSECURITY PROGRAM AND PROJECTS | FY 2017

FOR MORE INFORMATION, SEE: • Over 96,000 vulnerability advisories, with an
average of 62 new vulnerabilities added daily;
https://scap.nist.gov/
• 183 SCAP-expressed checklists across 123
CONTACT:
platforms containing thousands of low-level
Mr. David Waltermire
security confguration checks that can be
(301) 975-3390
used by SCAP-validated security products to
david.waltermire@nist.gov
perform automated evaluations of the system
state;
Security Automation Reference Data
• 293 non-SCAP security checklists (e.g., English
prose guidance and confguration scripts);
Through the National Vulnerability Database and
the National Checklist Program (see below), NIST is
• 249 U.S. Computer Emergency Readiness
providing relevant and important reference data in the
Team (US-CERT) alerts; 4,467 US-CERT
areas of vulnerability and confguration management.
vulnerability summaries; and 10,286 SCAP
SCAP and the programs that leverage it are moving
machine-readable software faw checks; and
the information assurance industry toward being
able to standardize communications and toward the • A product dictionary with over 124,000
collection and storage of relevant data in standardized operating system, application, and hardware
formats, as well as providing an automated means for name entries; and over 75,000 vulnerability
the assessment and remediation of systems for both advisories translated into Spanish.
vulnerabilities and confguration compliance.
NVD is hosted and maintained by NIST and is
sponsored by the Department of Homeland Security’s
National Vulnerability Database
US-CERT.
(NVD)
The use of SCAP data by commercial security
products, deployed in thousands of organizations
Security automation reference data is currently
worldwide, has extended NVD’s efective reach.
housed within the NVD. The NVD is a comprehensive
Increasing demand for NVD XML data feeds (i.e.,
cybersecurity vulnerability database that allows
mechanisms that provide updated data from data
the tracking of vulnerability trends over time. This
sources) and SCAP-expressed content from the NVD
trending service allows users to assess changes in
website demonstrates an increased adoption of SCAP.
vulnerability discovery rates within specifc products
or within specifc types of vulnerabilities. NVD data
In the past year, the NVD began providing CVSS
is represented using the SCAP specifcations. The
base scores following the CVSS v3 specifcation within
NVD includes databases of security confguration
the data feeds and completed a major enhancement
checklists for the NCP, listings of publicly known
to the overall user interface. The NVD has also seen a
software faws, product names, and impact metrics. A
signifcant increase (almost three fold) in vulnerabilities
formal validation program tests the ability of vendor
received and analyzed over the previous year. Overall,
products to use some forms of security automation
the NVD has experienced an average download
data, based on a product’s conformance in support of
growth rate of over 10 % per month.
specifc enterprise capabilities.
FOR MORE INFORMATION, SEE:
SCAP defnes the structure of standardized
https://nvd.nist.gov
software faws and security confguration reference
data, also known as SCAP content. This reference data
CONTACT:
is provided by the NVD.
Mr. Robert Byers
As of the end of September 2017, the NVD (301) 975-3279
contained the following resources: robert.byers@nist.gov
109
NIST/ITL CYBERSECURITY PROGRAM ANNUAL REPORT 2017

National Checklist Program (NCP) (FAR) was published. Paragraph (d) of section 39.101
states, “In acquiring information technology, agencies
There are many threats to IT, ranging from shall include the appropriate IT security policies and
remotely launched network service exploits to requirements, including the use of com

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-25", "model": "legacy"} -->
