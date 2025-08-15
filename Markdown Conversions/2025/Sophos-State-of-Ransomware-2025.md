# THE STATE OF RANSOMWARE 2025

Findings from an independent survey of 3,400 IT and cybersecurity leaders across 17 countries whose organizations were hit by ransomware in the last year.

A Sophos Whitepaper. June 2025

## Table of Contents
- [Introduction](#introduction)
- [Key findings](#key-findings)
  - [Why organizations fall victim to ransomware (Summary)](#why-organizations-fall-victim-to-ransomware)
  - [What happens to the data (Summary)](#what-happens-to-the-data)
  - [Ransoms: Demands and payments (Summary)](#ransoms)
  - [Business impact of ransomware (Summary)](#business-consequences-of-ransomware)
  - [Human impact of ransomware (Summary)](#human-consequences-of-ransomware)
- [Why organizations fall victim to ransomware](#why-organizations-fall-victim-to-ransomware)
  - [Technical root cause of attacks](#technical-root-cause-of-attacks)
  - [Operational root cause of incidents](#operational-root-cause-of-incidents)
  - [Operational root cause by business size](#operational-root-cause-by-business-size)
  - [Operational root cause by sector](#operational-root-cause-by-sector)
- [What happens to the data](#what-happens-to-the-data)
  - [Data encryption](#data-encryption)
  - [Data theft](#data-theft)
  - [Extortion-style attacks](#extortion-style-attacks)
  - [Recovery of encrypted data](#recovery-of-encrypted-data)
- [Ransoms](#ransoms)
  - [Ransom demands](#ransom-demands)
  - [Ransom payments](#ransom-payments)
  - [How actual payments stack up with the initial demand](#how-actual-payments-stack-up-with-the-initial-demand)
  - [Why most ransom payments differ from the amount initially demanded](#why-most-ransom-payments-differ-from-the-amount-initially-demanded)
- [Business consequences of ransomware](#business-consequences-of-ransomware)
  - [Recovery costs](#recovery-costs)
  - [Recovery time](#recovery-time)
- [Human consequences of ransomware](#human-consequences-of-ransomware)
- [Recommendations](#recommendations)
- [Learn more about ransomware and how Sophos can help you defend your organization.](#learn-more-about-ransomware-and-how-sophos-can-help-you-defend-your-organization)

---

## Introduction

Welcome to the sixth edition of the annual Sophos State of Ransomware report which reveals the reality of ransomware in 2025.

This year’s report details how organizations’ experiences of ransomware — both cause and consequences — have evolved over the last 12 months. It also shines light into previously unexplored areas, including the operational factors that left organizations exposed to attack and the human impact of incidents on the IT/cybersecurity team.

Based on the real-world frontline experiences of 3,400 IT and cybersecurity leaders across 17 countries whose organizations were hit by ransomware in the last year, the report provides unique insights into:

- Why organizations fall victim to ransomware.
- What happens to the data.
- Ransoms: Demands and payments.
- Business impact of ransomware.
- Human impact of ransomware.

### A note on reporting dates

To enable easy comparison of data across our annual surveys, we name the report for the year in which the survey was conducted. In this case, 2025. We are mindful that respondents are sharing their experiences over the previous year, so many of the attacks referenced occurred in 2024.

### About the survey

The report is based on the findings from an independent, vendor-agnostic survey into organizational experiences of ransomware that was commissioned by Sophos and conducted by a third-party specialist between January and March 2025. All respondents work in organizations with between 100 and 5,000 employees and were asked to answer based on their experiences in the previous 12 months.

Participants came from 17 countries and a wide range of industries, ensuring that the survey results reflect diverse experiences across the public and private sectors. The report includes comparisons with the findings from our previous reports, enabling year-over-year comparisons. All financial data points are in U.S. dollars.

## Key findings

### Why organizations fall victim to ransomware (Summary)

- For the third year running, victims identified exploited vulnerabilities as the most common technical root cause of attack, used in 32% of incidents.
- Multiple operational factors contribute to organizations falling victim to ransomware, with the most common being a lack of expertise, named by 40.2% of victims. It is followed in very close succession by having security gaps that the organization was not aware of, which was a contributing factor in 40.1% of attacks. In third place was lack of people/capacity, which contributed to 39.4% of attacks.

### What happens to the data (Summary)

- Data encryption is at the lowest level in six years, with 50% of attacks now resulting in data encryption, down from 70% in 2024.
- 28% of organizations that had data encrypted also experienced data exfiltration.
- 97% that had data encrypted were able to recover it.
- The use of backups to restore encrypted data is at the lowest rate in six years, used just in 54% of incidents.
- 49% of victims paid the ransom to get their data back. While this represents a slight drop from last year’s 56%, it is the second highest ransom payment rate in six years.

### Ransoms: Demands and payments (Summary)

- The average (median) ransom demand has dropped by one third (34%) over the last year, coming in at $1,324,439 in 2025 compared to $2 million in 2024.
- The average (median) ransom payment has fallen by 50% in the last year, down from $2M in 2024 to $1M in 2025. The primary factor behind this drop is a reduction in the percentage of ransom payments of $5M or more, down from 31% of payments in 2024 to 20% in 2025.
- When comparing demands vs. payments, only 29% said their payment matched the initial demand. 53% paid less than the initial ask while 18% paid more.

### Business impact of ransomware (Summary)

- Excluding any ransom paid, the average cost to recover from a ransomware attack dropped by 44% over the last year, coming in at $1.53 million, down from $2.73 million in 2024.
- Looking at speed of recovery, organizations are getting faster, with 53% fully recovered after a week, up from 35% in 2024.

### Human impact of ransomware (Summary)

- Every organization that had data encrypted reported that there were direct repercussions for the IT/cybersecurity team:
  - 41% of IT/cybersecurity teams say they have increased anxiety or stress about future attacks.
  - One third (34%) said the team experienced feelings of guilt that the attack was not stopped in time.
  - 40% report increased pressure from senior leaders but 31% report increased recognition.
  - 31% of teams have experienced staff absence due to stress/mental health issues related to the attack.
  - In one quarter of cases, the team’s leadership was replaced as a consequence of the attack.

## Why organizations fall victim to ransomware

### Technical root cause of attacks

For the third year running, victims identified exploited vulnerabilities as the most common root cause of ransomware incidents, used to penetrate organizations in 32% of attacks overall.

Compromised credentials remains the second most common perceived attack vector, although the percentage of attacks that used this approach dropped from 29% in 2024 to 23% in 2025. Email remains a major vector of attack with 19% of victims reporting malicious email as the root cause and a further 18% citing phishing — a notable jump from last year’s 11%.

![Chart 1: Technical root cause of ransomware attacks 2023–2025. Bar chart showing exploited vulnerability, compromised credentials, malicious email, phishing, brute force attack, and download as root causes across 2023, 2024, and 2025. Exploited vulnerability is 32% in 2025, down from 36% in 2023. Compromised credentials is 23% in 2025, down from 29% in 2023. Malicious email is 19% in 2025. Phishing is 18% in 2025, up from 11% in 2023. Brute force attack is 3% in 2025. Download is 2% in 2025.](Chart%201%20Technical%20root%20cause%20of%20ransomware%20attacks%202023-2025.png