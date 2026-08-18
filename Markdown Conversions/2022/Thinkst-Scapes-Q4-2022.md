# Organization: Thinkst
# Report Title: Scapes-Q4
# Year: 2022

Most companies find out way too late that they've been breached.

[https://canary.love](https://canary.love)

## Table of Contents
- [Introduction](#introduction)
- [Signature Validation At Scale, For Better Or Worse](#signature-validation-at-scale-for-better-or-worse)
- [Modern Post-Exploitation](#modern-post-exploitation)
- [Farming The Apple Orchards: Living Off The Land Techniques](#farming-the-apple-orchards-living-off-the-land-techniques)
- [Forgotten Legacy In Today’s Systems](#forgotten-legacy-in-todays-systems)
- [Kerberos’ RC4-HMAC Broken In Practice: Spoofing PACs With MD5 Collisions](#kerberos-rc4-hmac-broken-in-practice-spoofing-pacs-with-md5-collisions)
- [Nifty Sundries](#nifty-sundries)
- [On The Implications Of Spoofing And Jamming Aviation Datalink Applications](#on-the-implications-of-spoofing-and-jamming-aviation-datalink-applications)
- [{JS-ON: Security-OFF}: Abusing JSON-Based SQL Queries](#js-on-security-off-abusing-json-based-sql-queries)
- [Conclusion](#conclusion)

---

## Introduction

Themes covered in this issue:
- Signature validation at scale, for better or worse
- Modern post-exploitation
- Farming The Apple Orchards: Living Off The Land Techniques
- Forgotten legacy in today’s systems
- Kerberos’ RC4-HMAC broken in practice: spoofing PACs with MD5 collisions
- Nifty Sundries
- On the Implications of Spoofing and Jamming Aviation Datalink Applications
- {JS-ON: Security-OFF}: Abusing JSON-Based SQL Queries
- Conclusion

The first of October and the end... ts@thinkst.com!

| Conference/venue name | Number of publications reviewed |
|-----------------------|---------------------------------|
| Total                 | 45                              |

## Signature Validation At Scale, For Better Or Worse

At scale, for better or worse. Modern post-exploitation and abusing living off the land fit into any of the aforementioned...

Announcing GUAC, a great pairing with SLSA (and SBOM)!

The use of SAML... ![A figure showing one IdP and many SPs](image_idp_sps.png).

With the ever-present concern over software security, and specifically...

We are hopeful...

By now, teams may be getting tired and distracted affected by X vulnerability?” question. However, as supply chain attacks become more sophisticated, answering just this question is insufficient and becoming increasingly difficult. As teams start to ask, “If X was compromised, which software is affected?”, we hope to see a tool like...

This blog covers the SigStore project, specifically the Python-language implementation. SigStore allows developers to tie short-lived certificates with those certificates. This reduces the risk of a certificate being exposed, while also storing a record of the human identity associated with a specific official build system versus an attacker’s.

SigStore is filling a gap systems, their configuration, and even aspects of the resultant binaries...

## Modern Post-Exploitation

Your MacOS Privacy Mechanisms

### Farming The Apple Orchards: Living Off The Land Techniques

- LOLBINed – Using Kaspersky Endpoint Security “KES” Installer
- POPKORN: Popping Windows Kernel Drivers At Scale

TCC (Transparency, Consent, and Control). TCC provides a more fine-root permissions. They were able to find over 20 bypasses through loading utility to create a copy of the filesystem without the TCC entitlements. The work finishes with a review of the changes made in MacOS Ventura, and how some of the fixes are not entirely comprehensive.

While TCC does give users more control environment is going to be difficult. There is a balancing act between...

Living off the land is a post-exploitation technique used to minimise or to avoid triggering alerts for suspicious file execution, as LOLBins are...

This research explored living off the land in Apple’s MacOS environments. 

Living off the land... ![A flowchart showing more feature-filled by default, and other OS environments restrict](image_flowchart_lol.png).

...can be used to camouflage their malicious activity. In this post, the author details an approach to finding ways to execute code from Kaspersky’s...

This approach could offer an interesting setup for attackers who might...

This post demonstrates a number of tools, that other researchers can use to find unexpected behaviour in...

These patterns of abuse operate on the principle that "any action not specifically denied, is..."

...driver that fails to sufficiently sanitise that data before calling certain kernel...

The presented system, POPKORN, downloaded and extracted 5,000 driver an EoP exploit. Of the 5,000 drivers, only 212 were compatible with the vulnerability definition (WDM driver, took user-space data, called to one of the sink functions), and of these, POPKORN identified 38 vulnerabilities, 31 of which were new, and all were manually verified as true-positives. The CVE and disclosure processes were underway at time of publication, but...

This work highlights the trend more bug classes become codified as a vulnerability definition, it...

Years after DARPA’s Cyber Grand Challenge (CGC) still paying dividends. While CGC itself was focused on an artificial world benefits.

![The high-level design and flow of the POPKORN system](image_popkorn_design.png)

## Forgotten Legacy In Today’s Systems

RC4 Is Still Considered Harmful

Kerberos’ RC4-HMAC broken in practice: spoofing PACs

Exploring Ancient Ruins to Find Modern Bugs

By James Forshaw, he developed two attacks: the first attack is network-based to alter an unprotected field, creating a downgrade to RC4...

...require access to network authentication traffic...

The paper outlines a method for using MD5 Certificate. This attack also shows that reliance on the MD5 hash function has not yet been fully...

- Older legacy protocols
- ASN.1 parsing is difficult
- Active Directory security
- Kerberos network traffic

...maintain backwards compatibility, the additional logic adds significant...

The researchers built a scanning pipeline that would look for PE files on a remote attack that allows an attacker to map a file share they control to a remote victim machine, then man-in-the-middle shared file access.

...operations – mapping a...

RPC services make an attractive target that is difficult to...

Sovrin is a permissioned network (only specific nodes can create or...)

With any new complex distributed system, systems has been on both the financial risks (flash-lending attacks, etc.)...

The pace of development in this space, first movers, contributes to these types of vulnerabilities. As many of...

## Nifty Sundries

- On the Implications of Spoofing and Jamming Aviation Datalink Applications
- {JS-ON: Security-OFF}: Abusing JSON-Based SQL Queries

This work explored identifying specific drones via an acoustic fingerprint. Eight DJI Mini 2 drones, and multiple sets of spare propellers, were...

...environment shown in the figure below. Then, multiple analyses were performed on different sample lengths, with or without additional background noise, and different ML model types, to determine which...

With drone costs dropping...

Physically unclonable functions have been a field of study for many fingerprinting...

...being explored via different mediums is exciting and should offer many future benefits.

This work explored identifying specific drones via an acoustic fingerprint. Eight DJI Mini 2 drones, and multiple sets of spare propellers, were...

...environment shown in the figure below. Then, multiple analyses were performed on different sample lengths, with or without additional background noise, and different ML model types, to determine which...

While the existence of, additional authentication logic is added. The figure paints a scary...

## {JS-ON: Security-OFF}: Abusing JSON-Based SQL Queries

The majority of this research explored exploiting a specific product’s SQLi vulnerability, however, when the researcher tried to exploit the cloud version, it was blocked by AWS’ web application firewall (WAF).

...it appeared that specific SQL operators were triggering the WAF to drop...

...operators in SQL that may bypass the WAF, and discovered that modern database servers support JSON natively with new operators to simplify JSON...

Using the new JSON operators bypassed not only the AWS WAF, but all of the large WAF vendors. The researcher developed a patch to SQLMap and was able to trivially detect and exploit SQLi in WAF-protected web applications.

It is always difficult between JSON objects.

...to determine whether a sender was a camera, whether it was filming the traffic (unlike other devices that may have periods of inactivity) and more traffic sent when the user in the environment was moving (which causes...)

...their proximity to the camera. This process worked across 20 different...

This research has a clear benefit for travellers who would like to look other use cases that this counter-surveillance capability offers. Further...

As mentioned in last quarter’s ThinkstScapes, there is a significant explored LTE network traffic, and future work will likely determine...

## Conclusion

IN THIS QUARTER’S EDITION:

...behind us. We look forward to diving in, finding interesting...

[^1]: Footnote content referenced within technical documentation.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
