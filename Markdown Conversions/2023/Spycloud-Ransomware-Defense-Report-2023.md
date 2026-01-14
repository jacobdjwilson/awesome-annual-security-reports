# 2023 Ransomware Defense Report

## Table of Contents
- [Introduction](#introduction)
- [Why We Do This Survey](#why-we-do-this-survey)
- [Key Findings](#key-findings)
- [The Shifting Ransomware Trends](#the-shifting-ransomware-trends)
  - [On the Positive Side, We Saw Fewer Organizations Affected...](#on-the-positive-side-we-saw-fewer-organizations-affected)
  - [...But the Impact Remains Immense for Entire Organizations](#but-the-impact-remains-immense-for-entire-organizations)
  - [The Cost Is Climbing, Too](#the-cost-is-climbing-too)
  - [A False Sense of Confidence](#a-false-sense-of-confidence)
- [Ransomware Is More Than a SecOps Problem](#ransomware-is-more-than-a-secops-problem)
- [Where SecOps and BizOps Collide](#where-secops-and-bizops-collide)
- [Battling Ransomware on Multiple Fronts](#battling-ransomware-on-multiple-fronts)
- [Countermeasures Misaligned with New Ransomware Tactics](#countermeasures-misaligned-with-new-ransomware-tactics)
- [Future Defense Priorities Show Some Disconnect](#future-defense-priorities-show-some-disconnect)
- [All Eyes on Prevention and Automation](#all-eyes-on-prevention-and-automation)
- [Adapting Ransomware Defenses for Stealthier Attacks](#adapting-ransomware-defenses-for-stealthier-attacks)
- [Final Thoughts](#final-thoughts)
- [About SpyCloud](#about-spycloud)

---

# INTRODUCTION

For the last several years, we’ve watched our workplaces digitally transform, making the convenience of working and collaborating from anywhere the rule rather than an exception. Many organizations have welcomed this new reality, but they’ve struggled to keep their security defenses in step with the fast pace of digital growth and an expanding attack surface.

Cybercriminals, however, haven’t had any problem staying current with a digital-first, cloud-first environment. As they quickly pivot to next-generation tactics for exfiltrating data and access, security operations (SecOps) teams are falling farther behind – while exposure to cyberattacks like ransomware is at an all-time high.

## Some Background Before You Dig In

After the release of our last Ransomware Defense Report in September 2022, ransomware attacks showed some promising signs of slowing down. Criminals tested other tactics and government agencies cracked down, with the number of attacks leveling off by the end of year. But that glimmer of hope fizzled quickly, with attackers picking up the pace so fast in 2023 that we’re headed toward the second-most costly year for ransomware in history.

Last year, we found that organizations were losing ground and felt less confident about their defenses than before. This year’s Ransomware Defense Report examines how security frontline and leadership perceptions, practices, and priorities have changed since then, and how SecOps teams are doing in their fight against ransomware.

Even through that ebb-and-flow, the sophistication and impact of ransomware attacks has grown. At least one new ransomware group with double-extortion abilities surfaced every month last year, while the average cost of a ransomware attack escalated to $5.13 million – surpassing the average cost of a data breach. And one thing hasn’t changed: ransomware is one of the toughest cybersecurity challenges organizations of all sizes and industries continue to face. In SpyCloud’s 2023 Malware and Readiness Defense Report, security leaders and practitioners ranked ransomware as the top threat to their organization’s security.

---

# WHY WE DO THIS SURVEY

As we note in our findings, ransomware defenses are not keeping pace with cybercriminals. We do this survey to shine a light on one of the contributing causes: an emerging threat that could be an early warning sign of a ransomware event – information-stealing malware, or infostealers.

Criminals are using infostealers to siphon authentication data – including logs with information that enable access to enterprise networks and applications – and selling the data to ransomware operators. And through a deep analysis of recaptured infostealer logs, we’ve uncovered that the presence of infostealer malware is related to the likelihood that a company will experience a ransomware event in the near future.

## THE INFOSTEALER-RANSOMWARE CONNECTION, BROKEN DOWN

SpyCloud researchers conducted a detailed analysis using ransomware event data from ecrime.ch and our own database of recaptured records from the criminal underground. Of 2,613 North American and European companies victimized by ransomware in 2023, 30% had at least one infostealer infection prior to being attacked.

Our analysis also showed that the presence of specific infostealer infections – Raccoon, Vidar, and Redline – increases the probability that a company will experience a ransomware event.

## THE MOST PREVALENT INFOSTEALER FAMILIES ASSOCIATED WITH RANSOMWARE VICTIM COMPANIES

Companies with Raccoon, Vidar, and Redline infostealers experienced a ransomware event within an average of 16 weeks post-infection.

*Data reflect a sample of 400 companies known to have experienced a ransomware event in 2023

- Raccoon: 76%
- Vidar: 8%
- Redline: 8%
- Metastealer: 2%
- Lummac2: 2%
- Rhadamanthys: 2%
- Stealc: 1%
- Aurora: 1%

---

In 2023, 30% of North American and European ransomware victim companies had an infostealer infection prior to being attacked.*

*Data reflect a sample of 2,613 companies known to have experienced a ransomware event in 2023. Data is current as of October 20, 2023.

---

Many organizations fail to fully remediate infostealer and other malware infections, focusing primarily on protecting the infected device and skipping critical remediation of exposed credentials and active session data, leaving them exposed to follow-on attacks. In addition to presenting survey results in this report, we offer insights about how comprehensive Post-Infection Remediation can help prevent ransomware attacks – and ultimately enable security teams to get ahead of attackers.

## About the SpyCloud Ransomware Report

Since 2021, SpyCloud has gathered insights from security leaders and practitioners about ransomware’s impact on their organizations and their defensive practices. In this third year of the report, we continue to analyze the trends related to the evolution of this costly cyber threat.

We surveyed 316 individuals in active cybersecurity roles within organizations in the US, Canada, and the UK with at least 500 employees. We asked them about:

1.  **TOP CONCERNS** about ransomware for their business, including financial impact
2.  **THE MOST COMMON** defenses their organizations have in place or on their roadmap
3.  **KEY GAPS** that may be leaving their organizations exposed

The report also provides insights into next-generation strategies that support a more complete remediation cycle. We encourage you to look at these trends and learn how best practices are evolving to keep pace with new ransomware tactics, techniques, and procedures (TTPs).

---

# Survey Demographics

SpyCloud solicited responses from individuals whose roles range from cybersecurity analysts to C-suite security executives. The majority of the 316 participants come from leadership levels: 37% are cybersecurity directors, managers, or team leads; 29% are CIOs, CISOs, and security executives (Figure 1).

## SURVEY PARTICIPANTS BY ROLE

- CIO, CISO, or cybersecurity executive: 29%
- Cybersecurity director, manager, or team lead: 37%
- Cybersecurity architect / engineer: 11%
- Cybersecurity operator / analyst / incident responder: 11%
- Cybersecurity administrator: 4%
- Other role in cybersecurity: 8%

The cross-section of surveyed organizations ranges in size from small (500-999 employees) and midmarket (between 1,000 and 9,999 employees) to large enterprises (with 10,000 or more employees). The two biggest cohorts represent mid-sized employers: 30% with 1,000-4,999 workers and 23% with 5,000-9,999. The largest enterprises (10,000+ employees) comprise a total of 28% of respondents (Figure 2).

## SURVEY PARTICIPANTS BY SIZE OF ORG

- 500 - 999 employees: 19%
- 1,000 - 4,999 employees: 30%
- 5,000 - 9,999 employees: 23%
- 10,000 - 25,000 employees: 12%
- More than 25,000 employees: 16%

---

# KEY FINDINGS

1.  **Despite some positive developments, the impact of ransomware attacks remains high.**
    The good news? We found a drop in the number of organizations affected by ransomware and in the number paying ransom compared to the previous year. This likely reflects the temporary slowdown of ransomware activity in the later part of 2022 before things ramped up again in the first half of 2023. Overall, however, impact from ransomware remains high, with 81% of surveyed organizations affected at least once in the past 12 months, and 48% of those that were impacted paying a ransom. Only 12% of those affected said the cumulative cost over 12 months was negligible, and for 39%, the cost was at least $1 million. The impact, however, is much broader than financial losses. Ransomware also disrupts operations, damages organizational reputation, and drains SecOps resources – and the implications go on and on.

2.  **Security teams are changing how they defend their riskiest entry points – but will need to keep pivoting to combat new attack vectors.**
    Survey participants ranked phishing and social engineering as the riskiest entry points for ransomware attacks again this year. With human behavior an ongoing issue, security teams are changing their approach – shifting from user awareness and training to technology-driven countermeasures to mitigate the inevitable human-driven risks. As teams rely more heavily on tooling, they agree that automated workflows would significantly improve their ransomware defenses and overall security posture. This is a necessary shift to make, but more adjustments are required. The majority of respondents ranked data backup and endpoint device protection as primary mechanisms for defense, but those countermeasures are insufficient as cybercriminals increasingly target unmanaged devices and steal authentication data that allows them to impersonate users and gain access to organizations’ networks and critical business applications.

3.  **Infostealer malware is a precursor for a ransomware event, but teams aren't worried about it – and they aren’t prioritizing malware remediation.**
    Organizations are optimistic about their ransomware prevention capabilities, with 79% of surveyed security professionals expressing general confidence in their ability to prevent a full-blown ransomware incident. But their optimism may be misplaced, since only 19% of organizations are prioritizing improved visibility and remediation of exposed credentials and malware-exfiltrated data. Additionally, respondents ranked monitoring for compromised web session cookies and tokens as the third least important countermeasure. With infostealer malware infections preceding more than one-third of ransomware attacks this year, these findings tell us that many organizations’ post-infection remediation efforts are leaving the door wide open for follow-on attacks.

---

# THE SHIFTING RANSOMWARE TRENDS

As we noted, ransomware took a roller-coaster ride in the past 12 months. Some industry research showed a positive trend for 2022, with the number of attacks leveling off or even decreasing, and ransomware revenue dropping 40%. But the reprieve was temporary. During the second quarter of 2023, ransomware attacks skyrocketed – and ransomware payments approached record levels by June.

SpyCloud’s survey reflects these shifting trends. Although some of our indicators moved in a positive direction, upon digging in, we found a bleaker picture than appears on the surface.

## On the Positive Side, We Saw Fewer Organizations Affected...

First, the positive news. We found a slight decline in the number of organizations affected at least once by ransomware in the past 12 months: 81% in this year’s survey vs. 90% last year. Additionally, we saw a year-over-year drop in the number of organizations affected at least once or multiple times (Figure 3). It's important to note that 'affected' doesn't necessarily mean a business was impacted by a successful ransomware event; rather, that they were impacted to some degree that required business resources.

### PAST FREQUENCY OF RANSOMWARE INCIDENTS (Y-o-Y)

| Number of Times Affected by Ransomware | 2021 | 2022 | 2023 |
| :------------------------------------- | :--- | :--- | :--- |
| None                                   | 10%  | 10%  | 19%  |
| One time                               | 30%  | 30%  | 30%  |
| 2 to 5 times                           | 40%  | 40%  | 37%  |
| 6 to 10 times                          | 10%  | 10%  | 8%   |
| More than 10 times                     | 10%  | 10%  | 6%   |

Contributing to some good news for organizations on the financial front is a decline in the number of organizations paying a ransom (48% in the past 12 months compared to 65% the previous year) and a slight uptick in the number of those that recovered data at least partially if not fully, whether paying or not – 95% in this year’s survey vs. 93% last year (Figure 4).

### RESPONSE AND OUTCOME TO RANSOMWARE ATTACK

| Outcome                                  | 2022  | 2023  |
| :--------------------------------------- | :---- | :---- |
| Paid ransom, fully recovered data        | 36.2% | 32.9% |
| Paid ransom, partially recovered data    | 12.2% | 23.7% |
| Paid ransom, had to recover data another way | 3.6%  | 2.0%  |
| Paid ransom, lost our data               | 1.1%  | 1.2%  |
| Did not pay ransom, recovered data       | 2.9%  | 2.0%  |
| Did not pay ransom, did not recover data | 32.6% | 49.8% |

## ...But the Impact Remains Immense for Entire Organizations

Despite some positive trends, ransomware remains a huge problem for organizations of any size, given that the majority are affected.

While the prevailing assumption is that larger organizations are in a better position to defend themselves given budgets and resources, our data shows that large enterprises with 10,000 or more employees were affected just as much as mid-sized organizations, with more than 72% reporting being affected at least once. Smaller organizations, however, weathered the worst impacts, with 90% affected (Figure 5).

**AT LEAST 81% OF ALL ORGANIZATIONS SURVEYED REPORTED BEING AFFECTED BY RANSOMWARE AT LEAST ONCE IN THE PAST 12 MONTHS**

### AFFECTED BY RANSOMWARE AT LEAST ONCE (BY ORGANIZATION SIZE)

| Organization Size        | Percentage Affected |
| :----------------------- | :------------------ |
| 500 - 999 employees      | 90%                 |
| 1k - 4,999 employees     | 85%                 |
| 5k - 9,999 employees     | 76%                 |
| 10k - 25k employees      | 74%                 |
| > 25k employees          | 72%                 |

## The Cost Is Climbing, Too

Last year, security researchers found an increase in average ransom demands across many sectors, possibly because attackers were trying to make up for the lower payee count. Even when victims choose not to pay, they still see financial losses that go far beyond the ransom. Fewer than 12% of our surveyed organizations that were hit described their costs as negligible. For 39%, the price tag was over $1 million (Figure 6).

### CUMULATIVE COST OF RANSOMWARE ATTACKS (FOR THOSE ATTACKED IN THE PAST 12 MONTHS)

| Cost Range   | Percentage |
| :----------- | :--------- |
| Negligible   | 12%        |
| $10k - $100k | 17%        |
| $100k - $1M  | 32%        |
| $1M - $3M    | 17%        |
| $3M - $5M    | 15%        |
| $5M - $10M   | 5%         |
| > $10M       | 2%         |

The harder-to-measure costs, from reputational damage to impact on operations and drain on resources, can be just as high or higher than the ransom itself. For example, SpyCloud’s data shows that multiple core teams across the organization, not just SecOps, are involved in traditional malware incident response. Considering that recovery times grew longer last year in many industries, the expense of response alone can quickly add up.

## A False Sense of Confidence

The positive developments we noted perhaps explain why 79% of surveyed security professionals feel fairly or highly confident about their capabilities to prevent a full-blown ransomware attack in the next 12 months (Figure 7). After all, perceptions are colored by past experiences.

### CONFIDENCE ABOUT PREVENTING A RANSOMWARE ATTACK

- Not at all confident we can prevent ransomware: 1%
- Somewhat confident we can prevent ransomware: 20%
- Fairly confident we can prevent ransomware: 45%
- Highly confident we can prevent ransomware: 34%

**79% OF RESPONDENTS SAID THAT THEY ARE GENERALLY CONFIDENT IN THEIR ABILITY TO PREVENT A RANSOMWARE INCIDENT – BUT THEIR OPTIMISM MAY BE MISPLACED**

Measuring confidence based on the past or the current state breeds complacency – which is especially dangerous since attackers are constantly innovating. Security practitioners understand this better than security leaders: executives expressed much higher general confidence than practitioners in preventing an attack. For example, only 71% of responding SecOps practitioners agreed they’re highly or fairly confident in this ability, compared to 91% of executives (Figure 8).

### PERCENTAGE OF RESPONDENTS GENERALLY CONFIDENT IN ABILITY TO PREVENT RANSOMWARE (BY TITLE)

- Executive: 91%
- Overall: 79%
- Architect / Engineer: 77%
- Manager: 75%
- Other: 72%
- Security Admin: 71%
- SecOps: 71%

Another factor that may have contributed to the false sense of optimism in the past twelve months was a temporary slowdown in activity, as several ransomware syndicates experienced chaos. Governments doubled down on dismantling high-profile groups such as Conti and REvil. But the cybercriminals quickly rebounded. REvil, for instance, resurfaced within months with an attack on a multibillion-dollar manufacturing company.

In the meantime, multiple new groups popped up. Among them were Play, which uses self-propagation techniques; and Black Basta, which launched a widespread campaign using a banking trojan to steal credentials. In the second quarter of 2023 alone, at least 14 new ransomware-as-a-service groups emerged. As these developments illustrate, the actors are multiplying, tactics are evolving, and the speed of criminal innovation is no match for current defenses.

Our survey found that the two sectors most affected by ransomware at least once in the past 12 months were retail (93%) and technology (91%) (Figure 9). This isn’t surprising, considering these sectors also lead in the amount of exposed data available on the criminal underground. SpyCloud’s recent Fortune 1000 Exposure Report found, among other things, that:

- **TECHNOLOGY**: Had the lion’s share of compromised session cookies (1.26 billion of the 1.54 billion total), and nearly 68,000 malware-infected employees.
- **RETAIL**: Had 5.88 million compromised cookies and 11,950 malware-infected employees.

This authentication data, exfiltrated from devices infected by infostealers, enables cybercriminals to easily impersonate employees and infiltrate the company.

### INDUSTRY BREAKDOWN: ORGANIZATIONS AFFECTED AT LEAST ONCE

- Retail: 93%
- Technology: 91%
- Overall: 81%
- Manufacturing: 79%
- Financial Services: 79%
- Healthcare: 63%
- Government: 40%

We were surprised, however, that our survey identified the healthcare sector as the second-least affected industry. Although healthcare-specific cyberattacks don’t seem to appear as frequently in headlines as of late, the FBI’s Internet Complaint Center data shows more ransomware attack reports were received from healthcare organizations in 2022 than any other critical infrastructure sector.

---

# RANSOMWARE IS MORE THAN A SECOPS PROBLEM

Although some organizations may not see big, immediate financial impact from ransomware attacks, they recognize that the exposure due to data loss creates just as much risk, if not more. Participants ranked exposure of proprietary and sensitive data as the greatest potential impact of ransomware, followed by disruption to business operations and disruption to IT and SecOps (Figure 10).

The concern over data exposure maintained its lead from last year, reflecting the prevalent double-extortion trend. With 89% of ransomware attacks incorporating data exfiltration, organizations realize that they need to worry about much more than being locked out of their encrypted systems or data.

### PERCEIVED GREATEST IMPACTS OF RANSOMWARE (ON A SCALE FROM 1 TO 5)

- Exposure of sensitive or proprietary data: 4.17
- Disruption to business operations: 4.11
- Disruption to IT / security operations (or service levels): 4.05
- Loss of business-critical data: 3.98
- Hard cost of recovering and restoring to normal operations: 3.96
- Legal or compliance ramifications: 3.90
- Damage to brand reputation: 3.88
- Loss of customer satisfaction: 3.83
- Loss of revenue: 3.71
- Hard cost of paying the ransom: 3.46

---

RAN SO MWARE ATTACK
$5.13 AVERAGE COST ACCORDING TO 2023 IBM COST OF DATA BREACH REPORT

---

For years, compromised credentials (username + password combo) were considered the highest risk for cybercrimes such as account takeover (ATO). Today, with access as the new currency, session hijacking or next-generation ATO is emerging as a new tactic.

Session hijacking originates from the takeover (or “hijack”) of an active browser or application session using a stolen, still-valid authentication cookie where the criminal appears as a verified clone of a legitimate employee. This method goes beyond traditional credential exposure and expands the data criminals can now use to assume the access of an authenticated user.

Criminals leverage these active sessions to exfiltrate data, and monitor and mimic user behavior patterns.

## Where SecOps and BizOps Collide

As we’ve discussed, ransomware is not just a SecOps problem. It affects business operations by hoarding resources across the organization, often involving a minimum of seven internal departments, and can quickly result in damaged brand reputation or loss of business. IBM’s annual Cost of a Data Breach Report shows a painful price tag for an organization due to a ransomware attack: $5.13 million on average, not including the ransom itself.

But the burden to proactively protect business operations does generally fall on security teams working in the trenches, and these teams are often bringing the proverbial knife to a gunfight. Simply put, traditional malware remediation processes stop short of complete Post-Infection Remediation, keeping the door open for attackers to come back by leaving that stolen data out for the taking and available to use until it’s invalidated.

SpyCloud’s Malware Readiness and Defense Report, released earlier this year, found that 92% of security leaders and practitioners are extremely or significantly concerned about malware-stolen data leading to future attacks. Unfortunately, it also revealed that incident response today often lacks the crucial steps to negate the consequences of that exposed data – and, as we uncovered in this survey, it’s still much the same.

To prevent ransomware attacks and protect business operations, SecOps teams must remediate applications and users compromised by malware infections. A machine-centric process of isolating and reimaging the infected device only cuts the connection to the malicious intruder. It doesn’t address the stolen credentials, cookies, and other authentication data making its way to darknet markets, where it can be leveraged by initial access brokers selling guaranteed access to ransomware gangs.

Last year alone, SpyCloud researchers recaptured 22 billion stolen cookie records, which indicates criminals are shifting tactics to steal, buy, and trade this highly accurate and highly valuable data – minimizing their need for larger breach datasets that may be clouded with old, outdated, and for their purposes, somewhat useless data.

For ransomware attackers, session hijacking is a highly successful tactic, yielding much better return on investment – and we expect to see it become mainstream as a way around passwordless technologies (like passkeys).

---

# BATTLING RANSOMWARE ON MULTIPLE FRONTS

Phishing and social engineering, along with unpatched vulnerabilities, once again ranked as the riskiest entry points for ransomware (Figure 11). This was expected, since ransomware is often preceded by human behavior that results in a malware infection, which can then enable a ransomware attack. Similarly, respondents to our malware defense survey identified phishing and spear-phishing as the second greatest threat to their organization’s security overall, with ransomware as the top threat.

### PERCEIVED RISK OF ENTRY POINTS FOR RANSOMWARE (ON A SCALE FROM 1 TO 5)

- Phishing / social engineering: 3.87
- Unpatched vulnerabilities: 3.72
- Third-party or partner connections: 3.61
- Unmanaged employee devices: 3.57
- Exposed or weak credentials that enable ATO: 3.53
- Unmanaged contractor devices: 3.48
- Exposed (weak) APIs: 3.46
- Stolen cookies / tokens that enable session hijacking: 3.43

We were surprised, however, to see stolen cookies/tokens rated as the least risky entry point, suggesting that understanding of this new threat is just beginning. This entry point is an especially high risk in passwordless environments, which many view as the future of authentication. While passkeys are a tremendous improvement over passwords, cybercriminals are simply working around passwordless authentication with session hijacking attacks.

Not all sectors view their riskiest entry points through the same lens, with some placing higher emphasis than the average across all industries on risks such as stolen cookies and unmanaged or undermanaged devices. For example:

- **WEAK APIs** are a bigger concern in retail, manufacturing, and technology compared to the average.
- **Manufacturing, Technology, and Healthcare** view **COOKIES** as riskier than the average.

APIs and stolen API keys, which are another form of access being exfiltrated from malware-infected devices.

Across sectors, retail cybersecurity professionals are the most concerned about UNMANAGED EMPLOYEE DEVICES.

---

# COUNTERMEASURES MISALIGNED WITH NEW RANSOMWARE TACTICS

Year over year, data backup has remained the most important countermeasure for organizations (Figure 12). We highlight this as concerning because it shows that defenses are not adjusting to the shift in ransomware tactics. Backup was effective years ago when data encryption was the biggest problem, but it doesn’t mitigate the risks of modern ransomware – which relies heavily on malware-exfiltrated authentication data.

### MOST IMPORTANT COUNTERMEASURES IN PRACTICE TODAY (ON A SCALE FROM 1 TO 5)

- Data backup: 4.36
- Multi-factor authentication (MFA): 4.26
- Endpoint / device protection: 4.24
- Email security (with phishing detection): 4.21
- User awareness / training: 4.18
- Monitoring for exposed credentials: 4.13
- Patch & secure configuration management: 4.10
- Threat intelligence services: 4.08
- Network / resource segmentation: 4.04
- Monitoring for compromised web sessions (stolen cookies / tokens): 3.98
- User and entity behavior analytics (UEBA): 3.87
- Deception technology (e.g., virtual honeypots): 3.80

Organizations are optimistic about their ransomware prevention capabilities, with 79% of surveyed security professionals expressing general confidence in their ability to prevent a full-blown ransomware incident. But their optimism may be misplaced, since only 19% of organizations are prioritizing improved visibility and remediation of exposed credentials and malware-exfiltrated data. Additionally, respondents ranked monitoring for compromised web session cookies and tokens as the third least important countermeasure. With infostealer malware infections preceding more than a fifth of ransomware attacks this year, these findings tell us that many organizations’ post-infection remediation efforts are leaving the door wide open for follow-on attacks.

The importance of MFA grew significantly year over year, which may be contributing to organizations’ false sense of security. Although organizations should deploy MFA as one of their critical defense layers, they must also take the steps to identify malware-infected employees and invalidate stolen cookies that enable authentication bypass and session hijacking. As stated earlier, MFA and passwordless technology such as passkeys are not sufficient fixes because session hijacking bypasses any form of authentication.

Since technology and tools are only one part of the defense equation, we also asked the security pros about their operational and organizational countermeasures. Most feel that they adhere well to basic hygiene practices such as patching and applying least privilege techniques (Figure 13). While the majority already have strategies like ransomware-specific incident response in place, plenty of work remains to be done, with a good number of respondents noting they are considering or are only in the planning stages of implementing upgrades to their existing strategy.

### STATUS OF RANSOMWARE COUNTERMEASURES

| Countermeasure                                       | Already in Good Shape | Plan to Upgrade | Plan to Add | No Plans |
| :--------------------------------------------------- | :-------------------- | :-------------- | :---------- | :------- |
| Adhere to security hygiene best practices            | 60%                   | 21%             | 17%         | 2%       |
| Cyber insurance that includes coverage for ransomware attacks | 48%                   | 27%             | 17%         | 8%       |
| Ransomware-specific incident response team           | 48%                   | 32%             | 19%         | 4%       |
| Ransomware-specific incident response training or exercises | 45%                   | 30%             | 23%         | 2%       |
| Ransomware-specific incident response plan / playbook | 42%                   | 33%             | 23%         | 2%       |

It’s worth noting that there is a significant disconnect between the high confidence in operational practices and the high number of organizations that were affected by ransomware in this year’s survey. This gap tells us that either the combination of technology and processes isn’t working – or organizations are overly optimistic about their controls.

---

# THE IMPOSSIBLE HUMAN FACTOR

Organizations recognize that human behavior plays a major role in the ability to defend against ransomware, but they’re shifting from user awareness to technology-based measures. Unfortunately, these measures only work if SecOps teams have complete visibility and control across all users, applications, and devices connecting to the network and accessing sensitive data – and that’s not the case today. In recent findings, we learned that:

-   **36% OF ORGANIZATIONS** allow unmanaged personal devices to access business applications and systems.
-   **54% OF ORGANIZATIONS** struggle with shadow IT due to employee adoption of applications and systems without IT’s consent.
-   **28% OF ORGANIZATIONS** allow unmanaged third-party devices to access business applications and systems.

These risky practices illustrate that SecOps teams are struggling to keep up with the evolution of the digital workplace and often lack visibility into their sprawling attack surface.

---

# FUTURE DEFENSE PRIORITIES SHOW DISCONNECT

Lack of visibility, the inefficiency of manual tasks, and cumbersome or false alerts are recognized problems in cybersecurity. Survey participants overwhelmingly agree that better visibility of malware-exfiltrated data, along with automated remediation workflows, would improve their ability to combat ransomware and improve overall security posture (Figure 14).

### VISIBILITY & REMEDIATION OF MALWARE-EXFILTRATED DATA AS KEY TO COMBATING MALWARE

- Strongly agree: 51%
- Somewhat agree: 47%
- Somewhat disagree: 1%
- Strongly disagree: 1%

**98% OF RESPONDENTS AGREE THAT BETTER VISIBILITY INTO MALWARE-EXFILTRATED DATA AND AUTOMATED REMEDIATION WORKFLOWS WOULD IMPROVE THEIR OVERALL SECURITY POSTURE**

This sentiment, however, contradicts respondents’ views on the importance of session cookies, which they ranked in their bottom three countermeasures, as noted earlier. It also doesn’t align with reported authentication practices that are in place: automated workflows to remediate compromised session cookies/tokens and automated workflows to remediate exposed passwords are among the bottom three authentication practices that organizations are currently using (Figure 15). However, it’s clear that this is an area of increasing focus, as automation for remediating those two threats is at the top of priorities for the next 12 months.

### AUTHENTICATION PRACTICES IN USE OR PLANNED FOR IMPLEMENTATION/UPGRADE

| Authentication Practice                                     | Already in Good Shape | Plan to Upgrade or Add |
| :---------------------------------------------------------- | :-------------------- | :--------------------- |
| Password complexity requirements                            | 64%                   | 35%                    |
| Monitoring for exposed employee passwords                   | 59%                   | 39%                    |
| Banned password list (e.g., 123password)                    | 57%                   | 39%                    |
| Single sign-on                                              | 54%                   | 38%                    |
| Password manager solutions                                  | 53%                   | 43%                    |
| Passwordless authentication solutions (biometrics, passkeys) | 48%                   | 46%                    |
| Monitoring for exposed contractor, partner, and supplier passwords | 46%                   | 53%                    |
| Monitoring for stolen partner and supplier session cookies / tokens | 41%                   | 58%                    |
| Other authentication solutions                              | 40%                   | 59%                    |
| Monitoring for stolen employee session cookies/tokens       | 39%                   | 60%                    |
| Automated workflows to remediate compromised session cookies / tokens | 37%                   | 63%                    |
| Automated workflows to remediate exposed passwords          | 35%                   | 55%                    |
| Hard tokens for MFA                                         | 34%                   | 35%                    |

However troubling the disconnect, these findings are consistent with those from SpyCloud’s malware defense survey, in which 98% of security professionals also agreed that better visibility into business applications exposed by an infostealer infection would increase security posture. This lack of visibility hinders progress in the fight against ransomware, and SecOps teams have to figure out this problem in order to effectively reduce the risk of malware exposure.

---

# All Eyes on Prevention and Automation

Proactive prevention is just as important as strengthening defenses and response capabilities, and our respondents agreed when asked to pick their top three defense priorities. Improving ransomware prevention capabilities is the top priority for organizations in the next 12 months, followed by improving ransomware detection capabilities and automating security processes and workflows (Figure 16).

### TOP SECURITY PRIORITIES

- Improving ransomware prevention capabilities: 60%
- Improving ransomware detection capabilities: 44%
- Automating security processes and workflows: 41%
- Improving ransomware response capabilities: 34%
- Better ensuring the security of third-party connections and services: 30%
- Improving security hygiene practices: 25%
- Improving visibility and remediation for exposed credentials and malware-exfiltrated data: 19%
- Increasing the size / staffing of the security operations team: 18%
- Updating incident response plans