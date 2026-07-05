# RESEARCH REPORT: ENERGY SECTOR EXPOSURE ASSESSMENT

A comprehensive evaluation of 21 of the leading energy providers in the U.S.A. to understand security posture, identify systemic risks, and provide valuable insights to security leaders within the energy industry.

© 2025 SixMap, Inc. All rights reserved.

## Table of Contents
- [Methodology](#methodology)
- [Executive Summary](#executive-summary)
- [Overview of Findings](#overview-of-findings)
- [Hidden Exposures](#hidden-exposures)
- [Vulnerable Services](#vulnerable-services)
- [Vulnerabilities By Severity](#vulnerabilities-by-severity)
- [Vulnerability Distribution](#vulnerability-distribution)
- [Systemic Risks](#systemic-risks)
- [IPv6 Exposure](#ipv6-exposure)
- [Threat Actor Analysis](#threat-actor-analysis)
- [Silent Chollima](#silent-chollima)
- [ExCobalt](#excobalt)
- [Ethereal Panda](#ethereal-panda)
- [Circuit Panda](#circuit-panda)
- [Ryuk](#ryuk)
- [Tunnel Snake](#tunnelsnake)
- [Conclusion](#conclusion)
- [Appendix](#appendix)
- [About SixMap](#about-sixmap)

---

## Methodology
The goal of this project is to understand the cybersecurity posture of large organizations in the energy sector, identify potential trends that may indicate systemic risk, and provide data-based guidance to security leaders at other organizations within the industry.

To conduct this research, SixMap assessed the external exposures of 21 of the leading energy providers in the U.S.A. SixMap examined all domains and IP addresses, across both the IPv4 and IPv6 spaces, associated with each organization, as well as the ports and services exposed on each asset. For completeness and accuracy of data, all 65,535 ports were inspected.

This research did not engage in any intrusive or harmful activity. Only publicly available data obtained from Internet-facing systems was used for the purposes of this research. As such, this external vantage point cannot see internal mitigating controls that would minimize the damage in the event of attack or exploitation.

SixMap is uniquely positioned to collect and analyze this dataset for several reasons. First, SixMap owns and operates an Internet Service Provider (ISP), which enables exposure assessments to run in an efficient way that provides comprehensive data without causing latency, degrading service response, or creating noise on the networks of the organizations under evaluation.

Second, SixMap uses an innovation called Computational Mapping to enable precise host discovery across the IPv4 and IPv6 address spaces. While many organizations are certain they do not have any IPv6 assets, the discovery process routinely finds IPv6 addresses in use for almost every large organization assessed.

Finally, SixMap inspects all 65,535 ports on each asset, every scan. This provides more complete data and uncovers many exposed services that would not be detected through typical tooling that only checks the top 1,000 to 5,000 most commonly used ports.

---

## Executive Summary
As a major component of American critical infrastructure, the energy industry in the United States is highly targeted by both state-sponsored and financially-motivated cyber threat groups. Energy sector enterprises face an increasingly hostile threat landscape and must therefore pay close attention to all the exposures that could be uncovered and targeted by bad actors.

Among the 21 energy sector organizations evaluated for this research project, SixMap identified 39,986 hosts with a total of 58,862 services exposed to the Internet. Approximately 7% (3,910) of all exposed services are running on non-standard ports beyond the top 5,000 most commonly used ports. These 7% of exposures represent potential blind spots, as non-standard ports fall outside the scope of traditional attack surface management and vulnerability management tools.

SixMap found a total of 5,756 vulnerable services with CVEs across all exposures. Many CVEs were detected numerous times. This is true in two ways: several instances of the same CVE within the same organization’s environment and several detections of the same CVE in the external attack surfaces of multiple different organizations.

Of the 5,756 CVEs detected, 377 are known to be exploited in the wild, meaning the presence of those CVEs introduces a serious risk and high likelihood of exploitation.

There are 43 different CVEs common to 45% or more of the organizations in the sample group, potentially representing systemic risks for the energy sector.

A total of 304 vulnerable services (231 unique CVE IDs) are running on non-standard ports. 21 of those CVEs are known to be exploited by specific threat groups. This may represent a major challenge for the energy sector, as many industry-standard exposure management products only scan the top 5,000 most common ports by default. If a vulnerable service is running on a non-standard port, it would not be detected by these traditional tools, leaving a high-risk CVE invisible to the security team.

### KEY RECOMMENDATIONS:
- **Regularly scan all 65,535 ports** to uncover vulnerable services on non-standard ports.
- **Ensure vulnerability management** routinely updates vulnerable services.
- **Prioritize vulnerabilities** based on risk severity and known exploitation activity.
- **Gain visibility on IPv6 assets** to avoid unknown assets from introducing serious risk.

---

## Overview of Findings
![Chart showing IPv4 vs IPv6 space distribution]
- **Total Number of Hosts**: 39,986
- **Average Number of Hosts Per Organization**: 1,904
- **Average Number of IPv6 Hosts Per Organization**: 107

![Chart showing Standard vs Non-Standard ports]
- **Total Exposed Services**: 58,862
- **Total Exposed Services on Non-Standard Ports**: 3,910 (7%)
- **Average Exposed Services On Non-Standard Ports Per Org**: 186

![Chart showing Distribution of CVEs by Service]
- **Total CVEs Found**: 5,756
- **Total CVEs Tied to Threat Actors**: 377 (6.6%)
- **Total CVEs on Non-Standard Ports**: 304

---

## Hidden Exposures
SixMap identified a grand total of 58,862 open ports with services exposed to the Internet across the 21 energy organizations assessed. A total of 3,910 services, or about 7%, were running on non-standard ports that fall outside of the top 5,000 most common ports.

### Hypertext Transfer Protocol (HTTP)
- Total of 245 instances of http running on non-standard ports.
- Sample Non-Standard Ports Found: Port 8172 (117 instances), Port 65503 (22 instances), Port 65504 (22 instances), Port 6363 (8 instances), Port 10443 (4 instances).

### Real-Time Streaming Protocol (RTSP)
- Total of 119 instances of rtsp running on non-standard ports.
- Sample Non-Standard Ports Found: Port 55402 (11 instances), Port 55401 (11 instances), Port 55403 (10 instances), Port 55404 (10 instances), Port 10558 (9 instances).

### Secure Shell Protocol (SSH)
- Total of 16 instances of ssh running on non-standard ports.
- Sample Non-Standard Ports Found: Port 232 (4 instances), Port 18765 (3 instances), Port 252 (2 instances), Port 7822 (2 instances), Port 56383 (2 instances).

### Simple Mail Transfer Protocol (SMTP)
- Total of 12 instances of smtp running on non-standard ports.
- Sample Non-Standard Ports Found: Port 26 (12 instances).

### Memcached Protocol (Memcached)
- Total of 4 instances of memcached running on non-standard ports.
- Sample Non-Standard Ports Found: Port 11222 (2 instances), Port 22122 (2 instances).

### MQ Telemetry Transport Protocol (MQTT)
- Total of 1 instance of mqtt running on non-standard ports.
- Sample Non-Standard Ports Found: Port 8883 (1 instance).

### Transmission Control Protocol - Wrapped (TCPWrapped)
- Total of 45 instances of tcpwrapped running on non-standard ports.
- Sample Non-Standard Ports Found: Port 8013 (12 instances), Port 49152 (6 instances), Port 6556 (4 instances), Port 8020 (2 instances), Port 5227 (1 instance).

### Hypertext Transfer Protocol - Proxy (HTTP-Proxy)
- Total of 40 instances of http-proxy running on non-standard ports.
- Sample Non-Standard Ports Found: Port 8020 (35 instances), Port 8015 (2 instances), Port 8899 (1 instance), Port 7563 (1 instance), Port 11388 (1 instance).

### Universal Plug and Play Protocol (UPnP)
- Total of 36 instances of upnp running on non-standard ports.
- Sample Non-Standard Ports Found: Port 10100 (10 instances), Port 10200 (10 instances), Port 10201 (10 instances), Port 6391 (2 instances), Port 6390 (2 instances).

---

## Vulnerable Services
SixMap found a total of 5,756 vulnerable services across the 21 energy sector organizations. About 76% of these vulnerabilities were with various implementations of HTTP. SSH is of particular risk, as exploiting SSH often results directly in full compromise of a system.

![Bar chart showing frequency of vulnerable services: SSH (4536), HTTP (883), DNS (158), SLP-Proxy (81), HTTP-Proxy (66), SMTP (42), Memcached (6), MQTT (4)]

---

## Vulnerabilities By Severity
Critical and High severity vulnerabilities represent the most risk of serious disruption to an organization. 

![Chart showing distribution of vulnerabilities by severity]

---

## Vulnerability Distribution
SixMap’s research found 5,756 vulnerabilities across 21 energy sector organizations, averaging 274 vulnerabilities per organization. One outlier organization has 2,875 vulnerabilities, likely due to shadow IT assets. Approximately 7% of all CVEs detected were on non-standard ports, suggesting a lack of visibility.

---

## Systemic Risks
SixMap found 43 unique CVEs that were present in the external attack surfaces of at least 10 of the 21 (45%) energy sector organizations evaluated.

- **CVE-2023-38408**: SSH, Critical, 16 companies (76.19%), Known Threat Actor: Silent Chollima.
- **CVE-2024-38476**: SSH, Critical, 16 companies (76.19%), Known Threat Actor: Silent Chollima.
- **CVE-2020-15778**: SSH, High, 16 companies (76.19%), Known Threat Actor: None.
- **CVE-2024-38472**: HTTP, High, 11 companies (52.38%), Known Threat Actor: None.

---

## IPv6 Exposure
Every single one of the 21 organizations evaluated has at least one IPv6 address in use. In total, there are 2,253 IPv6 addresses in use, representing about 6% of all discovered IP addresses. Because traditional exposure management tools cannot discover IPv6 hosts, this is an area of significant risk.

---

## Threat Actor Analysis
Only a small percentage (4% to 6%) of known CVEs are ever exploited in the wild. CVEs with known exploitation activity should never be present in the external attack surface.

---

## Silent Chollima
- **AKA**: APT45, Andariel, Onyx Sleet, Stonefly
- **Origin**: North Korea
- **Overview**: DPRK state-sponsored actor, initially espionage-focused, now increasingly financially motivated.
- **CVEs**: CVE-2017-0199, CVE-2018-4878, CVE-2020-0601, CVE-2021-26411.

---

## ExCobalt
- **AKA**: Cobalt Group, Carbanak Group, Gold Kingswood
- **Origin**: Russia
- **Overview**: Financially motivated cybercriminal group targeting financial institutions.
- **CVEs**: CVE-2017-0199, CVE-2018-8174, CVE-2018-4878, CVE-2019-0859.

---

## Ethereal Panda
- **AKA**: APT27, Emissary Panda, LuckyMouse, Bronze Union, TG-3390
- **Origin**: China
- **Overview**: State-sponsored APT group involved in cyber-espionage.
- **CVEs**: CVE-2017-11882, CVE-2015-2545, CVE-2014-4114.

---

## Circuit Panda
- **AKA**: APT18, TG-0416, Wekby
- **Origin**: China
- **Overview**: State-sponsored actor focused on healthcare and pharmaceutical espionage.
- **CVEs**: CVE-2014-6332, CVE-2015-4852, CVE-2014-0160.

---

## Ryuk
- **Names**: Wizard Spider, Grim Spider, UNC1878
- **Origin**: Russia
- **Overview**: Notorious ransomware group targeting large organizations for extortion.
- **CVEs**: CVE-2017-11882, CVE-2019-0803, CVE-2020-0688.

---

## TunnelSnake
- **AKA**: UNC5221, MosaicRegressor
- **Origin**: China
- **Overview**: APT group known for sophisticated attacks using custom rootkits.
- **CVEs**: CVE-2014-6332, CVE-2015-4852, CVE-2014-0160.

---

## Conclusion
The 21 large energy industry organizations evaluated have massive digital estates that are difficult to monitor. Limitations of traditional security tools—specifically those that only scan the top 1,000 or 5,000 ports—leave vulnerable services exposed in the shadows of non-standard ports. SixMap’s computational mapping technology provides the necessary visibility to mitigate these risks.

---

## Appendix
(Full list of 43 common CVEs provided in the original report tables.)

---

## About SixMap
SixMap provides the most accurate and complete external view of your organization. Our platform interrogates all 65,535 ports as standard operating procedure—across IPv4 and IPv6—continuously hunting unknown assets, misconfigurations, and blindspots.

**SixMap, Inc.**
6731 Columbia Gateway Dr Suite 100, Columbia, MD 21046
[sixmap.io](http://sixmap.io)