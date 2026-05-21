# 2023 Hospitality Sector Threat Landscape

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Generative AI and Large Language Models (LLMs)](#generative-ai-and-large-language-models-llms)
- [Contactless Technology](#contactless-technology)
- [Third-party Risk and Exposure](#third-party-risk-and-exposure)
- [Dissecting the Attack Flow for Hospitality](#dissecting-the-attack-flow-for-hospitality)
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

## Executive Summary

![Infographic showing 31% of hospitality organizations have reported a data breach, with 89% affected more than once in a year, and an average cost of $3.4 million per breach.]

The global hospitality industry employs nearly 300 million individuals worldwide, and provides a place to stay, eat, and relax for billions of people all over the world. Spanning from hotels to restaurants to cruise ships, the industry has become deeply woven into our everyday routines, making its cybersecurity threat landscape especially vast, complex, and critical.

Nearly 31% of hospitality organizations have reported a data breach in their company’s history, of which 89% have been affected more than once in a year, according to a report by Cornell University and FreedomPay. These cyberattacks have resulted in the loss of sensitive data, financial losses, and reputational damage. While the average cost of a hospitality breach ($3.4M) is lower than the cross-industry average ($4.4M), the impact on reputation can cause significant harm to the bottom line due to the highly competitive nature of the industry.

A surge towards digital technologies prompted by the pandemic, along with the overall resurgence of the hospitality industry, has rendered hospitality companies well-acquainted with cyberattacks.

In February 2022, the global hotel and resort company Marriott was targeted through social engineering, and the attackers made out with 20 gigabytes of sensitive customer data, including personal information and credit card numbers. In September 2022, InterContinental Hotels Group (IHG) was hit by a cyberattack that downed its booking systems and mobile apps.

With over 250 security researchers across the globe, the Trustwave SpiderLabs team puts its resources to task in looking into what leads to these breaches. We are uniquely positioned to do so, as we perform over 100,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 4,000-8,000 a day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Continuous Threat Hunting, Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur as well as mitigations and controls that your organization can put in place to prevent these compromises.

There are a few factors that make the hospitality industry’s cybersecurity threat profile especially unique, including:

- **Seasonal and Less Sophisticated Workforce**: The hospitality sector employs a diverse workforce, with seasonal and less sophisticated staff often engaged during peak periods to meet demand. This presents a distinct risk of insider threat, intentional or not, due to the challenge of providing consistent security training to a continually changing group of employees.
- **Constant User Turnover**: Hospitality establishments encounter a fresh set of users virtually every day. This ongoing cycle demands consistent uptime, addresses bandwidth constraints, and strives to minimize potential exposure to security threats.
- **Dirty Networks**: Given the substantial volume of network users, whether they’re hotel guests or individuals connecting to coffee shop Wi-Fi, organizations within hospitality must operate under the assumption that their networks are highly susceptible to attacks due to the sheer number of users. There are hesitancies to deploy patches and configuration changes that might have an adverse impact on day-to-day operations.
- **Physical Security Concerns**: Unlike conventional office buildings where employee access is typically controlled through access cards, hospitality establishments face cybersecurity risks due to the accessibility of hardware by guests. For instance, the server closet in a hotel could be left unlocked and easily accessible or a thumb drive could easily be inserted into a nearby device.
- **Franchise Model**: The franchise framework leads to disparities in policy consistency and implementation across the industry, including cybersecurity measures. Different franchisers and franchisees adopt varied business models, resulting in divergent cybersecurity practices.

Given these circumstances, it is crucial for the hospitality sector to minimize its risk and prioritize information protection. This report’s objective is to thoroughly examine the multitude of threats that pose challenges to the hospitality industry.

We will begin by highlighting the significant trends currently affecting the industry, including contactless technology, generative AI, and third-party risk. Subsequently, we will analyze the attack flow specific to the hospitality sector, offering insight on specific threat actors, actionable intelligence, and recommended mitigations for each stage to illustrate how organizations can proactively identify and prevent attacks to avoid lasting impact.

---

## Emerging and Prominent Trends

### Generative AI and Large Language Models (LLMs)

**The Threat**
Generative AI and Large Language Models (LLMs) continue to take the world by storm. Generative AI is a powerful tool that is being increasingly used by the hospitality sector to improve the guest experience with services like chatbots or language translation. Following the Covid-19 pandemic, many hospitality entities began leveraging chatbots to interact with guests and provide 24/7 customer support.

However, similar to other industries, using this technology also raises concerns about data privacy and security. Hospitality businesses need to carefully consider the risks and benefits of using generative AI before deploying it.

**How This Could Affect You**
Generative AI systems can be used to collect and store large amounts of data about guests, including personal information, travel preferences, identification documents, and payment details. This can either be through employees inputting the information, or by the guests themselves through use of a chatbot. If exposed or accessed, this data could be used by cybercriminals to commit identity theft, fraud, or other crimes.

The hospitality industry is in the business of knowing its guests and their preferences. As a result, tailored and personalized marketing is a core component to stay competitive. As more business intelligence and customer analytics platforms integrate generative AI into their tools, the hospitality sector must vet and audit the security protections within those systems.

Additionally, social engineering attacks can become more sophisticated as LLMs have the capability to create highly personalized and targeted messages.

**Mitigations to Reduce Risk**
- Evaluate your security solutions with generative AI and LLMs in mind. Choose security tools or partners that can detect AI-generated threats like advanced phishing.
- Create robust internal policies, controls, and employee training for proper data usage and data sharing to help minimize the risk of data breaches.
- Consider instituting an internal AI Infosec working group across relevant teams (like Legal, Privacy, IT, Marketing, et al.) to deal with governance and data sharing guidelines.
- Carefully vet your supply chain and inspect their policies and controls around use of your corporate or customer data in their generative AI and LLM applications.
- Monitor generative AI systems for suspicious activity and keep them up to date.

---

## Dissecting the Attack Flow for Hospitality

### Attack Flow Overview
While the specifics and details of every breach and compromise may vary, there is typically a specific attack flow that occurs from the initial security bypass to escalation, compromise, followed by persistent home on your network and exfiltration and/or destruction of valuable data.

The typical sequence of events unfolds as follows:
1. Initial Foothold
2. Initial Payload
3. Expansion / Pivoting
4. Malware
5. Exfiltration / Post Compromise

### Initial Foothold: Phishing and Business Email Compromise (BEC)
Phishing stands out as the most commonly exploited method for gaining an initial foothold in an organization. Instead of attempting to exploit the software or systems on the network, attackers direct their focus towards targeting the individuals operating the keyboard.

**Trustwave SpiderLabs Insights**
Over the last year, the team has flagged Emotet and Qakbot as the most common email-borne malware in hospitality. HTML is the top file attachment being leveraged and is used in phishing as a redirector to facilitate credential theft and for delivering malware through HTML Smuggling.

**Mitigations to Reduce Risk**
- Regularly perform simulated phishing assessments to evaluate the efficiency of anti-phishing training and provide retraining for individuals who repeatedly fall victim.
- Enforce strong anti-spoofing protocols, involving the deployment of cutting-edge technologies within email gateways.
- Employ a multi-tiered approach to email scanning, utilizing a solution such as Trustwave MailMarshal to enhance the accuracy and efficacy of both detection and protective measures.

---

## Appendix/Reference

### Threat Groups
- **ALPHV/BlackCat**: A prominent ransomware-as-a-service group.
- **BianLian**: Known for double-extortion tactics.
- **Black Basta**: A prolific ransomware group targeting various sectors.
- **Clop**: Responsible for large-scale data exfiltration attacks, including the MOVEit campaign.
- **LockBit**: One of the most active ransomware operations globally.
- **Royal**: A threat group known for sophisticated targeting and extortion.

*(Note: The full report contains detailed analysis for all listed groups in the original document.)*

---

actors to maintain access by creating new user accounts or modifying
existing ones to ensure that attackers can gain recurring entry after initial
compromise. These include creating backdoor accounts, fake service
accounts, and “ghost accounts” among others.

ACCOUNT MANIPULATION

Account Manipulation, as a persistence mechanism, is a technique used
by threat actors that leverages vulnerabilities or weaknesses in user
accounts, credentials, and permissions to maintain continued access.
Techniques in this area include, but are not limited to, exploiting privilege
escalation vulnerabilities, password hash manipulation, pass the hash, and
kerberoasting among others.

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

Trustwave SpiderLabs
conducts 100K hours of
pentesting each year

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesMalware

Server

Malware

32

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

In-transit infostealers, on the other hand, are focused on stealing data that
users enter but is not stored as a file on the system. These Infostealers
usually manifest as malicious web browser plug-ins that act as proxy servers
for specific connections. For example, they may monitor connections to
your bank's website and manipulate the connection to steal your account
information or perform unauthorized actions, such as initiating a wire transfer,
by utilizing your access.

Trustwave SpiderLabs Insights
Trustwave SpiderLabs gains insights into potential infostealers in our clients’
environments obtained through delivery of our managed services, threat
hunts, DFIR, and malware analysis teams across clients worldwide.

The following are the infostealers that our team has observed operating in
the hospitality sector:

FORMBOOK

FormBook is an infostealer that has been operational since mid-2016. Its
primary function is to harvest sensitive information from compromised
systems, with a particular emphasis on extracting data tied to online forms,
passwords, and assorted credentials. Believed to originate in South Korea,
FormBook has been associated with multiple cybercriminal campaigns.

FormBook comprises a range of functionalities including keylogging,
screenshot capture, clipboard data recording, and the pilfering of data
from web-based forms. It is versatile and can target a diverse array of
applications, web browsers, and online services in order to pilfer sensitive
data. As time has progressed, FormBook has advanced its capabilities to
encompass attributes like obfuscation tactics, anti-analysis measures, and
the encryption of stolen data prior to its transmission.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExfiltration /Post CompromiseHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial Payload33

Our team has seen Formbook payloads and activity associated with Qakbot
email campaigns targeting our hospitality client base. Here is an example
from our data of a malicious emails spam that we have observed purporting
to be from Agoda.com that contains Formbook malware:

Email Spam, Purporting to be From Agoda.com, Contains Formbook Malware

VIDAR

Vidar is an infostealer that surfaced around 2018 that specializes in
harvesting sensitive data from compromised systems. It is distributed
through phishing emails, targeting personal and financial information like
login credentials and payment card details. It is equipped with keylogging
and, form grabbing capabilities and can intercept keystrokes and data
entered in online forms. The stolen data is then exfiltrated to remote
servers controlled by attackers. Vidar employs anti-analysis techniques
and features modular architecture for adapting its capabilities to different
attack scenarios.

LOKI BOT

Loki Bot is an infostealer that has been active for several years. It specializes
in infiltrating systems and harvesting sensitive data. Primarily targeting
credentials and valuable information across diverse online services, Loki Bot
is disseminated through phishing campaigns and exploit kits. Its modular
architecture enables attackers to customize functionalities while features
such as keylogging and web injection facilitate the theft of usernames,
passwords, and other data.

RACCOON STEALER

Initially marketed under the Malware-as-a-Service (MaaS) model, Raccoon
Stealer’s operations came to a halt when the primary developer was
apprehended in March 2022. Nonetheless, it didn't take much time for new
actors to rebuild Raccoon from scratch and reintroduce it in June of the
same year. This new version was built using C/C++ and introduces new
functionalities across its infrastructure, including new types of pilferable
data. Raccoon Stealer can extract browser credentials, stored credit card
information, cryptocurrency wallets, email content, and various other forms
of sensitive data from a wide array of applications.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies34

REDLINE STEALER

Redline is a .Net compiled executable capable of examining and collecting
diverse system information like the operating system version, active
processes, and installed software of an infected system. It has the capability
to gather credentials from web browsers, target cryptocurrency wallets,
and acquire login details from various applications, including NordVPN and
FileZilla.

Trustwave SpiderLabs published an analysis of Redline Stealer in conjunction
with an analysis of the Lapsu$ hacker group in 2022.

Mitigations to Reduce Risk

 ▪ Utilize host-based anti-malware tools to assist in identifying and
quarantining specific malware but understand that they do have
their limitations and are susceptible to evasion by custom malware
packages.

 ▪ If preventing infection isn't possible, prioritize audit controls. This

involves activating system logs on critical and valuable systems and
workstations, and implementing network logging through flows,
Network Monitoring Solutions, or IDS devices on ingress and egress
channels.

 ▪ Implement active monitoring, as merely enabling logs is insufficient;

logs lose effectiveness without vigilant observation. Regular
monitoring establishes a baseline of normal activity, making
anomalies or unusual traffic more conspicuous.

 ▪ Establish and routinely practice a formal Incident Response process.

 ▪ Perform continuous monitoring of Underground and Dark Web

sources to detect any information leakage that might have been
overlooked.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies35

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
The following are the Remote Access Trojans (RAT) that Trustwave
SpiderLabs team has observed operating in the hospitality sector:

HOUDINI RAT

Malware

Houdini RAT is a VBScript based malicious software that has been around
since 2013. It provides unauthorized access and control over compromised
systems, enabling threat actors to manage machines remotely, pilfer sensitive
data, and execute various malicious actions. This malware is distributed
through various phishing campaigns. Among the RAT functionalities are:

 ▪ Execution of VBScript statement

 ▪ Update the script itself

 ▪ Download files

 ▪ Upload files

 ▪ CMD shell

 ▪ Enumerate process and directory/files

It is also notable to understand that the worm spreads through removable
drives. Below is an actual sample of the Houdini RAT from an attack our team
has observed targeting a hotel in November 2022.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExfiltration /Post CompromiseHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial Payload36

Houdini VBSCript RAT

REMCOS

Remcos is a commercial RAT first seen in 2016. It has robust out-of-the-
box features which appeal to threat actors. Malware campaigns distributing
Remcos have attachments in the form of '.z' archives typically masquerade
as financial documents. Threat actors included decoy PDFs to make it look
credible and used compromised email accounts to target organizations.
Below is an example of an email spam containing the Remcos RAT that our
team observed during a Qakbot email campaign targeting hospitality clients.
Note the decoy PDF that attempts to make it look credible and note the use
of compromised email accounts.

Email Spam Containing Remcos RAT Which is Disguised as an Invoice and a Decoy PDF

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies37

AGENT TESLA

Agent Tesla is a RAT discovered in 2014 and is written in .Net. This threat
can take full control of a compromised system and can exfiltrate data via
HTTP, SMTP, FTP, and Telegram. It is commonly deployed via phishing emails
with archive or disc image attachments. We have observed Agent Tesla as
one of the binaries often associated with Qakbot campaigns (together with
Formbook and Remcos). It includes a keystroke logger, the ability to access
anything on the clipboard, and can search the hard drive for any other
valuable data. It also has a very flexible command and control channel.

Trustwave SpiderLabs published an analysis of Agent Tesla in conjunction
with how it is often attached to phishing campaigns.

ASYNC RAT

AsyncRAT is another common RAT. This malware emerged around 2016 and
has gained traction due to it having a user-friendly interface and being open
source. The RAT is typically deployed via phishing emails and uses a chain
of .BAT, .PS1, and .VBS files to evade detection. It has a lot of common
options like:

 ▪ View and record the victim's screen

 ▪ Log all keystrokes

 ▪ Chat mechanism with the victim

 ▪ Disable Windows Defender

 ▪ Access to upload, download, and delete files

Below illustrates a multiple stage attack we observed targeting a hospitality
client that started with an email and ended the final payload of AsyncRAT

Malicious
email

User clicks
a link that
redirects to Mediafire
file hosting site

a ZIP file is
downloaded

ZIP contains a
decoy PDF file &
a malicious batch file.

User clicks
the batch file
and connects
to the attacker's host

Malicious HTA file
is downloaded
that install the
end payload

AsyncRAT - remote access trojan
is installed in the victim's computer

Stages of the Attack Ending with AsyncRAT

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesTRUSTWAVE MDR ELITE
OFFERS AN MTTA OF 15
MINUTES AND MTTR OF
>30‧MINUTES

38

Mitigations to Reduce Risk

 ▪ Utilize host-based anti-malware tools to assist in identifying and
quarantining specific malware but understand that they do have
their limitations and are susceptible to evasion by custom malware
packages.

 ▪ If preventing infection isn't possible, prioritize audit controls. This

involves activating system logs on critical and valuable systems and
workstations, and implementing network logging through flows,
Network Monitoring Solutions, or IDS devices on ingress and egress
channels.

 ▪ Implement active monitoring, as merely enabling logs is insufficient;

logs lose effectiveness without vigilant observation. Regular
monitoring establishes a baseline of normal activity, making
anomalies or unusual traffic more conspicuous.

 ▪ Establish and routinely practice a formal Incident Response process.

 ▪ Perform continuous monitoring of Underground and Dark Web

sources to detect any information leakage that might have been
overlooked.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies39

Malware: Ransomware

The Threat
Ransomware is a type of malware that typically encrypts or locks data and
then demands the victim pay a ransom to regain access to that data. Modern
ransomware campaigns prevent recovery by attempting to remove access to
backup files and deleting Volume Shadow Copies.

More recently, ransomware groups have added an extortion component
to these attacks. They will exfiltrate valuable data prior to deploying the
ransomware and then publicly post proof of the attack to scare/shame the
victim organization into paying the ransom. If the ransom isn’t paid, the threat
actors still have a dataset they can turn around and sell. This is commonly
referred to as a double extortion tactic.

Trustwave SpiderLabs Insights
A significant part of stealing data from the hospitality sector involves
ransomware gangs. These groups are primarily motivated by financial gain.

Malware

Server

Based on our research across the Dark Web, we analyzed the ransomware
incidents directly targeting the hospitality business from the beginning
of 2022 to July 2023. The most active gang in the hospitality business is
LockBit which is responsible for around a third of the attacks.

Malware

Bla
c
k
S
h
a
d
o
w

Hive

Play

Lv

2
%

2
%
3%

3%

3%
3%

3%

3%

5%

Conti

Alphv

Ragnar

Karakurt

Royal

5%

Qilin

%
5

BlackBasta

%
8

n
a
i
L
n
a
i
B

Bit
k
c
Lo

%
7
2

5%

Revil

10%

Medusa

1
0
%

Vic
e S
o
ciety

Hospitality Ransomware Victims Distribution

LockBit is a well-known ransomware variant introduced in 2019 and operates
within the ransomware-as-a-service framework. The malware stands out
for its swift and automated data encryption methods and rapid impact. It
employs a "double extortion" strategy, LockBit not only encrypts data but
also exfiltrates sensitive content, leveraging its potential public exposure to
pressure for ransom payment. Below is a screenshot from the LockBit blog
which presents the status of all their victims and a countdown to when the
“hostage” data will be released publicly.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdExfiltration /Post CompromiseHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial Payload40

LockBit Blog Illustrates the Status of the Victims and Mentions Already Published Data

On the hospitality front, threat actors attack targets worldwide. We have
observed that more than 30% of the attacks were focused on establishments
in the United States, with Germany and the United Kingdom following at
10% each. This list may indicate ransomware gangs target victims in affluent
countries. Here is the geographical spread of the attacks:

Geographical Spread of Hospitality Victims According to Ransomware Gang Blogs

Aside from Lockbit, other ransomware variants that the Trustwave
SpiderLabs team has observed regularly in our engagements are Clop and
BlackCat. Through the metadata analysis of cases within the hospitality
sector, our team has observed a significant and currently ongoing surge
in Clop ransomware attacks, which are related to the MOVEit zero-day
vulnerability. Meanwhile, BlackCat (aka AlphaV), though not as prevalent as
Lockbit and Clop, has impacted the food and beverage sector particularly
through attacks on POS systems.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies90% REDUCTION IN
ALERT NOISE THROUGH
TRUSTWAVE
CO-MANAGED‧SOC

41

Mitigations to Reduce Risk

 ▪ Utilize host-based anti-malware tools to assist in identifying and
quarantining specific malware but understand that they do have
their limitations and are susceptible to evasion by custom malware
packages.

 ▪ If preventing infection isn't possible, prioritize audit controls. This

involves activating system logs on critical and valuable systems and
workstations, and implementing network logging through flows,
Network Monitoring Solutions, or IDS devices on ingress and egress
channels.

 ▪ Implement active monitoring, as merely enabling logs is insufficient;

logs lose effectiveness without vigilant observation. Regular
monitoring establishes a baseline of normal activity, making
anomalies or unusual traffic more conspicuous.

 ▪ Establish and routinely practice a formal Incident Response process.

 ▪ Perform continuous monitoring of Underground and Dark Web

sources to detect any information leakage that might have been
overlooked.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies42

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

Exfiltration /
Post Compromise

Malware

Trustwave SpiderLabs Insights

The primary motivating factor for threat actors attacking hospitality
organizations is data theft. From a historical perspective, the trend appears
to show that from 2015 to 2017, attacks were mostly PoS-related focusing on
payment data. Incidents from 2018 onwards appear to show a growing shift
towards PII, though payment data is still a big part of the motivation.

Based on Trustwave SpiderLabs incident data, we are seeing the following
impact from these attacks:

 ▪ Data encryption related to unspecified ransomware activity

 ▪ System recovery inhibition by deletion of shadow volumes and data

backups

 ▪ Resource hijacking by Crypto Mining software

 ▪ Network Denial of Service attempts

While we can individually track the number of records affected by a data
breach, it’s difficult to truly know how much of that data actually ends
up exposed either publicly or to a private buyer. Trustwave SpiderLabs
continuously monitors a variety of Dark Web forums, open web forums,
Twitter accounts, Telegram channels, and more for hospitality-related data.

Here is an example of an advertisement from the LockBit group of publicly
published data from a hospitality organization:

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesInitial FootholdHTML AttachmentCommand LineMalwareExpansion/ PivotingInitial PayloadMalware43

LockBit Blog, Exposing a Hotel’s Stolen Data

It is common practice for attackers to publicly expose information if the
intended victim did not follow the attacker's demands. The spreading of such
data ends with allowing other threat actors to extract all the significant and
valuable data and share it among others or put it to work. Additionally, script-
kiddies and beginners will try to raise their position and reputation by using
such information and sharing it in other forums and telegram channels.

Additionally, it should be noted that attacks directed at stealing data
may also lead to adjacent impact such as severe system disruptions in
hospitality organizations. For example, we have observed instances wherein
a ransomware attack has affected critical hotel systems such as the cash
and reservations system and even the central key management system (lock
and access key) thus disrupting operations and even potentially affecting the
safety and security of hotel guests.

100%

OF TRUSTWAVE'S
ADVANCED CONTINUAL
THREAT HUNTS RESULT
IN THREAT FINDINGS

Mitigations to Reduce Risk

 ▪ Consistently monitor the Dark Web to detect possible

compromises. Partners like Trustwave can assist with this.

 ▪ Conduct regular penetration tests to proactively uncover

vulnerabilities in your systems, networks, and applications.

 ▪ Minimize the time needed for remediation to substantially reduce

exposure and narrow the window for potential exploitation.

 ▪ Continuously engage in threat hunting activities, such as

Trustwave's Advanced Continual Threat Hunt, to uncover any
hidden compromises in your environments.

 ▪ Establish and routinely assess your incident response policy,

focusing on scenarios that are most likely to affect your
organization.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesKey Takeaways and
Recommendations

45

Although the hospitality industry isn’t alone in facing an elevated

threat landscape, the consequences of attacks in this sector can be

critical. One key aspect to note is the nature and scale of the hospitality

industry creates an environment that is inherently conducive and

appealing to threat actors.

First, is the data. The quantity, as well as the quality of data, makes the hospitality industry a
prime target for threat actors. Not only does it hold a large amount of payment information, but it
also contains even more PII that can be monetized quite easily nowadays. As a result, some of the
biggest breaches to-date have happened in the hospitality industry, with their CEOs being called
to testify in Senate hearings.

Second, is the exposure. The hospitality industry has a high number of third-party software and
vendors with a high prevalence of IoT devices, POS, contactless systems and customer-facing
computing devices. This, coupled with a predilection towards supplier-managed systems or
networks and the franchise model, makes it exposed to weak or inconsistent security control
implementations that can be easily leveraged by threat actors to gain initial foothold or move
laterally in the environment.

Last, are the people. The weakest link. The hospitality industry has a large workforce that has a
high turnover and is seasonal in nature. This is a target rich environment for phishing and social
engineering attacks. Thus, it is not surprising that a large part of the initial vectors of attack in the
hospitality industry focus on email-based attacks such as phishing and email-borne malware.

With this in mind, it is highly unlikely that attacks targeting hospitality-oriented organizations will
subside or slow down. While the technical aspects of these attacks may change over time, the
underlying tactics tend to remain consistent. Traditional methods such as phishing, exploiting
known vulnerabilities, and compromising third-party vendors continue to pose significant threats.

Additionally, threat actors will continue to find innovative ways to outpace defenses that are
instituted. For example, the emergence of generative AI and LLMs introduces new risks, including
sophisticated social engineering attacks, data breaches, and vulnerabilities. We have seen the
dawn of this with FraudGTP and WormGPT, which may significantly increase the quality and
quantity of social engineering attacks against the hospitality industry.

As a result, preventative measures remain the most effective defense against all types of
cyberattacks. As shared earlier in the previous sections of the attack cycle, the following chart
serves as a comprehensive reference for actionable mitigations that can effectively thwart
attackers and prevent lasting damage.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies46

Initial Foothold

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Regularly perform simulated phishing assessments to evaluate the efficiency of anti-
phishing training and provide retraining for individuals who repeatedly fall victim.
 ❏ Enforce strong anti-spoofing protocols, involving the deployment of cutting-edge

technologies within email gateways.

 ❏ Employ a multi-tiered approach to email scanning, utilizing a solution such as

Trustwave MailMarshal to enhance the accuracy and efficacy of both detection and
protective measures.

 ❏ Routinely change passwords (e.g., every quarter) and enforce password complexity to

mitigate potential problems tied to valid accounts.

 ❏ Enable multi-factor authentication (MFA) to add an extra layer for the protection

of accounts.

 ❏ Conduct regular audits of local administrative accounts and obfuscate admin accounts

by avoiding the use of "admin" in their names.

 ❏ Utilize LAPS on Windows systems to manage local accounts.
 ❏ Incorporate Privileged Access Management (PAM) and Privileged Identity Management

(PIM) solutions to deepen your defense-in-depth strategy.

 ❏ Employ vulnerability assessments and penetration testing to pinpoint susceptible

servers.

 ❏ Elevate the priority of system and software patching for databases containing

customer, employee, and payment information. Implement database auditing tools like
Trustwave's DbProtect, capable of identifying misconfigurations and user privileges, to
proactively mitigate potential risks.

 ❏ Enforce the placement of all servers within the confines of a firewall and adhere to

sound network segmentation practices to fortify access control measures.
 ❏ Reinforce access controls, setting them to the minimum essential levels for

authorized users.

Initial Payload & Expansion / Pivoting

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Carry out regular audits and assessments of all applications in your environment.
 ❏ Employ detailed application whitelisting for designated hosts to limit exposure.
 ❏ Prevent the deployment of applications by malicious entities, posing as legitimate apps

that execute malicious commands.

 ❏ One of the most effective means of detecting malicious activities is by reviewing the

commands being executed.

 ❏ Implement privilege restrictions to prevent unauthorized sources from executing

different shells.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies47

Malware

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Utilize host-based anti-malware tools to assist in identifying and quarantining specific
malware but understand that they do have their limitations and are susceptible to
evasion by custom malware packages.

 ❏ If preventing infection isn't possible, prioritize audit controls. This involves activating
system logs on critical and valuable systems and workstations, and implementing
network logging through flows, Network Monitoring Solutions, or IDS devices on
ingress and egress channels.

 ❏ Implement active monitoring, as merely enabling logs is insufficient; logs lose

effectiveness without vigilant observation. Regular monitoring establishes a baseline of
normal activity, making anomalies or unusual traffic more conspicuous.

 ❏ Establish and routinely practice a formal Incident Response process.
 ❏ Perform continuous monitoring of Underground and Dark Web sources to detect any

information leakage that might have been overlooked.

Exfiltration / Post Compromise

ACTIONABLE MITIGATION RECOMMENDATIONS:

 ❏ Consistently monitor the Dark Web to detect possible compromises. Partners like

Trustwave can assist with this.

 ❏ Conduct regular penetration tests to proactively uncover vulnerabilities in your

systems, networks, and applications.

 ❏ Minimize the time needed for remediation to substantially reduce exposure and narrow

the window for potential exploitation.

 ❏ Continuously engage in threat hunting activities, such as Trustwave's Advanced
Continual Threat Hunt, to uncover any hidden compromises in your environments.

 ❏ Establish and routinely assess your incident response policy, focusing on scenarios that

are most likely to affect your organization.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation StrategiesAppendix/Reference

49

Threat Groups

ALPHV/BlackCat
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

BianLian
 ▪ Starting in June 2022, BianLian has been an active cybercriminal group
involved in ransomware development, deployment, and data extortion.
It has targeted crucial US infrastructure sectors, alongside Australian
infrastructure, professional services, and property development. Their
entry point often involves exploiting valid Remote Desktop Protocol (RDP)
credentials, utilizing open-source tools and command-line scripts for data
discovery and credential gathering.

 ▪ After accessing victim systems, the BianLian group extracts data using File
Transfer Protocol (FTP), Rclone, or Mega and then threatens to publish this
data unless a ransom is paid. Initially utilizing a double-extortion approach,
they encrypted systems and stole data, but shifted towards focusing
on data exfiltration-based extortion around January 2023. To maintain
control, the group often deploys custom Go-written backdoors tailored to
each victim, accompanied by remote access tools like TeamViewer, Atera
Agent, SplashTop, and AnyDesk for continued command and control.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies50

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
First, Black Basta does not publicly recruit affiliates and most likely only
collaborates with actors with whom it has worked with previously. This
collaborative methodology is possible because it has been assessed
that the Black Basta was formed from members of other successful
ransomware groups, so they know other actors. Additionally, the group
outsources its capabilities utilizing established tools, such as QakBot and
Cobalt Strike, or network access brokers, allowing the group to have a high
success rate once inside a victim's environment.

BlackShadow
 ▪ Traces of BlackShadow's operations have been identified dating back to
early 2019, indicating a long-standing presence. The group employs its
own .NET backdoors and custom tools for various actions on compromised
systems, including downloading files, executing commands, and
exfiltrating data.

 ▪ Often associated with Iranian state sponsorship, BlackShadow is notably
linked to the Pay2Key ransomware, which typically targets Israeli entities.
However, their motives differ from typical ransomware groups, as they are
not primarily financially driven.

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

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies51

Conti
 ▪ Emerging in 2020, Conti ransomware has been associated with the Ryuk

strain through shared code and demonstrates links to cybercrime clusters
like Karakurt and TrickBot / Wizard Spider. A notable occurrence was
an affiliate's release of the group's playbook in August 2021, detailing
tactics and vulnerabilities exploited. A significant development occurred
with the release of ContiLeaks in February 2023, which disseminated
Conti's internal chat messages and exposed domains compromised with
BazarBackdoor malware, facilitating network access. These leaks have
prompted changes in the group's dynamics, potentially leading to internal
divisions and a diminished rivalry with other RaaS entities, resulting in a
noticeable slowdown in their ongoing operations.

 ▪ Leveraging insights from the historical attacks as well as mentioned

leaks, Conti actors often choose to exploit vulnerabilities in unpatched
assets, further escalating privileges and enabling lateral movement
within victim networks. They also known to exhibit reliance on TrickBot
malware for certain post-exploitation tasks. Conti's tactics underscore a
comprehensive strategy that combines existing software, strategic tool
additions, credential compromise, and vulnerability exploitation to maintain
persistence, escalate privileges, and conduct lateral movements within
targeted networks.

Hive
 ▪ Hive ransomware emerged in June 2021, operating as an affiliate-driven
ransomware campaign targeting diverse sectors worldwide, including
healthcare, nonprofits, retailers, and energy providers. Their reach extends
from the US to Japan, employing tactics such as phishing with malicious
attachments and leveraging Remote Desktop Protocol (RDP) for lateral
movement within networks.

 ▪ The group faced law enforcement action, with authorities seizing their
Dark Web sites on January 26, 2023. The seizure, executed through a
collaboration involving entities like the US Department of Justice, FBI,
Secret Service, Europol, and European countries, marked a significant blow
to Hive ransomware's extortion and data leak activities.

Karakurt
 ▪ Established in June 2021, the Karakurt Hacking Team operates adeptly
by deploying Cobalt Strike beacons, utilizing tools like Mimikatz and
AnyDesk, and employing diverse techniques for network traversal and
privilege escalation. Their extortion strategy centers on data deletion and
confidentiality, although breaches of trust have been reported even after
ransom payment.

 ▪ Karakurt's unconventional tactics involve targeting victims previously

attacked by other ransomware groups, potentially involving data
purchases. They have also engaged in simultaneous attacks alongside
other ransomware actors, occasionally employing exaggeration about
breach severity or stolen data, showcasing their deceptive approach.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies52

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

iteration of the ransomware. The updated version, released in June 2022,
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

LV
 ▪ Operating since late 2020, the LV group functions as a RaaS entity,
with purported ties to the REvil (Sodinokibi) ransomware. While the
exact relationship remains uncertain, indications suggest that LV's
developers modified REvil's binary script, possibly acquired through a
partnership where access to source code was shared, stolen, or sold.
LV ransomware seems to have repurposed a REvil v2.03 beta version
by altering configurations for their own ransomware activities. This shift
highlights their collaborative approach with underground actors, enabling
them to target a broad spectrum of regions and industries. The success
of a ransomware variant extends beyond new features, emphasizing the
significance of expansive reach and improved distribution networks.

 ▪ Collaborating with threat actors holding underground access, LV

ransomware has effectively expanded its impact across various regions
and industries. This underscores the point that the influence of a
ransomware strain is not solely shaped by augmenting functionalities, but
also hinges on factors like strategic partnerships and robust distribution
networks.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies53

Magniber
 ▪ The initial detection of the Magniber ransomware took place towards

the end of 2017, when it was observed employing the Magnitude Exploit
Kit for malvertising attacks specifically targeting users in South Korea.
Despite its early identification, the ransomware has remained active and
has continuously enhanced its strategies by adopting novel methods
of obfuscation and evasion. In April 2022, Magniber gained infamy for
masquerading as a Windows update file, enticing victims into unwittingly
installing it. Subsequently, it began propagating through JavaScript
starting in September 2022.

 ▪ In early 2022, Magniber distributed itself through fake installers in

APPX and MSI formats. The ransomware was executed using the MSI
CustomAction table, which called a malicious DLL within the package. The
installer also dropped a malware file called Fodscript, used for privileged
escalation. Magniber employed various tactics, including posing as fake
installers, Windows updates, and COVID-19-related files to deceive users.
Additionally, it utilized malformed digital signatures to bypass execution
blocks and exploit vulnerabilities such as CVE-2022-44698.

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

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies54

Qillin, Royal
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

 ▪ Royal has been observed employing various methods to gain initial access
to vulnerable systems, often including - callback phishing, SEO poisoning
and exploiting exposed RDP accounts. Once they have successfully gained
access, the group utilizes a range of tools to facilitate their intrusion
operations. These tools include Chisel, a TCP/UDP tunneling software, and
AdFind, an Active Directory query tool, among others.

Ragnar
 ▪ Active since December 2019, Ragnar Locker is a ransomware strain that

predominantly targets English-speaking users. Both the ransomware group
and its binary share the name "Ragnar Locker." This ransomware scans and
terminates running services on infected machines, focusing on decrypted
services. Operating on Windows and Linux systems, it exfiltrates data,
utilizes the Salsa20 encryption algorithm for file encryption, and demands
payment for data recovery.

 ▪ Employing a dual approach, the Ragnar Locker group practices double

extortion. Victims are required to pay not only for file decryption but also to
prevent the public release of stolen data. Furthermore, the group promises
insights into the attack's origin and security recommendations for those
complying with their financial demands. The ransomware goes beyond
encryption, erasing volume shadow copies to hinder file recovery and
terminating services like vss, sql, veeam, and logmein to maximize impact.

Vice Society
 ▪ The Vice Society ransomware group gained attention between late 2022

and early 2023 due to a series of high-profile attacks, including one
affecting San Francisco's rapid transit system. While primarily focused on
education and healthcare, evidence indicates they are also often targeting
the manufacturing sector, suggesting a diverse industry penetration
approach through compromised credentials procurement.

 ▪ Initially known for exploiting the PrintNightmare vulnerability, Vice Society

utilized ransomware strains like Hello Kitty/Five Hands and Zeppelin.
Recently, they developed their own ransomware builder and adopted
stronger encryption techniques. A joint advisory by FBI, CISA, and
MS-ISAC in September 2022 highlighted the group's disproportionate
targeting of the education sector, with expectations of heightened attacks
coinciding with the 2022-23 school year.

2023 Hospitality Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies