# The 2024 Data Loss Landscape

Global cybersecurity insights into departing users, determined attackers and misdirected email.

[proofpoint.com](https://proofpoint.com)

## Table of Contents
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [Data Loss Is a People Problem](#data-loss-is-a-people-problem)
- [Counting the Costs](#counting-the-costs)
- [Departing Users and Determined Attackers](#departing-users-and-determined-attackers)
- [Sounding the Alarm](#sounding-the-alarm)
- [Departing Dearly](#departing-dearly)
- [Dark Cloud Overhead](#dark-cloud-overhead)
- [Maturing Beyond Compliance](#maturing-beyond-compliance)
- [Looking Ahead: Better Visibility, More Expertise](#looking-ahead-better-visibility-more-expertise)
- [Conclusion](#conclusion)
- [Methodology](#methodology)

---

## Introduction

Welcome to the inaugural edition of our Data Loss Landscape report. In these pages, we’ll explore the current state of data loss prevention (DLP) and insider threats across 12 countries and 17 industries. This is a new category of report for Proofpoint. But we believe it is in keeping with our core principle: that people are a critical variable in data security.

Every year, a handful of vulnerabilities and zero-day attacks create headlines and headaches for security teams. But beyond these technical issues, most analysts recognize that data is typically lost by users rather than system vulnerabilities and misconfigurations. The underlying cause in these cases could be simple carelessness, credentials stolen by a threat actor, or in extreme examples, a malicious insider taking advantage of privileged access to steal valuable data and intellectual property.

Complicating the situation still further are a handful of macro factors affecting organizations of every size. Cloud workflows have changed how data is stored, accessed and synchronized. Hybrid work has multiplied the number of environments in which sensitive data is consumed. Generative AI is absorbing common tasks and confidential data. And resourceful threat actors are constantly innovating to take advantage of any lapses in vigilance and using emerging technologies to improve their techniques.

Taking all these issues together, it makes sense to ask: are current DLP approaches holding up against today’s challenges? To answer this question, we surveyed 600 security professionals about the current state of DLP around the world. And we’ve supplemented those answers with data from our own Proofpoint information protection platform to convey the scale of the challenges organizations face in addressing data loss and insider threats.

## Key Findings

- **85%** of organizations experienced one or more data loss incidents in the past year.
- **38%** of organizations have a “mature” DLP program.
- **50%** reported business disruption as a consequence.
- **“Careless users”** were the most cited cause of data loss.
- **Generative AI** is the fastest growing area of concern.
- **1%** of users are responsible for 88% of data loss events.

## Data Loss Is a People Problem

The vast majority (85%) of organizations polled in our survey experienced at least one data loss incident in the past year, showing just how widespread this issue has become. The mean number of incidents per organization was just over 15, amounting to more than one incident a month. While these findings are not surprising given the shift to hybrid work, accelerated cloud adoption and high rates of employee turnover, they are sobering and illustrate the scale of the problem. In fact, 10% of respondents reported more than 30 separate incidents apiece. English-speaking countries enjoyed slightly lower rates overall. But even the country with the lowest percentage—the United Kingdom—still had 73% of respondents reporting at least one incident in the past 12 months.

![Chart showing 84.7% of organizations experienced data loss incidents in the past 12 months, while 15.3% did not.]

The prevalence of data loss across countries and industries begs an obvious question: what’s causing all these incidents? Our survey provides a surprising answer, with “careless users” (including general employees, IT workers and contractors/vendors) selected by more than 70% of respondents. Examples of carelessness include:

- Misdirected emails
- Visiting phishing sites
- Installing unauthorized software
- Sharing sensitive files publicly
- Emailing personally identifiable information (PII) to a personal email account
- Any other unintended user exposure of systems or data

### WHAT IS A CARELESS USER?
Data loss isn’t always the result of deliberately malicious activity. Sometimes mistakes are made. Of course, with data loss it doesn’t matter if the door was kicked down by an intruder or left open by a careless employee—the consequences can still be severe.

In February 2023, around 14,000 employees of the Liverpool NHS trust in the U.K. found out that their personal data had been shared with hundreds of NHS managers and 24 people outside the organization. In an apology letter to victims, the trust’s chief executive explained that a spreadsheet file with a hidden tab had been attached to an email. Although the hidden tab was not visible to recipients, employees’ names, dates of birth and even salaries were exposed. The organization worked swiftly to make things right, but it didn’t change the fact that personal information was shared—a situation in clear violation of GDPR laws.

> 1% of users are responsible for 88% of data loss events. The identity of this 1% is likely to change month to month.

Technical causes appear next, in the form of compromised (48%) and misconfigured (45%) systems, with lack of time and resources adding a significant human element to these issues.

**Top Causes of Data Loss:**
- Careless Users: 70.6%
- Compromised Systems: 48.1%
- Misconfigured Systems: 45.3%

One of the most common manifestations of user carelessness is misdirected email. With most webmail and native email clients offering address autofill, it's easy for users in a hurry to make mistakes. According to 2023 data from Tessian, which Proofpoint acquired last fall, the problem is widespread. About a third of users sent about two emails per year to the wrong recipient. That means a business of 5,000 employees can expect to deal with around 3,400 misdirected emails per year.

## Counting the Costs

The high incidence of data loss reported in our survey is mirrored by an almost equal incidence of negative consequences. More than 90% of those who experienced at least one incident reported a negative outcome. Over half said the result was business disruption and almost 40% said their organizations suffered reputational damage.

**Consequences of data loss incidents:**
- Business disruption/revenue loss: 56.6%
- Damaged reputation: 38.9%
- Weakened competitive positioning: 35.8%
- Regulatory violation/fine: 34.8%
- Litigation expenses: 28%
- No consequences — not reported externally: 8.8%

## Departing Users and Determined Attackers

The modern threat landscape presents security teams with challenges from all sides. Employee turnover, hybrid work, cloud adoption, generative AI and evolving attack techniques all threaten data security.

Our survey asked participants to weigh up which users present the greatest risk of data loss. Employees with access to sensitive data, such as HR professionals, finance teams and customer support personnel, were the most popular answer, cited by 63% of survey respondents globally.

**Users who pose the greatest risk for potential data loss incidents:**
- Employees with access to sensitive data: 62.8%
- IT users with privileged access credentials: 50.6%
- Departing employees: 28.7%
- Partners/suppliers: 25.0%
- Contractors: 23.4%
- Executive employees: 23.1%
- Researchers/developers: 18.7%

## Sounding the Alarm

The threat from careless, compromised or malicious users is reflected in the kinds of data alerts triggered on the Proofpoint information protection platform. Among endpoints, almost half of all alerts were caused by either copying files to USB or uploading them to the web.

**Endpoint Incident Category:**
- Copy to USB: 24%
- Web Upload: 21%
- File Sync: 12%
- Write Block: 3%
- Document Open: 3%

**Cloud Incident Category:**
- File Sync Upload: 17%
- File Access: 15%
- File/Folder Download: 12%
- File Upload: 7%
- File Preview: 7%

### WHAT IS A MALICIOUS USER?
While it might be comforting to think of cyber criminals as distant figures in far-off places, sometimes the threat comes from inside the house. In fact, insider threats can be even more dangerous than external attacks. Malicious insiders are able to bide their time, using privileged access to find valuable data and weak spots in security.

In December 2020, Ubiquiti employee Nickolas Sharp stole gigabytes of the company’s confidential data. Sharp used the Surfshark VPN service to cover his tracks and to keep his identity hidden. He also used his administrative credentials to erase signs of intrusion on the company’s server logs. In May 2023, Sharp was sentenced to six years in prison.

## Departing Dearly

Security professionals consider departing employees the third riskiest category of user. Data from our platform backs up this concern. Over a nine-month period, 87% of anomalous file exfiltration among cloud tenants using Proofpoint was caused by departing employees. This unusually high volume may signal that an employee is hoarding files and data before they leave.

## Dark Cloud Overhead

Nearly 38% of respondents said that the proliferation of cloud/SaaS applications is a challenge for their DLP programs. Between January–September 2023, 96% of monitored cloud tenants were targeted by brute-force attacks. More worryingly, over the same period, 96% of tenants were also subject to precision attacks, such as targeted phishing attempts.

### WHAT IS A COMPROMISED USER?
Zero-day vulnerabilities might make a lot of headlines, but there’s a reason most large-scale cyber attackers focus on bypassing people rather than systems. In 2022, one of the world’s most popular password managers, LastPass, suffered a major data breach that resulted from a single compromised user. The attacker accessed more information, including employee credentials and decryption keys, eventually undermining confidence in password management as a security best practice.

## Maturing Beyond Compliance

Many DLP programs were first spun up in response to legal regulations. But according to respondents, regulation and compliance are no longer the main drivers. It appears that as these initiatives mature, focus is shifting to protecting customer and employee privacy, with over 50% of respondents citing these as a primary driver for their DLP program.

**Primary motivational drivers for DLP programs:**
- Protecting the privacy of employees and customers: 50.3%
- Minimizing costs associated with data loss: 40.6%
- Protecting our company’s reputation: 39.3%
- Protecting intellectual property: 38.8%
- Meeting regulatory compliance standards: 38.3%
- Meeting internal compliance standards: 32.0%
- Ensuring the competitiveness of my company: 29.9%

**Status of DLP Program Maturity, Globally:**
- Emerging: 55%
- Evolving: 38%
- Mature: 7%

## Looking Ahead: Better Visibility, More Expertise

As DLP programs mature, respondents largely agree about the most significant ongoing challenges. Almost 70% cite visibility into sensitive data, user behavior and external threats as the most important capability for their DLP program. But 43% say that this is an area where improvements are still needed.

## Conclusion

Over 90% of respondents in our survey said that their organizations are currently investing in DLP solutions. However, only 41% strongly agreed that their investments were adequate. As more organizations embrace the cloud, hybrid work and workflow innovations like generative AI, DLP solutions must do the same. Every insider threat and data loss incident is unique and has the potential to cause significant consequences. That’s why detecting, investigating and responding to each one requires an approach that recognizes data loss as a people problem.

## Methodology

### Proofpoint Internal Data
Data was sourced from our Proofpoint information protection platform between January–September 2023 and from randomly selected Tessian deployments between January and December 2023.

### Survey Data
Proofpoint partnered with cybersecurity market research firm, CyberEdge Group, to develop the 15-question survey instrument. Respondents are IT security professionals employed by a commercial, non-profit or government organization with 1,000 or more employees. Research participants were drawn from 12 countries and 17 industries. With a sample size of 600 participants, the global survey margin of error (at a standard 95% confidence level) is 4%.

### About CyberEdge Group
Founded in 2012, CyberEdge is the largest research, marketing and publishing firm to serve the cybersecurity vendor community.

### About Proofpoint, Inc.
Proofpoint, Inc. is a leading cybersecurity and compliance company that protects organizations’ greatest assets and biggest risks: their people. More information is available at [www.proofpoint.com](https://www.proofpoint.com).

©Proofpoint, Inc. Proofpoint is a trademark of Proofpoint, Inc. in the United States and other countries. All other trademarks contained herein are property of their respective owners.