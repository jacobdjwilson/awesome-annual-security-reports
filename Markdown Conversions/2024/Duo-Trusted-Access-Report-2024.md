# The 2024 Duo Trusted Access Report

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [01 Billions of Authentications](#01-billions-of-authentications)
- [02 Attack Surface Increase](#02-attack-surface-increase)
- [03 Establishing Device Trust](#03-establishing-device-trust)
- [04 Powerful Policy Controls](#04-powerful-policy-controls)
- [Closing Words](#closing-words)
- [Recommendations](#recommendations)

---

## Introduction
### The New Frontier of Access Management and Identity Security
In exploring the future, we’re often drawn to predicting the unknown. Our quest for answers is unending, and we rely heavily on data to guide our predictions. Organizations today navigate a treacherous digital landscape where the motives of attackers are as varied as their methods—ranging from financial gains, cyber espionage, and disruption to reputation damage to cyber warfare.

As organizations grapple with increasingly sophisticated cybersecurity threats, a demand for holistic access management solutions has been apparent for a few years. MFA is a great security measure, but not enough on its own. More sophisticated threats call for additional layers of security. By integrating context, an access management solution can analyze the situation in which access is being requested, such as information about the user’s typical behavior or environment including their usual login times, geolocation, and device.

## Methodology
In this report, we’ll delve into insights drawn from an analysis of over 16 billion authentications in the last year (and over 44B in the last 4 years), spanning nearly 52 million different browsers, on 58 million endpoints and 21 million unique phones across regions including North America, Latin America, Europe, the Middle East, and the Asia Pacific. We defined our 2023 annual time range as between June 1, 2022, and May 31, 2023.

## Key Findings
1. **Stronger Auth Methods Show Upward Trends**: 91.5% of accounts enable Duo Push. SMS and phone calls dipped to an all-time low of 4.9%.
2. **Return-to-Office is the New Hybrid Work Reality**: Remote access application authentications fell to nearly 25% as companies move staff back into the office.
3. **MFA Usage Continues to Expand Globally**: MFA authentications using Duo rose by 41% in the past year.
4. **Diverse Device Environments Require Vendor-Agnostic Security**: Windows leads at 38.2%, with iOS a strong second at 33.4%.
5. **Organizations are putting in stricter controls reducing risk of out-of-date software**: Failures due to out-of-date devices increased by 74.7% in 2023.
6. **Failed Authentications Highlight User Risks**: 5% of all measured authentications failed; 28% of those were due to users not being enrolled.
7. **Top 3 Policy Groups to Reduce Security Debt**: 96.4% of organizations have no policy related to location.
8. **Identity is The New Perimeter**: 23% of engagements observed by Talos IR involved attackers abusing compromised credentials to access valid accounts[^1].

[^1]: From Talos IR 2023 Year In Review, see “Telemetry Trends” pg. 6-7.

---

## 01 Billions of Authentications
![Figure 01: Monthly successful authentications chart showing growth from 2019 to 2023]

MFA continues to strengthen passwords. The number of MFA authentications using Duo rose by 41% in the past year. Account adoption of WebAuthn-enabled factors, including security keys and biometric technology like TouchID, increased by 53% from 2022 to 2023.

## 02 Attack Surface Increase
The number of MFA authentications using Duo rose by 41% in the past year. Germany saw a 52.3% increase. Globalization increases the probability of supporting more than one identity provider (IdP), which can lead to potential security gaps if not managed with vendor-agnostic access management.

![Figure 06: Top 10 countries that experienced an increase or decrease in authentication volume]

## 03 Establishing Device Trust
Gaining visibility into and securing myriad devices is an ongoing battle. 
- **Mobile OS Usage**: iOS (71.7%), Android (28.2%).
- **Top OS**: Windows (38.2%), iOS (33.4%), Mac OS X (13.7%), Android (13.1%).

![Figure 08: Different browsers used for authentication]

The percentage of failures due to out-of-date devices increased by 74.7% in 2023. The more operating systems an organization allows to authenticate, the more likely it is those authentications will occur with an out-of-date OS.

## 04 Powerful Policy Controls
Duo Push-based authentication was present in 99.3% of all global policies. 5% of all measured authentications failed, with 28% of those failures attributed to users not being enrolled in the system.

### Top 3 Policy Groups to Reduce Security Debt
1. **Geo-restrictions**: 96.4% of organizations have no policy related to location.
2. **Invalid or Outdated Devices**: Policies detect devices based on security posture (OS version, patches).
3. **Granular Access Policies**: Managing guest, dormant, or orphaned accounts to limit access.

---

## Closing Words
The future of identity security lies in bridging the gap between identity and security teams. Identity threat detection and response (ITDR) capabilities are becoming a necessity. Context is the new MFA; by analyzing the situation in which access is requested, organizations can differentiate between legitimate users and potential threats.

## Recommendations
- Organization-wide adoption of strong MFA and moving towards requiring only phishing-resistant MFA such as FIDO2 security keys for privileged access.

---

ccounts.

•  Enable Verified Duo Push which disarms push harassment and push fatigue attacks and

puts your organization on the path towards passwordless.

•  Ensure only trusted devices, managed or unmanaged, are granted access to

corporate resources.

•  Set data-informed user authentication policies that consider your organization’s risk levels
and focus points, with intelligent factor step-up that doesn’t impede user productivity.

•

Leverage a modern single sign-on solution as a policy enforcement tool to apply
principles of zero trust and least privilege access for each application.

•  Take advantage of solutions that assess user and device telemetry to identify known
threat patterns and anomalies, like Duo Risk-Based Authentication. Evaluate login
attempts for context and risk.

•

Identify the IAM complexities in your environment with ITDR and assess weak
points based on how much visibility you have. Leverage Identity Threat Detection
and Response capabilities to get visibility across your identity ecosystem in a single,
comprehensive interface.

36

© 2024 Cisco and/or its affiliates. All rights reserved.Credits

Data Science

Cyentia Institute

Elizabeth Gilbert

Kevin Pelaez, PhD

Rose Putler, M.S.

Writers

Katherine Yang

Michael Parker

Slavka Bila

Production

Yolina Nenov

Taylor Stewart

Design & Dev

Amanda Cash

Chris Canote

Clayton Chu

Mary Jane Duty

Tony Ly

References

•

•

•

•

•

“2023 STATE OF IDENTITY SECURITY: Protecting the Workforce,”
Oort, 2023

“Achieving Security Resilience: Findings from the Security Outcomes Report, Vol 3”
Cisco, 10 January 2023

“Cisco Cybersecurity Readiness Index,”
Cisco, March 2023

“Cisco Talos 2023 Year in Review,”
Cisco Talos, 5 December 2023

“Incident Response Trends Q2 2023: Data Theft Extortion Rises,
While Healthcare Is Still Most-Targeted Vertical,”
Cisco Talos, 26 July 2023

Start your free 30-day trial and quickly protect all
users, devices and applications at duo.com

© 2024 Cisco and/or its affiliates. All rights reserved. Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S.
and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks. Third-party trademarks mentioned are the property of
their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. 1266747417 02/2024