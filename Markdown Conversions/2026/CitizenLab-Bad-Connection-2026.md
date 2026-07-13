# Bad Connection: Uncovering Global Telecom Exploitation by Covert Surveillance Actors

## Table of Contents
- [Key Findings](#key-findings)
- [Introduction](#introduction)
- [Methods](#methods)
- [Background: Continued Broken Trust in Mobile Communications](#background-continued-broken-trust-in-mobile-communications)
- [Insecure by Design](#insecure-by-design)
- [Telecom Surveillance Actors: A Crowded and Shadowy Marketplace](#telecom-surveillance-actors-a-crowded-and-shadowy-marketplace)
- [Fingerprinting Telecom Surveillance Actors](#fingerprinting-telecom-surveillance-actors)
- [Gateways to Surveillance](#gateways-to-surveillance)
- [STA1: A Persistent Location Tracking Campaign](#sta1-a-persistent-location-tracking-campaign)
- [STA2: The SIM as the Spy](#sta2-the-sim-as-the-spy)
- [Correspondence](#correspondence)
- [Conclusion](#conclusion)

---

## Key Findings
- **Multi-Vector Surveillance**: We identified actors using multiple techniques to track targets by combining 3G and 4G signalling network protocols with direct device exploitation via SMS.
- **SIM Card Exploitation**: One campaign sent a malicious SMS containing hidden SIM card commands to extract location information, attempting to turn the device into a covert tracking beacon.
- **Sophisticated and Customized Tooling**: Both actors used customized surveillance tooling to spoof operator identities, manipulate signalling protocols, and steer traffic through specific interconnect network paths to evade defenses and mask attribution.
- **Global Network Infrastructure**: The attacks leveraged identifiers and infrastructure associated with operators worldwide, including networks based in the UK, Israel, China, Thailand, Sweden, Italy, Liechtenstein, Cambodia, Mozambique, Uganda, Rwanda, Poland, Switzerland, Morocco, Namibia, Lesotho, and the self-governing Island of Jersey, demonstrating extensive global reach.
- **Persistent Campaign Activity**: Telemetry shared by mobile signalling security provider Cellusys reveals that operator signalling identifiers were reused over multiple years, forming consistent clusters that enabled long-running surveillance operations.
- **Weak Intercarrier Provider OPSEC**: Weak screening of interconnect traffic allowed attackers to route surveillance messages through trusted operator pathways, enabling access to targeted networks.

## Introduction
In recent years, several investigations have exposed vulnerabilities in the mobile telecommunications ecosystem and how government security agencies have exploited them to track targets abroad while roaming. These studies include several Citizen Lab reports, along with work from other researchers. Our work builds on those findings, prompting further research into the structural weaknesses that continue to enable and evolve targeted surveillance.

In late 2024, the Citizen Lab launched an investigation into coordinated location-tracking activity following the identification of a series of unusual events in mobile signalling firewall logs and further intelligence provided by Cellusys. What initially appeared to be an isolated incident targeting a single mobile subscriber led to a broader investigation that uncovered campaigns by two distinct CSVs conducting long-term espionage operations by exploiting the global telecommunications ecosystem.

The first campaign, observed in November 2024, involved a multi-stage effort to track a high-profile mobile subscriber using multiple 3G and 4G networks. Information provided by the targeted user’s network operator indicated that the mobile number belonged to a well-known company executive, further described as a “VVIP.” This context indicated that the user was a high-value surveillance target.

In early 2025, we identified an additional coordinated-tracking event, with the use of a specially formatted SMS message. While technically distinct, both campaigns demonstrated advanced, highly structured, and repeated methods consistent with purpose-built surveillance platforms.

Our collaboration with mobile industry partners enabled a broad investigation using metadata from signalling logs, packet captures, routing data, and other telecommunications sources to trace the methods and origins of advanced surveillance activity. This analysis identified 4G infrastructure associated with operator networks based in Israel, the United Kingdom, and the Channel Islands. Notably, in prior public reporting these same countries have been linked to CSVs targeting mobile users.

Our findings highlight a systemic issue at the core of global telecommunications: operator infrastructure designed to enable seamless international connectivity is being leveraged to support covert surveillance operations that are difficult to monitor, attribute, and regulate. Despite repeated public reporting, this activity continues unabated and without consequence. The continued use of mobile networks, built on a close inter-operator trust model and relied upon by users worldwide, raises broader questions for national regulators, policymakers, and the telecom industry about accountability, oversight, and global security.

## Methods
This report is based on analysis in collaboration with multiple industry firms including the signalling firewall provider Cellusys, international signalling provider Telenor Linx, telecom data intelligence provider Roaming Audit, and telecom network security firm P1 Security.

We validated our research by correlating signalling data with additional independent data sources, enabling analysis of how messages were submitted, routed, and delivered across the global interconnect ecosystem. These sources included:
- Mobile network configurations from mobile operator GSMA (GSM Association) industry filings
- Telecom signalling Domain Name System (DNS) records
- Border Gateway Protocol (BGP) routing data and Autonomous System Number (ASN) registrations
- Publicly available records from national telecommunication regulators

We applied a multi-stage analytical process to attribute observed surveillance activity to distinct threat actors by identifying, clustering, and correlating suspicious signalling indicators across campaigns.

### Analytical Approach
1. **Detection of Suspicious Signalling Activity**: We identified commands in international signalling traffic that match known surveillance techniques across 3G SS7 and 4G Diameter signalling protocols.
2. **Surveillance Campaign Pattern Identification**: We analyzed traffic for repeated commands within short time intervals from individual operator signalling addresses.
3. **Target Validation**: Cellusys validated that each campaign targeted specific subscriber phone identifiers (IMSIs).
4. **Actor Fingerprinting and Clustering**: We identified distinct surveillance actors through technical fingerprinting of signalling characteristics.
5. **Infrastructure Mapping and Routing Analysis**: We correlated signalling identifiers with external data sources to map how attack traffic entered and traversed the signalling interconnect ecosystem.
6. **Historical Correlation**: Our final step was to correlate observed attack indicators with historical telemetry to measure the duration of campaign activity.

## Background: Continued Broken Trust in Mobile Communications
The system connecting mobile operators around the world for international travel and mobile services uses protocols consisting of a blend of SS7, known for older 3G networks, and Diameter for 4G and most 5G networks. While SS7 has long been considered a legacy protocol, it still maintains a critical role for international roaming, SMS, and emergency services. Together, this blended signalling ecosystem of vulnerable protocols creates additional opportunities for surveillance actors.

## Insecure by Design
The root of the security problem lies in the foundational signalling protocols themselves. Designed for a trusted community of mobile operators and legitimate third-party service providers, SS7 protocols lack the basic security mechanisms of IP networks, such as authentication and validation to verify the source of signalling messages, integrity checks to ensure that data has not been altered, and encryption to protect its contents.

The Diameter protocol, currently used in 4G and most 5G international roaming implementations, was designed with stronger security controls than SS7, introducing security components to address inherent signalling vulnerabilities.[^1] However, in practice, operators have largely failed to implement these protections and instead continue to rely on the same peer-to-peer trust model that plagues SS7.

[^1]: GSMA Document FS.19 Diameter Interconnect Security, Annex D Diameter IPX Network End-to-End Security Solution

### What is IR.21?
IR.21 is a document specification shared among mobile operators through the GSMA. It contains technical and operational details about an operator’s network, such as network codes, signalling address ranges and network assignments, interconnect details, and other information for managing international roaming services. Attackers with knowledge of IR.21 data can exploit it to identify network elements or create signalling messages that appear legitimate within the global telecommunication ecosystem.

![Figure 1: Combined Attach Surveillance Vulnerability]

## Telecom Surveillance Actors: A Crowded and Shadowy Marketplace
The telecom surveillance ecosystem is composed of two overlapping groups: state-linked espionage services that conduct signals intelligence operations through telecom networks, and CSVs that develop and sell interception and tracking services to government clients.

| Affiliation | Actor | Reported Telecom Surveillance Activity |
| :--- | :--- | :--- |
| State-Sponsored | Salt Typhoon | China Ministry of State Security (MSS) |
| State-Sponsored | Liminal Panda | China-Nexus Espionage Actor |
| State-Sponsored | MuddyWater | Iran Ministry of Intelligence and Security (MOIS) |
| Commercial | Circles, Cognyte, Rayzone, Defentek | Various |
| Commercial | RCS Lab / Tykelab | Italy |
| Commercial | Fink Telecom Services (FTS) | Switzerland |
| Commercial | Rayzone Group | Israel |

## Fingerprinting Telecom Surveillance Actors
To distinguish the surveillance campaigns identified in this investigation, we analyzed recurring indicators in the signalling traffic and historical attack telemetry.

1. **Manipulation of Signalling Identifiers**: Both actors manipulated signalling identifiers embedded in the attack messages to obscure the true origin of the traffic.
2. **Ordered SS7 Transaction Identifiers (TIDs)**: Location queries used near-sequential TIDs for surveillance messages across different SS7 networks.
3. **Non-Standard Diameter Session Identifiers**: Session ID values from both actors deviated from 3GPP Diameter standards.
4. **Identical Commands Across Networks**: Commands seen in the attack messages used identical parameters across multiple networks.

![Figure 3: Identical SS7 message parameters]
![Figure 4: Identical diameter message parameters]

## Gateways to Surveillance
The investigations in this report expose three mobile networks that repeatedly appear as the surveillance entry and transit points:
- **019Mobile (Israel)**: Repeatedly appears in Diameter surveillance attempts as an originating network and intermediary node.
- **Airtel Jersey/Sure (Channel Islands)**: An Airtel Jersey node was seen as the first hop for Diameter signalling surveillance queries.
- **Tango Networks UK**: A Diameter hostname with the Tango Networks MNC053/MCC 234 signalling identifier was used as a second entry point for 4G location tracking queries.

## STA1: A Persistent Location Tracking Campaign
We identify the first threat actor in this investigation as STA1, a persistent and technically sophisticated telecom surveillance group.

### The Chronology Of A Multi-Stage Location Tracking Campaign
On November 25, 2024, a sequence of signalling messages targeted a subscriber of a Middle East mobile operator. The attack involved five phases, ranging from initial reconnaissance via SS7 to protocol switching to 4G/Diameter and final manipulation of routing paths.

![Figure 5: Signalling network paths exploited by STA1]

## STA2: The SIM as the Spy
*(Content omitted in source text)*

## Correspondence
*(Content omitted in source text)*

## Conclusion
The findings in this report demonstrate that the global telecommunications ecosystem remains fundamentally insecure. The ability of surveillance actors to leverage legitimate operator infrastructure to conduct covert, long-term tracking operations highlights a critical failure in the oversight and security of international mobile roaming. Without significant reform in how signalling traffic is authenticated, screened, and regulated, these surveillance campaigns will continue to pose a persistent threat to global security and individual privacy.

---

atterns are consistent with a CSV leveraging a centralized, cloud-based C2 platform
offered to multiple clients, we analyzed operator information and routing metadata through
collaboration with mobile industry partners.
1. Use of AIS Thailand Hostname Formats and an IR.21-Listed Node
Surveillance activity associated with 019Mobile consistently used the AIS Thailand hostname format
ideabpl1h. In its most sophisticated tracking attempt, STA1 configured an AIS Thailand Diameter Edge
Agent (DEA) node (see Figure 6), typically used for inter-operator routing and topology hiding, while
configuring the Origin-Realm as belonging to China Unicom. This combination indicates detailed
knowledge of operator infrastructure, interconnection relationships, and access to GSMA IR.21 data.
Such capabilities are consistent with a sophisticated commercial telecom surveillance operation.
Figure 6: DEA hostname published in the AIS Thailand IR.21 Document.
2. Repeated Campaign Activity
Another surveillance campaign shown in Figure 7 captured by Cellusys from March 2025 shows multiple
location tracking attempts spoofing a China Unicom Origin-Host
dex01.epc.mnc001.mcc460.3gppnetwork.org with the same 019Mobile Israel Route-Record seen
in the November 2024 attack.
26

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
Figure 7: Repeated tracking attempts spoofing China Unicom with an 019Mobile network host.
3. Long-Running Campaign Activity
Historical telemetry reveals a long-running activity using the same hostname formats and identifiers
from multiple operators dating back to at least November 2022, as shown in Table 8. The use of similar
hostnames associated with multiple network operators over long durations is consistent with address
spoofing designed to hide attack origin. The telemetry reveals these hostnames used in over 500
location tracking attempts.
Date Origin Host Operator Origin Host Threat Type Operation
Address Country
9-Nov-22 dex01.epc.mnc00 SUNRISE Switzerland Location Discovery Insert-Subscriber-Dat
2.mcc228.3gppne SWITZERLAND a-Request
twork.org
9-Nov-22 dex01.epc.mnc00 KOLBI COSTA Costa Rica Location Discovery Insert-Subscriber-Dat
1.mcc712.3gppne RICA a-Request
twork.org
9-Nov-22 dex01.epc.mnc00 PLUS POLAND Poland Location Discovery Insert-Subscriber-Dat
1.mcc260.3gppne a-Request
twork.org
1-Mar-23 cst001.epc.mnc05 TANGO United Kingdom Location Discovery Insert-Subscriber-Dat
3.mcc234.3gppne NETWORKS UK a-Request
twork.org
2-Mar-23 cst001.epc.mnc05 TANGO United Kingdom Location Discovery Insert-Subscriber-Dat
3.mcc234.3gppne NETWORKS UK a-Request
twork.org
22-Mar-23 cst001.epc.mnc05 TANGO United Kingdom Location Discovery Insert-Subscriber-Dat
3.mcc234.3gppne NETWORKS UK a-Request
twork.org
30-Mar-23 dex01.epc.mnc01 019MOBILE Israel Location Discovery Insert-Subscriber-Dat
9.mcc425.3gppne a-Request
twork.org
27

CITIZEN LAB REPORT NO. 192  |  BAD CONNECTION

30-Mar-23  cst001.epc.mnc05 TANGO  United Kingdom  Location Discovery  Insert-Subscriber-Dat
| 3.mcc234.3gppne | NETWORKS UK  |     | a-Request  |
| --------------- | ------------ | --- | ---------- |
twork.org
30-Aug-23  cst001.epc.mnc05 TANGO  United Kingdom  Location Discovery  Insert-Subscriber-Dat
| 3.mcc234.3gppne | NETWORKS UK  |     | a-Request  |
| --------------- | ------------ | --- | ---------- |
twork.org
18-Sep-23  cst001.epc.mnc05 TANGO  United Kingdom  Location Discovery  Insert-Subscriber-Dat
| 3.mcc234.3gppne | NETWORKS UK  |     | a-Request  |
| --------------- | ------------ | --- | ---------- |
twork.org
20-Sep-23  dex01.epc.mnc01 019MOBILE  Israel  Location Discovery  Insert-Subscriber-Dat
| 9.mcc425.3gppne |     |     | a-Request  |
| --------------- | --- | --- | ---------- |
twork.org
20-Sep-23  dex01.epc.mnc00 CHINA UNICOM  China  Location Discovery  Insert-Subscriber-Dat
| 1.mcc460.3gppne |     |     | a-Request  |
| --------------- | --- | --- | ---------- |
twork.org
26-Sep-23  dex01.epc.mnc01 019MOBILE  Israel  Location Discovery  Insert-Subscriber-Dat
| 9.mcc425.3gppne |     |     | a-Request  |
| --------------- | --- | --- | ---------- |
twork.org
26-Sep-23  cst001.epc.mnc05 TANGO  United Kingdom  Location Discovery  Insert-Subscriber-Dat
| 3.mcc234.3gppne | NETWORKS UK  |     | a-Request  |
| --------------- | ------------ | --- | ---------- |
twork.org
26-Sep-23  dex01.epc.mnc01 019MOBILE  Israel  Communications  Authentication-Infor
| 9.mcc425.3gppne |     | Intercept  | mation-Request  |
| --------------- | --- | ---------- | --------------- |
twork.org
26-Sep-23  st001.epc.mnc05 TANGO  United Kingdom  Communications  Authentication-Infor
| 3.mcc234.3gppne | NETWORKS UK  | Intercept  | mation-Request  |
| --------------- | ------------ | ---------- | --------------- |
twork.org
27-Sep-23  dex01.epc.mnc01 019MOBILE  Israel  Location Discovery  Insert-Subscriber-Dat
| 9.mcc425.3gppne |     |     | a-Request  |
| --------------- | --- | --- | ---------- |
twork.org
27-Sep-23  cst001.epc.mnc05 TANGO  United Kingdom  Location Discovery  Insert-Subscriber-Dat
| 3.mcc234.3gppne | NETWORKS UK  |     | a-Request  |
| --------------- | ------------ | --- | ---------- |
twork.org
10-Dec-23  st001.epc.mnc05 TANGO  United Kingdom  Location Discovery  Insert-Subscriber-Dat
| 3.mcc234.3gppne | NETWORKS UK  |     | a-Request  |
| --------------- | ------------ | --- | ---------- |
twork.org
10-Dec-23  dex01.epc.mnc01 019MOBILE  Israel  Location Discovery  Insert-Subscriber-Dat
| 9.mcc425.3gppne |     |     | a-Request  |
| --------------- | --- | --- | ---------- |
twork.org
11-Dec-23  dex01.epc.mnc00 CHINA UNICOM  China  Location Discovery  Insert-Subscriber-Dat
| 1.mcc460.3gppne | MOBILE  |     | a-Request  |
| --------------- | ------- | --- | ---------- |
twork.org
28

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
14-Dec-23 cst001.epc.mnc05 TANGO United Kingdom Location Discovery Insert-Subscriber-Dat
3.mcc234.3gppne NETWORKS UK a-Request
twork.org
8-Jan-24 cst001.epc.mnc05 TANGO United Kingdom Location Discovery Insert-Subscriber-Dat
3.mcc234.3gppne NETWORKS UK a-Request
twork.org
8-Jan-24 dex01.epc.mnc00 SMARTONE Hong Kong, SAR Location Discovery Insert-Subscriber-Dat
6.mcc454.3gppne a-Request
twork.org
Table 8: History of STA1 Attacks
Note: The table shows a limited sample of historical attacks from over 500 threat events recorded as
attributed to STA1 since November 2022.
4. Global Targeting Patterns
Beyond the initial targeting of a high-profile user in the Middle East, we identified surveillance activity
across a wide geographic range. Targets included individual mobile subscribers associated with
operators in Thailand, South Africa, Norway, Bangladesh, Denmark, Sweden, Malaysia, Montenegro, and
multiple countries across Sub-Saharan Africa. The single user targeting across multiple operator
networks and country jurisdictions persisting for years is characteristic of a commercial surveillance
platform deployed across multiple operators and likely used by multiple global clients.
5. DNS Validation of Operator-Controlled Signalling Infrastructure
We analyzed IPX DNS records to determine the authoritative operators associated with domains seen in
attack traffic. The Tango Networks hostname cst001.epc.mnc053.mcc234.3gppnetwork.org
resolved successfully via authoritative IPX DNS, confirming it as a valid operator-controlled hostname
consistent with Tango Networks IR.21 records. Its repeated use in surveillance activity suggests that
STA1 maintained long-term access to Tango Networks infrastructure, likely through a commercial
arrangement.
However, analysis of 019Mobile yielded different results. The domain
epc.mnc019.mcc425.3gppnetwork.org consistently returned NXDOMAIN responses across multiple
IPX DNS servers, indicating the domain did not exist, or was deliberately suppressed from the IPX root
DNS environment. This suggests a possible technique to hide the discovery of 019Mobile IP addresses
attributed to signalling hosts transporting surveillance traffic. To further investigate whether 019Mobile
infrastructure was reachable via Diameter signalling, we looked for additional network data.
In the absence of DNS resolution, we examined whether any 019Mobile IP networks were advertised
within the IPX. We found two IP address ranges and the corresponding Autonomous System Number
(ASN 51825) listed in IR.21 filings from the Israeli-based operator Partner Communications.
29

CITIZEN LAB REPORT NO. 192  |  BAD CONNECTION

GRX/IPX Routing for Data Roaming
Connection to Inter-PMN IPv4 Backbone

| IP Address(Range)  | IPX VLAN  |   Network Owner  |
| ------------------ | --------- | ---------------- |

| 185.24.204.0/29  | Data-Roaming   | MNO  |
| ---------------- | -------------- | ---- |
| 185.24.204.8/29  | Data-Roaming   | MNO  |

Autonomous System Numbers (ASN)

| ASN    Network Owner  |     |     |
| --------------------- | --- | --- |
| 51825   MNO           |     |     |

ASN 51825 is the unique network identifier registered to “Telzar 019 International Telecommunications
Services LTD,” the parent company of 019Mobile as shown in Figure 8.

30

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
Figure 8: 019Mobile IP network and ASN attribution.
31

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
This IR.21 association indicates that Partner Communications acts as an upstream signalling
interconnect provider for 019Mobile, but raises a critical question: If the 019Mobile network domain
does not exist in the IPX, is the underlying infrastructure still reachable within the signalling ecosystem?
To validate this, we analyzed BGP routing information obtained from within the IPX backbone. The
results confirmed that the 019Mobile IP prefixes are actively advertised and reachable via Partner
Communications, showing a verifiable routing path into and out of the Diameter signalling ecosystem.
The BGP routing path was:
AS Path: → 12400 → 51825
This shows that signalling traffic destined for 019Mobile (AS51825) is routed through an intermediary
network belonging to Partner Communications (AS12400) before reaching its point of origin. The
presence of the Partner network in the routing path confirms that 019Mobile infrastructure is reachable
through an established interconnect relationship. Additional routing attributes show that the path is
valid, externally learned, and selected as the best route in the routing table:
Origin: IGP | localpref: 100 | valid, external, best
This confirms that, despite the absence of the 019Mobile domain from authoritative IPX DNS records,
surveillance traffic entering and exiting through this network can be routed and delivered while
remaining hidden from DNS discovery. While we don’t believe that 019Mobile conducted the attacks, the
evidence indicates that its network and Partner Communications were likely used as a transit path for
surveillance traffic.
Our findings described above provide insight into the methods used by STA1 to operate within the global
signalling ecosystem while limiting attribution. Across both SS7 and Diameter, routing manipulation,
path obfuscation, and signalling identifiers associated with multiple operators were used to deliver
surveillance traffic. These approaches used over several years indicate a high degree of persistence,
sophistication and coordination. The global distribution of targets and infrastructure suggests a system
designed for multiple tenants, consistent with a commercially developed telecom surveillance platform
supporting government intelligence activities. While at this time we do not attribute this campaign to a
specific actor, the evidence shows a deliberate and well-funded operation with deep integration into the
mobile signalling ecosystem.
STA2: The SIM as the Spy
Our second investigation, attributed to what we refer to as Surveillance Threat Actor 2 (STA2), used
different mobile surveillance techniques. Instead of manipulating SS7 and Diameter signalling protocols
for location tracking, STA2 combined device-level exploitation with network-level attacks.
32

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
Through detailed analysis of logs and a packet trace showing the header contents of the SMS message,
we identified that STA2 sent a specially formatted binary SMS with embedded commands. This was seen
during the attack sequence described in this section.
The message was designed to trigger a silent SIM-based exploit without requiring any user interaction,
with commands to turn the phone into a location tracking device. We linked the binary payload to a long
running campaign likely affecting thousands of devices, known as SIMjacker. Originally exposed by ENEA
in 2019, SIMjacker is a Zero-Click SMS exploit that invokes a hidden SIM card application called the S@T
browser. The S@T browser is a SIM toolkit (STK) application that interprets S@T bytecode and provides
access to STK commands. STK applications are used by mobile operators for service provisioning,
operator phone settings, and other value-added services. In this case, STA2 sent a command instructing
the STK to retrieve the device location and send it back in a silent SMS message to the attacker
infrastructure.
ENEA stated that SIMjacker “is currently being actively used by a specific private company that works
with governments to monitor individuals.” While ENEA did not name the company, the Citizen Lab has
linked the attack sources to SS7 addresses from mobile operators based in Rwanda, Sweden, and
Liechtenstein. This attack is a continuation of the SIMjacker threat, where the user’s SIM card becomes
the sensor and spy, using SMS messages for C2 communication.
How Can an SMS Control a Phone SIM?
SIM toolkit messages (aka SIM OTA messages) look nothing like normal text messages; your phone
never shows them and users have no way to know they were received, as they are used by network
operators to configure device network settings. Two fields inside the SMS header make this possible:
TP-PID = 127 - “This message is for the SIM card, not the user.”
Attackers use this to instruct the device to do the following:
● Don’t display the message
● Don’t store it in the inbox
● Deliver it to the SIM card for execution
TP-DCS = 22 (0x16) - “Treat this as binary code and send it straight to the SIM.”
This ensures the malicious code embedded in the SMS can be recognized and the instructions run by
the SIM.
● The message contains binary commands
● The instructions should be processed by the device SIM
● The device messaging app shouldn’t touch the message contents
33

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
A Different Modus Operandi
STA2 signatures are very different from STA1. On February 11, 2025, STA2 attempted a location tracking
operation using a sequential approach, combining network and device attack vectors. The attack began
with basic SS7 reconnaissance and location tracking attempts, escalated to a SIM exploit, and ended
with Diameter location tracking queries. The messages in our analysis, detailed in the following attack
sequence, were captured from firewall telemetry, flagged, and blocked by the signalling firewall listed in
Table 9.
Phase 1 – Testing the SS7 Waters (15:41 GMT)
The attack began with a single SS7 PSI message from GT 467647531812. This was likely used to probe
the target network to see if it would process a basic location tracking request and confirm if the target
phone was connected to the network.
Phase 2 – Weaponizing SMS (15:45 GMT)
Minutes later, the same GT sent an SS7 Mobile-Terminated Forward Short Message (mt-ForwardSM)
carrying a binary payload. This message delivered the SIM exploit.
Phase 3 – Cross-Protocol Camouflage (15:46 – 15:50 GMT)
After the SIM exploit was blocked, the actor pivoted to Diameter and launched a series of
Authentication-Information-Request (AIR) probing messages, followed by IDR location queries.
● Network Probing Using Fake Registration: The actor sent 10 AIR messages populated with the
IMSI of the target phone using 5 different operator network identifiers. The messages are
configured with an invalid Visited-PLMN Id = 0000. The AIR message is normally used to
establish a new phone connection and report the roaming Mobile Country Code (MCC) and
Network Code (MNC) values in the Visited-PLMN ID. In this case, the actor was not trying to
connect but used a malformed PLMN value to probe the security of the targeted network and
influence a successful response for follow-on location tracking attempts.
● Follow-on Location Tracking: The actor then sent a series of IDR location queries using network
identifiers from 3 different countries, with each Diameter IDR message flag set to retrieve the
current network state and cell id location of the target phone.
● Hostname and Routing Path Manipulation: The actor used a single, fixed host populated in the
Route-Record to direct the path of surveillance traffic to the operator exit path, using two
different hostname formats to identify the type of commands used in the attack.
● Spoofed Networks: Diameter messages used network identifiers originating from Poland (Plus),
Switzerland (Sunrise), Morocco (INWI), Lesotho (Econet), Namibia (MTC), and Mozambique
(Movitel), indicating the actor’s misuse of international signalling identities from multiple
operators.
34

CITIZEN LAB REPORT NO. 192  |  BAD CONNECTION

Timestamp  Protocol  Signalling  Source Node  Source  Source  Threat
|           |      | Operation     |             | Network  | Country  | Type      |
| --------- | ---- | ------------- | ----------- | -------- | -------- | --------- |
| 2/11/25   | SS7  | begin,        | 46764753181 | TELE2    | Sweden   | Location  |
| 15:41:33  |      | provideSubscr | 2           |          |          | Tracking  |
iberInfo
| 2/11/25   | SS7  | begin,      | 46764753181 | TELE2  | Sweden  | Binary SMS  |
| --------- | ---- | ----------- | ----------- | ------ | ------- | ----------- |
| 15:45:29  |      | mt-ForwardS | 2           |        |         |             |
M
2/11/25  Diameter  Authenticatio hss1.epc.mnc PLUS  Poland  Malformed
| 15:55:01  |     | n-Information | 001.mcc260.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Authenticatio hss1.epc.mnc PLUS  Poland  Malformed
| 15:55:06  |     | n-Information | 001.mcc260.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Authenticatio hss1.epc.mnc SUNRISE  Switzerland  Malformed
| 15:55:28  |     | n-Information | 002.mcc228.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Authenticatio hss1.epc.mnc SUNRISE  Switzerland  Malformed
| 15:55:33  |     | n-Information | 002.mcc228.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Authenticatio hss1.epc.mnc INWI   Morocco  Malformed
| 15:55:50  |     | n-Information | 002.mcc604.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Authenticatio hss1.epc.mnc INWI  Morocco  Malformed
| 15:55:50  |     | n-Information | 002.mcc604.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Authenticatio hss1.epc.mnc ECONET  Lesotho  Malformed
| 16:05:24  |     | n-Information | 002.mcc651.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
35

CITIZEN LAB REPORT NO. 192  |  BAD CONNECTION

2/11/25  Diameter  Authenticatio hss1.epc.mnc ECONET  Lesotho  Malformed
| 16:05:28  |     | n-Information | 002.mcc651.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Authenticatio hss1.epc.mnc MTC  Namibia  Malformed
| 16:05:36  |     | n-Information | 001.mcc649.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Authenticatio hss1.epc.mnc MTC  Namibia  Malformed
| 16:05:41  |     | n-Information | 001.mcc649.3  |     |     | Message  |
| --------- | --- | ------------- | ------------- | --- | --- | -------- |
|           |     | -Request      | gppnetwork.or |     |     |          |
g
2/11/25  Diameter  Insert-Subscri hss.epc.mnc0 ECONET  Lesotho   Location
| 16:06:37  |     | ber-Data-Req | 02.mcc651.3g   |     |     | Discovery  |
| --------- | --- | ------------ | -------------- | --- | --- | ---------- |
|           |     | uest         | ppnetwork.org  |     |     |            |
2/11/25  Diameter  Insert-Subscri hss.epc.mnc0 ECONET  Lesotho   Location
| 16:06:43  |     | ber-Data-Req | 02.mcc651.3g   |     |     | Discovery  |
| --------- | --- | ------------ | -------------- | --- | --- | ---------- |
|           |     | uest         | ppnetwork.org  |     |     |            |
| …         | …   | …            | …              | …   | …   | Location   |
Discovery
2/11/25  Diameter  Insert-Subscri hss.epc.mnc0 MTC  Namibia   Location
| 16:07:31  |     | ber-Data-Req | 01.mcc649.3g   |     |     | Discovery  |
| --------- | --- | ------------ | -------------- | --- | --- | ---------- |
|           |     | uest         | ppnetwork.org  |     |     |            |
2/11/25  Diameter  Insert-Subscri hss.epc.mnc0 MTC  Namibia   Location
| 16:07:36  |     | ber-Data-Req | 01.mcc649.3g   |     |     | Discovery  |
| --------- | --- | ------------ | -------------- | --- | --- | ---------- |
|           |     | uest         | ppnetwork.org  |     |     |            |
| …         | …   | …            | …              | …   | …   | …          |
2/11/25  Diameter  Insert-Subscri hss.epc.mnc0 MOVITEL  Mozambique   Location
| 16:12:32  |     | ber-Data-Req | 03.mcc643.3g   |     |     | Discovery  |
| --------- | --- | ------------ | -------------- | --- | --- | ---------- |
|           |     | uest         | ppnetwork.org  |     |     |            |
2/11/25  Diameter  Insert-Subscri hss.epc.mnc0 MOVITEL  Mozambique   Location
| 16:12:37  |     | ber-Data-Req | 03.mcc643.3g   |     |     | Discovery  |
| --------- | --- | ------------ | -------------- | --- | --- | ---------- |
|           |     | uest         | ppnetwork.org  |     |     |            |

Table 9: Attack Sequence for STA2 (February 11, 2025).
Note: Table is abridged for brevity. Ten additional IDR attempts ECONET, MTC, and MOVITEL, are
detailed in the full log data.
36

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
Technical Fingerprints
Several recurring indicators were used by STA2 that helped cluster related activity over time.
1. IMSI Embedded in the Diameter Message Session-ID field
The IMSI of the target device was hardcoded into the Session-ID field. This signature links attack
messages directly to the target, suggesting customized tooling with poor OPSEC. We observed
this signature used in this attack and in future attacks extending from 2025 into the early 2026
timeframe.
2. Hostname Conventions Used to Label the Diameter Message Command Code Field
Hostname formats identified the type of signalling message sent. This naming convention
suggests the hostnames were used as internal labels to distinguish surveillance queries.
● hss1 hostnames were used for AIR probing messages
● hss hostnames were used for IDR location query messages
3. Fixed Entry Path Through the Jersey-Airtel network
All attacks used the same Route-Record host:
dra1.je211.epc.mnc003.mcc234.3gppnetwork.org. The repeated use of this same host
indicates that STA2 used a single operator network to send surveillance traffic into the IPX
backbone.
Deconstructing the Binary SMS: Inside a SIMjacker Over-the-Air Exploit
Historically, malicious actors have used hidden commands within special types of SMS messages. Our
deconstruction of the binary SMS sent by STA2 provided unique insights into the surveillance operation.
A packet capture and logs from the signalling firewall showed the SMS headers, confirming the message
timestamps. A breakdown of how the attack was deployed and the information elements defined within
the structure of the SMS is shown in Figure 9.
Figure 9: PCAP file of the attack SMS, containing the payload including S@T browser STK commands.
37

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
● TP-Originating Address (TP-OA): 250730091970 identifies the SMS sender phone number
configured by the attacker as belonging to Airtel Rwanda.
● TP-Protocol Identifier (TP-PID): 127 identifies the message for use by a SIM card application.
● TP-Data Coding Scheme (TP-DCS): 22 identifies the message as binary, so the message is not
processed like a regular text SMS.
○ The TP-PID and TP-DCS indicate a SIM toolkit message containing instructions for the
SIM card. This type of SMS is invisible to the user and automatically parsed by the SIM,
without any user interaction.
● TP-User-Data: This field includes the body of the SMS.
SIMjacker attacks exploit a hidden application on the SIM card known as the S@T browser, which is part
of the SIM toolkit (STK). This exploit enables the attacker to hijack the SIM card invisibly without user
interaction. To perform the attack, STA2 sent an SMS with bytecode containing specialized commands
for the S@T browser (see Figure 10). The S@T browser interprets and executes the commands
immediately, as the communication lacks authentication. Consequently, there is no need for the attacker
to send additional messages to authenticate themselves before the S@T browser is ready to receive the
commands. We found that the binary SMS blocked by the firewall clearly matches the structure of S@T
browser commands. It uses a standardized Tag-Length-[Attribute]-Value (TL[A]V) format to encode the
commands and their parameters following the S@T Bytecode specification. The correctly structured
bytecode used by the attacker confirms that it was used as a SIM-level exploit rather than ordinary SMS
traffic.
What is the TL[A]V format?
Data structures in the Tag-Length-[Attribute]-Value (TL[A]V) format consist of four fields: Tag, Length,
Attributes, and Value, whereby the Attributes field is optional.
S@T browser commands use the TL[A]V format, so:
● Every command is identified by a unique one-byte Tag.
● The Tag indicates if the Attribute field is present.
● The Length field specifies how many of the subsequent bytes are part of the command. This
includes the Attributes and the Value field.
● The Attributes determine command-specific parameters.
● The Value field contains the data the command is operating on.
For example, the Init Variable command consists of the Tag 0x20 followed by the Length and Value
fields. The latter contains the ID and content of the initialized variable.
38

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
The payload of the exploit SMS contains a command header with a noticeable byte sequence 0x505348.
This byte sequence represents the Toolkit Application Reference (TAR) indicating a low priority push
message, in reference to step (1) in Figure 10. The low priority push is designed for messages of low
importance without the need for a reply or delivery confirmation. In this way, the messages leave no
traces on the SIM card, as they are dropped if the S@T browser is busy when they arrive. The reception
and processing of the messages is silent, so nothing is displayed to the user and users are unable to
notice them.
Low-priority push messages present an ideal attack surface because they bypass establishment of a
session. This allows an attack message to be accepted immediately. No further messages are required
beforehand to bring the target application into a reception state.
The Security Parameter Indicator (SPI) in the header is 0x0001 (step (1) in Figure 10), indicating that no
redundancy check, cryptographic checksum, or digital signature is used in the message, and that a proof
of reception is to be sent to the sender.
A Malicious Deck of Cards
A command packet for the S@T browser is organized into structures known as "decks," each containing
"cards" that group related commands. Because a packet can include multiple decks, the payload begins
with a deck list that defines its structure. The attack SMS contains one dynamic deck with one card (step
(2) in Figure 10). The S@T browser never saves dynamic decks, so no traces of the attack are left on the
SIM. This makes post-incident detection challenging, as it is difficult to determine if an attack was
conducted on the device. Only timestamped network traces of the malicious action can provide clues.
The card inside the attack SMS encloses five commands. Each bytecode command is identified by a tag.
Besides the bytecode commands, the S@T browser is capable of executing STK commands, which are
sent as proactive commands from the SIM card to the phone. The phone’s response is stored in a
variable of the S@T browser. The following commands would have been executed sequentially by the
S@T browser if the firewall did not block the SMS:
39

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
Figure 10: Structure of the binary SMS payload detailing the S@T browser commands.
● STK command Provide Local Information, step (3):
○ The first STK command instructs the S@T browser to send a proactive command to the
phone, requesting information about the network cell it is currently connected to, i.e.,
Cell Identifier, Location Area Code (LAC), Mobile Network Code (MNC), and Mobile
Country Code (MCC). The location information returned by the phone is stored in
variable 0x17.
○ Based on this data, the position of the phone can be determined with an accuracy
ranging from a kilometer in urban areas to a hundred kilometers in rural areas,
depending on the cell density.
● Initialize Variable, step (4):
○ Then, the variable 0x09 is initialized with 12 bytes of binary data.
○ We analyze the bytes' content in the next section.
● Concatenate Values, step (5):
○ Next, variable 0x09 is concatenated with the byte 0x0a, the variable 0x17, and the byte
sequence 0xcc 0xcc 0xcc. The concatenation result is stored in variable 0x10.
○ This command appends the location information stored in variable 0x17 to the binary
data in 0x09, while adding additional bytes to the stream.
● STK command Send Short Message, step (6):
40

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
○ Finally, the S@T browser issues a proactive command to the phone to send an
exfiltration SMS containing the contents of variable 0x10. It is addressed as
423790105651, assigned to FL1 Liechtenstein.
○ The SMS parameters are configured so that the user is not notified if the SMS
transmission fails, preventing detection of the attack.
The destination address of the exfiltration SMS reveals the attacker-controlled network,
as the attackers need access to it to receive the SMS.
● Exit Program, step (7):
○ The last command exits the program.
The Exfiltration SMS
Because the SMS message was blocked, it never reached the targeted phone, and no exfiltration
message with location data was actually sent. However, by parsing and decoding the commands
embedded in the intercepted SMS payload, we reconstructed how the exfiltration SMS would have been
generated and what it would contain if the attack was successful.
We analyzed the command sequence that would have been executed by the SIM card that defines how
location data would be collected and transmitted back to the attacker. The exploit would have silently
collected and sent its current location via SMS to the SMS Service Centre (SMSC) address configured by
the attacker, without any user interaction or visible indication on the device.
1. The SMS Header
The exfiltration SMS is first constructed from the contents of variable 0x10 (see step (5) of
Figure 10), with the first 12 bytes of this variable including the binary data from variable 0x09
(see step (4) in Figure 10). This data forms the SMS-SUBMIT header that controls the type of
SMS being sent and how it’s handled. In this case, it specifies that the SMS is sent from a device
to a remote SMSC, that it should accept duplicates, and does not request a delivery
confirmation.
2. The SMS Destination
The subsequent bytes of variable 0x09 are populated with the phone number of the destination
user, shown as 5548335237. This appears as a Brazil number (country code +55), but is
incomplete and does not conform to valid country numbering formats. As such, it is unlikely to
be used for message routing or delivery. Instead, it may function as a campaign identifier within
the STA2 surveillance infrastructure.
However, we were able to confirm that the SMSC address configured for the SMS matches a GT
observed in previous location-tracking attacks. Based on this information, we assess with
41

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
moderate confidence that the SMSC number was deliberately configured as a C2 endpoint by
STA2 to route and collect the SMS payload containing the target device location data (see Figure
11). While the destination number is invalid, the attackers can access the message delivered to
the SMSC address, enabling them to retrieve the exfiltrated location data without relying on
delivery to the end-device.
Figure 11: Exfiltration SMS delivery to the STA2 surveillance infrastructure masquerading as an FL1
SMSC
3. The Exfiltrated Data
The location data sent in the SMS is retrieved by the Provide Local Information command
and stored in variable 0x17. The Concatenate Values command adds a single length byte of
0x0a (see step (5) in Figure 10), with the last three bytes of the SMS probably used as artificial
padding. Through the Initialize Variable and Concatenate Values commands, the attackers craft
an exfiltration SMS that contains the location information and destination address likely
repurposed as an identifier for the target rather than a true delivery endpoint.
Comparison to SIMjacker
42

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
The attack SMS sent by STA2 fits a typical SIMjacker SMS configuration as described in ENEA’s 2019
report. Comparing the commands used, we note subtle differences. Nevertheless, ENEA states that the
SIMjacker SMSes observed in the wild also show variations. The attack SMS we observed could be a
more recent SIMjacker variant, adapting SIM or operator configurations to improve efficacy. The
distinctions are listed in Table 10.
Observed Attack SMS Common SIMjacker SMSes
Card element configured to No reset of variables Resetting all variables is
reset all variables in the S@T observed in more than 44% of
browser the SIMjacker SMSes analyzed
by ENEA.
Order of commands Obtains location information Creates SMS-SUBMIT header
first, then crafts the first, then retrieves the location
SMS-SUBMIT header and IMEI of the phone.
Data exfiltration Collects the phone’s location 93% of the traced SIMjacker
but not the IMEI SMSes collect the location and
the IMEI of the target device.
Variable with filler bytes Does not include a variable with Often include a variable with
filler bytes but single bytes, filler bytes, placed in different
which are added during the locations of the exfiltration SMS.
concatenation step This is probably done to
obfuscate the message.
Table 10: Comparison of the observed attack SMS to common SIMjacker SMSes
Sweden Operator Identifier Used as the Entry Point
The first two messages sent by STA2 used the same operator GT 467647531812, affirming its use as a
C2 endpoint address. We used a publicly available numbering plan search tool from PTS, Sweden’s
government telecom authority, shown in Figure 12, to confirm that number lies within a range allocated
to Telenabler AB. Telenabler is a network provider that offers services to Mobile Virtual Network
Operators (MVNOs). Telenabler’s website describes itself stating “We are specialists dealing with many
different country-specific telecom legislations and we work together with some of the strongest
telecommunication partners in the world.”
The Citizen Lab previously reported on Telenabler’s Global Title leasing business model in the 2023
Finding You report. In that report, we identified this same GT as a frequently detected source address
used in location tracking operations. Since that report, the activity from 467647531812 did not stop.
Between October 2023 and April 2025, we identified over 1,700 additional SS7 attacks originating from
this address, with over 92% of its traffic linked to location tracking. The primary SS7 query types seen
43

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
included provideSubscriberInfo (1,011) followed by provideSubscriberLocation (386) and
others. The repeated, high volume use of this GT with different location query types suggests it was
assigned specifically for surveillance purposes.
Figure 12: Number ranges allocated to Tenenabler by Sweden’s telecom regulator PTS.
SIMjacker Payload Exposes a Coordinated Attack Cluster
The signalling identifiers used in the SIMjacker exploit formed endpoints for C2 communication. The
attack used three numbers from different operators that played unique roles in the attack and in the
process, revealed tradecraft showing STA2’s detailed knowledge of the operator interconnect routing
ecosystem.
●
GT address to deliver the payload – 467647531812 – Telenabler Sweden
44

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
●
SMSC GT address used for exfiltration of location data – 423790105651 – FL1 Liechtenstein
●
Spoofed SMS sender address – 250730091970 – Airtel Rwanda
Mobile operators assign GT address ranges to specific core network functions (SMSCs, HLRs, MSCs, etc.)
and publish the assignments in IR.21 documents to ensure service availability and correct routing of
signalling traffic. Because GTs are routable signalling identifiers, they play a central role for roaming and
trust between operators. Many operators rely on address assignments published in IR.21 to enforce
security policies, rejecting signalling messages originating with inconsistent network assignments or
service functions.
The GT 423790105651 used in the attack falls within a range of addresses assigned by FL1 to SMSCs as
published in their IR.21 document (Figure 13). However, the configured address used in the attack
contains an extra digit beyond the documented range, showing the attacker’s knowledge of FL1’s IR.21
assignments. Appending an additional digit ensures the routing of the exfiltration SMS to the actor’s
surveillance C2 infrastructure, while also serving as an internal identifier for the surveillance application
labeling it as a SIMJacker operation and to process the target device location information within it.
Figure 13: SMSC global title range shown in the FL1 Liechtenstein IR.21.
The 250730091970 SMS sender address used in the SIMJacker attack is mapped to an Airtel Rwanda
GT range, but doesn’t appear to be designated to any particular network function. However, the attack
history behind this GT since 2022 shows over 600 events exclusively used in location tracking
operations.
Attribution Assessment
The STA2 campaign shows a unique approach to telecom surveillance, combining SS7 signalling,
SIM-based exploitation, and Diameter-based location tracking techniques. While we do not directly
attribute this activity to a specific organization, we have aligned the operational model based on
historical attack data, technical, and behavioural indicators.
A Long History of Network Surveillance
To assess the scale of STA2 activity, we analyzed historical SS7 and Diameter firewall telemetry
associated with the cluster of operator identifiers used in the campaign. We uncovered a prolific
operation with more than 15,700 location tracking attempts dating back to October 2022. An example of
early activity is shown in the Figure 14 screenshot, which shows a captured sequence of tracking
messages from October 19, 2022, with multiple operator identities all using the same Origin-Host
45

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
format (displayed in the “Source Node” column) and the Jersey-Airtel Route-Record. The targeted user
IMSI and portions of the IPX provider hostnames are partially redacted for privacy.
Figure 14: Early evidence of STA2 surveillance activity (October 19, 2022).
Table 11 summarizes the volume and progression of the STA2 surveillance activity over time.
Protocol October 2022
Diameter 109
SS7 103
Table 11: Progression of multi-year surveillance activity attributed to STA2.
Within that history of attacks, we looked for indicators that might point to a known surveillance actor.
The attack history associated with the GTs showed links to Fink Telecom Services (FTS), a Swiss-based
telecommunications provider exposed as a commercial telecom surveillance vendor in investigative
reporting by Lighthouse Reports and Bloomberg, which found attack clusters using the same signatures
as STA2.
The FTS Signalling Overlap
STA2 surveillance activity shows alignment with identifiers and patterns associated with FTS, including
same-day location tracking attacks and matching Diameter hostname formats. We analyzed a history of
attacks starting in November 2022 linked to both FTS and STA2. Prior to media reports of FTS linked to
SS7 surveillance, we identified numerous STA2 surveillance operations indirectly linked to FTS, with
46

CITIZEN LAB REPORT NO. 192  |  BAD CONNECTION

many occurring on the same day and with the same attack objective. A sample of these attacks are listed
in Table 12.
Date  Source Node  Network  Country  Threat Type  Signalling
Operation
4-Dec-22  ss.epc.mnc00 POLKOMTEL  Poland  Location  Insert-Subscri
| 1.mcc260.3gp  |     | Discovery  | ber-Data-Requ |
| ------------- | --- | ---------- | ------------- |
| pnetwork.org  |     |            | est           |
4-Dec-22  46727507103  FINK  Sweden  Location  provideSubscri
|     | TELECOM  | Discovery  | berInfo  |
| --- | -------- | ---------- | -------- |
SERVICES
15-Dec-22  25073009197 AIRTEL  Rwanda  Location  provideSubscri
| 0   | RWANDA  | Discovery  | berInfo  |
| --- | ------- | ---------- | -------- |
15-Dec-22  25671000034  UGANDA  Uganda  Location  provideSubscri
|     | TELECOM  | Discovery  | berInfo  |
| --- | -------- | ---------- | -------- |
15-Dec-22  26482000011  DEMSHI  Namibia  Location  provideSubscri
|     | TELECOM  | Discovery  | berInfo  |
| --- | -------- | ---------- | -------- |
18-Dec-22  25073009197 AIRTEL  Rwanda  Location  provideSubscri
| 0   | RWANDA  | Discovery  | berLocation  |
| --- | ------- | ---------- | ------------ |
18-Dec-22  25671000034  UGANDA  Uganda  Location  provideSubscri
|     | TELECOM  | Discovery  | berLocation  |
| --- | -------- | ---------- | ------------ |
19-Dec-22  79588879810  LETAI  Russia  Location  anyTimeInterr
|     |     | Discovery  | ogation  |
| --- | --- | ---------- | -------- |
19-Dec-22  26482000011  DEMSHI  Namibia  Location  anyTimeInterr
|     | TELECOM  | Discovery  | ogation  |
| --- | -------- | ---------- | -------- |
19-Dec-22  25073009197 AIRTEL  Rwanda  Location  anyTimeInterr
| 0   | RWANDA  | Discovery  | ogation  |
| --- | ------- | ---------- | -------- |
14-Feb-23  26482000011  DEMSHI  Namibia  Location  provideSubscri
|     | TELECOM  | Discovery  | berInfo  |
| --- | -------- | ---------- | -------- |
14-Feb-23  hss.epc.mnc0 POLKOMTEL  Poland  Location  Insert-Subscri
| 01.mcc260.3g   |     | Discovery  | ber-Data-Requ |
| -------------- | --- | ---------- | ------------- |
| ppnetwork.org  |     |            | est           |
14-Feb-23  25073009197 AIRTEL  Rwanda  Location  provideSubscri
| 0   | RWANDA  | Discovery  | berInfo  |
| --- | ------- | ---------- | -------- |
47

CITIZEN LAB REPORT NO. 192  |  BAD CONNECTION

11-Mar-23  hss.epc.mnc0 FINK  Switzerland  Location  Insert-Subscri
|     | 63.mcc240.3g   | TELECOM   |     | Discovery  | ber-Data-Requ |
| --- | -------------- | --------- | --- | ---------- | ------------- |
|     | ppnetwork.org  | SERVICES  |     |            | est           |
11-Mar-23  hss.epc.mnc0 MTS  Namibia  Location  Insert-Subscri
|           | 01.mcc649.3g   |          |         | Discovery  | ber-Data-Requ  |
| --------- | -------------- | -------- | ------- | ---------- | -------------- |
|           | ppnetwork.org  |          |         |            | est            |
| 5-Apr-23  | 4672750710     | FINK     | Sweden  | Location   | provideSubscri |
|           |                | TELECOM  |         | Discovery  | berInfo        |
SERVICES
5-Apr-23  25671000034  UGANDA  Uganda  Location  provideSubscri
|     |     | TELECOM  |     | Discovery  | berInfo  |
| --- | --- | -------- | --- | ---------- | -------- |
5-Apr-23  hss.epc.mnc0 POLKOMTEL  Poland  Location  Insert-Subscri
|     | 01.mcc260.3g   |     |     | Discovery  | ber-Data-Requ |
| --- | -------------- | --- | --- | ---------- | ------------- |
|     | ppnetwork.org  |     |     |            | est           |
16-Aug-23  hss.epc.mnc0 POLKOMTEL  Poland  Location  Insert-Subscri
|     | 01.mcc260.3g   |     |     | Discovery  | ber-Data-Requ |
| --- | -------------- | --- | --- | ---------- | ------------- |
|     | ppnetwork.org  |     |     |            | est           |
16-Aug-23  hss.epc.mnc0 FINK  Switzerland  Location  Insert-Subscri
|     | 63.mcc240.3g   | TELECOM   |     | Discovery  | ber-Data-Requ |
| --- | -------------- | --------- | --- | ---------- | ------------- |
|     | ppnetwork.org  | SERVICES  |     |            | est           |
23-Feb-24  46764753181 TELENABLER  Sweden  Location  provideSubscri
|     | 2   | AB  |     | Discovery  | berInfo  |
| --- | --- | --- | --- | ---------- | -------- |
23-Feb-24  25073009197 AIRTEL  Rwanda  Location  provideSubscri
|     | 0   | RWANDA  |     | Discovery  | berInfo  |
| --- | --- | ------- | --- | ---------- | -------- |
23-Feb-24  26482000045 DEMSHI  Namibia  Location  provideSubscri
|     | 8   | TELECOM  |     | Discovery  | berInfo  |
| --- | --- | -------- | --- | ---------- | -------- |

Table 12: Firewall telemetry with addresses linked to Fink Telecom Services and STA2.

The attacks summarized in Table 12 include identifiers seen in the STA2 campaign alongside GTs and
Diameter identifiers attributed to FTS highlighted in RED. Notably, the Diameter hostname formats used
in the STA2 attacks also use MCC/MNC values associated with FTS. The values listed in published IR.21
documents are shown in Figure 15.

48

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
Figure 15: Signalling domains published in the FTS IR.21 document.
While spoofing cannot be ruled out, the alignment of historical same-day location tracking attacks,
Diameter hostname formats used in the STA2 campaign, GT ranges published in FTS IR.21 documents,
and journalist publications exposing SS7 attacks attributed to FTS show clear links between STA2 and
FTS.
Correspondence
On April 17, 2026, we sent letters with questions about our research to 019Mobile, Airtel Jersey Sure,
and Tango Networks. As of the time of writing, only 019Mobile has responded to our questions. Their
response3 can be found here.
Update: After publishing this report, we received a response from Sure. Their response can be found
here.
Conclusion
This report is the first to map live SS7 and Diameter attack telemetry to operator identifiers and
interconnect routes used in cross-protocol mobile surveillance operations. Rather than implanting
device spyware or hacking corporate networks to carry out mobile espionage, the two actors leveraged
legitimate operator signalling identities and trusted interconnections to carry out targeted surveillance
across country borders. By blending their location queries into normal roaming traffic, and manipulating
protocols and network identifiers, they effectively operated as “ghost operators” within the global
telecom ecosystem.
The findings in this report expose how advanced actors operationalize telecom infrastructure to carry
out campaigns persisting for years without detection. Telecom networks form the backbone of global
civil society, and when trust is exploited for surveillance, the consequences extend beyond individual
victims to mobile users worldwide. This investigation exposes more than protocol vulnerability issues in
telecommunications; it shows governance failures across the entire interconnect ecosystem used for
3 We received a response from 019Mobile after our deadline but we are including it here. Their assertions do not
alter our conclusions, although we will investigate further and remain open to further information from them and
other providers.
49

CITIZEN LAB REPORT NO. 192 | BAD CONNECTION
critical mobile communications. It also demonstrates how those weaknesses enabled the use of
telecommunications infrastructure as a covert surveillance platform.
The global telecom ecosystem can no longer rely on legacy trust models. Without authentication,
enforceable interconnect controls, transparency in commercial network access, and regulatory
accountability, mobile networks will continue to serve as a global platform for covert espionage.
50