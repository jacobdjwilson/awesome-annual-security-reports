# 2023 Manufacturing Threat Landscape

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Ransomware Groups Targeting Manufacturing](#ransomware-groups-targeting-manufacturing)
- [Supply Chain Risk and Exposure](#supply-chain-risk-and-exposure)
- [Exposure of OT Environments Due to IT and OT Convergence](#exposure-of-ot-environments-due-to-it-and-ot-convergence)
- [Dissecting the Attack Flow for Manufacturing](#dissecting-the-attack-flow-for-manufacturing)
- [Attack Flow Overview](#attack-flow-overview)
- [Attack Flow Steps](#attack-flow-steps)
- [Initial Foothold: Phishing and Business Email Compromise (BEC)](#initial-foothold-phishing-and-business-email-compromise-bec)
- [Initial Foothold: Logging in](#initial-foothold-logging-in)
- [Initial Foothold: Vulnerability Exploitation](#initial-foothold-vulnerability-exploitation)
- [Initial Foothold: Supply Chain](#initial-foothold-supply-chain)
- [Initial Payload](#initial-payload)
- [Expansion / Pivoting](#expansion--pivoting)
- [Malware: Infostealers](#malware-infostealers)
- [Malware: RATs](#malware-rats)
- [Malware: Ransomware](#malware-ransomware)
- [Exfiltration / Post Compromise](#exfiltration--post-compromise)
- [OT Risks in Manufacturing](#ot-risks-in-manufacturing)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)
- [Appendix/Reference](#appendixreference)
- [Threat Groups](#threat-groups)
- [8BASE](#8base)
- [Bian Lian](#bian-lian)
- [BlackCat/ALPHV](#blackcatalphv)
- [Clop](#clop)
- [LockBit](#lockbit)
- [Play](#play)
- [RansomedVC](#ransomedvc)
- [Royal](#royal)

DECEMBER 2023

## Executive Summary
In an era defined by technological advancement and interconnected systems, the manufacturing industry is embracing digital transformation to fuel unprecedented efficiency and productivity. However, this evolution is accompanied by profound and growing cybersecurity challenges.

Cyberattacks can cripple production lines, resulting in staggering financial losses that can reach thousands of dollars per minute. These disruptions directly contradict the industry's primary objective of maximizing profitability.

As a result, manufacturers are facing a growing unease regarding cyber resilience. With only 19% of industry leaders confident in their cyber defense mechanisms, the sector is confronted by an array of cyber threats that pose a significant risk to operations, with the average cost of a manufacturing breach reaching $4.7M.

The digital transformation sweeping through the manufacturing industry has led to a convergence of operational technology (OT) and information technology (IT) systems, effectively expanding the potential attack surface for cyber threat actors. This convergence, while beneficial for operational efficiency, also introduces new cybersecurity challenges. Many OT systems, traditionally isolated from networked environments, are now exposed to cyber threats, often without sufficient defenses in place.

Among the prominent cyber threats facing the manufacturing sector is ransomware, with a growing global trend of threat actors exploiting disruption capabilities and lucrative ransom potential. Additionally, the sector's extensive repositories of intellectual property and supply chain data make it an attractive target for access and data brokers, who seek to capitalize on this valuable information.

In September 2023, US-based consumer and professional products manufacturer Clorox shared that its first-quarter results could see a "material impact" from a cybersecurity attack that damaged portions of its IT infrastructure and caused widescale disruption to its manufacturing operations. In May 2023, French electronics manufacturer Lacroix closed three factories for a week because of a cyberattack.

$4.7M
vs
$4.4M 
AVERAGE COST OF A 
DATA BREACH IN THE 
MANUFACTURING 
SECTOR COMPARED TO 
ALL OTHER INDUSTRIES

There are a number of factors that make manufacturers especially vulnerable to cyberattacks, including:

- **OT Attack Surface**: 
Manufacturing companies heavily rely on OT systems, such as industrial control systems (ICS) and supervisory control and data acquisition (SCADA) systems, to control and monitor their production processes. The increasing interconnection of these OT systems with the Internet heightens their vulnerability to cyberattacks. This connectivity also makes it easier for attackers to spread malware and viruses throughout a manufacturing environment.

- **Supply Chain**: 
Manufacturing companies are often part of complex supply chains, which can be exploited by cyber attackers to gain access to sensitive data or shut down systems. Supply chain attacks can be difficult to detect and prevent, as they often involve multiple actors and systems.

- **Legacy Systems**: 
Many manufacturing companies still use legacy systems that are not designed to withstand modern cyberattacks or are more difficult to patch. With the increasing drive for interconnectivity across the workplace, these systems are now more vulnerable to attacks that can exploit known vulnerabilities or take advantage of misconfigurations.

- **Downtime Impact**: 
Manufacturing operations are often highly automated and interconnected, which means that a cyberattack can have a significant impact on production and revenue. In some cases, a single attack can cost a company millions of dollars in lost revenue and downtime, making them a prime target.

- **Safety and Operational Risks**: 
Cyberattacks on manufacturing systems can have serious safety and operational consequences. For example, an attacker could manipulate a control system to cause a physical explosion or release hazardous materials. This becomes particularly prevalent during military conflicts. Nations or patriotic hackers, particularly in times of conflict, may attack water facilities, power plants, traffic light systems, etc., in an attempt to disrupt critical infrastructure or wreak havoc. It's important to consider the non-financial ramifications of a cyberattack; many small manufacturers are traditional, family-owned businesses and the psychological damage to their owners when cutting wages or downsizing staff due to the effects of a cyber incident are rarely given sufficient thought.

With more than 250 security researchers across the globe, the Trustwave SpiderLabs team puts its resources to task in looking into what leads to these breaches. We are uniquely positioned to do so, as we perform over 100,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 4,000 to 10,000 per day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Continuous Threat Hunting, Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur as well as mitigations and controls that your organization can put in place to prevent these compromises. 

This report will examine the multitude of threats that pose challenges to the manufacturing industry. It will also provide recommendations for how the manufacturing sector can mitigate these risks and protect their customers and data.

We will begin by highlighting the significant trends currently affecting the industry: ransomware, supply chain risk, and the convergence of OT and IT. Subsequently, we will analyze the attack flow specific to the manufacturing sector, offering insight on specific threat actors, actionable intelligence, and recommended mitigations for each stage to illustrate how organizations can proactively identify and prevent attacks to avoid lasting impact. 

In this report, we will examine many of the most prevalent threat tactics and threat actors operating across manufacturing and throughout the attack chain, including:

THREAT ACTORS
- LockBit
- Clop
- BlackCat/ALPHV
- Royal
- Play
- BlackBasta
- 8BASE
- Bianlian
- Malas
- Mallox

THREAT TACTICS
- Phishing and BEC
- Credential Access
- Initial Access Brokers
- Vulnerability Exploitation
- PowerShell
- IT and OT Convergence
- Malware

For additional information about the most prevalent threat actors, please go to the Appendix.

## Emerging and Prominent Trends
## Ransomware Groups Targeting Manufacturing
### The Threat
According to a recent GuidePoint report, manufacturing is the most impacted industry by ransomware. Ransomware attacks have a devastating impact on manufacturing companies, causing financial losses, operational disruptions, and reputational damage.

Hacker groups are increasingly targeting the manufacturing sector due to its perceived vulnerability and the potential for high-value ransoms. Ransomware attacks are expected to continue to rise in the manufacturing sector, driven by the evolving threat landscape and the increasing reliance on digital technologies. Attackers are targeting supply chains to gain access to multiple companies simultaneously, maximizing their impact and ransom demands. Furthermore, the supply chain is often an attack route to a specific, but better-protected target. Additionally, attackers are targeting OT systems to cause physical damage and disruptions.

### What Trustwave SpiderLabs Is Seeing
According to Trustwave’s ransomware research, LockBit 3.0 has emerged as the predominant ransomware strain, representing over 30% of the purported manufacturing victims. Other prominent ransomware strains such as Clop, BlackCat/ALPHV, and Royal have also substantially affected the manufacturing threat landscape. The presence of multiple strains, each less prevalent, indicates a strategic diversification by attackers in their operational tactics, eschewing dependence on a singular strain.

The pervasive nature of ransomware has no geographical limits and has adversely affected multiple manufacturing organizations globally. In our research, we’ve found the US emerges as the principal target, bearing 63% of the documented ransomware victims. It is followed by the UK and France, which account for 14% and 9% of the reported victims, respectively.

Our team has observed that companies specializing in industrial equipment, robotics, automation, heavy construction, automotive, electronics, and chemical manufacturing have been more prominently listed as victims on ransomware extortion websites.

![Top 10 threat actor groups in manufacturing over past 365 days]

These threat groups have increasingly targeted the manufacturing sector. LockBit was responsible for a cyberattack on one of the world's largest tire manufacturers in February 2023, and it also compromised automotive entities and targeted chemical manufacturing firms, auctioning unauthorized access and sensitive data. BlackCat/ALPHV operators compromised a US cooling products manufacturer in May 2023, highlighting vulnerabilities in the company's network.

Play ransomware targeted a German chemical product manufacturer in May 2023 and a US metals manufacturing and mining company in the following month. Additionally, BianLian claimed to have extracted 1.4 TB of data from a Maryland-based manufacturing company in April 2023, providing proof files. LockBit also targeted US-based aerospace manufacturer Boeing in November 2023.

These incidents underscore the growing ransomware threat to the manufacturing industry.

### Mitigations to Reduce Risk
- Remember the best defense is a good offense. The subsequent sections will dive into each of these further, but regularly train and test employees, make sure policies and patches are up to date, and deploy layered email security to help detect and cleanse malicious emails.

- If prevention of infection is not possible, audit controls become crucial indicators of potential compromise. This involves enabling system logs on valuable systems and workstations, as well as implementing network logging through flows, Network Monitoring Solutions, or IDS devices on ingress and egress channels.

- Implement active monitoring. Merely enabling logs is insufficient; if logs are not monitored, they lose their effectiveness. Regular monitoring helps establish a baseline of regular activity, making abnormal behavior or traffic more conspicuous.

- Establish and regularly practice a formal Incident Response process.

- Perform on going Underground and Dark Web monitoring for information leakage that may have been missed.

## Supply Chain Risk and Exposure
### The Threat
The supply chain constitutes a fundamental component of the manufacturing industry, serving as the pivotal process for transforming raw materials into finished products. 

This intricate operational process often involves the participation of multiple stakeholders. It is this interdependence that renders the manufacturing industry susceptible to cyberattacks, as a disruption within any facet of the supply chain can potentially trigger substantial downtime across the entire production spectrum.

For example, in 2022, one of the most significant supply chain attacks worldwide involved one of the biggest automakers in the world. A ransomware attack at one of the major suppliers, led to the Japanese vehicle manufacturer to partially take down its manufacturing processes. The downtime caused the company a five percent drop in production.

Manufacturers can also serve as a target in supply chain attacks where threat actors utilize less mature security controls as a route into other entities where disruption is the goal, or valuable intellectual property may be exposed.

Additionally, OT plays a critical role in the manufacturing industry's supply chain, encompassing the hardware and software systems that control and monitor industrial processes. As manufacturing operations become increasingly interconnected and reliant on digital technologies, OT security has emerged as a major concern in the supply chain threat landscape.

### What Trustwave SpiderLabs Is Seeing
The advent of the “Manufacturing-as-a-Service" paradigm has brought forth a transformation in supply chain dynamics. Amidst a growing trend of cybercriminals targeting supply chains to breach or disrupt critical business systems, the importance of fortifying supply chain security becomes much more important. The image below illustrates a classic example of what we call a “Domino Risk” from a supply chain perspective.

![Black Basta ransomware group claiming a successful attack on a leading light metal manufacturer]

The shift towards a heightened level of interconnectivity and interdependence within this paradigm has witnessed a proliferation of third-party integrations within IT and OT infrastructures. This proliferation, in turn, highlights the importance of validating suppliers’ cybersecurity measures and controls. This is particularly important with the proliferation of vulnerabilities in third party products like SolarWinds, MOVEit, and 3CX which highlights the exposure that third-party vendors can create for manufacturing organizations.

### Mitigations to Reduce Risk
- Know your supply chain. Have an inventory of all critical suppliers and ensure vendor security due diligence is being performed regularly.

- Prioritize the security and protection of your systems and those of third-party partners.

- Implement the latest security measures to ensure the safety of information assets and infrastructure.

- Recognize that the security of the ecosystem is dependent on the strength of its weakest link.

- Regularly update OT software and firmware patches to address known vulnerabilities and reduce the risk of exploitation.

- Implement segmentation techniques to isolate OT systems from IT networks, reducing the attack surface and limiting the spread of malware.

## Exposure of OT Environments Due to IT and OT Convergence
### The Threat
Historically, there was a clear demarcation that existed between OT and IT. OT traditionally bore the responsibility of overseeing and regulating physical processes and machinery integral to manufacturing operations. On the other hand, IT was chiefly concerned with data management, communication infrastructure, and the processing of information within the organization. This demarcation of roles and functions was long considered a fundamental aspect in the manufacturing and industrial domains.

But with the advent of digital technologies and the drive for increased efficiency, industries are increasingly integrating OT and IT systems. This integration is driven by the need to gather real-time data from the factory floor and use it for data analytics, predictive maintenance, and other business intelligence purposes.

### What Trustwave SpiderLabs Is Seeing
The convergence between IT and OT systems and the impact of this convergence can be highlighted by recent attacks wherein attacks on IT systems lead to disruptions on the OT side of the operations. Thus the relative obscurity and isolation of OT systems is not an assurance anymore that these systems are safe from attack. Consequently, many OT systems lack robust security measures which can potentially lead to access to infrastructure and sensitive data.

In attacks against manufacturing entities, we typically see threat actors gaining initial access through the IT environment. This access can be achieved through various methods, including exploiting vulnerabilities, conducting phishing attacks, or purchasing remote access from an Initial Access Broker (IAB).

For example, in June 2022, a cyberattack initiated by the Sandworm group targeted a critical infrastructure organization in Ukraine. They first infiltrated the organization's IT environment by deploying a well-known webshell on one of the victim's internet-facing servers. Following this, the attackers gained access to the organization's OT environment by going through a hypervisor that hosted a Supervisory Control And Data Acquisition (SCADA) management instance for the substation environment.

Once inside the IT environments of manufacturing organizations, threat actors can move across the enterprise network, potentially extending their reach to the manufacturing plant networks by exploiting connection points between enterprise and plant systems, like Historian systems, SCADA or file servers. Once in the plant network, attackers can disrupt operations through various vectors, among which are targeting Human Machine Interfaces (HMIs) which are used to interact with Industrial Control Systems (ICS). For example, by targeting HMIs, control machinery and processes, potentially causing significant disruptions or even complete shutdowns in plant operations.

### Mitigations to Reduce Risk
- Construct a consistent framework for communication protocols and data formats.

- Establish secure connectivity measures to link IT and OT systems.

- Perform detailed evaluations of IT and OT systems to pinpoint integration and security needs.

- Adopt secure middleware or gateway solutions for IT-OT system interoperability.

- Educate IT and OT staff on cooperative strategies to promote a collective security methodology.

- Formulate interdisciplinary oversight teams (IT and OT) for integration and coordination.

- Employ IoT platforms to integrate IT and OT systems, providing capabilities such as data ingestion, device management, analytical tools, and live monitoring.

## Dissecting the Attack Flow for Manufacturing
## Attack Flow Overview
While the specifics and details of every breach and compromise may vary, there is typically a specific attack flow that occurs from the initial security bypass to escalation, compromise, followed by persistent home on your network and exfiltration and/or destruction of valuable data. The following analysis presents an overview of the attack flow specific to the manufacturing sector, incorporating insights from the Trustwave SpiderLabs team and offering actionable mitigations for organizations to implement.

At each stage of this attack flow, the recommended actions aim to give proactive guidance, helping to minimize the potential risks—whether they are financial, reputational, regulatory, or physical—for a manufacturing organization. The usual sequence of events goes like this:

## Attack Flow Steps
### Initial Foothold
This is the step where the attacker successfully triggers a security bypass that will give them the ability to expand their access to suit their motives and goals. This initial foothold can take various forms, ranging from successful phishing attacks to vulnerability exploitation or even logging into public-facing systems using previously acquired credentials.

In this section, we will explore the most common methods through which attackers gain this initial foothold in manufacturing like phishing, vulnerability exploitation, and access brokers.

### Initial Payload
Once the attackers have established a foothold on the network, they will proceed to download more sophisticated tools and malware.

In this section, we will specifically concentrate on real-world examples of the types of payloads that frequently target the manufacturing industry.

![Attack Flow Steps](https://i.imgur.com/4012r4a.png)

### Expansion / Pivoting
The initial foothold typically involves a low-value workstation, such as a phishing victim's laptop, or a network appliance like a VPN endpoint.

In this section, we will highlight how once armed with the necessary tools, attackers can target higher-value accounts and systems, such as Domain Admins, root accounts, Active Directory Systems, and Database servers.

### Malware
There are a variety of malware types with a myriad of uses. We’re talking about Remote Access Toolkits (RATs), Infostealers, Ransomware, and many others.

In this section, we will focus on the types of malware that are prevalent in the manufacturing industry.

### Exfiltration / Post Compromise
In most cases, the primary motive behind compromises is data theft.

In this section, we will explore the types of data that are targeted and exfiltrated in manufacturing-related compromises. Additionally, we will present real-world examples of manufacturing data breaches to provide concrete illustrations.

## Initial Foothold: Phishing and Business Email Compromise (BEC)
### The Threat
Phishing and email-borne malware stand out as the most commonly exploited method for gaining an initial foothold in an organization. Instead of attempting to exploit the software or systems on the network, attackers direct their focus towards targeting the individuals operating the keyboard.

Using a persuasive and time-sensitive email, the attacker successfully convinces their victim to take specific actions, such as opening an attachment, clicking on an embedded URL, or following instructions to transfer funds to a purported "stranded CEO."

Typical phishing goals:
- **Credential theft**: 
Invoice from a customer includes a link. When the link is clicked it prompts the user for their password before “access is granted to the document”
- **Malware insertion**: 
Via PowerShell scripts, JavaScript, Macros
- **Triggering action**: 
Wire transfer for “stranded CEO” (BEC)

### Trustwave SpiderLabs Insights
The Trustwave SpiderLabs team is committed to monitoring various email-based threats, such as opportunistic phishing, targeted/spearphishing, and Business Email Compromise (BEC). In the past year, our team has noted intriguing developments in the tactics and delivery approaches used in email-based attacks within the manufacturing sector. These advancements have played a role in sustaining the continuing significance and effectiveness of these types of attacks.

Based on data from our manufacturing client base, we have observed that HTML comprises 72% of malicious attachment types in this sector. HTML is used to smuggle malware, phishing sites, and act as redirectors.

![The top malicious attachment filetypes for manufacturing]

An example of an HTML attachment that generates convincing fake Microsoft login

Executables are the next most prevalent filetype comprising 20% of all malicious attachments that our team has found in this sector. We have observed that Remote Access Trojans (RATs) such as Agent Tesla, Remcos, and AveMaria, and information stealers such as LokiBot, Azorult, Formbook, and Snake Keylogger make up most of these executables.

Our team has also observed that Microsoft Office documents comprised around 5% of the malicious attachments. They are mostly downloaders to facilitate the next stage threats. These files commonly capitalize on known vulnerabilities on Microsoft products such as CVE-2017-11882, CVE-2018-0802, and CVE-2021-40444.

![An example of a malicious Word document leveraging an exploit for CVE-2021-40444]

In December 2022, there was a surge in OneNote spam campaigns. The OneNote files had embedded malicious files like WSF and VBS which were disguised by an overlapping image often disguised as a clickable button. However, as quickly as this threat arrived, it disappeared again as Microsoft imposed greater restrictions on OneNote files.

As for major email botnet operations against the manufacturing industry, we observed that Emotet was mostly quiet in 2023. Meanwhile, Qakbot campaigns were more frequent during the start of the year but dropped during Q2 of this year due to its infrastructure being disrupted in a multinational operation.

![Activity trends in the major email botnet operations (Emotet and Qakbot)]

Aside from botnet operations, our team observed interesting developments in terms of the distribution mechanism used in phishing campaigns. IPFS has emerged as the most abused service, accounting for 46% of emails, with compromised WordPress sites coming in at second at 14%.

![Top URL categories used for distribution of phishing attacks]

![A Microsoft phishing example using IPFS URL to host a phishing site]

The five most common categories being impersonated by threat actors in phishing attacks are software services, like Microsoft, shipping providers, like DHL, and social network platforms, like Facebook. Microsoft was the most frequently impersonated brand (31%) with DHL and LinkedIn following at 13% and 12%, respectively.

![Breakdown of brands being impersonated in phishing attacks]

![An email posing as DHL informing the recipient about parcel’s arrival - note the victim email address at the end of the URL]

The most frequent phrases that appear across phishing emails focus on password-related alerts and “action required” phrases. Other common themes include mailbox-related alerts, document sharing, e-signing, and shipment notifications.

![Word cloud of the most common phrases used in phishing email subject lines]

Aside from mass phishing attacks, our team also BEC attacks which are often more sophisticated, making it easy for threat actors to trick their victims. Our analysis found a large portion of the phrases used are in relation to Payroll Diversion emails. Terms related to banking details such as ‘direct deposit,’ ‘bank information,’ and ‘payroll information’ are often used to refer to the payroll account of the impersonated employee.

![Word cloud of the most common phrases used in BEC attacks]

Other terms such as ‘change request,’ ‘change direct,’ and ‘update payroll’ are also related to this type of BEC emails. The phrase ‘before the next payroll’ is also commonly used by threat actors to request the adjustment of the banking information as soon as possible - before the next payroll is credited.

Additionally, Trustwave SpiderLabs has been monitoring the effect of AI and LLMs like ChatGPT on phishing and BEC types of attacks. Many of the red flags that we teach users to identify phishing emails include items like picking out misspellings, grammar mistakes, and general clumsiness of writing that may indicate that the author is not a native speaker.

The quick maturity and expanded use of LLM technology is making the crafting these emails even easier, more compelling, highly personalized, and harder to detect. Trustwave SpiderLabs has detected multiple spearphishing attacks with malicious attachments or links being used against manufacturing entities. Creating these targeting, compelling spearphishing emails will likely be made easier for attackers with LLM technology.

### Mitigations to Reduce Risk
- Consistently conduct mock phishing tests to assess the effectiveness of anti-phishing training and retrain repeat offenders.

- Implement robust anti-spoofing measures, including deploying technologies on email gateways.

- Deploy layered email scanning with a solution like MailMarshal to provide better detection and protection.

- Utilize techniques to detect domain misspellings, enabling the identification of phishing and BEC attacks.

> When layered, captures up to 90% of malicious emails missed by other email security vendors.

## Initial Foothold: Logging in
### The Threat
Sometimes attackers gain access to your network simply by logging in. This could occur if the default credentials for a device have not been changed, if weak passwords are used and vulnerable to brute-forcing, or if credentials have been purchased from an underground forum. Beyond simple credentials, attackers can purchase access to a webshell or active sessions already in place in a target organization.

### Trustwave SpiderLabs Insights
The Trustwave SpiderLabs team performs proactive threat hunts in our clients’ environments to identify breaches or compromises that have yet to be identified. In the course of these engagements, the team regularly finds the following issues that directly contribute to this threat.

**CREDENTIAL ACCESS**

The most common tactic observed in the reported incidents was Credential Access, which accounted for 45% of the incidents analyzed. The techniques observed in the attacks relied mostly on password brute-force attempts, but also OS credential dumping and stealing or forging Kerberos tickets.

![Incidents in manufacturing categorized using MITRE ATT&CK matrix]

The most common findings from our threat hunts indicate a prevalence in unsecured credentials related to automated scripts exposing passwords in clear text. Our team has observed that these findings often occur in scripts pertaining to file transfer applications.

**INITIAL ACCESS BROKERS**

In 2023, the underground market experienced a marked increase in the trade of access credentials pertaining to data, networks, and systems across a variety of industries, elevating these credentials to the status of highly coveted commodities. Initial Access Brokers, which have been more prevalent on underground marketplaces and forums, were observed offering unauthorized access to organizations within the manufacturing industry.

For example, our team observed that an undisclosed threat actor listed access to a firm operating within the steel industry in both Mexico and the United States. The access was offered in exchange for three bitcoins, which, at the time, was valued at approximately US $62,500.

The advertised access included an AnyDesk remote desktop account, an administrative account, a VPN account, and additional accounts, all reportedly equipped with remote connectivity capabilities. This provides everything needed for an attacker to gain initial access and the means to laterally move within the organization. Also note that this is not a unique occurrence as there are many other examples in various Dark Web and underground forums as seen in the examples below.

![Post taken form a Russian Dark Web forum with a threat actor selling Citrix access to manufacturers’ networks in US]

![Post taken form a Russian Dark Web forum with a threat actor selling root access to external websites for an industrial automation company]

![Post taken form a Russian Dark Web with a threat actor selling domain admin access to a US manufacturer]

We have often observed that manufacturing entities require remote access to industrial environments for internal users and third parties like vendors and service providers. Insecure implementations of remote access such as lack of multi-factor authentication (MFA) and weak ciphers oftentimes make it easier for threat actors to leverage stolen credentials to gain access to the organization.

Finally, the ability to monetize remote access affords sellers significant influence, allowing them to demand substantial sums, particularly when the targets are essential services. The manufacturing sector is increasingly targeted due to its substantial revenue, critical position in supply chains, and a perceived likelihood of complying with extortion demands.

**INFOSTEALERS**

The information stolen by infostealer malware is typically offered up for sale. Some of the notable information stealers that we have observed in the manufacturing industry are LokiBot, Azorult, Formbook, and Snake Keylogger.

**DRIVE-BY-DOWNLOADS**

Our teams have also observed the use of drive-by-downloads for initial access. For example, we have seen the SocGolish malware leverage drive-by-downloads by masquerading as a software browser update to gain initial access to the victim's machine. Typically, we see a malicious JScript file downloaded that then leads to information stealing and retrieval of additional malware from a remote host.

![Version of JScript that communicates with remote SocGolish infrastructure]

### Mitigations to Reduce Risk
- Regularly rotate passwords (e.g., every quarter) to mitigate issues related to valid accounts.

- Implement password complexity requirements to enhance security.

- Ensure that OT and IoT management have strong and complex passwords. Check for administrative consoles for these devices that might be running; they could be potential points of entry.

- Ensure secure remote access mechanisms are in place. Enable MFA to provide an additional layer of protection for accounts.

- Securely store credentials in programs in Password Managers to prevent credential abuse.

- Encrypt credentials when used in scripts to safeguard sensitive information.

- Audit local administrative accounts regularly and obfuscate admin accounts by not using admin in the name.

- Use LAPS on Windows systems to manage local accounts.

- Implement Privileged Access Management (PAM) and Privileged Identity Management (PIM) solutions to deepen defense in depth strategy.

## Initial Foothold: Vulnerability Exploitation
### The Threat
Exploiting vulnerabilities is often the first thing people think of when it comes to information security. This topic encompasses discussions on zero days, patch agility, proof-of-concept exploits, and vulnerability disclosure.

Simply put, a vulnerability refers to a bug in software that introduces security risks. Attackers develop specialized software or scripts to exploit the vulnerability and circumvent security controls, such as authorization, authentication, and audit controls. Once the vulnerability is exploited, the attacker can bypass a security control and introduce a payload, which can manifest as various types of malware, as we will explore later.

A software patch provided by the vendor resolves the bug responsible for the vulnerability and prevents exploitation.

### Trustwave SpiderLabs Insights
Through active monitoring, Trustwave SpiderLabs identified the most common exploits targeting our clients in the manufacturing industry.

The techniques used in the attacks were mostly unspecified Remote Code Execution attempts, Apache Log4J (CVE-2021-44228), MOVEit RCE (CVE-2023-34362), Exchange Server RCE (CVE-2021-41040, CVE-2022-41082). Other attempts leveraged Cross-Site Scripting.

One factor that we have observed in manufacturing is the prevalence of legacy systems, which hinders vulnerability remediation, as these systems often prove difficult to patch or replace. This gap in remediating vulnerabilities further increases the exposure of manufacturing entities to threat groups that may want to leverage these issues to gain access or disrupt operations. It is also common that threat actors leverage the existence of these vulnerabilities by selling and auctioning them to other threat actors.

For example, last May 2022 the Black Basta ransomware group claimed responsibility for an attack on a prominent US-based agricultural machinery manufacturer. Interestingly, a known threat actor specializing in the sale of initial access and vulnerabilities had previously listed a structured query language injection (SQLi) vulnerability associated with the same manufacturing entity. Though the correlation between the two events is ambiguous, cooperation activities in targeting the industrial products and services domain are evident.

In February 2023, this same threat actor also advertised SQLi vulnerabilities affecting multiple organizations, claiming that it could be exploited for data exfiltration purposes. In a subsequent development in March 2023, the threat actor announced additional SQLi vulnerabilities, including one purportedly impacting a major France-based industrial and manufacturing conglomerate, which allegedly led to the exposure of two databases containing eight sets of administrative credentials.

Additionally, a recent Trustwave SpiderLabs search of Shodan, which scans all public IP addresses on the Internet, turned up over 198,000 open ports, service banners, and/or application fingerprinting under the factory and manufacturing tag with the addition of the top 13 manufacturing companies in the world.

![Publicly accessible ports and services for the manufacturing sector]

Based on our review, HTTP/S related ports like 443 (https), 80 (http), 8081 (http) were the most common. Interestingly, 7547 (TR-069) appeared more prominently for manufacturing. This protocol is used for remote management of Customer Premises Equipment (CPE), or devices connected to a service provider's network, such as home routers, modems, and other network equipment. Our team also noted other common ports and services were 161 (SNMP), 123 (NTP), 22(SSH), 9090 and 179 (BGP).

![Top 10 publicly accessible ports for the manufacturing sector]

Across the manufacturing organizations that had exposed services, there were numerous devices, particularly network devices that are outdated and vulnerable to known attacks, potentially exposing their organizations to attacks. Here are some examples of the vulnerable systems that our team found:

![Multiple Fortinet Firewalls are exposed to CVE-2023-27997]

![Huge uptick of attacks on Cisco ASA SSL VPN’s, with most attacks exploiting default accounts and common username and password]

![Now discontinued, Boa webservers were used to attack Indian power grids back in 2022]

![CVE-2023-30799 is a vulnerability in Mikrotik router OS]

![Multiple instances of gSoap vulnerable to Devil’s Ivy (CVE-2017-9765)]

![A plex bug has been actively exploited according to CISA]

### Mitigations to Reduce Risk
- Utilize vulnerability assessments and penetration testing to identify vulnerable servers. Pay close attention to possible OT and IoT devices that may be running remote services.

- Promptly patch critical vulnerable systems. Ensure both IT and OT systems are covered by the vulnerability and patch management process. If patching is not possible or needs additional time, ensure that compensating controls like network based “virtual patching” and network isolation are in place.

- Databases that store sensitive consumer data should be a priority for system and software patching. Database auditing tools like Trustwave’s DbProtect that can flag misconfiguration and user rights can also help eliminate risk.

- Place all servers behind the firewall and practice proper network segmentation for enhanced access control.

- Disable Internet access for servers that do not require it.

- Strengthen access controls to minimum necessary levels for authorized users.

## Initial Foothold: Supply Chain
### The Threat
Supply chain attacks are increasingly prevalent. Instead of directly targeting multiple large entities, attackers concentrate their efforts on trusted third-party partners frequently utilized by these entities. This strategy is sometimes referred to as "the Domino Risk," as the attackers aim to topple one domino, causing a chain reaction that affects numerous others.

The return on investment for this type of attack appears to be substantial, considering its current popularity and the alarming compromise incidents we often encounter in headlines.

### Trustwave SpiderLabs Insights
The supply chain constitutes a fundamental component of the manufacturing industry, serving as the pivotal process for transforming raw materials into finished products. This intricate operational process often involves the participation of multiple stakeholders. It is this interdependence that renders the manufacturing industry susceptible to cyberattacks, as a disruption within any facet of the supply chain can potentially trigger substantial downtime across the entire production spectrum.

For example, in 2022, one of the most significant supply chain attacks worldwide involved one of the biggest automakers in the world. A ransomware attack one of the major suppliers, led to the Japanese vehicle manufacturer to partially take down its manufacturing processes. The downtime caused the company a five percent drop in production.

The advent of the “Manufacturing-as-a-Service" paradigm has brought forth a transformation in supply chain dynamics. Amidst a growing trend of cybercriminals targeting supply chains to breach or disrupt critical business systems, the importance of fortifying supply chain security becomes much more important. The image below illustrates a classic example of what we call a “Domino Risk” from a supply chain perspective.

![Black Basta ransomware group claiming a successful attack on a leading light metal manufacturer]

The shift towards a heightened level of interconnectivity and interdependence within this paradigm has witnessed a proliferation of third-party integrations within IT and OT infrastructures. This proliferation, in turn, highlights the importance of validating suppliers’ cybersecurity measures and controls. This is particularly important with the proliferation of vulnerabilities in third party products like SolarWinds, MOVEit, and 3CX which highlights the exposure that third-party vendors can create for manufacturing organizations.

### Mitigations to Reduce Risk
