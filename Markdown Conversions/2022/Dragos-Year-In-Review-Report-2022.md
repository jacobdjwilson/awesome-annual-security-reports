# ICS/OT Cybersecurity Year in Review 2022

## Table of Contents
- [2022 Key Findings Overview](#2022-key-findings-overview)
- [Key Highlights: By the Numbers](#key-highlights-by-the-numbers)
- [2022 Threat Activity](#2022-threat-activity)
- [2022 New Threat Groups](#2022-new-threat-groups)
- [Updates on Active Threat Groups](#updates-on-active-threat-groups)
- [CHERNOVITE’S PIPEDREAM](#chernovites-pipedream)
- [2022 Industrial Ransomware Analysis](#2022-industrial-ransomware-analysis)
- [ICS/OT Vulnerabilities](#icsot-vulnerabilities)
- [Dragos Frontline Perspective](#dragos-frontline-perspective)

---

## 2022 Key Findings Overview

2022 saw a breakthrough escalation in capabilities by a new modular industrial control systems (ICS) malware, PIPEDREAM, developed by the threat group, CHERNOVITE. CHERNOVITE’S PIPEDREAM toolkit has the capabilities to impact devices that control critical infrastructure – devices that manage the electrical grid, oil and gas pipelines, water systems, and manufacturing plants. For industrial operators this can be viewed as a supply chain risk, as the methods target key vendor systems.

PIPEDREAM is the first reusable cross-industry capability that impacts native functionality in industrial protocols and a wide variety of devices. Dragos and our third-party partners discovered and analyzed its capabilities before it was employed. Malware development is shifting towards improving on the known and successful techniques used in earlier ICS cyber attacks. This accumulated knowledge may have informed PIPEDREAM’s malware framework, which is more robust and modular and most likely will inform CHERNOVITE and other adversaries’ malware development in the future.

The threats and ransomware attacks tracked by Dragos in 2022 show a continued increase. Highlights of these attacks by vertical industry include:

*   The first attacks against the mining and metals industries in Australia and New Zealand (ANZ) region.
*   Continued targeting of renewable energy companies in the U.S. and the European Union (EU).
*   Increased attacks on energy, food and beverage, pharmaceuticals, chemicals, water and wastewater.
*   Accelerated attacks in electrical, manufacturing, oil and natural gas, and liquefied natural gas.

### Russia’s Invasion of Ukraine

On February 25, 2022, the day after Russia invaded Ukraine, the ransomware group Conti declared that if a cyber attack or warfare were directed against Russia, Conti would use “all possible resources to strike back at the critical infrastructure of an enemy.”¹

During 2022, Ukraine saw increased threat group activity targeting its energy and critical industrial infrastructure sectors. Russia’s 2022 invasion of Ukraine provided opportunities for Russia-aligned actors to use their cyber offensive capabilities preemptively and in parallel to its kinetic attacks. As Western countries placed sanctions on Russia and indicted key members of Russian cyber operations, the U.S. government’s Cybersecurity and Infrastructure Security Agency (CISA) prepared for potential retaliation by issuing a call for “Shields Up,” which included actions to safeguard ICS and OT environments.

According to an analysis of the threats against U.S. energy entities, adversaries are primarily focused on reconnaissance. Dragos has observed fewer cyber-focused attacks on OT in U.S. energy sectors than predicted at the beginning of the war between Russia and Ukraine. Dragos has not observed any ICS Cyber Kill Chain Stage 2 follow-on attacks against U.S. energy entities.

While Dragos observed less than the predicted activity, there was still at least one significant attack. The Dragos-designated threat group ELECTRUM deployed a new variant of CRASHOVERRIDE/INDUSTROYER at a Ukrainian power company; however, this new variant did not have the full capabilities of CRASHOVERRIDE.

¹ https://www.politico.com/news/2022/02/25/russian-ransomware-gang-threatens-countries-ukraine-00011896

### Impacts of Ransomware on Manufacturing

Ransomware attacks on industrial infrastructure organizations nearly doubled in 2022. With over 70 percent of all ransomware attacks focused on manufacturing, ransomware actors continue to broadly target many manufacturing sectors and subsectors. As ransomware activity increases, it results in more risk for OT networks, particularly networks with poor segmentation.

### Trends in ICS/OT Vulnerabilities

Vulnerabilities saw an increase of 27 percent in 2022. This was a material increase, but a slowdown in the growth rate. Improvements in the rate of mistakes and risk ratings were a very positive signal. The standard information technology (IT) approach to vulnerability mitigation is a patch. To patch in the OT world often requires system and plant shut-downs. ICS/OT relies on alternative mitigation to both reduce risk and maintain production. The 77 percent of vulnerabilities that lack that mitigation makes maintaining operations very challenging.

### Markers for a Strong ICS/OT Cyber Defense – 5 Critical Controls

On the defense side, Dragos recommends using the SANS “Five ICS Cybersecurity Critical Controls” for industrial cybersecurity as the frame to evaluate progress. The statistics shown are only “indicators” of the five critical controls, though derived from in-depth engagements with industrial clients.

Trends in ICS-Specific Incident Response, the first of SANS Five Critical Controls, were mixed, with improvements in detection, elevation, and plan activation; scores declined in the ability to communicate, document, and recover. Electric utilities showed the best preparedness, followed by oil and gas.

Manufacturing represented the worst results among verticals.

For Defensible Architecture, the second critical control, there were marked improvements to use of network segmentation in engagements. Environments with significant network segmentation issues were down 2700 basis points; but with 50 percent of environments still having issues, there is plenty of room for improvement. Similarly, uncontrolled external connections into OT were found in 53 percent of engagements in 2022; still high, but much better than 2021’s 70 percent.

ICS Network Visibility, the third critical control, continued to be a challenge. A full 80 percent of environments had little or no visibility into traffic and devices in ICS/OT environments. Though an improvement of 600 basis points from 2021, the large number indicates that a vast majority of environments will find it challenging to detect and investigate issues, much less maintain accurate asset inventory.

Secure Remote Access is the fourth critical control, and showed negative trending, with users in 54 percent of environments using same credentials for IT systems as OT systems. Remote access is the most common way for threat groups to penetrate OT systems; sharing the same credentials make it much easier for threats to cross from IT to OT systems.

Finally, for Risk-Based Vulnerability Management, the reduction in outright mistakes is encouraging. Only fifteen percent of CVEs included errors in 2022, down 4 percent from 2021. But with 77 percent of vulnerabilities lacking mitigation steps, it demonstrates the challenge of employing a risk-management approach that can both mitigate the risk of exploit AND reduce production downtime from patches.

Of course, that is a summary of only some of the findings. Much more detail from Dragos’s intelligence research, platform measurements, and consulting engagements follow.

## Key Highlights: By the Numbers

### PIPEDREAM summary

- **7th**: The seventh ICS-impacting Malware
- **3**: ICS-specific malware components inside PIPEDREAM
- **5**: ICS protocols abused: FINS, MODBUS, CODESYS, OPC UA, Schneider Electric NetManage
- **1000s**: of devices potentially impacted
- **100s**: of suppliers impacted

### Threat Group Summary

- **Two New Threat Groups Identified**: CHERNOVITE, BENTONITE

### Key Ransomware Findings

- **↑ 87%**: Ransomware attacks against industrial organizations increased 87 percent over last year.
- **+35%**: Dragos tracked 35% more ransomware groups impacting ICS/OT in 2022.
- **72%**: of all ransomware attacks targeted 437 manufacturing entities in 104 unique manufacturing subsectors.

### Key Service Engagement Findings

- **80%**: of services customers had limited OT visibility into their ICS environment (-6% FROM 2021)
- **50%**: of services engagements identified issues with network segmentation (-27% FROM 2021)
- **53%**: of services engagements discovered undisclosed or uncontrolled external connections to the OT environment (-17% FROM 2021)
- **54%**: of services customers lacked separate IT and OT user management (+10% FROM 2021)

### Key Vulnerabilities Findings

- **↑ 27%**: increase in the number of vulnerabilities that Dragos investigated in 2022 over 2021
- **34%**: of advisories contained errors in 2022.
- **53%**: Dragos provided mitigations for 53% of the advisories that had none.
- **83%**: of vulnerabilities reside deep within the ICS network.
- **13%**: of advisories were extremely critical in 2022
- **51%**: of the advisories that Dragos analyzed could cause both a loss of view and loss of control, up from 35% last year.

## 2022 Threat Activity

### Threat Activity Overview

After analyzing year-over-year activity, Dragos assesses with low confidence that the increase in threat group activity and the focus on energy sectors (electric, renewables, and ONG) could be the result of geopolitical tensions between the Russian Federation and the European Union (EU) over energy resources and the ongoing war in Ukraine. Threat group activity is relatively steady, and some of the increase in activity is unrelated to geopolitical tensions. Some threats Dragos tracks such as CHERNOVITE may proliferate into disruptive and destructive capabilities in the future.

### Summary of Dragos-designated threat group intelligence for 2022:

During 2022, Dragos tracked 20 threat groups and discovered two new threat groups — CHERNOVITE and BENTONITE.

- There are two new threat groups: CHERNOVITE and BENTONITE
- There were eight active threat groups: BENTONITE, CHERNOVITE, ELECTRUM, ERYTHRITE, KAMACITE, KOSTOVITE, WASSONITE and XENOTIME.
- KOSTOVITE, KAMACITE, XENOTIME and ELECTRUM exhibit all aspects of the ICS Kill Chain Stage 1, and several of Stage 2 (Develop, and Install/Modify).
- BENTONITE and WASSONITE demonstrate only Stage 1 aspects of the ICS Cyber Kill Chain
- ERYTHRITE demonstrates only Stage 2 aspects of the ICS Cyber Kill Chain.
- Twelve threat groups were dormant.
- Zero threat groups were retired in 2022.

For context, here are the Dragos-designated threat group statistics from the 2021 Year in review:

- Three new threat groups: KOSTOVITE, ERYTHRITE and PETROVITE
- CHERNOVITE is the threat group that developed PIPEDREAM. PIPEDREAM is the seventh and most recent ICS-targeted malware discovered in 2022.
- CHERNOVITE represents the most dangerous threat group to date as it exhibits all aspects of the ICS Kill Chain Stage 1 and Stage 2.
- Three active threat groups: STIBNITE, WASSONITE and KAMACITE
- BENTONITE targets the ONG and LNG industrial verticals in the U.S.

### How Dragos Tracks Threat Activity

To be prepared for future threats to industrial infrastructure, Dragos emphasizes the importance of understanding how adversaries steal information, and gain access to a company’s ICS/OT network and systems.

Dragos tracks threat groups that attempt to gain access to ICS/OT networks and that could cause a potential threat to them in the future.

A number of the threats that Dragos tracks may evolve their disruptive and destructive capabilities in the future because adversaries often do extensive research and development (R&D) and build their programs and campaigns over time. This R&D informs their future campaigns and ultimately increases their disruptive capabilities. For instance, most of PIPEDREAM’s modules are examples of capabilities that were designed to target OT and ICS infrastructure. Even when an adversary accidentally stumbles onto an OT environment, there is still a risk to that environment. Adversarial intent is not necessarily positively correlated with attacks on ICS/OT environments – they may be “targets of opportunity” discovered during enterprise IT reconnaissance.

For the 2022 Year in Review, Dragos has broadened its criteria for threat group reporting. Dragos now covers threat group activity from 2020 to 2022.

This methodology is based on the following parameters:

*   If a threat group has been active during the last 24 months, it is considered active.
*   If there is no threat group activity during the last 24-48 months, it is considered dormant.
*   If there is no activity in 48 months, the threat group is considered retired.
*   Dragos maintains a list of dormant threat groups to analyze new activity, looking for any overlaps or similarities in the threat group tactics, techniques, and procedures (TTP) or target sets.

This new approach allows Dragos to focus and provide intelligence on the cyber threats that occurred during the last two years. In cases where the evolution of an attack pattern is recognized, even when threat groups are retired, Dragos will report on this activity. Threat groups could go dormant for various reasons, such as the threat group stopping its activity or repurposing its operations. Or, potentially, we lost visibility of its actions.

## 2022 New Threat Groups

### CHERNOVITE & BENTONITE

#### CHERNOVITE – Developer of PIPEDREAM

CHERNOVITE is the developer of PIPEDREAM, a modular ICS attack framework and the seventh known ICS-specific malware, following STUXNET, HAVEX, BLACKENERGY2, CRASHOVERRIDE, TRISIS, and Industroyer2. CHERNOVITE’s PIPEDREAM is the first ever cross-industry disruptive/destructive ICS/OT capability. It represents a substantial escalation in adversarial capabilities.

CHERNOVITE possesses a breadth of ICS-specific knowledge beyond what has been demonstrated by previously discovered threat groups. The ICS expertise demonstrated in the PIPEDREAM malware includes capabilities to disrupt, degrade, and potentially destroy physical processes in industrial environments.

PIPEDREAM is the first scalable, cross-industry ICS attack framework known to date.

While PIPEDREAM itself is a new ICS capability, its emergence is also indicative of the trend toward more technically capable and adaptable adversaries targeting ICS/OT. In addition to implementing common ICS/OT-specific protocols in PIPEDREAM, CHERNOVITE improved the techniques from prior ICS malware. CRASHOVERRIDE, and the associated threat group, ELECTRUM, exploited the OPC Data Access (OPC DA) protocol to manipulate breakers and electrical switchgear. CHERNOVITE, on the other hand, uses the newer but comparable OPC UA protocol.

Dragos assesses with high confidence that a state actor developed PIPEDREAM intending to leverage it in future operations for disruptive or destructive purposes. Dragos assesses with moderate confidence that CHERNOVITE represents an “effects/impact team” instead of an “access team” — meaning, that PIPEDREAM was designed to be leveraged for impact after the initial access into the target environment has been obtained by another threat group.

Most likely, CHERNOVITE developed PIPEDREAM’s capabilities for a malicious operator with the intent and motivation to access, manipulate, and disrupt OT environments and processes. PIPEDREAM’s capabilities can provide an adversary with a range of options for learning about a target’s OT network architecture and identifying its assets and processes. This information can set the stage for disruptive and destructive effects, but it also increases an adversary’s knowledge to develop even more capabilities to disrupt or destroy on a much broader scale.

In its present form, the PIPEDREAM attack framework could be leveraged to target equipment in multiple sectors and industries. Given PIPEDREAM’s modular nature, CHERNOVITE could easily adapt it to compromise and disrupt a broader set of targets.

Therefore, it is necessary for defenders to harden their environment against CHERNOVITE’s known set of capabilities and focus on the tactics, techniques, and procedures (TTP), abuse of environment-native protocols and functionality, and exploitation of a lack of OT asset visibility and network monitoring.

Dragos assesses with low confidence that no adversary has employed or leveraged components of PIPEDREAM against industrial networks for disruptive or destructive effects. Dragos’s discovery of CHERNOVITE constitutes a rare case of accessing and analyzing malicious capabilities developed by an adversary before its employment, giving defenders a unique opportunity to prepare in advance.

#### CHERNOVITE

- **ADVERSARY**: Development and effects team focused on ICS disruption
- **CAPABILITIES**:
    - Unique tool development
    - Uses ICS-specific protocols for reconnaissance, manipulation, and disabling of PLCs
    - PLC Credential Capture. Password brute forcing and denial of service
- **VICTIMS**:
    - Could impact all industries, initially targeting electric, ONG, and manufacturing
    - Companies with Schneider Electric, Omron, and CODESYS PLCs, as well as any OPC UA
- **INFRASTRUCTURE**: Unknown
- **ICS IMPACT**: Loss of View, Availability, Safety, and Control; ICS Kill Chain Stage 2 – Install/Modify, Execute ICS

#### BENTONITE

BENTONITE is a new threat group increasingly and opportunistically targeting maritime oil and gas (ONG), governments, and the manufacturing sectors since 2021. BENTONITE conducts offensive operations for both espionage and disruptive purposes.

BENTONITE seeks to exploit vulnerable remote access assets or internet-exposed assets that can facilitate access.

BENTONITE’s operations have impacted North American ONG maritime support organizations and State Local Tribal and Territorial (SLTT) governments. BENTONITE compromised these organizations by exploiting vulnerabilities on internet-facing assets through Log4J and VMWare Horizons vulnerabilities.

Once BENTONITE achieves initial access, the adversary delivers a downloader-type malware implant to retrieve additional malware implants from adversary-created GitHub accounts. These malware implants conduct command and control to adversary-owned infrastructure, reconnoiter the compromised host, conduct network reconnaissance, and establish a connection through SSH, enabling the adversary operator to perform interactive operations.

BENTONITE’s activities are highly opportunistic when it comes to the victims they target. Additionally, once BENTONITE gains access to a victim’s environment, this adversary is very tenacious in its persistence to retain its access by performing lateral movement to other hosts, collecting credentials, and establishing long-term persistence to re-enable access to the adversary operator through scheduled tasks in combination with malware implants.

BENTONITE utilizes legitimate infrastructure, such as GitHub, and adversary-owned infrastructure for command and control and capability delivery. BENTONITE is capable of and has in past compromises disrupted operations through wipers; however, this was not observed in the compromises of the ONG or SLTT organizations.

BENTONITE has overlapping activity clusters with Microsoft’s activity group PHOSPHORUS (DEV-0270) and CrowdStrike’s activity group NEMESIS KITTEN.

#### BENTONITE

- **ADVERSARY**: Associated with PHOSPHORUS; Able to run multiple, concurrent operations
- **CAPABILITIES**: Multi-stage downloaders, victim enumeration, reconnaissance and C2 capabilities; Vulnerability exploitation; Heavy use of Powershell to facilitate compromise; Disruptive capabilities
- **VICTIMS**: Highly opportunistic; U.S. oil and gas, manufacturing; State, local, tribal and territorial organizations
- **INFRASTRUCTURE**: Credential harvesting; Separate domains for phishing and C2; Utilizes Github for delivery, SSH and HTTP for C2
- **ICS IMPACT**: Espionage, data exfiltrations, and IT compromise; Disruptive effects possible

## Updates on Active Threat Groups

### KOSTOVITE, KAMACITE, XENOTIME, ELECTRUM, ERYTHRITE, WASSONITE

#### KOSTOVITE

In June 2021, Dragos began tracking the threat group KOSTOVITE. KOSTOVITE’s operational technology (OT)-related operations have focused on the compromise of an energy firm and the firm’s managed global power generation facilities.

KOSTOVITE has achieved Industrial Control System (ICS) Cyber Kill Chain Stage 1 and subsequent ICS Kill Chain Stage 2, Develop events.

While KOSTOVITE’s demonstrated capabilities do not extend to industrial control system (ICS)-disruption-specific tools or resources, KOSTOVITE has demonstrated skilled lateral movement and initial access operations into ICS/OT environments and on SCADA assets.

KOSTOVITE focuses on compromising and subverting internet-exposed remote access devices as a jump-off point into OT targets while establishing persistence across the upgrades of the remote access devices.

KOSTOVITE maliciously enlists third-party internet of things (IoT) devices to relay and obfuscate the origin of their activities. KOSTOVITE shows unusual discipline by dedicating a set of compromised IoT devices to a single target and then performing a clean-up operation at the end of its activities.

Based on non-public reporting on Manganese adversary activity and activity described by an early 2022 Kaspersky ICS CERT report², multiple adversaries with different objectives may share a common infrastructure with KOSTOVITE.

While the infrastructure enumerated by Microsoft and Kaspersky shows a tentative link to the KOSTOVITE activity that Dragos observed in 2021, Dragos cannot definitively tie all these activities to one adversary.

Recent public reporting shows KOSTOVITE may be linked to the APT5 adversary group. The U.S. government reported in December 2022 that APT5 was actively exploiting a zero-day vulnerability in Citrix perimeter access devices, which parallels KOSTOVITE’s zero-day exploitation against an energy O&M firm in 2021, and previous APT5 campaigns targeting perimeter devices in 2019. Both KOSTOVITE and APT5 have leveraged vulnerabilities in perimeter-facing remote access appliances, achieving persistent access to targets over several months undetected. There is a likelihood that KOSTOVITE’s tooling may expand to include the remote access device zero-days exploited by APT5.

If KOSTOVITE once again takes aim at ICS and OT, asset owners and operators should be ready with robust detection, defense, and mitigation regimes for the ICS and OT enclaves that are inside the enterprise perimeter and potentially vulnerable to KOSTOVITE exploitation.

² Targeted attack on industrial enterprises and public institutions - Kaspersky ICS CERT
³ https://media.defense.gov/2022/Dec/13/2003131586/-1/-1/0/CSA-APT5-CITRIXADC-V1.PDF

#### KOSTOVITE

- **ADVERSARY**: High level of operational discipline and network device knowledge; Lives off land with stolen sys/net-admin creds
- **CAPABILITIES**: Zero-day exploits; Undetected intrusion via internet remote access device compromise and subversion
- **VICTIMS**: Global energy company based in U.S.; North America, Australia
- **INFRASTRUCTURE**: Dedicated per target; Compromised home and small business IoT devices exposed to Internet; Compromised enterprise perimeter devices
- **ICS IMPACT**: Stage 2 of ICS Kill Chain; Intrusion into OT networks and devices

#### KAMACITE

KAMACITE is a threat group targeting industrial infrastructure verticals since at least 2014. KAMACITE is linked to multiple industrial infrastructure intrusion events, including operations enabling the 2015 and 2016 Ukraine power events. KAMACITE possesses industrial control system (ICS)-specific capabilities but has also facilitated ICS disruptive events executed by other threat groups such as ELECTRUM.

Most recently, in June of 2022, Dragos identified KAMACITE network infrastructure communicating with an oblenergo (a regional power distribution entity) in Ukraine. The oblenergo KAMACITE targeted in this incident was one of the same oblenergos impacted in a 2015 cyber attack, which triggered a large-scale power outage across western Ukraine.

In February 2022, the National Cyber Security Centre (NCSC) in the UK released a joint report with CISA, NSA, and FBI detailing the new malware capability called CYCLOPS BLINK, stating that it targets “primarily small office/home office (SOHO) routers and network-attached storage (NAS) devices.”⁴ The CYCLOPS BLINK malware family targets routers and firewall devices from WatchGuard and ASUS and adds them to a botnet for command and control (C2).

Dragos assesses with high confidence that this activity is associated with KAMACITE. At the time of the February 2022 report, Dragos identified victims in the electric, natural gas, and food and agriculture (including manufacturing, processing, and storage) industries communicating with KAMACITE’s C2 infrastructure.

In March of 2022, Dragos analyzed new CYCLOPS BLINK samples that appeared in the wild.⁵ Based on this analysis, Dragos discovered new C2 infrastructure associated with KAMACITE’s CYCLOPS BLINK operations. Dragos identified a set of hosting provider-owned IP addresses, which host domains for organizations in the rail, aerospace, food & beverage, and automotive sectors, along with three U.S. Government IP addresses communicating with this new CYCLOPS BLINK C2 infrastructure.

Dragos assesses with moderate confidence that this was scanning activity to identify vulnerable target devices.

In April of 2022, the U.S. Department of Justice (DOJ) released a public notice that stated that through March of 2022, the U.S. DOJ had been copying and removing malware from vulnerable firewall devices, which were being used for C2 CYCLOPS BLINK operations.

⁴ https://www.ncsc.gov.uk/news/joint-advisory-shows-new-sandworm-malware-cyclops-blink-replaces-vpnfilter
⁵ https://portal.dragos.com/#/products/AA-2022-15

In May of 2022, KAMACITE targeted routers and IP cameras for initial network access to environments as early as March 2022. These devices were different from devices targeted in the CYCLOPS BLINK campaign. Dragos discovered victims throughout Ukraine and worldwide, including a victim in the food and beverage sector.

Based on past activities and renewed activities in 2022, Dragos assesses with moderate confidence that KAMACITE will continue to conduct reconnaissance and C2 operations.

#### KAMACITE

- **ADVERSARY**: Overlaps with SANDWORM activity⁶; Custom malware development & deployment; also known to modify third party criminal malware
- **CAPABILITIES**: Phishing & credential replay for initial access; Custom malware development & deployment; also known to modify third party criminal malware
- **VICTIMS**: Europe, including Ukraine, and U.S.
- **INFRASTRUCTURE**: Primary focus on compromised infrastructure in Europe; Spoofs legitimate technology & social media services
- **ICS IMPACT**: Operations linked to five ICS targeting events; Proven operations leading to disruption; Facilitated the 2015 and 2016 Ukraine power events

⁶ https://www.mandiant.com/resources/blog/ukraine-and-sandworm-team

#### XENOTIME

The Dragos-tracked threat group XENOTIME is one of the four (including CHERNOVITE, ELECTRUM, and KAMACITE) publicly known threat groups that has the intent, motivation, and capability to target and disrupt or destroy critical infrastructure, particularly in the ONG sector.

During 2022, Dragos observed XENOTIME reconnaissance and research activity focused on oil and natural gas (ONG) and liquefied natural gas (LNG) entities in the U.S., including component manufacturers that support ONG operations.

XENOTIME is the only threat group that has demonstrated the ability to compromise and disrupt industrial safety instrumented systems (SIS), which can lead to environmental damage, loss of containment, loss of control, and loss of life.

Dragos is aware of extensive XENOTIME research activity focused on LNG compressor train processes, LNG terminal ports, offshore production sites, and emergency response organizations for ONG, as well as onshore production sites around shale gas and midstream organizations.

Dragos has not observed any indication that XENOTIME is currently conducting active exploitation or compromise operations against ONG or LNG organizations. However, XENOTIME’s ongoing activities represent a significant increase in future risk to the LNG and ONG sectors.

Dragos assesses with low confidence XENOTIME’s ultimate goal is causing a loss of containment for environmental impact, which would delay operations or potentially shut down an LNG export terminal. Currently, XENOTIME is in the development phase of offensive cyber operations, most likely focusing on capability and infrastructure development.

#### XENOTIME

- **ADVERSARY**: Unique tool development
- **CAPABILITIES**: TRISIS; Custom credential harvesting; Off-the-shelf tools
- **VICTIMS**: Oil and gas, electric utilities; Middle East, North America
- **INFRASTRUCTURE**: Virtual Private Server and compromised, legitimate infrastructure; European web hosting providers; Asian shipping company
- **ICS IMPACT**: Demonstrated capability to execute disruptive ICS attack, such as the 2017 TRISIS incident

#### ELECTRUM

ELECTRUM is still active in 2022 and continues to develop and modify capabilities against electric grid operations.

In April 2022, Dragos learned of a series of recent public security announcements from the Slovakian security firm ESET, which identified multiple malware capabilities uncovered at a Ukrainian utility provider. Dragos assesses with moderate confidence that the threat group behind this 2022 attack was ELECTRUM, marking the third time ELECTRUM had attacked a Ukrainian utility provider. While the execution of a successful industrial control systems (ICS) attack was prevented, years earlier ELECTRUM’s malware was also used to attack a Ukrainian ICS electric grid in 2016.⁷

In the April 2022 incident, ELECTRUM deployed INDUSTROYER2 malware along with a set of wiper malware. The wiper malware deployed with INDUSTROYER2 was used to cover ELECTRUM’s tracks.

Dragos assesses with high confidence that ELECTRUM will continue to target electric utilities in Ukraine. ELECTRUM also has the capability to target electric entities outside of Ukraine because of the similar equipment and protocols in other electric environments.

⁷ https://www.dragos.com/threat/electrum/
⁸ https://www.mandiant.com/resources/blog/ukraine-and-sandworm-team

#### ELECTRUM

- **ADVERSARY**: Overlaps with SANDWORM activity⁸; Unique RAT & malicious wiper modules
- **CAPABILITIES**: Unique RAT & malicious wiper modules
- **VICTIMS**: Electric sector; Europe, including Ukraine
- **INFRASTRUCTURE**: Leveraged servers hosting many additional services such as Tor
- **ICS IMPACT**: Executed control system portion of 2016 Ukraine power event, deployed CRASHOVERRIDE designed to manipulate electric transmission equipment

##### INDUSTROYER2

INDUSTROYER2 is the sixth known ICS-specific malware; however, the April 2022 incident marked the first time ICS-specific malware had been reconfigured and then redeployed in an electric utility environment, which was also impacted by CRASHOVERRIDE in 2016.

INDUSTROYER2 utilizes the International Electrotechnical Commission (IEC) IEC-104 protocol to control and communicate with industrial equipment. INDUSTROYER2 is a new variant of CRASHOVERRIDE with fewer capabilities. The 2016 CRASHOVERRIDE malware had a modular framework and multiple components, including a 104 module that utilized the IEC 104 protocol for communicating with industrial equipment.

This module is designed to leverage the IEC 104 protocol to change the state of Information Object Addresses (IOA) to switch physical breaker statuses from open to closed or vice versa, causing disruptive effects. The targeted substations and IOA information contained within the configuration information indicate that ELECTRUM had a detailed understanding of the victim’s environment before deploying INDUSTROYER2.

#### ELECTRUM’s 2016 Attack

Looking back at ELECTRUM’s history, the second attack on the Ukrainian power grid occurred in December of 2016, causing a power grid outage in Kyiv that turned off the lights for a quarter million Ukrainians. It was a significant incident that blacked out a portion of the city’s electricity for about an hour. Dragos’s assessment of the events determined that at least two threat groups – KAMACITE and ELECTRUM – combined their efforts to execute this ICS attack.

In the 2016 attack, ELECTRUM used malware designed to attack industrial control systems (ICS) called CRASHOVERRIDE. However, unlike CRASHOVERRIDE, which had multiple components, INDUSTROYER2, used in April 2022, only utilizes the International Electrotechnical Commission (IEC) IEC-104 protocol to communicate with its industrial equipment targets.

#### ERYTHRITE

During 2022, ERYTHRITE continued to compromise industrial organizations across multiple sectors in North America with its adaptable search engine optimization (SEO) poisoning and custom, rapidly redeveloped malware. ERYTHRITE has a consistent ability to develop and deploy malware and infrastructure at scale.

While ERYTHRITE has not demonstrated any ICS-specific capabilities, ERYTHRITE poses a persistent and active threat to industrial organizations when you consider the volume of its activity, its focus on data and credential theft during its post-compromise activities, and its affiliation with the cybercriminal ecosystem. ERYTHRITE is a particular threat to organizations where poor ICS/OT network segmentation and network visibility have created a vulnerable environment.

Since 2021, Dragos has observed ERYTHRITE compromise the OT environment of a Fortune 500 manufacturer, the IT environments of two large electrical utilities, large food and beverage companies, auto manufacturers, IT service providers, and multiple oil and natural gas (ONG) service firms.

#### ERYTHRITE

- **ADVERSARY**: Overlap with group known as Solarmaker
- **CAPABILITIES**: Search Engine Optimization (SEO) poisoning; bespoke, rapidly refashioned low detection credential stealing and remote access malware
- **VICTIMS**: U.S., Canada; ~20% of Fortune 500 companies; Large Electric Utility; Electronic agreement and document signature company
- **INFRASTRUCTURE**: C2 and management in Russia, reverse proxies in North America and Europe, hundreds of thousands of vulnerable but otherwise legitimate websites abused for SEO poisoning
- **ICS IMPACT**: Credentials, sensitive information, and remote access to OT environments potentially sold to illicit third parties

#### WASSONITE

Since 2018, the Dragos-tracked threat group WASSONITE has targeted industrial control systems (ICS) entities in the nuclear energy, electric, oil and gas, advanced manufacturing, pharmaceutical, and aerospace industries predominately in South and East Asia, with some additional targets in North America. WASSONITE’s operations have demonstrated a repeated ability to achieve initial Stage 1 activity defined by the ICS Cyber Kill Chain.

In October 2022, Dragos analyzed WASSONITE’s use of nuclear energy-themed spear phishing lures written in Hangul to deliver the AppleSeed backdoor. The Appleseed backdoor is a multi-component backdoor that can take screenshots, log keystrokes, and collect removable media information and specific victim files. It can also upload, download, and execute follow-on commands from a command and control (C2) server.

WASSONITE’s use of spear phishing lures with content and titles highly targeted toward nuclear energy in East Asia is consistent with WASSONITE’s enduring, long-term interest in targeting organizations in this industry. Dragos’s analysis of the malicious files and the adversary’s infrastructure led to the identification of additional samples and domains associated with this campaign.

WASSONITE’s continued deployment of customized variants of the AppleSeed backdoor throughout 2021 and 2022 represented a shift in capabilities away from the previous use of customized variants of DTrack malware.

The WASSONITE activity group leverages spear phishing lures, often customized for specific industries and organizations, as their initial infection vector. WASSONITE malware variants also display highly targeted modifications for individual environments, including hard-coded credentials, non-public internet protocol (IP) addresses, and uncommon ports for specific applications.

Dragos assesses with moderate confidence that WASSONITE will continue to target ICS entities in nuclear energy, electric, oil and gas, advanced manufacturing, pharmaceutical, and aerospace industries in East Asia, South Asia, and North America.

⁹ https://www.dragos.com/threat/covellite/

#### WASSONITE

- **ADVERSARY**: Limited technical overlaps to COVELLITE⁹ and the cluster of activities tracked by other organizations as Kimsuky
- **CAPABILITIES**: Customized variants of the DTrack and Appleseed RATs; Mimikatz and system tools for lateral movement and file transfers
- **VICTIMS**: Nuclear energy, electric, oil and gas, advanced manufacturing, pharmaceutical, and aerospace industries; South/East Asia and North America
- **INFRASTRUCTURE**: Adversary-registered and controlled domains & infrastructure for C2; Use of compromised, legitimate services in some instances
- **ICS IMPACT**: Focus on targeting ICS-related organizations; Focus on network actions consistent with information gathering, including from protected network segments