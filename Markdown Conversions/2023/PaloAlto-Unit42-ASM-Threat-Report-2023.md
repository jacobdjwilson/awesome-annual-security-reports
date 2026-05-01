# Unit42-ASM-Threat-Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Attackers Move at Machine Speed](#attackers-move-at-machine-speed)
- [Top Attack Surface Exposures](#top-attack-surface-exposures)
- [Remote Access Exposures Lead to Ransomware](#remote-access-exposures-lead-to-ransomware)
- [Cloud Dynamism Is Straining Security Controls](#cloud-dynamism-is-straining-security-controls)
- [Cloud Exposures Dominate Most Organizations’ Security Risks](#cloud-exposures-dominate-most-organizations-security-risks)
- [Industry Attack Surface Breakdown](#industry-attack-surface-breakdown)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [Methodology](#methodology)

---

## Executive Summary

Modern organizations are racing to update their enterprise network architectures to take advantage of Zero Trust security designs, cloud computing, software-as-a-service (SaaS) value delivery, and distributed workforces. This has fueled a dramatic increase of infrastructure, known and unknown, which in turn has greatly increased the complexity of securing their environments.

Exposures on publicly facing assets put them at risk of being compromised, and sometimes this leads to organizations becoming victims of opportunity as opposed to a targeted attack. Understanding what you need to protect is a precursor to any successful cybersecurity program—but companies and government agencies struggle to understand what they own and what services expose the most risk.

To put these sweeping changes into context and provide actionable intelligence, Unit 42 analyzed several petabytes of public internet data collected by Cortex Xpanse — the Palo Alto Networks attack surface management solution — in 2022 and 2023. This report outlines aggregate statistics about how attack surfaces worldwide are changing and drills down into particular risks that are most relevant to the market.

### Key Findings
- **Constant change in the cloud creates new risk.** Cloud-based IT infrastructure is always in a state of flux. In a given month, an average of 20% of an organization’s cloud attack surface will be taken offline and replaced with new or updated services. The deployment of these new services is generally responsible for nearly half of the organizations’ new high or critical cloud exposures every month.
- **Remote access exposures are widespread.** Over 85% of organizations analyzed had Remote Desktop Protocol (RDP) internet-accessible for at least 25% of the month, leaving them open to ransomware attacks or unauthorized login attempts.
- **Cloud is the dominant attack surface.** A vast 80% of medium, high, or critical exposures belonging to the organizations analyzed were observed on assets hosted in the cloud.

---

## Attackers Move at Machine Speed

Attack surfaces are constantly changing, making it difficult for security teams to secure them. Defenders must remain vigilant as every configuration change, new cloud instance, and vulnerability disclosure present an opportunity for attackers. Today’s attackers have the ability to scan the entire IPv4 address space for vulnerable targets in minutes.

As we will explore in this report, attackers have been observed exploiting vulnerabilities in the wild within hours of their public disclosure. According to previous research, we found that on average, an organization takes more than three weeks to investigate and remediate a critical exposure.[^1] Even the largest, most-sophisticated, and best-resourced security teams struggle to remediate critical exposures as quickly as attackers can test and field new capabilities.

![Figure 1: Time elapsed before the first reported attack against 30 vulnerabilities exploited by a known threat actor in the last 12 months]

### Ransomware Threat Actors Exploit Critical Vulnerabilities Within Hours of Publication
Unit 42 analyzed 15 remote code execution (RCE) vulnerabilities actively used by ransomware operators. These CVEs were selected based on intelligence information about the threat actor group and their active exploitation within 12 months of publication. Threat actors targeted three of these critical RCE vulnerabilities within hours of disclosure, and six of the vulnerabilities were exploited within eight weeks of publication.

![Figure 2: Time elapsed before the first reported ransomware attack against 15 RCE vulnerabilities by a known threat actor in the last 12 months]

---

## Top Attack Surface Exposures

There are two broad categories of risks associated with the compromise of an internet-accessible asset for an organization:

1. **Risks related to attacker actions taken on a compromised device:** Examples include exfiltration of internet-accessible corporate laptop, ransomware attacks that disrupt payments processing, and physical damage from a compromised building control or industrial control system.
2. **Risks related to how an attacker can leverage unauthorized access:** Examples include moving laterally across an internal subnet to exfiltrate data from a critical datastore, compromising virtual private network (VPN) infrastructure to access and infect source code repositories in supply chain attacks, and using a compromised IP security camera to record employees physically entering login credentials.

![Figure 3: Distribution of exposure categories observed across the 250 organizations in the last 12 months]

- **Web framework takeover exposures** make up 22% of exposures observed.
- **Remote access services** account for 20% of exposures.
- **IT and networking infrastructure exposures** comprise 17% of exposures.
- **File sharing exposures** account for 12% of exposures.
- **Database exposures and vulnerabilities** make up 9% of exposures.

---

## Remote Access Exposures Lead to Ransomware

According to the 2022 Unit 42 Incident Response Report, the top suspected means of initial access for ransomware cases investigated by Unit 42 are software vulnerabilities (48%), followed by brute-force credential attacks (20%).[^2]

![Figure 4: Top five most common exposed remote access services by geography in the last 12 months]

Unit 42 found that the average national government organization had internet-accessible RDP exposures for 10 distinct days in a month. Eight of the nine industries that Unit 42 studied had internet-accessible RDP vulnerable to brute-force attacks for at least 25% of the month.

---

## Cloud Dynamism Is Straining Security Controls

Cloud-based IT infrastructure is always in a state of flux—on average over 20% of externally accessible cloud services change every month across the 250 organizations.

![Figure 5: Median proportion of new services introduced by a typical company in each industry during a given month]
![Figure 6: Median proportion of cloud-hosted exposures that are high risk observed on a typical company’s attack surface in each industry during a given month]

---

## Cloud Exposures Dominate Most Organizations’ Security Risks

According to our analysis, 80% of security exposures were observed in cloud environments.

![Figure 7: Distribution of exposures (Critical, High, Medium) in the cloud versus on-premises in 2022]
![Figure 8: Distribution of different categories of Exposures (Critical, High, Medium) in the Cloud vs. On-Premises in the last 12 months]

---

## Industry Attack Surface Breakdown

- **High Technology**: Insecure implementation of SSH servers is the leading contributor to remote access exposures.
- **National Governments**: File sharing and database exposures account for over 46% of all exposures.
- **Professional and Legal Services**: Unencrypted FTP servers are ubiquitous, opening avenues for data compromise.
- **Healthcare**: High rate of publicly exposed development environments.
- **Utilities and Energy**: Internet-accessible IT infrastructure control panels account for nearly one out of two exposures.
- **Manufacturing**: IT, security, and networking infrastructure are the most prevalent risks.
- **Education**: High exposure of IT, security, and networking infrastructure, followed by file-sharing services.
- **US State and Local Governments**: Remote access services are responsible for 24% of risks.
- **Transportation and Logistics**: Database exposures are responsible for one out of every four critical issues.
- **Finance**: Financial institutions most frequently expose file-sharing services.
- **Wholesale and Retail**: Remarkably high proportion of remote access services.

---

## Conclusion

Organizations across all industries face significant challenges and risks due to growing attack surfaces. Modern threat actors are experts at exploiting the path of least resistance to gain access to victims’ environments. To manage and secure their attack surfaces, organizations must adopt a proactive and holistic approach.

---

## Recommendations

- **Gain continuous visibility over all assets**: Ensure a comprehensive, real-time understanding of all internet-accessible assets.
- **Secure remote access services**: Implement strong authentication methods, such as MFA.
- **Prioritize remediation**: Focus on addressing the most critical vulnerabilities and exposures.
- **Address cloud misconfigurations**: Regularly review and update cloud configurations.
- **Monitor for emerging threats**: Stay informed about new vulnerabilities, exploits, and threat actors.
- **Get the help you need**: Consider a Unit 42 Attack Surface Assessment to jump-start your program.

---

## Methodology

Unit 42 and Cortex Xpanse collected petabytes of information on internet-accessible exposures across 250 organizations between March 31, 2022, and March 31, 2023. The research team used a rolling 10-day median to eliminate outlier bias. On-premises assets were defined as publicly accessible systems with statically assigned IP addresses, while cloud assets were defined as systems leased in dynamic IP space.

---

[^1]: 2021 Cortex Xpanse Attack Surface Threat Report, Palo Alto Networks, May 10, 2021.
[^2]: 2022 Unit 42 Incident Response Report, Palo Alto Networks, July 26, 2022.