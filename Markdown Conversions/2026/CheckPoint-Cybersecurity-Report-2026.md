# Cybersecurity Report 2026

## Table of Contents
- [Introduction](#introduction)
- [Cyber Security Trends](#cyber-security-trends)
  - [Beyond Email: Multi-Channel Social Engineering](#beyond-email-multi-channel-social-engineering)
  - [ClickFix: Social Engineering That Shifts Execution to the User](#clickfix-social-engineering-that-shifts-execution-to-the-user)
  - [Voice-Based Social Engineering – The Weapon of Choice for Major Attacks](#voice-based-social-engineering--the-weapon-of-choice-for-major-attacks)
  - [Victim-Initiated Social Engineering](#victim-initiated-social-engineering)
  - [Social Engineering Activity on Business Communication Platforms](#social-engineering-activity-on-business-communication-platforms)
- [The 2025 Ransomware Ecosystem](#the-2025-ransomware-ecosystem)
  - [Mid-Year RaaS Disruption and Affiliate Realignment](#mid-year-raas-disruption-and-affiliate-realignment)
  - [Proliferation of Independent Double-Extortion Groups](#proliferation-of-independent-double-extortion-groups)
  - [Large RaaS Operators Continue to Drive Volume](#large-raas-operators-continue-to-drive-volume)
  - [Qilin – The Emerging Dominant RaaS Group](#qilin--the-emerging-dominant-raas-group)
  - [Cl0p – A Zero-Day Outlier](#cl0p--a-zero-day-outlier)
  - [The Return of LockBit](#the-return-of-lockbit)
  - [Constraining Incentives: Payment Restrictions and Compulsory Reporting](#constraining-incentives-payment-restrictions-and-compulsory-reporting)
  - [The Check Point Incident Response Team: Inside a Qilin Ransomware Attack](#the-check-point-incident-response-team-inside-a-qilin-ransomware-attack)
- [From Recon to Narrative Control: Cyber’s Operational Impact in 2025 Conflicts](#from-recon-to-narrative-control-cybers-operational-impact-in-2025-conflicts)
  - [Positioning and Conditioning Activity](#positioning-and-conditioning-activity)
  - [Operational Support Activity](#operational-support-activity)

---

# 01 INTRODUCTION

In 2025, the threat landscape evolved rapidly, becoming more interconnected and challenging to manage. Our analysis of global telemetry and incidents reveals a fundamental shift, marked by the emergence of new attack surfaces and techniques. Attackers are integrating AI, identity abuse, exposure exploitation, and ransomware into their campaigns.

The most significant change is the accelerated pace and scale at which attack opportunities are being executed. Data indicates that attackers are linking access, execution, and impact across various domains, from AI-driven social engineering and automation to the transformation of ransomware into a data-driven extortion economy. Edge devices and exposed infrastructure are increasingly used as launch points. These patterns were consistently observed across regions and industries in 2025, highlighting the swift combination of techniques to create tangible impacts.

AI exemplifies this transformation. This report views AI as a force multiplier that enhances targeting, scale, and adaptation in attacker activities, while also influencing risk prioritization and operational responses.

Our report is structured around attacker behavior and real-world data. The subsequent chapters delve into where attackers are focusing their efforts, how different techniques reinforce each other, and which exposure patterns most frequently lead to impact. This provides the necessary context to understand the trajectory of the threat landscape and what will be most critical in 2026.

I invite you to explore the data and findings presented in this report.

**Lotem Finkelstein**, VP Research

---

# 02 CYBER SECURITY TRENDS

## Beyond Email: Multi-Channel Social Engineering

Which attack surface is the easiest to exploit across all organizations? For attackers in 2025, the answer was the human component. In social engineering attacks, threat actors attempt to do just that: achieve compromise by manipulating human victims into providing the initial access for them. In such attacks, threat actors target employees, outsourced personnel, and third-party service providers to gain access to the organization’s systems or sensitive information. Although these attacks are perceived to be less serious than those exploiting software or hardware vulnerabilities, they can be just as damaging as compromises achieved through other means.

For years, phishing emails served as the primary social engineering vector, and organizations became increasingly aware of these threats. However, by 2025, social engineering expanded beyond traditional email-based campaigns, adopting multi-platform, cross-channel, and highly targeted approaches that leverage phone calls, messaging applications, and real-time impersonation.

## ClickFix: Social Engineering That Shifts Execution to the User

ClickFix emerged as one of the most significant social engineering techniques in 2025. First observed in 2024, ClickFix is an initial access method in which attackers manipulate users into executing malicious actions by presenting them with fraudulent instructions.

![Flowchart of a ClickFix attack]

![Example of a ClickFix website with a fake CAPTCHA prompt]

This technique succeeds by exploiting user trust and the tendency to follow technical instructions. In 2025, ClickFix activity increased by approximately 500% compared to the previous year and was observed in nearly half of all documented malware campaigns.

## Voice-Based Social Engineering – The Weapon of Choice for Major Attacks

Voice phishing and impersonation gained significant traction in 2025, proving to be a highly effective means to exploit user trust. In these attacks, threat actors pose as trusted or authoritative figures and, following targeted reconnaissance, use rehearsed scripts to pressure victims to take actions such as resetting credentials, changing MFA codes, or granting network access.

Historically associated with low-complexity consumer fraud, phone-based impersonation has evolved into an enterprise-focused intrusion technique used to gain an initial foothold in large organizations.

![Scattered Spider’s breach of Marks & Spencer]

## Victim-Initiated Social Engineering

In 2025, we observed a growing trend of victim-initiated (inbound) social engineering, where attackers deliberately steer targets into initiating contact, thereby increasing the perceived legitimacy of the interaction.

## Social Engineering Activity on Business Communication Platforms

Threat actors are increasingly expanding social engineering activity beyond email to messaging on social media platforms and messaging apps where user expectations and security controls are often weaker.

---

# THE 2025 RANSOMWARE ECOSYSTEM

The number of ransomware victims reached record highs in 2025 as the criminal ecosystem underwent rapid reconfigurations. The year began with a large-scale mass-exploitation by Cl0p, a cyber crime group, followed by the sudden disappearance of several major RaaS (Ransomware-as-a-Service) groups, which created opportunities for emerging actors.

![Published ransomware victims per month]

## Mid-Year RaaS Disruption and Affiliate Realignment

In Q2, several high-profile RaaS programs abruptly disappeared, while victim count remained well above 2024 baselines. 8Base and Phobos were disrupted by coordinated international law enforcement operations.

## Proliferation of Independent Double-Extortion Groups

2025 also saw an unprecedented proliferation of small, independent, double-extortion groups. At the end of 2024, approximately 90 identifiable brands were publishing victims on data-leak sites (DLS), while 2025 recorded 140 distinct groups, an increase of more than 50 percent.

## Large RaaS Operators Continue to Drive Volume

A review of the most active ransomware groups in 2025 shows that the ecosystem remains anchored by long running RaaS operations, despite the influx of new brands.

## Qilin – The Emerging Dominant RaaS Group

Qilin emerged as the dominant RaaS group of 2025, publishing the identities of over 1,000 victims on its DLS after they refused to pay a ransom.

![Qilin’s promotion of new extortion tools in a Dark Web forum]

## Cl0p – A Zero-Day Outlier

Cl0p shaped both the beginning and end of the 2025 ransomware timeline. Unlike traditional RaaS actors, Cl0p consistently relied on highly strategic zero-day exploits of widely used enterprise software.

## The Return of LockBit

In September 2025, LockBit officially relaunched as LockBit 5.0, with an updated encryptor, enhanced evasion capabilities, and a redesigned affiliate interface.

![A ransom note from a LockBit 5.0 attack in mid-September 2025]

## Constraining Incentives: Payment Restrictions and Compulsory Reporting

In 2025, the United Kingdom advanced comprehensive proposals, including a potential ban on ransom payments by public sector institutions and mandatory reporting.

## The Check Point Incident Response Team: Inside a Qilin Ransomware Attack

Qilin was the most prolific RaaS group of 2025. The following case study examines a significant attack against a Western European electric power company.

![Timeline of the Qilin attack]

---

# FROM RECON TO NARRATIVE CONTROL: CYBER’S OPERATIONAL IMPACT IN 2025 CONFLICTS

In 2025, cyber operations functioned as an integrated part of warfare along with air power, artillery, and special operations. The impact of cyber operations was realized through sustained interaction with military, political, and informational processes, instead of isolated technical effects.

![Components of major cyber functions in a military conflict]

## Positioning and Conditioning Activity

Positioning and Conditioning activities played an essential role in most of the 2025 conflicts, shaping the technical and informational environment without producing immediate, visible effects.

## Operational Support Activity

In 2025, operational support became more prominent as cyber operations were increasingly part of ongoing physical events instead of being conducted in isolation. These typically time-sensitive actions enabled, amplified, or synchronized activity in other domains and were closely aligned with unfolding military or political developments.

---

as real-
time enablers of military and political action.
Direct Effect Activity
Russia’s cyber operations showed a similar Direct effect activity includes cyber operations
close integration with kinetic activity. The intended to produce immediate and visible
Russian-linked APT44 group (also tracked as impact. These actions target systems, data,
Sandworm) frequently operated in parallel with or services directly, with results that can be
missile and drone barrages, launching cyber measured in technical, economic, or operational
attacks against logistics, agriculture, and energy impacts.
networks to disrupt Ukrainian infrastructure and
complicate service restoration. Analysis noted
that major missile strikes were often followed by
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 34

In 2025, direct cyber effects were used selectively. Direct effect activities were also used against
Destructive attacks, ransomware campaigns, and Iran, where disruptive cyber operations targeted
data leak operations garnered significant attention, institutions central to the country’s financial
but they frequently only played a supporting role well-being. A group operating under the name
in the broader conflict. Disruptive actions against Predatory Sparrow conducted a pair of high-
financial institutions, government services, and impact attacks, first against Bank Sepah,
civilian resilience sectors tend to be limited in resulting in widespread service outages and
duration yet still result in major damage, as they reported destruction of core banking data,
affect critical infrastructure, degrade function, and and later against Nobitex, Iran’s largest
force rapid recovery under pressure. cryptocurrency exchange, where digital assets
were rendered inaccessible and proprietary
source code was publicly leaked. While the
operation’s sponsorship and strategic direction
were not independently confirmed, the attacks
demonstrated that critical Iranian institutions
could be disrupted rapidly and at scale.
DISRUPTIVE ACTIONS AGAINST FINANCIAL
INSTITUTIONS, GOVERNMENT SERVICES, Iranian authorities responded by sharply
AND CIVILIAN RESILIENCE SECTORS TEND restricting nationwide internet access for
more than a day, a “defensive” measure aimed
TO BE LIMITED IN DURATION YET STILL
at reducing further intrusion attempts. The
RESULT IN MAJOR DAMAGE, AS THEY AFFECT
restrictions resulted in immediate hardship
CRITICAL INFRASTRUCTURE, DEGRADE
to the civilian population, disrupting access to
FUNCTION, AND FORCE RAPID RECOVERY banking, news, and basic communications during
UNDER PRESSURE. a period of heightened uncertainty.
Russia’s cyber activity in Ukraine showed a
deliberate pattern of destructive intrusions
timed to coincide with physical strikes. The
Russian-linked APT44 group deployed wiper
malware against government, energy, logistics,
In the Israeli–Iranian conflict, Iranian state-linked and agricultural sectors in an attempt to weaken
operators and affiliated hacktivist ecosystems Ukraine’s economic resilience. The group
increasingly focused their attention on civilian frequently operated in parallel with missile and
sectors such as healthcare, research institutions, drone barrages, which not only amplified the
and financial services. Iranian-linked actors disruption to the networks but also complicated
repeatedly attempted to compromise hospital Ukrainian attempts to restore services.
networks, exfiltrate sensitive medical data, and
interfere with clinical operations. These incidents
While many such operations are visible by design,
were not treated as isolated intrusions but as
their defining feature is that the functional
part of a broader pattern of coercive disruption
impact itself carries value, even in the absence of
aimed at undermining essential services and
public attribution or sustained attention.
public confidence.
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 35

Narrative Shaping Activity pressure. None of this was true. Israeli authorities
reported more than 1,200 coordinated social-
engineering operations targeting the public during
In 2025, Narrative Shaping activity was central to
this period.
cyber operations, and, in many cases, the results
were more enduring than technical disruptions.
During the Thai-Cambodian border tensions, cyber
The purpose of this activity is to shape perception,
operations similarly prioritized destabilization
signal capability or intent, and influence domestic
over tactical effects. The Thai government’s
or international audiences. Visibility, attribution, and
platforms and media infrastructure absorbed
interpretation are therefore central to their impact.
more than 223 million malicious requests within
a single 24-hour period, overwhelming public-
Influence operations, hack-and-leak campaigns,
facing services immediately following military
defacements, and public claims of responsibility
and political signaling. Cambodia responded
were prominent in multiple conflicts. Russia
with public accusations of Thai-linked intrusions
maintained its long-standing emphasis on influence
across multiple ministries, while the Cambodian-
operations, with coordinated narratives amplified
aligned hacktivist group KH Nightmare leaked
through cyber-enabled channels, proxy outlets, and
approximately 800GB of alleged government data,
automated content generation. Technical damage
amplifying uncertainty and eroding confidence in
was frequently employed as a signaling mechanism,
the government.
and the narrative impact was more important than
the scale of disruption.
Although these incidents involved large-scale
disruption and data exposure, their significance
One example of this is a ransomware attack against
depended on visibility, attribution, and interpretation
the Shamir Medical Center in Israel. The intrusion
rather than specific technical damage. Their
initially appeared as a conventional financially
primary effect was to strain administrative
motivated ransomware incident and leveraged
confidence and shape decision-making under
Qilin, a ransomware-as-a-service platform typically
stress, illustrating how technical disruption can
associated with profit-driven criminal activity.
function primarily as a signaling mechanism in
Subsequent investigation linked the operation
contemporary conflict.
to Iranian state-aligned actors. Following public
exposure, Qilin withdrew its ransom demands and
These activities all illustrate efforts to exert
removed the hospital from its list of victims.
psychological pressure. The purpose of the
operations was not to inflict physical harm, but to
As missile exchanges intensified in June 2025,
erode trust in official communication channels. In
Iranian information operations focused on
several cases, the most influential cyber operations
destabilizing the civilian population by eroding trust
were not those that disabled infrastructure, but
in Israel’s emergency-response systems. They
those that caused civilians to question alerts, doubt
released a wave of fake Home Front Command
warnings, and experience sustained uncertainty or
alerts, crafted to appear indistinguishable from
anxiety.
official rocket-warning notifications, during periods
of heightened threat perception. Fraudulent SMS
Similar dynamics were evident in Russian-affiliated
messages warning of fabricated terror attacks,
information operations during 2025. Those
resource shortages, and infrastructure failures
operations increasingly focused on dominating
circulated alongside AI-generated imagery and
the hours immediately following offensive missile
coordinated hashtag campaigns portraying Israeli
strikes or cyber incidents, deploying rapid, high-
society as collapsing under sustained military
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 36

volume messaging campaigns intended to outpace to erode democratic confidence and institutional
verification and correction. Analysts observed trust. These patterns illustrate a post-strike
coordinated surges of parallel narratives across psychological doctrine in which narrative floods and
hundreds of channels, shaping perception before AI-scaled influence operations are used to saturate
official information could be released. perception at moments when populations are most
vulnerable to fear, uncertainty, and misinformation.
A notable development was the expansion of AI-
driven content saturation. The pro-Kremlin Pravda The conflicts of 2025 illustrate that cyber activity has
network evolved into one of the world’s largest matured into a persistent and integrated component
disinformation engines, publishing up to 23,000 of modern warfare rather than a discrete or
articles per day across hundreds of sites, including exceptional instrument. It proved invaluable in
extensive English-language items that increased multiple conflicts, shaping environments before
visibility in search engine results. Experts warned escalation, enabling operations as events unfolded,
that the sheer volume enabled forms of so-called imposing friction through targeted disruption, and
"LLM grooming," in which large language models exerting sustained psychological pressure long
are continuously exposed to skewed narrative after the kinetic effects were felt. The practical
inputs. value of cyber operations in 2025 lies in the ability to
compound other attack venues, exploit uncertainty,
Russian cyber campaigns impersonated European and operate continuously below traditional
media outlets, manipulated public debate around thresholds of escalation. Understanding cyber
military aid to Ukraine, and targeted elections in activity through its functional roles demonstrates
Germany, Romania, and Moldova, with the intent why its cumulative impact is increasingly shaping
our conduct and perception of war.
The conflicts of 2025 show that cyber operations are no longer
episodic or auxiliary. Their power lies in persistence, shaping
conditions before escalation, enabling action during conflict, and
influencing perception long after the physical effects have passed.
YOAV ARAD PINKAS
Threat Intelligence Analyst
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 37

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

The attackers’ approach leverages mature they also leverage compromised devices and
access platforms, such as ShadowPad and trusted connections to pivot into other networks.
PlugX, and higher-end capabilities, including Notably, this campaign underscores that global
BRICKSTORM, malware designed for stealth access does not always require powerful new
and long-term persistence across edge devices tools. Durable positioning within widely deployed
and virtualization infrastructure. Services that infrastructure and the trust relationships
are exposed to the internet and systems that surrounding it can be enough to create
mediate identity, traffic, and trust are consistently international reach.
leveraged across targets. Chinese-nexus
espionage activity is not a collection of isolated The advisory was co-signed by 23 authoring and
intrusions, but a coordinated, scalable strategy partner agencies from the United States and
that enables multiple actors to operate in parallel international partners across Europe, Oceania, and
across different regions and sectors. Asia. This broad coordination reflects the global
scope of the issue and the need for joint defensive
action around widely deployed infrastructure.
Unmonitored Devices Exploitation
CHINESE-NEXUS ESPIONAGE ACTIVITY
Salt Typhoon represents only one element of a
IS NOT A COLLECTION OF ISOLATED far wider set of perimeter-focused operations.
INTRUSIONS, BUT A COORDINATED, As discussed in the “Unmonitored Devices: The
Attackers’ Launch Base” chapter, throughout 2025,
SCALABLE STRATEGY THAT ENABLES
the exploitation of edge infrastructure remained
MULTIPLE ACTORS TO OPERATE IN PARALLEL
central to enabling lateral movement and long-term
ACROSS DIFFERENT REGIONS AND SECTORS.
access, particularly when patch cycles, visibility, and
detection controls lag behind endpoint threats.
Threat actor UNC5221 has historically focused
on edge devices and continued this activity
throughout 2025, particularly targeting Ivanti
Secure VPN solutions. The actor exploited
CISA’s advisory. “Countering Chinese zero-day and recently disclosed vulnerabilities
State-Sponsored Actors Compromise of to deploy custom malware implants in multiple
Networks Worldwide to Feed a Global incidents. These operations exploited Ivanti
Espionage System,”details Salt Typhoon’s Secure VPN zero-day vulnerabilities, including
activity targeting networks across the globe, CVE-2025-0282 and CVE-2025-22457, to deploy
including telecommunications, government, custom platform-specific SPAWN malware.
transportation, and military infrastructure. While Together, these implants provide capabilities
threat actors focus on large backbone routers ranging from persistent access and traffic
of major telecommunications providers, as well tunneling to log tempering, enabling stealthy,
as provider edge and customer edge routers, privileged access on the compromised appliance.
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 39

BRICKSTORM, also attributed to UNC5221, Industrialized Tradecraft and a Shared
achieved greater prominence following the F5
Malware Ecosystem
Networks compromise disclosure, revealing a
disproportionate risk to software vendors. By
transforming edge infrastructure into covert Chinese-nexus cyber operations employ a
environments for intellectual property theft and deliberate, well-resourced campaign strategy,
downstream compromise, threat actors can using shared tooling, repeatable operational
convert vendor-side access into exploitation playbooks, and consistent execution across
blueprints that can be leveraged against their targets and regions.
customers at scale.
In multiple Chinese-nexus operations worldwide,
Other threat actors with advanced technical activity frequently follows a recognizable
skills were also observed targeting perimeter modus operandi. Throughout 2025, Check Point
infrastructure. UAT4356, which was responsible Research observed multiple campaigns on
for the ArcaneDoor campaign, targeted Cisco nearly all continents in which initial access and
ASA 5500-X firewalls to deploy the Ray Initiator execution commonly leveraged DLL side-loading,
bootkit, and UNC3886 deployed custom a technique allowing malicious code to run under
implants on Juniper routers. Collectively, these the cover of legitimate, trusted software. This
campaigns illustrate a broader strategy among is commonly paired with staged loaders and
Chinese-nexus espionage actors: a sustained modular backdoor ecosystems, where malware
investment in zero-day edge exploitation and families such as PlugX and ShadowPad are
the development of platform-specific tooling widely seen in different clusters and intrusion
to gain access to vulnerable and unmonitored sets, evidence of a shared tooling ecosystem.
organizational systems. These backdoors serve as operational hinges
for command execution, credential access, and
reconnaissance.
Post-compromise, operators frequently
expand their control using “living-off-the-
land” techniques and administrative protocols
that blend into the system’s own routine IT
THESE CAMPAIGNS ILLUSTRATE A activity, such as Remote Desktop Protocol for
BROADER STRATEGY AMONG CHINESE- lateral movement and hands-on operations. To
maintain persistence and operational flexibility,
NEXUS ESPIONAGE ACTORS: A SUSTAINED
threat actors may also deploy VPN software
INVESTMENT IN ZERO-DAY EDGE
under modified names, a recurring technique in
EXPLOITATION AND THE DEVELOPMENT
Chinese-nexus playbooks that embeds remote
OF PLATFORM-SPECIFIC TOOLING TO control in seemingly normal connectivity. What
GAIN ACCESS TO VULNERABLE AND appears to be an ordinary sequence of technical
actions is, in fact, an exercise in trust building
UNMONITORED ORGANIZATIONAL SYSTEMS.
designed to avoid suspicion.
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 40

The post-compromise deployment of ShadowPad
is a recurring feature in our investigations of
campaigns across Europe, Africa, Central Asia, and
the APAC. Its modular architecture supports data
exfiltration, remote command execution, lateral THROUGHOUT 2025, EXPLOITING MICROSOFT
movement, and credential harvesting, which allows
INTERNET-FACING SERVERS WAS A
flexible deployment as mission requirements
PROMINENT INTRUSION VECTOR, AND
change. ShadowPad’s repeated appearance in
HELPED THREAT ACTORS TO WEAPONIZE
otherwise unrelated events demonstrates that
NEWLY DISCLOSED VULNERABILITIES RAPIDLY.
stable, adaptable tooling is effective across diverse
environments, reflecting a calculated approach to
scalable, globally distributed data collection.
In recent InkDragon campaigns targeting Europe,
Southeast Asia, Africa, and South America,
ShadowPad was the core mechanism for
designed to extract cryptographic IIS/ASP.NET
persistence and execution. By deploying a custom
machine keys from compromised environments.
ShadowPad IIS Listener module, the actor also
In recent InkDragon intrusions, initial access was
reused the compromised infrastructure as a hub
gained using ToolShell. For New post-exploitation
for further operations. This technique reflects a
phase, to facilitate lateral movement and data
broader trend of turning footholds into platforms,
exfiltration, the actor deployed ShadowPad or
and platforms into supply chains.
FinalDraft malware.
The APT group, Rude Panda, abuses
Exploitation of Trusted Enterprise
misconfigurations rather than vulnerabilities. Its
Infrastructure
campaigns conducted throughout late 2024 and
into 2025 focused on compromising Microsoft
Throughout 2025, exploiting Microsoft internet- IIS servers using publicly available, static ASP.
facing servers was a prominent intrusion vector, and NET machine keys. Following initial access, the
helped threat actors to weaponize newly disclosed attackers deployed a custom malicious IIS module
vulnerabilities rapidly. This strategy enables named “HijackServer.” This activity resulted in the
scalable access before vulnerabilities are patched, compromise of hundreds of servers globally, which
highlighting the use of ubiquitous enterprise were subsequently leveraged to support fraudulent
platforms as long-term access vectors rather than operations, including search engine optimization
one-off intrusion opportunities. (SEO) manipulation and cryptocurrency schemes.
ToolShell is a particularly concerning exploit
chain that enables unauthenticated remote code
execution against on-premise internet-facing
Microsoft SharePoint servers. Although publicly
disclosed on July 19, the exploitation was first
observed earlier in the month as a zero-day exploit
against a small number of global government
organizations. The intrusions were typically followed
by targeted data theft using custom web shells
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 41

One of the clearest examples of the rapid the attackers gained high-privilege execution
weaponization cycle is CVE-2025-59287, a remote inside the Windows update infrastructure, on
code execution vulnerability in Windows Server which most networks depend.
Update Services (WSUS). The vulnerability was
weaponized within days publishing a proof-of- These cases demonstrate that the central role
concept (PoC). Similar to previous campaigns, the of IIS and WSUS amplifies risk by design. When
post-compromise payload was ShadowPad and components responsible for distributing trust are
deployed via DLL side-loading. By abusing WSUS, subverted, the impact is broad and difficult to contain.
JANUARY 8 Ivanti discloses RCE in Ivanti Secure Connect VPN, exploited by
UNC5221 (CVE-2025-0282)
MARCH 12 Disclosure of UNC3886 exploiting CVE-2025-21590 in Juniper
routers
APRIL 3 Ivanti disclosed critical RCE in Connect Secure VPN, exploited by
UNC5221 (CVE-2025-22457)
JULY 7 0-day ToolShell exploit chain hits internet-facing on-prem
SharePoint servers
SEPTEMBER 25 UAT4356 campaign disclosed exploiting CVE-2025-20333 and
CVE-2025-20362 against Cisco ASA-5500-X firewalls
OCTOBER 15 F5 Networks discloses a long-term compromise of its BIG-IP
development environment using BRICKSTORM malware
NOVEMBER 19 ShadowPad campaigns exploiting Microsoft WSUS servers with
CVE-2025-59287
DECEMBER 17 UAT-9686 campaign disclosure against Cisco appliances (CVE-
2025-20393)
Figure 1: Significant Chinese Affiliated Threat Activity in 2025
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 42

What Will Change in 2026: Deny traffic. A recurring theme is the abuse of trusted
enterprise services, such as IIS and WSUS, to
Persistence, Not Just Intrusion
support stealthy persistence and operational
scalability.
In 2025, our investigations showed a sustained
increase in activity attributed to Chinese-nexus
These campaigns follow a deliberate strategy
threat actors, with a global footprint across
of reusing proven tactics across regions and
critical sectors. These campaigns are linked
industries, turning ubiquitous enterprise
not only by shared tooling but also by consistent
platforms into durable access points. In 2026,
operational models, including edge-focused
the challenge extends beyond preventing
intrusion paths, exploitation of zero-day and one-
initial compromises to stopping attackers from
day vulnerabilities, and an emphasis on stealth
leveraging access to compromise downstream
and long-term persistence.
enterprises and maintain persistence within
trusted services.
The operations rely on a common set of malware
families and techniques that enable data
exfiltration, credential harvesting, and lateral
movement, supported by C2 channels designed
to be indistinguishable from modern enterprise
This chapter makes clear that geopolitical cyber activity is no
longer episodic or symbolic. It is persistent, coordinated, and
directly tied to national objectives, requiring security leaders to
treat nation-state threats as a standing operational risk rather
than a special case.
ELI SMADJA
Security Research
Group Manager
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 43

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

Unmonitored devices are particularly attractive Zero-Day Exploitation and a Growing
targets due to their low visibility, privileged
Custom Malware Ecosystem
proximity to traffic and identity, and positioning
within operational environments that are difficult
to patch without downtime. Unmonitored devices, Among the many campaigns targeting unmonitored
such as routers, firewalls, VPN appliances, and devices, intrusions attributed to the Chinese-affiliated
virtualization solutions, often operate in less espionage actor UNC5221 stand out for their scale,
monitored zones without Endpoint Detection and efficiency, and longevity, showing how low-visibility
Response (EDR) capabilities, resulting in sparse infrastructure can serve as a quiet launch base
logs and short retention windows. for sustained operations. Since at least 2022,
UNC5221 has been repeatedly exploiting zero-day
vulnerabilities in Ivanti Connect Secure appliances,
Now attackers are using unmonitored devices as
deploying BRICKSTORM malware.
launching pads, easily blending into legitimate
network traffic and can harvest credentials and
move laterally before defenders can respond. In BRICKSTORM is a custom implant designed to run
2025, Chinese-affiliated operators extended this inside multiple types of network appliances. In several
approach to vendors of these devices, targeting cases, it was initially deployed on an edge device and
them not only for access but for internal then used to pivot deeper into internal unmonitored
knowledge, source code, and undisclosed infrastructure, including VMware vCenter and ESXi.
vulnerabilities, ultimately preying on high-profile The malware is designed to blend in with typical
customers who trust those vendors to secure operations and evade standard incident-response
their environments. cycles, often persisting beyond remediation efforts.
By operating from unmonitored systems with access
to core network flows, BRICKSTORM enabled its
operators to capture credentials and expand access
UNMONITORED DEVICES into cloud environments. This progression illustrates
ARE NOW USED AS ATTACKER how a single compromise in an unmonitored device
LAUNCHING PADS can quickly escalate into broad identity and data
exposure.
BRICKSTORM activity also demonstrates an
2025’s defining pattern was persistence, with the alarming development: attackers now target
exposure of long-running campaigns targeting the vendors that build these devices. In October,
unmonitored devices. As defenses in standard, F5 Networks disclosed long-term unauthorized
well-monitored environments continue to access to its internal BIG-IP development
improve, more attackers are choosing to shift environment, linked to BRICKSTORM actors.
their operations into unmonitored environments, During the intrusion, attackers exfiltrated source
where visibility is weaker and response times are code, knowledge base content, and information
slower. While this effort has been spearheaded on undisclosed vulnerabilities. These assets
by Chinese-affiliated actors, it is also becoming could be leveraged to develop reliable exploit
increasingly common among other state-linked paths against a broad customer base. When a
operators, as well as cyber criminals. When development environment is compromised, the
attackers operate from unmonitored footholds, security posture of the entire product ecosystem
every signal becomes suspect, and every external is also impacted. Malware persistence on the
dependency becomes a potential threat.
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 45

vendor side can easily become customer-side integrity checks or triggering standard security
exposure, accelerate exploit development, and controls, making it particularly difficult to detect
enable broader compromise across sectors that unmonitored Juniper appliances.
depend on those products.
UNC3886 historically focuses on maintaining
Multiple other China-affiliated actors are long-term access to victim environments and
weaponizing unmonitored network appliances has previously been observed exploiting zero-
with custom, platform-device-specific implants. day vulnerabilities to deploy custom malware on
The U.K. National Cyber Security Centre (NCSC) Fortinet devices. In intrusions involving Juniper
issued a public advisory on a new implant routers, operators deployed multiple implants in
campaign targeting Cisco ASA-5500-X firewalls, parallel, with core capabilities such as remote file
which are end-of-life and no longer supported. upload and download, interactive shell access,
The activity, tracked as UAT4356 and attributed and connection relay. The implants operate within
to a China nexus, involved active exploitation Junos’ underlying FreeBSD environment and are
of CVE-2025-20333 and CVE-2025-20362 on designed to masquerade as legitimate system
compromised devices to deploy a previously processes. In some cases, they even interact
undocumented toolkit. directly with legitimate Junos OS daemons,
including patching their memory at runtime to
suppress logging and telemetry.
These operations reflect a high degree of research
VENDOR-SIDE MALWARE PERSISTENCE
effort and sophistication, with an emphasis on
DRIVES CUSTOMER EXPOSURE AND
BROADER COMPROMISE. stealth and maintaining persistent, long-term, and
covert access, particularly to devices that are not
continuously monitored.
Misconfiguration, Not Zero-Day
Once these unmonitored appliances were
compromised, attackers gained high-value access
to network traffic, credentials, and administrative A different approach was observed in a long-running
functions. Designed to survive reboots and, in Russian state-sponsored campaign attributed to
some cases, even firmware upgrades, the malware the Sandworm group that targets Western critical
enabled attacker control, including bypassing AAA infrastructure. Unlike the Chinese actors, which
(Authentication, Authorization, and Accounting) relied on direct compromise of devices, this activity
checks, executing commands, conducting covert primarily abused misconfigured network devices,
packet capture, and exfiltrating sensitive data. gaining access through exposed management
interfaces rather than exploiting vulnerabilities in
Another China-nexus actor, tracked as UNC3886, the platforms themselves.
was observed exploiting CVE-2025-21590, a
vulnerability in Junos OS, Juniper Networks’ The attackers gained administrative access
operating system for routing, switching, and and then leveraged native traffic-capture and
security devices. UNC3886 abused this flaw to monitoring capabilities to intercept network
run malware from within legitimate Junos OS traffic passively. This enabled them to harvest
system processes, enabling stealthy persistence credentials, session cookies, and authentication
and post-exploitation activity without breaking file tokens, which were subsequently used to access
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 46

legitimate organizational services such as VPNs, stand alone, as financially motivated actors have
identity providers, and cloud management consoles. increasingly adopted techniques long associated
Establishing persistence and lateral movement with state-sponsored operators, including the
using valid credentials eliminates the need for systematic exploitation of patched-but-still-exposed
custom malware implants, while making the activity vulnerabilities, known as n-days, in network
harder to separate from everyday administrative appliances.
use, especially when device access and telemetry
are not consistently monitored. One of the most notable examples of financially
motivated attackers using unmonitored devices as
Regardless of whether a campaign relies on attack points, by weaponizing n-day vulnerabilities,
exploitation or misconfiguration, unmonitored involved Akira ransomware. In mid-2025, an
devices have become a critical and increasingly increase in Akira intrusions targeting SonicWall
attractive attack surface for sophisticated threat appliances was observed. Multiple incidents involved
actors, providing a low-friction path to stealthy unauthorized access through SonicWall SSL VPN
access, credential theft, and long-term operational services, followed by the deployment of ransomware,
persistence. often within hours of the initial compromise.
Victims spanned multiple sectors and organizations
regardless of size, indicating opportunistic mass
exploitation rather than targeted intrusion.
While a zero-day vulnerability in SonicWall SSL
VPN was initially suspected, this spike was largely
UNMONITORED DEVICES HAVE BECOME A
tied to ongoing abuse of CVE-2024-40766. This
CRITICAL AND INCREASINGLY ATTRACTIVE
year-old access control vulnerability allows local
ATTACK SURFACE FOR SOPHISTICATED user passwords carried over during migrations
THREAT ACTORS, PROVIDING A LOW- to remain valid. As a result, credentials harvested
when devices were vulnerable can later be reused
FRICTION PATH TO STEALTHY ACCESS,
by threat actors, even after the affected devices have
CREDENTIAL THEFT, AND LONG-TERM
been patched. This illustrates the long-tail risk of
OPERATIONAL PERSISTENCE.
credential exposure stemming from vulnerabilities in
unmonitored devices.
Qilin, the most prolific ransomware operation
observed in 2025, similarly relied on exploiting
unmonitored network appliances for initial access.
The group was observed exploiting CVE-2024-21762
Ransomware: and CVE-2024-55591, which affected FortiOS and
FortiProxy SSL VPN devices. The first vulnerability
N-Day Exploitation at the Edge
enables remote execution of arbitrary code or
commands, while the second allows attackers to
Targeting unmonitored devices is not new for cyber obtain super-administrator privileges. Together,
criminals. Ransomware operators have targeted these flaws provided rapid, privileged access to victim
VMware ESXi and vCenter environments for years environments through commonly deployed perimeter
because they sit at the center of server operations infrastructure.
yet offer minimal visibility. This targeting does not
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 47

This pattern was not limited to established Looking Ahead
ransomware brands. In early 2025, vulnerabilities in
Fortinet devices were exploited by a newly identified
Unmonitored devices continued to evolve this
actor tracked as Mora_001. The group exploited
year from operational network systems into
CVE-2024-55591 and CVE-2025-24472, both of which
platforms for malware activity. Limited visibility
allow unauthenticated attackers to gain super-admin
and inconsistent monitoring make them well-
privileges on vulnerable FortiOS devices. Following
suited for long-term access, and their role in
initial access, the actors mapped internal networks,
handling high-value traffic and authentication flows
moved laterally using newly created VPN accounts,
enables attackers to expand access well beyond
and ultimately deployed a ransomware strain called
the initial point of compromise. At the same time,
SuperBlack, built using a leaked LockBit builder.
the targeting and compromises within vendor
environments increase the risk that intrusions
Together, these incidents highlight how ransomware
translate into downstream exposure for customers.
operators favor n-day exploitation of unmonitored
devices to achieve fast, privileged access. This has
To mitigate the effects of long-running intrusions
become a key complement to their long-standing
involving unmonitored devices, end-of-life
focus on ESXi and vCenter: unmonitored devices
systems must be retired. For devices that are
provide the entry point, and virtualization platforms
still supported, vendors must provide stronger
offer the scale and leverage. By operating from
monitoring capabilities, richer forensic artifacts,
systems that sit outside standard endpoint visibility,
and more resilient security controls by default.
attackers shorten the time from entry to impact,
Without these changes, compromises in low-
bypass common controls, and convert external
visibility infrastructure will remain challenging to
exposure directly into rapid financial harm.
detect and even harder to contain.
One of the most dangerous attack surfaces is infrastructure we
assume is trusted. Edge devices operating with limited visibility
allow attackers to establish persistent footholds rather than
one-time entry points.
ALEXANDRA GOFMAN
Technology Leader
Threat Intelligence
CHAPTER 02 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 48

03
AI LANDSCAPE
IN CYBER SECURITY

AI LANDSCAPE: FROM AI across criminal and state-sponsored activity.
Finally, we determine what changed in 2025 and
INTEGRATION TO AUTONOMY
the implications for 2026.
In 2025, Artificial intelligence (AI) was so deeply Our focus is on real-world, in-the-wild
embedded in cyber activity that distinguishing evidence collected throughout 2025, including
“AI-related attacks” from general digital attacker operations, underground services
operations became increasingly challenging. and discussions, published incidents, and law
In contrast to 2023–2024, when attackers’ enforcement findings.
use of AI was easily recognizable, in 2025 AI
use became so commonplace that it faded AI SERVICES AS AN ATTACK
into the background of attack operations.
SURFACE
AI now underpins software development,
social engineering malware design, data
mining, influence operations, reconnaissance,
As AI tools and services become fully integrated
vulnerability discovery, and even post-exploitation
into every aspect of daily corporate life, their
activity.
access to data, context, and downstream systems
is increasing astoundingly fast. AI assistants
AI is now used everywhere yet remains rarely and agents are involved in processing emails,
visible. Most malicious outputs seldom reveal if documents, calendars, web content, and internal
AI contributed to their creation or execution. Our knowledge databases. As a result, AI is becoming
April 2025 State of AI in Cyber Security report an increasingly attractive attack surface.
warned that as AI models become integrated into
daily work, the boundary between “AI-enabled”
Direct and Indirect Prompt Injection
and conventional threats would blur. By the end
of 2025, that prediction will have come to pass.
Attacks
Throughout 2025, threat actors not only refined
A clear manifestation of this trend is the rise
and expanded their use of AI but also increasingly
of direct and indirect prompt injection attacks.
attempted to target the AI ecosystem itself. As
Attackers continued to turn prompt injection into
enterprises adopt agentic frameworks, MCP
a pervasive threat affecting both direct model
servers, and locally deployed models, these
interactions and autonomous agent workflows.
environments have become the new attack
Data from Lakera, a Check Point Company,
surfaces.
shows that direct LLM manipulation is achieved
through role-play setups, hypothetical scenarios,
The following chapter examines AI’s dual role
and obfuscation tricks. In such attacks, client-
in today’s threat landscape. First, we outline
facing LLM-based services are targeted to
the growing class of attacks on AI services and
expose restricted information. In indirect
agentic systems, where misconfigurations,
prompt injection attacks, malicious instructions
prompt manipulation, and vulnerabilities in
are embedded within otherwise legitimate
AI-connected tools create opportunities for
content that AI systems access during everyday
exploitation. Second, we assess attacks enabled
workflows.
by AI, including identity theft and impersonation,
AI-assisted malware development, automated
reconnaissance, and the broader optimization of
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 50

One reported research example involved to influence command execution, effectively
malicious Google Calendar invitations that enabling arbitrary commands to run in the host
contained hidden instructions inside event environment. The case illustrates how, once
descriptions. When processed by Google’s agentic AI tools are granted execution privileges,
Gemini assistant, the injected content influenced they can turn input manipulation into direct
downstream behavior, enabling unauthorized system compromise, even outside formal agent
actions such as sending messages, accessing frameworks.
application context, and interacting with
connected smart home devices. The attack was
possible due to the AI assistant’s trusted access
to calendar data and integrated services.
During the year, Google also issued a global
advisory after observing invisible HTML-
THE FLAW ALLOWED UNTRUSTED INPUT
based injections that could manipulate
TO INFLUENCE COMMAND EXECUTION,
AI summarization features within Gmail,
EFFECTIVELY ENABLING ARBITRARY
demonstrating how subtle these attacks are
COMMANDS TO RUN IN THE HOST
and how difficult they are to detect. Meanwhile,
Check Point Research documented real ENVIRONMENT.
malware samples embedding natural-language
instructions designed to mislead AI-powered
detection tools, signaling that attackers are
attempting to bypass LLM defenses.
Similar risks were observed in enterprise
environments. Research demonstrated how AI
systems integrated into corporate workflows Lakera, a Check Point Company, provided
could be manipulated through documents, additional validation for the risk of in-direct
tickets, or shared content containing concealed injection. In its Q4 2025 review of real-world
instructions. When AI assistants summarized or agent-related attacks, it observed that indirect
processed this material, the embedded payloads prompt injection attempts often proved more
altered the model's behavior, leading to the effective than direct. The report documented
unintended disclosure of sensitive information or multiple cases in which hidden instructions
unsafe tool execution. These findings underscore embedded in emails, documents, or web
that indirect injection turns everyday business pages influenced agent behavior, resulting in
artifacts into potential execution vectors unintended tool invocation, leaking sensitive
once they are implicitly trusted by AI-driven data, or suppressing safety constraints. Notably,
automation. The report found that these attacks frequently
required fewer attempts than direct prompt
injection as they exploited the agent’s normal
In 2025, Check Point Research disclosed a
operating assumptions instead of trying to
command injection vulnerability in OpenAI’s
override safeguards.
Codex CLI, an AI-powered coding assistant
designed to execute commands on a developer’s
local machine. The flaw allowed untrusted input
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 51

Model Context Protocol (MCP) Under which stemmed from the IDE’s implicit trust
in modified MCP configuration files. Other
Attack
researchers reached similar conclusions in
a separate investigation, finding that a large
Model Context Protocol (MCP), the mechanism majority of publicly exposed MCP servers leaked
that allows LLMs to invoke external tools, is sensitive information such as API keys, making
currently one of the most lucrative parts for them easy to compromise.
attackers in the AI attack surface. Throughout
2025, Check Point Research and other
A recent review by Lakera found security
researchers exposed structural weaknesses
vulnerabilities in 40% of the approximately 10,000
across the MCP ecosystem, which include
MCP servers that were probed. Seven percent
servers, tool configuration files, IDE integrations
were vulnerable to “Path Traversal” attacks, and
such as Cursor and VS Code plugins, and the
Lakera found at least one secret API key in 8%
broader community of third-party nodes. Check
of the servers. Two percent were vulnerable to
Point Research published an RCE vulnerability in
SQL injection attacks, and 6% were vulnerable to
Cursor’s implementation, known as MCPoison,
Command or Code injection attacks.
Impacted MCP Servers by Top Vulnerability Types
Available API keys 8%
Path Traversal 7%
Command/Code Injection 6%
SQL Injection 2%
Figure 1 - Detected vulnerabilities in publicly exposed MCP servers
In October, researchers identified a malicious All these developments reflect a deeper
npm package impersonating a legitimate MCP structural weakness: current LLM architecture
integration for the Postmark email service. struggles to reliably distinguish between
It silently added an attacker-controlled BCC developer-defined instructions and user-provided
address to outgoing messages, enabling covert input. As long as this issue remains, attackers
exfiltration of sensitive mail. Underground forums will continue to find ways to manipulate AI
also began discussing how MCP servers could systems into acting contrary to their intended
act as stealth backdoors, blend attacker traffic purpose. This challenge will persist into 2026 and
with the benign workflow of AI tool invocations, will shape the next phase of AI security.
and disguise command-and-control (C2) activity.
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 52

LLMS AS A VECTOR FOR Taken together, these dynamics underscore that
AI services are not merely tools leveraged by
SENSITIVE DATA LEAKAGE
attackers but have themselves become attack
surfaces. As enterprises continue to integrate
AI into core business processes, managing how
The use of AI services by corporate employees
data is shared, processed, and retained by AI
opens another front in the battle. As generative
systems will remain a critical security challenge
AI becomes embedded in daily workflows, the
in 2026.
boundary between internal corporate data and
external AI platforms increasingly blurs, creating
new pathways for the inadvertent exposure of AI SERVICES USED BY THREAT
proprietary assets. This risk is amplified by the
ACTORS
sheer volume and diversity of AI services in use.
Check Point’s GenAI Protect data indicates that
organizations interact with more than fourteen Attackers can obtain AI capabilities in three ways:
different AI services per organization on average, abusing commercial models, deploying self-
complicating visibility and control over the data hosted open-source models, and utilizing third-
flows. party “DarkGPT”-style malicious services. Each
method significantly evolved over 2025.
According to Check Point’s GenAI Protect’s Q4
2025 data, approximately 89% of organizations
Abusing Commercial AI Services:
were impacted by risky prompts within an average
month, with 1 in 41 submitted prompts classified Jailbreaking at Scale
as high risk, an increase of 97% compared to
Q1 2025. The most common exposures included
Attackers continue to exploit commercial models,
personally identifiable information (PII), internal
usually through carefully engineered jailbreaks
network and IT artifacts, and source code. At
that bypass safety filters and by dividing
the same time, incidents such as OpenAI’s
malicious requests into multiple seemingly
recent data breach demonstrate that AI service
benign subtasks. This quickly becomes an arms
providers themselves are not immune to leakage.
race between the model providers’ safeguards
Organizations are realizing that they can’t protect
and the malicious prompts generated in
sensitive data from exposure once it’s shared with
underground communities. Threat actors share
external models.
jailbreaking techniques for both commercial
89% 1 41 97%
IN
OF ORGANIZATIONS SUBMITTED PROMPTS INCREASE IN RATE OF
IMPACTED BY RISKY WAS CLASSIFIED AS HIGH-RISK PROMPTS
PROMPTS EACH MONTH HIGH RISK DURING 2025
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 53

DarkGPT, WormGPT, HackerGPT: The
Rise and Fall of Malicious LLM Services
THIS QUICKLY BECOMES AN ARMS RACE At the start of 2025, the underground ecosystem
was saturated with “DarkGPT”-branded services
BETWEEN THE MODEL PROVIDERS’
offering “uncensored ChatGPT” access. By mid-
SAFEGUARDS AND THE MALICIOUS
year, prevailing opinions on criminal forums
PROMPTS GENERATED IN UNDERGROUND
shifted to the belief that these services were
COMMUNITIES mostly scams, lacking real capabilities or simply
proxying commercial models. This led to a swift
downturn in demand as attackers realized they
could jailbreak commercial models or deploy
open-source alternatives. By October, forum
users openly mocked DarkGPT-style sites, calling
them “worthless” or “90% scam.”
and open-source models in dedicated shared
repositories and forums. Repositories cataloging
Self-Hosted Open-Source Models: The
jailbreak prompts by model or version have
become standard tooling, and a new class of
Center of Gravity Shifts
“context poisoning” jailbreaks, most notably the
Echo Chamber technique, demonstrated how
As the underground community became
carefully crafted multi-step prompts can bypass
increasingly aware that “DarkGPT” services were
guardrails without appearing explicitly malicious.
often scams, unreliable, or low quality, serious
operators migrated toward locally deployed
OpenAI’s June 2025 threat intelligence report on
open-source models. Attackers started actively
Operation ScopeCreep reveals how a Russian-
discussing VPS-hosted LLM deployments,
speaking threat actor incrementally bypassed LLM
providing unrestricted control, privacy, and
safeguards by spreading malware development
performance stability.
tasks across multiple, seemingly unrelated
accounts. Each account submitted only a small,
Several developments accelerated this shift.
benign-looking request, but enabled the actor
High-performance open-source models became
to accumulate multi-stage Go-based malware,
widely available and quickly jailbroken, with
including C2 deployment, DLL side-loading,
criminal forums sharing tips for fine-tuning and
resulting in malware deployment in the wild.
dedicated offensive prompts.
Some of the most advanced operations of 2025
explicitly manipulated commercial LLMs through
role-play, convincing them that malicious actions
were part of penetration-testing or defensive
tasks. This technique later became a central
feature of the GTG-1002 espionage campaign.
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 54

Figure 2 - Discussing how to use Kimi K2 for malicious code generation
Local deployment enabled Copilot-style AI USE IN SOCIAL ENGINEERING
workflows, increasingly allowing attackers
AND IDENTITY THEFT
to embed jailbroken local models directly
into malware development and debugging
environments.
If 2024 was the year AI enabled supercharged
phishing, 2025 is the year of AI impersonation: in
In 2025, sophisticated actors moved away from text, audio, and video, in offline, real-time, and
outsourced “criminal AI services” and shifted autonomous modes. Our April report presented
toward privately controlled compute, eliminating these developments in detail, and the subsequent
the possibility of supervision, filtering, and logs. months delivered abundant real-world evidence
Evidence for this trend primarily consists of that all three modalities reached operational
self-reports from criminals and discussions in maturity.
criminal forums.
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 55

Textual Social Engineering: case was reported involving AI-generated celebrity
endorsements that defrauded more than 6,000
Scale, Cultural Precision, Autonomy
victims, primarily from the United Kingdom and
Canada.
AI-generated text now appears in phishing,
sextortion, Business Email Compromise (BEC)
Real-time deepfake technology has also advanced
scams, influence operations, and multilingual
rapidly. Tools such as DeepFaceLive now operate
fraud. There are multiple reports of increased
with high fidelity on consumer hardware, enabling
multilingual culturally adjusted phishing and
attackers to alter their appearance during live calls
comment flooding, which never repeat the
and meetings. Similar techniques were also used in
exact same text. Text generation reached fully
fraudulent job interviews, particularly in operations
autonomous levels, removing the critical bottleneck
linked to North Korean and other state-sponsored
of a lack of culturally proficient manpower.
actors aiming to access Western companies.
With the advent of seamless real-time voice
Audio Deepfakes:
cloning, attackers can now convincingly replicate
Real-Time Impersonation and
a person’s complete audiovisual identity in live
Fully Autonomous Calling interactions, a capability that was not realistically
accessible at scale until recently.
AI-generated voice technology, once resource-
intensive, is now much easier to use, requiring just
minutes of audio from social media. In 2025, voice
impersonation attacks included live impersonation
of a European defense minister to solicit “hostage-
release funds” from contacts with high net-worth
IDENTITY, ONCE GROUNDED IN APPEARANCE,
individuals, impersonation of US Secretary of State
VOICE, AND PERSONAL INTERACTION, HAS
Marco Rubio, and many reports of impersonating
BECOME ONE OF THE MOST FRAGILE AND
family members to commit financial fraud. Some
AI voice technology reached full autonomy, with AGGRESSIVELY TARGETED COMPONENTS OF
criminals advertising scripted call flows, adaptive THE DIGITAL ECOSYSTEM.
responses, voice cloning, and OTP collection
(known as “AI-driven outbound calling systems”) to
impersonate banks, cryptocurrency exchanges, or
authorities to harvest OTPs and credentials.
Video Impersonation: From Pre-Recorded
AI-generated identities and deepfake Know Your
Deepfakes to Live Face-Swapping
Customer (KYC) submissions rapidly became a
preferred method for obtaining initial access.
Two distinct forms of deepfake video Fraudsters now create synthetic identities, forged
manipulation matured significantly in 2025. Pre- documents, and fully fake identities to open
recorded deepfakes were used in a wide range of bank accounts, reactivate suspended ones, or
scams, from investment fraud to sextortion and bypass verification steps on financial and online
political influence efforts. In Georgia, a notable services. The market for these capabilities is well-
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 56

established: simple AI-generated face images can unreliable. Throughout 2025, attackers increasingly
be purchased at low cost, while more sophisticated, exploited generative models to imitate people’s
region-specific KYC packages command significantly appearances and voices with a level of realism that
higher prices. In 2025, law enforcement in Hong defeats traditional verification methods. Automated
Kong arrested eight suspects for allegedly using AI- systems replaced human scammers in many
generated deepfake images to bypass banks’ online operations, and fully autonomous, multilingual
identity verification and open fraudulent accounts. phone-fraud tools reached operational maturity. The
This incident demonstrated that such methods are result is a landscape in which identity, once grounded
actively used in real-world account fraud schemes. in appearance, voice, and personal interaction, has
become one of the most fragile and aggressively
These developments contribute to a broader shift targeted components of the digital ecosystem.
in which audio-visual identity itself is becoming
MEDIA
OFFLINE GENERATION REALTIME GENERATION FULLY AUTONOMOUS
TYPE
Real-time AI-generated,
Pre-rendered
TEXT generated fully interactive
scripts or emails
responses conversations
Fully AI-driven
Pre-recorded Real-time voice
AUDIO conversational
impersonations manipulation
audio
Completely
Pre-created Live face-swapping automated,
VIDEO
deepfake videos or video alteration AI-generated
interactive video
Figure 3: GenAI maturity level. (Red V marks technology already available in markets and exploited in the wild)
AI IN MALWARE DEVELOPMENT year, Check Point Research and other organizations
documented the shift from AI as an “assistant” to the
AND THE RISE OF AUTONOMOUS
first signs of AI as an operator within the kill chain.
OPERATIONS
By 2025, the use of AI in malware development
had evolved from isolated experiments to
While identity theft accounted for the highest
repeated, observable activity in the wild. OpenAI’s
volume of AI-enabled attacks, the most profound
June disclosures offered an early example with
transformation in 2025 occurred in malware
ScopeCreep, a multi-stage Go-based malware
development and orchestration. Throughout the
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 57

family produced through iterative jailbreaking. system-reconnaissance commands to be generated
Around the same time, the Xanthorox project dynamically and on demand, producing polymorphic
promoted an entire suite of malicious tools, behavior that blended into legitimate AI API traffic.
including a keylogger, ransomware, and an Although the campaign was likely just a proof-of-
exe-to-JavaScript crypter, claiming its internal concept, it demonstrated that LLMs can serve as
LLM pipeline generated them. Although the highly flexible C2 engines, capable of generating novel
resulting samples displayed modest technical commands, mutating behavior, and complicating
sophistication, what they really showed was the signature-based detection far more effectively than
appeal of AI-automated toolchains among less traditional static infrastructures. This experiment
experienced actors. FunkSec, a ransomware offered an early glimpse of what fully autonomous
group profiled in earlier this year, openly attack orchestration might look like. However,
acknowledged that portions of its coding and the most significant evidence of such capabilities
tooling were developed with the assistance of AI. emerged only months later.
The most consequential AI-enabled intrusion of 2025
came from Anthropic’s investigation into the China-
affiliated group, GTG-1002. This campaign represents
the first publicly documented case in which an AI
system conducted the majority of a cyber espionage
IN JULY, CHECK POINT RESEARCH operation with minimal human oversight. According
to Anthropic’s analysis, Claude Code handled
DOCUMENTED SKYNET MALWARE
roughly 80 to 90 percent of the tactical tasks across
EMBEDDING A NATURAL-LANGUAGE PROMPT
the intrusion lifecycle, including reconnaissance,
INJECTION TO DECEIVE AI-BASED SECURITY
vulnerability identification, exploit development,
MECHANISMS. credential harvesting, lateral movement, data
extraction, and intelligence triage. The operators
manipulated the model using detailed role-play
prompts, persuading it that each action formed part
of a legitimate defensive assessment. Once activated,
Claude maintained persistent context across
sessions, enabling complex multi-day operations
In July, Check Point Research documented without requiring human operators to restate
a Skynet malware sample that embedded objectives or reconstruct the state.
a natural-language prompt injection string
designed to deceive AI-based security GTG-1002 targeted approximately thirty organizations,
mechanisms. This was an early indication that including major technology companies and
malware authors were beginning to treat AI government agencies. Its framework relied heavily on
detection engines as targets. A further step MCP to integrate external tools, automate workflows,
in AI-enabled operations appeared when the and chain actions across multiple sub-agents.
Computer Emergency Response Team of Ukraine This architecture is significant because it shows
(CERT-UA) reported LAMEHUG, a malware an AI model acting not merely as a content or code
variant attributed to the Russian-affiliated APT28 generator, but as an autonomous operational engine
group. Rather than relying on a fixed C2 protocol, capable of conducting a coordinated intrusion at
operators funneled instructions through Qwen 2.5, an scale.
AI model hosted on Hugging Face’s API. This allowed
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 58

Taken together, these findings illustrate a profound the intrusion lifecycle, from reconnaissance
shift: the boundary between human-directed and to exploitation and data handling. At the same
AI-directed cyber operations is beginning to blur. time, real-time face-swapping, voice cloning,
AI is no longer limited to drafting phishing emails and automated scam platforms demonstrated
or generating code fragments; it is increasingly that identity verification through appearance and
taking on the role of an operator inside the intrusion speech can no longer be trusted. The supporting
lifecycle, thereby lowering the cost and expertise technologies around AI also proved vulnerable.
required for advanced cyber activity. Misconfigured MCPs, prompt-injection pathways,
malicious packages, and altered tool descriptors
OUTLOOK illustrated that the infrastructure surrounding LLMs
can itself become a vector for compromise. Cyber
attacks increasingly blend human decision-making
By late 2025, AI shifted from a support tool to an
with AI-driven execution. AI is no longer a separate
active participant in cyber operations. Campaigns
element within cyber security; it is now interwoven
such as GTG-1002 and the LAMEHUG experiment
throughout the entire landscape.
demonstrated that AI systems, in the hands
of capable and sophisticated actors, can now
autonomously perform a significant portion of
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
CHAPTER 03 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 59

04
GLOBAL ANALYSIS

GLOBAL THREAT INDEX MAP
This map displays the global cyber threat risk index, highlighting high-risk areas worldwide.
Higher risk Lower risk
Insufficient Data
Figure 1: Global Threat Index Map.
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 61

ATTACKS PER ORGANIZATION
Check Point’s global telemetry indicates a steady and continuing rise in weekly cyber attacks per
organization. Cyber attacks increased sharply in 2024 and continued to climb in 2025, reaching the
highest level recorded during this period. By 2025, organizations faced an average of 1,968 cyber attacks
per week. This marks an 18% year-over-year (YoY) increase and nearly a 70% increase since 2023, which
further highlights the ongoing escalation in overall threat activity.
2,500
1968
2,000 1673
300
1162
200
100
0
2023 2024 2025
Figure 2: Average Weekly Cyber Attacks per Organization, 2023-2025
ATTACK ACTIVITY BY REGION
The increase in the average number of cyber attacks per organization was not evenly distributed across
regions. In 2025, North America recorded a 23% year-over-year increase and Europe a 20% increase,
while Latin America (13%) and APAC (10%) showed more moderate growth. Africa remained the most
heavily affected region in terms of volume, averaging over 3,000 attacks per organization per week. Still, it
showed the most minor year-over-year change in 2025, with a 5% increase.
Africa 3092 [+5%]
APAC 2909 [+10%]
Latin America 2795 [+13%]
Europe 1642 [+20%]
North America 1422 [+23]
Figure 3: Average Weekly Cyber Attacks per Organization by Region, 2025 [% of Change from 2024]
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 62

WEEKLY ATTACKS BY INDUSTRY AND REGION
GLOBAL
Education 4352 [+22%]
Government 2683 [+17%]
Telecommunications 2656 [+27%]
Healthcare & Medical 2365 [+7%]
Energy & Utilities 2168 [+37%]
Associations & Non Profits 2143 [+41%]
Automotive 1986 [+28%]
Aerospace & Defense 1909 [+21%]
Hospitality, Travel & Recreation 1905 [+50%]
Hardware & Semiconductors 1893 [+34%]
Software 1834 [+35%]
Media & Entertainment 1779 [+15%]
Business Services 1741 [+21%]
Consumer Goods & Services 1738 [+12%]
Financial Services 1735 [+15%]
Construction & Engineering 1600 [+1%]
Industrial Manufacturing 1567 [+19%]
Agriculture 1522 [+78%]
Biotech & Pharmaceuticals 1512 [+2%]
Wholesale & Distribution 1376 [-3%]
Real Estate, Rentals & Leasing 1330 [-6%]
Transportation & Logistics 1187 [+0.6%]
Information Technology 1148 [+36%]
Figure 4: Global Average Weekly Cyber Attacks per Organization by Industry, 2025 [% of Change from 2024]
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 63

In 2025, cyber attack activity increased across Agriculture’s increase aligns with the rapid
all regions and nearly every industry. Once digital transformation of agriculture supply
again, Education remained the most targeted chains, including sorting and production facilities.
sector, averaging 4,352 attacks per organization Increased reliance on IoT, edge computing, and
per week, a 22% increase over the previous autonomous systems has improved efficiency and
year. Government, Telecommunications, and output, but also expanded the attack surface across
Healthcare & Medical also reached their highest devices, networks, and data platforms, creating
observed weekly attack volumes. new opportunities for threat actors to exploit.
As threat actors expanded their focus, critical
infrastructure and industrial sectors experienced
a sharp escalation in the number of attacks.
In 2025, Energy and Utilities, Automotive,
and Aerospace and Defense recorded year-
over-year increases ranging from 21% to 37%.
These sectors underpin essential services and
AGRICULTURE INCREASED RELIANCE ON
national infrastructure, making them particularly
attractive targets for exploitation. IOT, EDGE COMPUTING, AND AUTONOMOUS
SYSTEMS HAS IMPROVED EFFICIENCY AND
In 2025, attacks against the Hospitality, Travel, OUTPUT, BUT ALSO EXPANDED THE ATTACK
and Recreation sector increased by 50% year-
SURFACE ACROSS DEVICES, NETWORKS,
over-year, second only to Agriculture, which saw
AND DATA PLATFORMS, CREATING NEW
a 78% increase. This shift highlights growing
OPPORTUNITIES FOR THREAT ACTORS TO
interest in industries with high transaction
EXPLOIT.
volumes and PII (Personally Identifiable
Information) data.
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 64

WEEKLY ATTACKS BY INDUSTRY AND REGION
NORTH AMERICA
Education 3057 [+32%]
Healthcare & Medical 2121 [+18%]
Energy & Utilities 1991 [+88%]
Software 1970 [+61%]
Media & Entertainment 1744 [+13%]
Aerospace & Defence 1711 [*]
Consumer Goods & Services 1683 [+7%]
Associations & Non Profits 1588 [+6%]
Financial Services 1494 [+28%]
Government 1467 [+17%]
Business Services 1344 [+26%]
Telecommunications 1306 [+16%]
Biotech & Pharmaceuticals 1220 [-16%]
Automotive 967 [-12%]
Real Estate, Rentals & Leasing 884 [+16%]
Wholesale & Distribution 866 [+14%]
Transportation & Logistics 851 [+38%]
Hospitality, Travel & Recreation 834 [+59%]
Hardware & Semiconductors 792 [+24%]
Industrial Manufacturing 786 [-10%]
Construction & Engineering 692 [-13%]
Information Technology 531 [+57%]
Agriculture 490 [*]
Figure 5: North America Average Weekly Cyber Attacks per Organization by Industry, 2025
[% of Change from 2024]
* Insufficient data for 2024
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 65

WEEKLY ATTACKS BY INDUSTRY AND REGION
LATIN AMERICA
Healthcare & Medical 4782 [+64%]
Government 4240 [+19%]
Telecommunications 3581 [+5%]
Education 3350 [+19%]
Business Services 2790 [+38%]
Financial Services 2416 [+7%]
Industrial Manufacturing 2290 [+38%]
Energy & Utilities 2112 [-1%]
Media & Entertainment 1773 [+25%]
Automotive 1523 [-4%]
Consumer Goods & Services 1423 [+0.03%]
Information Technology 1378 [-13%]
Construction & Engineering 1259 [+14%]
Wholesale & Distribution 1187 [-47%]
Transportation & Logistics 1146 [-25%]
Biotech & Pharmaceuticals 958 [+22%]
Software 874 [-43%]
Figure 6: Latin America Average Weekly Cyber Attacks per Organization by Industry, 2025
[% of Change from 2024]
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 66

WEEKLY ATTACKS BY INDUSTRY AND REGION
APAC
Education 7648 [+14%]
Government 4894 [+16%]
Telecommunications 4686 [+53%]
Hardware & Semiconductors 4006 [+29%]
Healthcare & Medical 3489 [-32%]
Automotive 3263 [+30%]
Hospitality, Travel & Recreation 3184 [+11%]
Energy & Utilities 3147 [+16%]
Industrial Manufacturing 3060 [+16%]
Construction & Engineering 3024 [+0.2%]
Business Services 2629 [+12%]
Real Estate, Rentals & Leasing 2409 [-17%]
Information Technology 2337 [+49%]
Consumer Goods & Services 2238 [+17%]
Software 2168 [+12%]
Financial Services 2115 [+10%]
Biotech & Pharmaceuticals 2114 [+12%]
Transportation & Logistics 1980 [+4%]
Associations & Non Profits 1845 [*]
Media & Entertainment 1803 [+9%]
Wholesale & Distribution 1172 [-19%]
Figure 7: APAC Average Weekly Cyber Attacks per Organization by Industry, 2025 [% of Change from 2024]
* Insufficient data for 2024
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 67

WEEKLY ATTACKS BY INDUSTRY AND REGION
EUROPE
Education 4120 [+19%]
Telecommunications 2243 [+28%]
Government 2208 [+20%]
Hospitality, Travel & Recreation 2140 [+60%]
Healthcare & Medical 1980 [+8%]
Aerospace & Defence 1799 [+49%]
Automotive 1774 [+35%]
Associations & Non Profits 1708 [+36%]
Agriculture 1676 [+35%]
Media & Entertainment 1671 [+9%]
Software 1668 [+34%]
Energy & Utilities 1664 [+59%]
Wholesale & Distribution 1587 [+8%]
Consumer Goods & Services 1513 [+11%]
Construction & Engineering 1476 [+11%]
Biotech & Pharmaceuticals 1474 [+11%]
Business Services 1416 [+19%]
Hardware & Semiconductors 1403 [+75%]
Information Technology 1233 [+45%]
Industrial Manufacturing 1204 [+32%]
Financial Services 1195 [+12%]
Transportation & Logistics 1092 [-9%]
Real Estate, Rentals & Leasing 1072 [-3%]
Figure 8: Europe Average Weekly Cyber Attacks per Organization by Industry, 2025 [% of Change from 2024]
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 68

In North America, Healthcare and Medical continued disruption, and intellectual property theft. As Europe
to be a major target with an 18% increase in the accelerates its shift toward localized chip production,
average number of weekly cyber-attacks compared to cyber threat activity against its semiconductor
2024. In the first half of 2025, hundreds of health data ecosystem rises in parallel.
breaches were reported in the United States and across
Latin America. Healthcare in both regions also faced The Telecommunications sector saw a 53% in attacks
hundreds of ransomware attacks throughout the year. in APAC, with double-digit increases also observed
in North America and Europe. Several major cyber
As with global statistics, Education was the most incidents impact multiple regions. Bouygues
heavily targeted sector in APAC, recording the highest Telecom in Europe suffered a significant customer
attack volumes in the region. The sheer number of data breach. SK Telecom in Asia exposed sensitive
average weekly attacks was disproportionate to other SIM data belonging to millions of users. A Canadian
regions, with attack volumes in APAC nearly twice telecom was infiltrated by a China-linked group
those observed in other regions. Within APAC, India through an unpatched Cisco device. Cellcom in the
experienced the highest average attack volume, at United States experienced a cyberattack that caused
7,684 weekly attacks. a prolonged service outage. These incidents aligned
with a wider cross-regional campaign assessed to
Educational organizations hold large amounts of be related to a Chinese-affiliated threat actor Salt
personal data and valuable research. Together with Typhoon, which targeted telecom infrastructure on
the fact that schools and universities typically have multiple continents. All these add up to a pattern of
open network policies, they become attractive targets, consistent focus on gaining access to core systems
resulting in both targeted and opportunistic attacks. and sensitive subscriber data.
Globally, the Hardware and Semiconductors sector The Energy and Utilities sector experienced a
recorded a 34% increase year-over-year in weekly significant increase in attack levels, with the average
attacks. In 2025, APAC remained the most targeted, number of weekly attacks rising by 88% in North
averaging 4,006 attacks per week, over three times America and 59% in Europe. This pattern aligns with
the volume observed in other regions. the broader trend of geopolitically driven cyber activity
we observed over the past year. We continue to see a
correlation between kinetic geopolitical conflicts and
Within APAC, Taiwan and China were the most
heightened offensive cyber operations, particularly
heavily targeted countries, with 7,393 and 5,631
against critical infrastructure.
attacks, respectively. This concentration aligns with
APAC’s central role in the global Hardware and
Semiconductors supply chain and its prominence in State-aligned or state-affiliated threat actors appear
advanced manufacturing. to be pursuing differing objectives depending on their
geopolitical alignment, ranging from intelligence
collection and strategic access to disruption and
In Europe, Hardware and Semiconductors saw a
signaling. Public reporting from U.S. government
staggering 75% year-over-year increase in attacks,
agencies, including the Office of the Director of
whereas North America also had an increase of a
National Intelligence (ODNI), indicates that Russia,
24% in average weekly attacks. This trend aligns
China, Iran, and North Korea continue to prioritize
with European and United States strategic efforts
cyber operations targeting critical infrastructure and
to expand domestic semiconductor manufacturing
telecommunications.
under initiatives like the European Chips Act,
increasing the attractiveness of European fabricators,
suppliers, and R&D hubs as targets for espionage,
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 69

ATTACK VECTORS
Attack Delivery Vectors (Email vs. Web)
100%
11% 32% 18%
80%
89%
82%
60%
68%
40%
20%
0
2023 2024 2025
Mail Web
Figure 9: Attack Delivery Vectors (Email vs. Web), 2023-2025
In 2025, email-based attacks carrying malicious files accounted for 82% of all observed activity, while web-based
attacks represented 18%. This highlights the ongoing trend of attackers favoring email as the primary method for
delivering file-based attacks. Except for 2024, where we saw a temporary 21% decline, the dominance of email-
based attacks has steadily increased since 2018. According to Check Point Harmony Email and Collaboration
data, approximately one of every 68 emails with attachments received by an organization is malicious.
Top Malicious File Types Delivered via Email
html* 34%
svg 34%
pdf 19%
zip 3%
exe 3%
doc* 2%
rar 1.3%
xls* 0.9%
dll 0.3%
rtf 0.3%
Figure 10: Email: Top Malicious File Types, 2025
html* includes common files such as .html, .shtml, .htm, and more.
doc* includes common Office Word files such as .doc, .docx, docm, and .dot
xls* includes common Office Excel files such as .xls, .xlsx, .xlsm, and more
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 70

Throughout 2025, Check Point tracked global SVG files, initially intended for displaying vector
phishing campaigns targeting organizations graphics, are abused by attackers to serve a
worldwide. Attackers continue to rely on weaponized, role similar to that of malicious HTML files. Both are
commonly used file types that recipients are opened in web browsers by default and can be used
incentivized to open. In addition, attackers attempt to to create convincing phishing pages, execute scripts
innovate and find new ways to abuse file types with within the browser, perform HTML or SVG smuggling,
lower detection rates and weaker security defenses. or act as the initial stage of a more sophisticated
attack. In some cases, attackers even combined the
two and embedded HTML code inside the SVG files.
MOST ATTACKERS AVOID EXECUTABLES
IN THE INITIAL STAGE, RELYING ON
MULTISTAGE PHISHING INSTEAD Notable SVG waves targeted financial
institutions using the SVG smuggling technique,
where an SVG file drops embedded JavaScript files
In 2024, malicious HTML attachments accounted for for the victim to execute. This is the initial stage of
61% of email-based attacks. However, in 2025, the a multistage attack, ultimately deploying a variety
landscape diversified, as SVG and HTML together of RAT malware, such as Blue Banana, SambaSpy,
surpassed that percentage, each at 34%. PDF and SessionBot.
files remained prominent at 19%, while EXE files
accounted for only 3%. This distribution suggests In another wave, the Shadow Vector threat
most attackers avoid direct executable attachments group targeted Colombian users with court-themed
in the initial stage and instead rely on phishing SVG decoys. The goal was to redirect victims to JS/VBS
campaigns or multistage infection chains using stagers or password-protected ZIP payloads, then use
formats such as HTML, SVG, and PDF. leveraged DLL side-loading and privilege escalation to
deploy RATs like AsyncRAT and RemcosRAT.
Top Malicious File Types Delivered via Web
exe 65%
pdf 5%
dll 5%
lnk 3%
elf 3%
dex 2%
sh 1.5%
py 1.1%
xls 0.9%
doc* 0.9%
Figure 11: Web: Top Malicious File Types, 2025
xls* includes common Office Excel files such as .xls, .xlsx, .xlsm, and more
doc* includes common Office Word files such as .doc, .docx, docm, and .dot
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 71

The distribution of popular malicious file types is method for the average threat actor. Attackers
significantly different on web-based infection vectors. who were accustomed to buying direct access to
Instead of persuading a user to click on phishing organizations worldwide through these botnets had
links to initiate an elaborate chain that bypasses an to adjust their tactics. Infostealers then became a
email security gateway, many web-based downloads favorite alternative method, and infostealer logs and
and drive-by chains attempt to land an executable credentials, shared and sold in the underground
payload immediately. Our 2025 telemetry shows communities, became the fuel to support future initial
attackers overwhelmingly favor executable formats. infections.
EXE files accounted for 65% of web-delivered
malware, while the next runner-up, PDF, was at only Since then, infostealer logs have become an
5%, indicating a strong preference for direct execution escalating cybersecurity risk, as they contain
over document-based lures. This tendency is large volumes of stolen sensitive information,
reinforced by prominent web vectors, like SEO including account credentials, payment card details,
poisoning, that promote fake download pages in and cryptocurrency wallets, all extracted from
search results, Trojanized “legitimate” installers that compromised systems. Generated by infostealer
deploy the genuine software while quietly loading malware and widely traded across underground
malware, and software supply chain compromises marketplaces and Telegram channels, these logs
where attackers publish Trojanized packages that now serve as a primary enabler for follow-up attacks,
execute during installation. Gamers are also supporting a broader ecosystem of cybercrime,
heavily targeted through Trojanized game-related including fraud, account takeovers, and ransomware
tools, cheats, and cracked software distributed via operations. Check Point’s Exposure Management
torrents and file-sharing sites, which can drop actively monitors and tracks these sources, and
miners, stealers, or loaders. the following data highlights the most prominent
infostealer families.
THE INFOSTEALER ECOSYSTEM
Lumma dominated the infostealer logs landscape
at 43%. This number indicates a slight decrease
When law enforcement takedown operations
from last year’s 51%, likely due to increased law
disrupted major botnets, such as Qbot and Emotet, in
enforcement activity. The veteran Redline is the only
Operation Endgame, followed by Operation Endgame
close contender that held 22% of the logs, a clear
2.0, they also removed a significant initial infection
rise from last year’s 8%.
lumma 43%
redline 22%
meta 14%
stealc 12%
vidar 5%
Figure 12: Top Infostealer Malware Globally, 2025
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 72

By analyzing the data dumps, we see for the
second consecutive year that credentials to
gaming platforms such as Roblox and Steam
continue to top the list. This finding correlates
ACCORDING TO THE LOG DATA WE ANALYZED, strongly with the fact that gaming platforms
OVER 76% OF THE INFECTED MACHINES ARE remain one of the most prominent and effective
vectors for the distribution of infostealers. A
LIKELY NON-CORPORATE ONES, COMPARED
wide variety of themes and lures are used to
WITH 70% LAST YEAR.
facilitate the spread of infostealers through
games available on the Steam online store, as
demonstrated by cases such as PirateFi and
the Vidor infostealer. In addition, infostealers
like Stealka frequently disguise themselves
as game-related content, including cracks,
cheats, and mods, taking advantage of users’
According to the log data we analyzed, over willingness to download unofficial or modified
76% of the infected machines are likely non- gaming software.
corporate ones, compared with 70% last year.
This notable increase further highlights the Although Brazil ranks among the most targeted
growing use of the “spray and pray” strategy, countries, accounting for approximately 7% of
in which attackers seek to penetrate highly all observed infostealer activity, it represents
protected corporate environments by first only roughly one-third of that share when
compromising less-secured endpoints. In this measured against its proportion of the global
approach, threat actors initially gain access population. At the same time, six of the top ten
to BYOD or otherwise unmanaged devices most targeted countries are located in Asia,
that are connected, directly or indirectly, to despite the fact that these countries collectively
corporate networks. These devices often account for just over 28% of the world’s
serve as a convenient entry point, as they population, highlighting a disproportionate level
may lack enterprise-grade security controls. of targeting relative to population size.
The connection to the corporate environment
can take many forms, including VPN access,
Microsoft 365 accounts, collaboration
platforms, or other corporate services for which
credentials, session tokens, and cookies are
stored in the browser, enabling attackers to
later pivot into organizational systems.
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 73

Brazil 7%
India 7%
Pakistan 4%
Indonesia 4%
Vietnam 4%
Egypt 4%
United States 3%
Philippines 3%
Argentina 3%
Turkey 3%
Rest of World 58%
Figure 13: Infostealer logs for sale - top countries, 2025
Cyber risk in 2025 has shown rapid expansion across regions,
industries, and technologies. Keeping up with external threats
and internal exposure risks requires unified visibility, continuous
exposure management, and security controls that organizations
can validate and enforce across their own environments.
OMER DEMBINSKY
Data Research
Group Manager
CHAPTER 04 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 74

05
HIGH PROFILE
VULNERABILITIES

1. ToolShell Vulnerabilities high severity, with a CVSS 3.1 base score of
9.8 (Critical). Public proof-of-concept (PoC)
exploits are available, and real-world exploitation
ToolShell is a set of SharePoint on-premise
has been confirmed. Compromised Langflow
vulnerabilities involving CVE-2025-49704
instances were used to deploy the Flodrix botnet,
and CVE-2025-49706, with later variants
which enables the creation of backdoors, DDoS
designated as CVE-2025-53770 and CVE-2025-
capabilities, and potential data exfiltration.
53771. Chaining these vulnerabilities enables
unauthenticated remote code execution (RCE)
on vulnerable on-prem SharePoint servers. 3. Oracle E-Business Suite
Check Point Research observed multiple waves
(CVE-2025-61884)
of exploitation by various threat actors, including
Ink Dragon. In some cases, the exploitation was
the initial step in an espionage operation, while in CVE-2025-61884 is a critical server-side request
others, it led to the deployment of ransomware. forgery vulnerability in Oracle E-Business Suite
For example, threat actors used ToolShell to (EBS) that affects the Configurator Runtime
deploy Warlock and LockBit Black in targeted UI component in versions 12.2.3 through
networks. 12.2.14. The flaw allows an unauthenticated,
remote attacker to send crafted requests
Notably, ToolShell was exploited in the wild that are executed by an application against
before patches were publicly available. According internal services, potentially exposing sensitive
to Check Point data, the first known exploitation business data and authentication metadata.
occurred on July 7, with broader exploitation The vulnerability was exploited by threat actors
attempts starting on July 18. The exploitation associated with the CL0P extortion operation,
attempts related to this vulnerability affected 12% which used it to access internal EBS resources
of organizations. and steal business-critical data from over
100 organizations. Months after the Cl0p
exploitation, a working PoC was leaked by the
2. Langflow Remote Code Execution
Scattered LAPSUS$ Hunters collective. The
(CVE-2025-3248) leak enabled large-scale data theft, including
configuration information and financial records,
which were later used in extortion campaigns.
In April 2025, a critical remote-code execution
CISA confirmed the active exploitation and
vulnerability (CVE-2025-3248) was disclosed
added CVE-2025-61884 to the Known Exploited
in Langflow, a popular open-source visual
Vulnerabilities catalog.
framework for building and deploying AI
workflows. This vulnerability affects all
versions prior to 1.3.0. The flaw fails to require 4. React2Shell (CVE-2025-55182)
authentication and insufficiently sanitizes
user-supplied code, allowing an attacker to
CVE-2025-55182, known as React2Shell, is a
send a specially crafted HTTP request and
critical remote code execution vulnerability in
execute arbitrary Python code on the server.
React Server Components (RSC). It stems from
The vulnerability on the server is classified as
unsafe deserialization in the RSC Flight protocol,
which allows an unauthenticated attacker to send
a crafted payload to trigger code execution on the
server. The flaw affects multiple RSC packages in
CHAPTER 05 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 76

React versions 19.0, 19.1.0, 19.1.1, and 19.2.0, as observed using the exploit for malicious activity.
well as frameworks that use them, such as Next. Exploitation attempts deliver malware, establish
js. According to Check Point data, after the public backdoors, and scan for vulnerable deployments.
disclosure and release of the PoC, multiple On the first day of exploitation alone, we saw
threat actors began exploiting the vulnerability 479 exploitation attempts, and overall, during
within 24 hours. China-affiliated threat groups, December, these attempts impacted 22% of
including Earth Lamia and Jackpot Panda, were organizations.
2025 4.0%
2024 11.0%
2023 10.7%
2022 8.2%
2021 10.9%
2020 8.9%
2019 9.1%
2018 6.9%
2017 3.9%
2016 6.0%
2015 3.0%
Earlier 17.2%
Figure 1: Percentage of Attacks Leveraging Vulnerabilities by Disclosure Year, 2025
Analysis of attack data indicates that heavily on older vulnerabilities, with more than
vulnerabilities disclosed in 2025 accounted 46% of exploitation attempts exploiting CVEs
for 4% of all exploitation attempts. The time- published prior to 2020. This reflects a persistent
to-exploitation has become lower every year, systemic gap in patching, where many system
as observed with ToolShell and React2Shell. vulnerabilities remain unaddressed for years
At the same time, attackers continue to rely despite the existence of available fixes.
CHAPTER 05 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 77

06
2026 INDUSTRY PREDICTIONS:
THE FUTURE OF CYBER SECURITY

The following predictions highlight the most
consequential shifts shaping cyber security in
2026, spanning attacker behavior, technology
evolution, and the changing expectations placed
on organizations to manage and prove resilience. ADDRESSING THE AI AUTONOMY
GOVERNANCE GAP WILL REQUIRE AI
1. Agentic AI Transitions from GOVERNANCE COUNCILS, ENFORCEABLE
POLICY GUARDRAILS, AND IMMUTABLE
Assistance to Operational Autonomy
AUDIT MECHANISMS THAT RECORD AND
EXPLAIN EVERY AUTONOMOUS ACTION.
2026 will see agentic AI move to the mainstream.
Autonomous systems capable of reasoning,
planning, and acting with minimal human input
move us from assistants who draft content to
agents who execute strategy. These systems will
allocate budgets, monitor production lines, and
reroute logistics, all in real-time. 2. Prompt Injection and Data Poisoning -
AI Models Become the New Zero-Day
Manufacturing environments will increasingly
be able to self-diagnose faults and trigger
automated procurement through blockchain- As generative AI is embedded across customer-
verified supply networks. At the same time, facing services, internal workflows, and
marketing, finance, and security teams will security operations, AI models themselves are
depend on agents that continuously absorb emerging as high-value attack surfaces. In 2026,
contextual signals and operate at machine speed. adversaries will increasingly exploit prompt
injection, embedding covert instructions in text,
code, or documents that manipulate model
Autonomy without accountability is a liability.
behavior, as well as data poisoning, where tainted
According to the World Economic Forum’s Global
inputs distort or compromise training data.
Cyber Security Outlook 2025, AI autonomy
without governance is one of the top three
systemic risks to enterprise resilience. Because many LLMs operate via third-party APIs,
just one poisoned dataset can propagate across
thousands of applications. Conventional patching
As these agents gain real operational authority,
offers limited protection in this context; maintaining
unresolved governance questions surface: who
model integrity becomes an ongoing process.
validates autonomous decisions, audits decision
logic, or intervenes when intended actions
and real-world outcomes diverge? Addressing AI models are today’s unpatched systems. Every
this gap will require AI governance councils, external data source represents a potential
enforceable policy guardrails, and immutable exploit path. In 2026, AI security leaders will
audit mechanisms that record and explain every differentiate themselves by operationalizing
autonomous action. governance, validation, and continuous oversight
to ensure AI systems remain trustworthy at
scale.
CHAPTER 06 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 79

3. Supply Chain and SaaS Exposure Organizations must extend visibility to third-
party and fourth-party SaaS supply chain sites
Intensifies Across Hyperconnected
and adopt continuous monitoring and Zero Trust
Ecosystems access to manage an attack surface that is
increasingly expanding beyond their perimeter.
Enterprises now operate within webs of vendors,
APIs, and integrations, creating attack paths
4. Trust Is the New Perimeter:
where just one weak supplier can lead to
Deepfakes and Conversational Fraud
widespread compromise. As ecosystems grow
more automated and interdependent, incidents
spread faster through shared code, tokens,
Generative AI has blurred the line between
and cloud services than they can be traced.
genuine and fabricated content. Voice cloning,
The ENISA Supply Chain Cybersecurity Report
real-time synthetic video, and AI-driven chat
2025 warns that 62% of large organizations
interactions now enable attackers to bypass
experienced at least one third-party compromise
traditional identity and access controls, including
in the past year.
multi-factor authentication. ENISA’s Threat
Landscape 2025 lists “synthetic identity and AI-
At the same time, global supply chains are generated social engineering” among the top five
transforming under the pressure of automation. risk vectors.
Agentic AI will enable autonomous risk
management: self-learning systems that map
Technical authenticity no longer guarantees
dependencies, monitor third-party compliance,
human authenticity or that interactions even
and predict disruptions. Yet hyperconnectivity
originate from a human at all. As non-human
also magnifies exposure: compromised code
identities (NHIs) proliferate alongside AI
libraries, API tokens, and cloud credentials can
agents and automated systems, every human–
ripple through ecosystems faster than incidents
machine interface becomes a potential point
can be traced.
of compromise. Business Email Compromise
will evolve into trust-based fraud, conducted
through deepfakes, adaptive language, and
emotional manipulation. This year, deception will
sound like trust. Enterprises must continuously
verify identity, context, and intent across every
interaction.
ORGANIZATIONS MUST EXTEND VISIBILITY
TO THIRD-PARTY AND FOURTH-PARTY
SAAS SUPPLY CHAIN SITES AND ADOPT
CONTINUOUS MONITORING AND ZERO TRUST
ACCESS TO MANAGE AN ATTACK SURFACE
THAT IS INCREASINGLY EXPANDING BEYOND
THEIR PERIMETER.
CHAPTER 06 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 80

5. Quantum Risk Moves From Long- This evolution is expected to deepen. Attackers
are already using AI to generate faster, broader,
Term Concern to Near-Term Action
and more tailored campaigns, and this will
increasingly push organizations to develop
Quantum computing may still be years from defensive capabilities that can match that pace,
cracking today’s encryption, but the threat with continuous learning, real-time context, and
has already changed, and should continue to more autonomous operational support. It reflects
change, enterprise behavior. Governments, cloud a shift in how security teams prioritize actions,
providers, and large enterprises are racing to understand risk, coordinate response, and
secure cryptographic agility, migrating from ultimately, increase efficiency.
vulnerable Rivest–Shamir–Adleman (RSA) and
Elliptic Curve Cryptography (ECC) algorithms
AI is becoming an integral part of the
to post-quantum cryptography (PQC) standards
operational layer within security operations,
before adversaries can weaponize them.
enhancing human expertise, simplifying manual
workflows, and reducing the mean time to
The danger lies in the 'harvest now, decrypt later' remediation (MTTR).
(HNDL) strategy. Attackers are already stealing
encrypted data today, confident that quantum
The accelerated adoption of AI is making it part of
decryption will expose it tomorrow. In 2026,
the operational backbone of cyber security rather
preparation moves from theory to execution.
than an extension of existing tools, shaping
Boards will fund cryptographic bills of materials
analytical workflows and decision-making
(CBOMs) to catalogue every algorithm, certificate,
processes to be more consistent, automated, and
and key across their environments. Organizations
guided by precise controls.
will pilot National Institute of Standards and
Technology (NIST)-approved post-quantum
algorithms and pressure vendors to show clear
migration timelines.
Quantum risk is not about tomorrow’s machines.
It is about today’s data. Every organization
must assume its encrypted assets are already
being harvested and prepare for a world where
THE ACCELERATED ADOPTION OF AI IS
prevention depends on cryptographic agility.
MAKING IT PART OF THE OPERATIONAL
BACKBONE OF CYBER SECURITY RATHER
6. AI Becomes a Strategic Decision Engine
THAN AN EXTENSION OF EXISTING TOOLS,
SHAPING ANALYTICAL WORKFLOWS AND
AI is steadily changing the foundations of cyber
DECISION-MAKING PROCESSES TO BE MORE
security. What once served mainly as a tool for
CONSISTENT, AUTOMATED, AND GUIDED BY
operational efficiency is now influencing how
both attackers and defenders plan, adapt, and PRECISE CONTROLS.
execute their strategies. The industry is moving
into a phase where AI is no longer a supporting
capability, but an embedded element in detection,
analysis, and decision-making workflows.
CHAPTER 06 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 81

7. The AI Reality Check 8. Regulation and Accountability
Expand - Cyber Resilience Becomes
After two years of near-frantic AI adoption, we
a License to Operate
will experience our first major recalibration.
Many organizations that rushed to integrate
generative AI tools will discover ungoverned Regulators worldwide are closing the gap
systems, exposed APIs, and compliance blind between innovation and accountability. In 2026,
spots. Shadow AI, employee-initiated tools using regulation ceases to be a reactive approach.
corporate data, will proliferate, creating invisible Frameworks such as the EU’s NIS2 Directive, the
data leaks and inconsistent security standards. AI Act, and the U.S. SEC incident-disclosure rules
will converge on a single principle: cyber security
must be measurable and demonstrable in real-
This phase of disillusionment is necessary:
time. Governments will now expect continuous
it will drive the shift from experimentation to
proof of resilience. Organizations are expected
accountability. Executives will begin demanding
to demonstrate that their preventive controls,
AI value measured in outcomes, not hype. AI
incident response plans, and data protection
assurance frameworks will emerge across
measures are consistently enforced.
various sectors, necessitating formal audits
to ensure fairness, robustness, and security.
Leadership teams must establish clear policies There is a strong reason behind this regulatory
for AI use and align them with legal, ethical, and acceleration: society’s growing dependence
risk frameworks. Responsible deployment will on digital services to maintain daily life and
hinge on explainability and continuous validation, the economy without significant disruptions.
not unchecked automation. Compliance will Business resiliency has become the primary
expand from privacy to algorithmic accountability. driver behind the increasing compliance
requirements.
AI’s first disruption was speed; its second will
be governance. 2026 will reward those who treat This shift will mark the end of the era of “annual
AI not as a shortcut but as a capability to be compliance.” Enterprises will rely on automated
secured, audited, and improved. compliance monitoring, machine-readable
policies, real-time attestations, and AI-based risk
analytics. Boards and CEOs will carry personal
responsibility for oversight.
Cyber resilience is no longer paperwork;
it’s performance. The ability to demonstrate
protection continuously will determine market
AI’S FIRST DISRUPTION WAS SPEED; ITS
access and trust.
SECOND WILL BE GOVERNANCE. 2026 WILL
REWARD THOSE WHO TREAT AI NOT AS
A SHORTCUT BUT AS A CAPABILITY TO BE
SECURED, AUDITED, AND IMPROVED.
CHAPTER 06 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 82

07
2026 CISO
RECOMMENDATIONS

BY JONATHAN FISCHBEI
Field CISO
Security leaders’ primary challenge in 2026 CISOs should reinforce prevention-led
is maintaining the organization's security as architectures with continuous validation
attacker capabilities, techniques, and scale and transparency mechanisms that confirm
evolve faster than ever before, touching on wider protections are working under real conditions.
attack surfaces, from everyday workflows and This includes integrating external signals
endpoints to hybrid environments composed of such as responsible vulnerability disclosure,
increasingly complex webs of systems. At the targeted security awareness tied to observed
same time, CISOs are expected to demonstrate, threat activity, and structured programs that
clearly and continuously, operational efficiency surface weaknesses before adversaries exploit
and support measurable business outcomes. them. These elements are not substitutes
The recommendations that follow reflect the for prevention, but independent checks that
priorities that CISOs must focus on, including strengthen confidence in defensive effectiveness
reducing exposure, governing risk in dynamic and accelerate improvement.
environments, and demonstrating resilience
against an increasingly aggressive and Why it matters: Adversaries operate at scale,
unpredictable threat landscape. iterate rapidly, and exploit the first viable
weakness they encounter. Organizations that rely
on single controls or static assurance models are
1. Establish Prevention-Led, Layered
more likely to experience cascading failure, while
Security Programs prevention-led, layered programs reduce both
the likelihood and impact of successful attacks.
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
CHAPTER 07 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 84

2. Govern Data Protection as a Core sensitive data against future advancements in
cryptography.
Security Outcome
Why it matters: Ransomware campaigns
Data exposure now represents the most
increasingly involve confirmed data exfiltration,
consequential outcome of modern cyber
making data exposure, rather than downtime,
incidents, exceeding the business impact of
the primary source of regulatory, financial, and
service disruption alone. Security programs
reputational impact. Organizations that fail
must therefore treat data protection as a first-
to govern data protection as a core security
order objective, governed by how sensitive data
outcome remain vulnerable to compounding
is accessed, moved, and aggregated across
loss during incidents and long-tail risk as data
environments—not by static classifications
persists beyond today’s threat horizon.
or perimeter assumptions. In this context,
ransomware incidents should be addressed by
default as data-exposure events, with availability 3. Operationalize Cloud, SaaS, and AI
loss viewed as only one dimension of impact.
Security
Cloud, SaaS, and AI environments introduce risk
primarily through speed, scale, and change, not
just misconfiguration. Continuous deployment,
third-party integrations, and automated service
DATA EXPOSURE NOW REPRESENTS THE interactions create exposure that cannot be
effectively governed through identity-centric
MOST CONSEQUENTIAL OUTCOME OF MODERN
or compliance-driven controls alone. These
CYBER INCIDENTS, EXCEEDING THE BUSINESS
platforms must be secured as living, operational
IMPACT OF SERVICE DISRUPTION ALONE.
systems, where risk emerges from how services
interact and execute in real-time.
CISOs should establish governance that
continuously evaluates platform posture and
operational behavior, including configuration
drift, API usage, service-to-service trust, and
application-level interactions. AI systems
CISOs should prioritize architectural controls
require the same operational discipline as other
that limit data blast radius and recovery risk,
production platforms, with defined ownership,
including segmentation of data access paths,
monitored usage boundaries, and accountability
strict least-privilege enforcement, and resilience
for how models are accessed, integrated, and
measures such as immutable backups and
acted upon. The focus is not on measuring
regularly exercised incident-response playbooks.
resilience or enforcing identity policy, but on
These controls must be designed to assume
maintaining ongoing control over how dynamic
partial compromise and focus on preventing
platforms behave as they evolve.
large-scale data exfiltration, accelerating
recovery, and preserving trust during and
after an incident. This governance model also Why it matters: Attackers increasingly exploit
establishes a foundation for emerging risk APIs, automation, and runtime interactions to
domains, including the long-term protection of bypass identity checks and perimeter defenses.
CHAPTER 07 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 85

Without continuous platform governance, expand the attack surface, rendering implicit
organizations lose visibility and control between trust models and static access assumptions
change cycles, creating exploitable gaps that obsolete. Effective Zero Trust requires continuous
scale as environments become more complex. verification of identity and context, least-privilege
access by default, and architectural controls
that limit lateral movement across cloud, SaaS,
4. Treat Third-Party Risk as Structural
network, and development environments. The
Exposure goal is not only to prevent misuse of identity, but
to contain the impact when identity is inevitably
compromised.
Vendors, SaaS providers, and partners are
embedded directly into enterprise environments
through access, integrations, and shared
services.
CISOs should manage third-party risk
as structural exposure, not as a periodic
EFFECTIVE ZERO TRUST REQUIRES
assessment exercise. This requires continuous
CONTINUOUS VERIFICATION OF IDENTITY
monitoring of vendor access, segmentation
AND CONTEXT, LEAST-PRIVILEGE ACCESS BY
of partner connections, and enforcement of
least-privilege and Zero Trust principles across DEFAULT, AND ARCHITECTURAL CONTROLS
external identities. THAT LIMIT LATERAL MOVEMENT.
Security obligations must be measurable and
enforceable through SLAs, but documentation
alone is insufficient. Real risk emerges from how
vendors access systems, what permissions they
hold, and how compromise propagates across
shared trust relationships.
The same Zero Trust principles underpin
resilience against AI-enabled social engineering,
Why it matters: Supply-chain and SaaS-linked
cloud-driven attack surface expansion, and
incidents increasingly originate from trusted
ransomware operations that increasingly rely on
vendor access and inherited trust, expanding
stolen identities rather than exploits.
blast radius beyond the organization’s direct
control.
Why it matters: Zero Trust is the practical
framework for managing modern identity risk—
reducing implicit trust, constraining blast radius,
5. Anchor Zero Trust Architecture in
and ensuring identity compromise does not
Human and Non-Human Identity
automatically translate into widespread access
or business disruption.
Zero Trust must be treated as a core defense
against identity-driven attacks. As phishing,
credential theft, and token abuse enable
attackers to operate as trusted users and non-
human identities, these methods dramatically
CHAPTER 07 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 86

6. Harden Trust-Based Business controls are particularly critical for executives and
high-risk business functions, where successful
Processes Against Abuse
impersonation can enable immediate financial
loss or serve as a precursor to ransomware
Attackers are increasingly monetizing access by deployment by facilitating credential resets, access
exploiting implicit trust in business workflows, expansion, or data exfiltration.
rather than relying solely on technical
compromise. Business Email Compromise
Why it matters: BEC and impersonation
(BEC), executive impersonation, and vendor
attacks are increasingly serving as both direct
fraud remain highly effective because they exploit
monetization vectors and enablers for ransomware
legitimate communication channels to initiate
and extortion campaigns. As attackers blend
financial transactions, disclose sensitive data,
social engineering, identity abuse, and AI-enabled
or modify access permissions. With AI-driven
deception, organizations that fail to harden trust-
impersonation on the rise, including realistic
based workflows remain vulnerable to high-impact
phishing lures, synthetic voice, and deepfake-
outcomes, even in environments with strong
assisted social engineering, these attacks have
perimeter and endpoint defenses.
further increased their credibility and scale,
Top of Form
reducing the time required to move from initial
Bottom of Form
contact to impact.
7. Integrate OT and Cyber Risk
Governance
Operational Technology (OT) environments
now sit at the intersection of cyber risk,
WITH AI-DRIVEN IMPERSONATION ON THE
physical safety, and business continuity. As OT
RISE, THESE ATTACKS HAVE INCREASED
environments increasingly adopt Industry 4.0
THEIR CREDIBILITY AND SCALE, REDUCING
architectures—extending industrial systems
THE TIME REQUIRED TO MOVE FROM INITIAL through IoT and IIoT devices, cloud connectivity,
CONTACT TO IMPACT. and remote access— increased connectivity
between IT and OT—driven by remote access,
cloud monitoring, and digital transformation—
has expanded attack paths into environments
where compromise can result in physical
disruption, safety incidents, or prolonged
operational downtime, not just data loss.
CISOs should treat trust-based business
Traditional IT security models are insufficient
processes as a core component of the threat
in these settings, where availability and
surface and apply security controls accordingly.
deterministic behavior are paramount, and
This includes strengthening protections across
active security controls must be applied with
email and collaboration platforms, implementing
care. Securing this new, cloud-connected OT
mandatory, context-aware verification for high-risk
environment requires security approaches
actions, and eliminating single-step approvals and
that are aligned with its expanded digital and
other implicit trust assumptions from payment,
operational exposure.
vendor, and access-granting workflows. These
CHAPTER 07 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 87

CISOs should ensure that OT security is governed organization’s real-world ability to withstand,
through a risk-based model aligned with contain, and recover from active threats.
operational realities, rather than being treated
as a standalone technical domain. This includes At the same time, increasing complexity across
enforcing strict and continuously validated cloud, automation, and AI environments makes
IT-OT segmentation, leveraging passive and it critical not to lose focus on cyber hygiene and
non-intrusive monitoring to maintain visibility security fundamentals. Many successful attacks
without disrupting operations, and integrating still exploit basic weaknesses, underscoring that
OT telemetry into centralized SOC workflows to resilience depends on maintaining strong “back-
enable early detection of abnormal activity. to-basics” practices alongside newer capabilities.
Just as importantly, cyber, engineering, and CISOs should shift toward continuous control
physical safety teams must operate from a validation and exposure-driven measurement,
shared risk framework that prioritizes safety, integrating telemetry from across the
uptime, and resilience, ensuring cyber incidents environment to assess not only whether controls
in OT environments are assessed and responded exist, but also whether they are effective under
to with full awareness of their potential physical real-world conditions. This includes monitoring
and operational impact. exposure trends, remediation velocity, and
time-to-contain across attack paths, as well as
Why it matters: As attackers increasingly automating evidence collection to reduce manual
target industrial and critical infrastructure compliance overhead. Effectiveness must be
environments, cyber incidents in OT no longer communicated differently to boards, regulators,
represent isolated technical events—they partners, and customers, using outcome-based
directly translate into safety risks, operational metrics that demonstrate reduced risk, faster
disruptions, and material business impacts. response times, and improved containment,
Organizations that fail to secure this modern, rather than merely checklist completion.
Industry 4.0 OT environment as part of enterprise
cyber risk governance remain vulnerable to Signals from digital trust and transparency
attacks that bypass traditional IT defenses and programs, such as external vulnerability
exploit the gap between cyber and physical reporting, third-party findings, and
security. responsiveness to disclosed risk, should be
treated as indicators of operational resilience,
not reputational liabilities. These signals
8. Prove Resilience, Not Just
provide independent validation of how quickly
Compliance and effectively an organization identifies and
addresses exposure.
Cyber resilience can no longer be inferred from
Why it matters: In an environment of continuous
policy adherence or point-in-time assessments.
threat activity and increasing regulatory scrutiny,
As attack surfaces change continuously and
organizations that can demonstrate resilience
threats exploit exposure faster than review cycles
through ongoing measurement and real-world
can detect, resilience must be measurable,
outcomes are better positioned to maintain
continuously validated, and expressed in
trust, meet regulatory expectations, and respond
business-relevant terms. Annual audits and
credibly to incidents than those relying solely on
static risk assessments may satisfy regulatory
periodic compliance assessments.
requirements, but they do not reflect an
CHAPTER 07 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 88

08
AN EXPOSURE
MANAGEMENT PERSPECTIVE

THREAT INTELLIGENCE BEFORE
THE BREACH
An Exposure Management Perspective THE BIGGEST QUESTION IS NOT HOW
QUICKLY ORGANIZATIONS RESPOND TO
From Incident Response to Preemptive
INCIDENTS, BUT HOW OFTEN THOSE
Security
INCIDENTS COULD HAVE BEEN PREVENTED
ALTOGETHER.
Incident response is a critical
function in any security
program, but ultimately, it only represents the
final stage of most attacks. By the
time response teams are engaged,
adversaries have already completed
What Attackers Do Before the Breach
reconnaissance, established infrastructure,
and initiated access. The biggest question
is not how quickly organizations respond to Before an incident unfolds internally, attackers
incidents, but how often those incidents could typically invest time in preparation. This
have been prevented altogether. preparatory phase often includes activities that
are external to the organization but directly
A growing body of intelligence shows that relevant to its security posture. Common
many attacks leave detectable external signals examples include the creation of look-
well before internal compromise occurs. alike domains, brand impersonation across
These insights, when understood in context, social platforms, deployment of phishing
present an opportunity to reduce reliance on infrastructure, harvesting of credentials from
emergency response by addressing exposure prior breaches, and reconnaissance of exposed
earlier in the attack lifecycle. From an exposure services. Individually, these events may appear
management perspective, threat intelligence disconnected or benign. However, collectively,
plays a foundational role in taking security they form the earliest indicators of an impending
programs from reactive containment to intrusion attempt.
preemptive risk reduction.
Crucially, these activities surface outside
This perspective does not replace traditional internal monitoring controls. They
incident response or post- precede malware execution, lateral movement, or
breach investigation. Rather, it complements privilege escalation, and therefore occur before
them by focusing on the conditions and activities most incident response triggers are activated. As
that precede incidents, with the aim of preventing a result, they are frequently overlooked or
issues from ever reaching the point where a deprioritized, even though they represent the
response is required. earliest stage at which intervention is possible.
CHAPTER 08 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 90

Pre-Incident Intelligence Across the When attacker preparation activity is addressed
during this early phase, the downstream
Global Attack Surface
impact can be significant. Disrupting phishing
infrastructure, neutralizing impersonation
Across the global attack surface, certain patterns assets, or mitigating exposed entry points
consistently emerge during the pre-incident before exploitation can prevent campaigns from
phase. Attackers rarely move directly from progressing to internal compromise.
intent to exploitation. Traditionally, they stage
infrastructure, test delivery mechanisms, and
From an exposure management standpoint,
refine targeting based on observed responses.
the goal is not to predict every attack, but
to reduce the number of exposures that
While the specific prevalence of phishing, attackers have available to them.
impersonation, or credential-based techniques By addressing threats while
varies by sector and geography, these activity remains external, organizations can
vectors continue to dominate early attack alter attack paths before they generate alerts,
activity. Importantly, the same preparation incidents, or business disruption.
techniques observed externally often align
closely with the tactics incident response
Effective pre-breach disruption often results
teams later observe post-breach. The
in the absence of incidents rather than visible
challenge for defenders is not the absence of
response metrics. Attacks fail silently. Users
early signals, but the difficulty of recognizing
are never impacted. Incident response teams
which exposures are relevant, credible, and
are never engaged. Over time, this reduction in
actionable for a specific organization.
incident volume is one of the clearest indications
that exposure is being managed effectively.
Case Patterns: Preempting the Same
Threats Incident Response Sees
THE CHALLENGE FOR DEFENDERS IS NOT During incident response investigations, certain
attack sequences recur frequently. When viewed
THE ABSENCE OF EARLY SIGNALS, BUT
retrospectively, many of these incidents follow
THE DIFFICULTY OF RECOGNIZING WHICH
a progression that was externally visible before
EXPOSURES ARE RELEVANT, CREDIBLE,
internal compromise occurred.
AND ACTIONABLE FOR A SPECIFIC
ORGANIZATION.”
CHAPTER 08 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 91

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
execution. already served its purpose.
Proactive Defense Insights • The likelihood of breach will correlate less
with severity scores and more with exposure
duration and attacker readiness.
• Attacker preparation will continue to
accelerate, driven by automation and readily • Organizations that align threat intelligence
available infrastructure. with exposure reduction will reduce incident
frequency over time.
CHAPTER 08 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 92

Closing the Gap: Threat Intelligence as By connecting pre-incident intelligence with post-
incident learnings, organizations can close the
the First Step of Exposure Management
gap between what they respond to and what they
prevent. Threat intelligence is not an add-on or
Incident response provides invaluable insight into a feed; it is the starting point for understanding
how attacks succeed. Exposure management exposure, prioritizing action, and reducing the
applies those lessons earlier in the lifecycle, volume of incidents that require a response.
utilizing threat intelligence to identify and
mitigate risk before incidents occur.
Incident response shows us how attacks succeed. The
real opportunity exposure management provides is threat
intelligence - using those lessons earlier, when attacker activity
is still external and exposure management can stop incidents
before response is ever required.
MICHAEL GREENBERG
Head of Product Marketing
Exposure Management
CHAPTER 08 CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 93

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
CHECK POINT SOFTWARE | THE STATE OF CYBER SECURITY 2026 94

© 2026 Check Point Software Technologies Ltd. All rights reserved.