# 2023 Mobile Security Index

## Table of Contents
- [Introduction](#introduction)
- [What’s at risk?](#whats-at-risk)
- [Plenty of stones left unturned](#plenty-of-stones-left-unturned)
- [Users and behaviors](#users-and-behaviors)
- [The complacency problem](#the-complacency-problem)
- [The danger of security fatigue](#the-danger-of-security-fatigue)
- [Is working from home here to stay?](#is-working-from-home-here-to-stay)
- [Users not as savvy as they think](#users-not-as-savvy-as-they-think)
- [Phishing is still a popular pastime](#phishing-is-still-a-popular-pastime)
- [Balancing security and user experience](#balancing-security-and-user-experience)
- [Applications](#applications)
- [Malware](#malware)
- [Ransomware](#ransomware)
- [Balancing security and freedom](#balancing-security-and-freedom)
- [Devices and things](#devices-and-things)
- [BYOD](#byod)
- [Device loss/theft](#device-losstheft)
- [SIM theft](#sim-theft)
- [Internet of Insecure Things?](#internet-of-insecure-things)
- [Balancing security and privacy](#balancing-security-and-privacy)
- [Networks and clouds](#networks-and-clouds)
- [Home Wi-Fi](#home-wi-fi)
- [Public Wi-Fi](#public-wi-fi)
- [Clouds](#clouds)
- [5G](#5g)
- [Balancing security and cost](#balancing-security-and-cost)
- [Conclusion](#conclusion)
- [Contributors](#contributors)

---

### Who should read this white paper?
We produced this Verizon Mobile Security Index white paper to help security professionals, such as chief information security officers (CISOs), assess their organization’s mobile security environment and calibrate their defenses. This report is also relevant to anyone involved in the specification, procurement or management of IT devices and services.

### Definitions
Security terms like “attack” and “breach” are often used interchangeably. For clarity and precision, we’ve used the following definitions throughout this report:

- **Attack**: A general term covering any deliberate unauthorized action toward a system or data. This may be as simple as attempting to access it without permission.
- **Compromise**: A successful attack that results in a system’s defenses being rendered ineffective. This could involve data loss, downtime, other systems being affected or no detrimental effects at all. It could be malicious or accidental.
- **Data breach**: An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party.
- **Exploit**: A definition, often in the form of a script or code, of a method to successfully leverage one or more vulnerabilities to access a system without proper authorization.
- **Incident**: Any form of security event, malicious or not, successful or not. This could be anything from a failed authentication attempt to a successful compromise and data breach. It includes non-malicious events, such as the loss of a device.
- **Risk**: A measure of the likelihood of a threat, an organization’s vulnerability to said event and the scale of the potential damage.
- **Threat**: Any danger that could impact the security of systems or privacy of data. This can apply to a technique, such as phishing, or an actor, such as an organized criminal group.
- **Vulnerability**: A weakness that could be exploited. It may be known or unknown—to the manufacturer, developer, owner or the world.

## Introduction
The statistics are sobering: 61% of CISOs (and 53% of CEOs) think that their organization is unprepared to cope with a targeted cyberattack in the next 12 months.[^1] With mobile devices now making up a large part—even the majority—of the device estate, mobile security is more important than ever.

Those managing security must protect a growing number and diversity of endpoints. Increasingly, those endpoints are mobile or using mobile connectivity. Bring-your-own-device (BYOD) policies, hybrid working and the proliferation of Internet of Things (IoT) have multiplied the scale and complexity of protecting endpoints.

In this report, we’ll look at some of the biggest threats to mobile devices—from the phone in your pocket to the predictive maintenance sensors on a 5-ton steel press.

[^1]: Proofpoint, Cybersecurity: The 2023 Board Perspective, 2023

## What’s at risk?
One of the reasons why mobile devices likely don’t get the attention that they deserve is that people focus on what’s on the device. But it’s not just what’s on the device that businesses have to worry about. As of 2022, 60% of all corporate data was stored in the cloud.[^2]

Mobile phones make an attractive target in a similar way to a wallet. The greatest potential value of compromising the device is the entry point it could offer to the company’s “crown jewels”—its customer data, intellectual property and other secrets.

**4 cons of mobile device security:**
- **Convenience**: The portability of mobile devices can make them easier to steal.
- **Connections**: Mobile devices typically connect to more networks—often insecure public ones.
- **Control**: Organizations often have less visibility of mobile devices and they’re often less well-protected than endpoints like servers.
- **Content**: Users often blur the lines between work and personal tasks when using mobile devices.

[^2]: Lookout, The State of Remote Work Security, 2023

## Plenty of stones left unturned
Unsurprisingly, headlines about security breaches tend to focus on the impact. What isn’t discussed very often is what happens between when a company’s systems are first compromised and when the attackers’ presence is detected.

![Chart showing time to detect intrusion]

**4 ways attackers can exploit access:**
1. **Persistence**: Lying low and staying alert can yield results.
2. **Lateral movement**: Cybercriminals will often use the access they’ve gained to move from system to system until they find something valuable.
3. **Impersonation**: Attackers can exploit this to access other systems, change payment details and more.
4. **Credential elevation**: Attackers can use a set of compromised credentials to compromise other credentials with greater access.

## Users and behaviors
The enormous increase in the functionality of mobile devices has fundamentally altered how we think about work. The first challenge is that the separation between work and personal device use has all but evaporated.

### The complacency problem
Despite improvements in cybersecurity training over the years, many users are not well-informed about the risks associated with mobile devices. Nearly half (49%) of users think that clicking on a malicious link or opening a malicious attachment can only affect their device.[^3]

[^3]: Proofpoint, State of the Phish 2023, 2023

### The danger of security fatigue
Fatigue is a serious concern. The risks of security fatigue are demonstrated by the increase in cyber-insurance claims connected with multifactor authentication (MFA) spamming attacks.

### Is working from home here to stay?
Not long ago it seemed like working from home could become the norm. But now, lots of companies are encouraging—in some cases forcing—workers back to the office.

### Users not as savvy as they think
Proofpoint has been tracking the awareness of cybersecurity among users and has generally seen an upward trend. Yet, the evidence shows otherwise. IBM’s X-Force Threat Intelligence Index found that 53.2% of victims clicked on the link in a simulated targeted phishing attack.[^4]

[^4]: IBM, 2022 X-Force Threat Intelligence Index, 2022

## Phishing is still a popular pastime
The 2023 DBIR reported a doubling of “Social Engineering” incidents, largely due to the use of pretexting.

![Chart showing analysis of users clicking on dangerous links]

## Balancing security and user experience
As remote working increases and workloads shift to the cloud, many are turning to approaches based on zero trust and secure access service edge (SASE). These approaches are designed for the hybrid-working, cloud-first, mobile-first and perimeter-less world of today.

## Applications
### Malware
Nearly 1 in 10 (9%) organizations were hit by mobile malware in 2022.[^5] Check Point identified a “vast increase in the number of malicious applications infiltrating Google and Apple stores.”

[^5]: Check Point, 2023 Cyber Security Report, 2023

### Ransomware
Over the past few years, ransomware has risen faster than a K-pop band. It can take many forms: crypto ransomware, lockers, scareware and doxware.

## Balancing security and freedom
To find the right balance, it’s important to cultivate a security-aware culture. Regular training sessions can educate employees on the importance of security measures, turning them into proactive defenders rather than potential vulnerabilities.

## Devices and things
### BYOD
The vast majority of organizations with a bring-your-own-device (BYOD) program give employees a stipend. A study by Oxford Economics and Samsung found that this is generally in the region of $30 per month to $50 per month.

### Device loss/theft
According to the 2023 Verizon DBIR, the loss of devices continues to dramatically outweigh theft.

### SIM theft
SIM theft, not to be confused with SIM swapping, is the robbery of a SIM card with the intent to use it for unauthorized calls or data.

### Internet of Insecure Things?
Securing IoT devices is one of the most challenging aspects of mobile device security. Attacks targeting IoT devices are rapidly evolving as the number of devices grows, the power of devices increases, and the applications become more mission-critical.

## Balancing security and privacy
Whether a company operates a BYOD policy or not, there’s an inherent conflict between work and personal use. Half (50%) of users checked personal email/messaging apps on their work device(s).

## Networks and clouds
### Home Wi-Fi
A staggering 71% of users don’t change the default password on their home Wi-Fi.

### Public Wi-Fi
The vast majority (90%) of remote workers access corporate resources from locations other than their home—the average is five different locations.

### Clouds
Security is often cited as a limiting factor—43% believe that the risks are more significant when using the public cloud versus an on-premises environment.

### 5G
With speeds measured in gigabits per second, single-millisecond latency and unlimited data plans, 5G is poised to disrupt how users—consumers and businesses—use mobile devices.

## Balancing security and cost
There’s always a balance to be found between security and cost. New options could change the dynamics and redefine the value equation, such as connected laptops or Fixed Wireless Access (FWA).

## Conclusion
As businesses have evolved, mobile devices have become indispensable tools. They serve as vital entry points to a company’s key systems, data and cloud-based resources. They can also put these resources at risk. Effectively protecting mobile devices entails leveraging solutions that provide robust security while ensuring seamless user experience.

## Contributors
- Akamai
- Allot
- Check Point
- Fortinet
- IBM
- Ivanti
- Lookout
- Proofpoint