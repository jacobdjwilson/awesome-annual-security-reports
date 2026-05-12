# 2023 Financial Services Sector Threat Landscape

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Artificial Intelligence and Generative AI](#artificial-intelligence-and-generative-ai)
- [Ransomware Groups Targeting Financial Services](#ransomware-groups-targeting-financial-services)
- [Supplier and Third-Party Risk](#supplier-and-third-party-risk)
- [Dissecting the Attack Flow for Financial Services](#dissecting-the-attack-flow-for-financial-services)
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
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)
- [Appendix/Reference](#appendixreference)
- [Threat Groups](#threat-groups)

---

# Executive Summary

![Average cost of a data breach in financial services ($5.9M) compared to all other industries ($4.4M)]

When questioned about why he robbed banks, Willie Sutton famously responded, "Because that's where the money is." Some things never change, and threat actors are similarly drawn to the financial services sector for the substantial financial rewards they offer.

Financial services organizations are attractive targets because of the elevated potential for monetary gain. Serving as repositories of wealth, this sector is rich with lucrative opportunities for cybercriminals, who exploit them for financial gains through extortion, theft, and fraud.

In addition to the money itself, the financial services sector stores large volumes of sensitive data, including customer information, financial records, and intellectual property.

Trailing only behind the healthcare industry, the financial services sector ranks second in terms of the cost of a data breach. In 2023, the average cost of a data breach in the financial services sector amounted to $5.9 million, compared to the industry average of $4.4 million, according to data from the Ponemon Institute.

In March 2023, Melbourne-based Latitude Financial had more than 14 million records compromised when a threat actor stole an employee’s login credentials. In June 2022, one of the largest financial providers in the U.S., Flagstar Bank, suffered a massive data breach, leaking the Social Security numbers of almost 1.5 million customers – their second cybersecurity incident in two years.

There are a number of factors that make the financial services industry especially vulnerable to cyberattacks, including:

- **Sensitive Data**: The financial services industry holds a vast amount of sensitive customer data, including names, addresses, Social Security numbers, bank account numbers, and credit card numbers, making the sector a high-value target. Organizations must be vigilant and inventory where this data resides. It’s impossible to protect something without knowing where it is.
- **Heavily Regulated**: Heightened regulation is a double-edged sword. While it incentivizes increased protections, it can also make it complex and expensive for financial institutions to implement and maintain effective cybersecurity programs.
- **Trust as Currency**: Consumers anchor their financial decisions on trust. If trust is eroded by the compromise of personal data or account information, customers can and will take their money elsewhere. This means they are a prime target for cyber criminals who will try to exploit this dependency on trust.
- **Partnership Complexity**: As a byproduct of strict regulations, it can be difficult for financial institutions to partner with vendors or incorporate tools that could improve their security posture. There are unique barriers and requirements for partners, adding complexity to an already complicated landscape.
- **Interconnectedness**: In addition to business partners, the financial services industry is heavily interconnected with other service vendors and financial entities, such as merchants and payment processors, opening it up to supply chain and third-party risk.

With more than 250 security researchers across the globe, the Trustwave SpiderLabs team puts its resources to task in looking into what leads to these breaches. We are uniquely positioned to do so, as we perform over 100,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 4,000 to 8,000 per day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Continuous Threat Hunting, Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur as well as mitigations and controls that your organization can put in place to prevent these compromises.

This report will examine the multitude of threats that pose challenges to the financial services industry. It will also provide recommendations for how financial institutions can mitigate these risks and protect their customers and data.

We will begin by highlighting the significant trends currently affecting the industry: Generative AI, ransomware, and third-party risk. Subsequently, we will analyze the attack flow specific to the financial services sector, offering insight on specific threat actors, actionable intelligence, and recommended mitigations for each stage to illustrate how organizations can proactively identify and prevent attacks to avoid lasting impact.

---

# Emerging and Prominent Trends

## Artificial Intelligence and Generative AI

### The Threat
Generative AI and Large Language Models (LLMs) have taken the world by storm. While AI isn’t new, the advances made in Generative AI and LLMs are setting new benchmarks for what’s possible for financial services organizations, adversaries, and defenders.

For financial services, the nature of the data, from credit card information to Social Security numbers, heightens the risks of data potentially being leaked to these tools.

Moreover, financial organizations face an increased risk of exposure due to their reliance on third-party vendors who may incorporate Generative AI or LLMs into their products, raising concerns about the potential loss of control over customer data used for training these models.

### What Trustwave SpiderLabs Is Seeing
Trustwave SpiderLabs consistently finds that phishing is one of the most effective methods attackers use to gain an initial foothold in financial services organizations. However, this method is highly dependent on the quality of the lure, the writing style, and the contextual and grammatical clues given in the phishing email.

But now comes the advent of Generative AI and LLMs. The quick maturity and expanded use of LLM technology makes the crafting of phishing emails even easier, more compelling, highly personalized, and harder to detect. We’re also seeing an increase in deepfakes as a result of more sophisticated technology.

Lately, we have seen the emergence of LLMs like WormGPT and FraudGPT on underground forums, highlighting the potential cybersecurity risks posed by their criminal use.

### Mitigations to Reduce Risk
- Evaluate your security solutions with Generative AI and LLMs in mind.
- Create robust internal policies and employee training for proper data usage.
- Determine how to govern the tools versus instituting broad-based bans.
- Consider instituting an internal AI Infosec working group.

---

## Ransomware Groups Targeting Financial Services

### The Threat
According to U.S. Commodity Futures Trading Commission (CFTC) commissioner Christy Goldsmith Romero, “A 2022 survey of 130 global financial institutions found that 74% experienced at least one ransomware attack over the past year.”

Clop has been the most active ransomware group targeting banks and financial services, with the GoAnywhere attack in February 2023 impacting banks and over 10 financial institutions being named among the victims of the MOVEit attack.

### What Trustwave SpiderLabs Is Seeing
Trustwave SpiderLabs has seen a continuing rise in ransomware incidents directly targeting the financial services sector. Clop, LockBit, and Alphv/BlackCat remain the predominant groups operating in this sector.

![Screenshot of the Lockbit Leak site claiming to have data from a breach of Banco De Venezuela]

### Mitigations to Reduce Risk
- Regularly train and test employees, ensure policies and patches are up to date, and deploy layered email security.
- Regularly back up your data and store backups offsite.
- Secure exposed RDP services, patch known vulnerabilities, and/or disable them if not necessary.

---

## Supplier and Third-Party Risk

### The Threat
The financial services industry is heavily interconnected with other businesses and with other financial entities, such as merchants and payment processors, opening it up to supply chain and third-party risk.

### What Trustwave SpiderLabs Is Seeing
Trustwave SpiderLabs has seen a sharp rise in successful attacks due to third-party software and services, including high-profile, supplier-based attack vectors like SolarWinds, 3CX, and just recently, MOVEit.

### Mitigations to Reduce Risk
- Ensure your own systems and those belonging to third-party partners are secure through regular penetration tests and vulnerability scans.
- Maintain an inventory management system for all software.
- Implement a routine vulnerability scan before installing any new applications.

---

# Dissecting the Attack Flow for Financial Services

## Attack Flow Overview
The typical sequence of events unfolds as follows:
1. Initial Foothold
2. Initial Payload
3. Expansion / Pivoting
4. Malware
5. Exfiltration / Post Compromise

## Initial Foothold: Phishing and Business Email Compromise (BEC)
Phishing and email-borne malware stand out as the most commonly exploited methods for gaining an initial foothold.

![Diagram showing phishing email flow: HTML attachment -> User Action -> LNK Shortcut -> Qakbot DLL]

### Trustwave SpiderLabs Insights
- HTML attachments are the most common malicious attachments (78%).
- 33% of these HTML files employ obfuscation.
- 24% of emails with malicious attachments attempted to spoof American Express.

## Initial Foothold: Logging in
The use of valid accounts continues to be one of the easiest and most efficient ways for a threat actor to get an initial foothold.

### Mitigations
- Regularly rotate passwords.
- Enable multi-factor authentication (MFA).
- Implement Privileged Access Management (PAM) solutions.

## Initial Foothold: Vulnerability Exploitation
Exploiting vulnerabilities is often the first thing people think of when it comes to information security.

### Common Exploits
- Apache Log4J (CVE-2021-44228)
- Exchange Server SSRF
- SQL Injection

## Initial Foothold: Supply Chain
Supply chain attacks are increasingly prevalent. Attackers concentrate their efforts on trusted third-party partners frequently utilized by these organizations.

---

# Appendix/Reference

## Threat Groups
- **8BASE**: A ransomware group known for targeting various sectors.
- **BlackCat/ALPHV**: A sophisticated ransomware-as-a-service (RaaS) operation.
- **Black Basta**: Known for double-extortion tactics.
- **Clop**: Highly active in targeting financial services via zero-day vulnerabilities (e.g., MOVEit).
- **Medusa**: A ransomware group targeting corporate networks.
- **LockBit**: One of the most prolific ransomware groups globally.
- **Play**: Known for utilizing sophisticated evasion techniques.
- **Royal**: A threat group that evolved from previous ransomware operations.

[^1]: Ponemon Institute data regarding the average cost of a data breach.

---

ntain continued access.  Techniques in this area include, but are not
limited to, exploiting privilege escalation vulnerabilities, password hash
manipulation, pass the hash, and kerberoasting among others.

EVENT-TRIGGERED EXECUTION

Different operating systems and cloud environments have mechanisms that
initiate actions in response to specific events such as user log ins or the
execution of particular applications or binaries. These mechanisms can be
exploited by adversaries to maintain continuous access to a compromised
system by repeatedly executing malicious code.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies35

Trustwave SpiderLabs
conducts 100K hours of
pentesting each year

Mitigations to Reduce Risk

 ▪ Perform routine assessments of all applications within the

environment to counter the use of custom applications that might
introduce vulnerabilities.

 ▪ Establish a detailed whitelist of applications on specified hosts
to reduce exposure. This will prevent malicious actors from
introducing applications that masquerade as legitimate apps and
executing malicious commands.

 ▪ Enforce privilege constraints to block unauthorized execution of

different shells by unprivileged sources.

 ▪ Conduct regular user and service account reviews to establish

account ownership and legitimacy of accounts.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesMalware

Server

Malware

36

Malware: Infostealers

The Threat
As the name may suggest, infostealers are specialized malware designed
with the primary function of stealing information. While various types of
malware, such as Remote Access Trojans (RATs) and certain ransomware
families, may possess this capability, infostealers specifically focus on this
function, often targeting specific types of data for theft. Infostealers primarily
seek data both at rest and in transit.

In-place infostealers primarily target local data stored on compromised
storage devices, aiming to exfiltrate information such as contacts, cached
passwords, cryptocurrency wallets, and system details (e.g., operating
system, patch level, installed software).

In-transit infostealers, on the other hand, focus on stealing data that users
enter but is not stored as a file on the system. These infostealers usually
manifest as malicious web browser plug-ins that act as proxy servers
for specific connections. For example, they may monitor connections to
your bank's website and manipulate the connection to steal your account
information or perform unauthorized actions, such as initiating a wire transfer,
by utilizing your access.

Trustwave SpiderLabs Insights
Trustwave SpiderLabs and threat operations teams have insights into
potential infostealers in our clients’ environments obtained through the
delivery of our managed services, threat hunts, DFIR, and malware analysis
teams across clients worldwide.

The following are the notable infostealers that our team has observed
operating in the financial services sector:

FORMBOOK

FormBook is an infostealer that has been operational since mid-2016. Its
primary function is to harvest sensitive information from compromised
systems, with a particular emphasis on extracting data tied to online forms,
passwords, and assorted credentials. Believed to originate in South Korea,
FormBook has been associated with multiple cybercriminal campaigns.
FormBook comprises a range of functionalities, including keylogging,
screenshot capture, clipboard data recording, and the pilfering of data
from web-based forms. It is versatile and can target a diverse array of
applications, web browsers, and online services to pilfer sensitive data. As
time has progressed, FormBook has advanced its capabilities to encompass
attributes like obfuscation tactics, anti-analysis measures, and the encryption
of stolen data prior to its transmission.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExfiltration /Post CompromiseHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial Payload37

This email, which claims to be from the financial department of a shipping company,

contains both Formbook malware and a credential phishing HTML attachment

XLOADER

XLoader is considered to be a derivative of Formbook. One notable feature
of XLoader is its cross-platform nature, particularly the ability to operate on
MacOS. Similar to Formbook, it has the capability to harvest login credentials,
capture screenshots, keylog, and execute malicious files. It is capable of
“recovering” passwords from multiple web browsers and email applications.
Additionally, XLoader can leverage various tactics to evade analysis,
including a large number of fake C&C domains.

LOKIBOT

Lokibot is an infostealer that has been active for several years. It specializes
in infiltrating systems and harvesting sensitive data. Primarily targeting
credentials and valuable information across diverse online services, Lokibot
is disseminated through phishing campaigns and exploit kits. Its modular
architecture enables attackers to customize functionalities while features
such as keylogging and web injection that facilitate the theft of usernames,
passwords, and other data.

SNAKE KEYLOGGER

In late 2020, Snake Keylogger emerged as a new information stealing
malware. The malware was written in the .NET programming language and
exhibits a modular design making it very versatile. Among its core functions
are keylogging, pilfering stored login credentials, screen captures, and
retrieving clipboard data. All of which are subsequently sent to the threat
actor.

Snake Keylogger is typically distributed through phishing and spearphishing
campaigns, leveraging emails with malicious Microsoft Office documents
or PDF files. The malware concealed within the document typically acts
as a downloader and leverages PowerShell scripts to fetch a copy of
Snake Keylogger onto the compromised system, subsequently initiating its
execution.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies38

Mitigations to Reduce Risk

 ▪ Use host-based anti-malware tools that can assist in identifying and
quarantining specific malware, but understand they have limitations
and are often circumvented by custom malware packages.

 ▪ If prevention of infection is not possible, audit controls become

crucial indicators of potential compromise. This involves enabling
system logs on valuable systems and workstations, as well as
implementing network logging through flows, Network Monitoring
Solutions, or IDS devices on ingress and egress channels.

 ▪ Implement active monitoring. Merely enabling logs is insufficient;
if logs are not monitored, they lose their effectiveness. Regular
monitoring helps establish a baseline of regular activity, making
abnormal behavior or traffic more conspicuous.

 ▪ Establish and regularly practice a formal Incident Response process.

 ▪ Perform ongoing Underground and Dark Web monitoring for

information leakage that may have been missed.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies39

Malware: RATs

The Threat
A Remote Access Trojan (RAT) is malware whose primary function is to
provide an administrative level backdoor to a compromised system. A RAT
typically has a wide variety of additional features that allow the attacker to:

 ▪ Download any files from the system

 ▪ Capture sensitive data, similar to infostealers

 ▪ Take screenshots

 ▪ Execute any binary on the system

 ▪ Upload and execute additional malware to the system

 ▪ Activate the webcam and/or microphone

 ▪ Sniff network traffic

Malware

Server

Trustwave SpiderLabs Insights
The following are the remote access trojans (RAT) that Trustwave SpiderLabs
team has observed operating in the financial services sector:

Malware

AGENT TESLA

Agent Tesla is a RAT written in .NET that first appeared in 2014. It can
take full control of a compromised system, it has a very flexible command
and control channel and can connect to the C2 via HTTP, HTTPS, Email,
or in a Telegram channel. We have observed Agent Tesla as one of the
executables frequently associated with email phishing campaigns in the
financial services industry.

Example of Word document attached to the phishing email that loads an external file,
an RTF document that leveraged CVE-2017-0199 to download and install the Agent

Tesla RAT

Agent Tesla includes a keystroke logger, the ability to access anything on the
clipboard, and can search the hard drive for other valuable data. Trustwave
SpiderLabs published an in-depth analysis of Agent Tesla in conjunction with
how it is often attached to phishing campaigns.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExfiltration /Post CompromiseHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial PayloadTRUSTWAVE MDR ELITE
OFFERS AN MTTA OF
15 MINUTES AND MTTR OF
<30‧MINUTES

40

GIGABUD RAT

We have been monitoring reports and various analyses of Gigabud RAT.
The threat actor behind this appears to be targeting financial institutions
in Asia-Pacific, particularly in Southeast Asia. Gigabud RAT was first
detected in September 2022. It impersonates trusted entities and targets
various businesses and institutions and then proceeds to capture sensitive
information through screen recording. As a remote access tool, Gigabud
provides the means for the threat actor to access a victim's account where it
can execute actions on the user's device including performing gestures.

Mitigations to Reduce Risk

 ▪ Use host-based anti-malware tools that can assist in identifying and
quarantining specific malware, but understand they have limitations
and are often circumvented by custom malware packages.

 ▪ If prevention of infection is not possible, audit controls become

crucial indicators of potential compromise. This involves enabling
system logs on valuable systems and workstations, as well as
implementing network logging through flows, Network Monitoring
Solutions, or IDS devices on ingress and egress channels.

 ▪ Implement active monitoring. Merely enabling logs is insufficient;
if logs are not monitored, they lose their effectiveness. Regular
monitoring helps establish a baseline of regular activity, making
abnormal behavior or traffic more conspicuous.

 ▪ Establish and regularly practice a formal Incident Response process.

 ▪ Perform ongoing Underground and Dark Web monitoring for

information leakage that may have been missed.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies41

Malware: Ransomware

The Threat
Ransomware typically encrypts or locks data and then demands the victim
pay a ransom to regain access to the data. Modern ransomware campaigns
prevent recovery by attempting to remove access to backup files and
deleting Volume Shadow Copies.

More recently, ransomware groups have added an extortion component
to these attacks. They will exfiltrate valuable data prior to deploying the
ransomware and then publicly post proof of the attack to scare/shame the
victim organization into paying the ransom. If the ransom isn’t paid, the threat
actor still has a dataset they can turn around and sell. This is commonly
referred to as a double extortion tactic.

Threat actors will go to great lengths to get paid. Triple extortion techniques
have also been seen where threat actors will strategically deploy a
Distributed Denial of Service (DDOS) attack as a three-layer extortion tactic.

Malware

Server

Trustwave SpiderLabs Insights
Trustwave SpiderLabs analyzed the ransomware incidents directly targeting
the financial services sector and found Clop, LockBit, and Alphv/BlackCat
continue to be the predominant groups operating in this sector. A more
detailed listing of the top threat groups below:

Malware

Clop

39%

O
t
h
e
r
s

Pla
y

3
%

3
%

4
%

BianLian

Royal

Akira

4%

4%

4%

5%

10%

8BASE

Black Basta

ALPHV

2
4
%

L
o
c
k
B
i
t
3
0

.

Top 10 threat actor groups in financial space over past 365 days

Though threat actors attack targets worldwide, a majority of the targeted
companies reporting a breach are from the U.S. with India, and Russia/Mexico
coming in a far second and third respectively.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExfiltration /Post CompromiseHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial Payload
42

51% United States

9% India

7% Russia

7% Mexico

5% Argentina

4% Brazil

4% United Kingdom

4% Canada

9% Other

Top 10 geographic locations of companies in financial sector suffering a
reported breach

Our teams continually encounter ransomware. Here is a summary of the
ransomware families encountered most often in the financial services sector.

CLOP

The Clop ransomware group appears to be the most prevalent ransomware
operating in the financial services sector and has recently been associated
with a massive campaign targeting an SQLi zero-day vulnerability in the
popular MOVEit file transfer software. The financial institutions Clop has hit
had an average of $2.9 billion in revenue.

LOCKBIT

LockBit is one of the most prominent ransomware groups in all sectors.
LockBit utilizes high payments for recruiting experienced malicious actors,
purchasing new exploits, and even running a bug bounty program that offers
high payouts.

LockBit 3.0’s victims typically had less annual revenue on average ($346
million) compared to those targeted by Clop. Organizations with less revenue
could have less dedicated resources to their security programs, indicating
the group has an easier time infiltrating these organizations. LockBit’s victims
are geographically more distributed when compared to Clop with 29.7%
within North America, 24.3% in Europe, and 10.8% in Asia and South America.

ALPHV/BLACKCAT

According to the FBI, ALPHV was the first group to successfully leverage
improved performance processing using the RUST programming language to
ransom a victim. ALPHV develops capabilities and functionality that are quickly
adopted by other threat actors. This activity likely indicates that its members
are ransomware veterans and capable of creating cutting-edge malware.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies43

For example, the group developed a search function in July 2022 for indexed
stolen data that security analysts had not seen previously. The group claimed
this was done to aid other cybercriminals to find confidential information,
which could be used to add pressure on victim organizations, forcing them to
pay the ransom. Recently, the group has released a new ransomware control
panel, named Sphynx, in February 2023

ALPHV victims had even less revenue than LockBit 3.0’s victims, averaging
$120.3 million. The group also indicated it likes to target smaller entities
in space.

A microfinance company that was targeted by AlphV

BLACK BASTA

Black Basta began operations in mid-April 2022, using a Ransomware-as-a-
service (RaaS) model. The group leverages Network Access Brokers (NABs)
to gain initial access. The group does not publicly recruit affiliates, as the
group privately collaborates with actors it has previously worked with.

The range of victim revenue was from $9 million to $2.1 billion. All breaches in
the past year were against financial institutions in either the U.S. or Canada.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies90% REDUCTION IN
ALERT NOISE THROUGH
TRUSTWAVE
CO-MANAGED‧SOC

44

8BASE

The 8BASE ransomware group began operations in April 2022, utilizing a
ransomware-as-a-service (RaaS) model. The group claims to utilize a private
ransomware strain named 8BASE aka RADAR 8BASE, which encrypts data
on network-attached storage (NAS), VMware ESXi hypervisors, and Unix and
Windows operating systems.

The group typically targets small to medium-sized entities, generating less
than $25 million in revenue, while maintaining an opportunistic approach.  All
breaches in the past year were against financial institutions in either the U.S.
or Canada.

Mitigations to Reduce Risk

 ▪ Use host-based anti-malware tools that can assist in identifying and
quarantining specific malware, but understand they have limitations
and are often circumvented by custom malware packages.

 ▪ If prevention of infection is not possible, audit controls become

crucial indicators of potential compromise. This involves enabling
system logs on valuable systems and workstations, as well as
implementing network logging through flows, Network Monitoring
Solutions, or IDS devices on ingress and egress channels.

 ▪ Implement active monitoring. Merely enabling logs is insufficient;
if logs are not monitored, they lose their effectiveness. Regular
monitoring helps establish a baseline of regular activity, making
abnormal behavior or traffic more conspicuous.

 ▪ Establish and regularly practice a formal Incident Response process.

 ▪ Perform ongoing Underground and Dark Web monitoring for

information leakage that may have been missed.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies45

Exfiltration / Post Compromise

The Threat
Once attackers have established themselves within a network and systems,
they will proceed to execute their final plan. This plan can take various forms
depending on their objectives.

In some cases, attackers may adopt a "smash and grab" strategy, aiming to
swiftly gather as much information as possible before making a hasty exit.
They will often make efforts to cover their tracks during this process.

On the other hand, certain attackers may have specific targets in mind, such
as a particular system, individual, or dataset. In these instances, they will
proceed cautiously and meticulously through the network, employing tactics
to avoid detection until they achieve their goal.

Server

Other attackers simply aim to cause widespread destruction, prioritizing
chaos over theft. They may employ ransomware to render valuable data
unusable or resort to deleting and corrupting data as well as backups.

Trustwave SpiderLabs Insights

Exfiltration /
Post Compromise

Malware

From a historical perspective, we can see that the primary motivating factor
for financial services organizations is data theft with ransom as a significant
adjacent motivational goal.

Just in the previous quarter, we have already seen notable banks such
as Latitude Financial, 1st Source Corp, Pacific Premier Bancorp, M&T
Bank, MidFirst Bank, European Investment Bank hit with various types of
cyberattacks exposing millions of customer records in the process.

Based on Trustwave SpiderLabs incident data, we see an overwhelming
tendency towards data encryption related to unspecified ransomware
activity. Even activities pertaining to inhibition by deletion of shadow volumes
and data backups are also related to the ransomware aspect of the attacks.

91%

8%

1%

0%

20%

40%

60%

80%

100%

T1486 Data Encrypted for Impact

T1490 Inhibit System Recovery

T1498 Network Denial of Service

Impact techniques observed

The Dark Web sites of the various ransomware gangs are full of
announcements and data leaks of their victims in all industries. Here is one
example from a ransomware website posting a leak for a financial services
organization:

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial PayloadMalware46

100%

OF TRUSTWAVE'S
ADVANCED CONTINUAL
THREAT HUNTS RESULT
IN THREAT FINDINGS

Clop Dark Web leaks website and subsequent torrent leak after bank decided not to
pay ransom

The example above in the Clop Dark Web leaks site is a classic case of
double extortion. The increasing sophistication of ransomware attacks
and the monetary incentive this presents to threat actors will make it more
difficult for financial services providers to defend against such attacks.

Mitigations to Reduce Risk

 ▪ Monitor the Dark Web on a regular basis for potential

compromises.

 ▪ Conduct regular penetration tests to proactively identify

vulnerabilities and weaknesses in your systems, networks, and
applications.

 ▪ Decrease the time to remediation to have a significant impact in

exposure and reduce the window of exploitation.

 ▪ Run continuous Threat Hunting, like Trustwave’s Advanced

Continual Threat Hunt through your environments for undetected
compromises.

 ▪ Formalize and regularly test your Incident Response Policy for the

scenarios that will most likely impact you.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesKey Takeaways and
Recommendations

48

The financial services industry is often considered one of,

if not the highest, value organizations targeted by threat actors.

Although the financial services sector isn’t alone in facing an

elevated threat landscape, the consequences of attacks in this

sector can be quite severe.

To put this into context, financial services organizations store and process a large amount of
sensitive data (e.g., credit card and bank information,) which, by its very nature, can be easily
monetized. Attackers are highly motivated by financial gains and continually adapt their methods
to outpace defenses.

Additionally, the broad scope of financial services also means it is not limited to financial data but
various levels of personal information, including sensitive health information, such as those from
insurance organizations.

Financial services organizations are also highly interconnected. This interconnection ranges from
inter-bank connections, connections to the central banks and regulatory agencies, heavy use of
third-party vendors and support providers, and the use of third-party code, web services, and
APIs, among others. This interconnectedness leads to an exponential increase in attack surface
and threat vectors.

As demonstrated in our attack cycle, attackers often employ multiple vectors to target these
organizations persistently. While the technical aspects of these attacks may change over time,
the underlying methods tend to remain consistent. Traditional methods such as phishing, email-
borne malware, exploiting known and zero-day vulnerabilities, and compromising third-party
vendors continue to pose significant threats. The continuing success of these proven methods
have led to the steady increase of successful cyberattacks, particularly ransomware.

With that said, traditional methods don't mean using the same old techniques. The methods may
be old (e.g., phishing) but threat actors have continued to refine and update their techniques
to stay ahead in the cybersecurity arms race. This report highlights novel types of phishing
techniques, new exploits, new malware, and even new technologies such as the emergence of
generative AI and LLMs for social engineering attacks. With this in mind, it is highly unlikely that
attacks targeting financial services organizations will subside or slow down in the future.

As a result, preventative measures remain the most effective defense against all types of
cyberattacks. As shared earlier in the previous sections of the attack cycle, the following chart
serves as a comprehensive reference for actionable mitigations that can effectively thwart
attackers and prevent lasting damage.

.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies49

Initial Foothold

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Consistently conduct mock phishing tests and retrain repeat offenders.
 ❏ Utilize techniques to detect domain misspellings, enabling the identification of phishing

and BEC attacks.

 ❏ Regularly rotate passwords, implement password complexity requirements, enable

multi-factor authentication (MFA), and securely store or encrypt credentials

 ❏ Implement vulnerability assessments and penetration testing to identify and address
vulnerabilities, along with promptly patching critical systems and keeping all software
up to date.

Initial Payload & Expansion / Pivoting

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Regularly audit all applications to prevent vulnerabilities from custom applications.
 ❏ Implement a detailed whitelist of applications on designated hosts to minimize

exposure and prevent malicious actors from introducing disguised harmful applications.

 ❏ Impose additional restrictions on privileges to prevent unauthorized execution of

different shells from unprivileged sources.

Malware

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Use host-based anti-malware tools that can assist in identifying and quarantining

specific malware.

 ❏ If prevention of infection is not possible, Audit controls become crucial indicators
of potential compromise. This involves enabling system logs on valuable systems
and workstations, as well as implementing network logging through flows, Network
Monitoring Solutions, or IDS devices on ingress and egress channels.

 ❏ Implement active monitoring. Merely enabling logs is insufficient; if logs are not

monitored, they lose their effectiveness. Regular monitoring helps establish a baseline
of regular activity, making abnormal behavior or traffic more conspicuous.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies50

Exfiltration / Post Compromise

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Monitor the Dark Web on a regular basis for potential compromises.
 ❏ Run continuous Threat Hunting through your environments for undetected

compromises.

 ❏ Formalize and regularly test your Incident Response Policy for the scenarios that will

most likely impact you.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesAppendix/Reference

52

Threat Groups

8BASE
 ▪ 8BASE is a ransomware group that began operations in April 2022 utilizing
a Ransomware-as-a-Service (RaaS) model. They claim to utilize a private
ransomware strain named 8BASE aka RADAR 8BASE, which encrypts data
on Network-attached storage (NAS), VMware ESXi hypervisors, and both
Unix and Windows operating systems.

 ▪ The ransomware resembles a customized version of the Babuk and

Phobos ransomware variants, indicating some level of cross-over between
groups. Based on this, and the group’s recent surge in activity, it is
believed that 8BASE group members are an offshoot of other ransomware
groups. The group typically targets small to medium sized entities, while
maintaining an opportunistic approach.

BlackCat/ALPHV
 ▪ BlackCat/ALPHV first appeared in late 2021. This ransomware group was

the fourth most active in the second quarter of 2022 and third most active
in the third quarter 2022. Intel471 reported the group was responsible
for about 6.5% of the total reported ransomware cases during this
period. While the amount is smaller compared to LockBit or Black Basta,
newcomer BlackCat has managed to stand out from the crowd. The group
developed a search function in July 2022 for indexed stolen data that had
not been seen previously. The group claimed this was done to aid other
cybercriminals in finding confidential information which can be used to
add pressure to victim organizations forcing them to pay the ransom. This
idea was quickly copied with LockBit adding its own, lighter version to its
toolset.

 ▪ ALPHV has also set other trends. According to the FBI, ALPHV was the

first group to successfully utilize Rust to ransom a victim, well before Hive
made the switch. ALPHV’s ability to develop capabilities and functionality
that are quickly adopted by other threat actors most likely indicates that
its members are most likely ransomware veterans and there are indications
the group was linked to the infamous Darkside and BlackMatter gangs.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies53

Black Basta
 ▪ One of the newest ransomware groups is Black Basta. The group has had
alleged ties to other gangs, such as Conti, REvil, and Fin7 (aka Carbanak).
These ties come in the form of possible former members/affiliates, in the
case of Conti, or custom tools, which are potentially linked to Fin7. With
potentially experienced members, the group was able to publish more
than 20 organizations to its name-and-shame blog within the first two
weeks of the group being identified in April 2022, according to Intel471.
Since the initial identification of the group, they have compromised over 90
organizations as of September 2022 with no sign of slowing down.

 ▪ The group has had unprecedented success for the short period that

they have been active. This success can be linked to a couple of factors.
First, Black Basta does not publicly recruit affiliates and most likely
only collaborates with actors with whom it has worked previously. This
collaborative methodology is possible because it has been assessed
that the Black Basta was formed from members of other successful
ransomware groups, so they know other actors. Additionally, the group
outsources its capabilities utilizing established tools, such as QakBot and
Cobalt Strike, or network access brokers, allowing the group to have a high
success rate once inside a victim's environment.

Clop
 ▪ Clop is a ransomware family that was first observed in February 2019

and has been used against retail, transportation and logistics, education,
manufacturing, engineering, automotive, energy, financial, aerospace,
telecommunications, professional and legal services, healthcare, and high-
tech industries. Clop is a variant of the CryptoMix ransomware.

 ▪ In addition to exploiting a previously undisclosed vulnerability (CVE-2023-

34362) in MOVEit Transfer, group has a history of conducting similar
campaigns using zero-day exploits, targeting Accellion File Transfer
Appliance (FTA) devices in 2020 and 2021, as well as Fortra/Linoma
GoAnywhere MFT servers in early 2023.

Medusa
 ▪ MedusaLocker is a ransomware strain that emerged in 2019 and has
since spawned various versions, though core functionalities remain
unchanged. Alterations include modified file extensions for encrypted data
and variations in the appearance of the ransom note. Ransom payments
from victims are typically divided between the affiliate (55-60%) and the
developer.

 ▪ This ransomware often infiltrates victim systems via vulnerable Remote
Desktop Protocol (RDP) setups, alongside employing email phishing and
direct attachment of the ransomware to emails in spam campaigns for
initial access.

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies54

LockBit
 ▪ LockBit has continued its reign as the most prominent ransomware group

in 2022. For those that don't closely follow these groups, LockBit is
and continues to be, the group that dominates the ransomware space.
They utilize high payments for recruiting experienced malicious actors,
purchasing new exploits, and even run a bug bounty program that offers
high-paying bounties - a first for a ransomware group[1]to identity of one
of its users. With all these programs and the continued effectiveness of
the group, it is forecasted that it will remain the most active and effective
group for the foreseeable future.

 ▪ As for developments, the group has developed LockBit 3.0, the newest
iteration of ransomware. The updated version, released in June 2022,
and includes additional features that can automate permission elevation,
disable Windows Defender, a "safe mode" to bypass installed Antivirus,
and the ability to encrypt Windows systems with two different ransomware
strains to decrease the chance of decryption from a third party. With these
new features, the group has been able to conduct successful attacks,
accounting for roughly 44% of successful ransomware attacks so far in
2022 according to Infosecurity Magazine.

 ▪ On a law enforcement note, a member of the LockBit group was recently
arrested in Canada and is awaiting extradition to the United States. A
dual Russian and Canadian national has allegedly participated within the
LockBit campaign and has been charged with conspiracy to intentionally
damage protected computers and to transmit ransom demands. The
charges carry a maximum of five years in prison.

Play
 ▪ Unveiled in June 2022, Play ransomware concentrates its attacks primarily

on Latin American nations, with Argentina and Brazil as key targets.
Drawing inspiration from Russian counterparts Hive and Nokoyawa, Play
employs akin encryption methods.

 ▪ Leveraging reused or leaked credentials, Play breaches networks and
systems, relying on tools like Cobalt Strike, SystemBC, Empire, and
Mimikatz for lateral movement. Its unique employment of AdFind sets it
apart from Hive and Nokoyawa, emphasizing a potential affiliation through
shared tactics and tools.

Royal
 ▪ Royal is ransomware that first appeared in early 2022; a version that also
targets ESXi servers was later observed in February 2023. Royal employs
partial encryption and multiple threads to evade detection and speed
encryption. Royal has been used in attacks against multiple industries
worldwide--including critical infrastructure.

 ▪ Royal operates as a private group, distinguishing themselves from other

cybercrime operations by purchasing direct access to corporate networks
from underground Initial Access Brokers (IABs). Security researchers have
identified similarities in the encryption routines and TTPs used in Royal and
Conti attacks and noted a possible connection between their operators
(the group suspected of being primarily composed of former members of
the Conti ransomware group operates discreetly and in a secretive manner.
This group, referred to as Team One, consists of ex-members who have
come together to form this new entity).

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies