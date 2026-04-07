# 2021 IBM Security X-Force Cloud Threat Landscape Report

IBM Security X-Force Threat Intelligence
Special Intelligence Report

## Table of Contents
- [Introduction](#introduction)
- [Key takeaways](#key-takeaways)
- [Section 1: A thriving dark web market for cloud access](#section-1-a-thriving-dark-web-market-for-cloud-access)
- [Section 2: Vulnerabilities in cloud environments grow in number and severity](#section-2-vulnerabilities-in-cloud-environments-grow-in-number-and-severity)
- [Section 3: How threat actors are getting into cloud environments](#section-3-how-threat-actors-are-getting-into-cloud-environments)
- [Section 4: Threat actors using cloud environments for miners, ransomware, botnets and worse](#section-4-threat-actors-using-cloud-environments-for-miners-ransomware-botnets-and-worse)
- [Section 5: Recommendations and best practices for preparing for and reacting to cloud breaches](#section-5-recommendations-and-best-practices-for-preparing-for-and-reacting-to-cloud-breaches)

---

## Introduction

In 2020, IBM Security X-Force produced a report containing exclusive research and data on ground-truth statistics surrounding threat actor targeting of cloud environments. Cloud adoption continues to thrive, providing convenience, cost savings, and near-permanent uptimes for organizations compared to on-premises infrastructure.

At the same time, threat actors continue to target cloud environments regardless of organization size, and shifting to a cloud model requires a specialized approach different from that of traditional deployments. A key factor to successful deployment—and management—of cloud environments is understanding how threat actors target them, what motivates them, and how to avoid common pitfalls that leave the cloud vulnerable.

This year, we have augmented our 2020 report with new and more robust data spanning Q2 2020 through Q2 2021. Data sets we used include dark web analysis, IBM Security X-Force Red penetration testing data, IBM Security Services metrics, X-Force Incident Response analysis and X-Force Threat Intelligence research. These multiple data sources help us better understand how threat actors are getting into cloud environments, what types of malicious activity are pursued once they’re inside and how organizations can prepare and react to security incidents involving their cloud environments more effectively.

## Key takeaways

### Cloud environments need to be better secured
- **Cloud accounts/resources on the dark web**: A thriving dark web market exists for public cloud access, with advertisements for tens of thousands of cloud accounts and resources for sale.
    - In 71% of cases, threat actors offered Remote Desktop Protocol (RDP) access to cloud resources, enabling attackers to have direct access and conduct malicious activity.
    - In some cases, account credentials to access cloud environments were being sold for a few dollars.
- **Passwords & Policies**: 100% of X-Force Red penetration tests of cloud environments found issues with either passwords or policies.
- **Hardening systems**: Based on X-Force research, two thirds of cloud breaches would likely have been prevented by more robust hardening of systems, such as properly implementing security policies and patching systems.
- **Cloud vulnerabilities surge**: Almost half of the more than 2,500 disclosed cloud-related vulnerabilities recorded to date were disclosed in the last 18 months. While some of this growth can be attributed to better tracking (cloud vulnerabilities were added to MITRE’s CVE standards in January 2020), this steep growth emphasizes the importance of closely managing this growing risk as more vulnerabilities are exposed.

### Threat actors target cracks in the armor
- **Public API policies** represented a significant security gap. Two-thirds of the incidents analyzed involved improperly configured Application Programming Interface (APIs), based on analysis of X-Force Incident Response data of impacted clients.
- **One of the top attack vectors** X-Force observed targeting cloud was threat actors pivoting from on-premises environments into cloud environments. This lateral movement was seen in almost a quarter of incidents X-Force responded to in 2020.
- **IBM estimates** that over half of cloud breaches occurred due to “shadow IT”, emerging via unauthorized systems spun up against security policies which likely lacked vulnerability and risk assessments, as well as hardened security protocols.

### Threat actors continue investing in cloud targeting
- **Cryptominers and ransomware** remain the top dropped malware into cloud environments, accounting for over half of detected system compromises, based on the data analyzed.
- **Threat actors are continuing to pursue clouds** in their malware development, with new variants of old malware focusing on Docker containers, as well as new malware being written in programming languages, like Golang, that run cross-platform.

---

## Section 1: A thriving dark web market for cloud access

IBM investigated dark and deep web sales of access to cloud accounts, and the results were sobering. Tens of thousands of accounts and resources were potentially offered for sale on multiple dark web markets. The vast majority of these sales were on markets automatically populated by different info-stealers and malware opportunistically compromising victims and offering credentials for sale.

### Many cloud accounts for sale, but not all created equal
Within the timeframe noted above, X-Force research found almost 30,000 cloud accounts potentially for sale on dark web marketplaces. 

Outside of the botnet-populated markets, cloud account advertisements in other dark web forums show prices that range from a few dollars to over $15,000 per account access credentials, based on a variety of factors. Those that appear to impact value of accounts for sale include amount of credit on the account, geography and level of account access to the organization that owns that account (root access versus less privileged users).

### Looking for cloud credits
A number of cloud-related advertisements on the dark web involved selling cloud accounts that had access to account credits. 

On average, the price tag for cloud access rose an extra $1 for every $15-30 in credit the account held. An account with $5000 in available credit would be worth about $250 (a ratio of 20:1). 

### Low-cost access, potential for high impact
The low price of cloud accounts with high credit value could be the result of a few possibilities. Interestingly, threat actors often offer warranties on sold access, promising a refund if the access is no longer available 7 or 14 days after sale, indicating access may not have a long lifespan.

> Stolen accounts not only offer adversaries opportunity to launch attacks in the cloud, they also provide a way for attackers to gain a foothold in an organization’s overall environment and access other parts of the network.

### Assessing your value to threat actors
The dark web research shows that threat actors remain interested in accessing and taking advantage of cloud accounts, but IBM’s research also highlights that not all accounts hold the same perceived value to an attacker. For instance, an account based in western Europe with significant credits would be of very high value to threat actors and could increase an organization’s threat profile.

---

## Section 2: Vulnerabilities in cloud environments grow in number and severity

Despite cloud environments’ myriad of security benefits, researchers continue to discover new vulnerabilities that can help attackers break into the cloud. IBM research indicates that cloud vulnerabilities are growing in number, currently totaling over 2,500 vulnerabilities, a 150% increase in the last five years.

![Chart showing the growth of cloud vulnerabilities from 2006 to 2021]

When it comes to vulnerabilities, IBM Security X-Force Red uses a multifaceted ranking algorithm to score the severity of vulnerabilities with a “Risk Score.” The Risk Score uses a variety of factors, such as ease of use, level of access granted and impact on the affected system, to accurately measure vulnerabilities.

---

## Section 3: How threat actors are getting into cloud environments

Threat actors continue to access cloud data illicitly, and in this year’s report IBM brings a host of new data points to refine our understanding of how they are targeting organizations’ cloud assets.

Password and policy violations, often from shadow IT, continue to plague cloud environments. X-Force Red found that 100% of their penetration tests into cloud environments in 2021 uncovered issues with at least one of these two components.

### IBM Security X-Force Incident Response insights
The IBM Security X-Force Incident Response (IR) team analyzed cases over the last year involving cloud breaches and identified the most commonly exploited vulnerabilities and misconfigurations:

- **Virtual machines and other resources** with default security settings that were erroneously exposed to the Internet.
- **Insufficient access control mechanisms**, such as a lack of Multifactor Authentication (MFA) for SaaS solutions.
- **Insufficiently segmented virtual networks** and promiscuous trust relationships between on-premises and cloud computing environments.

### Improperly configured resources
Insecure public APIs are a pervasive problem. Two thirds of cloud incidents in the data sample related to misconfigured API keys that allowed improper access. 

> Password spraying, exploited software vulnerabilities and cloud deployment misconfigurations are the most common methods threat actors use to access cloud environments.

### Remote exploitation favors RDP
Dark web data further reinforces the effectiveness of remote access compromise. IBM’s analysis of dark web markets found that RDP accounted for the access vector in over 70% of cloud resources offered for sale on the dark web.

![Chart: Dark web cloud accounts by access type: 71% RDP, 20% Other, 4.5% cPanel, 4.5% Shell]

---

## Section 4: Threat actors using cloud environments for miners, ransomware and botnets

X-Force analyzed data from our IR teams to find how threat actors are using cloud environments once they’re inside. Based on our analysis of incidents, cryptominers and ransomware were used extensively, accounting for over half of system compromises.

### Malware focus on Docker
Analyzing malware trends impacting cloud environments, X-Force IR observed multiple malware families shifting their sights from targeting generic Linux systems to focusing on Docker containers. Some malware families illustrating this shift include XoRDDOS, Groundhog and Tsunami.

### Cloud-centric malware development on the rise
Research by Intezer highlights threat actors’ continued investment in evolving the code in cryptominers, botnets and ransomware. 

![Chart: Frequency of unique code strings by malware category (Banker, Botnet, Miner, Ransomware)]

### Command and control shifts
Threat actors continue to use cloud infrastructure to host malicious payloads and maintain Command and Control (C2) backend for their operations. Illustrative examples include:
- **PowerSlack**: A cloud-leveraging backdoor using Slack for C2 communications.
- **Astaroth**: Stored C2 information in YouTube video descriptions.

### Fileless malware
Evasive, fileless malware lurking in memory can elude standard detection tools. Threat actors are now using Ezuri, an open-source crypter and memory loader written in Golang.

---

## Section 5: Recommendations and best practices for preparing for and responding to cloud breaches

IBM Security X-Force suggests cloud users should consider implementing a multi-phased security approach.

### Preparation
- **Use an open and integrated security approach** to connect the dots between security data.
- **Implement a zero trust philosophy**, including virtual network segmentation.
- **Evaluate trust relationships** between on-premises and cloud environments.
- **Extend monitoring and detection** capabilities to cloud environments.
- **Deploy a bastion host** to isolate private cloud network zones.
- **Implement cloud web application defenses**, including WAFs.
- **Implement and enforce strong access control**, including the principle of least privilege and MFA.
- **Automate security group privileges** and new user creation.
- **Modernize Identity and Access Management (IAM)**.
- **Implement provisioning policies** to govern the lifecycle of deployed resources.
- **Use automation extensively** to remove human error.
- **Scope penetration testing projects** to identify vulnerabilities.
- **Engage in adversary simulation exercises**.

### Responding
- **Implement AI and automate incident response** and malware analysis.
- **Preserve forensic artifacts** by redeploying, not reimaging, affected machines.
- **Leverage threat intelligence** during incident response.
- **Ensure your organization has the right tools and personnel** for cloud breaches.
- **Have surge assistance on speed dial**, such as an X-Force Incident Response Retainer.

---

## About IBM Security X-Force
The X-Force team is comprised of industry-leading, highly skilled incident response professionals experienced in investigating compromises of on-prem, cloud and hybrid cloud environments. If you would like to learn more about any of the X-Force report findings or would like to learn about any X-Force services schedule a consult [here](https://www.ibm.com/security/services/incident-response).

### Contributors
- Charles DeBeck
- Richard Emerson
- Andrew Gorecki
- Charlotte Hammond
- Intezer
- Scott Lohr
- Mitch Mayne
- Scott Moore
- Jason Riggs
- Oscar Sanchez
- Johnny Shaieb

© Copyright IBM Corporation 2021