# X-Force Threat Intelligence Index 2022

## Table of Contents
- [Executive summary](#executive-summary)
- [Report highlights](#report-highlights)
- [Key stats](#key-stats)
- [Top attack types](#top-attack-types)
- [Top infection vectors](#top-infection-vectors)
- [Threats to operational technology and Internet of Things](#threats-to-operational-technology-and-internet-of-things)
- [Top threat actors of 2021](#top-threat-actors-of-2021)
- [Trends in malware development](#trends-in-malware-development)
- [Geographic trends](#geographic-trends)
- [Industry trends](#industry-trends)
- [Risk mitigation recommendations](#risk-mitigation-recommendations)
- [About IBM Security X-Force](#about-ibm-security-x-force)
- [About IBM Security](#about-ibm-security)
- [Contributors](#contributors)

---

## Executive summary

The world continues to grapple with a lasting pandemic, shifts to work-from-home and back-to-office, and geopolitical changes spawning a constant drone of mistrust. All of this equates to chaos, and it is in chaos that cybercriminals thrive. In 2021, IBM Security® X-Force® saw how threat actors opportunistically used a shifting landscape to adopt tactics and techniques to successfully infiltrate organizations across the globe.

The IBM Security X-Force Threat Intelligence Index maps new trends and attack patterns we observed and analyzed from our data—drawing from billions of datapoints ranging from network and endpoint detection devices, incident response (IR) engagements, domain name tracking and more. This report represents the culmination of that research based on data collected from January to December 2021.

We offer these findings as a resource to IBM clients, researchers in the security industry, policy makers, the media and to the broader community of security professionals and business leaders.

Given the volatile landscape and the evolution of both threat types and threat vectors, you need threat intelligence insights to stay ahead of attackers and fortify your critical assets more than ever.

### Report highlights

*   **Top attack type**: Ransomware was again the top attack type in 2021, although the percentage of attacks X-Force remediated that were ransomware decreased nearly 9% year-over-year. REvil—a ransomware type X-Force also refers to as Sodinokibi—was the most common ransomware strain X-Force observed for a second year, making up 37% of all ransomware attacks, followed by Ryuk at 13%. Law enforcement activity has probably been the primary force driving down ransomware and IoT botnet attacks in 2021, but this does not preclude a potential resurgence in 2022.
*   **Supply chain vulnerabilities**: Supply chain security was pushed to the forefront of government and policymakers’ attention, with the Biden administration’s executive order on cybersecurity, and guidance from the U.S. Department of Homeland Security, CISA, and NIST doubling down on zero trust guidance. These guidelines put a spotlight on vulnerabilities and trusted relationships. Vulnerability exploitation was the top initial attack vector in manufacturing, an industry grappling with the effects of supply chain pressures and delays.
*   **Most phished brands**: X-Force closely tracked how cybercriminals are using phishing kits throughout 2021, and our research revealed that Microsoft, Apple and Google were the top three brands criminals attempted to mimic. These mega brands were used repeatedly in phishing kits, with attackers likely seeking to capitalize on their popularity and the trust many consumers place in them.
*   **Top threat groups**: Suspected Iranian nation-state threat actor ITG17 (MuddyWater), cybercriminal group ITG23 (Trickbot), and Hive0109 (LemonDuck) were some of the most active threat groups X-Force intelligence analysts observed in 2021. Threat groups worldwide were seeking to augment their prowess and infiltrate more organizations. Malware they used was embedded with greater defense-evasion techniques, in some cases hosted via cloud-based messaging and storage platforms to get through security controls. These platforms were abused to hide command and control communication in legitimate network traffic. Threat actors also continued to develop Linux versions of malware, to enable them to cross over to cloud environments more easily.

### Key stats

*   **21%**: Ransomware share of attacks. Ransomware was the number one attack type observed by X-Force last year, decreasing to 21% of attacks from 23% in the previous year. REvil ransomware actors (aka Sodinokibi) were responsible for 37% of all ransomware attacks.
*   **17 months**: Average time before a ransomware gang rebrands or shuts down. Ransomware gangs studied by X-Force had an average lifespan of 17 months before rebranding or disbanding. REvil, one of the most successful gangs, shut down in October 2021 after 31 months (two and a half years).
*   **41%**: Percentage of attacks exploiting phishing for initial access. Phishing operations emerged as the top pathway to compromise in 2021, with 41% of incidents X-Force remediated using this technique to gain initial access.
*   **33%**: Increase in the number of incidents caused by vulnerability exploitations from 2020 to 2021. Four out of the top five vulnerabilities exploited in 2021 were new vulnerabilities, including the Log4j vulnerability CVE-2021-44228—which was ranked number two, despite only being disclosed in December.
*   **3X**: Click effectiveness for targeted phishing campaigns that add phone calls. The click rate for the average targeted phishing campaign was 17.8%, but targeted phishing campaigns that added phone calls (vishing or voice phishing) were three times more effective, netting a click from 53.2% of victims.
*   **146%**: Increase in Linux ransomware with new code. The percentage of Linux ransomware with unique (new) code increased year-over-year by 146%, according to Intezer, indicating an increase in the level of Linux ransomware innovation.
*   **#1**: Manufacturing industry rank for attacks. Manufacturing replaced financial services as the top attacked industry in 2021, representing 23.2% of the attacks X-Force remediated last year. Ransomware was the top attack type, accounting for 23% of attacks on manufacturing companies.
*   **61%**: Manufacturing share of compromises on OT-connected organizations. Sixty-one percent of incidents at OT-connected organizations last year were in the manufacturing industry. In addition, 36% of attacks on OT-connected organizations were ransomware.
*   **2,204%**: Increase in reconnaissance against OT. Attackers increased their reconnaissance of SCADA Modbus OT devices accessible via the internet by 2,204% between January and September 2021.
*   **74%**: Share of IoT attacks originating from Mozi botnet. In 2021, attacks against IoT devices originated from the Mozi botnet 74% of the time.
*   **26%**: Share of global attacks that targeted Asia. Twenty-six percent of all attacks had targets in Asia in their crosshairs. Asia was the most attacked geography of 2021.

---

## Top attack types

For the purposes of this report, we categorize attack types by the end goal an attacker is seeking to achieve once they have gained access to a victim’s network. Attack types differ from initial infection vectors, with the latter being the initial method of entry into a network.

As examples, some attack types include ransomware, data theft, and BEC, based on the end goal of the threat actor’s operation. Examples of initial infection vectors include phishing, using stolen credentials, and vulnerability exploitation.

The following sections provide details and data on the most prolific attack types our data revealed in 2021.

### Ransomware

For more than three years, ransomware has been the top attack type observed by X-Force, and 2021 was no exception. Twenty-one percent of attacks remediated by X-Force incident response in 2021 were ransomware attacks. This is down slightly from the year prior, when 23% of attacks X-Force remediated were ransomware attacks; however, the volume of ransomware attacks has remained steady year-over-year.

![Figure 1: Breakdown of top attack types, 2020-2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-1-top-attack-types-2021-vs-2020.png)
*Figure 1: Top attack types, 2021 vs. 2020*

The frequency of ransomware attacks X-Force observes tends to shift throughout the year, with May and June tending to see higher frequencies of attacks, while January tends to see lower. In addition, ransomware attacks appear to decrease in late summer or early fall. In 2021, that drop largely came in August and again in November, likely spurred by the permanent or temporary shutdown of several groups in the months prior: DarkSide and Babuk in May, Avaddon in June, and REvil in October.

![Figure 2: Percentage of X-Force Incident Response engagements that were ransomware, 2020-2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-2-percentage-of-ir-incidents-that-were-ransomware-by-month.png)
*Figure 2: Percentage of IR incidents that were ransomware, by month, 2020 vs. 2021*

> Many ransomware actors have continued operations under new names

According to X-Force research, 17 months is the average time before a ransomware group either rebrands or shuts down, with a median of 18 months. Ransomware groups often spring up and rebrand once there is a threat of arrest or action by law enforcement. In some cases, law enforcement action forces ransomware groups to shut down entirely. Despite this dynamic environment—or perhaps because of it—many ransomware actors remain at large, and X-Force assesses that criminal ransomware activity will continue into the foreseeable future, based on the high profits generated by this activity and current limitations on law enforcement for widely shutting down ransomware activity. X-Force is aware of many ransomware actors that have rebranded and continued operations under new names, with GandCrab to REvil, Maze to Egregor, and DoppelPaymer to Grief as examples.

Law enforcement activity is probably the primary factor driving down the percentage of ransomware attacks X-Force observed in 2021, but it is very likely that the groups we have seen disappear will rebrand and re-emerge in 2022 under new names and that ransomware activity will continue.

![Figure 3: Sample of ransomware groups that have shut down, 2017-2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-3-ransomware-groups-that-have-shut-down.png)
*Figure 3: Ransomware groups that have shut down*

Of the ransomware strains observed by X-Force in 2021, REvil made up 37%—over one-third—of all ransomware incidents our team remediated. A strong second was Ryuk, making up 13% of attacks observed last year. REvil actors as of mid-October 2021 appear to have permanently shut down operations, probably due to law enforcement activity. Both Ryuk and REvil constitute some of the longest-running ransomware operations, having emerged in April 2019 and August 2018, respectively.

![Figure 4: Ransomware types observed by X-Force Incident Response in 2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-4-types-of-ransomware-observed-in-2021.png)
*Figure 4: Types of ransomware observed in 2021*

### How ransomware attacks happen

Given the deep experience X-Force Incident Response (X-Force IR) has in remediating ransomware attacks, our team has observed a recent pattern emerge across the vast majority of ransomware attacks. In particular, we have been able to develop a five-stage model that defines the common pattern observed in most ransomware incidents.

![Figure 5: Standard attack flow for ransomware attacks, as observed by X-Force Incident Response](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-5-stages-of-a-ransomware-attack.png)
*Figure 5: Stages of a ransomware attack*

*   **Stage 1: Initial access**: The most common access vectors for ransomware attacks continue to be phishing, vulnerability exploitation, and remote services such as remote desktop protocol.
*   **Stage 2: Post exploitation**: Depending on the initial access vector, the second stage may involve an intermediary remote access tool (RAT) or malware prior to establishing interactive access with an offensive security tool such as Cobalt Strike or Metasploit.
*   **Stage 3: Understand and expand**: During the third stage of the attack, attackers have consistently focused on understanding the local system and domain that they currently have access to and acquiring additional credentials to enable lateral movement.
*   **Stage 4: Data collection and exfiltration**: Almost every ransomware incident X-Force IR has responded to since 2019 has involved the “double extortion” tactic of data theft and ransomware. During stage 4 of the attack, the focus of the ransomware operators switched primarily to identifying valuable data and exfiltrating it.
*   **Stage 5: Ransomware deployment**: In almost every single ransomware incident X-Force IR has responded to, the ransomware operators targeted a domain controller as the distribution point for the ransomware payload.

A concerning new trend in ransomware has been the expansion of “triple extortion” tactics. In this type of attack, threat actors encrypt and steal data and also threaten to engage in a distributed denial of service (DDoS) attack against the affected organization. This kind of attack is particularly problematic for organizations because victims have their networks held hostage with two kinds of malicious attacks—often simultaneously—and are then further victimized by the theft (and often leak) of data.

Ransomware gangs are beginning to look to their primary victim’s extended business partners to pressure them into paying a ransom to prevent their own data leakages or business disruptions caused by the ransomware attack.

### Server access

*   **11%** of attacks were server access.
Server access attacks—where the attacker gained unauthorized access to a server, but the final end goal is unknown—was the second-most common attack type, making up 11% of all incidents X-Force IR team remediated in 2021.

The majority of these attacks occurred in Asia, and in many cases the threat actors were successful in deploying malware or employing penetration testing tools on a server, including China Chopper Webshells, Black Orifice malware, Printspoofer, and Mimikatz.

In some instances, the threat actors exploited a known vulnerability, such as CVE-2020-7961, which would allow for remote code execution on a server.

In multiple cases threat actors exploited vulnerabilities in Microsoft Exchange servers to gain unauthorized access to networks of interest. These vulnerabilities are included in the top 10 vulnerabilities of 2021 listed below.

Some of the server access attacks observed by X-Force’s IR team may have been failed attempts to steal data or deploy ransomware. Thus, while companies aim to prevent attackers from gaining any level of unauthorized access to their networks, it’s likely that a high number of server access attacks indicates that organizations are identifying and eradicating attacks before they progress into more damaging operations.

### Business email compromise

After a downturn in business email compromise (BEC) attacks in 2020, X-Force observed a decrease in this attack type again in 2021. BEC was the third-most common attack type remediated by our X-Force IR team. Last year, we theorized that widespread implementation of multifactor authentication (MFA) was decreasing the number of successful attacks BEC threat actors were able to execute. That theory held in 2021, since BEC attackers may have realized greater success by shifting focus to geographies where MFA is not as widely implemented.

For example, Latin American organizations appeared to be bearing the brunt of BEC attacks the X-Force IR team is remediating. North American organizations were still strongly in the crosshairs of BEC operations, but the surge we noticed against Latin American organizations suggests that BEC attackers shifted the geographic focus of their operations: zero percent of attacks against Latin American organizations were BEC in 2019, but 20% of attacks were BEC in 2020 and 20% of attacks in 2021 were BEC.

![Figure 6: Percentage of incidents that were BEC in each region, 2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-6-percentage-of-incidents-that-were-bec-in-each-region.png)
*Figure 6: Percentage of incidents that were BEC, 2021*

---

## Top infection vectors

In addition to examining the end goal of threat actors X-Force observes, our team also tracks how threat actors gain initial access to victims’ networks. Phishing and vulnerability exploitation tend to be the most common methods we observe, followed by use of stolen credentials, brute force, remote desktop protocol (RDP), removable media and password spraying making up a small percentage of intrusions.

![Figure 7: Breakdown of infection vectors observed by X-Force Incident Response, 2020-2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-7-top-infection-vectors-2021-vs-2020.png)
*Figure 7: Top infection vectors, 2021 vs. 2020*

### Phishing

Phishing emerged as the top infection vector in 2021, surpassing vulnerability exploitation, which took the lead in 2020. Phishing was observed in 41% of the incidents X-Force remediated. While vulnerability exploitation dominated in Q3 of 2021, the significant number of phishing-related incidents X-Force observed in Q1 and Q4 pushed this infection vector into the lead for the year.

![Figure 8: Percentage of attacks linked with various infection vectors, by quarter, in 2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-8-percentage-of-attacks-tied-to-phishing-vulnerability-exploitation-and-stolen-credentials-by-quarter.png)
*Figure 8: Percentage of attacks tied to phishing, vulnerability exploitation, and stolen credentials, by quarter, 2021*

Part of X-Force Red’s focus areas include conducting social engineering penetration testing attacks through phishing emails. For targeted phishing campaigns in 2020 and 2021, the average click rate for an X-Force Red simulated campaign was 17.8%. When vishing (voice phishing) phone calls were added to the campaign, the click rate rose to 53.2%, three times as effective.

BEC attackers have leveraged phishing campaigns and social engineering with great success. And particularly in 2021, X-Force observed ransomware actors rely even more heavily on phishing campaigns to gain initial access to victim networks for ransomware attacks.

For example, multiple REvil ransomware incidents observed in 2021 began with a QakBot phishing email. These emails usually have very short messages, often refer to unpaid invoices, and occasionally will even hijack ongoing email conversations and reply all with only a malicious attachment.

When opened, the document will instruct the recipient to enable macros which will drop the QakBot banking trojan, gaining an initial foothold on a system. The operation is then transferred to REvil ransomware actors who conduct reconnaissance and proceed with the operation from there.

A sample QakBot phishing email is included in figure 9.

![Figure 9: Example of QakBot phishing email with malicious attachment](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-9-sample-qakbot-phishing-email.png)
*Figure 9: Sample QakBot phishing email*

When the recipient attempts to open the attachment, they are prompted by a popup (see figure 10) to enable macros by choosing “Enable editing” and “Enable content.” This allows the threat actor to deploy malware on the victim’s machine with the assistance of malicious macros.

![Figure 10: Message in malicious attachment prompting the recipient to enable macros](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-10-sample-popup-message-from-qakbot-phishing-attachment.png)
*Figure 10: Sample popup message from QakBot phishing attachment*

#### Phishing kit deployments short-lived, abuse technology and bank brands

IBM analyzed thousands of phishing kits from around the world to determine the frequency and effectiveness of this particular attack vector. Our investigation suggests that malicious actors who use phishing kits probably put in tedious hours with limited gains. In particular, our investigation showed that:

*   Phishing kit deployments generally had a short lifespan, with almost one-third of deployed kits being used for no longer than a day. In some cases, an individual deployment of a phishing kit lasted only seven-to-eight hours before most hosting providers identified the site as malicious and blocked it.
*   Each deployment on average had no greater than 75 potential victims who visited the site.
*   Phishing kits asked for user credentials (email/ID/password combinations) in nearly every kit observed (close to 100%), followed in popularity by credit card data (61% of requests), mailing address (40%), phone number (22%), date of birth (17%), identity card number (15%), security questions (14%), and ATM PINs (3%).

In addition, X-Force looked at which brands were most frequently spoofed in phishing kits. The top brands included large technology companies and large financial institutions. The top 11 brands are listed below.

*   Microsoft
*   Apple
*   Google
*   BMO Harris Bank (BMO)
*   Chase
*   Amazon
*   Dropbox
*   DHL
*   CNN
*   Hotmail
*   Facebook

The Anti Phishing Work Group (APWG) noted that June 2021 set an all-time record high with 222,127 phishing attacks that month alone. X-Force assesses with high confidence that phishing kits will continue to be used by threat actors due to their easy-to-use nature and low resource requirement. Monitoring for suspicious connections to likely spoofed brands can help organizations minimize the probability of impact from this attack vector.

Using a DNS service that’s dedicated to data privacy, like Quad9², can also help mitigate the risk of phishing attacks.

² IBM Security X-Force is a Quad9 partner.

### Vulnerability exploitation

Despite dropping to the second-most common in 2021, the number of incidents that were caused by vulnerability exploitation this past year rose 33% from 2020, indicating this attack vector’s strong hold in threat actors’ arsenals. This vector allows threat actors to gain access to victim networks for further operations—in many cases with elevated privileges.

X-Force observed actors leveraging multiple known vulnerabilities, such as CVE-2021-35464 (a Java deserialization vulnerability) and CVE-2019-19781 (a Citrix path traversal flaw), to gain initial access to networks of interest. In addition, we observed threat actors leverage zero-day vulnerabilities in major attacks like the Kaseya ransomware attack and Microsoft Exchange Server incidents to access victim networks and devices.

Near the end of 2021, widespread exploitation of the Log4j vulnerability CVE-2021-44228 also launched this vulnerability into second place in X-Force’s top 10 list for 2021. Several mitigation measures can assist your organization in avoiding becoming a victim of this vulnerability.

#### Number of vulnerabilities hit another record high

Over the past five years, the number of vulnerabilities discovered per year has risen steadily. Even more concerning is that the number of exploits—tools threat actors can use to exploit a vulnerability—are also rising steadily, creating an ever-expanding array of options for threat actors seeking to exploit vulnerabilities.

Vulnerabilities related to Internet of Things (IoT) and industrial control systems (ICS) increased at an even faster rate than overall vulnerabilities, with these two categories experiencing a 16% and 50% year-over-year increase respectively, compared to a 0.4% growth rate in the number of vulnerabilities overall.

![Figure 11: New vulnerabilities identified each year, 2011-2021, and cumulative number of vulnerabilities](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-11-vulnerabilities-discovered-by-year.png)
*Figure 11: Vulnerabilities discovered by year, 2011-2021*

#### Top 10 vulnerabilities of 2021

While any vulnerability carries risk and should be assessed, the following list includes the top vulnerabilities that X-Force IR observed threat actors exploit or attempt to exploit during the course of operations in 2021. X-Force recommends prioritizing patching of these vulnerabilities if your organization has not done so already.

1.  CVE-2021-34523 – Microsoft Exchange server flaw enabling malicious actors to bypass authentication and impersonate an administrator. Known generically as ProxyLogon.
2.  CVE-2021-44228 – Vulnerability in Apache Log4j Library
3.  CVE-2021-26857 – Microsoft Exchange Server remote code execution vulnerability
4.  CVE-2020-1472 – Netlogon elevation of privilege vulnerability
5.  CVE-2021-27101 – Accellion FTA vulnerability susceptible to SQL injection
6.  CVE-2020-7961 – Liferay Portal deserialization of untrusted data allows for remote code execution via JSON web services
7.  CVE-2020-15505 – MobileIron vulnerability allowing for remote code execution
8.  CVE-2018-20062 – NoneCMS ThinkPHP remote code execution vulnerability
9.  CVE-2021-35464 – ForgeRock AM server Java deserialization vulnerability allows for remote code execution
10. CVE-2019-19781 – Citrix Server path traversal flaw

---

## Threats to operational technology and Internet of Things

Known vulnerabilities related to industrial control systems (ICS)—and, by extension, operational technology (OT)—as well as Internet of Things (IoT) vulnerabilities are increasing each year, with an appreciable increase in identified vulnerabilities from 2020 to 2021.

As more “things” come alive with the power of digitization and internet protocols, so do new vulnerabilities and risks. While many of these issues affect only industrial organizations, any organization that uses IoT in its infrastructure is also increasingly exposed to risk.

In addition to this increased digitization, the dynamics of supply chains are affecting the attack surface for many OT-connected organizations. Threat actors understand the critical role manufacturing and energy play in global supply chains and are seeking to disrupt these organizations because of the ripple effect it can have across multiple industries and the pressure these multiplying effects create for victims to pay a ransom.

![Figure 12: Month-by-month breakdown of SCADA Modbus reconnaissance activity, 2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-12-scada-modbus-reconnaissance-volume-breakdown-by-month.png)
*Figure 12: SCADA Modbus reconnaissance volume, breakdown by month, 2021*

### Threat actors accelerate reconnaissance against OT devices

Analyzing data from 2021, X-Force observed attackers conducting massive reconnaissance campaigns searching for exploitable communications in industrial networks. Specifically, 2021 saw a considerable increase in reconnaissance activity targeting TCP port 502. This port uses Modbus, an application layer messaging protocol used to provide client-to-server communication between connected buses, networks, and programmable logic controller (PLC) devices in industrial networks. Port 502 is commonly used by supervisory control and data acquisition (SCADA). Access to Modbus could allow threat actors to control physical devices connected to the internet.

Between January and September of 2021, X-Force observed a 2204% increase in adversarial reconnaissance activity targeting port 502.

Threat actors may have heightened Modbus reconnaissance to begin finding targets to ransom or seize control and cause harm. Given Modbus’s lack of security features, once an attacker has found an accessible Modbus device, they could then issue harmful commands to the device and impact connected ICS or IoT systems.

Although SCADA Modbus resides in Level 2 of the Purdue Model within ICS environments—which ideally should be segmented from the enterprise network and placed behind a demilitarized zone—in some cases the SCADA Modbus port 502 can be accessed directly over the open internet. Lack of authentication and transmission of messages in plain text are some additional aspects of Modbus that make it less secure when compared to other, more modern technologies.

### Manufacturing most targeted of OT industries, ransomware leads

In terms of industries with OT networks, X-Force observed manufacturing was the most attacked in 2021 by a significant margin, victimized in 61% of incidents X-Force assisted in remediating. Ransomware actors in particular find manufacturing to be an attractive target, likely due to these organizations’ low tolerance for down time.

![Figure 13: Breakdown of attacks against six operational technology industries targeted, as observed by X-Force IR, 2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-13-ot-industries-targeted-2021.png)
*Figure 13: OT industries targeted, 2021*

For all industries with OT networks where X-Force observed attacks in 2021—engineering, mining, utilities, oil and gas, transportation and manufacturing—ransomware again led the charge for attack types, accounting for 36% of all attacks and echoing the overall attack trend across all industries. While the IT networks were compromised in the vast majority of these attacks, the impact carried over to victims’ operational technology in many of these instances.

Other top attack types included server access, DDoS, RATs, insiders, and credential harvesting operations.

![Figure 14: Breakdown of attack types on operational technology, 2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-14-attack-types-on-ot-2021.png)
*Figure 14: Attack types on OT, 2021*

### Mozi botnet continues to threaten IoT and OT assets

Since 2019, X-Force has identified a high volume of IoT malware activity—including a nearly 3000% surge between Q3 2019 and Q4 2020. The Mozi botnet continued to make up the most significant volume of IoT malware compared to all other IoT malware types, at 74% of the total volume of IoT malware X-Force observed in 2021.

![Figure 15: IoT malware activity, broken down by quarter, 2018-2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-15-iot-attack-volume-breakdown-by-quarter.png)
*Figure 15: IoT attack volume breakdown by quarter, 2018-2021*

Mozi abuses weak Telnet passwords and exploits vulnerabilities to target networking devices, IoT, and video recorders, among other internet-connected products. Post-infection, it is capable of maintaining persistence on network gateways, which can be particularly effective initial access points for lateral movement to high-value networks, including OT and ICS networks. In addition, by infecting routers, threat actors behind Mozi can position themselves to conduct man-in-the-middle attacks that lead to ransomware deployment, including attacks on OT networks.

In addition to Mozi’s access and lateral movement capabilities, a large Mozi botnet that infects a large number of security cameras or similar IoT devices at an organization can diminish an organization’s ability to effectively conduct physical security operations.

Chinese law enforcement reportedly arrested the authors of the Mozi botnet in June and August 2021, and the decrease in IoT attack volume in Q4 2021 is probably a side-effect of these arrests.

---

## Top threat actors of 2021

Our 2021 IR data show that where a threat actor could be identified, cybercriminals were the leading source of attacks.

Nation-state actors made up only 2% of the engagements X-Force remediated in 2021, underscoring the high volume of activity generated by cybercriminal activity. The nation-state actors we observed were largely seeking to conduct espionage and surveillance, and in some cases, may have been laying the groundwork for future sabotage. Only 1% of the activity we observed was from hacktivist groups.

The following sections provide additional detail on some of the more interesting and active threat groups X-Force observed in 2021.

![Figure 16: Threat actor groups observed by X-Force IR, broken down by type, 2021](https://www.ibm.com/content/dam/connect/global/en/content/images/reports/threat-intelligence/2022/figure-16-threat-actors-observed-by-x-force-incident-response-2021.png)
*Figure 16: Threat actors observed by X-Force Incident Response, 2021*

### Suspected Iran-based ITG17 uses Aclip backdoor

In 2021, IBM Security X-Force observed a threat actor using a new backdoor that X-Force named “Aclip.” In addition, the adversary leveraged a legitimate messaging and collaboration application tool likely to obfuscate operational communications, allowing malicious traffic, or traffic with underlying malicious intent, to go unnoticed. Based on the tools, tactics, and infrastructure observed, we assess with moderate confidence that the threat actor we track as ITG17³ (aka MuddyWater), a suspected Iranian nation-state group, was behind this activity for the possible purpose of surveillance.

### ITG23—Trickbot Gang—enables Conti ransomware operations

X-Force analysts have been closely tracking the cybercriminal group behind the Trickbot banking trojan—a group we identify as ITG23, also known as Wizard Spider or Trickbot Gang. Phishing emails with the Trickbot trojan are often used as an entry point for Conti ransomware, and X-Force has observed that an uptick in ITG23 Trickbot activity coincided with an uptick in Conti ransomware attacks.

The group has relied on email campaigns delivering malicious Excel documents, as well as the notable BazarCall campaign, in which subscription themed emails encourage recipients to contact a fraudulent call center where the telephone operator then guides the user to download the BazarLoader malware, under the guise of unsubscribing from a service. Additionally, the group has more recently been hijacking email threads and will then “reply all” with malicious attachments.

### Hive0109 active in 2021

X-Force observed multiple Hive0109—also known as LemonDuck—compromises in 2021, and the group has proven itself adept at leveraging the ProxyLogon vulnerabilities to compromise unpatched Microsoft Exchange servers. LemonDuck targets both Linux and Windows systems and is known to capitalize on news-worthy events for phishing lures in its campaigns.

LemonDuck is persistent malware that was primarily used to mine cryptocurrency. It has likely been active at least since 2018 and has since evolved into a large botnet. LemonDuck propagates quickly and acts as a