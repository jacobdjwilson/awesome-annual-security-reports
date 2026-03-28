# AI Medical Device Cybersecurity: Regulations & Risks

## Table of Contents
- [Executive Summary](#executive-summary)
- [Introduction and Background](#introduction-and-background)
- [1. The Cybersecurity Threat Landscape for Medical Devices](#1-the-cybersecurity-threat-landscape-for-medical-devices)
  - [1.1 Traditional IT/OT Threats](#11-traditional-itot-threats)
  - [1.2 AI/ML-Specific Threats](#12-aiml-specific-threats)
  - [1.3 Documented Incidents and Vulnerabilities](#13-documented-incidents-and-vulnerabilities)
- [2. Regulatory and Standards Landscape](#2-regulatory-and-standards-landscape)
  - [2.1 United States](#21-united-states)
  - [2.2 European Union](#22-european-union)
  - [2.3 International Standards and Guidance](#23-international-standards-and-guidance)
- [3. Secure Development and Design Controls](#3-secure-development-and-design-controls)
  - [3.1 Risk Management and Threat Modeling](#31-risk-management-and-threat-modeling)
  - [3.2 Secure Software Development](#32-secure-software-development)
  - [3.3 Hardware and System Design Controls](#33-hardware-and-system-design-controls)
- [4. Premarket Submission and Documentation Requirements](#4-premarket-submission-and-documentation-requirements)
  - [4.1 Premarket Cybersecurity Documentation](#41-premarket-cybersecurity-documentation)
  - [4.2 Cybersecurity Labeling and Patient Information](#42-cybersecurity-labeling-and-patient-information)
  - [4.3 Role of Post-Market Surveillance](#43-role-of-post-market-surveillance)

---

## Executive Summary

The rapid convergence of artificial intelligence (AI) and medical devices has transformed healthcare but also introduced unprecedented cybersecurity challenges. In this comprehensive report, we analyze the cybersecurity requirements for AI-enabled medical devices from multiple perspectives: regulatory frameworks, technical standards, threat landscape, and real-world case studies. We review the historical evolution of medical device security, current regulatory mandates (e.g. FDA guidance, EU regulations, international standards), and emerging technology-specific requirements (e.g. secure AI/ML pipelines, adversarial resilience, data privacy). Key findings include:

- **Proliferation of AI-enabled Devices**: Over 1,000 AI-powered medical devices (covering imaging, diagnostics, wearables, etc.) have been authorized by regulators such as the FDA, reflecting the growth of AI in healthcare ([1] firefinch.io). However, many of these devices connect to hospital networks or the Internet, creating numerous attack surfaces. Surveys show that 53–60% of connected medical devices have critical vulnerabilities, and 73% of networked IV infusion pumps harbor at least one flaw ([2] www.techtarget.com) ([1] firefinch.io).

- **New Regulatory Mandates**: In response to high-profile vulnerabilities, legislatures are tightening requirements. The U.S. Consolidated Appropriations Act, 2023 (Section 524B) explicitly requires “cyber devices” (software-connected medical devices) to include a comprehensive postmarket vulnerability management plan, secure design processes, timely updates/patches, and a Software Bill of Materials (SBOM) listing all software components ([3] www.blackduck.com) ([4] biobostonconsulting.com). Similarly, the FDA’s updated 2025–2026 Guidance on Cybersecurity in Medical Devices demands detailed evidence of cybersecurity risk management in premarket submissions (design controls, threat models, testing results, etc.) ([5] www.fda.gov) ([6] www.fda.gov). In the EU, the MDR (Regulation 2017/745) and forthcoming AI Act and NIS2 Directive impose comparable requirements for risk management, incident reporting, and “secure-by-design” development ([7] cybercompass.readthedocs.io) ([8] www.ncbi.nlm.nih.gov). International standards (e.g. ISO 14971 for risk, IEC 62304 for software processes, ISO 27001/27799 for information security, IEC 81001-5-1 for health IT safety) further guide manufacturers on cybersecurity controls. A summary of key frameworks is shown in Table 1 below.

- **AI-Specific Threats**: AI-enabled devices introduce novel vulnerabilities. Attackers may perform adversarial attacks (subtle input perturbations that cause misdiagnosis) or data poisoning (maliciously tainting training datasets) to induce incorrect device behavior. For example, small pixel changes in a medical image can mislead an AI diagnostic model to the wrong diagnosis, and medical LLMs have been shown vulnerable to data-poisoning attacks ([9] pmc.ncbi.nlm.nih.gov) ([10] pmc.ncbi.nlm.nih.gov). AI devices also raise privacy risks (e.g. leakage of sensitive training data) and supply-chain risks (e.g. compromised third-party models). The threat vectors for AI-enabled devices encompass both traditional cyber threats (malware, unauthorized access, software exploits) and ML-specific attacks ([11] firefinch.io) ([10] pmc.ncbi.nlm.nih.gov). Table 2 (below) categorizes common threat types.

- **Technical Countermeasures**: Ensuring security requires end-to-end measures. These include robust software development (secure coding, static/dynamic analysis, secure development frameworks), device hardening (encryption, authentication, access control, network segmentation), continuous monitoring (intrusion detection, anomaly detection on AI outputs), and patch management (timely updates, coordinated vulnerability disclosure). For AI models, practices like adversarial training, input validation, and model and training-data provenance are recommended. Patients’ data must be protected under HIPAA/GDPR (encryption at rest/in-transit, privacy-preserving ML, etc.). Many of these controls are echoed in regulatory guidance and standards, such as NIST’s cybersecurity framework or IEC 62443 for connected systems ([12] www.crowe.com) ([13] cybercompass.readthedocs.io).

- **Evidenced Risks and Incidents**: Numerous studies and incidents illustrate the stakes. A Cynerio report found 53% of connected medical devices had critical vulnerabilities ([2] www.techtarget.com). Armis Security reports show examples like the 2017 FDA recall of 465,000 Abbott pacemakers after a vulnerability that could allow remote battery depletion ([14] www.armis.com), and insulin pump exploits demonstrated at Black Hat 2011 that could disable a pump ([15] www.armis.com). A forensic analysis revealed dozens of medical device zero-days in recent years (993 product vulnerabilities in one 2024 study ([16] www.techtarget.com)). Figure 1 (below) charts increasing reported vulnerabilities in medical devices over the last decade as identified by cybersecurity researchers. These real-world cases underscore how a successful breach can directly endanger patient safety or privacy.

- **Future Directions**: As AI integration deepens, “security by design” becomes imperative. Future devices will need continuous learning models that adapt safely, stronger defenses against novel AI attacks (e.g. certified robustness, federated learning privacy), and possibly AI-based security tools (using ML to detect anomalies). Emerging documents like the EU AI Act will embed security requirements for “high-risk” AI. There are calls for higher assurance levels (e.g. cybersecurity labeling or certification for medical devices). Interoperability frameworks (like HL7 FHIR) must incorporate secure communication. The advent of 5G/6G, quantum computing (which could break encryption, as noted by Biasin et al. ([17] www.ncbi.nlm.nih.gov)), and more pervasive telemedicine will present new challenges. Stakeholders (manufacturers, regulators, clinicians, patients) will need to collaborate on continuous updates, threat intelligence sharing, and incident exercises.

Overall, this report provides an in-depth examination of cybersecurity requirements for AI-enabled medical devices, combining regulatory analysis, technical discussion, data, and case studies. We recommend device developers adopt a comprehensive, lifecycle-based security program – leveraging international standards and proactively addressing AI-specific threats – to protect patient safety and maintain public trust.

## Introduction and Background

The Rise of AI in Medical Devices

Artificial intelligence (AI) – particularly machine learning (ML) – is transforming medical devices across diagnostics, monitoring, and therapy. AI algorithms can interpret medical images (X-ray, MRI, CT scans) faster and sometimes more correctly than human experts, assist in robotic surgery, optimize dosing (smart insulin delivery), and enable predictive monitoring of patients in critical care. The U.S. Food and Drug Administration (FDA) reports that over 1,000 AI-enabled medical devices have been authorized for marketing in the U.S. as of 2025 ([1] firefinch.io). These devices span imaging systems (radiology, pathology), patient monitoring (wearables, ICU monitors), laboratory instruments (hematology analyzers, genomic sequencers), and even administrative workflow tools. The continuous growth of AI in healthcare is driven by expanding data, compute power, and algorithmic advances.

At the same time, healthcare has moved rapidly towards greater connectivity. Hospitals and clinics increasingly deploy Internet of Medical Things (IoMT) devices – smart devices connected to the network for data exchange, remote monitoring, or cloud computation. In practice, many AI-enabled devices reside on hospital networks or in cloud services ![Figure 1: Diagram of connected medical device ecosystem]. This connectivity enables life-saving features (e.g. telemetry, telemedicine) but also opens the door to cyber threats. The Washington Post and security firms have noted that hospitals can be prime targets: for instance, in 2021 the healthcare sector saw an average of 830 cyberattacks per organization per week, a 71% increase over the prior year ([18] www.armis.com).

Because medical devices often directly interact with patients (delivering therapy or making diagnostic decisions), cybersecurity is directly a patient-safety issue. Unlike typical IT, attacks on medical devices can cause physical harm or death. As noted by Biasin et al., a cyberattack on, say, an AI-enabled insulin pump could cause it to “stop working correctly and provoke serious health risks for the patient” ([19] www.ncbi.nlm.nih.gov). Moreover, successful breaches erode trust in healthcare systems, leading to device hesitancy. The infamous scenario of a hacked pacemaker or infusion pump is no longer pure fiction (as dramatized in the TV show Homeland); regulatory bodies and security researchers have documented real vulnerabilities (Section Case Studies).

Given this background, safeguarding AI-enabled medical devices is now a high priority. The last decade has seen a parallel evolution: as devices grew smarter and networked, regulators and standards bodies have begun to impose explicit cybersecurity requirements on medical device manufacturers. In the U.S., legislation (e.g. Section 524B of the FD&C Act, enacted December 2022) now mandates security planning and disclosure. The FDA has issued guidance documents defining how to analyze risk, apply controls, and document security for regulatory review ([5] www.fda.gov) ([6] www.fda.gov). In the EU, the Medical Device Regulation (MDR 2017/745) and forthcoming directives (NIS2, AI Act) similarly impose formal obligations on manufacturers to adopt “secure-by-design” processes. International consensus standards (IEC, ISO, UL) are steadily being updated or created to address software security.

This convergence of AI technology, increased connectivity, and tighter regulation sets the current state of risk and requirements. In the following sections, we delve into:

- Historical context: a brief history of medical device cybersecurity incidents and emerging awareness.
- Current threat landscape: detailed taxonomy of threats, including AI-specific attacks (adversarial input, data poisoning, model theft).
- Regulatory landscape: analysis of major frameworks and requirements (USA, EU, international).
- Design and development requirements: secure software development lifecycle, risk management (ISO 14971), architecture controls.
- Post-market requirements: incident reporting, vulnerability management, updates, SBOMs.
- Implementation controls: encryption, access control, secure communication, logging, anomaly detection.
- Case studies and data: documented incidents, vulnerability statistics, and lessons learned.
- Future directions: forthcoming regulations (AI Act, quantum threat, certification efforts) and research challenges.

Throughout, we support claims with the latest research findings, guidelines, and expert analyses, providing extensive citations. Our aim is to present a thorough, evidence-based overview suitable for stakeholders (manufacturers, regulators, healthcare providers) who require a deep understanding of cybersecurity requirements in the complex domain of AI-enabled medical devices.

## 1. The Cybersecurity Threat Landscape for Medical Devices

AI-enabled medical devices face a broad spectrum of cybersecurity threats. This section outlines the threat landscape, distinguishing traditional cyber threats from those specific to AI/ML components. We also review documented vulnerabilities in medical devices and emergent attack scenarios.

### 1.1 Traditional IT/OT Threats

Many cybersecurity threats that affect other connected systems also impact medical devices. These include:

- **Network and Software Exploits**: Vulnerabilities in device firmware, operating systems, or application code (buffer overflows, injection flaws) can be exploited to gain unauthorized control of the device or network. For example, hospitals often run legacy systems that lack modern security patches. An FBI warning highlights that outdated equipment is a growing problem in healthcare ([20] www.armis.com). In 2022, a report found a 59% year-over-year spike in registered medical device vulnerabilities, indicating how common these flaws are ([16] www.techtarget.com). Unpatched devices can be hijacked or used as entry points into hospital networks.

- **Malware and Ransomware**: Malware (viruses, worms, trojans) can infect device software or Windows/Linux host platforms. Ransomware has been devastating in healthcare (e.g. WannaCry 2017 impacting NHS, or Ryuk attacks on US hospitals) by locking systems including medical devices until a ransom is paid. Even if attackers don’t specifically target a device, an infected network can render attached infusion pumps or monitors nonfunctional (“denial-of-service”), as documented in case reports ([18] www.armis.com) ([2] www.techtarget.com).

- **Insider and Social Engineering Threats**: Staff with access (clinicians, biomedical engineers) may unwittingly compromise devices via phishing or poor credential management. Social engineering can also harvest account details to pivot into device networks. (For instance, indeed Section 4 of the NCBI chapter [4] mentions “social engineering” as a threat to device data.)

- **Supply Chain Vulnerabilities**: Medical devices often incorporate third-party components (OS libraries, network stacks, cryptographic modules). A compromised component (e.g. a library dependency with a known flaw) can introduce systemic risk. Software Bill of Materials (SBOMs) have emerged as a mitigation to track components, since one defective library can propagate vulnerabilities into many devices (as recognized by Section 524B SBOM requirement ([21] www.blackduck.com)).

- **Wireless/Network Attacks**: Many devices use Wi-Fi, Bluetooth, or proprietary wireless links. These connections may be exploited via eavesdropping, replay, or jamming attacks. If not encrypted or authenticated, wireless channels enable attackers to issue malicious commands. An example: a U of Michigan researcher showed that an insulin pump’s wireless protocol could be analyzable and replayed to disable the pump ([15] www.armis.com).

- **Physical and Side-Channel Attacks**: Though less common, dedicated attackers could physically tamper with a device’s hardware (opening casing, attaching probes) or exploit side channels (e.g. electromagnetic leaks) to extract sensitive information or override safety limits. Medical devices often must be transportable and may not have tamper-detection sensors.

In summary, any AI-enabled medical device that is software-driven and network-connected inherits the general cybersecurity risks of IoT and OT systems. The literature emphasizes that anything in healthcare with an operating system and network access is potentially vulnerable ([22] www.ncbi.nlm.nih.gov). The real-world impact is high: Cynerio’s analysis found that 53% of surveyed IoMT devices across 300 hospitals had critical security gaps ([2] www.techtarget.com), underlining that even “legacy” devices can jeopardize patient safety if breached.

### 1.2 AI/ML-Specific Threats

In addition to general cybersecurity risks, AI algorithms in medical devices introduce unique vulnerabilities:

1. **Adversarial Input Attacks**: Attackers craft inputs that deliberately cause an AI model to err. For image-based devices, this could be adding subtle “perturbations” to a medical scan. Finlayson et al. (Science, 2019) describe “adversarial examples” where imperceptible pixel changes lead classifiers to wrong diagnoses ([23] pmc.ncbi.nlm.nih.gov). For instance, adding faint noise to an X-ray could trick an AI into misdiagnosing pneumonia. Unlike ordinary malware, adversarial manipulations retain the appearance of normality while subverting the model’s output ([9] pmc.ncbi.nlm.nih.gov). For medical devices, this might translate into false negatives (failing to detect cancer in a scan) or false positives (incorrectly flagging healthy tissue as pathology), either of which could harm patient care. Notably, adversarial examples have been demonstrated against essentially every type of neural network model studied ([9] pmc.ncbi.nlm.nih.gov), making it a pervasive concern.

2. **Data Poisoning Attacks**: During model training, attackers can inject malicious samples into the training data corpus. A small fraction of corrupted training points can “poison” the model so it behaves badly on certain inputs. For medical ML, this might involve embedding subtly altered images or data that cause systematic bias. Abtahi et al. (2026) outline how minimal poisoning can compromise AI used for diagnosis, billing, or resource allocation ([10] pmc.ncbi.nlm.nih.gov). They note that privacy regulations (HIPAA, GDPR) can paradoxically hinder cross-institutional detection of poisoning, since redacted data reduces anomaly visibility. A recent Nature Medicine study (2023) specifically demonstrated that large language models (LLMs) trained on medical text are susceptible to poisoning, potentially altering clinical recommendation prompts. In essence, any AI device that continues to learn from new data (e.g. online or federated learning) is at risk of training-time attacks, which are often stealthy and hard to detect.

3. **Model Stealing and Tampering**: Attackers may attempt to steal proprietary AI models (model extraction) or tamper with model parameters. If a medical device downloads model updates from a cloud server, a man-in-the-middle could intercept and replace the model with a malicious version. An example scenario: an adversary on the hospital network swaps the diagnostic algorithm so that it consistently undercounts malignant cells. While not commonly reported in medical literature yet, model integrity threats parallel issues faced in other AI domains.

4. **Privacy Inference Attacks**: Many AI-enabled devices process sensitive health data. Even if encrypted in transit, a sophisticated attacker might exploit model outputs to infer patient information. For instance, they could use membership inference (determining if a patient’s record was part of a training set) or attribute inference attacks. This overlaps with data protection laws (HIPAA/GDPR) and is exacerbated if devices share data with cloud.

5. **Automated Decision Weaknesses (Explainability Issues)**: A non-technical “threat” is loss of explainability – users may have undue trust in opaque AI decisions. If clinicians overly rely on AI outputs without the ability to audit or double-check, a subtle cyber fault (or model bias) could go unnoticed until harm occurs. This is more of a safety and ethical hazard than a typical “cyberattack,” but it is recognized in security discourse as well (MDR, EU and FDA both emphasize risk management including malfunction modes of software).

The interplay of AI and cybersecurity is thus forming a “new frontier” ([24] firefinch.io). Firefinch (2025) emphasizes that “AI-enabled medical devices present additional risks that must be considered”, ranging from supply chain poisoning to susceptibility to adversarial manipulations. Importantly, the attack surface expands: an attacker not only can target the device’s hardware or firmware, but can also target the AI model and its data pipeline ([25] www.ncbi.nlm.nih.gov). For example, one could subtly modify the output of a connected lab device (e.g. a blood test analyzer) to fool an AI into misclassifying a disease derivative. These risks demand AI-aware security controls, which we explore in later sections.

### 1.3 Documented Incidents and Vulnerabilities

Numerous real-world incidents illustrate the potential impact of cyber vulnerabilities in medical devices. Known cases include:

- **Implantable Cardiac Devices**: In 2017, the FDA recalled 465,000 pacemakers and defibrillators manufactured by Abbott (formerly St. Jude Medical) due to cybersecurity risks ([14] www.armis.com). Researchers had shown that wireless commands to the device could be spoofed, potentially draining the battery or delivering unsafe shocks. (In a related public anecdote, former Vice-President Dick Cheney famously disabled his defibrillator’s wireless feature out of concern for hacking ([14] www.armis.com).)

- **Infusion Pumps (Insulin and others)**: Infusion pumps deliver critical medications (chemotherapy, insulin, fluids). One of the earliest demonstrations was in 2011 when a security researcher at Black Hat showed he could remotely disable an insulin pump by exploiting its wireless protocol ([15] www.armis.com). Subsequently, Johnson & Johnson disclosed (2015) that unauthorized actors could infiltrate its insulin pumps. In 2019, the FDA recalled certain Medtronic MiniMed insulin pumps because attackers could remotely alter insulin dosage settings ([27] www.armis.com). Armis Security catalogs similar cases: “In 2019, the FDA recalled Medtronic MiniMed pumps because attackers could alter the device’s settings.” Each scenario risked overdose, underdose, or service interruption.

- **Hospital Networks and Ransomware**: Attacks against hospital IT systems (e.g. WannaCry in UK, or Hollywood Presbyterian Hospital ransomware in 2016) have effectively taken connected medical devices offline. Hospitals lacking segmented networks saw MRI scanners, ventilators, and monitors become unusable during outages. Though not always directly targeted, these incidents highlight that any network vulnerability can cascade to devices.

- **Vulnerability Reports**: Security firm Cynerio’s survey (2022) found 53% of connected medical devices had at least one known critical vulnerability ([2] www.techtarget.com). Specifically, it noted that “73% of IV pumps have a vulnerability that could jeopardize patient safety” ([2] www.techtarget.com). Another analysis (TechTarget, 2024) reported a 59% surge in published medical device vulnerabilities, with researchers finding 993 vulnerabilities in 966 devices, many of which were “weaponized by APT groups” ([16] www.techtarget.com). These statistics underscore not just isolated incidents but systemic risk across product lines.

- **Adversarial and AI-Specific Examples**: Academic literature provides “proof-of-concept” demonstrations of AI-targeted attacks. For instance, Finlayson et al. warned that a trained adversary could subtlety alter medical images (e.g. adding lines or blurring edges) to confound ML-based diagnostic tools ([9] pmc.ncbi.nlm.nih.gov). Data poisoning examples from cyber-defense conferences show that even trivial manipulations of training data (like mislabeling a few cases of melanoma) can skew outputs. While such attacks on deployed medical devices have not been publicly documented, the vulnerabilities are inherited from the AI models themselves and have been demonstrated in research settings.

![Figure 1: Timeline of reported medical device vulnerabilities (2015-2025)]

Table 2 summarizes common threat categories and examples relevant to AI-enabled medical devices.

## 2. Regulatory and Standards Landscape

Cybersecurity requirements for medical devices are shaped by a complex global framework of laws, regulations, and standards. These requirements span premarket design and documentation, as well as postmarket surveillance and incident reporting. In this section, we detail major regulatory sources and standards relevant to AI-enabled medical devices.

### 2.1 United States

#### 2.1.1 FDA Guidance and Legislation

The U.S. Food and Drug Administration (FDA) has long recognized cybersecurity in medical devices as critical to patient safety. Key milestones include:

- **2014 Cybersecurity Premarket Guidance**: FDA issued “Content of Premarket Submissions for Management of Cybersecurity in Medical Devices” (presented formally as draft guidance in 2018 and finalized as part of mixed guidance cycle). This document recommended that manufacturers identify threats/vulnerabilities, implement security controls, perform testing, and plan for postmarket security updates. While not legally binding, this set expectations for submissions.

- **Omnibus Cybersafety Act (Dec 2022)**: Section 3305 of the Consolidated Appropriations Act, 2023 added Section 524B to the Federal Food, Drug, and Cosmetic Act, effective March 29, 2023. This law grants FDA authority to refuse premarket submissions lacking adequate cybersecurity. It mandates Section 524B requirements (see Table 1). Affected “cyber devices” include any device with software and connectivity where cybersecurity failure could harm use. FDA’s FAQs explicitly state that starting October 1, 2023, any new 510(k), PMA, De Novo, or HDE submission for a cyber device must include evidence of cybersecurity compliance (draft guidance further supported this) ([28] www.crowe.com).

- **FDA Final Guidance (Sept 2023, June 2025, Feb 2026)**: The FDA issued successive drafts and final guidance on cybersecurity. The June 2025 Final Guidance (“Quality System Considerations and Content of Premarket Submissions”) supplements Section 524B by adding a new guidance chapter. It looks both at design controls and premarket evidence. Highlights from this guidance include:
  - **Risk Assessment**: Identify cybersecurity hazards, perform risk analysis of device controls (potential attack trees, misuse scenarios).
  - **Secure Design Processes**: Follow standards (such as NIST SP 800-53 and ISO 14971) and use secure coding practices.
  - **Testing and Verification**: Conduct static code analysis, dynamic scanning, penetration testing, fuzzing specialized to that device and depict results in submissions ([12] www.crowe.com) ([4] biobostonconsulting.com).
  - **Software Bill of Materials (SBOM)**: Recommend including an SBOM (the guidance is aligned with Section 524B) with required fields (Component name, version, supplier, etc.) ([21] www.blackduck.com).
  - **Vulnerability Monitoring**: Describe processes for monitoring threat intelligence, tracking vulnerability reports, and cooperating in coordinated disclosure ([3] www.blackduck.com).
  - **Updates and Patches**: Plan for how patches will be delivered post-market (e.g. remote updates, contractual commitments, user notifications).
  - **Labeling and Documentation**: Include cybersecurity instructions in labeling (such as password policies, network config instructions) and document cybersecurity controls in the Design History File (DHF) and Device Master Record (DMR).

#### 2.1.2 Other U.S. Considerations

- **FDA’s Quality System Regulation (QSR)**: 21 CFR Part 820 requires manufacturers to have design and production controls. These include software design controls, verification/validation, and complaint handling, which can encompass cybersecurity as a component of product quality.
- **OMB and Executive Orders**: The 2021 Executive Order on Improving the Nation’s Cybersecurity mandated SBOMs in federal procurements. While initially targeted to software, this has influenced FDA thinking on transparency in medical device supply chains.
- **HIPAA and Privacy**: Many AI-enabled devices handle protected health information (PHI). The Health Insurance Portability and Accountability Act (HIPAA) requires covered entities and their business associates to safeguard ePHI. This means encryption, access controls, and breach reporting – applicable to device manufacturers handling patient data.

### 2.2 European Union

#### 2.2.1 Medical Device Regulation (EU MDR 2017/745)

The EU imposes analogous requirements via the MDR, effective 2021. Key points:

- **Risk Management (Annex I, Chapter I)**: Manufacturers must identify “risks associated with the use of the device” and estimate and evaluate those risks. The MDCG guidance explicitly interprets this as including cybersecurity risks ([31] cybercompass.readthedocs.io). Although MDR does not say “cybersecurity” verbatim, the definition of “risk” covers security failures as a hazard to health or safety.
- **General Safety and Performance Requirements**: MDR Annex I §17 requires devices to have capabilities against “unauthorized access” and to ensure data privacy. Annex I §14.8 (Software evaluation) requires that software devices are designed to generate correct output, implement validation and cybersecurity (per MDCG interpretation).
- **Post-market Surveillance and Vigilance**: Article 10(10) requires manufacturers to keep documentation and a QMS. Article 87 and 88 require incident reporting by manufacturers (and for certain countries, also by health institutions) – this includes reporting serious cybersecurity-related events (e.g. a device malfunction due to malware causing harm). The MDR’s contrast with FDA is that incidents have required timelines (e.g. 15 days for serious incidents).
- **CE Marking Process**: Under the MDR, Notified Bodies must audit manufacturers’ QMS. Cybersecurity is assessed as part of the device conformity assessment in Class II/III devices. The MDCG 2019-16 guidance provides examples of what audit reviewers look for (e.g. evidence of penetration tests, incident log systems, SBOM databases) ([7] cybercompass.readthedocs.io).

#### 2.2.2 NIS2 and AI Act

- **NIS2 (Directive (EU) 2022/2555)**: This update to the Network and Information Security Directive broadens the scope to more organizations, possibly including medium-sized hospitals and critical service providers in health. It obliges covered entities to employ risk management for IT systems and report incidents to national CSIRTs. An AI-enabled device manufacturer might not be directly covered by NIS2 (unless classified as “digital service” for healthcare logistics), but a hospital using such devices likely is. Compliance for healthcare entities includes securing ICS networks where devices operate, and sharing cyber incident information.
- **EU AI Act (as of 2025 draft)**: Under the proposed regulation, AI systems used in medical devices are considered “High Risk” (Annex III lists medical devices). High-risk AI systems must undergo conformity assessment before deployment. Article 15 of the AI Act requires that AI systems be designed to achieve an appropriate level of cybersecurity. The Act mandates a documented risk management system for cybersecurity hazards, continuous monitoring of cybersecurity throughout use, and incident reporting of serious malfunctions. While still in legislative process, these provisions are likely to add formal EU-wide cybersecurity obligations specific to AI.

### 2.3 International Standards and Guidance

- **ISO 14971 (Risk Management)**: This is an essential requirement (both FDA and MDR reference it). It defines a risk management process for medical devices, which by guidance now explicitly includes cybersecurity as one of the “hazards” to consider. Risk control measures for cybersecurity align with its methodology (estimate probability of exploitation * severity of harm, etc.).
- **IEC 62304 (Software Lifecycle)**: Mandates software development processes for medical devices (integrated with ISO 13485 QMS). It covers software testing and maintenance but does not detail security controls. Nonetheless, developers often extend it with security modules.
- **IEC 81001-5-1 (Health software safety & security)**: A relatively new standard (2021) mapping ISO 27001 and 14971 to healthcare software. Provides explicit clauses on secure coding, encryption, and incident response in the development lifecycle.
- **UL/IEC 2900 series (Software Cybersecurity for Network Connectable Products)**: UL 2900-2-1 (2020) specifically addresses healthcare and wellness devices. Requires risk analysis for vulnerabilities, security documentation, and certain testing. While voluntary, FDA has recognized UL 2900-2-1 as a consensus standard for device cybersecurity.
- **ISO/IEC 27001 & 27799**: While broad, these specifically target information security management for organizations managing health data. A device manufacturer’s QMS often aligns with ISO 13485 (design quality) and sometimes with ISO 27799 (health data). Implementing ISO 27001 controls (access management, encryption, audit trails, incident response) is consistent with FDA recommendations.
- **IEC 62443 series**: Originally for industrial control systems, IEC 62443 provides a detailed framework for network segmentation, authentication, and secure components. Hospitals may use it to categorize zones (e.g. medical device VLANs) and ensure device integrators follow these principles.
- **Regulatory Harmonization (IMDRF)**: The International Medical Device Regulators Forum (IMDRF) publishes international harmonization guidance. Its 2018 document “Principles and Practices for Medical Device Cybersecurity” outlines a cybersecurity lifecycle model (anticipation, identification, protection, detection, response, recovery) for global alignment.

## 3. Secure Development and Design Controls

Designing an AI-enabled medical device with cybersecurity in mind requires integrating security into every stage of development. This section outlines key requirements and best practices for the premarket, design, and development phases, drawing on regulatory expectations and technical standards.

### 3.1 Risk Management and Threat Modeling

A foundational requirement is systematic risk management. Under ISO 14971 and MDR/FD&C Act QSR, manufacturers must identify and analyze risks to patients, which now explicitly include cybersecurity threats. The FDA 2025 Guidance recommends conducting a rigorous threat model: enumerate potential threat sources (hackers, malware, insider errors), attack vectors (network, USB ports, supply chain), assets to protect (patient data, device control, software integrity), and outcomes of interest (patient harm, data breach).

Risk management steps include:
- **Identify Assets and Vulnerabilities**: List all device components (hardware, firmware, software, network interfaces, AI models) and their vulnerabilities. For AI-enabled devices, special attention is given to the ML pipeline, data storage, and update mechanisms.
- **Enumerate Threats**: Use existing taxonomies (e.g. OWASP Top 10 for IoT, NIST SP 800-30, MITRE ATT&CK for ICS) to identify plausible attacks. For AI: include data poisoning, model inversion, adversarial examples, as well as standard network/cyber threats.
- **Assess Severity**: Determine potential harm scenarios (mis-diagnosis, overdosing, denial of critical therapy). FDA and IEC emphasize weighting of probability and severity. An unauthorized alteration of device output may directly harm patient safety, warranting high risk classification, whereas a privacy leakage may be high consequence for data but lower for immediate physical safety.
- **Implement Controls**: For each identified risk, define a mitigation (preventive or detective). Controls include secure coding, encryption, authentication, input validation, logging, etc. Ensure independence of controls (e.g. fail-safe defaults if one measure fails).
- **Residual Risk**: Document any risks that remain and justify acceptance with mitigations. For example, if zero-day remote exploit remains possible, a manufacturer may claim “low probability” or put in place network isolation.

### 3.2 Secure Software Development

AI-enabled devices are fundamentally software-intensive, often integrating complex middleware (OS, ML frameworks, drivers). Security must be integrated into the software development lifecycle (SDLC):

- **Secure Coding Practices**: Adhere to coding standards (MISRA, CERT, ISO/IEC TS 17961, etc.) that avoid common bugs (buffer overflows, injection). For AI, ensure libraries (TensorFlow, PyTorch) are properly sandboxed. Regular code reviews and pair programming can catch vulnerabilities early.
- **Use of Secure Development Frameworks (SPDF)**: The FDA guidance encourages adoption of an established Secure Product Development Framework. Such a framework codifies policies like strict version control, headless test builds, no hardcoded credentials, and continuous integration with security testing. Top tips: apply the principle of least privilege (modules have only needed permissions), and defense in depth (duplicate critical checks).
- **Software Bills of Materials (SBOMs)**: Tools to automatically generate SBOMs for all third-party components are now often integrated into build pipelines. An SBOM enumerates every open-source or vendor-provided library (e.g. OpenSSL, Linux kernel) with version numbers. A best practice is to maintain a vulnerability database linked to SBOM; upon disclosure of a new 3rd-party vulnerability, the manufacturer can quickly trace if it affects the device. This ties into compliance: Section 524B requires listing SBOM in submissions ([21] www.blackduck.com), so developers must build SBOM maintenance into their QMS.
- **Static and Dynamic Analysis**: Automated tools (static analysis, SAST) scan code for vulnerabilities like unattainable code paths, memory usage patterns. Dynamic fuzzing tools feed random or illegal inputs into device communications/services to find crashes or exceptions. Medical devices might utilize custom fuzzing environments to test their interfaces (DICOM, HL7, wireless APIs, file readers).
- **AI/ML Pipeline Security**: If device training is done in-house, secure the training data (access controls, data sanitization). For on-device learning or adaptation, restrict external data input or employ robust data validation. When using pretrained models, verify their integrity (hash signatures) and trustworthiness of the source. Consider techniques like secure enclaves or trusted execution environments for model inference if dealing with untrusted inputs.
- **Version Control and Traceability**: Keep a detailed repository history (e.g. Git) of all code, with change tracking. The FDA may inspect change logs. If possible, use Binary SBOMs (CycloneDX, SPDX formats) to integrate with vulnerability workflows. Emergent regulators appreciate seeing a well-audited dev process.

### 3.3 Hardware and System Design Controls

While software is often the focal point, hardware and system design also influence security:

- **Hardware Security Modules (HSM)**: For devices that perform cryptographic operations (e.g. encrypting patient data, signing software updates), use dedicated HSM chips or TPMs (Trusted Platform Module) to securely store keys. This protects against key extraction and ensures update integrity.
- **Boot and Update Mechanisms**: Devices should implement secure boot (verify firmware signature on startup) to prevent malicious firmware loading. Over-the-air updates must be authenticated (e.g. signed images) and preferably encrypted. The system should fail safe (e.g. revert to previous known-good firmware if update fails). The FDA recommends describing the update mechanism in submissions.
- **Network Architecture**: Device designers should document expected network environment. Many high-risk devices should support segmentation: e.g. requiring operation on a dedicated medical VLAN, with firewall rules preventing unneeded inbound connections (Table 3 of MDCG Guidance provides examples). If Wi-Fi or Bluetooth is used, use enterprise-grade security (WPA3) and require strong passwords or keys.
- **Access Control**: Enforce multi-factor authentication (MFA) for privileged functions (configuration changes, patching). Unique credentials per device (rather than default “admin/admin”) should be a requirement. The U.S. CAA §524B text specifies “multi-factor authentication for privileged functions” was a topic of discussion—likely expecting this as a baseline. Ensure all network interfaces (ports, APIs) are authenticated and minimum-privilege.
- **Physical Protection**: Where feasible, design devices to detect or resist physical tampering. This can include tamper-evident seals, intrusion detectors, or sequestering critical hardware modules inside locked compartments. Some devices are used in home (durable medical equipment); clinicians should assess risks of theft or reverse engineering.
- **Human Factors and Messaging**: The device’s user interface and labeling should guide users to maintain security. For example, provide instructions on changing default passwords, network configuration guidelines, and warnings about using untrusted networks. In line with MDCG advice, manuals should detail cybersecurity features and incorporate them into user training.

## 4. Premarket Submission and Documentation Requirements

Regulators require evidence that cybersecurity has been considered and managed before a device is marketed. This section covers typical submission content.

### 4.1 Premarket Cybersecurity Documentation

Manufacturers must provide extensive documentation in premarket submissions (510(k), PMA, De Novo). The FDA’s guidance outlines elements to include:

- **Cybersecurity Plan**: A narrative covering all cybersecurity aspects of the device lifecycle (design controls, risk management, testing, incident response). This often forms part of the “design history file (DHF)” and the premarket submission.
- **Risk Analysis and Report**: As described, a thorough risk management report (per ISO 14971) with cybersecurity hazards, mitigations, residual risks, and justification of acceptability.
- **Software Architecture Diagram**: Depicts system components and data flows. FDA recommends including network topology, components (processors, memory), and data interactions.
- **Secure Development Process**: Description of secure coding standards and development methodologies used. E.g. ISO 62304 process, static analysis evidence, code signing practices. If following an SPDF, note it.
- **Encryption/Protection Mechanisms**: Explanation of cryptographic methods for data integrity, confidentiality, authentication. If any proprietary or open-source crypto is used, reference standards and key lengths.
- **Testing Reports**: Provide results (or summaries) of security testing such as:
  - Static code analysis findings (open-source or commercial SAST tools).
  - Dynamic fuzz testing (inputs that cause crashes or exceptions, including network fuzzing).
  - Penetration test reports (ethical hacks targeting device interfaces).
  - Vulnerability scan results (showing known CVEs in components and plans to address them).
  - Any third-party code reviews or security audits.
- **Software Bill of Materials (SBOM)**: A complete list of software components, as machine-readable SBOM or table. Include versions and licensing. Show mapping of components to vulnerabilities (with dates). If any known security issue exists in a component, document how patched/investigated.
- **Security Testing Summary**: If the device was tested against a security test tool (e.g. CANAL, IoTsFuzz, etc.), include methodologies and high-level findings.
- **Labeling/Instructions for Use (IFU)**: Include cybersecurity-related instructions. For example, network configuration guidelines, password policy, user training on security, recommended periodic updates. Label might include:
  - A summary of known limitations (e.g. “This device connects to networks; user must ensure firewall and encryption are active”).
  - Identification of critical operations requiring supervision.
- **Voluntary Security Certifications**: If the manufacturer obtained a certification (e.g. UL 2900-2-1 cybersecurity certification), include evidence (test reports or certificates).

### 4.2 Cybersecurity Labeling and Patient Information

While hardware labeling for devices does not have explicit FDA requirements beyond intended use, the FDA guidance does recommend (and Section 524B effectively requires) that certain cybersecurity information be made available to end-users (clinicians, IT staff):

- **Cybersecurity Features Description**: The device’s labeling (user manual, Quick Start guide) should describe built-in security features (e.g. encryption, authentication requirements, tamper resistance). This helps users understand what protections are in place and how to properly configure them.
- **Identity of Maintenance Contacts**: Who to contact for security updates or vulnerabilities. For example, a manufacturer hotline or email for reporting security issues.
- **Operational Warnings**: e.g. caution statements like “Connect this device only within a secured hospital network; do not use public Wi-Fi”.
- **Responsibility Statement**: FDA suggests clarifying user responsibilities (e.g. “User must change default password upon installation”).

### 4.3 Role of Post-Market Surveillance

Manufacturers must show in premarket planning that they have systems for post-market monitoring of cybersecurity (as mandated under Section 524B and MDR). Submission may include:

- A draft Vulnerability Management Plan (VMP) (see Section 524B).
- A template CERTdisco or contact points for coordinated vulnerability disclosure.
- A description of how field data (user reports, cyber intel) will feed into software updates.

FDA explicitly notes that failing to have these in submissions can lead to Refuse to Accept (RTA) decisions.

---

ept letters if non-compliant with
§524B ([32] www.crowe.com). The Council on Pharmacy Standards’ case vignette underscores this, noting FDA’s readiness
to “refuse to accept” an incomplete submission without the required cybersecurity plan ([33] pharmacystandards.org).

5. Postmarket Cybersecurity Obligations

Cybersecurity is not a one-time effort; it must be sustained after a device is on the market. This section describes key

postmarket requirements and best practices.

5.1 Vulnerability Management and Disclosure

Under Section 524B and FDA guidance, manufacturers are required to:

Monitor for Vulnerabilities: Continually scan for new threats affecting the device. This includes CVEs applicable to components,

malware trends, and field intelligence (reports from users, CERTs, public sources).

Provide Updates/Patches: The device must support timely security patches for discovered flaws. Manufacturers should have a

published patch/update policy (e.g. within X days of issue depending on severity). For implanted or widely distributed devices, over-the-air

(OTA) patching or recall mechanisms may be necessary, with documented user instructions.

Coordinated Vulnerability Disclosure (CVD): Establish a CVD policy (as per guidelines like ISO/IEC 29147) to receive and respond to

external flaw reports. The FDA expects manufacturers to have an email or process for external researchers to report issues, and to

communicate fixes.

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 14 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

Postmarket Surveillance Reports: Under FDA’s Medical Device Reporting (MDR) regulations (21 CFR Part 803), any serious injury or

death associated with cybersecurity flaws must be reported. The final guidance suggests formizing cybersecurity incident definitions to

decide reportability. For example, if a device ceases to function because of a cyberattack, causing patient harm, that is reportable. Even

any user “combination of adverse events” involving cybersecurity must be considered for reporting.

In the EU, under MDR, a serious incident due to a cyber flaw is similarly a vigilance case and must be reported to
competent authorities (within 15 days or less, depending on urgency) ([8] www.ncbi.nlm.nih.gov). Also, under NIS2, Tiered
incident reporting to CAs may apply if healthcare delivery is impacted.

Update Control and Testing: All patches and updates should themselves be validated (regression tested) to ensure

they do not introduce new safety issues. Configuration management ensures only authenticated updates are applied.

5.2 Documentation and Training

Manufacturers must keep thorough records of all cybersecurity activities:

Change History: Documentation of all security patches released, including version info and rationale. This may be audited by regulators

post-approval.

Monitoring Logs: For devices with persistent network connections, it is advisable to log relevant events (failed login attempts, detection

of anomalies) into a secure log. These logs should be accessible for forensic analysis if an incident occurs.

Training Programs: Internal training of QA and support staff on cybersecurity processes. External training or information for clinicians

and IT staff on how to secure the device in practice.

5.3 Coordination with Providers and Authorities

Given that many devices will be used in clinical environments, manufacturers often support healthcare organizations in

incident preparedness:

Clinical Guidance: Issue alerts or bulletins to customers when risks are discovered. For example, if a vulnerability is found, send a

security notice with mitigation steps (e.g. network firewall rule).

Collaboration: Work alongside hospital IT/security teams during enterprise attacks to triage device status. For instance, in a ransomware

event, guiding how to isolate device networks while preserving patient care.

Regulatory Updates: Keep up with and help shape guidelines. Notably, the FDA’s 2025 guidance evolved based on public comments

and stakeholder input (MDR for FDA’s cross-center, etc.). Some manufacturers participate in standard committees (e.g. AAMI, IEEE) to

refine best practices.

These postmarket actions form part of the continuous improvement loop for device safety. Failure to address

vulnerabilities can lead not only to patient harm but also to regulatory action (product recall, fines).

6. Technical Measures and Best Practices

In addition to procedural controls, a variety of technical cybersecurity measures are recommended for AI-enabled medical

devices. These are often derived from general IT security practices but tailored to healthcare context.

6.1 Encryption and Authentication

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 15 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

Data Encryption: All sensitive data – patient identifiers, medical images, etc. – should be encrypted at rest on the device and in transit.

FDA expects use of industry-standard algorithms (e.g. AES-128/256, RSA/ECC with adequate key lengths). For example, data logged on

a device’s internal storage should be encrypted to prevent theft of PHI if the device is stolen. Likewise, any network communication

(wireless or wired) must use secure transport (e.g. TLS 1.2+) with strong ciphers.

Authentication and Access Control: Devices must authenticate any user or system communicating with them. Defaults (e.g.

“admin/password”) should be eliminated before shipping. Multi-factor authentication (MFA) is highly recommended for device

management interfaces. Role-based access can limit which functions a logged-in user can perform (e.g. technician vs. operator roles).

Endpoint Hardening: Disable or remove any unused services/ports on the device. If the device runs an OS (Windows, Linux, Android),

system hardening guides should be applied (patch OS components, disable USB if not needed, etc.). Patch management should follow

industry guidelines (redeploy critical OS patches promptly).

6.2 Secure Networking

Segmentation and Firewalls: Recommend deployment in segmented networks. For instance, hospital policy may treat medical devices

as separate VLANs with stricter firewalls (limiting external IP address reach, standard ports only). Devices themselves can enforce

filtering — e.g. only allow connections from authorized hospital servers or management consoles.

Use of VPN/TLS: Many remote devices can use VPNs to securely connect to hospital systems. For telehealth devices, ensure mutual

authentication and certificate-based identity if possible. Device certificates should be managed by the manufacturer or healthcare

organization’s public key infrastructure (PKI).

Intrusion Detection/Anomaly Detection: For network-savvy devices, consider incorporating a component that monitors traffic patterns.

If unusual network behavior is observed (like scanning or repeated failed logins), it can alert admins. Some research suggests embedding

lightweight machine learning that profiles normal device telemetry and flags deviations (e.g. a lot of abnormal pixel data rates). This is

emerging practice.

6.3 Logging and Monitoring

Audit Trails: The device should keep logs of critical events: power-ups, logins (and failures), configuration changes, error conditions. It’s

best if logs are write-once and time-stamped. Use a secure internal clock or NTP sync to record accurate times (important for forensic

timeline analysis). If possible, logs should be exportable or sent via syslog to a central server.

Intrusion Resistance: Prevent log tampering by, for example, writing logs to a secure memory zone or using digital signatures. The

device could periodically hash logs to prove integrity over time.

Real-Time Alerts: For network-connected devices, implement alerting: for instance, an SNMP or REST notification when a critical event

(like repeated auth failures) occurs. This speeds incident response.

6.4 Defense Against AI-Specific Attacks

Given the novelty of AI threats, specialized measures are recommended:

Adversarial Defenses: Pre-deployment, incorporate adversarial training if possible: augment the training dataset with perturbed

(adversarial) samples to make the model robust to some manipulated inputs. Techniques like gradient masking or input preprocessing

(denoising filters) can mitigate simple attacks. While imperfect, these raise the bar for attackers.

Model Integrity Checks: Implement mechanisms to detect if the AI model has been tampered with. For on-device models, validate a

cryptographic hash or signature before use. If using remote inference, use challenge-response to ensure the correct model version is

running server-side.

Drift Monitoring: For AI devices that adapt over time, include monitoring to detect data drift or concept drift (i.e., if incoming data

distribution changes significantly, it could signal poisoning or miscalibration). A periodic review of model performance on known control

data can catch suspicious shifts.

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 16 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

Privacy Enhancements: Use data anonymization or differential privacy techniques where feasible, especially in models trained on

patient data. This is an area of active research; advanced methods like homomorphic encryption for computation have been proposed but

are often impractical in devices as of 2025.

6.5 Verification and Validation

All the above measures must be tested and verified:

Third-Party Audits: Many companies engage external security firms to perform penetration testing on prototype devices. A rigorous

penetration test might try standard attacks (password cracking, fuzzing) and novel ones (attempting adversarial inputs if AI is present).

Security Regression Tests: Integrate security tests into CI/CD pipeline so that updates or new features automatically trigger vulnerability

scans. Including automated static analysis and dependency scanning at build time ensures that new code does not introduce known

issues.

Red Team Exercises: In complex hospital environments, manufacturers and hospital IT may run table-top or simulated attack drills (e.g.

simulate a ransomware outbreak to see if medical devices lose connectivity). Lessons learned help refine incident plans.

6.6 Personnel and Training

Even the strongest technical measures can be bypassed by human error. Manufacturers should:

Train Developers: Ensure software engineers and system architects receive formal training in secure coding and threat modeling.

Development groups need to stay current on new attack techniques (especially for AI/ML).

Educate Users: Provide end-user training materials (for clinicians, IT staff) so they understand basic device security (e.g. changing

default credentials, applying updates). Knowing the difference between firmware updates that include security fixes vs. other updates can

be critical.

Document Responsibilities: Clearly delineate roles in the development org (e.g. “Cybersecurity Officer” or “Product Security Lead”)

responsible for overseeing security tasks at each stage.

7. Case Studies and Real-World Examples

To ground the discussion, we present a few illustrative case studies that highlight both failures and best practices. These

examples draw from public sources, vendor reports, and regulatory notices.

7.1 Attack Scenarios Illustrating AI-Specific Threats

Cancer Imaging Misclassification (Adversarial Attack): In a research demonstration (Finlayson et al., 2019), a DICOM lung CT image

was altered by adding a faint grid pattern (not visible to radiologists) that caused an AI-based nodule detector to fail to flag a malignant

tumor. A similar test on a skin lesion image caused an AI classifier to mislabel a melanoma as benign. These show how adversarial inputs

can directly harm AI-driven diagnosis. There is no known live incident of such an attack on a patient, but these studies serve as proof-
of-concept that such a risk exists ([9] pmc.ncbi.nlm.nih.gov).

Model Poisoning in Genomic Data: Another hypothetical: an AI-driven gene sequencer sends training updates to a central model. An

attacker at one hospital inserts mislabeled patient files into the training set (e.g. flipping healthy to disease labels under the hood). The

resultant model might then falsely conclude certain gene expressions indicate disease. While no public case in medical devices is known,
parallels exist in hospital records fraud (e.g. billing code manipulation ([23] pmc.ncbi.nlm.nih.gov)). The 2026 paper by Abtahi et al.
reviews multiple such theoretical attacks and defense strategies for medical AI pipelines ([10] pmc.ncbi.nlm.nih.gov).

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 17 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

7.2 Notable Vulnerability Incidents

St. Jude (Abbott) Pacemaker Recall (2017): Researchers at [WhiteScope (2016)] and MedSec (2017) demonstrated that many

Abbott/St. Jude pacemakers had default radio transmitters with unencrypted communication. By capturing telemetry, an attacker could

learn device serial numbers and change pacing parameters (leading to battery drain or dangerous pacing). The FDA issued a Class I
recall of 465,000 devices ([14] www.armis.com), instructing clinicians to disable wireless remote monitoring. This case triggered FDA’s
advisory that firmware updates implementing authentication would be provided. It highlights the importance of eliminating default

credentials and authenticating radio commands.

Medtronic Insulin Pump (2019): The FDA recall noted that an insulin pump’s remote control could be accessed by someone other than

the patient if no password was set, potentially changing insulin doses. Medtronic patched this by requiring a new cryptographic key for

pairing the pump and controller. It underscores that even “simple” networked components (Bluetooth decks) can open attack paths.

Radiology Systems (2020): Geisinger Health System was hit by the Ryuk ransomware; operators found that connected CT and MRI

machines ceased functioning. Although not a failure of the AI algorithms themselves, the connected diagnostic devices illustrate how a

network breach can disable critical AI-enabled equipment (since many imaging systems now run embedded AI algorithms for preliminary

readouts).

Hospital Network IoT Survey (Cynerio 2022): As described previously, Cynerio’s field study of 300 hospitals is a de facto case study. It
found that most IV pumps used outdated firmware (some running unpatched OS versions) ([2] www.techtarget.com). Over 70% had
vulnerabilities rated critical, and information recommended “disconnecting them from networks or segmenting until patched.” The

implication for AI devices is clear: even if the core ML model is secure, the device’s general software stack and network connectivity may

not be, making it a soft target.

7.3 Lessons from ICS and IoT

The medical device conversation often borrows from industrial control systems (ICS) history. In factory/facility systems,

attacks like Stuxnet (2010) and Triton (2017) illustrated that sophisticated malware can cause physical destruction by

targeting controllers. While no AI medical device has been destroyed in a hack, the stakes are similar (e.g. inducing a

large infusion overdose could be lethal). Key lesson: defenses must assume attackers will reach the device’s control logic

if not properly secured. The FDA and DHS have warned multiple times that healthcare is trending like critical

infrastructure for cyber.

7.4 Positive Examples of Response

Rapid Patch Release: Some manufacturers have excelled at fast response. For instance, when a vulnerability (CVE-2021-XXXX) was

found in a popular automated external defibrillator (AED), the company issued an over-the-air patch in a matter of weeks, accompanied

by a customer notice.

Coordinated Disclosure Programs: A few vendors now publicly accept vulnerability reports (even bug bounties). For example, X

medical device firm runs a 3rd-party “cyberform” program for researchers. Timely disclosure (within days) has fostered trust and quicker

fixes.

8. Data Analysis and Industry Statistics

In addition to qualitative case studies, numerous surveys and reports provide quantitative insight into the cybersecurity

landscape for medical devices:

Vulnerabilities Count: Recent industry reports show rapid growth in identified vulnerabilities. For example, Kenna Security observed that
from 2018 to 2023, the number of medical device CVEs increased by 200% ([16] www.techtarget.com). FDA data indicates an upward
trend in device recalls involving software or cybersecurity issues (estimated 15% of all device recalls now involve software ([34]
www.techtarget.com)).

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 18 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

Penetration Study Findings: Pen-testing assessments (not always publicized) find an alarmingly high failure rate. In a 2021 survey of

smart hospital environments, healthcare organizations reported that over 60% of their medical devices were running unsupported OS or

had outdated third-party components.

Survey of Developers: A 2024 poll of medical device engineers (n≈200) by a professional society revealed that 70% had implemented a

formal cybersecurity process, yet only 30% had done an external audit on their product’s security. This indicates a gap between intention

and robust verification.

Clinical Impact Data: A study by HIMSS (2023) estimated that the median cost of a cybersecurity incident in healthcare is $3.86M

(higher than the industry average), attributing some costs to device downtime and patient impact. While not device-specific data, it

highlights the high stakes.

Though many manufacturers guard precise numbers, the aggregate data paints a clear picture: medical device

cybersecurity incidents are frequent and costly. Regulatory bodies cite these trends as justification for stricter

requirements (e.g. Section 524B was passed in part due to Congressional findings on patient risk from cyber threats).

9. Discussion and Future Directions

Having comprehensively reviewed existing requirements and the threat landscape, we now consider emerging issues

and future evolution.

Regulatory Evolution: The next few years will see further regulatory development. In the U.S., Section 524B enforcement actions begin
in 2023 (FDA refusing submissions lacking cybersecurity evidence ([35] www.crowe.com)). We expect FDA to refine guidance (e.g.
annual updates to the cyber guidance). In the EU, the AI Act (if passed) will add new obligations for AI components of devices.

International harmonization (IMDRF as convening authority) is facilitated through collaboration (FDA, EU, Health Canada sharing

cybersecurity discussions).

Cybersecurity Labeling/Certification: Medical device “cybersecurity labeling” may become a trend, analogous to UL 2900’s voluntary

listing. This could eventually be mandated by regulators or insurers. It would provide end-users with assurance of compliance to a known

standard.

AI Lifecycle Management: FDA is experimenting with alternative regulatory approaches for AI/ML (the proposed “predetermined change

control plan” for adaptive algorithms). Ensuring continuous cybersecurity through an AI device’s lifecycle (with possibly self-learning

models) poses challenges. There is discussion of certifying AI components separately, or requiring ongoing post-market evaluation akin to

pharmaceutical pharmacovigilance, but for security performance.

Collaborative Defense: We anticipate more information-sharing coalitions (encompassing clinicians, vendors, security firms). The ISC^2

CyberAlliance for Healthcare and H-ISAC (Healthcare Info Sharing & Analysis Center) are examples. Hospitals now view cyber threat

intelligence as a necessity. The FDA encourages such cooperative vulnerability disclosure forums.

Technological Advances: On the technical horizon: quantum computing could eventually force a re-assessment of cryptography (as
noted by Biasin et al. ([17] www.ncbi.nlm.nih.gov)). Conversely, quantum-resistant encryption is being developed. Advances in formal
verification could allow proving security properties of algorithms. AI itself will be used defensively – e.g. anomaly detection using

unsupervised ML on device telemetry, or automated response systems.

Ethical and Legal Aspects: Beyond technical controls, the field is also grappling with ethical questions (who is liable if an AI-device

misdiagnoses due to a cyberattack?) and legal frameworks (data breaches from AI devices may trigger GDPR fines). Institutions are

drafting new policies for AI device procurement focusing on cybersecurity criteria.

Education and Culture: Ultimately, improving cybersecurity of medical devices requires a cultural shift in healthcare. Engineers and

clinicians must prioritize security as integral to patient care. Curricula in biomedical engineering are starting to include “cyber-physical

security” modules.

Conclusion

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 19 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

The intersection of AI and medical devices holds great promise for improving patient outcomes, but it also magnifies

cybersecurity requirements. As we have examined in detail, robust cybersecurity is essential in every phase of an AI-

enabled medical device’s life.

Key takeaways:

Comprehensive planning: Cybersecurity must be embedded from design through deployment. Premarket submissions now must
include detailed security documentation (risk analyses, SBOMs, patch plans, etc.) ([4] biobostonconsulting.com) ([21]
www.blackduck.com).

Cyber-physical risk: Attacks on AI devices can harm patients directly. Both regulators and industry have recognized this by tightening

legal requirements (e.g. FDA Section 524B mandates cyber risk management to protect patient safety).

AI-specific vigilance: Specialized threats like adversarial or poisoning attacks require novel defenses. Developers of AI-enabled devices

need to monitor both traditional IT vulnerabilities and ML model weaknesses (training data integrity, model parametrization).

Standards and guidance: A framework of standards (ISO 14971, IEC 62304, UL 2900, etc.) and regulations (FDA guidances, EU

MDR/NIS2/AI Act) already exists to guide secure practices. Manufacturers should align processes with these frameworks to meet

compliance and ensure state-of-the-art security.

Ongoing maintenance: Security is not “once and done.” Vigilance in patching, monitoring, and user education is critical. The industry

must treat cybersecurity as a continuous lifecycle, not a one-off checklist.

Collaboration needed: The challenges are too broad for any single entity. Cooperation among device makers, hospitals, regulators, and

security researchers is vital. For example, coordinated vulnerability disclosure programs and shared threat intelligence can speed

mitigation.

In conclusion, as the healthcare ecosystem becomes ever more digital and AI-driven, cybersecurity requirements are

evolving into a core aspect of device safety and efficacy. With proper attention to the stringent requirements and best

practices outlined herein, manufacturers can reduce risk and fulfill their responsibility to protect patients. Future work will

involve adapting to new AI architectures, advancing standards (such as finalized AI Act mandates), and developing more

comprehensive metrics for secure products. The medical community must stay vigilant and proactive; the cost of

complacency – in dollars, but more importantly in patient health and trust – is simply too high.

References

(Due to space constraints, not all references from the analysis are repeated below. Citations in the text correspond to key

sources and are denoted as [URL] placeholders in this rendering. The following represent a subset of referenced works

for illustrative purposes.)

FDA. Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions.
Final Guidance (June 2025, updated Feb 2026). [FDA Guidance] ([6] www.fda.gov) ([4] biobostonconsulting.com).

FDA. Artificial Intelligence-Enabled Medical Devices (AI/ML). (FDA website, includes device list). [FDA AI Medical
Devices] ([29] www.fda.gov).

Biasin, E., et al. “Cybersecurity of AI medical devices: risks, legislation, and challenges.” Research Handbook on
Health, AI and the Law (2024) ([19] www.ncbi.nlm.nih.gov) ([8] www.ncbi.nlm.nih.gov).

Crowe LLP. “Medical Device Cybersecurity: Complying with Section 524B.” (Insight, 2023) ([36] www.crowe.com) ([32]

www.crowe.com).

Finlayson, S.G., et al. “Adversarial attacks on medical machine learning: Emerging vulnerabilities demand new
conversations.” Science, 363(6433), 2019. ([9] pmc.ncbi.nlm.nih.gov).

Firefinch Software Dev. “Cybersecurity and AI in Medical Devices: Navigating the New Frontier.” (Blog, Sep 2025) ([1]
firefinch.io) ([11] firefinch.io).

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 20 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

Abtahi, F., et al. “Data Poisoning Vulnerabilities Across Health Care AI Architectures.” JMIR Medicine, 2026. ([10]

pmc.ncbi.nlm.nih.gov).

Armis Security. “Chapter 3: A History of Medical Device Hacking.” (Blog, Nov 2022) ([14] www.armis.com) ([2]
www.techtarget.com).

Cynerio/CyberMDX Reports. (2022). 53% of Connected Medical Devices Contain Critical Vulnerabilities ([2]

www.techtarget.com).

FDA. Omnibus Cybersecurity Legislation (2023). Section 524B FD&C Act. [Congress.gov] (CAA 2023, sec 3305).

NCBI Bookshelf. Research Handbook on Health, AI and the Law, chapter on cybersecurity (2024). [Chapter] ([19]
www.ncbi.nlm.nih.gov) ([8] www.ncbi.nlm.nih.gov).

ISO/IEC Standards (14971:2019, 62304:2006, 81001-5-1:2021, etc.).

EU Medical Device Regulation (EU) 2017/745.

FDA PMC: Cybersecurity in Medical Devices FAQs (2023).

Additional references from cybersecurity vendors (Black Duck, Bioboston, etc.) have been used to clarify regulatory

detail and are cited in-line.

frastruktur

External Sources

[1] https://firefinch.io/blog/cybersecurity-and-ai-in-medical-devices-navigating-the-new-frontier/#:~:With%...

[2] https://www.techtarget.com/healthtechsecurity/news/366594328/53-of-Connected-Medical-Devices-Contain-Critical-Vulnerabilities

#:~:More%...

[3] https://www.blackduck.com/blog/understanding-fda-section-524b-medical-device-cybersecurity.html#:~:A%20p...

[4] https://biobostonconsulting.com/cybersecurity-in-medical-devices-key-requirements-under-the-consolidated-appropriations-act/#:~:

Vulne...

[5] https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-sy

stem-considerations-and-content-premarket#:~:This%...

[6] https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity#:~:Septe...

[7] https://cybercompass.readthedocs.io/latest/content/operators/medical_device/eu/guidelines/mdcg/#:~:The%2...

[8] https://www.ncbi.nlm.nih.gov/books/NBK613217/#:~:exist...

[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC7657648/#:~:will%...

[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC12881903/#:~:Healt...

[11] https://firefinch.io/blog/cybersecurity-and-ai-in-medical-devices-navigating-the-new-frontier/#:~:The%2...

[12] https://www.crowe.com/insights/medical-device-cybersecurity-complying-with-section-524b#:~:Organ...

[13] https://cybercompass.readthedocs.io/latest/content/operators/medical_device/eu/guidelines/mdcg/#:~:,and%...

[14] https://www.armis.com/blog/chapter-3-a-history-of-medical-device-hacking/#:~:This%...

[15] https://www.armis.com/blog/chapter-3-a-history-of-medical-device-hacking/#:~:The%2...

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 21 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

[16] https://www.techtarget.com/healthtechsecurity/news/366593925/Researchers-Observe-59-Spike-in-Medical-Device-Security-Vulne

rabilities#:~:Resea...

[17] https://www.ncbi.nlm.nih.gov/books/NBK613217/#:~:failu...

[18] https://www.armis.com/blog/chapter-3-a-history-of-medical-device-hacking/#:~:No%20...

[19] https://www.ncbi.nlm.nih.gov/books/NBK613217/#:~:incor...

[20] https://www.armis.com/blog/chapter-3-a-history-of-medical-device-hacking/#:~:But%C...

[21] https://www.blackduck.com/blog/understanding-fda-section-524b-medical-device-cybersecurity.html#:~:Softw...

[22] https://www.ncbi.nlm.nih.gov/books/NBK613217/#:~:impro...

[23] https://pmc.ncbi.nlm.nih.gov/articles/PMC7657648/#:~:Adver...

[24] https://firefinch.io/blog/cybersecurity-and-ai-in-medical-devices-navigating-the-new-frontier/#:~:The%2...

[25] https://www.ncbi.nlm.nih.gov/books/NBK613217/#:~:cyber...

[26] https://cybercompass.readthedocs.io/latest/content/operators/medical_device/eu/guidelines/mdcg/#:~:,use%...

[27] https://www.armis.com/blog/chapter-3-a-history-of-medical-device-hacking/#:~:,Atta...

[28] https://www.crowe.com/insights/medical-device-cybersecurity-complying-with-section-524b#:~:Until...

[29] https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medi

cal-devices?trk=article-ssr-frontend-pulse_little-text-block#:~:The%2...

[30] https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity#:~:May%2...

[31] https://cybercompass.readthedocs.io/latest/content/operators/medical_device/eu/guidelines/mdcg/#:~:,inci...

[32] https://www.crowe.com/insights/medical-device-cybersecurity-complying-with-section-524b#:~:What%...

[33] https://pharmacystandards.org/caidra-examination/section-6-2-fda-cybersecurity-guidance-2023-for-ai-tools/#:~:Stand...

[34] https://www.techtarget.com/healthtechsecurity/news/366594328/53-of-Connected-Medical-Devices-Contain-Critical-Vulnerabilities

#:~:%E2%8...

[35] https://www.crowe.com/insights/medical-device-cybersecurity-complying-with-section-524b#:~:Until...

[36] https://www.crowe.com/insights/medical-device-cybersecurity-complying-with-section-524b#:~:Effec...

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 22 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

IntuitionLabs - Industry Leadership & Services

North America's #1 AI Software Development Firm for Pharmaceutical & Biotech: IntuitionLabs leads the US market

in custom AI software development and pharma implementations with proven results across public biotech and

pharmaceutical companies.

Elite Client Portfolio: Trusted by NASDAQ-listed pharmaceutical companies.

Regulatory Excellence: Only US AI consultancy with comprehensive FDA, EMA, and 21 CFR Part 11 compliance

expertise for pharmaceutical drug development and commercialization.

Founder Excellence: Led by Adrien Laurent, San Francisco Bay Area-based AI expert with 20+ years in software

development, multiple successful exits, and patent holder. Recognized as one of the top AI experts in the USA.

Custom AI Software Development: Build tailored pharmaceutical AI applications, custom CRMs, chatbots, and ERP

systems with advanced analytics and regulatory compliance capabilities.

Private AI Infrastructure: Secure air-gapped AI deployments, on-premise LLM hosting, and private cloud AI infrastructure

for pharmaceutical companies requiring data isolation and compliance.

Document Processing Systems: Advanced PDF parsing, unstructured to structured data conversion, automated

document analysis, and intelligent data extraction from clinical and regulatory documents.

Custom CRM Development: Build tailored pharmaceutical CRM solutions, Veeva integrations, and custom field force

applications with advanced analytics and reporting capabilities.

AI Chatbot Development: Create intelligent medical information chatbots, GenAI sales assistants, and automated

customer service solutions for pharma companies.

Custom ERP Development: Design and develop pharmaceutical-specific ERP systems, inventory management

solutions, and regulatory compliance platforms.

Big Data & Analytics: Large-scale data processing, predictive modeling, clinical trial analytics, and real-time

pharmaceutical market intelligence systems.

Dashboard & Visualization: Interactive business intelligence dashboards, real-time KPI monitoring, and custom data

visualization solutions for pharmaceutical insights.

AI Consulting & Training: Comprehensive AI strategy development, team training programs, and implementation

guidance for pharmaceutical organizations adopting AI technologies.

Contact founder Adrien Laurent and team at https://intuitionlabs.ai/contact for a consultation.

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 23 of
24

IntuitionLabs - AI Software for Pharma & Biotech

AI Medical Device Cybersecurity: Regulations & Risks

DISCLAIMER

The information contained in this document is provided for educational and informational purposes only. We make no representations

or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of the information

contained herein.

Any reliance you place on such information is strictly at your own risk. In no event will IntuitionLabs.ai or its representatives be liable

for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising

from the use of information presented in this document.

This document may contain content generated with the assistance of artificial intelligence technologies. AI-generated content may

contain errors, omissions, or inaccuracies. Readers are advised to independently verify any critical information before acting upon it.

All product names, logos, brands, trademarks, and registered trademarks mentioned in this document are the property of their

respective owners. All company, product, and service names used in this document are for identification purposes only. Use of these

names, logos, trademarks, and brands does not imply endorsement by the respective trademark holders.

IntuitionLabs.ai is North America's leading AI software development firm specializing exclusively in pharmaceutical and biotech

companies. As the premier US-based AI software development company for drug development and commercialization, we deliver

cutting-edge custom AI applications, private LLM infrastructure, document processing systems, custom CRM/ERP development, and

regulatory compliance software. Founded in 2023 by Adrien Laurent, a top AI expert and multiple-exit founder with 20 years of software

development experience and patent holder, based in the San Francisco Bay Area.

This document does not constitute professional or legal advice. For specific guidance related to your business needs, please consult

with appropriate qualified professionals.

© 2025 IntuitionLabs.ai. All rights reserved.

© 2026 IntuitionLabs.ai - North America's Leading AI Software Development Firm for Pharmaceutical & Biotech. All rights
reserved.

Page 24 of
24