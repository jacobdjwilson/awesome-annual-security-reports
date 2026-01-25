# 2025 Cybersecurity Threat Report

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

# 2025
# Comcast Business
# Cybersecurity
# Threat Report

## Foreword
By Noopur Davis
Executive Vice President, Chief Information
Security and Product Privacy Officer, Comcast

The cybersecurity environment we face in 2025 is unlike any that
has come before. Threats are growing in scale, stealthiness, and
sophistication. But this is also a transformative time for cyber defense,
with advances in AI, automation, and industry collaboration opening
new opportunities to innovate.

Technology is a defining factor in this landscape. Artificial intelligence
(AI), in particular, is reshaping the cyber battlefield by introducing
not only new risks, but also powerful tools for defenders to outpace
their adversaries. Yet even with these advances, one reality remains
unchanged: people make the difference. Skilled professionals are
essential to interpret subtle signals, investigate anomalies, and
make rapid decisions when an incident unfolds. People, paired with
advanced technology, are what ultimately determines resilience.

At Comcast, we are in a unique position to see what many others
cannot. Our visibility spans across vast residential and business
networks, giving us early insights into the trends and tactics shaping
today’s threat landscape. This perspective strengthens our defenses
and directly informs the services we deliver through Comcast
Business. By combining multi-layered security solutions with deep
security operations center (SOC) expertise, we help organizations
simplify complexity, extend their capabilities, and respond with
confidence in a high-stakes environment.

This cybersecurity threat report is the product of that commitment. It
distills learnings from billions of real-world events, advanced analytics,
and cross-industry intelligence to provide decision-makers with
actionable insights on where to focus their defenses. The goal is not
just to inform, but to empower leaders with a clear view of current
risks and opportunities, so they can focus effort where it matters most
and build stronger, more resilient organizations.

My call to you is simple: use the insights in this report to strengthen
defenses, rethink risk, and embrace partnerships. Cybersecurity is a
collective effort. By working together, we can not only stay ahead of
the threats but also harness innovation to protect what matters most.

## Executive
Summary

In 2025, enterprise leaders
find themselves operating
in a global threat landscape
characterized by accelerating
scale and sophistication.

As adversaries weaponize artificial intelligence, double down on exploiting human trust, and
adopt more sophisticated evasion tactics, the traditional calculus for managing enterprise
risk is being fundamentally rewritten. Business and technology leaders are now tasked
with defending an expanding attack surface against threats that are greater in volume and
attackers that are more adept at blending in with normal business activity.

This report draws from the analysis of 34.6 billion cybersecurity events Comcast Business
detected from June 1, 2024 through May 31, 2025 across its cybersecurity customers. It
provides data-driven intelligence on how the tactics used by cyber adversaries are evolving,
alongside the advanced strategies and technologies organizations can deploy to counter
them. Ultimately, this report equips leaders with the intelligence needed to better assess
organizational exposure, anticipate adversary evolution, and proactively adapt defenses.

The numbers presented throughout the report represent the collective and anonymized data
of customers leveraging Comcast Business security offerings, including distributed denial
of service (DDoS) mitigation, endpoint detection and response (EDR), vulnerability scanning
and exposure management, managed detection and response (MDR), and other services.
Our internal data, mapped to the MITRE ATT&CK® framework, is complemented by industry
research, insights from our vendor partners, and the expertise of Comcast’s security product,
threat intelligence, and operations teams.[^1] This comprehensive perspective provides a well-
rounded analysis of the direct threats we see, the trends shaping the cybersecurity landscape,
and the business and risk implications for enterprise leaders.

Agentic AI, large language models (LLMs), proxy-based infrastructures, and other
technologies are expanding the attack surface in new ways. AI is lowering the barrier
to entry for attackers, and enterprise adoption of AI and shadow AI use by employees
creates new blind spots in identity and access management (IAM). Proxy abuse and
attacker-controlled infrastructure further amplify risk by disguising malicious traffic.

Our analysis reveals adversaries that are smarter, faster, and more resourceful than
ever, mounting high-volume phishing and drive-by compromise campaigns, exploiting
“living-off-the-land” (LOTL) techniques, and deploying increasingly sophisticated DDoS
attacks. Fortunately, defenders are hard at work, too. They’re innovating new tools to
prevent and respond to attacks—and combining the power of technology with human
expertise to weed out intruders who may be hiding in plain sight. The role of people
remains central to cybersecurity, from expert analysts who uncover weak signals in vast
streams of data to employees whose awareness and vigilance, or lack thereof, can either
stop attacks before they escalate or represent the weakest link in defense.

Organizations must adopt a multi-layered, adaptive security strategy that blends
preventative and responsive measures. Prevention remains critical—strong patch and
vulnerability management, secure email and web gateways, posture management, and
phishing-resistant multifactor authentication (MFA) can block many threats before they
reach users. But since some intrusions will inevitably get through, success also requires
advanced detection, behavioral analytics, AI-driven automation, and expert-led threat
hunting to contain them quickly. Aligning these capabilities to the organization’s most
critical business risks, and reinforcing them with a culture of resilience, helps leaders
reduce exposure and adapt defenses with confidence.

Threats are becoming
smarter, faster, and
harder to detect.

Security teams
and end-users face
mounting pressure.

Security strategy must
be tied to business
impact.

[^1]: ©2025 The MITRE Corporation. This work is reproduced and distributed
with the permission of The MITRE Corporation.

## What the Threat
Landscape Is Telling Us

### Threat Volume and Velocity Continue to Grow
Attacks are growing in volume, speed, scale,
and stealth, with Comcast Business detecting
34.6 billion cybersecurity events over a
12-month period. Attackers blend high-volume,
automated threats with “low-and-slow” tactics
that evade traditional detection, intensifying
pressure on defenders.

Business impact: Without automated
response, higher alert volumes stretch
resources, increasing response times, breach
risk, and associated costs.

### Human Factors and Fatigue
Stymie Security Efforts
Security teams are under intense pressure,
facing burnout from alert overload as well as
budget and staffing constraints. Meanwhile,
end-users remain a primary target and are often
the weakest link, as a single-clicked phishing
email or misused password can allow an attacker
to bypass perimeter security tools.

Business impact: Human error continues to
drive breach exposure and increase workloads
for security teams. Investing in security culture
and tooling is no longer optional.

### AI is an Enabler as Well as a Risk Multiplier
The cybersecurity AI landscape is quickly
evolving on three key fronts.
Front 1: Threat actors are leveraging generative
AI (LLMs) to craft more convincing phishing lures
and malware at scale, lowering the skill barrier
and increasing the efficacy of attacks.
Front 2: Enterprise adoption of LLMs and
employee use of “shadow AI” broaden the attack
surface, while AI agents raise new concerns
about non-human identity (NHI) management
and digital trust.
Front 3: Defenders are deploying AI
and machine learning (ML) to scale anomaly
detection and automate responses.

Business impact: AI has tremendous
business value but can also be a liability. It
must be governed and secured while being
strategically leveraged.

### Multi-Layered and Adaptive Defense Is Critical
Many threats exploit basic security lapses like
unpatched systems and weak credentials,
highlighting why best practices and user
education remain crucial. As attackers employ
more advanced methods to bypass the
perimeter, organizations must evolve their
prevention, detection, and response capabilities,
and root out early-stage compromises with
active threat hunting.

Business impact: Basic cyber hygiene
mistakes and over-reliance on perimeter
security can lead to high-impact breaches.
A holistic approach must pair employee
education and advanced technology with
mature processes and skilled people.

### It’s Time to Rethink Enterprise Risk
Faced with this complex and rapidly evolving
threat landscape, organizations must align
cybersecurity investments to critical business
risks, prioritize exposures, and use a new AI-
driven risk calculus to make smarter decisions
about accepting, mitigating, or transferring risks.

Business impact: Cybersecurity is no longer
just IT’s challenge. It is a board-level business
continuity, resilience, and reputational
challenge.

## Key Data Findings

The high-level trends shaping the 2025 threat landscape come into sharper
focus when examined through the lens of our cybersecurity solution data.
Comcast Business’s analysis of 34.6 billion cyber events reveals significant
patterns, illuminating not just the sheer volume of potential threats, but the
specific tactics and techniques that define how modern attacks unfold.

34.6 billion cybersecurity events
analyzed, including:

19.5B
Resource development events
related to botnet activity

9.7B
Drive-by compromise events
attempting to install malware

4.7B
Phishing events attempting
to compromise credentials or
deliver malware

44K
DDoS attacks attempting to
test or overwhelm defenses

### Early-stage Threats Put Pressure on the Perimeter
Comcast Business detected and blocked billions of phishing (4.7 billion)
and drive-by compromise (9.7 billion) events aimed at bypassing perimeter
defenses. In our analysis, drive-by compromise emerged as the top
technique used to attempt to gain initial access. This low-effort approach
for attackers requires no user interaction beyond simply visiting a
compromised or malicious website.

### Attackers Invest in Resource Development
While many pre-attack activities, such as purchasing domains, acquiring
Secure Sockets Layer (SSL) certificates, and setting up social media
accounts, are invisible to security tools because they happen outside the
network, others, like botnet usage, can be observed. Comcast Business
detected 19.5 billion events attributed to attackers using botnets to probe
our customers’ networks, a sub-technique within the MITRE ATT&CK®
resource development tactic. The massive scale of botnet events detected
suggests that attackers are investing heavily in setup before the first
malicious packet is sent.

### Resourceful Adversaries Are Living off the Land
Once inside a network, attackers are increasingly employing LOTL
techniques by conscripting trusted system tools and files to move
laterally, escalate privileges, and exfiltrate data without tripping traditional
defenses. This approach minimizes the attacker’s footprint and extends
dwell time by evading signature-based detection.

### DDoS Tactics Evolve with Short Bursts and Carpet Bombing
Comcast Business detected 44,069 DDoS events, with attackers using high-
velocity, short-burst assaults as a form of reconnaissance and stress-testing
of defenses. These quick hit-and-run DDoS attacks may last only seconds, probing
for weaknesses before larger onslaughts are unleashed. In parallel, “carpet
bombing” DDoS campaigns—spreading attack traffic across many target
IPs or subnets simultaneously—overwhelm networks in a stealthier manner.

### Proxy Abuse and Attacker Hideouts
Threat actors abuse compromised proxy networks, botnets, and legitimate
cloud services to hide their infrastructure. Across its combined residential
and business customers, Comcast’s threat intelligence team has identified
groupings of tens of thousands of infected or co-opted devices that
are quietly forwarding traffic for outsiders. Commonly referred to as
“residential proxies,” these can use any compromised personal or business
device including routers, IP cameras, and other Internet of Things (IoT)
devices. Once compromised, the devices’ IP addresses are often sold or
rented to attackers. The Comcast threat intelligence team has visibility
into these threats, even though they often originate from devices that are
outside of Comcast ownership and management.

### Security Fundamentals: Back to Basics
Our data shows that attackers continue to exploit basic lapses, particularly
around unpatched software, open ports, misconfigurations, and credential
hygiene. Access to valid accounts via compromised credentials was among
the most commonly observed post-compromise techniques, underscoring
the importance of enforcing strong password policies, MFA, and timely
deprovisioning of stale or unused accounts.

## The 2025 Cybersecurity Prism:
Building Enterprise Resilience
with Layered Security

In 2025, cybersecurity is inseparable from business resilience. A successful breach
is not just a technological event. It can disrupt operations, impact revenue, and
damage reputation. Multi-layered defense, therefore, is no longer simply an IT best
practice. It is a cornerstone of organizational resilience.

Resilient security anticipates that some defenses will fail. By layering protection
across the network, cloud, endpoints, and people, businesses can detect and
contain threats more quickly, minimizing downtime and recovery costs. This
approach hardens operations while enabling faster recovery when incidents occur.

Technology alone is not enough. AI-powered monitoring and automated response
provide speed, but skilled analysts and threat hunters are critical to interpret signals,
prioritize risks, and act decisively. The combination of human expertise and adaptive
technology ensures attacks do not spiral into crises.

For business leaders, the lesson is clear: cybersecurity is a board-level concern.
Investing in adaptive, multi-layered defenses builds resilience, protects customer
trust, and helps the enterprise keep moving forward in an uncertain environment.

### How Comcast Business Helps Enable
Enterprise Resilience through Cybersecurity

Comcast Business provides scalable, multi-
layered security solutions to counter modern
threats. This year’s report shows attackers are
striking earlier and faster with sophisticated
evasion tools, demanding a coordinated defense
across the entire attack chain and enterprise. Our
comprehensive portfolio integrates advanced
capabilities into customers’ infrastructure,
including network firewalls, intrusion prevention,
vulnerability and exposure management, cloud
security, and sophisticated detection and
response solutions such as Endpoint Detection

and Response (EDR), Network Detection and
Response (NDR), and Managed Detection and
Response (MDR). These work in tandem with
Secure Access Service Edge (SASE) frameworks,
zero trust architectures, and targeted security
such as DDoS mitigation.

By combining these technologies with around-
the-clock monitoring, threat intelligence, and
a team of skilled analysts, Comcast Business
helps organizations detect, prevent, and
respond to threats with speed and precision.

## Bringing the
Data to Life

To provide clarity and an actionable structure, this report maps our security log data against
the MITRE ATT&CK® framework and provides parenthetical links to tactics, tactics, and sub-techniques mentioned. This industry-standard model helps technology leaders
visualize the entire attack lifecycle, establish a common language for discussing threats,
and directly link adversary behaviors to proven mitigations and security controls. To help
illustrate the lifecycle of a modern cyberattack, we’ve organized the narrative into four
stages. While these are not official MITRE ATT&CK® stages, this structure helps leaders see
not just what individual techniques look like, but also highlights the interconnected nature
of techniques as bad actors attempt to execute an end-to-end attack:

### 01.
Identifying Targets & Testing Defenses
The initial phase where adversaries perform
reconnaissance, develop resources, and attempt
to compromise defenses.

### 02.
Establishing a Foothold
The critical post-compromise stage where
attackers execute code, establish persistence,
and escalate privileges.

### 03.
Digging Deeper & Expanding Reach
The dangerous phase of lateral movement,
credential harvesting, and defense evasion as
attackers burrow deeper into a network.

### 04.
Playing Out the Endgame
The final stage where attackers establish
command and control, exfiltrate data, and deploy
their ultimate payload, whether that’s destroying
data, stealing it, or holding it for ransom.

| Attack Stage 1 | Attack Stage 2 | Attack Stage 3 | Attack Stage 4 |
|---|---|---|---|
| Identifying Targets &
Testing Defenses | Establishing a
Foothold | Digging Deeper &
Expanding Reach | Playing Out the
Endgame |
| Reconnaissance
(TA0043) | Execution
(TA0002) | Defense Evasion
(TA0005) | Command & Control
(TA0011) |
| Resource
Development
(TA0042) | Persistence
(TA0003) | Credential Access
(TA0006) | Exfiltration
(TA0010) |
| Initial Access
(TA0001) | Privilege Escalation
(TA0004) | Discovery (TA0007) | Impact
(TA0040) |
| | | Lateral Movement
(TA0008) | |
| | | Collection (TA0009) | |

Interspersed throughout the MITRE-based narrative are insights on the
broader trends shaping the threat landscape—such as the rise of LOTL
techniques that abuse legitimate system tools, the pervasive use of proxy
networks to mask malicious activity, and the role of AI as both a defensive
accelerator and a risk multiplier. Together, these insights illustrate how
adversaries are evolving and how defenses must adapt in an increasingly
high-stakes, AI-driven environment.

To bring these threats and defensive actions to life, we have included SOC
case studies. These illustrative examples are based on anonymized, real-world
events with additional details added by Comcast Business SOC analysts to
better demonstrate some typical techniques and behaviors of an attack.
They provide an inside look at how multi-stage attacks can unfold and how a
combination of advanced technology and human expertise can interrupt the
attack chain and mitigate business impact.

## Attack Stage 1

### Identifying Targets
& Testing Defenses

This initial stage covers the early steps in an attack, where
adversaries identify weaknesses and attempt to gain entry.

MITRE Tactics Covered:
Reconnaissance | TA0043
Resource Development | TA0042
Initial Access | TA0001

### Reconnaissance is Constant
Just like with physical crimes, cyber adversaries often begin
by quietly casing the perimeter. Every day, threat actors (from
low-level cyber criminals to nation-state backed groups) probe
common entry points such as firewalls, web servers, remote
access ports, virtual private network (VPN) gateways, and IoT
devices, seeking any crack in the enterprise perimeter. This
“background noise” is largely automated and commoditized,
as botnets and scan-as-a-service tools continually sweep the
internet. That automation has supercharged reconnaissance,
with Fortinet recording a 16.7% year-over-year surge in automated
global scanning, peaking at a velocity of 36,000 scans per
second.[^2]

While you cannot eliminate reconnaissance activity, you can
harden and minimize the attack surface, institute robust
vulnerability and patch management, and monitor for early
warnings (e.g., ingesting threat intelligence on known scanner
IPs and blocking aggressive probing can preempt attacks).

16.7%
YoY surge in
automated
global scanning

Source: Fortinet, 2025 Global
Threat Landscape Report

[^2]: Fortinet, 2025 Global Threat Landscape Report

### DDoS Short Bursts as
Reconnaissance
Comcast Business detected an increase in short-
duration (less than 5 minutes) DDoS attacks that
threat actors can use as a reconnaissance tool to
essentially jiggle the locks on network defenses.
These hit-and-run DDoS attacks overwhelm
defenses briefly and then stop before traditional
mitigation can engage. For example, a threat
actor might hit a web service with a 30-second
burst of traffic to gauge DDoS detection triggers,
then back off to see what happens. Attackers
can learn valuable information about defense
capabilities without causing too much of a stir,
revealing how quickly a target mitigates, what
threshold causes a response, and which parts of
the infrastructure are less secure. These short-
burst attacks confirm that reconnaissance isn’t
limited to quiet scanning—sometimes it’s loud
and brash, meant to test defenses.

Comcast Business detected increased
use of short-burst DDoS attacks,
with some lasting less than 10 seconds.

405 events
in less than 5 minutes

56 events
in less than 10 seconds

### As New Vulnerabilities
Proliferate, Patch Management
Remains a Cornerstone
of Proactive Cyber Defense

Patching may not always grab headlines,
but—coupled with security posture and
system configuration hardening—it
can reduce one of the most common
paths attackers use to compromise
organizations. Yet, fully closing the patch
gap is challenging because it is difficult
to identify software dependencies that
rely on the prior version, and dependency
updates must be tested in advance. The
sheer volume of Common Vulnerabilities and
Exposures (CVEs), the complexity of
enterprise IT environments, and downtime
considerations can all slow mitigation.
This is why a risk-based approach to
vulnerability management, coupled with
continuous testing, is crucial.

#### The Scale of Common Vulnerabilities and
Exposures Continues to Climb

Tracking the growth of CVEs from 2020 through 2024.

2020
18,375

2021
20,161

2022
25,059

2023
28,961

2024
40,077

Source: CVE.org data

### Resource Development

Before attackers make an intrusion attempt, they spend time building
and positioning their assets. Resource development techniques include
acquiring or compromising tools like domains, servers, SSL certificates,
and proxy IPs as well as setting up social media accounts and
developing custom malware for use in future attacks. This preparatory
stage has become highly commoditized and supercharged by
automation, fueling a higher volume of attacks as criminals no longer
need advanced skills or expensive infrastructure to launch campaigns.

Comcast Business detected 19.5 billion resource development events
tied to botnet activity, where adversaries harness compromised
machines to probe customer networks for weaknesses. This activity
reflects how much effort attackers put into staging their campaigns
before ever sending a malicious payload. The scale suggests that
botnets are a core element of industrialized attack preparation, giving
adversaries the ability to scan, test, and refine their approaches at
massive scale.

Outside botnets, we detected especially high alert volume across
the following techniques: acquire infrastructure (T1583), compromise
infrastructure (T1584), and develop capabilities (T1587). These alerts
indicate the benefit of managed detection and response for blocking
attacks earlier in the attack chain and taking a more proactive
defensive stance by interrupting threat actors in the set-up phase.

#### Acquire/Compromise Infrastructure (T1583 & T1584)

Threat actors acquire domains, cloud servers, and hacked websites to
use as launchpads. Some use Virtual Private Servers (VPS) hosted by
bulletproof hosting services[^3] that resist takedown requests, while others
simply compromise legitimate sites to host malware. A key trend is the
use of Initial Access Brokers (IABs), who sell network access on criminal
marketplaces. This allows attackers, like ransomware operators, to
bypass the time-consuming and sophisticated reconnaissance phase by
purchasing a ready-made foothold.

#### Develop Capabilities (T1587)

The development of malware and exploits has also evolved, with
attackers often buying tools instead of creating them. They can
purchase malware “root kits,” use open-source tools, or subscribe to
malware-as-a-service offerings. Additionally, AI has become a force
multiplier for capability development. In 2024, we saw the emergence
of tools like WormGPT (an AI model tuned for malware coding)
marketed on dark web forums. Generative AI can now fill skill gaps
for criminals, helping them write effective malicious code or create
polymorphic malware that changes to evade detection.

[^3]: Bulletproof hosting is a general reference to web hosting services
that ignore or evade law enforcement requests.

### Initial Access
Once attackers conduct prep work, they shift
their energies to attempting to access their
target environments. This often begins with
social engineering in the form of phishing. This
technique has long been used to trick users
into revealing valid credentials to threat actors
but is undergoing a shift as security education
programs make users more wary of entering
credentials when prompted. Increasingly,
phishing messages are being used to set
up another initial access technique: drive-by
compromise. An innocent looking link in an
email, text, or chat leads to a compromised or
malicious website, where attackers use malware
to gain a foothold within the user’s device.

#### Top Initial Access
Methods Detected

Drive-by Compromise (T1189)
Visiting a compromised or malicious
website can automatically infect a user’s
system with malicious code without any
further action.

Phishing (T1566)
Deceptive messages are used to trick
victims into revealing credentials,
clicking malicious links, or deploying
malware.

#### Phishing (T1566) as a primary vector

“Click This” remains at the top of the hacker’s playbook, and for good reason. Phishing
continues to be rampant across email, text (smishing), voice (vishing) and, increasingly,
workplace collaboration tools (such as Microsoft Quick Assist), as adversaries look to
trick users into either giving up credentials or executing malware.[^4]

Key Takeaway

Threat actors are escalating phishing campaigns with new AI-driven tactics.[^5] Generative AI
helps churn out convincing phishing messages at unprecedented speed and scale, while
AI-based voice cloning has given rise to more convincing vishing schemes where victims
hear familiar voices, like those of a CEO or loved one, to deceive them. Attackers even
deploy deepfake images and video in these social engineering ploys. Whatever the channel,
phishing continues to adapt and thrive. AI tools are only helping increase the realism,
speed, and scale of phishing attempts, making this vector more formidable than ever.

4.72B
phishing events
detected by
Comcast Business

[^4]: Microsoft, Threat actors misusing Quick Assist in social engineering attacks leading to ransomware
[^5]: Federal Bureau of Investigation, Criminals Use Generative Artificial Intelligence to Facilitate Financial Fraud

### Drive-by Compromise (T1189)

Drive-by compromise emerged as a prevalent initial access vector in our
data set, with nearly 9.8 billion events blocked. In a drive-by attack, a user
visits a compromised or malicious website that then automatically triggers
malware download or exploit code (often via malvertising or fake prompts).
Notable examples are SocGholish[^6] (injects fake browser update dialogs
into legitimate but compromised websites) and ClickFix[^7] (produces fake
error messages or security alerts, often displayed as pop-up windows, that
can trigger infostealer installation). The massive scale of our detections
indicates that attackers find drive-by attacks attractive for targeting broad
user populations.

These attacks can deliver malware that opens the door to larger-scale
compromises if not caught and contained. Defending against drive-
by attacks requires layered web security: updated browsers, Domain
Name System (DNS) filtering, web proxy scanning, and isolating or
shielding untrusted web content. User education helps, but given these
attacks are often invisible to the user, technical controls are the front
line. Encouragingly, many drive-by attempts are noisy and can be readily
detected by security tools. The case study below, from the Comcast
Business SOC, illustrates one such detection.

[^6]: SocGholish is a JavaScript-based loader malware that has been used since at least 2017.
[^7]: ClickFix attacks are a sophisticated form of social engineering, leveraging the appearance
of authenticity to manipulate users into executing malicious scripts.

### SOC Casebook

#### Comcast Business Threat Hunting Team
Contains Fake Browser Update Attempting
to Establish a Foothold for Attackers

In this example, we see how a drive-by compromise using a fake update enabled attackers to
establish persistence and command and control (C2) communication, as well as how rapid, managed
SOC detection and containment cut off the attack before escalation or ransomware deployment.

A user browsing an infected news site encountered a
pop-up urging a “critical browser update.” Trusting the
prompt, they downloaded and ran the installer, which
was actually SocGholish, a JavaScript-based loader
favored by ransomware crews. In MITRE terms, this
represents a drive-by compromise (T1189) and user
execution (T1204) sequence.

Once active on the employee’s workstation, SocGholish
decrypted its stage-one payload, planted a hidden
scheduled task (T1053.005) for persistence (TA0003),
and reached out over HTTPS to an attacker-controlled
C2 server (T1071.001) to await further instructions that
typically include Cobalt Strike beacons or ransomware.

Comcast Business threat-hunting analytics flagged
the new scheduled task, unfamiliar binary hash, and
anomalous outbound beacon. The SOC remotely
quarantined the workstation, blocked the C2 domain,
and contacted the customer to reimage the device
and reset credentials. Rapid containment severed the
backdoor’s command channel before it could pull
secondary payloads, preventing potential privilege
escalation, data theft, and encryption.

SOC Insights:
User-driven infections remain
potent: Fake browser-update lure
bypasses perimeter controls by
exploiting user trust and normal
download workflows.

Behavioral hunting closes the
gap: Detecting a never-before-
seen hash, sudden scheduled
task creation, and quick HTTPS
beaconing exposed SOCGholish
before stage-two malware
arrived.

Education plus layered security
is essential: Continuous
awareness, combined with
endpoint detection and 24/7 SOC
monitoring, provides security
against aggressive malware.

## The Human
Element

In cybersecurity, technology sets the stage, but people
determine the outcome. While security strategies increasingly
emphasize AI, automation, and zero trust architectures,
human behavior remains one of the most significant variables
in both risk exposure and defense effectiveness. Every phase
of the attack chain, from the first phishing click to impact, is
shaped by human actions, oversights, and intuition.

In cybersecurity, technology sets the stage,
but people determine the outcome.

Human-triggered exposures and IT misconfigurations play
a role in a large amount of successful attack attempts.
From phishing emails to poor credential hygiene, attackers
continue to exploit natural human tendencies like urgency,
curiosity, and trust.

Yet it’s not just end-users at risk. The defenders
themselves—security analysts, engineers, and IT teams—
are overwhelmed. The global cybersecurity workforce
gap has widened to 4.76 million professionals and 67% of
organizations report a staffing shortage that puts them
at risk, according to ISC2’s 2024 Cybersecurity Workforce
Study.[^8] This chronic overload contributes to higher risk in
subtle but serious ways. Alert fatigue can lead analysts to
miss real threats buried in the noise. Repetitive tasks drain
focus and morale. Turnover among experienced staff can
leave organizations exposed at critical moments.

67%
of organizations
report a shortage in
cybersecurity staffing,
leading to increased
risk and burnout.

Source: ISC2

Key Takeaway

The challenge also reveals an opportunity: empowering people through smarter processes and
technology. Leading organizations are investing in tools that augment human judgment, reducing
burnout while sharpening response capabilities. AI-enabled MDR services, for example, are
transforming the role of human analysts from triage engines to strategic threat hunters. Elsewhere,
behavior-aware security platforms are adapting to individual user patterns, spotting anomalies like
unusual login behavior or file movements that might escape traditional rule-based alerts. These
tools can act as a second set of eyes, flagging human mistakes before they escalate into breaches.

[^8]: ISC2, 2024 ISC2 Cybersecurity Workforce Study

## Attack Stage 2

### Establishing
a Foothold

This critical post-compromise stage details how
attackers solidify their presence within a network to
maintain access and expand their control.

MITRE Tactics Covered:
Execution | TA0002
Persistence | TA0003
Privilege Escalation | TA0004

### Stealthy Execution Is the Norm
After penetrating a system, attackers tend to avoid noisy,
obvious exploits. Rather than dropping known binaries,
threat actors live off the land, enlisting tools such as, but not limited to, PowerShell, Windows Management
Instrumentation (WMI), scripting languages, and other
built-in Windows and Linux tools to run their code. By
piggybacking on these trusted utilities—while also using
fileless, in-memory malware—adversaries can execute
their objectives while looking like routine IT work.

Our data reinforces this trend, with command and
scripting interpreter (T1059) misuse ranked as the most
detected post-compromise techniques we blocked. In
practice, that means an attacker might launch scripts
to start malicious processes under the guise of normal
system activity. Security teams must therefore scrutinize
even mundane processes. As IBM notes in its X-Force
2025 Threat Intelligence Index, nearly one in three
attacks[^9] now involves the use of valid accounts rather
than malware, indicating that many intrusions execute
entirely under the radar of traditional antivirus. The
bottom line: once inside, attackers run quiet by default.

#### Top Techniques
Used for Execution

Command and Scripting Interpreter
(T1059): Built-in command and
scripting tools are abused to execute
malicious commands and scripts.

User Execution (T1204): Malicious
code is executed by tricking a user into
performing an action, such as opening
a malicious file or clicking a link.

Windows Management
Instrumentation (T1047): The native
WMI framework is abused to execute
malicious commands and payloads,
enabling interaction with local and
remote systems.

Exploitation for Client Execution
(T1203): Malicious code is executed by
exploiting software vulnerabilities in
common client applications, such as
web browsers or productivity software.

[^9]: IBM, IBM X-Force 2025 Threat Intelligence Index

### Maintaining Footholds
With a beachhead established, attackers work to
persist in the network, ensuring they survive reboots or
initial incident response actions. Common persistence
techniques include adding autorun keys in the registry,
planting scripts in startup folders, abusing scheduled
tasks, and even creating covert new user accounts. For
example, an intruder might register a malicious service
that quietly respawns their backdoor or schedule a nightly
task to re-download malware. In server environments,
attackers may install legitimate remote access software
(like screen-sharing or remote monitoring tools) as their
backdoor, knowing such software won’t raise suspicions
or be flagged by anti-malware defenses.

Key Takeaway

Defenders should monitor closely for unusual changes
to systems,