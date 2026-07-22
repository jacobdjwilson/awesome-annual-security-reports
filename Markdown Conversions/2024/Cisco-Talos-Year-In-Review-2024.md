# Cisco Talos Year in Review 2024 Report

## Table of Contents
- [Introduction](#introduction)
- [Top-targeted vulnerabilities](#top-targeted-vulnerabilities)
- [Email threats](#email-threats)
- [Most used tools](#most-used-tools)
- [Ransomware](#ransomware)
- [Identity-based threats](#identity-based-threats)
- [Attacks against MFA](#attacks-against-mfa)
- [AI threats](#ai-threats)

---

## Introduction

In 2024, threat actors prioritized stealth, simplicity, and efficiency, largely abandoning the use of custom malware and zero-day vulnerabilities in favor of simpler yet highly effective techniques. This environment underscores that it is more critical than ever for organizations to prioritize security fundamentals.

Identity was an enduring theme in 2024, as threat actors looked for ways to compromise users’ unique digital footprint and coopt it for their own malicious purposes. This includes identifiers like login credentials, session IDs, API keys, digital certificates, and more. Identity-based attacks were dominant, accounting for 60% of all Cisco Talos Incident Response (Talos IR) cases, and actors relied on these techniques for major phases of their operations — initial compromise, lateral movement, privilege escalation, and more. Difficult to prevent and even harder to detect, identity-based attacks proved to be highly effective in 2024, allowing adversaries to go unnoticed for longer periods of time by using compromised valid accounts, foregoing the use of detectable malware, and sometimes leading to unfettered access to entire networks.

“Easy access” was another dominant theme, with decades-old CVEs topping our list of most-targeted vulnerabilities and security issues like misconfigured systems, MFA weaknesses, and unpatched systems appearing in more than half of Talos IR cases. Ransomware actors in particular honed in on this and attempted to disable poorly configured security solutions in most of the IR incidents we responded to, succeeding nearly 50% of the time. Unsurprisingly, education and healthcare were the top-targeted industry verticals, as actors continue to compromise organizations that tend to have lower cyber budgets and deal with more administrative bureaucracy that makes it difficult for them to maintain quick, agile footing in defense of these threats.

As we look ahead, threats to the very systems that underpin our networks remain persistent, and organizations will need to continue prioritizing security and addressing aging infrastructure that poses significant risks. Sophisticated adversaries are capitalizing on vulnerable network hardware, public-facing applications, and cloud applications — all ingress points to network environments that should not be overlooked from a security perspective. Furthermore, as attacks in this space are increasingly relying on identity-based techniques, it’s more important than ever that organizations adhere to security fundamentals, as so many of these attacks can be prevented by properly deploying and configuring multi-factor authentication, spotting socially engineered phishing lures, and identifying unusual activity emanating from legitimate accounts on the network.

In the artificial intelligence (AI) space, threat actor use of AI and machine learning (ML) largely fell short of industry projections in 2024, with actors relying on these technologies to enhance their techniques rather than aid in the creation of new ones. Adversaries used generative AI tools, such as large language models (LLMs), to create convincing social engineering campaigns and automate malicious activities. In 2025, we expect to see their use expand, possibly with actors leveraging the technologies to create capabilities that can compromise AI models, systems, and infrastructure.

![Cisco’s global visibility map showing location of devices](![Figure 1: Cisco’s global visibility map showing located devices globally across 193 countries and regions])

Cisco’s global reach and dominant role in the network infrastructure space gives us incredible insight into many of today’s enduring and emerging threats. The findings in this report are pulled from the collective research of hundreds of threat hunters, malware experts, detection specialists, data modeling professionals, and IR personnel. We receive and process telemetry from over 46 million devices globally across 193 countries and regions, amounting to more than 886 billion security events per day. Talos’ Year in Review, which covers January 1, 2024 to December 31, 2024, leverages all of this data and expertise to deliver the analysis herein.

---

## Top-targeted vulnerabilities

Actors key in on historic, widely used CVEs in 2024. The top-targeted vulnerabilities in 2024 were mostly older CVEs that have been public for several years. Notably, four of the top twelve CVEs that made our list were published a decade ago, and the notorious Log4j vulnerabilities — which were disclosed in early 2021 — are also featured. This is a stark reminder that threat actors frequently target unpatched systems, and failure to apply security updates leaves organizations vulnerable to many attacks that could otherwise be prevented.

Exploitation attempts against the Apache Log4j logging library remain high nearly four years after the vulnerabilities were discovered. Log4J is one of the most widely used open-source programs in the world. While the vulnerabilities, collectively known as “Log4Shell,” were patched shortly after discovery, they will likely pose a long-term risk for organizations because Log4j is so deeply embedded in the software supply chain. The U.S. Department of Homeland Security estimates it will take at least a decade to find and fix every vulnerable instance.

Relatedly, all of the vulnerabilities on our list impact widely used software and hardware, creating an incredibly broad attack surface that threat actors can exploit to infiltrate a broad range of sectors and geographies. For example, CVE-2017-9841 and CVE-2024-4577 affect PHP, a common programming language. Estimates show that between 75 and 80 percent of the world’s two billion websites rely on PHP, including popular sites like Facebook and Wikipedia and e-commerce platforms like Etsy and Shopify. Vulnerabilities in the underlying code of these websites can allow attackers to gain unauthorized access and even lead to major data breaches. In January 2024, CISA and the FBI published an advisory warning of actors exploiting CVE-2017-9841 to deploy Androxgh0st, a malware known for its ability to establish a botnet that can further identify and compromise vulnerable networks.

As mentioned previously, all of the top-targeted vulnerabilities affect software and hardware that are ubiquitous in systems globally, creating a broad attack surface. The types of threat actors that have been observed exploiting these CVEs increases the concern around risks to vulnerable organizations. For example, a variety of advanced threat actors have reportedly leveraged CVE-2023-42793 (impacting JetBrains’ TeamCity servers) in their operations, including the Russian state-sponsored threat group APT29 (aka CozyBear), multiple North Korean state-sponsored groups, and the BianLian ransomware gang.

### Shellshock’s lasting impact

The Shellshock vulnerability, which affects the Bash scripting language in widely used operating systems like Linux and macOS, remains a problem more than a decade after its discovery in 2014. Bash is integrated deeply into applications and system processes globally. Additionally, many web servers, routers and internet-of-things (IoT) devices rely on Bash to execute commands, meaning that vulnerable devices connected to the internet are potential targets. These hardware components are often less frequently updated or harder to patch, especially in industrial or critical infrastructure settings.

Shellshock’s direct consequences may not have been as catastrophic as other high-profile breaches and cyber attacks, but it is a persistent problem. For example, in 2019, Talos discovered a global state-sponsored espionage campaign called “Sea Turtle” that manipulated DNS records to gain access to sensitive systems. The adversary relied on several vulnerabilities, including Shellshock, to gain initial access.

While other confirmed public examples of state-sponsored cyber actors targeting Shellshock are limited, it’s very likely that other advanced actors have attempted to exploit Shellshock. Many well-known adversaries like the Russian state-sponsored group APT28 and North Korean state-sponsored Lazarus Group exploit critical vulnerabilities in widely used software, making Shellshock a likely tool in their broader espionage and attack campaigns.

![Chart showing top-targeted vulnerabilities in 2024 including Log4j, JetBrains TeamCity Server, PHP, and GNU Bash / Shellshock](![Figure 2: Top-targeted vulnerabilities in 2024])

### Top-targeted network device CVEs

We also looked specifically at the top-targeted network device vulnerabilities to see what types of devices attackers are prioritizing in their operations. This list only includes network device vulnerabilities that were added to CISA’s Known Exploited Vulnerabilities (KEV) catalog in 2023 or 2024. Of those, three (CVE-2024-24919, a Check Point VPN zero-day; and CVE-2024-3273 and CVE-2024-3272, affecting older D-Link hardware), accounted for more than 50% of network device targeting in that data set (see figure 3).

Many of these vulnerabilities have largely been exploited by known botnets like Mirai, Gafgyt, and others, which can establish control over compromised devices and command them to carry out distributed denial-of-service (DDoS) attacks and other malicious activity. Because of the access that routers, firewalls, and other network devices afford, their compromise can allow an attacker to easily move laterally, carry out other phases of their attacks, and potentially take over entire networks. At least one of the vulnerabilities (CVE-2023-38035) has been exploited by ransomware operators.

Notably, some of these top-targeted vulnerabilities affect end-of-life (EOL) devices and therefore have no available patches, despite still being actively targeted by threat actors. Examples include CVE-2024-3273 and CVE-2024-3272 (D-Link NAS devices), which were the second and third most targeted network device vulnerabilities on our list, respectively. This underscores the importance of decommissioning and replacing EOL components of an organization’s network as soon as possible.

![Chart showing top-targeted network device CVEs including Check Point and D-Link](![Figure 3: Top-targeted network device CVEs])

#### Top 10 most targeted network device vulnerabilities

| CVE | Manufacturer | Product | Device type | Vulnerability description |
| --- | ------------ | ------- | ----------- | ------------------------- |
| CVE-2024-24919 | Check Point | Quantum Security Gateways | Firewall/VPN | Attacker can read sensitive data like password hashes. |
| CVE-2024-3273 | D-Link | Multiple NAS Devices | Network attached storage (NAS) | Allows attacker to execute arbitrary base 64-encoded commands on the devices. |
| CVE-2024-3272 | D-Link | Multiple NAS Devices | Network attached storage (NAS) | Allows attacker to execute arbitrary base 64-encoded commands on the devices. |
| CVE-2023-1389 | TP-Link | Archer AX21 | Router | Attacker can inject commands, which would be run as root, with a simple POST request. |
| CVE-2024-3400 | Palo Alto Networks | PAN-OS | Firewall | Gives attacker ability to execute commands with root privileges on the firewall. |
| CVE-2023-36845 | Juniper | Junos OS | Network device software | Attacker can inject and execute malicious code. |
| CVE-2021-44529 | Ivanti | Endpoint Manager Cloud Service Appliance | Endpoint device manager | Allows attacker to execute malicious code with limited permissions. |
| CVE-2023-38035 | Ivanti | Ivanti Sentry | Security gateway | Allows attacker to access sensitive API data and configurations, run system commands, or write files onto the system. |
| CVE-2024-36401 | OSGeo | GeoServer | Server | Attacker can conduct remote code execution via specially crafted input. |
| CVE-2024-0012 | Palo Alto Networks | PAN-OS Firewall | Firewall | Allows attacker to gain administrator privileges. |

![Chart showing top security weaknesses in Talos IR cases](![Figure 5: Top security weaknesses in Talos IR cases including MFA weakness, vulnerable systems, lack of logging retention, poor password policies, EDR configuration issues, and poor security awareness training])

### Talos’ top 10 tips for securing network devices:

1. **Update devices as aggressively as possible.** This includes patching current hardware and software against known vulnerabilities and replacing EOL hardware and software.
2. **Implement robust authentication methods.** Use multifactor authentication, select complex passwords and community strings, and avoid default credentials.
3. **Adhere to security best practices**, including conducting regular updates, managing access controls, implementing user education, and enforcing network segmentation.
4. **Encrypt all monitoring and configuration traffic**, including SNMPv3, HTTPS, SSH, NETCONF, and RESTCONF.
5. **Stay informed and up-to-date** on security advisories from the U.S. government and industry. Consider suggested configuration changes to mitigate issues captured by these reports.
6. **Lock down and actively monitor credential systems**, such as TACACS+ and any jump hosts.
7. **Store configurations centrally and push to devices.** Do not allow devices to be the trusted source for their configurations.
8. **Use authentication, authorization, and accounting (AAA)** to deny configuration changes for key device protections, such as local accounts, TACACS+, and RADIUS.
9. **Monitor your environment for unusual changes in behavior or configuration.** Be on the lookout for exposure of administrative or unusual interfaces (such as SNMP, SSH, and HTTP(S)), and monitor syslog and AAA for unusual activities.
10. **Profile your devices’ baseline** to identify any changes. Fingerprint network devices via NetFlow and port scanning for a shift in surface view, including new ports opening/closing and traffic to/from. When possible, develop NetFlow visibility to identify unusual volumetric changes.

---

## Email threats

### Attackers spoof well-known brands in phishing lures

Phishing continues to be a main method of compromise, as threat actors can easily and anonymously send out high volumes of emails to reach their victims. We saw adversaries gain initial access via phishing in nearly a quarter of Talos IR incidents. In those cases, embedded malicious links appear to be more successful than other modes of phishing, like email attachments or voice phishing (vishing). Social engineering is a hallmark in this space, and artificial intelligence (AI) tools have made it even easier for actors to create believable lures crafted specifically for their targets.

We analyzed our email telemetry to identify prevailing social engineering preferences or trends. Figure 7 shows the most common brands appearing in sender display names from emails that were blocked. The findings give us a sense of the types of companies that threat actors might be trying to spoof to trick victims into engaging with their malicious phishing lures.

Microsoft Outlook was the most commonly spoofed brand, appearing as the sender name in 25% of blocked emails. Tech behemoths Amazon and Apple also had high prevalence. Other names that top the list include popular online payment services, international retail companies, and common enterprise collaborative applications. It’s no surprise that these companies are among threat actors’ favorites to imitate given their global ubiquity: High brand recognition likely coincides with increased trust and higher click rates.

![Chart showing types of phishing in Talos IR cases: Malicious link (58%), Malicious attachment (25%), Vishing (17%)](![Figure 6: Types of phishing in Talos IR cases])

![Chart showing top spoofed brands in sender names including Linkedin, Microsoft Outlook, Amazon, American Express, Apple, Sharepoint Online, Shein, Confluence, Netflix HR, Wordpress Support Department, DHL Express, Temu, Microsoft Docusign, PayPal, Spotify via Docusign, Sam's Club, Capital One, Accounts Payable, Admin](![Figure 7: Top spoofed brands in sender names])

### Actors use simple subject lines in phishing lures but still leverage major events

In addition to making emails appear like they’re coming from a legitimate, trusted sender, threat actors also rely on the email’s subject line to creatively and convincingly trick victims into opening the email. Figure 8 shows the most common terms appearing in subjects of blocked emails. These terms were overwhelmingly ordinary, common words one would expect to see in their daily inbox. Threat actors largely abandoned the use of urgent or time-sensitive subjects in their lures, instead opting for terms that are far less sensational and perhaps more likely to be mistaken as benign messages.

While ordinary words and phrases were the most prevalent terms appearing in email subject lines for the year writ large, we also saw evidence that threat actors remain attuned to major national events, and we see them quickly incorporate those themes into phishing lures and spam email to get higher click rates. In the example below, we saw the terms “Biden,” “Harris,” and “Trump” appearing more or less frequently across varying subject lines as threat actors tuned their message based on current events. Some of these changes aligned with major events in the 2024 presidential race. For example, when former Vice President Harris announced her campaign, we saw an increase in lures leveraging “Harris,” while lures with “Biden” started to drop off. In the immediate weeks following the election, email lures featuring “Harris” dropped off dramatically, while those leveraging “Trump” remained consistently high.

![Chart showing common terms in subject lines of malicious emails including Shared, Email, Request, Invitation, Business Update, Document, Invoice, Report, Message, Account, Payment, Fwd](![Figure 8: Common terms in subject lines of malicious emails])

![Chart showing malicious emails with election themed lures featuring Trump, Harris, and Biden across key election dates in 2024](![Figure 9: Malicious emails with election themed lures])

---

## Most used tools

### Actors largely preferred LoLBins, enabling them to blend in with regular network traffic

When we observed tool usage in Talos IR engagements, actors prioritized living-off-the-land binaries (LoLBins) — or tools and utilities found natively on an endpoint — more than commercial or open source tools (figure 11). While we saw LoLBins more frequently, the number of different LoLBins paled in comparison to the variety of commercial and open source tools (figure 10). This is because there are only a limited number of LoLBins native to targeted endpoints that will be of use to a threat actor. By contrast, the number of commercial and open source tools is ever growing, with actors continuously developing or creating these for their own use to deploy onto compromised systems.

Common LoLBins, such as PSExec, PowerShell and remote desktop protocol (RDP) are just three of the top five tools that were used to facilitate large components of an adversary’s attack chain. For example, Talos IR responded to a ransomware incident in which PsExec, originally designed for network management, was used to execute malicious batch (BAT) files as well as the final BlackBasta ransomware binary, underscoring the impact of the misuse of common LoLBins.

LoLBins enable actors to blend in with regular network traffic and avoid triggering antivirus or endpoint detection solutions. Furthermore, the nature of these binaries as default Windows operating systems can make it difficult to define normal usage patterns, complicating efforts by defenders to identify abuse. LoLBins also likely help improve the efficiency of malicious operations, as an attacker does not need to take the time to install additional software or test the efficacy of external tools and exploits.

One example of a newly observed open-source tool this year in Talos IR engagements was DonPAPI, which automates credential dumping remotely on multiple Windows computers. This tool locates and retrieves Windows Data Protection API (DPAPI) protected credentials, also known as DPAPI dumping. From an identity perspective, open-source tools like DonPAPI pose a significant risk to organizations based on the wide availability on code repositories like GitHub and the ease of installation. DonPAPI searches for files, including Wi-Fi keys, RDP passwords, and credentials saved in web browsers, to help authenticate and move laterally to identify other assets in the environment. Ransomware groups have reportedly used DonPAPI for a few years now, highlighting the emphasis adversaries put on obtaining credentials using these types of tools.

Since organizations regularly use many of these tools to support daily operations, it can be difficult to discern when their use or presence on an endpoint might be nefarious. The table on the following page shows the most commonly seen tools in Talos IR cases from each category (e.g., LoLBin (PsExec), open-source (Impacket), and commercial (Mimikatz)) are intended to be used, and how actors are coopting them for their own malicious purposes.

![Chart showing classification of tools observed in Talos IR incidents: Open Source (57%), Commercial (26%), LoLbins (17%)](![Figure 10: Classification of tools observed in Talos IR incidents])

![Chart showing LoLBins and tools used across the attack chain in Talos IR incidents including PsExec, PowerShell, Mimikatz, RDP, Cobalt Strike, Impacket, AnyDesk, RDPClip, Splashtop, NetScan, Filezilla, WinSCP, VPN services, Rclone, Advanced Port Scanner](![Figure 11: LoLBins used across the attack chain in Talos IR incidents])

### Use and abuse of most common tools in Talos IR cases

| Tool | PsExec | Impacket | Mimikatz |
| --- | ------ | -------- | -------- |
| **Intended use** | Part of Microsoft’s Sysinternals suite of tools; allows users to run commands on local and remote systems. | Open-source Python library for performing network audits. | A credential-dumping utility commonly used by penetration testers and red teams to extract plain text passwords. |
| **Malicious capabilities** | Has the ability to execute processes on other systems remotely, remotely create accounts on target systems, download or upload a file over a network share. | Impacket modules like SecretsDump allow actors to steal account and password information from Active Directory databases. | Contains functionality to acquire information about credentials, including from LSASS memory, registry hives, DPAPI, among others. |
| **Threat actor abuse** | Many ransomware operations use PsExec to run their payload on all systems in the domain. | APTs and other actors frequently use Impacket to gain a foothold in the victim environment and move laterally. | Cybercriminals to APT groups use Mimikatz to steal account logins and credentials to aid in moving laterally in the victim environment. |

---

## Ransomware

### Higher education hit hardest in 2024

Ransomware actors targeted education entities more than any other sector in 2024. This is in line with trends from previous years, where education was also the most targeted in 2022, and the second most targeted in 2023. Ransomware attacks were also high against public administration, manufacturing, and healthcare entities, suggesting ransomware actors focused their operations against large organizations that traditionally have a low downtime tolerance and/or limited security budgets (see figure 12).

Interestingly, almost all the ransomware attacks against the education sector targeted higher education entities. Universities typically have greater cybersecurity budgets than primary and secondary schools, presumably leaving them better defended, but the data they house such as proprietary and/or government-funded research is likely of greater value for a ransomware attack. Universities also rely more heavily on their IT infrastructure for things like online classes and student research, incentivizing these institutions to minimize disruptions to their operability.

![Chart showing targeted sectors for ransomware attacks in 2024 led by Education and Public administration](![Figure 12: Targeted sectors for ransomware attacks])

#### What makes education such an attractive sector?
- **Insufficient funding:** Primary, secondary, and high schools in particular often lack funding for proper information security capabilities, enabling adversaries to cause maximum damage with minimal ability for the victim to recover quickly.
- **Irregular monitoring:** Effective cybersecurity often requires the ability to monitor and respond to threats 24/7, which schools may not have the bandwidth for outside of school hours, on weekends, and during breaks.
- **Minimal network segmentation:** Many university networks have minimal segmentation between student networks, research networks, and administrative networks, providing adversaries a large attack surface and opportunity for lateral movement.
- **Attractive data stores:** Schools, particularly universities, store a range of data that is of interest to ransomware actors, including financial account information, personally identifiable information (PII), and classified research data.
- **Poor device hygiene:** Students often lack cybersecurity training and/or are less inclined to be concerned with the security of a school’s network, leading to a low level of personal device hygiene. This poor hygiene creates easier lots of points for actors looking to compromise easy targets and gain access to a school’s network.

![Chart comparing top affected sectors across 2023 and 2024 IR data](![Figure 13: Top affected sectors from both ransomware and our broader data set remain consistent across 2023 and 2024 IR data])

### Ransomware attacks more frequent in spring and summer

Ransomware actors appeared to be more active on average during the spring and summer, based on Talos IR findings (see figure 14). These months overlap with times when schools are closed for break or employees or students might be more likely to be on vacation — possibly contributing to slower response times to cyber incidents or a more relaxed cyber security posture in general. Education entities typically always operate at a reduced capacity during the summer months, and their calendars are often available online for the public — and possible attackers — to reference.

We’ve seen instances where adversaries take advantage of personnel being “out of office,” including one Talos IR case where a LockBit ransomware operator gained control of an IT account belonging to an employee on vacation. The threat actor easily gained access and created another account with admin rights to the entire domain to facilitate lateral movement.

![Chart showing ransomware attacks by month peaking in spring and summer](![Figure 14: Ransomware attacks by month])

### Actors prioritize disabling security solutions frequently and early on in their operations

Ransomware operators endeavored to disable targets’ security solutions in most of the Talos IR cases we observed, almost always succeeding (see figure 15). This was often one of the first actions actors took upon logging into a compromised network, taking advantage of endpoint solutions that did not require an agent or connector password and/or that were not configured properly.

Actors were quick to uninstall endpoint security products, which detect and quarantine the deployment of threats like ransomware on the system. They also modified certain solutions, like creating new firewall rules that can allow the adversary remote access, and removed evidence of their activity by deleting shadow copies and clearing event logs related to System, Application, and Security, a commonly observed ransomware TTP. These actions not only severely inhibit detection capabilities, but they also make system recovery much more difficult.

Separately, we also saw ransomware actors abuse poorly configured security solutions. Many out-of-the-box security products come with baseline/default policies enabled, but organizations often fail to configure these products specifically for their own network’s needs. Therefore, we saw many cases where ransomware operations were successful in environments where security policies were set to “audit-only” mode, meaning that the product only alerted an administrator to malicious activity but did not automatically block it.

We often see organizations have deployed endpoint protection in a passive manner, meaning the product is producing alerts to the user but not blocking malicious activity.

We repeatedly noticed alerts generated for an initial compromise, followed by alerts on suspicious behaviors for privilege escalation and lateral movement, and finally for execution of a malicious payload, all without a single event being blocked or actioned. If solutions are deployed passively, a security team may have only a short time window to see an alert, validate if it’s a true positive, and mitigate the activity with a response.

![Chart showing disablement of security solutions in Talos IR cases: Successful removal (48%), Not attempted (31%), Undetermined (17%), Unsuccessful removal attempt (4% )](![Figure 15: Disablement of security solutions])

### Initial access largely achieved via valid accounts

Ransomware actors overwhelmingly leveraged valid accounts for initial access in 2024, with this tactic appearing in almost 70% of related cases (see figure 16). As we outline in a later section of this report, actors are increasingly using identity-based attacks across the threat landscape, and with great success. In many cases, it’s much easier and safer for adversaries to simply log in to legitimate user accounts using stolen credentials than to use more complex means like exploiting vulnerabilities or deploying malware. This tactic is facilitated in large part by the sale of compromised credentials on dark web forums, enabling ransomware actors to essentially buy their key into a targeted organization.

Ransomware actors exploited public-facing applications nearly 20% of the time. Public-facing applications can be accessed by anyone on the internet, not just internal users within a company, making this an incredibly vast attack vector. These include applications that support online shopping platforms, customer login portals, social media sites, online banking systems, email servers, customer service portals, and more. Attackers often exploit known vulnerabilities or misconfigurations to gain access. These types of attacks typically require more technical skill, with actors relying on techniques such as SQL injection, cross-site scripting (XSS), or remote code execution, which likely explains why we see this less often than the simpler method of compromising valid accounts.

The prevalent use of valid accounts for initial access shines a light on the role of initial access brokers (IABs) in the ransomware ecosystem. Compromised credentials remain a valuable commodity, keeping IABs in business and streamlining adversaries’ operations.

![Chart showing initial access vectors: Valid accounts (69%), Public-facing application (19%), Drive-by compromise (12%)](![Figure 16: Initial access])

### Actors rely heavily on remote access tools, commercial products, and LoLBins

Based on our review of the tools ransomware actors most frequently used in 2024, we saw a focus on remote access (see figure 17). Specifically, actors leveraged commercial products and LoLBins for command and control in their campaigns. Many organizations rely on legitimate remote access applications such as AnyDesk and Splashtop for daily operations, such as remote work or IT help, making detecting or blocking malicious use of these tools more challenging.

While effectively blocking all unauthorized remote management tools may be a challenge, security can still be greatly improved through policy and technical controls. Adopting just one or two approved remote access solutions and banning all others is a good practice, as security teams can also ensure the chosen solutions are thoroughly tested and deployed as securely as possible. Additional controls, such as auditing and blocking DNS queries associated with these tools, blocking hashes associated with remote access software installers, and employing an application allowlisting program can also be leveraged to mitigate this threat.

![Chart showing top tools seen in Talos IR ransomware engagements including Mimikatz, PsExec, RDPclip, AnyDesk, Splashtop, RDP, Impacket, Cobalt strike, PowerShell, Netscan, HRSword, Advanced port scanner, AteraAgent, WinSCP, FileZilla, Putty, SoftPerfect, 7zip](![Figure 17: Top tools seen in Talos IR ransomware engagements])

### Ransomware operators impersonate IT personnel to gain remote access

Starting in November 2024, according to Talos IR observations, actors distributing BlackBasta and Cactus ransomware launched a campaign that leveraged social engineering to attain remote access to targets’ computers.

The actors first sent a flood of email spam to a victim mailbox, then proceeded to call the victim a few days later, usually via Microsoft Teams, posing as IT support and offering help for the email flood issue. Targets were directed to initiate a Microsoft Quick Assist remote access session and to install the software if they didn’t already have it on their system. Once the QuickAssist session was established, the adversary loaded tooling to collect information about the target system, establish persistence, elevate privileges, and ultimately deploy ransomware. BlackBasta ransomware was observed in earlier attacks, with the actors pivoting to Cactus ransomware later in the campaign.

This campaign underscores how organizations’ reliance on remote access tools for legitimate purposes can be manipulated by adversaries. It also serves as a reminder for organizations to educate users on recognizing approved ways in which their IT personnel will engage with them.

### LockBit remained top player while newcomer RansomHub quickly ascended to the #2 spot

For the third year in a row, LockBit was the most active ransomware-as-a-service (RaaS) group, based on our monitoring of posts made to ransomware actors’ leak sites. LockBit had the highest volume of posts (i.e., alleged victim compromises) among the 60+ groups we track, effectively claiming 16% of the market share in this crowded space (see figure 18). LockBit appearing as the frontrunner for the third year in a row is incredibly notable — in a dynamic space defined by constant change and the rise and fall of new ransomware groups, this type of longevity is unexpected.

Moreover, LockBit was the target of a major law enforcement takedown operation in early 2024, but was able to rebound and reconstitute, returning to normal activity levels soon after. Of note, LockBit’s builder was leaked in September 2022, likely contributing to the ransomware’s dominance as it expanded the pool of operators leveraging this encryptor.

Notably, newcomer RansomHub — a suspected successor of the Knight ransomware group that was first seen in February 2024 — followed close behind, accounting for 11% of posts.

Many of the RaaS groups that ranked as most active this year did not make the top ten last year, demonstrating how dynamic this space is.

#### Threat actor spotlight: RansomHub
RansomHub is a financially motivated RaaS group that has been increasingly active since at least February 2024. The ransomware is likely an updated version of Knight ransomware, which was for sale on underground forums in February 2024. RansomHub affiliates commonly leverage double extortion, encrypting a victim’s data while also stealing information and threatening to publish it on their data leak site unless a ransom is paid.

RansomHub currently plays a significant role in the ransomware threat landscape. They have attracted affiliates associated with well-known ransomware groups LockBit and ALPHV, as well as Scattered Spider, a financially motivated cybercrime gang that previously used ALPHV ransomware for their operations. RansomHub typically targets large organizations, likely in pursuit of hefty payouts; the average employee count of organizations targeted in RansomHub incidents we responded to this year was over 18,000 employees.

In line with the trend detailed above, we observed RansomHub operators successfully uninstalling endpoint protection on compromised hosts, including critical servers, in the majority of RansomHub engagements this year, enabling them to quietly deploy their ransomware.

![Chart showing 2024 volume of posts made to data leak sites by ransomware groups led by LockBit 3.0 (16%) and RansomHub (11%)](![Figure 18: 2024 volume of posts made to data leak sites by ransomware groups])

### Release of decryptor is the game-changer in disrupting ransomware gangs

2024 saw a number of disruptive operations led by law enforcement, with varying impacts on the targeted ransomware groups. One thing was clear, though — ransomware actors are far less likely to fully rebound from a takedown if associated decryption tools are made publicly available. ALPHV’s dominance plummeted after an FBI disruption at the end of 2023. This group was ranked second in our 2023 report and dropped to 22nd this year. As part of this disruption, the FBI seized several websites operated by the group and offered a decryption tool to affected victims, enabling them to restore their systems. Though the group stood up new servers after the takedown, the decryption operations significantly impacted the group’s revenue, and in March, administrators made the decision to shut down operations and declared their intent to sell their source code.

By contrast, the LockBit ransomware group was also targeted in a major takedown, but this operation did not include the release of a decryptor. Dubbed Operation Cronos, authorities in Ukraine, Poland, and the United States executed simultaneous actions against LockBit in February, taking control of key darknet infrastructure and arresting several affiliates. Though LockBit activity dropped— their posts on data leak sites went from 926 last year to 783 this year — they still emerged as the top actor in this space for the third year in a row.

Finally, in May 2024, Europol launched the largest-ever operation against malware loaders and botnets that support first-stage ransomware deployment, including IcedID, Smokeloader, SystemBC, Pikabot, and Bumblebee. This operation included the arrest of relevant targets, taking down of criminal infrastructure, and freezing of illegal proceeds. Nevertheless, we did not observe any notable dip in ransomware activity or in the overall volume of posts made to data leak sites, suggesting affiliates pivoted to using other tools and/or the malware’s infrastructure was rebuilt. Further, the prevalent use of valid accounts this past year could mean ransomware operators are no longer relying on tools such as these for ransomware deployment.

---

## Identity-based threats

### Identity attacks dominated the threat landscape in 2024

Identity was a common through line in 2024 across much of the data we looked at for this report. From initial access vectors to operational techniques further down the attack chain, threat actors relied heavily on identity-based attacks to power their operations. Adversaries are increasingly opting to compromise networks and accounts by simply logging in, rather than using more complex methods like exploiting vulnerabilities or deploying malware.

Identity-based attacks are attractive to threat actors because they can allow an adversary to carry out a range of malicious operations, often with minimal effort or without meeting much resistance from a security standpoint. This is due in large part to the activity being difficult to detect because it emanates from seemingly legitimate user accounts.

In addition to these types of operations being highly effective, there’s also a major market for stolen credentials — which are often used in the early stages of an operation — with valid password and username combinations frequently traded on the dark web. This means that there is a strong financial incentive for cybercriminals to steal credentials for future sale, and it also underscores the ease at which bad actors can obtain access to stolen credentials for use in their own operations.

In addition to credentials or personally identifiable information (PII), illicit marketplaces on the dark web also offer tools-as-a-service specifically for performing identity-based attacks, as well as outsourced services to obtain specific data or accesses to certain victim networks. Here are some other findings we’ve seen in this space, based on our dark web research:
- Marketed stolen data includes plaintext credentials, particularly for email accounts; SSH credentials; financial data, like bank identification numbers (BIN) or credit card numbers; session tokens from browser caches; addresses; and more. Cyber actors may have acquired this data using one or several TTPs we outline later in this section, or by using malware like infostealers.
- Software and infrastructure are sold as-a-service, commonly in tiered subscriptions ranging from less than $50 to around $750 for tools specially geared towards credential theft, like phishing kits and infostealers. These tools have user-friendly interfaces and offer customer assistance, lowering the barrier to entry for novice cyber actors.
- Experienced actors advertise their services and can be hired to perform specific functions. They also auction off access to high-profile companies, which on average sell between $1,000 and $3,000.
- Bulk lists of credentials commonly sell for as little as $10 to $15 on dark web marketplaces.

### Why are we seeing more identity-based attacks?
- **Growing attack surface:** The use of web applications, cloud-based environments, BYOD policies, and SSO solutions have been on the rise in recent years, especially with the normalization of remote work. This, in turn, has increased the number of credential-enabled access points within a network that could be exploited by attackers.
- **Hard to detect:** Many of these attacks leverage legitimate authentication processes, making them hard to detect at the network perimeter. Moreover, once an attacker gains access, malicious activity emanating from a valid user’s compromised account is more likely to go unnoticed.
- **Easy to carry out:** Attackers can easily obtain stolen credentials, often via the dark web and previous data breaches. Additionally, identity-based attacks largely rely on social engineering rather than technically sophisticated means.
- **Enables other operations:** In addition to gaining initial access to a target device, threat actors can continue to use identity attacks throughout their operations to escalate privileges, move laterally, internal social engineering attacks, and more.
- **Achieves significant access:** Using relatively simple means, actors can beat identity-based security challenges and gain access to the Active Directory, where an entire organization’s access and permissions are managed; cloud applications that power daily operations; or even IT networks and operational technology (OT) systems-crucial components of any organization’s cybersecurity.

### What is an identity attack?
An identity-based attack targets the unique digital identity of a user, organization, or machine to access data or networks. Digital identities encompass much more than just usernames and passwords for valid accounts. To obtain initial access, actors exploit a range of identifiers, like digital certificates, API keys, encryption keys, login credentials, and session tokens.

---

## Attacks against MFA

*(Content continues from report text relating to Multi-Factor Authentication attacks)*

---

## AI threats

*(Content continues from report text relating to Artificial Intelligence threats)*

[^1]: Footnote content referenced from Cisco Talos Year in Review 2024 telemetry and incident response data.

---

eys, session tokens, and more.
A unique identifier used to authenticate
and authorize a user or calling program to
an API. Used for security purposes and for
monitoring/limiting usage.
Digital certificate
An electronic file that verifies the
identity of a user, device, or server
Encryption key
A string of random bits that scrambles
and unscrambles data. Used in secure
connections like SSH, HTTP, and Telnet.
Session ID
Identifies a user’s session on a website
or application. If stolen, an attacker
can access resources as a legitimate
authenticated user.

©© 22002255 CCiissccoo aanndd//oorr iittss aaffiffilliiaatteess.. AAllll rriigghhttss rreesseerrvveedd.. || ttaalloossiinntteelllliiggeennccee..ccoomm ppaaggee 2288
4202
WEIVER
NI
RAEY
Identity-based threats
4202
WEIVER
NI
RAEY
Identity attacks omnipresent credentials, the use of a technique called DCSync
to abuse a Windows Domain Controller’s API, and
throughout the attack chain
attempts to access Local Security Authority (LSA)
Identity attacks in 2024
secrets—which can contain a variety of different
The most common tactic we observed in Talos
credential materials—which adversaries can obtain
IR engagements was the use of valid accounts —
We have seen a strong shift toward identity-based attacks in Talos IR incidents.
with system access to a host.
typically seen in the initial access phase — where
In 2024, the most common technique used to gain initial access was valid
accounts, making this the top access vector for the second consecutive year. adversaries obtained and abused credentials of Based on our assessments of threat actor intentions,
existing accounts to carry out various phases of we found that half of all identity-based attacks
their operations. OS credential dumping was also were related to ransomware and pre-ransomware
extremely common. While the majority of actors operations. Actors were also frequently motivated by
targeted credentials in LSASS memory and Active their intent to sell stolen credentials for a profit, such as
Adversaries’ goals in identity attacks
60%
Directory, we also saw a variety of other techniques with initial access brokers (32%), stealing credentials
in this threat category, including attempts to extract for espionage purposes or to enable future operations
credentials from the Security Account Manager (10%), and financial fraud, such as stealing credit card
More than half of (SAM) database, attempts to access cached domain data or conning victims into sending money (8%).
Talos IR cases had
an identity attack
Figure 19
component in 2024. Types of identity attacks observed in Talos IR
Number of attacks
Valid accounts
OS credential
dumping
44% Phishing
Brute force or
password spray
50% Ransomware and pre-ransomware
Nearly half of all identity Bypass MFA
32% Credential theft for monetization
attacks targeted the Active
AitM
10% Data theft for future operations
Directory. Another 20%
Web browser
8% Financial fraud
targeted cloud applications. credentials
Kerberoasting
Pass the hash

©© 22002255 CCiissccoo aanndd//oorr iittss aaffiffilliiaatteess.. AAllll rriigghhttss rreesseerrvveedd.. || ttaalloossiinntteelllliiggeennccee..ccoomm ppaaggee 2299
4202
WEIVER
NI
RAEY
Identity-based threats
4202
WEIVER
NI
RAEY
Identity in-the-wild:
Compromising Active
Case study:
Directory
How adversaries leverage
As mentioned above, 44% of all identity-
AD to disrupt data centers
based attacks seen in Talos IR incidents
and critical services
targeted Active Directory, a widely used
Microsoft service for Windows. Active
Directory holds critical user information In August 2024, a Cisco customer in the
like usernames, passwords, and access manufacturing sector reported that multiple
permissions, making it a gold mine of endpoint detection and response (EDR)
high-value data for attackers. Moreover, solutions had unexpectedly been uninstalled
according to a recent government report, from servers hosted in the organization’s
Active Directory is the most widely used managed data center, including two domain
authentication and authorization solution controllers, potentially indicating threat actors
in enterprise IT networks globally. had full Active Directory domain access. In
this investigation, Talos IR observed evidence
Adding to the risks around Active
suggesting the actor had compromised the
Directory being such a high-value target
Active Directory in preparation for deploying
for attackers, organizations often fail to
ransomware. The adversary leveraged
properly secure these environments.
ADExplorer, a utility that is part of the suite of
In many of the Talos IR cases involving
the Sysinternals admin tools, to browse the
compromised Active Directory,
different domains in the environment and dump
successful attacks occurred in enterprise
the Active Directory database.
environments that had misconfigured
security products and/or policies In this case, we saw the attacker use identity-
inconsistent with industry-recommended based attacks in the initial stages of their
best practices. operation, showing how affective these
techniques can be. We also saw how initial
access to the Active Directory was essential
to kicking off the broader attack, and how that
type of access can enable the deployment of
high-impact threats like ransomware.
Active Directory holds critical enterprise user information and is also the most widely used identity
and access management (IAM) solution globally, underscoring why actors targeted this service in
nearly 50% of all identity-based attacks seen in Talos IR cases.

©© 22002255 CCiissccoo aanndd//oorr iittss aaffiffilliiaatteess.. AAllll rriigghhttss rreesseerrvveedd.. || ttaalloossiinntteelllliiggeennccee..ccoomm ppaaggee 3300
4202
WEIVER
NI
RAEY
Identity-based threats
4202
WEIVER
NI
RAEY
Case study: Active Directory attack
1 2 3 4 5 6 7
Extract local Escalate to Reset Lateral Installation Access Result in pre-ransomware TTPs
passwords privileged passwords; movement of backdoors backup which could have eventually led
and password admin create new to domain and other systems to deployment of ransomware
hashes within accounts accounts to controllers software to if not actioned swiftly
AD database maintain and use of maintain
persistence Mimikatz persistent
access
We frequently observe accounts (i.e., user, admin, and service) with excessive
or incorrect privileges, accounts with weak or default passwords, flat network architectures,
and missing or misconfigured MFA. Our recommendations for mitigating Active Directory
compromises are in line with CISA’s strategies to mitigate the 17 most common techniques
used by adversaries and malicious actors to compromise Active Directory.

©© 22002255 CCiissccoo aanndd//oorr iittss aaffiffilliiaatteess.. AAllll rriigghhttss rreesseerrvveedd.. || ttaalloossiinntteelllliiggeennccee..ccoomm ppaaggee 3311
4202
WEIVER
NI
RAEY
Identity-based threats
4202
WEIVER
NI
RAEY
Identity in-the-wild:
Compromising
Here is an example of how threat actors could leverage many of the identity-based attack techniques
cloud services
to compromise cloud APIs, based on our experience in responding to these types of incidents.
providers’ APIs
Attacks targeting the cloud are also
Step 1: Access cloud API using compromised digital IDs Step 3: Execute commands for post-compromise activity
on the rise, with 20% of identity-
based compromises impacting cloud
• For initial access, a threat actor could leverage stolen API keys or • With proper permissions, actors may abuse cloud APIs to execute
applications, according to Talos IR
session cookies to bypass MFA and pivot to the cloud environment. commands by leveraging the cloud provider’s command line interface,
findings. Cloud APIs are necessary
In the case of Microsoft Entra ID, a cloud-based IAM service, a stolen which is intended to be used to manage cloud resources.
to facilitate seamless communication,
Primary Refresh token can be leveraged to maintain access and sign in
• Actors could execute commands to setup backdoors or create reverse-
integration, and data transfers
to services across the Microsoft cloud.
shell connections for persistence or to exfiltrate data.
between a wide range of cloud
• An actor could also steal credentials via phishing, deploying
services and between cloud and on-
infostealers, or, if the API relies on weak or easily guessable
premise applications.
credentials, using brute force techniques like password spraying
APIs are attractive targets because Step 4: With this level of access, there is the potential
or credential stuffing.
they can provide direct access to
for widespread disruptive and destructive attacks.
• Note that threat actors have found success in repurposing traditional
sensitive data and critical application
techniques to compromise cloud environments. • Actors could steal data that is handled by APIs, which includes PII like social
functionalities, as they are used
security numbers, financial data like credit card information, health-related
in software designed to support
data like medical records, intellectual property, private correspondences,
users and companies across all
Step 2: Use a cloud-specific tool to enumerate data
or user activity data like browsing history or physical locations.
business verticals. Cloud APIs are
Step 5: Evade detection
also inherently difficult to manage
• Skilled actors have created tooling that is freely available on the open web, • Potential attacks:
due to their sheer number, diverse
easy to deploy, and designed to specifically target cloud environments.
• Attackers can attempt
• Use stolen identities to impersonate victims for financial theft.
functionalities across different cloud
to evade detection by
• Some examples include ROADtools and AAAInternals,
providers, and the need to constantly • Use stolen accounts to conduct business email compromise (BEC)
deleting or modifying logs,
publicly available frameworks designed to enumerate
monitor and update them to keep attacks against third parties, including customers and trusted
burying malicious activity
Microsoft Entra ID environments. These tools can
pace with evolving cloud services. business partners.
by mimicking legitimate API
collect data on users, groups, applications,
Moreover, many cloud APIs are
• Disrupt business operations, possibly leading to delays traffic, reverting changes they
service principals, and devices,
publicly accessible, making it easy
in critical services. made to a cloud instance,
and execute commands.
for attackers to discover and test
• Remove users’ access to their accounts. and more.
ROADtools can also
potential vulnerabilities.
work with custom • Conduct ransomware or data theft extortion operations, possibly • Evasive measures can be
plug-ins to query and leading to financial loss, reputational damage, and government taken at any point in the
analyze data. compliance violations. attack lifecycle.

2024
YEAR IN REVIEW
Attacks against MFA
In partnership with
32

Attacks against MFA
© 2025 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com
4202
WEIVER
NI
RAEY
Threat actors capitalize Figure 20 Talos IR observations point to four top security
Observed MFA weaknesses in Talos IR cases
on a variety of MFA practices to guide MFA deployment:
weaknesses
8% 3% 24%
A key way in which actors can compromise
Enable MFA on VPN services: We consistently observed threat actors
a user’s identity, as mentioned earlier, is MFA bypass Passwordless No MFA
1
taking advantage of a lack of MFA on VPN services. Organizations,
by targeting the multi-factor authentication authentication enrollment
particularly those whose employees use VPNs to access corporate
(MFA) process. Given the amount of
networks, should prioritize requiring MFA to access their VPNs.
activity in this space, and the role that we 8%
see it play in attacks that could have been
New device
prevented, it made sense to devote an
maliciously enrolled Enact user education and MFA prompt thresholds: Threat actors
entire section of the report specifically to
2 also leveraged MFA exhaustion attacks, also known as MFA fatigue,
MFA attacks. Here, we explore the threats
by sending repeated requests to authenticate until the user finally
facing MFA, a key component of the rise in
accepted one. This attack can be mitigated by improving user
identity attacks we saw in 2024.
education as well as limiting the number of failed MFA requests from a
MFA weakness was the leading security single IP address or device.
weakness in Talos IR data this year, an
enduring trend year over year. Lack of
Implement higher security factors: Organizations should implement
MFA enrollment made up a quarter of
3 additional security measures, such as “challenge-response
the MFA issues observed; however, we
authentication,” where a user must provide a valid answer to a
saw a variety of other ways in which MFA
question. Examples of this include security questions, such as “what
was insufficiently deployed this year,
16% 22%
is your maiden name,” or “where did you go to high school;” and
enabling threat actors to gain access to
MFA exhaustion MFA not CAPTCHA, where an image is presented to the user who then must
key resources and establish persistence in
successful fully enabled
enter the characters they see to verify they are human. This creates
targeted networks.
another layer of challenges one must pass to gain access to the
19%
desired information or digital assets.
No MFA on
VPN services
Conduct robust monitoring of device registrations: Security teams
4 should continuously monitor and log when new devices are enrolled in
MFA, and/or require new users to authenticate through an additional
method before the new device is enrolled. Some MFA products, like
Duo, provide logging for organizations. In many cases, we saw actors
successfully add their own authentication device to victims’ MFA
Though MFA is proven to provide strong security, some organizations may choose not to employ it, systems, allowing them to operate under the radar.
given the cost and complexity of knowing which systems and resources to defend with it.
page 33

Attacks against MFA
© 2025 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 34
4202
WEIVER
NI
RAEY
MFA attackers go straight Figure 21
Types of applications targeted in MFA attacks
for IAM applications
Based on Cisco Duo data, IAM applications were most
frequently targeted in MFA attacks, accounting for nearly 24% Identity and access management (IAM) 6% Authentication protocol
a quarter of related incidents. IAM applications, combined
14% Network security 6% Authentication and network access control (NAC)
with network security, authentication and networking, and
remote access applications, accounted for more than 50%
10% Authentication and networking 6% Cloud security and authentication
of incidents where attackers targeted MFA deployments
(see figure 21).
9% Remote access 3% Operating system
The most commonly targeted IAM applications are listed
9% Application delivery and security
3% API communication protocol
below. A variety of vendors were targeted, including Citrix,
Microsoft, Fortinet, Palo Alto Networks, Cisco, and F5,
8% Software development kit (SDK)
2% Email and collaboration
which is not surprising given the widespread use of these
companies’ products globally.
Applications most frequently targed in IAM attacks
Shibboleth Central Authentication Active Directory Duo Central Microsoft 365 SSO
Service (CAS) Federation
An open-source SSO solution Duo’s centralized web portal SSO for Microsoft 365,
Service (ADFS)
widely used in education and An open-source SSO that users can visit to get enabling unified authentication
research institutions. solution that provides secure A Microsoft solution for SSO access to their organization’s for Microsoft services.
authentication for web and identity federation. applications.
applications.

Attacks against MFA
© 2025 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 35
4202
WEIVER
NI
RAEY
High volume, easily Figure 22 Top-targeted verticals Figure 23
Types of MFA attacks Top-targeted industries in MFA attacks
preventable spray align with broader
attacks are most attack trends Number of MFA attacks
17% 7% 1%
common
Higher
It is no surprise that the most targeted
RDP SSH DDOS education
industries in MFA attacks were education
Attackers are probing for organizations brute brute
force force and healthcare, as these sectors have
lacking MFA or with MFA incorrectly
IT
consistently been among the top-targeted
configured. Password spray attacks,
in our Talos IR findings across all attack
in which an adversary tries common
types as well as ransomware campaigns Healthcare
passwords to access many accounts,
specifically (detailed earlier in this report).
were the most frequent type of threat
we observed against MFA-protected When looking at the types of impacted Manufacturing
applications. However, MFA is highly education entities, colleges and universities
effective at mitigating brute force and were targeted six times more frequently
Finance
password spray attacks due to the additional than K-12 schools. Higher education
authentication measure that is required, institutions can be ideal targets for data
Business
which often results in lower success rates theft and password harvesting for several
services
for these types of campaigns. reasons: 1) There is a wider attack surface,
as high volumes of students are accessing Public
Push spray was the second most common
administration
university resources via their mobile
attack type. This technique, also known as
devices; 2) Students with access to this
MFA “bombing” or “fatigue,” goes beyond Real estate
information are likely easy targets because
& construction
the simple password guessing approach
they may not employ good cybersecurity
represented by spray attacks. Threat actors
practices; and 3) The applications colleges
Legal services
flood a victim’s device with MFA push
and universities use are more likely to store
notifications prompting them to confirm/
sensitive information about their students,
accept the login request in hopes that the K-12
including social security numbers, billing education
victim will eventually relent and unwittingly
and payment information, driver’s licenses,
grant the adversary access.
and other PII that is typically not collected Retail
by primary, secondary, and high schools.
Nonprofit
22% 53% Transportation
& storage
Push spray Password
spray
Utilities

Attacks against MFA
© 2025 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 36
4202
WEIVER
NI
RAEY
MFA in-the-wild:
Phishing and device
Case study: MFA attack against university
compromise lead to
major breach at large
university
Victim: Large university
(100,000+ users)
The following case study is an example of
how we see the above trends play out in
everyday scenarios. In this incident, a large
university with more than 100,000 users We later confirmed this device
was the victim of both phishing and device was not active with any other
compromise. users and blocked it from being
used as an MFA device on Duo.
Based on our investigation, the threat
actor already had stolen credentials (login/
password combinations) for targets at
this organization, which they had likely
purchased from an initial access broker
(IAB) or obtained from a separate data
leak. The actor sent phishing emails to a
system administrator and tricked them into
clicking an authentication link that added
the attacker’s device to the victim’s MFA
account. From there, the adversary was
able to send internal phishing emails to
Actor obtains first Actor sends Victim clicks activation Actor uses
several other users on the network.
factor creds phishing email to link, actor adds their compromised
One major security pitfall for the (username/password admin with device to the victim’s MFA account to
organization was that it had 50 combos), likely through activation link compromised gain access to
administrator accounts — a significantly data leak or IAB MFA account internal email
More than 50 admins, Actor targets other
high number given the sensitive access
working as contractors users on the networks
admins have. Moreover, all of the admins
in mass phishing
were contractors, which is not a security
campaign
best practice, and we know from our own
research that threat actors often prefer to
target contractors over account holders
with comparable privileges.

2024
YEAR IN REVIEW
AI threats
37

AI threats
© 2025 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com
4202
WEIVER
NI
RAEY
Overview of the AI threat landscape How threat actors could leverage AI in 2025
in 2024 and 2025
We predict the following developments in 2025:
2024 brought the continued proliferation of artificial intelligence and
machine learning (AI/ML) applications, as well as various business The rise of agentic AI:
integrations and tools. Meanwhile, in cybersecurity, service
Agentic AI, “AI systems and models that can act autonomously to achieve
providers have increasingly integrated AI into their products and
goals without the need for constant human guidance,” could imperil
workflows to enhance threat and vulnerability detection, automate
organizations that are neither prepared nor equipped to handle agentic
responses, and bolster organizations’ overall security postures.
systems and their potential for compromise. As agentic systems increasingly
While the advancement and adoption of AI/ML technology
integrate with disparate services and vendors, the opportunity for exploitation
has paved the way for copious new business opportunities, it
or vulnerability is ripe. Agentic systems may also have the potential to conduct
also complicates risk and threat environments. Cisco’s Robust
multi-stage attacks, find creative ways to access restricted data systems,
Intelligence team — the threat researchers and developers behind
chain seemingly benign actions into harmful sequences, or learn to evade
Cisco’s new AI Defense security solution — is watching this space
detection by network and system defenders.
closely. Here are the potential AI-based cyber attacks they are
most worried about as we look ahead:
Continued social engineering at scale:
• Cybersecurity risk to AI systems, applications, and infrastructure;
From social engineering to propaganda proliferation, cybercriminal and state-
• Data exfiltration, tampering, accessibility risk from AI models; and sponsored actors will continue to leverage AI technologies to improve the
personalization and professionalization of their malicious activities.
• Use of AI to automate and professionalize threat actor cyber
operations, particularly in social engineering
Automated vulnerability discovery and exploitation:
While these types of threats might be on the horizon for 2025 and
Threat actors could use AI to uncover vulnerabilities, including zero-day
beyond, 2024 mainly saw AI enhance existing malicious tactics,
exploits, leading to faster exploitation and increased risk across both the public
rather than aid in the creation of new ones.
and private sectors.
Threat actor use of AI
Capabilities that can compromise AI models,
off to a slow start in 2024 systems, and infrastructure:
Numerous areas of risk could emerge in the development of capabilities
Generative AI is powerful and its potential to influence the threat
targeting AI models and systems themselves, including using adversarial
landscape is staggering, but in 2024, threat actors’ use of AI did
inputs to trick AI-powered security filters, hijacking AI agents used in business
not significantly enhance attackers’ TTPs. Although threat actors
operations workflows, as well as attacking elements of the AI supply chain
have the potential to harness AI and develop novel capabilities, we
(e.g., corrupting training data, compromising a model’s cloud infrastructure),
have not yet observed those capabilities deployed at scale in-the-
not to mention traditional cyber attacks that can be used to target AI models
wild. In the meantime, we have observed both state-sponsored
and systems.
adversaries and cybercriminals use AI for 1) social engineering,
and 2) task automation and other productivity improvements in the
threat actors’ attack lifecycle.
page 38

AI threats
© 2025 Cisco and/or its affiliates. All rights reserved. | talosintelligence.com page 39
4202
WEIVER
NI
RAEY
Generative AI for social engineering Task automation and productivity gains
in the attack lifecycle
The accessibility of generative AI tools, such
Interested in more of what
as large language models (LLMs) and deepfake Threat actors have attempted to leverage chatbots
technologies, has led to a surge in sophisticated to assist in malware development and task
Cisco has to say about AI?
social engineering attacks, but this increase can automation to improve their success rates. For
be broken down into two distinct parts: the use example, malicious actors have queried chatbots as
A significant number of new AI policy developments occurred in
of AI for social engineering and the use of AI for a summation tool to gather open-source intelligence
2024, largely in response to the increasing prevalence of AI-powered
automating malicious activities. By combining these on their targets.
technologies and their market expansion. In Cisco’s inaugural State of AI
two components, attackers can increase their
Research has proven that LLMs can be used to Security report, we provide a comprehensive overview of developments in
success rates exponentially, as they can produce
exploit one-day vulnerabilities (i.e., vulnerabilities that the AI threat landscape. The report covers important developments in U.S.
higher volumes of socially engineered lures that are
have been disclosed but not patched in a system). and international AI policy; in-depth analysis of threats to AI infrastructure,
of higher quality with the assistance of LLMs and
Threat actors have leveraged LLMs to assist with AI supply chains, and AI applications; and original research into many
generative AI. As such, we expect phishing and
basic scripting tasks and code debugging, but cutting-edge AI security topics like algorithmic jailbreaking, dataset
other social engineering techniques to continue
we have not yet observed threat actors deploying poisoning, and data extraction.
improving with AI’s assistance, while spam and
advanced AI capabilities for vulnerability scanning
phishing detection races to catch up.
and exploitation in real-world scenarios. However, Read here
In 2024, cybercriminals leveraged these technologies cybercriminals have allegedly developed and sold
to create convincing phishing campaigns and multiple tools that can aid in vulnerability research,
manipulate individuals into divulging sensitive reconnaissance, and exploit writing. © 2025 Cisco and/or its affilies. All rights reserved.
information or granting unauthorized access to their
organization’s networks and systems.
State-sponsored advanced persistent threat (APT)
groups and other sophisticated actors may leverage
aspects of these features, such as deepfake video
and audio for conducting interviews or phone calls
or automating social engineering.

2024
About Cisco Talos
YEAR IN REVIEW
Cisco Talos is one of the most trusted threat intelligence research teams on the globe.
We are comprised of world-class researchers, analysts, incident responders and engineers.
Talos powers the Cisco portfolio with comprehensive, proven and tested intelligence covering
every customer environment, every event, every single day, all around the world. Talos’
core mission is to protect and defend Cisco’s customers by understanding the broad threat
landscape and distilling the massive amount of telemetry we digest into verifiable detection,
intelligence and response for our customers, users and the internet at large.
Our job is your defense.
Stay connected
View our blog: TalosIntelligence.com/blog | Subscribe: Threat Source newsletter | Follow us: LinkedIn, X, Mastadon and BlueSky
© 2025 Cisco and/or its affiliates. All rights reserved. Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates
in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks. Third-party trademarks mentioned
©ar e2 0th2e5 pCroispceor tayn odf/ othr eitisr raeffislpiaetcetsiv. eA lol wrignehtrss .r Tesheer uvesed .o f| t htael owsoinrtde lpligaretnnceer .dcoomes not imply a partnership relationship between Cisco and any other company. (1110R) pppaaagggeee 444000