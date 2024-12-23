# 2020 Unit 42 IoT Threat Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [01 IoT Security Landscape](#01-iot-security-landscape)
- [Organizations Lack the Tools to Discover and Secure IoT](#organizations-lack-the-tools-to-discover-and-secure-iot)
- [Enterprises Sit on a Time Bomb](#enterprises-sit-on-a-time-bomb)
- [Healthcare Is in Critical Shape](#healthcare-is-in-critical-shape)
- [Basic Network Segmentation Best Practices Aren’t Followed](#basic-network-segmentation-best-practices-arent-followed)
- [Case Study: Conficker in Healthcare](#case-study-conficker-in-healthcare)
- [02 Top IoT Threats](#02-top-iot-threats)
- [Exploits, Password Attacks, and IoT Worms Top the Chart](#exploits-password-attacks-and-iot-worms-top-the-chart)
- [Unpatched Devices and Legacy Protocols: Means of Lateral Movement](#unpatched-devices-and-legacy-protocols-means-of-lateral-movement)
- [Threats Evolving to Specifically Target IoT Environments](#threats-evolving-to-specifically-target-iot-environments)
- [Case Study: Cryptojacking in the Wild](#case-study-cryptojacking-in-the-wild)
- [03 Conclusion and Recommendations](#03-conclusion-and-recommendations)
- [Take Steps to Reduce Risk](#take-steps-to-reduce-risk)
- [Step 1: Know your risk and discover IoT devices on the network](#step-1-know-your-risk-and-discover-iot-devices-on-the-network)
- [Step 2: Patch printers and other easily patchable devices](#step-2-patch-printers-and-other-easily-patchable-devices)
- [Step 3: Segment your IoT devices across VLANs](#step-3-segment-your-iot-devices-across-vlans)
- [Step 4: Enable active monitoring](#step-4-enable-active-monitoring)
- [Perfect Your IoT Strategy](#perfect-your-iot-strategy)
- [Best Practice 1: Think holistically, orchestrate the entire IoT lifecycle](#best-practice-1-think-holistically-orchestrate-the-entire-iot-lifecycle)
- [Best Practice 2: Expand security to all IoT devices through product integrations](#best-practice-2-expand-security-to-all-iot-devices-through-product-integrations)
- [About](#about)
- [Palo Alto Networks](#palo-alto-networks)
- [Unit 42](#unit-42)
- [Methodology](#methodology)

## Executive Summary
According to a 2019 Gartner report, "By the end of 2019, 4.8 billion [IoT] endpoints are expected 
to be in use, up 21.5% from 2018." While the internet of things (IoT) opens the door for innovative 
new approaches and services in all industries, it also presents new cybersecurity risks. To evaluate 
the current state of the IoT threat landscape, the Unit 42 threat intelligence team analyzed security 
incidents throughout 2018 and 2019 with the Palo Alto Networks IoT security product, Zingbox®, 
spanning 1.2 million IoT devices in thousands of physical locations across enterprise IT and healthcare 
organizations in the United States. We found that the general security posture of IoT devices is 
declining, leaving organizations vulnerable to new IoT-targeted malware as well as older attack 
techniques that IT teams have long forgotten. This report details the scope of the IoT threat landscape, 
which IoT devices are most susceptible, top IoT threats, and actionable next steps to immediately 
reduce IoT risk. 

IoT devices are encrypted 
and unsecured
98% of all IoT device traffic is unencrypted, 
exposing personal and confidential data on 
the network. Attackers who’ve successfully 
bypassed the first line of defense (most 
frequently via phishing attacks) and 
established command and control (C2) 
are able to listen to unencrypted network 
traffic, collect personal or confidential 
information and then exploit that data for 
profit on the dark web.

57% of IoT devices are vulnerable to 
medium- or high-severity attacks, making 
IoT the low-hanging fruit for attackers. 
Because of the generally low patch level 
of IoT assets, the most frequent attacks 
are exploits via long-known vulnerabilities 
and password attacks using default 
device passwords.  

IoMT devices are running 
outdated software
83% of medical imaging devices run on 
unsupported operating systems, which is 
a 56% jump from 2018, as a result of the 
Windows® 7 operating system reaching its 
end of life. This general decline in security 
posture opens the door for new attacks, 
such as cryptojacking (which increased 
from 0% in 2017 to 5% in 2019) and 
brings back long-forgotten attacks such as 
Conficker, which IT teams had previously 
been immune to for a long time.

The internet of medical things (IoMT) devices 
with the most security issues are imaging 
systems, which represent a critical part of the 
clinical workflow. For healthcare organizations, 
51% of threats involve imaging devices, 
disrupting the quality of care and allowing 
attackers to exfiltrate patient data stored on 
these devices.

Healthcare organizations 
are displaying poor network 
security hygiene 
72% of healthcare VLANs mix IoT and IT 
assets, allowing malware to spread from users’ 
computers to vulnerable IoT devices on the same 
network. There is a 41% rate of attacks exploiting 
device vulnerabilities, as IT-borne attacks scan 
through network-connected devices in an 
attempt to exploit known weaknesses. We’re 
seeing a shift from IoT botnets conducting 
denial-of-service attacks to more sophisticated 
attacks targeting patient identities, corporate 
data, and monetary profit via ransomware.

IoT-focused cyberattacks are 
targeting legacy protocols
There is an evolution of threats targeting 
IoT devices using new techniques, such as 
peer-to-peer C2 communications and worm-
like features for self-propagation. Attackers 
recognize the vulnerability of decades-old 
legacy OT protocols, such as DICOM, and are 
able to disrupt critical business functions in 
the organization.

## 01 IoT Security Landscape
IoT is rapidly growing...

...and has a big security problem
High-profile, IoT-focused cyberattacks are forcing industries to recognize and manage IoT’s risks 
to protect their core business operations. Markets such as healthcare are exposed to an amount of 
risk that surpasses previous expectations. Some IoT vulnerabilities are life-threatening, while some 
attack critical enterprise functions or exfiltrate confidential data.
Read on to learn more about the IoT security landscape.
[^1]
[^1]: “Gartner Says 5.8 Billion Enterprise and Automotive IoT Endpoints Will Be in Use in 2020,” Gartner, August 29, 2019, 
https://www.gartner.com/en/newsroom/press-releases/2019-08-29-gartner-says-5-8-billion-enterprise-and-
automotive-io.

By the end of 2019, IoT adoption grew to an estimated 4.8 
billion devices, an increase of 21.5% from the end of 2018.[^1]
More and more newly developed IoT devices are network- 
or internet-connected.
By now, more than 30% of all network-connected 
endpoints are IoT devices (excluding mobile devices) at 
the average enterprise.
98% of all IoT traffic is unencrypted, exposing personal 
and confidential data on the network.
57% of IoT devices are vulnerable to medium- or high-
severity attacks, making IoT the low-hanging fruit for 
attackers.

83% of medical imaging devices run on unsupported 
operating systems—a 56% jump from 2018, as a result of 
Windows 7 reaching its end of life.

## Organizations Lack the Tools to Discover 
and Secure IoT
Enterprises face a significant challenge in not knowing the risk exposed by IoT devices and 
applications. The main reasons are lack of device discovery and inventory.  
IT’s lack of IoT visibility
An outdated, static inventory of IoT assets checks a box, but is far from effective security 
management. The identification of devices using traditional IT device characteristics, such as IP 
addresses and underlying operating systems is not working for IoT. Only by identifying the specific 
type of device can an organization accurately plan its network access requirements, deployment 
tactics, security strategy optimization, and operations plans. Once device identities are determined, 
security systems can track device behavior in the context of the organization’s workflows rather 
than just viewing them as dynamic, changing IP addresses of an unknown device type.

Existing security systems don’t support IoT
Endpoint protection systems are designed for computers, tablets, and phones with the ability to 
run agents, but IoT devices often run custom or outdated operating systems without such ability. 
As a result, cybersecurity systems see IoT devices as unknown endpoints, and thus do not know the 
specific device type, its risk profile, and its expected behavior.

Network-based cybersecurity systems have the visibility to identify network-connected endpoints, 
but they rarely incorporate the ability to accurately identify, track, and secure IoT devices.

Organizational and human resource challenges between OT 
and IT
Most organizations manage information technology (IT) and operational technology (OT) as 
separate teams with separate processes and tools. While IT focuses on the organization’s IT 
assets—such as computers, network equipment, and printers—OT focuses on non-IT assets, such 
as medical devices and security cameras.

As these teams report to different parts of the organization, they have different ways to maintain 
device security. Often, IT is more advanced in this respect because of the rapid evolution of personal 
computers and server operating systems as well as their proactive security operations in contrast to 
medical devices.

As a healthcare example, in hospitals, biomedical engineers know and maintain the medical 
devices, but they don’t maintain the underlying operating systems that power the devices. As these 
network-connected medical devices (such as X-RAY machines) often run end-of-life operating 
systems with known vulnerabilities, they pose a high risk to the organization’s employees, patients, 
computer systems, and—eventually—business operations.

## Enterprises Sit on a Time Bomb
When we work on a device other than a desktop, laptop, or phone, that’s an IoT device. We see them 
in our offices every day: IP phones, printers, etc. These network-connected devices are all targets 
for attackers, and they often aren’t properly maintained by IT.

Good news for IP phones: They account for 44% of all enterprise IoT devices but only 5% of all security 
issues. Used across a wide range of industries, IP phones are often designed to be enterprise-grade in both 
reliability and security.

![Image of a bar graph showing Enterprise IoT Devices vs Security Issues. IP Phone has 44% of devices and 5% of security issues. Printer has 18% of devices and 24% of security issues. Intercom System has 24% of devices and 7% of security issues. Consumer Electronics has 9% of devices and 5% of security issues. Camera has 5% of devices and 33% of security issues. Other has 0% of devices and 5% of security issues. Tracking and Locating Systems has 1% of devices and 1% of security issues. Wearable has 3% of devices and 3% of security issues. IoT Gateway has 1% of devices and 2% of security issues. Energy Management has 3% of devices and 6% of security issues.]

Security cameras 
make up only 5% of 
enterprise IoT devic­
es, but they account 
for 33% of all security 
issues. This is be­
cause many cameras are designed to be 
­
consumer-grade, focusing on simplicity of 
use and ­
deployment over security.

What can an attacker do with 
a security camera?
In 2016, teen scammers initiated the large-
scale Mirai attack, involving more than 
600,000 CCTV cameras, to scan big blocks 
of the internet for open telnet in an attempt 
to log in using default passwords.

Printers account for 
18% of IoT devices 
and 24% of security 
incidents. They have 
­
inherently less built-in 
security, and vulnera­
bilities in browser interfaces often make 
them ideal targets as entry points for 
launching cyberattacks.

How dangerous is a printer on the loose? 
They can:
- Provide access to print logs
- Open up lateral movement to other 
computers on the network
- Be used as part of a DDoS attack

_Figure 1: IP phones have only 5% of all security issues_

## Healthcare Is in Critical Shape
![Image of a bar graph showing Medical IoT Devices vs Security Issues. Infusion Pump has 44% of devices and 11% of security issues. Imaging System has 16% of devices and 51% of security issues. Patient Monitoring has 14% of devices and 1% of security issues. Point of Care Analyzer has 4% of devices and 5% of security issues. Nurse Call System has 4% of devices and 9% of security issues. Medical Device Gateway has 3% of devices and 1% of security issues. Medication Dispensing has 2% of devices and 0% of security issues. ECG Machine has 1% of devices and 0% of security issues. Defibrillator has 1% of devices and 0% of security issues. Other has 1% of devices and 2% of security issues.]

![Image of a pie chart showing Medical devices running outdated operating systems. 17% are in Active Support, 83% are No Support. Active support is broken down into: Win 7 56%, Win 8.1 2%, Linux 2%, Embedded 2%, Win 10 11%, Win (other) 2%. No Support is broken down into: Unix 3%, Linux 4%, Embedded 7%, WinXP 11%.]

Medical devices running outdated operating systems
Due to their long lifecycles, medical IoT devices are 
among the worst offenders of running outdated and, 
in many cases, end-of-life operating systems. These 
devices are neither maintained by IT nor supported by 
the operating system vendors.

Security function missing in the organization 
Biomedical engineers who maintain medical devices 
often lack training and resources to follow IT security 
best practices to employ password rules, store pass­
words securely, and maintain up-to-date patch levels 
on devices.

Imaging systems run on various 
operating systems, including 
Windows, Linux, and Unix. As 
of this writing, 83% of all medi­
cal imaging systems run on end-
of-life operating systems with 
known vulnerabilities and no 
security updates or patch sup­
port. This is a 56% jump from 
2018 as a result of ­
Windows 7 
reaching its end of life.

New attacks exploit vulnerabil­
ities in the underlying operating 
system to target medical IoT 
devices. Imaging systems are 
particularly susceptible to this 
kind of attack due to support 
for their underlying OS expiring 
well before the devices are re­
tired or decommissioned.

Good news: The National 
Cybersecurity Center of 
Excellence (NCCoE) completed 
a medical IoT device security 
project in 2019 called Securing 
Picture Archiving and Commu­
nication Systems (PACS) to 
provide guidance and reference­
able architecture for securing 
the PACS ecosystem and to 
include example solutions 
using existing commercial and 
open source cybersecurity 
products. 

Progress: A new bill 
in the US ­
Congress 
attempts to address 
smart-device se­
curity regulations. 
The IoT Cyberse­
curity Act of 2019 
states that NIST 
should settle on 
standards for the 
secure develop­
ment of IoT devic­
es, device man­
agement, patching, 
and ­
configuration 
management. 

Imaging systems are extremely vulnerable
A 2019 Gartner survey found that 40% of healthcare CIOs plan to spend new or additional funds on 
cybersecurity tools in 2020.[^2] For the time being, medical devices are in a critical state.

_Figure 2: Medical devices and security issues_

_Figure 3: Smart device security regulations_

[^2]: "2019 Top Actions for Healthcare Provider CIOs: Summary and Retrospective View," Gartner, February 26, 2019, 
https://www.gartner.com/en/documents/3903067/2019-top-actions-for-healthcare-provider-cios-summary-an.

## Basic Network Segmentation Best 
Practices Aren’t Followed
The simplest IoT risk remediation practice is network segmentation. Despite this, only 3% of all 
segmented networks or virtual local area networks (VLANs) in the healthcare organizations we 
studied contained strictly medical IoT devices, and 25% contain non-medical IoT devices (IP 
phones, printers, etc.).

Network segmentation isn’t enough: Microsegmentation is ideal
While the overall trend is encouraging, network segmentation alone is not sufficient. For instance, 
housing mission-critical heart rate monitors in the same network as imaging systems would not be 
a sound practice. A device profile-based microsegmentation approach that considers a multitude of 
factors, including device type, function, mission criticality, and threat level, provides an isolation 
approach that significantly reduces the potential impact of cross-infection.

![Image of a pie chart showing VLAN mix. 72% are Mixed, 25% are Non-Medical Only, 3% are Medical Only.]

72% of healthcare VLANs house a mix of 
medical IoT devices, generic enterprise 
IoT devices, and IT devices. This ­
lowers 
the barrier for lateral movement. For 
example, an infected laptop can easily 
target surveillance cameras and DICOM 
viewers found in the same network. 
This is low-hanging fruit for healthcare 
­
organizations to address this year.

This is still more than a 
threefold improvement 
from 2017
Although there is room 
for improvement, we 
observed an increasing 
adoption of network 
­
segmentation:
- In 2017, only 12% of 
hospitals ­
employed 
more than 20 VLANs.
- In 2019, this number 
rose to 44%.

![Image of a bar graph showing VLAN usage in hospitals. 2017 and 2019 are compared. 0-9 VLANs: 2017: 25%, 2019: 16%. 10-19 VLANs: 2017: 16%, 2019: 2%. 20-29 VLANs: 2017: 2%, 2019: 31%. 30-39 VLANs: 2017: 43%, 2019: 45%. 40-49 VLANs: 2017: 2%, 2019: 4%. 50-59 VLANs: 2017: 4%, 2019: 0%. 60-69 VLANs: 2017: 0%, 2019: 0%. 70-79 VLANs: 2017: 0%, 2019: 2%. 80-89 VLANs: 2017: 1%, 2019: 0%. 90-99 VLANs: 2017: 1%, 2019: 1%. 100+ VLANs: 2017: 5%, 2019: 0%.]

_Figure 4: VLANs have a mix of medical IoT devices_

_Figure 5: More than a threefold increase in use of VLANs at hospitals_

## CASE STUDY: Conficker in Healthcare 
Zingbox, the Palo Alto Networks IoT security product, alerted one of the hospitals of Conficker 
traffic detected in its network. The offending device was a mammography machine. In the days 
following, Zingbox identified another mammography machine, a DICOM (Digital Imaging and 
Communications in Medicine) viewer, a digital radiology system, and a few other infected devices 
exhibiting Conficker behavior.

The hospital staff responded by turning these devices 
off when they were not in use. To verify the infection, 
the staff took one of the infected mammography 
machines and the DICOM viewer offline to re-image 
them. Within hours of the devices coming back online, 
Conficker infected them again.

Further investigation revealed that while re-imaging 
the devices had removed the malware, the approved 
images were outdated: they did not include the latest 
security patches, leaving the devices vulnerable to 
Conficker. Given the peer-to-peer nature of how 
Conficker spreads on a network, it was only a matter 
of time before another infected device passed the virus 
back along.

The hospital then took all infected devices offline, ­
re-imaged them, installed the latest security patches, 
and brought back the devices online one by one, closely 
monitoring anomalous behaviors. Over the span of a 
week, the devices were reintroduced to the network and 
showed no further signs of Conficker infection.

This is a typical example of the challenges many 
organizations face today. They are hampered by a 
lack of real-time visibility into IoT device behavior 
and the cybersecurity expertise to quickly respond to 
threats, contain the spread of infection, and eradicate 
the underlying cause. In some organizations, the 
critical nature of their devices makes troubleshooting, 
shutdown, and re-imaging impossible or extremely 
difficult to do without disrupting business operations. 
As a result, many organizations find themselves in 
an endless loop of simply treating the symptoms and 
hoping for the best.

Conficker 
is back! 
Conficker, 
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
home users in 190+ countries. Once 
IT teams and antivirus vendors 
could finally counter the worm, 
they were able to reduce infected 
computers to 1.7 million by 2011 and 
400,000 by 2015.

More recently, IT teams had long 
since forgotten the worm—until 
it started appearing again on 
medical devices running outdated 
or unsupported Windows OS 
versions. At the time of this report, 
nearly 20% of Zingbox healthcare 
customers have been infected by 
Conficker at some point in time.

## 02 Top IoT Threats
Threats continue to evolve and target IoT devices with new techniques, 
such as peer-to-peer C2 communications and worm-like self-propagation.
This evolution is enabled by a weak device and network security posture:
- 72% of healthcare VLANs mix IoT and IT assets, allowing malware 
to spread from users’ computers to vulnerable IoT devices on the 
same network.
- 41% of attacks exploit device vulnerabilities, as IT-borne attacks 
scan through network-connected devices in an attempt to exploit 
known weaknesses.
- Decades-old legacy OT protocols, such as DICOM, are attacked to 
disrupt critical business functions or propagate throughout in the 
organization.

The gap between OT and IT security practices and operations enables 
attacks that IT has otherwise been immune to for over a decade.
Read on to learn more about our findings on top threats and attack 
techniques.

41%
of attacks exploit
device vulnerabilities
of healthcare VLANs
mix IoT and IT assets
72%

## Exploits, Password Attacks, and IoT 
Worms Top the Chart
No. 1: Exploits 
targeting device 
vulnerabilities
While the security postures 
of IoT devices make them 
easy targets, in most cases, 
the devices are only used as 
stepping stones in lateral 
movement to attack other 
systems on a network.

We’re seeing a large number of 
network scans, IP scans, port 
scans, and vulnerability scans on 
networks, attempting to identify 
other devices and systems, 
looking for targets for the next 
step in lateral movement.

No. 2: Password attacks
Default, manufacturer-set passwords and poor password security practices continue to fuel password-
related attacks on IoT devices. With California’s SB-327 IoT law now prohibiting the use of default 
credentials, we expect this trend to change direction.

Operational misalignment also enables password-targeted 
attacks. In many cases, passwords chosen by OT staff are not in 
line with IT’s more advanced password policies and password 
management practices. This is one example of organizational 
misalignment between OT and IT.

No. 3: IoT worms are becoming more 
common than IoT botnets
We’re witnessing a shift away from attackers’ primary 
motivation—running botnets to conduct distributed denial-of-
service (DDoS) attacks via IoT devices—to malware spreading 
across the network via worm-like features, enabling attackers to 
run malicious code to conduct a wide variety of new attacks.

Wireless routers 
under threat
Unit 42 found a Gafgyt variant 
targeting more than 32,000 po­
tentially vulnerable small office 
and home wireless routers to 
conduct a botnet attack against 
gaming servers on the internet.

Today, wireless routers are 
some of the most common IoT 
devices in organizations, making 
them targets for IoT botnets, 
degrading both the production 
network and the reputation of 
the IP addresses of affected 
companies.

![Image of a pie chart showing the breakdown of top IoT threats. Exploits 33%, Malware 41%, User Practice 26%. Malware is broken down into: Zero-Day 3%, Worm 12%, SQL Injection 4%, Others 5%, Buffer Overflow 5%, Command Injection 5%, Remote Code Execution 5%, Network Scan 14%, Cryptojacking 5%, Phishing 8%, Password 13%, Ransomware 8%, Backdoor Trojan 7%, Botnet 6%.]

_Figure 6: Breakdown of top IoT threats_

## Unpatched Devices, Legacy Protocols: 
Means of Lateral Movement
Low patch levels
IoT exploits represent a unique challenge because they often involve legacy OS that don’t offer 
security updates anymore. We found that 83% of medical imaging devices run end-of-life, 
unsupported OS. This means old, well-known exploits can still pose significant threats to them.

Aged OT protocols are targets
We observed vulnerabilities in aged industry 
OT protocols. These protocols were designed 
to run on devices behind the firewall without 
much interference with other systems or users. 
As the network perimeter disappearing with 
the shift toward cloud technologies, these 
decades-old protocols get exposed to the hustle 
and bustle of today’s enterprise networks.

Lateral movement
We see lateral movements originating from 
successful phishing attacks targeting IoT 
systems on the same network and exploiting 
vulnerabilities remotely. 57% of IoT devices are 
vulnerable to medium- or high-severity attacks, 
making IoT the low-hanging fruit for attackers.

Two-staged attacks through backdoors left untreated
Backdoors installed from previous breaches are often overlooked or not properly disabled, 
lowering the barrier of entry for a wide range of other attacks. As an example, we’re seeing 
WannaCry ransomware attacks spreading through backdoors left open by previous Pebble Pulser 
malware infections.

With the growing number of unpatchable devices, such as those running Windows 7, we’re not expecting 
this trend to turn around unless more organizations follow the best practices in these materials.

Legacy OT protocol hack story 
We found a vulnerability in the DICOM 
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
privacy reasons—essentially, this malware 
was protected by design.

## Threats Evolving to Specifically Target 
IoT Environments
Peer-to-peer features
We see an evolution of threats targeting IoT 
environments by way of decentralized peer-to-peer 
C2 communications wherein compromised devices—
controlled by one node over a server connection—
communicate with each other on the local network. 
This lets attackers minimize connections to the 
outside world and enables the swarm to operate even 
without an internet connection.

Vulnerabilities in cloud-connected IoT devices (e.g., 
security cameras with remote viewing capabilities) 
enable attackers to bypass firewalls and access 
private networks.

Fight for the host
We have observed a trend of malware attempting 
to remove other malware to occupy the victim IoT 
device exclusively. This is likely to address hardware 
resource constraints, as device manufacturers 
minimize the hardware capacity in their purpose-
built boards to reduce energy consumption and 
retail prices.

Leaked IoT malware code fuels 
new varieties
The leakage of the IoT botnet Mirai’s source code has 
fueled the birth of numerous Mirai variants in the past 
year. Adversaries have been building these variants in 
a fashion similar to the way open source developers 
fork new code versions from each other’s work.

Now, Mirai has grown into a framework to which developers can add new device exploits as new variants.

Mirai botnet attack
Mirai malware turns networked 
devices running Linux into remotely 
controlled bots that can be used as 
part of a botnet in large-scale network 
attacks. It primarily targets online 
consumer devices, such as IP cameras 
and home routers.

On October 12, 2016, a massive DDoS 
attack brought about by a Mirai botnet 
made much of the internet inaccessible 
on the east coast of the US. Authorities 
initially feared this attack was the 
work of a hostile nation-state.

WannaCry ransomware 
spreading on unsegmented 
networks 
When we come across WannaCry cases 
on healthcare customers’ networks, 
they are always mixed networks 
with PCs, scanners, nuclear imaging 
devices, etc. WannaCry has a strong 
self-propagation and infection 
capability, enabling it to cross-infect 
devices across IoT and IT.

## CASE STUDY: Cryptojacking in the Wild
Zingbox alerted a customer participating in this research about a cryptomining code transfer 
between an IT storage device and an OT device in its internal network. The IT team wanted to shut 
down the device, but the OT team disagreed due to production safety concerns. While waiting for the 
device to be allowed to go offline, the IT staff investigated the storage device as Zingbox continued 
to monitor the network traffic for further malicious activities.

The next day, cryptomining code transfer was again detected on the network. Further investigation 
identified the offending device as a server that hosted hundreds of VM guests on the OT network, 
making the offending VM guest difficult to find. Continuous network traffic monitoring revealed 
a twice-weekly scheduled data transfer. The regular pattern enabled the IT staff to identify the 
offending process and offending VM guest, which they then removed from the VM host.

Cryptojacking malware is an emerging online threat that hides on a device and uses the 
machine’s resources to “mine” forms of cryptocurrency, such as bitcoin. Like most malicious 
attacks, the motive is profit, but unlike most, it’s designed to stay hidden from the user. 
Cryptojacking causes high CPU and network usage and drains critical healthcare systems, 
potentially impacting life-saving capabilities.

![Image of a graphic showing Cryptojacking drains critical healthcare systems]

_Figure 7: Cryptojacking drains critical healthcare systems_

## 03 Conclusion and Recommendations
CSOs can take steps now to reduce their IoT risk...
CSOs can immediately act to reduce their organizations’ exposure to IoT-initiated attacks. 
These steps aren’t comprehensive, but they reduce a large share of IoT risks:
1. Know your risk—discover IoT devices on the network
2. Patch printers and other easily patchable devices
3. Segment IoT devices across VLANs
4. Enable active monitoring

… and an effective IoT strategy prepares the organization in 
the long term.
To know and manage risk proactively, an organization needs an effective IoT security strategy. 
Our research team chose two additional practices every IoT strategy should incorporate:
1. Think holistically: orchestrate the entire IoT lifecycle
2. Expand security to all IoT devices through product integrations

## Take Steps to Reduce Risk
### Step 1: Know your risk—discover IoT devices on the network
IoT security solutions enable organizations to discover and identify IoT devices on their networks. 
We found that 30% of network-connected devices in an average enterprise are IoT assets, excluding 
smartphones. Although this a significant number of assets, most organizations are unaware of 
these devices and don’t manage their security postures or risk profiles.

Intelligent device scanning and profiling enables IT security teams to have visibility of their 
network-connected IoT devices, their risk profiles, and their network behavior when interacting 
with other devices on the network. Today’s most advanced IoT security solutions, such as Zingbox, 
use machine learning to identify even never-before-seen IoT devices and recognize malicious 
network communication patterns before they cause damage.

Discovering IoT devices’ internet connectivity profiles is important. IoT devices with direct internet 
access can carry higher risk profiles because internet connectivity allows exploits to move faster than 
they can on devices that are only LAN-connected. Even so, purely LAN-connected IoT devices expose 
a larger practical risk: These devices have been built with the assumption of safety behind a firewall. 
Compared to internet-connected, SaaS-based assets, we're seeing more cleartext communication, 
open ports, and weak credentials being used on these devices. A computer network in which 
employees and such devices are mixed presents the challenge of user devices cross-infecting IoT assets.

As soon as IT discovers the devices and acknowledges their risk profiles, they can start the 
remediation work.

### Step 2: Patch printers and other easily patchable devices
Our research shows printers and security cameras are the most abundant and vulnerable devices 
across enterprise networks. In healthcare, imaging and patient monitoring systems top the charts.

After initial IoT device discovery, we recommend investigating the security posture of the top two 
or three most abundant network-connected devices and working with their respective vendors on a 
patch management strategy for routine maintenance moving forward.

### Step 3: