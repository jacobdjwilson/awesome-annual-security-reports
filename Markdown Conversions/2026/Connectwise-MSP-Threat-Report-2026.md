# 2026 MSP Threat Report

## Table of Contents
- [Foreword](#foreword)
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [The 2025 Threat Landscape](#the-2025-threat-landscape)
- [Ransomware in 2025: A Shift in Frequency and Strategy](#ransomware-in-2025-a-shift-in-frequency-and-strategy)
- [Software Supply Chain Attacks](#software-supply-chain-attacks)
- [Potentially Unwanted Programs Trojanized for Higher Impact](#potentially-unwanted-programs-trojanized-for-higher-impact)
- [SSL VPN Compromises](#ssl-vpn-compromises)
- [The Continued Rise of ClickFix in 2025](#the-continued-rise-of-clickfix-in-2025)
- [AI Cybersecurity Threats](#ai-cybersecurity-threats)
- [From Insights to Action: How ConnectWise Can Help](#from-insights-to-action-how-connectwise-can-help)
- [Methodology: How We Build This Report](#methodology-how-we-build-this-report)

---

## Foreword

The most damaging incidents in 2025 didn’t rely on novel exploits or advanced malware. Instead, attackers succeeded by abusing trust.

Attackers consistently exploited identities that were assumed to be legitimate, software that was assumed to be safe, automation that was assumed to be reliable, and users who believed they were following normal instructions. These attacks did not break systems; they blended into them.

For managed service providers (MSPs), this represents a fundamental shift in the nature of risk. MSPs are no longer defending isolated endpoints or individual networks. They are defending interconnected ecosystems where access, updates, tooling, and users are deeply interdependent. When trust fails at any point in that ecosystem, the consequences extend quickly across clients, vendors, and shared infrastructure.

The MSPs that succeed in the years ahead will be those that move beyond reactive security models and rethink how trust is granted, monitored, and enforced across the environments they manage.

**Patrick Beggs**
Chief Information Security Officer, ConnectWise

---

## Introduction

The 2026 MSP Threat Report analyzes the most significant threats observed throughout 2025, drawing from real-world incident response investigations, ConnectWise partner intelligence, and industry research. The findings focus specifically on attack patterns that materially impacted MSP-managed environments and the small and midsized businesses (SMBs) they support.

Rather than cataloging every emerging tactic or malware family, this report concentrates on how attackers consistently gained access, why defenses failed, and what those failures reveal about modern MSP environments. Across investigations, adversaries favored techniques that were reliable and repeatable.

Each section of this report examines a major threat category observed in 2025 and the growing influence of artificial intelligence on threats and attacks. We analyze real incidents and translate those findings into actionable guidance to strengthen defenses in the year ahead.

---

## Key Findings

- **Initial access was rarely sophisticated, but it was highly effective**: Most successful intrusions began with credential abuse, misconfigured VPN infrastructure, or user-initiated execution. Attackers did not need zero-day exploits when valid access paths already existed.
- **Trust was the primary attack surface**: Adversaries repeatedly abused trusted identities, software updates, system utilities, and user behavior. Security controls that assumed trust rather than verifying it were routinely bypassed.
- **Ransomware surged to record levels with faster, more disruptive attacks**: Ransomware activity intensified in Q4 2025. Groups such as Akira moved rapidly from access to impact, targeting backup infrastructure, harvesting credentials, and exfiltrating data before defenders could respond.
- **Software supply chains amplified blast radius**: Compromises of upstream packages, installers, and update mechanisms allowed single intrusions to cascade across thousands of downstream environments, often without immediate detection.
- **User-mediated execution became a dominant technique**: Techniques such as ClickFix demonstrated that convincing users to manually execute commands is one of the most reliable ways to bypass traditional endpoint and email defenses.
- **Reactive security models consistently failed MSP environments**: Detection after execution was often too late. Environments with limited identity monitoring, weak application controls, or poor visibility into execution context suffered the greatest impact.
- **AI increased attacker scale, not visibility**: While AI’s role is often invisible in incident telemetry, its impact was evident in phishing quality, fraud realism, malware iteration speed, and operational efficiency.

---

## The 2025 Threat Landscape

The cyberthreat landscape facing MSPs and their clients intensified throughout 2025, driven by a sharp increase in ransomware activity and a broader shift in how attackers achieve scale and impact. 

### Key Drivers:
- **Supply chain attacks**: Targeted public package registries, maintainer accounts, and CI/CD pipelines.
- **User-driven attacks**: ClickFix surged in frequency, persuading users to run commands manually.
- **VPN abuse**: Remained a primary intrusion vector due to weak credential hygiene and legacy MFA implementations.
- **AI integration**: Lowered the barrier to entry for attackers while increasing operational scale and precision.

---

## Ransomware in 2025: A Shift in Frequency and Strategy

Ransomware victim counts surged sharply in 2025, with one security firm observing a 58% year-over-year increase.

### Akira Ransomware
Akira was one of the most disruptive threats, focusing on SMBs.
- **MFA Bypass**: Affiliates logged into SonicWall SSL VPN accounts even when OTP-based MFA was enabled, likely using stolen OTP seeds.
- **BYOVD (Bring Your Own Vulnerable Driver)**: Used to disable endpoint protection services prior to exfiltration and encryption.

---

## Software Supply Chain Attacks

Modern software development relies on the reuse of trusted components. Attackers target these upstream sources to distribute malicious, signed updates.

- **npm (Shai-Hulud 2.0)**: An aggressive campaign that leveraged automation to propagate across thousands of packages.
- **PyPI**: Continued to see phishing attempts targeting maintainer credentials.
- **NuGet**: Recurring waves of supply chain abuse via typosquatting and malicious MSBuild targets.
- **Rust**: Malicious crates (`faster_log` and `async_println`) were used to exfiltrate crypto wallet keys.

---

## Potentially Unwanted Programs Trojanized for Higher Impact

PUPs are no longer just "endpoint clutter." In 2025, they were weaponized for persistence and credential theft.

- **TamperedChef**: A campaign distributing trojanized apps (PDF editors, recipe searchers) that enrolled devices as residential proxies and harvested browser data.

---

## SSL VPN Compromises

SSL VPNs are often treated as "set it and forget it" infrastructure.
- **Ivanti (Pulse Connect Secure)**: Exploitation of CVE-2025-0282 allowed unauthorized access without credentials.
- **SonicWall**: Inherited credentials from older hardware migrations allowed attackers to bypass MFA.
- **Cisco ASA**: Zero-day exploits (CVE-2025-20362 and CVE-2025-20333) were used to implant persistent malware.

---

## The Continued Rise of ClickFix in 2025

ClickFix manipulates users into manually executing attacker-provided commands.
- **Evolution**: Moved from simple browser verification lures to complex BSOD-themed prompts and OAuth consent abuse.
- **Operational Maturity**: Attackers used URL shorteners and redirect services to abstract infrastructure, making the same lure effective even as backend payloads changed.

---

## AI Cybersecurity Threats

AI's influence is often hidden, but its impact on attacker efficiency is undeniable.
- **Deepfake Fraud**: Real-time face-swapping and voice cloning used to authorize fraudulent wire transfers.
- **AI-Generated Phishing**: Use of LLMs to create SVG files that bypass email security filters.
- **Man-in-the-Prompt (MitP)**: Malicious browser extensions intercepting and manipulating prompts in AI tools like ChatGPT and Gemini.
- **AI-Assisted Malware**: Emergence of tools like PROMPTFLUX that generate malicious scripts on demand.

---

## From Insights to Action: How ConnectWise Can Help

ConnectWise provides integrated solutions to enforce the principle of least privilege and ensure rapid recovery:
- **Privileged Access Management**: Enforces least-privileged access and audits administrative sessions.
- **ConnectWise SIEM™**: Aggregates and correlates telemetry to identify abnormal patterns.
- **ConnectWise MDR™**: Provides continuous monitoring and expert-led response.
- **x360Recover**: Provides immutable backups to resist tampering.

---

## Methodology: How We Build This Report

![Methodology description: This report is based on real-world incident response investigations, ConnectWise partner intelligence, and industry research conducted throughout 2025.]

---
<< [BACK TO TABLE OF CONTENTS](#table-of-contents)

---

enabling rapid recovery,

systems, endpoints, network devices, and cloud platforms.

x360Recover ensures MSPs can restore systems confidently

Without centralized visibility, these signals are easy to miss.

when preventative and detective controls are bypassed.

25

<< BACK TO TABLE OF CONTENTS

2026 MSP THREAT REPORTMethodology: How We Build This Report

The ConnectWise MSP Threat Report was first introduced in 2020 to provide MSPs with practical, real-world insight into the

evolving cybersecurity landscape. The report highlights the threats, attack patterns, mitigations, and solutions most relevant to

environments MSPs manage every day.

Our annual MSP Threat Report is made possible by the research and findings from the ConnectWise Cyber Research Unit™ (CRU).

This elite team is composed of experienced threat hunters and cybersecurity professionals with deep expertise in engineering,

IT admin, security operations, incident analysis, and incident response. The team gathers threat intelligence 24/7 from a wide

range of sources, including real-world incident response investigations, telemetry from ConnectWise partner and SMB client

environments, ransomware leak sites, and malicious infrastructure such as botnets and command-and-control networks. By

correlating these data points, the CRU identifies emerging trends, common attack techniques, and recurring points of failure

across MSP-managed environments.

The goal of this report is not simply to document threats, but to translate complex threat intelligence into actionable insight

for MSPs.

About ConnectWise

ConnectWise powers IT businesses by simplifying operations, enhancing experiences, and driving growth. Trusted by IT solution

providers worldwide, ConnectWise sets the standard for innovation and service delivery. For more than 40 years, ConnectWise

has been committed to partner success, delivering software, services, and an open ecosystem of integrations. The ConnectWise

Platform provides unmatched scale and AI-driven automation across PSA, RMM, cybersecurity, and data protection, helping our

partners deliver and secure services more efficiently. Discover how ConnectWise is transforming the IT industry at connectwise.com.

26

<< BACK TO TABLE OF CONTENTS

connectwise.com

2026 MSP THREAT REPORT