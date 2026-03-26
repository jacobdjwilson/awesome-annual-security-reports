# Cloud-Threat-Horizons-Report-H1 2024

## Table of Contents
- [Mission Statement](#mission-statement)
- [Executive Summary](#executive-summary)
- [Cryptomining Remains the Dominant Consequence of Weak Cloud Configurations](#cryptomining-remains-the-dominant-consequence-of-weak-cloud-configurations)
- [Strengthen Security to Counter Ransomware Attacks and Data Theft in the Cloud](#strengthen-security-to-counter-ransomware-attacks-and-data-theft-in-the-cloud)
- [Don’t Get Caught in the Dark: Shining Lights with Logs](#dont-get-caught-in-the-dark-shining-lights-with-logs)
- [Advanced Persistent Threat (APT) Actors In Cloud Architecture Spotlight: People’s Republic of China (PRC)](#advanced-persistent-threat-apt-actors-in-cloud-architecture-spotlight-peoples-republic-of-china-prc)

---

## Mission Statement

The Google Cloud Threat Horizons Report provides decision-makers with strategic intelligence about threats to cloud enterprise users, along with cloud-specific research, based on intelligence-derived threat actor trends and expertise from Google Cloud security leaders and practitioners. Most importantly, the report delivers recommendations on mitigating these risks and improving cloud security posture from Google’s intelligence and security teams, including Google Cloud’s Office of the CISO, Google’s Threat Analysis Group, Mandiant, and various Google Cloud product teams.

---

## Executive Summary

This iteration of the Google Cloud Threat Horizons Report provides a forward-thinking view of cloud security with intelligence on emerging threats and actionable recommendations from Google’s security experts. This report explores top cloud threats and security concerns for 2024, including credential abuse, cryptomining, ransomware, and data theft.

In 2023, threats increased in number and sophistication targeting all IT environments—on-premise, mobile, IT/OT, and the cloud. Issues specific to cloud providers were often due to security hygiene or misconfigurations rather than underlying vulnerabilities. We saw threat actors evolve their methods for abusing and monetizing cloud infrastructure, gaining initial access to cloud networks, conducting cloud-based supply chain attacks, and running malicious operations from cloud environments.

Based on our research and analysis, the following areas should inform cloud customer security strategies in 2024:

- **Credential abuse resulting in cryptomining** remains a persistent issue, with threat actors continuing to exploit weak or nonexistent passwords to gain unauthorized access to cloud instances, while some threat actors are shifting to broader threat objectives.
- **Ransomware and data theft** remain a concern in all IT environments, including on-premise and cloud, as threat actors are continuously evolving their methods for conducting ransomware and data theft attacks—making robust data loss prevention strategies more essential than ever before.
- **Increased focus on security event logging** is necessary to address threat actors’ evolving tactics of manipulation and deleting logs. Threat actors are increasingly targeting security event logging software in novel ways to disrupt and evade detection.
- **People’s Republic of China (PRC)-affiliated espionage threat actors** are increasingly targeting cloud services and infrastructure given the enhanced adoption of cloud across industries globally.

The cloud threats and security issues identified in 2023 will likely continue this year as threat actors seek new ways to bypass security measures, breach customer cloud projects, move laterally, access sensitive data, refine proven techniques, and explore new tactics using Artificial Intelligence (AI).

Looking ahead, high-profile global events in 2024 (e.g. elections worldwide, the Summer Olympics, regional conflicts in multiple regions, etc.) will continue to serve as attractive targets for threat actors seeking novel ways for conducting malicious activities like information operations, espionage, and other cyber campaigns to achieve their objectives. As such, weak points within customer cloud projects will likely be among the top methods attackers utilize to achieve their objectives. We will continue leveraging our threat intelligence and insights to identify actionable risk mitigations to help organizations enhance their cloud security.

---

## Cryptomining Remains the Dominant Consequence of Weak Cloud Configurations

![Chart showing 2023 Cloud Compromises: Initial Access, with Weak or no password at 51.1%, Leaked credentials at 17.3%, Misconfiguration at 13.7%, Vulnerable software at 11.5%, Sensitive UI or API exposed at 3.6%, and Other at 2.9%.]

Credential issues remain the predominant security oversight observed among Google Cloud customers. Over half of incident data shows that threat actors are compromising Cloud instances with weak or no passwords on common remote access protocols, Secure Shell (SSH) and Remote Desktop Protocol (RDP), to gain unauthorized access to Cloud instances. This provides threat actors with easy access to compromised cloud resources, which they can monetize by selling access, often for a couple of dollars per credential pair. Given that harvesting such credentials is low-effort for a threat actor, this trend will likely continue to affect organizations that fail to meet basic standards of security.

Cryptomining remained one of the principal motivations behind threat actors who abused cloud access, accounting for nearly two-thirds of observed activity. This quick and easy money maker serves a clear profit motive for criminal actors, as it allows threat actors to use a victim’s cloud processing power to mine for cryptocurrency in a shorter period of time. However, this dominance, cited in the Threat Horizons Report throughout 2023, risks overshadowing an insidious trend. Several times throughout 2023, we observed threat actors leverage illicit cloud access in an attempt to infect third parties. This less common tactic, constituting over 25% of observed incidents, has significant security impacts for organizations on both sides of the attack.

![Chart showing 2023 Cloud Compromises: Impact, with Coin mining at 65.4%, Other at 26.0%, Intrusion attempt at 5.8%, Account leaked credentials at 2.0%, and DOS at 0.8%.]

### Mitigations
- Lock down SSH, RDP, and any other known remote access software with organization-level policy controls on GCP.
- Use Essential Contacts to ensure every cloud service used by an organization has point of contact (POC) information updated.
- Monitor cloud resource utilization, and establish alerts for anomalous events.
- Consider leveraging Security Command Center to detect CPU/memory spikes related to cryptomining activity.
- Reassess your cloud incident response and reconstitution plan.

---

## Strengthen Security to Counter Ransomware Attacks and Data Theft in the Cloud

Threat actors continued targeting unprotected public cloud storage services, misconfigured networks, and weak cloud storage naming conventions for ransomware and data exfiltration in 2023.

![Table: Common Causes of Ransomware and Data Theft in the Cloud: Weak credentials, Misconfigurations and errors, Weak storage defenses, Application vulnerabilities, and Third-party issues.]

![Figure 2: Model of a Cloud Storage Bucket Naming Convention Exploited by a Threat Actor. Shows an attacker anticipating bucket names to exfiltrate data.]

### Mitigations
- Follow Google Cloud and industry best practices for cloud asset risk management.
- Establish a cloud-specific backup strategy with testing.
- Use technologies, such as WORM (Write Once Read Many), or the Bucket Lock feature on Google Cloud.
- Implement resilient architecture, such as multi-region cloud use and backup mirroring.
- Encrypt all backups; Google Cloud customers can add an additional layer of encryption by using customer-managed encryption keys (CMEK).

---

## Don’t Get Caught in the Dark: Shining Lights with Logs

In 2023, threat actors targeted security event logging software in all IT environments in a number of novel ways that evade detection. Robust logging practices are fundamental to an organization’s security posture.

### Mitigations
- Identify relevant logs to collect and monitor as outlined from Google Cloud’s MITRE ATT&CK mapping.
- Export logs to a centralized, well-governed repository.
- Securely configure IAM permissions so only key individuals have access to change logging settings.
- Monitor for missing logs.
- Assure sensitive information is not available to threat actors with access to logs using Cloud Data Loss Prevention (DLP).

---

## Advanced Persistent Threat (APT) Actors In Cloud Architecture Spotlight: People’s Republic of China (PRC)

Throughout 2023, the People’s Republic of China (PRC) has increasingly targeted cloud infrastructure. The TTPs, particularly those focused on “Living-off-the-Land” (LOTL) tactics, have enabled threat actors to blend into normal network activities, evading detection.

### The Case of UNC3236 aka Volt Typhoon
Google Cloud security partners track this threat as UNC3236, a PRC-nexus threat actor active since at least 2021. This actor is targeting US critical infrastructure, with the goal of gathering intelligence and disrupting operations.

### The Case of Storm 0588
In July 2023, Microsoft’s Storm-0558 campaign involved the use of forged tokens to access the email systems of about 25 entities, including government agencies and public cloud consumer accounts.

### Mitigations
- **Security by Design; Safe by Default; Security in Deployment**: Build software that is inherently secure.
- **Leverage Chronicle Cybershield**: Build a scalable and centralized threat intelligence and analysis capability.
- **Defense in Depth Approach**: Use multiple complementary controls, failsafes, and redundancies.
- **Cloud Key Management Service**: Create and manage encryption keys for use in compatible Google Cloud services.
- **Engage in collaboration**: Participate in Information Sharing and Analysis Centers (ISACs).

[^1]: Footnote content here.