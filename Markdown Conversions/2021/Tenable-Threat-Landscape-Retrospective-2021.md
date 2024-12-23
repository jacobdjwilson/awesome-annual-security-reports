# TENABLE’S 2021 THREAT LANDSCAPE RETROSPECTIVE
A guide for security professionals to navigate the modern attack surface

## Table of Contents
- [FOREWORD](#foreword)
- [EXECUTIVE SUMMARY](#executive-summary)
- [KEY TAKEAWAYS](#key-takeaways)
- [METHODOLOGY](#methodology)
- [INTRODUCTION](#introduction)
- [SECTION 1: VULNERABILITY LANDSCAPE](#section-1-vulnerability-landscape)
  - [Microsoft Exchange Vulnerabilities](#microsoft-exchange-vulnerabilities)
  - [Print Spooler](#print-spooler)
  - [Zero-Day Vulnerabilities](#zero-day-vulnerabilities)
  - [Still VPNs](#still-vpns)
  - [Other Vulnerabilities of Interest in 2021](#other-vulnerabilities-of-interest-in-2021)
- [SECTION 2: THREAT LANDSCAPE](#section-2-threat-landscape)
  - [Supply Chain](#supply-chain)
  - [Ransomware](#ransomware)
  - [Breaches](#breaches)
- [CONCLUSION](#conclusion)
- [SECTION 3: A CLOSER LOOK AT THE KEY VULNERABILITIES IN 2021](#section-3-a-closer-look-at-the-key-vulnerabilities-in-2021)

## FOREWORD
Let’s break some patterns
Turbulent. Can you think of a better word to describe 2021? I can’t.
As we were putting the finishing touches on the 2021 Threat Landscape Retrospective, the cybersecurity industry was 
rocked by the revelation of a critical vulnerability in Apache Log4j 2, a widely used Java logging library. The vulnerability, 
dubbed Log4Shell, emerged as cybersecurity professionals continued to grapple with fallout from the  COVID-19 pandemic. 
Now in its second full year, the pandemic has triggered unprecedented changes in how we all live and work. We saw 
organizations around the world embracing remote work models, transforming how we define “the perimeter.” We watched as 
the pace of digital transformation accelerated, driving the mass migration of mission-critical applications to the cloud. And 
we observed as attackers continued to make effective use of the age-old tactic of daisy chaining vulnerabilities to facilitate 
ransomware attacks and breaches like SolarWinds and Kaseya, all of which served to remind us how risky the software 
supply chain has truly become. 
Yet, even in the midst of all this turbulence, we are frustrated by all the many things that haven’t changed enough in 2021. 
We’ve seen far too many organizations still trying to apply traditional cybersecurity tactics to modern deployments of cloud 
infrastructure. We’ve seen far too many legacy vulnerabilities still being left unpatched, even when they’re known to have 
been actively utilized by attackers to gain entry to an organization’s environment. And — as Log4Shell makes clear — we’ve 
seen organizations overlooking obvious points of security failure throughout their software supply chain, from the initial 
creation of code to how updates are deployed to users. 
This retrospective is intended to help security professionals make sense of the morass of threats and vulnerabilities that 
made 2021 an especially risky year. It’s intended as a clear reminder that practicing cybersecurity fundamentals — including 
finding and fixing critical vulnerabilities and addressing misconfigurations in the cloud and Active Directory — is more 
important than ever. We want to bring to light the sheer scope of the challenge security organizations face, in hopes that it 
will spark discussion that will lead to true, lasting change in how cybersecurity is managed. 
We believe a new approach to cybersecurity is warranted. The way forward requires not only  remediating vulnerabilities in 
the products your organization deploys but also finding the means to continuously evaluate the trust relationships within 
your environment to develop a clearer understanding of how they might be exploited. Now that cloud adoption has rapidly 
increased and organizations are embracing the flexibility that cloud-native infrastructure provides, it is vital to find and fix 
every flaw before deployment. The reliance on code libraries has led to software flaws being replicated ad infinitum. By the 
time software reaches run-time, it’s already too late. It’s long past time for detection to move from reactive to proactive, 
so that security teams don’t have to wait for infrastructure to be created in order for them to discover and mitigate 
vulnerabilities in code. It’s time for GitOps to be seen as the de facto universal for a wide variety of operations to manage 
entire workflows. Merging GitOps and Infrastructure as Code approaches will allow organizations to take a security-first 
approach to codifying how their servers should operate, as well as offering security teams visibility into the entire line
of operations. 
With the traditional perimeter atomized by remote work, it’s essential for all organizations to begin addressing cybersecurity 
at the source by “shifting left” and embracing a culture of DevSecOps. It’s time to embrace new approaches to cybersecurity 
that break the patterns of the past and empower security professionals to play a role in reducing risk at all stages of 
software development.
Renaud Deraison 
Co-founder and Chief Technology Officer
Tenable

## EXECUTIVE SUMMARY
The past year certainly had more than its fair share of headline-grabbing attacks and vulnerabilities. Tenable’s 
Security Response Team (SRT) saw several cyberattacks cross the chasm from the digital world to the physical, 
rattling the public’s faith in fuel and food supply chains, among other unpleasant outcomes. And, as we were 
finalizing this year’s Threat Landscape Retrospective in December 2021, security practitioners were having their 
holiday season disrupted by the Log4Shell vulnerability in Apache Log4j 2, a widely used Java logging library. As 
Tenable’s CTO Renaud Deraison states, this vulnerability reveals troubling fissures in the very practices that are 
the bellwether of sound security.
Yet, the majority of events analyzed by the Security Response Team for this report are far more ordinary, and many 
are readily mitigated by patching legacy vulnerabilities and addressing misconfigurations that limit attack paths.
Indeed, even as we see the vulnerability and threat landscape constantly evolving from year to year, we recognize 
a certain familiarity in the struggles organizations face as they tackle age-old security challenges in new 
infrastructure. Organizations continue to struggle with protecting, or even defining, the perimeter. Migration to 
cloud platforms, reliance on managed service providers, software and infrastructure as a service have all changed 
how organizations must think about and secure the perimeter. Fragmented security solutions and poorly defined 
security outcomes must be left behind to match the complexity of the modern attack surface.
Defining risk is more important than ever. Beyond counting up the individual vulnerabilities or misconfigurations 
on their systems, modern security leaders and practitioners must think more holistically about the attack paths 
that exist within their networks and how they can efficiently disrupt them. We must examine threat actor behavior 
to understand which attack paths are the most fruitful and leverage these insights to define an effective security 
strategy. And we must consider the peculiarities of dealing with cloud vulnerabilities, which present unique 
challenges for organizations seeking to understand their own risk and security posture.
The goal of this report is to help defenders understand the full scope of today’s modern attack surface so they can 
continue to refine their cybersecurity strategies and reduce risk. In this report, we explore:
- The most notable vulnerabilities of the year and how they were used in attack chains, with specific focus on 
the value of Active Directory to threat actors.
- Risks presented by increased connectivity across information and operational technology.
- The unique challenges of understanding security postures in cloud environments.
- How trust relationships can be exploited by attackers to gain access to sensitive environments.
- How ransomware groups continue to evolve, from double extortion to attacks against critical infrastructure 
and the supply chain.
- Breach factors and the challenges in analyzing breach data, given the limited information available.
- Details of the key vulnerabilities affecting enterprise software.  
![Image of "TOP 5 VULNERABILITIES IN 2021" with PROXYLOGON, PRINTNIGHTMARE, VMWARE VSPHERE, PULSE CONNECT SECURE, and ZEROLOGON listed]
Key Stats
21,957
New CVEs
Assigned in 2021
1,825
Total Breach
Entries*
40B+
Total Records 
Exposed*
105
Total number 
of zero-day 
vulnerabilities
* November 2020 - 
October 2021

## KEY TAKEAWAYS
Evolution of the perimeter:
Adoption of cloud solutions, software and infrastructure as a service, and the increasingly complex service 
provider ecosystem all continue to challenge traditional conceptions of the perimeter. However, traditional 
perimeter devices like VPNs remain valuable targets for attackers.
Patching problems:
Staying on top of patching assets is difficult enough, but in 2021 it was even more challenging due to incomplete 
patches, miscommunications from vendors and patch bypasses, making it even harder for defenders to stay on top 
of securing critical systems.
Majority of zero-days exploited in the wild
83% of zero-day vulnerabilities disclosed in 2021 were exploited in attacks with web browser zero-days 
accounting for over 30% of them.
Ongoing risks of interconnection:
Code and library re-use have resulted in vulnerabilities persisting for years across potentially millions of sensitive 
operational technology (OT) devices. Software libraries and network stacks used commonly amongst OT devices 
often introduce additional risk when security controls and code audits are not in place.
Misconfigurations increase risk:
Cloud and Active Directory (AD) misconfigurations are low hanging fruit for threat actors. Openly accessible
cloud databases and overly permissive AD configurations give attackers access to an organization’s most 
sensitive information.
Attackers target AD environments:
Threat groups, particularly ransomware, have increasingly exploited vulnerabilities and misconfigurations in
Active Directory.
Surging ransomware attacks:
Ransomware attacks increased in both volume and sophistication. Ransomware groups leveraged zero-days and 
legacy vulnerabilities alike to target sensitive sectors like healthcare, education and the physical supply chain.
Physical and software supply chains under attack:
Supply chains of all kinds were targeted by diverse threat groups in 2021. Ransomware groups favored physical 
supply chain disruption as a tactic to extort payment while cyberespionage campaigns exploited the software 
supply chain to access sensitive data. And 61% of security leaders reported that their organization was exposed to 
increased risk related to its expanding supply chain.
Data breaches continue to increase:
Over 2.5 times as many breaches were reported in 2021 than in 2020. Additionally, there was a 78% increase in the 
number of records exposed.

## METHODOLOGY
This report was compiled based on events we’ve analyzed throughout 2021. 
We tracked government, vendor and researcher advisories to understand the 
vulnerability and threat landscapes. Our breach data was compiled by collecting 
publicly available information from national and local news outlets reporting 
on data breaches from November 2020 through October 2021. The common 
vulnerability scoring system (CVSS) scores found throughout the report are 
derived from the National Institute of Standards and Technology’s (NIST) National 
Vulnerability Database (NVD). In cases where no NVD score is available, scoring is 
based on the vendor advisory or vulnerability disclosure.
How to use this report
- Disrupt attack paths by identifying and remediating the vulnerabilities and 
misconfigurations referenced in this report.
- Keep attackers at bay by learning how threat actors are breaching 
organizations and the tactics they’re employing to hold organizations for 
ransom.
- Protect data by examining some of the common ways data breaches occur 
and what your organization can do to prevent them from happening.
- Redefine the perimeter by examining how cloud and OT assets are secured 
and integrated within your organization.
- Broaden your security controls and address AD misconfigurations that 
attackers continue to target.

## INTRODUCTION
Throughout the year, Tenable’s Security Response Team tracks and reports on vulnerabilities and security 
incidents, providing guidance to security professionals as they plan their response strategies. We 
compile those year-long observations and analyze them holistically to better understand the evolution of 
the threat landscape. These findings provide insight into how organizations should prepare to face the 
oncoming challenges in 2022. Understanding threat actor behavior can help organizations effectively 
prioritize security efforts to disrupt attack paths and protect critical systems and assets.
In Section 1, we explore the 2021 vulnerability landscape and the trends that defined it, including:
- Flaws in ubiquitous products like Microsoft Exchange and Windows Print Spooler
- Analysis of the zero-days disclosed and exploited
- The impact of legacy vulnerabilities, particularly those in Secure Socket Layer Virtual Private 
Networks (SSL VPNs)
- Vulnerabilities and common misconfigurations affecting OT and cloud infrastructure
In Section 2, we explore attacker behavior in the 2021 threat landscape, including:
- Attacks against the software supply chain
- The surge in ransomware attacks against nearly all sectors
- Analysis of the year’s data breaches
In Section 3, we provide a detailed list of key vulnerabilities affecting a wide range of vendors, including:

## SECTION 1: VULNERABILITY LANDSCAPE
Each year, members of the security community disclose tens of thousands of vulnerabilities in a variety of products used for 
business. From 2016 to 2021, the number of reported CVEs increased at an average annual growth rate of 28.3%. The 21,957 CVEs 
reported in 2021 represent a 19.6% increase over the 18,358 reported in 2020 and a 241% increase over the 6,447 disclosed in 2016. 
The following section explores some key trends in the 2021 vulnerability landscape.

### Microsoft Exchange Vulnerabilities
From the beginning of 2021, threat actors targeted vulnerable Microsoft Exchange instances around the world. These threat 
actors leveraged a host of vulnerabilities in on-premises Exchange disclosed throughout the year. While the specific features of 
the vulnerabilities differ (full details can be found in Section 3), they are uniquely attractive to attackers because of the ubiquity of 
Microsoft Exchange in high-value environments.

In March, Microsoft disclosed a state-sponsored cyberespionage campaign exploiting four zero-day vulnerabilities in Microsoft 
Exchange Server that had begun in January. ESET research later reported that other cyberespionage groups were exploiting 
this attack chain, specifically calling out CVE-2021-26855, named ProxyLogon. It was eventually revealed that over 60,000 
organizations were compromised in these attacks. Over time, ProxyLogon was adopted by non-state-sponsored attackers to 
distribute cryptominers and ransomware.
According to a joint alert from the Cybersecurity and Infrastructure Security Agency (CISA), Australian Cyber Security Centre 
(ACSC), United Kingdom’s National Cyber Security Centre (NCSC) and Federal Bureau of Investigation (FBI) issued in July, 
ProxyLogon and its companions were some of the top exploited vulnerabilities by threat groups in the first half of 2021. Attacks 
against vulnerable servers were so rampant that, in April, the FBI conducted an operation to remotely remove malicious web 
shells from affected servers.
| CVE             | Vulnerability Type          | CVSSv3 |
|-----------------|---------------------------|--------|
| ProxyLogon CVE-2021-26855 | Server-Side Request Forgery | 9.8    |
| CVE-2021-26857  | Insecure Deserialization   | 7.8    |
| CVE-2021-26858  | Arbitrary File Write       | 7.8    |
| CVE-2021-27065  | Arbitrary File Write       | 7.8    |
| ProxyShell CVE-2021-34473 CVE-2021-34523 CVE-2021-31207 | Remote Code Execution Elevation of Privilege Security Feature Bypass | 9.8 9.8 7.2 |
| CVE-2021-42321  | Remote Code Execution      | 8.8    |

In August, the ProxyShell attack chain was disclosed at the Black Hat USA 
and DEF CON security conferences. Like ProxyLogon, ProxyShell was quickly 
adopted into attack chains by advanced persistent threat (APT) and nation-
state groups. According to reports, the LockFile, Conti, BlackByte and Babuk 
ransomware groups have all adopted this attack chain, as have cryptomining 
botnets and malicious spam campaigns. Having already been the subject of 
government warnings, we expect the ProxyShell attack chain will remain among 
the top exploited vulnerabilities from 2021.
To wrap out the year, Microsoft patched CVE-2021-42321, a post-authentication 
remote code execution (RCE) in Exchange that was exploited at the Tianfu Cup, 
a Chinese cybersecurity contest. The Microsoft Threat Intelligence Center also 
reported limited targeted attacks exploiting this flaw and it was quickly added to 
CISA’s Catalog of Known Exploited Vulnerabilities.
A key reason these vulnerabilities have been utilized heavily by attackers is 
the widespread use and accessibility of Exchange Servers at organizations 
around the world and due to their ability to be chained with other vulnerabilities. 
ProxyLogon and ProxyShell have been chained with several of the vulnerabilities 
we cover in following sections. For instance, the Black Kingdom ransomware 
has chained ProxyLogon with a vulnerability in Pulse Connect Secure that 
was among our Top 5 Vulnerabilities of 2020 (CVE-2019-11510) and the LockFile 
ransomware has chained ProxyShell with either PetitPotam, a new technology 
LAN manager (NTLM) relay attack, or Zerologon (CVE-2020-1472) to target AD. 
AD is a top target, particularly for ransomware. Threat actors seek out attack 
chains that allow them to pivot from remote attacks into AD takeover.

### Print Spooler
The summer of 2020 saw a flurry of activity so great, we dubbed it “Vulnerability 
Season.” If we continue that naming convention, the summer of 2021 was “Print 
Spooler Season.” From June through October, nearly a dozen vulnerabilities 
were disclosed in Windows Print Spooler, the Microsoft service that supports all 
printing functions, including ‘print to PDF’, in Windows environments. 
Attacks targeting Print Spooler are not new though. Over a decade ago, Print 
Spooler was exploited in the Stuxnet attacks. Much like Microsoft Exchange 
Server, the ubiquity of the service makes it valuable for attacks but even more 
so because it is enabled by default in the vast majority of environments, most 
notably on domain controllers.
Nearly a dozen vulnerabilities were disclosed and patched in Print Spooler 
during the summer creating confusion and stress among defenders. This was 
especially disruptive given the continued necessity of printer functionality in 
many corporate environments. The confusion began at the end of June when 
two different research teams published information about CVE-2021-1675. 
As it turned out, the second proof-of-concept (PoC) release, the one named 
“PrintNightmare,” was a distinct vulnerability which received CVE-2021-34527 
and an out-of-band patch. Over the following months, Microsoft released many 
more updates for Print Spooler and even changed the default behavior of the 
Point and Print function, which was key to many of the exploits released.

What is PrintNightmare?
While originally the name given to the PoC developed for CVE-2021-34527, 
PrintNightmare became a catch-all term for vulnerabilities in Print Spooler 
disclosed in the relevant timeframe by a certain set of researchers.
As with the Exchange vulnerabilities, these Print Spooler flaws have been widely 
adopted by threat actors. Ransomware groups in particular were attracted to 
these vulnerabilities due to the high probability that a wide scope of targets 
would have the service enabled. Magniber and Vice Society ransomware have 
both leveraged CVE-2021-34527 in their attack chains.
![Image of "Timeline of Print Spooler Disclosures"]

### Zero-Day Vulnerabilities
Our analysis of publicly available vendor advisories, news articles and disclosures 
about zero-day vulnerabilities throughout the year reveals that 105 zero-day 
vulnerabilities were disclosed in 2021 across a variety of popular software applications. 
As we saw last year, browser-related vulnerabilities led the pack, capturing 30.5% of 
the market share for zero-days in 2021, a 5.2% decrease from 2020. Operating systems 
accounted for 25.7% of zero-day vulnerabilities identified in 2021, a 2.9% decrease 
from 2020. In the chart below, we have broken down the zero-day vulnerabilities by 
product type and the number of vulnerabilities identified.
![Image of "2021 Zero-Day Vulnerabilities by Software/Hardware Type"]

This year, 27.6% of all zero-day vulnerabilities were found in Microsoft products, 
followed by Apple with 21% and Google products at 18.1%.
![Image of "2021 Zero-Day Vulnerabilities by Vendors"]
 A ZERO-DAY 
VULNERABILITY 
IS A FLAW IN 
SOFTWARE OR 
HARDWARE THAT 
IS UNKNOWN TO 
A VENDOR PRIOR 
TO ITS PUBLIC 
DISCLOSURE, 
OR HAS BEEN 
PUBLICLY 
DISCLOSED
PRIOR TO A
PATCH BEING
MADE AVAILABLE.

As expected, the bulk of zero-day vulnerabilities originated in products with a large user 
base. Apple iOS accounted for 12.8% of all zero-day vulnerabilities identified this year, 
followed by Google Chrome at 12.1%. Microsoft Windows-based vulnerabilities accounted 
for 10.6% of all those identified.
![Image of "2021 Zero-Day Vulnerabilities by Products"]
![Image of "2021 Zero-Day Vulnerabilities by In-the-Wild Exploitation"]
Our analysis shows that 83% of the zero-day vulnerabilities we’ve tracked in 2021 have 
been exploited in the wild.

Many of the details surrounding zero-day vulnerabilities are often kept under wraps as 
vendors focus on providing patches and ensuring users have had ample time to apply
said patches.
ZERO-DAY 
VULNERABILITIES 
TYPICALLY 
BECOME MORE 
PROBLEMATIC 
FOR MOST 
ORGANIZATIONS 
AFTER THEY’VE 
MADE THE 
TRANSITION TO 
LEGACY STATUS.

Zero-day vulnerabilities are primarily leveraged in limited, targeted attacks 
against a specific set of victims, so the risk to most organizations is minimal at 
best. That said, the true value of a zero-day vulnerability is often not defined 
by its exploitation prior to discovery, but by the blog posts and proof-of-
concept code published in the weeks and months after disclosure . Zero-day 
vulnerabilities typically become more problematic for most organizations after 
they’ve made the transition to legacy status, particularly if an organization has 
not yet applied available patches before widespread exploitation begins.
One zero-day that simultaneously counters and supports what we know about 
zero-day vulnerabilities is CVE-2021-44228, Log4Shell. It is ubiquitous enough 
to have immediately been a concern for huge swaths of the internet-connected 
world and will assuredly have a long tail as vendors and organizations alike try 
to determine where they have either implemented the vulnerable framework 
or deployed a product that does, and remediate all instances. Attackers were 
exploiting Log4Shell as early as December 1, more than a week before it became 
a publicly known zero-day. After public disclosure, attackers were off to the 
races. Botnets and ransomware led the charge in adopting the exploit, as they so 
often do, and nation-states soon joined the fray.

### Still VPNs
In the 2020 Threat Landscape Retrospective, we highlighted the risks posed by 
legacy vulnerabilities. One class of legacy vulnerabilities in particular, secure 
socket layer SSL VPN flaws, made up three of our top five vulnerabilities from 
2020: 
- CVE-2018-13379:
Fortinet FortiOS SSL VPN Web Portal Information Disclosure
- CVE-2019-11510:
Pulse Connect Secure Arbitrary File Disclosure
- CVE-2019-19781:
Citrix Application Delivery Controller (ADC) and Gateway Directory Traversal
Even though these three flaws were patched between 2019 and early 2020, they 
were some of the most exploited vulnerabilities throughout 2020. They were 
featured in several government alerts from U.S. agencies like CISA, the NSA and 
the FBI, highlighting their use by APT and ransomware groups.
Our concern was that, as with most legacy vulnerabilities, these flaws would be 
forgotten and left unpatched amidst the plethora of vulnerabilities disclosed 
and exploited in 2021. In fact, we published a blog post in August 2021 stressing 
the importance for organizations to patch their SSL VPNs, as we continued to 
see these flaws being exploited by attackers in the wild. In 2022, we expect VPN 
vulnerabilities to continue wreaking considerable havoc against organizations.
Outside of these three vulnerabilities, attackers utilized other legacy flaws, as 
well as new vulnerabilities in SSL VPNs, throughout 2021.
UNPATCHED SSL 
VPNS ARE AN IDEAL 
ENTRY POINT FOR 
ATTACKERS TO 
GAIN A FOOTHOLD 
IN A NETWORK 
TO PERFORM 
CYBERESPIONAGE, 
EXFILTRATE 
SENSITIVE AND 
PROPRIETARY 
INFORMATION AS 
WELL AS ENCRYPT 
NETWORKS AND 
HOLD THEM
FOR RANSOM.

In January, SonicWall was targeted by “highly sophisticated threat actors” that 
breached its internal systems. In late January, NCC Group identified a candidate 
for the breach and in February, SonicWall published an advisory for CVE-2021-
20016, a zero-day vulnerability in its Secure Mobile Access SSL VPN.
In April, Ivanti, which acquired Pulse Secure in 2020, published an out-of-cycle 
security advisory for CVE-2021-22893, an authentication bypass zero-day 
vulnerability in Pulse Connect Secure that was being exploited by attackers in 
the wild to target government agencies. In addition to this newly disclosed flaw, 
Ivanti also placed emphasis on other legacy vulnerabilities being leveraged in 
the bulk of attacker-related activity, including: CVE-2019-11510, CVE-2020-8243, 
a code injection vulnerability and CVE-2020-8260, an unrestricted file upload 
vulnerability.
In July, CVE-2019-19781, a critical vulnerability in the Citrix ADC and Gateway was 
identified as the No. 1 most-exploited vulnerability in 2020 in a joint advisory 
issued by CISA, the ACSC, the United Kingdom’s NCSC and FBI. In January 2021, 
this vulnerability was used by attackers to breach the U.S. Census Bureau 
systems in January.
Unpatched SSL VPNs are an ideal entry point for attackers to gain a foothold 
in a network to perform cyberespionage, exfiltrate sensitive and proprietary 
information as well as encrypt networks and hold them for ransom. As part of 
a post-mortem into a ransomware attack, Capcom confirmed that attackers 
managed to gain access to its network by targeting an old VPN backup device. 
Even if the attackers don’t leverage this access, they can sell it to the highest 
bidder, as we saw when attackers exploited a Fortinet FortiOS SSL VPN 
vulnerability and leaked 500,000 credentials.
The NSA and CISA published an information sheet in September on how to select 
and harden VPNs through a variety of measures, including the timely application 
of patches that address critical vulnerabilities like the ones referenced above.
As we grapple with the paradigm shift in the workforce, whether it is a hybrid 
or fully remote strategy, VPNs will continue to remain a popular target for 
cybercriminals. Therefore, it is paramount for organizations to protect their 
perimeters by identifying these assets and ensuring they receive regular 
security updates.

### Other Vulnerabilities of Interest
in 2021
Named vulnerabilities and attack chains 
dominated the news cycle while having varied 
real-world effects on organizations. As is 
always the case, many unnamed vulnerabilities 
proved much more effective than their named 
counterparts. Perimeter devices like SSL 
VPNs, Microsoft and Apple products, cloud 
solutions and operational technologies were 
all among notable targets for these attacks.

Governments name the
most-exploited flaws
The joint cybersecurity advisory from CISA, 
the FBI, ACSC and NCSC that listed the most 
exploited vulnerabilities in 2020 and the first 
half of 2021 stated that threat actors have 
been prioritizing “perimeter-type devices” in 
their attacks. Microsoft Exchange, Accellion, 
Pulse Secure and Fortinet SSL VPNs were the 
most exploited for the first half of the year and 
are covered in other sections of this report. 
The Accellion incident at the beginning of 
the year, wherein threat actors leveraged a 
vulnerability in the File Transfer Appliance, had 
a far-reaching impact. Dozens of organizations 
have disclosed data breaches linked to the 
four zero-days patched by Accellion.
Another top exploited vulnerability in 2021 
was CVE-2021-21985, a RCE in VMware 
vCenter Server. Patched at the end of May, 
mass scanning, likely by threat actors, for 
CVE-2021-21985 was reported on June 3, the 
same day a working PoC was published. In 
September, VMware patched CVE-2021-22005, 
an arbitrary file upload vulnerability that was 
quickly adopted by threat actors. In October, 
CISA included it in the “Catalog of Known 
Exploited Vulnerabilities” released alongside 
Binding Operational Directive (BOD) 22-01. 
The BOD lists vulnerabilities that represent 
“significant risk to the federal enterprise.” It 
also calls for aggressive remediation of all the 
vulnerabilities listed in the catalog.

#### Operational Technology
In the wake of major attacks on critical infrastructure in 2021, concerns surrounding the security of OT environments have never 
been higher. In May, the White House released Executive Order (EO) 14028, “Improving the Nation’s Cybersecurity.” The executive 
order outlines policies and steps to ensure the federal government and private sector work hand-in-hand to prioritize and 
modernize cybersecurity strategy. Recognizing the importance of OT, the executive order mentions the importance of protecting 
these systems used in critical industries.
While doomsday scenarios and predictions are made each year, 2021 proved that information technology (IT) and OT
environments are in attackers’ crosshairs. In the early hours of the Colonial Pipeline incident, fears were high around the impact 
the ransomware attack may have had on Colonial’s OT environment. While we later learned none of the OT environment was 
impacted, the incident highlighted the importance of securing organizations that are critical to the supply chain. As the prevalence 
of connected devices grows, researchers continue to examine OT security and risks by focusing on the underlying protocol stacks 
utilized by these devices. 
Over the past few years, there have been a number of research efforts to highlight the flaws within OT/internet of things (IoT) 
devices, including URGENT/11, Ripple20 and AMNESIA:33. 
Since January, researchers have publicly disclosed over 80 vulnerabilities across several libraries and software development kits 
(SDKs) found in billions of devices across the globe.
| Date      | Vulnerability | Campaign    | Number of Vulnerabilities Identified |
|-----------|---------------|-------------|------------------------------------|
| February 10 | NUMBER:JACK   |             | 9                                  |
| April 13    | NUMBER:WRECK  |             | 9                                  |
| April 29    | BadAlloc      |             | 27                                 |
| August 2   | PwnedPiper    |             | 9                                  |
| August 4   | INFRA:HALT    |             | 14                                 |
| November 9  | NUCLEUS:13    |             | 13                                 |

As part of Project Memoria, Forescout Research Labs began researching 
Transmission Control Protocol/Internet Protocol (TCP/IP) stacks used by 
various devices. As the backbone of interconnected network devices, TCP/
IP is a foundational set of communications protocols and an ideal target for 
exploration. As part of its research, Forescout released four pieces of research 
this year. Starting with NUMBER:JACK, the research focuses on TCP/IP stack 
security and explores nine vulnerabilities affecting multiple TCP/IP stacks. 
Less than two months later, Forescout released NAME:WRECK, a new set of 
nine vulnerabilities found across four TCP/IP stacks. The focus of this research 
was Domain Name System (DNS) vulnerabilities. INFRA:HALT, a joint research 
effort from Forescout and JFrog Security Research focused on the NicheStack 
TCP/IP stack and contained 14 new vulnerabilities. NicheStack is used in OT 
and industrial control systems (ICS) devices found in critical infrastructure and 
used by some of the biggest OT device manufacturers. In November, Forescout 
released NUCLEUS:13, a set of 13 vulnerabilities in the Nucleus TCP/IP stack. 
Nucleus NET is the TCP/IP stack of the Siemens-owned Nucleus real-time 
operating systems (RTOS), which is reportedly used in a staggering 3 
billion devices. 
In April, Microsoft’s Section 52, the Azure Defender for IoT security research 
group, announced a set of 27 critical memory allocation vulnerabilities dubbed 
BadAlloc. These vulnerabilities were found in a range of RTOS, SDKs and C 
standard library (libc) implementations used in a wide variety of devices. 
Armis researchers disclosed PwnedPiper in August, a set of nine critical 
vulnerabilities in the Translogic pneumatic tube system (PTS) used to transfer 
materials in thousands of hospitals. These nine vulnerabilities can be exploited 
to take control of the PTS system to physically manipulate sensitive materials, 
like blood samples, as well as taking control of the paths to redirect a carrier to 
another path. In a real-world scenario, one could imagine the disastrous effects 
an attack like this would have for patients in need of urgent care.
As we reflect on the assortment of vulnerabilities found within the libraries, 
SDKs and RTOSes within billions of devices across the world, we are reminded 
of the complexities in securing these devices. A common theme from many of 
these disclosures is the use of insecure protocols such as file transfer protocol 
and telnet. While these protocols have served a purpose in years past, they 
present unnecessary risk to organizations that may not even be aware the 
services are running. With the widespread use and re-use of software libraries 
and RTOS across numerous devices and manufacturers, patch management and 
asset enumeration remain difficult problems for most organizations. In some 
cases, mitigations and network segmentation may be the only viable options for 
devices that may no longer be manufactured or supported by vendors. 
We are now seeing the OT landscape struggle with some of the security 
concerns that plagued desktops in