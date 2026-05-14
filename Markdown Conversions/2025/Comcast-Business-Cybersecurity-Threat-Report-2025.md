# 2025 Comcast Business Cybersecurity Threat Report

## Table of Contents
- [Foreword by Noopur Davis](#foreword-by-noopur-davis)
- [Executive Summary](#executive-summary)
- [What the Threat Landscape Is Telling Us](#what-the-threat-landscape-is-telling-us)
- [Key Data Findings](#key-data-findings)
- [The 2025 Cybersecurity Prism: Building Enterprise Resilience with Layered Security](#the-2025-cybersecurity-prism-building-enterprise-resilience-with-layered-security)
- [Bringing the Data to Life](#bringing-the-data-to-life)
- [Attack Stage 1: Identifying Targets & Testing Defenses](#attack-stage-1-identifying-targets--testing-defenses)
- [The Human Element](#the-human-element)
- [Attack Stage 2: Establishing a Foothold](#attack-stage-2-establishing-a-foothold)
- [The Hidden Threat: Proxy Abuse and Masked Adversaries](#the-hidden-threat-proxy-abuse-and-masked-adversaries)
- [Attack Stage 3: Digging Deeper & Expanding Reach](#attack-stage-3-digging-deeper--expanding-reach)
- [MDR & EDR: Elevating Detection from Reactive to Proactive](#mdr--edr-elevating-detection-from-reactive-to-proactive)
- [Attack Stage 4: Playing Out the Endgame](#attack-stage-4-playing-out-the-endgame)
- [DDoS: Escalating Scale and Sophistication](#ddos-escalating-scale-and-sophistication)
- [Recommendations for Strengthening Defense](#recommendations-for-strengthening-defense)
- [How Comcast Business Can Help](#how-comcast-business-can-help)

---

## Foreword by Noopur Davis
_Executive Vice President, Chief Information Security and Product Privacy Officer, Comcast_

The cybersecurity environment we face in 2025 is unlike any that has come before. Threats are growing in scale, stealthiness, and sophistication. But this is also a transformative time for cyber defense, with advances in AI, automation, and industry collaboration opening new opportunities to innovate.

Technology is a defining factor in this landscape. Artificial intelligence (AI), in particular, is reshaping the cyber battlefield by introducing not only new risks, but also powerful tools for defenders to outpace their adversaries. Yet even with these advances, one reality remains unchanged: people make the difference. Skilled professionals are essential to interpret subtle signals, investigate anomalies, and make rapid decisions when an incident unfolds. People, paired with advanced technology, are what ultimately determines resilience.

At Comcast, we are in a unique position to see what many others cannot. Our visibility spans across vast residential and business networks, giving us early insights into the trends and tactics shaping today’s threat landscape. This perspective strengthens our defenses and directly informs the services we deliver through Comcast Business. By combining multi-layered security solutions with deep security operations center (SOC) expertise, we help organizations simplify complexity, extend their capabilities, and respond with confidence in a high-stakes environment.

This cybersecurity threat report is the product of that commitment. It distills learnings from billions of real-world events, advanced analytics, and cross-industry intelligence to provide decision-makers with actionable insights on where to focus their defenses. The goal is not just to inform, but to empower leaders with a clear view of current risks and opportunities, so they can focus effort where it matters most and build stronger, more resilient organizations.

My call to you is simple: use the insights in this report to strengthen defenses, rethink risk, and embrace partnerships. Cybersecurity is a collective effort. By working together, we can not only stay ahead of the threats but also harness innovation to protect what matters most.

---

## Executive Summary

In 2025, enterprise leaders find themselves operating in a global threat landscape characterized by accelerating scale and sophistication.

As adversaries weaponize artificial intelligence, double down on exploiting human trust, and adopt more sophisticated evasion tactics, the traditional calculus for managing enterprise risk is being fundamentally rewritten. Business and technology leaders are now tasked with defending an expanding attack surface against threats that are greater in volume and attackers that are more adept at blending in with normal business activity.

This report draws from the analysis of 34.6 billion cybersecurity events Comcast Business detected from June 1, 2024 through May 31, 2025 across its cybersecurity customers. It provides data-driven intelligence on how the tactics used by cyber adversaries are evolving, alongside the advanced strategies and technologies organizations can deploy to counter them. Ultimately, this report equips leaders with the intelligence needed to better assess organizational exposure, anticipate adversary evolution, and proactively adapt defenses.

The numbers presented throughout the report represent the collective and anonymized data of customers leveraging Comcast Business security offerings, including distributed denial of service (DDoS) mitigation, endpoint detection and response (EDR), vulnerability scanning and exposure management, managed detection and response (MDR), and other services. Our internal data, mapped to the MITRE ATT&CK® framework, is complemented by industry research, insights from our vendor partners, and the expertise of Comcast’s security product, threat intelligence, and operations teams.[^1]

[^1]: ©2025 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.

---

## What the Threat Landscape Is Telling Us

- **Threat Volume and Velocity Continue to Grow**: Attacks are growing in volume, speed, scale, and stealth. Attackers blend high-volume, automated threats with “low-and-slow” tactics that evade traditional detection.
- **Human Factors and Fatigue Stymie Security Efforts**: Security teams are under intense pressure, facing burnout from alert overload. End-users remain a primary target and are often the weakest link.
- **AI is an Enabler as Well as a Risk Multiplier**: Threat actors are leveraging generative AI to craft more convincing phishing lures. Enterprise adoption of LLMs and "shadow AI" broaden the attack surface. Defenders are deploying AI and machine learning to scale anomaly detection.
- **Multi-Layered and Adaptive Defense Is Critical**: Many threats exploit basic security lapses like unpatched systems and weak credentials. Organizations must evolve their prevention, detection, and response capabilities.
- **It’s Time to Rethink Enterprise Risk**: Cybersecurity is no longer just IT’s challenge. It is a board-level business continuity, resilience, and reputational challenge.

---

## Key Data Findings

34.6 billion cybersecurity events analyzed, including:

- **19.5B**: Resource development events related to botnet activity.
- **9.7B**: Drive-by compromise events attempting to install malware.
- **4.7B**: Phishing events attempting to compromise credentials or deliver malware.
- **44K**: DDoS attacks attempting to test or overwhelm defenses.

---

## The 2025 Cybersecurity Prism: Building Enterprise Resilience with Layered Security

In 2025, cybersecurity is inseparable from business resilience. A successful breach is not just a technological event; it can disrupt operations, impact revenue, and damage reputation. Multi-layered defense is a cornerstone of organizational resilience.

Resilient security anticipates that some defenses will fail. By layering protection across the network, cloud, endpoints, and people, businesses can detect and contain threats more quickly. Technology alone is not enough; skilled analysts and threat hunters are critical to interpret signals, prioritize risks, and act decisively.

---

## Bringing the Data to Life

To provide clarity, this report maps security log data against the MITRE ATT&CK® framework. We have organized the narrative into four stages:

1. **Identifying Targets & Testing Defenses**: Reconnaissance, Resource Development, Initial Access.
2. **Establishing a Foothold**: Execution, Persistence, Privilege Escalation.
3. **Digging Deeper & Expanding Reach**: Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection.
4. **Playing Out the Endgame**: Exfiltration, Impact.

---

## Attack Stage 1: Identifying Targets & Testing Defenses

### Reconnaissance is Constant
Every day, threat actors probe common entry points such as firewalls, web servers, and IoT devices. Automation has supercharged reconnaissance, with Fortinet recording a 16.7% year-over-year surge in automated global scanning.

### DDoS Short Bursts as Reconnaissance
Comcast Business detected an increase in short-duration (less than 5 minutes) DDoS attacks used to "jiggle the locks" on network defenses. 

### The Scale of Common Vulnerabilities and Exposures (CVEs)
- 2020: 18,375
- 2021: 20,161
- 2022: 25,059
- 2023: 28,961
- 2024: 40,077

---

## The Human Element

In cybersecurity, technology sets the stage, but people determine the outcome. While security strategies emphasize AI and automation, human behavior remains a significant variable. 

- **Staffing Shortages**: The global cybersecurity workforce gap has widened to 4.76 million professionals, and 67% of organizations report a staffing shortage.
- **Empowerment**: Leading organizations are investing in tools that augment human judgment, reducing burnout while sharpening response capabilities.

---

## Attack Stage 2: Establishing a Foothold

### Stealthy Execution
After penetrating a system, attackers avoid noisy exploits. They "live off the land," enlisting tools such as PowerShell, WMI, and scripting languages to run code. 

### AI Agents & Non-Human Identities (NHIs)
As enterprises deploy AI agents, the attack surface expands to include NHIs (API keys, service accounts). These credentials are proliferating at a massive scale and create significant blind spots for defenders.

---

## The Hidden Threat: Proxy Abuse and Masked Adversaries

Attackers increasingly hide behind "residential proxies" (ResProxies)—co-opting internet-connected devices in homes and businesses so malicious requests appear to come from ordinary IPs. 

![Diagram showing bad actors using proxy marketplaces to route traffic through compromised devices to target endpoints.]

---

## Attack Stage 3: Digging Deeper & Expanding Reach

### Quiet Lateral Movement
Attackers perform internal discovery and lateral movement slowly to blend in with legitimate user activity. 

### Credential Harvesting
"Credentials are the keys to the kingdom." Attackers use tools like LaZagne or built-in OS commands to dump passwords and hashes. Info-stealer malware has shifted credential theft into overdrive.

---

## MDR & EDR: Elevating Detection from Reactive to Proactive

Managed Detection and Response (MDR) and Endpoint Detection and Response (EDR) are essential for modern defense. By combining advanced technology with human expertise, these services allow organizations to:
- Detect threats early in the attack chain.
- Automate responses to common threats.
- Provide 24/7 monitoring to identify subtle anomalies that automated tools might miss.

---

## Attack Stage 4: Playing Out the Endgame

The final stage involves command and control, data exfiltration, and the ultimate payload (ransomware, data destruction). The goal of the defender here is to minimize the "blast radius" through rapid containment and incident response.

---

## DDoS: Escalating Scale and Sophistication

DDoS attacks are evolving. Beyond simple volume-based attacks, we are seeing:
- **Carpet Bombing**: Spreading attack traffic across many target IPs simultaneously.
- **Short-Burst Reconnaissance**: Using quick hits to test mitigation thresholds.

---

## Recommendations for Strengthening Defense

1. **Adopt a Zero Trust Architecture**: Verify every access request, regardless of origin.
2. **Prioritize Patch Management**: Use a risk-based approach to address critical vulnerabilities.
3. **Implement Phishing-Resistant MFA**: Move beyond SMS-based codes to hardware keys or biometric authentication.
4. **Invest in Human Expertise**: Pair automated tools with skilled analysts to handle complex investigations.
5. **Monitor for LOTL Techniques**: Baseline normal system behavior to detect the abuse of legitimate tools.

---

## How Comcast Business Can Help

Comcast Business provides scalable, multi-layered security solutions to counter modern threats. Our comprehensive portfolio integrates:
- Network firewalls and intrusion prevention.
- Vulnerability and exposure management.
- Cloud security.
- Sophisticated detection and response (EDR, NDR, MDR).
- DDoS mitigation.

By combining these technologies with around-the-clock monitoring and a team of skilled analysts, Comcast Business helps organizations detect, prevent, and respond to threats with speed and precision.

---

modified to hinder
detection and allow malicious activity to go unnoticed.

Masquerading (T1036): Malicious files, tasks, or services are
disguised to look legitimate by manipulating their names,
locations, or other features to evade detection.

Obfuscated Files or Information (T1027): Files or information
are encrypted, encoded, or compressed to make their malicious
contents difficult for security tools to discover and analyze.

Subvert Trust Controls (T1553): Security controls that rely on trust,
such as code signing or download warnings, are undermined to
allow malicious programs to execute without alerts.

Key Takeaway

Cover-up behavior is expected in modern breaches. Security teams must
deploy controls to make evasion harder (e.g. disable unnecessary scripting
tools, enforce Windows Event Log retention and forwarding) and employ
detection methods that focus on anomalies and attacker techniques.

24 Adversaries may abuse these common files to execute malicious
code or deliver malware—rundll32.exe, regsvr32.exe, wscript.exe.

29
29

SOC Casebook

Workplace Chat Tool Phished
for Remote Takeover

A threat actor initiated external workplace chats posing as
the customer’s IT support, an example of the MITRE ATT&CK®
initial access sub-technique called spearphishing via service
(T1566.003). Several employees accepted the invites and
followed instructions to “fix a security issue,” downloading a
legitimate-looking remote access tool from a public URL.

Launching the installer triggered user execution (T1204.002),
after which the program silently registered itself as a
service, granting the adversary interactive control over each
workstation through external remote services (T1133). The
attacker was now positioned to perform privilege escalation,
harvest data, or deploy ransomware.

Comcast Business security analytics and SOC analysts
correlated the sudden burst of external chat sessions with
first-time downloads of remote-administration binaries
across multiple hosts. Our analysts quarantined the
compromised machines and disabled the affected accounts,
contacting the customer to begin reimaging and resetting
credentials. The swift response severed the attacker’s live
sessions, blocked lateral movement, and helped prevent
potential data exfiltration or ransomware deployment.

SOC Insights:
Chat platforms are
phishing venues:
External chat invites can
bypass email filters.

Legitimate tools are
used for malicious
activity: Off-the-shelf
remote access software
gives attackers hands-on
control while evading
basic malware defenses.

Rapid quarantine
contains damage:
Isolating endpoints and
disabling accounts cut
C2 channels, preventing
escalation to data
theft or ransomware.

30

MDR & EDR: Elevating
Detection from
Reactive to Proactive

In cybersecurity, time is often the most critical factor. Attackers attempt to
blend in with legitimate activity not just to be stealthy but to buy the time
needed to achieve their objectives. This is why detect-and-response tools,
whose primary function is to shrink the window between initial compromise
and decisive response, matter more in 2025 than ever before.

Once an attacker gains a foothold, the clock starts ticking. It can take mere
minutes for an adversary to escalate privileges and move laterally across the
network—a concept known as “breakout time.”

Our data includes detections across early post-compromise MITRE techniques
and sub-techniques such as Windows Management Instrumentation (T1047),
process injection (T1055), DLL injection (T1055.001), and Software Packing
(T1027.002). Responses to these detections interrupt attackers before they
have time to escalate privileges or move laterally, which are key steps on the
path to compromising data.

Our analysis also reveals how MDR provides crucial opportunities to get
ahead of the attacker’s timeline altogether. By combining threat intelligence
with anomalous behavior detection, these tools can pick up signals that
point to early-stage resource development techniques, including acquiring
or compromising infrastructure (T1583, T1584) and developing malicious
capabilities (T1587). This helps move response further to the left in the attack
chain often disrupting threats before a foothold can be established.

But automated detection is only one part of the solution.

The Human Element: Threat Hunting at Scale
Continuous threat hunting provides active defense, unlike passive alerting.
Skilled hunters proactively search networks, cloud, and endpoints for subtle
indicators of compromise that evade automated tools. This is vital because
our analysis shows that some of the most frequent alerts don’t necessarily
indicate an attack, with benign alert rates hitting 96% for some alert types.
The volume of these false alerts can cause significant analyst fatigue, thus
underscoring the importance of proactive threat hunting.

Why It Matters for Enterprises

Rapid triage and prioritization using AI-augmented
analytics to separate signal from noise.

Cross-kill-chain correlation to connect seemingly unrelated
events and reveal coordinated attack campaigns.

24/7 monitoring helps prevent high-priority alerts being
missed during off-hours or resource gaps.

31

Attack Stage 4

Playing Out
the Endgame

In the final stage of an attack, adversaries attempt to
take charge by establishing command and control (C2)
channels to manipulate compromised systems, attempt
to exfiltrate sensitive data, and execute impact actions
(ransomware deployment, data destruction, fraud, etc.).

MITRE Tactics Covered:
Command and Control | TA0011
Exfiltration | TA0010
Impact | TA0040

Encrypted and Covert
Command and Control Traffic
The endgame phase of an intrusion is defined by subtlety. Adversaries
rarely send unencrypted instructions. Instead, they cloak outbound
communication in trusted channels to avoid detection. Tactics such as
domain fronting, DNS tunneling, and hijacking popular services (Slack,
Discord, GitHub) allow attackers to make their C2 beacons appear
indistinguishable from routine traffic.

These subtle C2 activities represent a key point in the battle between
attackers and defenders. If attackers go unnoticed here, they are finally
positioned to steal, compromise, or ransom an organization’s data.

Over a six-month period, Comcast Business detected and blocked
more than 708 million command and control attempts, including over
191 million attempts made through proxy-based channels, like those
we explored earlier in the report. These detections underscore the
scale at which attackers attempt to conceal their operations in plain
sight, and the extent to which covert C2 has become the standard for
modern intrusions.

Defending against this activity requires looking beyond simple
indicators. Effective countermeasures include anomaly detection that
flags unusual destinations (e.g., a host suddenly initiating encrypted
traffic to a new geography), Transport Layer Security (TLS) inspection
of encrypted traffic to surface hidden payloads, and continuous
monitoring for outbound traffic irregularities. Together, these measures
provide defenders with the best chance to detect and disrupt
adversaries before data exfiltration and impact can take place.

708 Million C2
Attempts Blocked by
Comcast Business

Phishing-linked C2: 497M
Adversaries repurpose phishing
infrastructure for covert control.

Proxy-based C2: 191M
Beacons routed through
residential proxies to mask
origins.

Scanner-to-C2 transitions: 13M
Reconnaissance tools later
serve as command relays.

Botnet C2: 2.0M
Distributed malware networks
acting as control hubs.

Web attack C2: 2.0M
Exploits delivered via malicious
sites with embedded C2.

Windows exploit C2: 1.7M
Post-exploit channels tied to
Windows vulnerabilities.

Spam-source C2: 1.1M
Malicious traffic hidden within
spam relay networks.

Mobile threat C2: 2.5K
Small but persistent presence
of mobile malware calling back.

32
32

Data Exfiltration and Impact
After establishing command and control, adversaries often turn to exfiltration or direct impact.
Data theft is rarely loud. Attackers favor slow and deliberate methods designed to fly under the
radar. Rather than a single large transfer, stolen information is often broken into smaller packets,
moved outside normal business hours, or tunneled through alternative protocols like DNS, File
Transfer Protocol (FTP), or Simple Mail Transfer Protocol (SMTP). Comcast Business telemetry
reflected this trend, with exfiltration over alternative protocols (T1048) appearing as one of the
most frequently attempted late-stage techniques.

Impact actions follow closely behind. Palo Alto’s Unit 42 reported that 86% of incidents they
investigated in 2024 involved operational downtime, reputational damage, or both.25 In other
words, adversaries aren’t only stealing data—they’re disrupting business continuity as a means of
creating leverage or sowing chaos.

The combined data makes clear that while the number of these late-stage detections is
understandably much smaller than early-stage threats, they represent the most consequential
moments of an attack chain. If exfiltration or destructive actions succeed, the result is often
immediate business disruption, high recovery costs, and reputational harm.

Ransomware as an Endgame
Ransomware remains one of the most dominant impact payloads in 2025. Once footholds are
secured and data is staged, attackers encrypt critical systems to halt operations and pressure
victims into payment. Groups such as Cl0p26 and Qilin27 continue to refine their tradecraft,
deploying ransomware at speed and scale across industries.

What makes ransomware especially challenging is the multi-pronged approach many groups
now employ. Encryption is often paired with data theft, creating a “double extortion” model
where sensitive files are stolen before systems are locked down. Even if victims refuse to pay for
decryption, they may still face threats of public leaks or exposure of confidential information. The
result is that ransomware incidents extend well beyond technical disruption—they can trigger
legal, regulatory, and reputational consequences that persist long after systems are restored.

Wipers and Destructive Payloads
Not all attackers are financially motivated. Nation-state actors and politically aligned groups have
repeatedly deployed wiper malware designed to irreversibly destroy data or corrupt systems.
Cisco Talos, for example, identified “PathWiper” in 2025 being used against a Ukrainian critical
infrastructure organization, delivered through legitimate administrative tools to maximize reach and
disruption.28

Unfortunately, nation-state actors now regularly engage in cyber-crime activity to generate cash
and fund state-sponsored priorities, including nuclear weapons development.29 This blurring of
motives means that even small and mid-sized organizations are now potential targets of groups
operating out of adversaries. For these actors, destructive attacks and financial extortion are two
sides of the same coin—tools to generate revenue, exert pressure, or destabilize adversaries.

25 Palo Alto Networks, Global Incident Response Report 2025
26 CISA, #StopRansomware: CL0P Ransomware Gang Exploits CVE-2023-34362 MOVEit Vulnerability
27 Office of Information Security, HC3: Threat Profile
28 Cisco Talos, Newly identified wiper malware “PathWiper” targets critical infrastructure in Ukraine
29 CISA, Cybersecurity & Infrastructure Security Agency – Nation-State Threats

33

SOC Casebook

Custom Detection Rules Help
Protect Connected Devices

During an authorized penetration test, a
consultant downloaded a staged payload from
a remote server onto a workstation that was
USB-tethered to a medical infusion pump.

The action matched ingress tool transfer
(T1105) and triggered a Comcast Business written
EDR detection rule: an unknown binary hash
coupled with an outbound HTTPS fetch from an
uncategorized domain.

Seconds later the file attempted to execute
(T1204.002), but before any post-exploitation
steps could fire, Comcast Business MDR
analysts quarantined the host and contacted
the customer. Built-in EDR analytics and the
customer’s MDR platform recorded no alerts,
underscoring the value of custom detections.

SOC Insights:
Custom rules close visibility
gaps: Proprietary analytics
surfaced a threat missed by
default detection logic.

Early interruption stops the
chain: Blocking execution at
the download stage prevented
credential theft, lateral spread,
and encryption-for-impact.

Layered EDR + MDR shortens
dwell time: Integrated monitoring
reduced detection-to-response
to minutes, a critical advantage
against fast-acting malware.

34

DDoS: Escalating Scale
and Sophistication

DDoS attacks have become a persistent threat to organizations of all sizes, and one
that carries serious implications. A successful DDoS attack can result in business
downtime that can lead to financial loss and reputational damage, especially if
customer-facing services are taken offline.

Comcast Business detected 44,069 DDoS events last year, while research such as
NETSCOUT’s DDoS Threat Intelligence Reports from 2023 and 2024 show a 27.9%
year-over-year uptick in detected DDoS attacks, pointing to a DDoS landscape
growing in both size and complexity.30

According to our analysis, attackers now commonly leverage DNS amplification
and reflection-based tactics, such as DNS NXDOMAIN (“water torture”) attacks,
to flood entire networks. We also saw a surge in “carpet bombing” DDoS, where
attackers spread traffic across numerous IP addresses or subnets simultaneously to
complicate mitigation. Such attacks can fly under the radar of defenses that focus on
a single IP, overwhelming networks in aggregate. The net effect is a higher baseline
of disruptive traffic that businesses must be prepared to absorb or deflect.

DDoS attack patterns have also shifted toward short, intense bursts used to probe
defenses, identify vulnerabilities, or mask other cyber intrusions. In practice, a threat
actor might unleash a 60-second blast of malicious traffic to degrade a victim’s web
servers, overwhelm a security appliance or just probe cybersecurity infrastructure.
Geopolitical tensions further complicate the threat landscape, as politically motivated
hacktivists like the pro-Russian group NoName057(16)31 employ DDoS for disruption
or propaganda, rather than monetary gain.

Much like we are seeing across other threat types, artificial intelligence is helping
attackers augment DDoS attacks. According to NETSCOUT’s 2024 DDoS report,
AI is being used to bypass CAPTCHAs and enable more advanced capabilities like
behavior mimicry and real-time attack adaptation. These developments make
attacks more efficient and relentless while lowering the barrier to entry for attackers.

30 2023 NETSCOUT DDoS Threat Intelligence Report / NETSCOUT DDoS Threat Intelligence
31 Netscout, The threat actor NoName057(16) has likely conducted over 1,500 DDoS attacks since March 2022

35

Recommendations for
Strengthening Defense

The 2025 threat landscape is intensifying and evolving in complex ways. Adversaries are launching
high-volume early-stage attacks, leveraging new tactics like residential proxy networks and AI-
driven scams to conceal their activities, and continuing to exploit human weaknesses. This paints a
challenging picture, but it also highlights where defenders should focus their efforts. To navigate these
threats, consider a multi-layered, adaptive security strategy that includes SD-WAN, MDR/XDR, DDoS
mitigation, and vulnerability management to help organizations address the following priorities.

Reinforce the Perimeter
Maintain strong preventive measures on the
front lines. Application firewalls with unified
threat management (UTM), strict identity and
access controls, multi-factor authentication,
and network segmentation can mitigate the
risk to your attack surface. Many opportunistic
attackers will move on to easier targets if they
encounter well-fortified basic defenses.

Implement Robust Patch Management
Establish a routine for regularly updating
and patching all software and systems, use
automated vulnerability scanning tools to
identify and prioritize the remediation of
vulnerabilities, and develop and enforce policies
so patches are applied promptly.

Deploy Advanced Detection and
Response Technologies
Accept that some attacks will slip through.
Invest in advanced detection and response
capabilities to catch intruders quickly. This
includes deploying AI-driven analytics and using
EDR and extended detection and response
(XDR) tools to spot subtle malicious behavior, as
well as ensuring 24/7 monitoring via a security
operations center (in-house or through a trusted
MDR partner). The faster you can detect and
contain an intrusion, the less damage it can do.
Adopting a “when not if” mindset regarding
intrusion means continuously hunting for signs
of compromise and being ready to respond at a
moment’s notice.

Empower People and Ease the Burnout
Security is ultimately a human endeavor.
Organizations should invest in tools and
services that amplify human analysts rather
than overwhelm them with alerts that aren’t
actionable. Automate routine tasks and enrich
alerts with context so security analysts can
make decisions faster. Consider managed
services to extend your team’s capabilities (for
example, an MDR partner to shoulder 24/7
monitoring and response). The goal is to reduce
alert fatigue and staffing strain so your experts
can focus on strategic initiatives without
burning out.

Build a Cybersecurity Culture
Simultaneously, continue to educate and
engage the general employee base, turning
the weakest link into the first line of defense.
A culture of security (where employees report
suspicious emails and adhere to best practices)
can thwart many attacker’s attempts at the
initial access stage.

Rethink Risk Management
Adopt a modern risk calculus. Since not every
threat can be eliminated, leadership must
identify high-impact scenarios and consciously
decide which risks to mitigate, transfer, or
accept. Bolster this strategy by regularly
practicing incident response and maintaining
robust business continuity plans to ensure rapid
recovery from an attack.

36

How Comcast Business Can Help

In the face of an ever-changing threat landscape, Comcast Business offers advanced
cybersecurity and networking solutions, spanning secure SD-WAN, SASE, MDR and XDR, and
DDoS Mitigation, to help reduce dwell time, and lower operational burden for security teams.

Our solutions include:

Secure SD-WAN with Advanced Security
Combines resilient software-defined networking
with built-in Unified Threat Management (UTM)
security controls, Next-Generation Firewall
(NGFW), Intrusion Prevention System (IPS),
URL filtering, and Data Loss Prevention (DLP),
providing consistent policy enforcement and
secure connectivity for users on-site or in the
cloud. This helps ensure that your distributed
locations and remote workforce can achieve
optimized performance and enterprise-grade
security at the network edge.

Unified Threat Management (UTM)
An all-in-one security platform that consolidates
essential features—next-generation firewall,
intrusion prevention, antivirus/anti-malware,
web filtering, and more—into a single, centrally
managed solution. UTM simplifies security
management and provides comprehensive
visibility across your network, helping to block
commodity exploits and attacks before they
reach your users or critical systems.

Secure Access Service Edge (SASE)
A unified, cloud-delivered framework that
integrates networking and UTM security. Comcast
Business’s SASE offering brings together SD-WAN
connectivity with advanced security functions—
SWG, DNS security, Cloud Access Security Broker
(CASB), Zero Trust Network Access (ZTNA), and
DLP—under one centrally managed service.
The result is adaptive security against user-
dependent risk for threats like phishing, drive-by
compromise, and shadow IT.

Managed Detection and Response (MDR)
24/7 threat monitoring and active cyber
defense managed by our team of experts.
MDR combines advanced threat detection
technology with SOC-led human threat hunters
who investigate and triage incidents in real time.
Automated response contains or disrupts threats
before a major security incident occurs. This
service helps businesses quickly identify hard-
to-detect threats, contain incidents, and reduce
dwell time.

37
37

Vulnerability Scanning and Management
Proactive assessment services to identify,
prioritize, and remediate security weaknesses
in your IT environment. Regular automated
scanning and expert analysis help you close gaps
(such as unpatched software, misconfigurations,
or exposed ports) before attackers can exploit
them. Ongoing vulnerability management
ensures your organization’s “attack surface”
stays as small and well-fortified as possible.

DDoS Mitigation Services
Network-based defenses against Distributed
Denial of Service attacks. Comcast Business
provides DDoS monitoring and mitigation that
can identify unusual traffic spikes in real time
and filter out malicious traffic bursts. These
services help keep your websites, applications,
and internet-facing services available even
when under heavy attack, minimizing
disruption and downtime.

DNS Security
Offering network security for small businesses,
SecurityEdge® is a cloud-based internet
security solution that uses DNS filtering to
help protect all connected devices on your
network from malware, phishing scams,
ransomware, and botnet attacks from bad
domains. This easy-to-install cloud-based
solution offers customizable web filtering with
threat intelligence updated every 5 minutes.

Managed Endpoint Detection &
Response (EDR)
Advanced endpoint security for computers
that connect to your network, coupled with
24/7 threat identification and response by
the Comcast Business SOC. Our managed
EDR solution continuously monitors laptops,
servers, and other endpoints for suspicious
behavior, using machine learning to detect
malware, ransomware, and other threats that
evade traditional antivirus. When a threat
is detected, the SOC’s analysts can validate
the alerts and, if EDR is combined with MDR,
trigger automated containment actions to
prevent the threat from spreading—helping
prevent a single compromised device from
turning into a widespread incident.

3838

Learn more about how Comcast
Business can help protect your
business today.

Learn more

©2025 Comcast Corporation. All Rights Reserved.

39