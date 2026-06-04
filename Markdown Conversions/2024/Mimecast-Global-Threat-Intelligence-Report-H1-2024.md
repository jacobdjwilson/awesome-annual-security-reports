# Global Threat Intelligence Report: January - June 2024

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [The Threatcast](#the-threatcast)
- [Major Events](#major-events)
- [Threat Landscape in Charts](#threat-landscape-in-charts)
- [Major Campaigns Targeting Mimecast Users](#major-campaigns-targeting-mimecast-users)
- [Recommendations](#recommendations)
- [Best Practices and Advisories](#best-practices-and-advisories)
- [Mimecast Recommendations/Checklist](#mimecast-recommendationschecklist)
- [Conclusion](#conclusion)

---

## Introduction
To adapt to the latest cyberthreats, organizations large and small need to leverage good threat intelligence, quickly update their cybersecurity processes and infrastructure, and harden defenses around their businesses’ communications, people, and data.

Mimecast generates threat intelligence through its analysis of more than 1.7 billion messages per day on behalf of more than 42,000 customers. Email and messaging are the channels through which most cyberthreats launch, allowing Mimecast to detect and analyze threats before they become widespread.

In this Global Threat Intelligence Report, Mimecast has distilled insights from our intelligence analysts for the first six months of 2024, combining our data with open-source intelligence from the cybersecurity community at large. The report includes analysis of threat activity, statistics revealing attack trends, and a series of recommendations for businesses of all sizes to better mitigate the risks of cyberthreats.

## Executive Summary
The first half of 2024 emphasized the French saying, “Plus ça change, plus c’est la même chose” — the more things change, the more they stay the same. 

The adoption of AI technology by both cyber attackers and defenders, for example, continues to promise massive changes in the way cybersecurity is conducted; so far, the impact has been limited on both sides. The battle for dominance of the cyber domain is unrelenting, as cybercriminal cloud services and as-a-service offerings continue to expand the availability of attack tools, phishing kits, and databases of stolen information. Law enforcement agencies have shown signs of adapting, with cross-jurisdictional collaboration resulting in the disruption of major groups.

Email continues to evolve as attackers reduce their reliance on malware attachments, opting for malicious links to legitimate cloud file-sharing services, such as SharePoint and Google Drive. A temporary surge in attacks against medium-sized businesses has subsided, with small-business users again seeing the most threats. And credential theft has become a major focus of attackers, who then sell stolen credentials on underground markets or use them in credential-stuffing attacks to gain access to businesses’ cloud services.

The future holds some predictable challenges. As companies further migrate to the cloud and develop their infrastructure, the overall attack surface has expanded. The growing dependency on data stored within the clouds means security control is increasingly blurred, while the inherent reliance on third-party software and infrastructure makes supply chain security a major problem. In the face of continued ransomware attacks, maintaining data confidentiality, integrity, and availability—the CIA triad of information security—is a key to successful business outcomes. Finally, generative AI and machine learning will improve the targeting and content of phishing campaigns, driving the defender’s requirement to be able to detect and quickly respond to new and novel attack techniques.

## Key Findings
1. **Messaging attacks evolve**: Shifting from pushing malware to using links, with more layers of links providing obfuscation from detection. This requires more interaction from victims, including clicking through more links and responding to CAPTCHAs and false multi-factor authentication requests.
2. **Industry targeting**: The banking, arts and entertainment, and travel and hospitality industries experienced the most malicious URL messages in Q2 2024, while the IT consulting and legal professional services sectors encountered the most spam and impersonation messages.
3. **Development services abuse**: Attackers are using development services, such as Replit, to host and develop campaigns. File-sharing services, including SharePoint and Google Drive, are also popular ways of hosting intermediate documents that link out to credential harvesting pages.
4. **Regional trends**: Impersonation attacks dominated threats targeting European users, while spam accounted for most attacks in Africa. The Asia-Pacific region saw a dramatic spike in attacks against small businesses.

## The Threatcast
This year promises surging spam, phishing, and disinformation attacks as a convergence of important world events conspires to produce plenty of subject matter from which to construct phishing lures and motivate attackers. In 2024, a massive election season kicks off with major votes in the United States and Europe, snap elections in France, and more democracies deciding their fate than in any previous year.[^1] The continuing Russian invasion of Ukraine and the conflict between Israel and Hamas in Gaza have resulted in significant surges in disinformation attempts. Major sporting events — from the Summer Olympics and Paralympics in Paris to the recent Euro 2024 and COPA America football tournaments — have attracted attacks from a variety of groups.

[^1]: 2024 is the biggest election year in history. The Economist. The World Ahead. 23 Nov 2023.

## Major Events
- **JAN: Trello leaks 15 million user records**
  - Vulnerability: Insecure public API
  - Impact: Email addresses fuel future attacks.
- **FEB: i-SOON insider leaks hacking info**
  - Vulnerability: Insider leak
  - Impact: Sensitive information about Chinese hacking operations made public.
- **MAR: Lockbit operation disrupted by global effort**
  - Vulnerability: Law enforcement action
  - Impact: Disruption of major cybercrime organization.
- **APR: CISA releases details of Microsoft email hack**
  - Vulnerability: Stolen signing key
  - Impact: Exposed sensitive emails of highly placed U.S. officials.
- **MAY: Insecure credentials leak data from Snowflake**
  - Vulnerability: Lack of multifactor authentication
  - Impact: Customer data leaked from cloud storage.
- **JUN: Disinformation attacks influence EU elections**
  - Vulnerability: Widespread misinformation
  - Impact: Increased polarization, potential impact on elections.

## Threat Landscape in Charts
![Chart showing Threats per User (TPU) by business size: Small, Medium, Large]
![Chart showing Threats per User by attack type: Spam, Malicious Links, Impersonation, Unknown Malware, Known Malware]
![Chart showing Top-5 Industries by TPU]
![Chart showing Top-10 File-Sharing Services used in attacks]
![Chart showing Top-10 Vulnerabilities used in attacks]

## Major Campaigns Targeting Mimecast Users
1. **BlackMatter Surge**: Targeting chemical and pharmaceutical scientists with links leading to ransomware.
2. **LinkedIn Redirect Abuse**: Using LinkedIn's redirect functionality to lead victims to fake Microsoft Outlook sign-in pages.
3. **SharePoint/Google Drive folders**: Using legitimate file-sharing sites to host phishing links.
4. **Using online AI tools**: Using Replit to host credential-stealing pages disguised as HR portals.
5. **Abusing Atlassian, Archbee, and Nuclino**: Using collaboration platforms as intermediate stages for redirection chains.
6. **Email scams backed by AI bot call centers**: Using automated LLM-powered call centers to collect information from consumers.

## Recommendations
1. **Block images in email messages**: Prevent the loading of images to evade phishing lures.
2. **Segment the network and log internal traffic**: Reduce lateral movement during ransomware attacks.
3. **Harden user credentials, deploy MFA**: Eliminate default passwords and enforce robust authentication.
4. **Provide awareness training**: Address human error as the first line of defense.
5. **Mandate more security from third parties**: Review service-level agreements and monitor suppliers.
6. **Scan external network for open ports**: Identify and close exploitable routes like RDP.

## Best Practices and Advisories
- **31 Jan 2024**: Hearing on CCP Cyber Threat (Volt Typhoon activity).
- **14 Feb 2024**: Staying Ahead of Threat Actors in the Age of AI (LLM experimentation by APT groups).
- **29 Mar 2024**: Reported Supply Chain Compromise Affecting XZ Utils (CVE-2024-3094).
- **2 Apr 2024**: Cyber Safety Review Board Releases Report on Microsoft Online Exchange Incident.
- **2 May 2024**: North Korean Actors Exploit Weak DMARC Security Policies.
- **26 Jun 2024**: Exploring Memory Safety in Critical Open Source Projects.

## Mimecast Recommendations/Checklist
- **Single sign-on**: Utilize SSO or Mimecast’s built-in MFA.
- **Auto-Allow Policies**: Set to 'strict' to ensure spam scanning is not bypassed.
- **Impersonation protection**: Optimize settings for C-Level/VIP policies.
- **Re-writing of URLs**: Ensure all URLs are scanned upon click.
- **End user reporting**: Encourage reporting of malicious messages to the SOC.
- **SIEM and XDR vendors**: Utilize pre-built integrations for log capture and analysis.

## Conclusion
The evolution of the threat landscape continues to challenge cybersecurity teams. Malicious links remain the preferred delivery method for payloads. Employees at small and medium businesses continue to see more than twice the number of threats compared to users at large enterprises. As companies migrate to the cloud, the attack surface expands, and the abuse of generative AI will likely improve the targeting and content of phishing campaigns. Maintaining data availability and focusing on the "human in the loop" remain critical to successful business outcomes.