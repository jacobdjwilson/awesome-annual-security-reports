# CrowdStrike 2024 Global Threat Report

## Table of Contents
- [Foreword](#foreword)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Threat Landscape Overview](#threat-landscape-overview)
- [2023 Themes](#2023-themes)
  - [Identity-Based and Social Engineering Attacks](#identity-based-and-social-engineering-attacks)
  - [Adversaries Continue to Develop Cloud-Consciousness](#adversaries-continue-to-develop-cloud-consciousness)
  - [Third-Party Relationship Exploitation](#third-party-relationship-exploitation)
  - [Vulnerability Landscape: “Under the Radar” Exploitation](#vulnerability-landscape-under-the-radar-exploitation)
  - [2023 Israel-Hamas Conflict: Cyber Operations Focus on Disruption and Influence](#2023-israel-hamas-conflict-cyber-operations-focus-on-disruption-and-influence)
- [Threats on the 2024 Horizon](#threats-on-the-2024-horizon)
  - [Generative AI Use Within the Threat Landscape](#generative-ai-use-within-the-threat-landscape)
  - [2024 Elections](#2024-elections)
- [eCrime Landscape](#ecrime-landscape)
  - [Big Game Hunting](#big-game-hunting)
  - [eCrime Enablers](#ecrime-enablers)
  - [Targeted eCrime](#targeted-ecrime)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [CrowdStrike Products and Services](#crowdstrike-products-and-services)
- [About CrowdStrike](#about-crowdstrike)

## Foreword
The 2024 edition of the CrowdStrike Global Threat Report arrives at a pivotal moment for our global community of protectors. The speed and ferocity of cyberattacks continue to accelerate as adversaries compress the time between initial entry, lateral movement and breach. At the same time, the rise of generative AI has the potential to lower the barrier of entry for low-skilled adversaries, making it easier to launch attacks that are more sophisticated and state of the art. 

These trends are driving a tectonic shift in the security landscape and the world. The “good enough” approach to cybersecurity is simply no longer good enough for modern threats. As organizations increasingly move business to the cloud, adversaries are advancing their capabilities to exploit this, and abuse features unique to the cloud. We continue to see identity-based attacks take center stage, as adversaries focus on social engineering attacks that bypass multifactor authentication. The use of legitimate tools to execute an attack, an increasingly prevalent technique, impedes the ability to differentiate between normal activity and a breach.

We are entering an era of a cyber arms race where AI will amplify the impact for both the security professional and the adversary. Organizations cannot afford to fall behind, and the legacy technology of yesterday is no match for the speed and sophistication of the modern adversary.

With the release of the CrowdStrike 2024 Global Threat Report, our elite Counter Adversary Operations team is delivering the actionable intelligence you need to stay ahead of today’s threats and secure your future. This year’s report provides critical insight and observations into adversary activity, including:

- The tactics and techniques that adversaries use to exploit gaps in cloud protection
- The continued exploitation of stolen identity credentials and increasingly sophisticated methods adversaries use to gain initial access
- The growing menace of supply chain attacks and exploitation of trusted software to maximize the ROI of attacks
- The potential for adversaries to target global elections in a year that has the potential to transform geopolitics around the world for the near future

From Day One, CrowdStrike has said, “You don’t have a malware problem, you have an adversary problem.” We pioneered the concept of adversary-focused cybersecurity because it’s the best way to protect customers and stop breaches. We know the adversary better than anyone, and we use this insight to guide our innovation, protect customers, stop breaches and increase the cost to the adversary.

A secure future requires a strong foundation. This is what we’re delivering with the AI-native CrowdStrike Falcon® XDR platform. We’re driving the convergence of data, cybersecurity and IT, with generative AI and workflow automation built natively within a single, unified platform to give you and your teams the speed you need to beat the adversary.

I hope you find the CrowdStrike 2024 Global Threat Report informative and inspiring in our shared fight against the adversary. CrowdStrike will remain unrelenting in our mission to deliver the security outcome you need most: stopping the breach.

George Kurtz
CrowdStrike CEO/Co-Founder

## Table of Contents
- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Threat Landscape Overview](#threat-landscape-overview)
- [2023 Themes](#2023-themes)
  - [Identity-Based and Social Engineering Attacks](#identity-based-and-social-engineering-attacks)
  - [Adversaries Continue to Develop Cloud-Consciousness](#adversaries-continue-to-develop-cloud-consciousness)
  - [Third-Party Relationship Exploitation](#third-party-relationship-exploitation)
  - [Vulnerability Landscape: “Under the Radar” Exploitation](#vulnerability-landscape-under-the-radar-exploitation)
  - [2023 Israel-Hamas Conflict: Cyber Operations Focus on Disruption and Influence](#2023-israel-hamas-conflict-cyber-operations-focus-on-disruption-and-influence)
- [Threats on the 2024 Horizon](#threats-on-the-2024-horizon)
  - [Generative AI Use Within the Threat Landscape](#generative-ai-use-within-the-threat-landscape)
  - [2024 Elections](#2024-elections)
- [eCrime Landscape](#ecrime-landscape)
  - [Big Game Hunting](#big-game-hunting)
  - [eCrime Enablers](#ecrime-enablers)
  - [Targeted eCrime](#targeted-ecrime)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [CrowdStrike Products and Services](#crowdstrike-products-and-services)
- [About CrowdStrike](#about-crowdstrike)

## Introduction
As we reflect on the 2023 cyber threat landscape, the theme of stealth prevails. Adversaries have faced a hardening attack surface thanks to advancements in threat defense technology and threat awareness, and they have responded by increasingly adopting and relying on techniques that empower them to move faster and evade detection.

These techniques are evident in the consistent prevalence of eCrime, a highly attractive and lucrative business venture for many criminals. Unsurprisingly, eCrime persisted as the most pervasive threat across the 2023 threat landscape as adversaries leveraged techniques to maximize stealth, speed and impact.

While ransomware remains the tool of choice for many big game hunting (BGH) adversaries, data-theft extortion continues to be an attractive — and often easier — monetization route, as evidenced by the 76% increase in the number of victims named on BGH dedicated leak sites (DLSs) between 2022 and 2023.

Access brokers continued to profit by providing initial access to eCrime threat actors throughout the year, with the number of advertised accesses increasing by 20% from 2022.

Nation-state adversaries were also active throughout 2023. China-nexus adversaries continued to operate at an unmatched pace across the global landscape, leveraging stealth and scale to collect targeted group surveillance data, strategic intelligence and intellectual property.

In other areas of the world, conflict continued to drive nation-state and hacktivist adversary activity. In 2023, as the Russia-Ukraine war entered its second year, Russia-nexus adversaries and activity clusters maintained high, sustained levels of activity in support of Russian Intelligence Service intelligence collection, disruptive activity, and information operations (IO) targeting Ukraine and NATO countries.

> DATA-THEFT EXTORTION CONTINUES TO BE AN ATTRACTIVE — AND OFTEN EASIER — MONETIZATION ROUTE, AS EVIDENCED BY THE 76% INCREASE IN THE NUMBER OF VICTIMS NAMED ON BGH DEDICATED LEAK SITES

Iran-nexus adversaries and Middle East hacktivist adversaries were also observed pivoting cyber operations in the latter half of the year in alignment with kinetic operations stemming from the 2023 Israel-Hamas conflict.

North Korean adversaries maintained a consistently high tempo throughout 2023. Their activity continued to focus on financial gain via cryptocurrency theft and intelligence collection from South Korean and Western organizations, specifically in the academic, aerospace, defense, government, manufacturing, media and technology sectors.

Across the rest of the world, stealth played a key role in adversary activity focused on digital surveillance, information collection and control in support of government agendas. The assessed geographic range of this activity, as well as the capabilities and target scope of global threat actors, continued to underscore the extent to which targeted intrusion capabilities have proliferated beyond those demonstrated by commonly reported countries. In some cases, this activity was assisted by private sector offensive actors and openly available adversary emulation frameworks.

One of the greatest threat actor motivations driving stealth in cyber threat operations is CrowdStrike’s development of new products and partnerships throughout 2023. These changed the stakes within the operational landscape and left adversaries with no place to hide.

In 2023, CrowdStrike Falcon® Intelligence and CrowdStrike® Falcon OverWatch™ merged to become CrowdStrike Counter Adversary Operations (CAO). Combining the power of threat intelligence with the speed of dedicated hunting teams and trillions of cutting-edge telemetry events from the AI-native CrowdStrike Falcon® platform that detect, disrupt and stop today’s sophisticated adversaries, this merger has exponentially raised the business cost of conducting cyberattacks.

In 2024, CrowdStrike CAO repackaged CrowdStrike’s threat intelligence modules to add managed threat hunting (an industry first), empowering organizations to better pursue adversaries and stop breaches.

Over the course of 2023, CrowdStrike CAO introduced 34 new adversaries — including a newly tracked, Egypt-based adversary, WATCHFUL SPHINX — raising the total number of actors tracked across all motivations to 232. In addition to named adversaries, CrowdStrike CAO tracks more than 130 active malicious activity clusters.

CrowdStrike CAO drives unparalleled, actionable reporting coverage that captures new cyber threat developments in real time and identifies and tracks new adversaries. The CrowdStrike 2024 Global Threat Report sheds light on the standout trends from last year, how adversaries’ activities and motivations are evolving and the ways CrowdStrike anticipates the threat landscape will evolve in the coming year.

> OVER THE COURSE OF 2023, CROWDSTRIKE CAO INTRODUCED 34 NEW ADVERSARIES — INCLUDING A NEWLY TRACKED, EGYPT-BASED ADVERSARY, WATCHFUL SPHINX — RAISING THE TOTAL NUMBER OF ACTORS TRACKED ACROSS ALL MOTIVATIONS TO 232. IN ADDITION TO NAMED ADVERSARIES, CROWDSTRIKE CAO TRACKS MORE THAN 130 ACTIVE MALICIOUS ACTIVITY CLUSTERS.

CrowdStrike CAO Innovations

THE CROWDSTRIKE CAO TEAM PUTS RAPID INSIGHTS INTO THE HANDS OF FRONT-LINE TEAMS SO THEY CAN DISRUPT ADVERSARIES FASTER THAN EVER BEFORE.

IN THE FALL OF 2023, CROWDSTRIKE CAO ROLLED OUT AN IDENTITY THREAT HUNTING CAPABILITY, PAIRING THE LATEST INTELLIGENCE ON ADVERSARY MOTIVES AND TACTICS, TECHNIQUES AND PROCEDURES (TTPS) WITH CROWDSTRIKE FALCON® IDENTITY THREAT PROTECTION AND ELITE CAO THREAT HUNTERS TO QUICKLY IDENTIFY AND REMEDIATE COMPROMISED CREDENTIALS, TRACK LATERAL MOVEMENT AND STAY AHEAD OF ADVERSARIES WITH 24/7 COVERAGE.

AND WHILE THE CAO TEAM HUNTS FOR ADVERSARY ACTIVITY INSIDE CUSTOMER ORGANIZATIONS, THE NEW CAO “EXTERNAL ATTACK SURFACE EXPLORE” CAPABILITY ENABLES CUSTOMERS TO HUNT FOR AND EXAMINE ADVERSARY INFRASTRUCTURE.

CROWDSTRIKE MADE KEY INVESTMENTS IN AUTOMATION IN 2023, HELPING CUSTOMERS IMMEDIATELY TAKE ACTION ON CAO-IDENTIFIED THREATS. VIA FALCON IDENTITY THREAT PROTECTION, CROWDSTRIKE INTRODUCED NEW AUTOMATED WORKFLOWS FOR RESETTING CUSTOMER PASSWORDS EXPOSED ON THE CRIMINAL UNDERGROUND; ONE-CLICK TYPOSQUATTING DOMAIN BLOCKING AND TAKEDOWN; AND NEW CROWDSTRIKE FALCON® FUSION PLAYBOOKS FOR AUTOMATIC INDICATORS OF COMPROMISE (IOCS) RESULTING FROM TYPOSQUATTING THREATS AND THIRD-PARTY SYSTEM INTEGRATION. THESE NEW ENHANCEMENTS ALLOW USERS TO QUICKLY RESPOND TO THREATS THROUGHOUT THEIR SECURITY WORKFLOWS.

THE NEW CROWDSTRIKE CAO MODULES — CROWDSTRIKE FALCON® ADVERSARY OVERWATCH™, CROWDSTRIKE FALCON® ADVERSARY INTELLIGENCE AND CROWDSTRIKE FALCON® ADVERSARY HUNTER — HAVE LINKED THREAT HUNTING EVEN MORE CLOSELY TO THEIR INTELLIGENCE CAPABILITIES, UNIFYING THE USER EXPERIENCE SO CUSTOMERS CAN EASILY LEVERAGE A SINGLE, CONSISTENT USER INTERFACE TO VIEW CRUCIAL INFORMATION ACROSS ALL CAO CAPABILITIES.

CROWDSTRIKE CUSTOMERS ALSO BENEFIT FROM ENHANCED CONTEXT AROUND OBSERVABLES, NEW INDICATOR OF ATTACK (IOA) INTEGRATIONS TO ACCELERATE SECURITY INFORMATION AND EVENT MANAGEMENT (SIEM) DETECTION AND RESPONSE, THREAT HUNTING WORKFLOWS THAT WILL MORE EFFECTIVELY IDENTIFY ENVIRONMENTAL THREATS, AND IMPROVEMENTS TO DATA UNIFICATION AND LINKAGE ACROSS THE FALCON PLATFORM AND THIRD-PARTY APPLICATIONS.

## Naming Conventions
Adversary | Nation-State or Category
---|---
BEAR | RUSSIA
BUFFALO | VIETNAM
CHOLLIMA | DPRK (NORTH KOREA)
CRANE | ROK (REPUBLIC OF KOREA)
HAWK | SYRIA
JACKAL | HACKTIVIST
KITTEN | IRAN
LEOPARD | PAKISTAN
LYNX | GEORGIA
OCELOT | COLOMBIA
PANDA | PEOPLE’S REPUBLIC OF CHINA
SPIDER | ECRIME
TIGER | INDIA
WOLF | TURKEY
SPHINX | EGYPT

## Threat Landscape Overview
34 new adversaries tracked by CrowdStrike, raising the total to 232
Cloud environment intrusions increased by 75% YoY
76% YoY increase in victims named on eCrime dedicated leak sites
Cloud-conscious cases increased by 110% YoY
84% of adversary-attributed cloud-conscious intrusions were focused on eCrime

+34
232
75%
76%
110%
84%
year over year = (YoY)

Today’s cyber threats are particularly alarming due to the widespread use of hands-on or “interactive intrusion” techniques, which involve adversaries actively executing actions on a host to accomplish their objectives. Unlike malware attacks that depend on the deployment of malicious tooling and scripts, interactive intrusions leverage the creativity and problem-solving skills of human adversaries. These individuals can mimic expected user and administrator behavior, making it difficult for defenders to differentiate between legitimate user activity and a cyberattack.

In 2023, CrowdStrike observed a 60% year-over-year increase in the number of interactive intrusion campaigns, with a 73% increase in the second half compared to 2022.

The technology sector was the most frequently targeted industry in which CrowdStrike CAO observed interactive intrusion activity in 2023, a continuing trend from 2022. The charts below reflect the relative frequency of intrusions in the top 10 industry verticals and in geographical regions.

After gaining initial access to a network, adversaries seek to “break out” and move laterally from the compromised host to other hosts within the environment. The time it takes for them to do this — “breakout time” — is crucial because the initially compromised machines are rarely the ones adversaries need to achieve their goals. They must move laterally into the network, conduct reconnaissance, establish persistence and locate their targets. Responding within the breakout time window allows defenders to mitigate costs and other damages associated with intrusions.

This year, the average breakout time for interactive eCrime intrusion activity decreased from 84 minutes in 2022 to 62 minutes in 2023. The fastest observed breakout time was only 2 minutes and 7 seconds.

Interactive Intrusions by Industry

![Interactive Intrusions by Industry Chart]

Interactive Intrusions by Region

![Interactive Intrusions by Region Chart]

> 75% 71% 62% 51% 40% MALWARE-FREE ACTIVITY 2023 2022 2021 2020 2019

Anatomy of an eCrime Interactive Intrusion

In this case, the security team had the “quarantine on write” policy setting disabled, enabling the four files to be written to disk. The adversary executed a legitimate tool to obtain system information for reconnaissance and then dropped three more files, including ransomware, onto the system. They attempted to execute a network discovery and reconnaissance tool to map out lateral movement options, which was immediately blocked and quarantined by the Falcon sensor. This caused the adversary to open the control panel to understand which security tool was in use. When they identified the Falcon platform, they never attempted to execute the second discovery tool or the ransomware (which would have been prevented and quarantined) and moved to another victim. Within minutes, CrowdStrike CAO threat hunters notified the customer, took the machine offline and reset the user password.

Once an initial compromise occurs, it only takes seconds for adversaries to drop tools and/or malware on a victim’s environment during an interactive intrusion. However, the saying “time is money” holds true for adversaries. More than 88% of the attack time was dedicated to breaking in and gaining initial access. By reducing or eliminating this time, adversaries free up resources to conduct more attacks.

To do this, they have continued to move beyond malware to faster, more effective means such as identity attacks (phishing, social engineering and access brokers) and the exploitation of vulnerabilities and trusted relationships. This trend is apparent over the last five years, as malware-free activity represented 75% of detections in 2023 — up from 71% in 2022.

To gain a better understanding of interactive intrusions, the following timeline illustrates the speed of a real-world hands-on attack:

![Timeline of a real-world hands-on attack]

This trend is partly related to the success of identity attacks, access brokers and the prolific abuse of valid credentials to facilitate access and persistence in victim environments. Access brokers are threat actors who acquire access to organizations and provide or sell this access to other actors, including ransomware operators. These adversaries continued to profit from providing initial access to a variety of eCrime threat actors in 2023, with the number of accesses advertised increasing by almost 20% compared to 2022.

Today’s sophisticated cyberattacks only take minutes to succeed. Adversaries use techniques such as interactive hands-on-keyboard attacks and legitimate tools to attempt to hide from detection. To further accelerate attack tempo, adversaries can access credentials in multiple ways, including purchasing them from access brokers for a few hundred dollars. Organizations must prioritize protecting identities in 2024.

Access Broker Advertisements by Month

![Access Broker Advertisements by Month Chart]

## 2023 Themes
### Identity-Based and Social Engineering Attacks
Adversaries spanning multiple motivations and regions continue to use phishing techniques spoofing legitimate users to target valid accounts, as well as other authentication and identifying data, to conduct their attacks. In addition to stealing account credentials, CrowdStrike CAO observed adversaries targeting API keys and secrets, session cookies and tokens, one-time passwords (OTPs) and Kerberos tickets throughout 2023.

![Identity-based attack vectors]

**Figure 1. Identity-based attack vectors**

ACCOUNT CREDENTIALS
Adversaries can authenticate to a system and/or user account using stolen credentials, which can either be obtained by the adversary directly (for example, using information stealers or exploiting unmanaged edge devices) or by purchasing them.

API KEYS AND SECRETS
Access to protected resources using stolen API keys and secrets may allow an adversary to steal sensitive data. Unless the API keys and secrets are changed, the adversary could maintain indefinite access.

SESSION COOKIES AND TOKENS
Adversaries can steal session cookies and tokens to masquerade as the legitimate user and authenticate to an application.

ONE-TIME PASSWORDS (OTPs)
OTP theft allows the adversary to bypass multifactor authentication (MFA) by SIM swapping, SS7 attacks, socially engineering the victim or email compromise.

KERBEROS AND KERBEROS TICKETS
By stealing or forging Kerberos tickets, adversaries can gain access to encrypted credentials, which can then be cracked offline. CrowdStrike CAO recorded a 583% increase in Kerberoasting attacks in 2023.

BEAR Adversaries Conduct Credential Collection Campaigns

FANCY BEAR conducted regular credential collection campaigns throughout 2023. In March 2023, Microsoft patched a zero-day elevation-of-privilege vulnerability in Microsoft Outlook (CVE-2023-23397), which FANCY BEAR had been exploiting since at least March 2022 to solicit NT LAN Manager authentication sessions from targets using specially crafted spear-phishing emails. The Polish Cyber Command reported that the adversary used this authentication data to connect to Exchange servers and change additional high-value account mailbox permissions through the Exchange Web Services protocol.[^1]

FANCY BEAR also conducted credential phishing campaigns and developed a custom toolkit to capture credentials from Yahoo! Mail and ukr.net webmail users. The adversary expanded this toolkit to use the Browser-in-the-Browser technique in April 2023 and added MFA interception capabilities to its toolkit to collect OTPs sent to the MFA contact (e.g., a phone number) linked to the targeted account.

COZY BEAR has conducted credential phishing campaigns using Microsoft Teams messages to solicit MFA tokens for Microsoft 365 accounts since at least late May 2023. If a user accepts its initial message request, COZY BEAR attempts to socially engineer the target by claiming a change was made to their current MFA settings and stating an MFA code is required for verification.

CrowdStrike® Services has observed COZY BEAR connecting to a compromised account using Microsoft Entra ID (previously Azure Active Directory) before registering a new device and enabling a passwordless phone sign-in for the user. The adversary also exported certificates containing private keys and requested a KRBTGT-authentication ticket for a different account using a legitimately issued certificate.

[^1]: https://www.wojsko-polskie.pl/woc/articles/aktualnosci-w/detecting-malicious-activity-against-microsoft-exchange-servers/

SCATTERED SPIDER Conducts Sophisticated Social Engineering Campaigns

Identity-based techniques are also central to SCATTERED SPIDER tradecraft. Throughout 2023, this adversary conducted sophisticated social engineering campaigns to access victim accounts. SCATTERED SPIDER’s tactics included SMS phishing (smishing) and voice phishing (vishing) to harvest credentials; it also to provide password and/or MFA resets for targeted accounts. In many cases, SCATTERED SPIDER also leveraged earlier intrusions at telecom organizations to SIM swap targeted employee phone numbers, enabling the adversary to then receive SMS messages containing OTP codes.

SCATTERED SPIDER deliberately selects social engineering campaign targets from employees in information security and other IT-related teams. This is likely due to direct employee access to security tools as well as applications and documentation that may support lateral movement and further account compromise. In a minority of incidents, SCATTERED SPIDER targeted accounts belonging to employees who had direct access to company financial resources.

Additionally, SCATTERED SPIDER often configured residential proxies to appear as though they were logging in to victim accounts from the same geographical area as the legitimate account owner. In doing so, the adversary further exhibited its understanding of identity-related security policies in enterprise organizations.

### Adversaries Continue to Develop Cloud-Consciousness
As predicted, cloud environment intrusions increased by 75% from 2022 to 2023 (Figure 2), with cloud-conscious cases increasing by 110% and cloud-agnostic cases increasing by 60%.

Cloud-conscious is a term referring to threat actors who are aware of the ability to compromise cloud workloads and use this knowledge to abuse features unique to the cloud for their own purposes.

eCrime adversaries are especially active in targeting cloud environments: 84% of cloud-conscious intrusions attributed to adversaries were conducted by likely eCrime actors, compared to 16% conducted by targeted intrusion actors. Traditional BGH adversaries, such as INDRIK SPIDER, became more cloud-conscious throughout the year.

SCATTERED SPIDER predominantly drove cloud-conscious activity increases throughout 2023, accounting for 29% of total cases. Throughout 2023, SCATTERED SPIDER demonstrated progressive and sophisticated tradecraft within targeted cloud environments to maintain persistence, obtain credentials, move laterally and exfiltrate data.

Adversaries’ preference for identity-based techniques is evident in their cloud-focused attacks. Next are several observations of cloud- and identity-focused activities categorized by the MITRE ATT&CK® enterprise tactics of Initial Access, Persistence, Privilege Escalation, Credential Access, Lateral Movement, Exfiltration and Impact.

> AS PREDICTED, CLOUD ENVIRONMENT INTRUSIONS INCREASED BY 75% FROM 2022 TO 2023 (FIGURE 2), WITH CLOUD-CONSCIOUS CASES INCREASING BY 110% AND CLOUD-AGNOSTIC CASES INCREASING BY 60%.

![Increases in cloud cases]

**Figure 2. Increases in cloud cases**

INCIDENTS IN THE CLOUD

CLOUD-CONSCIOUS
ACTORS ARE AWARE THEY GAINED ACCESS TO A VICTIM-OWNED CLOUD ENVIRONMENT AND USE THEIR ACCESS TO ABUSE THE VICTIM-OWNED CLOUD SERVICE

CLOUD-CONSCIOUS CASES 110%

60% CLOUD-AGNOSTIC CASES

CLOUD-AGNOSTIC
ACTORS EITHER WERE NOT AWARE THEY HAD COMPROMISED A CLOUD ENVIRONMENT OR DID NOT TAKE ADVANTAGE OF CLOUD FEATURES

2021 2022 2023

75% IN CLOUD INTRUSIONS

Initial Access

Adversaries relied on valid credentials to achieve initial access. They obtained these credentials via accidental credential leakage, brute-force attacks, phishing/social engineering, credential stealers, access brokers, insecure self-service password-reset services and insider threats.

Persistence

To maintain access to Azure and Microsoft 365, adversaries commonly achieved persistence at the identity level.

Privilege Escalation

Adversaries escalated privileges by obtaining access to additional identities from stored credentials, social engineering campaigns or insecure password-reset portals. They also escalated privileges by modifying policies or adding identities to privileged groups or roles.

> ACHIEVING PERSISTENCE AT THE IDENTITY LEVEL IS COMMONLY ACHIEVED BY REGISTERING ADDITIONAL AUTHENTICATION FACTORS IN ENTRA ID.

> SCATTERED SPIDER USED AN IDENTITY PROVIDER TO ESTABLISH PERSISTENCE WITH A FEDERATED DOMAIN IN ENTRA ID, INITIALLY RELYING ON AADINTERNALS AZURE AD BACKDOOR.[^2] THIS PROVIDED THE ADVERSARY WITH PERSISTENT ACCESS TO MULTIPLE ENTRA ID IDENTITIES. LATER, SCATTERED SPIDER TRANSFERRED THE CONCEPT TO OKTA AND ADDED A FEDERATED IDENTITY PROVIDER TO A VICTIM’S OKTA TENANT.

> IN THE WILD
> DURING AN INTRUSION TARGETING A NORTH AMERICAN SOFTWARE COMPANY, SCATTERED SPIDER ESCALATED PRIVILEGES BY ATTACHING A NEW ADMINISTRATOR ACCESS POLICY TO A PREEXISTING CLOUD USER, TO WHICH THEY ADDED A NEW ACCESS KEY.

> IN THE WILD
> FANCY BEAR AND SCATTERED SPIDER COMMONLY TARGETED MICROSOFT 365 CREDENTIALS VIA CREDENTIAL-PHISHING ATTACKS.

[^2]: https://aadinternals.com/post/aadbackdoor/

Credential Access

Threat actors harvested credentials from password stores and information repositories.

Lateral Movement

Threat actors moved back and forth between on-premises and cloud environments.

Exfiltration

Adversaries exfiltrated data by using tooling, by directly downloading data from internet-accessible repositories — such as SharePoint Online or GitHub — or by uploading data to internet-accessible web services.

> SCATTERED SPIDER OFTEN USED ACCESS TO VICTIMS’ MICROSOFT 365 ENVIRONMENTS TO SEARCH SHAREPOINT ONLINE FOR VIRTUAL PRIVATE NETWORK (VPN) SETUP INSTRUCTIONS AND THEN LOGGED ON TO THE VPN AND MOVED LATERALLY TO ON-PREMISES SERVERS.

> SCATTERED SPIDER WAS ALSO OBSERVED USING AZURE RUN COMMANDS AND SIMILAR CAPABILITIES TO MOVE LATERALLY FROM THE CLOUD CONTROL PLANE TO COMPUTE INSTANCES.

> IN THE WILD
> SCATTERED SPIDER LEVERAGED THE OPEN-SOURCE S3 BROWSER TO EXFILTRATE DATA TO AN EXTERNAL, ADVERSARY-CONTROLLED CLOUD STORAGE BUCKET.

> IN THE WILD
> INDRIK SPIDER ACCESSED CREDENTIALS STORED IN AZURE KEY VAULT. IN A SEPARATE ATTACK, SCATTERED SPIDER ACCESSED CREDENTIALS STORED IN A CLOUD SECRETS MANAGER, AN IDENTITY-BASED SECRETS AND ENCRYPTION MANAGEMENT SYSTEM, AND SHAREPOINT.

> IN ANOTHER CASE, SCATTERED SPIDER ALSO LOCATED A DOMAIN CONTROLLER INSIDE A VICTIM’S AZURE TENANT, COPIED THE DISKS AND CREATED A NEW ADVERSARY-CONTROLLED VIRTUAL MACHINE (VM) INTO WHICH THEY MOUNTED DOMAIN-CONTROLLER DISK COPIES. FROM THOSE DISK COPIES, THE ADVERSARY DUMPED ACTIVE DIRECTORY (AD) DATABASE NTDS.DIT.

Impact

Some cloud-conscious BGH threat actors targeted cloud storage as part of their operations.

> CROWDSTRIKE CAO SPECIFICALLY OBSERVED SCATTERED SPIDER ADOPTING BGH TACTICS AND DEPLOYING RANSOMWARE FOR IMPACT.

> IN A SEPARATE INCIDENT, AN ALPHA SPIDER AFFILIATE DEPLOYED TOOLING THAT ENABLES Alphv TO ENCRYPT AZURE STORAGE FILE SHARES. IN A LockBit INCIDENT, INDRIK SPIDER DELETED BACKUPS STORED IN AZURE BACKUPS.

### Third-Party Relationship Exploitation
Throughout 2023, targeted intrusion actors consistently attempted to exploit trusted relationships to gain initial access to organizations across multiple verticals and regions. This type of attack takes advantage of vendor-client relationships to deploy malicious tooling via two key techniques: 1) compromising the software supply chain using trusted software to spread malicious tooling and 2) leveraging access to vendors supplying IT services.

Threat actors targeting third-party relationships are motivated by the potential return on investment (ROI): One compromised organization can lead to hundreds or thousands of follow-on targets. These stealthy attacks can also more effectively provide an opportunity for attackers seeking to exploit a hardened end target.

> FOR MORE INFORMATION ON ANY OF THE ADVERSARIES MENTIONED IN THIS REPORT AND THOSE TARGETING YOUR INDUSTRY OR REGION, CHECK OUT THE CROWDSTRIKE ADVERSARY UNIVERSE.

Threat Highlight: Trusted-Relationship Compromises by China-Nexus Adversaries

In 2023, China-nexus adversaries increasingly targeted third-party relationships in efforts to deploy malicious implants and gain initial access. Two adversaries — JACKPOT PANDA and CASCADE PANDA — consistently exploited trusted relationships through supply chain compromises and actor-on-the-side or actor-in-the-middle attacks. In each case, the operations focused on Chinese-speaking victims, possibly indicating ongoing domestic surveillance.

Throughout 2023, JACKPOT PANDA continued to use trojanized executables to deploy malicious utilities or second-stage implants. Beginning in May 2023, the adversary used a trojanized installer for CloudChat, a China-based chat application popular with illegal, Chinese-speaking gambling communities in Mainland China. The trojanized installer served from CloudChat’s website contained the first stage of a multi-step process that ultimately deployed XShade — a novel implant with code that overlaps with JACKPOT PANDA’s unique CplRAT implant.

Additional JACKPOT PANDA activity was identified in May 2023 using a signed .NET downloader, dubbed QuestDownloader, launched by a LiveHelp100 process. LiveHelp100 is associated with Comm100, a software utility targeted by a JACKPOT PANDA supply chain compromise in September 2022. QuestDownloader was ultimately used to deploy Cobalt Strike and UltraVNC.

Beginning in late 2023, CASCADE PANDA routinely used likely actor-in-the-middle or actor-on-the-side attacks to intercept legitimate update traffic from common utilities, as well as Chinese-language tools, to deploy WinDealer — a malicious remote access tool (RAT) uniquely associated with this adversary. In all CASCADE PANDA instances from this time period, legitimate software update processes connected to legitimate infrastructure associated with respective products and legitimate Chinese internet service provider infrastructure.

CASCADE PANDA likely distributes WinDealer by using domestic infrastructure to redirect legitimate traffic in transit. In one instance, CASCADE PANDA used a legitimate trojanized Chinese-language translation tool executable to deploy WinDealer.

Unattributed targeted intrusion actors using TTPs consistent with China-nexus adversaries also exploited trusted relationships to conduct operations in 2023. Throughout the second half of the year, an unattributed actor compromised an India-based information security software vendor and used the resulting access to distribute trojanized executables via legitimate software update processes. These attacks target victims from multiple regions and industries, including the construction, financial services, government, technology, telecom and logistics sectors throughout the U.S., India, Brazil, Sri Lanka, the Philippines, Zambia, Mexico and Malaysia. Though this trusted-relationship exploitation activity remains unattributed, the final payload used in this attack shares significant code overlaps with BackShell and StealthPipes, two tools uniquely attributed to WET PANDA.

A second unattributed actor was observed in late 2023 distributing ShadowPad to suspected Chinese-speaking targets as part of a likely supply chain compromise. The actor compromised a China-based virtual conference platform and leveraged the resulting access to deploy a trojanized ShadowPad installer masquerading as a legitimate software tool. Though this activity is unattributed, ShadowPad is exclusively used by China-nexus adversaries such as AQUATIC PANDA, WICKED PANDA and VAPOR PANDA.

In early 2023, an unattributed actor likely compromised an update server associated with iPhone i4Tools management software to deploy AvanteGarde, a malware framework associated with China-nexus activity cluster InnateSpark. Though CrowdStrike CAO was able to confirm at least 250 customers had connected to the compromised update server, only 10% received the malicious update, possibly indicating the actor down-selected high-value targets.

Threat Highlight: North Korea’s Supply Chain Compromises

Democratic People’s Republic of Korea (DPRK) adversaries also demonstrated an increased interest in exploiting trusted relationships in 2023. In particular, LABYRINTH CHOLLIMA abused a trusted relationship between a technology vendor and a client in three instances last year, highlighting an interest in using supply chain compromises as an intrusion vector.

This exploitation tradecraft was first observed in March 2023, when an adversary compromised software at VoIP provider 3CX. This compromise appears to have started with an upstream supply chain compromise of financial technology firm Trading Technologies. The adversary used trojanized 3CX Electron Windows and macOS desktop application variants to deliver information stealers to victim environments. The threat actors then persisted with a July 2023 campaign that similarly abused access to a technology company in efforts to compromise its product and use legitimate infrastructure to infiltrate the compromised company’s clientele.

CrowdStrike CAO also observed LABYRINTH CHOLLIMA distributing malware via a trojanized CyberLink media player variant. This campaign stands out among other LABYRINTH CHOLLIMA supply chain compromises, as the adversary used execution guardrails that limited the campaign to a specific geography and temporal window, suggesting the targeting of a particular victim set.

The motivation driving these compromises remains undefined. In one supply chain compromise, CrowdStrike CAO detected trojanized software in the environments of 62 customers; however, subsequent supply chain compromises were more limited in scope. The adversary may be using supply chain compromises to cast a wide net and deliver appropriate follow-on tooling to interesting targets.

LABYRINTH CHOLLIMA is equally likely abusing trusted relationships between suppliers and product users to infiltrate specific high-value targets for currency generation and espionage campaigns. CrowdStrike CAO assesses that additional LABYRINTH CHOLLIMA supply chain compromises are increasingly likely to occur in the near future. The adversary likely considers supply chain compromise a useful tactic with potential to streamline operations. This assessment is made with moderate confidence based on the volume of supply chain compromises observed in 2023.

Outlook: Third-Party Relationship Exploitation

Trusted-relationship compromises