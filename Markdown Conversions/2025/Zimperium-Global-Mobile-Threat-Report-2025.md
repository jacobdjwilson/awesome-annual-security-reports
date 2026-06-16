# Global Mobile Threat Report 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [The Expanding Enterprise Mobile Footprint: Scale Meets Risk](#the-expanding-enterprise-mobile-footprint-scale-meets-risk)
- [Global Threat Landscape](#global-threat-landscape)
- [Top Threats and Risks](#top-threats-and-risks)
- [iOS Threats](#ios-threats)
- [Android Threats](#android-threats)
- [Mishing](#mishing)
- [Mobile Malware](#mobile-malware)
- [Sideloaded Apps](#sideloaded-apps)
- [The Need for Platform Vulnerability Management](#the-need-for-platform-vulnerability-management)
- [Are Your Work Apps Making it Easy to Steal Data?](#are-your-work-apps-making-it-easy-to-steal-data)
- [How do work apps handle sensitive data?](#how-do-work-apps-handle-sensitive-data)
- [Do the apps you use communicate securely?](#do-the-apps-you-use-communicate-securely)
- [Where’s my enterprise data going?](#wheres-my-enterprise-data-going)
- [App Data Going to Embargoed or High Risk Countries](#app-data-going-to-embargoed-or-high-risk-countries)
- [Apps Put the “A” in AI](#apps-put-the-a-in-ai)
- [Continuous App Vetting Is Mandatory](#continuous-app-vetting-is-mandatory)
- [Security Gaps in the Mobile Apps You Build](#security-gaps-in-the-mobile-apps-you-build)
- [What Your Tooling Says About Your Security Posture](#what-your-tooling-says-about-your-security-posture)
- [The Data Leaks You Don’t See](#the-data-leaks-you-dont-see)
- [Why Most Apps Are Still Failing Industry Best Practices](#why-most-apps-are-still-failing-industry-best-practices)
- [The Invisible Risk Inside Your App](#the-invisible-risk-inside-your-app)
- [Know Your Device - Device Attestation Is Critical](#know-your-device---device-attestation-is-critical)
- [Conclusion](#conclusion)

---

## Executive Summary

The 2025 Global Mobile Threat Report reveals that attackers have adopted a mobile-first attack strategy, making it essential for organizations to understand and mitigate mobile risks. This report offers insights into the evolving mobile threat landscape, helping organizations identify security gaps and align their defenses with relevant real-world risks.

### Key Security Findings on Threats to Your Mobile Devices
- **Mishing Surge**: Mishing (mobile-targeted phishing) represents roughly one-third of threats identified by zLabs. zLabs has observed that smishing (SMS phishing) comprises over two-thirds of mishing attacks. Mobile phishing attacks of vishing and smishing have also risen substantially (by 28% and 22%, respectively). Additionally, PDF phishing has emerged as a new and effective attack vector.
- **Mobile Vulnerability Management Challenges**: A significant percentage (25.3%) of devices are not upgradeable due to the device's age.
- **Sideloaded Mobile App Risk**: Sideloaded apps are present on 23.5% of enterprise devices.
- **Data Security in Work Apps**: zLabs found that 23% of apps used on work devices analyzed communicated with risky or embargoed countries.

### Key Security Findings in Mobile Apps Your Organization Develops
1. **App Protection Tooling Reflects Security Posture**: Across Android and iOS, most apps rely on basic tools or have no protection.
2. **The Perfect Supply Chain Attack Is Hiding in Your App**: Over 60% of top Android and iOS third-party components or SDKs are shipped as precompiled binaries, often with partial or missing SBOMs.
3. **Your App Is Only as Secure as the Device It Runs On**: At any given point in the year, over 50% of mobile devices are running outdated OS versions.

![25% of mobile devices can't upgrade their OS]

---

## The Expanding Enterprise Mobile Footprint: Scale Meets Risk

Enterprises are more mobile than ever. As of the end of 2024, there are approximately 7.2 billion smartphone users worldwide[^1]. Mobile devices now routinely use apps to access sensitive systems, data, and workflows once limited to secured desktops.

By the end of 2024, there were around 1.96 million apps on the Apple App Store and 2.87 million on Google Play. A typical user has between 80 and 100 apps installed[^2], yet only 11 are work-related[^3]. Meanwhile, 66% of American employees use their personal smartphones for work[^4], and 70% of organizations support BYOD[^5].

---

## Global Threat Landscape

### Top Threats and Risks
zLabs has observed and categorized the top threats by OS platform:

#### iOS Threats
54% of all iOS threats are mishing-based and 39.8% are network threats (man-in-the-middle attacks).
- **Device Vulnerabilities**: Jailbreaking and system tampering.
- **Network Risks**: Untrusted or insecure Wi-Fi networks leading to MITM attacks.
- **Application Risks**: Malicious, unexpected, or risky behavior from sideloaded apps.
- **Mishing Attacks**: Malicious links embedded in mishing content.

#### Android Threats
- **Device Vulnerabilities**: Rooting, privilege escalation, and failure to patch OS vulnerabilities.
- **Network Risks**: Untrusted or insecure Wi-Fi networks.
- **Application Risks**: Sideloaded applications.
- **Mishing Attacks**: Smishing (SMS/text phishing).

---

## Mishing

In 2024, the United States continues to be the #1 phished region worldwide, with zLabs data showing they comprised 44% of mobile phishing targets.

![Figure 1: Mishing Attack Vectors (SMS 69.3%, PDF 28.4%, QR 2.4%)]

![Figure 2: PDF Smishing Attack Example]

![Figure 3: Example of Toll Road Smishing Attack]

---

## Mobile Malware

zLabs research confirms that 18.1% of devices in our analysis set had mobile malware installed.

![Figure 4: Malware Family Distribution (Spyware 36.9%, Riskware 25.1%, Trojan 14.6%, Banker 3.4%, Adware 1.0%, Malware 18.0%)]

---

## The Need for Platform Vulnerability Management

| | 2022 | 2023 | 2024 |
| :--- | :--- | :--- | :--- |
| # of CVE (Android) | 1223 | 1422 | 501 |
| # of high or critical CVSS (Android) | 494 | 404 | 305 |
| # of zero day CVEs exploited in the wild (Android) | 41 | 97 | 12 |
| # of CVE (iOS) | 243 | 269 | 317 |
| # of high or critical CVSS (iOS) | 155 | 120 | 125 |
| # of zero day CVEs exploited in the wild (iOS) | 5 | 20 | 5 |

*Table 1: CVE data for iOS and Android OS versions*

---

## Are Your Work Apps Making it Easy to Steal Data?

### How do work apps handle sensitive data?
The top 10 permissions requested by work apps fall into a broad category of permissions that provide access to the user's location or personal information.

### Do the apps you use communicate securely?
A substantial percentage of work applications engage in insecure communication practices, such as failing to properly verify the authenticity of the servers they connect to.

---

## Where’s my enterprise data going?

![Graph: Top 10 non U.S. Countries iOS Work Apps Communicate With]

![Graph: Top 10 non U.S. Countries Android Work Apps Communicate With]

### App Data Going to Embargoed or High Risk Countries
zLabs found that 23% of work apps connect to embargoed or high-risk countries.

---

## Apps Put the “A” in AI

We have observed approximately 160% growth in the use of AI services within apps present on employee devices. OpenAI stands out as the dominant player, integrated into roughly 70% of the AI-powered apps analyzed.

---

## Security Gaps in the Mobile Apps You Build

### What Your Tooling Says About Your Security Posture
- **High “No Code Protection” Rates**: 16–34% of Android apps and 60% of iOS apps have no code protection.
- **Free Tools Dominate Android**: Over 60% of Android apps rely on open-source security tools.

---

## The Data Leaks You Don’t See

In apps across all iOS categories, 50–60% of apps are vulnerable to leaking personally identifiable information (PII), surpassing the Android rate, which peaks at around 43%.

---

## Why Most Apps Are Still Failing Industry Best Practices

The most frequently violated categories across OWASP and MASVS point to insecure data storage, weak cryptography, and improper use of platforms and APIs.

---

## The Invisible Risk Inside Your App

62% of the top 100 widely used Android frameworks and 46% of the top 100 widely used iOS libraries are only available as precompiled binaries, creating a "blind spot" in the supply chain.

---

## Know Your Device - Device Attestation Is Critical

- 61.2% of Android devices and 49.2% of iOS devices ran an outdated OS during a 12-month period.
- 1 in 400 Android devices is rooted.
- 1 in 2,500 iOS devices is jailbroken.
- 3 out of every 1,000 mobile devices are compromised.
- 1 out of every 5 Android devices encountered malware.

---

## Conclusion

Mobile is now a primary attack surface. Organizations must adopt a risk-based approach, including continuous app vetting, binary-level analysis, and mandatory device attestation to secure the enterprise mobile footprint.

---

### Sources
[^1]: https://explodingtopics.com/blog/smartphone-stats
[^2]: https://buildfire.com/app-statistics/
[^3]: https://www.gartner.com/en/newsroom/press-releases/2023-05-10-gartner-survey-reveals-47-percent-of-digital-workers-struggle-to-find-the-information-needed-to-effectively-perform-their-jobs
[^4]: https://attotime.com/blog/cell-phones-work-statistics
[^5]: https://jumpcloud.com/blog/byod-statistics