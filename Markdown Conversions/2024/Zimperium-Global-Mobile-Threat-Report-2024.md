# GLOBAL MOBILE THREAT REPORT 2024
## The Rise of a Mobile-First Attack Strategy

[TOC]

1
Executive Summary 
2
The Enterprise Mobile Footprint 
4
Global Threat Landscape 
8
8
9
     9
10
Threats Enterprises Must Prioritize 
11
     From Phishing to Mishing! 
11
     Industries Targeted by Phishing 
15
 Mobile Malware: Advanced Attacks 
15
     Malware Families by Region 
   17
     Unsecured Networks 
18
The Sideloading Saga                  
20
     Why Sideload Apps 
20
     Sideloaded Malware Family Distribution 
    21
     Sideloaded App Attack Chain on Android 
    21
     Sideloading on iOS 
 21
Application Vetting 
23
     Third-Party Work Apps 
23
     Where is my enterprise data going? 
23
     24
     Does the app have secure communication? 
 25
     In-House Developed Apps 
26
     Are the apps easy to reverse-engineer? 
    26
     Is the Third-party code safe? 
 27
     Personal Apps From Public Stores 
28
     Apps Removed From Stores 
28
     Personal VPN Apps 
31
     Platform & OS Vulnerabilities 
32
Conclusion 
        34
Table of Contents
Sources
        35
About Zimperium
        36
8
Key Stats 
Top Threats By Platform 
Top Threats in Public Sector 
Top Threats in the Private Sector By Vertical          
Top 3 Drivers 
Is the app asking for dangerous permissions? 
2
  
82%
of organizations
 
allow BYOD

# Executive Summary

The exponential growth of mobile devices including mobile phones 
and tablets that have access to critical business applications and 
data has empowered and enabled workers and enterprises across 
the world. However, evidence shows that security controls and 
policies have not kept pace with the evolving threat that this may 
pose. More than half of organizations(54%)in a recent study 
experienced a data breach 
<sup>1</sup> due to employees' inappropriate 
access to sensitive and confidential information on their mobile 
devices. It seems that cybercriminals and other bad actors have 
recognized the opportunity that lies within this new mobile-
focused environment.

Organizations continue to strike a balance between Bring Your Own Device (BYOD) and Corporate-
Owned, Personally Enabled (COPE).  According to Samsung about 15% of businesses issue mobile devices 
to all employees, while 39% of companies rely fully on a Bring Your Own Device (BYOD) approach. 
<sup>2</sup> The 
remaining 46% of businesses take a hybrid approach, providing devices to some employees while 
allowing others to use their own. This dual use, however, presents a high risk of data exposure and 
enterprise infiltration due to the sophistication of mobile threats today which are beyond the capabilities 
of traditional MDM and MAM solutions. Employees increasingly expect the flexibility to use mobile devices 
for work, while businesses seek to maintain control over corporate data. 

The ubiquitous nature of mobile applications on enterprise devices exacerbates this complexity. This 
enterprise app footprint comprises apps developed in-house or from a third-party and personal apps 
installed from the public store. Enterprise apps can be for employees, partners, or customers.  Having 
both enterprise and personal apps on the same device create unique security risks. Enterprise apps 
often handle sensitive corporate and customer data and may have vulnerabilities, particularly third-
party apps. Personal apps downloaded from public app stores can introduce malware or exploit 
platform vulnerabilities, potentially compromising enterprise apps and in-app data.

Over 40,000 applications from these groups were reviewed, 
and the top violations were Insecure Communication (76%) 
and Insecure SSL/TSL (27%) on iOS. On Android, Leaky Storage 
(53%), Insecure Communication (59%), and Dynamic Data 
Leakage (31%) are major security issues.

*All statistics in this report, unless otherwise noted in a footnote, are from Zimperium Labs research.*

Contrary to perception, app stores are not responsible for preventing every malicious app from getting in 
or protecting apps from abuse. With more than 300 public app stores, 1,300 device manufacturers, and 
constant OS updates, enterprise mobile device risk postures become very dynamic.  Because so few 
enterprises prioritize the security of mobile apps and devices, this becomes the attack surface of choice.

Recognizing these vulnerabilities, attackers have adopted a 
“mobile first” attack strategy as mobile 
presents a large, unsecured, and unmanaged attack surface for entry to the network and to corporate 
data.

Concentrating on these key areas allows enterprises to take decisive steps to neutralize the most 
significant risks and protect their mobile environments from risks, threats, and attacks. 

*   **Mishing (Mobile-Targeted Phishing Attacks)** - 83% 
of phishing sites specifically targeted mobile devices
*   **Mobile Malware** - unique malware samples increased 
by 13% over the previous year
*   **Sideloaded Apps** - threats from sideloaded apps are 
dominated by riskware and trojans (which total 80% 
of observed malware)
*   **Platform Risks** - 14% of Android devices and 1% of iOS 
devices monitored in today's enterprises cannot be 
upgraded, leaving them susceptible to exploitation
*   **OS Application Vulnerabilities** saw a surge in privacy 
vulnerabilities around data storage, privacy controls and 
app supply chain security

# The Enterprise Mobile Footprint

## Enterprises are more mobile than ever

As of 2024, there are approximately 6.8 billion smartphone users worldwide. If we include all mobile 
devices—such as tablets, feature phones, and wearables—the number exceeds 16 billion connected 
mobile devices globally.  This figure reflects a world where many people own multiple mobile devices and 
where the internet of things (IoT) is increasingly integrated into daily life. According to IDC,  nearly 60% of 
the U.S. workforce today are mobile, frontline workers -- employees who don’t require a desk or an office to 
do their work. This estimate includes both corporate-issued devices and personal devices used for work 
purposes, as the majority of organizations believe that mobile is critical to enhancing worker productivity 
and fostering business growth.  As a result, mobile workforces, remote work, and enterprise mobility 
initiatives have grown exponentially, allowing mobile devices to access more data and interact with more 
enterprise systems every year.

In addition to smartphone’s very large global use footprint the devices possess more processing power 
than most of today’s PCs and are more powerful than mainframe computer NASA used to send astronauts 
to the moon. 

*Image Description: A line graph titled "Desktop vs Mobile vs Tablet Market Share Worldwide from Jan 2009 - Aug 2024". The graph shows the market share of Desktop, Mobile, and Tablet devices over time. Mobile usage has increased significantly, overtaking Desktop usage around 2016, while Tablet usage remains relatively low.*

*   71% of employees leverage smartphones for work tasks.
*   Over 60% of employees use their smartphones for work-related communication.
*   48% of employees use their smartphones for accessing work-related information.

Adopting mobile apps has tangible benefits, but enterprises should ask if they are really built to protect 
their employees, sensitive data, and infrastructure. We analyzed over 40,000 of the most famous work 
and non-work categories and apps to help get insights into this question. Let's look at the data. 

The number of apps has exploded.
Today, the work app footprint in enterprises is comprised of in-house developed apps, third-party 
applications, and personal apps on work devices. 

There are now around 1,889,653 Apple iOS applications, and 3,466,806 Android apps within their respective 
app stores.  Add in the other 300 or more non-official stores and these numbers get even larger. A typical 
smartphone user has at least 80 mobile applications installed,  with anywhere between 5 to 11 of these 
being work apps pushed to their device by their employer.  

These statistics provide a better understanding of how much our personal devices are used for work.

### Table 1 - iOS - Avg. Number of Violations per Application

| App Category      | MASVS | GDPR | NIAP | PC | HIPAA |
|-------------------|-------|------|------|----|-------|
| business          | 18    | 17   | 8    | 5  | 9     |
| medical           | 19    | 17   | 8    | 5  | 9     |
| financial         | 20    | 18   | 9    | 6  | 9     |
| productivity      | 16    | 14   | 7    | 5  | 8     |
| travel            | 19    | 20   | 8    | 6  | 9     |
| Developer tools   | 14    | 10   | 5    | 4  | 6     |
| Social networking | 20    | 19   | 8    | 6  | 10    |
| dating            | 19    | 19   | 8    | 6  | 9     |
| entertainment     | 17    | 16   | 7    | 5  | 9     |
| shopping          | 21    | 19   | 9    | 6  | 9     |
| utilities         | 17    | 15   | 7    | 5  | 9     |
| gaming            | 23    | 20   | 9    | 8  | 13    |

### Table 2- Android - Avg. Number of Violations per Application

| App Category      | MASVS | OWASP | NIAP | PCI | GDPR | HIPAA |
|-------------------|-------|-------|------|-----|------|-------|
| communication     | 24    | 21    | 9    | 5   | 11   | 5     |
| shopping          | 27    | 24    | 11   | 5   | 13   | 6     |
| financial         | 26    | 22    | 12   | 5   | 12   | 5     |
| business          | 24    | 21    | 10   | 5   | 11   | 6     |
| medical           | 25    | 22    | 10   | 5   | 11   | 5     |
| dating            | 26    | 22    | 12   | 5   | 14   | 5     |
| gaming            | 25    | 23    | 9    | 5   | 12   | 5     |
| Developer tools   | 20    | 18    | 6    | 4   | 8    | 5     |
| travel            | 26    | 22    | 10   | 5   | 12   | 5     |
| utilities         | 23    | 19    | 8    | 4   | 9    | 5     |
| social networking | 25    | 22    | 10   | 5   | 12   | 5     |
| productivity      | 24    | 20    | 9    | 4   | 10   | 5     |
| entertainment     | 24    | 21    | 9    | 4   | 10   | 5     |

These frameworks and regulations—MASVS, OWASP, NIAP, PCI, GDPR, and HIPAA—serve as important 
security and privacy standards across different industries and regions. Running apps that violate 
security frameworks like MASVS, OWASP, PCI, GDPR, or HIPAA on enterprise devices exposes businesses to 
severe risks. These include cyberattack vulnerabilities, significant non-compliance fines, data breaches, 
and privacy violations. Financial penalties, reputational damage, and operational disruptions can follow, 
particularly when sensitive customer or financial data is compromised. 

With the continued rise of no-code/low-code development approaches, developers will look to build 
cloud-native apps up to 10 times faster than traditional coding while using up to 70 percent fewer 
resources.  However, focusing on speed often means that best security practices are overlooked or 
improperly implemented. This could lead to more exploitable apps being deployed into production 
without the proper app protections and security testing, increasing the likelihood of data breaches and 
compromised systems.

## How Prepared Are You for Mobile Risk

Mobile devices and their app footprint make them an easy target for attacks and require an effort to 
secure them.  Use of the same device for work and personal use is not new.  This has been the case for 
desktop and laptop computers for decades but mobile is different.

Unlike traditional endpoints like desktops or laptops, mobile devices operate in a constantly shifting 
environment, they are constantly exposed to unsafe networks—public Wi-Fi, harmful apps, and 
phishing links, malware etc —exposing the enterprise to a variety of potential threats. 

1.  The devices are controlled by the end-user, not the enterprise IT 
team. You can't really lock them down or force the user to update
 
software on their device.
2.  There are an unlimited combination of mobile device hardware and
 
operating systems out there.  So each mobile device has a different
 
risk posture.
3.  85% of the apps on the device are personal apps and they all
 
impact the risk exposure to the enterprise.

> HERE IS WHY: 
> The question becomes: 
> Can your current security 
> framework handle this diversity 
> and unpredictability? 

# Global Threat Landscape

## Key Stats

### Network
*   The number of unsecured networks detected increased by 36%.
*   The number of devices connecting to unsecured networks increased by 45%.
*   The number of devices connecting to a rogue access point has increased by 100%.

### Phishing
*   82% of phishing sites are adapted to mobile.
*   76% of phishing sites are using HTTPS.
*   40% of phishing sites detected in 2023 used the .dev domain.

### Malware
*   1 in 4 protected devices worldwide encountered malware.
*   We detected over 87K malware a month. 13% increase Y-o-Y.
*   80% more spyware samples detected on enterprise devices. Most not known by the industry.

### Platform
*   80% of iOS versions in 2023 were actively exploited at some point.
*   15% of devices running a vulnerable or non-upgradeable Android version.

### OS

## Top Threats by Platform

### Android
*   28%  Sideloaded Apps
*   18%  Vulnerable Non-upgradable
Android Version
*   15%  Passcode Not Enabled
*   12%  Malware
*   6% Malicious Websites

### iOS
*   27% Passcode Not Enabled
*   24% Sideloaded App
*   19% Vulnerable Non-upgradeable
*   11% Unsecured Wi-Fi
*   9% Captive Portal

*All statistics in this report, unless otherwise noted in a footnote, are from Zimperium Labs research.*

## Top Threats in U.S. Public Sector 
### Federal, State & Local Governments
1.  Unsafe Networks - 57%
2.  Phishing - 10%
3.  Passcode Not Enabled - 3.5%

## Top Threats in the Private Sector By Vertical

### Automotive
1.  Mishing - 13%
2.  Passcode Not Enabled - 9%
3.  Vulnerable Non-upgradable Android - 8%
4.  Sideloaded Apps - 7%

### Communications
1.  Unsafe Networks - 24%
2.  Vulnerable and Non-upgradeable Android - 6%
3.  Sideloaded Apps - 1%

### Consulting
1.  Sideloaded Apps -  28%
2.  Vulnerable and Non-upgradeable - 7%
3.  Risky Device Setting - 7%

### Consumer Goods
1.  Unsafe Networks - 51%
2.  Sideloaded Apps -  5%
3.  Passcode Not Enabled - 2%
4.  Vulnerable and Non-upgradeable - 4%

### Energy & Utilities
1.  Unsafe Networks - 45%
2.  Unsecured Wi-Fi  - 36%
3.  Mishing - 26%

### Financial Services
1.  Sideloaded Apps - 68%
2.  Unsecured Wi-Fi  - 11%
3.  Passcode Not Enabled - 2%
4.  Mishing - 2%

### Healthcare
1.  Unsafe Networks - 50%
2.  Mishing - 39%
3.  Sideloaded Apps  - 1%

### Information Technology
1.  Unsafe Networks - 68%
2.  Sideloaded Apps - 15%
3.  Vulnerable and Non-upgradeable - 4%
4.  Mishing - 4%

### Manufacturing
1.  Unsafe Networks - 86%
2.  Mishing - 2%

### Higher Education
1.  Unsafe Networks - 81%
2.  Mishing - 5%

### Retail
1.  Mishing - 48%
2.  Unsafe Networks - 4%

## Top 3 Drivers

### BYOD - Personal Devices For Work

Nearly 67% of employees use personal devices for work,  regardless of whether their 
company has a formal bring-your-own-device (BYOD) policy. Alarmingly, 70% of 
businesses fail to adequately secure personal devices used for work purposes.  This 
lack of security likely increases the actual risk, reinforcing the belief held by 55% of 
professionals that smartphones are the most exposed endpoints in their organization. 

### Cyber Hygiene is Poor on Mobile Devices

User behavior often blurs the lines between work and personal activities, increasing the 
chances of breaches when checking personal messages or emails on a work device or 
using unsecured Wi-Fi networks. Notably, 71% of employees admit to engaging in 
actions they knew were risky. 
<sup>11</sup> As noted above,  Zimperium research found 15% or more 
of employees do not have a passcode enabled on their mobile devices. 

### AI-Powered Bad Actors 

Bad actors increasingly leverage artificial intelligence 
(AI) to discover new attack surfaces and vulnerabilities, 
rapidly adapting their techniques to enhance attacks 
on mobile devices that access enterprise networks. 
Some of the most common uses of AI-driven attacks 
include:

*   Automatic tailoring of phishing vectors (QR code,
websites, URLs etc)
*   Automation of malware sample creation
*   Mutation of malware samples to avoid detection
*   Automatic tailoring of phishing emails and
messages

# Threats Enterprises Must Prioritize

Despite the large number of mobile threats and risks, there are four that are paramount to tackle and 
doing so will reduce risk from the rest. The four most important threats are:

i.  Mishing: Mobile-Targeted Phishing Attacks
ii. Mobile Malware
iii. Sideloaded Apps
iv. Application Vetting and Protection for your users mobile apps
v. Platform Vulnerabilities

*Image Description: A bar chart showing the percentage of devices that encountered a phishing attack, broken down by operating system (iOS and Android) and region (APAC, EMEA, North America, South America). Android devices in APAC and EMEA have a higher percentage of phishing attacks compared to other regions.*

Here is a detailed look at each threat so we can better understand how it works and how we can defend 
against it.

## From Phishing to Mishing!

In 2023, the Anti-Phishing Working Group reported nearly five million phishing attacks, 
<sup>12</sup> marking it the
worst year on record and surpassing the 4.7 million attacks seen in 2022. Zimperium’s zLABS threat data 
aligns with this trend, underlining the increasing sophistication of phishing sites. Notably, 82% of 
phishing sites examined by Zimperium specifically targeted mobile devices, delivering content 
formatted for mobile, reflecting a 7% increase over the last three years.  
<sup>13</sup> 25% of mobile users tapped on at 
least one phishing link every quarter in 2019.

This trend underscores the growing number of phishing attacks targeting mobile users. Compared to 
desktop systems, mobile devices often have fewer security measures in place. Users may not install security 
software or be less likely to notice phishing attempts due to smaller screen sizes and less visible security 
indicators, such as hidden URL bars.

The four standard types of mobile targeted phishing attacks include Mobile-Targeted  Email Phishing, 
Smishing, Vishing and Quishing. These four phishing attack methods go beyond tailoring emails to be 
deceptive on the small screens of our mobile devices.  Three methods leverage the unique features of a 
mobile device: text/sms features (Smishing) , voice features (Vishing)  and the fact that it is a camera 
enabled device (Quishing). The fourth, Mobile-Targeted Email Phishing consists of an attack that is launched 
via a standard email message, but only executes when a link (or attachment) is clicked by the user from a 
mobile device. If clicked from a standard endpoint device such as a laptop, the attack is aborted.

> 76%
> of phishing sites using HTTPS now employ this protocol. This can give users
> a false sense of security, leading them to believe the website is legitimate.

> 79%
> of credentials were harvested through phishing attacks.
> Source: Egress

> 50%
> of phishing sites are detected within 72 hours of creation.
> Source: Zimperium

> Hence a new name is 
> needed that covers all four 
> of these phishing methods: 
> Mishing!

*Image Description: A line graph showing the time in days between domain creation and detection of phishing sites. The graph indicates that a significant portion of phishing sites are detected within a short time frame after creation, with a peak around day 0.*

Following the trend of previous years, the US continues to lead the top countries hosting phishing 
sites, accounting for 84% of such sites. This does not imply that most phishing attacks originate from 
the US but rather that attackers are leveraging its infrastructure, such as hosting services or new 
types of top-level domains, to carry out these activities. 

Understanding this fast-paced lifecycle is key to developing countermeasures and protecting 
sensitive information from being harvested. Attackers operate incredibly quickly and precisely, 
hooking their prey and reaping the rewards as stolen credentials quickly lead to account takeovers.

Addressing this problem on mobile demands a reevaluation of current approaches and the 
exploration of more dynamic and proactive measures. 

### The Struggle to Keep Up with Phishing 

Phishing sites exemplify a hit-and-run approach in the digital threat landscape. These deceptive 
domains are notorious for their rapid setup and equally swift disappearance, creating significant 
challenges for cybersecurity defenses. Moreover, Zimperium reports that around one-quarter of 
phishing sites become operable less than 24 hours after their creation, launching malicious 
activities almost immediately. This quick deployment enables cybercriminals to reap substantial 
rewards in a short time frame before the site vanishes or is taken down by authorities.

Potential strategies might include: 

*   **Enhanced Detection Speed:** Leveraging on-device detection 
techniques to identify phishing domains before they are clicked on.
*   **Real-Time Blocking:** Implementing systems that update URL 
blocking/filtering in real-time, minimizing the window during which 
sites can be accessed.
*   **Public Awareness and Education:** Increasing efforts to educate 
employees about the risks of phishing attacks and how to 
recognize suspicious links, reducing the success rate of such 
attacks.

> Phishing ranks as the 
> second most expensive 
> attack, costing
> organizations an 
> average of 
> $4.76 million USD
> per incident. 

*Image Description: A pie chart showing the most phished brands globally, with Microsoft being the most imitated brand at 23%, followed by WhatsApp at 15%, Facebook at 5%, and other brands.*

### BRANDS PHISHED BY REGION

*   **NORTH AMERICA**
    *   57% Microsoft
    *   13% WhatsApp
    *   6% Facebook
*   **SOUTH AMERICA**
    *   33% WhatsApp
    *   10% Deniz Bank
    *   9% Facebook
*   **EMEA**
    *   37% Gazprom
    *   17% Facebook
    *   11% Instagram
*   **APAC**
    *   26% Bet365
    *   14% Facebook
    *   13% Garena

## Industries Targeted by Phishing

No industry is immune to the insidious threat of phishing attacks. 
Zimperium threat data revealed the healthcare industry experienced the 
highest number of threats in 2023, with a staggering 39% of its mobile 
threats attributed to phishing attacks. 

*   2% MANUFACTURING
*   4.2% HIGHER EDUCATION
*   39% HEALTHCARE

According to the World Economic Forum,  the increase in mobile-connected devices and AI-driven 
cyberattacks are key factors contributing to the growing vulnerability of critical infrastructure. The 
proliferation of mobile devices and their use in accessing essential services make them prime targets for 
ransomware, 
   
leading to significant disruptions in critical sectors like healthcare, energy, and 
transportation.

## Mobile Malware: Advanced Attacks

Think you’ve got mobile malware under control? Think again. With its widespread accessibility and 
immense scale, malware has become the weapon of choice for nearly every cybercriminal. Mobile 
malware rapidly spreads and extensively disrupts systems, with millions of unique variants and new 
malicious apps emerging daily. According to a recent survey, when asked about their primary 
cybersecurity concerns, 41% of CISOs cited malware, while 32% expressed concern about ransomware. 
(Pulse).

Zimperium researchers analyzed over 859k malware samples detected in the wild.
On average, that equates to over 16,500 new malware samples a week. Remarkably, 72% of the malware 
samples were completely unknown at the time of detection (not known to the free av engines), 
highlighting Zimperium’s advanced capabilities in staying ahead of the curve when it comes to malware 
identification and protection. 

### Malware Family Distribution

While the number of unique malware samples has risen by 13% since 2022, there has 
been a notable increase across the various malware families. Specifically, riskware 
and spyware have seen significant growth compared to other types of malware. 

*Image Description: A line graph showing malware detections by month in 2023. The graph indicates that the highest number of malware detections occurred in July 2023.*

In July 2023, Zimperium recorded the highest number of malware 
detections for the year, representing nearly 15% of all events for the year. 

*Image Description: A bar chart comparing malware family distribution between 2023 and 2022. The chart shows that riskware and spyware have increased significantly in 2023 compared to 2022.*

### Malware Families by Region

*   **NORTH AMERICA**
    *   70%  Malware      
    *   11%    Trojan            
    *   9%     Riskware
*   **SOUTH AMERICA**
    *   66%   Malware     
    *   11%     Trojan            
    *   10%   Riskware
*   **EMEA**
    *   57% Malware 
    *   10% Riskware 
    *   8%     Trojan
*   **APAC**
    *   37%  Malware 
    *   28%  Riskware 
    *   15%   Trojan

General purpose malware is a global issue, with North America experiencing the highest impact, 
accounting for 70% of malware events. With one in twenty protected devices encountering malware in a 
year, extrapolating this means 15.5 million devices are affected by malware yearly.

> WHAT IS RISKWARE?
> It’s a potentially vulnerable app. 

*Image Description: A pie chart showing the main spyware families. SpinOK is the most prevalent at 61.4%, followed by Spynote at 8.6%, and other spyware families.*

### Main Spyware Families

*   SpinOK 61.4%
*   Lucifer_Pinduo 5.1%
*   Spyloan 1.3%
*   SMSSpy 4.2%
*   LoanSpy 5.1%
*   Spymax 2.4%
*   TrackViewPro 2.9%
*   Others 7.9%

## Unsecured Networks

An unsecure network is a network that lacks adequate security 
measures such as encryption, making it vulnerable to 
unauthorized access and data interceptions. Connecting to these 
networks is bad for business because it can lead to data 
exfiltration, resulting in financial losses, legal liabilities, and access 
to intellectual property. 

In 2023, the number of devices connected to unsecured networks 
increased by 45%. Zimperium found that on average, a mobile 
device connects to a risky network 17 times in the span of a year. 
Additionally other reports indicate that around 35% of individuals 
access public WiFi three to four times a month and  four in 10 have 
had their information compromised while using public WiFi. This 
highlights that public WiFi is frequently used as a last resort when a 
cell connection is unavailable, allowing people to stay connected 
for leisure and work purposes. 

Using public Wi-Fi while traveling poses a higher risk to online 
security compared to usage at fixed locations. Among 
respondents who had their online security compromised while 
using public Wi-Fi, the highest percentage—23%—reported that 
these incidents occurred at the airport.

> Only 5% of 
> individuals think 
> public WiFi is 
> completely unsafe, 
> suggesting a need for 
> more information 
> and resources to help 
> make informed 
> decisions about using 
> these unsafe 
> networks.

Attackers can easily intercept traffic through man-in-the-middle (MitM) attacks or lure employees into 
using rogue Wi-Fi hotspots; it means they exploit vulnerabilities in network security to gain unauthorized 
access to data being transmitted between devices and networks. Zimperium identified that 33% of 
network threats are MiTM. In a MiTM attack, an attacker secretly intercepts and possibly alters the 
communication between two parties they believe are directly communicating with each other. 

> Network detections in EMEA have 
> quadrupled with malware occurring 
> at nearly double the rate. 
> (Radar.cloudflare) (WatchGuard)

*Image Description: A bar chart showing network attacks by region, broken down by operating system (iOS and Android) and region (APAC, EMEA, North America, South America). EMEA has the highest percentage of network attacks for both iOS and Android devices.*

With the rise of cloud-based services for mission-critical tasks, mobile devices have become 
indispensable for business operations. Zimperium threat data shows that Europe, the Middle East, and 
Africa (EMEA) experience the highest number of network attacks, with nearly 6% of iOS devices and 5% of 
Android devices encountering such threats.

### Network Attacks by Region

An Early Warning Sign for Imminent Threats

Zimperium conducted a study on the security of Wi-Fi networks and rogue access points. The findings 
indicate that when devices connected to these unsecure or rogue networks, it took less than ten minutes 
for malicious activities, such as 
interception, unauthorized 
access, or the installation of 
malware to be detected on the 
devices. This highlights the risk 
associated with connecting to 
unsecured networks and the 
speed at which cyber threats 
can compromise mobile 
devices in such environments. 

# The Sideloading Saga

Sideloading is the practice of installing mobile apps on a device that are not from the official app stores. 
This is typically done on a rooted Android device or a jailbroken iOS device. With the blurring of personal and 
professional boundaries, sideloaded apps are increasingly showing up on personal devices used for work. 
Zimperium’s threat data shows that approximately one in four Android devices face this issue. While 
sideloading is much more prevalent on Android, the recent Digital Markets Act (DMA) is expected to 
increase its prevalence on iOS.

> APAC outpaces all 
> regions, with 
> 43%
> of Android devices 
> sideloading apps. 

In the most severe cases, sideloading apps can lead to a 
complete mobile device compromise, granting remote attackers 
full control. This could enable threat actors to access sensitive user 
information, such as corporate information, credentials, or 
personal information, and impersonate the user for unauthorized 
access to banking accounts or other critical systems, among 
other potential consequences.

## Why Sideload Apps

With each sideloaded app, employees unknowingly expose their mobile devices or corporate ecosystems 
to vulnerabilities by bypassing standard app stores such as Google Play. 
Here are some reasons why users choose unofficial store apps:

*   To access apps unavailable in their region or banned.
*   To unlock features that are otherwise restricted.
*   To download free or cheaper games and movies.
*   To engage in illegal activities like bypassing Digital Rights Management (DRM).

Researchers at Zimperium found that riskware and trojans 
are the most common malware families found in 
sideloaded apps. As riskware often includes potentially 
unwanted programs (PUPs) and adware, its high 
occurrence indicates a broader spectrum of threats 
beyond traditional malware. Additionally, trojans, known for 
their deceptive nature in disguising themselves as 
legitimate apps, present a persistent challenge in evading 
detection and compromising device security. 

Our research indicates that globally, users who engage in 
sideloading are
 
   200% more likely to have malware 
running on their devices than those who do not. In fact, 
sideloading is a great contributor to malware risk; in 8.3% 
of cases where malware was detected, the source can be 
traced back to a sideloaded application.

> TOP 3 CATEGORIES OF 
> SIDELOADED MALWARE
> Riskware 
> 73%
> Trojan 
> 11%
> General Purpose Malware 
> 10%

*Image Description: A bar chart showing the top industries sideloading mobile apps. Financial Services has the highest percentage at 73%, followed by Consulting Services at 45%, and Consumer Goods at 23%.*

### Top Industries Sideloading Mobile Apps 
*   Financial Services 73%
*   Consulting Services