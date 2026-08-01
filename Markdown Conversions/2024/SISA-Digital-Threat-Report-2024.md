# DIGITAL THREAT REPORT 2024
## For the Banking Financial Services and Insurance (BFSI) Sector

A COLLABORATIVE EFFORT OF SISA, CERT-IN & CSIRT-FIN.

## Table of Contents
- [Preface](#preface)
- [Introduction](#introduction)
- [Point of View](#point-of-view)
- [Highlights](#highlights)
- [Methodology & Sources](#methodology--sources)
- [Threat Landscape Overview](#threat-landscape-overview)
  - [Shift Towards Social Engineering and Credential Theft](#shift-towards-social-engineering-and-credential-theft)
  - [Impact of Artificial Intelligence on Cyber Threats](#impact-of-artificial-intelligence-on-cyber-threats)
  - [Increase in Supply Chain and Third-Party Attacks](#increase-in-supply-chain-and-third-party-attacks)
  - [Exploiting Weak Links: Security Lapses and Cloud Vulnerabilities](#exploiting-weak-links-security-lapses-and-cloud-vulnerabilities)
- [Inside the Breach: Key Cybersecurity Breaches and Attack Vectors](#inside-the-breach-key-cybersecurity-breaches-and-attack-vectors)
  - [Case 1: The Reward Heist: Exploiting System Vulnerabilities for Financial Fraud](#case-1-the-reward-heist-exploiting-system-vulnerabilities-for-financial-fraud)
  - [Case 2: The Silent Heist : Low-Volume Fraud Targeting Small Entities in BFSI Sector](#case-2-the-silent-heist--low-volume-fraud-targeting-small-entities-in-bfsi-sector)
  - [Case 3: The Silent Infiltration: Ransomware Through the Core Banking Supply Chain](#case-3-the-silent-infiltration-ransomware-through-the-core-banking-supply-chain)
  - [Case 4: The Wallet Exploit: Breaching Payment Systems Through Vulnerable Wallet Flows](#case-4-the-wallet-exploit-breaching-payment-systems-through-vulnerable-wallet-flows)
  - [Case 5: The Cashback Manipulation: Exploiting Payment Systems Through Transaction Interception](#case-5-the-cashback-manipulation-exploiting-payment-systems-through-transaction-interception)
  - [Case 6: The Webshell Breach - Exploiting XSS to Infiltrate Cloud Infrastructure](#case-6-the-webshell-breach---exploiting-xss-to-infiltrate-cloud-infrastructure)
  - [Case 7: The Insider Threat: Manipulating Dormant Accounts for Financial Gain](#case-7-the-insider-threat-manipulating-dormant-accounts-for-financial-gain)
- [Securing the Expanding IoT Frontier in BFSI: A Growing Imperative](#securing-the-expanding-iot-frontier-in-bfsi-a-growing-imperative)

---

## PREFACE

Finance sector not just in India but across the globe is undergoing rapid digital transformation and adopting new technology-driven solutions. Though, technology intervention helps streamline processes and customer service delivery, it also expands the security threat landscape, necessitating need for a robust and effective cyber security framework.

As the sector continues to adopt Fintech and digital solutions, cyberattacks are growing more sophisticated, frequent, and targeted. A cyberattack on a financial institution can have disastrous results. Cyberattacks in financial institutions can have systemic effects that are exacerbated by technological and financial ties between other financial and non-financial institutions, resulting in exponential losses.

Thus, efficient, and effective response to and rapid recovery from a cyber incident by financial organisations are essential to limit these financial stability risks. Further, considering the interconnectedness and interdependency of financial entities and the borderless nature of cyber incidents, the cyber risk of any given entity is no longer limited to the entity’s owned or controlled systems, networks, and assets. Further entities which were not the primary target or source of disruption may also be affected. Hence, it becomes much more important for authorities to coordinate at sector/national level.

CERT-In and CSIRT-Fin are playing a critical role by coordinating with various global & national financial organisations, regulators, national CERTs and other government agencies in rendering a timely and efficient cyber incident response to contain, reduce, or even eliminate cyber risk.

CERT-In and CSIRT-Fin have noticed a clear pattern in which cyberattacks in the financial industry are becoming more complicated and sophisticated. Malicious actors use sophisticated tactics, techniques and procedures to plan these attacks in order to get beyond traditional defenses. The cyber security landscape is changing in tandem with the spread of cutting-edge technologies like cloud computing, Application Programming Interfaces (APIs), and Artificial Intelligence/Machine Learning (AI/ML). Notable findings also show that some firms still struggle with basic cyber hygiene procedures and do not follow established security policies and procedures.

The report prepared by CERT-In, CSIRT-Fin and SISA offers an in-depth analysis of the evolving cyber threat landscape, focusing on the methods, tactics, techniques and procedures (TTPs) employed by threat actors targeting the BFSI sector. It provides a comprehensive overview of the methods malicious actors use to exploit vulnerabilities in BFSI organizations. The report outlines practical, actionable recommendations that organizations in the BFSI sector can implement across three pillars of the people, process, and technology. These include key security controls and mitigation strategies designed to fortify defenses and reduce vulnerabilities.

The report’s timely insights will help organizations to better safeguard their assets by taking proactive steps in enhancing their security postures and preparing for potential future breaches before they occur. The report also promotes sector-wide collaboration, allowing organizations to learn from each other’s experiences and improve resilience of individual organizations as well as strengthen the BFSI sector as a whole by facilitating team work through a collective response to emerging cyber threats.

**S. KRISHNAN, I.A.S.**  
Secretary,  
Ministry of Electronics & Information Technology, (MeitY),  
Government of India  

---

## INTRODUCTION

Welcome to the 2024 Digital Threat Report for the BFSI Sector. This report represents a convergence of insights from cybersecurity leaders, bringing together the strengths of frontline solution providers, national agencies, and expert responders. By pooling real-world data, early threat detection capabilities, and incident handling expertise, we have created a comprehensive view of the most critical risks facing the industry today. The collaborative nature of this report ensures that organizations gain visibility from multiple vantage points—providing a holistic understanding of adversary tactics, techniques, and procedures.

In an era where cyber threats evolve at an unprecedented pace, resilience is no longer optional—it is the foundation of organizational strength. This resilience emerges when compliance and security are viewed not as separate endeavors but as interconnected pillars of a unified strategy. When harmonized, they empower organizations to anticipate vulnerabilities, respond proactively, and build a formidable defense against emerging threats.

The 2024 Digital Threat Report for the BFSI Sector reflects this principle, combining intelligence from root cause analysis of cyber incidents conducted by CSIRT-Fin team, and forensic investigations conducted by SISA. It serves as a vital resource for navigating a landscape where security and compliance are not just essential but mutually reinforcing. It underscores the growing interdependence between regulatory frameworks and security practices. The insights offered are not merely reactive; they are forward-looking, designed to help organizations anticipate challenges and drive sustained readiness for the future.

The BFSI and digital payments industries lie at the heart of global digital transformation. Projected to generate $3.1 trillion by 2028—accounting for 35% of total banking revenue—this sector’s transition from cash to digital transactions introduces immense opportunities alongside heightened risks. As digital payments grow, they increasingly attract malicious actors who exploit system vulnerabilities, making this sector a prime focus for cyberattacks.

From threats targeting cloud identities and infrastructure to sophisticated attack patterns on digital applications, the report explores how adversaries adapt to evolving technological landscapes. It not only details these emerging threats but also offers practical strategies for emulating and mitigating these risks—empowering businesses to enhance detection and response capabilities.

Our mission is to bridge the gap between awareness and action, equipping organizations to refine their approach to threat detection, response, and long-term resilience. This report delivers intelligence designed to help security teams stay one step ahead, ensuring they are prepared not just for today’s challenges but for those that lie ahead.

Together, let’s transform challenges into opportunities, safeguarding the digital payments ecosystem to ensure it remains secure, resilient, and ready for the future.

**DHARSHAN SHANTHAMURTHY**  
Founder & CEO, SISA  

---

## POINT OF VIEW

Technology has been a driving force in shaping the securities market, enabling greater efficiency, accessibility, and affordability. However, with swift technological advancements, protection of IT infrastructure and data has become a key concern for the securities market regulator Securities and Exchange Board of India (SEBI) and its Regulated Entities (REs).

In order to strengthen the cybersecurity measures and to ensure adequate cyber resiliency against cybersecurity incidents/attacks in Indian securities market, SEBI has issued Cybersecurity and Cyber Resilience Framework (CSCRF). CSCRF is a standards based framework and broadly covers the five cyber resiliency goals, viz. Anticipate Withstand, Contain, Recover, and Evolve, which are adopted from CERT-In Cyber Crisis Management Plan (CCMP), for countering Cyber Attacks and Cyber Terrorism.

**AVNEESH PANDEY**  
Chief General Manager and CISO  
Securities and Exchange Board of India (SEBI)  

The digital payments landscape is evolving at an unprecedented pace. While these advancements improve accessibility and the efficiency of various payment platforms, they also require continuous vigilance.

As a key enabler of India’s digital payments infrastructure, the National Payments Corporation of India (NPCI) understands that cybersecurity and resilience are crucial to maintaining public trust and financial stability.

The key threats identified in the Global Threat Report 2024 for the BFSI Sector highlight the growing risks to payment networks, such as real-time fraud, API security gaps, and targeted attacks on financial infrastructures. With the increasing reliance on AI-driven transactions and embedded finance models, safeguarding the payments ecosystem from phishing, malware, and supply chain vulnerabilities is more critical than ever. Recent cyber incidents reinforce the need for multi-layered security strategies, real-time threat intelligence, and AI-enabled technologies to mitigate risks.

The Digital Threat Report 2024, developed by SISA in collaboration with CERT-In and CSIRT-Fin, provides critical insights into the evolving attack methods, reinforcing the urgency for market participants to adopt robust security measures, strengthen compliance protocols, and enhance threat detection capabilities.

In my opinion, the research findings mentioned in the report will augment the CSCRF framework towards the implementation of various solutions for cybersecurity and cyber resiliency, thus promoting digital trust, innovation, and sustainable growth.

This report, developed by SISA in collaboration with CERT-In and CSIRT-Fin, offers insights into the evolving threat landscape, stressing the urgency for payment networks, banks, and fintech players to adopt zero-trust architectures, strengthen compliance frameworks, and enhance cyber resilience and fraud detection capabilities.

I commend the collaborative effort behind this report and encourage all stakeholders across the digital payments industry to use these insights to strengthen security measures, build cyber resilience, and maintain consumer trust in our fast-growing digital economy.

**DILIP ASBE**  
Managing Director and CEO of the National Payments Corporation of India (NPCI)  

The Indian BFSI domain has witnessed rapid digital innovation. It is evolving into a tech-driven ecosystem where digital platforms, advanced analytics, and alternative distribution channels are shaping products and services. While technology is transforming the insurance sector at breakneck speed, regulators and industry players face several interlinked challenges.

Digitization has exposed entities in BFSI sector to cyberattacks, which can compromise sensitive personally identifiable information and disrupt core services.

The use of artificial intelligence to improve efficiency & reduce costs, the proliferation of APIs for delivering personalized services has brought heightened risks to information assets, making cybersecurity a critical focus area for organizations striving to protect their assets, reputation, and customers.

The report highlights some of the major attacks the BFSI sector is facing in the form of Data Exfiltration, Ransomware attacks exposing sensitive client data, Insecure API exploitation leading to unauthorized access, threat of Quantum Computing, third-party data breaches compromising personal information, Internal Threats etc. along with the recommendation for protecting and strengthening the cyber Security posture and resilience of organisations.

The report also highlights the growing interconnectedness of financial systems amplifying the impact of such breaches. Thereby, requiring effective and efficient responses to these incidents, along with rapid recovery mechanisms to mitigate damage and maintain trust.

By collaborating with global and national financial organizations and Regulators, CERT-In and CSIRT-Fin have been providing critical incident response coordination, threat intelligence sharing, and guidance on mitigating cyber risks to BFSI sector. Their efforts are enabling organizations to anticipate and address emerging threats more effectively, thereby improving the resilience of the BFSI sector.

As a Regulator for Insurance Industry, it is evolving IRDAI has taken various measures to ensure its Regulated Entities have put in place effective controls to protect their information assets in the face of evolving cyber security landscape. The measures include comprehensive guidelines on information and cybersecurity mandating establishment of robust cybersecurity frameworks including technical controls, annual comprehensive audit, incident response policy & plan including forensic, training and awareness and collaboration with industry and Cert-In. These measures aim to strengthen the cybersecurity posture of the insurance industry, ensuring resilience against evolving cyber threats while safeguarding sensitive customer data and maintaining trust.

As the financial sector continues its journey of rapid digital transformation, the importance of robust cybersecurity practices cannot be overstated. By leveraging the expertise of CERTs, implementing actionable recommendations across people, processes, and technology, and taking proactive steps to enhance security postures, organizations can effectively address the evolving cyber threat landscape. The commitment to continuous improvement and vigilance ensures that financial organizations remain resilient in the face of emerging challenges, safeguarding both their operations and their customers.

The report will certainly help the entities in BFSI sector to review their cyber security posture and ensure that their IT systems are resilient to the cyber vulnerabilities.

**A.R. NITHIYANANTHAM**  
Executive Director, IRDAI  

---

## HIGHLIGHTS

This report draws on the collective expertise and insights of industry leaders to provide a unified view of the cybersecurity landscape in 2024. It reflects a seamless exchange of knowledge, shaped by real-world cyber incidents, evolving adversarial tactics, and emerging threat intelligence.

By integrating a national perspective on cyber trends with frontline experience in mitigating sophisticated attacks, this report delivers a holistic understanding of the shifting threat environment. The result is a comprehensive resource that empowers organizations to anticipate risks, strengthen defenses, and navigate the complexities of today’s cybersecurity challenges.

Over the past year, cyberattacks have grown more sophisticated, driven by the intersection of new techniques and the persistence of proven methods. Social Engineering, in particular, has surged to the forefront, with Business Email Compromise (BEC) and advanced phishing campaigns operating with alarming precision. These attacks, often bolstered by data sourced from the dark web, bypass traditional defenses by leveraging stolen credentials and session cookies, effectively neutralizing multi-factor authentication. Meanwhile, supply chain breaches have escalated, exploiting the trust organizations place in third-party vendors and open-source repositories, thereby introducing vulnerabilities at scale.

Yet, the rising tide of cyber threats is not occurring in isolation. As digital ecosystems expand, so too does the recognition that compliance must evolve beyond rigid frameworks. This report explores how regulatory landscapes are shifting towards harmonization, with the goal of unifying disparate standards across regions. Compliance is transforming from a burdensome obligation into a strategic enabler—one that can unlock growth, improve operational efficiency, and reinforce resilience in sectors like digital payments, where sensitive data remains a prime target for attackers.

Beneath these strategic shifts lies a more pressing reality—critical control gaps continue to persist across industries. Weak access controls, over-privileged user accounts, and misconfigurations leave even the most fortified organizations exposed. This report highlights how these vulnerabilities are not merely by-products of oversight but structural weaknesses that adversaries consistently exploit to devastating effect. As the industry braces for what lies ahead, the future of cybersecurity is already being shaped by artificial intelligence (AI). The same technology that drives innovation is arming attackers with the tools to conduct highly personalized, evasive, and large-scale attacks. In 2025 and beyond, AI-driven threats will challenge existing defense mechanisms, forcing organizations to rethink their approach to threat detection and response.

This report offers concrete recommendations rooted in frontline audits and incident analysis, outlining the steps necessary to close control gaps, strengthen defenses, and build adaptive strategies against emerging threats. The findings presented here serve as both a reflection of the current landscape and a guidepost for navigating the uncertainties of tomorrow.

### Specifically, the report aims to:
- **Illuminate Adversaries’ Playbooks**: Offer insights into the methods, tactics, and procedures (TTPs) employed by threat actors, including how they exploit vulnerabilities, use AI to enhance their attacks, and target organizations through novel means.
- **Anticipate Future Attacks**: Predict potential future breaches based on current trends, dark web chatter, and the evolution of attack techniques, enabling organizations to proactively prepare for emerging threats.
- **Assess the Impact of AI in Breaches**: Explore how AI and machine learning are being utilized by attackers to develop sophisticated malware, automate attacks, create convincing deepfakes, and lower the barriers for cybercriminal activities.
- **Recommend Preventive and Detective Controls**: Provide actionable recommendations and key controls that organizations can implement across the pillars of people, process, and technology. These preventive and detective measures are designed to fortify defenses, mitigate risks, and enhance overall cybersecurity resilience against both current and emerging threats.
- **Highlight Current Trends and Select Cases**: Examine recent breaches, including those affecting organizations with robust security postures, to understand how and why these incidents occurred despite strong defenses.

### Methodology & Sources
The report is based on a synthesis of various sources, including:
- **Direct Observations from SISA’s DFIR Investigations**: Drawing on select cases and insights gained from digital forensics and incident response (DFIR) projects handled by SISA over the past year.
- **Observations of CSIRT-Fin, CERT-In**: Based on a comprehensive analysis of cyber incidents affecting the BFSI sector, with actionable recommendations for enhancing cyber maturity, data protection, backup strategies, and recovery measures.
- **Research and Analysis**: Leveraging research on AI’s impact on cybersecurity, including adversarial machine learning, deepfake technology, and malicious use of large language models.
- **Cybersecurity Reports and Data Pointers**: Incorporating findings from vulnerability databases, and observed trends in malware and exploit usage.

---

## THREAT LANDSCAPE OVERVIEW

Cyber threats are no longer a distant concern—they are an immediate and inescapable reality, particularly for the BFSI industry. In 2024, the sector witnessed a surge in the sophistication, scale, and diversity of cyberattacks, highlighting a rapidly evolving threat landscape. With the average cost of a data breach reaching an all-time high of $4.88 million globally[^1]—a 10% increase from 2023—and $2.18 million in India[^2], the financial stakes have never been higher.

The BFSI sector ecosystem faces unique challenges due to its interconnected infrastructure and the high-value financial data it safeguards. This convergence of high rewards and expanding technological complexity has made the sector a prime target for attacks by cyber malicious actors. Phishing and compromised credentials are some of the key forms of cyber-attacks in India.

For the financial sector in India, H1 2024 alone saw a 175%[^3] surge in phishing attacks compared to the same period last year, underscoring the heightened activity within an increasingly volatile threat landscape. Cloud exploits emerged as a critical entry point, exposing gaps in complex infrastructures and amplifying the financial and operational impacts of breaches. Meanwhile, supply chain attacks have evolved to exploit interconnectivity, breaching even the most fortified systems with persistent and adaptive tactics.

As attackers increasingly leverage artificial intelligence (AI), identity-based attacks have grown more sophisticated and pervasive. AI’s ability to exploit identity vulnerabilities and bypass defenses using social engineering techniques signals a troubling evolution in cyber tactics. Deepfake technology, for instance, is enabling large-scale impersonation scams, including executive-level Business Email Compromise (BEC) attacks and misinformation campaigns. With India experiencing a higher than average rise in deepfake identity fraud[^8], organizations face unprecedented challenges in preserving digital trust.

> The average time from vulnerability disclosure to exploitation has decreased dramatically, with some vulnerabilities being exploited within hours of public disclosure.

By 2025 we expect AI-driven cyber attacks to become one of the most scalable and adaptable threats, challenging traditional defenses and requiring innovative countermeasures.

In the sections that follow, this report will trace the details of these challenges, vulnerabilities, and emerging trends. Understanding these intricacies is critical to formulating a defense strategy and mitigating the evolving risks to the digital payments ecosystem.

---

### Shift Towards Social Engineering and Credential Theft

Social engineering remains one of the most pervasive attack methods in 2024.

#### Business Email Compromise (BEC)
A notable trend has been the rise of social engineering, with Business Email Compromise (BEC) and sophisticated phishing campaigns dominating the threat landscape. Attackers are increasingly turning to AI-powered tools to mine social media, scrape employee data, and craft highly personalized lures that bypass traditional security filters. Pretexting, the art of creating false scenarios, plays a central role in these attacks, deceiving employees into transferring funds, sharing credentials, or altering account information under the guise of legitimate requests. The growing accessibility of “deepfake as a service” platforms further amplify the effectiveness of these schemes, allowing adversaries to convincingly impersonate executives and bypass manual verification processes. 
*(54% of the Business Email Compromise case investigated had instances of pretexting[^4].)*

#### Phishing Attacks
Stolen credentials and information stealing malware remain among the most effective tactics for attackers to breach organizational networks. Malicious actors acquire credentials through phishing, information stealing malware, or dark web purchases, targeting usernames, passwords, and session cookies that bypass multi-factor authentication (MFA). These credentials grant access to critical systems like single sign-on platforms, virtual private networks (VPNs), email accounts, and software as a service (SaaS) applications. Many SaaS platforms include client-specific information in URLs, compounding the risk by exposing sensitive data when combined with compromised credentials. 
*(Phishing attacks, accounting for 25% of initial infection vectors, deceive individuals into revealing sensitive information by impersonating trusted entities[^5].)*

---

### Impact of Artificial Intelligence on Cyber Threats

Phishing attacks have become increasingly sophisticated with attackers employing advanced social engineering tactics, often enhanced by artificial intelligence (AI), to create highly convincing phishing emails and messages that are difficult to distinguish from legitimate communications. AI’s accessibility has democratized cyber attacks, enabling even smaller groups to launch impactful attacks.

The use of AI-generated content to craft phishing lures that are free of grammatical errors and awkward phrasing, which traditionally served as warning signs of malicious intent.

These AI-enhanced phishing attempts can mimic the tone, style, and branding of trusted entities with remarkable accuracy, making them more persuasive and harder to detect.

Further, generative AI models can produce personalized content that exploits specific information about targets, increasing the likelihood of deceiving recipients into revealing sensitive information or clicking on malicious links.

The emergence of malicious Large Language Models (LLMs), such as WormGPT and FraudGPT, has lowered the barrier to entry for sophisticated cyber attacks, enabling less skilled actors to craft convincing phishing emails, generate malware, and exploit vulnerabilities.

The advent of chatbot phishing scams represents a new frontier in phishing techniques. Attackers use AI-powered chatbots with NLP capabilities to engage potential victims in seemingly benign conversations, subtly extracting personal information or login credentials over time. This method leverages the interactive nature of chatbots and can be particularly effective as users may be less guarded during real-time exchanges.

Deepfake-enhanced social engineering attacks are on the rise, with attackers using convincing AI-generated audio and video to impersonate trusted individuals. These advanced impersonations trick users into revealing MFA codes or approving unauthorized authentication requests.

#### Key Tactics Observed
- **Diversification of File Formats**: Attackers are also diversifying the file formats used in phishing campaigns to evade email security filters. Common tactics include sending malicious attachments in archive formats like ZIP and RAR files, which conceal harmful content from scanners, especially when password-protected. Additionally, there is increased use of HTML-based files such as Compiled HTML Help (CHM) and LNK (shortcut) files, which are often overlooked by security software due to their legitimate uses.
- **Abuse of Legitimate Internet Services (LIS)**: Attackers exploit services like GitHub Pages, cloud storage platforms, and messaging applications such as Discord and Telegram to lend credibility to their phishing campaigns and to bypass traditional security defenses that trust these well-known platforms.

---

### Increase in Supply Chain and Third-Party Attacks

Supply chain vulnerabilities remained a prominent attack vector for the digital payments industry in 2024. By infiltrating third-party vendors or manipulating widely used software, attackers achieved large-scale breaches. These attacks leveraged trusted relationships to bypass direct defenses, making detection and response increasingly difficult.

In these attacks, the threat actors compromise a product development entity—such as a software vendor or a third-party library provider—to inject malicious code into legitimate applications. This compromised code could be delivered to clients via regular software updates or new releases, allowing attackers to potentially infiltrate multiple organizations without direct targeting.

One prevalent technique is exploiting access to code repositories. Attackers inject obfuscated malicious code into the source code of widely used applications by gaining unauthorized access to developer accounts. This malware can evade detection during automated and manual reviews due to advanced obfuscation techniques.

Another tactic involves publishing malicious libraries disguised as legitimate ones on platforms like GitHub or PyPI. These libraries, promoted to gain developer trust, are unknowingly integrated into projects, introducing vulnerabilities or backdoors.

#### Key Tactics Observed
- **Third-Party Exploits**: The MOVEit and GoAnywhere breaches highlighted the risks posed by compromised managed file transfer services. Threat Actor Groups like CL0P launched attacks on managed file transfer (MFT) services, including Fortra’s GoAnywhere and Progress Software’s MOVEit, impacting thousands of organizations and exposing sensitive data.
- **Open-Source Risks**: Threat actors exploited vulnerabilities in open-source libraries and components, often targeting Linux environments. For instance, the XZ Utils data compression library was compromised, introducing a backdoor that could have allowed unauthorized access to systems using the library. This incident prompted major Linux distributions to revert to previous, uncompromised versions to mitigate potential risks.

---

### Exploiting Weak Links: Security Lapses and Cloud Vulnerabilities

Organizations with inadequate cloud configurations or insufficient security controls are becoming prime targets for cyberattacks. Common vulnerabilities include poor access controls, lack of multi-factor authentication (MFA), delayed security patches, and mismanagement of privileged accounts.

Cloud misconfigurations—such as publicly accessible storage buckets or default credentials—have led to unauthorized access and massive data exposures. The shift to remote work and the rapid adoption of cloud services have further widened the attack surface, with many organizations failing to recalibrate their security postures to match the speed of digital transformation.

A significant surge has been observed in attackers exploiting vulnerabilities as a primary method to gain initial access into organizational networks. By targeting both known and zero-day vulnerabilities in widely deployed systems and applications, attackers can bypass traditional defenses. These vulnerabilities often affect internet-facing services and can be discovered through public scanning, making them attractive for mass exploitation.

> Attackers exploit flaws within hours of vulnerability’s disclosure, with the average time to exploitation now just eight days. This leaves organizations struggling to patch in time.

Recent research highlights a 180% increase in exploits leveraging vulnerabilities to infiltrate networks, emphasizing the growing reliance on this tactic[^6]. Internet-exposed systems, unpatched software, and misconfigured services present low-hanging fruit for attackers seeking entry points.

However, even organizations with strong security frameworks are not immune. Despite mature security practices, breaches continue to occur, often exploiting subtle vulnerabilities and human error. Sophisticated attackers bypass advanced defenses through social engineering, manipulating trusted insiders to gain unauthorized access.

In a few incidents outside India, it has been observed that super users have been approached with cryptocurrency-based tactics, persuading them to modify security settings, leading to unauthorized access to critical environments.

Application Program Interfaces (APIs) also become a key attack vector. Weaknesses in API authentication—such as hardcoded API keys, credential reuse across environments, and predictable patterns—are frequently exploited by threat actors. Attackers leverage these gaps to breach systems, often with devastating results.

Furthermore, MFA, once considered a cornerstone of modern security, is increasingly under fire. Attackers bypass MFA through mechanisms such as session hijacking, brute-force attacks on push notifications, and advanced social engineering techniques, including the use of deepfake technology to impersonate trusted individuals. The OTP Bypass via BOLA (Broken Object Level Authentication) is another critical vulnerability which enables malicious actors to bypass authorization mechanisms, granting them unauthorized access to sensitive data or allowing the execution of unauthorized actions.

---

## INSIDE THE BREACH: KEY CYBERSECURITY BREACHES AND ATTACK VECTORS

The evolving cyber threat landscape highlights that no single point of defense is sufficient to protect the intricate and interconnected systems underpinning modern financial services. As adversaries adapt and exploit weak links across digital payments, cloud environments, third-party integrations, and internal processes, BFSI entities must move beyond isolated security measures to adopt a system-level approach to cybersecurity.

Cyberattacks are no longer confined to external breaches or malware infections; they now infiltrate the entire BFSI value chain—from core financial application platforms and payment gateways to cloud infrastructure and customer-facing applications. Supply chain attacks, identity theft, and phishing campaigns are not standalone threats but interwoven tactics that target vulnerabilities across multiple layers of financial services operations. Zero-day vulnerabilities, API exploitation, and social engineering persist as recurring attack vectors, often bypassing traditional security postures by exploiting human error, misconfigurations, or third-party software dependencies.

Recent incidents reveal that no operational domain is immune. BFSI entities have faced ransomware encrypting their systems, low-value unauthorized transactions slipping past payment processing systems, and AI-powered BEC scams exploiting communication channels. Attackers leverage API weaknesses to breach mobile wallets, exploit cloud misconfigurations to access sensitive customer data, and manipulate dormant accounts internally to siphon funds undetected.

To address these challenges, a structured and segmented approach for attack vectors has been adopted to understand the threat actors’ tactics. This approach is outlined through eight use cases, each reflecting a unique attack scenario targeting a distinct operational segment of BFSI infrastructure. These cases provide a comprehensive, system-level view of vulnerabilities exploited, attack methods, audit findings and proposed mitigation strategies, illustrating how attackers move fluidly between domains to maximize impact.

### Structured and Segmented Approach for Attack Vectors across the BFSI Operations

| Core Banking Systems | Payment Processing Systems | Digital Financial Services Apps |
| :--- | :--- | :--- |
| **Ransomware & Data Encryption**<br>Disruption of core banking operations by encrypting databases. | **API Exploitation**<br>Weakness in wallet APIs allows unauthorized payments. | **App Vulnerabilities**<br>Exploiting mobile app vulnerabilities (XSS, SQL injection) to compromise accounts. |
| **Insider Fraud**<br>Unauthorized manipulation of dormant accounts and transaction records. | **MITM (Man-in-the-Middle) Attacks**<br>Transaction data is altered during processing. | **Credential Theft**<br>Phishing and AI-powered scams to steal user login information. |
| **Supply Chain Attacks**<br>Malicious code injected via third-party core banking software providers. | | **Session Hijacking**<br>Attackers bypass MFA by hijacking active sessions. |

| Cloud & Infra Management | Vendor & Partner Integration Systems | IoT & Connected Device Security |
| :--- | :--- | :--- |
| **Cloud Misconfigurations**<br>Public exposure of cloud storage and weak IAM settings. | **Supply Chain Attacks**<br>Injecting malicious code into third-party banking software. | **Hardware Vulnerabilities**<br>Fault injection techniques bypassed security on a Trezor hardware wallet, unlocking $2 million in cryptocurrency. |
| **Privilege Escalation**<br>Gaining admin rights through API vulnerabilities. | **Third-Party Breaches**<br>Compromising vendor systems to gain access to bank networks. | |
| **Cross-Site Scripting (XSS)**<br>Exploiting web applications hosted in the cloud. | | |

---

### CASE 1: THE REWARD HEIST: EXPLOITING SYSTEM VULNERABILITIES FOR FINANCIAL FRAUD

This case (outside India) is of a multi-stage cyberattack targeting a reward points system, exploiting server vulnerabilities, and leveraging weaknesses in API for financial fraud.

Attackers breached a Linux web server, exploiting vulnerabilities to deploy malware and secure remote access for themselves. After gaining initial access, the attackers moved laterally within the system by exploiting hardcoded database credentials to access sensitive information. This oversight in database security provided the attackers unrestricted access, allowing them to manipulate critical data.

Attackers targeted the reward points system, inflating the value of 250 points from $50 to $50,000. They updated only specific wallets with these manipulated points, eventually making them universally accessible for redemption and monetization, thus enabling widespread exploitation.

Attackers were able to deceive the system by crediting manipulated reward points to users’ mobile wallets. This credit served as a stepping stone for the next phase of the attack which was to transfer funds from mobile wallets to bank accounts. Using a replay attack methodology, they replicated genuine bank transfer requests from physical transactions branches, mimicking API calls with identical request identities to bypass security checks and execute unauthorized transfers.

The attackers’ ultimate objective—to inflate reward points, credit unauthorized amounts to wallets, and transfer funds to external accounts—was successfully achieved.

> This case underscores significant vulnerabilities, such as the use of hardcoded database credentials, the lack of validation in the reward points system, and the absence of mechanisms to detect replay attacks. It also highlights the importance of robust vulnerability management, secure transaction workflows, and continuous monitoring to prevent such exploitation.

#### Top 5 Mitigation Steps
1. **Multi-Factor Authentication (MFA)**: Enable MFA for VPNs, webmail, and accounts accessing critical systems.
2. **Network Segmentation**: Segment and segregate networks into security zones, separating administrative networks from business processes using physical controls and virtual local area networks (VLANs).
3. **Application Whitelisting**: Enforce whitelisting on endpoints to block unauthorized software execution.
4. **Log Monitoring and Retention**: Audit and monitor logs to detect unusual patterns or behaviors in events and incidents. Redesign log retention policies to store logs for at least 180 days to ensure availability for incident investigations.
5. **Regular Updates and Virtual Patching**: Ensure all operating systems and applications are updated regularly. Use virtual patching to protect legacy systems and networks.

---

### CASE 2: THE SILENT HEIST : LOW-VOLUME FRAUD TARGETING SMALL ENTITIES IN BFSI SECTOR

CSIRT-Fin/CERT-In has been watchful and has proactively taken measures and thwarted cyber-attacks which could have caused damage in the BFSI sector. 

But for the timely intervention and preventive measures, any lapses would have resulted in financial and reputational risk for the sector.

Small entities in the BFSI sector must take proactive steps to secure their information system infrastructure against cyber-attacks.

The attackers aimed to bypass security checks and exploit gaps in the information infrastructure of these small entities. Key protective measures include enforcing Multi-Factor Authentication (MFA), segmenting networks into secure zones, implementing application whitelisting, using virtual patching for legacy systems, and deploying robust web and email filters with antivirus scanning at both host and gateway levels.

#### Top 5 Mitigation Strategies
1. **Multi-Factor Authentication (MFA)**: Enforce MFA for accessing critical systems.
2. **Network Segmentation**: Segment and segregate networks into security zones to protect sensitive information and services.
3. **Application Whitelisting**: Enforce whitelisting on endpoints to prevent unauthorized software execution.
4. **Virtual Patching**: Use virtual patching to safeguard legacy systems and networks.
5. **Deploy Filters**: Implement web and email filters to block known malicious domains, sources, and addresses. Scan all emails, attachments, and downloads with a reputable antivirus solution at both host and gateway levels.

---

### CASE 3: THE SILENT INFILTRATION: RANSOMWARE THROUGH THE CORE BANKING SUPPLY CHAIN

A third-party service provider in the BFSI sector was impacted by a cyber attack.

The attacker, a member of the notorious RansomEXX ransomware group, gained access through vulnerabilities in the provider’s infrastructure, slipping past defenses undetected.

Once inside, the attacker deleted critical database backups and deployed a custom ransomware variant called ‘cryptor’, encrypting critical files. The ransom note left behind was more than just a demand—it was a threat of double extortion, warning that sensitive client data would be leaked if the ransom wasn’t paid. (Double extortion – (1) demand for ransom, (2) leaking client data)

The compromised entity suffered reputational damage, operational disruption, and an increased risk of customer churn.

> This wasn’t a direct assault on the BFSI entity—but rather an exploitation of the supply chain that underpinned the entity’s core services.

#### Top 5 Mitigation Strategies
1. **Multi-Factor Authentication (MFA)**: Enable MFA for VPNs, webmail, and accounts accessing critical systems.
2. **Regular Updates**: Ensure all operating systems and applications are updated regularly. Use virtual patching to protect legacy systems and networks.
3. **Data Protection**: Enforce data protection, backup, and recovery measures. Encrypt data at rest to safeguard against breaches and exfiltration.
4. **Advanced Security Systems**: Deploy intrusion detection & prevention systems, network detection and response system, extended detection and response system, network behaviour and anomaly detection system, and firewalls as appropriate for enhanced threat detection and prevention.
5. **Network Segmentation**: Implement network segmentation into security zones. Separate administrative networks from business processes using physical controls and VLANs.

---

### CASE 4: THE WALLET EXPLOIT: BREACHING PAYMENT SYSTEMS THROUGH VULNERABLE WALLET FLOWS

In a carefully orchestrated attack on a payment service entity, the threat actors exploited a vulnerability in the wallet flow of the payment service entity, targeting the integration between the payment service provider and merchants, to carry out multiple unauthorized transactions.

By leveraging this exploit, the attackers seamlessly placed orders through third-party applications, exploiting the direct link between the payment service provider and external merchants. The loophole created a perfect storm—transactions appeared valid on the merchant’s side while leaving the actual wallet balances untouched.

The payment service provider faced financial losses. Subsequently this vulnerability has been fixed.

#### Top 5 Mitigation Strategies
1. **Confidentiality**: Restrict access to API documentation, including Postman collections, ensuring it is accessible only to authorized personnel.
2. **Strong Authentication**: Use robust mechanisms like API keys, OAuth, or JSON web token (JWT) with secure token management practices, appropriate expiration times, and granular access control based on user roles and permissions.
3. **Multi-Factor Authentication (MFA)**: Enable multi-factor authentication of users particularly for accounts that access critical systems.
4. **Secure Storage**: Encrypt and secure API keys, credentials, and sensitive data with access controls.
5. **Cross-Origin Resource Sharing (CORS) Configuration**: Properly configure CORS to restrict API access to specific domains, preventing unauthorized cross-origin requests.

---

### CASE 5: THE CASHBACK MANIPULATION: EXPLOITING PAYMENT SYSTEMS THROUGH TRANSACTION INTERCEPTION

A digital payments and financial services company fell victim to a sophisticated man-in-the-middle (MITM) attack that exploited the intricacies of an instant cashback promotion tied to EMI purchases on an e-commerce platform.

By intercepting and altering transaction details midstream, the attacker systematically inflated cashback values, bypassing essential verification steps. This allowed the perpetrator to successfully claim unauthorized cashback rewards.

The lack of real-time validation or API integrity checks facilitated the attack’s longevity, resulting in unauthorized cashback claims.

This breach not only inflicted direct financial losses but also exposed systemic vulnerabilities in the payment service entity’s API security and transaction validation mechanisms.

#### Top 5 Mitigation Strategies
1. **API Security**: Secure APIs used between the merchant’s website, payment aggregator, payment gateway, and acquirer with strong authentication, encryption, and access controls.
2. **Server-to-Server Validation**: Use server-to-server validation techniques instead of browser redirection or callbacks for enhanced security.
3. **Hash Sensitive Details**: Include sensitive payment details like card numbers, transaction amounts, and statuses in the hash or checksum transmitted with transaction data.
4. **Real-Time Monitoring**: Implement monitoring and anomaly detection systems to identify unusual patterns or potential security incidents in real time. Set up alerts for security threats.
5. **Encrypt Payment Data**: Protect stored payment data with strong encryption algorithms to prevent unauthorized access.

---

### CASE 6: THE WEBSHELL BREACH - EXPLOITING XSS TO INFILTRATE CLOUD INFRASTRUCTURE

A fintech company specializing in tax-related services became the target of a sophisticated cyberattack that exposed critical weaknesses in its cloud infrastructure. The breach began with the exploitation of cross-site scripting (XSS) in a commonly used rich text editor embedded in the company’s web applications.

The attacker used the XSS vulnerability to inject malicious scripts, establishing a foothold within the company’s environment. From there, the threat actor escalated access, deploying webshells (enables a threat actor to remotely access the web server) to execute commands directly on the company’s Amazon Web Services (AWS) infrastructure. By leveraging these webshells, the attacker gained unauthorized access to the company’s Simple Storage Service platform (S3 bucket), where sensitive client data was stored.

This unauthorized access led to a severe data breach, operational disruption, and financial losses. Client trust eroded as sensitive financial records and business data were compromised, highlighting the cascading impact of inadequate web application security combined with cloud misconfigurations.

#### Top 5 Mitigation Strategies
1. **Multi-Factor Authentication**: Enable multi-factor authentication of users particularly for cloud, virtual private networks, webmail, and accounts that access critical systems.
2. **Cloud Instance Security**: Check public accessibility of all cloud instances in use. Make sure that no server/bucket is inadvertently leaking data due to inappropriate configurations.
3. **Access Token Security**: Ensure proper security of AWS/Azure/GCP access tokens. The tokens should not be exposed publicly in website source code, any configuration files, etc.
4. **Data Protection and Encryption**: Enforce data protection, backup, and recovery measures. Encryption of the data at rest should be implemented to prevent the attacker from accessing the unencrypted data in cases of data breaches/exfiltration.
5. **Least Privilege Access Control**: Implement least privilege principle for access control with granular permission to cloud resources.

---

### CASE 7: THE INSIDER THREAT: MANIPULATING DORMANT ACCOUNTS FOR FINANCIAL GAIN

An insider threat case (outside India) reveals how an employee abused administrative privileges to manipulate dormant accounts and withdraw funds undetected. With access to critical systems, the insider threat actor orchestrated financial pilferage over a period of two years.

The insider exploited dormant accounts in the system, using administrative access to request for prepaid cards linked to these accounts. By altering address details, the insider redirected the cards to itself, bypassing original account holders.

Post receiving the prepaid cards, the perpetrator manipulated the database to inflate account balances, loading the cards with substantial funds. The withdrawal of the money was via ATMs, concealing the modus operandi by deleting transaction data and restoring balances to erase all traces.

To maintain persistence, the perpetrator created misleading root cause analysis (RCAs) for unauthorized transactions. The investigations were misdirected ensuring the cover up continued undetected for two years.

#### Top 5 Mitigation Strategies
1. **Least Privilege Principle**: Apply the principle of least privilege across all system levels to minimize risk. Limit administrative access to critical systems and enforce strict role-based access controls (RBAC).
2. **Log Retention and Monitoring**: Redesign log retention policies to store logs for at least 180 days. Continuously audit and monitor logs to detect unusual patterns or unauthorized access to dormant accounts.
3. **Multi-Factor Authentication (MFA)**: Enforce MFA for accessing critical systems. Mandate MFA for remote access to prevent unauthorized administrative actions.
4. **Regular Security Audits**: Conduct regular security audits of internal systems and databases through CERT-In empaneled auditors. Regularly review and reconcile dormant accounts to detect and prevent unauthorized manipulation.
5. **Application Whitelisting and Network Segmentation**: Enforce application whitelisting on endpoints to block unauthorized software execution. Segment networks to restrict administrative access to specific zones, ensuring that sensitive systems are isolated from broader environments.

---

## SECURING THE EXPANDING IoT FRONTIER IN BFSI: A GROWING IMPERATIVE

The Internet of Things (IoT) is transforming the way businesses operate, particularly in industries driven by digital innovation such as Banking, Financial Services, and Insurance (BFSI). IoT has embedded itself into daily workflows, revolutionizing customer experiences and streamlining operations. From connected ATMs to wearable payment devices, the integration of IoT in financial services has redefined engagement, data collection, and service delivery.

The number of Internet of Things (IoT) opening through smart speakers and mobile devices. These advancements not only enrich customer experiences but also provide valuable insights into consumer behavior.

However, in the BFSI sector, IoT applications extend beyond front-end customer interactions. Check scanners, touch-enabled kiosks, branch digital signage, and bluetooth beacons silently operate behind the scenes, enhancing user engagement and operational efficiency. On-premise ATMs interfa

---

[^1]: Global Data Breach Report 2024.
[^2]: Cost of a Data Breach Report India 2024.
[^3]: Phishing Trends in India H1 2024.
[^4]: SISA DFIR Analysis on BEC Incidents 2024.
[^5]: Global Phishing and Initial Access Statistics 2024.
[^6]: Vulnerability Exploitation Research Report 2024.
[^8]: Deepfake Identity Fraud Statistics 2024.

---

ce with connected devices,
devices worldwide is forecast to reach 32.1 amplifying potential vulnerabilities.
billion IoT devices in 2030, significantly
broadening the attack surface. As IoT A key challenge in securing IoT in financial
adoption accelerates, financial institutions services is visibility and control—knowing
are increasingly relying on these devices where devices are deployed and how they
to optimize processes and enhance operate. Forrester’s research highlights
customer interactions. However, with this that 36% of financial leaders prioritize IoT-
exponential growth comes an alarming rise driven operational efficiency. Yet, many
in security vulnerabilities. Nearly 99% of IoT IoT deployments in banking, trade finance,
exploitation attempts leverage previously and supply chain management often lack
known vulnerabilities (CVEs), exposing adequate oversight. This lack of visibility
critical gaps in security infrastructure. leaves financial ecosystems exposed to
potential breaches and cyberattacks.
Financial institutions are increasingly
leveraging IoT for personalized services. The consequences of IoT vulnerabilities
Banks utilize IoT to identify and greet are significant. Forrester’s findings reveal
customers as they enter branches, enhance that 34% of enterprises impacted by IoT
credit risk assessments through real- breaches experienced losses ranging from
time data, and deliver targeted product $5 million to $10 million—substantially
recommendations via wearables. IoT- higher than attacks on traditional IT
powered devices also facilitate on-the-go infrastructure.
transactions and enable remote account
The last case is an in-depth analysis that explores IoT vulnerabilities and attacks,
providing valuable insights into how these risks translate to the BFSI sector. By
examining real-world incidents—from breaches through connected fish tanks and
medical devices to compromised home security cameras and cryptocurrency wallets—
this analysis underscores the critical need for enhanced IoT security measures.
23 DIGITAL THREAT REPORT 2024

CASE 8:
TURNING A $2 MILLION HACK INTO
A HARDWARE-HACKING MILESTONE
STRUCTURED AND SEGMENTED APPROACH FOR ATTACK VECTORS ACROSS THE BFSI OPERATIONS
Core Banking Systems Payment Processing Systems
Digital Financial Services Apps Cloud & Infra Mgmt
Vendor & Partner Integration Systems IoT & Connected Device Security
Hardware hacker Joe Grand successfully out” during the boot process, Grand tuning of signal widths, wire lengths,
unlocked a Trezor wallet (outside India) disrupted the firmware’s security check, and trigger points proved essential in
containing US$2 million in cryptocurrency by forcing the Trezor to copy the unencrypted hitting the microcontroller at exactly the
exploiting hardware vulnerabilities through seed and PIN into RAM—allowing him to right moment. After hours of meticulous
fault injection7. extract them without triggering the system’s attempts, Grand successfully retrieved the
safeguards. funds, demonstrating how microcontroller
Faced with strict PIN limits and irreversible weaknesses in embedded devices can be
data erasure, Grand used voltage glitching The attack required precise manipulation— exploited if not rigorously secured against
to disrupt the wallet’s boot process, removing capacitors, fine-tuning glitch fault attacks.
bypassing the Readout Protection (RDP) parameters, and avoiding crashes
mechanism. By precisely inducing a “brown- that could erase critical data. Careful
Mitigations Steps to Prevent Hardware Wallet Hacks
Strengthen Hardware and Physical Protection (RDP) levels and securely consumption, electromagnetic leaks,
Security locking or disabling debug interfaces or timing information. Implementing
in production environments is crucial to protections against side channel attacks
Ensuring the physical security of thwart such attacks. Debug interfaces are and continuously evaluating device
hardware wallets is paramount to prevent often exploited to access sensitive data or security through SCA simulations is critical.
unauthorized access and tampering. manipulate firmware, so securing them from Encrypting sensitive data stored in RAM
Implementing tamper detection systems the outset ensures a more resilient device. and employing secure communication
that trigger automatic data wipes if protocols during data exchanges adds
tampering is detected can significantly Ensure Secure Boot and Trusted further resilience against potential memory
reduce risks. Additionally, employing Firmware extraction attacks. This layered approach
tamper-evident and tamper-resistant minimizes the risk of data leakage even if
packaging serves as a deterrent against The boot process represents a critical attack parts of the device are compromised.
physical breaches. By isolating critical surface, making it essential to secure boot
components and restricting physical access processes with verified bootloaders. Utilizing Continuous Monitoring and Security
to sensitive areas, attackers are further a Hardware Root of Trust (HRoT) ensures Audits
hindered from exploiting vulnerabilities. that only authorized and verified firmware is
Secure microcontrollers with built-in loaded during the boot process, preventing Regularly updating and patching firmware
protections provide another layer of malicious code injections. Encrypting ensures that vulnerabilities are addressed
defense, making unauthorized physical sensitive data in RAM and minimizing promptly, reducing exposure to newly
access extremely challenging. exposure during the boot sequence further discovered threats. Comprehensive
reduces the attack surface. By ensuring hardware security audits help identify
Enhance Fault Injection and Debugging that each layer of the boot process is weaknesses in the device’s design and
Protections authenticated, potential attackers are implementation, allowing for pre-emptive
unable to manipulate firmware or introduce mitigations. Additionally, employing secure
One of the most effective ways to prevent vulnerabilities at the boot / startup time. communication protocols during data
hardware hacks is by implementing robust exchanges ensures that sensitive information
fault injection countermeasures. Fault Mitigate Side Channel and Memory- remains encrypted in transit. By establishing
injection attacks exploit vulnerabilities by Based Attacks a cycle of continuous improvement through
disrupting normal hardware operations, audits, patches, and updates, hardware
allowing attackers to bypass security Side channel attacks (SCA) can extract wallets remain resilient against evolving
mechanisms. Strengthening Readout sensitive information by analyzing power attack techniques.
24 DIGITAL THREAT REPORT 2024

REGULATORY FOCUS:
REGULATORY FOCUS:
A SPECIAL FEATURE
A SPECIAL FEATURE
25 DIGITAL THREAT REPORT 2024
25 DIGITAL THREAT REPORT 2024

2025 AND BEYOND: NAVIGATING EVOLVING
REGULATIONS IN THE DIGITAL PAYMENTS LANDSCAPE
As we move into 2025, the digital payments variations often result in inefficiencies, The integration of compliance and
and BFSI industries stand at the cusp of a especially in cross-border payment innovation is not merely a response to
transformative shift driven by regulatory solutions, which are crucial to the financial external pressures but a fundamental shift
changes and the accelerating digitization of industry’s global operations. in how organizations view their roles in the
financial services. digital ecosystem. The expected growth
Despite these hurdles, the narrative is of cyber attacks underscores the critical
In this shifting landscape, compliance is beginning to shift toward regulatory need for resilience and adaptability. In this
no longer merely a matter of adhering to harmonization. context, compliance is no longer seen as
checklists but has emerged as a strategic a cost center but as a cornerstone of trust
imperative that will shape the industry’s and a catalyst for growth. It has become an
future. This transformation is not without essential component of an organization’s
its challenges, but it also opens a gateway The push for unified ability to build credibility and foster long-
to significant opportunities for growth and global standards is gaining term customer loyalty.
resilience. momentum, offering a
way to bridge regional As the BFSI industry moves forward,
The rapid pace of regulatory evolution gaps and create cohesive the conversation around compliance is
has created a complex environment for frameworks that simplify evolving. What was once perceived as
financial institutions. Mandates such as compliance and improve a reactive, burdensome process is now
CERT-IN directives for reporting cyber operational efficiency. recognized as a strategic driver of resilience
incidents within 6 hours of noticing such and innovation. The ability to navigate a
incidents or being brought to notice about harmonized compliance framework will not
such incidents, RBI Master Direction in This movement toward regulatory alignment only help organizations manage the growing
Digital Payment Security Controls(DPSC) is not just a means of reducing friction but complexity of regulatory requirements
and Master Direction in Outsourcing of hold the promise of making compliance an but also position them to thrive in an
Information technology services; RBI enabler of growth for the financial sector interconnected, data-driven global
Cyber Security Framework in Banks globally. economy. The next decade will redefine
(CSF); SEBI’s Cybersecurity and Cyber the role of compliance, transforming it into
Resilience Framework (CSCRF), Digital The dual demands of regulatory compliance a force that propels the industry toward
Personal Data Protection (DPDP) Act, and technological innovation present a greater trust, innovation, and sustainable
2023, PCI DSS 4.0, European General Data delicate balancing act for digital payment growth.
Protection Regulation (GDPR),the California organizations. The need to stay ahead in
Consumer Privacy Act (CCPA) have set new areas such as real-time payments, fraud
benchmarks for accountability and data detection, and predictive financial services
protection. These frameworks underscore requires a forward-looking approach RBI, IRDA and SEBI are
the urgent need for organizations to to compliance. Emerging techniques proactively supporting the
anticipate and adapt to emerging risks, like data anonymization and synthetic BFSI sector from a policy
especially as the digital payments sector, data generation are paving the way for and direction perspective,
with its vast repository of sensitive financial innovation without compromising privacy CERT-In and CSIRT-Fin are
data, becomes an increasingly attractive or security. Additionally, embedding helping from a strategic,
target for cyber perpetrators. However, compliance into the design phase of new tactical and operational
the fragmented nature of compliance technologies is proving to be a game- perspective. Thus, all
frameworks across jurisdictions adds changing strategy, enabling organizations to these entities are working
another layer of complexity, particularly for future-proof their innovations and mitigate cohesively to ensure trust
businesses operating across borders. Local risks proactively. and resilience in the BFSI
laws, cultural nuances, and jurisdictional sector for all stakeholders.
26 DIGITAL THREAT REPORT 2024

SUGGESTIONS TO
POLICY MAKERS
Cybersecurity should be a techno- Empower CISOs through direct
commercial business decision and reporting to the CEO/CRO instead of
notjustdecidedonlyoncommercials CTO or CIO
Cybersecurity investments must be driven Granting Chief Information Security Officers
by a balance of technical requirements and (CISOs) direct access to top leadership
commercial viability. Prioritizing security as a enables better alignment of cybersecurity
strategic enabler ensures resilience, robust strategies with business goals, ensuring
protection against threats, safeguarding accountability and a stronger focus on
business continuity and customer trust. organizational risk management.
Digital Payment Security to have Create more Certified Digital Payment
common standards for all Digital Security Specialists in the ecosystem
Payment Form Factors
Harmonizing security standards across all Addressing the talent gap requires fostering
digital payment methods—not just cards— a skilled workforce through certification
ensures a consistent and comprehensive programs focused on payment security.
security framework that addresses emerging This will enable enterprises to design secure
risks in alternative payment systems like payment applications and implement robust
wallets, UPI, and QR codes. security standards effectively.
Clear Preparation Roadmap for Post- Building a Responsible AI Framework
Quantum Cryptography for BFSI
Policymakers must prioritize developing a To ensure the responsible deployment of
strategic roadmap to transition to quantum- AI and ML in the banking and financial
resistant cryptography, ensuring businesses services industry, policymakers must
are prepared for future threats posed by implement clear, comprehensive regulations
quantum computing advancements. that balance innovation with consumer
protection and system stability. Providing
the industry with clear guidelines around
critical aspects such as data privacy, ethical
AI use, and algorithmic transparency
will encourage responsible AI adoption,
supporting growth while safeguarding
the integrity of the financial sector and
protecting consumer interests.
27 DIGITAL THREAT REPORT 2024

INSIGHTS ACROSS LAYERS
INSIGHTS ACROSS LAYERS
OF DEFENSE SEEN IN BFSI
OF DEFENSE SEEN IN BFSI
SECTOR
SECTOR
28 DIGITAL THREAT REPORT 2024
28 DIGITAL THREAT REPORT 2024

Now that we’ve explored advanced threats on cybersecurity, it also underscores a with robust defenses face significant risks,
and exploitation techniques, let’s examine concerning trend: the more we spend, the emphasizing the need for continuous
the compliance levels based on sampled more sophisticated and widespread attacks vigilance, proactive measures, and
entities in the BFSI sector. become. This paradox isn’t merely about alignment between compliance and security.
advanced threat actors; it’s also about Achieving resilience requires continuous
Cybersecurity today mirrors Einstein’s notion foundational cracks in how organizations threat visibility, proactive defense strategies,
of insanity—relying on the same strategies approach cybersecurity. continuous training & awareness of the work
and expecting different outcomes. force, robust processes and a security-first
Despite increasing investments in security For instance, the average organization mindset that uses compliance frameworks as
technologies, breaches remain frequent. deploys an astonishing 64-76 cybersecurity a foundation.
tools8, yet breaches do occur. Why?
Consider this: Gartner projects worldwide Because the solution isn’t simply about In the next section, we decode the domains
end-user spending on information security spending more money or adding more where further improvements are needed.
to reach US$212 billion by 2025, marking tools. Resilience cannot be achieved
a 15.1% increase from 2024. While this through isolated efforts. Both organizations
reflects the growing importance placed with weak security postures and those
% COMPLIANT IN % COMPLIANT
HEADING CONTROL
INDIA GLOBAL
Hardening and configuration documentation
System Hardening and Configuration
aligned with Center for Internet Security (CIS)
Management
standards
System Hardening and Configuration Configuration standard and baseline document
Management maintenance
Encryption of cardholder data and masking of
Data Protection and Encryption
sensitive information
Use of tokenization or TDE (Transparent Data
Data Protection and Encryption
Encryption) for sensitive data
User access lists for Cardholder Data
Access Control and User Management Environment (CDE) and privileged access
controls
Timely application of patches and adherence to
Patch and Vulnerability Management
vulnerability management procedures
IDS/IPS configurations to detect and prevent
Intrusion Detection and Prevention
unauthorized access
Network segmentation to isolate CDE and
Network Security and Segmentation
prevent lateral movement
Multi-factor authentication (MFA) and password
Authentication and Password Management
configuration policies
Centralized logging and monitoring of failed
Log Monitoring and Event Management
logins and access attempts
Defined incident response procedures and
Incident Response and Contingency Planning
contingency planning
Regular internal and external vulnerability scans
Regular Testing and Vulnerability Scanning
and penetration testing
Manageable Needs Improvement Major Concern
29 DIGITAL THREAT REPORT 2024

METHODOLOGY FORDETERMINING COMPLIANCE PERCENTAGES
(FOR INDIA &GLOBAL)
| Assessment Scope | Data Sources | Standards Covered |
| ---------------- | ------------ | ----------------- |
SISA assessed approximately 1,550 clients  The analysis is based on technical gap  The gap assessments included PCI DSS, PCI
globally between November 2022 and  reports generated from assessments  PIN, P2PE, PCI SAQ, and local governance
November 2024 to derive the observed  conducted by SISA’s Qualified Security  standards and regulations.
| control gap compliance percentages.    | Assessors (QSAs).                         |     |
| -------------------------------------- | ----------------------------------------- | --- |
| India-Specific Calculation             | Global Calculation                        |     |
| Out of 850 clients assessed in India,  | A similar methodology was applied to 700  |     |
clients assessed outside India to determine
765 were compliant while frequently
global compliance percentages.
encountering observed control gaps.
EVALUATINGSECURITY MATURITY:TECHNICAL TRENDS
AND GAPS IN THE BFSISECTOR
The security posture of financial institutions audited/reviewed across various domains
demonstrates a mixed level of compliance and maturity in critical security areas.
Here’s a breakdown of key trends and gaps observed across different security layers
in the BFSI sector:
Perimeter Security/Network Security
Content Filtering / Proxy: This area
| Firewall: Most institutions have  | Conformance (DMARC), and Sender Policy  |     |
| --------------------------------- | --------------------------------------- | --- |
implemented basic firewall configurations,  lacks dedicated solutions and consistent
Framework (SPF) configurations. However,
rule reviews. Absence of content control
| however, clients allow all traffic through  | geo-location-based blocking and periodic  |     |
| ------------------------------------------- | ----------------------------------------- | --- |
increases exposure to unfiltered, potentially
| open policy configurations, lacking granular  | rule reviews are often missing, which  |     |
| --------------------------------------------- | -------------------------------------- | --- |
control. Additionally, insufficient impact  weakens phishing and spam defences. malicious traffic.
analysis in change management processes
Web Application Firewall (WAF):WAF
| leads to critical changes not being tracked,  | Virtual Network / Network Segregation: |     |
| --------------------------------------------- | -------------------------------------- | --- |
implementation is inconsistent. Many
| increasing the risk of unauthorized access. | Many institutions have implemented          |                                              |
| ------------------------------------------- | ------------------------------------------- | -------------------------------------------- |
|                                             | network segmentation but often lack proper  | applications are not covered, and URI paths  |
DDoS Mitigation: DDoS protection is  are not adequately tested or blocked. High
testingandvalidationofthesesegmentation
and medium threat signatures are often
| largely limited to internet service provider  | controls. Overly broad access control  |     |
| --------------------------------------------- | -------------------------------------- | --- |
set only to detect, leaving gaps in active
| (ISP)-level solutions, and dedicated  | mechanisms are frequently observed, which  |     |
| ------------------------------------- | ------------------------------------------ | --- |
enterprise-grade DDoS mitigation is often  undermines the intended security benefits  defences.
| missing. This leaves institutions vulnerable  | of segmentation. |     |
| --------------------------------------------- | ---------------- | --- |
to volumetric and application-layer attacks.
Secure Configuration
Application Security
Content Filtering / Proxy: Similar to
Webserver & Database: Lack of application
| application security, network-level content  | IPS/IDS: There is a fair presence of Intrusion  |     |
| -------------------------------------------- | ----------------------------------------------- | --- |
hardening and limited security standards
| filtering shows a lack of dedicated solutions  | Prevention and Detection systems. However,  |     |
| ---------------------------------------------- | ------------------------------------------- | --- |
in application design, coupled with
| and regular reviews, which are essential for  | medium and low severity signatures often  |     |
| --------------------------------------------- | ----------------------------------------- | --- |
filtering malicious or unwanted traffic. remain unblocked, and many organizations  inadequate coordination between security
and application teams, results in a larger
lack internal IPS, posing risks to application
attack surface and greater exposure to
| Email Gateway: Email gateways  | security. |     |
| ------------------------------ | --------- | --- |
vulnerabilities.
primarily use standard Domain-based
Message Authentication, Reporting, and
30 DIGITAL THREAT REPORT 2024

Cloud Security IAM (Identity and Access Data Protection and Encryption
Management) Security
General Cloud Security: Cloud Encryption of data and masking
environments show significant gaps. Identity Security: Identity security remains sensitive information – Sensitive and
Subscriptions often lack hardening per CIS a crucial gap. MFA is not universally confidential data is not stored in encrypted
or global standards, with MFA and logging enforced on VPN profiles, and conditional form or masked leading to a breach
not enabled by default. Local accounts, access policies are missing in a majority of of confidentiality of stored data. Non-
sometimes exposed to the internet, increase environments, which increases susceptibility compliance to this control may lead to
risk of unauthorized access. to unauthorized access. malicious entity to derive the sensitive data.
Cloud Environment Specifics (AWS, Azure, User Access review: If excessive user
GCP): Common gaps include missing audit rights are not revoked or accounts for all VAPT (Vulnerability Assessment and
logging for PaaS, insufficient hardening, and terminated users have not been removed Penetration Testing)
absent MFA. These vulnerabilities reflect a in due time, they may be used by malicious
need for stronger cloud access control and users for unauthorized access. Internal/External vulnerabilities and
monitoring. Penetration testing – Periodic vulnerability
management and penetrations testing are
Endpoint Security not regularly followed by many financial
Monitoring & Response institutions. Attackers routinely look for
Endpoint Detection and Response (EDR): unpatched or vulnerable externally facing
Security Logging: Critical logs such as Most large financial institutions have servers, which can be leveraged to launch a
DNS, proxy, MFA, and O365 (email logs) implemented EDR solutions, providing directed attack. Because external networks
are not integrated by many organizations. advanced detection and response are at greater risk of compromise, external
This lack of integration limits visibility and capabilities. However, some mid-sized and vulnerability scanning must be performed
hampers the ability to detect potential smaller clients are still relying primarily periodically.
threats effectively. Additionally, API- on traditional antivirus (AV) solutions with
based integrations for SAAS services limited EDR functionality. This limits the
are sometimes constrained by licensing scope of endpoint threat containment
limitations, further impacting comprehensive and makes them more vulnerable to
threat monitoring. sophisticated attacks that require proactive
threat hunting and automated response.
SIEM Integration: SIEM integration lacks
comprehensive data feeds, such as DNS and
MFA logs, essential for threat correlation.
This hinders timely detection and response
capabilities, particularly for SAAS and cloud
environments.
31 DIGITAL THREAT REPORT 2024

GAZING THROUGH THE
GAZING THROUGH THE
CRYSTAL BALL FOR 2025
CRYSTAL BALL FOR 2025
32 DIGITAL THREAT REPORT 2024
32 DIGITAL THREAT REPORT 2024

GAZING THROUGH THE CRYSTAL BALL FOR 2025
TBhefiso rree pwoer td idvrea iwnsto o rne ctohme mcoelnledcattiivoen s  aarrteifi schiaiflt iinntge ltloigweanrcdes.  Ahtatramckosn iinz a2t0io2n5 ,w  ill  Drawing insights from observed threats
ebxapseedrt oisne  tahned g ianpssig ahntds  vouf lninedraubstilriyti es  wnoitth o tnhlye  bgeo mal oorfe  usnoipfyhiinstgic datisepda brautte a lso  across the digital payment ecosystem,
lheigadhleigrsh tteod p inro tvhied ep rae vuinoiufise sde cvtiieown,  oitf’ s  setxapnodnaerndtsia allcyr mososr ere egviaosnivse.  Canodm ppeliravnacsiev e.  we present a series of predictions for
tchruec ciayl btoe rssheicftu oriutyr  floacnudss fcoarpwea ridn  a2n0d2 4g.r asp  iTsh trreaants afoctromrsin agre f rsoemt t oa  hbaurrndeesns sAoIm toe  craft  2025 - seven highly anticipated attack
Ihto rwefl tehcet cs yab esersaemculeristys  leaxncdhsacnagpee  ios fs et to  ohibglhiglya ctiuosnto imntioze ad  satsrasateugltsic,  leenavaibnlge rm—inimal  methodologies likely to dominate the threat
ktrnaonwsfolerdmg ien,  tshhea cpoemdi nbgy  yreeaarl.- wUondrledr sctyabnedri ng  otrnacee t hasa tt hceayn  oupneloractke  gatr oawn tuhn, pimrepcerodveen ted  landscape in 2025.
| itnhcei dtreenntdss,  aenvdo lcvhinaglle andgveesr osaf r2ia0l2 t5a cist incos,t  and  |     | oscpaelera—tipoonwael reefdfic bieyn tchye,  saanmde r ereinvofolurctieo nary  |     |
| -------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------ | --- |
ejumste vragliunagb lteh—reiat’st  iinmtpeellirgateivnec efo.r crafting  rteecshilineonloceg iiens  steracntsofrosr mlikineg d iingdituaslt prieasy ments,  These insights aim to empower
strategies that are resilient to the threats of  wglhoebraell ys.e Andsidti vtoe  tdhaatta t hreem loaoinmsi nag p qriumanet um  organizations with a forward-looking
Btoym inotrerogwra.ting a national perspective on  tcaormgeptu tfionrg a rtetavockluetrios.n capable of rendering  perspective, guiding them to anticipate,
cyber trends with frontline experience  today’s encryption obsolete, organizations  adapt, and fortify their defenses in the
iAns  mwieti gpeateirn ign tsoo tphhei sftuitcuartee odf  actytbaeckrsse, ctuhriist y,  Bfaecnee aant he vtohlevsineg s atrnadte cgoimc pshleifxt sr eliaelist ya.  more  face of an increasingly volatile cyber
rtheep ocrryt sdtaell ibvaelrls r eav heoallsis ati cla undndscearpstea nding  pPrreepssairningg r feoarl itthye—sec rsietiicsaml icc osnhtifrtos l isg anpo s  environment.
| odrfa tmhea tsichaiflltyin rges thharpeeadt  ebnyv tihroen pmoewnetr.  oTfh e  |     | cloonngteinr uoep ttioo npael;r siti’sst  eascsreonstsia iln fdour ssturriveisv.a l. |     |
| ------------------------------------------------------------------------------ | --- | ------------------------------------------------------------------------------------ | --- |
| result is a comprehensive resource that                                        |     | Weak access controls, over-privileged                                                |     |
| empowers organizations to anticipate                                           |     | user accounts, and misconfigurations                                                 |     |
| risks, strengthen defenses, and navigate                                       |     | leave even the most fortified                                                        |     |
| the complexities of today’s cybersecurity                                      |     | organizations exposed. This report                                                   |     |
Rise of deep fakes &
| challenges. |     | highlights how these vulnerabilities are  |     |
| ----------- | --- | ----------------------------------------- | --- |
AI generated content
not merely by-products of oversight but
structural wAtetaackkenrse wsisll elesv etrhagaet  daedepv ersaries
Over the past year, cyberattacks have
fakes to impersonate executives
| grown more sophisticated, driven by  |     | consistentalynd e bxyppalsos ivte triofic adtieonv,a esntaabtliinngg  effect. |     |
| ------------------------------------ | --- | ----------------------------------------------------------------------------- | --- |
social engineering attacks.
the intersection of new techniques and
| the persistence of proIovTe dne mviceeths oedxps.a nding |     | As the industry braces for what lies  |     |
| -------------------------------------------------------- | --- | ------------------------------------- | --- |
Growing threat of
Social engineering, ina tptaacrkti csuurlfaar,c ehsas  ahead, the future of cybersecurity is  supply chain attacks
and malicious libraries
| surged to the forefront, with Business  |     | already being reshaped by artificial  |     |
| --------------------------------------- | --- | ------------------------------------- | --- |
Compromised IoT devices
Email Compromise (BprEoCvid) ea enndtry  apdoivntas nfocr eatdta ckers,  intelligence (AI). The same technology  Malicious code injected into
|     | enabling lateral movement  |     | trusted software updates or  |
| --- | -------------------------- | --- | ---------------------------- |
phishing campaigns oacproessr anettiwnogrk ws ainthd  potentially  that drives innovation is arming attackers  libraries compromises entire supply
alarming precision. Tdhiseruspeti nagt tcaritcickasl ,o poefrtaetionn s. chains, spreading vulnerabilities
with the tools to conduct highly
across multiple organizations.
| bolstered by data sourced from the dark  |     | personalized, evasive, and large-scale  |     |
| ---------------------------------------- | --- | --------------------------------------- | --- |
01
| web, bypass traditional defenses by           |     | attacks. In 2025 and beyond, AI-driven      |     |
| --------------------------------------------- | --- | ------------------------------------------- | --- |
| leveraging stolen credentials and session     |     | threats0 w7ill challenge existing defense   |     |
| cookies, effectively neutralizing multi-      |     | mechanisms, forcing organizations to0 2     |     |
| factor authentication. Meanwhile, supply      |     | rethink their approach to threat detection  |     |
| chain breaches have escalated, exploiting     |     | and respoAnNseT.ICIPATED CYBER              |     |
| the trust organizations place in third-party  |     | THREATS IN 2025                             |     |
Crypto - A new frontier Emerging threat of
| vendors anfdo ro cpyebner- stohurercaets repositories  |     | T0h6is report offers concrete  |     |
| ------------------------------------------------------ | --- | ------------------------------ | --- |
Identify. Defend.  LLM prompt hacking
| thereby int | ro d u c i n g   v u l n e r a bilities at  | recommendatSioecnusr ero thoete fudt uinre f.rontline  | 03  |
| ----------- | ------------------------------------------- | ------------------------------------------------------ | --- |
C yb e r a t ta c ke r s  e x p lo it   Attackers manipulate LLM
scale.  cryptocurrencies for anonymous  audits and incident analysis, outlining the  (Large Language Models)
transactions, target crypto wallets,  steps necessary to close control gaps,  inputs to extract sensitive data,
and attack exchanges, leading to  override controls, and induce
Yet, the risifinngan ctiiadl teh eoft fa ncdy bexetorr ttiohnr.eats is  harmful outputs in local Al
strengthen defenses, and build adaptive  05
applications.
| not occurring in isolation. As digital   |     | strategies against emergin0g4 threats. The  |     |
| ---------------------------------------- | --- | ------------------------------------------- | --- |
| ecosystems expand, so too does the       |     | findings presented here serve as both a     |     |
| recognition that compliance must evolve  |     | reflection of the current landscape and a   |     |
| beyond rigid frameworks. This report     |     | guidepost for navigating the uncertainties  |     |
explores how regulatory landscapesQ uantum coomf ptoumtinogr r-ow. Adversarial LLMs
|     | A looming threat to           | enchaning attack                 |     |
| --- | ----------------------------- | -------------------------------- | --- |
|     | cryptography                  | capabilities                     |     |
|     | Quantum advancements          | Malicious LLMs (Large Language   |     |
|     | threaten to break current     | Models) enable attackers to      |     |
|     | encryption methods, exposing  | automate malware creation,       |     |
|     | sensitive data and enabling   | phishing campaigns, and exploit  |     |
|     | large-scale cyber espionage.  | development, intensifying the    |     |
threat landscape.
833 DDIIGGIITTAALL  TTHHRREEAATT  RREEPPOORRTT  22002244

ANTICIPATED ATTACK 1:
RISE OF DEEP FAKES AND AI-GENERATED CONTENT
Attackers are expected to increasingly for multi-factor authentication (MFA),
leverage deep fakes and AI-generated passwords, or other sensitive information.
content as potent tools for intrusion,
particularly in social engineering attacks. The challenges in detection and verification
The advancement of deep fake technology of such AI-generated content are significant.
enables the creation of highly realistic and As the technology becomes more
manipulated audio and video content that sophisticated and accessible, it becomes
can convincingly impersonate individuals. increasingly difficult for users to distinguish
between genuine and manipulated media.
Deep fake voice and video allow cyber Traditional verification methods that rely
perpetrators to mimic the voices and on voice recognition or visual confirmation
appearances of executives, employees, or are no longer sufficient, as deep fakes can
trusted partners. For example, an attacker replicate these cues with high accuracy.
might use a deep fake video during a This creates substantial risks, especially in
virtual meeting to deceive a finance team business contexts where critical decisions
into authorizing a unauthorized transfer or and transactions are made based on virtual
employ a deep fake voice to trick individuals interactions.
into revealing one-time passwords (OTPs)
ANTICIPATED ATTACK 2:
GROWINGTHREATOFSUPPLYCHAIN
ATTACKS AND MALICIOUS LIBRARIES
Attackers are expected to increasingly Unsuspecting developers may inadvertently
focus on supply chain attacks, exploiting incorporate these tainted libraries into
vulnerabilities in software development their projects, introducing vulnerabilities,
processes to compromise multiple backdoors, or malware into their
organizations simultaneously. One applications. This method allows attackers
primary method involves the exploitation to spread malicious code across a wide
of code repositories. Cyber attackers array of software products and services,
gain unauthorized access to developers’ amplifying the potential impact.
accounts on platforms like GitHub or inject
malicious code into the source code of Furthermore, there is growing apprehension
widely used applications. By infiltrating the about the influence on Large Language
development environment, attackers can Models (LLMs). Attackers may attempt to
insert malware directly into the codebase, manipulate LLMs or their training data to
which is then unknowingly distributed to promote malicious libraries. By poisoning
clients through regular software updates or the datasets or exploiting vulnerabilities
new releases. This tactic enables attackers in the models, they can cause LLMs to
to bypass traditional security measures, as suggest or generate code that includes
the malicious code originates from a trusted compromised libraries. Developers
source. relying on LLMs for coding assistance or
recommendations might then integrate
these malicious components into their
applications, unknowingly propagating
Another concerning trend vulnerabilities. Even in organizations that
is the distribution of prohibit direct use of LLM-generated
maliciouslibrariesdisguised code, developers may still seek guidance
as genuine. Attackers from these models, increasing the risk of
publish counterfeit libraries incorporating tainted libraries.
that mimic legitimate ones,
often with names that
are deceptively similar to
popular libraries.
34 DIGITAL THREAT REPORT 2024

ANTICIPATED ATTACK 3:
EMERGING THREAT OF LLM PROMPT HACKING IN APPLICATIONS
As Large Language Models (LLMs) become Attackers can exploit these vulnerabilities
increasingly integrated into various to manipulate the LLM’s output, leading to
applications, there is a growing threat unauthorized actions, disclosure of sensitive
of LLM prompt hacking, where attackers information, or the generation of harmful
manipulate the inputs to these models content.
to induce unintended and potentially
harmful behaviors. This threat is particularly Prompt Hacking Techniques and Risks
pronounced in applications that host
LLMs locally, rather than relying on APIs One common prompt hacking technique
from established providers like OpenAI or involves crafting inputs that bypass the
Anthropic. model’s intended constraints, such as the
“grandmother exploit,” where attackers
manipulate the model into providing
disallowed information by framing the
request in a specific context.
Locally hosted LLMs may
proprietary data or personally identifiable
lack the comprehensive
Attackers may use prompt injection attacks information (PII) that the model has been
safety measures and
to override system prompts or extract trained on.
robust security features
confidential data that the model has been • Manipulate decision-making processes:
implemented by these
exposed to during training. In applications Influencing the outputs of the LLM in
providers, making them
like chatbots, virtual assistants, or interactive ways that could affect business decisions,
more susceptible to
voice response (IVR) systems, attackers customer interactions, or automated
exploitation.
with knowledge of the underlying LLM can systems.
manipulate prompts to:
Vulnerabilities in Locally Hosted LLMs The risks associated with LLM prompt
• Inject malicious content: Causing hacking are significant, as successful
When organizations incorporate LLMs the LLM to generate harmful or attacks can compromise data integrity,
directly into their environments, they assume inappropriate responses that could confidentiality, and system availability.
the responsibility for implementing security damage the organization’s reputation or Organizations relying on LLMs for critical
measures to protect against prompt hacking lead to legal issues. functions may face severe consequences,
and other attacks. Many locally hosted LLMs • Exfiltrate data: Extracting sensitive including data breaches, financial losses,
may not have sufficient safeguards against information from the model, such as and erosion of customer trust.
adversarial inputs, leaving them vulnerable.
ANTICIPATED ATTACK 4:
INFLUENCE OF ADVERSARIAL LLMS ENHANCING
ATTACK CAPABILITIES
Attackers are increasingly leveraging generated malware and exploits can adapt, Furthermore, the availability of adversarial
adversarial Large Language Models (LLMs) obfuscate, and mutate to avoid detection LLMs lowers the barrier for novice malicious
to significantly enhance their cyberattack by conventional antivirus software and actors. Individuals with limited technical
capabilities, posing new challenges to Endpoint Detection and Response (EDR) expertise can now execute complex
cybersecurity defenses. These malicious systems. cyberattacks by simply interacting with these
LLMs—such as WormGPT, FraudGPT, malicious AI models. This democratization
WolfGPT, and XXXGPT—are designed to of advanced attack capabilities leads to an
generate sophisticated and tailored cyber increase in the volume and sophistication
threats with minimal effort. By utilizing these The polymorphic nature of cyber threats, as more threat actors can
advanced models, attackers can create of AIcrafted code means launch attacks that previously required
highly effective malware, craft convincing that signature-based specialized skills.
phishing emails, and automate the detection methods are less
development of exploits. effective, as each iteration
can appear unique while
One of the key concerns is the evasion maintaining its malicious
of traditional security measures. AI- functionality.
35 DIGITAL THREAT REPORT 2024

ANTICIPATED ATTACK 5:
QUANTUM COMPUTING - A LOOMING THREAT TO CRYPTOGRAPHY
Quantum computing is set to revolutionize Current encryption methods, both symmetric encryption by effectively halving
the world of information technology by asymmetric algorithms like RSA and the key length.
introducing computational power that symmetric algorithms such as Triple DES (3-
vastly exceeds current capabilities. With an DES) and certain key lengths of AES (like 64- In such a scenario, we face a situation
exponential increase in processing speed— bit AES), rely on the computational difficulty where the integrity of the sender in any
sometimes described in astronomical terms of specific mathematical problems. Classical communication cannot be trusted. Intruders
like 2 to power of 3 to the power of 1000 computers find it infeasible to solve these equipped with quantum computers could
—quantum computers can tackle complex problems within a reasonable timeframe, easily break encryption keys and algorithms,
problems that are practically unsolvable by which is why these encryption methods are enabling them to conduct man-in-the-
classical computers. considered secure. middle attacks. They could intercept,
decrypt, and even alter messages without
However quantum computing holds the the sender or receiver being aware,
potential to break existing encryption compromising the confidentiality and
The introduction of algorithms and keys that safeguard our integrity of the communication.
quantum computing digital communications. Algorithms
poses a critical threat like Shor’s algorithm can factor large
to all applications and numbers and compute discrete logarithms
communication channels exponentially faster than classical
that rely on public key algorithms. This capability effectively
infrastructure, digital renders asymmetric encryption vulnerable.
certificates, and key Similarly, Grover’s algorithm can speed up
exchange protocols. the brute-force search process, weakening
ANTICIPATED ATTACK 6:
CRYPTO: A NEW FRONTIER FOR CYBER THREATS
Cryptocurrency has significantly altered Additionally, a new breed of malware This trend has led to the development of
the cyber threat landscape, empowering has emerged that goes beyond the an entire ecosystem designed to support
intruders in ways that previous technologies traditional goal of harvesting Personally these illicit transactions. Services and
could not. Initially, the cyber perpetrators Identifiable Information (PII). These platforms have emerged to facilitate the
utilized Bitcoin for illicit transactions sophisticated malware programs scan exchange, laundering, and obfuscation of
due to its widespread acceptance. infected environments not just for sensitive cryptocurrency funds, making it easier for
However, they’ve since migrated to other data but specifically for the presence of intruders to monetize their activities without
cryptocurrencies like Monero (XMR), cryptocurrency wallets or the keys that leaving a traceable trail.
which offer enhanced privacy and non- secure them. By extracting these keys,
traceability. Monero’s advanced encryption intruders can gain unauthorized access to
techniques obscure transaction details, victims’ crypto assets, leading to significant
making it exceptionally challenging for law financial losses.
enforcement agencies to trace funds and
identify the individuals involved.
This shift in cryptocurrency preference has
The evolution of
also seen a change in the tactics employed
cryptocurrency has also
by intruders. They have evolved from using
facilitated the rise of
compromised systems merely as crypto
ransom and data extortion
miners—where infected computers are
schemes. Malicious
hijacked to mine cryptocurrencies without
actors now commonly
the owner’s knowledge—to more direct
demand payment
and profitable endeavours like targeting
in cryptocurrencies,
cryptocurrency exchanges. By attacking
leveraging their anonymity
these exchanges, intruders aim to steal
to avoid detection.
large amounts of digital currency, exploiting
security vulnerabilities within these
platforms.
36 DIGITAL THREAT REPORT 2024

ANTICIPATED ATTACK 7:
IoT,THE EMERGINGTHREATS TO EMBEDDED DEVICES
Cloud-Connected Embedded Devices malicious firmware, bricking devices or
causing widespread failures. Attackers can
Embedded devices increasingly rely on exploit open debug interfaces to reverse
cloud services like Amazon Elastic Compute engineer firmware and tamper with the
Cloud (AWS EC2) and Message Queuing OTA process. Since firmware is often
Telemetry Transport (MQTT) brokers to identical across devices, malicious updates
transmit and store data. These devices propagate rapidly, turning a single breach
collect sensor or user data and push it into a system-wide threat.
to services like AWS S3 using temporary
credentials assigned by the cloud. While
efficient, this creates vulnerabilities— Hardware Trojans, chip backdoor &
compromised credentials from one device “Movie-Style” Attacks in real life
can grant attackers access to the larger
cloud infrastructure. If thousands of devices Hardware Trojans—malicious circuit
share identical configurations, breaching modifications—can be inserted during
one can expose the entire fleet, risking chip fabrication or assembly. Attackers
data theft, lateral movement, or operational or nation-states can implant these rogue
disruption. components that remain dormant until
triggered. An extra chip can be concealed
beneath a Ball Grid Array (BGA) package or
Firmware Reverse Engineering, IP masked with high-temperature adhesives,
Theft, Digital Twins & Secret Extraction making detection nearly impossible without
specialized forensics. These implants
Firmware holds the core intellectual enable remote takeovers, allowing attackers
property (IP) and operational logic of to control infrastructure with a single
embedded devices, making it a high- command. In large-scale deployments,
value target for attackers. By reverse compromising one node can escalate
engineering firmware, adversaries can inject to entire networks. Lack of PCB-level
malicious code, alter device behavior, or inspectionsleavescriticalsystemsvulnerable
create “digital twins” that mimic legitimate to these stealthy attacks.
devices while feeding manipulated data
into real systems. This can disrupt critical
operations, especially in environments Scalability of Attacks, Mod Chips, Side-
where devices control physical processes or Channel Analysis and Glitching
infrastructure. Additionally, firmware often
contains proprietary algorithms and secrets, Hardware exploits, once developed, can
allowing attackers to clone products, bypass be mass-produced through mod chips
protections, or extract shared encryption or glitching techniques. Mod chips—
keys embedded across entire product lines. initially used to bypass gaming console
Asinglecompromiseddevicecanexpose an security—can scale to automotive and IoT
entire fleet, enabling adversaries to escalate systems, bypassing protections at scale.
privileges, manipulate data, or propagate Side-channel analysis reveals sensitive
malware across interconnected systems, data by monitoring power consumption or
threatening IP, operational security, and electromagnetic leaks, while voltage faults
product integrity. at critical moments can bypass security
checks. These scalable methods transform
niche vulnerabilities into widespread threats,
OTA Updates & Single-Device Pivot compromising even highly secure systems.
Over the air (OTA) updates simplify firmware
patching but introduce significant risk. A
compromised update server can distribute
37 DIGITAL THREAT REPORT 2024

RECOMMENDATIONS:
RECOMMENDATIONS:
STRENGTHENING YOUR
STRENGTHENING YOUR
CYBERSECURITY POSTURE
CYBERSECURITY POSTURE
38 DIGITAL THREAT REPORT 2024
38 DIGITAL THREAT REPORT 2024

RECOMMENDATIONS: STRENGTHENING
YOUR CYBERSECURITY POSTURE
Having explored the TTPs (Tactics, The solution lies in establishing effective, defenses, mitigate vulnerabilities, and
Techniques, and Procedures) used by adaptable, and forward-thinking effectively protect sensitive data. These
attackers, examined unique case studies cybersecurity strategies. recommendations aim to empower
showcasing their stealth and evasion organizations to stay ahead in an ever-
techniques, and gained a glimpse into The following section highlights the key evolving threat landscape while enhancing
the anticipated trends of 2025, it’s time controls organizations should implement, operational efficiency and resilience.
to focus on the critical question: What based on insights from audit and
can organizations do to stay secure? incident analysis findings, to strengthen
ADAPTABLE, FORWARD-THINKING CYBERSECURITY IS BUILT
ON KEY CONTROLS THAT DEFEND, MITIGATE, AND PROTECT.
PEOPLE
(Awareness, Training, and Culture)
• Increase the Frequency of Information Security Training
• Strengthen Risk Management and Governance
• Focus on Securing Remote and Hybrid Work Technologies
PROCESS
ENHANCING
(Policies, Procedures, and Governance)
RESILIENCE
• Accelerate Vulnerability Assessments Time Frame
• Develop Comprehensive Incident Response Playbooks
ACROSS KEY
• Integrate Threat Intelligence into Monitoring Processes
• Defense-in-depth program
DOMAINS
• Zero Trust Architecture (ZTA) Implementation
TECHNOLOGY
(Tools, Systems, and Solutions)
• Increase the Frequency of Patching Network Devices
• Implement Al-Powered Anomaly Detection and Dark Web Monitoring
• Application and API Security
• Authentication and Access Control
• Endpoint and Email Security
• Security Testing of Al-Native Applications
39 DIGITAL THREAT REPORT 2024

BUILDING A RESILIENT PEOPLE - FORCE: STRENGTHENING CYBERSECURITY
THROUGH TRAINING, GOVERNANCE, AND REMOTE SECURITY
A strong and adaptable cybersecurity posture begins with people. Organizations must
foster a culture where cybersecurity awareness is continuous, leadership-driven, and
embedded across all levels.
Continuous Information Security Risk Management and Governance
Training for Long-Term Resilience
Transitioning from annual to quarterly A proactive, comprehensive risk
security training enhances resilience by management framework is essential
keeping employees vigilant against evolving to enhance regulatory adherence and
threats like AI-driven phishing and deepfake fortify the overall security posture. This
scams. Frequent education ensures that framework drives transparency, enables
staff stay informed about emerging attack standardized reporting, and facilitates
vectors and reinforces proactive security benchmarking against industry best
behavior. By involving the entire workforce, practices. Strong governance mechanisms
from executives to frontline employees, ensure accountability, incident disclosure,
organizations establish a unified defense and effective resource allocation to mitigate
against social engineering tactics. risks.
Leadership plays a crucial role in shaping Regular security assessments, incident
this culture. When executives prioritize monitoring, and performance tracking
cybersecurity and actively champion training through metrics—such as known
initiatives, it signals the importance of vulnerabilities and training completion
security as part of the broader business rates—provide actionable insights that
strategy. This top-down approach not drive timely adjustments. Governance
only protects sensitive data but also structures that evaluate AI-related risks,
builds customer trust and solidifies the adversarial threats, and ethical concerns
organization’s long-term success. position organizations to address emerging
vulnerabilities before they escalate.
Securing Remote and Hybrid Work By integrating cybersecurity governance
Environments into the organization’s core, businesses not
only enhance regulatory compliance but
As remote and hybrid work models expand also foster resilience against increasingly
the attack surface, organizations must sophisticated threats. This holistic approach
secure the technologies that support ensures that cybersecurity measures
these environments. Conducting regular align with broader business objectives,
vulnerability assessments, enforcing timely empowering the organization to navigate
patching, and strengthening remote access and thrive in a complex digital landscape.
solutions are essential steps. High-profile
incidents, such as the MOVEit Transfer
vulnerabilities, underscore the critical need
for ongoing vigilance in securing internet-
facing systems and remote infrastructure.
40 DIGITAL THREAT REPORT 2024

STRENGTHENING CYBERSECURITY THROUGH
PROACTIVE PROCESSES AND LAYERED DEFENSES
Effective cybersecurity relies on processes that not only anticipate threats but also
build resilience through continuous monitoring, adaptive defense strategies, and
structured responses.
By embedding dynamic processes, organizations can minimize vulnerabilities,
streamline detection, and respond swiftly to emerging threats.
Accelerated Vulnerability  Defense-in-Depth as a Strategic  Zero Trust Architecture (ZTA) for
| Assessments | Imperative | Modern Threats |
| ----------- | ---------- | -------------- |
In today’s rapidly evolving threat landscape,  No single solution can fully protect against  The traditional network perimeter is no
waiting for quarterly or annual vulnerability  modern cyber threats. Defense-in-Depth  longer sufficient as remote work, cloud
assessments is no longer sufficient.  offers a layered strategy where multiple  services, and mobile devices expand the
Conducting daily or weekly assessments  controls—firewalls, intrusion prevention,  attack surface. Zero Trust Architecture (ZTA)
using automated solutions is essential to  and endpoint detection—work in tandem  enforces continuous authentication, granular
identify and mitigate weaknesses before  to detect, delay, or mitigate attacks.  access control, and micro-segmentation to
attackers exploit them. The time between  This holistic framework extends beyond  safeguard sensitive assets. By assuming that
vulnerability disclosure and exploitation  technology, incorporating policies and  no user or device can be implicitly trusted,
has drastically shortened, making real- procedures that reinforce organizational  ZTA reduces lateral movement and limits
time scanning a critical component of  resilience. Endpoint Detection and  the damage potential of compromised
organizational security. Automated tools  Response (EDR) tools play a pivotal role  credentials or insider threats.
| ensure systems are continuously monitored,  | in addressing AI-driven and customized  |     |
| ------------------------------------------- | --------------------------------------- | --- |
allowing teams to prioritize remediation and  malware threats, bridging the gap left by  Proactive processes form the backbone
close security gaps swiftly. traditional antivirus solutions. This layered  of a resilient cybersecurity strategy. By
|     | approach creates redundancies, ensuring        | accelerating assessments, embedding        |
| --- | ---------------------------------------------- | ------------------------------------------ |
|     | that even if one control fails, others remain  | intelligence, deploying layered defenses,  |
Threat Intelligence Integration
|     | active to contain breaches. | and implementing Zero Trust, organizations  |
| --- | --------------------------- | ------------------------------------------- |
can build robust frameworks that withstand
| As adversaries grow more sophisticated,  |     | evolving threats. |
| ---------------------------------------- | --- | ----------------- |
Comprehensive Incident
the integration of threat intelligence into
| monitoring processes is crucial. Threat  | Response Playbooks |     |
| ---------------------------------------- | ------------------ | --- |
actors often share tools and vulnerabilities,
| necessitating collective action and           | Preparedness is critical. Standardized        |     |
| --------------------------------------------- | --------------------------------------------- | --- |
| intelligence sharing. Organizations must      | playbooks for responding to diverse cyber     |     |
| incorporate reputable threat feeds (such as   | incidents ensure that teams act quickly,      |     |
| from CERT-In) into their security frameworks  | uniformly for the type of incident and        |     |
| to proactively detect attack patterns. This   | decisively. These playbooks guide analysis,   |     |
| intelligence-driven approach enables faster   | containment, and mitigation, reducing the     |     |
| response times and anticipates threats        | chance of oversight during critical moments.  |     |
| based on evolving tactics, strengthening      | By establishing predefined response           |     |
| defenses across the board. By fostering       | protocols, organizations can streamline       |     |
| collaboration between vendors, enterprises,   | investigations, minimizing operational        |     |
| and industry peers, organizations create      | disruptions and financial losses.             |     |
a unified defense that mirrors the
interconnected strategies used by threat
actors.
41 DIGITAL THREAT REPORT 2024

TECHNOLOGY: BUILDING RESILIENT CYBER DEFENSES
Accelerate Patching of Network Application and API Security Securing AI-Native Applications
Devices
APIs represent a critical attack vector, APIs within AI-native applications are often
Network devices are prime targets for especially in AI-native and payments overlooked during development. API
attackers, with vulnerabilities in firewalls ecosystems. To mitigate threats: security testing must be embedded early
and VPNs surging by 229% in the past year. • Secure APIs with strong authentication in the Software Development Lifecycle
Zero-day exploits are being weaponized (OAuth, JWT, API keys) and enforce IP (SDLC) to uncover hidden vulnerabilities.
faster, with some attacks launched within whitelisting. By expanding Dynamic Application Security
hours of disclosure. To stay ahead, • Use server-to-server validation to Testing (DAST) to cover API endpoints,
organizations must aggressively patch safeguard sensitive transactions, avoiding organizations address gaps that traditional
network devices on a continuous basis, browser redirects. scanning might miss. Proactive testing
reducing exposure and closing critical • Implement CORS (Cross-Origin against OWASP Top 10 API vulnerabilities
gaps before exploitation occurs. This Resource Sharing) restrictions to prevent ensures AI systems are protected at scale.
proactive stance is essential to safeguard unauthorized domains from accessing
infrastructure from evolving AI-powered APIs. Through a layered technological defense,
attack techniques. organizations can reduce exploitable
By locking down API access and restricting weaknesses, safeguard sensitive operations,
sensitive documentation, organizations can and stay resilient in the face of rapidly
AI-Driven Anomaly Detection and reduce risks of API-driven data breaches and evolving cyber threats.
Dark Web Monitoring unauthorized system interactions.
Traditional security tools fall short against
stealthy, adaptive threats. AI-powered Endpoint and Email Security
anomaly detection continuously monitors
for irregular behaviors that evade standard Endpoints remain a primary entry point
defenses. These systems can identify subtle for phishing and ransomware. Application
deviations in user behavior, pinpointing whitelisting should be enforced to block
malicious activities hidden within normal unauthorized software, while robust email
operations. Simultaneously, dark web and web filters intercept phishing attempts
monitoring ensures early detection of and malicious advertisements. Keeping
compromised credentials, allowing antivirus solutions updated and restricting
organizations to enforce rapid password unnecessary remote-access tools further
resets and mitigate potential breaches strengthens endpoint defenses. Limiting
before they escalate. exposure at this level reduces the likelihood
of breaches escalating across the network.
Strengthen Authentication and
Access Control
Multi-Factor Authentication (MFA) must
be enforced across all sensitive financial
operations (e.g., NEFT/RTGS). This ensures
robust identity verification and mitigates
insider threats. Strict access control lists
should be maintained and regularly
reviewed to prevent overprovisioned
accounts. Applying the principle of least
privilege reduces unnecessary access,
narrowing the attack surface and minimizing
potential damage from compromised
accounts.
42 DIGITAL THREAT REPORT 2024

CONCLUSION
CONCLUSION
43 DIGITAL THREAT REPORT 2024
43 DIGITAL THREAT REPORT 2024

CONCLUSION
And with that, CERT-In, CSIRT-Fin and interconnected systems, requires constant
SISA wrap up this year’s journey through vigilance and adaptability to protect against
the shifting sands of the cybersecurity emerging risks.
landscape. We hope this report has
provided you with meaningful insights, We hope this report serves as a valuable
actionable takeaways, and maybe even resource in helping you identify potential
a fresh perspective on the challenges we vulnerabilities, prepare for the unexpected,
collectively face. and prioritize investments in your
cybersecurity strategies. At the heart of this
The BFSI industry stands at a unique effort is the shared goal of building a secure
intersection of opportunity and risk. As digital society—one that safeguards trust,
non-cash transactions continue to grow at innovation, and growth.
an extraordinary pace, fueled by the shift
to e-commerce and the digitization of B2B We want to extend our heartfelt thanks
payments, the sector is transforming into to the many contributors who helped
an increasingly complex ecosystem. While bring this report to life, from data partners
these advancements open new doors for to researchers, whose expertise and
innovation and customer engagement, they collaboration made it possible. And to you,
also present attractive targets for cyber our readers, thank you for your continued
adversaries seeking to exploit vulnerabilities engagement, feedback, and commitment to
for gain. advancing cybersecurity.
The journey to secure this ecosystem is far The road ahead will undoubtedly be filled
from over. Threats are constantly evolving, with challenges, but with the right insights,
and as technology advances, so do the preparation, and dedication, it’s a road we
tactics and motives of those seeking to can navigate together. Here’s to building a
disrupt it. The digital payments sector, with safer and more secure future for all.
its immense value and increasing reliance on
ACKNOWLEDGEMENTS
We express our deepest gratitude to our Team for the Indian Financial Sector) and
customers and partners, whose trust and CERT-In (Indian Computer emergency
collaboration are the cornerstone of our Response Team), whose contributions have
efforts. Engaging with them not only helps been instrumental in the creation of this
us exchange knowledge but also drives our report. Their ability to synthesize findings,
continuous growth and learning. Together, provide insights, and bring this analysis to
we share a vision of building a more secure life underscores the incredible talent, depth
and resilient digital ecosystem. and dedication within the respective teams.
A huge thanks to SISA’ites, officers of CSIRT-
Fin (Computer Security Incident Response
This report is a product of collective effort, collaboration,
and shared commitment to cybersecurity, and we are
immensely grateful to everyone who made it possible.
44 DIGITAL THREAT REPORT 2024

REFERENCES
1. https://www.ibm.com/reports/data-breach
2. https://www.business-standard.com/finance/news/average-cost-of-data-breaches-in-
india-hits-2-18-million-rbi-report-124072900610_1.html
3. https://www.financialexpress.com/life/technology-phishing-attacks-on-financial-sectors-
soar-in-india-increasing-by-175-in-2024-report-3669276/
4. SISA Forensics Investigations
5. SISA Forensics Investigations
6. Verizon DBIR 2024: Five Compelling Stats
7. https://cointelegraph.com/news/engineer-hacks-trezor-wallet-recovers-2m-in-lost-crypto
8. https://panaseer.com/resources/reports/2022-security-leaders-peer-report
https://www.sharefile.com/resource/blogs/cybersecurity-trends
https://www.beyondtrust.com/blog/entry/beyondtrust-cybersecurity-trend-predictions
https://blog.shi.com/cybersecurity/are-you-protected-2025s-top-cybersecurity-trends-and-strategies-to-follow-now/
https://medium.com/@DataFlowX/the-future-of-cybersecurity-predictions-and-trends-for-2025-21e95173d1e9
https://www.pwc.com/gx/en/tmt/5g/pwc-securing-5gs-future.pdf
https://www.sharefile.com/resource/blogs/cybersecurity-trends
https://www.beyondtrust.com/blog/entry/beyondtrust-cybersecurity-trend-predictions
https://blog.checkpoint.com/security/2025-cyber-security-predictions-the-rise-of-ai-driven-attacks-quantum-threats-and-social-media-
exploitation/
https://www.weforum.org/stories/2024/10/cyber-resilience-emerging-technology-ai-cybersecurity/
https://www.forbes.com/councils/forbestechcouncil/2024/07/11/the-future-of-cybersecurity-emerging-threats-and-how-to-combat-them/
https://blog.checkpoint.com/research/ransomwares-evolving-threat-the-rise-of-ransomhub-decline-of-lockbit-and-the-new-era-of-data-
extortion/
https://www.scworld.com/news/north-korean-nation-state-threat-actor-using-play-ransomware
https://www.datacenterknowledge.com/data-storage/evolving-ransomware-threats-why-offline-storage-is-essential-for-modern-data-
protection
https://www.scmr.com/article/regulations-are-forcing-organizations-to-address-software-supply-chain-security/procurement
https://cybersecurityventures.com/software-supply-chain-attacks-to-cost-the-world-60-billion-by-2025/
https://www.scmr.com/article/supply-chain-cyberattacks
https://venturebeat.com/security/forresters-ciso-budget-priorities-for-2025-focus-on-api-supply-chain-security/
https://cybersecurity-magazine.com/why-are-supply-chain-attacks-increasing/
https://www.infosecurityeurope.com/en-gb/blog/threat-vectors/supply-chain-attacks-cyber-threat.html
https://fintechmagazine.com/articles/why-the-finance-sector-grapples-with-software-security-debt
https://hbr.org/2024/10/phishing-attacks-are-evolving-heres-how-to-resist-them
https://flashpoint.io/blog/russian-apt-groups-cyber-threats/
https://www.thisdaylive.com/index.php/2024/09/26/top-vulnerabilities-in-iot-devices-what-hackers-target-how-to-defend-against-them/
https://www.zscaler.com/press/zscaler-threatlabz-finds-400-increase-iot-and-ot-malware-attacks-year-over-year-underscoring
https://www.paymentsjournal.com/asia-overtakes-north-america-as-leading-crypto-development-hub/
https://www.statista.com/statistics/1393453/crypto-payments-global-market-size/
https://www.darkreading.com/cyberattacks-data-breaches/cryptocurrency-attacks-quadrupled-cybercriminals-cash-in
https://www.thomsonreuters.com/en-us/posts/government/identity-theft-drivers/
https://venturebeat.com/security/how-ai-driven-identity-attacks-are-defining-the-new-threatscape/
https://www.scworld.com/resource/why-identity-has-become-a-trojan-horse-and-what-to-do-about-it
https://www.techbusinessnews.com.au/blog/ai-driven-cyber attacks-the-alarming-surge/
https://www.londondaily.news/unlocking-the-potential-of-5g-technology-opportunities-and-challenges-ahead/
https://www.techradar.com/pro/the-rise-of-identity-related-cyberattacks-costs-challenges-and-the-role-of-ai
https://www.techmagic.co/blog/ai-in-cybersecurity
https://www.micromindercs.com/blog/ai-threat-intelligence-empowering-cybersecurity
https://securityintelligence.com/articles/3-proven-use-cases-for-ai-preventative-cybersecurity/
https://www.intelligentcio.com/eu/2024/04/22/the-role-of-cybersecurity-in-securing-critical-infrastructure/
45 DIGITAL THREAT REPORT 2024

REFERENCES
https://www.auditboard.com/blog/security-vs-compliance/
https://www.tripwire.com/state-of-security/compliance-vs-security-striking-right-balance-cybersecurity
https://www.scrut.io/post/how-to-prevent-cyberattacks-by-balancing-security-and-compliance
https://www.securitymagazine.com/articles/99259-compliance-and-security-are-two-sides-of-the-same-coin
https://www.tripwire.com/resources/guides/mind-the-cybersecurity-compliance-gap
https://www.csoonline.com/article/1309993/grc-impact-and-challenges-to-cybersecurity.html
https://www.mckinsey.com/industries/financial-services/our-insights/global-payments-in-2024-simpler-interfaces-complex-reality
https://cxotoday.com/interviews/turning-data-breaches-into-opportunities-strategies-for-indian-businesses-to-strengthen-cybersecurity-and-
reduce-risks/
https://www.scworld.com/resource/building-cybersecurity-resilience-strategies-technologies-and-best-practices-from-industry-leaders
https://www.techtarget.com/searchsecurity/tip/5-tips-for-building-a-cybersecurity-culture-at-your-company
https://www.weforum.org/stories/2024/04/cybersecurity-key-strategies-cyber-resilience-2024/
https://www.techtarget.com/searchsecurity/feature/Security-posture-management-a-huge-challenge-for-IT-pros
https://www.techtarget.com/healthtechsecurity/feature/Navigating-cyber-insurance-coverage-as-threats-evolve
https://www.helpnetsecurity.com/2024/07/05/iot-security-privacy-challenges/
https://www.paloaltonetworks.com/cybersecurity-perspectives/how-to-secure-iot-in-financial-services
https://securityintelligence.com/articles/what-are-the-risks-of-the-iot-in-financial-services/
https://www.statista.com/statistics/1183457/iot-connected-devices-worldwide/
46 DIGITAL THREAT REPORT 2024

SISA
SISA is a forensics-driven cybersecurity company solutions provider specializing in
securing the digital payments industry. As a Global Payment Forensic Investigator of the
PCI Security Standards Council, we leverage forensics insights into preventive, detective,
and corrective security solutions, protecting 1,000+ organizations across 40+ countries
from evolving cyberthreats. Our suite of solutions from AI-driven compliance, advanced
security testing, agentic detection/ response and learner focused-training has been
honored with prestigious awards, including from Financial Express, DSCI-NASSCOM and
The Economic Times. With commitment to innovation, and pioneering advancements in
Quantum Security, Hardware Security, and Cybersecurity for AI, SISA is shaping the future
of cybersecurity through cutting-edge forensics research.
CERT-In
CERT-In is the national agency for responding to computer security incidents as and
when they occur. In the Information Technology Amendment Act 2008,CERT-In has
been designated to serve as the national agency to perform the following functions
in the area of cyber security:
• Collection,analysis and dissemination of information on cyber incidents.
• Forecast and alerts of cyber security incidents.
• Emergency measures for handling cyber security incidents.
• Coordination of cyber incident response activities.
• Issue guidelines,advisories,vulnerability notes and whitepapers relating to information
security practices,procedures, prevention,response and reporting of cyber incidents.
• Such other functions relating to cyber security as may be prescribed
Refer www.cert-in.org.in for more details
CSIRT-Fin
Computer Security Incident Response Team in Finance sector (CSIRT-Fin) , is a
nodal sectoral CSIRT which provides Incident Prevention and Response services
as well as Security Quality Management Services to the entities of the Indian
financial sector. It manages cyber incidents and coordinate responses across
banking, securities market infrastructure, insurance, and pension funds entities.
It carries out the following roles related to the cyber security in financial sector:
i. Collection, analysis & dissemination of information on cyber incidents.
ii. Forecast and alerts on cyber security incidents.
iii. Emergency measures on cyber security incidents.
iv. Coordination for cyber incident response activities.
v. Issue guidelines, advisories, vulnerability, and white papers relating to
information security.
vi. Monitor sectoral efforts in the financial sector towards maintaining
dynamic and modern cyber security architecture, developing awareness
amongst regulated entities and public in general.
vii.Such other functions relating to cyber security in the financial sector, as may
be prescribed.
47 DIGITAL THREAT REPORT 2024

48 DIGITAL THREAT REPORT 2024