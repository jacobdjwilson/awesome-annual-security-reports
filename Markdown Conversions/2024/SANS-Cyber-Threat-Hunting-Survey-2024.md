# SANS 2024 Threat Hunting Survey: Hunting for Normal Within Chaos

## Table of Contents
- [Executive Summary/Introduction](#executive-summaryintroduction)
- [Participants/Demographics](#participantsdemographics)
- [How We Hunt and What We Find](#how-we-hunt-and-what-we-find)
- [Tactics, Techniques, and Procedures (TTPs) for the Attack Schema](#tactics-techniques-and-procedures-ttps-for-the-attack-schema)
- [Charting the Shifting Sands of Cyber Threats](#charting-the-shifting-sands-of-cyber-threats)
- [Structured Tracking of the Threat Landscape](#structured-tracking-of-the-threat-landscape)
- [The Vendors’ Threat Landscape](#the-vendors-threat-landscape)
- [Are Hunters Using a Methodology or Being Given a Policy?](#are-hunters-using-a-methodology-or-being-given-a-policy)
- [Building the Methodology](#building-the-methodology)
- [Methodology Selection](#methodology-selection)
- [Do Organizations Still Want to Employ Threat Hunters?](#do-organizations-still-want-to-employ-threat-hunters)
- [Hunting for an Impact Within Your Organization](#hunting-for-an-impact-within-your-organization)
- [Conclusion](#conclusion)
- [Product Briefing: Threat Hunting with Splunk](#product-briefing-threat-hunting-with-splunk)

---

## Executive Summary/Introduction

This is SANS’s ninth year of conducting our annual Threat Hunting Survey. As authors who also work in the field of threat hunting and incident response, we interpret raw data from respondents to provide guidance for those trying to mature their methodologies.

Key findings include:
- Half of organizations now have formally defined threat hunting methodologies (up from 35% in 2023).
- Lack of skilled staff remains the top barrier (50%), followed by data quality issues and tool limitations.
- 37% of organizations outsource their threat hunting.
- 64% of organizations formally measure the success of their efforts (up from 34% in 2023).
- Business email compromise (BEC) is the most common threat actor caught (68%).

## Participants/Demographics

![Demographics of Survey Respondents: Gear and building icons representing industry and size, and person icons representing roles.]

The survey covers a broad spread of industries, with Cybersecurity (15%) leading. Organization sizes range from fewer than 100 employees to more than 100,000. 65% of respondents are headquartered in the United States.

![Respondents’ Primary Industry chart]
![Respondents’ Organization Size chart]
![Respondents’ Corporate Headquarters chart]

## How We Hunt and What We Find

Most threat hunting operations today are intelligence-based. We asked what attackers respondents are facing:
- Business email compromise (BEC): 68%
- Ransomware: 64%
- Nation-states: 38%

![Most Common Types of Attackers chart]

## Tactics, Techniques, and Procedures (TTPs) for the Attack Schema

For ransomware, the top TTP is "custom malware" (61%), followed by "targeted exfiltration" (56%). For nation-state attacks, "living off the land" is the leading TTP (76%).

![Ransomware Techniques chart]
![Nation-State Attacker Techniques chart]

## Charting the Shifting Sands of Cyber Threats

Organizations stay updated via:
- Vendor blogs/papers: 59%
- Independent blogs/papers: 59%
- Commercial intelligence providers: 55%
- Own research: 50%

![Sources for the Latest Attack Techniques chart]

## Structured Tracking of the Threat Landscape

61% of respondents have a formal program to track changes in the threat landscape. The dominant method for monitoring is using open-source intelligence (OSINT) tools (70%).

## The Vendors’ Threat Landscape

Most organizations consume EDR/XDR vendor intelligence, with 47% using it in combination with their own intelligence, 14% depending on it entirely, and 30% using it as a fallback.

## Are Hunters Using a Methodology or Being Given a Policy?

51% of organizations report having formally defined threat hunting methodologies. There is a trend toward more regular, scheduled reviews (monthly or quarterly) rather than ad hoc changes.

![Use of Threat Hunting Methodologies chart]
![Frequency of Reviewing/Changing Methodologies chart]

## Building the Methodology

The CISO is the primary contributor to methodology development (40%), followed by external entities (35%) and incident response teams (33%).

## Methodology Selection

47% of organizations report that available human resources influence the selection of methodologies, reflecting a pragmatic adaptation to the skills gap.

![The Relationship Between Methodologies and Staffing chart]

## Do Organizations Still Want to Employ Threat Hunters?

37% of organizations outsource their threat hunting. While outsourcing provides access to external expertise, it can create challenges regarding data governance, continuity, and a disconnect from the organization's unique business context.

![Threat Hunting Maturity chart]
![Outsourcing of Threat Hunting chart]

## Hunting for an Impact Within Your Organization

64% of organizations now formally measure the success of their threat hunting. 63% report measurable improvements in their security posture, particularly in hardening network/endpoints and creating more accurate detections.

![Formal Measurement of Threat Hunting Efforts chart]
![Improvements Resulting from Threat Hunting chart]

## Conclusion

The 2024 survey reveals a cybersecurity landscape in transition. Organizations are committing to significant investments in both human and technological capital, with a focus on AI integration and better data management to overcome the persistent challenge of the skilled staff gap.

## Product Briefing: Threat Hunting with Splunk

Splunk offers a comprehensive data platform for end-to-end threat visibility. To address the skills gap, Splunk’s SURGe security research team developed the PEAK Threat Hunting Framework, which includes the Hunting Maturity Model (HMM). This allows organizations to determine their current capabilities and advance their security maturity through iterative, data-driven processes.

![The Hunting Maturity Model (HMM) diagram]
![Splunk’s Operationalized Data Science Pipeline diagram]

[^1]: SANS 2024 Threat Hunting Survey: Hunting for Normal Within Chaos, March 2024.