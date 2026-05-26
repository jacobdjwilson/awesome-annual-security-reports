# Arctic Wolf Labs: Cybersecurity Predictions 2025

## Table of Contents
- [Introduction](#introduction)
- [01: Organizations Will See a Continued Breakdown of Their Perimeter Defense as Threat Actors Target VPN Gateways and Other Edge Devices](#01-organizations-will-see-a-continued-breakdown-of-their-perimeter-defense-as-threat-actors-target-vpn-gateways-and-other-edge-devices)
- [02: Adversaries Will Continue To Create and Leverage Opportunities for Large-Scale Social Engineering Campaigns, While Incorporating New TTPs](#02-adversaries-will-continue-to-create-and-leverage-opportunities-for-large-scale-social-engineering-campaigns-while-incorporating-new-ttps)
- [03: Ransomware and Other Attacks Will Increasingly Exploit Weaknesses in Identity and Access Management (IAM) Configurations](#03-ransomware-and-other-attacks-will-increasingly-exploit-weaknesses-in-identity-and-access-management-iam-configurations)
- [04: Critical Infrastructure Will Continue To Be Targeted, Both for Financial Gain and in Preparation for Potential Hybrid Conflicts](#04-critical-infrastructure-will-continue-to-be-targeted-both-for-financial-gain-and-in-preparation-for-potential-hybrid-conflicts)
- [05: The Widespread Availability of Advanced AI Reasoning Will Allow Threat Actors to Rapidly Uncover Novel Initial Access Techniques](#05-the-widespread-availability-of-advanced-ai-reasoning-will-allow-threat-actors-to-rapidly-uncover-novel-initial-access-techniques)
- [Conclusion](#conclusion)
- [How Arctic Wolf Can Help](#how-arctic-wolf-can-help)

---

## Introduction

### Adaptability and Opportunism in 2025

Looking ahead to 2025, we believe two forces will exert a significant influence on tomorrow’s threat landscape: adversaries’ ability and willingness to adapt, and their propensity for financial gain. Unencumbered by laws, certain ethical standards, or institutional inertia, attackers of all types — from nation-state agencies, to ransomware groups, to hacktivists, to individuals — benefit from an opportunistic advantage and nimbleness of execution that defenders may lack. Closely related, threat actors perceive the world through a lens of opportunity. With this outlook, practically any new technology, or emerging crisis, or change in IT architectures — to list just a few circumstances — can be leveraged.

Against this backdrop, our specific observations lead to our five core predictions for 2025:

1. Many organizations will see a continued breakdown of their perimeter defense as threat actors target VPN gateways and other edge devices.
2. Malicious actors will continue to refine their social engineering methods, creating opportunities for large-scale campaigns.
3. Ransomware attacks will increasingly exploit weaknesses in identity and access management (IAM) configurations.
4. Critical infrastructure will continue to be targeted, both for extortion and to prepare the digital battlefield for potential hybrid conflicts.
5. The widespread availability of advanced AI reasoning will allow threat actors to rapidly uncover novel initial access techniques.

These predictions are the work of several of our brightest minds who aim to prepare security teams for the challenges of the year ahead to mitigate the risks posed by threat actor activity. It is also important to note that these listed predictions highlight areas of concern but are not presented in a ranked or hierarchal format. We suggest determining the priority of each topic based on the specifics of your environment.

**Dan Schiappa**
Chief Product & Services Officer

---

## 01: Organizations Will See a Continued Breakdown of Their Perimeter Defense as Threat Actors Target VPN Gateways and Other Edge Devices

Once the cornerstone of a strong cybersecurity posture, the perimeter has undergone unprecedented transformation in recent years — resulting in both a larger attack surface and a plethora of remote access tools that threat actors are eager to exploit.

### The Only Constant Is Change
The past few years have brought considerable change as multiple trends converged. First, enterprise perimeters themselves have transformed. From IoT devices and cloud infrastructure to customer-facing applications and many other interface points, today’s perimeters bear little resemblance to those of even the recent past.

Second, the adoption of remote work has imposed new requirements and introduced new challenges. To enable this, organizations introduced and continue to refine their tooling, including VPN gateways and zero trust network access (ZTNA) tools.

Third, threat actors have adjusted their tactics, techniques, and procedures (TTPs) to take advantage of these shifts. More edge devices and services mean more configurations to harden and vulnerabilities to patch, with any mistake or delay creating an opportunity for an attacker to gain initial access.

### Turning the Tables
Threat actors have had considerable success attacking the tools organizations rely upon for remote work. For instance, 2024 saw widespread exploitation of software vulnerabilities within VPN gateways (e.g., Palo Alto Networks, SonicWall). Additionally, adversaries frequently leverage stolen credentials to turn an otherwise secure gateway into a convenient means of surreptitiously accessing the enterprise environment.

![Image: Diagram illustrating the expansion of the attack surface from traditional perimeters to remote work and IoT devices.]

### Recommendations
- Ensure network and endpoint logs are available for examination and correlation.
- Train the workforce on credential hygiene best practices.
- Reduce the blast radius of compromised accounts and devices by using network segmentation.
- Implement a vulnerability management program that prioritizes continuous vulnerability remediation and assessment.
- Subscribe to security bulletins and incorporate their recommendations.
- Pay special attention to securing Internet of Things (IoT) devices.

---

## 02: Adversaries Will Continue To Create and Leverage Opportunities for Large-Scale Social Engineering Campaigns, While Incorporating New TTPs

Social engineering offers a cheap and effective way for threat actors to bypass technological defenses, and new tools — particularly generative AI — make it even easier to execute even more effective attacks.

### Don’t Believe Everything You See and Hear
“Never let a good crisis go to waste.” — Winston Churchill. We regularly see threat actors immediately spring into action when disaster strikes. Compounding the threat, generative AI is lowering the bar to entry for crafting convincing messaging and creating deepfakes. Voice phishing (vishing) is growing as a threat, with adversaries masquerading as employees and targeting call centers and help desks.

### MFA Implementation Details Matter
In response to phishing, many organizations have deployed multi-factor authentication (MFA). However, threat actors are executing adversary-in-the-middle (AiTM) attacks and employing MFA fatigue. Correct configurations should render these types of attacks impossible, but reaching that state often requires modern MFA techniques like those employing the WebAuthn/FIDO2 phishing-resistant standards.

### Recommendations
- Educate users about phishing and conduct phishing attack simulation.
- Implement email controls as a defensive layer.
- Implement and enforce modern, phishing-resistant MFA.
- Reduce the blast radius of compromised accounts and devices through network segmentation and least-privilege access controls.
- Ensure SaaS logs are available for examination and correlation.
- Employ a multi-vendor strategy to limit exposure to outages.

---

## 03: Ransomware and Other Attacks Will Increasingly Exploit Weaknesses in Identity and Access Management (IAM) Configurations

Identity has rapidly risen to prominence as one of the most important and complicated cybersecurity domains. Misconfigurations and permissive policies play right into the hands of ransomware affiliates and other threat actors.

### Of Details and Perceived Trade-Offs
Identity is a specialized and challenging domain. Results of errors — including overprivileged access, orphaned accounts, and shadow directories — can be exploited to gain unauthorized access. Furthermore, Active Directory (AD) configurations are not specifically designed to be “secure by default.”

### Infostealers and Credential Abuse
Threat actors are willing to take advantage of any weakness in identity infrastructure. In particular, the use of infostealers to acquire credentials or active session cookies is a major threat. Verizon’s 2024 Data Breach Investigations Report (DBIR) indicates that over 80% of breaches involve compromised identity.

### Recommendations
- Work with your IAM and application providers to strengthen defenses against account takeovers (ATOs).
- Block authentication attempts from hosting-based traffic.
- Set automated blocking on authentication attempts to hinder password-spraying.
- Configure syslog to forward VPN and firewall logs to your security operations provider.
- Implement network segmentation to limit lateral movement.
- Ensure telemetry from on-premises and SaaS authentication providers is available for correlation.

---

## 04: Critical Infrastructure Will Continue To Be Targeted, Both for Financial Gain and in Preparation for Potential Hybrid Conflicts

Key sectors will be subjected to disruptive attacks and stealthy intrusions as adversaries look for financial payouts and aim to prepare the digital battlefield for potential conflict.

### Critical Infrastructure Is Under Attack
Presidential Policy Directive 21 (PPD-21) designates 16 sectors as “critical infrastructure.” In 2024, we saw an increase in threat activity against these sectors, including the Water and Wastewater Systems, Energy, and Healthcare sectors.

### From Disruption to Destruction
The coming year could represent a geopolitical tipping point. Adversaries often attempt to take advantage of change, and a number of Western nations have recently experienced leadership transitions. Should a conflict arise, nation-state affiliated actors may be called upon to escalate from disruption to outright destruction.

### Recommendations
- Implement a vulnerability management program that prioritizes continuous remediation.
- Subscribe to security bulletins.
- Ensure network and endpoint logs are available for examination and correlation.
- Reduce the blast radius of compromised accounts and devices through network segmentation.
- Ensure a comprehensive, realistic, and up-to-date disaster recovery plan is in place.
- Maintain proper backup practices and follow the 3-2-1 principle of backup.
- Test your recovery processes and capabilities.

---

## 05: The Widespread Availability of Advanced AI Reasoning Will Allow Threat Actors to Rapidly Uncover Novel Initial Access Techniques

Thus far, even the most advanced AI models have failed to replicate human reasoning capabilities, but that may soon change. Once it does, threat actors will harness this power to uncover new ways to break into protected environments.

### The State of the Art
While frontier large language models (LLMs) already possess some programming capabilities, they haven’t yet led to a significant increase in new initial access techniques. However, once LLMs are able to competently reason about the flow of data through an application, they are expected to facilitate the discovery of novel vulnerabilities or chain together vulnerabilities in a manner that is more difficult for humans to achieve.

### An Ongoing Arms Race
The warning signs are already here: in 2024, OpenAI identified a cluster of ChatGPT accounts using the platform for scripting and vulnerability research tasks, all with nation-state ties. As these TTPs become more common and affordable, they will be incorporated into more attacker toolsets.

### Recommendations
- Implement network segmentation and the principle of least privilege.
- Conduct audits and penetration tests to identify areas of weakness.
- Employ managed detection and response (MDR) to provide continuous monitoring.

---

## Conclusion

### Anticipating the Future Helps Us Prepare for It
By examining the evolution of attacker TTPs, we are able to propose reasonable answers to the question, “What will adversaries try next?” These answers help inform preventative measures. However, no defense is impenetrable. Consequently, just as important as preventative measures are the abilities to detect and respond — quickly and effectively — to cyber attacks that do occur.

---

## How Arctic Wolf Can Help

Cybersecurity is a team sport. Arctic Wolf® is a global leader in security operations, delivering the first cloud-native security operations platform to end cyber risk. Powered by threat telemetry spanning endpoint, network, identity, and cloud sources, the Arctic Wolf Aurora Platform ingests and analyzes trillions of security events each week.

For more information about Arctic Wolf, visit [arcticwolf.com](https://arcticwolf.com).

©2025 Arctic Wolf Networks, Inc. All rights reserved. | Public ARCTIC WOLF LABS