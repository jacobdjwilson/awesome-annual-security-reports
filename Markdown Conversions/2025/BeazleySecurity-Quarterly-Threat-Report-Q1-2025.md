# Quarterly Threat Report: First Quarter, 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Q1 2025 Key Takeaways](#q1-2025-key-takeaways)
- [Ransomware Overview](#ransomware-overview)
- [Ransomware Incident Trends](#ransomware-incident-trends)
  - [Initial Access Resulting in Ransomware Deployments](#initial-access-resulting-in-ransomware-deployments)
  - [Abusing Windows Defender Access Control (WDAC)](#abusing-windows-defender-access-control-wdac)
- [Beazley Security MDR Trends and Overview](#beazley-security-mdr-trends-and-overview)
- [Vulnerability Trends and Overview](#vulnerability-trends-and-overview)
  - [Edge Device and Service Vulnerabilities](#edge-device-and-service-vulnerabilities)
  - [Supply Chain Attacks Due to Zero-Days](#supply-chain-attacks-due-to-zero-days)
- [Key Observations in the Threat Landscape](#key-observations-in-the-threat-landscape)
  - ["Oracle Cloud Classic" Data Breach](#oracle-cloud-classic-data-breach)
  - [Fake Snail Mail Extortion Letters](#fake-snail-mail-extortion-letters)
  - [Firewall Configurations Leaked in Cybercrime Forum](#firewall-configurations-leaked-in-cybercrime-forum)
- [Sources and Beazley Security Labs Publications](#sources-and-beazley-security-labs-publications)

---

## Executive Summary

The first quarter of 2025 brought an escalation in observed ransomware activity, as threat actors adapted their tactics and broadened their victim profiles. Beazley Security observed nearly a 35% increase in ransomware victims published on leak sites – many linked to ransomware operators launching large-scale exploitation campaigns against zero-days.

This report also tracks the evolving nature of how attackers are gaining initial access to target environments. Many incidents started with stolen credentials or by exploiting critical software flaws in internet-facing systems such as firewalls and file transfer tooling. In one emerging trend, attackers have begun abusing built-in windows features to disable advanced security software such as Windows Defender Application Control (WDAC) to disable Endpoint Detection and Response (EDR) solutions in order to evade prevention and detection solutions during ransomware attacks (read blog). In another campaign, ransomware actors compromised remote support tooling leading to crippling supply chain attacks. Beazley’s incident response and MDR teams were on the front lines of these developments, providing rapid containment while tracking threat actor tactics as they evolved.

This quarter also saw an uptick in deceptive tactics such as fake CAPTCHA validation pages tricking users into running malicious commands to aid in initial access through infostealer malware and a rise of fraudulent extortion letters claiming to have compromised organizations sent by traditional mail underscoring the creativity of the threat landscape.

As trends in this report demonstrate, the ransomware ecosystem continues to mature rapidly. Organizations must remain vigilant with layered defenses, strong phishing protections, modern MFA deployments, faster patching of internet-facing vulnerabilities, and awareness of supply chain risks.

## Q1 2025 Key Takeaways

- Ransomware activity on leak sites up 35% in Q1, aided by widespread exploitation of Zero-day vulnerabilities
- Cl0p Ransomware group most active with 373 victims posted on leak site
- Compromised VPN credentials lead to 56% of observed ransomware deployments, reinforcing the value of strong MFA requirements
- A 22% rise in the number of actively exploited vulnerabilities in Q1
- Newer ransomware groups such as Fog and Interlock are gaining traction, expanding ransomware ecosystem
- Emerging EDR Killer technique abusing Windows Defender Access Control (WDAC) policies is observed in the wild by Beazley Security
- Fake CAPTCHA scams tricking users into running malicious commands have expanded significantly as effective initial access method
- Supply chain compromise via vulnerable third-party software, such as SimpleHelp become a key trend
- Beazley Security’s MDR service saw most threats contained in early- to mid-attack stages, with credential access and discovery as top tactics
- Oracle “legacy cloud” breach led to significant investigation by the information security community and Beazley Security
- Firewall configuration leaks and growing access broker markets may fuel future compromise

## Ransomware Overview

The ransomware landscape in Q1 2025 was marked by high activity and evolving techniques amongst threat actors. Beazley Security observed and responded to multiple ransomware engagements throughout the quarter, with threat actors continuing to maximize impact and ransom demands. The total number of victims posted on public data leak sites increased approximately 35% from last quarter, with Cl0p ransomware operators emerging as the most active - publicly posting 373 victims due to a large scale zero-day campaign documented later in this report. Beazley Security has also been trending evolving initial access tactics used by these ransomware actors, with the usage of stolen but valid credentials being used most frequently to gain access to a victim’s network, as detailed in the Ransomware Incident Trends section below.

Other points of interest include:
- Beazley Ransomware claims have increased in the first quarter of 2025, up nearly 16% as compared to the fourth quarter of 2024.
- Healthcare and Business Service sectors reflected the greatest increase, accounting for ~ 22% and ~15 % of claims this quarter respectively.
- Professional Services dropped from Q4 with a significant 37% reduction in claims for Q1 of 2025, however this sector still accounts for a large percentage of total claims demonstrating it continues to be a high value target.

## Ransomware Incident Trends

Of the ransomware incidents responded to this quarter, Beazley Security documented activity by threat actor, as well as documenting the patterns of initial access and deployment techniques used. The most frequent ransomware actors for the quarter included the following:

- RansomHub activity remained relatively similar this quarter with 234 reported victims on their data leak site. This consistency parallels the group’s reputation and large operation at scale.
- Akira ransomware saw a significant uptick in activity, with a 66% increase in purported victims reported on their leak site since Q4, 2024. Researchers have started attributing the increase to a broader focus in victimology, including small and medium-sized businesses and different industries.
- Fog ransomware is a relatively new ransomware group initially observed in May of 2024 that has quickly claimed over 90 victims on their leak site since January of this year. Most notably, Fog victim counts increased more than 36% from Q4 2024.

### Initial Access Resulting in Ransomware Deployments

Understanding initial access methods used by threat actors is critical to helping prevent future ransomware attacks. But discovering initial access can be complex as organization often do not have detailed log or telemetry data to fully enable our investigations. Additionally, threat actors actively attempt to delete log data in attempts to clear their tracks and thwart investigations.

In Q1 Beazley Security incident responders tracked compromised, valid credentials as the leading initial access method. Often, internet facing services such as SSL VPNs and Remote Desktop Services (RDS) are targeted once credentials are obtained – either through social engineering or purchased from initial access brokers. In some cases, management and service accounts lacking MFA were discovered or brute forced to gain access.

Beazley Security also saw the continued successful exploitation of critical vulnerabilities that target edge devices and services in Q1. Ransomware operators were observed launching campaigns that targeted vulnerable appliances such as firewalls, remote management software suites, and file transfer solutions in attempt to infiltrate protected networks.

Firewalls, and some edge services, run on appliances that may not be compatible with modern EDR technology. This makes intrusion and post exploitation activity harder to monitor and detect.

Several of the more prevalent exploits ransomware actors successfully leveraged during the quarter include the following:

| Actor | Exploitation Campaign |
| :--- | :--- |
| Akira | SonicWall appliances targeting CVE-2024-53705 |
| Fog | SonicWall appliances targeting CVE-2024-53705 |
| Cl0p | Cleo file transfer suites targeting CVE-2024-50623 |
| Medusa | SimpleHelp RMM targeting CVE-2024-57727 |

### Abusing Windows Defender Access Control (WDAC)

Along with the significant trend of ransomware actors leveraging stolen credentials and weaponizing zero-day exploits, Beazley Security observed an emerging technique leveraged by ransomware operators for defense evasion and to persist in environments. The technique leverages built in Windows Defender capabilities to disable multiple modern EDR vendors.

The situation unfolded like this. In February, Beazley Security responded to a ransomware incident where the threat actor was able to subvert a market-leading Endpoint Protection Platform (EPP) to deploy ransomware. Embargo ransomware operators were discovered leveraging a built-in Windows security feature known as Windows Defender Application Control (WDAC) to disable the EPP tooling. As confirmed with further research and testing, the built-in WDAC capabilities were able to completely disable several market-leading EPP solutions, allowing actors to not only deploy ransomware but exfiltrate customer data and limit the telemetry available to responders.

The Beazley Security Labs (BSL) team worked to identify this behavior and has released a blog post extensively detailing the emerging technique. The BSL team has since worked directly with other security researchers investigating this activity, as well as with EPP vendors to ensure they can prioritize detection and mitigation capabilities.

## Beazley Security MDR Trends and Overview

During Q1, Beazley Security MDR teams responded to a breadth of incidents across client environments, with most response activity occurring in early- and mid-stages. As noted in the graphic, initial access (~16%), discovery (~14% ), and credential access attempts (~11%) were the most observed MITRE ATT&CK tactics.

This reflects a strong emphasis on threat actors attempts to perform reconnaissance and continuous attempts to move laterally within target environments. The monitored activity is consistent with opportunistic, automated campaigns conducted by attackers attempting to abuse initial access methods expand existing footholds quickly. Another method observed was attempting initial compromise through the usage of infostealers. Many infostealer deployments are attempted right after a user is tricked into clicking a phishing link or downloading malicious files.

Middle stage activity included privilege escalation, execution, persistence, defense evasion, and lateral movement attempts which reflected substantial adversary effort to gain control within an enviornment. Activities contained by Beazley Secuity MDR include attempts to trick end users into downloading and deploying malicious payloads, including advanced infostealers via fake CAPTCHA attacks, which was documented in a recent blog post.

Late-stage behavior such as collection, establishing C2 connectivity, and dropping ransomware lockers highlight incidents where adversaries were able to obtain the level of access necessary to attempt data theft or operational disruption. These circumstances sometimes occur when an organization suffered from a compromised trusted 3rd party, or if the victim’s environment lack critical controls such as hardened authentication mechanisms, or logging and monitoring that would help either prevent initial access or detect threat activities within an environment.

| Actor | % | Exploitation Campaign |
| :--- | :--- | :--- |
| Early-Stage | 48% | Usage of credential access attempts and discovery attacks detected and contained |
| Middle-Stage | 38% | Attempts to sustain and expand adversarial control in environments contained |
| Late-Stage | 14% | Critical threats such as data exfiltration and ransomware deployments contained |

## Vulnerability Trends and Overview

Beazley Security Labs monitors the daily reporting of software vulnerabilities to NIST, which can be in the thousands each month. From these, our research focuses on investigating high-impact vulnerabilities that are remotely reachable, and in products that see heavy use from our client base to provide targeted advisories and mitigations.

Below is a quarter over quarter comparison of publicly disclosed vulnerability activity for Q1.

| Vulnerability | Q1 2025 | Change from Q4 |
| :--- | :--- | :--- |
| New CVEs published by NIST | 12,066 | + 8.69% |
| CVEs added to CISA KEV | 45 | + 22% |
| Critical zero-day advisories published by BSL | 8 | + 60% |

*\*Critical BSL advisories are made publicly available here.*

In Q1, the number of new CVE’s published by NIST rose to 12,066 – an 8.69% increase. More significantly, the number of vulnerabilities added to CISA’s Known Exploited Vulnerabilities (KEV) catalog outpaced new CVEs, increasing 22%. This increase signals a growing focus by threat actors to actively develop and leverage exploits in the wild. As ransomware groups and their affiliates grow through extortion campaigns, Beazley Security expects that threat actors will continue to reinvest ransom payments into capabilities such as purchasing or developing new exploits which will likely result in a faster exploitation cycle.

Also highlighted in this quarter’s trends is the critical need for organizations to adopt a risk-based prioritization strategy when remediating vulnerabilities, particularly focusing on zero-day exploits and those impacting internet-facing services or network appliances. Beazley Security has seen attempted exploitation of internet facing devices within hours of vulnerabilities being disclosed by vendors.

### Edge Device and Service Vulnerabilities

Beazley Security Labs continues to monitor ransomware actors use of zero-day exploits to gain initial access to their victims.

In an example case, internet facing FortiGate firewall devices became the suspected initial access point in a client’s environment. The victim engaged Beazley Security to perform a compromise assessment after they noticed random, unauthorized administrative accounts had been created on firewall appliances. On investigation, forensic evidence pointed to the abuse of a remote authentication bypass vulnerability in Fortinet’s software which we discussed in the following BSL advisory: CVE-2024-55591.

Another significantly impactful zero-day exploitation campaign was the confirmed exploitation of VLTrader, an internet-facing file transfer service authored by Cleo. Cleo’s software has since been patched but Beazley Security has continued to observe the ransomware group Cl0p opportunistically target victims with this exploit.

BSL released this advisory outlining the vulnerability and risks (CVE-2024-55956).

### Supply Chain Attacks Due to Zero-Days

In Q1, BSL released an advisory regarding active exploitation of a critical vulnerability (CVE-2024-57727) impacting the remote monitoring and management (RMM) software suite SimpleHelp. Shortly after, Beazley Security was engaged in related Medusa ransomware cases, attributing initial access to SimpleHelp exploitation. In the observed cases, victims were not actually hosting vulnerable SimpleHelp servers but were instead running client software that connected back to third-party vendor support systems.

Medusa’s campaign targeted third-party vendors using a SimpleHelp exploit to gain access to vulnerable SimpleHelp servers. The actor then used the compromised servers to hijack clients connected, seamlessly abusing an update mechanism in the software to connect back to threat-actor managed SimpleHelp infrastructure. Once connected to the malicious SimpleHelp server, the threat actor was able to transparently establish a persistent command-and-control (C2) connection through the otherwise legitimate SimpleHelp client and leverage the compromised assets to move laterally in the victims’ environments, eventually exfiltrating data and deploying ransomware.

The exploitation underscores the importance of understanding third-party exposure and supply chain risks. In these cases, victim organizations were relying on external vendors for support, and vulnerabilities within the third-party applications to facilitate that support were exploited to serve as an entry point into their environments.

## Key Observations in the Threat Landscape

### "Oracle Cloud Classic" Data Breach

On March 20, a user on the cybercriminal forum BreachForums claimed to have compromised Oracle Cloud Infrastructure authentication servers, offering access to approximately 6 million credentials and authentication data for 100,000 Monero (XMR). The actor “Rose87168” provided sample data to substantiate this claim, with an offer to remove compromised accounts from the dataset for an unspecified fee.

While Oracle initially adamantly denied any breach occurred, security researchers continued to validate there was likely some form of unauthorized access to a subset of Oracle’s cloud identity systems. As evidence mounted, Oracle eventually acknowledged that “two obsolete servers” (That Beazley Security assessed were still in use to authenticate to Oracle Cloud Classic) had been compromised. The company stated the servers contained encrypted and hashed passwords and that no actual customer environments were accessed by the attacker.

The breach ultimately raised concerns for both Oracle customers and the cybersecurity community due to the nature of potentially compromised LDAP authentication data and Oracle’s lack of transparency during the incident. The incident highlights the importance of timely and transparent communications of a cybersecurity incident, with many still requesting additional details from Oracle. More information into Beazley Security’s research on this event is available on our blog.

### Fake Snail Mail Extortion Letters

Fake letters were reportedly distributed late February claiming to have come from the ransomware group BianLian. These letters targeted executives of organizations and alleged that their networks had been breached. Within the letter, a bitcoin payment address and QR code were provided. In letters observed by Beazley Security responders, a ransom of $250,000 was requested which, if not paid within 10 days, would result in the victim’s data being published to a public leak site for download. Security researchers eventually concluded that these letters were fakes, as none of the organizations appear to have been posted on the real BianLian ransomware leak site.

The FBI eventually released a public service announcement warning of the traditional mail scam.

### Firewall Configurations Leaked in Cybercrime Forum

Q1 proved a tough quarter for Fortinet clients. On top of several FortiOS vulnerabilities being actively exploited, over 15,000 compromised firewall configurations were dumped and made available to download on the popular cybercrime forum BreachForums. Firewall configurations contain several pieces of sensitive information, such as internal network mappings, administrative information, and even credentials to access a network.

Beazley Security Labs sampled the data and confirmed administrative username and password pairs were made available within the dump. Additional information on that analysis was discussed on BSL’s blog. As the situation developed, it was speculated among researchers that this data had likely been gathered over time by exploiting an old Fortinet vulnerability from 2022 (CVE-2022-40584), known to be exploited in the wild to download firewall configurations. Another interesting observation made by researchers is that the only country exempt of victim configurations was Iran.

Beazley Security has routinely observed ransomware operators leverage stolen, valid credentials against perimeter network devices to gain an initial foothold into a victim’s environment. Often these credentials are harvested and made for sale on criminal forums by initial access brokers (IABs). In this case, thousands of aggregated configurations were dumped for free, which could mean potential fallout for years to come.

## Sources and Beazley Security Labs Publications

- [https://labs.beazley.security/advisories/BSL-A1107](https://labs.beazley.security/advisories/BSL-A1107)
- [https://labs.beazley.security/advisories/BSL-A1115](https://labs.beazley.security/advisories/BSL-A1115)
- [https://labs.beazley.security/advisories/BSL-A1110](https://labs.beazley.security/advisories/BSL-A1110)
- [https://labs.beazley.security/advisories/BSL-A1104](https://labs.beazley.security/advisories/BSL-A1104)
- [https://labs.beazley.security/articles/disabling-edr-with-wdac](https://labs.beazley.security/articles/disabling-edr-with-wdac)
- [https://labs.beazley.security/advisories/BSL-A1106](https://labs.beazley.security/advisories/BSL-A1106)
- [https://www.fortinet.com/blog/psirt-blogs/update-regarding-cve-2022-40684](https://www.fortinet.com/blog/psirt-blogs/update-regarding-cve-2022-40684)
- [https://www.bleepingcomputer.com/news/security/oracle-says-obsolete-servers-hacked-denies-cloud-breach/](https://www.bleepingcomputer.com/news/security/oracle-says-obsolete-servers-hacked-denies-cloud-breach/)
- [https://www.ic3.gov/PSA/2025/PSA250306-2](https://www.ic3.gov/PSA/2025/PSA250306-2)

---

![Additional reports and factsheet navigation footer links including Third-Party Risk Monitoring Factsheet, Quarterly Threat Report First Quarter 2026, and Quarterly Threat Report Fourth Quarter 2025]

Privacy Policy  
©2026 Beazley Security is a wholly owned subsidiary of Beazley plc, providing cyber security services. Beazley Security does not provide insurance products or services, nor does it provide legal services or advice. Customer information may be shared between Beazley Security and Beazley plc and/or its affiliates and subsidiaries; however, such information will not be used to inform the underwriting or claims decisions of any Beazley insurance affiliate, unless the customer agrees to disclose such information for that purpose.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
