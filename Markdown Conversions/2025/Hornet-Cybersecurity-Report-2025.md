An In-Depth Analysis of the Microsoft 365 Threat
Landscape Based on Insights from

hornetsecurity.com

## ABOUT HORNETSECURITY

Hornetsecurity empowers companies and organizations of all sizes to focus on their core business by
protecting M365 workloads, email communications, securing data, and ensuring business continuity and
compliance with next-generation cloud-based solutions.

Our flagship product, 365 Total Protection, is the most comprehensive cloud security solution for Microsoft
365 on the market, including email security, compliance, governance, and backup.

## WHAT IS THE CYBERSECURITY REPORT?

The Cybersecurity Report by Hornetsecurity is an annual analysis of the Microsoft 365 threat landscape
based on real-world data collected and studied by Hornetsecurity’s dedicated Security Lab team. Hornet-
security’s cybersecurity solutions process more than 4 and a half billion emails every month. By analyzing
the threats identified in these communications, combined with a detailed knowledge of the wider threat
landscape, the Security Lab reveals major security trends, threat actor actions and can make informed
projections for the future of Microsoft 365 security threats, enabling businesses to act accordingly. Those
findings and data are contained within this report.

## WHAT IS THE SECURITY LAB?

The Security Lab is a division of Hornetsecurity that conducts forensic analysis of current and critical
security threats, specializing in email security in the Microsoft 365 ecosystem. Our multinational team of
security specialists has extensive experience in security research, software engineering, and data science.

An in-depth understanding of the threat landscape established through hands-on examination of real-
world phishing attacks, malware, ransomware gangs and more, is critical to developing effective counter-
measures. The detailed insights uncovered by the Security Lab serve as the foundation for Hornetsecuri-
ty’s next-gen cybersecurity solutions.

2

## Table of Contents
- [CHAPTER 1 – EXECUTIVE SUMMARY](#chapter-1--executive-summary)
- [CHAPTER 2 – THE CURRENT MICROSOFT 365 THREAT LANDSCAPE](#chapter-2--the-current-microsoft-365-threat-landscape)
  - [EMAIL SECURITY TRENDS](#email-security-trends)
  - [SPAM, MALWARE, ADVANCED THREAT METRICS](#spam-malware-advanced-threat-metrics)
  - [ATTACK TECHNIQUES USED IN EMAIL ATTACKS IN 2024](#attack-techniques-used-in-email-attacks-in-2024)
  - [ATTACHMENT USE AND TYPES IN ATTACKS](#attachment-use-and-types-in-attacks)
  - [EMAIL THREAT INDEX FOR BUSINESS VERTICALS](#email-threat-index-for-business-verticals)
  - [BRAND IMPERSONATION](#brand-impersonation)
  - [SAFETY OF DATA IN THE CLOUD](#safety-of-data-in-the-cloud)
  - [Passkeys and Adversary in the Middle (AitM) Attacks](#passkeys-and-adversary-in-the-middle-aitm-attacks)
  - [Vendor Overdependence Concerns Deepen](#vendor-overdependence-concerns-deepen)
  - [What is Microsoft Responsible for?](#what-is-microsoft-responsible-for)
  - [The Difficulties Posed by Multiple Tenants in the Microsoft Cloud](#the-difficulties-posed-by-multiple-tenants-in-the-microsoft-cloud)
- [CHAPTER 3 – AN ANALYSIS OF THE MAJOR SECURITY INCIDENTS AND CYBERSECURITY NEWS OF 2024](#chapter-3--an-analysis-of-the-major-security-incidents-and-cybersecurity-news-of-2024)
  - [THE CROWDSTRIKE INCIDENT](#the-crowdstrike-incident)
  - [CHANGE HEALTHCARE](#change-healthcare)
  - [NATIONAL PUBLIC DATA](#national-public-data)
  - [MGM AND CAESAR’S CASINO BREACH](#mgm-and-caesar’s-casino-breach)
  - [23ANDME DNA TESTING SERVICE BREACH](#23andme-dna-testing-service-breach)
  - [LOCKBIT’S LEADER UNMASKED](#lockbit’s-leader-unmasked)
  - [XZ UTILS BACKDOOR](#xz-utils-backdoor)
  - [A YEAR OF MICROSOFT SECURITY DRAMA](#a-year-of-microsoft-security-drama)
- [CHAPTER 4 – FORECASTING THE THREAT LANDSCAPE IN 2025](#chapter-4--forecasting-the-threat-landscape-in-2025)
  - [DID WE GET LAST YEAR’S PREDICTIONS RIGHT?](#did-we-get-last-year’s-predictions-right)
  - [THE SECURITY LAB’S PREDICTIONS](#the-security-lab’s-predictions)
  - [LLMs in Attacker’s Hands](#llms-in-attacker’s-hands)
  - [AI-Enabled Deepfakes Used for Spear-Phishing and to Influence the Public](#ai-enabled-deepfakes-used-for-spear-phishing-and-to-influence-the-public)
  - [We’ll Start to See Noteworthy Attacks on LLM-Products](#we’ll-start-to-see-noteworthy-attacks-on-llm-products)
  - [Legal Cases Will Arise Due to AI Use and Will Lead to Regulation](#legal-cases-will-arise-due-to-ai-use-and-will-lead-to-regulation)
  - [New Regulatory Frameworks and Challenges](#new-regulatory-frameworks-and-challenges)
  - [Corruption of the Open Source Community](#corruption-of-the-open-source-community)
  - [Continued Predictions for Quantum Computing](#continued-predictions-for-quantum-computing)
  - [Increased Adoption of “Memory Safe” Languages](#increased-adoption-of-“memory-safe”-languages)
  - [HOW MUCH AT RISK WILL MY ORGANIZATION BE IN 2025?](#how-much-at-risk-will-my-organization-be-in-2025)
  - [WHAT ORGANIZATIONS SHOULD DO TO DEFEND THEMSELVES](#what-organizations-should-do-to-defend-themselves)
  - [Culture Eats Strategy for Breakfast](#culture-eats-strategy-for-breakfast)
  - [A Balanced Security Strategy](#a-balanced-security-strategy)
- [CHAPTER 5 – RESOURCES](#chapter-5--resources)

4

# CHAPTER 1
EXECUTIVE SUMMARY

4

## CHAPTER 1 – EXECUTIVE SUMMARY

By leveraging its huge user dataset, Hornetsecurity is uniquely positioned to conduct a detailed examina-
tion of email-based threats as well as those threats targeting the greater Microsoft 365 ecosystem. This
allows the security researchers at Hornetsecurity to distill this data into important insights for IT teams
and security professionals. Email continues to be a major communication channel, particularly for compa-
nies and professional organizations. In our analysis of more than 55.6 billion emails in 2024, 36.9% are cat-
egorized as “unwanted.” 97.8% of unwanted emails are spam or rejected outright due to external indicators
and 2.3% of unwanted emails were flagged as malicious.

## ANALYSIS OF MORE THAN 55.6 BILLION EMAILS

![Image description: A bar chart showing the classification of emails scanned by Hornetsecurity. The chart displays 'Clean' emails and 'Unwanted' emails, with 'Unwanted' being a smaller portion.](FIG 1. CLASSIFICATION OF EMAILS SCANNED BY HORNETSECURITY)

![Image description: A pie chart illustrating the classification of unwanted emails. The slices represent 'Spam', 'Threat', 'AdvThreat', and 'Rejected'.](FIG 2. CLASSIFICATION OF UNWANTED EMAILS)

5

## 33.3% OF ATTACKS

When we look at the attack types used in email
attacks, phishing retains its top place as the most
prevalent attack method, accounting for 33.3% of
attacks. This is followed closely by malicious URLs
accounting for 22.7% of cases. These numbers align
with the types of attacks that have gained pop-
ularity amongst threat actors over the past year
- mainly in reverse-proxy style credential theft at-
tacks that heavily leverage social engineering and
malicious links.

A renewed focus on social engineering and secu-
rity token / credential theft is noticeable in our data
regarding malicious file types as well. We track the
types of files used for the delivery of malicious
payloads in email attacks and found that there are
noted decreases in the use of malicious attach-
ments period. Nearly every malicious file type saw
a decrease in comparison with last year. That
said, HTML files, PDFs, and Archive files remain in
the top three spots in a continuation from the pre-
vious year.

Threat actors have been leveraging a slightly high-
er volume of easier to detect (and ultimately “re-
jected”) email attacks over the data period. This is
indicated by the slight decrease in the number of
malicious emails that were classified as “Threats”
and “AdvThreats”. As a result, we saw the threat in-
dex for nearly every industry drop during the data
period. This is because our industry threat index
compares the number of clean emails vs. the vol-
ume of “Threats” and “AdvThreats”. Also notable is
the fact that there is little variation from industry
to industry. Yes, there are some that are higher
than others, but the data continues to show, year
after year, that EVERY industry is under attack.

In terms of brand impersonations over the last
year, we found that despite remaining in the posi-
tion of number 1 most impersonated brand there
was a large decrease in the amount of DHL imper-
sonation attempts.

That said, the amount of FedEx impersonation
attempts tripled, Docusign and Facebook both had
more than double the amount of impersonation
attempts, while Mastercard and Netflix both saw
notable increases as well.

Finally, when we continue our annual discussion
regarding the safety of data in the cloud, a key
theme that we’ve seen from attackers this year is,
again, the increasing use of credential / token theft
toolkits via an Adversary-in-the-Middle attack.
When compared with previous years, these attacks
have become popular with threat actors. This is
because of the ease with which they can target
a large number of victims with VERY convincing
landing pages with minimal effort.

6

These toolkits are designed to account for MFA (Multi-Factor) authentication, which many organi-
zations assume (wrongly) keeps them 100% safe from said attacks. The cybersecurity industry continues
to address this concern with better scanning mechanisms, security awareness training, and phishing-re-
sistant login technologies like passkeys. However, these mitigations take time of course, and as a result,
some organizations have fallen victim leading to a loss or leakage of sensitive data.

As this style of attack still makes heavy use of email communications as well as increasing use

of chat communications like Microsoft Teams, a robust email and Microsoft 365 security strategy

is essential for operating safely in today’s digital ecosystem.

7

# CHAPTER 2
THE CURRENT MICROSOFT 365
THREAT LANDSCAPE

8

## CHAPTER 2 – THE CURRENT MICROSOFT 365 THREAT LANDSCAPE

On an annual basis, Hornetsecurity’s dedicated Security Lab reviews the company’s extensive data set
and analyzes the state of global email threats and communication statistics. Additionally, the team regu-
larly conducts forward-thinking exercises and provides insight into potential future threats. This chapter
focuses on reviewing the data from November 1st, 2023, to October 31st, 2024, which forms the basis for
projections of the changing threat landscape laid out in Chapter 4.

### EMAIL SECURITY TRENDS

Despite increasing usage of collaboration and instant messaging software, such as Microsoft Teams, email
continues to be a top area of concern in terms of cyberattacks. We’ve observed a continued decrease in the
number of emails categorized as Threats/AdvThreats - 2.3% this year, compared to 3.7% from last year, and
5.5% the year before that (When looking at “Unwanted” emails). That said, the risk to businesses around
the globe remains high. This is primarily due to increased use in social engineering techniques via low-ef-
fort spray-style email attacks that seek to get the target user to engage somehow.

By reviewing more than 55.6 billion emails collected over the current reporting period (November 1st, 2023
- October 31st, 2024), the Security Lab has made the following determinations:

### SPAM, MALWARE, ADVANCED THREAT METRICS

As we’ve seen over the last decade, email continues to be one of the primary methods that threat actors
use to launch attacks. Our data from this report’s data period classifies 36.9% of all emails as “Unwanted”
- a 0.6 percentage point increase from 2023. The definition of “unwanted” refers to emails that are not
genuine communications desired by the recipient. The chart below shows our breakdown of unwanted
emails along with clean emails.

This contrasts with last year’s reported number of 36.3% of all emails being categorized as “unwanted”,
showing a slight increase in unwanted emails year over year.

When you consider that we processed 55.6 billion emails in 2024, the number of unwanted emails accounts
for roughly 20.5 billion “unwanted” emails sent to businesses over the reporting period.

![Image description: A bar chart showing the classification of unwanted emails by category for 2024, including clean emails.](FIG 3. 2024. UNWANTED EMAILS BY CATEGORY INCLUDING CLEAN)

9

For a concise breakdown of percentages that make
up “unwanted” emails, we classified them as follows:

### ATTACK TECHNIQUES USED IN
EMAIL ATTACKS IN 2024

In our data analysis of emails from the data period
we observed the below breakdown of attack types
used in email attacks:

| CATEGORY | DESCRIPTION |
|---|---|
| Spam | These emails are unwanted and are often promotional or fraudulent. The emails are sent simultaneously to a large number of recipients. |
| Threat | These emails contain harmful content, such as malicious attachments or links, or they are sent to commit crimes like phishing. |
| AdvThreat | Advanced Threat Protection has detected a threat in these emails. The emails are used for illegal purposes and involve sophisticated technical means that can only be fended off using advanced dynamic procedures. |
| Rejected | Our email server rejects these emails directly during the initial connection from the sending email server because of external characteristics, such as the sender’s identity, and the emails are not analyzed further. |

**NOTE:** To provide a little more detail, the “Rejected” cate-
gory refers to mail that Hornetsecurity services rejected
during the SMTP dialog because of external characteris-
tics, such as the sender’s identity or IP address. If a sender
is already identified as compromised, the system does not
proceed with further analysis. The SMTP server denies
the email transfer right at the initial point of connection
based on the negative reputation of the IP and the send-
er’s identity.

![Image description: A bar chart showing the attack techniques used in email attacks in 2024. The categories include Phishing, Malicious URLs, Advanced-Fee Scams, Extortion, and Other.](FIG 5. ATTACK TECHNIQUES USED IN EMAIL ATTACKS 2024)

**NOTE:** In previous years we’ve been able to track the
change in occurrence of attack types from year to year.
However, due to changes in how we identify malicious
items and unwanted emails, there is a subset of occur-
rences that are marked as “Other”. This category includes
various attack methods that do not neatly fit into one of
the main categories we’ve displayed in previous years.
While we can provide a breakdown of attack types for
this data period, comparing this data directly to last year
would not yield an accurate representation.

10

What our data does show us for this data period is that phishing remains the number one attack
type used in email-based attacks, followed by malicious URLs. The growing popularity of mali-
cious URLs among attackers is largely driven by their use in reverse-proxy credential harvesting
attacks, leveraging tools like Evilginx.

Outside of that, Advanced-Fee scams are still quite popular amongst threat-actors followed by extortion
in 4th place. Extortion is notable as we continue to see cases where threat-actors will first exfiltrate data
prior to putting ransomware in place within a given environment. Should the target refuse to pay (due to
recovering from backup) the threat actor will threaten to release the data to the public.

### ATTACHMENT USE AND TYPES IN ATTACKS

Email attachments continue to be used by threat actors for the delivery of malicious payloads in 2024.
Threat actors use attachments to hide malware as well as add an air of authenticity to their malicious com-
munications, depending on the attached file type in use. Additionally, some rudimentary spam/malware
filters may be unable to scan certain file types leading to infection by more complex attacks such as HTML
smuggling. In fact, the use of malicious HTML files remains in the number one spot for most used file types
used in malicious emails, as shown below.

The breakdown of the file-types used for delivery of malicious payloads over the data period is shown
below:

![Image description: A bar chart showing the file types used for malicious payloads in 2024. The categories include HTML, PDF, Archive, Executable, and Other.](FIG 6. FILE-TYPES FOR MALICIOUS PAYLOADS IN 2024)

- PDF file usage saw a 3.6% point decrease
in 2024

- Archive files saw a similar trend in a
percentage point decrease of 1.8 in 2024

- We observed a near universal decrease in all
malicious file types as attackers pivot to other
attack styles

Over the past year, the use of malicious attach-
ments has not been as useful for threat actors as it
has in the past. As such we’ve seen a trend where
attackers are pivoting to more social engineering
with the goal of getting the target to take an action
other than open an attachment. For example, the
use of reverse-proxy adversary-in-the-middle
toolkits has seen much use during the data period.
This is due to the fact that with increasing adop-
tion of Multi-Factor Authentication (MFA), attack-
ers are leveraging token theft more frequently via
tools like Evilginx and PyPhisher. It’s easier to pro-
cure the authentication token as opposed to deal-
ing with the headache of gaining access to the tar-
get’s MFA method.

### EMAIL THREAT INDEX FOR
BUSINESS VERTICALS

One of the key areas we review on an annual (and
monthly) basis, is the number of threats being
levied at different industry verticals. This allows
us to determine if there are dedicated campaigns
or targeted attacks on specific industries. It also
provides some insights that business leaders can
use to help determine if they’re at increased risk of
attack or not.

Most notable in this year’s data is the fact that
EVERY industry vertical saw a decrease of the
associated email threat index. This correlates with
our data above showing the number of emails
classified as “Threats” and “AdvThreats” decreasing when compared with last year.

That all said, there were some industries that were
targeted slightly more than others.

- Mining Industry - Most mining organizations
have the same types of problems and chal-
lenges as a manufacturing organization. They
also commonly deal in precious metals, and this
tends to make them a prime target for threat
actors looking to use ransomware to extract
money from the organization.

- Entertainment Industry - Organizations of this
type typically fall into gambling, or tickets sales
etc. These organizations have become a target
due to the large amount of money involved.
Look at the 2023 attack on MGM and Caesars
Entertainment that we discuss in more detail
below.

- Manufacturing - The manufacturing space
has a history of being targeted frequently by
threat actors. This typically comes down to
threat actors going after intellectual property
for profit and / or ransom and many see this
sector as an easy target for double-extortion
and production disruption due to the nature of
their network security and also the fact that
they often utilize a large number of insecure
Internet of Things (IoT) devices and program-
mable logic controllers (PLCs).

The table below shows the threat index rating for
major industry verticals.

12

| MINING INDUSTRY | ENTERTAINMENT INDUSTRY | MANUFACTURING INDUSTRY | MEDIA INDUSTRY | RESEARCH INDUSTRY | HOSPITALITY INDUSTRY | EDUCATION INDUSTRY | CONSTRUCTION INDUSTRY | HEALTHCARE INDUSTRY | FINANCIAL INDUSTRY | AUTOMOTIVE INDUSTRY | REAL ESTATE INDUSTRY | TRANSPORT INDUSTRY | AGRICULTURE INDUSTRY | PROFESSIONAL SERVICE INDUSTRY | RETAIL INDUSTRY | UTILITIES | INFORMATION TECHNOLOGY | LOGISTICS INDUSTRY | OTHER AND/OR UNKNOWN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0.0 | 0.5 | 1.0 | 1.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| OCT 2022 - SEPT 2023 | OCT 2023 - SEPT 2024 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

![Image description: A bar chart comparing the median threat vs clean email ratio per industry for two periods: Oct 2022 - Sept 2023 and Oct 2023 - Sept 2024.](FIG 7. MEDIAN THREAT VS CLEAN EMAIL RADIO PER INDUSTRY)

**NOTE:** The threat index value is determined by the fol-
lowing calculation:

Threat Index Percentage = number of malicious emails
(Threat+AdvThreat) / (the number of malicious emails
(Threat+AdvThreat) + the number of clean emails) mul-
tiplied by 100 – This excludes spam and info mail.

Note on methodology
Different (sized) organizations receive a differ-
ent absolute number of emails. Thus, we cal-
culate the percent share of threat emails from
each organization’s threat and clean emails
to compare organizations. We then calculate
the median of these percentage values for all
organizations within the same industry to form
the industry’s final threat score.

### BRAND IMPERSONATION

Brand impersonation continues to be a major email
attack technique targeting end users and busi-
nesses in 2024.

The shipping company DHL has seen perhaps
the most dramatic shift in brand impersonation
attempts. The brand saw a mere fraction of imper-
sonation attempts in 2024 vs. 2023. That said, it
still remains in the number one spot on our most
impersonated brands list, followed closely by
FedEx.

Shipping brands continue to be popular due to the
fact that they can be easily incorporated in social
engineering style attacks via phishing and smish-
ing. Both attack styles boast a high degree of simi-
larity to real communications from these organiza-
tions and easily trick less trained users into giving
away personal details and / or payment informa-
tion.

13

Other notable data in this area:

- The amount of FedEx and Facebook brand
impersonations has tripled in the past year

- The amount of Docusign brand impersonations
has doubled over the data period

- Mastercard and Netflix are two other notable
brands that have seen noted increases as well

Our full data over the reporting period has revealed
most impersonated brands, as follows:

**NOTE:** Brand impersonation data is heavily affected by
regional variation. Several German brands are listed here
due to our large customer base in Germany.

Our analysis of 10,743,561 active mail-sending
domains in 2024 reveals gaps in email authentica-
tion implementation, leaving many organizations
vulnerable to brand impersonation attacks and
email spoofing.

|  | DHL | FEDEX | 1&1 | DOCUSIGN | AMAZON | FACEBOOK | MASTERCARD | VOLKS -UND RAIFEISENBANK | STRATO | NETFLIX |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 5 | 10 | 15 | 20 | 25 |  |  |  |  |  |
| OCT 2022 - SEPT 2023 |  |  |  |  |  |  |  |  |  |  |
| OCT 2023 - SEPT 2024 |  |  |  |  |  |  |  |  |  |  |

![Image description: A bar chart showing the top 10 impersonated brands for two periods: Oct 2022 - Sept 2023 and Oct 2023 - Sept 2024.](FIG 8. TOP 10 IMPERSONATED BRANDS)

Only 35.4% of analyzed domains have implemented
DMARC (Domain-based Message Authentication,
Reporting, and Conformance) protocols, indicating
that nearly two-thirds of domains lack this critical
security measure. Just 16.6% of all domains utilize
RUA (Aggregate Reporting URI) capabilities, which
provides essential visibility into email authentica-
tion results.

RUA (Aggregate Reporting URI) records are a vital
component of DMARC that enables domain
owners to receive detailed reports about emails sent
using their domain. These reports include:

- Volume of messages received

- IP addresses sending mail on behalf of
the domain

- Authentication pass/fail rates

- Sending sources and their compliance with
domain policies

Of the domains that have implemented DMARC,
47% are leveraging RUA capabilities, demonstrat-
ing that many organizations who adopt DMARC
understand the value of monitoring and visibility.

14

Through RUA monitoring, organizations are able to observe surges in spoofed emails originating from pre-
viously unknown IPs, enabling them to alert their customers about the specific phishing campaign. Finan-
cial institutions often utilize RUA monitoring to initiate takedown procedures within hours of a phishing
campaign’s launch.

### SAFETY OF DATA IN THE CLOUD

The “cloud” has been here for more than a decade now, but we’ve just started to see businesses either
mass-migrating to cloud services or being established as 100% cloud-hosted businesses. Take the storage
of business data for example. 10 years ago, most businesses still held some sort of on-premises file server
that hosted the organization’s critical data. Now it’s becoming more common to leverage cloud storage
for this. SharePoint Online and OneDrive for Business are increasingly becoming the place where data
lives and is secured with services like Microsoft Entra. As such the safety of data in the cloud becomes
an important discussion, not just in the M365 cloud, but for cloud services in general. While we’ll focus on
Microsoft 365 and the Microsoft cloud ecosystem throughout this report, much of what is discussed here
applies to other cloud providers as well.

Baseline defenses in the Microsoft Cloud have improved over the years, but they are far from perfect. More
organizations are making use of newer security features like Multi-Factor Authentication (MFA) and basic
email security through services like Exchange Online Protection, but this is often still not enough. Attack-
ers are always evolving and that can be seen clearly in the case of Adversary-in-the-Middle attacks.

### Passkeys and Adversary in the Middle (AitM) Attacks

Where defenders go, attackers follow. For several
years, we here at Hornetsecurity, as well as every
other security minded person and company, has
advocated for MFA as a more secure replacement for
the traditional username + password dance for sign-
ing in to systems. There has been a slow and steady
increase in the adoption of various forms of MFA,
from SMS text messages to hardware security keys.
However, it’s not like the criminals are going to throw
up their hands and give up their lucrative “business”
and they have adapted instead.

Their main approach has been to use reverse-proxy-
style phishing kits, either open source or “commer-
cial” packages that both help with crafting convinc-
ing email lures to trick users into clicking a link, and
also sets up proxy services with legitimate looking
sign in pages.

15

When a user clicks the link and is taken to a fake login page to enter their username and password, these
credentials are then passed onto the real site (as well as captured by the attacker). When the MFA prompt
is then raised, these reverse-proxy toolkits enable the end user to enter their MFA code or approve the
prompt as usual and it too is passed onto the real sign in page behind the scenes. Meanwhile the attacker
steals the token that the target identity service generated (Entra ID for example) and now the attacker can
use it to sign in as the user, thus this method is called Attacker in the Middle (AitM).

To defeat these more sophisticated attacks, you need a phishing resistant MFA method. These methods
are newer and not seeing huge adoption (yet) in the industry. Some examples include Windows Hello for
Business, FIDO2 hardware USB keys and most recently Passkeys. These MFA methods lock the authen-
tication to the legitimate site URL only, so even if the user is tricked into visiting a sign in page that looks
legitimate, the technology itself refuses to work because it sees that the site address isn’t matching.

The problem is that Windows Hello for Business requires specialized hardware (and only works for Win-
dows), while FIDO2 hardware keys are costly which has limited their adoption. That said, a Passkey uses
the same technologies as a FIDO2 key but relies on the security chip in your iPhone or Android phone
instead, removing the need for extra hardware.

Here, again, adoption has been slow, but more and more services now support it, and if you’re responsible
for security at your organization, you should definitely start piloting it today. We predict that now that
Microsoft’s Entra ID, Google Workspace and AWS along with Facebook and many others support Passkeys,
adoption will increase dramatically over the next 12 months.

### Vendor Overdependence Concerns
Deepen with Regards to Cloud Data
Safety

Vendor Overdependence is the practice of placing
many or nearly all core business processes and
procedures into the hand of a vendor partner. The
problem with the arrangement is if the vendor
has issues of some sort (security related or other-
wise), then the business suffers as a result.

We’ve talked at length about the potential
ven-
dor overdependence issue that some businesses
could face with Microsoft extensively via our
Monthly Threat Reports and The Security Swarm
Podcast. Needless to say, it’s an issue that per-
sists and is likely to worsen as Microsoft contin-
ues to build market share in various areas.

16

That all said, there are some new concerns that
have come to light over the past year to shine
an even brighter light on this issue. In the ongo-
ing series of successful breaches at Microsoft an
interesting article surfaced in June 2024.

In summary, Andrew Harris, who was working at
Microsoft at the time, identified a serious flaw in
Active Directory Federation Services (AD FS) and
tried desperately to get it fixed. His fears were
downplayed and as the US federal government
was about to sign a multi-billion-dollar deal with
Microsoft for their cloud services, the issue was
essentially swept under the rug. After he left
Microsoft in 2020, the SolarWinds attack, probably
the largest supply chain attack ever, was revealed
- and while the focus was on SolarWindows and their
compromised Orion product, Russian attackers
spread through networks using the ADFS flaw
after their initial foothold. This of course happened
long before the Cyber Safety Review Board (CSRB)
report mentioned further below, and long before
the Secure Future Initiative (SFI) at Microsoft got
started in earnest but time will tell if the “new”
Microsoft will indeed put security above new fea-
tures, something that’s a challenge for every com-
mercial company.

Again, organizations each need to make their own
decision when it comes to the matter of vendor
overdependence, but taking into account years of
varying security concerns at multiple levels, and
the fact of where Microsoft’s responsibility ends
with regards to your data, the choice becomes
clear.

### What is Microsoft Responsible for?

Many ask: “If Microsoft isn’t taking care of my data
and security, what are they really responsible for?”
The current stance from Microsoft on this question
has not altered in 2024. To fully understand, you
must be familiar with Microsoft’s Shared Respon-
sibility Model.

The important bit is that the shared responsibility
model states,

THE RESPONSIBILITY IS
ALWAYS RETAINED BY
THE CUSTOMER FOR:

- Information and Data
- Devices (Mobiles and PC)
- Accounts and Identities

17

Essentially, the customer is responsible for securing and protecting their information and data. Microsoft
is not. As organizations move to the cloud, they must keep this in mind when protection strategies are
implemented.

Another point worth mentioning is something that we included in this report last year. It’s still coming as a
surprise to many existing M365 customers so it’s worth mentioning in this annual report as well. Microsoft
changed its long-time stance in 2023 on the use of backup applications with M365. At a Microsoft confer-
ence last year, Microsoft announced Microsoft 365 Backup. A service was shown to provide basic backup
capabilities for M365. The important part of this announcement is not the service itself, but the change of
Microsoft’s long-time stance of “you don’t need to backup data in M365”. Many in the industry see this as
being driven by one of two things:

1. Microsoft has finally capitulated and now agrees that a focus on data retention alone is NOT enough
in M365

2. Microsoft simply wants a piece of the M365 backup market now that they’ve seen there is a large
market for such a service.

Both options seem likely, with option 2 being bolstered by the fact that they have also released a backup
API that vendors can use as well, for a fee. Regardless, the message is clearer than ever. Businesses ARE
responsible for the protection of any data that they place within Microsoft Cloud services.

### The Difficulties Posed by Multiple Tenants in the Microsoft Cloud

As Microsoft’s core cloud services have been out for a decade or more many organizations are finding
themselves in a place where they need to manage and maintain multiple Microsoft 365 environments.
This could be a business that has conducted several mergers and acquisitions, or maybe you’re a managed
services provider (MSP) providing IT services across multiple customers. In both cases many of these orga-
nizations are realizing the difficulties around managing multiple M365 tenants.

When we talk about the man-power overhead associated with this increased management burden there
can be direct ramification on the safety of data in the cloud. As an organization there have most likely
been standards defined for security best practices and feature enablement within the M365 environments
under management. Many administrators are finding that enforcing standards and limiting configuration
drift / mistakes within multiple disparate M365 tenants is highly difficult. With the nature of cloud services,
one misconfiguration can be the difference between a safe organization and a serious data breach.

18

Tenant Management is increasingly becoming more important for organizations looking to keep their M365
data safe. While Microsoft does provide a utility called Lighthouse, it has some limitations and many MSPs
find it lacking in features and scale. Some software vendors have built solutions to address this manage-
ment need for MSPs like 365 Multi-Tenant Manager for MSPs by Hornetsecurity