# The State of Cybersecurity in the Finance Sector

darktrace.com © 2025 Darktrace Holdings Limited. All rights reserved.

## Disclaimer

This report is for informational purposes only. While every effort has been made to ensure the accuracy and completeness of the findings, the conclusions are based on the available data at the time, which may be subject to change. The information does not constitute legal, financial, or professional advice, and readers should consult relevant experts for specific guidance.

The views expressed in this report are those of the authors and do not necessarily reflect the views of any specific organization or governmental entity. The report does not guarantee the security of any systems, and ongoing vigilance and adaptive strategies are required to address emerging threats.

This report is provided “as is,” without warranties or representations, express or implied, regarding the accuracy or completeness of this report, and Darktrace will not be liable for any damages or losses arising from the use or reliance on the content.

## Table of Contents
- [Acknowledgements](#acknowledgements)
- [Executive summary](#executive-summary)
- [Objectives and Methodology](#objectives-and-methodology)
- [Threat Landscape Overview](#threat-landscape-overview)
- [Protocol & Infrastructure Targeting](#protocol--infrastructure-targeting)
- [Threat Actor Spotlights](#threat-actor-spotlights)
- [Current DPRK-Linked Campaign Targeting the Finance Sector](#current-dprk-linked-campaign-targeting-the-finance-sector)
- [Conclusion](#conclusion)
- [Appendices](#appendices)

---

## Acknowledgements

**Authors:**
Calum Hall, Hugh Turnbull, Parvatha Ananthakannan, Tiana Kelly, and Vivek Rajan

**Thank you to the following contributors:**
Emma Foulger, Nathaniel Jones, Nicole Wong, Ryan Traill, Tara Gould, and the Darktrace Threat Research and Incident Management teams.

**And a special thank you to:**
Michael Cannizzo – Chief Information Security Officer, HEDGESERV; Peter Fiveash – Chief Operating Officer, Hosking Partners; Will Miller – Chief Compliance Officer, Hosking Partners, and others who wish to remain anonymous.

---

## Executive summary

The financial sector, encompassing commercial banks, credit unions, financial services providers, and cryptocurrency platforms, faces an increasingly complex and aggressive cyber threat landscape.

This report provides an overview of the evolving risks to confidentiality, integrity, and availability within financial institutions, drawing on expert interviews, threat intelligence, and telemetry from real-world customer environments.

Cyber threat actors are exploiting vulnerabilities in edge infrastructure, cloud environments, and legacy systems to gain initial access. Attack vectors such as phishing, credential harvesting, and exploitation of virtual private networks (VPNs) and remote access gateways remain prevalent.

Notably, adversary-in-the-middle (AiTM) and QR code phishing techniques have emerged as sophisticated methods to bypass multi-factor authentication (MFA) and evade detection.

Insights from CISOs reveal operational challenges in managing cloud complexity and insider risk stemming from gaps in workforce cybersecurity awareness. The rapid adoption of AI, often without adequate governance, has introduced new risks, while budget constraints and boardroom dynamics continue to hinder proactive security investment.

Threat actor groups such as Cl0p, Lazarus Group, and RansomHub have demonstrated advanced capabilities in ransomware deployment, data exfiltration, and supply chain compromise. Their campaigns have targeted financial institutions with tailored payloads and extortion tactics, often exploiting trusted infrastructure and third-party software.

Darktrace’s Threat Research team identified routine scanning of internet-facing file transfer systems in financial institutions, with indicators of Denial-of-Service (DoS) attempts against Fortra GoAnywhere MFT.

Previous research also confirmed Democratic People’s Republic of Korea (DPRK)-linked malware activity in the sector. These findings show ongoing targeting of exposed infrastructure and the presence of state-sponsored threats.

As financial institutions continue to digitize and expand globally, the need for resilient, adaptive cybersecurity strategies is more urgent than ever.

Cross-sector collaboration, investment in AI-driven defense, and a renewed focus on governance and training are essential to safeguarding the financial ecosystem in the face of escalating cyber risk.

---

## Objectives and Methodology

This research analyzes the evolving threat landscape facing the financial sector. The majority of institutions analyzed in this report are commercial banks, credit unions, and financial services providers.

Central banks were also included, but they only account for a small number of cases due to their typically robust and mature security posture, which puts off most financially motivated and opportunistic attackers. Financial organizations involved in cryptocurrency trading, custody, or infrastructure were also included, given their increasing exposure in cyber space.

Darktrace models leverage anomaly detection and integrate outputs from Darktrace Deep Packet Inspection (DPI), telemetry inputs, and additional modules to create tailored threat detection. Darktrace applies Self-Learning AI to an organization’s data to understand and identify anomalies specific to that environment.

This research leverages insights gained from Darktrace’s model alerts, which trigger when observed activity is deemed to be anomalous. Each alert contains metadata such as timestamps, source and destination IP addresses, and the protocols used.

The threat landscape research in this report is organized according to the principles of the CIA triad: Confidentiality, Integrity, and Availability. The CIA triad is a foundational model in information security that defines three core objectives for protecting data and systems: ensuring that sensitive information remains private (Confidentiality), maintaining the accuracy and trustworthiness of data (Integrity), and guaranteeing that systems and information are accessible when needed (Availability) [2].

### Objectives
- Identify the most significant cyber threats impacting the financial sector, including those linked to digital transformation such as cloud adoption and cryptocurrency.
- Examine commonly exploited initial access vectors and attack surfaces exposed by financial institutions during modernization efforts.
- Analyze the motivations and tactics of both state-sponsored actors (e.g., DPRK campaigns targeting cryptocurrency) and financially motivated threat groups.
- Contextualize findings with insights from expert interviews and real-world Darktrace telemetry to understand evolving risks.

### Methodology
This research draws on a combination of:
- **Darktrace Telemetry**: Anonymized alert metadata and incident data from financial sector customer deployments with a focus on the United Kingdom and United States.
- **Open-Source Intelligence (OSINT)**: Including threat intelligence reports, government advisories, and public disclosures of cyber incidents.

Threat actor behaviors were analyzed using established frameworks, including:
- **The Diamond Model of Intrusion Analysis**: A conceptual model that represents cyber intrusions through four interconnected components: adversary, capability, infrastructure, and victim. It emphasizes understanding relationships between these elements to reveal attacker intent, capabilities, and operational patterns [1].
- **Hypothesis-Driven Threat Hunting**: A proactive methodology where analysts form hypotheses about potential threats based on intelligence, patterns, and anomalies. These hypotheses guide structured investigations, enabling researchers to uncover hidden threats that traditional detection methods might miss.
- **Behavioral-Based Analysis**: An approach focused on identifying behaviors and tactics rather than static indicators like signatures or hashes. It examines attacker tactics, techniques, and procedures (TTPs), and anomalies in system or network activity to detect evolving threats and sophisticated adversaries.

---

## Threat Landscape Overview

> CISO Insights: “No one really knows what to prepare for until it happens. That’s a challenge for us because we aren’t as large as JP Morgan. We rely on our peer group to understand general preparation strategies. Organizations often struggle to anticipate the full range of potential crises. The complexity of modern financial services means threats can emerge from unexpected directions—cyber incidents, market volatility, regulatory changes, supply chain failures, or even geopolitical events. Smaller firms may lack the resources to model every scenario, making it difficult to know what to prepare for until a crisis actually unfolds” - Will Miller, Chief Compliance Officer, Asset Mgmt. Fund.

### Confidentiality
Confidentiality remains a primary concern for financial institutions, as attackers increasingly target sensitive customer data, financial records, and internal communications. The financial sector’s reliance on digital infrastructure and its role in managing high-value transactions make it a prime target for both financially motivated and state-sponsored threat actors.

#### Data Theft and Exfiltration
Data breaches in the financial sector often involve the theft of personally identifiable information (PII), account credentials, and financial transaction data. In many cases, attackers exploit unpatched vulnerabilities or use stolen credentials to gain unauthorized access to internal systems. Once inside, they exfiltrate data for resale on dark web markets or use it to facilitate further attacks such as fraud or identity theft.
- In the UK, ransomware campaigns increasingly prioritize data theft and extortion over encryption-only attacks, reflecting a broader trend identified by the National Cyber Security Centre (NCSC) and National Crime Agency (NCA) in their joint ransomware threat assessment [3].
- In the US, financial institutions have been disproportionately targeted, with attackers leveraging data exfiltration as a primary extortion tactic [4].

Compliance issues remain a persistent risk, with the size of financial sector organizations leading data loss prevention (DLP) to be an inherent challenge.

- **214,000**: In October alone, Darktrace observed over 214,000 emails across financial sector customers which contained unfamiliar attachments and were sent to users’ suspected personal addresses.
- **351,000**: Across the same set of customers, more than 351,000 emails containing unfamiliar attachments were sent to freemail addresses in October, highlighting clear concerns around DLP.

> CISO Insights: “From a regulatory standpoint, the SEC appears to be spending more time on cybersecurity and AI. However, there’s little detail or explanation provided. It’s similar to the UK—regulators are trying to cover too much and set expectations without fully understanding the landscape, and it feels too early in the process.” - Will Miller, Chief Compliance Officer, Asset Mgmt. Fund.

#### Phishing and Credential Harvesting
Phishing continues to be a leading initial access vector for attacks targeting confidentiality. Financial institutions are frequently targeted with phishing emails designed to harvest login credentials. Darktrace has observed the following techniques in the wild:

- **AiTM (Adversary-in-the-Middle)**: AiTM techniques are increasingly used in phishing campaigns to bypass MFA [9], making them one of the most concerning developments in credential theft. In AiTM attacks, threat actors intercept login sessions by deploying reverse proxies that capture both credentials and session cookies. This allows them to impersonate users even when MFA is enabled, effectively rendering traditional authentication methods ineffective.
- **QR code phishing (“Quishing”)**: A tactic used to evade email security filters. Attackers embed malicious QR codes into emails, documents, or even physical materials, which redirect victims to spoofed websites designed to harvest credentials or install malware [10]. In Darktrace’s 2025 Mid-Year Review it was reported that over 1 million QR code-based phishing emails were detected in February 2025 alone [11].

**Almost 2,400,000 PHISHING EMAILS** observed by Darktrace within financial sector customer deployments in the first half of 2025.

#### Business Email Compromise (BEC)
BEC remains one of the most financially damaging cyber threats, with global losses reported between 2013 and 2023 exceeding $55 billion [5]. These attacks exploit trusted relationships between employees, executives, and third-party vendors to redirect payments or steal sensitive information. The FBI reported over $2.7 billion [6] in BEC-related losses in 2024, with financial institutions among the most affected.

Attackers increasingly use AI-generated content to craft convincing phishing emails that mimic internal communications, making detection more difficult. Darktrace’s Annual 2024 Threat Report found that 32% of phishing attacks in 2024 used novel social engineering techniques, such as AI-generated text [7]. Darktrace’s own CEO, Jill Popelka, was targeted by this technology with an AI clone of her own voice during a board meeting [8].

> CISO insights: One CISO interviewed noted that AI-driven phishing emails now exhibit improved grammar and realism, reducing the effectiveness of traditional phishing training and simulations.

#### Case Study: Business Email Compromise
Almost 30% of all phishing emails across financial sector customer deployments were targeted towards VIP users. Not all phishing attacks targeting the financial sector had an immediate financial gain as an objective. Darktrace’s research also observed phishing emails containing malicious links as the initial entry point into customer networks.

In one case study from late 2024, a phishing link was opened by an employee of a finance company, allowing the threat actor to continue through further stages of the Cyber Kill Chain. The attack began when a sophisticated phishing email sent from a compromised domain known to the victim was received by a VIP user within a bank. The email contained a link to a PDF hosted in Google Drive, which included a link to download a malicious .RAR file. When downloaded and opened, the .RAR file deployed malware onto the VIP user’s computer.

The average amount requested in BEC wire fraud rose by 46% globally between December 2024 and early 2025, reflecting the growing financial impact of these attacks [12].

---

### Integrity
Integrity refers to the accuracy, consistency, and trustworthiness of data and systems. Threats to integrity can undermine confidence in financial transactions, compromise internal controls, and enable fraud or unauthorized access.

> CISO insights: One CISO reported a rise in phishing attacks leveraging AI for improved realism and highlighted cultural challenges among new hires who underestimate the impact of cyber incidents.

#### Credential Misuse and Account Takeover
The misuse of valid credentials remains a significant threat to the integrity of financial systems. Attackers often obtain credentials through phishing, brute-force attacks, or data breaches, before using them to impersonate legitimate users. In one 2023 incident, compromised administrator credentials were used to deploy PsExec and other lateral movement tools, ultimately leading to ransomware deployment on a DNS server [13].

#### Trojan Malware and Data Manipulation
Trojan malware continues to be a key tool for attackers seeking to compromise the integrity of financial systems:
- **BeaverTail**: A JavaScript-based stealer linked to DPRK threat actors, used to exfiltrate browser credentials and cryptocurrency wallet data.
- **Zloader**: A modular banking trojan used to disable security tools and inject malicious code into applications [16].
- **WarmCookie**: A backdoor observed capturing screenshots, executing commands, and delivering additional malware payloads [17].

#### Insider Threats and Social Engineering
Insider threats, whether malicious or unintentional, pose a persistent risk to data integrity. Social engineering campaigns have exploited job-seeking employees by posing as recruiters, tricking them into downloading malware-laden applications [18].

> CISO Insights: “For us, AI’s impact is all about data stewardship. Guardrails on proprietary and client data are essential to protect our financial models, performance metrics, and confidential client information. We enforce strict controls on data, devices, and personnel awareness. We restrict use of AI for transcription or recording because we know that data could be exposed to large language models (LLMs). We’re still assessing and imposing restrictions. Ultimately, it’s all about safeguarding the data.” - Will Miller, Chief Compliance Officer, Asset Mgmt. Fund.

---

### Availability
Availability refers to the ability of financial institutions to maintain uninterrupted access to critical systems, services, and data.

#### Ransomware and System Lockouts
Ransomware remains the most prominent threat to availability. In the US, ransomware attacks on financial institutions accounted for nearly 64% of all incidents in 2023 [20]. In the UK, ransomware incidents reported to the Financial Conduct Authority (FCA) rose sharply, accounting for 31% of all cyber incidents in H1 2023 [22].

> CISO Insights: “Crisis management planning is critical—what happens when a service fails? For example, if a key system goes down, we only have one backup. Consider cloud outages: if Bloomberg goes down because Azure fails on the East Coast, that creates a massive impact. Suddenly, we can’t access the market, which affects our ability to make money. Third-party providers, data accessibility, disaster recovery, and COOP (Continuity of Operations) are essential concepts.” - Will Miller, Chief Compliance Officer, Asset Mgmt. Fund.

#### Distributed Denial of Service (DDoS) Attacks
DDoS attacks remain a persistent threat, often used as smokescreens to distract security teams while other malicious activities, such as data exfiltration or credential theft, are carried out.

#### Exploitation of Edge Infrastructure
Edge infrastructure, including VPNs, firewalls, and remote access gateways, continues to be a well-utilized entry point. In December 2025, Darktrace’s threat research team investigated a major campaign exploiting vulnerabilities in Palo Alto firewall devices (CVE 2024-0012 and 2024-9474). Additionally, in August 2025, Darktrace saw active exploitation of Ivanti EPMM vulnerabilities (CVE-2025-4427 and CVE-2025-4428).

---

## Protocol & Infrastructure Targeting

> CISO insights: Interview feedback highlighted gaps in Microsoft Conditional Access policies, which do not apply to command-line interfaces or scripts, leaving ADFS and Office 365 logins exposed.

### Commonly Exploited Protocols
- **Server Message Block (SMB)**: Used for lateral movement and ransomware deployment.
- **Domain Name System (DNS) Tunneling**: Used for covert command-and-control (C2) and data exfiltration.
- **RDP**: Frequently used for lateral movement and privilege escalation.
- **Kerberos (Kerberoasting)**: Attackers extract service account hashes from Kerberos tickets and attempt offline cracking.

### Third-Party Software Risks
Supply chain vulnerabilities in widely used third-party applications have become a major vector for initial access and data exfiltration.
- **File Transfer Platforms**: Threat actors have targeted enterprise file transfer solutions such as MOVEit and GoAnywhere, exploiting flaws that allowed unauthorized access and remote command execution [26].
- **Webshell Deployment**: Attackers have deployed web shells within vulnerable file transfer systems to maintain persistent access.

![Figure 01: Suspected pre-CVE detection of the GoAnywhere MFT vulnerability, as seen in the Darktrace platform]

---

## Threat Actor Spotlights

### Lazarus Group
The Lazarus Group is a DPRK state-sponsored APT known for its dual focus on cyber espionage and financial theft.
- **Notable Campaigns**: BeaverTail malware deployment via fake job interviews; Flash loan exploit on a UK lending protocol (2023).
- **Tactics**: Social engineering, trojanized applications, credential theft, and LOTL (Living-off-the-land) techniques.

#### Malware Deep Dive: BeaverTail
BeaverTail is a JavaScript-based information stealer and malware loader.
- **Delivery**: Trojanized npm packages, fake job interview platforms, and ClickFix social engineering.
- **Capabilities**: Cross-platform support, keylogging, screenshot capture, and clipboard monitoring.
- **Recent Evolution**: Merged with OtterCookie; leverages blockchain-based C2 infrastructure (EtherHiding).

### Cl0p Ransomware
A financially motivated group known for aggressive extortion tactics and exploitation of zero-day vulnerabilities in enterprise software.
- **Notable Campaigns**: MOVEit Transfer exploitation (2023) and Cleo File Transfer attacks (2024).

### RansomHub & LockBit
RansomHub emerged following the disruption of LockBit. They operate under a RaaS model, targeting high-value institutions with low tolerance for downtime.

---

## Current DPRK-Linked Campaign Targeting the Finance Sector

Darktrace detected multiple coordinated attempts targeting the finance industry as recent as December 8, 2025. Targets included organizations in the cryptocurrency, fintech, and gambling sectors across the UK, Sweden, Portugal, Spain, Chile, Kenya, and Nigeria.

### Case One: UK Financial Organization Compromised via Likely Malicious npm Package
The attack likely originated from a malicious npm package. The malware deployed included **Beavertail** (infostealer) and **Tsunami Injector** (loading Tsunami modules for session hijacking and cookie exfiltration).

### Case Two: React2Shell Exploitation Across Multiple Targets
Attackers exploited **React2Shell (CVE-2025-55182)**, a pre-authentication remote code execution vulnerability. The payload, **EtherRAT**, uses Ethereum smart contracts for C2 resolution, polling every 500ms.

---

## Conclusion

The financial sector remains a cornerstone of global economic stability and a prime target for both financially motivated and state-sponsored cyber adversaries. Rapid digital transformation has expanded the attack surface, introducing new vulnerabilities in edge infrastructure, identity systems, and third-party ecosystems.

AI is emerging as a critical component of defense, enabling anomaly detection and automated response at scale. At the same time, its ungoverned adoption poses significant risks. Collaboration across sectors is essential to share intelligence, strengthen identity controls, and accelerate patch management.

---

## Appendices

### Indicators of Compromise (IoCs)
- http://5.180[.]24[.]17:1244
- 3dfb3c49d5430a32da442178965b188a – next-preconfig-1.0.0.flatten.js
- 23.227.202[.]52:1224 /brow/5/504
- brow5_504.py
- proxy1.ip2worlds[.]
- wet4g13ncu255d[.]icu
- lnzafqrdnkbqligzetxljqgnsp5eb32wh.oast.fun
- 193.24.123[.]68:3001
- gfdsgsdfhfsd_ghsfdgsfdgsdfg.sh
- 91.215.85[.]42:3000/api/reobf/3481534f-07db-4e32-bf0e-df8ba7510211
- d5725519d9e66bc590ac54c11d1d90e5

### Bibliography
[^1]: [Online]. Available: https://www.threatintel.academy/wp-content/uploads/2020/07/diamond_summary.pdf.
[^2]: [Online]. Available: https://www.nccoe.nist.gov/publication/1800-26/VolA/index.html.
[^3]: [Online]. Available: https://www.ncsc.gov.uk/pdfs/whitepaper/ransomware-extortion-and-the-cyber-crime-ecosystem.pdf.
[^4]: [Online]. Available: https://www.csoonline.com/article/4032874/ransomware-attacks-the-evolving-extortion-threat-to-us-financial-institutions.html.
[^5]: [Online]. Available: https://www.fbi.gov/how-we-can-help-you/scams-and-safety/common-frauds-and-scams/business-email-compromise.
[^6]: [Online]. Available: https://www.conduitsecurity.com/blog/2024-ic3-report.
[^7]: [Online]. Available: https://www.darktrace.com/resources/annual-threat-report-2024.
[^8]: [Online]. Available: https://www.thetimes.com/business-money/technology/article/darktrace-boss-i-was-deepfaked-and-i-couldnt-tell-difference-sxzw0nk5z.
[^9]: [Online]. Available: https://www.darktrace.com/blog/a-snake-in-the-net-defending-against-aitm-phishing-threats-and-mamba-2fa.
[^10]: [Online]. Available: https://www.darktrace.com/blog/phishing-with-qr-codes-how-darktrace-detected-and-blocked-the-bait.
[^11]: [Online]. Available: https://www.darktrace.com/blog/2025-cyber-threat-landscape-darktraces-mid-year-review.
[^12]: [Online]. Available: https://www.fortra.com/blog/bec-global-insights-report-january-2025.
[^13]: [Online]. Available: https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/.
[^14]: [Online]. Available: https://malpedia.caad.fkie.fraunhofer.de/details/js.beavertail.
[^15]: [Online]. Available: https://attack.mitre.org/software/S1246/.
[^16]: [Online]. Available: https://www.microsoft.com/en-us/security/blog/2022/04/13/dismantling-zloader-how-malicious-ads-led-to-disabled-security-tools-and-ransomware/.
[^17]: [Online]. Available: https://www.darktrace.com/blog/disarming-the-warmcookie-backdoor-darktraces-oven-ready-solution.
[^18]: [Online]. Available: https://www.darktrace.com/blog/meeten-malware-a-cross-platform-threat-to-crypto-wallets-on-macos-and-windows.
[^19]: [Online]. Available: https://unit42.paloaltonetworks.com/2025-unit-42-global-incident-response-report-social-engineering-edition/.
[^20]: [Online]. Available: https://news.sophos.com/en-us/2023/07/13/the-state-of-ransomware-in-financial-services-2023/.
[^21]: [Online]. Available: https://www.federalreserve.gov/publications/files/cybersecurity-report-202507.pdf.
[^22]: [Online]. Available: https://www.fca.org.uk/freedom-information/information-cyber-attacks-and-data-breaches-reported-fca-october-2023.
[^23]: [Online]. Available: https://www.patelco.org/securityupdate.
[^24]: [Online]. Available: https://www.darktrace.com/blog/darktraces-view-on-operation-lunar-peek-exploitation-of-palo-alto-firewall-devices-cve-2024-2012-and-2024-9474.
[^25]: [Online]. Available: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-317a.

---

regime-backed-programmer-charged-conspiracy-conduct-multiple-cyber-attacks-and.

[63] [Online]. Available: https://www.cyber.gc.ca/en/guidance/profile-ta505-cl0p-ransomware.

[64] [Online]. Available: https://www.cisa.gov/sites/default/files/publications/202103231400_Analyst_Note_CL0P_TLP_WHITE.pdf.

[65] [Online]. Available: https://www.cisa.gov/sites/default/files/publications/202103231400_Analyst_Note_CL0P_TLP_WHITE.pdf.

[66] [Online]. Available: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a.

[67] [Online]. Available: https://www.enisa.europa.eu/sites/default/files/publications/ENISA Threat Landscape 2023.pdf.

23 | The State of Cybersecurity

darktrace.com

[68] [Online]. Available: https://www.cisa.gov/sites/default/files/2023-07/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_8.pdf.

[69] [Online]. Available: https://cybelangel.com/blog/moveit-cl0p-breach/.

[70] [Online]. Available: https://www.darktrace.com/blog/cleo-file-transfer-vulnerability-patch-pitfalls-and-darktraces-detection-of-post-exploitation-activities.

[71] [Online]. Available: https://www.darktrace.com/blog/cleo-file-transfer-vulnerability-patch-pitfalls-and-darktraces-detection-of-post-exploitation-activities.

[72] [Online]. Available: https://www.datastackhub.com/security/clop-ransomware/.

[73] [Online]. Available: https://www.cisa.gov/news-events/news/cisa-and-fbi-release-advisory-cl0p-ransomware-gang-exploiting-moveit-vulnerability.

[74] [Online]. Available: https://www.nationalcrimeagency.gov.uk/the-nca-announces-the-disruption-of-lockbit-with-operation-cronos.

[75] [Online]. Available: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-242a.

[76] [Online]. Available: https://blog.checkpoint.com/research/ransomwares-evolving-threat-the-rise-of-ransomhub-decline-of-lockbit-and-the-new-era-of-data-extortion/.

[77] [Online]. Available: https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/..

[78] [Online]. Available: https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2.

[79] [Online]. Available: https://otx.alienvault.com/indicator/domain/wet4g13ncu255d.icu.

[80] [Online]. Available: https://socket.dev/blog/weaponizing-oast-how-malicious-packages-exploit-npm-pypi-and-rubygems..

[81] [Online]. Available: https://www.sysdig.com/blog/etherrat-dprk-uses-novel-ethereum-implant-in-react2shell-attacks..

[82] [Online]. Available: https://krebsonsecurity.com/2025/02/notorious-malware-spam-host-prospero-moves-to-kaspersky-lab..

[83] [Online]. Available: https://krebsonsecurity.com/2025/02/notorious-malware-spam-host-prospero-moves-to-kaspersky-lab..

darktrace.com

The State of Cybersecurity  | 24

Darktrace is a global leader in AI cybersecurity that keeps organizations ahead of the changing threat landscape every day. Founded in 2013
in Cambridge, UK, Darktrace provides the essential cybersecurity platform to protect organizations from unknown threats using AI that
learns from each business in real-time. Darktrace’s platform and services are supported by 2,700+ employees who protect nearly 10,000
customers globally. To learn more, visit www.darktrace.com.

darktrace.com | info@darktrace.com

© 2025 Darktrace Holdings Limited. All rights reserved.North America: +1 (415) 229 9100Europe: +44 (0) 1223 394 100Asia-Pacific: +65 6804 5010Latin America: +55 11 4949 7696 ·About Darktrace