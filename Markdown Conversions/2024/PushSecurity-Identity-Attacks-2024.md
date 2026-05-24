# 2024: A year of identity attacks

Looking back on identity attacks in 2024 and what they tell us about how identity-based techniques and tools are evolving.

## Table of Contents
- [Introduction](#introduction)
- [Welcome to the identity era](#welcome-to-the-identity-era)
- [Identity security’s watershed moment: Snowflake](#identity-securitys-watershed-moment-snowflake)
- [Identity is the new perimeter](#identity-is-the-new-perimeter)
- [Why attackers are focusing on vulnerable identities](#why-attackers-are-focusing-on-vulnerable-identities)
- [How identities are exploited for account takeover](#how-identities-are-exploited-for-account-takeover)
- [Why attack paths are changing with the shift to identity attacks](#why-attack-paths-are-changing-with-the-shift-to-identity-attacks)
- [SaaS attacks aren’t an add-on](#saas-attacks-arent-an-add-on)
- [How attackers profit from identity attacks](#how-attackers-profit-from-identity-attacks)
- [2024 in review](#2024-in-review)
- [Identity attacks by the numbers](#identity-attacks-by-the-numbers)
- [Public identity breaches in 2024](#public-identity-breaches-in-2024)
- [Top 3 public identity related breaches in 2024](#top-3-public-identity-related-breaches-in-2024)
- [Threat actor case studies](#threat-actor-case-studies)
- [How identity-based techniques evolved in 2024](#how-identity-based-techniques-evolved-in-2024)
- [Final thoughts](#final-thoughts)

---

## Introduction

Identity attacks where attackers look to take over accounts on internet-facing apps and services are by far the most common attack experienced by organizations today. But the events of 2024 show that they’re now also the most impactful.

The major cyber security stories from 2024 have revolved around identity attacks, with identity-based campaigns from APT29 and Scattered Spider, infostealer campaigns and credential theft on an industrial scale, a booming underground marketplace for stolen data, and MFA-bypassing AitM and BitM phishing techniques becoming the new normal.

The standout story was the campaign against ~165 Snowflake customers, impacting hundreds of millions of end-customers and billed as one of the biggest breaches in history. Snowflake was a watershed moment for attackers and defenders that laid bare the threat posed by identity attacks and account takeover.

The rise in identity attacks is wrapped up in broader transformational change in IT and working practices, driven by the shift to remote working and the so-called SaaS revolution.

The result is that work now happens in employee browsers, across a vast ecosystem of internet-based apps and services. So, where identity was once governed and administered in your centralized identity store like Active Directory, it’s now radically decentralized — with multiple identity providers, hundreds of apps, and thousands of identities per organization.

Naturally, this gives attackers a vast surface to target, where vulnerable identities are the lowest-hanging fruit. And to top it all off, the controls we’ve historically relied on to stop identity attacks are being routinely bypassed. When all an attacker needs to do is log into an internet-facing app and steal your data to be able to profit, they don’t need to worry about bypassing your firewalls and EDR, for example.

There’s no doubt that identity attacks are the #1 threat facing organizations today — but we’re still only scratching the surface of what’s possible in the world of interconnected SaaS and decentralized identity infrastructure.

It’s vital that organizations arm themselves with the knowledge and understanding of how the threat has evolved — and re-evaluate their defenses accordingly.

## Welcome to the identity era

Whenever there’s a paradigm shift in cyber security, it’s typically triggered by an event or series of events (usually a high-profile attack) that exposes the limitations of the status quo.

Identity is the new perimeter. But before we tell you why, let’s first look at how we got here.

### The dawn of modern network security: The SQL Slammer

The dawn of modern network security as we know it was spurred on by the infamous SQL Slammer worm in 2003, which infected ~75k servers worldwide, crippling retail POS systems and ATMs. This demonstrated the risk posed by universal attacks exploiting common vulnerabilities – a free-for-all rather than specific hosts or networks.

The response to the SQL Slammer, as well as the earlier CodeRed and Nimda worms, was to acknowledge the limitations of traditional network firewalls introduced in the late 1980s. These events moved the industry toward application-layer firewalls, deep packet inspection (beyond just IP addresses and ports), and intrusion prevention and detection systems, as well as default-deny firewall policies. They also highlighted the need for routine patch management (the exploited vulnerability was 6-months old), prompting the Microsoft Trustworthy Computing initiative and the first ever Patch Tuesday.

This event ushered in an era where internet-exposed servers were the lowest hanging fruit for attackers to pick at – the first “perimeter” of modern computer networks — and building tall walls became the top objective for security departments.

### The shift to the endpoint: Operation Aurora

The next shift occurred in 2009 when Operation Aurora hit the headlines. This was a highly sophisticated series of attacks targeting U.S. technology and defense companies, attributed to state-sponsored hackers from China.

The attack, which exploited a zero-day vulnerability in Microsoft Internet Explorer, was one of the first widely publicized attacks where zero-day exploits were used in a targeted and sophisticated manner. The attacker deployed malware including a Remote Access Trojan, enabling them to move laterally, escalate their privileges, and ultimately steal sensitive data from victims.

This attack highlighted the need for greater defense in depth as opposed to a model that was “crunchy on the outside, chewy in the middle” to be able to defend against unforeseeable zero-day exploits; equally, it exposed the limitations of the signature-based AV solutions that had failed to detect the custom malware used by the attacker. This inspired a new wave of specialist providers to come to market, and the EDR industry was born.

![Diagram showing the evolution from Network perimeter to Endpoint perimeter to Identity perimeter]

## Identity security’s watershed moment: Snowflake

The previous 18 months have seen a number of significant breaches propelled by identity attacks, with threat actors like Cozy Bear and Scattered Spider publicly leveraging identity attack techniques, and the Okta, Microsoft, MGM Resorts breaches getting plenty of news coverage.

But, it’s the attacks on Snowflake customers in 2024 that will be remembered as the watershed moment for identity — touted by news outlets as “one of the biggest breaches ever”, impacting hundreds of millions of end-customers.

Between April and July this year, user accounts belonging to approximately 165 Snowflake customers around the world were compromised using stolen credentials from infostealer infections dating back to 2020, enabling attackers to log into accounts without MFA (which was not turned on by default).

The attacker simply logged into the app, used a basic utility to gather information from accounts, and executed the same set of SQL commands across customer instances to exfiltrate data.

Snowflake is just the tip of the iceberg. But it serves as a wake-up call for what’s coming (or rather, what’s already happening).

![Flowchart of the Snowflake attack lifecycle: Credentials stolen via infostealer -> Snowflake identified as high-value target -> Login page identified -> Credentials used to authenticate -> Data appears on underground markets -> Victims hit with ransom -> Data mass exfiltrated -> Attacker crafts utility to collect data]

## Identity is the new perimeter

In the wake of Snowflake, it’s clear that identity is the new perimeter.

Identity attack is synonymous with account takeover, where the attacker hijacks an account connected to an application or service. Most commonly, identity techniques are used during the initial access phase of an attack.

The so-called SaaS revolution means that organizations are using hundreds of apps, with thousands of accounts as a result. Some are entirely SaaS-native, with no traditional network to speak of, but most have adopted a hybrid model with a mixture of on-premise, cloud, and SaaS services forming the backbone of business applications being used.

Not only this, they’re no longer conveniently managed and administered from a central identity system like Active Directory (who’d have thought we’d miss it?).

Most organizations have looked to SSO and MFA as the key to tackling identity sprawl. Unfortunately, the reality is that:

- Requiring MFA when logging into an IdP account and requiring MFA at the application level are separate things — meaning SSO logins can have MFA enabled at the same time that local logins do not.
- SSO isn’t always possible depending on your app and IdP combination. Not all apps support all SSO methods or provide integrations with every IdP.
- SSO doesn’t prevent users from creating or using non-SSO logins alongside SSO (often this needs to be configured in-app, if it’s possible at all).
- Many apps lack the ability to enforce MFA by default, meaning that even if you are aware of an app and it’s managed by the security team, there still might not be much you can do to track or improve user account security.
- Because many apps are adopted organically by users, security teams aren’t always aware of them to enroll them in SSO.
- When self-adopting an app, users often default to a username and password (and don’t set MFA).

## Why attackers are focusing on vulnerable identities

The scale of the challenge posed by managing identities in this modern context means that it’s easy for identity misconfigurations and vulnerabilities to creep in. So identity vulnerabilities exist almost everywhere.

Some are certainly more likely to be exploited than others (e.g. an account with a reused password and no MFA is a higher risk than an account with MFA) but attackers have the means to take over most accounts using widely available tooling and know-how. A determined attacker can get into pretty much any account, regardless of the configuration and most of the time account takeover can be achieved by using even the most basic techniques.

## How identities are exploited for account takeover

To be able to hijack an account, an attacker needs to possess one of two things:

- Authentication material e.g. a username and password, with a login portal URL.
- Session material e.g. session cookies.

Attackers mainly acquire these materials through credential phishing and infostealers, using stolen cookies and credentials to perform different account takeover techniques, albeit with the same goal: Account takeover.

![Diagram showing the flow of Phishing and Infostealers leading to Stolen Credentials and Stolen Cookies, which then lead to Valid Accounts, Session Hijacking, and ultimately Account Takeover]

## Why attack paths are changing with the shift to identity attacks

Because modern businesses effectively run on interconnected SaaS apps, attackers simply have to log into accounts on these apps to be able to exploit them.

![Diagram comparing the Traditional attack path (Network -> Endpoint -> Server -> Data) vs the Modern attack path (Identity -> SaaS App -> Data)]

## SaaS attacks aren’t an add-on

It’s a common misconception that SaaS compromise typically comes after the traditional attack chain (a myth largely promoted by old-school consultancy providers, MSSPs, and managed SOC providers).

There’s no need for an attacker looking to take over a SaaS account to target the conventional network first — and many organizations today simply no longer have one.

This isn’t to say that there aren’t examples of SaaS compromises involving lateral movement from SaaS to SaaS or SaaS to cloud. Equally, there are examples of very short and direct account takeover in enterprise cloud environments leading to ransomware deployment.

But statistically, the average SaaS attack path involves little to no lateral movement, privilege escalation, and defense evasion, particularly when compared to a conventional network or hybrid attack.

These attacks are so successful because they bypass many of the existing security tools and frameworks that we’ve come to rely on — like EDR, firewalls, IDS, etc. — because they don’t touch the environments that they protect. And without the luxury of defense in depth, the controls that are still in play are having their limitations exposed.

## How attackers profit from identity attacks

Most account takeover attacks result in data theft opportunities, since ransomware deployment would involve additional lateral movement to conventional network resources (on-premise or cloud-hosted). And as many organizations today are SaaS-native, this isn’t always worthwhile (or even possible).

Of course, it depends on the app in question, but most business apps contain sensitive data that can be monetized — either directly in-app, or via an OAuth integration with another app or service.

Most cyber attacks that businesses encounter can be boiled down to one of three financially motivated end-goals:

- **Fraud**: Social engineering a victim to unknowingly perform a malicious action on the attacker’s behalf. There are many overlaps here with business email compromise (BEC) — except business email isn’t the only possible context.
- **Data theft**: Stealing data to extort a ransom payment, blackmail end-customers, and/or sell the data via underground criminal marketplaces.
- **Ransomware**: All the elements of data theft but also involving forced encryption of services and devices.

![Chart showing Top app types by ATO risk]

## 2024 in review

### Identity attacks by the numbers

We’ve curated some of the most impactful identity-related stats from reports issued in 2024.

- There are 600 million identity attacks per day (Microsoft).
- 79% of web application compromises were the result of breached credentials (Verizon).
- 75% of attacks in 2023 were malware-free and “cloud conscious” attacks increased by 110% (CrowdStrike).
- Infostealer activity increased by 266% in 2023, while the number of attacks featuring valid credentials saw a 71% increase year-over-year (IBM).
- One million new infostealer logs are distributed every month (Flare).
- Nearly half of the malware detected last year targeted victims’ data specifically, and the majority of that malware was classified as infostealers (Sophos).
- 39,000 session token attacks are detected per day and AitM attacks increased 146% in 2023 (Microsoft).
- Attacks on session cookies happen at the same rough order of magnitude as password-based attacks (Google).

### Public identity breaches in 2024

In 2024, we experienced a notable spike in news relating to data breaches where identity attacks played a significant role — usually as the method of initial access to company systems (either in the form of third-party SaaS or managed servers/devices/appliances).

![Infographic showing a list of companies impacted by identity-related breaches in 2024, including Snowflake, Microsoft, AT&T, and others]

### Top 3 public identity-related breaches in 2024

#### #3 - Microsoft
The threat group known as APT29, associated with the Russian SVR intelligence service, utilized password spray attacks that successfully compromised a non-production tenant account that did not have multi-factor authentication (MFA) enabled. They then leveraged this account to compromise a ‘test’ OAuth application that had elevated access to the Microsoft corporate environment. This was then used to access the email accounts of Microsoft employees.

#### #2 - Change Healthcare
In February, attackers stole 6TB of data from UnitedHealth subsidiary Change Healthcare as part of a severe ransomware attack that caused massive disruption to the US healthcare industry. This impacted a wide range of critical services used by healthcare providers across the U.S., including payment processing, prescription writing, and insurance claims, and caused financial damages estimated at $872 million. The attack impacted the personal medical data of over 100M customers.

#### #1 - Snowflake
165 organizations around the world were targeted using stolen credentials gathered from infostealer infections dating back to 2020. The impacted accounts lacked MFA, meaning successful authentication only required a valid username and password. As the Snowflake credentials found in infostealer malware credential dumps had not been rotated or updated, they remained valid and could be used to authenticate to user accounts on Snowflake tenants belonging to various customers.

## Threat actor case studies

Let’s take a closer look at the tactics, techniques and procedures (TTPs) used by some of the more prolific threat actors from 2024 known for identity-related attacks.

### APT29
APT29 is a cyber espionage group and part of the Russian Foreign Intelligence Service (SVR). In 2024, they demonstrated a conscious adoption of identity-based techniques to target cloud-based services. Their TTPs include residential proxies, malicious OAuth integrations, credential stuffing, session hijacking, and MFA fatigue.

### Scattered Spider
Scattered Spider is a native English-speaking cybercriminal group known for social engineering attacks involving SIM swapping and helpdesk scams. Their TTPs include social engineering of helpdesk personnel, credential theft from marketplaces, AitM phishing, and automated credential harvesting.

### ShinyHunters
ShinyHunters is the alleged threat group behind the Snowflake campaign. Their TTPs include exfiltration via in-app functionality, mass credential stuffing using stolen credentials from infostealers, and targeting unmanaged devices.

## How identity-based techniques evolved in 2024

### Phishing 2.0: AitM & BitM
MFA-bypassing phishing kits are now the standard choice for attackers. Adversary-in-the-Middle (AitM) and Browser-in-the-Middle (BitM) kits have become the new normal. These techniques bypass most forms of MFA by prompting the victim to complete the request as part of the attack.

### Infostealers 2.0
Modern infostealers are used primarily to extract information from web browsers such as passwords, session cookies, and autofill information. They are often delivered via malvertising or compromised websites and are designed to evade EDR and other endpoint controls.

### Credential stuffing 2.0
Despite the rise in SSO, accounts continue to be hacked due to weak, reused, and/or previously breached credentials. Attackers use automated tools to test stolen credentials across thousands of apps, often exploiting "ghost logins" where local passwords exist alongside SSO.

### Session hijacking 2.0
Modern session hijacking involves an attacker using stolen cookies extracted from the victim’s browser to resume a valid session. Unlike legacy attacks, this is performed over the public internet and is highly effective at bypassing standard defensive controls like VPNs or geo-restrictions.

## Final thoughts

Account takeover via identity attacks is now the go-to approach for threat actors.

- The threat of identity attacks is significantly increased by the SaaS-ification of business IT due to the increased identity attack surface.
- Identity attacks are routinely evading many established controls, including MFA, SSO, SWG, EDR, and so on, leaving organizations unknowingly exposed.
- Many accounts are highly vulnerable to even basic attacks, while even more robust configurations can be bypassed using widely accessible tooling and techniques.
- Attackers can compromise many organizations by targeting the various company tenants of a single SaaS app, often following repeatable steps post-account takeover.
- Once an account is compromised, attack paths can be very short, resulting in quicker time-to-value for the attacker.

It may have been a landmark year for identity attacks, but we’re still only scratching the surface of what’s possible in the new world of decentralized, SaaS-centric IT. There’s no doubt that we should expect the threat of identity attacks to grow further in 2025.

This means that it’s essential that organizations re-evaluate and strengthen their defenses against identity attacks.