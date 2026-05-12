# 2024 Threat Hunting Report

## Table of Contents
- [Introduction](#introduction)
- [Naming Conventions](#naming-conventions)
- [Front-Line Snapshot](#front-line-snapshot)
- [Sector Targeting](#sector-targeting)
- [Sector Spotlights](#sector-spotlights)
- [Intrusion Trends by Adversary](#intrusion-trends-by-adversary)
- [Observations from the Front Lines](#observations-from-the-front-lines)
- [Hunting the Cross-Domain Threat](#hunting-the-cross-domain-threat)
- [Case Study: SCATTERED SPIDER Abuses Cloud Management Agent to Establish Persistence](#case-study-scattered-spider-abuses-cloud-management-agent-to-establish-persistence)
- [Hunting the Insider Threat](#hunting-the-insider-threat)
- [Case Study: FAMOUS CHOLLIMA Insider Threats Target 100+ U.S.-Based Companies](#case-study-famous-chollima-insider-threats-target-100-u.s.-based-companies)
- [Identity Hunting](#identity-hunting)
- [Case Study: HORDE PANDA Activity](#case-study-horde-panda-activity)
- [Cloud Hunting](#cloud-hunting)
- [Case Study: Adversaries Pivot Between Cloud Control Plane and Hosted VMs](#case-study-adversaries-pivot-between-cloud-control-plane-and-hosted-vms)
- [Case Study: Threat Actor Enumerates Cloud Account Information from Compromised VMs](#case-study-threat-actor-enumerates-cloud-account-information-from-compromised-vms)
- [Endpoint Hunting](#endpoint-hunting)
- [Case Study: Hunting the STATIC KITTEN Adversary](#case-study-hunting-the-static-kitten-adversary)
- [Countering the Adversary](#countering-the-adversary)
- [Case Study: Hunting PUNK SPIDER](#case-study-hunting-punk-spider)
- [Conclusion](#conclusion)
- [About CrowdStrike](#about-crowdstrike)

---

## Introduction

Stealth and speed were the dominant themes of the 2023 cyber threat landscape. Adversaries have faced a hardened attack surface due to advancements in threat defense technology and threat awareness. In response, they have increasingly adopted and relied on techniques that allow them to move faster and evade detection.

CrowdStrike's Counter Adversary Operations team brings together industry-leading threat intelligence and pioneering managed threat hunting with the AI-powered CrowdStrike Falcon® platform to detect, disrupt and stop today’s sophisticated adversaries. Their efforts safeguard thousands of customers from the most sophisticated adversaries by providing the intelligence, threat hunting skills and resources that most organizations lack.

As adversaries adopt new tactics, the CrowdStrike OverWatch team does the same. Cross-domain threat hunting has become essential as threat actors target multiple domains across an organization's infrastructure — most notably identity, endpoint and cloud — in their efforts to evade detection. These cross-domain threats pose a challenge to threat hunters because they often generate fewer detections in a single domain or product, making the activity difficult to recognize as malicious. Adversaries that gain access continue to operate under the radar using legitimate remote monitoring and management (RMM) tools. As they strive to shrink their footprint and refine their attacks, CrowdStrike OverWatch works tirelessly to detect them with cross-domain threat hunting.

![The CrowdStrike 2024 Threat Hunting Report highlights the trends the CrowdStrike OverWatch team has observed over the past 12 months and details how CrowdStrike OverWatch utilizes proactive, intelligence-informed threat hunting to relentlessly track, detect and ultimately disrupt the adversary no matter when or where they operate.]

The cross-domain threat is increasing as adversaries attempt to infiltrate targets through human access, commonly known as “insider threats.” This year, CrowdStrike OverWatch identified individuals associated with the Democratic People’s Republic of Korea (DPRK)-nexus adversary FAMOUS CHOLLIMA applying to, or actively working at, more than 100 unique companies. This threat actor exploited the recruitment and onboarding processes to obtain physical access through legitimately provisioned systems, which were housed at intermediary locations. The adversary insiders remotely accessed these systems to log in to corporate VPNs posing as developers. This masquerade gave FAMOUS CHOLLIMA deeply enduring access to dozens of organizations and proved nearly impossible to detect without the benefit of CrowdStrike OverWatch threat hunting and the support of far-reaching visibility provided by the Falcon platform.

In addition to conducting cross-domain attacks, adversaries are developing greater expertise in moving seamlessly between platforms and using tools that are equally effective across operating systems. This rise in “hybrid threats” presents significant challenges to defenders across disciplines. DPRK-nexus adversaries, for example, quickly navigate multiple platforms, build custom tooling and spontaneously pivot actions on objectives — highlighting the need for fast, proactive and intelligence-driven hunting to stay one step ahead of the threat actors.

Identity-based detections are particularly important, as they can identify suspicious activity on unmanaged hosts and supplement traditional endpoint detection and response (EDR) events. Consistent with last year, threat actors increasingly use identity-based attacks to gain initial access. Using CrowdStrike Falcon® Identity Protection, CrowdStrike OverWatch threat hunters continued to expand their hunting mission and routinely countered persistent adversaries that employ identity attacks, including formidable threat actors like China-nexus HORDE PANDA.

Adversaries are also increasingly pivoting to cloud environments, with a noted 75% increase in 2023, as stated in the CrowdStrike 2024 Global Threat Report. While many threat actors employ basic techniques, others — such as prolific eCrime adversary SCATTERED SPIDER and Russia-nexus adversary COZY BEAR — evolve quickly, and proactive hunters must stay one step ahead in the cloud. CrowdStrike OverWatch keeps pace with these adversaries by developing innovative hunting techniques for cloud services, workloads and control planes as well as using advances in CrowdStrike's identity protection module.

While threat hunters faced many new challenges in the past 12 months, long-standing endpoint threats did not abate. Adversaries continued to leverage a seemingly endless list of RMM tools, which are appealing due to their wide availability and their use as legitimate solutions in many organizations. eCrime and targeted intrusion adversaries alike continue to rely on RMM tooling. Examples include eCrime adversary CHEF SPIDER and Iran-nexus adversary STATIC KITTEN, which both used phishing campaigns delivering RMM tools to create an effective initial access beachhead.

Speed, accuracy and threat intelligence are integral components to countering the adversary through proactive hunting. This year, in the MITRE Engenuity ATT&CK® Evaluations: Managed Services, Round 2, detection-only test, CrowdStrike delivered comprehensive detection coverage and rapid mean time to detect (MTTD) at an impressive four minutes.

Over the past 12 months, CrowdStrike OverWatch threat hunters distilled their findings into hundreds of new behavior-based preventions. As a result, the team’s front-line findings directly augment the Falcon platform’s ability to detect and prevent the latest threats. In the past year alone, these new behavior-based detections have enabled the Falcon platform to prevent an additional 2.4 million malicious events that would have otherwise evaded autonomous detection methods — amounting to approximately 4.6 preventions per minute.

The CrowdStrike 2024 Threat Hunting Report presents trends identified from July 1, 2023, to June 30, 2024, exposed by proactive, intelligence-informed threat hunting. Year-over-year, CrowdStrike OverWatch observed the following:

- **Interactive intrusions increased by 55%.** An interactive intrusion occurs when threat actors perform hands-on-keyboard activities within a victim's environment.
- **86% of all interactive intrusions were attributed to eCrime activity.**
- **eCrime-related interactive intrusions against the healthcare sector increased 75%.**
- **Interactive intrusions impacting the technology sector increased 60%**, making technology the most frequently targeted industry for the seventh consecutive year.
- **FAMOUS CHOLLIMA insiders were identified applying to or actively working at more than 100 unique companies.**
- **Adversary use of RMM tools increased 70%**, and 27% of all interactive intrusions leveraged RMM tools.

This report represents the Counter Adversary Operations team’s relentless efforts to disrupt the adversary. Behind every CrowdStrike threat hunter is the power of a unified security solution, empowering hunters with the richest security telemetry — encompassing endpoint, identity and cloud workloads as well as intelligence — to find and stop adversaries in their tracks.

## Naming Conventions

| Nation-State or Category | Adversary |
| :--- | :--- |
| RUSSIA | BEAR |
| VIETNAM | BUFFALO |
| DPRK (NORTH KOREA) | CHOLLIMA |
| ROK (REPUBLIC OF KOREA) | CRANE |
| SYRIA | HAWK |
| HACKTIVIST | JACKAL |
| IRAN | KITTEN |
| PAKISTAN | LEOPARD |
| GEORGIA | LYNX |
| COLOMBIA | OCELOT |
| PEOPLE’S REPUBLIC OF CHINA | PANDA |
| KAZAKHSTAN | SAIGA |
| EGYPT | SPHINX |
| eCRIME | SPIDER |
| INDIA | TIGER |
| TURKEY | WOLF |

## Front-Line Snapshot

![Interactive intrusions are typically more sophisticated and difficult to detect compared to automated attacks, requiring advanced threat hunting and incident response capabilities to identify and mitigate.]

The statistics provided in this report reflect insights from the CrowdStrike OverWatch threat hunting team from July 1, 2023, through June 30, 2024. This data specifically focuses on interactive intrusions — attacks where adversaries establish an active presence within a target network, often engaging in hands-on-keyboard activities to achieve their objectives.

Unlike automated attacks, interactive intrusions involve human operators who interact with systems in real time, adapting their tactics as needed. Interactive intrusions are typically more sophisticated and difficult to detect compared to automated attacks, requiring advanced threat hunting and incident response capabilities to identify and mitigate.

Interactive intrusions are characterized by:

- **Manual Intervention**: Attackers manually navigate the network, leveraging their skills and knowledge to bypass security controls.
- **Persistence**: Attackers establish and maintain long-term access to the network, often using advanced techniques to evade detection.
- **Lateral Movement**: After gaining initial access, attackers move laterally across the network to identify and compromise additional systems.
- **Data Exfiltration**: The primary goal is often to steal sensitive data, intellectual property or credentials.
- **Customization**: Attackers tailor their techniques to the specific environment and defenses of the target organization.

Over the past 12 months, CrowdStrike OverWatch observed interactive intrusions continue to climb, increasing 55% year-over-year. The overall distribution of interactive intrusion activity by threat type saw a noted increase in activity by eCrime adversaries — 86% of the total volume was associated with eCrime — highlighting the increased threat posed by criminal threat actors seeking financial gain. These observations underscore the persistent and pervasive threat of eCrime adversaries as well as CrowdStrike OverWatch’s ability to quickly identify and uncover them.

![Interactive Intrusions Over Time | Q3 2022-Q2 2024]
![Interactive Intrusions by Motivation | Q3 2023-Q2 2024 (14% Targeted Intrusions, 86% eCrime)]
![Top Verticals by Intrusion Frequency | Q3 2023-Q2 2024]

## Sector Targeting

For the reporting period, interactive intrusions impacting technology entities increased 60% year-over-year, making technology the most frequently targeted industry for the seventh consecutive year. The technology sector encompasses a broad range of organizations that develop computer software and hardware or provide IT services or technology. Due to its relationship to many other verticals, the technology sector is a high-value target for both targeted intrusion and eCrime adversaries.

![Figure 2. Targeted sectors by intrusion frequency, July 2022-June 2023 vs. July 2023-June 2024]

## Sector Spotlights

### Healthcare
While technology entities remain attractive targets for various adversaries, eCrime-related interactive intrusions against healthcare entities increased 75% over the prior 12 months. The healthcare sector includes a large variety of entities that possess patients’ protected health information (PHI), financial information (such as credit card and bank account numbers) and personally identifiable information (PII), making these entities a prime target for eCrime threat actors.

Big game hunting (BGH) adversaries — which remain the primary threat to all sectors, including healthcare — use data theft, extortion and ransomware to pressure victims into paying a ransom. Access brokers — threat actors that acquire access to organizations and provide or sell this access to other actors — and commodity services also continue to threaten the healthcare sector by facilitating the financially motivated operations of other eCrime threat actors. To evidence this threat, access broker advertisements for healthcare entities increased 142% compared to the previous 12 months.

### Consulting and Professional Services
Targeted intrusion activity targeting the consulting and professional services vertical increased by 141% year-over-year, moving this vertical up to second place in overall sector targeting trends and displacing both financial services and retail.

The consulting and professional services sector provides specialist services and/or consultancy and is staffed by employees with specific skill sets or training. This sector includes human resources, architectural, recruitment agency, consultancy and marketing services. Consulting and professional services entities possess a significant amount of sensitive information — including financial and personal data, strategic plans and trade secrets — that makes these entities increasingly attractive for targeted intrusion adversaries.

Given the sector’s supporting nature, targeted intrusion adversaries can also target entities in this sector to gain access to additional downstream victims. The consulting and professional services sector is becoming a popular target for various eCrime adversaries, including BGH threat actors and access brokers, as entities within this sector present numerous opportunities for these threat actors to profit financially. To evidence this threat, access broker advertisements for consulting and professional services entities increased 152% year-over-year.

## Intrusion Trends by Adversary

CrowdStrike is a pioneer in adversary profiling and attribution. With detailed information into 245+ attributed eCrime, targeted intrusion and hacktivist adversaries — and more than 140 active clusters of malicious activity that have not yet met CrowdStrike’s standards for adversary graduation — CrowdStrike OverWatch threat hunters are well positioned to quickly and accurately disrupt the adversary.

![Figure 4. Interactive adversary disruptions across the world, July 2023-June 2024]

eCrime adversaries are the most prevalent type of threat actors that CrowdStrike OverWatch threat hunters disrupt; these adversaries are prolific and often opportunistic. In many instances, CrowdStrike OverWatch detects targeted intrusion adversary activity early in the kill chain before it reaches an interactive stage.

## Observations from the Front Lines

### Hunting the Cross-Domain Threat
Cross-domain threat hunting refers to CrowdStrike OverWatch’s ability to identify adversary behavior even when it takes place across several domains of an organization's security structure, notably identity, endpoint and cloud. Attacks that take place across multiple domains pose a significant challenge because they often generate fewer detections in any single domain or product.

### Case Study: SCATTERED SPIDER Abuses Cloud Management Agent to Establish Persistence
In May 2024, CrowdStrike OverWatch observed SCATTERED SPIDER establish a foothold on a cloud-hosted virtual machine (VM) instance via a cloud service VM management agent. To do so, the adversary compromised existing credentials to authenticate to the cloud control plane via an identified phishing campaign.

After authenticating to the cloud console, the adversary established persistence by executing commands on the cloud-hosted VM via the management agent. After establishing an initial connection, SCATTERED SPIDER executed the ping command against several domains within and outside of the target organization, likely to identify their level of access and visibility within the network. The adversary then ran several variations of the `nltest` command to identify domain controllers (DCs) of interest and the `wmic` command to identify programs currently installed on the host.

Finally, the adversary established persistence by creating a new user on the host and attempting to download FleetDeck remote access software.

![Figure 5. SCATTERED SPIDER cross-domain attack]

### Hunting the Insider Threat
CrowdStrike OverWatch hunters are continually faced with new challenges as adversaries increasingly seek stealthy and creative avenues for initial access. In addition to leveraging cross-domain attacks, adversaries are becoming more platform-agnostic, moving seamlessly between platforms with tooling and capabilities that are equally effective for Windows, macOS and Linux.

### Case Study: FAMOUS CHOLLIMA Insider Threats Target 100+ U.S.-Based Companies
In April 2024, CrowdStrike Services responded to the first of several incidents in which FAMOUS CHOLLIMA malicious insiders targeted more than 30 U.S.-based companies, including aerospace, defense, retail and technology organizations. The malicious insiders claimed to be U.S. residents and were hired in early 2023 for multiple remote IT positions.

Leveraging information from a single incident, CrowdStrike OverWatch quickly developed a scalable plan to hunt for this emerging insider threat and discovered more than 30 additional affected customers within two days. Threat hunters found that after obtaining employee-level access to victim networks, the insiders performed minimal tasks related to their job role. In some cases, the insiders also attempted to exfiltrate data using Git, SharePoint and OneDrive. Additionally, the insiders installed the following RMM tools: RustDesk, AnyDesk, TinyPilot, VS Code Dev Tunnels and Google Chrome Remote Desktop.

![Figure 6. Hunting FAMOUS CHOLLIMA insider threat operations]

## Identity Hunting
Adversaries continue to maximize the use of stolen identities and attempt to minimize defenders’ network visibility by “living off the land” and therefore reducing potential indicators or alerts on the endpoint, which the adversary knows is heavily scrutinized. This tactic hinders threat hunters’ ability to differentiate adversary activity from typical user and system administrator activity.

### Case Study: HORDE PANDA Activity
Between late June 2023 and early August 2023, using identity-based indicators, CrowdStrike OverWatch identified suspicious activity at a South Asian telecommunications provider. The China-nexus HORDE PANDA adversary leveraged multiple compromised identities to attempt to embed themselves further into the network and move laterally. The adversary gained initial access via the VPN IP range.

## Cloud Hunting
The boundary between the endpoint domain and cloud domain is increasingly blurred as adversaries develop their cross-domain prowess. As the number of organizations moving to or hosting data on cloud services increases, so does the importance of defending cloud environments.

### Case Study: Adversaries Pivot Between Cloud Control Plane and Hosted VMs
Traditional BGH adversaries continue to lead cloud-conscious activity. SCATTERED SPIDER remains the most prominent adversary in cloud-based intrusions, conducting 29% of all associated activity observed in 2023.

### Case Study: Threat Actor Enumerates Cloud Account Information from Compromised VMs
In this case, a threat actor accessed a cloud-hosted VM from a malicious implant predating the Falcon sensor and used a pre-installed command line tool to enumerate information from the cloud control plane. The command line tool allows users to update and query information from their cloud account using a specified set of commands.

## Endpoint Hunting
CrowdStrike OverWatch’s threat hunters have constantly honed and refined their tooling and threat hunting methodologies to adapt to the constantly evolving threat landscape. Though novel TTPs for endpoint exploitation are always emerging, adversaries still frequently rely on previous reliable techniques, including leveraging legitimate RMM tools for illicit activity.

### Case Study: Hunting the STATIC KITTEN Adversary
Targeted intrusion adversaries, including prolific Iran-based adversary STATIC KITTEN, also continue to rely on RMM tooling in their operations. STATIC KITTEN routinely relies on RMM tools for persistence within target networks, and during the past year, CrowdStrike OverWatch observed the adversary using multiple RMM tools, including Atera, Level.io, SimpleHelp, ScreenConnect, Tactical RMM and Action1.

## Countering the Adversary
### Case Study: Hunting PUNK SPIDER
[Content regarding PUNK SPIDER activity and disruption.]

## Conclusion
[Summary of the 2024 threat landscape and the importance of proactive, intelligence-informed threat hunting.]

## About CrowdStrike
[Company information.]

[^1]: MITRE ATT&CK and ATT&CK are registered trademarks of The MITRE Corporation. To learn more about MITRE ATT&CK, visit https://attack.mitre.org/matrices/enterprise/.
[^2]: U.S. Department of Justice, “Charges and Seizures Brought in Fraud Scheme, Aimed at Denying Revenue for Workers Associated with North Korea,” May 16, 2024: www.justice.gov/opa/pr/charges-and-seizures-brought-fraud-scheme-aimed-denying-revenue-workers-associated-north; Federal Bureau of Investigation (FBI), “Democratic People's Republic of Korea Leverages U.S.-Based Individuals to Defraud U.S. Businesses and Generate Revenue,” May 16, 2024: https://www.ic3.gov/Media/Y2024/PSA240516

---

iles via msiexec.exe is a standard Windows execution method,
resulting in a significant amount of data to analyze. Determining which

processes may be malicious by process name alone can be time-

consuming.

Even narrowing a search to include only RMM software installers may

not yield results, as adversaries such as STATIC KITTEN will often

rename the installer file.

To identify RMM tool execution (such as Atera Agent), CrowdStrike

OverWatch threat hunters search for command lines containing

integrator login account details in the form of email addresses.

Additionally, CrowdStrike OverWatch focuses on STATIC KITTEN’s

common delivery methods. The adversary regularly downloads tooling

from cloud service providers; another way to detect STATIC KITTEN

is by hunting for web browser processes containing single-argument

command lines to cloud storage services. Organizations with

embedded threat hunting teams can further narrow their search

criteria by identifying which RMM and cloud storage services are

expected in their environment.

STATIC KITTEN routinely changes TTPs and operational cadence

for each campaign, but CrowdStrike OverWatch threat hunters have

observed that STATIC KITTEN often recycles techniques — albeit with

variations — in each campaign. For example, the adversary may update

or rewrite their custom tooling, but the execution method may remain

the same. Alternatively, while STATIC KITTEN may use a new RMM

tool, they may use the same cloud storage provider to deliver the tool

to a targeted host. CrowdStrike OverWatch threat hunters collaborate

closely with the larger CrowdStrike Counter Adversary Operations team

to track adversaries such as STATIC KITTEN by understanding their

actions across their entire kill chain.

CROWDSTRIKE 2024 THREAT HUNTING REPORT
35

To hunt for and protect against RMM threats,

CrowdStrike recommends the following measures:

 ► Establish a baseline of approved RMM software and expected RMM users

in your organization by collaborating with relevant stakeholders such as IT

services. Thoroughly investigate unexpected RMM tools or users.

 ► Establish a baseline of expected legitimate RMM tool behavior. Profile normal

directory paths, remote connection domains, remote IP addresses and files written

by RMM tools. For example, AnyDesk normally writes a file named gcapi.dll; files with
other names may be malicious. Define expected child and grandchild process trees.

 ► Monitor for known RMM tool-related filenames, file paths or process names.

Though some adversaries rename RMM tools, less sophisticated adversaries do not.

 ○ For example, ScreenConnect’s network deployer is named

ScreenConnectClientNetworkDeployer.exe by default. TeamViewer’s core
process is named TeamViewer_Desktop.exe by default, and the main GUI process is
named TeamViewer.exe. AnyDesk is installed to C:\ProgramData\AnyDesk\AnyDesk.exe
by default.

 ► Monitor for or block access to main service provider domains hosting RMM tools

(e.g., download.teamviewer[.]com).

 ► Monitor for anomalous DNS requests and network connections typical of unexpected RMM tools.

 ► Monitor process trees for anomalous parameters and flags typical of unexpected RMM tools:

 ○ ConnectWise ScreenConnect uses numerous launch parameters, including e,  y,  h,  p,  s,  k,  t

and c (see Figure 11).

 ○ ConnectWise ScreenConnect can run manual shell commands that manifest as .cmd

scripts with filenames ending in run.cmd
(e.g., "cmd.exe" /c "C:\Windows\TEMP\ScreenConnect\<version>\<uuid>run.cmd").

 ○ AnyDesk command line installers (EXE and MSI versions) run with the –install flag, and

adversaries typically install AnyDesk with the –silent flag.

"C:\Program Files (x86)\ScreenConnect Client

([uuid])\ScreenConnect.ClientService.exe"

"?e=Access&y=Guest&h=instance-[REDACTED - Relay

ID]-relay.screenconnect.com&p=443&s=[truncated]&k=[truncated]&t=&c=&c=

&c=&c=&c=&c=&c=&c="

Figure 11. ScreenConnect launch process example

 ► Search for artifacts (such as logs) that RMM tools write to disk.

For example, AnyDesk artifacts are written to C:\ProgramData\AnyDesk\ or
C:\Users\%Username%\Appdata\Roaming\AnyDesk\ by default. ConnectWise typically writes files
to C:\Program Files (x86)\ScreenConnect Client ([uuid])\.

CROWDSTRIKE 2024 THREAT HUNTING REPORT
36

Countering
the Adversary

Hunting and countering today’s adversaries requires speed, accuracy and

human ingenuity — and CrowdStrike delivers all three. As adversaries continue

to evolve, threat hunters have to apply creative and lateral thinking to ensure

they maintain the speed and accuracy necessary to outpace the adversary.

The CrowdStrike 2024 Global Threat Report identified that the average

breakout time for an eCrime adversary was 62 minutes in 2023. Breakout time

refers to the average time it takes an adversary to move laterally within a victim

network after gaining access. For most organizations, 62 minutes is a very

narrow window to disrupt the adversary before they embed, which is where

the support of CrowdStrike OverWatch’s cutting-edge threat hunting bridges

the gap.

To highlight the importance of speed, accuracy and human ingenuity when

hunting and countering the adversary at every turn, the following interactive

intrusion case study examines an attack by one of the most prevalent and

fast-moving eCrime adversaries: PUNK SPIDER.

When accessing victims’ network environments, PUNK SPIDER typically

operates quickly to identify and exfiltrate sensitive data and deploy Akira
ransomware, requiring an urgent response from network defenders.

In this incident, the Falcon sensor immediately detected the adversary,

and CrowdStrike OverWatch and Falcon Complete prevented PUNK SPIDER

from impacting the victim.

CROWDSTRIKE 2024 THREAT HUNTING REPORT
37

 CASE STUDY:

Hunting PUNK SPIDER

PUNK SPIDER has emerged as one of the most prevalent and fastest

adversaries that CrowdStrike OverWatch has observed over the past year.

First identified in April 2023, PUNK SPIDER is a BGH adversary that develops
and maintains the Akira ransomware and the associated Akira dedicated leak
site (DLS). Similar to many other BGH actors, PUNK SPIDER leverages sensitive

data exfiltration and encryption to extort ransom payments from victims.

In April 2024, CrowdStrike OverWatch and Falcon Complete identified

suspected PUNK SPIDER activity at a North American technology company.

Together — and supplemented with information from the victim — CrowdStrike

identified that PUNK SPIDER had accessed the victim’s network environment
through an unmanaged3 Palo Alto Networks GlobalProtect VPN appliance

vulnerable to CVE-2024-3400 exploitation. The first evidence of adversary

activity was when PUNK SPIDER used a service account to log on to another

network host via Remote Desktop Protocol (RDP), causing the Falcon sensor

to immediately alert CrowdStrike OverWatch to potential malicious activity.

PUNK SPIDER then attempted to dump credentials and deploy legitimate

proxy-tunneling and remote access tools to establish persistence.

The adversary attempted to elevate their privileges by adding compromised

and adversary-created user accounts to local administrator groups and the

ESX Admins group. PUNK SPIDER commonly uses this technique to gain privileged

access to ESXi devices, as members of the ESX Admins group automatically have

administrative access to all ESXi devices in the same Active Directory domain.

However, the Falcon sensor blocked these privilege escalation attempts.

In communication with the victim, Falcon Complete began containing

compromised accounts and devices to prevent PUNK SPIDER from

adversely affecting the victim’s operations.

PUNK SPIDER attempted to use the open-source reconnaissance tool
SharpShares to enumerate network shares — the adversary regularly identifies
network shares before exfiltrating data and deploying their proprietary Akira
ransomware. When the Falcon sensor prevented this execution, the adversary

attempted to use an Antimalware Scan Interface (AMSI) bypass to execute

Invoke-ShareFinder.ps1, another network share reconnaissance
tool — and the Falcon sensor also prevented this execution. PUNK SPIDER
attempted to execute Akira ransomware on compromised devices, and the
Falcon sensor prevented the Akira ransomware from encrypting any files.

Running out of time, PUNK SPIDER used WinRAR to collect and archive data

and attempted to use FileZilla to exfiltrate the file archives. When countering

a known adversary such as PUNK SPIDER, Falcon Complete leverages tactical

custom IOAs and applies them to the customer environment. This prevented

PUNK SPIDER from using FileZilla to exfiltrate data.

3  An unmanaged device is a device without an installed Falcon sensor.

CROWDSTRIKE 2024 THREAT HUNTING REPORT
38

VS.

PUNK SPIDER

INITIAL
ACCESS

A service account is used to RDP
into a system

The Falcon sensor flags this activity as
suspicious and alerts Falcon Complete
and CrowdStrike OverWatch

+ 12-14
MINUTES

PUNK SPIDER begins their initial post-access
actions 12 minutes after leveraging the
compromised credentials

The Falcon sensor prevents these files
from running on the system in real time

RECONNAISSANCE

PUNK SPIDER begins to conduct basic
network reconnaissance and downloads
additional payloads unique across the
CrowdStrike telemetry

The reconnaissance conducted by PUNK
SPIDER triggers CrowdStrike OverWatch
detections, and the Falcon sensor prevents
the additional payloads from running

+ 3
MINUTES

ESCALATION

+ 8
MINUTES

CONTAINMENT

+ 15
MINUTES

+ 60
MINUTES

PUNK SPIDER attempts to dump additional
credentials from the system in an attempt to
look for additional privileges that could help
them in their objectives

The attempted credential dumping creates
additional CrowdStrike OverWatch detections,
which are being actively monitored

PUNK SPIDER begins to introduce custom
scripts onto the system in an attempt to
subvert Falcon sensor preventions

The Falcon sensor flags this activity as
suspicious and alerts Falcon Complete
and CrowdStrike OverWatch

CrowdStrike OverWatch has triggered
customer alerts and provided the details to
its Falcon Complete counterparts

Falcon Complete contains the hosts while
it escalates to the customer and further
investigates

Falcon Complete informs the customer
about the host containment and provides
immediate recommendations

Falcon Complete holds an advisory call
with the customer detailing the disabling of
compromised accounts as well as custom
IOC/IOA preventions that were put in place

Figure 12. CrowdStrike counters PUNK SPIDER at a North American technology company

Throughout the incident, CrowdStrike OverWatch and Falcon Complete identified

PUNK SPIDER-associated user accounts and network traffic and ultimately terminated their

access to the victim, preventing the adversary from exfiltrating data and deploying ransomware.

Adversaries such as PUNK SPIDER will continue to push the limits of their capabilities to achieve

their actions on objectives, often returning to the same target and attempting a new approach.

However, CrowdStrike OverWatch is always one step ahead, constantly improving advanced detections

and gaining insights into adversary behaviors.

CROWDSTRIKE 2024 THREAT HUNTING REPORT39

Conclusion

This report shares the perspectives and insights that CrowdStrike

OverWatch threat hunters gain during interactive intrusion attempts on

a daily basis. As technology evolves and security strategies improve,

adversaries are becoming stronger, smarter and faster. From cross-domain

proficiency to identity-based attacks and cloud targeting, adversaries

continuously strive to widen their reach and deepen their impact.

While adversaries seek weaknesses and search for creative ways to

avoid detection, the CrowdStrike OverWatch team is similarly sharpening

its tools and narrowing its focus. When attackers and defenders battle

over operational sophistication and tradecraft, speed often becomes

the tiebreaker.

As adversaries gain access to victims more quickly and shift gears

when necessary to navigate new security challenges, defenders race to

maintain the advantage. To increase their speed, attackers and defenders

leverage all available tools, including AI. However, attackers have only

recently leveraged AI to conduct faster, more sophisticated attacks,

whereas CrowdStrike has long been using AI to predict adversary

behavior and significantly improve protection.

Since its 2011 founding, CrowdStrike has been at the forefront of machine

learning and AI innovation in cybersecurity, and it will continue to pioneer

in this space. CrowdStrike’s AI is trained on trillions of security events and

augmented with continuous feedback from CrowdStrike OverWatch threat

hunters and intelligence experts. CrowdStrike regularly uses AI to:

 ► Combat increasingly sophisticated attacks by identifying adversary

behavior and threat patterns.

 ► Solve hyperscale data challenges by analyzing intelligence and threat

telemetry with speed and at scale.

 ► Automate repetitive security tasks and unleash machine-speed

intelligence to automate detection and response.

CROWDSTRIKE 2024 THREAT HUNTING REPORT
40

In 2021, CrowdStrike OverWatch patented a hunting tool
that detects security violations.4 The tool employs AI to predict

whether an event is malicious based on the command line’s ancestry.

Using three distinct AI models to identify behaviors associated

with malware and targeted intrusion activity, the tool supports both

hunting lead generation and optimization. It classifies hunting leads,

funneling only relevant data for threat hunters and ensuring that

hunters can operate at scale quickly to identify an intrusion at its

earliest stages.

In today’s challenging threat landscape, tooling is imperative — and AI

is just one tool in an arsenal that empowers CrowdStrike OverWatch

threat hunters. CrowdStrike OverWatch continuously harnesses

cutting-edge technologies to enhance defenses and stop adversaries

in their tracks.

But tooling alone is not enough to thwart today’s sophisticated

adversaries. While CrowdStrike OverWatch threat hunters work

relentlessly to detect and disrupt adversaries, CrowdStrike Counter

Adversary Operations — and the extended CrowdStrike team —

provide additional layers of human expertise and a unified security

approach to stop even the stealthiest of adversaries.

Adversaries aren't stopping, and neither are we. Together, we can

outsmart and outpace today's most sophisticated threats. We have

never been more committed to stopping breaches and building a

more resilient future together.

4  https://www.crowdstrike.com/blog/falcon-overwatch-granted-patents-for-two-innovative-workflow-tools/

CROWDSTRIKE 2024 THREAT HUNTING REPORT
41

About
CrowdStrike

CrowdStrike (Nasdaq: CRWD), a global cybersecurity leader, has redefined

modern security with the world’s most advanced cloud-native platform for

protecting critical areas of enterprise risk — endpoints and cloud workloads,

identity and data.

Powered by the CrowdStrike Security Cloud and world-class AI, the

CrowdStrike Falcon® platform leverages real-time indicators of attack, threat

intelligence, evolving adversary tradecraft and enriched telemetry from across

the enterprise to deliver hyper-accurate detections, automated protection and

remediation, elite threat hunting and prioritized observability of vulnerabilities.

Purpose-built in the cloud with a single lightweight-agent architecture, the

Falcon platform delivers rapid and scalable deployment, superior protection and

performance, reduced complexity and immediate time-to-value.

CrowdStrike: We stop breaches.

Learn more: www.crowdstrike.com

Follow us: Blog | X | LinkedIn | Facebook | Instagram

Start a free trial today: www.crowdstrike.com/free-trial-guide

© 2024 CrowdStrike, Inc. All rights reserved. CrowdStrike, the falcon logo, CrowdStrike Falcon and

CrowdStrike Threat Graph are marks owned by CrowdStrike, Inc. and registered with the United States

Patent and Trademark Office, and in other countries. CrowdStrike owns other trademarks and service

marks, and may use the brands of third parties to identify their products and services.

CROWDSTRIKE 2024 THREAT HUNTING REPORT