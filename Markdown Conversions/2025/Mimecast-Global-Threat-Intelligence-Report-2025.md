# AI Instruction Set for Converting Technical PDFs to Markdown

## Purpose
Ensure technical PDFs are converted to Markdown with complete fidelity, preserving all content, structure, and formatting.
## Goals
1. **Full Conversion**: Include all text, quotations, footnotes, references, and technical terminology without omission or summarization.  
2. **TOC Format**: Include a fully functional Table of Contents with proper linking.  
3. **Markdown Conventions**: Use clear, consistent, and professional formatting.  
4. **Images**: Describe image contents without embedding.
## Conversion Instructions
### Content
- **Include All Text**: Retain all sections, preserving the original structure and content.  
- **Headings**: Format with `#` for main headings, `##` and `###` for subheadings.  
- **Lists**: Use `1.` for ordered lists, `-` for unordered lists.  
- **Emphasis and Formatting**: Apply `_italic_`, `**bold**`, `>` for block quotes, and \`\`\` for code blocks.  
- **Links**: Format as `[text](URL)` and ensure accuracy.
### Images
- **Do Not Embed**: Replace with descriptive text: `![Image description]`.
### Table of Contents
- Place after the document title but before the main content:
  ## Table of Contents
  - [Section Title](#section-title)
  - [Subsection Title](#subsection-title)
- Ensure anchor links work and follow the format `(#section-title)`.
### Footnotes and References
- Use Markdown footnote syntax:  
  Content with a footnote[^1].  
  [^1]: Footnote content here.
- Retain all technical and academic terms exactly.
## Verification and Quality Assurance
1. **Accuracy**: Verify the entire document is converted without omissions.  
2. **TOC Functionality**: Check all links point to the correct headings.  
3. **Readability**: Ensure professional formatting and adherence to Markdown standards.
4. **Fidelity**: Confirm the output matches the original PDF exactly.

# 2025 Global Threat Intelligence Report

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Risk Radar](#risk-radar)
- [Threats in Focus](#threats-in-focus)
- [ClickFix](#clickfix)
- [CAPTCHAs Foil Threat Gathering](#captchas-foil-threat-gathering)
- [SVG Usage on the Rise](#svg-usage-on-the-rise)
- [Abuse of Notification Services](#abuse-of-notification-services)
- [Usage of Remote Monitoring and Management](#usage-of-remote-monitoring-and-management)
- [Change of Communications Channel](#change-of-communications-channel)
- [The Threat Landscape in Charts](#the-threat-landscape-in-charts)
- [Living off Trusted Services (LOTS)](#living-off-trusted-services-lots)
- [Recommendations](#recommendations)
- [Collaboration Threats](#collaboration-threats)
- [Campaign Detail](#campaign-detail)
- [Recommendations](#recommendations-1)
- [Industry Snapshot](#industry-snapshot)
- [Recommendations](#recommendations-2)
- [BEC Attempts Rising Again](#bec-attempts-rising-again)
- [Campaign Detail](#campaign-detail-1)
- [Recommendations](#recommendations-3)
- [Top Vulnerabilities Over Time](#top-vulnerabilities-over-time)
- [Recommendations](#recommendations-4)
- [Tracked Threat Actor Activity](#tracked-threat-actor-activity)
- [Scattered Spider MCTO3050](#scattered-spider-mcto3050)
- [UAC-0050 (DAVINCI GROUP) MCTO1025](#uac-0050-davinci-group-mcto1025)
- [MCTO3001](#mcto3001)
- [STORM-1865 MCTO1020](#storm-1865-mcto1020)
- [MCTO5005](#mcto5005)
- [MCTO3035](#mcto3035)
- [MCT03028](#mct03028)
- [MCTO3022](#mcto3022)
- [Conslusion](#conslusion)

The official report URL is: https://www.mimecast.com

# Report Content Below

<a name="introduction"></a>
## Introduction

In the first nine months of 2025, Mimecast processed more than

DEFENDING AGAINST THESE

24 Trillion data points for its nearly 43,000 customers, flagging

more than 9.13 billion threats during the nine-month period.

The data reveals trends, including greater usage of trusted

services, the preferred attacks against specific industries, and

signs of AI usage among cyber threat groups. To best defend

business systems, companies need to be aware of what

techniques attackers are employing.

In our 2025 Global Threat Intelligence report, Mimecast has

collected threat data from across our platform, focusing on

the risks posed by business communications, collaboration

environments, and workers. Along with insights from our

intelligence analysts and open sources, this threat report

aims to take vitals of the global threat landscape.

RISKS REQUIRES REFRAMING

CYBERSECURITY AS NOT ONLY

A TECHNICAL CHALLENGE BUT

A HUMAN AND GOVERNANCE

ONE. IN GENERAL, COMPANIES

NEED TO FOCUS ON SECURITY

HYGIENE, INCLUDING

AWARENESS TRAINING AND

HARDENING SYSTEMS. WHILE

TECHNICAL VULNERABILITIES

REMAIN IMPORTANT, THREAT

ACTORS INCREASINGLY

RECOGNIZE THAT PEOPLE

AND UNMANAGED SYSTEMS

ARE THE WEAKEST LINKS IN

ORGANIZATIONAL SECURITY.

<a name="executive-summary"></a>
## Executive Summary

The cybersecurity landscape in 2025 underscores

Shadow IT creates blind spots for defenders,

both attackers’ persistence and the iterative

allowing exploitation of tools and services outside of

improvements in attack techniques. Financial

organizations’ managed security controls. Whether

platforms, regulatory agencies, and city governments

through third-party wallet integrations in financial

have all found themselves in the crosshairs, and the

services or personal collaboration tools in corporate

adversaries range from profit-driven ransomware

environments, attackers weaponize convenience

operators to disciplined state-aligned teams.

against organizations. Remote work further

compounds this challenge, as employees operate

Human workers remain the most consistent point

from less secure environments, often with minimal

of attack, with shadow IT and AI-driven social

oversight or lack of awareness about their colleagues’

engineering providing attackers with both new tools

identities. Limited visibility enables undetected

and new targets. Social engineering tactics — from

intrusions until significant damage occurs.

business email compromise (BEC) to credential

phishing — are evolving into AI-powered operations

Finally, the rise of generative AI has dramatically

that are increasingly able to mimic vendors, partners,

lowered the barrier for highly convincing attacks.

and employees with credible email chains. Attackers

Threat actors can now automate spear-phishing

have also further adopted the tactic of shifting

campaigns, generate synthetic voices and video,

communication channels (from email to voice, for

and craft messages that evade traditional detection

example) and of using legitimate online services as the

tools. This amplifies the scale and precision of social

foundation of their offensive infrastructure.

engineering, turning what were once niche, labor-

intensive attacks into scalable operations. As a result,

organizations must adapt by ensuring employees are

prepared to recognize AI-augmented attacks and by

adopting AI internally to improve business workflows

and security operations.

<a name="key-findings"></a>
## Key Findings

### 01

HUMAN ELEMENT
UNDER ASSAULT

Threat actors

increasingly target

the human link in

the attack chain as

the most vulnerable

element, doubling

down on phishing

attacks and social

engineering with

schemes such

as ClickFix and

AI-augmented

phishing attacks.

### 02

BEC ATTACKS
EMBRACE
AUTOMATION

Business email

compromise (BEC)

has become more

sophisticated

with attackers

using automated

conversation chains

to further the illusion

that a worker is

communicating with a

legitimate vendor and

that a senior executive

is taking part.

![Image description: Restore pointlp-34.34-3 fix 41°24'12.2 23°44'54.4PE-3 NVGT]

### 03

MULTI-CHANNEL
ATTACK
STRATEGIES

Attacks increasingly

incorporate a change

of communication

channels, such as

including a phone

number for the victim

to call in a phishing

email, which helps

attackers bypass

organizational

defenses and

minimizes visibility

into attacks.

### 04

LEGITIMATE
SERVICES
WEAPONIZED
AT SCALE

Continuing the trend of

living off the land, living

off trusted services

(LOTS) has become

more common, with

attackers finding new

ways to incorporate

a wider variety of

legitimate services

— such as Adobe

Pay, DocuSign, and

Salesforce — into their

attack chains.

### 05

NOVEL
OBFUSCATION
METHODS

Attackers constantly

adopt new file formats

that allow code

execution or better

obfuscation, such

as hiding JavaScript

in Scalable Vector

Graphics (SVG) files

or using QR codes

to make it harder for

users and security

software to verify links.

<a name="risk-radar"></a>
## Risk Radar

THREAT ACTORS CONTINUE TO EVOLVE IN 2025, WITH MAJOR

CYBERCRIMINALS GROUPS TARGETING A WIDE SWATH OF INDUSTRIES,

SUCH AS RETAIL, AVIATION, INSURANCE, TECHNOLOGY, MANAGED SERVICE

PROVIDERS (MSPS), AND CRITICAL INFRASTRUCTURE.

![Image description: V2527-A5PPO-399.3]

Social engineering and manipulation of human

Threat actors have also adopted methods that

behavior are increasingly important pages in these

make reversing their attacks and attribution more

cyberattackers’ playbooks, as they shift from

challenging. Cyberattackers’ increasingly use

traditional malware-based attacks to human-oriented

compromised systems— especially developing

tactics targeting messaging and collaboration

technology hubs in Southeast Asia and Africa — to

platforms. Scattered Spider, also known as

launch their attacks complicating attempts to trace

Storm-0875 or Octo Tempest, is a highly adaptive,

the origin of attacks, as researchers can only track

well-resourced group that excels at sophisticated

adversaries to these jumping-off points. The ability to

social engineering tactics, often impersonating IT

use advanced proxy networks, compromised home

teams or help desks. Another group, TA2541, uses

routers, and common affiliate networks that distribute

virtual private servers to send phishing emails

an attacker’s workforce further obfuscates the

masquerading as requests for quotes and purchase

attribution process.

orders, which eventually lead to malicious scripts

embedded in files on Google Drive and OneDrive.

Despite that, Mimecast collects a trove of data from

attackers’ attempts to infiltrate and compromise

These threat actors also embody another shift in

our customers’ systems, shedding light on the latest

tactics: The increase in usage of trusted services as

techniques and trends.

a primary attack vector to deliver their payload and

conduct attacks. Trusted services complicate the

work of detecting and preventing these threats using

traditional security controls. Organizations need to

focus on policies, procedures, and user awareness

to complement technical security controls and make

their workforce more resilient to these human-

oriented attacks.

![Image description: F.RV2527-A5V2527-A5Restore pointfield flow controlp-34.34-3 fixW 41°24'12.2E 23°44'54.4PE-3 NVGT]

<a name="threats-in-focus"></a>
## Threats in Focus

SINCE OUR 2024 REPORT, CYBERCRIMINALS

AND RANSOMWARE GANGS HAVE GREATLY

EXPANDED THE USE OF TRUSTED SERVICES

TO AVOID TECHNICAL DEFENSES THAT MIGHT

OTHERWISE BLOCK THEIR ATTACKS — ADOPTING

A GREATER VARIETY OF SERVICES AND USING

THEM FAR MORE FREQUENTLY.

![Image description: V2527-A5PPO-399.3]

<a name="clickfix"></a>
## ClickFix

Attackers have increasingly shifted toward exploiting

user’s trust to bypass technical security precautions.

Mimecast has documented the increasing use

of the ClickFix technique — a social engineering

scam where attackers use fake error messages or

verification prompts to trick users into copying and

running malicious commands on their own devices.

A typical ClickFix attack chain uses website pop-ups

or phishing landing pages to urge users to copy-and-

paste a script onto the Windows command line or a

PowerShell terminal. Doing so typically leads to the

installation of infostealers, remote access trojans

(RATs), ransomware, and credential stealers.

First detected in March 2024, the use of ClickFix

has rapidly proliferated across the threat landscape.

Mimecast detected multiple malware campaigns

leveraging ClickFix in 2025, which has taken off in

popularity, increasing by more than 500% in the

first six months of the year. Overall, ClickFix

accounted for nearly 8% of attacks reported,

second only to phishing.

The constant abuse of these services has now

become the de facto standard for attacks:

Threat actors use DocuSign, Intuit, and PayPal

to send notifications of invoices due with a call-

back number to switch the communications

channel; they abuse email service providers

such as SendGrid and Mailgun to bypass email

authentication and block lists; and increasingly,

they are rewriting links to foil security solutions

that rely on reputations.

While living off trusted services (LOTS) helps

attackers bypass technical controls, artificial

intelligence has augmented their own attack chain

allowing them to create more convincing phishing

messages and automated email campaigns that

fool the human element. While exploitation

continues to be used in a minority of cases,

attacks using ClickFix and AI-generated email

messages have become the norm.

900,000

DETECTIONS OF THE TECHNIQUE ACROSS

OUR CUSTOMERS IN THE UNITED STATES AND

THE UNITED KINGDOM.

2M

OF MALICIOUS SVG FILES DETECTED,

USING A VARIETY OF SOCIAL-

ENGINEERING LURES

<a name="captchas-foil-threat-gathering"></a>
## CAPTCHAs Foil Threat Gathering

Legitimate and custom CAPTCHA services allow threat

actors to both better trick victims and slow threat

researchers’ ability to detect attacks. By embedding

CAPTCHAs on landing pages or within attack chains,

threat actors block automated security crawlers and

threat analysis tools from accessing and analyzing

malicious content, simultaneously taking advantage

of CAPTCHA’s legitimacy. Sophisticated JavaScript

obfuscation further disables functions[^1] like right-click or

keyboard shortcuts, hampering manual investigation and

dynamic analysis by human analysts.

Mimecast data shows that these advanced deceptive

techniques are on the rise, with thousands of unique

malicious CAPTCHA-protected URLs being detected

each month. Most recently, the cybercriminal group

Scattered Spider has used CAPTCHAs to foil defensive

analysis, with more than 900,000 detections of the

technique across our customers in the United States

and the United Kingdom.

[^1]: https://www.mimecast.com/threat-intelligence-hub/captcha-obfuscation/

<a name="svg-usage-on-the-rise"></a>
## SVG Usage on the Rise

Phishing campaigns are increasingly exploiting the

Scalable Vector Graphics (SVG) format to embed

malicious JavaScript and other executable code

in seemingly benign images. The malicious SVG

files often execute code when opened, redirecting

users to phishing pages or malware-download sites.

Between mid-February and mid-March, Mimecast

detected more than 2 million instances[^2] of malicious

SVG files, using a variety of social-engineering lures,

such as voice messages and multi-step redirections

involving fake PDF downloads.

Threat Actors will often also use obfuscation

techniques — such as Base64 encoding and

encryption — to evade security controls. Techniques

such as AutoSmuggle, a tool released in May 2022[^3],

make hiding JavaScript in SVG files even easier.

Mimecast expects attackers to continue using SVG

images, expanding into a wider range of image

formats to deliver and exploit systems in the future.

There are many novel ways that images can be used,

including composite images with QR codes, non-

visible code or beacons in a single pixel, or

embedded executables.

[^2]: https://www.mimecast.com/threat-intelligence-hub/svg-attachment-abuse/
[^3]: https://cofense.com/blog/svg-files-abused-in-emerging-campaigns/

<a name="abuse-of-notification-services"></a>
## Abuse of Notification Services

Email notification services are continuing to be

abused to deliver malicious content. Instead of using

low-reputation infrastructure, threat actors rely on

known providers that organizations already trust,

including:

- DocuSign
- Adobe Sign
- Intuit
- PayPal
- HelloSign

The abuse of trusted notification services such as

PayPal, DocuSign, and Intuit is a rapidly growing

and significant threat to organizations. Attackers

increasingly leverage these essential workflow tools

to deliver malicious emails

that blend seamlessly with legitimate

business communications, making detection

by both users and security systems

extremely challenging.

This trend is marked by a high dependency

on trusted notification platforms, which are

exploited for a range of attack techniques

including:

- Business Email Compromise (BEC)

scams that use minimal content in the

notification body and request a callback to

a threat actor-controlled number, enabling

further social engineering.

- Phishing links and QR codes

embedded within files hosted on these

notification services, directing victims to

credential harvesting sites or malware.

- Large-scale callback operations

that combine notification services with other

platforms, such as Microsoft SRS, to reach a

wide array of targets and increase the likelihood

of successful compromise.

<a name="usage-of-remote-monitoring-and-management"></a>
## Usage of Remote Monitoring and Management

Threat actors are increasingly turning to legitimate

Remote Monitoring and Management (RMM) tools—

such as ScreenConnect (ConnectWise), TeamViewer,

AnyDesk, and LogMeIn—to gain initial access to

victim computers. This marks a significant shift from

traditional tactics that relied on delivering malicious

files or attachments via email. By abusing trusted

RMM software, attackers can bypass many security

controls, as these tools are commonly used by

IT teams and their presence often does not raise

immediate suspicion. Instead of sending malware-

laden attachments, attackers now use phishing

emails or social engineering to trick users into

installing these legitimate RMM agents, granting

remote access without triggering standard

security alerts.

<a name="change-of-communications-channel"></a>
## Change of Communications Channel

Another significant trend this year is the increasing

use of multi-channel attacks, where threat actors

initiate contact with victims through email and

then transition to phone communication to further

their schemes. In campaigns such as Business

Email Compromise (BEC), phishing, and malware

distribution, attackers start with a convincing email—

often impersonating executives, IT staff, or trusted

vendors—to establish a plausible scenario or sense

of urgency. Once initial contact is made, they follow

on to phone communication. This approach is highly

effective because it leverages the personal and

immediate nature of voice communication, making

victims more likely to comply with requests to visit

malicious websites, make fraudulent payments, or

download malware.

READ MORE

The transition from email to phone allows attackers

to bypass traditional email security controls and

exploit psychological tactics such as authority,

urgency, and familiarity. During the phone call,

attackers use real-time persuasion, answer

questions, and address doubts, which reduces

skepticism and increases the likelihood of victim

compliance. This method has been observed in

high-profile attacks, including executive

impersonation and IT support scams, and is further

amplified by the use of AI-generated voices and

deepfake technology. The result is a more convincing

and harder-to-detect attack chain, making this

email-to-phone transition a major area of concern

for organizations in 2025.

<a name="the-threat-landscape-in-charts"></a>
## The Threat Landscape in Charts

THE TELEMETRY FROM MIMECAST SECURITY

SERVICES HIGHLIGHTS TRENDS IN ATTACKER

BEHAVIOR.

Not only are threat actors increasingly using trusted

services as the foundation for their campaign

infrastructure, but the detection shows signs

that attackers are increasingly using AI-generated

messages to create more phishing attacks[^4].

Data from various industries shows the most

commonly faced threats, from impersonation

attacks on the Professional Education sector to

phishing attacks against Real Estate brokers and

malware targeting Manufacturing.

MIMECAST ANALYZED HUNDREDS OF

MILLIONS OF DETECTIONS ANONYMOUSLY

ACROSS CUSTOMERS TO GAIN INSIGHT INTO

THE LATEST TACTICS AND TECHNIQUES BEING

USING BY THREAT ACTORS.

[^4]: https://www.mimecast.com/blog/how-chatgpt-upended-email/

<a name="living-off-trusted-services-lots"></a>
## Living off Trusted Services (LOTS)

### 01

Threat actors continue to weaponize legitimate

Virtual meeting room and hosting service DocSend,

business services to bypass security controls and

for example, has become much more popular, rising

exploit organizational trust relationships. Beyond

to become the most abused service in 2025, jumping

notification services, attackers exploit a broader

from the fourth most abused service in the latter half

ecosystem of trusted platforms to host malicious

of 2024. Adobe, Google, Microsoft SharePoint, and

content and redirect victims. These campaigns

email marketing service GetResponse were popular

leverage established providers that organizations

ways for attack campaigns to start, while the most

already trust, including:

popular destination remained DocSend, but other

popular ones include “smart link” service Click Magic, a

- SendGrid or Salesforce CRM for email delivery,
- SharePoint or Google Drive for hosting, and
- Cloudflare for CAPTCHAs.

known purveyor of adware, and Google.

Link-rewriting abuse is a tactic where attackers

compromise tools that sanitize email links—like

PHISHING NOW ACCOUNTS FOR 77% OF ALL ATTACKS, UP

secure email gateways—to create safe-looking links

FROM 60% IN 2024, LIKELY DUE TO ATTACKERS USING AI

TO DRAMATICALLY INCREASE PHISHING VOLUME.

THE GRAPH BELOW SHOWS THE OBFUSCATION METHODS,

PAYLOAD TYPES, AND DESTINATION DOMAINS OF THESE

MALICIOUS LINKS.

with hidden malicious redirects. Since these links

come from trusted sources, users and security tools

are more likely to trust them, making it harder to

distinguish between legitimate and malicious activity.

![Image description: Chart 01: The top legitimate domains used by attackers include DocSend, GetResponse, and Sharepoint, which resolve to pages on DocSend, ClkMg.com, and Microsoft SharePoint.]

![Image description: gamma.appgamma.appgamma.appgamma.applist-manage.comlist-manage.comlist-manage.comlist-manage.comforms.gleforms.gleforms.gleforms.glegoogle.comgoogle.comgoogle.comgoogle.com1drv.ms1drv.ms1drv.ms1drv.msadobe.comadobe.comadobe.comadobe.commystrikingly.commystrikingly.commystrikingly.commystrikingly.comOtherOtherOtherOthersharepoint.comsharepoint.comsharepoint.comsharepoint.comgetresponse.comgetresponse.comgetresponse.comgetresponse.comdocsend.comdocsend.comdocsend.comdocsend.comCompromisedCompromisedCompromisedCompromisedMalwareMalwareMalwareMalwarePhishingPhishingPhishingPhishingcphi-china.cncphi-china.cncphi-china.cncphi-china.cngamma.appgamma.appgamma.appgamma.appgospelfolio.comgospelfolio.comgospelfolio.comgospelfolio.comlive.comlive.comlive.comlive.comadobe.comadobe.comadobe.comadobe.comgoogle.comgoogle.comgoogle.comgoogle.commystrikingly.commystrikingly.commystrikingly.commystrikingly.comOtherOtherOtherOthersharepoint.comsharepoint.comsharepoint.comsharepoint.comclkmg.comclkmg.comclkmg.comclkmg.comdocsend.comdocsend.comdocsend.comdocsend.com]

<a name="recommendations"></a>
## Recommendations

Countering attacks that exploit trusted

services requires organizations to move

beyond traditional technical filtering and

implement comprehensive security hygiene

practices. Organizations must align their

security controls with actual business

operations while preparing for increasingly

sophisticated AI-enhanced attacks.

Create a baseline for business-critical

environments to understand normal

activity patterns, enabling detection of

anomalies when trusted services are

misused for malicious purposes and

blocking untrusted services.

Implement least privilege and

separation of duty principles to prevent

single points of failure across systems

CAMPAIGN DETAIL

Malicious campaigns distributed through Google

and user access.

Docs lead victims to files containing obfuscated

links. These campaigns employ URL shortening

Deploy layered security controls that

services to disguise the true destination, directing

continue protecting when individual

users to websites that automatically download

defenses are bypassed, rather than

MSI files containing remote monitoring and

relying on isolated defenses, and use

management (RMM) tools like LogMeIn Resolve

multiple detection systems to gain

Unattended. These legitimate RMM applications

comprehensive visibility.

have become a preferred initial access vector,

allowing attackers to establish persistent remote

Prepare for AI-enhanced attacks that

control over compromised systems while

create increasingly authentic-looking

appearing to use authorized business software.

messages, making both technical controls

READ MORE

and human awareness training critical

defensive layers.

<a name="collaboration-threats"></a>
## Collaboration Threats

### 02

Collaboration platforms fundamentally changed

Mimecast threat data sampled from Microsoft Teams,

communication — and how threat actors operate.

SharePoint and OneDrive environments show that

The platforms create persistent repositories where

platform threats are mostly malware. Because most

nothing truly disappears. When compromised these

enterprise collaboration is among closed groups,

tools, provide comprehensive organizational visibility,

spam and phishing tend to be less of a threat,

enabling lateral movement and the hosting of

while malware is either inadvertently forwarded

malicious content within trusted environments. The

attachments and links or self-propagating threats.

persistence of data amplifies risk, as platforms retain

However when we strip back the malware layer the

years of conversations, credentials, and strategic

really interesting data surfaces, highlighting the usage

plans that traditional email systems might purge.

of phishing and untrustworthy links.

This accumulated intelligence allows attackers to

build detailed profiles of targets, understand internal

processes, identify key personnel, and craft highly

convincing social engineering attacks.

Security teams now face the challenge of protecting

INTERESTINGLY, THE TRAINING AND TOOLS CATEGORY

CONTAINED THE MOST MALICIOUS CONTENT, WITH 96%

OF THE URLS ASSIGNED A CLASSIFICATION OF HIGH OR

MEDIUM RISK. IN ADDITION, THE SOCIETY CATEGORY,

WHICH INCLUDES POLITICS, HAD A HIGH PROPORTION OF

dynamic, persistent environments where the line

RISKY CONTENT AS WELL.

between internal and external, trusted and untrusted,

continues to blur.

![Image description: Chart 02: Detections of malware dominate collaboration environments (not shown), while spam and phishing make up the second and third-most encountered threats.]

<a name="campaign-detail"></a>
## Campaign Detail

Cybercriminals distribute phishing emails disguised as

business solicitations, directing recipients to malicious

files hosted on SharePoint and Google Drive. These

campaigns utilize compromised Office 365 accounts to

increase legitimacy and often employ sender domains

from industries related to the target organization,

enhancing the likelihood of user engagement. The

hosted files contain links that redirect to credential

harvesting sites designed to capture legitimate login

information. By leveraging trusted cloud platforms

and industry-specific domains, these attacks bypass

traditional email security filters while exploiting the

trust relationships organizations maintain with familiar

business platforms.

READ MORE

<a name="recommendations-1"></a>
## Recommendations

Hardening business environments against

collaboration platform threats requires

comprehensive security measures that

address both technical vulnerabilities

and human factors. Organizations must

implement robust controls that protect

persistent data repositories while

maintaining the collaborative functionality

that drives business operations.

Train employees on collaboration-specific

threats and set clear protocols for secure

information sharing across platforms.

Use human-risk management tools to

identify and block malicious links and files

in collaboration environments.

Deploy data loss prevention tools to

monitor sensitive data movement and

minimize information leakage across

collaboration channels.

Implement phishing-resistant multi-factor

authentication and establish governance

policies that define acceptable external

sharing practices with vendors and

partners.

This approach recognizes that collaboration
platforms create unique security challenges
due to their persistent nature and the valuable
organizational intelligence they contain,
requiring specialized defensive strategies beyond
traditional email security measures.

<a name="industry-snapshot"></a>
## Industry Snapshot

### 03

Attackers use different techniques against different

The Arts & Entertainment and Manufacturing sectors

industries, tailoring their approaches based on

tend to be targeted by malware more often than other

what works through experience and understanding

industries — likely due to their valuable intellectual

of sector-specific vulnerabilities. By calculating the

property, complex supply chains, and the potential for

average number of threats detected per user for each

operational disruption that ransomware can cause.

industry and attack type, our analysts determined

These sectors often have legacy systems, specialized

distinct threat profiles that reveal how threat actors

software that may have unpatched vulnerabilities, and

adapt their tactics to exploit industry-specific

highly privileged users without technical experience,

workflows, regulatory requirements, and business

making them attractive targets for malware

practices. To show details of the most significant

campaigns.

attacks, detections of spam and emails sent by low-

reputation senders have been removed.

![Image description: Chart 03: Threats per user (TPUs) for the Top-8 Industries]

Workers at real-estate companies encounter significantly more phishing attacks than employees in other

industries, driven by the sector’s high-value transactions, frequent wire transfers, and reliance on email

communication between multiple parties including buyers, sellers, agents, and attorneys. The time-sensitive

nature of real estate closings creates pressure that attackers exploit through urgency-based phishing lures.

Phishing is also a major threat for the Travel & Hospitality sector.

These patterns demonstrate that attackers conduct reconnaissance not just on individual organizations but

on entire industries, developing specialized playbooks that exploit sector-specific business processes and pain

points. Understanding your industry’s threat profile is essential for prioritizing security investments and tailoring

awareness training to the most likely attack scenarios your employees will face.

<a name="recommendations-2"></a>
## Recommendations

Industry threat profiles should guide security

prioritization, but organizations need

comprehensive protection against all

attack vectors.

Align security controls with your

industry’s primary threat patterns while

maintaining broad defensive coverage.

Use risk-based analysis that accounts

for both frequent industry threats and

high-impact attacks like business email

compromise.

Implement defense-in-depth and zero

trust frameworks as foundational

security approaches.

Tailor awareness training to emphasize

attack types most common in your

sector.

CAMPAIGN DETAIL

A sophisticated phishing campaign is targeting the IT

Software industry using adversary-in-the-middle (AitM)

techniques to capture both passwords and multi-

factor authentication (MFA) tokens of super-admin

ScreenConnect users. Attackers leverage Amazon’s

Simple Email Service (SES) to send convincing

phishing emails that bypass common security filters.

Compromised super admin accounts give attackers

full control over remote access infrastructure,

enabling malware deployment and data theft.

READ MORE

<a name="bec-attempts-rising-again"></a>
## BEC Attempts Rising Again

### 04

Business email compromise (BEC) threats dropped

Wire transfers and invoice fraud remain the top two

during late February until early April — representing

mechanisms used in BEC attacks, while help requests

a temporarily shift to malware-based attacks — but

and payroll changes are less common. These financial-

quickly picked up in late spring and throughout the

focused attacks typically involve larger sums and are

summer. The current BEC landscape shows attackers

harder to reverse than gift card scams, making them

focusing on wire transfers and using urgent language,

more attractive to sophisticated threat actors. The

employing the classic “we need this money transfer

chart of tactics associated with BEC campaigns also

now” pressure tactic — a trend that will gain strength

shows that creating a sense of urgency and changing

as deepfake voice and video allow attackers to create

the communications channel are both increasingly

convincing impersonations of executives during phone

common tactics, with attackers often combining email

calls or video conferences. While requests for gift

with phone calls or text messages. Meanwhile, the

cards used to be popular, more recent BEC attack

once popular gift card scam has largely disappeared

vectors focus on payment through fake invoices, bank

following increasing awareness of the tactic and

account changes, payroll updates, and requests for

improved employee training programs that specifically

aging reports or other financial information.

warn against these requests.

BEC Threats: Common Tags

wire tranfers and banking

invoice

urgency

communication channel switch

payroll change

help reqeust

gift cards

![Image description: Chart 04: BEC Threats Common Tags Count per Week]

<a name="campaign-detail-1"></a>
## Campaign Detail

Cyberattackers continue to refine their BEC attacks,

from originally focusing on impersonating CEOs

to now impersonating multiple sides of an email

chain between a vendor and executives. During

reconnaissance, attackers focus on obtaining

accounting reports containing financial details like

customer names, balances, and accounts payable

contacts. These enable attackers to craft fraudulent

invoice schemes. At the same time, human resources

and payroll data are targeted through social

engineering, often under the guise of routine HR

processes or urgent business needs. By exploiting

both financial and employee information, they

increase their chances of successfully impersonating

trusted parties and manipulating transactions.

To create the actual email chains, attackers rely

increasingly on AI to fabricate the thread of messages

between a vendor, the victim, and a purported

third party, crafted to appear to be a CEO or senior

executive urging quick payment of the invoice.

READ MORE

<a name="recommendations-3"></a>
## Recommendations

Business email compromise requires

both technical controls and strict

financial processes to catch unauthorized

bank account changes or payment

requests lacking proper purchase orders.

Company executives should establish

secondary communication channels

for verifying requests, and privileged

employees need regular training.

Prioritize awareness training as the

primary defense against BEC attacks,

as attackers may replicate executive

communication styles.

Implement multi-step verification

processes before processing

any invoice payments or money

transfers.

Establish secondary verification

channels that bypass email when

confirming financial requests.

Maintain training programs that

emphasize current BEC tactics,

as reduced gift card scams

demonstrate effective

awareness education.

<a name="top-vulnerabilities-over-time"></a>
## Top Vulnerabilities Over Time

### 05

In 2024, nearly 40,000 vulnerabilities were reported

to the National Vulnerability Database (NVD), or about

768 security issues every week. In 2025, the rate is

on track to surpass an average of 900 vulnerabilities

per week.

volume

NEARLY 40,000 VULNERABILITIES

REPORTED TO NVD, AVERAGING ABOUT 768

SECURITY ISSUES PER WEEK.

Yet volume tells only