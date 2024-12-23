# 2024 Attack Intelligence Report
## Table of Contents
- [Executive Summary](#executive-summary)
- [Big Picture: Threat Climate Change](#big-picture-threat-climate-change)
- [Vulnerability Exploitation Trends](#vulnerability-exploitation-trends)
  - [A Note on Exploitation Terminology](#a-note-on-exploitation-terminology)
  - [2023 New Widespread Threats](#2023-new-widespread-threats)
  - [Ground Zero: Pre-Patch Exploitation](#ground-zero-pre-patch-exploitation)
  - [Countdown to Exfil: File Transfer Hacks](#countdown-to-exfil-file-transfer-hacks)
  - [Silver Linings](#silver-linings)
  - [Other 2023 Exploited Vulnerabilities](#other-2023-exploited-vulnerabilities)
  - [State-Sponsored Threat Activity](#state-sponsored-threat-activity)
- [Ransomware](#ransomware)
  - [2023 Initial Access Vectors](#2023-initial-access-vectors)
- [Life on the Edge: Network Pivots 2020 - 2024](#life-on-the-edge-network-pivots-2020---2024)
- [Attacker Utilities](#attacker-utilities)
- [Vulnerability Classes](#vulnerability-classes)
  - [Programming Language Distribution: 2023 Vulnerabilities](#programming-language-distribution-2023-vulnerabilities)
  - [Government Guidance on Eliminating Key Vulnerability Classes](#government-guidance-on-eliminating-key-vulnerability-classes)
- [Practical Guidance for Defenders](#practical-guidance-for-defenders)
  - [Additional Resources](#additional-resources)
- [Appendix](#appendix)
  - [Notes on Methodology](#notes-on-methodology)
  - [Threat Categorization](#threat-categorization)
  - [Ransomware Citations](#ransomware-citations)
  - [Calculating Time to Known Exploitation (TTKE)](#calculating-time-to-known-exploitation-ttke)
  - [Glossary of Terms](#glossary-of-terms)
    - [Attacker Utilities](#attacker-utilities-1)
    - [Vulnerability Classes](#vulnerability-classes-1)
- [References](#references)

©RAPID7
Caitlin Condon, Director of Vulnerability Intelligence
Stephen Fewer, Principal Vulnerability Researcher
Christiaan Beek, Senior Director of Threat Analytics

Since 2020, Rapid7 has released an annual Vulnerability Intelligence Report 
with curated vulnerability data and in-depth analyses of exploit trends. In an 
effort to broaden the scope of this research and offer a more holistic view of 
the attack landscape, this year's report — renamed The Attack Intelligence 
Report — combines vulnerability and exploit research with hands-on data from 
Rapid7's managed detection and response (MDR) division, as well as our threat 
analytics and emergent threat response teams. 

Our 2024 Attack Intelligence Report presents insights and guidance that 
security practitioners can use to better understand and anticipate modern cyber 
threats. This year’s report highlights multi-year vulnerability and exploit trends 
in addition to examining recent high-impact attacks and CVEs. This research 
is based on 210+ vulnerabilities disclosed since the end of 2019, including 
60+ exploited vulnerabilities from 2023 and early 2024. See our appendix for 
additional context on vulnerability selection.

## Executive Summary
Key findings include:
- In 2023, for the second time in three years, more mass compromise 
events arose from zero-day vulnerabilities than from n-day vulnerabilities. 
- 53% of new widespread threat vulnerabilities through the beginning of 
2024 were exploited before software producers could implement fixes 
— a return to 2021 levels of widespread zero-day exploitation (52%) 
after a slight respite (43%) in 2022. 
- Mass compromise events stemming from exploitation of network edge 
devices have almost doubled since the start of 2023, with 36% of widely 
exploited vulnerabilities occurring in network perimeter technologies. 
- More than 60% of the vulnerabilities Rapid7 analyzed in network and 
security appliances in 2023 were exploited as zero-days. 
- While skilled adversaries are still fond of memory corruption exploits, 
most of the widely exploited CVEs from the past few years have arisen 
from simpler, more easily exploitable root causes, like command injection 
and improper authentication issues. 
- 41% of incidents Rapid7 MDR observed in 2023 were the result 
of missing or unenforced multi-factor authentication (MFA) on internet-
facing systems, particularly VPNs and virtual desktop infrastructure.
- Rapid7 Labs tracked more than 5,600 separate ransomware incidents 
over the course of 2023 and the first few months of 2024. The number of 
unique ransomware families reported across 2023 incidents decreased 
by more than half, from 95 new families in 2022 to 43 in 2023.

![5,600 ransomware incidents over the course of 2023 and early 2024. Rapid7 Labs tracked more than in 2023 the number of unique ransomware families decreased by more than half]

## Big Picture: Threat Climate Change
Over the last several years, Rapid7 researchers have regularly published in-depth 
analyses of significant vulnerabilities and major cyber incidents, prioritizing attack 
vectors that have threatened many organizations globally. In 2020, amid what 
was then considered to be an “outbreak” of critical vulnerability exploitation, 
our research team began tracking widely exploited CVEs separately from 
CVEs used in limited, targeted attacks, which were often conducted by a single 
threat actor. Rapid7’s inaugural vulnerability intelligence report included just 
over a dozen of these “widespread threats,” meaning vulnerabilities with many 
attackers and a large vulnerable target population. At the time, this elevated 
risk climate was novel, compelling, even alarming. 

But 2021 onward put prior years to shame, drawing a rather stark divide 
between “then” and “now.” Zero-day exploitation soared, reaching a new zenith 
before leveling off at what looks to be permanently high altitude; the median 
number of days between vulnerability disclosure and exploitation, which we 
began tracking several years ago, has stayed in single digits across the CVEs 
in our annual datasets; widespread exploitation of major vulnerabilities has 
shifted from a notable event to a baseline expectation; ransomware attacks 
regularly take entire public-facing systems offline, sometimes for weeks or 
months at a time; and state-sponsored adversaries have ramped up activity 
across sectors, using geopolitical conflict as both a rationale and a disguise 
for espionage, hacktivism, supply chain sabotage, and more.

A hearty and heartfelt disdain for hype is baked into Rapid7 research philosophy. 
When we talk about a changing threat climate, we require hard evidence — 
evidence collected and analyzed beyond the binary categorization of “exploited” 
and “not.” If we’re to say the world has changed, our research ideology demands 
we produce data to support that claim.

The world has changed. As in previous years, zero-day attacks and widespread 
exploitation remained common across the vulnerabilities we analyzed in 2023 
and the start of 2024. But we’ve also seen a pronounced shift in the way some 
widespread compromise events play out. 

Instead of following the familiar pattern of “many attackers, many targets,” 
nearly a quarter (23%) of widespread threat CVEs arose from well-planned, 
highly orchestrated zero-day attacks in which a single adversary compromised 
dozens or hundreds of organizations in one fell swoop, often leveraging custom 
tooling like proprietary exploits and backdoors. These aren’t our grandparents’ 
cyberthreats — this is a mature, well-organized cybercrime ecosystem at 
work, with increasingly sophisticated mechanisms to gain access, establish 
persistence, and evade detection. 

Anecdotally, these compounding changes in the threat climate have also incited 
some regressive practices among software producers. In our experience, 
it’s been increasingly common for vendors to silently patch security issues, 
withholding advisories and CVE descriptions until days or weeks later. Even 
then, more vendors appear to be deliberately obfuscating vulnerability details, 
declining to publish root cause and attack vector information based on an 
understandable but misguided belief that obscurity deters adversaries and 
mitigates reputational risk to software producers. 

Finally, we’ve also seen the broader security market start to veer even more 
heavily toward privatization of vulnerability and exploit information, with 
technical findings often shared in closed loops rather than openly — for profit 
or otherwise. The rumors of Twitter’s demise exacerbated this trend starting 
in late 2022, with many disillusioned security community members opting to 
migrate to an array of alternative platforms and closed intelligence-sharing 
circles. As of March 2024, industry concern over the future of the National 
Vulnerability Database (NVD) has sparked new discussions on whether a 
move toward private ownership of the database might be an improvement 
over public stewardship. 

These are nuanced challenges without simple solutions, and often without 
institutional or industry support for the human critical infrastructure that so 
much of our technological ecosystem depends upon — from exhausted security 
practitioners to beleaguered open-source maintainers and under-appreciated 
public-sector analysts. Privatization can be a powerful tool, but it’s not a panacea. 
When we consider it, we should also consider what we may be giving up. 

## Vulnerability Exploitation Trends
### A Note on Exploitation Terminology
Starting in 2023, all of the vulnerabilities we categorize as exploited in the wild 
in our data are confirmed to have been exploited successfully by adversaries in 
real-world production environments. This is a departure from previous years, 
where occasionally we would use third-party honeypot data as a primary source 
of in-the-wild exploitation of the CVEs in our vulnerability intelligence datasets. 

Certain attack-related terms have become more broadly adopted by the industry 
over the past 18 to 24 months. We’ve seen a higher number of claims signaling 
“mass exploitation” or “widespread exploitation” of new vulnerabilities, including 
in a number of cases where, upon further investigation, “mass exploitation” 
actually meant a public proof of concept being lazily thrown at the internet, 
without any exploitable code paths to execute it. This is a particular risk when 
assessing threat activity around library vulnerabilities or flaws in third-party 
components. Shared components are implemented in different ways and 
places in technology stacks, which more often than not makes them remotely 
inaccessible and difficult to target with one-size-fits-all exploits. 

We have frequently observed that honeypot data does not (or cannot) distinguish 
scanning or unsuccessful exploit attempts from genuine, successful compromise 
of target systems; this is an understandable technological limitation, but it can also 
mean clumsy exploit attempts that are unlikely to succeed in real environments 
may be incorrectly interpreted as “mass exploitation.” While scanning activity 
or exploit attempts (e.g., with publicly available proof-of-concept code) can be 
reasonable indicators of attacker interest, they are rarely indicative of attacker 
skill. As we know well, “vulnerable” and “exploitable” are not the same thing, 
particularly without sufficient ability to develop and execute successful attacks 
outside limited test cases. The sheer number of honeypots littering the internet 
also contributes to inflated prevalence and faulty attack intel.

While some of the vulnerabilities discussed in this report have also been 
exploited in honeypot deployments, going forward we are changing our practices 
to only include honeypot data as authoritative evidence of exploitation if we 
can confirm code execution, payload delivery, or other high-fidelity indicators 
of successful compromise. This applies to our own honeypot data as well as 
third-party feeds.

### 2023 New Widespread Threats
Rapid7 vulnerability researchers prioritize CVEs that are likely to impact many 
organizations, instead of those likely to affect only a few. We differentiate mass 
attacks from smaller-scale exploitation; when a vulnerability is exploited to 
compromise many organizations across many verticals and geolocations, we 
deem that vulnerability a widespread threat. Organizations should expect to 
conduct incident response investigations that look for indicators of compromise 
(IOCs) and post-exploitation activity during widespread threat events in addition 
to activating emergency patching protocols.

Rapid7 researchers tracked more than 30 new vulnerabilities that were widely 
exploited in 2023 and the start of 2024. More than half (53%) of the following 
CVEs arose from zero-day exploits. Rapid7 MDR has observed exploitation of 
many of the below vulnerabilities in customer environments. 

Broadly exploited vulnerabilities that drove compromises across many 
verticals and target organizations in 2023 include:
- CVE-2023-0669 Fortra GoAnywhere MFT Remote Code Execution
- CVE-2023-3519 Citrix NetScaler ADC/Gateway Remote Code Execution
- CVE-2023-2868 Barracuda Email Security Gateway Remote Command Injection
- CVE-2023-42793 JetBrains TeamCity CI/CD Server Authentication Bypass
- CVE-2023-24489 Citrix ShareFile Improper Access Control
- CVE-2023-29059 3CX Supply Chain Compromise
- CVE-2023-34362 Progress Software MOVEit Transfer SQL Injection
- CVE-2023-20269 Cisco ASA and FTD Unauthorized Access
- CVE-2023-46604 Apache ActiveMQ Remote Code Execution
- CVE-2023-40044 Progress Software WS_FTP Server Deserialization of Untrusted Data
- CVE-2023-20198 Cisco IOS XE Web UI Privilege Escalation
- CVE-2023-26360 Adobe ColdFusion Improper Access Control
- CVE-2022-47986 IBM Aspera Faspex Unauthenticated Remote Code Execution
- CVE-2023-20273 Cisco IOS XE Web UI Command Injection
- CVE-2023-22515 Atlassian Confluence Server and Data Center Broken Access Control
- CVE-2023-4966 Citrix NetScaler ADC/Gateway Buffer Overflow
- CVE-2023-46805 Ivanti Connect Secure and Policy Secure Authentication Bypass
- CVE-2023-22518 Atlassian Confluence Improper Authorization
- CVE-2023-28771 Zyxel Multiple Firewalls OS Command Injection
- CVE-2023-32315 Ignite Realtime Openfire Path Traversal
- CVE-2022-47966 Zoho ManageEngine Unauthenticated Remote Code Execution
- CVE-2023-27532 Veeam Backup & Replication Remote Code Execution
- CVE-2023-38831 RARLAB WinRAR Code Execution
- CVE-2022-36537 ZK Framework Information Disclosure (ConnectWise R1Soft Server Backup Manager Remote Code Execution)
- CVE-2023-27350 PaperCut NG Improper Access Control Vulnerability
- CVE-2023-24880 Microsoft SmartScreen Security Feature Bypass
- CVE-2022-44877 CentOS Web Panel Unauthenticated Remote Code Execution
- CVE-2023-3722 Avaya Aura Device Services OS Command Injection
- CVE-2023-22952 SugarCRM Remote Code Execution
- CVE-2022-46169 Cacti Command Injection

Two Citrix NetScaler ADC/Gateway vulnerabilities (CVE-2023-3519 and CVE-
2023-4966, disclosed in July and October respectively) drove incidents that 
spanned the back half of 2023 and extended into early 2024. CVE-2023-42793, 
a critical authentication bypass in JetBrains TeamCity CI/CD software, was 
disclosed in September 2023 and exploited by Russian and North Korean 
state-sponsored threat actors, prompting bulletins from global intelligence 
agencies months after a patch was released. It was the second major supply 
chain attack vector that broke news in 2023, after a desktop application from 
telecommunications company 3CX was found to have been backdoored (CVE-
2023-29059) as part of a suspected North Korean threat campaign.

Adobe ColdFusion CVE-2023-26360 was initially disclosed in March 2023 
as having been exploited in a limited, targeted fashion, but the vulnerability 
served as an initial access vector in multiple campaigns throughout the year, 
including a successful attack on U.S. government servers. A zero-day remote 
code execution vulnerability in SugarCRM (CVE-2023-22952) was used to 
deploy webshells and cryptominers in addition to providing initial access to 
AWS cloud environments). Attackers exploited CVE-2023-46604, a zero-day 
remote code execution flaw in Apache ActiveMQ, to drop at least two different 
kinds of ransomware, as well as webshells, cryptominers, and rootkits.

While widely exploited vulnerabilities have become commonplace over the last 
few years, the past 15 months have seen a significant shift in attacker behavior 
during widespread compromise events. Before 2023, the most common 
attack pattern we observed for opportunistically exploited vulnerabilities was 
“many attackers, many targets” — namely, an initial wave of low-skilled exploit 
attempts, frequently looking to deliver cryptominers or webshells, followed by 
more adept ransomware group and/or APT exploitation. 

Starting in 2023, however, we’ve seen an increase in mass compromise events 
where initial exploitation was orchestrated and executed by a single motivated 
threat actor using complex zero-day exploit chains and/or custom implants. 
A number of 2023’s large-scale attacks followed this pattern: 
- The Cl0p ransomware group used new zero-day exploits to target two 
popular file transfer solutions, MOVEit Transfer (CVE-2023-34362) and 
GoAnywhere MFT (CVE-2023-0669), in highly orchestrated smash-and-grab 
campaigns that resulted in data exfiltration and extortion for hundreds of 
organizations around the world, prompting breach notifications to tens of 
millions of consumers. Both attacks were exceedingly well-planned and 
executed; the MOVEit Transfer attack, which began over a holiday weekend 
in the U.S., may have been the culmination of nearly two years of threat 
actor reconnaissance and testing. 
- In a truly wild series of updates over the course of several weeks starting 
in May 2023, Barracuda Networks disclosed an incident where a single 
adversary used a zero-day command injection exploit (CVE-2023-2868) to 
compromise a large swath of Email Security Gateway (ESG) appliances with 
a custom backdoor so persistent that the vendor finally told customers to 
decommission physical devices entirely. In late December 2023, the company 
disclosed a second zero-day vulnerability (CVE-2023-7102) that had also 
been exploited by attackers.
- In October 2023, Cisco Talos shared information on a pair of Cisco IOS XE 
zero-day vulnerabilities (CVE-2023-20198, CVE-2023-20273) that had been 
exploited by an as-yet-unattributed threat actor to deploy a custom implant 
christened “BadCandy.” The implant had reportedly been deployed on tens 
of thousands of devices before the adversary modified it to evade industry 
detection — the implant is now on at least its third iteration. 
- Investigation into a “suspected APT” attack on Ivanti Connect Secure 
and Policy Secure gateways in January 2024 revealed a zero-day exploit 
chain (CVE-2023-46805, CVE-2024-21887) that adversaries had used to 
compromise vulnerable devices, after which they deployed webshells and 
backdoored legitimate files. Thousands of gateways remained vulnerable 
to follow-on CVE disclosures as of mid-February. U.S. government agencies 
published a joint advisory on February 29 emphasizing that threat actors 
were able to deceive Ivanti’s Integrity Checker Tool (ICT), resulting in a failure 
to detect compromise; the advisory notes that “The authoring organizations 
strongly urge all organizations to consider the significant risk of adversary 
access to, and persistence on, Ivanti Connect Secure and Ivanti Policy Secure 
gateways when determining whether to continue operating these devices 
in an enterprise environment.” 

We’ve seen plenty of low-skill, opportunistic attacks during 2023 and early 
2024 — so-called script kiddies haven’t magically disappeared. But overall, the 
skill and sophistication observed in incidents like those above have trended 
much higher than in years past. While all the vulnerabilities above pertained to 
either network edge devices or file transfer technologies, concern over shifting 
attacker behavioral patterns has also made its way into discussions about 
supply chain security and insider threats — and for good reason, as key 2023 
supply chain attack vectors and major incidents showed. 

### Ground Zero: Pre-Patch Exploitation
Between the end of 2020 and the end of 2021, large-scale incidents that 
resulted in the compromise of many organizations more than doubled; those 
statistics have never returned to pre-2021 levels. But even more concerning 
is that widespread zero-day threat events quintupled (and then some) in 2021 
and have become a mainstay since then. 

> In 2023, for the second time in three years, more 
mass compromise events arose from zero-day 
vulnerabilities than from n-day vulnerabilities.

![Widespread Threat CVEs 2020-2024. # of Widespread Threat CVEs (n=105). Exploited as n-day. Exploited as 0-day]

Since 2021, Rapid7 researchers have tracked the time between when vulnerabilities 
become known to the public and when they are (reliably) reported as exploited 
in the wild. This window, which we call “Time to Known Exploitation,” or TTKE, 
has narrowed considerably in the past three years, largely as a result of prevalent 
zero-day attacks. Zero-day flaws accounted for 43% of the known-exploited 
CVEs we’ve reported on since January 2021, with 55% of those vulnerabilities 
having been exploited within a week of public disclosure and 60% within two 
weeks. For comparison, zero-day flaws comprised under a quarter of our 2020 
Vulnerability Intelligence Report data, with 30% of vulnerabilities exploited 
within a week and 32% within two weeks. 

Average time to known exploitation tends to be a less useful metric when such 
a large proportion of TTKE values are zero. Nevertheless, the average time 
to known exploitation is just over 22 days for CVEs in our data whose TTKE 
values are known. One day is the median time to known exploitation for our 
cumulative annual datasets.

The following chart examines exploited and widely exploited vulnerabilities 
that Rapid7 has included in annual research datasets over the past four years, 
along with the percentage of these vulnerabilities that were exploited as zero-
day flaws. Since our vulnerability classification and selection methodologies 
have necessarily become stricter and more prescribed over time, the 2023 
data below is a relatively conservative analysis of today’s exploitation trends. 

![Time to Known Exploitation 2020-2024. # of Vulnerabilities (n=188). 1day: 83, 7 days: 21, 14 days: 8, 30 days: 14, Unknown: 25, 31 days: 37]

Our takeaway from this data is that organizations are under considerable 
pressure not only to patch new vulnerabilities quickly and continually reduce 
internet-facing attack surface area, but also to implement compensating 
controls and detection strategies that minimize an adversary’s ability to achieve 
objectives after that adversary has already gained access to a target network. 
Technologies like endpoint detection and response (EDR) are key components 
of a defense-in-depth strategy, but we believe that business leaders should 
be aware that combating and preventing modern cyberthreats continues to 
require human expertise in addition to technology. More than ever, burnout and 
brain drain on security teams compound risk from well-resourced, motivated 
adversary operations.

### Countdown to Exfil: File Transfer Hacks
Cl0p attacks on GoAnywhere MFT CVE-2023-0669 and MOVEit Transfer 
CVE-2023-34362 have dominated news headlines for the past year, in no 
small part because of the steady stream of breach notifications that went 
out to tens of millions of global consumers in 2023. But GoAnywhere MFT 
and MOVEit Transfer weren’t the only file transfer technologies exploited by 
financially motivated adversaries over the past year and a half. In fact, these 
incidents were enough of a pattern in 2023 that Rapid7 researchers created a 
new “smash-and-grab” attacker utility category for half a dozen file transfer 
CVEs (see Attacker Utilities later in this report). 

![Attack Scale and Speed Trends (Cumulative). # of Vulnerabilities (n=188). Exploited: 44%, Widely Exploited: 40%, 0-day (% of all exploited): 21%, 37%, 47%, 52%, 0-day (% of widely exploited): 43%, 53%, 53%]

CVE-2022-47986, a YAML deserialization issue in IBM’s Aspera Faspex data 
transfer solution, was exploited by both ransomware and Iranian state-
sponsored threat actors (Rapid7 researchers analyzed the vulnerability and 
had “more trouble preventing [the application] from crashing than actually 
exploiting it”). CVE-2023-40044, another deserialization issue in Progress 
Software’s WS_FTP secure file transfer product, came under attack via multiple 
exploit chains, including for attempted ransomware deployment. Interestingly, 
deserialization is overrepresented as a root cause across smash-and-grab 
exploits — a deserialization issue was also at the root of GoAnywhere MFT 
CVE-2023-0669, and while MOVEit Transfer CVE-2023-34362 itself is a SQL 
injection flaw, a .NET deserialization issue was a key part of the full remote 
code execution attack chain. 

Citrix ShareFile CVE-2023-24489, which very narrowly made our widespread 
threat list this year, saw a brief spike in honeypot exploitation activity in August 
2023 that tapered off faster than expected, possibly because the vendor allegedly 
disabled access on the vulnerable component until the patch had been applied. 
Still, by early 2024 the vulnerability had been cited in enough ransomware 
incident reports (public example here) to demonstrate that unpatched controllers 
remain tempting targets. The final bug we categorized as a smash-and-grab 
opportunity appears to be unexploited at time of writing — CVE-2023-43177, 
an unauthenticated remote code execution issue in CrushFTP for which a nifty 
exploit chain is publicly available. 

These technologies are a boon for financially motivated adversaries in ransomware 
and extortion campaigns because of the sensitive data they can store; moreover, 
many of the attacks Rapid7 has observed on file transfer products have been 
executed quickly, with attackers getting in, stealing data, and getting out 
within minutes or hours rather than days or weeks. While there can be room 
for interpretation on data breach notification regulations generally, an attack 
ending in data exfiltration from a file transfer application has a lot less wiggle 
room as far as regulatory reporting requirements go. 

Those reporting requirements were also part of the reason that security firms, 
media, and regulators were able to quantify victims from these types of attacks 
so granularly, especially when it came to collateral damage. Counting the 
number of consumer breach notifications that go out as a result of a major 
cybersecurity incident may not be the best way to quantify attack impact, but 
it’s highly effective for tracking so-called “blast radius.” 

### Silver Linings
File transfer vendors seem to have gotten understandably spooked by the 
MOVEit Transfer and GoAnywhere MFT hacks perpetrated by Cl0p (and the 
public relations nightmare that followed for many victims). But The Year of the 
File Transfer Hack™ wasn’t without its silver linings, sparse as they may have 
been. In Rapid7’s own experience disclosing vulnerabilities to file transfer 
vendors in 2023, they were exceptionally responsive, displaying a high sense 
of urgency throughout the disclosure process and in most cases shipping 
fixes for new vulnerabilities within weeks instead of months. In several cases, 
these companies patched reported vulnerabilities in less than half the time 
most firms take. 

More broadly, there’s been evidence that some file transfer technology vendors 
are using recent Cl0p attacks as an impetus for maturing vulnerability disclosure 
and product security practices — for example, by speeding up remediation SLAs, 
establishing formal disclosure mechanisms for external security researchers, 
and implementing more frequent and transparent patch release cycles. 

These are positive indicators that may help accelerate and streamline vendor 
vulnerability responses in the future, alongside strong proactive measures that 
seek to identify new vulnerabilities before adversaries do. 

### Other 2023 Exploited Vulnerabilities
The following vulnerabilities are known to have been exploited in the wild in 
either 2023 or 2024 but as of February 2024, did not have enough technical 
evidence of large-scale attacks to be included in our widespread threat list. 
- CVE-2023-46747 F5 BIG-IP Configuration Utility Authentication Bypass
- CVE-2023-36845 Juniper Junos OS EX and SRX PHP External Variable Modification
- CVE-2023-38035 Ivanti Sentry Admin Portal Authentication Bypass
- CVE-2023-29298 Adobe ColdFusion Access Control Bypass
- CVE-2023-7102 Barracuda Email Security Gateway Arbitrary Code Execution
- CVE-2023-49103 ownCloud Graph API Critical Information Disclosure
- CVE-2023-38203 Adobe ColdFusion Deserialization of Untrusted Data
- CVE-2022-21587 Oracle E-Business Suite Remote Code Execution
- CVE-2023-28432 MinIO Information Disclosure
- CVE-2023-33246 Apache RocketMQ Remote Command Execution
- CVE-2023-21839 Oracle WebLogic Server Remote Code Execution
- CVE-2023-37580 Synacor Zimbra Collaboration Suite Cross-Site Scripting
- CVE-2023-41265 Qlik Sense Enterprise HTTP Tunneling Vulnerability
- CVE-2023-20867 Broadcom VMware Tools Authentication Bypass
- CVE-2023-29357 Microsoft SharePoint Server Elevation of Privilege
- CVE-2023-47246 SysAid Path Traversal
- CVE-2023-20887 Broadcom VMware Aria Operations for Networks Command Injection
- CVE-2023-23397 Microsoft Outlook Elevation of Privilege
- CVE-2023-1671 Sophos Web Appliance Command Injection
- CVE-2023-34048 Broadcom VMware vCenter Server Out-of-Bounds Write
- CVE-2023-36884 Microsoft Windows Search Remote Code Execution
- CVE-2023-41179 Trend Micro Apex One Arbitrary Code Execution
- CVE-2023-35078 Ivanti Endpoint Manager Mobile Authentication Bypass
- CVE-2023-28252 Microsoft Windows Common Log File System Driver Elevation of Privilege
- CVE-2023-27997 Fortinet FortiOS Heap-Based Buffer Overflow
- CVE-2023-35081 Ivanti Endpoint Manager Mobile Path Traversal
- CVE-2022-41328 Fortinet FortiOS Path Traversal
- CVE-2023-35082 Ivanti Endpoint Manager Mobile and MobileIron Core Authentication Bypass

Network edge devices, application development and delivery technologies, and 
IT security management systems make up most of the exploited vulnerabilities 
above, but a few outliers merit a mention. Microsoft SharePoint CVE-2023-
29357 started out on our “impending threat” list but was exploited in the wild 
before this report was finalized. A pair of information disclosure vulnerabilities 
(MinIO CVE-2023-28432, ownCloud CVE-2023-49103) offered attackers access 
to cloud secrets, including credentials. An HTTP tunneling vulnerability (CVE-
2023-41265) in Qlik Sense, a data analytics platform, was exploited by the 
Cactus ransomware group in November 2023 for initial access to corporate 
environments. 

Vulnerabilities that are exploited in targeted zero-day attacks often have some 
of the more scintillating backstories, and this crop is no exception. Of the 28 
CVEs in the above list, 15 were exploited as zero-day vulnerabilities (54%). 
Some of the notable inclusions:
- CVE-2023-34048, a memory corruption issue in VMware vCenter Server that 
according to Mandiant was exploited by UNC3886, a Chinese espionage 
group, for more than a year before it was discovered; 
- CVE-2023-28252, a privilege escalation vulnerability in Microsoft’s CLFS 
drivers that was discovered during a Nokoyawa ransomware campaign;
- CVE-2023-36884, a Windows vulnerability that Microsoft indicated was 
used in both targeted espionage and opportunistic phishing campaigns 
with Ukraine-related lures; 
- CVE-2023-23397, a critical elevation of privilege (NTLM hash leak) bug in 
Microsoft Outlook that Microsoft said was exploited by a Russia-based APT 
for nearly a year in attacks on government entities, critical infrastructure 
providers, and military suppliers;
- CVE-2023-47246, a path traversal vulnerability in SysAid servers whose 
zero-day exploitation Microsoft attributed to LaceTempest — the threat 
actor known for distributing Cl0p ransomware. 

CVE-2023-37580 was a reflected cross-site scripting (XSS) bug disclosed 
in Zimbra Collaboration, a popular attack target, in June 2023. According to 
Google’s Threat Analysis Group (TAG), the vulnerability was used in at least 