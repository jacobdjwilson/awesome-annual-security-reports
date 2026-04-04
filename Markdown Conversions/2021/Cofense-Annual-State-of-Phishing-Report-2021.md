# Annual State of Phishing Report 2021

## Table of Contents
- [Executive Summary](#executive-summary)
- [Let’s Get Started—The Phishing Defense Center (PDC) Today](#lets-get-started-the-phishing-defense-center-pdc-today)
- [The Big Phishing Campaigns of 2020—Emotet and Ryuk](#the-big-phishing-campaigns-of-2020-emotet-and-ryuk)
- [How COVID-19 Changed the Threat Landscape](#how-covid-19-changed-the-threat-landscape)
- [Fighting Crafty Humans—Malware in 2020](#fighting-crafty-humans-malware-in-2020)
- [The Need for Decreasing Dwell Time](#the-need-for-decreasing-dwell-time)
- [Stopping Attackers with Human Reporting and Analysis—PhishMe in 2020](#stopping-attackers-with-human-reporting-and-analysis-phishme-in-2020)
- [What We Might See in 2021](#what-we-might-see-in-2021)
- [About Cofense](#about-cofense)

---

## Executive Summary

If you think Cofense is a company that promotes phishing simulations to build naughty vs. nice lists to hand out pink slips for failing a “phish test,” then I recommend abandoning this report now.

### 2020 year in review
In fact, in 2020 Cofense stood alone actively discouraging sending COVID-19 themed phishing simulations at the outbreak of the pandemic. The peanut gallery of information security experts grumbled on Twitter about the need for realism. While they were occupied retweeting, the Cofense customer community produced more REAL coronavirus/COVID-19 phishing email indicators than the entirety of the global cyber vendor landscape combined.[^1]

Let that gel for a bit. The inventors of phishing simulations blocked COVID-19 themed PhishMe templates, yet our customers’ employees reported more real COVID-19 phish than anyone else.

This report explains how Cofense is in a unique position to report on this. In fact, most of this report is focused on the REAL phish we see that bypassed multiple layers of automation, only to be smoked out by real humans who are backed by organizations that encourage reporting.

### What went wrong in 2020
Over 1.5 million simulated phishing emails leave our PhishMe infrastructure every Monday. Unfortunately, some non-Cofense customers did not heed our cautionary tale of avoiding certain emotionally charged lures. 2020 claimed new CISO victims whose “awareness programs” publicly blew up on social media when the promise of a bonus in a phishing simulation to an organization cutting budget was not well received. 2020 pwned a security awareness vendor, too. While they were busy creating naughty employee lists for their Computer Based Training upsell, it was clear in their Incident Response webinar they didn’t have a serious program in place to triage suspicious email reports.

### Minimum effective dose
There is a problem in the awareness community that I’ll write more about in the coming months. It boils down to this: Your organization isn’t unique, and your security awareness program isn’t special. You need just enough phishing simulations to produce enough employee reports to enable your operations team to stop a REAL phishing campaign. We have published data on how to achieve this in previous years that continues to be overlooked and replaced with elaborate wastes of time.

Unfortunately, when it comes to phishing detection and response, I’m seeing partial information being reported to boards that emphasizes the wrong data. If you are producing reports void of employee reporting metrics, you are doing it wrong. I’m still seeing awareness professionals playing gotcha games with individual business units, completely detached from how real phishing actually works. Let’s not forget that organizations are taking these measures based on TRAINING data. What other training program exists where someone can lose their job for failing? All is not well in Security Operations Centers either. Everyone wants automation to do their job so they can be a threat hunter. Much like Homer Simpson’s self-driving semi. The good news is, if you stop more phishing campaigns in progress, you have fewer alerts. This means, you get more time to work on bug bounties on the company dime…ehh…I mean be a “threat hunter.” The fallacy is, if automation worked all the time, you wouldn’t have an alert queue.

### Malware is dead. Long live phishing.
We are no longer going to be producing a separate malware report like in years past. Instead, malware trends will be in this report. The vast majority of phishing campaigns are credential theft or conversational. While malicious attachments still play a role in phishing, the frequency of this has dramatically declined over the years. In fact, most phish attachments these days are not even malware, but instead, conduits to open a browser to further credential theft. While on the decline, we have our finger on the pulse of phishing related malware, and we will share that in this report.

### Setting the stage
While making the shift to a combined report, we also decided to take this opportunity to shift a few other notable mentions about the data. First, the time period covered in our research spans the calendar year. The next item relates to notifications to the user letting them know the security technology worked—‟Invoice.docx was malicious and removed.ˮ While these alerts could appear suspicious to the end user, technically these messages are informational. Lastly, we adjusted how we make industry comparisons. Finally, throughout the report you’ll find references to NAICS—North American Industry Classification Standard. We settled on this standard to align with other major research reports.

Thank you for suffering through my ramblings. Our teams burned the midnight oil organizing this data and we appreciate your interest. We have been working on this phishing problem for years, and our insight is only made possible by servicing a growing global population of the largest organizations. This report wouldn’t be possible without the data, and the data wouldn’t exist without our amazing customers and their employees reporting phishing.

Aaron Higbee
Co-Founder & CTO

[^1]: as measured by the COVID-19 Cyber Threat Coalition.

---

## Let’s Get Started—The Phishing Defense Center (PDC) Today

An enterprise customer asked us to manage their Cofense Triage application four years ago. This one-off project exploded into the Phishing Defense Center (PDC) staffed by a team of expert threat analysts, inside five locations across the globe, operating 24/7, processing millions of reported emails each year for large enterprises. What started out as a way of helping a customer shaped how we look at phishing detection and response today.

With Managed Phishing Detection and Response (Managed PDR) delivered through the PDC, we’ve gained even greater insight into the phishing threat landscape. In fact, we have a larger pool of enterprise phishing threat intelligence data than anyone else in the world. What’s even more remarkable is getting to see firsthand that well-conditioned users report real phish quickly and that reduces overall risk to an organization.

**We’ll say that again: Well-conditioned users report real phish quickly!**

![Chart showing reporting times: 19% <30 sec, 52% 0-5 min, 73% 0-30 min, 82% 0-59 min]

### It Only Takes One —To Bring Down an Entire Organization
1 in 11 user-reported emails are malicious (As identified by Cofense in customer environments).

### Cofense PDC Phishing Facts
In the millions of emails the Cofense PDC analyzed, they determined:
- 57% were credential phish
- 12% delivered malware
- 6% were business email compromise or CEO fraud
- 45% of the credential phish were Microsoft-themed
- 17% were finance-themed
- 9.3% of the reported messages were malicious:
    - 38% had a URL only
    - 36% had attachments
- Of the 255,000 malicious emails, we found nearly 100 unique malware families

### Fact: All Secure Email Gateways Leak
While your Secure Email Gateway (SEG) serves its purpose to remove many threats from your users’ inbox, none are 100% secure.

### Threat Actors Pivot Quickly—SEGs Can’t Keep Up
The tactics, techniques, and procedures (TTPs) leveraged by phishing attackers range from tried-and-true to innovative. In 2020, Cofense Intelligence tracked several common delivery tactics used to defeat email gateways and other perimeter controls.

### Long-Standing TTPs Unfortunately Still Work
Credential-stealing campaigns account for over 50% of phish reported by end users to the PDC. These emails have been found in enterprise environments with diverse types of phishing defense, including SEGs and content filters.

### Layering
The malicious pages threat actors stand up to capture credentials live for a very short time, putting Cofense in a unique position: we review reported messages within 60 minutes of human report. Globally. 24/7. One tactic we increasingly observed over the past year is the use of multi-stage websites for the user to navigate, also known as layering, that leveraged safe domains.

![Figure 1 - Layering: A 4-step process from OneNote file to credential harvesting]

### Trusted platform abuse
Phishing threat actors are abusing trusted platforms with increasing frequency to deliver malware and credential harvesting pages. Credential phishing pages and malicious payloads are often hosted on legitimate web hosting or cloud services.

![Figure 2 - Example of abusing trusted platforms]

### Look-Back Attacks: Finding New Ways to Abuse Aged-Out Features
In 2020, CVE-2017-11882—also known as the Equation Editor vulnerability—and Office macro-enabled documents continued to dominate as the most popular delivery mechanisms for malware in phishing campaigns.

![Figure 3 - Example of abusing older software features]

### Responses matter
One of the key features in Cofense Triage is getting a response back to the user reporting the suspicious email. Almost 17% of the emails identified as malicious were related to a financial transaction.

### A New Delivery Mechanism, Built to Evade
In 2020, GuLoader rose as one of the top malware delivery mechanisms in phishing, first appearing in Q1 and surging during Q2. GuLoader uses advanced techniques at every stage of execution to try to evade network, email, and host-based security technology.

---

## The Big Phishing Campaigns of 2020—Emotet and Ryuk

If we learned anything from 2020, it’s that threat actors’ abilities to quickly adjust their methods to world events can be lightning fast. From Emotet to Ryuk, and let’s not forget COVID-19, Cofense and our Cofense Labs and Intelligence teams worked overtime.

### Emotet
Cofense has been tracking the Emotet botnet for several years now. The primary method in which Emotet propagates itself is through malicious emails. Once an account has been compromised, Emotet scraps the userʼs emails and generates contact lists and unique phishing templates that are then sent out via the same compromised email accounts and systems. The tactic of using existing emails and responding to them as if it were a continuation of a previous conversation is known as a reply-chain attack.

![Figure 4 - Emotet Reply-Chain Sample]

### A final note on Emotet
On January 27, 2021, authorities from eight countries conducted a disruption operation against Emotet. However, do not count Emotet out yet. Emotet has been so effective that abandoning it entirely would be highly likely to represent a lost opportunity for considerable profit.

### The Ryuk Threat: Why BazarBackdoor Matters Most
On October 28, 2020, media reports and US Government (USG) notifications emerged regarding an active “credible” Ryuk ransomware threat targeting the US Healthcare and Public Health sector. Cofense assessed with high confidence that BazarBackdoor is the primary delivery mechanism currently used for Ryuk operations.

![Figure 5 - Ryuk Example]
![Figure 6 - Ryuk Example 2]

---

## How COVID-19 Changed the Threat Landscape

COVID-19 was certainly the source of the most disruption in 2020. During the peak of pandemic-themed campaigns, phishing emails predominantly delivered credential phishing and Agent Tesla keylogger, but threat actors also delivered ransomware, keyloggers, remote access Trojans, and information stealers.

### 6 Frequent COVID-related Phishing Themes
1. Pandemic updates and guidance purporting to be from global, federal, or local health organizations
2. COVID-19 office infection data/contact tracing
3. Updates on remote working changes—company news and meeting invites
4. Federal financial relief packages for small or medium business loans
5. Teleconferencing platform invites or required updates related to platforms like Zoom, Teams, WebEx
6. Financial claims related to COVID-19

---

## Fighting Crafty Humans—Malware in 2020

No matter how much automation drives a phishing campaign execution, behind every phishing attack is a threat actor. These adversaries understand what motivates and moves humans to action. They understand the power of social engineering, and how to outwit defense technologies and uneducated users.

### New and Returning Malware in 2020
- **New in 2020:** Avaddon Ransomware, Cheetah Keylogger, FireBird RAT, Gamorrah Bot, Grandoreiro, Hive RAT, LolKek Malware, Mass Logger, Matiex Keylogger, RedLine Stealer, STR RAT.
- **Returning after 9+ month dormancy:** Chanitor/Hancitor, Cobian RAT, Dharma Ransomware, Expiro, LatentBot, Proyecto RAT, Qarallax RAT, Remote Manipulator System (RMS), Sality.
- **Returned in 2020 after months of dormancy:** Black RAT, Nemty Ransomware, Hakbit Ransomware, BetaBot, Iced-ID, KPOT, Kutaki, Loda, Pyrogenic Stealer, Valak, Vidar Stealer.

---

## The Need for Decreasing Dwell Time

When malicious emails reach the inbox, the chance of at least one erroneous click remains high. Average click rate for credential phishing simulations in PhishMe customers in 2020 is 10.7%. One metric of growing importance is dwell time—the elapsed time between an attacker gaining access to an environment and when they are detected, and the threat mitigated.

---

## Stopping Attackers with Human Reporting and Analysis—PhishMe in 2020

You can’t stop human attackers without human reporting and analysis.

### PhishMe Data—Simulations
- Credential: 29%
- URL: 59%
- Attachment: 12%

### But what about training?
There is a reason we started with the phishing threat landscape and left the topic of training your users for the end. When it comes to training your users on threats leading to a data breach, simulating real threats is most effective.

---

## What We Might See in 2021

- **SOC Voice:** We expect the SOC to have a more active voice in enterprise email configuration.
- **MFA:** Phishing campaigns and tooling will be more aware of multi-factor-authentication.
- **URL Analysis:** Techniques to evade Automated URL analysis will improve.
- **Smishing:** Smishing will continue to be a big-nothing-burger.

---

## About Cofense

Cofense solves the problem of phishing emails that get past SEGs (Secure Email Gateways) and deliver threats to the inbox.

### What Makes Cofense Unique
- **Automated Response + Human Detection:** Cofense conditions end users to report suspicious emails.
- **Phishing Intelligence:** Cofense Intelligence maintains the largest, most accurate data set on phish that have hit the inbox.
- **Network Effect:** Over 25 million users are equipped with the Cofense Reporter button.
- **Unbiased Insights:** We are Switzerland for email security.
- **Focus:** 100% of our R&D is focused on developing solutions to stop phishing attacks.

© 2021 Cofense. All rights reserved.