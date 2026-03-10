# Cybersecurity-Report 2026

## Table of Contents
- [Introduction](#introduction)
- [Cyber Security Trends](#cyber-security-trends)
  - [Beyond Email: Multi-Channel Social Engineering](#beyond-email-multi-channel-social-engineering)
  - [The 2025 Ransomware Ecosystem](#the-2025-ransomware-ecosystem)
  - [From Recon to Narrative Control: Cyber's Operational Impact in 2025 Conflicts](#from-recon-to-narrative-control-cybers-operational-impact-in-2025-conflicts)
- [Global Analysis](#global-analysis)
- [High Profile Vulnerabilities](#high-profile-vulnerabilities)
- [2026 Predictions](#2026-predictions)
- [Recommendations](#recommendations)
- [An Exposure Management Perspective](#an-exposure-management-perspective)

---

# Introduction

In 2025, the threat landscape evolved rapidly, becoming more interconnected and challenging to manage. Our analysis of global telemetry and incidents reveals a fundamental shift, marked by the emergence of new attack surfaces and techniques. Attackers are integrating AI, identity abuse, exposure exploitation, and ransomware into their campaigns.

The most significant change is the accelerated pace and scale at which attack opportunities are being executed. Data indicates that attackers are linking access, execution, and impact across various domains, from AI-driven social engineering and automation to the transformation of ransomware into a data-driven extortion economy. Edge devices and exposed infrastructure are increasingly used as launch points. These patterns were consistently observed across regions and industries in 2025, highlighting the swift combination of techniques to create tangible impacts.

AI exemplifies this transformation. This report views AI as a force multiplier that enhances targeting, scale, and adaptation in attacker activities, while also influencing risk prioritization and operational responses.

Our report is structured around attacker behavior and real-world data. The subsequent chapters delve into where attackers are focusing their efforts, how different techniques reinforce each other, and which exposure patterns most frequently lead to impact. This provides the necessary context to understand the trajectory of the threat landscape and what will be most critical in 2026.

I invite you to explore the data and findings presented in this report.

Lotem Finkelstein, VP Research

---

# Cyber Security Trends

## Beyond Email: Multi-Channel Social Engineering

Which attack surface is the easiest to exploit across all organizations? For attackers in 2025, the answer was the human component. In social engineering attacks, threat actors attempt to do just that: achieve compromise by manipulating human victims into providing the initial access for them. In such attacks, threat actors target employees, outsourced personnel, and third-party service providers to gain access to the organization’s systems or sensitive information. Although these attacks are perceived to be less serious than those exploiting software or hardware vulnerabilities, they can be just as damaging as compromises achieved through other means.

For years, phishing emails served as the primary social engineering vector, and organizations became increasingly aware of these threats. However, by 2025, social engineering expanded beyond traditional email-based campaigns, adopting multi-platform, cross-channel, and highly targeted approaches that leverage phone calls, messaging applications, and real-time impersonation.

### ClickFix: Social Engineering That Shifts Execution to the User

ClickFix emerged as one of the most significant social engineering techniques in 2025. First observed in 2024, ClickFix is an initial access method in which attackers manipulate users into executing malicious actions by presenting them with fraudulent instructions.

![Flowchart of a ClickFix attack]

This technique succeeds by exploiting user trust and the tendency to follow technical instructions. It has proven highly effective due to its simplicity, scalability, and ability to bypass certain security controls. In 2025, ClickFix activity increased by approximately 500% compared to the previous year and was observed in nearly half of all documented malware campaigns.

![Example of a ClickFix website with a fake CAPTCHA prompt]

### Voice-Based Social Engineering – The Weapon of Choice for Major Attacks

Voice phishing and impersonation gained significant traction in 2025, proving to be a highly effective means to exploit user trust. Historically associated with low-complexity consumer fraud, phone-based impersonation has evolved into an enterprise-focused intrusion technique used to gain an initial foothold in large organizations.

![Scattered Spider’s breach of Marks & Spencer]

![SalesForce attacks attributed to ShinyHunters]

---

## The 2025 Ransomware Ecosystem

The number of ransomware victims reached record highs in 2025 as the criminal ecosystem underwent rapid reconfigurations. The year began with a large-scale mass-exploitation by Cl0p, a cyber crime group, followed by the sudden disappearance of several major RaaS (Ransomware-as-a-Service) groups, which created opportunities for emerging actors.

Ransomware activity reached unprecedented levels in 2025. Over 7,960 victims were named on data-leak sites operated by double-extortion groups, a 53 percent year-over-year increase.

![Published ransomware victims per month]

### Qilin – The Emerging Dominant RaaS Group

Qilin emerged as the dominant RaaS group of 2025, publishing the identities of over 1,000 victims on its DLS after they refused to pay a ransom. Following RansomHub’s abrupt collapse in April 2025, Qilin aggressively recruited orphaned affiliates.

![Qilin’s promotion of new extortion tools in a Dark Web forum]

### The Check Point Incident Response Team: Inside a Qilin Ransomware Attack

The incident began with a “super” domain administrator account referred to here as ADMIN. The account held extensive privileges and was used routinely for daily management tasks. Critically, it could be accessed from an unmanaged personal laptop over VPN and did not require multi-factor authentication (MFA).

![Timeline of the Qilin attack]

---

## From Recon to Narrative Control: Cyber's Operational Impact in 2025 Conflicts

In 2025, cyber operations functioned as an integrated part of warfare along with air power, artillery, and special operations. The impact of cyber operations was realized through sustained interaction with military, political, and informational processes, instead of isolated technical effects.

![Components of major cyber functions in a military conflict]

The cyber operations we observed in 2025 served a small number of recurring functions:
1. **Positioning and Conditioning Activity**: Establishing and maintaining access.
2. **Operational Support Activity**: Enabling or reinforcing ongoing military/political operations.
3. **Direct Effect Activity**: Causing immediate disruption or degradation.
4. **Narrative Shaping Activity**: Influencing information flows and public perception.

In the Israeli–Iranian confrontation, previously compromised civilian surveillance infrastructure was activated to provide operational visibility. In June 2025, Iranian operators accessed security cameras surrounding the Weizmann Institute and adjacent street-facing systems, gaining live feeds of roads, parking areas, and movement patterns. These feeds were monitored in the hours leading up to and during an Iranian missile strike on the Weizmann Institute, repurposing consumer-grade sensors into an improvised reconnaissance network supporting real-world targeting.

---

upporting role
in the broader conflict. Disruptive actions against
financial institutions, government services, and
civilian resilience sectors tend to be limited in
duration yet still result in major damage, as they
affect critical infrastructure, degrade function, and
force rapid recovery under pressure.

DISRUPTIVE ACTIONS AGAINST FINANCIAL
INSTITUTIONS, GOVERNMENT SERVICES,
AND CIVILIAN RESILIENCE SECTORS TEND
TO BE LIMITED IN DURATION YET STILL
RESULT IN MAJOR DAMAGE, AS THEY AFFECT
CRITICAL INFRASTRUCTURE, DEGRADE
FUNCTION, AND FORCE RAPID RECOVERY
UNDER PRESSURE.

In the Israeli–Iranian conflict, Iranian state-linked
operators and affiliated hacktivist ecosystems
increasingly focused their attention on civilian
sectors such as healthcare, research institutions,
and financial services. Iranian-linked actors
repeatedly attempted to compromise hospital
networks, exfiltrate sensitive medical data, and
interfere with clinical operations. These incidents
were not treated as isolated intrusions but as
part of a broader pattern of coercive disruption
aimed at undermining essential services and
public confidence.

Direct effect activities were also used against
Iran, where disruptive cyber operations targeted
institutions central to the country’s financial
well-being. A group operating under the name
Predatory Sparrow conducted a pair of high-
impact attacks, first against Bank Sepah,
resulting in widespread service outages and
reported destruction of core banking data,
and later against Nobitex, Iran’s largest
cryptocurrency exchange, where digital assets
were rendered inaccessible and proprietary
source code was publicly leaked. While the
operation’s sponsorship and strategic direction
were not independently confirmed, the attacks
demonstrated that critical Iranian institutions
could be disrupted rapidly and at scale.

Iranian authorities responded by sharply
restricting nationwide internet access for
more than a day, a “defensive” measure aimed
at reducing further intrusion attempts. The
restrictions resulted in immediate hardship
to the civilian population, disrupting access to
banking, news, and basic communications during
a period of heightened uncertainty.

Russia’s cyber activity in Ukraine showed a
deliberate pattern of destructive intrusions
timed to coincide with physical strikes. The
Russian-linked APT44 group deployed wiper
malware against government, energy, logistics,
and agricultural sectors in an attempt to weaken
Ukraine’s economic resilience. The group
frequently operated in parallel with missile and
drone barrages, which not only amplified the
disruption to the networks but also complicated
Ukrainian attempts to restore services.

While many such operations are visible by design,
their defining feature is that the functional
impact itself carries value, even in the absence of
public attribution or sustained attention.

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   35

Narrative Shaping Activity

In 2025, Narrative Shaping activity was central to
cyber operations, and, in many cases, the results
were more enduring than technical disruptions.
The purpose of this activity is to shape perception,
signal capability or intent, and influence domestic
or international audiences. Visibility, attribution, and
interpretation are therefore central to their impact.

Influence operations, hack-and-leak campaigns,
defacements, and public claims of responsibility
were prominent in multiple conflicts. Russia
maintained its long-standing emphasis on influence
operations, with coordinated narratives amplified
through cyber-enabled channels, proxy outlets, and
automated content generation. Technical damage
was frequently employed as a signaling mechanism,
and the narrative impact was more important than
the scale of disruption.

One example of this is a ransomware attack against
the Shamir Medical Center in Israel. The intrusion
initially appeared as a conventional financially
motivated ransomware incident and leveraged
Qilin, a ransomware-as-a-service platform typically
associated with profit-driven criminal activity.
Subsequent investigation linked the operation
to Iranian state-aligned actors. Following public
exposure, Qilin withdrew its ransom demands and
removed the hospital from its list of victims.

As missile exchanges intensified in June 2025,
Iranian information operations focused on
destabilizing the civilian population by eroding trust
in Israel’s emergency-response systems. They
released a wave of fake Home Front Command
alerts, crafted to appear indistinguishable from
official rocket-warning notifications, during periods
of heightened threat perception. Fraudulent SMS
messages warning of fabricated terror attacks,
resource shortages, and infrastructure failures
circulated alongside AI-generated imagery and
coordinated hashtag campaigns portraying Israeli
society as collapsing under sustained military

pressure. None of this was true. Israeli authorities
reported more than 1,200 coordinated social-
engineering operations targeting the public during
this period.

During the Thai-Cambodian border tensions, cyber
operations similarly prioritized destabilization
over tactical effects. The Thai government’s
platforms and media infrastructure absorbed
more than 223 million malicious requests within
a single 24-hour period, overwhelming public-
facing services immediately following military
and political signaling. Cambodia responded
with public accusations of Thai-linked intrusions
across multiple ministries, while the Cambodian-
aligned hacktivist group KH Nightmare leaked
approximately 800GB of alleged government data,
amplifying uncertainty and eroding confidence in
the government.

Although these incidents involved large-scale
disruption and data exposure, their significance
depended on visibility, attribution, and interpretation
rather than specific technical damage. Their
primary effect was to strain administrative
confidence and shape decision-making under
stress, illustrating how technical disruption can
function primarily as a signaling mechanism in
contemporary conflict.

These activities all illustrate efforts to exert
psychological pressure. The purpose of the
operations was not to inflict physical harm, but to
erode trust in official communication channels. In
several cases, the most influential cyber operations
were not those that disabled infrastructure, but
those that caused civilians to question alerts, doubt
warnings, and experience sustained uncertainty or
anxiety.

Similar dynamics were evident in Russian-affiliated
information operations during 2025. Those
operations increasingly focused on dominating
the hours immediately following offensive missile
strikes or cyber incidents, deploying rapid, high-

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   36

volume messaging campaigns intended to outpace
verification and correction. Analysts observed
coordinated surges of parallel narratives across
hundreds of channels, shaping perception before
official information could be released.

A notable development was the expansion of AI-
driven content saturation. The pro-Kremlin Pravda
network evolved into one of the world’s largest
disinformation engines, publishing up to 23,000
articles per day across hundreds of sites, including
extensive English-language items that increased
visibility in search engine results. Experts warned
that the sheer volume enabled forms of so-called
"LLM grooming," in which large language models
are continuously exposed to skewed narrative
inputs.

Russian cyber campaigns impersonated European
media outlets, manipulated public debate around
military aid to Ukraine, and targeted elections in
Germany, Romania, and Moldova, with the intent

to erode democratic confidence and institutional
trust. These patterns illustrate a post-strike
psychological doctrine in which narrative floods and
AI-scaled influence operations are used to saturate
perception at moments when populations are most
vulnerable to fear, uncertainty, and misinformation.

The conflicts of 2025 illustrate that cyber activity has
matured into a persistent and integrated component
of modern warfare rather than a discrete or
exceptional instrument. It proved invaluable in
multiple conflicts, shaping environments before
escalation, enabling operations as events unfolded,
imposing friction through targeted disruption, and
exerting sustained psychological pressure long
after the kinetic effects were felt. The practical
value of cyber operations in 2025 lies in the ability to
compound other attack venues, exploit uncertainty,
and operate continuously below traditional
thresholds of escalation. Understanding cyber
activity through its functional roles demonstrates
why its cumulative impact is increasingly shaping
our conduct and perception of war.

The conflicts of 2025 show that cyber operations are no longer
episodic or auxiliary. Their power lies in persistence, shaping
conditions before escalation, enabling action during conflict, and
influencing perception long after the physical effects have passed.

YOAV ARAD PINKAS

Threat Intelligence Analyst

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   37

THE DOMINANCE OF
CHINESE-NEXUS CYBER
THREATS

Cyber operations in 2025 no longer respect
national borders. Chinese-affiliated threat
actors run concurrent campaigns across
multiple continents and critical sectors.
Actors treat global telecommunication
organizations, cloud service providers,
enterprise infrastructure, and the
surrounding internet ecosystem as a
shared operational environment, effectively
creating a single attack surface.

The attackers’ approach leverages mature
access platforms, such as ShadowPad and
PlugX, and higher-end capabilities, including
BRICKSTORM, malware designed for stealth
and long-term persistence across edge devices
and virtualization infrastructure. Services that
are exposed to the internet and systems that
mediate identity, traffic, and trust are consistently
leveraged across targets. Chinese-nexus
espionage activity is not a collection of isolated
intrusions, but a coordinated, scalable strategy
that enables multiple actors to operate in parallel
across different regions and sectors.

CHINESE-NEXUS ESPIONAGE ACTIVITY
IS NOT A COLLECTION OF ISOLATED
INTRUSIONS, BUT A COORDINATED,
SCALABLE STRATEGY THAT ENABLES
MULTIPLE ACTORS TO OPERATE IN PARALLEL
ACROSS DIFFERENT REGIONS AND SECTORS.

CISA’s advisory. “Countering Chinese
State-Sponsored Actors Compromise of
Networks Worldwide to Feed a Global
Espionage System,”details Salt Typhoon’s
activity targeting networks across the globe,
including telecommunications, government,
transportation, and military infrastructure. While
threat actors focus on large backbone routers
of major telecommunications providers, as well
as provider edge and customer edge routers,

they also leverage compromised devices and
trusted connections to pivot into other networks.
Notably, this campaign underscores that global
access does not always require powerful new
tools. Durable positioning within widely deployed
infrastructure and the trust relationships
surrounding it can be enough to create
international reach.

The advisory was co-signed by 23 authoring and
partner agencies from the United States and
international partners across Europe, Oceania, and
Asia. This broad coordination reflects the global
scope of the issue and the need for joint defensive
action around widely deployed infrastructure.

Unmonitored Devices Exploitation

Salt Typhoon represents only one element of a
far wider set of perimeter-focused operations.
As discussed in the “Unmonitored Devices: The
Attackers’ Launch Base” chapter, throughout 2025,
the exploitation of edge infrastructure remained
central to enabling lateral movement and long-term
access, particularly when patch cycles, visibility, and
detection controls lag behind endpoint threats.

Threat actor UNC5221  has historically focused
on edge devices and continued this activity
throughout 2025, particularly targeting Ivanti
Secure VPN solutions. The actor exploited
zero-day and recently disclosed vulnerabilities
to deploy custom malware implants in multiple
incidents. These operations exploited Ivanti
Secure VPN zero-day vulnerabilities, including
CVE-2025-0282 and CVE-2025-22457, to deploy
custom platform-specific SPAWN malware.
Together, these implants provide capabilities
ranging from persistent access and traffic
tunneling to log tempering, enabling stealthy,
privileged access on the compromised appliance.

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   39

BRICKSTORM, also attributed to UNC5221,
achieved greater prominence following the F5
Networks compromise disclosure, revealing a
disproportionate risk to software vendors. By
transforming edge infrastructure into covert
environments for intellectual property theft and
downstream compromise, threat actors can
convert vendor-side access into exploitation
blueprints that can be leveraged against their
customers at scale.

Other threat actors with advanced technical
skills were also observed targeting perimeter
infrastructure. UAT4356, which was responsible
for the ArcaneDoor campaign, targeted Cisco
ASA 5500-X firewalls to deploy the Ray Initiator
bootkit, and UNC3886  deployed custom
implants on Juniper routers. Collectively, these
campaigns illustrate a broader strategy among
Chinese-nexus espionage actors: a sustained
investment in zero-day edge exploitation and
the development of platform-specific tooling
to gain access to vulnerable and unmonitored
organizational systems.

THESE CAMPAIGNS ILLUSTRATE A
BROADER STRATEGY AMONG CHINESE-
NEXUS ESPIONAGE ACTORS: A SUSTAINED
INVESTMENT IN ZERO-DAY EDGE
EXPLOITATION AND THE DEVELOPMENT
OF PLATFORM-SPECIFIC TOOLING TO
GAIN ACCESS TO VULNERABLE AND
UNMONITORED ORGANIZATIONAL SYSTEMS.

Industrialized Tradecraft and a Shared
Malware Ecosystem

Chinese-nexus cyber operations employ a
deliberate, well-resourced campaign strategy,
using shared tooling, repeatable operational
playbooks, and consistent execution across
targets and regions.

In multiple Chinese-nexus operations worldwide,
activity frequently follows a recognizable
modus operandi. Throughout 2025, Check Point
Research observed multiple campaigns on
nearly all continents in which initial access and
execution commonly leveraged DLL side-loading,
a technique allowing malicious code to run under
the cover of legitimate, trusted software. This
is commonly paired with staged loaders and
modular backdoor ecosystems, where malware
families such as PlugX and ShadowPad are
widely seen in different clusters and intrusion
sets, evidence of a shared tooling ecosystem.
These backdoors serve as operational hinges
for command execution, credential access, and
reconnaissance.

Post-compromise, operators frequently
expand their control using “living-off-the-
land” techniques and administrative protocols
that blend into the system’s own routine IT
activity, such as Remote Desktop Protocol for
lateral movement and hands-on operations. To
maintain persistence and operational flexibility,
threat actors may also deploy VPN software
under modified names, a recurring technique in
Chinese-nexus playbooks that embeds remote
control in seemingly normal connectivity. What
appears to be an ordinary sequence of technical
actions is, in fact, an exercise in trust building
designed to avoid suspicion.

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   40

THROUGHOUT 2025, EXPLOITING MICROSOFT
INTERNET-FACING SERVERS WAS A
PROMINENT INTRUSION VECTOR, AND
HELPED THREAT ACTORS TO WEAPONIZE
NEWLY DISCLOSED VULNERABILITIES RAPIDLY.

designed to extract cryptographic IIS/ASP.NET
machine keys from compromised environments.
In recent InkDragon intrusions, initial access was
gained using ToolShell. For New post-exploitation
phase, to facilitate lateral movement and data
exfiltration, the actor deployed ShadowPad or
FinalDraft malware.

The APT group, Rude Panda, abuses
misconfigurations rather than vulnerabilities. Its
campaigns conducted throughout late 2024 and
into 2025 focused on compromising Microsoft
IIS servers using publicly available, static ASP.
NET machine keys. Following initial access, the
attackers deployed a custom malicious IIS module
named “HijackServer.” This activity resulted in the
compromise of hundreds of servers globally, which
were subsequently leveraged to support fraudulent
operations, including search engine optimization
(SEO) manipulation and cryptocurrency schemes.

The post-compromise deployment of ShadowPad
is a recurring feature in our investigations of
campaigns across Europe, Africa, Central Asia, and
the APAC. Its modular architecture supports data
exfiltration, remote command execution, lateral
movement, and credential harvesting, which allows
flexible deployment as mission requirements
change. ShadowPad’s repeated appearance in
otherwise unrelated events demonstrates that
stable, adaptable tooling is effective across diverse
environments, reflecting a calculated approach to
scalable, globally distributed data collection.

In recent InkDragon campaigns targeting Europe,
Southeast Asia, Africa, and South America,
ShadowPad was the core mechanism for
persistence and execution. By deploying a custom
ShadowPad IIS Listener module, the actor also
reused the compromised infrastructure as a hub
for further operations. This technique reflects a
broader trend of turning footholds into platforms,
and platforms into supply chains.

Exploitation of Trusted Enterprise
Infrastructure

Throughout 2025, exploiting Microsoft internet-
facing servers was a prominent intrusion vector, and
helped threat actors to weaponize newly disclosed
vulnerabilities rapidly. This strategy enables
scalable access before vulnerabilities are patched,
highlighting the use of ubiquitous enterprise
platforms as long-term access vectors rather than
one-off intrusion opportunities.

ToolShell is a particularly concerning exploit
chain that enables unauthenticated remote code
execution against on-premise internet-facing
Microsoft SharePoint servers. Although publicly
disclosed on July 19, the exploitation was first
observed earlier in the month as a zero-day exploit
against a small number of global government
organizations. The intrusions were typically followed
by targeted data theft using custom web shells

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   41

One of the clearest examples of the rapid
weaponization cycle is CVE-2025-59287, a remote
code execution vulnerability in Windows Server
Update Services (WSUS). The vulnerability was
weaponized within days publishing a proof-of-
concept (PoC). Similar to previous campaigns, the
post-compromise payload was ShadowPad and
deployed via DLL side-loading. By abusing WSUS,

the attackers gained high-privilege execution
inside the Windows update infrastructure, on
which most networks depend.

These cases demonstrate that the central role
of IIS and WSUS amplifies risk by design. When
components responsible for distributing trust are
subverted, the impact is broad and difficult to contain.

JANUARY 8

MARCH 12

APRIL 3

JULY 7

SEPTEMBER 25

OCTOBER 15

NOVEMBER 19

DECEMBER 17

Figure 1: Significant Chinese Affiliated Threat Activity in 2025

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   42

Ivanti discloses RCE in Ivanti Secure Connect VPN, exploited by UNC5221 (CVE-2025-0282)Disclosure of UNC3886 exploiting CVE-2025-21590 in Juniper routersIvanti disclosed critical RCE in Connect Secure VPN, exploited by UNC5221 (CVE-2025-22457)0-day ToolShell exploit chain hits internet-facing on-prem SharePoint serversUAT4356 campaign disclosed exploiting CVE-2025-20333 and CVE-2025-20362 against Cisco ASA-5500-X firewallsF5 Networks discloses a long-term compromise of its BIG-IP development environment using BRICKSTORM malwareShadowPad campaigns exploiting Microsoft WSUS servers with CVE-2025-59287UAT-9686 campaign disclosure against Cisco appliances (CVE-2025-20393)What Will Change in 2026: Deny
Persistence, Not Just Intrusion

In 2025, our investigations showed a sustained
increase in activity attributed to Chinese-nexus
threat actors, with a global footprint across
critical sectors. These campaigns are linked
not only by shared tooling but also by consistent
operational models, including edge-focused
intrusion paths, exploitation of zero-day and one-
day vulnerabilities, and an emphasis on stealth
and long-term persistence.

The operations rely on a common set of malware
families and techniques that enable data
exfiltration, credential harvesting, and lateral
movement, supported by C2 channels designed
to be indistinguishable from modern enterprise

traffic. A recurring theme is the abuse of trusted
enterprise services, such as IIS and WSUS, to
support stealthy persistence and operational
scalability.

These campaigns follow a deliberate strategy
of reusing proven tactics across regions and
industries, turning ubiquitous enterprise
platforms into durable access points. In 2026,
the challenge extends beyond preventing
initial compromises to stopping attackers from
leveraging access to compromise downstream
enterprises and maintain persistence within
trusted services.

This chapter makes clear that geopolitical cyber activity is no
longer episodic or symbolic. It is persistent, coordinated, and
directly tied to national objectives, requiring security leaders to
treat nation-state threats as a standing operational risk rather
than a special case.

ELI SMADJA

Security Research
Group Manager

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   43

UNMONITORED DEVICES:
THE ATTACKERS’ LAUNCH BASE

The role of the network perimeter has
quietly shifted in recent years. Once
viewed as a protective barrier, attackers
are instead effectively turning it into an
attack platform. This risk was often framed
through edge devices, but that definition
has broadened during 2025. Most important
is not where a device sits, but whether it is
visible to defenders and actively monitored.

Unmonitored devices are particularly attractive
targets due to their low visibility, privileged
proximity to traffic and identity, and positioning
within operational environments that are difficult
to patch without downtime. Unmonitored devices,
such as routers, firewalls, VPN appliances, and
virtualization solutions, often operate in less
monitored zones without Endpoint Detection and
Response (EDR) capabilities, resulting in sparse
logs and short retention windows.

Now attackers are using unmonitored devices as
launching pads, easily blending into legitimate
network traffic and can harvest credentials and
move laterally before defenders can respond. In
2025, Chinese-affiliated operators extended this
approach to vendors of these devices, targeting
them not only for access but for internal
knowledge, source code, and undisclosed
vulnerabilities, ultimately preying on high-profile
customers who trust those vendors to secure
their environments.

UNMONITORED DEVICES
ARE NOW USED AS ATTACKER
LAUNCHING PADS

2025’s defining pattern was persistence, with the
exposure of long-running campaigns targeting
unmonitored devices. As defenses in standard,
well-monitored environments continue to
improve, more attackers are choosing to shift
their operations into unmonitored environments,
where visibility is weaker and response times are
slower. While this effort has been spearheaded
by Chinese-affiliated actors, it is also becoming
increasingly common among other state-linked
operators, as well as cyber criminals. When
attackers operate from unmonitored footholds,
every signal becomes suspect, and every external
dependency becomes a potential threat.

Zero-Day Exploitation and a Growing
Custom Malware Ecosystem

Among the many campaigns targeting unmonitored
devices, intrusions attributed to the Chinese-affiliated
espionage actor UNC5221 stand out for their scale,
efficiency, and longevity, showing how low-visibility
infrastructure can serve as a quiet launch base
for sustained operations. Since at least 2022,
UNC5221 has been repeatedly exploiting zero-day
vulnerabilities in Ivanti Connect Secure appliances,
deploying BRICKSTORM malware.

BRICKSTORM is a custom implant designed to run
inside multiple types of network appliances. In several
cases, it was initially deployed on an edge device and
then used to pivot deeper into internal unmonitored
infrastructure, including VMware vCenter and ESXi.
The malware is designed to blend in with typical
operations and evade standard incident-response
cycles, often persisting beyond remediation efforts.
By operating from unmonitored systems with access
to core network flows, BRICKSTORM enabled its
operators to capture credentials and expand access
into cloud environments. This progression illustrates
how a single compromise in an unmonitored device
can quickly escalate into broad identity and data
exposure.

BRICKSTORM activity also demonstrates an
alarming development: attackers now target
the vendors that build these devices. In October,
F5 Networks disclosed long-term unauthorized
access to its internal BIG-IP development
environment, linked to BRICKSTORM actors.
During the intrusion, attackers exfiltrated source
code, knowledge base content, and information
on undisclosed vulnerabilities. These assets
could be leveraged to develop reliable exploit
paths against a broad customer base. When a
development environment is compromised, the
security posture of the entire product ecosystem
is also impacted. Malware persistence on the

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   45

vendor side can easily become customer-side
exposure, accelerate exploit development, and
enable broader compromise across sectors that
depend on those products.

Multiple other China-affiliated actors are
weaponizing unmonitored network appliances
with custom, platform-device-specific implants.
The U.K. National Cyber Security Centre (NCSC)
issued a public advisory on a new implant
campaign targeting Cisco ASA-5500-X firewalls,
which are end-of-life and no longer supported.
The activity, tracked as UAT4356 and attributed
to a China nexus, involved active exploitation
of CVE-2025-20333 and CVE-2025-20362 on
compromised devices to deploy a previously
undocumented toolkit.

VENDOR-SIDE MALWARE PERSISTENCE
DRIVES CUSTOMER EXPOSURE AND
BROADER COMPROMISE.

Once these unmonitored appliances were
compromised, attackers gained high-value access
to network traffic, credentials, and administrative
functions. Designed to survive reboots and, in
some cases, even firmware upgrades, the malware
enabled attacker control, including bypassing AAA
(Authentication, Authorization, and Accounting)
checks, executing commands, conducting covert
packet capture, and exfiltrating sensitive data.

Another China-nexus actor, tracked as UNC3886,
was observed exploiting CVE-2025-21590, a
vulnerability in Junos OS, Juniper Networks’
operating system for routing, switching, and
security devices. UNC3886 abused this flaw to
run malware from within legitimate Junos OS
system processes, enabling stealthy persistence
and post-exploitation activity without breaking file

integrity checks or triggering standard security
controls, making it particularly difficult to detect
unmonitored Juniper appliances.

UNC3886 historically focuses on maintaining
long-term access to victim environments and
has previously been observed exploiting zero-
day vulnerabilities to deploy custom malware on
Fortinet devices. In intrusions involving Juniper
routers, operators deployed multiple implants in
parallel, with core capabilities such as remote file
upload and download, interactive shell access,
and connection relay. The implants operate within
Junos’ underlying FreeBSD environment and are
designed to masquerade as legitimate system
processes. In some cases, they even interact
directly with legitimate Junos OS daemons,
including patching their memory at runtime to
suppress logging and telemetry.

These operations reflect a high degree of research
effort and sophistication, with an emphasis on
stealth and maintaining persistent, long-term, and
covert access, particularly to devices that are not
continuously monitored.

Misconfiguration, Not Zero-Day

A different approach was observed in a long-running
Russian state-sponsored campaign attributed to
the Sandworm group that targets Western critical
infrastructure. Unlike the Chinese actors, which
relied on direct compromise of devices, this activity
primarily abused misconfigured network devices,
gaining access through exposed management
interfaces rather than exploiting vulnerabilities in
the platforms themselves.

The attackers gained administrative access
and then leveraged native traffic-capture and
monitoring capabilities to intercept network
traffic passively. This enabled them to harvest
credentials, session cookies, and authentication
tokens, which were subsequently used to access

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   46

legitimate organizational services such as VPNs,
identity providers, and cloud management consoles.
Establishing persistence and lateral movement
using valid credentials eliminates the need for
custom malware implants, while making the activity
harder to separate from everyday administrative
use, especially when device access and telemetry
are not consistently monitored.

Regardless of whether a campaign relies on
exploitation or misconfiguration, unmonitored
devices have become a critical and increasingly
attractive attack surface for sophisticated threat
actors, providing a low-friction path to stealthy
access, credential theft, and long-term operational
persistence.

UNMONITORED DEVICES HAVE BECOME A
CRITICAL AND INCREASINGLY ATTRACTIVE
ATTACK SURFACE FOR SOPHISTICATED
THREAT ACTORS, PROVIDING A LOW-
FRICTION PATH TO STEALTHY ACCESS,
CREDENTIAL THEFT, AND LONG-TERM
OPERATIONAL PERSISTENCE.

Ransomware:
N-Day Exploitation at the Edge

Targeting unmonitored devices is not new for cyber
criminals. Ransomware operators have targeted
VMware ESXi and vCenter environments for years
because they sit at the center of server operations
yet offer minimal visibility. This targeting does not

stand alone, as financially motivated actors have
increasingly adopted techniques long associated
with state-sponsored operators, including the
systematic exploitation of patched-but-still-exposed
vulnerabilities, known as n-days, in network
appliances.

One of the most notable examples of financially
motivated attackers using unmonitored devices as
attack points, by weaponizing n-day vulnerabilities,
involved Akira ransomware. In mid-2025, an
increase in Akira intrusions targeting SonicWall
appliances was observed. Multiple incidents involved
unauthorized access through SonicWall SSL VPN
services, followed by the deployment of ransomware,
often within hours of the initial compromise.
Victims spanned multiple sectors and organizations
regardless of size, indicating opportunistic mass
exploitation rather than targeted intrusion.

While a zero-day vulnerability in SonicWall SSL
VPN was initially suspected, this spike was largely
tied to ongoing abuse of CVE-2024-40766. This
year-old access control vulnerability allows local
user passwords carried over during migrations
to remain valid. As a result, credentials harvested
when devices were vulnerable can later be reused
by threat actors, even after the affected devices have
been patched. This illustrates the long-tail risk of
credential exposure stemming from vulnerabilities in
unmonitored devices.

Qilin, the most prolific ransomware operation
observed in 2025, similarly relied on exploiting
unmonitored network appliances for initial access.
The group was observed exploiting CVE-2024-21762
and CVE-2024-55591, which affected FortiOS and
FortiProxy SSL VPN devices. The first vulnerability
enables remote execution of arbitrary code or
commands, while the second allows attackers to
obtain super-administrator privileges. Together,
these flaws provided rapid, privileged access to victim
environments through commonly deployed perimeter
infrastructure.

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   47

This pattern was not limited to established
ransomware brands. In early 2025, vulnerabilities in
Fortinet devices were exploited by a newly identified
actor tracked as Mora_001. The group exploited
CVE-2024-55591 and CVE-2025-24472, both of which
allow unauthenticated attackers to gain super-admin
privileges on vulnerable FortiOS devices. Following
initial access, the actors mapped internal networks,
moved laterally using newly created VPN accounts,
and ultimately deployed a ransomware strain called
SuperBlack, built using a leaked LockBit builder.

Together, these incidents highlight how ransomware
operators favor n-day exploitation of unmonitored
devices to achieve fast, privileged access. This has
become a key complement to their long-standing
focus on ESXi and vCenter: unmonitored devices
provide the entry point, and virtualization platforms
offer the scale and leverage. By operating from
systems that sit outside standard endpoint visibility,
attackers shorten the time from entry to impact,
bypass common controls, and convert external
exposure directly into rapid financial harm.

Looking Ahead

Unmonitored devices continued to evolve this
year from operational network systems into
platforms for malware activity. Limited visibility
and inconsistent monitoring make them well-
suited for long-term access, and their role in
handling high-value traffic and authentication flows
enables attackers to expand access well beyond
the initial point of compromise. At the same time,
the targeting and compromises within vendor
environments increase the risk that intrusions
translate into downstream exposure for customers.

To mitigate the effects of long-running intrusions
involving unmonitored devices, end-of-life
systems must be retired. For devices that are
still supported, vendors must provide stronger
monitoring capabilities, richer forensic artifacts,
and more resilient security controls by default.
Without these changes, compromises in low-
visibility infrastructure will remain challenging to
detect and even harder to contain.

One of the most dangerous attack surfaces is infrastructure we
assume is trusted. Edge devices operating with limited visibility
allow attackers to establish persistent footholds rather than
one-time entry points.

ALEXANDRA GOFMAN

Technology Leader
Threat Intelligence

CHAPTER 02

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   48

03

AI LANDSCAPE
IN CYBER SECURITY

AI LANDSCAPE: FROM
INTEGRATION TO AUTONOMY

AI across criminal and state-sponsored activity.
Finally, we determine what changed in 2025 and
the implications for 2026.

In 2025, Artificial intelligence (AI) was so deeply
embedded in cyber activity that distinguishing
“AI-related attacks” from general digital
operations became increasingly challenging.
In contrast to 2023–2024, when attackers’
use of AI was easily recognizable, in 2025 AI
use became so commonplace that it faded
into the background of attack operations.
AI now underpins software development,
social engineering malware design, data
mining, influence operations, reconnaissance,
vulnerability discovery, and even post-exploitation
activity.

AI is now used everywhere yet remains rarely
visible. Most malicious outputs seldom reveal if
AI contributed to their creation or execution. Our
April 2025 State of AI in Cyber Security report
warned that as AI models become integrated into
daily work, the boundary between “AI-enabled”
and conventional threats would blur. By the end
of 2025, that prediction will have come to pass.

Throughout 2025, threat actors not only refined
and expanded their use of AI but also increasingly
attempted to target the AI ecosystem itself. As
enterprises adopt agentic frameworks, MCP
servers, and locally deployed models, these
environments have become the new attack
surfaces.

The following chapter examines AI’s dual role
in today’s threat landscape. First, we outline
the growing class of attacks on AI services and
agentic systems, where misconfigurations,
prompt manipulation, and vulnerabilities in
AI-connected tools create opportunities for
exploitation. Second, we assess attacks enabled
by AI, including identity theft and impersonation,
AI-assisted malware development, automated
reconnaissance, and the broader optimization of

Our focus is on real-world, in-the-wild
evidence collected throughout 2025, including
attacker operations, underground services
and discussions, published incidents, and law
enforcement findings.

AI SERVICES AS AN ATTACK
SURFACE

As AI tools and services become fully integrated
into every aspect of daily corporate life, their
access to data, context, and downstream systems
is increasing astoundingly fast. AI assistants
and agents are involved in processing emails,
documents, calendars, web content, and internal
knowledge databases. As a result, AI is becoming
an increasingly attractive attack surface.

Direct and Indirect Prompt Injection
Attacks

A clear manifestation of this trend is the rise
of direct and indirect prompt injection attacks.
Attackers continued to turn prompt injection into
a pervasive threat affecting both direct model
interactions and autonomous agent workflows.
Data from Lakera, a Check Point Company,
shows that direct LLM manipulation is achieved
through role-play setups, hypothetical scenarios,
and obfuscation tricks. In such attacks, client-
facing LLM-based services are targeted to
expose restricted information. In indirect
prompt injection attacks, malicious instructions
are embedded within otherwise legitimate
content that AI systems access during everyday
workflows.

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   50

One reported research example involved
malicious Google Calendar invitations that
contained hidden instructions inside event
descriptions. When processed by Google’s
Gemini assistant, the injected content influenced
downstream behavior, enabling unauthorized
actions such as sending messages, accessing
application context, and interacting with
connected smart home devices. The attack was
possible due to the AI assistant’s trusted access
to calendar data and integrated services.

During the year, Google also issued a global
advisory after observing invisible HTML-
based injections that could manipulate
AI summarization features within Gmail,
demonstrating how subtle these attacks are
and how difficult they are to detect. Meanwhile,
Check Point Research documented real
malware samples embedding natural-language
instructions designed to mislead AI-powered
detection tools, signaling that attackers are
attempting to bypass LLM defenses.

Similar risks were observed in enterprise
environments. Research demonstrated how AI
systems integrated into corporate workflows
could be manipulated through documents,
tickets, or shared content containing concealed
instructions. When AI assistants summarized or
processed this material, the embedded payloads
altered the model's behavior, leading to the
unintended disclosure of sensitive information or
unsafe tool execution. These findings underscore
that indirect injection turns everyday business
artifacts into potential execution vectors
once they are implicitly trusted by AI-driven
automation.

In 2025, Check Point Research disclosed a
command injection vulnerability in OpenAI’s
Codex CLI, an AI-powered coding assistant
designed to execute commands on a developer’s
local machine. The flaw allowed untrusted input

to influence command execution, effectively
enabling arbitrary commands to run in the host
environment. The case illustrates how, once
agentic AI tools are granted execution privileges,
they can turn input manipulation into direct
system compromise, even outside formal agent
frameworks.

THE FLAW ALLOWED UNTRUSTED INPUT
TO INFLUENCE COMMAND EXECUTION,
EFFECTIVELY ENABLING ARBITRARY
COMMANDS TO RUN IN THE HOST
ENVIRONMENT.

Lakera, a Check Point Company, provided
additional validation for the risk of in-direct
injection. In its Q4 2025 review of real-world
agent-related attacks, it observed that indirect
prompt injection attempts often proved more
effective than direct. The report documented
multiple cases in which hidden instructions
embedded in emails, documents, or web
pages influenced agent behavior, resulting in
unintended tool invocation, leaking sensitive
data, or suppressing safety constraints. Notably,
The report found that these attacks frequently
required fewer attempts than direct prompt
injection as they exploited the agent’s normal
operating assumptions instead of trying to
override safeguards.

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   51

Model Context Protocol (MCP) Under
Attack

Model Context Protocol (MCP), the mechanism
that allows LLMs to invoke external tools, is
currently one of the most lucrative parts for
attackers in the AI attack surface. Throughout
2025, Check Point Research and other
researchers exposed structural weaknesses
across the MCP ecosystem, which include
servers, tool configuration files, IDE integrations
such as Cursor and VS Code plugins, and the
broader community of third-party nodes. Check
Point Research published an RCE vulnerability in
Cursor’s implementation, known as MCPoison,

which stemmed from the IDE’s implicit trust
in modified MCP configuration files. Other
researchers reached similar conclusions in
a separate investigation, finding that a large
majority of publicly exposed MCP servers leaked
sensitive information such as API keys, making
them easy to compromise.

A recent review by Lakera found security
vulnerabilities in 40% of the approximately 10,000
MCP servers that were probed. Seven percent
were vulnerable to “Path Traversal” attacks, and
Lakera found at least one secret API key in 8%
of the servers. Two percent were vulnerable to
SQL injection attacks, and 6% were vulnerable to
Command or Code injection attacks.

Impacted MCP Servers by Top Vulnerability Types

Figure 1 - Detected vulnerabilities in publicly exposed MCP servers

In October, researchers identified a malicious
npm package impersonating a legitimate MCP
integration for the Postmark email service.
It silently added an attacker-controlled BCC
address to outgoing messages, enabling covert
exfiltration of sensitive mail. Underground forums
also began discussing how MCP servers could
act as stealth backdoors, blend attacker traffic
with the benign workflow of AI tool invocations,
and disguise command-and-control (C2) activity.

All these developments reflect a deeper
structural weakness: current LLM architecture
struggles to reliably distinguish between
developer-defined instructions and user-provided
input. As long as this issue remains, attackers
will continue to find ways to manipulate AI
systems into acting contrary to their intended
purpose. This challenge will persist into 2026 and
will shape the next phase of AI security.

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   52

8%7%6%2%Available API keysPath TraversalCommand/Code InjectionSQL InjectionLLMS AS A VECTOR FOR
SENSITIVE DATA LEAKAGE

The use of AI services by corporate employees
opens another front in the battle. As generative
AI becomes embedded in daily workflows, the
boundary between internal corporate data and
external AI platforms increasingly blurs, creating
new pathways for the inadvertent exposure of
proprietary assets. This risk is amplified by the
sheer volume and diversity of AI services in use.
Check Point’s GenAI Protect data indicates that
organizations interact with more than fourteen
different AI services per organization on average,
complicating visibility and control over the data
flows.

According to Check Point’s GenAI Protect’s Q4
2025 data, approximately 89% of organizations
were impacted by risky prompts within an average
month, with 1 in 41 submitted prompts classified
as high risk, an increase of 97% compared to
Q1 2025. The most common exposures included
personally identifiable information (PII), internal
network and IT artifacts, and source code. At
the same time, incidents such as OpenAI’s
recent data breach demonstrate that AI service
providers themselves are not immune to leakage.
Organizations are realizing that they can’t protect
sensitive data from exposure once it’s shared with
external models.

Taken together, these dynamics underscore that
AI services are not merely tools leveraged by
attackers but have themselves become attack
surfaces. As enterprises continue to integrate
AI into core business processes, managing how
data is shared, processed, and retained by AI
systems will remain a critical security challenge
in 2026.

AI SERVICES USED BY THREAT
ACTORS

Attackers can obtain AI capabilities in three ways:
abusing commercial models, deploying self-
hosted open-source models, and utilizing third-
party “DarkGPT”-style malicious services.  Each
method significantly evolved over 2025.

Abusing Commercial AI Services:
Jailbreaking at Scale

Attackers continue to exploit commercial models,
usually through carefully engineered jailbreaks
that bypass safety filters and by dividing
malicious requests into multiple seemingly
benign subtasks. This quickly becomes an arms
race between the model providers’ safeguards
and the malicious prompts generated in
underground communities. Threat actors share
jailbreaking techniques for both commercial

89%

OF ORGANIZATIONS
IMPACTED BY RISKY
PROMPTS EACH MONTH

1IN 41

SUBMITTED PROMPTS
WAS CLASSIFIED AS
HIGH RISK

97%

INCREASE IN RATE OF
HIGH-RISK PROMPTS
DURING 2025

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   53

DarkGPT, WormGPT, HackerGPT: The
Rise and Fall of Malicious LLM Services

At the start of 2025, the underground ecosystem
was saturated with “DarkGPT”-branded services
offering “uncensored ChatGPT” access. By mid-
year, prevailing opinions on criminal forums
shifted to the belief that these services were
mostly scams, lacking real capabilities or simply
proxying commercial models. This led to a swift
downturn in demand as attackers realized they
could jailbreak commercial models or deploy
open-source alternatives. By October, forum
users openly mocked DarkGPT-style sites, calling
them “worthless” or “90% scam.”

Self-Hosted Open-Source Models: The
Center of Gravity Shifts

As the underground community became
increasingly aware that “DarkGPT” services were
often scams, unreliable, or low quality, serious
operators migrated toward locally deployed
open-source models. Attackers started actively
discussing VPS-hosted LLM deployments,
providing unrestricted control, privacy, and
performance stability.

Several developments accelerated this shift.
High-performance open-source models became
widely available and quickly jailbroken, with
criminal forums sharing tips for fine-tuning and
dedicated offensive prompts.

THIS QUICKLY BECOMES AN ARMS RACE
BETWEEN THE MODEL PROVIDERS’
SAFEGUARDS AND THE MALICIOUS
PROMPTS GENERATED IN UNDERGROUND
COMMUNITIES

and open-source models in dedicated shared
repositories and forums. Repositories cataloging
jailbreak prompts by model or version have
become standard tooling, and a new class of
“context poisoning” jailbreaks, most notably the
Echo Chamber technique, demonstrated how
carefully crafted multi-step prompts can bypass
guardrails without appearing explicitly malicious.

OpenAI’s June 2025 threat intelligence report on
Operation ScopeCreep reveals how a Russian-
speaking threat actor incrementally bypassed LLM
safeguards by spreading malware development
tasks across multiple, seemingly unrelated
accounts. Each account submitted only a small,
benign-looking request, but enabled the actor
to accumulate multi-stage Go-based malware,
including C2 deployment, DLL side-loading,
resulting in malware deployment in the wild.

Some of the most advanced operations of 2025
explicitly manipulated commercial LLMs through
role-play, convincing them that malicious actions
were part of penetration-testing or defensive
tasks. This technique later became a central
feature of the GTG-1002 espionage campaign.

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   54

Figure 2 - Discussing how to use Kimi K2 for malicious code generation

Local deployment enabled Copilot-style
workflows, increasingly allowing attackers
to embed jailbroken local models directly
into malware development and debugging
environments.

In 2025, sophisticated actors moved away from
outsourced “criminal AI services” and shifted
toward privately controlled compute, eliminating
the possibility of supervision, filtering, and logs.
Evidence for this trend primarily consists of
self-reports from criminals and discussions in
criminal forums.

AI USE IN SOCIAL ENGINEERING
AND IDENTITY THEFT

If 2024 was the year AI enabled supercharged
phishing, 2025 is the year of AI impersonation: in
text, audio, and video, in offline, real-time, and
autonomous modes. Our April report presented
these developments in detail, and the subsequent
months delivered abundant real-world evidence
that all three modalities reached operational
maturity.

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   55

Textual Social Engineering:
Scale, Cultural Precision, Autonomy

AI-generated text now appears in phishing,
sextortion, Business Email Compromise (BEC)
scams, influence operations, and multilingual
fraud. There are multiple reports of increased
multilingual culturally adjusted phishing and
comment flooding, which never repeat the
exact same text. Text generation reached fully
autonomous levels, removing the critical bottleneck
of a lack of culturally proficient manpower.

Audio Deepfakes:
Real-Time Impersonation and
Fully Autonomous Calling

AI-generated voice technology, once resource-
intensive, is now much easier to use, requiring just
minutes of audio from social media. In 2025, voice
impersonation attacks included live impersonation
of a European defense minister to solicit “hostage-
release funds” from contacts with high net-worth
individuals, impersonation of US Secretary of State
Marco Rubio, and many reports of impersonating
family members to commit financial fraud. Some
AI voice technology reached full autonomy, with
criminals advertising scripted call flows, adaptive
responses, voice cloning, and OTP collection
(known as “AI-driven outbound calling systems”) to
impersonate banks, cryptocurrency exchanges, or
authorities to harvest OTPs and credentials.

case was reported involving AI-generated celebrity
endorsements that defrauded more than 6,000
victims, primarily from the  United Kingdom and
Canada.

Real-time deepfake technology has also advanced
rapidly. Tools such as DeepFaceLive now operate
with high fidelity on consumer hardware, enabling
attackers to alter their appearance during live calls
and meetings. Similar techniques were also used in
fraudulent job interviews, particularly in operations
linked to North Korean and other state-sponsored
actors aiming to access Western companies.

With the advent of seamless real-time voice
cloning, attackers can now convincingly replicate
a person’s complete audiovisual identity in live
interactions, a capability that was not realistically
accessible at scale until recently.

IDENTITY, ONCE GROUNDED IN APPEARANCE,
VOICE, AND PERSONAL INTERACTION, HAS
BECOME ONE OF THE MOST FRAGILE AND
AGGRESSIVELY TARGETED COMPONENTS OF
THE DIGITAL ECOSYSTEM.

Video Impersonation: From Pre-Recorded
Deepfakes to Live Face-Swapping

Two distinct forms of deepfake video
manipulation matured significantly in 2025. Pre-
recorded deepfakes were used in a wide range of
scams, from investment fraud to sextortion and
political influence efforts. In Georgia, a notable

AI-generated identities and deepfake Know Your
Customer (KYC) submissions rapidly became a
preferred method for obtaining initial access.
Fraudsters now create synthetic identities, forged
documents, and fully fake identities to open
bank accounts, reactivate suspended ones, or
bypass verification steps on financial and online
services. The market for these capabilities is well-

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   56

established: simple AI-generated face images can
be purchased at low cost, while more sophisticated,
region-specific KYC packages command significantly
higher prices. In 2025, law enforcement in Hong
Kong arrested eight suspects for allegedly using AI-
generated deepfake images to bypass banks’ online
identity verification and open fraudulent accounts.
This incident demonstrated that such methods are
actively used in real-world account fraud schemes.

These developments contribute to a broader shift
in which audio-visual identity itself is becoming

unreliable. Throughout 2025, attackers increasingly
exploited generative models to imitate people’s
appearances and voices with a level of realism that
defeats traditional verification methods. Automated
systems replaced human scammers in many
operations, and fully autonomous, multilingual
phone-fraud tools reached operational maturity. The
result is a landscape in which identity, once grounded
in appearance, voice, and personal interaction, has
become one of the most fragile and aggressively
targeted components of the digital ecosystem.

MEDIA
TYPE

OFFLINE GENERATION

REALTIME GENERATION

FULLY AUTONOMOUS

TEXT

Pre-rendered
scripts or emails

Real-time
generated
responses

AUDIO

Pre-recorded
impersonations

Real-time voice
manipulation

VIDEO

Pre-created
deepfake videos

Live face-swapping
or video alteration

AI-generated,
fully interactive
conversations

Fully AI-driven
conversational
audio

Completely
automated,
AI-generated
interactive video

Figure 3: GenAI maturity level. (Red V marks technology already available in markets and exploited in the wild)

AI IN MALWARE DEVELOPMENT
AND THE RISE OF AUTONOMOUS
OPERATIONS

While identity theft accounted for the highest
volume of AI-enabled attacks, the most profound
transformation in 2025 occurred in malware
development and orchestration. Throughout the

year, Check Point Research and other organizations
documented the shift from AI as an “assistant” to the
first signs of AI as an operator within the kill chain.

By 2025, the use of AI in malware development
had evolved from isolated experiments to
repeated, observable activity in the wild. OpenAI’s
June disclosures offered an early example with
ScopeCreep, a multi-stage Go-based malware

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   57

family produced through iterative jailbreaking.
Around the same time, the Xanthorox project
promoted an entire suite of malicious tools,
including a keylogger, ransomware, and an
exe-to-JavaScript crypter, claiming its internal
LLM pipeline generated them. Although the
resulting samples displayed modest technical
sophistication, what they really showed was the
appeal of AI-automated toolchains among less
experienced actors. FunkSec, a ransomware
group profiled in earlier this year, openly
acknowledged that portions of its coding and
tooling were developed with the assistance of AI.

IN JULY, CHECK POINT RESEARCH
DOCUMENTED SKYNET MALWARE
EMBEDDING A NATURAL-LANGUAGE PROMPT
INJECTION TO DECEIVE AI-BASED SECURITY
MECHANISMS.

In July, Check Point Research documented
a Skynet malware sample that embedded
a natural-language prompt injection string
designed to deceive AI-based security
mechanisms. This was an early indication that
malware authors were beginning to treat AI
detection engines as targets. A further step
in AI-enabled operations appeared when the
Computer Emergency Response Team of Ukraine
(CERT-UA) reported LAMEHUG, a malware
variant attributed to the Russian-affiliated APT28
group. Rather than relying on a fixed C2 protocol,
operators funneled instructions through Qwen 2.5, an
AI model hosted on Hugging Face’s API. This allowed

system-reconnaissance commands to be generated
dynamically and on demand, producing polymorphic
behavior that blended into legitimate AI API traffic.
Although the campaign was likely just a proof-of-
concept, it demonstrated that LLMs can serve as
highly flexible C2 engines, capable of generating novel
commands, mutating behavior, and complicating
signature-based detection far more effectively than
traditional static infrastructures. This experiment
offered an early glimpse of what fully autonomous
attack orchestration might look like. However,
the most significant evidence of such capabilities
emerged only months later.

The most consequential AI-enabled intrusion of 2025
came from Anthropic’s investigation into the China-
affiliated group, GTG-1002. This campaign represents
the first publicly documented case in which an AI
system conducted the majority of a cyber espionage
operation with minimal human oversight. According
to Anthropic’s analysis, Claude Code handled
roughly 80 to 90 percent of the tactical tasks across
the intrusion lifecycle, including reconnaissance,
vulnerability identification, exploit development,
credential harvesting, lateral movement, data
extraction, and intelligence triage. The operators
manipulated the model using detailed role-play
prompts, persuading it that each action formed part
of a legitimate defensive assessment. Once activated,
Claude maintained persistent context across
sessions, enabling complex multi-day operations
without requiring human operators to restate
objectives or reconstruct the state.

GTG-1002 targeted approximately thirty organizations,
including major technology companies and
government agencies. Its framework relied heavily on
MCP to integrate external tools, automate workflows,
and chain actions across multiple sub-agents.
This architecture is significant because it shows
an AI model acting not merely as a content or code
generator, but as an autonomous operational engine
capable of conducting a coordinated intrusion at
scale.

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   58

Taken together, these findings illustrate a profound
shift: the boundary between human-directed and
AI-directed cyber operations is beginning to blur.
AI is no longer limited to drafting phishing emails
or generating code fragments; it is increasingly
taking on the role of an operator inside the intrusion
lifecycle, thereby lowering the cost and expertise
required for advanced cyber activity.

OUTLOOK

By late 2025, AI shifted from a support tool to an
active participant in cyber operations. Campaigns
such as GTG-1002 and the LAMEHUG experiment
demonstrated that AI systems, in the hands
of capable and sophisticated actors, can now
autonomously perform a significant portion of

the intrusion lifecycle, from reconnaissance
to exploitation and data handling. At the same
time, real-time face-swapping, voice cloning,
and automated scam platforms demonstrated
that identity verification through appearance and
speech can no longer be trusted. The supporting
technologies around AI also proved vulnerable.
Misconfigured MCPs, prompt-injection pathways,
malicious packages, and altered tool descriptors
illustrated that the infrastructure surrounding LLMs
can itself become a vector for compromise. Cyber
attacks increasingly blend human decision-making
with AI-driven execution. AI is no longer a separate
element within cyber security; it is now interwoven
throughout the entire landscape.

AI is expanding the attack surface and accelerating the
attacker playbook. Models, data, and AI integrations across
hybrid environments now require first-class protection, while
adversaries use AI to scale social engineering, speed up malware
development, and exploit vulnerabilities faster. Keeping pace
will require tighter governance and controls across the AI stack,
alongside AI-enabled detection and response.

MICHAEL ABRAMZON

Architect
Threat Intelligence and Research

CHAPTER 03

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   59

04

GLOBAL ANALYSIS

GLOBAL THREAT INDEX MAP

This map displays the global cyber threat risk index, highlighting high-risk areas worldwide.

Figure 1: Global Threat Index Map.

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   61

Higher riskInsufficient DataLower riskATTACKS PER ORGANIZATION

Check Point’s global telemetry indicates a steady and continuing rise in weekly cyber attacks per
organization. Cyber attacks increased sharply in 2024 and continued to climb in 2025, reaching the
highest level recorded during this period. By 2025, organizations faced an average of 1,968 cyber attacks
per week. This marks an 18% year-over-year (YoY) increase and nearly a 70% increase since 2023, which
further highlights the ongoing escalation in overall threat activity.

Figure 2: Average Weekly Cyber Attacks per Organization, 2023-2025

ATTACK ACTIVITY BY REGION

The increase in the average number of cyber attacks per organization was not evenly distributed across
regions. In 2025, North America recorded a 23% year-over-year increase and Europe a 20% increase,
while Latin America (13%) and APAC (10%) showed more moderate growth. Africa remained the most
heavily affected region in terms of volume, averaging over 3,000 attacks per organization per week. Still, it
showed the most minor year-over-year change in 2025, with a 5% increase.

Figure 3: Average Weekly Cyber Attacks per Organization by Region, 2025 [% of Change from 2024]

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   62

Africa3092 [+5%]2909 [+10%]2795 [+13%]1642 [+20%]1422 [+23]APACLatin AmericaEuropeNorth America1968167311622,5002,0003002001000202320242025WEEKLY ATTACKS BY INDUSTRY AND REGION
GLOBAL

Figure 4: Global Average Weekly Cyber Attacks per Organization by Industry, 2025 [% of Change from 2024]

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   63

Business ServicesMedia & EntertainmentSoftwareHardware & SemiconductorsHospitality, Travel & RecreationAerospace & DefenseAutomotiveAssociations & Non ProfitsEnergy & UtilitiesHealthcare & MedicalTelecommunicationsGovernmentEducation1741 [+21%]1779 [+15%]1834 [+35%]1893 [+34%]1905 [+50%]1909 [+21%]1986 [+28%]2143 [+41%]2168 [+37%]2365 [+7%]2656 [+27%]2683 [+17%]4352 [+22%]1738 [+12%]1735 [+15%]1600 [+1%]1567 [+19%]1522 [+78%]1512 [+2%]1376 [-3%]1330 [-6%]1187 [+0.6%]1148 [+36%]Consumer Goods & ServicesFinancial ServicesConstruction & EngineeringIndustrial ManufacturingAgricultureBiotech & PharmaceuticalsWholesale & DistributionReal Estate, Rentals & LeasingTransportation & LogisticsInformation TechnologyIn 2025, cyber attack activity increased across
all regions and nearly every industry. Once
again, Education remained the most targeted
sector, averaging 4,352 attacks per organization
per week, a 22% increase over the previous
year. Government, Telecommunications, and
Healthcare & Medical also reached their highest
observed weekly attack volumes.

Agriculture’s increase aligns with the rapid
digital transformation of agriculture supply
chains, including sorting and production facilities.
Increased reliance on IoT, edge computing, and
autonomous systems has improved efficiency and
output, but also expanded the attack surface across
devices, networks, and data platforms, creating
new opportunities for threat actors to exploit.

As threat actors expanded their focus, critical
infrastructure and industrial sectors experienced
a sharp escalation in the number of attacks.
In 2025, Energy and Utilities, Automotive,
and Aerospace and Defense recorded year-
over-year increases ranging from 21% to 37%.
These sectors underpin essential services and
national infrastructure, making them particularly
attractive targets for exploitation.

In 2025, attacks against the Hospitality, Travel,
and Recreation sector increased by 50% year-
over-year, second only to Agriculture, which saw
a 78% increase. This shift highlights growing
interest in industries with high transaction
volumes and PII (Personally Identifiable
Information) data.

AGRICULTURE INCREASED RELIANCE ON
IOT, EDGE COMPUTING, AND AUTONOMOUS
SYSTEMS HAS IMPROVED EFFICIENCY AND
OUTPUT, BUT ALSO EXPANDED THE ATTACK
SURFACE ACROSS DEVICES, NETWORKS,
AND DATA PLATFORMS, CREATING NEW
OPPORTUNITIES FOR THREAT ACTORS TO
EXPLOIT.

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   64

WEEKLY ATTACKS BY INDUSTRY AND REGION
NORTH AMERICA

Figure 5: North America Average Weekly Cyber Attacks per Organization by Industry, 2025
[% of Change from 2024]

* Insufficient data for 2024

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   65

Biotech & PharmaceuticalsTelecommunicationsBusiness ServicesGovernmentFinancial ServicesAssociations & Non ProfitsConsumer Goods & ServicesAerospace & DefenceMedia & EntertainmentSoftwareEnergy & UtilitiesHealthcare & MedicalEducation1220 [-16%]1306 [+16%]1344 [+26%]1467 [+17%]1494 [+28%]1588 [+6%]1683 [+7%]1711 [*]1744 [+13%]1970 [+61%]1991 [+88%]2121 [+18%]3057 [+32%]967 [-12%]884 [+16%]866 [+14%]851 [+38%]834 [+59%]792 [+24%]786 [-10%]692 [-13%]531 [+57%]490 [*]AutomotiveReal Estate, Rentals & LeasingWholesale & DistributionTransportation & LogisticsHospitality, Travel & RecreationHardware & SemiconductorsIndustrial ManufacturingConstruction & EngineeringInformation TechnologyAgricultureWEEKLY ATTACKS BY INDUSTRY AND REGION
LATIN AMERICA

Figure 6: Latin America Average Weekly Cyber Attacks per Organization by Industry, 2025
[% of Change from 2024]

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   66

Wholesale & DistributionConstruction & EngineeringInformation TechnologyConsumer Goods & ServicesMedia & EntertainmentEnergy & UtilitiesIndustrial ManufacturingFinancial ServicesBusiness ServicesEducationTelecommunicationsGovernmentHealthcare & Medical1259 [+14%]1378 [-13%]1423 [+0.03%]1523 [-4%]1773 [+25%]2112 [-1%]2290 [+38%]2416 [+7%]2790 [+38%]3350 [+19%]3581 [+5%]4240 [+19%]4782 [+64%]1187 [-47%]1146 [-25%]958 [+22%]874 [-43%]Transportation & LogisticsBiotech & PharmaceuticalsSoftwareAutomotiveWEEKLY ATTACKS BY INDUSTRY AND REGION
APAC

Figure 7: APAC Average Weekly Cyber Attacks per Organization by Industry, 2025  [% of Change from 2024]

* Insufficient data for 2024

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   67

Business ServicesConstruction & EngineeringIndustrial ManufacturingEnergy & UtilitiesHospitality, Travel & RecreationAutomotiveHealthcare & MedicalHardware & SemiconductorsTelecommunicationsGovernmentEducation2629 [+12%]3024 [+0.2%]3060 [+16%]3147 [+16%]3184 [+11%]3263 [+30%]3489 [-32%]4006 [+29%]4686 [+53%]4894 [+16%]7648 [+14%]2409 [-17%]2337 [+49%]2238 [+17%]2168 [+12%]2115 [+10%]2114 [+12%]1980 [+4%]1845 [*]1803 [+9%]1172 [-19%]Real Estate, Rentals & LeasingInformation TechnologyConsumer Goods & ServicesSoftwareFinancial ServicesBiotech & PharmaceuticalsTransportation & LogisticsAssociations & Non ProfitsMedia & EntertainmentWholesale & DistributionWEEKLY ATTACKS BY INDUSTRY AND REGION
EUROPE

Figure 8: Europe Average Weekly Cyber Attacks per Organization by Industry, 2025 [% of Change from 2024]

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   68

Wholesale & DistributionEnergy & UtilitiesSoftwareMedia & EntertainmentAgricultureAssociations & Non ProfitsAutomotiveAerospace & DefenceHealthcare & MedicalHospitality, Travel & RecreationGovernmentTelecommunicationsEducation1587 [+8%]1664 [+59%]1668 [+34%]1671 [+9%]1676 [+35%]1708 [+36%]1774 [+35%]1799 [+49%]1980 [+8%]2140 [+60%]2208 [+20%]2243 [+28%]4120 [+19%]1513 [+11%]1476 [+11%]1474 [+11%]1416 [+19%]1403 [+75%]1233 [+45%]1204 [+32%]1195 [+12%]1092 [-9%]1072 [-3%]Consumer Goods & ServicesConstruction & EngineeringBiotech & PharmaceuticalsBusiness ServicesHardware & SemiconductorsInformation TechnologyIndustrial ManufacturingFinancial ServicesTransportation & LogisticsReal Estate, Rentals & LeasingIn North America, Healthcare and Medical continued
to be a major target with an 18% increase in the
average number of weekly cyber-attacks compared to
2024. In the first half of 2025, hundreds of health data
breaches were reported in the United States and across
Latin America. Healthcare in both regions also faced
hundreds of ransomware attacks throughout the year.

As with global statistics, Education was the most
heavily targeted sector in APAC, recording the highest
attack volumes in the region. The sheer number of
average weekly attacks was disproportionate to other
regions, with attack volumes in APAC nearly twice
those observed in other regions. Within APAC, India
experienced the highest average attack volume, at
7,684 weekly attacks.

Educational organizations hold large amounts of
personal data and valuable research. Together with
the fact that schools and universities typically have
open network policies, they become attractive targets,
resulting in both targeted and opportunistic attacks.

Globally, the Hardware and Semiconductors sector
recorded a 34% increase year-over-year in weekly
attacks. In 2025, APAC remained the most targeted,
averaging 4,006 attacks per week, over three times
the volume observed in other regions.

Within APAC, Taiwan and China were the most
heavily targeted countries, with 7,393 and 5,631
attacks, respectively. This concentration aligns with
APAC’s central role in the global Hardware and
Semiconductors supply chain and its prominence in
advanced manufacturing.

In Europe, Hardware and Semiconductors saw a
staggering 75% year-over-year increase in attacks,
whereas North America also had an increase of a
24% in average weekly attacks. This trend aligns
with European and United States strategic efforts
to expand domestic semiconductor manufacturing
under initiatives like the European Chips Act,
increasing the attractiveness of European fabricators,
suppliers, and R&D hubs as targets for espionage,

disruption, and intellectual property theft. As Europe
accelerates its shift toward localized chip production,
cyber threat activity against its semiconductor
ecosystem rises in parallel.

The Telecommunications sector saw a 53% in attacks
in APAC, with double-digit increases also observed
in North America and Europe. Several major cyber
incidents impact multiple regions. Bouygues
Telecom in Europe suffered a significant customer
data breach. SK Telecom in Asia exposed sensitive
SIM data belonging to millions of users. A Canadian
telecom was infiltrated by a China-linked group
through an unpatched Cisco device. Cellcom in the
United States experienced a cyberattack that caused
a prolonged service outage. These incidents aligned
with a wider cross-regional campaign assessed to
be related to a Chinese-affiliated threat actor Salt
Typhoon, which targeted telecom infrastructure on
multiple continents. All these add up to a pattern of
consistent focus on gaining access to core systems
and sensitive subscriber data.

The Energy and Utilities sector experienced a
significant increase in attack levels, with the average
number of weekly attacks rising by 88% in North
America and 59% in Europe. This pattern aligns with
the broader trend of geopolitically driven cyber activity
we observed over the past year. We continue to see a
correlation between kinetic geopolitical conflicts and
heightened offensive cyber operations, particularly
against critical infrastructure.

State-aligned or state-affiliated threat actors appear
to be pursuing differing objectives depending on their
geopolitical alignment, ranging from intelligence
collection and strategic access to disruption and
signaling. Public reporting from U.S. government
agencies, including the Office of the Director of
National Intelligence (ODNI), indicates that Russia,
China, Iran, and North Korea continue to prioritize
cyber operations targeting critical infrastructure and
telecommunications.

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   69

ATTACK VECTORS
Attack Delivery Vectors (Email vs. Web)

Figure 9: Attack Delivery Vectors (Email vs. Web), 2023-2025

In 2025, email-based attacks carrying malicious files accounted for 82% of all observed activity, while web-based
attacks represented 18%. This highlights the ongoing trend of attackers favoring email as the primary method for
delivering file-based attacks. Except for 2024, where we saw a temporary 21% decline, the dominance of email-
based attacks has steadily increased since 2018. According to Check Point Harmony Email and Collaboration
data, approximately one of every 68 emails with attachments received by an organization is malicious.

Top Malicious File Types Delivered via Email

Figure 10: Email: Top Malicious File Types, 2025
html* includes common files such as .html, .shtml, .htm, and more.
doc* includes common Office Word files such as .doc, .docx, docm, and .dot
xls* includes common Office Excel files such as .xls, .xlsx, .xlsm, and more

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   70

MailWeb100%40%80%20%60%020232024202589%68%82%11%32%18%0.3%0.3%0.9%1.3%2%3%3%19%34%34%rtfdllxls*rardoc*exezippdfsvghtml*Throughout 2025, Check Point tracked global
phishing campaigns targeting organizations
worldwide. Attackers continue to rely on weaponized,
commonly used file types that recipients are
incentivized to open. In addition, attackers attempt to
innovate and find new ways to abuse file types with
lower detection rates and weaker security defenses.

MOST ATTACKERS AVOID EXECUTABLES
IN THE INITIAL STAGE, RELYING ON
MULTISTAGE PHISHING INSTEAD

In 2024, malicious HTML attachments accounted for
61% of email-based attacks. However, in 2025, the
landscape diversified, as SVG and HTML together
surpassed that percentage, each at 34%. PDF
files remained prominent at 19%, while EXE files
accounted for only 3%. This distribution suggests
most attackers avoid direct executable attachments
in the initial stage and instead rely on phishing
campaigns or multistage infection chains using
formats such as HTML, SVG, and PDF.

SVG files, initially intended for displaying vector
graphics, are abused by attackers to serve a
role similar to that of malicious HTML files. Both are
opened in web browsers by default and can be used
to create convincing phishing pages, execute scripts
within the browser, perform HTML or SVG smuggling,
or act as the initial stage of a more sophisticated
attack. In some cases, attackers even combined the
two and embedded HTML code inside the SVG files.

Notable SVG waves targeted financial
institutions using the SVG smuggling technique,
where an SVG file drops embedded JavaScript files
for the victim to execute.  This is the initial stage of
a multistage attack, ultimately deploying a variety
of RAT malware, such as Blue Banana, SambaSpy,
and SessionBot.

In another wave, the Shadow Vector threat
group targeted Colombian users with court-themed
SVG decoys. The goal was to redirect victims to JS/VBS
stagers or password-protected ZIP payloads, then use
leveraged DLL side-loading and privilege escalation to
deploy RATs like AsyncRAT and RemcosRAT.

Top Malicious File Types Delivered via Web

Figure 11: Web: Top Malicious File Types, 2025
xls* includes common Office Excel files such as .xls, .xlsx, .xlsm, and more
doc* includes common Office Word files such as .doc, .docx, docm, and .dot

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   71

0.9%0.9%1.1%1.5%2%3%3%5%5%65%doc*xlspyshdexelflnkdllpdfexeThe distribution of popular malicious file types is
significantly different on web-based infection vectors.
Instead of persuading a user to click on phishing
links to initiate an elaborate chain that bypasses an
email security gateway, many web-based downloads
and drive-by chains attempt to land an executable
payload immediately. Our 2025 telemetry shows
attackers overwhelmingly favor executable formats.
EXE files accounted for 65% of web-delivered
malware, while the next runner-up, PDF, was at only
5%, indicating a strong preference for direct execution
over document-based lures. This tendency is
reinforced by prominent web vectors, like SEO
poisoning, that promote fake download pages in
search results, Trojanized “legitimate” installers that
deploy the genuine software while quietly loading
malware, and software supply chain compromises
where attackers publish Trojanized packages that
execute during installation. Gamers are also
heavily targeted through Trojanized game-related
tools, cheats, and cracked software distributed via
torrents and file-sharing sites, which can drop
miners, stealers, or loaders.

THE INFOSTEALER ECOSYSTEM

When law enforcement takedown operations
disrupted major botnets, such as Qbot and Emotet, in
Operation Endgame, followed by Operation Endgame
2.0, they also removed a significant initial infection

method for the average threat actor. Attackers
who were accustomed to buying direct access to
organizations worldwide through these botnets had
to adjust their tactics. Infostealers then became a
favorite alternative method, and infostealer logs and
credentials, shared and sold in the underground
communities, became the fuel to support future initial
infections.

Since then, infostealer logs have become an
escalating cybersecurity risk, as they contain
large volumes of stolen sensitive information,
including account credentials, payment card details,
and cryptocurrency wallets, all extracted from
compromised systems. Generated by infostealer
malware and widely traded across underground
marketplaces and Telegram channels, these logs
now serve as a primary enabler for follow-up attacks,
supporting a broader ecosystem of cybercrime,
including fraud, account takeovers, and ransomware
operations. Check Point’s Exposure Management
actively monitors and tracks these sources, and
the following data highlights the most prominent
infostealer families.

Lumma dominated the infostealer logs landscape
at 43%. This number indicates a slight decrease
from last year’s 51%, likely due to increased law
enforcement activity. The veteran Redline is the only
close contender that held 22% of the logs, a clear
rise from last year’s 8%.

Figure 12: Top Infostealer Malware Globally, 2025

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   72

43%22%14%12%5%lummaredlinemetastealcvidarBy analyzing the data dumps, we see for the
second consecutive year that credentials to
gaming platforms such as Roblox and Steam
continue to top the list. This finding correlates
strongly with the fact that gaming platforms
remain one of the most prominent and effective
vectors for the distribution of infostealers. A
wide variety of themes and lures are used to
facilitate the spread of infostealers through
games available on the Steam online store, as
demonstrated by cases such as PirateFi and
the Vidor infostealer. In addition, infostealers
like Stealka frequently disguise themselves
as game-related content, including cracks,
cheats, and mods, taking advantage of users’
willingness to download unofficial or modified
gaming software.

Although Brazil ranks among the most targeted
countries, accounting for approximately 7% of
all observed infostealer activity, it represents
only roughly one-third of that share when
measured against its proportion of the global
population. At the same time, six of the top ten
most targeted countries are located in Asia,
despite the fact that these countries collectively
account for just over 28% of the world’s
population, highlighting a disproportionate level
of targeting relative to population size.

ACCORDING TO THE LOG DATA WE ANALYZED,
OVER 76% OF THE INFECTED MACHINES ARE
LIKELY NON-CORPORATE ONES, COMPARED
WITH 70% LAST YEAR.

According to the log data we analyzed, over
76% of the infected machines are likely non-
corporate ones, compared with 70% last year.
This notable increase further highlights the
growing use of the “spray and pray” strategy,
in which attackers seek to penetrate highly
protected corporate environments by first
compromising less-secured endpoints. In this
approach, threat actors initially gain access
to BYOD or otherwise unmanaged devices
that are connected, directly or indirectly, to
corporate networks. These devices often
serve as a convenient entry point, as they
may lack enterprise-grade security controls.
The connection to the corporate environment
can take many forms, including VPN access,
Microsoft 365 accounts, collaboration
platforms, or other corporate services for which
credentials, session tokens, and cookies are
stored in the browser, enabling attackers to
later pivot into organizational systems.

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   73

Figure 13: Infostealer logs for sale - top countries, 2025

Cyber risk in 2025 has shown rapid expansion across regions,
industries, and technologies. Keeping up with external threats
and internal exposure risks requires unified visibility, continuous
exposure management, and security controls that organizations
can validate and enforce across their own environments.

OMER DEMBINSKY

Data Research
Group Manager

CHAPTER 04

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   74

Brazil7%7%4%4%4%4%3%3%3%3%58%IndiaPakistanIndonesiaVietnamEgyptUnited StatesPhilippinesArgentinaTurkeyRest of World05

HIGH PROFILE
VULNERABILITIES

1. ToolShell Vulnerabilities

ToolShell is a set of SharePoint on-premise
vulnerabilities involving CVE-2025-49704
and CVE-2025-49706, with later variants
designated as CVE-2025-53770 and CVE-2025-
53771. Chaining these vulnerabilities enables
unauthenticated remote code execution (RCE)
on vulnerable on-prem SharePoint servers.
Check Point Research observed multiple waves
of exploitation by various threat actors, including
Ink Dragon. In some cases, the exploitation was
the initial step in an espionage operation, while in
others, it led to the deployment of ransomware.
For example, threat actors used ToolShell to
deploy Warlock and LockBit Black in targeted
networks.

Notably, ToolShell was exploited in the wild
before patches were publicly available. According
to Check Point data, the first known exploitation
occurred on July 7, with broader exploitation
attempts starting on July 18. The exploitation
attempts related to this vulnerability affected 12%
of organizations.

2. Langflow Remote Code Execution

(CVE-2025-3248)

In April 2025, a critical remote-code execution
vulnerability (CVE-2025-3248) was disclosed
in Langflow, a popular open-source visual
framework for building and deploying AI
workflows. This vulnerability affects all
versions prior to 1.3.0. The flaw fails to require
authentication and insufficiently sanitizes
user-supplied code, allowing an attacker to
send a specially crafted HTTP request and
execute arbitrary Python code on the server.
The vulnerability on the server is classified as

high severity, with a CVSS 3.1 base score of
9.8 (Critical). Public proof-of-concept (PoC)
exploits are available, and real-world exploitation
has been confirmed. Compromised Langflow
instances were used to deploy the Flodrix botnet,
which enables the creation of backdoors, DDoS
capabilities, and potential data exfiltration.

3. Oracle E-Business Suite
(CVE-2025-61884)

CVE-2025-61884 is a critical server-side request
forgery vulnerability in Oracle E-Business Suite
(EBS) that affects the Configurator Runtime
UI component in versions 12.2.3 through
12.2.14. The flaw allows an unauthenticated,
remote attacker to send crafted requests
that are executed by an application against
internal services, potentially exposing sensitive
business data and authentication metadata.
The vulnerability was exploited by threat actors
associated with the CL0P extortion operation,
which used it to access internal EBS resources
and steal business-critical data from over
100 organizations. Months after the Cl0p
exploitation, a working PoC was leaked by the
Scattered LAPSUS$ Hunters collective. The
leak enabled large-scale data theft, including
configuration information and financial records,
which were later used in extortion campaigns.
CISA confirmed the active exploitation and
added CVE-2025-61884 to the Known Exploited
Vulnerabilities catalog.

4. React2Shell (CVE-2025-55182)

CVE-2025-55182, known as React2Shell, is a
critical remote code execution vulnerability in
React Server Components (RSC). It stems from
unsafe deserialization in the RSC Flight protocol,
which allows an unauthenticated attacker to send
a crafted payload to trigger code execution on the
server. The flaw affects multiple RSC packages in

CHAPTER 05

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   76

React versions 19.0, 19.1.0, 19.1.1, and 19.2.0, as
well as frameworks that use them, such as Next.
js. According to Check Point data, after the public
disclosure and release of the PoC, multiple
threat actors began exploiting the vulnerability
within 24 hours. China-affiliated threat groups,
including Earth Lamia and Jackpot Panda, were

observed using the exploit for malicious activity.
Exploitation attempts deliver malware, establish
backdoors, and scan for vulnerable deployments.
On the first day of exploitation alone, we saw
479 exploitation attempts, and overall, during
December, these attempts impacted 22% of
organizations.

Figure 1: Percentage of Attacks Leveraging Vulnerabilities by Disclosure Year, 2025

Analysis of attack data indicates that
vulnerabilities disclosed in 2025 accounted
for 4% of all exploitation attempts. The time-
to-exploitation has become lower every year,
as observed with ToolShell and React2Shell.
At the same time, attackers continue to rely

heavily on older vulnerabilities, with more than
46% of exploitation attempts exploiting CVEs
published prior to 2020. This reflects a persistent
systemic gap in patching, where many system
vulnerabilities remain unaddressed for years
despite the existence of available fixes.

CHAPTER 05

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   77

Earlier201520172018201920202021202220232024202517.2%3.0%6.0%3.9%6.9%9.1%8.9%10.9%8.2%10.7%11.0%4.0%201606

2026 INDUSTRY PREDICTIONS:
THE FUTURE OF CYBER SECURITY

The following predictions highlight the most
consequential shifts shaping cyber security in
2026, spanning attacker behavior, technology
evolution, and the changing expectations placed
on organizations to manage and prove resilience.

1. Agentic AI Transitions from

Assistance to Operational Autonomy

2026 will see agentic AI move to the mainstream.
Autonomous systems capable of reasoning,
planning, and acting with minimal human input
move us from assistants who draft content to
agents who execute strategy. These systems will
allocate budgets, monitor production lines, and
reroute logistics, all in real-time.

Manufacturing environments will increasingly
be able to self-diagnose faults and trigger
automated procurement through blockchain-
verified supply networks. At the same time,
marketing, finance, and security teams will
depend on agents that continuously absorb
contextual signals and operate at machine speed.

Autonomy without accountability is a liability.
According to the World Economic Forum’s Global
Cyber Security Outlook 2025, AI autonomy
without governance is one of the top three
systemic risks to enterprise resilience.

As these agents gain real operational authority,
unresolved governance questions surface: who
validates autonomous decisions, audits decision
logic, or intervenes when intended actions
and real-world outcomes diverge? Addressing
this gap will require AI governance councils,
enforceable policy guardrails, and immutable
audit mechanisms that record and explain every
autonomous action.

ADDRESSING THE AI AUTONOMY
GOVERNANCE GAP WILL REQUIRE AI
GOVERNANCE COUNCILS, ENFORCEABLE
POLICY GUARDRAILS, AND IMMUTABLE
AUDIT MECHANISMS THAT RECORD AND
EXPLAIN EVERY AUTONOMOUS ACTION.

2. Prompt Injection and Data Poisoning -
AI Models Become the New Zero-Day

As generative AI is embedded across customer-
facing services, internal workflows, and
security operations, AI models themselves are
emerging as high-value attack surfaces. In 2026,
adversaries will increasingly exploit prompt
injection, embedding covert instructions in text,
code, or documents that manipulate model
behavior, as well as data poisoning, where tainted
inputs distort or compromise training data.

Because many LLMs operate via third-party APIs,
just one poisoned dataset can propagate across
thousands of applications. Conventional patching
offers limited protection in this context; maintaining
model integrity becomes an ongoing process.

AI models are today’s unpatched systems. Every
external data source represents a potential
exploit path. In 2026, AI security leaders will
differentiate themselves by operationalizing
governance, validation, and continuous oversight
to ensure AI systems remain trustworthy at
scale.

CHAPTER 06

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   79

Organizations must extend visibility to third-
party and fourth-party SaaS supply chain sites
and adopt continuous monitoring and Zero Trust
access to manage an attack surface that is
increasingly expanding beyond their perimeter.

4. Trust Is the New Perimeter:

Deepfakes and Conversational Fraud

Generative AI has blurred the line between
genuine and fabricated content. Voice cloning,
real-time synthetic video, and AI-driven chat
interactions now enable attackers to bypass
traditional identity and access controls, including
multi-factor authentication. ENISA’s Threat
Landscape 2025 lists “synthetic identity and AI-
generated social engineering” among the top five
risk vectors.

Technical authenticity no longer guarantees
human authenticity or that interactions even
originate from a human at all. As non-human
identities (NHIs) proliferate alongside AI
agents and automated systems, every human–
machine interface becomes a potential point
of compromise. Business Email Compromise
will evolve into trust-based fraud, conducted
through deepfakes, adaptive language, and
emotional manipulation. This year, deception will
sound like trust. Enterprises must continuously
verify identity, context, and intent across every
interaction.

3. Supply Chain and SaaS Exposure

Intensifies Across Hyperconnected
Ecosystems

Enterprises now operate within webs of vendors,
APIs, and integrations, creating attack paths
where just one weak supplier can lead to
widespread compromise. As ecosystems grow
more automated and interdependent, incidents
spread faster through shared code, tokens,
and cloud services than they can be traced.
The ENISA Supply Chain Cybersecurity Report
2025 warns that 62% of large organizations
experienced at least one third-party compromise
in the past year.

At the same time, global supply chains are
transforming under the pressure of automation.
Agentic AI will enable autonomous risk
management: self-learning systems that map
dependencies, monitor third-party compliance,
and predict disruptions. Yet hyperconnectivity
also magnifies exposure: compromised code
libraries, API tokens, and cloud credentials can
ripple through ecosystems faster than incidents
can be traced.

ORGANIZATIONS MUST EXTEND VISIBILITY
TO THIRD-PARTY AND FOURTH-PARTY
SAAS SUPPLY CHAIN SITES AND ADOPT
CONTINUOUS MONITORING AND ZERO TRUST
ACCESS TO MANAGE AN ATTACK SURFACE
THAT IS INCREASINGLY EXPANDING BEYOND
THEIR PERIMETER.

CHAPTER 06

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   80

5. Quantum Risk Moves From Long-
Term Concern to Near-Term Action

Quantum computing may still be years from
cracking today’s encryption, but the threat
has already changed, and should continue to
change, enterprise behavior. Governments, cloud
providers, and large enterprises are racing to
secure cryptographic agility, migrating from
vulnerable Rivest–Shamir–Adleman (RSA) and
Elliptic Curve Cryptography (ECC) algorithms
to post-quantum cryptography (PQC) standards
before adversaries can weaponize them.

The danger lies in the 'harvest now, decrypt later'
(HNDL) strategy. Attackers are already stealing
encrypted data today, confident that quantum
decryption will expose it tomorrow. In 2026,
preparation moves from theory to execution.
Boards will fund cryptographic bills of materials
(CBOMs) to catalogue every algorithm, certificate,
and key across their environments. Organizations
will pilot National Institute of Standards and
Technology (NIST)-approved post-quantum
algorithms and pressure vendors to show clear
migration timelines.

Quantum risk is not about tomorrow’s machines.
It is about today’s data. Every organization
must assume its encrypted assets are already
being harvested and prepare for a world where
prevention depends on cryptographic agility.

6. AI Becomes a Strategic Decision Engine

AI is steadily changing the foundations of cyber
security. What once served mainly as a tool for
operational efficiency is now influencing how
both attackers and defenders plan, adapt, and
execute their strategies. The industry is moving
into a phase where AI is no longer a supporting
capability, but an embedded element in detection,
analysis, and decision-making workflows.

This evolution is expected to deepen. Attackers
are already using AI to generate faster, broader,
and more tailored campaigns, and this will
increasingly push organizations to develop
defensive capabilities that can match that pace,
with continuous learning, real-time context, and
more autonomous operational support. It reflects
a shift in how security teams prioritize actions,
understand risk, coordinate response, and
ultimately, increase efficiency.

AI is becoming an integral part of the
operational layer within security operations,
enhancing human expertise, simplifying manual
workflows, and reducing the mean time to
remediation (MTTR).

The accelerated adoption of AI is making it part of
the operational backbone of cyber security rather
than an extension of existing tools, shaping
analytical workflows and decision-making
processes to be more consistent, automated, and
guided by precise controls.

THE ACCELERATED ADOPTION OF AI IS
MAKING IT PART OF THE OPERATIONAL
BACKBONE OF CYBER SECURITY RATHER
THAN AN EXTENSION OF EXISTING TOOLS,
SHAPING ANALYTICAL WORKFLOWS AND
DECISION-MAKING PROCESSES TO BE MORE
CONSISTENT, AUTOMATED, AND GUIDED BY
PRECISE CONTROLS.

CHAPTER 06

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   81

7. The AI Reality Check

After two years of near-frantic AI adoption, we
will experience our first major recalibration.
Many organizations that rushed to integrate
generative AI tools will discover ungoverned
systems, exposed APIs, and compliance blind
spots. Shadow AI, employee-initiated tools using
corporate data, will proliferate, creating invisible
data leaks and inconsistent security standards.

This phase of disillusionment is necessary:
it will drive the shift from experimentation to
accountability. Executives will begin demanding
AI value measured in outcomes, not hype. AI
assurance frameworks will emerge across
various sectors, necessitating formal audits
to ensure fairness, robustness, and security.
Leadership teams must establish clear policies
for AI use and align them with legal, ethical, and
risk frameworks. Responsible deployment will
hinge on explainability and continuous validation,
not unchecked automation. Compliance will
expand from privacy to algorithmic accountability.

AI’s first disruption was speed; its second will
be governance. 2026 will reward those who treat
AI not as a shortcut but as a capability to be
secured, audited, and improved.

AI’S FIRST DISRUPTION WAS SPEED; ITS
SECOND WILL BE GOVERNANCE. 2026 WILL
REWARD THOSE WHO TREAT AI NOT AS
A SHORTCUT BUT AS A CAPABILITY TO BE
SECURED, AUDITED, AND IMPROVED.

8. Regulation and Accountability

Expand - Cyber Resilience Becomes
a License to Operate

Regulators worldwide are closing the gap
between innovation and accountability. In 2026,
regulation ceases to be a reactive approach.
Frameworks such as the EU’s NIS2 Directive, the
AI Act, and the U.S. SEC incident-disclosure rules
will converge on a single principle: cyber security
must be measurable and demonstrable in real-
time. Governments will now expect continuous
proof of resilience. Organizations are expected
to demonstrate that their preventive controls,
incident response plans, and data protection
measures are consistently enforced.

There is a strong reason behind this regulatory
acceleration: society’s growing dependence
on digital services to maintain daily life and
the economy without significant disruptions.
Business resiliency has become the primary
driver behind the increasing compliance
requirements.

This shift will mark the end of the era of “annual
compliance.” Enterprises will rely on automated
compliance monitoring, machine-readable
policies, real-time attestations, and AI-based risk
analytics. Boards and CEOs will carry personal
responsibility for oversight.

Cyber resilience is no longer paperwork;
it’s performance. The ability to demonstrate
protection continuously will determine market
access and trust.

CHAPTER 06

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   82

07

2026 CISO
RECOMMENDATIONS

CISOs should reinforce prevention-led
architectures with continuous validation
and transparency mechanisms that confirm
protections are working under real conditions.
This includes integrating external signals
such as responsible vulnerability disclosure,
targeted security awareness tied to observed
threat activity, and structured programs that
surface weaknesses before adversaries exploit
them. These elements are not substitutes
for prevention, but independent checks that
strengthen confidence in defensive effectiveness
and accelerate improvement.

Why it matters: Adversaries operate at scale,
iterate rapidly, and exploit the first viable
weakness they encounter. Organizations that rely
on single controls or static assurance models are
more likely to experience cascading failure, while
prevention-led, layered programs reduce both
the likelihood and impact of successful attacks.

Security leaders’ primary challenge in 2026
is maintaining the organization's security as
attacker capabilities, techniques, and scale
evolve faster than ever before, touching on wider
attack surfaces, from everyday workflows and
endpoints to hybrid environments composed of
increasingly complex webs of systems. At the
same time, CISOs are expected to demonstrate,
clearly and continuously, operational efficiency
and support measurable business outcomes.
The recommendations that follow reflect the
priorities that CISOs must focus on, including
reducing exposure, governing risk in dynamic
environments, and demonstrating resilience
against an increasingly aggressive and
unpredictable threat landscape.

1. Establish Prevention-Led, Layered

Security Programs

Security programs must be designed to stop
attacks as early as possible while assuming no
single preventive control will be sufficient on
its own. In 2026, effective programs prioritize
prevention at multiple points across the attack
chain, reducing exposure and attack success
rates, while ensuring secondary, complementary
safeguards can contain the impact when prevention
is bypassed. This approach moves beyond
monolithic defenses and toward layered, adaptive
protection that reflects how attackers operate.

CHAPTER 07

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   84

BY JONATHAN FISCHBEIField CISO2. Govern Data Protection as a Core

Security Outcome

Data exposure now represents the most
consequential outcome of modern cyber
incidents, exceeding the business impact of
service disruption alone. Security programs
must therefore treat data protection as a first-
order objective, governed by how sensitive data
is accessed, moved, and aggregated across
environments—not by static classifications
or perimeter assumptions. In this context,
ransomware incidents should be addressed by
default as data-exposure events, with availability
loss viewed as only one dimension of impact.

DATA EXPOSURE NOW REPRESENTS THE
MOST CONSEQUENTIAL OUTCOME OF MODERN
CYBER INCIDENTS, EXCEEDING THE BUSINESS
IMPACT OF SERVICE DISRUPTION ALONE.

CISOs should prioritize architectural controls
that limit data blast radius and recovery risk,
including segmentation of data access paths,
strict least-privilege enforcement, and resilience
measures such as immutable backups and
regularly exercised incident-response playbooks.
These controls must be designed to assume
partial compromise and focus on preventing
large-scale data exfiltration, accelerating
recovery, and preserving trust during and
after an incident. This governance model also
establishes a foundation for emerging risk
domains, including the long-term protection of

sensitive data against future advancements in
cryptography.

Why it matters: Ransomware campaigns
increasingly involve confirmed data exfiltration,
making data exposure, rather than downtime,
the primary source of regulatory, financial, and
reputational impact. Organizations that fail
to govern data protection as a core security
outcome remain vulnerable to compounding
loss during incidents and long-tail risk as data
persists beyond today’s threat horizon.

3. Operationalize Cloud, SaaS, and AI

Security

Cloud, SaaS, and AI environments introduce risk
primarily through speed, scale, and change, not
just misconfiguration. Continuous deployment,
third-party integrations, and automated service
interactions create exposure that cannot be
effectively governed through identity-centric
or compliance-driven controls alone. These
platforms must be secured as living, operational
systems, where risk emerges from how services
interact and execute in real-time.

CISOs should establish governance that
continuously evaluates platform posture and
operational behavior, including configuration
drift, API usage, service-to-service trust, and
application-level interactions. AI systems
require the same operational discipline as other
production platforms, with defined ownership,
monitored usage boundaries, and accountability
for how models are accessed, integrated, and
acted upon. The focus is not on measuring
resilience or enforcing identity policy, but on
maintaining ongoing control over how dynamic
platforms behave as they evolve.

Why it matters: Attackers increasingly exploit
APIs, automation, and runtime interactions to
bypass identity checks and perimeter defenses.

CHAPTER 07

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   85

Without continuous platform governance,
organizations lose visibility and control between
change cycles, creating exploitable gaps that
scale as environments become more complex.

4. Treat Third-Party Risk as Structural

Exposure

Vendors, SaaS providers, and partners are
embedded directly into enterprise environments
through access, integrations, and shared
services.

CISOs should manage third-party risk
as structural exposure, not as a periodic
assessment exercise. This requires continuous
monitoring of vendor access, segmentation
of partner connections, and enforcement of
least-privilege and Zero Trust principles across
external identities.

Security obligations must be measurable and
enforceable through SLAs, but documentation
alone is insufficient. Real risk emerges from how
vendors access systems, what permissions they
hold, and how compromise propagates across
shared trust relationships.

Why it matters: Supply-chain and SaaS-linked
incidents increasingly originate from trusted
vendor access and inherited trust, expanding
blast radius beyond the organization’s direct
control.

5. Anchor Zero Trust Architecture in
Human and Non-Human Identity

Zero Trust must be treated as a core defense
against identity-driven attacks. As phishing,
credential theft, and token abuse enable
attackers to operate as trusted users and non-
human identities, these methods dramatically

expand the attack surface, rendering implicit
trust models and static access assumptions
obsolete. Effective Zero Trust requires continuous
verification of identity and context, least-privilege
access by default, and architectural controls
that limit lateral movement across cloud, SaaS,
network, and development environments. The
goal is not only to prevent misuse of identity, but
to contain the impact when identity is inevitably
compromised.

EFFECTIVE ZERO TRUST REQUIRES
CONTINUOUS VERIFICATION OF IDENTITY
AND CONTEXT, LEAST-PRIVILEGE ACCESS BY
DEFAULT, AND ARCHITECTURAL CONTROLS
THAT LIMIT LATERAL MOVEMENT.

The same Zero Trust principles underpin
resilience against AI-enabled social engineering,
cloud-driven attack surface expansion, and
ransomware operations that increasingly rely on
stolen identities rather than exploits.

Why it matters: Zero Trust is the practical
framework for managing modern identity risk—
reducing implicit trust, constraining blast radius,
and ensuring identity compromise does not
automatically translate into widespread access
or business disruption.

CHAPTER 07

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   86

6. Harden Trust-Based Business
Processes Against Abuse

Attackers are increasingly monetizing access by
exploiting implicit trust in business workflows,
rather than relying solely on technical
compromise. Business Email Compromise
(BEC), executive impersonation, and vendor
fraud remain highly effective because they exploit
legitimate communication channels to initiate
financial transactions, disclose sensitive data,
or modify access permissions. With AI-driven
impersonation on the rise, including realistic
phishing lures, synthetic voice, and deepfake-
assisted social engineering, these attacks have
further increased their credibility and scale,
reducing the time required to move from initial
contact to impact.

controls are particularly critical for executives and
high-risk business functions, where successful
impersonation can enable immediate financial
loss or serve as a precursor to ransomware
deployment by facilitating credential resets, access
expansion, or data exfiltration.

Why it matters: BEC and impersonation
attacks are increasingly serving as both direct
monetization vectors and enablers for ransomware
and extortion campaigns. As attackers blend
social engineering, identity abuse, and AI-enabled
deception, organizations that fail to harden trust-
based workflows remain vulnerable to high-impact
outcomes, even in environments with strong
perimeter and endpoint defenses.
Top of Form
Bottom of Form

WITH AI-DRIVEN IMPERSONATION ON THE
RISE, THESE ATTACKS HAVE INCREASED
THEIR CREDIBILITY AND SCALE, REDUCING
THE TIME REQUIRED TO MOVE FROM INITIAL
CONTACT TO IMPACT.

CISOs should treat trust-based business
processes as a core component of the threat
surface and apply security controls accordingly.
This includes strengthening protections across
email and collaboration platforms, implementing
mandatory, context-aware verification for high-risk
actions, and eliminating single-step approvals and
other implicit trust assumptions from payment,
vendor, and access-granting workflows. These

7. Integrate OT and Cyber Risk

Governance

Operational Technology (OT) environments
now sit at the intersection of cyber risk,
physical safety, and business continuity. As OT
environments increasingly adopt Industry 4.0
architectures—extending industrial systems
through IoT and IIoT devices, cloud connectivity,
and remote access— increased connectivity
between IT and OT—driven by remote access,
cloud monitoring, and digital transformation—
has expanded attack paths into environments
where compromise can result in physical
disruption, safety incidents, or prolonged
operational downtime, not just data loss.

Traditional IT security models are insufficient
in these settings, where availability and
deterministic behavior are paramount, and
active security controls must be applied with
care. Securing this new, cloud-connected OT
environment requires security approaches
that are aligned with its expanded digital and
operational exposure.

CHAPTER 07

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   87

CISOs should ensure that OT security is governed
through a risk-based model aligned with
operational realities, rather than being treated
as a standalone technical domain. This includes
enforcing strict and continuously validated
IT-OT segmentation, leveraging passive and
non-intrusive monitoring to maintain visibility
without disrupting operations, and integrating
OT telemetry into centralized SOC workflows to
enable early detection of abnormal activity.

Just as importantly, cyber, engineering, and
physical safety teams must operate from a
shared risk framework that prioritizes safety,
uptime, and resilience, ensuring cyber incidents
in OT environments are assessed and responded
to with full awareness of their potential physical
and operational impact.

Why it matters: As attackers increasingly
target industrial and critical infrastructure
environments, cyber incidents in OT no longer
represent isolated technical events—they
directly translate into safety risks, operational
disruptions, and material business impacts.
Organizations that fail to secure this modern,
Industry 4.0 OT environment as part of enterprise
cyber risk governance remain vulnerable to
attacks that bypass traditional IT defenses and
exploit the gap between cyber and physical
security.

8. Prove Resilience, Not Just

Compliance

Cyber resilience can no longer be inferred from
policy adherence or point-in-time assessments.
As attack surfaces change continuously and
threats exploit exposure faster than review cycles
can detect, resilience must be measurable,
continuously validated, and expressed in
business-relevant terms. Annual audits and
static risk assessments may satisfy regulatory
requirements, but they do not reflect an

organization’s real-world ability to withstand,
contain, and recover from active threats.

At the same time, increasing complexity across
cloud, automation, and AI environments makes
it critical not to lose focus on cyber hygiene and
security fundamentals. Many successful attacks
still exploit basic weaknesses, underscoring that
resilience depends on maintaining strong “back-
to-basics” practices alongside newer capabilities.

CISOs should shift toward continuous control
validation and exposure-driven measurement,
integrating telemetry from across the
environment to assess not only whether controls
exist, but also whether they are effective under
real-world conditions. This includes monitoring
exposure trends, remediation velocity, and
time-to-contain across attack paths, as well as
automating evidence collection to reduce manual
compliance overhead. Effectiveness must be
communicated differently to boards, regulators,
partners, and customers, using outcome-based
metrics that demonstrate reduced risk, faster
response times, and improved containment,
rather than merely checklist completion.

Signals from digital trust and transparency
programs, such as external vulnerability
reporting, third-party findings, and
responsiveness to disclosed risk, should be
treated as indicators of operational resilience,
not reputational liabilities. These signals
provide independent validation of how quickly
and effectively an organization identifies and
addresses exposure.

Why it matters: In an environment of continuous
threat activity and increasing regulatory scrutiny,
organizations that can demonstrate resilience
through ongoing measurement and real-world
outcomes are better positioned to maintain
trust, meet regulatory expectations, and respond
credibly to incidents than those relying solely on
periodic compliance assessments.

CHAPTER 07

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   88

08

AN EXPOSURE
MANAGEMENT PERSPECTIVE

THREAT INTELLIGENCE BEFORE
THE BREACH

An Exposure Management Perspective

From Incident Response to Preemptive
Security

Incident response is a critical
function in any security
program, but ultimately, it only represents the
final stage of most attacks. By the
time response teams are engaged,
adversaries have already completed
reconnaissance, established infrastructure,
and initiated access. The biggest question
is not how quickly organizations respond to
incidents, but how often those incidents could
have been prevented altogether.

A growing body of intelligence shows that
many attacks leave detectable external signals
well before internal compromise occurs.
These insights, when understood in context,
present an opportunity to reduce reliance on
emergency response by addressing exposure
earlier in the attack lifecycle. From an exposure
management perspective, threat intelligence
plays a foundational role in taking security
programs from reactive containment to
preemptive risk reduction.

This perspective does not replace
incident response or post-
breach investigation. Rather, it complements
them by focusing on the conditions and activities
that precede incidents, with the aim of preventing
issues from ever reaching the point where a
response is required.

THE BIGGEST QUESTION IS NOT HOW
QUICKLY ORGANIZATIONS RESPOND TO
INCIDENTS, BUT HOW OFTEN THOSE
INCIDENTS COULD HAVE BEEN PREVENTED
ALTOGETHER.

What Attackers Do Before the Breach

Before an incident unfolds internally, attackers
typically invest time in preparation. This
preparatory phase often includes activities that
are external to the organization but directly
relevant to its security posture. Common
examples include the creation of look-
alike domains, brand impersonation across
social platforms, deployment of phishing
infrastructure, harvesting of credentials from
prior breaches, and reconnaissance of exposed
services. Individually, these events may appear
disconnected or benign. However, collectively,
they form the earliest indicators of an impending
intrusion attempt.

Crucially, these activities surface outside
traditional internal monitoring controls. They
precede malware execution, lateral movement, or
privilege escalation, and therefore occur before
most incident response triggers are activated. As
a result, they are frequently overlooked or
deprioritized, even though they represent the
earliest stage at which intervention is possible.

CHAPTER 08

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   90

Pre-Incident Intelligence Across the
Global Attack Surface

Across the global attack surface, certain patterns
consistently emerge during the pre-incident
phase. Attackers rarely move directly from
intent to exploitation. Traditionally, they stage
infrastructure, test delivery mechanisms, and
refine targeting based on observed responses.

While the specific prevalence of phishing,
impersonation, or credential-based techniques
varies by sector and geography, these
vectors continue to dominate early attack
activity. Importantly, the same preparation
techniques observed externally often align
closely with the tactics incident response
teams later observe post-breach. The
challenge for defenders is not the absence of
early signals, but the difficulty of recognizing
which exposures are relevant, credible, and
actionable for a specific organization.

THE CHALLENGE FOR DEFENDERS IS NOT
THE ABSENCE OF EARLY SIGNALS, BUT
THE DIFFICULTY OF RECOGNIZING WHICH
EXPOSURES ARE RELEVANT, CREDIBLE,
AND ACTIONABLE FOR A SPECIFIC
ORGANIZATION.”

When attacker preparation activity is addressed
during this early phase, the downstream
impact can be significant. Disrupting phishing
infrastructure, neutralizing impersonation
assets, or mitigating exposed entry points
before exploitation can prevent campaigns from
progressing to internal compromise.

From an exposure management standpoint,
the goal is not to predict every attack, but
to reduce the number of exposures that
attackers have available to them.
By addressing threats while
activity remains external, organizations can
alter attack paths before they generate alerts,
incidents, or business disruption.

Effective pre-breach disruption often results
in the absence of incidents rather than visible
response metrics. Attacks fail silently. Users
are never impacted. Incident response teams
are never engaged. Over time, this reduction in
incident volume is one of the clearest indications
that exposure is being managed effectively.

Case Patterns: Preempting the Same
Threats Incident Response Sees

During incident response investigations, certain
attack sequences recur frequently. When viewed
retrospectively, many of these incidents follow
a progression that was externally visible before
internal compromise occurred.

CHAPTER 08

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   91

EXTERNAL IMPERSONATION → INTERNAL CREDENTIAL THEFT

In numerous cases, attacker activity begins with external brand impersonation, such as
look-alike domains, spoofed communications, or fraudulent social profiles, all designed
to establish credibility. These assets are then used to harvest credentials, which later become
the primary mechanism for internal access. By the time credential abuse is detected internally,
the initial impersonation infrastructure has often already served its purpose.

PHISHING INFRASTRUCTURE → ESCALATION TO INCIDENT RESPONSE

Phishing campaigns that ultimately result in incident response engagement rarely appear without
warning. The infrastructure supporting these campaigns typically surfaces in advance. When this
infrastructure remains active long enough to reach users, the likelihood of escalation increases
significantly. Alternatively, when such infrastructure is disrupted early, many campaigns fail
to progress beyond initial delivery attempts, never reaching their potential.

EXPOSURE INTELLIGENCE → COMPENSATING CONTROLS BEFORE EXPLOITATION

Not all pre-breach activities are identity-driven. In many cases, attacker preparation aligns with
known weaknesses in exposed services or configurations. When intelligence indicates active
interest in specific attack paths, organizations can apply compensating controls such as temporary
mitigations or virtual protections to reduce exposure while permanent remediation is pending.
These remediations can break exploitation chains before attackers move from reconnaissance to
execution.  already served its purpose.

Proactive Defense Insights

•  Attacker preparation will continue to

accelerate, driven by automation and readily
available infrastructure.

•  The likelihood of breach will correlate less

with severity scores and more with exposure
duration and attacker readiness.

•  Organizations that align threat intelligence

with exposure reduction will reduce incident
frequency over time.

CHAPTER 08

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   92

Closing the Gap: Threat Intelligence as
the First Step of Exposure Management

Incident response provides invaluable insight into
how attacks succeed. Exposure management
applies those lessons earlier in the lifecycle,
utilizing threat intelligence to identify and
mitigate risk before incidents occur.

By connecting pre-incident intelligence with post-
incident learnings, organizations can close the
gap between what they respond to and what they
prevent. Threat intelligence is not an add-on or
a feed; it is the starting point for understanding
exposure, prioritizing action, and reducing the
volume of incidents that require a response.

Incident response shows us how attacks succeed. The
real opportunity exposure management provides is threat
intelligence - using those lessons earlier, when attacker activity
is still external and exposure management can stop incidents
before response is ever required.

MICHAEL GREENBERG

Head of Product Marketing
Exposure Management

CHAPTER 08

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   93

ABOUT CHECK POINT SOFTWARE TECHNOLOGIES LTD.

Check Point Software Technologies Ltd. (www.checkpoint.com) is a leading AI-powered,
cloud-delivered cyber security platform provider protecting over 100,000 organizations
worldwide. Check Point leverages the power of AI everywhere to enhance cyber security
efficiency and accuracy through its Infinity Platform, with industry-leading catch
rates enabling proactive threat anticipation and smarter, faster response times. The
comprehensive platform includes cloud-delivered technologies consisting of Check
Point Harmony to secure the workspace, Check Point CloudGuard to secure the cloud,
Check Point Quantum to secure the network, and Check Point Infinity Core Services for
collaborative security operations and services.

CONTACT US

WORLDWIDE HEADQUARTERS

5 Shlomo Kaplan Street, Tel Aviv 6789159, Israel

Tel: 972-3-753-4599

Email: info@checkpoint.com

U.S. HEADQUARTERS

100 Oracle Parkway, Suite 800, Redwood City, CA 94065

Tel: 800-429-4391

UNDER ATTACK?

Contact our Incident Response Team:

emergency-response@checkpoint.com

CHECK POINT RESEARCH

To get our latest research and other exclusive content,

Visit us at www.research.checkpoint.com

www.checkpoint.com

 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026   94

© 2026 Check Point Software Technologies Ltd. All rights reserved.