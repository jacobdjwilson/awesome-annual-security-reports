# The 2024 Duo Trusted Access Report

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [01 Billions of Authentications](#01-billions-of-authentications)
- [Stronger Auth Methods Show Upward Trends](#stronger-auth-methods-show-upward-trends)
- [Return-to-Office is the New Hybrid Work Reality](#return-to-office-is-the-new-hybrid-work-reality)
- [Futureproofing Against Attackers](#futureproofing-against-attackers)
- [02 Attack Surface Increase](#02-attack-surface-increase)
- [The Continuing Rise in Global MFA Usage](#the-continuing-rise-in-global-mfa-usage)
- [Identity is The New Perimeter](#identity-is-the-new-perimeter)
- [The Talos Perspective](#the-talos-perspective)
- [03 Establishing Device Trust](#03-establishing-device-trust)
- [A Diverse Device Environment](#a-diverse-device-environment)
- [Device Visibility: Protecting What You Can’t See](#device-visibility-protecting-what-you-cant-see)
- [Authentication with Out-of-Date Software](#authentication-with-out-of-date-software)
- [04 Powerful Policy Controls](#04-powerful-policy-controls)
- [Learning From When Authentications Fail](#learning-from-when-authentications-fail)
- [Benefits of Strong Device-Based Policies](#benefits-of-strong-device-based-policies)
- [Top 3 Policy Groups to Reduce Security Debt](#top-3-policy-groups-to-reduce-security-debt)
- [+ Closing Words](#closing-words)
- [The Future of Identity Security](#the-future-of-identity-security)
- [Recommendations](#recommendations)
- [Credits](#credits)
- [References](#references)

---

Guide Cisco Public© 2023 Cisco and/or its affiliates. All rights reserved. Cisco Confidential

## Introduction

### The New Frontier of Access Management and Identity Security

In exploring the future, we’re often drawn to predicting the unknown. Our quest for answers is unending, and we rely heavily on data to guide our predictions. Organizations today navigate a treacherous digital landscape where the motives of attackers are as varied as their methods — ranging from financial gains, cyber espionage, and disruption to reputation damage to cyber warfare. Concurrently, these organizations also manage various internal complexities, from the intricacies of their IT stacks to dispersed hybrid workforces and a great variety of devices accessing their systems and applications. This evolution from ad hoc remote work setups to hybrid work models has extended the traditional enterprise perimeter to the far corners of the cyber realm.

Years ago, protecting an IT infrastructure might have been largely about ensuring that systems were running smoothly — the proverbial “keeping the lights on.” Now, the remit has expanded exponentially; it encompasses a vigilant defense against a host of external cyber threats, from ransomware to state-sponsored hacking. As the threat landscape has widened, so has the surface area for attacks, with every employee’s access or device becoming a potential entry point. This shift has transformed IT departments from units concerned primarily with operational uptime to essential guardians against a spectrum of sophisticated external threats.

While we can’t tell precisely what the future will bring, analyzing historical patterns provides insights into future possibilities. For instance, the previous edition of the Trusted Access Report pointed out the soaring adoption of multi-factor authentication (MFA) as companies have been looking to reduce risk in a more advanced security landscape.

As organizations grapple with increasingly sophisticated cybersecurity threats, a demand for holistic access management solutions has been apparent for a few years. MFA is a great security measure, but not enough on its own. More sophisticated threats call for additional layers of security.

By integrating context, an access management solution can analyze the situation in which access is being requested, such as information about the user’s typical behavior or environment including their usual login times, geolocation and device. This adds an additional layer of security, providing a more holistic and dynamic approach to authentication. In essence, adding context to the authentication process allows systems to better differentiate between legitimate users and potential threats, enhancing security while maintaining a good user experience. Thus, context becomes the new form of MFA.

Contextual factors such as location or device details (operating systems, for example) have been included in Trusted Access Reports for years. However, with hybrid work as a firmly ingrained reality, the importance of contextual factors carries even more weight.

Another area where we have detected a rising level of interest is the future of identity; more specifically ways of addressing proliferation of digital identities from the cybersecurity perspective. In the modern workplace, every employee may have multiple digital identities across various systems, applications, and platforms. This can range from email accounts, to access credentials for internal systems, to profiles on collaboration platforms like Slack.

As businesses continue to adopt cloud services, software-as-a-service platforms, and remote collaboration tools, the number of these digital identities grows. This proliferation has significant implications for both productivity and security. On one hand, these identities can enable more seamless collaboration and access to necessary resources, improving efficiency. On the other hand, managing these numerous identities and ensuring they are properly secured becomes a complex task.

Risk visibility across an organization’s identity ecosystem in a single, comprehensive interface has become a must. This can be achieved via identity threat detection and response (ITDR) capabilities. The evolution of ITDR is integral to the future of identity, ensuring that our digital identities remain secure as they become increasingly prevalent in our day-to-day lives.

The challenge is clear: as the MFA usage continues to expand globally, so do attackers’ methods. To minimize chances of a breach, traditional MFA does not only need to be enhanced with contextual factors such as the user’s typical behavior or environment but also the visibility across an organization’s identity ecosystem in a single, comprehensive interface.

## Methodology

In this report, we’ll delve into insights drawn from an analysis of over 16 billion authentications in the last year (and over 44B in the last 4 years), spanning nearly 52 million different browsers, on 58 million endpoints and 21 million unique phones across regions including North America, Latin America, Europe, the Middle East, and the Asia Pacific. We defined our 2023 annual time range as between June 1, 2022, and May 31, 2023.

## Key Findings

### 01 Billions of Authentications

#### MFA continues to strengthen passwords

Multi-factor authentication holds strong while adding to the security of traditional password usage. The number of MFA authentications using Duo rose by 41% in the past year.

#### Push preferred

Duo Push is the most-used authentication method, accounting for 21% of all authentications.

#### Passwordless adoption continues to rise

Account adoption of WebAuthn-enabled factors, including security keys and biometric technology like TouchID, increased by 53% from 2022 to 2023 alone.

![Figure 01 Monthly successful authentications](Image description: A line graph showing monthly successful authentications in billions from September 2019 to May 2023. The graph shows a general upward trend in authentications over time.)

### Stronger Auth Methods Show Upward Trends

The weaknesses of passwords as a sole authentication method are well-documented. They can be guessed, cracked, phished, or stolen, and users often exacerbate these vulnerabilities by reusing passwords across multiple services or creating simple, easily decipherable passwords. In contrast, multi-factor authentication (MFA) mitigates these risks by introducing additional hurdles for potential attackers. Even if a password is compromised, the chances of an attacker also having access to the user’s physical device or biometric information are significantly lower. However, recent high-profile cyber-attacks have shown that simply enabling a second factor does not make an account impenetrable. Not all authenticators are born equal, with factors like FIDO2 security keys and WebAuthn-enabled biometrics proving harder to exploit compared to weaker, but more accessible, factors like SMS text or phone call.

![Figure 02 Authentication percentage over time by factor count](Image description: A stacked area chart showing the percentage of authentications by factor count from June 2019 to June 2023. The chart shows trends for Policy-enabled 2FA, Push, Phone & SMS, OTP, Hardtoken, Other, and WebAuthn/U2F.)

![Figure 03 Percent of accounts using WebAuthn for authentication](Image description: Multiple bar charts showing the percentage of accounts using WebAuthn for authentication across different market segments (Enterprise, Mid-Market, Small and Medium Business, Very Small Business) from May 2019 to May 2023.)

![Figure 04 WebAuthn adoption by market segment](Image description: A line graph showing WebAuthn adoption by market segment (Very Small Business, Small & Medium Business, Mid-Market, Enterprise) from 2020 to 2023.)

Luckily, authenticator apps like Duo Mobile appeal to both demand for higher security and ease-of-use. 91.5% of accounts enable Duo Push, a one-tap authentication available via the Duo Mobile application, accounting for 21% or over 3.2 billion authentications. We also observed a decreasing trend in SMS texts and phone calls as a factor, dipping to an all-time-low with 4.9% of authentications — a 22% decrease from 2022. More secure methods like WebAuthn and hard tokens take their place as the benefits of phishing-resistant MFA and smarter access policies gain traction amongst SMB and enterprises alike.

### Return-to-Office is the New Hybrid Work Reality

![Figure 05 Authentications for Remote Access Applications](Image description: A line graph showing the percentage of authentications for remote access applications from September 2019 to March 2023.)

Remote access applications are software apps that allow a user to remotely access and control another computer or network over the internet or a local network connection. These apps are used for various purposes including troubleshooting, file transfers, remote administration, or accessing files and software on an office computer from a remote location.

Last year, the number of authentications for remote access applications reached nearly 25%. This is lower than pre-pandemic levels after the peak we saw in 2020. The quantity of authentications in this category has continued to decline since then as more companies move staff back into the office. While we observe a lower volume of authentications across the board during the December and January holiday periods, several industries including education, retail, and healthcare spiked during the first calendar quarter.

Let’s set the scene...

With the return of business travel, designated in-office policy, or even just flu season, predictable ebb and flow of authentication requests begin to fluctuate. The cadence breaks as employees take leave, work remotely, or operate on varied schedules. These changes can lead to a surge in remote access requests, with employees reaching out to corporate networks from a multitude of locations and devices, not just their usual work terminals. Consequently, the IT systems must handle an influx of mixed on-premises and off-site login attempts with a greater reliance on VPNs and other remote access technologies.

Moreover, seasonality can also bring about an increase in temporary staff as businesses scale up to meet demand. This influx requires the creation and management of additional temporary credentials, a wave of new entries into the authentication system. Once the season wanes, there’s a corresponding outflow as these seasonal credentials are revoked.

This variance does not merely alter the volume, but also the nature of authentications. There is a heightened need for robust security measures as the risk of cyber threats often spikes during these times. Thus, a layered security approach becomes even more crucial — with MFA as a minimum requirement.

During these peak times, the IT environment’s authentication protocols must be both elastic and secure, expanding to accommodate the increased and varied load while maintaining the integrity of the system. IT staff remain on high alert to watch for any anomalous activity that could signify a breach attempt.

### Futureproofing Against Attackers

The identity threat landscape is rapidly evolving, and trusted identity providers have fallen under attack. According to CISA, attackers are actively exploiting identity policy gaps to gain access to critical applications. Regardless of the increased risk, 85% of organizations feel they are not prepared and ready to protect themselves against modern attacks according to the Cisco Secure Readiness Index study³.

Visibility across the identity infrastructure is a must-have when addressing the types of attacks adversaries concoct. While there’s been a significant uptick amongst MFA authentications through Duo, another piece of research suggests that security gaps are still across the market: the average company has 40% of accounts with either no MFA or weak MFA⁴. Especially in periods of change, strong access management and identity visibility is critical. For brief moments you might strike the right balance, only to be disrupted by new and emerging threats, changing user behavior, and a complex IT environment.

This is why modern security initiatives require continuous monitoring across identity, critical applications, and human resources information system (HRIS) versus a “set it and forget it” approach. As the security landscape evolves, many businesses are adopting a zero trust access policy strategy to mitigate modern attack surfaces. Organizations with a mature zero trust implementation score 30% higher in security resiliency than organizations without a zero trust strategy⁵.

In 2023, we saw a proliferation of two specific types of MFA-targeting attacks taking advantage of push-based authentications and unassuming users:

1.  **Push harassment**: Multiple successive push notifications to bother a user into accepting a push for a fraudulent login attempt.
2.  **Push fatigue**: Constant MFA means users pay less attention to the details of their login, causing a user to mindlessly accept a push login request.

Duo already supports WebAuthn FIDO2 authenticators, which offer the strongest protection against MFA-based attacks. However, we know that rolling passwordless out across an organization is a journey. It’s encouraging to see that Duo Verified Push, a more flexible step-up factor that became generally available to all Duo customers during the data period of this report, was enabled on over 5,600 accounts.

As attackers’ techniques become more sophisticated, a multi-layered defense system is crucial. Trust in users is essential, but no longer enough. The addition of outside vendors and contractors adds complexity to closed, managed endpoint-only access policy. Duo Trusted Endpoints, made available to all Duo editions, adds an extra layer of security even if an organization cannot manage the device directly. Administrators can define a trust policy for every endpoint—whether managed or unmanaged, company-issued, contractor-owned, or personal—and stop attacker’s unknown devices even if they are able to bypass MFA.

Increased friction often appears as a challenge to user adoption. As part of balancing security with productivity, we enhanced Duo Remembered Devices to account for changes in risk: when we recognize the device a user is on, we use a securely generated device token to authenticate so long as trust is maintained.

While access security should be tailored to the level of risk, organizations can struggle to get buy-in to add friction for every login. Duo’s Risk-Based Authentication solution addresses this challenge—only stepping up to the more secure method when environment risk signals indicate there are potential threats, like location anomalies or known attack patterns. Whether security teams enable Verified Duo Push for all users, or through a risk-based approach, this allows organizations to make access security decisions based on their risk appetite and organization’s needs.

IT teams must ensure that their Identity Security program is built on a strong foundation with the right tools, like strong MFA factors and intelligent step-up. Once these tools and policies are in place, Identity Threat Detection and Response (ITDR) can bolster an organization’s identity security posture by arming the IT security professionals with both proactive and reactive tools.

ITDR helps proactively detect policy misconfigurations, identity-provider-to-HRIS discrepancies, and excessive privileges. It can also catch high-risk scenarios such as dormant or inactive accounts and accounts with MFA disabled—a trend noted in the 2023 Cisco Talos ‘Year in Review’ Report⁶. On the reactive side, the tool equips IT teams to respond to suspicious activities such as new MFA device registration, risky SSO sessions, superman (unrealistic travel) logins, access from a new device or location and more.

Footnotes:
1.  See “Cisco Cybersecurity Readiness Index,” which categorizes companies into four stages of readiness: from Beginner, to Formative, Progressive, and finally Mature, based on their preparedness across five key pillars and the state of deployment of 19 security solutions within those
2.  From the State of Identity Security report (Oort), see Section 2 “Multi Factor Authentication: Full Coverage Remains Elusive”
3.  Read more findings from the Security Outcomes Report, Vol 3 published by Cisco (Renner)
4.  Read all Cisco Talos Year in Review

## 02 Attack Surface Increase

### The Continuing Rise in Global MFA Usage

Data shows that the global customer base protected by Duo’s multi-factor authentication security is continuing to grow. The number of MFA authentications using Duo rose by 41% in the past year, with countries like Germany seeing a 52.3% increase in authentications year over year. In the Asia-Pacific region, Japan, the Philippines, and Australia saw continued growth from last year, increasing by 28%, 24.9%, and 16.9% respectively. For the first year measured, Brazil makes the third highest increase in authentications seeing 26.3% more MFA usage from 2022.

This indicates a rising trend in the recognition of the importance of enhanced security measures predominantly as a response to a rising volume of cyber threats, but also as a reflection of international compliance requirements such as GDPR, C5, AgID, or HIPAA.

![Figure 06 The top 10 countries that experienced an increase or decrease by authentication volume based on access device IP address](Image description: A bar chart showing the percentage increase or decrease in MFA authentications using Duo in various countries over the past year. Countries with increases include Germany, Japan, Brazil, Philippines, Australia, Canada, United States, Singapore, United Kingdom, and India. Countries with decreases include Israel, Netherlands, El Salvador, Kenya, Taiwan, Ireland, Hungary, Hong Kong, Jamaica, and China.)

![Figure 7 Average number of different countries accessed by organizations of a particular country](Image description: A bar chart showing the average number of different countries from which users authenticate for organizations in various countries. Hong Kong has the highest average, followed by the United Kingdom, United States, and Canada.)

An internationally dispersed workforce means more employees, contractors, clients, and third parties can access the organization’s business’s digital infrastructure from various locations, often on different devices, networks, and operating systems which can introduce additional vulnerabilities. Data and resources can be accessed from a greater scale of networks and endpoints. This helps support the concept that ‘identity is the new perimeter’ and ‘context is the new MFA.’ Identity security is a forever evolving problem and it’s a daunting task for organizations to plug every hole the user journey creates.

In addition, an international presence does not only increase the variety in technology stack, but it can also add a wider array to the physical challenges of a more geographically diverse user base. Also, IT systems must cater to mixed tech stacks and varying data protection and privacy laws. This pushes the complexity that IT teams need to deal with yet another notch.

Globalization, like the organization size, increases the probability of a presence of more than one identity provider. Moreover, large organizations may acquire other companies, each of which may have its own existing identity provider. Instead of consolidating everything under one identity provider, which can be complex and disruptive, organizations sometimes choose to maintain multiple identity providers.

Managing identities increases in complexity with greater probabilities of supporting more than one identity provider (IdP). Without proper security measures in place, this can lead to potential security gaps or vulnerabilities that can be exploited for identity-based attacks like compromised credentials.

Global business practice requires broader, vendor-agnostic access management that helps organizations detect, respond to, and report attacks.

### Identity is The New Perimeter

Identity security is a key part of access management. Securing and verifying identities allows an identity and access management (IAM) system to manage access to resources effectively and securely. Because of this, it’s important to spend a few moments highlighting identity-security trends that have come to light when we were pulling together this report.

There are a few reasons why gaps in identity security occur. For some companies, the prompt comes from cloud migration. As companies grow and move their operations to the cloud, they often need to introduce new IAM systems but do not completely deprecate older IAM systems. For other companies it is migration from an on-premises directory to a cloud-based directory but keeping both. And the third group is composed of companies that have acquired one or more companies and support numerous identity platforms.

Another contributing factor comes in the form of operational challenges. Identity security often falls under the IT function and may not receive the attention and resources it needs to be effective. It requires investment in technology and personnel to manage and continuously monitor the IAM systems, ensure compliance with regulations, and respond to security incidents.

For some, cloud migrations and organizational scaling require the introduction of new IAM systems. Mergers and acquisitions, operational globalization, and a geographically diverse user base add even more complexity to keeping track of authenticating identities.

In the face of digital transformation, identity security may suffer from a lack of resources or prioritization — typically bucketed as an IT function rather than a security one. Without proper visibility and threat detection, identity infrastructure provides ample opportunity for attackers to gain entry to critical systems. Identity has traditionally been managed by an organization’s IT teams. With identity being a top attack vector, it’s critical to bring together identity teams and the Security Operations Center (SOC) with ITDR so everyone is on the same page.

> Without proper visibility and threat
> detection, identity infrastructure provides
> ample opportunity for attackers to gain
> entry to critical systems

### The Talos Perspective

Cyber attackers are agile and often backed by substantial resources, including state sponsorship. This has led to an increase in advanced persistent threats which can target identities to gain access to sensitive information.

But this is nothing new. Attackers have targeted identities in their campaigns for many years. For example, on-premises identity directories or VPNs that lack additional protections have fallen victim to several attacks. Managing an increased range of identities is also an indicator of expanded attack surface. Talos Incident Response (Talos IR) has repeatedly seen attackers targeting vendor and contractor accounts (VCAs), which typically have expanded privileges and access. VCAs are often overlooked during account audits due to trust placed in the third party, making them an easy target for attackers.

The Talos 2023 Year in Review report saw compromised credentials on valid accounts making up 23% of initial access vectors, with use of valid accounts as the second-most common MITRE ATT&CK technique observed⁷. While one major vulnerability is improperly implemented MFA or lack thereof, in some engagements attackers were able to bypass MFA through MFA fatigue or push bombing attacks. ITDR can help surface the risks associated with valid account attacks and help correlate information from HRIS to identity providers and critical applications to help mitigate low-hanging fruit credential attacks.

#### Identity sprawl

Organizations are struggling with “identity sprawl,” which occurs when users have numerous accounts and identities managed by multiple systems that are not synchronized. This presents a continuous security risk and operational challenge for many security and IT teams.

Identity sprawl is a growing challenge. Talos IR research noted that it was challenging to identify how the credentials were compromised considering they were obtained from devices outside the company’s visibility, such as saved credentials on an employee’s personal device. One report shared that on average, companies have 340.5 personal accounts (Gmail, Yahoo, Hotmail, iCloud, etc.) with access to company data⁸. With the BYOD and perimeter-less work culture, a growing quantity of employee identities goes unchecked or unmanaged.

*   23% of initial access vectors consisted of compromised valid account credentials
*   340.5 Personal accounts accessing company data, on average

Footnotes:
7.  From Talos IR 2023 Year in Review, see “Telemetry Trends” pg. 6-7
8.  From the State of Identity Security report (Oort), see Section 3 “Identity and Access Management: Poor Hygiene Enabling Attackers”

## 03 Establishing Device Trust

Gaining visibility into and securing myriad devices is still an ongoing battle, especially for organizations and industries that see a large diversity of endpoints such as higher education. Strong authentication mechanisms are at the heart of the security protocol — an essential line of defense in confirming the identities of users accessing the network. However, robust authentication is just one piece of the cybersecurity puzzle.

Ensuring users are using trusted devices and networks to access corporate data adds another layer of complexity. IT environments with complex supply chain operations, third-party partnerships, and contractor devices introduce risk of outside, unmanaged devices and unknown endpoints. This variability makes it challenging, if not impossible, to guarantee visibility and trust without a dedicated layer of security. Even with strong end-user authentication, the uncertainty of unmanaged network and device security remains a vulnerable chink in the armor.

In this context, identity-centric security is a dynamic and multifaceted endeavor. It demands a strategy that is comprehensive and adaptive, integrating advanced authentication, network security solutions, endpoint protection, continuous monitoring, and an informed and conscientious workforce.

### A Diverse Device Environment

The starting point for establishing device trust is gaining a comprehensive understanding of the devices themselves — their operating systems, the browsers they use, their patch levels, and their compliance with corporate security policies. This understanding is critical because the security posture of any device is heavily influenced by the currency and integrity of its OS and browser. Outdated software can be riddled with unpatched vulnerabilities that are ripe for exploitation, turning an unassuming device into a Trojan horse within the network.

To determine if a device can be considered trustworthy, IT and security teams must be able to answer several key questions:

*   Are there any unauthorized applications or software present?
*   Is the device encrypted, and are its security settings configured according to the enterprise’s standards?
*   What OS is the device running?
*   Is this OS still supported and receiving security updates?
*   What browser versions are installed, and are they set to update automatically?

First, let’s take a look at the browsers and OSes Duo customers use:

Mobile and non-traditional operating systems platforms show steady adoption, making up 61.8% of measured authentications. While we find that Windows is still the frontrunner, mixed IT environments can lead to more platform-agnostic security considerations.

**Mobile OS Usage**
*   iOS: 71.7%
*   Android: 28.2%

**Top OS**
*   Windows: 38.2%
*   iOS: 33.4%
*   Mac OS X: 13.7%
*   Android: 13.1%
*   Chrome OS: 1.1%
*   Linux: 0.45%

While Windows continues to lead the pack, we note that iOS is a strong second at 33.4% in the overall listings. Apple continues to rule the roost in the mobile category with the nearest contender being Android, which has a far lower adoption rate at 28.2%.

![Figure 8 Different browsers used for authentication](Image description: Two sets of bar charts showing the percentage of desktop and mobile authentications by browser. Chrome is the dominant desktop browser, while Mobile Safari is the dominant mobile browser.)

![Figure 9 Percentage of mobile browsers used](Image description: A stacked area chart showing the percentage of mobile browsers used from 2020 to 2023. Mobile Safari consistently accounts for the largest share.)

IT environments that have a wider diversity of systems and browsers have a more pressing need to adopt more stringent device-based policies.

### Device Visibility: Protecting What You Can’t See

Maintaining device trust is a continuous process, requiring regular assessments and updates. This might involve automated compliance checks that verify whether a device is operating within the set parameters before granting access. Should a device fall short — say, running an OS version that’s no longer supported — it can be flagged for review, blocked from accessing sensitive resources, or provided with limited, controlled access to mitigate potential risks.

This is important as applications and browsers like Google Chrome up the frequency of patches, accounting for performance and security bug fixes on a weekly basis. But how often are people relaunching and updating their applications? Of the 16 billion authentications measured, 62% of non-mobile authentications are attributed to the Chrome browser. The ability to see access device patch levels and prompt users to self-remediate out-of-date devices grows even more critical.

Visibility can be achieved through various tools and practices. Endpoint management systems, for instance, offer dashboards that provide real-time insights into the status of every device connected to the network. Automated inventory tools can keep track of the devices in use, their software versions, and their patch history. This monitoring is essential not just for ongoing management but also for responding to potential security incidents with speed and precision.

### Authentication with Out-of-Date Software

**Out-of-date failures**

The percentage of failures due to out-of-date devices increased by 74.7% in 2023. This is despite the fact that the percentage of organizations with policies governing out-of-date devices decreased by 6.9%. The Asia-Pacific region ranked highest, with 3.8% of authentications occurring on an out-of-date browser.

![Figure 10 Typical (geometric mean) percentage of successful authentications using out-of-date browsers](Image description: A bar chart showing the typical percentage of successful authentications using out-of-date browsers by region (APAC, AMER, EMEA, LATAM).)

The core of device trust lies in the ability to achieve complete visibility over the devices that are requesting access to corporate applications and data. In the ever-evolving geography of digital threats, authenticating within an IT environment that relies on outdated software is akin to navigating a ship with an old map.

Outdated software often contains unpatched vulnerabilities, which are like hidden, open backdoors for cyber attackers. These vulnerabilities are well-documented and easily exploitable as they stay in the public domain, providing a treasure map for malicious entities to gain unauthorized access. In this scenario, each authentication event is a gamble, increasing the chances that a security flaw can be used to compromise credentials.

Moreover, software that is past its support life no longer receives updates from its developers. This means that even as new threats emerge, the authentication mechanisms stay static and become increasingly ineffective against the sophisticated techniques employed by modern cyber adversaries. It is a static defense against a dynamic offense.

![Figure 11 OS diversity and percentage of authentications that use an out-of-date operating system](Image description: A scatter plot showing OS diversity on the x-axis and the proportion of authentications with out-of-date OSes on the y-axis. The plot illustrates a correlation between OS diversity and the likelihood of using out-of-date OSes.)

OS (Shannon) Diversity

The horizontal axis represents how “diverse” (in the ecological sense) a set of OSes is used to authenticate within an organization. A higher number means a wider variety of OSes that share an equal proportion of authentications. On the vertical axis is the proportion of authentications made with out-of-date OSes. The line across the bottom shows organizations that enforce OSes to be up to date, and the vertical line on the left shows organizations that use only a single OS.

Based on the data in Figure 11, the correlation shows that the more operating systems an organization allows to authenticate, the more likely it is those authentications will occur with an out-of-date OS. This becomes a fast reality for those expanding IT environments

To rely on outdated authentication software is to walk on a tightrope without a safety net. It’s an open invitation to security breaches, data theft, and the many consequences that follow. For an IT environment to remain secure and effective, it is imperative to invest in current, robust device trust methods that evolve in lockstep with the landscape of digital threats, providing visibility and enabling remediation. This is not just best practice; it is a fundamental tenet of responsible IT management in the digital age.

On Encryption & Firewall…

With the hybrid work model, organizations must also consider the use of virtual private networks (VPN), application of strict firewall policies, enforcement of data encryption, and secure setup of home networks. We looked at Duo Endpoint Health, particularly seeking to find out if organizations were generally increasing or decreasing their use of various protections. On an organization-by-organization basis, we see that, on average, organizations increased the percentage of encryption usage by 69%.

Device hygiene for the enterprise is an ongoing, evolving requirement, not a set-it-and-forget-it policy. This responsibility extends to the end-of-life process for devices, ensuring that all data is securely wiped and that devices are disposed of in a manner that does not pose a security threat. Similarly, user access levels must be adjusted to mitigate unnecessary or excessive privileges. Regular audits and compliance checks ensure that device and identity hygiene practices are not just in place but are effectively enforced and updated.

By diligently managing and monitoring operating system and browsers, among other device attributes, organizations can enforce a strong security posture and ensure that trust is not blindly given, but is based on verifiable, compliant device behavior.

## 04 Powerful Policy Controls

In a previous section, we highlighted the critical challenge of security debt — an accumulation of unaddressed risks and vulnerabilities that an organization must manage. Security debt can arise from various sources such as outdated software, legacy systems, technical shortcuts, and the delayed application of security patches. Reducing this debt is essential for maintaining a robust security posture and minimizing the organization’s exposure to potential breaches.

One of the most effective strategies for mitigating security debt is through the comprehensive management of risk. This includes identifying, assessing, and prioritizing the vulnerabilities within an organization’s IT infrastructure. By understanding where the greatest risks lie, an organization can allocate resources and efforts more effectively to address the most pressing security concerns first, thereby reducing the overall security debt.

### Learning From When Authentications Fail

When reviewing the policy data, we uncovered some notable findings. In a move towards stronger methods of authentication, Duo Push-based authentication was present in 99.3% of all global policies. Mobile one-time passcodes were in 91.4% of policies defined. One of the more interesting findings was that WebAuthn was in 69.2% of the global policies.

It is just as important, if not more so, to measure the authentications that failed. It was noted that 5% of all measured authentications were ones that failed. When we further examined the data, we discovered that 28% of the failed authentications were due to the users not being enrolled in the system.

![Figure 12 Percent of authentication failure reasons](Image description: A bar chart showing the percentage of authentication failures by reason, including Deny unenrolled user, User not in permitted group, Location restricted, Denied network, Out of date, Invalid device, Version restricted, Anonymous IP, No screen lock, and No disk encryption.)

![Figure 13 Percent of authentication failure reasons](Image description: A bar chart showing the percentage of authentication failures by policy, including Invalid Device, No screen lock, Denied network, Out of date, Anonymous IP, Version restricted, No disk encryption, and Location restricted.)

Here we see that even though a little less than 1% of organizations have a policy concerning location, they account for a substantial proportion of failures. In removing failures caused by user enrollment, we can zoom in on those failed authentications influenceable by policy settings.

### Benefits of Strong Device-Based Policies

A cornerstone of this risk reduction strategy is the implementation of uniform security policies across all assets in the environment. Device-based policies are especially critical because they provide a consistent security framework that applies to every device within the organization, irrespective of its location or user. These policies can control various aspects of device security, including the enforcement of strong authentication measures, the application of regular patches and updates, the configuration of firewalls and antivirus software, and the management of user privileges.

Uniform device-based policies are beneficial for several reasons:

*   **Consistency**: They ensure that every device adheres to the same security standards, which helps to cut weak links in the security chain that attackers might exploit.
*   **Scalability**: As the organization grows, new devices can be brought into the fold with established policies automatically applied, making it easier to manage security at scale.
*   **Compliance**: Device-based policies help organizations meet regulatory requirements by ensuring that all devices are compliant with industry standards and laws, reducing the risk of fines and other penalties.
*   **Automation**: These policies can often be enforced automatically, reducing the need for manual intervention and the associated human error.
*   **Visibility and Control**: Implementing uniform policies aids in the monitoring and control of device security, as deviations from the policy are easier to detect and remediate

### Top 3 Policy Groups to Reduce Security Debt

While reducing security debt is a complex, multifaceted endeavor, the foundation of this effort lies in the consistent application of comprehensive device-based policies. Such an approach addresses the security debt at its root, reducing risk and fostering a more secure, resilient organizational environment.

The interplay between access devices and security policies is a critical facet of an organization’s cybersecurity framework. Rigorous security policies are set in place to ensure that devices attempting to access corporate resources meet certain standards of security before they are granted entry into the network. When a device does not meet these prescribed criteria, it triggers a series of automated responses aimed at safeguarding the organization’s digital assets.

Duo’s data shows that organizations that implement device-based policies most commonly block access from locations they consider unsecure