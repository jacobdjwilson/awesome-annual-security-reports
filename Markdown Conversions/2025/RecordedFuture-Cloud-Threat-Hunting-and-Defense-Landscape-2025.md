# CYBER THREAT ANALYSIS

By _Insikt Group_®
August 4, 2025

Cloud Threat Hunting
and Defense Landscape

As organizations increasingly adopt cloud infrastructure, they encounter novel and unique security challenges that threat actors are actively exploiting.

Threat actors targeting cloud environments rely mainly on exploiting misconfigurations and employing coercion tactics for initial access.

Vulnerability and misconfiguration scanning campaigns, alongside initial access brokers, represent the primary means by which threat actors obtain cloud credentials.

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Introduction](#introduction)
- [Background](#background)
- [Methodology](#methodology)
- [Threats To Cloud Environments](#threats-to-cloud-environments)
  - [Cloud Abuse](#cloud-abuse)
    - [Key Takeaways](#key-takeaways)
    - [Cost of Impact: 4 (High)](#cost-of-impact-4-high)
    - [Commonality: 4 (High)](#commonality-4-high)
    - [Evolution Potential: 4 (High)](#evolution-potential-4-high)
    - [Effort to Perform: 3 (Moderate)](#effort-to-perform-3-moderate)
    - [Threat Summary](#threat-summary)
    - [Outlook](#outlook)
    - [Mitigations and Detections](#mitigations-and-detections)
    - [Examples In the Wild](#examples-in-the-wild)
  - [Exploitation](#exploitation)
    - [Key Takeaways](#key-takeaways-1)
    - [Cost of Impact: 3 (Moderate)](#cost-of-impact-3-moderate)
    - [Commonality: 2 (Low)](#commonality-2-low)
    - [Evolution Potential: 4 (High)](#evolution-potential-4-high-1)
    - [Effort to Perform: 4 (High)](#effort-to-perform-4-high)
    - [Threat Summary](#threat-summary-1)
    - [Outlook](#outlook-1)
    - [Mitigations and Detections](#mitigations-and-detections-1)
    - [Examples in the Wild](#examples-in-the-wild-1)
  - [Endpoint Misconfiguration](#endpoint-misconfiguration)
    - [Key Takeaways](#key-takeaways-2)
    - [Cost of Impact: 3 (Moderate)](#cost-of-impact-3-moderate-1)
    - [Commonality: 5 (Severe)](#commonality-5-severe)
    - [Evolution Potential: 1 (Minimal)](#evolution-potential-1-minimal)
    - [Effort to Perform: 1 (Minimal)](#effort-to-perform-1-minimal)
    - [Threat Summary](#threat-summary-2)
    - [Outlook](#outlook-2)
    - [Mitigations and Detections](#mitigations-and-detections-2)
    - [Examples in the Wild](#examples-in-the-wild-2)
  - [Cloud Ransomware](#cloud-ransomware)
    - [Key Takeaways](#key-takeaways-3)
    - [Cost of Impact: 5 (Severe)](#cost-of-impact-5-severe)
    - [Commonality: 3 (Moderate)](#commonality-3-moderate)
    - [Evolution Potential: 3 (Moderate)](#evolution-potential-3-moderate)
    - [Effort to Perform: 4 (High)](#effort-to-perform-4-high-1)
    - [Threat Summary](#threat-summary-3)
    - [Outlook](#outlook-3)
    - [Mitigations and Detections](#mitigations-and-detections-3)
    - [Examples in the Wild](#examples-in-the-wild-3)
  - [Credential Abuse and Account Takeover](#credential-abuse-and-account-takeover)
    - [Key Takeaways](#key-takeaways-4)
    - [Cost of Impact: 4 (High)](#cost-of-impact-4-high-1)
    - [Commonality: 4 (High)](#commonality-4-high-1)
    - [Evolution Potential: 2 (Low)](#evolution-potential-2-low)
    - [Effort to Perform: 2 (Low)](#effort-to-perform-2-low)
    - [Threat Summary](#threat-summary-4)
    - [Outlook](#outlook-4)
    - [Mitigations and Detections](#mitigations-and-detections-4)
    - [Examples in the Wild](#examples-in-the-wild-4)
- [General Mitigations](#general-mitigations)
- [Outlook](#outlook-5)
- [About Insikt Group®](#about-insikt-group)
- [About Recorded Future®](#about-recorded-future)

## Executive Summary

In a review of recently observed attack methods, _Insikt Group_ identified five attack vectors that currently pose the greatest potential threat to cloud environments. Three of these attack methods, vulnerability exploitation, endpoint misconfiguration, and credential abuse leading to account takeover, can grant threat actors initial access. In certain circumstances, these three attack methods can also be employed following initial access to gain increased permissions within a cloud environment, modify the cloud environment, and allow lateral movement, either to additional cloud environments, traditional on-premise environments, or user devices. The two remaining attack methods, cloud abuse and cloud ransomware, demonstrate impact actions threat actors can perform within a cloud environment.

Hunting for each of these threats often requires the implementation of robust logging within cloud environments to ensure that data such as network communications, user access, and cloud service usage metrics can be readily accessed and scrutinized for aberrations. Log data assists in both proactive discovery of suspicious activity originating at the edge of cloud environments, such as in instances where misconfiguration and vulnerability scanning occur, and in identifying instances where cloud accounts and resources are abused for malicious purposes.

To mitigate threats from impacting cloud environments, proper configuration of the environment is paramount, both at the edge of the cloud environment, including the methods by which users and services interact with the environment, and within the environment itself. Cloud environments that are configured appropriately minimize the risk of initial access and can significantly limit the malicious actions a threat actor is capable of performing post-initial access. Additionally, the most common cloud platforms provide native services focused on security for cloud environments, such as web application firewalls (WAF), identity and access management (IAM) services, secrets storage and management suites, and secure data connectors for hybridized cloud environments, that allow cloud architects to mitigate the threats discussed in this report with relative ease.

[^1]: CTA-2025-0804

## Key Findings

- Most initial compromises start with exposed or misconfigured cloud endpoints, with attackers using open-source scanners to identify misconfigured endpoints.
- Stolen or weak credentials, often gathered from initial access brokers (IABs) and previous malicious actions performed by the attacker, remain the fastest path to full-tenant cloud takeover.
- Threat actors increasingly abuse legitimate SaaS and IaaS resources, shifting costs to the owners of victimized environments and abusing resources to complicate the detection of follow-on malicious actions, such as phishing campaigns.
- Ransomware groups have adopted cloud-native tactics, encrypting S3 and Azure storage directly and disabling backups to maximize leverage.
- Hybrid infrastructure lets attackers pivot seamlessly between on-premise and multi-cloud environments, so visibility and controls must extend beyond the cloud environment to the devices and services that access it.

## Introduction

During the past decade, a steady shift from traditional on-premise IT infrastructure to cloud-based infrastructure and hybrid cloud infrastructure has taken place. According to _PwC_'s 2023 _Cloud Business Survey_, 39% of private respondents stated that the entirety of their operations had been moved to cloud environments. Cloud computing has become a trusted and integral part of many corporations' day-to-day operations. Since the time of _PwC_'s reporting, cloud computing as an industry has only grown with no signs of slowing.

The breadth of cloud products and the depth of services provided by cloud environments continue to grow daily. In a joint study conducted by _Amazon_ and _Telecom Advisory Services_, cloud adoption accounted for a total of $1 trillion in the global gross domestic product, with a projected increase to $12 trillion between 2024 and 2030. This estimate indicates that traditional computing environments will continue to migrate to cloud environments rapidly in the coming years. That demand for cloud computing resources will continue to increase for the foreseeable future.

The success of cloud computing can be squarely attributed to the benefits that adopters are provided. When properly configured, cloud environments allow their adopters to shift costs associated with traditional on-premise environments, create high-availability to remote assets, and eliminate development overhead by gaining access to managed services. As cloud providers continue to offer additional services and products that make similar offerings for traditional environments less effective from cost and operational perspectives, cloud adoption will only continue to grow in the future.

## Background

Cloud technologies, platforms, and services are increasingly implemented into corporate structures, providing all of the benefits of traditional on-premise environments while reducing costs associated with an on-premise environment in nearly every conceivable way. This relationship was demonstrated in _PwC_'s "_2024 Cloud and AI Business Survey_," which reported that, out of a survey of 1,000 companies that implemented cloud technologies, 74% of the surveyed companies that have optimized their cloud environments reported increased profitability, and 65% of the same respondents reported increased cost savings. While these benefits are highly appealing to corporations, cloud environments pose unique risks and security challenges, challenges that require a fresh approach to cybersecurity to mitigate properly.

The advancement of cloud environments has also increased the number of network-accessible endpoints that an organization must monitor and defend. In instances where large enterprise entities have fully migrated their operations to cloud environments, the endpoints required to facilitate user access, deploy web applications, support data transfer, and provide many other kinds of access on a day-to-day basis add up quickly and create a diverse boundary that is constantly interacting with the broader internet. The technologies that interface with and are embedded within this boundary pose unique risks and security challenges. Looking inward, similar issues persist, with cloud defenders requiring a fresh understanding of how cloud environments can be effectively architected to provide the benefits of a cloud environment without allowing undue access to sensitive information and control over mission-critical assets hosted in these environments.

As _Insikt Group_ discusses in this report, threat actors have become increasingly aware of the security challenges cloud defenders must address, as well as the opportunities that cloud technologies, environments, and services afford them. The overwhelming amount of data, applications, systems, and other assets hosted on cloud environments, coupled with the task of defending these assets, provides threat actors with novel opportunities to compromise information, abuse environment resources, and profit from illicit activities in ways previously unattainable in on-premise environments. Additionally, threat actors have begun to understand the usefulness of cloud resources as part of an attack chain, realizing they are afforded all of the same benefits of legitimate cloud users, with the added benefits of anonymity and reduced detection capabilities in a way that is unobtainable with traditional infrastructure.

Understanding the threat posed by these adversaries, this report was created to shed light on the most impactful and emerging tactics, techniques, and procedures (TTPs) displayed by threat actors that target and abuse cloud environments. In doing so, it aims to provide an understanding of how threat actors are impacting and abusing cloud environments at a granular level, as well as how to mitigate these threats and hunt for indicators of compromise associated with them so that cloud defenders are better able to identify and respond when necessary.

## Methodology

This report identified