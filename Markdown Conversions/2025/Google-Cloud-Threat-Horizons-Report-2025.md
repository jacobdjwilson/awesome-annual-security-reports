# Cloud Threat Horizons Report: H2 2025

## Table of Contents
- [Mission Statement](#mission-statement)
- [Executive Summary](#executive-summary)
- [Foundational Security Remains Critical Against Persistent Threats](#foundational-security-remains-critical-against-persistent-threats)
- [Cloud-Native Backup and Recovery for Modern Cyber Threats](#cloud-native-backup-and-recovery-for-modern-cyber-threats)
- [North Korea’s Social Engineering Leading to Cloud Compromises and Cryptocurrency Thefts](#north-koreas-social-engineering-leading-to-cloud-compromises-and-cryptocurrency-thefts)
- [How Decoy Files Turn Trusted Cloud Services into Attack Vectors](#how-decoy-files-turn-trusted-cloud-services-into-attack-vectors)
- [Hardening the Chrome Extension Supply Chain Against Account Compromise](#hardening-the-chrome-extension-supply-chain-against-account-compromise)
- [Contributors](#contributors)

---

## Mission Statement
The Google Cloud Threat Horizons Report provides decision-makers with strategic intelligence on threats to not just Google Cloud, but all cloud service providers. The report focuses on recommendations for mitigating risks and improving cloud security for leaders and practitioners. The report is informed by Google Cloud’s Office of the CISO, Google Threat Intelligence Group (GTIG), Mandiant Consulting, and various Google Cloud intelligence, security, and product teams.

## Executive Summary
### Heightened Cloud Threats: Actors Refine Tactics for Evasion, Persistence, and Supply Chain Compromise

Cloud environments face an increasingly sophisticated threat landscape as actors advance their methods for data exfiltration, identity compromise, and supply chain attacks, while simultaneously improving evasion and persistence techniques. This Google Cloud Threat Horizons Report offers cloud security professionals critical insights into these evolving threats, supported by intelligence and actionable risk mitigations from Google’s security experts.

The dangers of prolonged access, complex recovery scenarios, and supply chain vulnerabilities are not new. Throughout 2025, Google Cloud security and intelligence teams have continued to track these risks. The findings in this report underscore a significant evolution: threat actors are not only honing their tactics for greater impact within cloud environments but are also demonstrating increased sophistication. This sophistication is evident in their targeting of recovery mechanisms, developer ecosystems, and their methods for achieving high-value compromises.

Recognizing our shared responsibility in defending against these advanced cloud threats, this report delivers timely analysis and actionable mitigations, drawing on the following key trends identified by our security and threat intelligence experts:

- **Foundational security remains the strongest defense**: Google Cloud research indicates that credential compromise and misconfiguration remain the primary entry points for threat actors into cloud environments, emphasizing the critical need for robust identity and access management and proactive vulnerability management.
- **Targeting of backup infrastructure**: Financially motivated threat groups are increasingly targeting backup systems as part of their primary objective, challenging traditional disaster recovery, and underscoring the need for resilient solutions like Cloud Isolated Recovery Environments (CIRE) to ensure business continuity.
- **Sophisticated social engineering and multi-factor authentication (MFA) bypass**: Advanced threat actors are leveraging social engineering to steal credentials and session cookies, bypassing MFA to compromise cloud environments for financial theft, often targeting high-value assets.
- **Misuse of trusted cloud services for decoy file delivery to facilitate malware infections**: In a recent campaign, threat actors used .desktop files to infect systems by downloading decoy PDFs from legitimate cloud storage services from multiple providers, a tactic that deceives victims while additional malicious payloads are downloaded in the background.
- **Browser extension supply chain risk**: To combat threat actors using compromised OAuth tokens to bypass MFA and inject malicious code via automated CI/CD pipelines, Google has introduced Verified CRX Upload controls to secure the non-human identities used in these cloud-based build processes.

To effectively navigate the evolving threat landscape in H2 2025 and beyond, organizations must prioritize a defense-in-depth strategy focusing on identity security, robust recovery mechanisms, continuous vigilance against sophisticated social engineering and deception tactics, and supply chain integrity.

## Foundational Security Remains Critical Against Persistent Threats
Google Cloud’s latest research highlights that common hygiene gaps like credential issues and misconfigurations are persistently exploited by threat actors to gain entry into cloud environments. During the first half of 2025, weak or absent credentials were the predominant threat, accounting for 47.1% of incidents (Fig. 1). Misconfigurations (29.4%) and API/UI compromises (11.8%) followed as the next most frequently observed initial access vectors.

![H1 2025 Distribution of Initial Access Vectors Exploited by Threat Actors]

### Identity and Access Management (IAM) Controls:
- **Regularly audit permissions**: Use Google IAM Recommender to automatically identify and help remove excessive permissions to enforce the Principle of Least Privilege.
- **Protect applications from credential stuffing**: Implement Identity-Aware Proxy (IAP) to enhance protection with zero trust.
- **Proactively monitor for leaked credentials**: Leverage Google Cloud’s integrations that actively monitor for leaked credentials on public sources.

### Visibility and Proactive Defense Controls:
- **Maintain a unified view**: Use Google Security Command Center (SCC) as a central platform to continuously monitor for misconfigurations, vulnerabilities, and threats.
- **Maintain a robust vulnerability and patch management program**: Use SCC’s vulnerability detection or scan container images in Artifact Registry to identify vulnerabilities.

## Cloud-Native Backup and Recovery for Modern Cyber Threats
Financially motivated cyber criminals are targeting not only production systems and data, but also backup infrastructure and platforms. We are seeing threat groups like UNC2165, UNC4393, and UNC2465 targeting backup platforms to hinder response and recovery efforts.

### Common Recovery Architectures
- **Cloud Isolated Recovery Environment (CIRE)**: Highest resiliency; backup data is isolated and pre-staged.
- **Isolated Data Vault**: Moderate resiliency; utilizes recent backups from a separate vault.
- **Online/Production-Integrated Backups**: Lowest resiliency; prone to threat actor disruption.

### Mitigations
- **Logical Isolation & Segmentation**: Design separate VPC networks for production and backup environments.
- **Immutable Storage**: Leverage Cloud Storage with Object Versioning and Bucket Lock.
- **On-Demand Compute & Validation (IVE)**: Utilize the elasticity of Compute Engine to rapidly provision resources for data restoration.

## North Korea’s Social Engineering Leading to Cloud Compromises and Cryptocurrency Thefts
Google Threat Intelligence Group (GTIG) is tracking UNC4899, a North Korean threat actor targeting cryptocurrency and blockchain industries.

### A Tale of Two Thefts
UNC4899 utilized social engineering (Telegram/LinkedIn) to convince employees to execute malicious Docker containers. This led to the deployment of downloaders like GLASSCANNON and backdoors like PLOTTWIST and MAZEWIRE.

![UNC4899 Attack Lifecycle in a Victim’s Google Cloud Environment]
![UNC4899 Attack Lifecycle in a Victim’s AWS Environment]

### Mitigations
- **Fortify Identity with MFA & Session Management**: Prevent credential misuse by enforcing MFA and strict session controls.
- **Enhance Endpoint & Cloud Workload Threat Detection**: Integrate EDR telemetry with Google Security Operations.
- **Secure Software Development & Supply Chains**: Protect CI/CD pipelines by managing build artifacts with Artifact Registry and enforcing Binary Authorization.

## How Decoy Files Turn Trusted Cloud Services into Attack Vectors
Threat actors are increasingly using trusted cloud storage services (Google Drive, SharePoint, Dropbox, GitHub) to host decoy files (often PDFs) to deceive victims while malicious code executes in the background.

### Mitigations
- **User Awareness**: Conduct training highlighting the sophistication of social engineering.
- **Inbound File Inspection**: Utilize advanced email security and secure web gateway solutions with URL Sandboxing.
- **Endpoint Detection and Response**: Monitor for unusual process trees (e.g., PDF readers launching command interpreters like powershell.exe).

## Hardening the Chrome Extension Supply Chain Against Account Compromise
To counter the risk of compromised developer accounts distributing malicious updates, Google introduced the **Verified CRX Upload** feature.

### Mitigations
- **Implement Verified CRX Upload**: Opt-in to a flow that requires a second factor (a unique private key) for the upload process.
- **Promote Secure Developer Key Management**: Store private keys in highly secure locations (e.g., PKCS#12 or Java Keystore), independent of Google account credentials.

![How Verified CRX Upload Helps Protect Users]

## Contributors
Jason Bisson, Chary Chen, Anton Chuvakin, Michael Cote, Charles DeBeck, Elliot Eaton, Jack Fermon, Christopher Liebchen, Crystal Lister, Angelus Llanos, Jose Luis Sanchez Martinez, Bob Mechler, Noah McDonald, Glenn Staniforth, Chris Linklater, Matthew McWhirt, Joachim Metz, Simon Scannell, John Stone.