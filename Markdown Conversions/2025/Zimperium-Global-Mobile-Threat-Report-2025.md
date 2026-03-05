# GLOBAL MOBILE THREAT REPORT 2025

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

![Infographic showing Smishing comprises over two-thirds of mishing attacks]

### Key Security Findings on Threats to Your Mobile Devices

*   **Mishing Surge**: Mishing (mobile-targeted phishing) represents roughly one-third of threats identified by zLabs. zLabs has observed that smishing (SMS phishing) comprises over two-thirds of mishing attacks. Mobile phishing attacks of vishing and smishing have also risen substantially (by 28% and 22%, respectively), which is not surprising given the widespread rise in the use of AI tools by attackers. Additionally, PDF phishing has emerged as a new and effective attack vector. All of which necessitates a defense response of advanced mobile threat defense coupled with robust user education.
*   **Mobile Vulnerability Management Challenges**: A significant percentage (25.3%) of devices are not upgradeable due to the device's age. These older devices present a data compromise risk to the organization if an OS vulnerability is used in an attack.
*   **Sideloaded Mobile App Risk**: Sideloaded apps are present on 23.5% of enterprise devices. Sideloaded apps substantially increase the risk of mobile device compromise as they may be repackaged versions of ‘legit’ apps where additional functionality is offered but potentially malicious code is embedded within the app.
*   **Data Security in Work Apps**: Work apps need to be vetted. zLabs found that 23% of apps used on work devices analyzed communicated with risky or embargoed countries. This report emphasizes the need for vetting work apps and for security professionals to understand where the servers of even legitimate work apps are located.

---

## Key Security Findings in Mobile Apps Your Organization Develops

1.  **App Protection Tooling Reflects Security Posture—And the Gaps Are Alarming**: Across Android and iOS, most apps rely on basic tools or have no protection, including in high-risk sectors like Finance. Organizations are either underestimating the sophistication of mobile threats or relying too heavily on platform-level security. The burden of fragmented tooling falls squarely on Android developers, often leading to misconfigurations and friction. On iOS, an over-reliance on the platform results in widespread under-protection. In both cases, the gap between app security investment and real-world risk leaves mobile apps dangerously exposed.
2.  **The Perfect Supply Chain Attack Is Hiding in Your App**: Over 60% of top Android and iOS third-party components or SDK's are shipped as precompiled binaries, often with partial or missing SBOMs. Even when source code exists, developers commonly test open-source versions but deploy the compiled binaries for speed, leaving what ships and runs unchecked. This allows attackers to poison the mobile supply chain with malicious or tampered components, bypassing traditional static and SCA tools. Without runtime introspection, these invisible dependencies become ideal targets for exploitation.
3.  **Your App Is Only as Secure as the Device It Runs On**: At any given point in the year, over 50% of mobile devices are running outdated OS versions, and a significant number are compromised or infected. This creates untrusted environments where even apps that employ security measures are susceptible to manipulation. Without device attestation, apps can’t distinguish between safe and hostile execution environments, exposing sensitive data and operations. For AppSec and Dev teams, device attestation isn’t a nice-to-have—it’s the gatekeeper for enforcing trust, preventing fraud and safeguarding sensitive data at scale.

![Infographic stating 25% of mobile devices can't upgrade their OS]

---

## Recommendations for Leaders:

*   **Rigorous, Continuous App Vetting**: Enforce strict processes for analyzing third-party apps on mobile devices to assess the application's composition (e.g. SBOM) and the actual risk it poses, with a deep focus on critical vectors like excessive permissions, insecure data handling, and vulnerable communication channels.
*   **Combat Mishing**: To protect against advanced and mobile-targeted social engineering tactics, security teams should implement AI-enabled mobile threat defense and provide regular employee training to raise awareness.
*   **Mobile Vulnerability Management**: Define and enforce policy on timely OS and app updates and data access by end-of-life devices to minimize enterprise data and infrastructure risk.
*   **Secure Your Third-Party Code**: Require mobile app teams to analyze app binaries early during development, including closed-source components, to uncover hidden vulnerabilities, assess runtime behavior, and prevent malicious code from entering the production pipeline.
*   **Mandate Device Attestation for Your Mobile Apps**: Ensure your mobile app development teams implement device attestation to enable apps to detect untrusted environments and respond in real-time on the device to mitigate risk.

---

## The Expanding Enterprise Mobile Footprint: Scale Meets Risk

Enterprises are more mobile than ever. As of the end of 2024, there are approximately 7.2 billion smartphone users worldwide driven by mobile workforces, remote access and enterprise mobility initiatives. Mobile devices now routinely use apps to access sensitive systems, data and workflows once limited to secured desktops—significantly expanding the digital attack surface.[^1]

At the same time, the number of work and personal apps has exploded—blurring the lines between enterprise and consumer environments. By the end of 2024, there were around 1.96 million apps on the Apple App Store and 2.87 million on Google Play. A typical user has between 80 and 100 apps installed, yet only 11 are work-related, according to Gartner.[^2] Meanwhile, 66% of American employees use their personal smartphones for work,[^3] and 70% of organizations support BYOD.[^4]

This means the average work-enabled device is dominated by apps outside IT’s control, assessment, or development, introducing unmonitored attack surfaces that security teams often can’t see, let alone secure. As enterprise mobility scales, so does the risk. The explosion in mobile apps isn’t just a usability shift—it’s a threat multiplier.

---

## Global Threat Landscape

### Top Threats and Risks

As mobile devices continue to be prime targets, understanding the specific methods attackers employ to compromise them is critical. Our analysis breaks down the prevalent threats observed across both Android and iOS platforms, highlighting the key attack vectors targeting devices, networks, applications, and users through sophisticated mishing (mobile targeted phishing) and other campaigns.

#### iOS Threats
54% of all iOS threats are mishing based and 39.8% are network threats (man-in-the-middle attacks).

*   **Device Vulnerabilities**: The most critical threats targeting iOS devices involve jailbreaking and system tampering that compromise the integrity of the operating system, compounded by the significant risk posed by failing to apply essential OS updates that address known vulnerabilities.
*   **Network Risks**: The leading iOS network threat originates from connecting to untrusted or insecure Wi-Fi networks, which directly enables attackers the ability to initiate dangerous Man-in-the-Middle (MITM) attacks.
*   **Application Risks**: Primary app threats surrounding iOS are from applications exhibiting malicious, unexpected and/or risky behavior, exposed from sideloaded app threats.
*   **Mishing Attacks**: Malicious links embedded in mishing content pose a major risk, immediately attempting to direct users to harmful or data-stealing websites.

#### Android Threats
The top Android threats are malicious apps delivered via sideloaded apps and mishing/social engineering.

*   **Device Vulnerabilities**: The most significant threats to Android devices stem from compromised states such as rooting or privilege escalation, alongside critical risks introduced by failure to patch known OS vulnerabilities.
*   **Network Risks**: Connecting to untrusted or insecure Wi-Fi networks remains a primary network threat for Android devices, critically exposing users to Man-in-the-Middle (MITM) attacks.
*   **Application Risks**: Sideloaded applications represent the leading application-based threat to Android users, bypassing official app store security checks.
*   **Mishing Attacks**: Smishing (SMS/text phishing), the dominant mishing threat on Android, involves malicious links designed to immediately redirect users to dangerous phishing or malware-hosting sites.

---

## Mishing

We discussed the move from phishing to mishing (mobile targeted phishing) in last year’s report as attackers adopted a mobile-first attack strategy. This year’s data validates that prediction:
*   Incidence of Vishing up 28%
*   Incidence of Smishing up 22%
*   The rise of PDF phishing via mobile

In 2024, the United States continues to be the #1 phished region worldwide with zLabs data showing they comprised 44% of mobile phishing targets.

![Figure 1: Mishing Attack Vectors (SMS 69.3%, PDF 28.4%, QR 2.4%)]

---

## Mobile Malware

Malware remains a primary weapon for both opportunistic cybercriminals and sophisticated advanced persistent threats. zLabs research confirms that 18.1% of devices in our analysis set had mobile malware installed.

![Figure 4: Malware Family Distribution (Spyware 36.9%, Riskware 25.1%, Trojan 18.0%, Malware 14.6%, Banker 3.4%, Adware 1.0%)]

---

## Sideloaded Apps

Sideloading is the practice of installing mobile apps on a device that are not from the official app stores. zLabs identified 23.5% of mobile devices having the presence of one or more sideloaded apps. Sideloaded apps are amongst the top 3 risks for both iOS and Android devices per zLabs.

---

## Are Your Work Apps Making it Easy to Steal Data?

App vetting is aimed at assessing the risk that an app poses to the organization. Our analysis showed that, while not always required, a substantial percentage of apps don’t fully declare what sensitive information they access or collect.

### Do the apps you use communicate securely?
We have observed a rise in insecure communication of data across numerous work app categories on the Android platform. This failure to validate secure connections makes the data exchanged by these apps highly susceptible to interception via Man-in-the-Middle (MITM) attacks.

---

## Apps Put the “A” in AI

The use of AI has been exploding in apps. We have observed approximately 160% growth in the use of AI services within apps present on employee devices. Our analysis confirms that AI capabilities are being leveraged across a broad spectrum of application types, extending far beyond typical productivity tools.

---

## Security Gaps in the Mobile Apps You Build

Assessing the third-party applications you use allows you to make informed business decisions. Equally important are the applications that your organization is developing.

### What Your Tooling Says About Your Security Posture
A notable percentage of Android apps (16–34%) and iOS apps (60%) have no code protection at all, leaving them vulnerable to reverse engineering, credential theft, and fraud.

---

## The Invisible Risk Inside Your App

Third-party libraries and frameworks are extensively used in mobile app development. 62% of the top 100 widely used Android frameworks and 46% of the top 100 widely used iOS libraries are only available as precompiled binaries. This lack of transparency introduces silent vulnerabilities that traditional security tools struggle to detect.

---

## Know Your Device - Device Attestation Is Critical

Today, the mobile device itself has become a critical point of vulnerability. Device attestation is essential for validating device integrity in real time, allowing organizations to block high-risk interactions, protect sensitive data and defend against fraud before it starts.

*   **1 in 400** Android devices is ROOTED
*   **1 in 2,500** iOS devices is JAILBROKEN
*   **3 out of every 1,000** mobile devices are COMPROMISED

---

## Conclusion

The findings of this 2025 Global Mobile Threat Report make one thing clear: mobile is now a primary attack surface, not a secondary concern. Organizations must adopt a risk-based approach to mobile security to counter the mobile-first strategies of attackers. Mobile security is no longer optional or peripheral; it is now a strategic pillar of enterprise risk management.

---

### Sources
[^1]: https://explodingtopics.com/blog/smartphone-stats
[^2]: https://buildfire.com/app-statistics/
[^3]: https://attotime.com/blog/cell-phones-work-statistics
[^4]: https://jumpcloud.com/blog/byod-statistics