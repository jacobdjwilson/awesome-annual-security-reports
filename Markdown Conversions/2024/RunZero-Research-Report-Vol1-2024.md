# runZero Research Report 2024 Volume 1

## Table of Contents
- [Chapter 1 Introduction](#chapter-1-introduction)
- [Chapter 2 OT & Cloud Impacts on Attack Surfaces](#chapter-2-ot--cloud-impacts-on-attack-surfaces)
- [Chapter 3 Unusual Assets Are Risky Assets](#chapter-3-unusual-assets-are-risky-assets)
- [Chapter 4 Some Old Enemies](#chapter-4-some-old-enemies)
- [Chapter 5 Emerging Threats](#chapter-5-emerging-threats)
- [Chapter 6 Fingerprints & Snapshots](#chapter-6-fingerprints--snapshots)
- [Chapter 7 AI & the Need for Specificity](#chapter-7-ai--the-need-for-specificity)
- [About runZero](#about-runzero)

// Research Team
HD Moore    //    Rob King    //    Tom Sellers
2024
VOLUME 1      •     MAY 2024

In this report we share runZero’s observations from our unique perspective as an applied security research team. Our goal is to provide insight into how the security landscape is changing, and recommendations on what you can do to get ahead of these changes. 

Foreword by Rob King
>“Plus ça change, plus c’est la même chose” [The more things change, the   more they stay the same.] 
>—Jean-Baptiste Alphonse Karr, Les Guêpes, 1849.

The only constant in information security is that this year will be different from last year. Not only will new individual threats emerge, but entirely new classes of threats will make their debut. Some evergreen threats will finally die off,  while others will roar back from oblivion. More devices (and more types of devices!) will be connected to networks, and attack surfaces will continue to grow in sophistication and scope.

While this may seem daunting, it’s also very exciting. We do not work in a boring industry, and we get to solve fascinating and complex problems every single day. runZero’s research team exists to discover new and innovative  ways to solve these problems and, just as importantly, identify new problems to solve tomorrow.

<a id="chapter-1-introduction"></a>
## Chapter 1
### Introduction
We hope that you will find our first research report educational and possibly even entertaining. We would appreciate your feedback; if you have suggestions, questions, or comments, please reach out by email via research@runzero.com.

Rob King
Director of Security Research

### Executive Summary
Tectonic shifts are happening in the cybersecurity industry, brought about by the rapid coalescence of several powerful trends and technological developments that have been years in the making.

First and foremost, vulnerabilities are being exploited at a truly unprecedented pace. And it’s working. So much so that the SEC now requires 8K filings for data breaches, not to mention the constant flow of news about emerging vulnerabilities and  successful compromises across organizations of every size and sector.

While zero day attacks at the network edge have surged, suppliers are struggling to provide timely patches for their products, often leaving customers at the mercy of attackers for days or weeks.  In response to the acceleration of exploitation, suppliers are now often releasing indicators of compromise (IOCs) in conjunction with their initial notifications to customers. Recently, the xz-utils backdoor became a stark reminder that supply chains are still under immense attack with catastrophic potential. The incident also catalyzed conversations about what it means to be a responsible consumer of open source products, and what “supplier” means in a shared security model.

Meanwhile, enterprise environments are changing faster than ever. The convergence between operational technology (OT) and information technology (IT) networks is an inevitable conclusion, creating a greenfield of high-value targets for cybercriminals to plunder.

Security programs have matured dramatically over the years, but are still dogged by end-of-life systems, unknown assets, and network segmentation challenges. These time-consuming issues compete for resources with short-term fire drills related to emerging threats and exposures. Defenders continue to juggle scoping, patch management, emergency response, and incident analysis on top of business requirements – all while security budgets shrink.

Our analysis also indicates that large organizations are still struggling with long-standing configuration problems. Remote management services are not in great shape. The trends for outdated TLS stacks, continued use of outdated protocols like SMB v1, and general hygiene issues with the Secure Shell and Remote Desktop Protocols continue unabated, with serious implications for long-term security. The silver lining is that default choices by operating system vendors are making a difference, but not fast enough to reduce the risk to the overall attack surface.

While generative artificial intelligence (Gen AI) and large language models (LLMs) have been touted as the next big thing for security, the reality is more modest. LLMs are helpful in many contexts, but are still prediction engines at heart. As a result, LLMs are limited to helping with the human side of security and struggle to replace expert systems and logic-based decision-making.

// runZero Research Objective
Amidst all of these dynamics, one thing remains clear: as more and more devices are attached to networks, we need faster ways to focus limited information security resources where they are needed most.

Our objective as a research team is to identify  incredibly efficient ways to pinpoint at-risk devices, through both precise fingerprinting and fast outlier analysis, and to quickly  get these tools into the hands of our customers and community. This first research report includes insights derived from our data analyses, and also describes how we work as a team with this objective in mind.

runZero’s primary data collection method is the runZero Explorer; a lightweight network point-of-presence that is delivered as software and performs active scans, analyzes traffic passively, and integrates with dozens of applications and services.

runZero Explorers provide a true insider’s perspective on global cybersecurity, finding ephemeral devices (phones, watches, cars), devices that normally are less monitored (thermostats, projectors, door locks), and the vast “dark matter” of ad hoc and forgotten networks, alongside the assets already on IT’s radar.

### Scope & Methodology
This report is based on a representative, anonymized data sample from the public runZero cloud platform.  This sample comprises almost four million assets with nearly fifty million associated, distinct data points, including more than 160 network protocols that have been normalized into 800+ distinct attributes and filtered through more than 17,000 unique fingerprints.

4M Assets
800+ Distinct Attributes
17K+ Unique Fingerprints
50M Data Points
160+ Network Protocols

### runZero’s Unique Perspective
runZero was founded on the principle that applied research makes for better asset discovery, and that better asset discovery is the foundation of modern exposure management. Today, runZero is recognized as the leading edge of Cyber Asset Attack Surface Management (CAASM).

This success is due to the work of the runZero research team: a group of industry veterans with decades of experience in information security. The practical output of their research is the accurate and in-depth identification of assets across cloud, on-premises, and remote environments.

CAASM was born out of the old adage that security teams can’t defend what they don’t know about. The same goes for assets with unknown attributes like their location, type, and nature. In addition to discovering devices and their associated details, CAASM attempts to methodically uncover the types and severity of exposures impacting those assets, offering defenders a new vantage point to observe the attack surface. 

CAASM elevates the discovery and visibility (both to attackers and defenders) of assets to a first-class field under the infosec umbrella, and is now considered foundational and critical components of an organization’s information security posture. This dynamic is directly tied to the exponential expansion of attack surfaces and to exposures outpacing defenders’ resources.

HD Moore
CEO & Co-Founder
Rob King
Director of Security Research
Tom Sellers
Principal Research Engineer

//Oddball Devices in Our Data Set 
Our data has uncovered a plethora of unusual connected devices, some of which have sufficient connectivity and services to route traffic, ranging from crockpots to cars.

The attack surface of an organization is no longer defined by on-premises locations with a known set of managed devices. Today, the attack surface consists of personal mobile phones, smart watches, thermostats in conference rooms, aquarium pumps in the lobby, game consoles in the CEO’s living room, and countless other devices, many of which come and go from the network on a regular basis.

![Figure 1: A list of devices with multiple attack surface designations found by runZero. Devices that span attack surfaces can provide entry points for attackers into internal organizational networks.]

Crockpot
Vacuum Cleaner
Light Bulb
Light Switch
Thermostat
DVR
Scanner
Voice Assistant

The COVID-19 pandemic resulted in an explosion of the attack surface perimeter. While remote work was previously a perk, suddenly it became the standard for countless organizations. Huge numbers of employees retreated from  the office and added their home networks as entry points to the previously gated and walled garden under the CISO’s watchful eye.

Once considered an island unto itself, operational technology (OT) and industrial control systems (ICS) have converged with IT and further compounded complexity. The whole world has, with very rare exceptions, settled on Ethernet and the Internet Protocol stack for IT. The vast, chaotic sea of proprietary protocols and competing standards of the OT/ICS world have now joined the fray in earnest, along with all the growing pains that come with it.

Today, the world’s living rooms and parking lots have become the CISO’s responsibility, as well as its factories and utility grids. In 2024, the US Environmental Protection Agency (EPA) wrote an open letter describing how “disabling cyberattacks” are attacking water and wastewater systems throughout the United States. Not so long ago, these systems were unreachable directly from the wider Internet. Today, many of them are perilously and openly  exposed to attackers from around the world.

It is in this world that we, as information security practitioners, now find ourselves. Defining attack surfaces is no longer an academic exercise that can be table-topped once a quarter. As exposures emerge at lightspeed, rapid, real-time discovery and CAASM are more critical than ever before.

>Today, the worlds' living rooms and parking lots have become the CISO's responsibility, as well as its factories and utility grids.

<a id="chapter-2-ot--cloud-impacts-on-attack-surfaces"></a>
## Chapter 2
### OT & Cloud Impacts on Attack Surfaces
In cosmology, there is the concept of the holographic universe: the idea that a three-dimensional volume of space can be entirely described by the exposed information on its two-dimensional surface.

In the context of an organization’s security posture, attack surface is everything; A vulnerability is almost meaningless unless it is exploitable by a bad actor. The trick to determining where the vulnerable rubber meets the exposed road is in identifying what’s actually reachable, taking into account security controls, or other defenses in depth.

As described in the previous section, attack surfaces are expanding in multiple ways, becoming more numerous and more specific. Two areas of attack surface growth that merit attention are operational technology and the cloud, not only because of their prevalence but also because of the associated risks.

The merging of operational technology and industrial control systems (OT/ICS) devices under the general IT umbrella has created another high-value attack surface. In the past, OT/ICS devices typically had completely separate, dedicated networks. Now they are increasingly attached to enterprise IT networks, making them a valuable and vulnerable part of an organization’s attack surface.

Meanwhile, the increasing commoditization and virtualization of infrastructure means that virtually all organizations now have a cloud-based attack surface to protect. Both independently and combined, these shifts have created new footholds for attackers that are worth examining.

### OT & IT Are Converging
Historically, security was of less concern than safety and reliability for the “grade-separated” networks supporting OT/ICS devices. These networks had different dynamics, using industry-specific network protocols and following maintenance schedules that were less frequent than IT systems.

OT equipment is designed for long-term reliability and infrequent changes. The result is that many factory floors, water treatment plants, critical infrastructure, and other industrial processes use equipment that is relatively slow compared to modern PCs.  In order to support real-time control requirements, OT equipment often excludes encryption and authentication at the protocol level.

OT systems offered a soft target for malicious actors, but only if they could reach these networks. Until recently, OT was simply not IT’s problem.

Improvements to networking and security technologies have changed this,  allowing organizations to link their OT and IT networks (sometimes on purpose, and sometimes not).

Teams that were previously responsible for securing laptops and servers are now also responsible for OT security. With mandates to improve management and monitoring efficiencies, systems that were once in a walled garden are now, at least in theory, reachable from anywhere in the world.

The 2022 report from the President’s National Security Telecommunications Advisory Committee on IT-OT Convergence concludes that we must “accept that IT/OT convergence will be the end state” of IT and OT.

>“IT/OT convergence will be the end state”

![Figure 2: A selection of industrial devices detected by runZero on the public Internet.]

### OT/ICS AROUND THE WORLD
runZero data confirms that thousands of OT/ICS devices are indeed “reachable from anywhere in the world.” These devices are prime targets for state actors and ransom seekers, as compromising them can result in industrial or utility disruption.

The number of industrial control systems (ICS) directly exposed to the public Internet is terrifying. While the year-over-year increase of exposed devices has finally slowed, the total number continues to climb. Over 7% of the ICS systems in this report’s sample data were connected directly to the public Internet, illustrating that organizations are increasingly placing critical control systems on the public Internet.

### OT SCANNING MOVES FROM PASSIVE TO SOMETIMES ACTIVE
OT devices often run industry-specific software on hardware with limited computing power. These constraints, combined with the long-term nature of OT deployments, result in an environment that does not respond well to unexpected or excessive network traffic. 

Stories abound of naive security consultants accidentally shutting down a factory floor with vulnerability scans. As a result, OT engineers have developed a healthy skepticism for any asset inventory process that sends packets on the network and instead opted for vendor-specific tools and passive network monitoring. Passive monitoring works by siphoning network traffic to an out-of-band processing system that identifies devices and unexpected behavior, without creating any new communication on the network.

While passive discovery is almost entirely safe, it is also limited. By definition, passive discovery can only see the traffic that is sent, and if a device is quiet or does not send any identifying information across the network, the device may be invisible. 

Passive deployments are also challenging at scale, since it’s not always possible to obtain a full copy of network traffic at every site, and much of the communication may occur between OT systems and never leave the deepest level of the network.

Active scanning is faster, more accurate, and less expensive to deploy, but most scanning tools are not appropriate or safe to use in OT environments. Active scanning must be performed with extreme care. Large amounts of traffic, or traffic that is not typically seen by OT devices, can cause communication disruptions and even impact safety systems. 

![Figure 4: A partial screenshot of an OT device detected by a runZero active scan.]

![Figure 3: An Allen-Bradley industrial PLC indicating 100% CPU utilization due to the device receiving a high rate of packets from an active scan NOT conducted by runZero.]

### SAFE ACTIVE SCANS
runZero enables safe scans of fragile systems through a unique approach to active discovery. This approach adheres to three fundamental principles.

→Send as little traffic as possible
→Only send traffic that the device expects to see
→Incrementally discover each asset to avoid methods that may be unsafe for a specific device

runZero supports tuning of traffic rates at the per-host level as well as globally across the entire task. runZero’s active scans can be configured to send as little as one packet per second to any specific endpoint, while still quickly completing scans of a large environment at a reasonable global packet rate.

![Figure 5: A high-level overview of the “progressive enhancement” probing process.]

runZero is careful to send only valid traffic to discovered services and specifically avoids any communication over OT protocols that could disrupt the device. This logic is adaptive, and runZero’s active scans are customized per target through a policy of progressive enhancement.

runZero’s progress enhancement is built on a series of staged “probes.” These probes query specific protocols and applications and use the returned information to adapt the next phase of the scan for that target. The earliest probes are safest for any class of device and include ARP requests, ICMP echo requests, and some UDP discovery methods. These early probes determine the constraints for later stages of discovery, including enumeration of HTTP services and application-specific requests. The following diagram describes how this logic is applied.

Safely Probe Asset
Create Empty Flag Set
Assets to Scan?
Pick Asset
Initialize Probes
Update Flags with Probe Results
Run Probe
Safe
Skip Probe
Unsafe
For Each Stage in Probing
For Each Probe in Stage
Flags Indicate Probe is Safe for Asset?

Lastly, runZero’s active scans also take into account shared resources within the network path. Active scans will treat all broadcast traffic as a single global host and apply the per-host rate limit to these requests. Scans that traverse layer 3 devices also actively reset the state within session-aware middle devices using a patent-pending algorithm. This combination allows runZero’s active scans to safely detect fragile devices and reduce the impact on in-path network devices as well as CPU-constrained  systems within the same broadcast domain.

For those environments where active scanning is inappropriate or unavailable, runZero also supports comprehensive passive discovery through a novel traffic sampling mechanism. This sampling procedure applies runZero’s deep asset discovery logic to observed network traffic, which produces similar results to runZero’s active scanner in terms of depth and detail.

### The Cloud Is Someone Else’s Attack Surface
The commoditization of computing power, massive advancements in virtualization, and fast network connectivity have led to just about any form of software, hardware, or infrastructure being offered “as a service” to customers. Where companies used to run their own data centers or rent rack units in someone else’s, they can now rent fractions of a real CPU or pay for bare metal hardware on a per-minute basis.

Cloud migrations are often framed  as flipping a switch, but the reality is that these efforts can take years and often result in a long-term hybrid approach that increases attack surface complexity. The result is more systems to worry about, more connectivity between systems, and greater exposure overall.

### CLOUD MIGRATIONS
// Migration Realities
Over the last five years, runZero has observed and assisted with dozens of cloud migration projects. These projects often take longer than planned and result in more assets  to manage at completion.

A common approach to cloud migrations is to enumerate the on-premises environment and then rebuild that environment virtually within the cloud provider. runZero helps customers with this effort by providing the baseline inventory of the on-premises data center and making it easy to compare this with the new cloud environment. During this process, organizations may end up with more than twice as many assets, since the migration process itself often requires additional infrastructure.

The migration process can be tricky, with a gradual approach requiring connectivity between the old and new environments. Shared resources such as databases, identity services, and file servers tend to be the most difficult pieces to migrate; however, they are also the most sensitive components of the environment. 

The result is that many cloud environments still have direct connectivity back to the on-premises networks (and vice-versa). A compromised cloud system is often just as, if not more, catastrophic to an organization’s security situation as a compromised on-premises system. 

Ultimately, the lengthy migration process can lead to increased asset exposure in the short-term due to  implied bidirectional trust between the old and new environments.

### NEW EXPOSURES
Cloud providers assume many of the challenges with data center management; failures at the power, network, storage, and hardware level now become the provider’s problem, but new challenges arise to take their place including unique risks that require a different set of skills to adequately address.

Cloud-hosted systems are Internet-connected by definition. While it’s possible to run isolated groups of systems in a cloud environment, cloud defaults favor extensive connectivity and unfiltered egress. Although cloud providers offer many security controls, only some of these are enabled  by default, and they function differently than on-premises solutions. 

Cloud-hosted systems are also vulnerable to classes of attacks that are only significant in a shared computing environment. CPU-specific vulnerabilities like  Meltdown,  Spectre, and Spectre v2  force cloud operators to choose between performance and security. The mitigations in place for these vulnerabilities are often bypassed. For example, the recently-disclosed CVE-2024-2201 allows for Spectre-style data stealing attacks on modern processors, a concern in shared-hosting cloud environments.

Additionally, the ease of spinning up new virtual servers means that cloud-based inventory is now constantly in flux, often with many stale systems left in unknown states. Keeping up with dozens (or even thousands) of cloud accounts and knowing who is responsible for them becomes a problem on its own.

We analyzed systems where runZero detected end-of-life operating systems (OSs), and found that the proportions of systems running unsupported OSs are roughly the same across the  cloud and external attack surfaces. This implies that the ease of upgrading cloud systems may not be as great as advertised.

![Figure 7: Comparison of end-of-life operating system distribution between cloud and external attack surfaces.]

Cloud
External
Past EOL
10.3%
8.1%
Past Extended EOL
1.7%
1.1%

![Figure 6: CPU-specific vulnerabilities targeting cloud operators.]

V1
V2

### HYBRID IS FOREVER
Cloud infrastructure is here to stay, but so is on-premises computing. Any organization with a physical presence – whether retail, fast food, healthcare, or manufacturing – will require on-premises equipment and supporting infrastructure.

Cloud services excel at providing highly available central management, but a medical clinic can’t stop treating patients just because their Internet connection is temporarily offline. A hybrid model requires faster connectivity and increasingly powerful equipment to securely link on-premises and cloud environments.

Even in more simplistic environments, cloud migrations leave behind networking devices, physical security systems, printers, and file servers. All of that equipment will most likely be linked to cloud environments, whether through a VPN or over the public Internet.

>While cloud migrations can help organizations modernize, these environments still require equally comprehensive asset visibility and exposure management with on-premises infrastructure.

<a id="chapter-3-unusual-assets-are-risky-assets"></a>
## Chapter 3
### Unusual Assets Are Risky Assets
>The beginning of many great projects start with a researcher saying “that’s odd.”

One of these moments led to the runZero concept of the “outlier score,” a single, simple numeric value that quantifies how “different” an asset is compared to its neighbors and, importantly, the discovery of how that difference corresponds to the risk associated with a given asset.

Identifying risky assets is fundamental to successful exposure management programs, but this process can be challenging due to the quantity and sources of data. In this chapter, we will explore how runZero outlier scores can be used to quickly identify risky assets, even in cases where no vulnerability management data is available.

// Identifying Outliers
Our research shows that the outlier score, defined as how unique an asset is within the context of its neighbors, strongly correlates with the risk ranking sourced from third-party vulnerability management data, providing organizations another valuable method to pinpoint potential exposures.

Risk
critical
Outlier score
500

### Calculating Outlier Scores
runZero ingests data from third-party integrations such as vulnerability scanners, device management systems, and security analysis tools, and then combines these data points with our own analysis. This produces a unified numeric risk rank for an asset. In general, the “riskier” an asset appears to be, the higher its rank becomes on the risk scale.

runZero looks for assets that differ significantly from their peers, using multiple dimensions and points of comparison. The more an asset deviates from the site’s “baseline,” the greater its outlier status from runZero’s perspective. This is quantified in a single number, known as the outlier score: the more unusual a device is in its context from the baseline, the higher its outlier metric will be.  The outlier metric starts at zero, but has no practical upper bound (though values >600 are fairly rare).

Identifying outliers breaks through the noise by highlighting assets that merit further investigation by security teams. Often, sites will have large numbers of very similar assets – a server farm of systems running Linux and some routers and switches, or an office with a large number of Windows PCs and printers. In those instances, a small number of, or even a single instance of, unusual devices may indicate that there is an asset that has escaped notice and attention by staff.

// Research Note
>Note that for sites with no “common baseline” of assets, no outlier scores are computed. If they were, everything would be an outlier!

### Outliers Are Riskier, on Average
runZero observed that outlier scores are strongly predictive of asset risk.  An analysis of 680,000 assets across sites in a variety of organizations and settings revealed that this correlation is quite strong.

Figure 8 illustrates the correlation between the average risk rank of an asset with a given outlier score; color intensity indicates overlapping data points. Lines of best fit are provided for all data points (black), and those with an outlier score ≤300; higher outlier scores indicate that an asset is more unusual.

![Figure 8: Average risk rank versus runZero outlier score.]

4.0
3.5
3.0
2.5
2.0
1.5
1.0
0.5
0.0
0.0
100
200
300
400
500
600
700
≥800

Average Risk Rank
Outlier Score

By definition, most assets have a relatively low outlier score, but note that there is a particularly strong correlation between outlier score and risk rank. It is especially notable that very few devices have an outlier score ≥300 without also having a risk rank ≥2.0.

This correlation is particularly notable for its predictive power. In general, an asset with an outlier score ≥250 has a 78% chance of having a risk rank ≥2.0. Importantly, the opposite also generally holds true: an asset with an outlier score of ≤250 has a 69% chance of having a risk rank ≤2.0.

### Guidance
An unusual asset may be riskier than its peers, but that doesn’t guarantee that it will be noticeable. The outlier score can often reveal when assets differ from the baseline in ways that would not necessarily be apparent to staff: for example, an unusual round-trip time on TCP connections, a slightly different set of services running, and so on.

runZero’s research shows that these assets, even if just slightly unusual, are often significantly riskier than others. The outlier score gives security practitioners a powerful tool to find riskier assets –  even when no one else might notice.

Risk
critical
Outlier score
500

<a id="chapter-4-some-old-enemies"></a>
## Chapter 4
### Some Old Enemies
>Make new friends, but keep the old: one is silver, the other gold.

Despite enormous advances within information technology, security practitioners are still plagued by common problems. Advances in secure-by-default designs, zero-trust architectures, and overall security awareness all help, but organizations still struggle with end-of-life assets, network dark matter, and segmentation challenges. These problems are difficult to solve and they often exist outside of defenders’ areas of control. Most importantly, from the attacker’s perspective, they still provide easy footholds into an environment.

### End-of-Life Is Not the End
All of the system hardening and security patches in the world cannot protect a system that is not updated to use those features. System vendors generally provide patches and updates for a limited timespan. At that point, end users must invest in an upgrade to a newer version of the system or fend for themselves and hope for the best with an end-of-life (EOL), outdated asset lurking on the attack surface. 

EOLed systems often stick around for years, mostly forgotten but still part of an organization’s infrastructure and, therefore, its attack surface. New vulnerabilities are still discovered and exploited in these outdated systems as the April 2024 D-Link NAS issue illustrated. Despite the known exposure, being EOL means that fixes will not be forthcoming.

While this may seem like an academic exercise, EOLed systems are surprisingly common. Our findings show many still-active EOLed operating systems in various environments.

### OPERATING SYSTEM END-OF-LIFE
Operating systems typically have multiple phases of vendor support, referred to as a support lifecycle. The duration of the lifecycle and services provided in various stages vary from vendor to vendor,  usually tapering off with fewer updates and patches in later stages.

The two phases we are most concerned with are:

Mainstream support: during which vendors release patches that may add new features, fix bugs, or mitigate security vulnerabilities.

Extended support: during which only critical bugs and vulnerabilities are addressed.

While some vendors’ terminology and phases may slightly differ, generally speaking, most support lifecycles can be broadly mapped to these two phases.

When a vendor stops providing upgrades for non-critical issues, the product is considered in an “End-of- Life” (EOL) status. There may be an additional period known as “Extended-End-of-Life” (EEOL) during which the vendor continues to provide updates for critical issues. EOL and EEOL can happen concurrently or separately depending on the system and the vendor. Most importantly, after EOL, systems no longer receive critical updates or security patches, and thus become much greater risks to keep around.

But around they are! Systems have a long tail: if they still work, replacing them with a supported alternative may be more trouble than it’s worth. In some cases, the responsible staff can’t or won’t; in others, the system may host critical functions that are not supported on newer systems. Uptime guarantees and financial considerations may also play a role.

The presence of Windows Server 2012 R2 isn’t very surprising; it reached extended EOL only very recently, in October of 2023. While unfortunate, it’s not unusual for server migrations to drag on past EOL dates due to logistical and compatibility concerns.

![Figure 9: Top OS past extended EOL.]

Microsoft Windows Server 2012 R2
12.69%
Ubuntu Linux 14.04.x
7.66%
Microsoft Windows 10 (1809)
5.90%
Microsoft Windows 7
5.30%
Microsoft Windows 10 (1909)
5.01%
Microsoft Windows 10 (1607)
4.68%
Microsoft Windows Server 2008 R2
4.03%
VMware ESXi 6.7.0
3.11%
VMware ESXi 6.5.0
2.23%
Microsoft Windows 10 (20H2)
2.16%

When we look at our sample data for operating systems that are past their extended EOL dates, we see that the majority are running some version of Microsoft Windows:

The second major group is composed of various Windows 10 releases. Windows 10 was originally released in July of 2015. Microsoft has generally released two major updates for it every year since. Typically, updates released in the first half of the year are supported for 18 months and those released in the second half are supported for 30 months. There are some variations on this theme, with  Long-Term Servicing Channel (LTSC) editions, for example, having longer lifespans.

![Figure 10: Windows 10 past extended EOL.]

Microsoft Windows 10 (1809)
28.31%
Microsoft Windows 10 (1909)
24.06%
Microsoft Windows 10 (1607)
22.45%
Microsoft Windows 10 (20H2)
10.38%
Microsoft Windows 10 (1803)
7.69%
Microsoft Windows 10 (21H1)
3.67%
Microsoft Windows 10 (1709)
1.77%
Microsoft Windows 10 (1703)
1.33%
Microsoft Windows 10 (1511)
0.33%

### EXPOSED SYSTEMS PAST EXTENDED EOL
While operating  systems outside of their extended lifespans are always worth looking into, those with exposure to an external attack surface are particularly worrisome. Of all systems exposed to an external attack surface and for which EOL data was available, 7.9% were past their extended EOL dates. That means that roughly 8% of all devices exposed to external attackers are probably not receiving security updates.

For server operating systems specifically, approximately 6% were past their extended EOL dates, with the individual percentages varying across operating systems. Of particular note is VMware ESXi, with over a third of exposed systems being past their extended EOL date.

![Figure 11: Server operating systems with external attack surface exposure, past extended EOL.]

VMware ESXi
34.4%
Debian Linux
11.7%
Windows
8.7%
Ubuntu Linux
7.3%
Windows Server
3.1%
Enterprise Linux (RHEL & derivaties)
1.2%

### CASE STUDY: THE BOA WEB SERVER
The Boa webserver is an open source web server designed to have low resource requirements for users and to be compatible with embedded applications. The last official release of the Boa webserver, version 0.94.14rc21, was in February of 2005. For comparison, the Colts have won a Super Bowl more recently than the latest release of the Boa web server, and the Colts haven’t won a Super Bowl since 2007!

There are known vulnerabilities in Boa that have been exploited in critical infrastructure in the past. For example, in November 2022, Microsoft disclosed that Boa web servers in Internet-of-Things (IoT) devices were a common attack vector against power grids in India.

While it is relatively easy for an administrator to determine if a server is running Boa, it is much harder to detect in an embedded device. Boa is common in embedded devices like security cameras and  IP phones that are widely deployed in enterprise networks. Therefore, curating an accurate inventory of an organization’s embedded devices, not just servers, that are running Boa is critical for protecting these networks.

![Figure 12: Boa web server version distribution in runZero data.]

![Figure 13: Device types still running Boa in sample runZero data.]

58.07%
26.12%
8.4%
2.57%
2.02%
1.42%
0.95%
0.29%
0.13%
0.03%
Boa/0.94.14rc21
Boa/0.93.15
Boa/0.94.13
Boa/0.94.14rc18
Boa/0.94.14rc19
Boa/0.94.14rc20
Boa/0.94.101wk
Boa/0.92o
Boa/0.94.11
Boa/0.94.8.3

Network-Attached Camera
92.3%
Media & Telephony Devices
5.5%
Environmental Control Devices
0.9%
Network Devices
0.9%
Industrial Control Devices
0.3%

### Dark Matter: IoT & Embedded Devices
The level of attention, monitoring, and updates that network-connected devices receive can be divided into a three-tier hierarchy, a “hierarchy of visibility” as it were.

At the top level, there are devices that humans interact with directly, or form part of a production system: our laptops, desktops, servers, routers, and switches. They tend to have high visibility to the information security team via mechanisms like Simple Network Management Protocol (SNMP) and endpoint management (EPM) software. These systems usually get frequent, managed updates that are often installed automatically and en masse.

The middle tier consists of “limited visibility” devices present in every office: smart TVs and projectors, media devices like Rokus and Apple TVs, wireless access points, and printers. These devices often support updates over the network but may not receive frequent updates and may require manual intervention to apply them. How often do we think about updating the firmware on our venerable Brother printers?

And last but not least, the dark matter of networks makes up the bottom tier. Much like dark matter in cosmology, these devices are present on the network and their influence can be felt, but they are mostly invisible to IT and management tools. These are things like thermostats, smart plugs and lights, aquarium pumps, refrigerators, sprinkler systems, physical access control systems, and so on. These