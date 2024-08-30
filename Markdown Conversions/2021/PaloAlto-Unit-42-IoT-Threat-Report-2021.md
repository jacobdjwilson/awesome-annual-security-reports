2020 Unit 42 IoT
Threat ReportTable of ContentsExecutive Summary01IoT Security LandscapeOrganizations Lack the Tools to Discover and Secure IoTEnterprises Sit on a Time BombHealthcare Is in Critical ShapeBasic Network Segmentation Best Practices Arent FollowedCase Study: Conficker in Healthcare02Top IoT ThreatsExploits, Password Attacks, and IoT Worms Top the ChartUnpatched Devices and Legacy Protocols: Means of Lateral MovementThreats Evolving to Specifically Target IoT EnvironmentsCase Study: Cryptojacking in the Wild03Conclusion and RecommendationsTake Steps to Reduce RiskStep 1: Know your risk and discover IoT devices on the networkStep 2: Patch printers and other easily patchable devicesStep 3: Segment your IoT devices across VLANsStep 4: Enable active monitoringPerfect Your IoT StrategyBest Practice 1: Think holistically, orchestrate the entire IoT lifecycle345678910111213141516161617181919Best Practice 2: Expand security to all IoT devices through product integrations20AboutPalo Alto NetworksUnit 42Methodology21212122P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t2Executive SummaryAccording to a 2019 Gartner report, "By the end of 2019, 4\.8 billion \[IoT] endpoints are expected 
to be in use, up 21\.5% from 2018\." While the internet of things (IoT) opens the door for innovative 
new approaches and services in all industries, it also presents new cybersecurity risks. To evaluate 
the current state of the IoT threat landscape, the Unit 42 threat intelligence team analyzed security 
incidents throughout 2018 and 2019 with the Palo Alto Networks IoT security product, Zingbox, 
spanning 1\.2 million IoT devices in thousands of physical locations across enterprise IT and healthcare 
organizations in the United States. We found that the general security posture of IoT devices is 
declining, leaving organizations vulnerable to new IoT\-targeted malware as well as older attack 
techniques that IT teams have long forgotten. This report details the scope of the IoT threat landscape, 
which IoT devices are most susceptible, top IoT threats, and actionable next steps to immediately 
reduce IoT risk.IoT devices are encrypted 
and unsecured98% of all IoT device traffic is unencrypted, 
exposing personal and confidential data on 
the network. Attackers whove successfully 
bypassed the first line of defense (most 
frequently via phishing attacks) and 
established command and control (C2\) 
are able to listen to unencrypted network 
traffic, collect personal or confidential 
information and then exploit that data for
profit on the dark web.57% of IoT devices are vulnerable to 
medium\- or high\-severity attacks, making 
IoT the low\-hanging fruit for attackers. 
Because of the generally low patch level
of IoT assets, the most frequent attacks 
are exploits via long\-known vulnerabilities 
and password attacks using default
device passwords.IoMT devices are running 
outdated software83% of medical imaging devices run on 
unsupported operating systems, which is 
a 56% jump from 2018, as a result of the 
Windows 7 operating system reaching its 
end of life. This general decline in security 
posture opens the door for new attacks, 
such as cryptojacking (which increased 
from 0% in 2017 to 5% in 2019\) and 
brings back long\-forgotten attacks such as 
Conficker, which IT teams had previously 
been immune to for a long time.The internet of medical things (IoMT) devices 
with the most security issues are imaging 
systems, which represent a critical part of the 
clinical workflow. For healthcare organizations, 
51% of threats involve imaging devices, 
disrupting the quality of care and allowing 
attackers to exfiltrate patient data stored on 
these devices.Healthcare organizations 
are displaying poor network 
security hygiene72% of healthcare VLANs mix IoT and IT 
assets, allowing malware to spread from users 
computers to vulnerable IoT devices on the same 
network. There is a 41% rate of attacks exploiting 
device vulnerabilities, as IT\-borne attacks scan 
through network\-connected devices in an 
attempt to exploit known weaknesses. Were 
seeing a shift from IoT botnets conducting 
denial\-of\-service attacks to more sophisticated 
attacks targeting patient identities, corporate 
data, and monetary profit via ransomware.IoT\-focused cyberattacks are 
targeting legacy protocolsThere is an evolution of threats targeting 
IoT devices using new techniques, such as 
peer\-to\-peer C2 communications and worm\-
like features for self\-propagation. Attackers 
recognize the vulnerability of decades\-old 
legacy OT protocols, such as DICOM, and are 
able to disrupt critical business functions in 
the organization.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t301IoT Security LandscapeIoT is rapidly growingBy the end of 2019, IoT adoption grew to an estimated 4\.8 
billion devices, an increase of 21\.5% from the end of 2018\.1More and more newly developed IoT devices are network\- 
or internet\-connected.By now, more than 30% of all network\-connected 
endpoints are IoT devices (excluding mobile devices) at
the average enterpriseand has a big security problem98% of all IoT traffic is unencrypted, exposing personal 
and confidential data on the network.57% of IoT devices are vulnerable to medium\- or high\-
severity attacks, making IoT the low\-hanging fruit for 
attackers.83% of medical imaging devices run on unsupported 
operating systemsa 56% jump from 2018, as a result of 
Windows 7 reaching its end of life.High\-profile, IoT\-focused cyberattacks are forcing industries to recognize and manage IoTs risks 
to protect their core business operations. Markets such as healthcare are exposed to an amount of 
risk that surpasses previous expectations. Some IoT vulnerabilities are life\-threatening, while some 
attack critical enterprise functions or exfiltrate confidential data.Read on to learn more about the IoT security landscape.1\. Gartner Says 5\.8 Billion Enterprise and Automotive IoT Endpoints Will Be in Use in 2020, Gartner, August 29, 2019, 
https:www.gartner.comennewsroompress\-releases2019\-08\-29\-gartner\-says\-5\-8\-billion\-enterprise\-and\-
automotive\-io.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t4Organizations Lack the Tools to Discover 
and Secure IoTEnterprises face a significant challenge in not knowing the risk exposed by IoT devices and 
applications. The main reasons are lack of device discovery and inventory.ITs lack of IoT visibilityAn outdated, static inventory of IoT assets checks a box, but is far from effective security 
management. The identification of devices using traditional IT device characteristics, such as IP 
addresses and underlying operating systems is not working for IoT. Only by identifying the specific 
type of device can an organization accurately plan its network access requirements, deployment 
tactics, security strategy optimization, and operations plans. Once device identities are determined, 
security systems can track device behavior in the context of the organizations workflows rather 
than just viewing them as dynamic, changing IP addresses of an unknown device type.Existing security systems dont support IoTEndpoint protection systems are designed for computers, tablets, and phones with the ability to 
run agents, but IoT devices often run custom or outdated operating systems without such ability. 
As a result, cybersecurity systems see IoT devices as unknown endpoints, and thus do not know the 
specific device type, its risk profile, and its expected behavior.Network\-based cybersecurity systems have the visibility to identify network\-connected endpoints, 
but they rarely incorporate the ability to accurately identify, track, and secure IoT devices.Organizational and human resource challenges between OT 
and ITMost organizations manage information technology (IT) and operational technology (OT) as 
separate teams with separate processes and tools. While IT focuses on the organizations IT 
assetssuch as computers, network equipment, and printersOT focuses on non\-IT assets, such 
as medical devices and security cameras.As these teams report to different parts of the organization, they have different ways to maintain 
device security. Often, IT is more advanced in this respect because of the rapid evolution of personal 
computers and server operating systems as well as their proactive security operations in contrast to 
medical devices.As a healthcare example, in hospitals, biomedical engineers know and maintain the medical 
devices, but they dont maintain the underlying operating systems that power the devices. As these 
network\-connected medical devices (such as X\-RAY machines) often run end\-of\-life operating 
systems with known vulnerabilities, they pose a high risk to the organizations employees, patients, 
computer systems, andeventuallybusiness operations.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t5Enterprises Sit on a Time BombWhen we work on a device other than a desktop, laptop, or phone, thats an IoT device. We see them 
in our offices every day: IP phones, printers, etc. These network\-connected devices are all targets 
for attackers, and they often arent properly maintained by IT.Enterprise IoT DevicesSecurity Issues9%5%7%5%5%5%18%24%44%33%IP PhonePrinterIntercom System0%Consumer ElectronicsCameraOtherTracking and Locating SystemsWearableIoT GatewayEnergy Management1%1%3%3%2%
2%3%2%6%0%10%20%30%40%50%Figure 1: IP phones have only 5% of all security issuesGood news for IP phones: They account for 44% of all enterprise IoT devices but only 5% of all security 
issues. Used across a wide range of industries, IP phones are often designed to be enterprise\-grade in bothreliability and security.Security cameras 
make up only 5% ofenterprise IoT devic\-es, but they accountfor 33% of all securityissues. This is be\-Printers account for 
18% of IoT devicesand 24% of securityincidents. They have inherently less built\-insecurity, and vulnera\-cause many cameras are designed to bebilities in browser interfaces often make consumer\-grade, focusing on simplicity ofthem ideal targets as entry points foruse anddeployment over security.launching cyberattacks.What can an attacker do witha security camera?In 2016, teen scammers initiated the large\-scale Mirai attack, involving more than600,000 CCTV cameras, to scan big blocksof the internet for open telnet in an attemptto log in using default passwords.How dangerous is a printer on the loose?They can:Provide access to print logsOpen up lateral movement to othercomputers on the networkBe used as part of a DDoS attackP a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t6Healthcare Is in Critical ShapeA 2019 Gartner survey found that 40% of healthcare CIOs plan to spend new or additional funds on 
cybersecurity tools in 2020\.2 For the time being, medical devices are in a critical state.Medical devices running outdated operating systemsSecurity function missing in the organizationDuetotheirlonglifecycles,medicalIoTdevicesareBiomedicalengineerswhomaintainmedicaldevicesamong the worst offenders of running outdated and,often lack training and resources to follow IT securityin many cases, end\-of\-life operating systems. Thesebest practices to employ password rules, store pass\-devices are neither maintained by IT nor supported bywords securely, and maintain up\-to\-date patch levelsthe operating system vendors.on devices.Medical IoT DevicesSecurity Issues16%14%11%26%44%51%86%Infusion Pump2%Imaging SystemPatient MonitoringPoint of Care AnalyzerNurse Call SystemMedical Device GatewayMedication DispensingECG MachineDefibrillatorOther9%1%4%5%4%3%1%2%1%
1%
0%1%
0%Good news: The National
Cybersecurity Center of
Excellence (NCCoE) completed 
a medical IoT device security 
project in 2019 called Securing 
Picture Archiving and Commu\-
nication Systems (PACS) to 
provide guidance and reference\-
able architecture for securing 
the PACS ecosystem and to 
include example solutions
using existing commercial and 
open source cybersecurity 
products.0102030405060Figure 2: Medical devices and security issuesImaging systems are extremely vulnerableImaging systems run on variousoperating systems, includingWindows, Linux, and Unix. Asof this writing, 83% of all medi\-cal imaging systems run on end\-of\-life operating systems withknown vulnerabilities and nosecurity updates or patch sup\-port. This is a 56% jump from2018 as a result ofWindows 7reaching its end of life.New attacks exploit vulnerabil\-ities in the underlying operatingsystem to target medical IoTdevices. Imaging systems areparticularly susceptible to thiskind of attack due to supportfor their underlying OS expiringwell before the devices are re\-tired or decommissioned.Win (other)
2%Unix
3%Win 10
11%Linux
4%Embedded
7%WinXP
11%17%
Active
Support83%
No SupportEmbedded
2%Linux
2%Win 8\.1
2%Win 7
56%Progress: A new bill 
in the USCongress 
attempts to address 
smart\-device se\-
curity regulations. 
The IoT Cyberse\-
curity Act of 2019 
states that NIST 
should settle on 
standards for the 
secure develop\-
ment of IoT devic\-
es, device man\-
agement, patching, 
andconfiguration 
management.Figure 3: Smart device security regulations2\. "2019 Top Actions for Healthcare Provider CIOs: Summary and Retrospective View," Gartner, February 26, 2019, 
https:www.gartner.comendocuments39030672019\-top\-actions\-for\-healthcare\-provider\-cios\-summary\-an.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t7Basic Network Segmentation Best 
Practices Arent FollowedThe simplest IoT risk remediation practice is network segmentation. Despite this, only 3% of all 
segmented networks or virtual local area networks (VLANs) in the healthcare organizations we 
studied contained strictly medical IoT devices, and 25% contain non\-medical IoT devices (IP 
phones, printers, etc.).Non\-Medical Only
25%Medical Only
3%72% of healthcare VLANs house a mix of 
medical IoT devices, generic enterprise 
IoT devices, and IT devices. Thislowers 
the barrier for lateral movement. For 
example, an infected laptop can easily 
target surveillance cameras and DICOM 
viewers found in the same network. 
This is low\-hanging fruit for healthcare 
 organizations to address this year.Mixed
72%Figure 4: VLANs have a mix of medical IoT devices2019201731%25%43%45%16%16%This is still more than athreefold improvementfrom 2017Although there is room 
for improvement, we 
observed an increasing 
adoption of network 
 segmentation:In 2017, only 12% ofhospitalsemployedmore than 20 VLANs.In 2019, this numberrose to 44%.09101920\-2930\-392%40\-492%4%4%50\-5960\-6970\-7980\-8990\-99100\+0%
0%0%
0%1%0%1%0%1%0%5%2%Figure 5: More than a threefold increase in use of VLANs at hospitals0%10%20%30%40%50%Network segmentation isnt enough: Microsegmentation is idealWhile the overall trend is encouraging, network segmentation alone is not sufficient. For instance, 
housing mission\-critical heart rate monitors in the same network as imaging systems would not be 
a sound practice. A device profile\-based microsegmentation approach that considers a multitude of 
factors, including device type, function, mission criticality, and threat level, provides an isolation 
approach that significantly reduces the potential impact of cross\-infection.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t8CASE STUDY: Conficker in HealthcareZingbox, the Palo Alto Networks IoT security product, alerted one of the hospitals of Conficker 
traffic detected in its network. The offending device was a mammography machine. In the days 
following, Zingbox identified another mammography machine, a DICOM (Digital Imaging and 
Communications in Medicine) viewer, a digital radiology system, and a few other infected devices 
exhibiting Conficker behavior.The hospital staff responded by turning these devices 
off when they were not in use. To verify the infection, 
the staff took one of the infected mammography 
machines and the DICOM viewer offline to re\-image 
them. Within hours of the devices coming back online, 
Conficker infected them again.Further investigation revealed that while re\-imaging 
the devices had removed the malware, the approved 
images were outdated: they did not include the latest 
security patches, leaving the devices vulnerable to 
Conficker. Given the peer\-to\-peer nature of how 
Conficker spreads on a network, it was only a matter 
of time before another infected device passed the virus 
back along.The hospital then took all infected devices offline,
re\-imaged them, installed the latest security patches, 
and brought back the devices online one by one, closely 
monitoring anomalous behaviors. Over the span of a 
week, the devices were reintroduced to the network and 
showed no further signs of Conficker infection.This is a typical example of the challenges many 
organizations face today. They are hampered by a 
lack of real\-time visibility into IoT device behavior 
and the cybersecurity expertise to quickly respond to 
threats, contain the spread of infection, and eradicate 
the underlying cause. In some organizations, the 
critical nature of their devices makes troubleshooting, 
shutdown, and re\-imaging impossible or extremely 
difficult to do without disrupting business operations. 
As a result, many organizations find themselves in 
an endless loop of simply treating the symptoms and 
hoping for the best.Conficker 
is back!Conficker, 
also known 
as Downup 
and Kido, 
is a worm 
that targets 
Microsoft Windows. When first 
detected in November 2008, it 
used flaws and ran dictionary 
attacks on administrator passwords 
to propagate while forming a 
botnet. By 2009, it had infected an 
estimated 15 million computers 
across government, business, and 
home users in 190\+ countries. Once 
IT teams and antivirus vendors 
could finally counter the worm, 
they were able to reduce infected 
computers to 1\.7 million by 2011 and 
400,000 by 2015\.More recently, IT teams had long 
since forgotten the wormuntil 
it started appearing again on 
medical devices running outdated 
or unsupported Windows OS 
versions. At the time of this report, 
nearly 20% of Zingbox healthcare 
customers have been infected by 
Conficker at some point in time.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t902Top IoT ThreatsThreats continue to evolve and target IoT devices with new techniques, 
such as peer\-to\-peer C2 communications and worm\-like self\-propagation.This evolution is enabled by a weak device and network security posture:72%72% of healthcare VLANs mix IoT and IT assets, allowing malware 
to spread from users computers to vulnerable IoT devices on the 
same network.41% of attacks exploit device vulnerabilities, as IT\-borne attacks 
scan through network\-connected devices in an attempt to exploit 
known weaknesses.Decades\-old legacy OT protocols, such as DICOM, are attacked to 
disrupt critical business functions or propagate throughout in the 
organization.The gap between OT and IT security practices and operations enables 
attacks that IT has otherwise been immune to for over a decade.of healthcare VLANsmix IoT and IT assets41%Read on to learn more about our findings on top threats and attack 
techniques.of attacks exploitdevice vulnerabilitiesP a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 0Exploits, Password Attacks, and IoT 
Worms Top the ChartNo. 1: Exploits 
targeting device 
vulnerabilitiesWhile the security postures 
of IoT devices make them 
easy targets, in most cases, 
the devices are only used as 
stepping stones in lateral 
movement to attack other 
systems on a network.Were seeing a large number of 
network scans, IP scans, port 
scans, and vulnerability scans on 
networks, attempting to identify 
other devices and systems, 
looking for targets for the next 
step in lateral movement.Cryptojacking
5%Phishing
8%Password
13%26%
User Practice41%ExploitsBotnet
6%Backdoor Trojan
7%33%
MalwareNetwork Scan
14%Remote Code 
Execution
5%Command Injection
5%Buffer Overflow
5%Others
5%SQL Injection
4%Zero\-Day
3%Ransomware
8%Worm
12%Figure 6: Breakdown of top IoT threatsNo. 2: Password attacksDefault, manufacturer\-set passwords and poor password security practices continue to fuel password\-
related attacks on IoT devices. With Californias SB\-327 IoT law now prohibiting the use of default 
credentials, we expect this trend to change direction.Operational misalignment also enables password\-targeted 
attacks. In many cases, passwords chosen by OT staff are not in 
line with ITs more advanced password policies and password 
management practices. This is one example of organizational 
misalignment between OT and IT.No. 3: IoT worms are becoming more 
common than IoT botnetsWere witnessing a shift away from attackers primary 
motivationrunning botnets to conduct distributed denial\-of\-
service (DDoS) attacks via IoT devicesto malware spreading 
across the network via worm\-like features, enabling attackers to 
run malicious code to conduct a wide variety of new attacks.Wireless routers
under threatUnit 42 found a Gafgyt variant 
targeting more than 32,000 po\-
tentially vulnerable small office 
and home wireless routers to 
conduct a botnet attack against 
gaming servers on the internet.Today, wireless routers are 
some of the most common IoT 
devices in organizations, making 
them targets for IoT botnets, 
degrading both the production 
network and the reputation of 
the IP addresses of affected 
companies.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 1Unpatched Devices, Legacy Protocols: 
Means of Lateral MovementLow patch levelsIoT exploits represent a unique challenge because they often involve legacy OS that dont offer 
security updates anymore. We found that 83% of medical imaging devices run end\-of\-life, 
unsupported OS. This means old, well\-known exploits can still pose significant threats to them.Aged OT protocols are targetsWe observed vulnerabilities in aged industry 
OT protocols. These protocols were designed 
to run on devices behind the firewall without 
much interference with other systems or users. 
As the network perimeter disappearing with 
the shift toward cloud technologies, these 
decades\-old protocols get exposed to the hustle 
and bustle of todays enterprise networks.Lateral movementWe see lateral movements originating from 
successful phishing attacks targeting IoT 
systems on the same network and exploiting 
vulnerabilities remotely. 57% of IoT devices are 
vulnerable to medium\- or high\-severity attacks, 
making IoT the low\-hanging fruit for attackers.Legacy OT protocol hack storyWe found a vulnerability in the DICOM 
protocol. Attackers could change the header 
in a DICOM packet to replace the image 
captured by the device with an executable 
file. As the image was saved, the malware 
persisted on a network drive. When another 
DICOM device opened the image, the DICOM 
viewer executed the image, which ran the 
malware. Because DICOM images tend to 
store patient information, antivirus software 
is not allowed to scan the file locations for 
privacy reasonsessentially, this malware 
was protected by design.Two\-staged attacks through backdoors left untreatedBackdoors installed from previous breaches are often overlooked or not properly disabled, 
lowering the barrier of entry for a wide range of other attacks. As an example, were seeing 
WannaCry ransomware attacks spreading through backdoors left open by previous Pebble Pulser 
malware infections.With the growing number of unpatchable devices, such as those running Windows 7, were not expecting 
this trend to turn around unless more organizations follow the best practices in these materials.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 2Threats Evolving to Specifically Target 
IoT EnvironmentsPeer\-to\-peer featuresWe see an evolution of threats targeting IoT 
environments by way of decentralized peer\-to\-peer 
C2 communications wherein compromised devices
controlled by one node over a server connection
communicate with each other on the local network. 
This lets attackers minimize connections to the 
outside world and enables the swarm to operate even 
without an internet connection.Vulnerabilities in cloud\-connected IoT devices (e.g 
security cameras with remote viewing capabilities) 
enable attackers to bypass firewalls and access 
private networks.Fight for the hostWe have observed a trend of malware attempting 
to remove other malware to occupy the victim IoT 
device exclusively. This is likely to address hardware 
resource constraints, as device manufacturers 
minimize the hardware capacity in their purpose\-
built boards to reduce energy consumption and 
retail prices.Leaked IoT malware code fuels 
new varietiesThe leakage of the IoT botnet Mirais source code has 
fueled the birth of numerous Mirai variants in the past 
year. Adversaries have been building these variants in 
a fashion similar to the way open source developers 
fork new code versions from each others work.WannaCry ransomware 
spreading on unsegmented 
networksWhen we come across WannaCry cases 
on healthcare customers networks, 
they are always mixed networks 
with PCs, scanners, nuclear imaging 
devices, etc. WannaCry has a strong 
self\-propagation and infection 
capability, enabling it to cross\-infect 
devices across IoT and IT.Mirai botnet attackMirai malware turns networked 
devices running Linux into remotely 
controlled bots that can be used as 
part of a botnet in large\-scale network 
attacks. It primarily targets online 
consumer devices, such as IP cameras 
and home routers.On October 12, 2016, a massive DDoS 
attack brought about by a Mirai botnet 
made much of the internet inaccessible 
on the east coast of the US. Authorities 
initially feared this attack was the 
work of a hostile nation\-state.Now, Mirai has grown into a framework to which developers can add new device exploits as new variants.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 3CASE STUDY: Cryptojacking in the WildCryptojacking malware is an emerging online threat that hides on a device and uses the 
machines resources to mine forms of cryptocurrency, such as bitcoin. Like most malicious 
attacks, the motive is profit, but unlike most, its designed to stay hidden from the user. 
Cryptojacking causes high CPU and network usage and drains critical healthcare systems, 
potentially impacting life\-saving capabilities.Figure 7: Cryptojacking drains critical healthcare systemsZingbox alerted a customer participating in this research about a cryptomining code transfer 
between an IT storage device and an OT device in its internal network. The IT team wanted to shut 
down the device, but the OT team disagreed due to production safety concerns. While waiting for the 
device to be allowed to go offline, the IT staff investigated the storage device as Zingbox continued 
to monitor the network traffic for further malicious activities.The next day, cryptomining code transfer was again detected on the network. Further investigation 
identified the offending device as a server that hosted hundreds of VM guests on the OT network, 
making the offending VM guest difficult to find. Continuous network traffic monitoring revealed 
a twice\-weekly scheduled data transfer. The regular pattern enabled the IT staff to identify the 
offending process and offending VM guest, which they then removed from the VM host.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 403Conclusion and RecommendationsCSOs can take steps now to reduce their IoT riskCSOs can immediately act to reduce their organizations exposure to IoT\-initiated attacks.
These steps arent comprehensive, but they reduce a large share of IoT risks:1\.Know your riskdiscover IoT devices on the network2\.Patch printers and other easily patchable devices3\.Segment IoT devices across VLANs4\.Enable active monitoring and an effective IoT strategy prepares the organization in 
the long term.To know and manage risk proactively, an organization needs an effective IoT security strategy.
Our research team chose two additional practices every IoT strategy should incorporate:1\.Think holistically: orchestrate the entire IoT lifecycle2\.Expand security to all IoT devices through product integrationsP a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 5Take Steps to Reduce RiskStep 1: Know your riskdiscover IoT devices on the networkIoT security solutions enable organizations to discover and identify IoT devices on their networks. 
We found that 30% of network\-connected devices in an average enterprise are IoT assets, excluding 
smartphones. Although this a significant number of assets, most organizations are unaware of 
these devices and dont manage their security postures or risk profiles.Intelligent device scanning and profiling enables IT security teams to have visibility of their 
network\-connected IoT devices, their risk profiles, and their network behavior when interacting 
with other devices on the network. Todays most advanced IoT security solutions, such as Zingbox, 
use machine learning to identify even never\-before\-seen IoT devices and recognize malicious 
network communication patterns before they cause damage.Discovering IoT devices internet connectivity profiles is important. IoT devices with direct internet 
access can carry higher risk profiles because internet connectivity allows exploits to move faster than 
they can on devices that are only LAN\-connected. Even so, purely LAN\-connected IoT devices expose 
a larger practical risk: These devices have been built with the assumption of safety behind a firewall. 
Compared to internet\-connected, SaaS\-based assets, we're seeing more cleartext communication, 
open ports, and weak credentials being used on these devices. A computer network in which 
employees and such devices are mixed presents the challenge of user devices cross\-infecting IoT assets.As soon as IT discovers the devices and acknowledges their risk profiles, they can start the 
remediation work.Step 2: Patch printers and other easily patchable devicesOur research shows printers and security cameras are the most abundant and vulnerable devices 
across enterprise networks. In healthcare, imaging and patient monitoring systems top the charts.After initial IoT device discovery, we recommend investigating the security posture of the top two 
or three most abundant network\-connected devices and working with their respective vendors on a 
patch management strategy for routine maintenance moving forward.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 6Step 3: Segment IoT devices across VLANsNetwork segmentation has become a general practice for most organizationsa chore to set up in 
practice, but one with strong security benefits across the enterprise. A properly segmented network 
stops lateral movement of exploits, reduces the attack surface, and minimizes the aftermath. 
Organizations can implement network segments leveraging VLAN configurations and firewall 
policies. Inter\-segment access and north\-south communication should be strictly guarded by the 
network boundary, switch ACLs, and firewall policies. This essentially creates a strong perimeter 
defense around network tiers or security zones that protect confined IoT and IT assets based on 
their assigned security value or significance to the organization.According to our researchVLAN use increased more thanWe found that only72%of healthcare VLANs dont followsound networking practices3foldin 2019 compared totwo years before3%of healthcare VLANs exclusivelyhost IoMT devicesIntelligent microsegmentation
process using device profile typeSegmenting OT, enterprise IoT, and IT 
devices is just a start. Organizations should 
also consider segmentation based on device 
characteristics and profiles.The best practice for segmenting an 
organizations network is to base it on
device type, threat levels, usage patterns,
and other device profile characteristics.In a 2018 report, Gartner predicted that 
more than 60% of IoT devices in an 
enterprise infrastructure would be virtually 
segmented within two years.3 Were seeing 
growth in the number of IoTIT segmented 
networks, but organizations must employ 
a solution that can identify device types 
and the characteristics of their network 
behavior to fully leverage the benefits of 
microsegmentation.A healthcare exampleIn a typical healthcare organization, there are 
mission\-critical medical IoT devices, generic 
non\-medical IoT devices, and IT devices. In a 
securely designed network, mission\-critical 
medical IoT devices are deployed in isolated 
network segments.In parallel with basing segmentation on IoT 
device identity, network teams can further 
segment IoT devices by security levelfor 
instance, by separating those with endpoint 
security agents from those without them, 
or devices running on end\-of\-life OS from 
those with up\-to\-date security patches. The 
deployment of IoT devices with different 
security capabilities should also follow a well\-
designed segmentation scheme.To enable profile\-based microsegmentation, 
healthcare organizations must employ accurate 
device identification methods with continuous, 
real\-time device analysis to factor in the ever\-
changing device vulnerabilities, risks, and other 
fluid characteristics that indicate the current 
level of their IoT device security status.3\. Predicts 2019: IoT Will Drive Profound Changes to Your Core Business Applications and IT Infrastructure,
Gartner, December 13, 2018, https:www.gartner.comendocuments3895863predicts\-2019\-iot\-will\-drive\-
profound\-changes\-to\-your\-co.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 7Step 4: Enable active monitoringTo accurately identify attacks, a monitoring solution must be able to scale and run continuously, 
identify all vulnerabilities, and analyze the behavior of all network\-connected devices, all in real 
time. IoT security solutions typically rely on machine learning and run in highly scalable cloud 
architecture to learn, profile, and alert security teams about anomalies.In healthcare, close collaboration with the IT team enables biomedical teams to create best practice 
guidelines for securely maintaining medical IoT devices. With the increase in devices running on 
end\-of\-life OS, healthcare organizations must plan to employ these recommendations as early as 
possible to help manage and secure their medical IoT assets.High Risk
10%Low Risk
43%We examined the distribution of 
risk across 1\.2 million enterprise 
and healthcare customers' IoT 
devices (see figure 8\). Of note, 
we found that 57% of surveyed 
IoT devices are vulnerable 
to medium\- or high\-severity 
attacks,making IoT the low\- 
hanging fruit for attackers.Medium Risk
47%Figure 8: Distribution of risk across 1\.2 million devicesIoT device risk management best practicesThe Common Vulnerability Scoring System (CVSS) is an industry\-accepted system that assigns a 
numerical score to device vulnerabilities to indicate their severity. The score can be translated to a risk 
level to help organizations properly assess and prioritize their vulnerability management processes:High riskMedium riskLow riskDevices considered to be 
at high risk often require 
immediate action. The 
urgency arises from the 
detection of security 
incidents or missing 
critical patches that leave 
the devices exposed. 
These devices typically 
have vulnerabilities with 
CVSS scores of 9 or 10\.Devices are considered 
low risk if there 
are no real\-time 
security alerts and no 
indication of policy 
violations as defined 
by the organization. 
If vulnerabilities exist 
on such a device, they 
typically have CVSS 
scores lower than 4\.Most IoT devices fall 
into this range. These 
devices are not diligently 
maintained, often lack 
the latest security patch, 
use weak or default 
passwords, and run 
end\-of\-life OS. They 
often have unauthorized 
applications running on 
them, and if they host 
a web browser, they 
might connect to sites 
deemed risky or malicious. 
These devices have 
vulnerabilities with CVSS 
scores between 4 and 8\.9\.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 8Perfect Your IoT StrategyBest Practice 1: Think holistically, orchestrate the entire
IoT lifecycleManaging the IoT lifecycle is a new challenge for organizations. A holistic approach to orchestrating 
the entire IoT lifecycle consists of six steps:OnboardSecureOptimizeManageRetireIdentifyOrchestrateFigure 9: The IoT lifecycle1\.Identify: Be notified any time a new device is connected to the network. Identify the device, its 
category, its risk profile, and usage statistics.2\.Onboard: Most IT teams architect their networks to dynamically onboard IT devices using 
network access control (NAC), but this capability is not extended to IoT assets. Manual 
onboarding of IoT devices is a challenge. Today, several IoT security solutions offer integration 
with NAC and next\-generation firewalls to consider a devices identity, purpose, and risk profile 
in its onboarding and network segmentation.3\.Secure: Unprotected, connected IoT devices pose high risks to all organizations. Traditional 
endpoint detection and response (EDR) solutions cannot protect such assets since they 
require software agents. IoT security solutions offer real\-time monitoring of identified IoT 
devices through network traffic. Via alerts and product integrations, they enable securing or 
quarantining of devices.4\.Optimize: For expensive IoT assets, such as imaging devices in hospitals, deep statistics ondevice utilization are important inputs for capital planning and asset optimization.5\.Manage: Real\-time monitoring, reporting, and alerting are crucial for organizations to managetheir IoT risks.6\.Retire: Devices carry personal and confidential information and are subject to compliance 
requirements in many cases. Retiring such assets becomes a managed and audited process.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t1 9Best Practice 2: Expand security to all IoT devices through 
product integrationsEnterprise IT networks are equipped with advanced IT security systems, such as next\-generation 
firewalls; NAC; and security orchestration, automation, and response (SOAR) solutions. However, 
most of these products are designedtomonitorandcontrolservers, laptops, and mobile phones
they are blind to IoT devices due to these devices custom, outdated OS builds and lack of agent 
support or IT management capabilities.Without IoT context, security solutions often misclassify IoT devices. Properly classifying IoT 
devices ensures they are only granted access to appropriate resources and placed in the right 
network segments, reducing the risk of threats to other resources and networks. IoT security 
products bring in this context, enabling IT to channel this intelligence to existing security solutions 
through product integrations.Categories of product integration include:Asset management and computerized maintenance management systems (CMMS)Security information and event management (SIEM)Security orchestration, automation, and response (SOAR)Next\-generation firewalls (NGFW)Network access control (NAC)WirelessNetwork management solutionsP a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t2 0AboutPalo Alto NetworksBillions of connected devices are coming online in every industry. 
Unfortunately, their promise of innovation and transformation has been 
accompanied by concerns of visibility, onboarding, vulnerability, service 
disruptions, business impact, ongoing management, compliance, and 
even device upgrades and retirement. Solving these problems is why 
Zingbox was founded and subsequently acquired by Palo Alto Networks in 
September 2019\.At Palo Alto Networks, we recognize that to realize the full benefit of IoT 
devices requires a revolutionary approach to performing and orchestrating 
each phase of the device lifecycle. We recognize the importance of 
traditional IT best practices as well as the positive business impact that OT 
can have. To make IoT work well requires the unique blend of IT and OT 
that we deliver. Our solution is unobtrusive, clientless, cloud\-based, and 
out of band. These capabilities are not simply the benefits of our solution
they are the underlying principles.Unit 42Unit 42 is the global threat intelligence team at Palo Alto Networks 
and a recognized authority on cyberthreats, frequently sought out by 
enterprises and government agencies around the world. Our analysts are 
experts in hunting and collecting unknown threats as well as completely 
reverse\-engineering malware using code analysis. With this expertise, 
we deliver high\-quality, in\-depth research that provides insight into 
tools, techniques, and procedures threat actors execute to compromise 
organizations. Our goal is to provide context wherever possible, explaining 
the nuts and bolts of attacks as well as whos executing them and why so 
that defenders globally can gain visibility into threats to better defend their 
businesses against them.P a l oA l t oN e t w o r k s\|U n i t4 2\|I o TT h r e a tR e p o r t2 1MethodologyThis IoT threat report was created by the Zingbox team in collaboration with 
Unit 42\. The information in this report was derived from a two\-year analysis 
of hundreds of customers and more than 1\.2 million IoT devices throughout 
2018 and 2019\. The information was gathered using Zingbox deployments 
at thousands of healthcare and enterprise locations in the United States. 
These two verticals were chosen as representative of IoT usage in critical 
infrastructures and mission\-critical business operations. Our report uses 
data from real deployments and includes the following data set:Devices analyzed:1,272,000Network sessions analyzed:73\.2 billionDevice types analyzed:8,3553000 Tannery WaySanta Clara, CA 95054Main:\+1\.408\.753\.4000Sales:\+1\.866\.320\.4788Support:\+1\.866\.898\.9087www.paloaltonetworks.com 2020 Palo Alto Networks, Inc. Palo Alto Networks is a registered
trademark of Palo Alto Networks. A list of our trademarks can be found at
https:www.paloaltonetworks.comcompanytrademarks.html. All other
marks mentioned herein may be trademarks of their respective companies.
Palo Alto Networks assumes no responsibility for inaccuracies in this document 
and disclaims any obligation to update information contained herein. Palo Alto 
Networks reserves the right to change, modify, transfer, or otherwise revise this 
publication without notice. 2020\-unit42\-iot\-threat\-report\-030620