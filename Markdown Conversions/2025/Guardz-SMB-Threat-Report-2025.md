## Table of Contents
- [Report Content Below](#report-content-below)
- [The Current Threat Landscape](#the-current-threat-landscape)
- [From the SentinelOne perspective](#from-the-sentinelone-perspective)
- [Phishing & Business Email Compromise (BEC) Adapt with AI](#phishing--business-email-compromise-bec-adapt-with-ai)
- [Exchange Online Attack Overview](#exchange-online-attack-overview)
- [Identity-Based Attacks](#identity-based-attacks)
- [Industries in the Crosshairs](#industries-in-the-crosshairs)
- [Evolving Tactics and Emerging Threats](#evolving-tactics-and-emerging-threats)
- [Strategic Recommendations](#strategic-recommendations)

Phishing persists as the leading breach vector. Direct phishing incidents have declined as threat actors increasingly bypass “spray-and-pray” emails in favor of using stolen credentials for stealthy logins. Generative AI is supercharging social engineering, enabling attackers to craft eerily realistic phishing messages and deepfake voices at scale, fooling even tech-savvy users.

Cloud assets are under siege. As SMBs migrate data and infrastructure to the cloud, attackers follow. The vast majority of breaches now involve cloud-stored data. Password attacks on cloud accounts spiked tenfold, targeting cloud login portals. Threat actors aggressively seek cloud access tokens and keys. Weakly secured cloud apps and third-party services have contributed to a significant surge in recent cloud intrusions.

Evolving tactics and emerging threats include attackers increasingly leveraging legitimate tools for “living off the land” (LOTL) attacks to bypass antivirus, deepfake content, and AI-driven malware blurring truth and automating hacking tasks, session token hijacking and token theft, ransomware groups pivoting to pure data theft and extortion, and threat actors themselves leveraging generative AI to accelerate attack development.

In summary, the first half of 2025 underscores that SMBs are at the forefront of the cyber threat landscape. Attackers are drawn to SMBs’ valuable data and often limited defenses, employing both tried-and-true methods and cutting-edge techniques to achieve their aims. This report provides a detailed breakdown of key threat trends, targeted industries, attacker tactics, emerging threats, and strategic recommendations. MSPs and MSSPs should use these insights to reassess their risk posture and invest in resilience.
02

## The Current Threat Landscape
Ransomware Rampant as Extortion Grows

Ransomware continues to wreak havoc on organizations of all sizes, with SMBs
becoming an increasingly attractive target. Many small businesses falsely assumed
they were “too small to target,” only to find that a significant portion suffered from
many attempts, many involving ransomware. Ransomware-as-a-Service (RaaS)
operations have proliferated, enabling criminals to deploy ransomware at scale.

A few top ransomware gangs are responsible for almost half of all reported
attacks, reflecting a concentrated ecosystem. Attackers perceive SMBs as having
weaker defenses and limited incident response capabilities, making them easier
targets. Many SMB victims lack robust data backups or redundant systems,
increasing pressure to pay ransoms to restore operations. Ransomware incidents
rose globally and remain steady. Data exfiltration combined with ransomware
payloads – the “double-extortion” tactic – is now routine, meaning even
organizations with backups face extortion risks. Some threat groups skip
encryption altogether, relying solely on data theft extortion, accounting for about
one-quarter of breaches.

Downtime from ransomware can cripple daily business, with many SMB leaders
saying even one day of outage could shut down their company. Ransom and
recovery costs continue to rise, and while many incidents are more minor than
enterprise breaches, even a fraction of these costs can be devastating. Public
sector entities, including local governments and schools, have seen high-impact
attacks. Ransomware remains a top-tier threat in 2025, with adequate backups,
network segmentation, and incident response plans being critical to defense.

03

## From the SentinelOne perspective

From the SentinelOne perspective: In the recent SentinelOne threat intelligence
classification analysis, a total of 412 distinct threat groups were identified across the
monitored environment. The distribution of detections highlights the breadth of
malicious activity and the diversity of attack techniques in use.

Malware remains the most prevalent category, with 5,476 detections, underscoring its
continued dominance as a primary threat vector. Ransomware accounted for 556
detections, reflecting the sustained risk posed by encryption-based extortion
campaigns. Potentially Unwanted Applications (PUA) were identified in 252 instances,
indicating the presence of software that, while not overtly malicious, poses
operational and security risks due to unwanted behavior.

Cryptominer activity was observed in 164 detections, signaling attempts to exploit
computing resources for illicit cryptocurrency mining. Infostealer variants appeared in
79 cases, targeting sensitive information and credential theft. In 49 cases, flagged
activity was assessed as benign, requiring no immediate remediation.

Additionally, 27 detections involved hack tools, which are often leveraged in the
reconnaissance or exploitation phase of an attack chain. Packed binaries accounted
for 19 detections, suggesting the use of obfuscation and compression techniques to
bypass detection mechanisms.

This classification provides a clear operational picture of the active threat landscape,
enabling targeted response measures and informed risk prioritization.

Guardz Data
Insights

2.  5%

3.  3%

4.  1%

5476

Malware

556

Ransomware

164

Cryptominer

252

PUA

49

Benign

19

45

79

27

Packed

Virus

Infostealer

Hacktool

04

## Phishing & Business Email Compromise (BEC) Adapt with AI
Phishing remains the most prevalent initial attack vector in breaches, accounting for roughly one-fifth of incidents. SMBs are particularly vulnerable due to limited security training and high trust within small teams. However, generic phishing attacks have declined as attackers increasingly use stolen credentials to gain access quietly. Phishing is becoming more targeted and sophisticated.

Business Email Compromise (BEC) scams surged against SMBs, causing significant financial losses globally. BEC attackers impersonate trusted parties to request fraudulent payments or sensitive data. Employees at small businesses face significantly more social engineering attacks than those at larger companies. Generative AI is a game-changer, enabling cybercriminals to craft polished, personalized scam emails and deepfake voice impersonations. This technology increases the scale and believability of attacks, making detection harder. SMBs are responding by increasing security awareness efforts, but gaps remain. Phishing in 2025 remains a shape-shifting threat, still the most common attack vector, but increasingly more complex to detect.
05

## Exchange Online Attack Overview

Attack Category | Total Attempts | Avg. Severity | Primary Industry Target
--- | --- | --- | ---
Phishing | 1,876 | 4.3 | Financial Services
Business Email Compromise (BEC) | 1,423 | 4.7 | Financial Services
Al-Enhanced Attacks | 893 | 4.8 | Professional Services
Credential Harvesting | 1,247 | 4.5 | Healthcare
Supply Chain Compromise | 682 | 4.6 | Manufacturing

)'/1/,+.0*-

:9867

-0,1-

54328

-0+-(&0*/

Stolen credentials have become the
center of the cybercriminal playbook,
with over 80% of breaches involving
compromised credentials. Credential-
focused attacks surged dramatically
year-over-year. The underground
market is flooded with billions of
stolen usernames and passwords,
primarily harvested by information-
stealing malware. These infostealers
quietly harvest saved logins, browser
cookies, and authentication tokens
from infected devices, with usage
surging recently.

Alarmingly, a ma(cid:31)ority of SMBs do not
enforce multi-factor authentication,
leaving a massive security gap.
Attackers leverage stolen credentials
for stealthy logins, e(cid:4)tended dwell
times, privilege escalation, and lateral
movement. Session hi(cid:31)acking and
token theft techniques have become
widespread, allowing attackers to
impersonate authenticated users
without needing passwords or MFA.
Token-based attacks are increasing
rapidly, bypassing traditional
authentication mechanisms. SMB(cid:19)
and the MSPs that secure them must
urgently improve identity security by
enforcing MFA, using password
managers, monitoring for
compromised accounts, and adopting
#ero-trust principles.

06

## Identity-Based Attacks

Attack Type | Count | % of Total | Avg. Severity (1-5)
--- | --- | --- | ---
Password Spray | 576 | 18.9% | 4.6
Credential Stuffing | 437 | 14.4% | 4.7
MFA Bypass | 312 | 10.3% | 4.9
Legacy Authentication Abuse | 298 | 9.8% | 4.3
Account Takeover | 267 | 8.8% | 4.8
Subtotal | 1,890 | 62% | 4.7

Privilege & Access Abuse

Attack Type | Count | % of Total | Avg. Severity (1-5)
--- | --- | --- | ---
OAuth App Consent | 312 | 10.3% | 4.3
Credential Stuffing | 243 | 8.0% | 4.1
MFA Bypass | 187 | 6.1% | 4.9
Legacy Authentication Abuse | 156 | 5.1% | 4.5
Account Takeover | 134 | 4.4% | 4.2
Subtotal | 1,032 | 33.9% | 4.4

Microsoft 365 Most Targeted Applications

Application | Attack Count | % of M365 Attacks
--- | --- | ---
Outlook/Exchange | 1,247 | 41%
SharePoint | 623 | 20.5%
Teams | 532 | 17.5%
OneDrive | 378 | 12.4%
Power Apps | 262 | 8.6%
Total | 3,042 | 100%
