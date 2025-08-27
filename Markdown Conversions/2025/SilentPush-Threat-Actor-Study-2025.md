# THREAT ACTOR STUDY

## Table of Contents
- [A Year In Summary](#a-year-in-summary)
- [1 Introduction](#1-introduction)
- [2 The Ever-Evolving Threat Landscape](#2-the-ever-evolving-threat-landscape)
  - [Silent Push Key Statistics](#silent-push-key-statistics)
  - [Top Threat Trends](#top-threat-trends)
  - [RASPBERRY ROBIN](#raspberry-robin)
- [3 Advanced Persistent Threats (APTs)](#3-advanced-persistent-threats-apts)
  - [State-Sponsored APT Groups](#state-sponsored-apt-groups)
  - [APT28 (FANCY BEAR)](#apt28-fancy-bear)
  - [KIMSUKY (APT43)](#kimsuky-apt43)
  - [SAPPHIRE SLEET](#sapphire-sleet)
    - [EVASION TECHNIQUES](#evasion-techniques)
- [4 Financially-Motivated Threat Actors](#4-financially-motivated-threat-actors)
  - [FIN7](#fin7)
    - [FIN7 SHELL DOMAINS MORPHING INTO PHISHING WEBSITES](#fin7-shell-domains-morphing-into-phishing-websites)
    - [MORPHED DOMAIN (ALLIANT)](#morphed-domain-alliant)
  - [STARK INDUSTRIES & SILENT PUSH TAKEDOWNS](#stark-industries--silent-push-takedowns)
  - [THE COMM - SCATTERED SPIDER & CRYPTOCHAMELEON](#the-comm---scattered-spider--cryptochameleon)
    - [SCATTERED SPIDER](#scattered-spider)
      - [SCATTERED SPIDER ATTACK METHODOLOGY](#scattered-spider-attack-methodology)
      - [ATTACK METHODOLOGY](#attack-methodology)
      - [PHISHING PAGES](#phishing-pages)
      - [REGISTRARS AND HOSTING PROVIDERS](#registrars-and-hosting-providers)
      - [LAST QUARTER OF 2024:](#last-quarter-of-2024)
      - [REUSE OF DEDICATED SERVERS](#reuse-of-dedicated-servers)
      - [ADVANCED TOOLS - EVILGNIX](#advanced-tools---evilgnix)
      - [ADVANCED TOOLS - MALWARE](#advanced-tools---malware)
    - [CRYPTOCHAMELEON](#cryptochameleon)
      - [AS NAMES](#as-names)
      - [AS NUMBERS](#as-numbers)
  - [INVESTMENT SCAMS / PIG BUTCHERING](#investment-scams--pig-butchering)
  - [TRIAD NEXUS](#triad-nexus)
  - [FUNNULL CNAME CHAINS](#funnull-cname-chains)
  - [AIZ RETAIL & CRYPTO PHISHING NETWORK](#aiz-retail--crypto-phishing-network)
    - [TARGETED BRANDS INCLUDED:](#targeted-brands-included)
  - [JOB SCAMS & FAKE TRADING APPS](#job-scams--fake-trading-apps)
  - [VISERBANK INVESTMENT SCAMS](#viserbank-investment-scams)
  - [SMISHING TRIAD](#smishing-triad)
  - [ILLEGAL ONLINE PHARMACIES](#illegal-online-pharmacies)
  - [BAZARCALL](#bazarcall)
  - [UNDERGROUND MARKETS](#underground-markets)
- [5 Malware and Threat Actor Infrastructure Trends](#5-malware-and-threat-actor-infrastructure-trends)
  - [FIN7 MALWARE CAMPAIGNS](#fin7-malware-campaigns)
  - [MALWARE IDENTIFIED ON OPEN DIRECTORIES](#malware-identified-on-open-directories)
    - [BLACKMOON TROJAN](#blackmoon-trojan)
    - [LUMMA STEALER](#lumma-stealer)
    - [CHROME APPBOUND ENCRYPTION](#chrome-appbound-encryption)
  - [BULLETPROOF HOSTS](#bulletproof-hosts)
    - [THE RISE OF THE BULLET PROOF REGISTRAR](#the-rise-of-the-bullet-proof-registrar)
  - [BITLAUNCH](#bitlaunch)
  - [PROLIFIC PUMA](#prolific-puma)
- [6 Silent Push Highlights & App Improvements](#6-silent-push-highlights--app-improvements)
  - [CLOUDFLARE UNMASKING](#cloudflare-unmasking)
  - [NEW DATA SOURCES](#new-data-sources)
- [7 Strategic Recommendations](#7-strategic-recommendations)
  - [Utilizing Silent Push Offerings](#utilizing-silent-push-offerings)
  - [Actionable Steps For Organizations](#actionable-steps-for-organizations)
- [8 Predictions For 2025](#8-predictions-for-2025)
- [9 Pushing The Boundaries of Modern Threat Intelligence](#9-pushing-the-boundaries-of-modern-threat-intelligence)

---

## A Year In Summary

2024 marked a transformative year in cyber threat intelligence. Rapidly evolving adversary tactics, increasingly novel malware proliferation techniques, and the widespread availability of artificial intelligence (AI) enabled malicious infrastructure scaling methods have made the jobs of security teams exponentially more challenging worldwide.

Dealing with these threats thus requires a transformative approach. Reactive defense measures are no longer effective, and Indicators of Compromise (IOCs) are stale at best. The industry is turning toward Indicators of Future Attack (IOFAs) to gain actionable threat intelligence that can stop attacks before they are weaponized.

In pursuit of that goal, the preemptive cybersecurity intelligence company Silent Push spent 2024 tracking millions of hidden malicious domains and IP addresses, fingerprinting attacker infrastructure—both at scale and as it was built—mapping the impact of critical vulnerabilities spread across the web and working closely with partners to disrupt global threat actor operations.

We delivered world-first, in-depth technical reporting to our customers and produced IOFA feeds setting the gold standard for preemptive threat intelligence. We continue to perfect our rigorously curated, first-party dataset and intuitive threat-hunting platform. At Silent Push, when we say, “We Know First,” – we mean it.

[silentpush.com](https://silentpush.com)

# 1 Introduction

From C-suite leaders to hands-on keyboard analysts, Silent Push strives to ensure that the information we provide benefits all our readers. This “Year in Review” white paper contains a mix of technical information and analysis alongside high-level overviews and key trends regarding cyber attackers who have swiftly embraced the rise of AI to scale their operations and become more sophisticated by the minute.

We report the threat landscape as we see and experience it. Delving into some of the technical details behind Advanced Persistent Threats (APTs) pursuing nation-state objectives and major crimeware families focused purely on extracting financial gain, we objectively explore some of the latest emerging threats the security industry is facing. Examining the various malware and malicious infrastructure trends we have observed, we cover our own improvements and contributions in the fight against these threats and provide strategic recommendations for cyber-conscious organizations alongside our predictions for 2025.

The insights powering this paper are built on our proprietary dataset, which represents the most comprehensive view of the internet available anywhere in the world, to map attacker tactics, techniques, and procedures (TTPs) and infrastructure in real time. Our technology enables the tracking and analysis of adversaries’ network changes as they occur, stopping them at the gates – before they can get in.

**Note**: Operational security requirements prevent us from revealing certain technical details in this and the rest of our public-facing publications. For in-depth analysis of the threats listed herein (as well as many others), access to our industry-defining data, IOFA feeds, and more, please contact our Sales team to see about becoming an enterprise customer.

[silentpush.com](https://silentpush.com)

# 2 The Ever-Evolving Threat Landscape

## Silent Push Key Statistics

We enable organizations to stay one step ahead of emerging threats:

- Hundreds of thousands of Indicators of Future Attack (IOFAs) provided on a constantly recurring basis to organizations worldwide alongside a similar number of indicators in our Bulk Data Feeds.
- Published dozens of blogs and technical reports detailing analysis and mitigation needed to stop activities of multiple APTs and major crimeware groups.
- Collaborated with worldwide partners in law enforcement and the security industry, leading to the disruption and/or takedown of numerous networks and the blocking of countless cyber attacks.
- Continuously expanded our data collection, processing, and fingerprinting capabilities.

## Top Threat Trends

The cybersecurity environment in 2024 experienced rapid escalation in both volume and complexity of cyber threats. Silent Push analysts noted considerable increases in activity driven by both state-sponsored APTs and financially-motivated cybercriminal groups, including a dramatic increase in the sophistication of phishing kits – with new iterations appearing faster than ever before to shift targeting across industry verticals (financial, retail, technology, and energy).

Another trend, one of the most significant in 2024, was the proliferation of AI-powered infrastructure scaling. Threat actors harnessed AI to enhance their spear-phishing campaigns, automate malware development, and obfuscate their infrastructure. The use of generative AI tools has made it easier for adversaries to scale operations and create convincing lures, complicating traditional detection and response efforts.

[silentpush.com](https://silentpush.com)

“Infrastructure Laundering” is a term we coined to describe the growing criminal practice our analysts observed of threat actors intentionally hiding their infrastructure behind large, mainstream providers hosting many otherwise legitimate subscribers. We see it as an increasingly pressing issue. Our research into Triad Nexus (some of which we covered publicly and will discuss later), combined with insights driven by our unparalleled DNS data, has revealed troubling associations between cybercrime and real-world criminal gangs, most notably Chinese Triad groups.

Threat actors increasingly exploited Cloudflare’s proxying services to obscure their infrastructure, effectively concealing the true IP addresses behind their malicious campaigns. This tactic allowed adversaries to add a layer of anonymity and resilience to their operations, complicating efforts to identify and disrupt their hosting environments. Silent Push’s research utilized advanced unmasking techniques to reveal the real IPs behind proxied domains, enabling organizations to uncover hidden infrastructures and preemptively defend against these sophisticated threats.

Exemplified by actors like Raspberry Robin, that facilitated human-operated ransomware campaigns by providing compromised infrastructure to other threat groups, “Access-as-a-Service” models have continued to grow in prominence. These services streamlined the ability of less sophisticated actors to execute high-profile attacks, further diversifying the threat landscape. They also have worrisome ties to Russian threats that the industry should keep in mind when defending against them.

[silentpush.com](https://silentpush.com)

## RASPBERRY ROBIN

Raspberry Robin evolved from its initial discovery in September 2021 as a highly prevalent worm with little post-compromise activities to a key player in Access-as-a-Service operations.

Originally spread via USB drives, the worm’s payloads evolved to more traditional methods that utilize file-sharing websites and various victim-targeted lures. Once infected, victim devices connect to compromised QNAP NAS devices whose IP addresses are mapped via DNS A Records to short, two- and three-letter domains on niche domain suffixes, that act as command and control (C2) servers. Raspberry Robin is one of the most significant initial access brokers (IABs) operating today.

Silent Push researchers uncovered Raspberry Robin domains by identifying key nameservers, naming conventions, and a combination of IP and autonomous system number (ASN) diversity patterns. This led to the discovery of more than 180 unique Raspberry Robin C2 domains and allowed us to continue to track their