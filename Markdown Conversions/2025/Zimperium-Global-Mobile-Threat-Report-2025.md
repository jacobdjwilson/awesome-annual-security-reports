# GLOBAL MOBILE THREAT REPORT

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
  - [Do the apps you use communicate securely](#do-the-apps-you-use-communicate-securely)
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

# Executive Summary

The 2025 Global Mobile Threat Report reveals that attackers have adopted a mobile-first attack strategy, making it essential for organizations to understand and mitigate mobile risks. This report offers insights into the evolving mobile threat landscape, helping organizations identify security gaps and align their defenses with relevant real-world risks.

> Smishing (SMS phishing) comprises over two-thirds of mishing attacks

### Key Security Findings on Threats to Your Mobile Devices

-   **Mishing Surge**: Mishing (mobile-targeted phishing) represents roughly one-third of threats identified by zLabs. zLabs has observed that smishing (SMS phishing) comprises over two-thirds of mishing attacks. Mobile phishing attacks of vishing and smishing have also risen substantially (by 28% and 22%, respectively), which is not surprising given the widespread rise in the use of AI tools by attackers. Additionally, PDF phishing has emerged as a new and effective attack vector. All of which necessitates a defense response of advanced mobile threat defense coupled with robust user education.
-   **Mobile Vulnerability Management Challenges**: A significant percentage (25.3%) of devices are not upgradeable due to the device's age. These older devices present a data compromise risk to the organization if an OS vulnerability is used in an attack.
-   **Sideloaded Mobile App Risk**: Sideloaded apps are present on 23.5% of enterprise devices. Sideloaded apps substantially increase the risk of mobile device compromise as they may be repackaged versions of ‘legit’ apps where additional functionality is offered but potentially malicious code is embedded within the app.
-   **Data Security in Work Apps**: Work apps need to be vetted. zLabs found that 23% of apps used on work devices analyzed communicated with risky or embargoed countries. This report emphasizes the need for vetting work apps and for security professionals to understand where the servers of even legitimate work apps are located.

### Key Security Findings in Mobile Apps Your Organization Develops

1.  **App Protection Tooling Reflects Security Posture—And the Gaps Are Alarming**
    Across Android and iOS, most apps rely on basic tools or have no protection, including in high-risk sectors like Finance. Organizations are either underestimating the sophistication of mobile threats or relying too heavily on platform-level security. The burden of fragmented tooling falls squarely on Android developers, often leading to misconfigurations and friction. On iOS, an over-reliance on the platform results in widespread under-protection. In both cases, the gap between app security investment and real-world risk leaves mobile apps dangerously exposed.
2.  **The Perfect Supply Chain Attack Is Hiding in Your App**
    Over 60% of top Android and iOS third-party components or SDK's are shipped as precompiled binaries, often with partial or missing SBOMs. Even when source code exists, developers commonly test open-source versions but deploy the compiled binaries for speed, leaving what ships and runs unchecked. This allows attackers to poison the mobile supply chain with malicious or tampered components, bypassing traditional static and SCA tools. Without runtime introspection, these invisible dependencies become ideal targets for exploitation.
3.  **Your App Is Only as Secure as the Device It Runs On**
    At any given point in the year, over 50% of mobile devices are running outdated OS versions, and a significant number are compromised or infected. This creates untrusted environments where even apps that employ security measures are susceptible to manipulation. Without device attestation, apps can’t distinguish between safe and hostile execution environments, exposing sensitive data and operations. For AppSec and Dev teams, device attestation isn’t a nice-to-have—it’s the gatekeeper for enforcing trust, preventing fraud and safeguarding sensitive data at scale.

> 25% of mobile devices can't upgrade their OS

### Recommendations for Leaders:

-   **Rigorous, Continuous App Vetting**: Enforce strict processes for analyzing third-party apps on mobile devices to assess the application's composition (e.g. SBOM) and the actual risk it poses, with a deep focus on critical vectors like excessive permissions, insecure data handling, and vulnerable communication channels.
-   **Combat Mishing**: To protect against advanced and mobile-targeted social engineering tactics, security teams should implement AI-enabled mobile threat defense and provide regular employee training to raise awareness.
-   **Mobile Vulnerability Management**: Define and enforce policy on timely OS and app updates and data access by end-of-life devices to minimize enterprise data and infrastructure risk.
-   **Secure Your Third-Party Code**: Require mobile app teams to analyze app binaries early during development, including closed-source components, to uncover hidden vulnerabilities, assess runtime behavior, and prevent malicious code from entering the production pipeline.
-   **Mandate Device Attestation for Your Mobile Apps**: Ensure your mobile app development teams implement device attestation to enable apps to detect untrusted environments and respond in real-time on the device to mitigate risk.

Organizations can significantly reduce mobile risk exposure and protect sensitive data by aligning mobile device and application security to real-world threats and risks. For mobile device security, this includes fortifying protections against mishing (mobile phishing) and continuously vetting third-party apps on enterprise connected devices. For mobile app security, organizations must account for today’s threat sophistication and move away from fragmented tooling. Organizations should select solutions that simplify the implementation of security measures and foster better collaboration between security and development teams. This allows teams to efficiently build, secure, and release secure mobile apps at scale.

# The Expanding Enterprise Mobile Footprint: Scale Meets Risk

Enterprises are more mobile than ever. As of the end of 2024, there are approximately 7.2 billion smartphone users worldwide driven by mobile workforces, remote access and enterprise mobility initiatives.[^1] Mobile devices now routinely use apps to access sensitive systems, data and workflows once limited to secured desktops—significantly expanding the digital attack surface.

At the same time, the number of work and personal apps has exploded—blurring the lines between enterprise and consumer environments. By the end of 2024, there were around 1.96 million apps on the Apple App Store and 2.87 million on Google Play.[^2] A typical user has between 80 and 100 apps installed, yet only 11 are work-related, according to Gartner.[^3] Meanwhile, 66% of American employees use their personal smartphones for work,[^4] and 70% of organizations support BYOD.[^5]

This means the average work-enabled device is dominated by apps outside IT’s control, assessment, or development, introducing unmonitored attack surfaces that security teams often can’t see, let alone secure. As enterprise mobility scales, so does the risk. The explosion in mobile apps isn’t just a usability shift—it’s a threat multiplier.

The result is a fragmented, under-secured mobile landscape where apps and devices become potential vectors for data loss, fraud, and enterprise breaches.

A deep dive into today’s mobile threat environment based on real-world data reveals where vulnerabilities lie, how attackers take advantage, and what organizations must do to defend their mobile footprint.

# Global Threat Landscape
## Top Threats and Risks

As mobile devices continue to be prime targets, understanding the specific methods attackers employ to compromise them is critical. Our analysis breaks down the prevalent threats observed across both Android and iOS platforms, highlighting the key attack vectors targeting devices, networks, applications, and users through sophisticated mishing (mobile targeted phishing) and other campaigns.

zLabs has observed and categorized the top Threats by OS platform:

### iOS Threats

54% of all iOS threats are mishing based and 39.8% are network threats (man-in-the-middle attacks).

Breaking it down further by Device, Network, Application and Mishing attack vectors:

-   **Device Vulnerabilities**
    The most critical threats targeting iOS devices involve jailbreaking and system tampering that compromise the integrity of the operating system, compounded by the significant risk posed by failing to apply essential OS updates that address known vulnerabilities. Furthermore, our analysis also revealed disruptive system anomalies, marked by unexpected system and application service crashes observed throughout the year.
-   **Network Risks**
    The leading iOS network threat originates from connecting to untrusted or insecure Wi-Fi networks, which directly enables attackers the ability to initiate dangerous Man-in-the-Middle (MITM) attacks, on both WiFi and Cellular networks. We also observed critical network anomalies throughout the year, prominently featuring suspicious connections to high-risk countries and excessive outbound data traffic.
-   **Application Risks**
    Primary app threats surrounding iOS are from applications exhibiting malicious, unexpected and/or risky behavior, exposed from sideloaded app threats, a risk previously more associated with Android but now becoming a notable vector on iOS.
-   **Mishing Attacks**
    Analysis of our mobile phishing threat data consistently shows that malicious links embedded in mishing content pose a major risk, immediately attempting to direct users to harmful or data-stealing websites upon clicking.

### Android Threats

The top Android threats are malicious apps delivered via sideloaded apps and mishing/social engineering.

Breaking it down further by Device, Network, Application and Mishing attack vectors:

-   **Device Vulnerabilities**
    The most significant threats to Android devices stem from compromised states such as rooting or privilege escalation, alongside critical risks introduced by failure to patch known OS vulnerabilities or the continued use of devices too old to receive essential security updates.
-   **Network Risks**
    Connecting to untrusted or insecure Wi-Fi networks remains a primary network threat for Android devices, critically exposing users to Man-in-the-Middle (MITM) attacks where sensitive data can be intercepted. Similarly to iOS, we also observed critical network anomalies throughout the year, prominently featuring suspicious connections to high-risk countries and excessive outbound data traffic.
-   **Application Risks**
    Sideloaded applications represent the leading application-based threat to Android users, bypassing official app store security checks and frequently containing malicious code or severe security flaws.
-   **Mishing Attacks**
    Smishing (SMS/text phishing), the dominant mishing threat on Android, involves malicious links designed to immediately redirect users to dangerous phishing or malware-hosting sites.

Based on our analysis across both Android and iOS platforms, Mishing stands out as the top overall mobile threat, aligning with the broader increase in such attacks. While sideloaded applications represent the second biggest threat for Android, a risk historically unique to the platform, network threats are the second most prevalent for iOS. Notably, sideloaded app threats are now emerging as a developing concern for iOS, particularly following the availability of third-party app marketplaces in 2024 due to regulatory changes. A consistent top risk across both operating systems is the presence of devices running vulnerable or outdated OS versions that cannot be upgraded. Mitigating this requires decommissioning non-upgradeable devices and promoting timely OS updates for all users.

### KEY TAKEAWAYS

-   Mishing, especially via SMS, represents a high risk and requires both threat detection capabilities and user training to combat this threat.
-   Time lag between OS upgrade availability and installation by the end user exposes the enterprise to vulnerability risk from outdated/vulnerable OS.
-   Reduce sideloaded app risk by thoroughly vetting every application using a comprehensive application vetting solution to assess security, compliance and overall risk, particularly for apps on devices accessing sensitive enterprise data.

### Top Threats in US Public Sector

Based on our analysis across both Android and iOS platforms, the top threats in the US public sector come from mishing, risky wifi network connections that can lead to MITM attacks, and from sideloaded apps on Android. As with the overall analysis, a consistent risk across both operating systems is the presence of devices running vulnerable or outdated OS versions that cannot be upgraded. Mitigating this requires decommissioning non-upgradeable devices and promoting timely OS updates for all users.

### KEY TAKEAWAYS FOR PUBLIC SECTOR

-   Encourage user upgrades as soon as OS updates are available.
-   Discourage users from connecting to unsecured WiFi networks. Implement conditional access policies to avoid sensitive data being accessed or shared over the network when on unsecured networks.
-   Reduce sideloaded app risk by thoroughly vetting every application using a comprehensive application vetting solution to assess security, compliance, and overall risk, particularly for apps on devices accessing sensitive data.

### Mishing

We discussed the move from phishing to mishing (mobile targeted phishing) in last year’s report as attackers adopted a mobile-first attack strategy – attacking via the largely unsecured mobile device instead of the largely secured PC device running Windows or MacOS. This year’s data validates that prediction where we observe:

-   incidence of Vishing up 28%[^6]
-   incidence of Smishing up 22%[^7]
-   the rise of PDF phishing via mobile[^8]

In 2024, the United States continues to be the #1 phished region worldwide with zLabs data showing they comprised 44% of mobile phishing targets.

Although mishing can target both consumers and businesses, business compromise via phishing was responsible for $2.9 billion dollars in losses in the U.S. in 2023 according to the FBI’s Internet Crime Complaint Center.

In a business phishing attack, a threat actor impersonates an employee, vendor or other trusted party in an email or other messaging communication and attempts to trick the employee into sharing credentials, privileged information, or some other asset. This shows up in the 2024 data:

> Vishing incidents in Q3 2024 increased more than 28% over Q2 volumes. And smishing incidents – phishing via SMS and text messages – increased more than 22%.[^9]

According to Zimperium's zLabs research team, SMS (smishing) has emerged as the dominant mishing vector, now comprising over two-thirds of observed attack attempts, signifying a critical pivot in threat actor methodology, as presented in Figure 1.

![Pie chart showing Mishing Attack Vectors: SMS 69.3%, PDF 28.4%, QR 2.4%.](Figure-1-Mishing-Attack-Vectors-source-zLabs)

Attackers are always looking for the next vector. In the past year, Zimperium has observed attackers increasingly leveraging PDF attachments delivered via SMS messages because these files can effectively obfuscate malicious content and evade traditional security scans. This tactic exploits the fact that users have become accustomed to and generally trust PDF documents in their daily interactions, and many defense mechanisms may not thoroughly inspect them for embedded threats. To enhance their deception, attackers frequently leverage well-known brands within these malicious PDFs to manipulate user trust, compelling victims to click through and initiate the attack, as demonstrated in Figure 2. This evolution signifies a sophisticated attempt to bypass established security measures and capitalize on user familiarity and trust.

![Screenshot of a mobile phone showing a text message with a malicious PDF attachment, impersonating a well-known brand to trick the user into downloading and activating the PDF.](Figure-2-PDF-Smishing-Attack-Example)

This example is one of many that attempt to trick a user into downloading a PDF document that executes the attack after download and user activation to “view” the PDF.[^10]

A second smishing attack that has surged in volume is one that takes advantage of the widespread prevalence of toll roads in the U. S. This method has received a lot of press attention in recent months.

In this attack the user is told they have an unpaid toll on the widely used EZPass system. This leverages a tool kit that is actively sold via the dark web to enable attackers to easily send text messages to redirect the victim to a phishing site that looks like one for a toll road operator. See Figure 3.

![Screenshot of a mobile phone showing a text message impersonating a toll road operator (EZPass) with a malicious link, designed to trick the user into paying a fake unpaid toll.](Figure-3-Example-of-Toll-Road-Smishing-Attack) [^11]

### Consumer and Enterprise Brands continue to be exploited as part of Mishing Attacks

Attackers continue to impersonate well-known brands as a means to tricking the user into taking risky actions. Phishing typically impersonates regional consumer and enterprise brands to raise the likelihood of the target responding to the phish attempt. These brands boast enormous user bases and have cultivated significant user trust, making phishing attempts appear highly credible and increasing the likelihood of success. Critically, these services are repositories for vast amounts of valuable personal, financial and business-critical data. By compromising accounts on these platforms, attackers can gain access to everything from sensitive emails and cloud storage to financial details linked to shopping or payment services. Access to one of these accounts, particularly email or social media platforms, can often provide a foothold to compromise numerous other linked services.

Most recently, zLabs researchers analyzed a targeted campaign that leveraged a DocuSign impersonation scheme attempting to harvest corporate credentials from company executives.[^12] The analysis of this campaign revealed an interesting attack chain that incorporated advanced evasion techniques, mobile-specific targeted phishing links inside PDF files, and a sophisticated infrastructure designed to circumvent traditional security controls while maintaining a convincing corporate appearance.

The financial incentives are substantial, ranging from direct theft of funds or payment information to leveraging business platforms for larger-scale fraud.

The Top 3 Brands leveraged for mishing by geographic region in 2024 were:

**NORTH AMERICA**
-   Facebook
-   USPS
-   Microsoft Office 365

**SOUTH AMERICA**
-   Facebook
-   Apple
-   Microsoft Office 365

**EMEA**
-   Facebook
-   Crypto Services
-   Microsoft Office 365

**APAC**
-   Facebook
-   Crypto Services
-   WhatsApp

### Mobile Malware

Malware remains a primary weapon for both opportunistic cybercriminals and sophisticated advanced persistent threats targeting mobile devices globally. zLabs research confirms the widespread nature of this threat, finding that 18.1% of devices in our analysis set had mobile malware installed. Figure 4 provides a visual distribution of the prevalent malware types we observed.

![Pie chart showing Malware Family Distribution: Spyware 36.9%, Riskware 25.1%, Trojan 18.0%, Malware 14.6%, Banker 3.4%, Adware 1.0%.](Figure-4-Malware-Family-Distribution)

#### Malware Trends

Analyzing the malware family distribution reveals that Spyware has emerged as the most prevalent malware family throughout 2024. This is a concerning trend, yet aligns directly with the observed surge in mishing attacks. Spyware is insidious by design; it secretly infiltrates a user's device to stealthily gather a wide range of sensitive data – from personal information to device specifics – and exfiltrates it to attackers without the user's consent. Its hidden data-gathering capability makes it a favored tool in campaigns aiming for covert data theft.

Compounding this picture is a significant escalation in Trojan activity. We have documented a striking 50% increase in the deployment of Trojans in attacks compared to activity seen in 2023. This surge is further evidenced by zLabs discovery of multiple dangerous new banker trojan families, including Vultur, DroidBot, Errorfather, and BlankBot. The threat posed by these new variants heavily targets the Android ecosystem, as all but the Errorfather family are specifically engineered for Android devices. The dominance of spyware and the alarming rise of sophisticated, Android-focused Trojans collectively underscore the evolving and increasingly data-centric nature of global mobile threats.

### Sideloaded Apps

Sideloading is the practice of installing mobile apps on a device that are not from the official app stores. This is typically done on a rooted Android device or a jailbroken iOS device. In 2024, the EU DMA resulted in the availability of sideloaded apps on iOS devices, so we are starting to see their presence on iPhones.[^