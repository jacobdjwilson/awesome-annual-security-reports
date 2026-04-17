# The State of Exposure Management in 2024

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Measuring Security Posture](#measuring-security-posture)
- [A Primer on Attack Paths](#a-primer-on-attack-paths)
- [Enumerating Exposures](#enumerating-exposures)
- [Points of Convergence](#points-of-convergence)
- [Organizational Comparisons](#organizational-comparisons)
- [Finding & Categorizing Exposures](#finding--categorizing-exposures)
- [Exposures in IT/Network Devices](#exposures-in-itnetwork-devices)
- [Exposures in Cloud Environments](#exposures-in-cloud-environments)
- [Exposures in Active Directory](#exposures-in-active-directory)
- [Conclusion](#conclusion)
- [Appendix A: Security Posture Scores by Sector](#appendix-a-security-posture-scores-by-sector)
- [Appendix B: Top Cloud Techniques](#appendix-b-top-cloud-techniques)

---

## Executive Summary

What if you could identify all the ways in which your organization is exposed to cyber attacks, understand how adversaries will exploit those exposures, and prioritize remediation efforts to reduce risk most effectively? Well, that is exactly what this report is all about.

This report presents key insights drawn from hundreds of thousands of attack path assessments conducted through the XM Cyber Continuous Exposure Management (CEM) platform during 2023. These assessments uncovered over 40 million exposures affecting 11.5 million entities deemed critical to business operations. Data gathered from the XM Cyber platform were anonymized and provided to Cyentia Institute for independent analysis to generate the insights that fill the pages to follow.

### Everyone’s talking about exposure management

Exposure Management seems to be the hot topic on everyone’s lips right now, but defining what this means and how best to implement a Continuous Threat Exposure Management (CTEM) framework is still causing some confusion.

Aiming to move away from the pain point of endless lists of vulnerabilities, organizations are embracing technologies that claim to provide greater coverage of exposure types, and additional context to aid the prioritization and risk analysis of these different exposure types. However, the context is still often limited to each individual asset or focused solely on the intrusion risk, as in which asset is the mostly likely breach point.

At XM Cyber, we’ve been providing holistic Exposure Management powered by our XM Attack Graph Analysis™ for over 8 years. We’re proud to once again distill those findings into this third edition of our annual State of Exposure Management report. We hope these insights will bolster your security team’s important mission over the next year.

---

## Key Findings

- **Exposure Management is much more than just CVEs.** Organizations typically have about 15,000 exposures across their environments that attackers could exploit. Traditional CVE-based vulnerabilities account for less than 1% of those and just 11% of all exposures to critical assets.
- **Poor cyber hygiene plagues the security of endpoints.** 79% of organizations have problems with cached domain credentials or local credentials that are present on multiple machines across the network. While most organizations use EDR (91%), over a quarter of devices aren’t typically covered.
- **One size doesn’t fit all for managing exposures.** On average, financial firms manage 5x more digital assets than the energy sector, but the proportion of exposures affecting critical assets is 21x higher in the latter.
- **Exposure Management can’t be a one-time or annual project.** It’s an ever-changing, continuous process to drive improvements. Organizations with poor posture scores have six times the number of security exposures (30k) compared to high scorers (5k). What’s worse is that the gap between those groups widened over time.
- **Effective Exposure Management needs to integrate attack path modeling.** XM Attack Graph Analysis™ identifies that 2% of exposures reside on “choke points” of converging attack paths that adversaries can use to reach critical assets. There’s a 20x difference in choke point ratio between organizations with the worst vs. best security posture.
- **Cloud environments are not exempted from the risk of exposure.** Over half (56%) of critical asset exposures are in cloud platforms. Furthermore, attackers can traverse on-premises to cloud environments in 70% of organizations and then compromise 93% of critical assets in the cloud in just two hops.
- **Identity and credential issues represent a huge exposed attack surface.** Active Directory typically accounts for 80% of all security exposures identified in organizations as well as one-third of their issues that put critical assets at risk.

---

## Measuring Security Posture

Organizations still struggle to get a holistic view of risk posture. We’ll soon dig into our detailed analysis of attack paths, but let’s first set the stage with an overall assessment of organizational risk exposure. The XM Posture Score™ provides such a view.

XM Cyber evaluates the risk to critical assets for various attack scenarios, each of which receives a score from 0 to 100. This score is based on the number and complexity of paths leading to critical assets in that scenario. A lower score indicates higher risk due to numerous shorter, simpler attack paths. Higher scores signify the opposite; critical assets are less susceptible to compromise. Scores for all scenarios are averaged to derive the overall security score for the organization.

![Figure 1: Organizations with the highest (blue) and lowest security scores (red)]

The median score across all organizations is 79. Security scores are not static over time; they shift up and down as changes in the environment and evolving attack scenarios alter risk to critical assets.

---

## A Primer on Attack Paths

Organizations face a constant threat of cyber-attacks that can jeopardize critical assets, exfiltrate data or disrupt business operations. The term **Attack Path** refers to the logical path across your network and around your different security defenses that the attack takes in order to execute their Kill Chain and reach the end goal of your business-critical assets and systems.

To help address this challenge, **Attack Path Modeling** is a foundational methodology needed for Exposure Management. It helps cyber defenders and security stakeholders identify and map potential routes that threat actors could take to exploit vulnerabilities, misconfigurations and weak security posture in order to compromise critical assets.

### Introducing XM Attack Graph Analysis™

XM Attack Graph Analysis™ gives you clear and concise exposure intelligence, built from context-based insights across all exposures from Cloud to Core, by pinpointing key intersections where attack paths converge and present the most critical risk to business operations.

![Figure 3: Example attack graph identifying entities, dead ends, choke points, and critical assets]

---

## Enumerating Exposures

Data collected from XM Attack Graph Analysis™ continually points to a core cybersecurity challenge facing every organization: there are just too many issues for defenders to realistically fix and too many ways for attackers to exploit them.

We typically identify 15,000 security exposures that attackers could exploit in each organization on a monthly basis.

- **Entities**: Any endpoint, workstation, server, identity, access tokens, cloud resources, etc. in an environment that an attacker can use to advance an attack path toward critical assets.
- **Exposures**: Exposures are combinations of techniques and entities susceptible to those techniques. They essentially enumerate the many options attackers have at their disposal.

---

## Points of Convergence

Rather than treating all exposures equally, a far more manageable approach is to identify the subset of issues that represent the highest risk and prioritize those for remediation. The majority (74%) of security exposures afflicting organizations are on “dead ends” that limit attackers’ lateral movement toward critical assets.

A small subset of exposures, however, affect critical assets and/or represent “choke points” of converging attack paths.

![Figure 5: A depiction of the typical attack surface, showing the ratio of “choke points” among all identified exposures]

We suggest focusing first on the exposures that matter most—and that’s clearly the choke points towards critical assets. This is the power of the XM Cyber approach to exposure management—98% reduction in effort for maximum risk reduction efficacy!

---

## Organizational Comparisons

When it comes to security, one size never fits all! Low scorers typically have 6X more exposures and a 23X higher ratio of choke points.

![Figure 7: Comparison of exposure statistics for organizations with high vs. low security scores]

In general, industries that have a lot of entities also have a lot of exposures. The fact that the median number of exposures affecting healthcare providers is 5X that of the Energy and Utilities sector points to the inherent challenges of minimizing risk in those environments.

---

## Finding & Categorizing Exposures

Where do all these exposures exist? How do attackers exploit them? What attack techniques can cause the most harm?

- **Active Directory** constitutes just over half of entities identified across all environments.
- **On-premises IT and network devices** account for another 31% of entities.
- **Cloud environments** house the remaining 17%.

However, if we rescope the attack surface to focus on exposures to critical assets, a very different picture emerges: Cloud environments now encompass over half of all critical asset exposures, followed by AD at 33% and IT/Network devices at 11%.

---

## Exposures in IT/Network Devices

Enterprise networks can be complex labyrinths, but that doesn’t mean attackers can’t navigate quickly through them. Over 60% of critical assets can be compromised in just a single hop from the initial point of intrusion into on-prem networks.

### Top on-prem attack techniques
We found exploitable vulnerabilities in most organizations (86%) but they accounted for less than 1% of all exposures and 11% of critical exposures. The two biggest techniques from a critical assets perspective are:
1. **Taint Shared Content**: Attackers “tainting” files in shared folders with malicious code.
2. **Local Credentials**: Common or shared accounts created locally on multiple devices.

---

## Exposures in Cloud Environments

We found exposures in 70% of organizations that allow attackers to pivot between enterprise networks and cloud environments. After gaining initial access to a cloud environment, attackers can compromise 88% of critical assets in a single hop.

Cloud security practices are still relatively immature in many organizations. Managing identities and permissions in cloud environments can be very different from their equivalents for enterprise infrastructure.

---

## Exposures in Active Directory

Active Directory is the key to your network, responsible for connecting users with network resources—but it’s also a prime target for attackers. Active Directory accounts for a huge proportion (80%) of security exposures across the typical enterprise network.

Many of these exposures stem from the inherent nature of dynamic configuration issues in Active Directory as well as the challenge of keeping it updated. Techniques like credential harvesting, dumping, relay, and domain credentials feature prominently.

---

## Conclusion

The report highlights the importance of Exposure Management as a multifaceted task that involves more than just addressing vulnerabilities and CVEs. Organizations must transition to a holistic and continuous Exposure Management methodology, integrating attack path modeling to identify and remedy choke points in their infrastructure.

The findings also stress the importance of adopting a Continuous Threat Exposure Management (CTEM) approach to improve overall security posture and mitigate risks across diverse attack surfaces.

---

## Appendix A: Security Posture Scores by Sector

![Figure A1: Comparison of overall security scores by sector]

The Financial Services sector, which often ranks high for strong security posture, actually sits in the middle of the pack as measured here. Healthcare institutions face numerous challenges when it comes to cybersecurity, and that fact is reflected in the relatively low security score for that sector.

---

## Appendix B: Top Cloud Techniques

The figures that follow list the top techniques observed by XM Cyber during attack path analyses conducted in 2023.

![Figure B1: Top techniques in AWS environments]

[^1]: Footnote content here.

---

WS Modify EC2 Instance User DataAWS EBS Share Volume SnapshotAWS S3 Bucket Write DataAWS S3 Bucket Read DataAWS Update Login ProfileAWS Create User Access KeyAWS Update Role Impersonation PolicyAWS IAM Add Policy Privilege EscalationAWS Access Keys StealerFigure B2: Top techniques in Azure environments

Figure B3: Top techniques in GCP environments

34

Navigating the Paths of Risk: The State of Exposure Management in 202431%14%4.4%31%0.20%19%30%0.66%21%28%0.059%0%27%13%4.7%27%13%4.5%25%0.56%0.17%25%0.026%0.00014%25%0.025%0.000058%24%0.71%16%23%20%7.0%21%9.7%3.1%20%8.1%2.6%19%3.2%2.8%17%1.1%0.42%15%2.2%1.3%9.9%0.14%3.4%9.3%3.7%0.00029%Azure Certificate Stealer from DiskAzure Group Member of GroupMicrosoft Intune - Execute ScriptAzure Queues CompromiseAzure Applications Can Add Passwords to Other ApplicationsAzure Upload BlobsAzure Read BlobsAzure Tables CompromiseAzure Member Of GroupModify OneDrive Files using Azure ApplicationsRead OneDrive Files using Azure ApplicationsAzure Key Vaults CompromiseAzure Run Command On VMAzure Run Command On VM Using VM ExtensionsAzure Access Token StealerAzure Add Role AssignmentAzure Graph Role CompromiseAzure Application Owner Can Compromise the Application Service PrincipalsOrganizationsExposuresCritical Exposures14.8%1.53%4.10%6.79%15.3%4.79%6.79%12.1%6.15%6.79%5.93%1.26%6.79%5.59%1.27%6.79%5.46%1.65%6.79%3.02%1.04%6.79%2.59%5.47%6.79%2.49%5.21%6.79%1.71%6.19%6.79%0.165%0.202%6.79%0.126%0.0302%6.17%3.07%6.13%6.17%2.67%6.00%6.17%2.43%6.29%6.17%2.42%6.04%6.17%1.78%10.1%6.17%1.58%5.57%5.56%10.8%2.55%4.94%10.1%2.49%4.32%0.104%5.97%3.09%5.71%6.01%GCP Member Of GroupGCP Set a Folder IAM PolicyGCP Write BigQueryGCP Read BigQueryGCP Set Service Account IAM PolicyGCP Set a Project IAM PolicyGCP Signing Well-Formed JWTGCP Request Service Account Token By Implicit DelegationGCP Allows Signing of Arbitrary PayloadsGCP Request Service Account TokenGCP Read FirestoreGCP Compromised Service Account KeyGCP Service Account From ResourceGCP Create Function with Specified Service AccountGCP Create VM with Specified Service AccountGCP Set Storage IAM PolicyGCP Read SecretGCP Read Data From BucketGCP Write Data To BucketGCP Create Service Account KeyGCP Compromise Linux VMGCP Access Token StealerOrganizationsExposuresCritical ExposuresAppendix C: Top Attack Techniques

MITRE ATT&CK is a popular knowledge base of adversary tactics, techniques, and procedures
(TTPs) used across the cybersecurity industry. Because of this popularity, we maintain a mapping
between our attack path techniques and ATT&CK. Based on that mapping, Figure C1 lists the top
ATT&CK techniques identified by XM Cyber in 2023.

Figure C1: Top ATT&CK techniques identified by XM Cyber attack path analysis during 2023

Figure C2 compares techniques that expose critical assets in on-prem networks, cloud platforms,
and Active Directory. Overall, there’s surprisingly little overlap between the columns. That suggests
prioritization of TTPs and defenses should be done specific to the environment in view. It also
reiterates the importance of context in threat and risk assessment.

Figure C2: Comparison of critical ATT&CK techniques identified by XM Cyber in different scenarios

35

Navigating the Paths of Risk: The State of Exposure Management in 202499.4%15.5%37.2%95.7%10.3%10.1%95.1%36.3%14.4%94.4%9.31%2.72%93.8%3.56%6.58%93.2%0.934%1.53%92.0%8.96%2.06%90.1%2.88%3.53%90.1%2.88%3.53%89.5%5.25%2.88%87.7%0.951%0.896%84.0%0.355%4.74%83.3%0.420%2.60%Exploitation for Privilege Escalation (T1068)Exploitation of Remote Services (T1210)Adversary-in-the-Middle (T1557)Taint Shared Content (T1080)Windows Management Instrumentation (T1047)Scheduled Task/Job (T1053)Boot or Logon Initialization Scripts (T1037)OS Credential Dumping (T1003)Remote Services (T1021)Permission Groups Discovery (T1069)Account Manipulation (T1098)Use Alternate Authentication Material (T1550)Valid Accounts (T1078)OrganizationsExposuresCritical Exposures33.5%8.23%31.5%8.23%23.2%15.3%2.50%26.3%6.77%86.8%8.23%Active DirectoryWindows Management Instrumentation (T1047)Valid Accounts (T1078)Use Alternate Authentication Material (T1550)Taint Shared Content (T1080)Scheduled Task/Job (T1053)Remote Services (T1021)Account Manipulation (T1098)CloudIT/Network devices