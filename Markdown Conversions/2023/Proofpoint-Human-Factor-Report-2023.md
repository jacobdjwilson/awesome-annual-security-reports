# The Human Factor 2023

Analyzing the cyber attack chain

[proofpoint.com](https://proofpoint.com)

REPORT

## Table of Contents
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [About This Report](#about-this-report)
- [The Threat Landscape](#the-threat-landscape)
- [Identity Crisis](#identity-crisis)
- [APT Spotlight](#apt-spotlight)
- [New Developments](#new-developments)
- [Spotlight on SocGholish](#spotlight-on-socgholish)
- [Chatting with Attackers](#chatting-with-attackers)
- [Spotlight on Emotet](#spotlight-on-emotet)
- [Opportunistic Attacks](#opportunistic-attacks)
- [A Dark Cloud](#a-dark-cloud)
- [Conclusions](#conclusions)

---

## Introduction

After two years of pandemic-induced disruption, 2022 felt like a return to business as usual for many. And that certainly seems to have been the case for the world’s cyber criminals. As COVID-19 medical and economic programs began to wind down, attackers had to get back to making a living the old-fashioned way: by honing their social engineering skills, enhancing their tooling, and looking for opportunity in unexpected places.

All of this has led to an explosion in ingenuity. From the commoditization of sophisticated techniques like multifactor authentication bypass to threats that rely solely on the attacker’s charm and persuasiveness, the cyber attack chain—and the landscape as a whole—has seen major development on several fronts. And with Microsoft’s moves to curtail abuse of Office macros creating unignorable pressure to innovate, many threat actors are still experimenting to figure out what comes next.

But no matter which tactics or techniques attackers turn to, their victims remain stubbornly human. Cyber attackers target people. They exploit people. Ultimately, they are people. That’s what makes protecting people from cyber threats such a profound and fascinating challenge.

---

## Key Findings

- **13 million**: TOAD messages peaked at more than 13 million per month.
- **94%**: of cloud tenants were targeted every month.
- **x12**: Conversational attacks via mobile devices grew twelvefold.
- **25 million**: Emotet topped the charts again, sending over 25 million messages.
- **Top 5**: Novel distribution pushed SocGholish into the top-five ranking for malware (by message volume).
- **Office macro use**: Collapsed after Microsoft rolled out controls to block them.
- **MFA-Bypass**: Accounted for more than a million messages per month.

---

## About This Report

For more than 20 years, Proofpoint has been in the business of protecting people and defending data from cyber attacks. In that time, our research has consistently led us toward a simple but powerful observation: people—not technology—are the most critical variable in today’s cyber threats.

This year, Human Factor report takes an even closer look at new developments in the threat landscape, focusing on the combination of technology and psychology that makes modern cyber attacks so dangerous.

### What this report covers
This report covers threats detected, mitigated and resolved during 2022 among Proofpoint deployments around the world: one of the largest, most diverse data sets in cybersecurity.

We largely focus on threats that are part of a broader attack campaign, or series of actions taken by an attacker to accomplish a goal. Sometimes, we’re able to link these campaigns to a specific threat actor, a process known as attribution.

### Scope
The data in this report draws on the Proofpoint Nexus Threat Graph, using data collected from Proofpoint deployments around the globe. Each day, we analyze more than 2.6 billion email messages, 49 billion URLs, 1.9 billion attachments, 28 million cloud accounts, 1.7 billion suspicious SMS and more. Together, this amounts to trillions of data points across the digital channels that matter.

This report covers Jan. 1–Dec. 31, 2022. Where specific campaigns are discussed, this is the result of direct observation by our global network of threat researchers. Campaigns are defined as a series of common actions taken by a single attacker to accomplish a goal.

---

## The Threat Landscape

The more things change, the more they stay the same. In some respects, 2022 saw a lot of development in the threat landscape. Attack chains became more varied. Delivery mechanisms were rapidly tested and discarded. And threat actors began to match their ingenuity with new-found patience.

### Leaders and losers
Despite an erratic year, TA542, the entity behind Emotet, regained its place as the world’s most prolific threat actor. Its return to the top comes only a year after law enforcement took the botnet offline in January 2021.

![Chart showing Threat Actors by Message Volume: TA542, TA569, TA2725, TA577, TA2536, TA544, TA570, TA578, TA5453, TA579]

### Linked or attached?
The split between URLs and attachments for threat delivery also remained consistent year on year. While there were a few periods when trends grew close, URLs accounted for around three quarters of all threats overall.

### Top malware
With TA542 the leading threat actor by volume, it will come as no surprise to see Emotet at the top of the malware chart. Commodity malware used by a range of threat actors occupies three of the other four places (FormBook, Netsupport and AgentTesla). But the rise of SocGholish is noteworthy.

### Top lures
Abusing our familiarity and trust in major brands is one of the simplest forms of social engineering. Microsoft products and services occupied four of the top five positions for abused brands across all threats, with Amazon taking the other spot.

### Top techniques
Among the many attacks we classified, the vast majority relied on some element of psychological manipulation.

---

## Identity Crisis

Whether their chosen mode is phishing or malware distribution, attackers invest a lot of effort into gaining access to corporate credentials and devices. So it’s worth spending a moment to consider why this access is so highly prized.

User credentials are analogous to identity. Once your login and password are compromised, an attacker effectively becomes you as far as the systems you have access to are concerned. 

- **1 in 6**: Endpoints contain risk.

---

## APT Spotlight

As the lure themes mentioned in the last section show, financial motives dominate the threat landscape. So much so, that only a tiny fraction of our customers are targeted by state-sponsored APT actors.

- **TA416**: An APT actor aligned with the Chinese state, was one of the most active.
- **TA453**: Believed to be aligned with the Islamic Revolutionary Guard Corps of Iran, typically targets academic, dissidents, journalists and other figures of political influence.

---

## New Developments

Over the course of 2022, several technical and tactical innovations grew to become ubiquitous in the threat landscape.

### MFA bypass
In 2022, phish kits gained a powerful new capability: bypassing MFA. In the fourth quarter of the year, we gained visibility into attacks using three prominent MFA bypass frameworks: EvilProxy, Evilginx2 and NakedPages.

### Attack of the TOADs
Last year we reported on an increase in telephone-oriented attack delivery (TOAD), a novel technique involving a high degree of interaction between victim and attacker. We now detect and mitigate millions of TOAD messages per month.

### Forced evolution
Over the course of 2022, Microsoft made changes to how its productivity suite treats files downloaded from the internet, making it much harder for cyber criminals to deliver malware through Office documents. Volumes of messages containing Office macros fell sharply.

---

## Spotlight on SocGholish

One of the year’s standout threats appeared in the form of SocGholish, a malware exclusively delivered by cyber criminal group TA569.

### The attack chain
Unlike most of the malware discussed in this report, SocGholish isn’t delivered directly to victims in the form of an emailed URL or attachment. In fact, most emails flagged as SocGholish by our systems come from legitimate senders. Instead, SocGholish is a “drive-by” malware, which sits on infected websites and tricks victims into downloading it with fake browser update alerts.

---

## Chatting with Attackers

Conversational attacks have been a part of the threat landscape for a while. But over the course of the year, our data reveals a significant increase in the number of conversational attacks from financially motivated actors.

- **$2.5B**: Losses due to cryptocurrency scams in 2022.
- **$2.7B**: In BEC losses to U.S. companies.

---

## Spotlight on Emotet

In January 2021, law enforcement shut down the Emotet botnet. Last November Emotet blinked back into life and began sending out new campaigns. Despite a fitful pattern, TA542, the group behind Emotet, still sent more malicious email last year than any other threat actor we track.

---

## Opportunistic Attacks

Timeliness is key consideration in social engineering. Lures that refer to recent events or time-sensitive decisions can cause victims to skip some of the scrutiny they might otherwise apply.

- **Russia-Ukraine**: Within days of the invasion, our researchers identified a likely state-sponsored phishing attack using compromised Ukrainian armed service credentials.
- **Queen Elizabeth II**: In September, the death of Queen Elizabeth II led one threat actor to spin up an unusual phishing campaign.
- **Silicon Valley Bank**: Within hours of U.S. authorities taking control of the ailing bank in March, our researchers saw dozens of lookalike and typosquatting domains being registered.

---

## A Dark Cloud

Last year we reported on how the ubiquity of cloud infrastructure led to a noteworthy rise in the number of threats faced by cloud tenants. This year, that trend has continued to the point where it is now cloud threats themselves that have become truly ubiquitous.

- **62%**: Of targeted cloud tenants were successfully compromised.
- **400%**: The average monthly volume of brute-force attacks rose in early 2023 vs. the 2022 monthly average.

---

## Conclusions

No matter where attackers look next for inspiration, a people-centric approach to prevention is the key to defending against future threats. Users who are trained to expect the unexpected will be primed to spot a threat and break the attack chain.

1. **Build a robust email fraud defense.**
2. **Protect cloud accounts from takeover and malicious apps.**
3. **Partner with a threat intelligence vendor.**

---

### Footnotes
[^1]: FBI. “Internet Crime Report 2022.” March 2023.