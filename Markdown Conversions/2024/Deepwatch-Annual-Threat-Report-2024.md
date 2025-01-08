# Deepwatch Adversary Tactics and Intelligence (ATI) 2024 Annual Threat Report

## Table of Contents
- [Observations, Metrics, Trends & Forecast](#observations-metrics-trends-forecast)
- [Introduction](#introduction)
- [2023 Trends](#2023-trends)
- [2023 Observations](#2023-observations)
- [2023 Observations Quick Look](#2023-observations-quick-look)
- [Suspicious Activity and Account Compromise Dominated Incident Response Engagement](#suspicious-activity-and-account-compromise-dominated-incident-response-engagement)
- [Ransomware Still Continues to Affect Many Industry Sectors](#ransomware-still-continues-to-affect-many-industry-sectors)
- [Malware](#malware)
- [Exploitation of Critical Vulnerabilities for Internet-Facing Systems](#exploitation-of-critical-vulnerabilities-for-internet-facing-systems)
- [Top ATT&CK Techniques and Detections Observed in 2023](#top-attck-techniques-and-detections-observed-in-2023)
- [Top 5 MITRE ATT&CK Tactics Observed in 2023](#top-5-mitre-attck-tactics-observed-in-2023)
- [Top 5 Detections Observed in 2023](#top-5-detections-observed-in-2023)
- [Top Detections Observed in the Majority of Months in 2023](#top-detections-observed-in-the-majority-of-months-in-2023)
- [Cobalt Strike, MimiKatz, and Qakbot Among the Most Reported Malware](#cobalt-strike-mimikatz-and-qakbot-among-the-most-reported-malware)
- [Recommendations](#recommendations)
- [Perimeter (Internet Edge)](#perimeter-internet-edge)
- [Accounts](#accounts)
- [Network & Host](#network--host)
- [Disaster Recovery](#disaster-recovery)
- [2024 Forecast](#2024-forecast)
- [2024 Forecast Quick Look](#2024-forecast-quick-look)
- [Information Stealing Malware Will Continue to Become More Sophisticated](#information-stealing-malware-will-continue-to-become-more-sophisticated)
- [Mass Vulnerability Exploitation and Supply Chain Attacks Will Continue to be a Significant Threat](#mass-vulnerability-exploitation-and-supply-chain-attacks-will-continue-to-be-a-significant-threat)
- [Techniques Involving External Remote Services, User Execution, and Application Layer Protocol Will Continue to be Widely Observed](#techniques-involving-external-remote-services-user-execution-and-application-layer-protocol-will-continue-to-be-widely-observed)
- [Prevalence of AI in Malleable Tool Performance and Defense Evasion](#prevalence-of-ai-in-malleable-tool-performance-and-defense-evasion)
- [Abuse of Legitimate Internet Services Will Continue, Likely Escalating in 2024](#abuse-of-legitimate-internet-services-will-continue-likely-escalating-in-2024)
- [Rise of Non-Malware-Based Cyber Attacks in 2024](#rise-of-non-malware-based-cyber-attacks-in-2024)
- [Deepwatch Threat Intelligence Process](#deepwatch-threat-intelligence-process)
- [Appendix](#appendix)
- [TECHNIQUE STATS](#technique-stats)
- [TECHNIQUE STATS BY MONTH](#technique-stats-by-month)
- [MITRE ATT&CK Technique Stats](#mitre-attck-technique-stats)
- [DETECTION STATS](#detection-stats)
- [TOP 10 DETECTIONS](#top-10-detections)
- [DETECTIONS BY MONTH](#detections-by-month)
- [TOP 10 DETECTIONS BY MONTH](#top-10-detections-by-month)
- [Malware and Hacking Tool Stats](#malware-and-hacking-tool-stats)
- [ALL MALWARE FAMILIES OBSERVED IN 2023 THROUGH OSINT REPORTING](#all-malware-families-observed-in-2023-through-osint-reporting)
- [Top 10 Malware Families Observed In 2023 Through OSINT Reporting](#top-10-malware-families-observed-in-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN FEBRUARY 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-february-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN JANUARY 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-january-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN MARCH 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-march-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN APRIL 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-april-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN JUNE 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-june-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN MAY 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-may-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN JULY 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-july-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN AUGUST 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-august-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN OCTOBER 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-october-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN SEPTEMBER 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-september-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN NOVEMEBER 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-novemeber-2023-through-osint-reporting)
- [TOP 10 MALWARE FAMILIES OBSERVED IN DECEMBER 2023 THROUGH OSINT REPORTING](#top-10-malware-families-observed-in-december-2023-through-osint-reporting)
- [Threat Response Metrics](#threat-response-metrics)
- [TOP ENGAGEMENT TYPE](#top-engagement-type)
- [ENGAGEMENTS BY INDUSTRY](#engagements-by-industry)
- [Suspicious Activity by Industry](#suspicious-activity-by-industry)
- [ENGAGEMENTS BY MONTH](#engagements-by-month)
- [Account Compromise by Industry](#account-compromise-by-industry)
- [Ransomware Incident by Industry](#ransomware-incident-by-industry)
- [Malware Infection by Industry](#malware-infection-by-industry)
- [Vulnerability Exploitation by Industry](#vulnerability-exploitation-by-industry)
- [Deepwatch](#deepwatch)
- [Contact](#contact)

## Observations, Metrics, Trends & Forecast
For our third year, the Deepwatch Adversary Tactics and Intelligence team presents our Annual Threat Report. Here we provide Deepwatch Observations from 2023, and forecast what organizations can expect in 2024.
With in-depth analysis of our open source intelligence reporting, we share data on nearly 1.5 million security related events detected across our customers’ environments, and through response engagements.
For 2023, we cover the most predominant threats, techniques, and trends, as well as our most significant observations. Finally, our 2024 forecast calls for increased cyber resilience
This report sets itself apart with our proprietary data and insights derived from comprehensive detection coverage coupled with human-led expert investigation and confirmation of threats. The data that powers Deepwatch results from thousands of expert investigations across hundreds of thousands of protected systems.
Each of the nearly 1.5 million detected security related events that we responded to have one thing in common: They were not prevented by our customers’ expansive security controls—they are the product of our analytics that we use to detect the threats that would otherwise go undetected.
When our Security Content team and detection engineers develop detection analytics, they map them to one or more corresponding MITRE ATT&CK techniques. If the detection uncovers a potential threat, a Deepwatch expert will investigate and, if confirmed, provide detailed information about the activity observed.
Because we know which ATT&CK techniques a detection aims to detect and which detection led us to identify a threat, we can look at this data over time and determine technique prevalence, correlation, and much more.
To ensure effective detection coverage, Deepwatch takes advantage of a defense in depth strategy encompassing various stages of an attack. As a result, technique coverage is not skewed to a specific stage. This contrasts with other providers whose visibility may focus towards the beginning, middle, or later stages of an intrusion due to technology visibility limitations.
This report examines the broader landscape of threats that leverage techniques and other tradecraft. We also track specific threats associating malicious or suspicious activity with a new or existing threat activity cluster, specific malware variants, abuse of legitimate tools, and known threat actors. ATI continually tracks and analyzes threats throughout the year, publishing weekly threat intelligence reports.
In 2024 organizations can expect:
- Information Stealing Malware Will Continue to Become More Sophisticated
- Mass Vulnerability Exploitation and Supply Chain Attacks Will Continue to be a Significant Threat
- Tactics Involving External Remote Services, User Execution, and Application Layer Protocol Will Continue to be Widely Observed
- Prevalence of Ai in Malleable Tool Performance and Defense Evasion
- Abuse of Legitimate Internet Services Will Continue, Likely Escalating in 2024
- Rise of Non-Malware-Based Cyber Attacks in 2024
Welcome to the Deepwatch ATI 2024 Annual Threat Report

## Introduction
2
3
3
CONTENT
INSIDE
Introduction
2
2023 Trends
4
2024 Forecast
17 - 23
Appendix
25 - 47
Contact
48
2023 Observations
5 - 12
Method
24

## 2023 Trends
2023 Top Threats
In an ever-evolving cyber threat landscape, understanding the top threats from the previous year is crucial for organizations to bolster their cybersecurity posture. Identifying the top threats provides valuable insights into the methods and motivations of threat actors and serves as a cornerstone for developing robust defense strategies.
This knowledge enables organizations to anticipate potential attacks, prioritize security investments, and effectively tailor their incident response plans.By analyzing these critical aspects, organizations can see the shifts in the cyber threat environment, identify emerging trends, and proactively adapt to the changing tactics of adversaries.
This, in turn, enhances resilience against cyber threats, ensuring the continuity and protection of critical assets, in a landscape marked by sophistication and unpredictability.

## 2023 Observations
2023
MITRE ATT&CK Technique Metrics
Total of All Techniques Observed: 1,343,862
MITRE ATT&CK TECHNIQUE STATS
Detection Metrics
Total of All Detections: 1,351,145
DETECTION STATS
Malware and Hacking Tool Metrics
Total Malware Families Reported in OSINT: 207
MALWARE STATS
Threat Response Metrics
Total Engagements: 45 (not including benign activity and pentest activity)
INCIDENT RESPONSE ENGAGEMENT STATS
4

## 2023 Observations Quick Look
In 2023, over half of incident response engagements involved suspicious activities and account compromises, signifying a major challenge for organizations. These included unauthorized account access and malicious script executions, often evading standard security measures and leading to fraudulent activities. This underscored the need for improved email security and employee training.
Ransomware remained a significant threat, particularly targeting healthcare organizations, with sophisticated attacks using double extortion tactics. Deepwatch responded to a range of ransomware groups, including ALPHV, Monti, and Blacksuite, highlighting the evolving threat landscape.
The year also saw diverse malware and hacking tool attacks, notably impacting the manufacturing and finance sectors. Deepwatch frequently dealt with threats like Raccoon Stealer, IcedID, and Cobalt Strike, emphasizing the need for continuous vigilance and advanced security measures.
Additionally, the exploitation of critical vulnerabilities in internet-facing systems was prevalent, particularly involving known vulnerabilities. This trend called for a proactive risk management approach, evidenced by numerous system exploitation responses, including ColdFusion Exploitation.
The MITRE ATT&CK framework revealed consistent attack tactics in 2023, including Valid Accounts, User Execution, and Brute Force, indicating a focus on exploiting legitimate credentials and user interaction. The most observed tactics were Application Layer Protocol, Valid Accounts, Brute Force, Create or Modify System Process, and External Remote Services.
Finally, malware and hacking tool families like Cobalt Strike, Mimikatz, and QakBot dominated open-source reports. Known for network infiltration and credential theft, these malware families continued to challenge global cybersecurity, quickly resuming operations even after law enforcement disruptions.
2023
5

## Suspicious Activity and Account Compromise Dominated Incident Response Engagement
6
Suspicious Activity and
Account Compromise
Dominated Incident
Response Engagement
Account compromise and various forms of other suspicious activity were a top threat for organizations in 2023. The activity typically involves unauthorized access to user accounts, malicious network traffic, script execution, suspicious network traffic, and brute force activity to carry out fraudulent activities, such as stealing sensitive information or requesting wire transfers. Additionally, these attacks can be challenging to detect and prevent because cybercriminals use compromised accounts to access various data and perform actions, such as sending phishing emails and setting inbox rules. Whereas various suspicious activities may bypass security solutions. As a result, organizational leadership expects their security teams to increase their focus on email security and employee training to mitigate the risk of BEC and EAC in 2024.
> When a threat actor has the keys to the kingdom (valid admin usernames and passwords) they are afforded a level of access and freedom within a network that allows them to bypass standard security measures with ease. These credentials can be used to perform actions with the same authority as legitimate administrators, rendering traditional detection mechanisms ineffective.
> Eric Ford, Deepwatch Senior Intelligent Analyst
In Q1, over 50% of threat response engagements resulted from account compromises and suspicious activities, including social engineering attacks on IT help desks, abnormal O365 access with unauthorized inbox rule creations, RDP brute force attacks, and the execution of malicious scripts and applications.
Over 50% of all incident response engagements involved suspicious activity or account compromise, encompassing everything from unauthorized account access and various activities to access a user account to suspicious network traffic and brute force activity.
Deepwatch responded to account compromise and malicious activity for organizations across nine different industries, predominantly in the finance and insurance, manufacturing, and health care and social assistance sectors.
2023

## Ransomware Still Continues to Affect Many Industry Sectors
7
Ransomware Still
Continues to Affect
Many Industry Sectors
Ransomware continued to be a significant threat in 2023, as cybercriminals continued to use this type of malware to hold organizations’ data and systems hostage for financial gain. Despite increased awareness and efforts by businesses and governments to protect against ransomware attacks, the frequency and sophistication of these attacks continued to advance. The use of double extortion techniques, where attackers encrypt data and threaten to release stolen data publicly, added to the pressure on organizations to pay the ransom. Businesses continue to incur significant losses due to ransomware attacks, both from the ransomware payment and operational costs due to disruption of service and restoration.
2023
> The majority of ransomware events we responded to involved the use of double extortion techniques, where threat actors not only encrypt data but also, threaten to release stolen data publicly, adding to the pressure on organizations to pay the ransom.
Health Care and Social Assistance organizations were the leading targets for ransomware incidents observed and responded to by Deepwatch.
Deepwatch responded to incidents involving ALPHV, Monti, and Blacksuite Ransomware threat groups. Several incidents involved the exfiltration of data.
8

## Malware
In 2023, Deepwatch observed various malware families during incident response engagements, highlighting the evolving nature of cyber threats. Various malware families have different purposes, from dropping additional malware and data theft to establishing command and control to enrolling the infected device in a botnet. Our team detected and responded to various malware infections, such as Raccoon Stealer, IcedID, Cobalt Strike, ngrok usage, and malicious script executions in customer environments. This diverse range of threats underscores the need for continuous vigilance and advanced security measures in the ever-changing landscape of cyber threats.
Malware
2023
Almost 15% of all incident response engagements involved a malware infection, not including ransomware.
Nearly all infections impacted the manufacturing and finance and insurance sectors.
64 Cyber Intel Briefs published in the last year involved malware.
9

## Exploitation of Critical Vulnerabilities for Internet-Facing Systems
Exploitation of Critical
Vulnerabilities for
Internet-Facing Systems
In 2023, active exploitation of software vulnerabilities was a common trend observed in the threat landscape. We observed this trend across various industries and organizations, significantly impacting incident response efforts. Many organizations responded to multiple instances of active exploitation, often involving known vulnerabilities and publicly available exploit code. Despite the efforts of security teams to patch and secure systems, the speed and sophistication of attackers made it challenging to prevent or quickly remediate these types of incidents. Looking forward, organizations should take additional steps to be more vigilant and proactive in their approach to risk management to mitigate the impact posed by active exploitation.
2023
2023
50% of Deepwatch threat response engagements resulted from coldfusion exploitation.
10% of all incident response engagements involved significant system exploitation.
9 customer advisories involved vulnerabilities being actively exploited against internet-facing systems.
10

## Top ATT&CK Techniques and Detections Observed in 2023
Top ATT&CK Techniques
and Detections
Observed in 2023
In 2023, the cybersecurity landscape was dominated by a consistent pattern of attack tactics and threat detections.
They underscore a persistent focus of threat actors on exploiting system vulnerabilities and leveraging legitimate credentials for unauthorized access.
This trend suggests that threat actors are increasingly bypassing conventional security measures, emphasizing the need for robust identity and access management. Trends demand continuous monitoring of system processes and network activities.
The top detections, particularly the recurring instances of Suspicious Activity and Increasing Risk Score observed in the majority of months, highlight the critical importance of proactive threat detection and risk assessment strategies.
The frequent occurrence of Internal Network Service Discovery and Increased Activity by New Threat Object detections further indicates that adversaries constantly evolve their methods,. It demands a dynamic and adaptive security posture that can quickly respond to emerging threats and anomalies within the network infratstructure.

### Top 5 MITRE ATT&CK Tactics Observed in 2023
- T1071: Application Layer Protocol
- T1078: Valid Accounts
- T1110: Brute Force
- T1543: Create or Modify System Process
- T1133: External Remote Services
The following MITRE ATT&CK tactics placed in the Top 10 of observed tactics in every month of 2023
- T1078: Valid Accounts
- T1204: User Execution
- T1046: Network Service Scanning
- T1543: Create or Modify System Process
- T1110: Brute Force
- T1071: Application Layer Protocol i
2023
11
11
11

### Top 5 Detections Observed in 2023
External Authentication from Non-Excluded Country: The objective of this detection rule is to detect suspicious authentications to resources by monitoring the country information that the user’s are logging in from. If the user is logging in from a Country that is not expected, then it will alert.
Suspicious Activity: This detection rule’s objective is to detect when many distinct anomalies are observed for a single user or system over a 7 day time period.
Increasing Risk Score: This detection rule is intended to detect when the risk score for a single user or system rapidly increases in a 24 hour time period.
Increased Activity by New Threat Object: This detection rule is intended to detect when a new threat object (i.e., a known malicious domain, IP address, etc.) is observed across multiple risk objects or detection/anomaly searches in a 7 day time period.
Internal Network Service Discovery: This rule is designed to detect an internal host sending unsolicited packets to many destinations over a single port to map the network or discover live hosts to exploit.
2023

### Top Detections Observed in the Majority of Months in 2023
- Suspicious Activity 10 months
- Increasing Risk Score 10 months
- Internal Network Service Discovery 7 months
- Increased Activity by New Threat Object 7 months
12

## Cobalt Strike, MimiKatz, and Qakbot Among the Most Reported Malware
Cobalt Strike, MimiKatz,
and Qakbot Among the
Most Reported Malware
In 2023, open-source reporting was dominated by a triad of formidable malware families: Cobalt Strike, Mimikatz, and QakBot. These families not only persisted as significant threats ,but also topped the list of the most reported malware in hundreds of open-source reports gathered from various vendors throughout the year. Cobalt Strike, originally a legitimate penetration testing tool, was frequently exploited by attackers for its advanced network infiltration and reconnaissance capabilities.
Mimikatz, on the other hand, gained notoriety for its effectiveness in harvesting credentials from Windows systems, making it a go-to tool for threat actors seeking unauthorized access.
QakBot, a multifaceted and evolving banking trojan, continued to cause disruptions with capabilities including credential theft and network propagation.
While law enforcement action in August 2023 disrupted QakBot operations, it was not long before they resumed operations in December.
The prevalence of these three malware families in 2023 underscores their adaptability, sophistication, and the continuous challenge they pose to cybersecurity defenses worldwide.
Cobalt Strike consistently ranked as the most reported malware family in almost every month of 2023.
MimiKatz consistently ranked in the top 10 most reported malware families, making the top 10 in 9 of the 12 months of 2023.
QakBot was consistently ranked in the top 10 most reported malware families, and topped the list in two of the 12 months.
2023
13

## Recommendations

### Perimeter (Internet Edge)
Organizations should implement a perimeter discovery and attack surface monitoring solution, like Deepwatch’s Threat Signal, to identify internet-exposed systems and the threats targeting these systems. Deepwatch’s Threat Signal adopts an 'outside-in' perspective, evaluating an organization's externally accessible presence from the perspective of an attacker to pinpoint risky systems and services.
Regularly scan systems for vulnerabilities and patch systems as soon as possible. Prioritization should be placed on those systems that are internet-exposed with a focus on known exploited vulnerabilities like those featured in CISA’s Known Exploited Vulnerabilities Catalog.
Assets on the public internet expose exploitable services, such as RDP. Where these services must be exposed, appropriate compensating controls should be implemented to prevent common forms of abuse and exploitation. All unnecessary OS applications and network protocols should be disabled on internet-facing assets.
Integrating a secure email gateway as part of the organizational technology stack can significantly reduce the risk of phishing emails arriving in the end-user's inboxes.
Prevent users from launching embedded files in Microsoft OneNote files, like .hta, .bat, .com, .cmd, .exe, .js, .jse, ps1, .scr, .vbs, and .wsf, through Group Policy settings by using the “Embedded Files Blocked Extensions” template available from Microsoft here.
2023
> The KEV catalog sends a clear message to all organizations to prioritize remediation efforts on the subset of vulnerabilities that are causing immediate harm based on adversary activity. Organizations should use the KEV catalog as an input to their vulnerability management prioritization framework.
> -CISA
14

### Accounts
Integrating phishing-resistant multi-factor authentication (MFA) as part of the organizational policy can significantly reduce the risk of a cybercriminal gaining control of valid credentials for additional tactics such as initial access, lateral movement, and collecting information. Organizations can also use phishing-resistant MFA to restrict access to cloud resources and APIs.
An enforced organization-wide policy and process that requires changing default passwords for all hardware, software, and firmware before being deployed on any network. Organizations have a system-enforced policy requiring a minimum password length of 15 or more characters for all password-protected IT assets, and all OT assets are technically possible.
No user accounts have administrator or super-user privileges. Administrators maintain separate user accounts for all actions and activities not associated with the administrator role (e.g. for business email, web browsing, etc.)—Disable remote PowerShell execution for non-administrative users where possible.
2023
15

### Network & Host
Determine if certain websites or attachment types (such as Telegram, Discord, .lnk, and .iso.) are necessary for business operations and block access if security analysts cannot monitor the activity well or if it poses a significant risk.
Prevent users from opening scripts, like .hta, .jse, .js, .vbs, and .wsf, through Group Policy settings and prevent the execution of script interpreters (MSHTA.exe and WSCRIPT.exe) through Group Policy or Application Control.
A system-enforced policy that disables Microsoft Office macros, or similar embedded code, by default on all devices. If macros must be enabled in specific circumstances, there is a policy for authorized users to request that macros are enabled on specific assets.
Employ an anti-virus or EDR solution that can automatically quarantine suspicious files.
Security applications that look for behavior used during exploitation can be used to mitigate some exploitation behavior. Control flow integrity checking is another way to potentially identify and stop a software exploit from occurring.
2023
16

### Disaster Recovery
Customers are highly encouraged to establish an incident response plan and frequently test it. These plans should include the calculation for the amount of time it would take to restore from backups and the overall cost. Customers should restore data from backups when testing their plans.
Customers with encrypted off-site backups should ensure that the digital decryption key or the applications needed to restore are not stored on a local file-sharing network and access is tightly controlled.
2023
17

## 2024 Forecast

### 2024 Forecast Quick Look
Heading into 2024, the threat landscape is expected to rapidly evolve with sophisticated threats that demand proactive and dynamic responses.
Information-stealing malware will likely become more advanced, capitalizing on compromised credentials and expanding the cybercriminal toolbox beyond traditional malware.
Organizations will also witness a surge in mass vulnerability exploitation and supply chain attacks, with cybercriminals exploiting software-as-a-service vulnerabilities. They reveal the critical need for organizations tovalidate their suppliers' cybersecurity practices.
Furthermore, predictive analysis indicates a continued reliance on tactics like External Remote Services, User Execution, and Application Layer Protocol, as per the MITRE ATT&CK framework, signaling persistent and sophisticated attack vectors.
The integration of Artificial Intelligence in malware development will add a new dimension to threat capabilities, enhancing evasion techniques and adaptability.
The abuse of legitimate internet services is expected to escalate, with platforms like GitHub and Telegram being increasingly leveraged for malicious purposes.
Finally, organizations may see more malware and tool-less attacks as threat actors leverage compromised credentials to access networks and employ various techniques to avoid files. As the threat landscape evolves, these trends underscore the urgent need for robust and adaptable cybersecurity strategies in 2024.
2024
17

### Information Stealing Malware Will Continue to Become More Sophisticated
18
Information Stealing
Malware Will Continue
to Become More
Sophisticated
2024
As cybercriminals look for new ways to access sensitive information for financial gain, information-stealing malware will continue enhancing their capabilities, increasing in sophistication in 2024. As long as organizations allow users to store credentials in their browsers and policies are not established to invalidate sessions after they have ended, cybercriminals will continue to use infostealers to compromise accounts.
In addition, as more businesses and individuals work remotely and use devices to access sensitive internet-facing systems, the attack surface increases, giving cybercriminals more attack vectors. As a result, we can expect to see a continued increase in the development and use of information-stealing malware as a means for cybercriminals to steal sensitive information and sell it on cybercriminal marketplaces.
> A significant development at the end of 2023 saw various infostealers incorporate an exploit that allowed cybercriminals to restore expired Google cookies, even after users reset their passwords.
> With infostealers now able to restore expired Google cookies, we expect the continuous enhancement of infostealers to incorporate additional exploitation techniques and vulnerabilities. Many are expected to become all-purpose data stealers, targeting other data types beyond passwords stored in browsers.
> The rise in infostealing malware in 2023 will see an increase in stolen credentials being sold on cybercriminal marketplaces. This trend will likely result in gaps between initial infostealer infection and follow-on post-infection activity.

### Mass Vulnerability Exploitation and Supply Chain Attacks Will Continue to be a Significant Threat
19
2023 saw cybercriminals exploiting vulnerabilities to target hundreds of organizations. Significant events included mass exploitation of vulnerabilities in Fortra GoAnywhere, Progress MOVEit Transfer, and Citrix, as well as the supply chain attacks against 3CX, JetBrains, and Okta.
As more organizations use software-as-a-service to streamline critical processes, the attack surface for cybercriminals continues to expand. As more sensitive information is stored and processed online, the incentives for attackers to find and exploit vulnerabilities in these software systems will only continue to grow. Many organizations do not validate the cybersecurity of their suppliers, making them attractive targets for cybercriminals. This highlights the need for organizations to vet the cybersecurity practices of their suppliers, before acquiring any software solution.
2024
Mass Vulnerability
Exploitation and Supply
Chain Attacks Will Continue
to be a Significant Threat
> Over the past year, the trend of exploiting vulnerabilities in software supply chains indicates that cybercriminals will likely continue to exploit these vulnerabilities in 2024.
> Cybercriminals can effortlessly identify vulnerable systems for exploitation, allowing them to quickly develop exploit code or weaponize publicly available proof-of-concept code. Organizations are forced to rely on the security practices of their suppliers to ensure their data is safe. This is compounded by organizations' lack of knowledge of their full attack surface and the race against cybercriminals in identifying vulnerable systems and must first ensure the patches do not “break” current production systems giving the upper hand to cybercriminals.

### Techniques Involving External Remote Services, User Execution, and Application Layer Protocol Will Continue to be Widely Observed
20
Our predictive analysis, leveraging advanced modeling techniques on historical cybersecurity data, provides a forecast for the upcoming year that is crucial for shaping cybersecurity strategies. We focused on the three most observed MITRE ATT&CK techniques - 'External Remote Services,' 'User Execution,' and 'Application Layer Protocol.'
The model anticipates a fluctuating yet consistently high occurrence for External Remote Services. Adversaries initially leverage external-facing remote services to access and/or persist within a network. This suggests threat actors' sustained reliance on this tactic, necessitating continued vigilance and enhanced defensive measures in network security and access control protocols. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. Often, remote service gateways manage connections and credential authentication for these services.
User Execution is forecasted to maintain a relatively stable presence. This stability implies continued reliance on users to interact with files and highlights the importance of ongoing user education and behavioral analysis as key defense strategies. Adversaries rely on user interaction for the execution of malicious code. User interaction may include installing applications, opening email attachments, or granting higher document permissions. Adversaries may embed malicious code or visual basic code into files such as Microsoft Word and Excel documents or software installers. Execution of this code requires that the user enable scripting or write access within the document. Embedded code may not always be noticeable to the user, especially in cases of trojanized software.
The Application Layer Protocol technique is expected to increase slightly in use. This uptrend underscores a growing sophistication in attack methods targeting application layers, emphasizing the need for robust application security and real-time monitoring systems. Adversaries communicate using OSI application layer protocols to avoid detection/ network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. Adversaries may utilize many protocols, including those used for web browsing, transferring files, electronic mail, or DNS. For connections that occur internally, such as those between a proxy or pivot node and other nodes, commonly used protocols are SMB, SSH, or RDP.
These forecasts underscore the importance of adaptive and proactive cybersecurity strategies. While the consistency in some techniques reflects persistent threat vectors, the variations highlight the evolving nature of cyber threats. Organizations should prioritize resource allocation towards these identified areas, ensuring their defense mechanisms are robust and agile enough to respond to these projected trends.
2024
Techniques Involving External
Remote Services, User Execution,
and Application Layer Protocol Will
Continue to be Widely Observed

### Prevalence of AI in Malleable Tool Performance and Defense Evasion
21
The rapid advancement of AI’s technical skills along with its increased availability to the general public has provided an easy way to leverage its capabilities without a high level of technical proficiency. While very few real-world examples of AI being used by adversaries have been noted, given AI's ease of use and available nature, its usage in malicious operations is expected to increase in 2024. One example of how threat actors can use AI is to enumerate various obfuscation variances of the same command/objective. While specific prompts requesting obfuscation routes for a command may be denied for violating content policies, bypassing these restrictions is not difficult.
Taking one command a malware sample needs to run and using AI to create a list of various obfuscated versions as backup paired with logic error handling is a simple example of how malicious developers and threat actors could use AI to add redundancy and flexibility to malicious code with minimal time investment. While partially automated, this still involves manual/static inclusion of the generated variants of the original command. Beyond using AI to enumerate commands, the idea of connecting an AI tool to a Command and Control (C2) panel and programming prompts based on status updates from infected endpoints reporting to the C2 server is not far-fetched given current AI tools’ compatibility with API’s and automated input. Doing so would allow a C2 server to dynamically create alternate commands/routes that would be returned to the infected client if a specific action is detected or blocked by Endpoint Detection & Response (EDR) or Antivirus solutions.
This type of dynamic adaptation enabled by AI would not only allow individual compromised hosts to adapt to defensive measures, but it could also allow the entire fleet of compromised machines to receive AI-generated code that has adapted since the original malware deployment to evade global updates to defensive measures such as CrowdStrike and Windows Defender.
Malware polymorphism is not a new concept, and malleable profiles and modularity of components have been around for decades. Still, the presence and availability of AI presents an opportunity to integrate these features with a lower skill level and time commitment.
For defenders, malicious code with access to the command and control server may act more like a human operator with complex problem-solving skills and more persistent and diverse actions at the procedural level. This represents a significant departure from a blocked malware action as "not being a problem". Malware with AI-based augmentation is significantly less likely to try an action, be blocked, and run out of error-handling mechanisms to achieve the objective. This persistence and adaptation, typically seen more with "hands-on keyboard" activity by human operators, will become increasingly available to automated malware strains. As the chances of evading defenses increase, defenders must pay