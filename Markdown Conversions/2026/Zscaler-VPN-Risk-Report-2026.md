Zscaler
ThreatLabz 2026
VPN Risk Report
1

| Executive Overview  |     |     |     |     |     | 3   |
| ------------------- | --- | --- | --- | --- | --- | --- |
Table of

| Fighting AI with Blindfolds  |     |     |     |     |     | 4   |
| ---------------------------- | --- | --- | --- | --- | --- | --- |
Contents

| AI-powered Social Engineering: The Credential Theft Multiplier   |     |      |     |     |     |     5 |
| ---------------------------------------------------------------- | --- | ---- | --- | --- | --- | ----- |

| The Response Window Has Collapsed  |     |     |     |     |     | 6   |
| ---------------------------------- | --- | --- | --- | --- | --- | --- |

| What the Tunnel Hides  |     |     |     |     |     | 7   |
| ---------------------- | --- | --- | --- | --- | --- | --- |

| Lateral Movement Is the Multiplier Once Attackers Get In   |     |     |     |     |     |   8 |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |

| The Hole In the Firewall  |     |     |     |     |     | 9   |
| ------------------------- | --- | --- | --- | --- | --- | --- |

| One Credential, Full Access  |     |     |     |     |     | 10  |
| ---------------------------- | --- | --- | --- | --- | --- | --- |

| Ransomware’s Favorite Door  |     |     |     |     |     | 11  |
| --------------------------- | --- | --- | --- | --- | --- | --- |

| The Operational Tax  |     |     |     |     |     | 12  |
| -------------------- | --- | --- | --- | --- | --- | --- |

| Nation-States Inside the Perimeter  |     |     |     |     |     | 13  |
| ----------------------------------- | --- | --- | --- | --- | --- | --- |

| The Clock Is the Risk  |     |     |     |     |     | 14  |
| ---------------------- | --- | --- | --- | --- | --- | --- |

| From Reactive to Resilient  |     |     |     |     |     | 15  |
| --------------------------- | --- | --- | --- | --- | --- | --- |

| Zero Trust – The Execution Gap  |     |     |     |     |     | 16  |
| ------------------------------- | --- | --- | --- | --- | --- | --- |

| VPN to Zero Trust: Readiness Assessment  |     |     |     |     |     | 17  |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- |

Predictions For 2026 And Beyond                                                                                                              18

| How Zscaler Transforms Secure Access   |     |     |     |     |     | 19  |
| -------------------------------------- | --- | --- | --- | --- | --- | --- |

|     Key Differentiators of Zscaler Private Access (ZPA)   |     |     |     |     |     | 20  |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |

| Methodology & Demographics  |     |     |     |     |     | 21  |
| --------------------------- | --- | --- | --- | --- | --- | --- |
Zscaler ThreatLabz 2026 VPN Risk Report   ©2026  Cybersecurity Insiders.  All Rights Reserved. 2

Executive_
Overview
For decades, VPN was the default answer to remote access
security – reliable, familiar, and deeply embedded in
enterprise architecture. That era is ending. AI has accelerated • The response window has collapsed. 79% say the greatest • Encrypted tunnels shield the attacker. Sixty percent inspect a
attack timelines from weeks to minutes, automated AI-driven risk is attackers weaponizing vulnerabilities faster quarter or less of encrypted VPN traffic. Fifty-two percent describe
credential theft at industrial scale, and given adversaries a than patches can be deployed. Only 6% can patch a critical VPN their VPN as a transport layer with limited or no inspection capability.
speed advantage that human-led defense cannot match. vulnerability within 24 hours; 54% need a week or more. CrowdStrike Malware delivery, command-and-control, and data exfiltration all ride
VPN was built for a world where defenders had time to measured average eCrime breakout time at 29 minutes in 2025, the same encrypted tunnel as legitimate traffic, indistinguishable and
patch, investigate, and respond. That world no longer exists. with the fastest at 27 seconds.¹ Attackers operate in minutes. Most uninspected. Attackers don’t need to build covert channels when the
defenders still operate in weeks. VPN already provides one.
Our survey of 822 IT and cybersecurity professionals surfaces
a persistent gap: organizations recognize VPN risk clearly, but • Defenders are fighting AI with blindfolds on. 61% report • Operational friction is eroding security. Seventy-three percent
the perimeter-based access architecture they still depend on confirmed or suspected AI-enabled attacks in the past twelve say VPN demands more effort than modern alternatives. Forty-five
cannot contain AI-driven threats that now move in minutes. months, yet only 5% trust their VPN to detect and stop them. 70% percent report significant or major productivity impact. The predictable
The remaining question is how fast they replace it. report limited or no visibility into AI-enabled threats traversing VPN result: 63% say users intentionally bypass VPN controls to reach
connections. With one in five unable to distinguish AI-assisted applications faster. When the sanctioned path is the slowest path,
intrusions from conventional attacks, many organizations will not the VPN generates the exposure it was designed to prevent.
recognize an AI-powered attack until the damage is done.
The VPN architecture itself is the constraint. Faster patching, • Zero trust adoption is accelerating, but the gap remains.
better monitoring, and tighter policies help at the margins, • After compromise, containment fails. 84% express extreme or Eighty-four percent are planning or transitioning to zero trust, up from
but none address the underlying exposure VPN creates by significant concern about lateral movement, yet 77% cannot contain 78% two years ago. Fifty-one percent report declining VPN usage.
design, and AI-driven attacks now exploit that exposure it once it starts. Only 11% can restrict a compromised session to a The drivers map directly to this report’s findings: lateral movement
faster than any manual process can close it. single application, and in one-third of environments a single stolen elimination (67%) and reduced operational overhead (62%). Hybrid
credential opens the entire network. AI-driven speed makes the initial VPN environments will persist for years, extending exposure during
This report examines each risk in detail, quantifies the VPN compromise more likely; once inside, attackers find little to stop the coexistence period.
operational cost, and provides a readiness assessment them. Ransomware operators exploit this gap systematically - the
structured around the CISA Zero Trust Maturity Model to Akira group collected over $42 million from VPN-based campaigns
help security leaders measure the gap and prioritize the path confirmed by FBI and CISA.²
from Reactive to Resilient maturity levels. The window to act
is measured in the same unit as the threats: minutes.
1. CrowdStrike, 2026 Global Threat Report, February 2026. 2. FBI and CISA, Joint Cybersecurity Advisory: Akira Ransomware, April 2024; updated reporting through 2025.
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 3

Fighting AI In the past 12 months, has your organization experienced or detected any
attacks you believe were AI-enabled or AI-assisted?
with Blindfolds
Confirmed 61%
18%
AI attacks
confirmed
Suspected
43% or suspected
AI attacks
In the past 12 months, has your organization experienced or detected any
20%
In this report, “AI-enabled attack” refers to One in five organizations cannot distinguish an No evidencaettacks you believe were AI-enabled or AI-assisted?
attack activity where respondents observed AI-assisted intrusion from a conventional attack.
This 19% means the real figure
Unable to
19%
AI being used to increase speed, scale, or That 19% means the incident figures reported
distinguish is almost certainly higher
Confirmed 61%
18%
sophistication – for example automated here are almost certainly an undercount. AI attacks
reconnaissance, AI-generated social confirmed n=822
Suspected
0 10 20 30 43%40 5o0r susp6e0cted
engineering, rapid exploit adaptation, or evasion Defensive readiness has not kept pace. Over AI attacks
techniques. The classification reflects what half say legacy VPN infrastructure blocks
Figure 1: AI Attacks Are Already Here
20%
defenders observed and attributed in their integration of AI-driven security tools entirely, No evidence
environments, not laboratory-grade certainty. which is why only one in four has managed to
This 19% means the real figure
Unable to
deploy AI-powered monitoring. 79% fear AI will
Do you believe your current VP1N9 %infrastructure is capable of inspecting and
distinguish is almost certainly higher
stopping AI-generated attacks?
AI-assisted attacks have been building for years, weaponize vulnerabilities faster than they can
74 pts
The gap between fear and readiness
but the last twelve months pushed them into patch, yet only 5% trust their VPN to detect and
n=822
79% fear AI exploit speed vs. 5% trust VPN Otnoly s 5t%o ptr uits t
17%
day-to-day reality. 18% confirmed AI-enabled stop AI-enabled threats when patching fails. 0 10 20 30 40 50 60
their VPN to
Unsure 5%
attacks in the past twelve months and another That 74-point gap between fear and readiness detect and stop
69%Figure 1: AI Attacks Are Already HFeurelly capable
AI-enabled
43% suspected them. Together, that means defines the defensive crisis this report measures.
threats
61% report confirmed or suspected AI-enabled cannot inspect
or are unsure 26%
attacks. Only 5% trust their VPN to detect and Do you believe your current VPN infrastructure is capable of inspecting and
Partially,
stopping AI-generated attacks?
stop AI-enabled threats.
with trade-offs
52%
No — VPN is
Only 5% trust
17%
just a pipe
their VPN to
Unsure 5%
detect and stop
69% Fully capable
Figure 2: VPNs Can’t See What’s Coming AI-enabled
threats
cannot inspect
or are unsure 26%
Partially,
Closing that gap requires moving inspection and detection inline at the access layer, where defensive AI
with trade-offs
52%
can match the speed of modern automated attack.
No — VPN is
just a pipe
Every quarter that gap stays open, the advantage tilts further toward the attacker.
Figure 2: VPNs Can’t See What’s Coming
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 44

AI-powered Social Engineering:
The Credential Theft Multiplier
Which AI-enabled attack techniques are Recent credential-theft campaigns show
organizations most concerned about targeting how rapidly VPN phishing is evolving. Since
their VPN infrastructure? The clear leader is AI- mid-January 2026, researchers reported a Which AI-enabled attack techniques are organizations most
concerned about targeting their VPN infrastructure?
generated phishing or social engineering to steal threat actor using SEO poisoning to lure VPN
VPN credentials (63%)—ahead of automated users to trojanized installers that display a fake
vulnerability scanning and exploitation at scale login prompt to steal enterprise VPN credentials,
AI-generated phishing or social
63%
engineering to steal VPN credentials
(57%) and adaptive attacks that evade traditional then route victims to the legitimate site to
detection signatures (49%). That ordering reduce suspicion.³ Automated vulnerability scanning and
57%
exploitation at scale
matters: it signals that for many adversaries, the
Adaptive attacks that evade
fastest path to VPN compromise isn’t “breaking This is why credential theft remains one of the
49%
traditional detection signatures
in,” but logging in. most structurally dangerous VPN risks. The
Automated lateral movement once
perimeter-style model authenticates once and
38%
initial VPN access is gained
AI raises both the speed and success rate of then grants access based on that moment in
AI-assisted reconnaissance of your
social engineering. Pretexts can be customized time. Anyone holding a valid credential can 25%
network topology through VPN conne
in seconds, lures can be iterated continuously, inherit the user’s reach—often beyond what
Deepfake or synthetic identity
and targeting can expand from executives to any the role requires, and often without continuous 18%
attacks to bypass VPN authentication
user with remote access. In VPN environments, verification of device posture or behavioral
the outcome is the same: once an attacker signals. In that context, AI-powered social
0 10 20 30 40 50 60 70
obtains a valid credential, the VPN often treats engineering isn’t just another technique; it’s the
that identity as trusted and extends broad multiplier that makes credential compromise
Figure 3: Social engineering is the most-feared AI-driven attack technique targeting VPNs
connectivity into internal resources—turning a reliable, repeatable, and scalable.
single successful phish into a high-confidence
entry point.
One phished credential. Full access. To break that chain, authentication must shift from
a one-time perimeter event to a persistent control—continuously evaluating identity,
device posture, and behavior on every request, not just at login.
3. Microsoft, 2026. Storm-2561 uses SEO poisoning to distribute fake VPN clients for credential theft. March 2026.
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 55

When the initial foothold is the access layer itself, compensating controls sit downstream
The Response Window of the compromise. A patched concentrator prevents the foothold, but once exploitation
succeeds, containment depends on segmentation and inspection capabilities that this
Has Collapsed survey shows are weak across most environments. As long as remote access depends on a
customer-managed appliance, every organization remains one unpatched CVE away from
compromise. Removing the VPN concentrator from the equation eliminates one of the most
exposed patch surfaces in remote access.
Every VPN vulnerability starts the same clock. Only 6% of organizations can deploy a critical
But can defenders patch before attackers exploit? VPN patch within 24 hours. The majority, 54%,
In 2026, that race is over for most organizations. need a week or more. The CrowdStrike 2026
From the moment a critical VPN vulnerability is publicly disclosed, how long does it
Global Threat Report measured average eCrime typically take your organization to fully deploy patches across all VPN appliances?
In January 2025, a critical Ivanti VPN zero-day breakout time at 29 minutes in 2025, with the
Average eCrime breakout time: 29 minutes (CrowdStrike 2026)
(CVE-2025-0282) entered active exploitation fastest observed at 27 seconds.¹ For many
before any patch existed; CISA and Mandiant organizations, compromise occurs before their
Vendor-
confirmed that post-exploitation malware patch process clears the first approval gate. Less than 1–3 4–7 54% need a week managed
survived factory resets and firmware updates.⁴ 24 hours days days or more patching
Practitioners call it the CVE of the week: wake
That was one incident. By year’s end, three up to a CVSS 9.8 alert, scramble to deploy, do it 6% 15% 21% 28% 17% 9% 4%
Cisco ASA/FTD zero-days had been exploited again six days later. 56% rank patching as their
by a state-sponsored actor over five months, top operational challenge, and 61% acknowledge Only 6% can
1–2 2-4 +1
patch within weeks weeks month
a WatchGuard Firebox zero-day (CVE-2025- that vulnerabilities are weaponized faster than
24 hours
14733) had exposed 125,000 devices globally, fixes deploy. The defenders who spend the most
and Arctic Wolf had confirmed a sustained time patching are also the ones who know it will Figure 4: Patching Takes Weeks. Breakout Takes Minutes
SonicWall SSL VPN campaign with short never be fast enough.
intervals between initial access and ransomware
encryption. The cadence is no longer episodic; Zscaler ThreatLabz analyzed 411 VPN CVEs over
What challenges does your organization face with patching
it is continuous. five years and found 82.5% growth in annual
VPN vulnerabilities today?
volume, with 60% of the most recent year rated
high or critical. The vulnerability pipeline is Operational delays 65% Both exceed
structural, not episodic. the majority
Weaponized before patched 61% threshold
Vendor dependencies 46%
Slow vulnerability
37%
identification
0 10 20 30 40 50 60 70
Figure 5: Why Patching Never Catches Up
4. CISA, Emergency Directive 25-01: Mitigate Ivanti Connect Secure Vulnerabilities, January 2025; Mandiant, CVE-2025-0282 Analysis, January 2025.
1. CrowdStrike, 2026 Global Threat Report, February 2026. Multiple responses allowed
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 66

What the Tunnel
Hides
What percentage of the SSL/TLS (encrypted) traffic flowing through your VPN is
your organization currently able to fully inspect for malware and threats without
degrading performance?
Only 8% can
inspect virtually
everything
60%
inspect a quarter or less The same encrypted tunnel that protects a The entire chain crossed encrypted tunnels
legitimate session also shields every attack that no inspection layer examined. When 52%
33% 27% 19% 13% 8% that crosses it. Whether the appliance is fully describe their VPN as a transport layer with
patched or not. limited or no inspection capability, they are
No inspection 1%–25% 26%–50% 51%–75% 76%–100%
describing what the technology was built to do:
VPN was engineered to create encrypted systems performing according to design, in an
tunnels, and at that task it performs exactly environment that design never anticipated.
One-third inspect
nothing at all as designed. Encrypted transport has since
Figure 6: The Encrypted Blind Spot
become the primary delivery mechanism for One-third of organizations inspect zero
modern threats, and VPN is rarely configured, encrypted VPN traffic for threats. Add the
or in many cases capable, of inspecting what 27% examining less than a quarter, and 60%
the tunnel carries. Attackers embed payloads in of enterprises run remote access with minimal
SSL/TLS sessions, run command-and-control or no visibility into what crosses it. Only 8%
frameworks like Cobalt Strike through encrypted can inspect virtually everything. 83% rank
connections, and exfiltrate data through the ransomware through VPN tunnels as a top
same tunnels that carry legitimate traffic. The concern, yet 60% barely look at what’s inside
result is a blind spot that grows with every them. The gap is even wider for AI-enabled
A credential-stuffing bot, a C2 beacon, and a 3:00 encrypted session. Adversaries can hide inside threats: 70% report limited or no visibility into
AM exfiltration disguised as a file sync all cross “legitimate” encrypted traffic and adapt their AI attacks traversing VPN connections. The
the tunnel looking identical to legitimate traffic. techniques faster than legacy controls can detect organizations with the most to fear have the
The technology built to protect data in transit now 52% what’s moving through the tunnel. least ability to see it coming.
provides cover for every stage of an attack.
In January 2026, Huntress documented an
say their VPN is
Inspecting traffic inline at the point of access attack chain where a compromised SonicWall
just a pipe with
restores the visibility and control that encrypted VPN provided initial access, enabling the
no inspection
tunnels strip away. attacker to pivot through to VMware ESXi
capability
hypervisors using an exploit toolkit developed
over a year before disclosure.⁵
5. Huntress, SonicWall VPN to ESXi Attack Chain Analysis, January 2026.
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 77

Lateral Movement
Is the Multiplier
Once Attackers Get In
Organizations know lateral movement is a major risk,
but most still lack the controls to contain it after login
Initial access is rarely the end of the story, it’s Segmentation gaps make lateral movement
the beginning of expansion. With VPN-based easier to operationalize. 56% have no
remote access, a single authenticated session per-application segmentation through VPN,
often lands a user on the internal network, and 24% provide entirely open access after
turning one compromised credential into broad authentication. The result is a structural
reach across systems and services. mismatch: defenders may detect an intrusion,
but lack the access controls to contain it quickly.
The report shows how limited containment
still is in most environments: only 11% of That tension shows up clearly in priorities: 81%
81% 77%
organizations can restrict a compromised session flag lateral movement as a top concern, yet
to a single application. In 32% of environments, a 77% lack confidence in containing it. When
single stolen credential opens the entire network remote access grants network-level connectivity
and 14% can’t describe their own blast radius. instead of app-level containment, lateral
say lateral lack
movement becomes the multiplier that turns
Nearly half of enterprises can’t confidently one compromise into many. movement is confidence
predict what an attacker could reach after login.
a top containing
concern it once it
starts
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 88

The Hole In
the Firewall
If a threat actor successfully compromised a single remote user’s VPN credentials
today, how much of your network would they have access to?
Only 11% can
restrict
to a single 43%
The perimeter was supposed to be the hard 56% have no per-application segmentation application Subnet or segment
boundary. For most organizations, VPN turned through VPN, and 24% provide entirely open
it into an open door, and the uninspected traffic access after authentication. Almost everyone
46%
11%
documented earlier flows straight through it. who recognizes the threat also lacks the means
Single
to address it: 81% flagged lateral movement application wide open
or unknown
Networking teams have grown vocal about as a top concern, yet 77% lack confidence in
the irony: you spend millions on firewalls, then containing it.
14% Unknown blast radius 14% can’t
punch a giant, persistent hole in it for VPN to describe their
32% Entire network
own blast
listen on. Every VPN session passes through the Site-to-site connections amplify the exposure:
radius
perimeter, places the remote user directly on the 61% report limited or no visibility into traffic
internal network, and bypasses the inspection flowing across permanent tunnel links between
Figure 7: One Credential, Wide-Open Access
layers the organization spent years building. offices, data centers, and partner networks.
41% still route vendor and contractor
Only 11% can restrict a compromised session connections through this same infrastructure,
to a single application. In 32% of environments, typically granting the same access as employees.
a single stolen credential can open the entire Every one of these connections extends the
Does your VPN infrastructure enable app-level segmentation for different user groups?
network. Another 14% cannot describe their blast radius of a single breach.
own blast radius. Nearly half of all enterprises
App-level segmentation 13%
cannot predict what an attacker would reach
after login. Role/group-based 27%
56%
Network/subnet only 32%
have no per-application
Open after authentication 24%
segmentation
Other/Not sure 4%
0 10 20 30 40
In contrast, an access model that connects each session only to its intended application leaves a
Figure 8: Segmentation Stops at the Network Layer
compromised credential with nowhere to go.
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 99

One Credential,
Full Access
Composite — Attack risk, Architecture concern, Ransomware vector, Concern level
# 1 A C R O S S E V E R Y R I S K D I M E N S I O N
84%
In most breach investigations, the root cause AI has industrialized the supply side. Infostealer
70%
68%
lands in the same place: a stolen credential malware now harvests VPN credentials at scale,
63% 84% extreme
that opened the front door. VPN makes that feeding access broker marketplaces where
or significant
concern credential uniquely dangerous. verified logins are sold with bulk pricing and
customer service for ransomware affiliates.
Credential theft dominates every risk dimension In December 2025, GreyNoise detected a
the survey measured. As the greatest coordinated brute-force campaign targeting
Attack risk Ransomware Architecture Concern level
VPN attack risk, 63% named it first. As an Cisco SSL VPN and Palo Alto GlobalProtect
entry vector concern
architecture concern, 70% ranked it the top portals, with over 10,000 unique IPs probing
Figure 9: Credentials: #1 Across Every Risk Dimension threat. As a ransomware entry vector, 68% exposed authentication endpoints in a
Multiple responses allowed
placed it above all alternatives. 84% expressed single week.⁶
extreme or significant concern. No other finding
achieved that consistency. Dormant vendor accounts, provisioned months
Does your organization have processes in place to regularly audit application access
ago, never audited, still active, rank among the
rights for VPN users (including third parties)?
The reason is structural. VPN authenticates most valuable listings on access broker forums.
once at the perimeter and extends network Every unaudited credential is an open invitation
access from that single event. Anyone holding that never expires.
39%
a valid credential inherits whatever access the
43% 57%
legitimate user had, often far more than the role
No
Yes requires. Yet 57% of organizations do not audit
do not audit
the third-party access those credentials unlock.
or are unsure
18%
Not sure
Figure 10: Third-Party Access: Unaudited, Unmanaged Continuous identity verification - evaluating device posture and behavior on every request, not just at
the perimeter - transforms authentication from a single event into a persistent control.
6. GreyNoise Intelligence, Mass Exploitation Campaign Targeting VPN Portals, December 2025.
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 1100

Until every stage of that kill chain meets a control that stops it – continuous identity
verification, inline traffic inspection, per-session application access, and automated
Ransomware’s threat detection – the path from first credential to final payload stays clear.
Favorite Door
In your opinion, what is the primary weak point or entry vector for ransomware in
your VPN environment?
A ransomware operator needs three things: a way The survey data maps onto this kill
Credentials lead
in, room to move, and time to work. VPN provides chain precisely: broad access in 56% of Stolen credentials 68% every risk category
in this report
all three. environments, flat topologies in 32%,
Unpatched concentrators 59%
zero inspection in a third. 83% rank
The credential exposure and patching gaps documented ransomware through VPN as a top-tier No segmentation 53%
in this report converge here. Once inside, the attacker concern – yet 53% report no meaningful
Third-party access 50%
lands on a segment with access exceeding what the role segmentation to slow it down.
requires. Without meaningful segmentation, the pivot The concern is nearly universal; the
Unpatched connected systems 45%
from entry to encryption is unobstructed. capability to act on it barely exists.
Compromised endpoints 42%
The Fog ransomware group completed full chains from
0 10 20 30 40 50 60 70
VPN login to encryption in under two hours.⁷ A joint FBI
and CISA advisory confirmed Akira collected over $42
Figure 11: How Ransomware Gets In Through VPN
million from VPN exploitation campaigns; the group Multiple responses allowed
surged again in mid-2025 targeting SonicWall SSL VPN
devices.² Black Basta’s leaked internal communications
read like procurement documentation: vulnerabilities Under 2 hours from login to encryption
ranked by exploitability, credential pricing from access
brokers, target lists filtered by internet-facing portals.⁸
1 2 3 4
Multiple campaigns in 2024 and 2025 demonstrated
that implanted malware can survive reboots and
ENTRY LANDING MOVEMENT ENCRYPTION
firmware upgrades on VPN appliances, meaning Stolen Broad Flat topology No inspection
credential network enables lateral to detect
a compromised concentrator maintains access
or exploited access spread payload
indefinitely through a tunnel designed never to close. CVE
33%
56% 32%
inspect
lack per-app have flat
7. Arctic Wolf Labs, Fog Ransomware Campaign Analysis, 2025. Full chain from
VPN login to encryption in under two hours. segmentation network access nothing
2. FBI and CISA, Joint Cybersecurity Advisory: Akira Ransomware, April 2024.
$42M+ in proceeds from VPN-based campaigns.
8. Black Basta internal communications leaked in February 2025;
analyzed by multiple threat intelligence vendors. Figure 12: The VPN Ransomware Kill Chain
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 1111

The Operational
VPN now creates more
Tax exposure through workarounds
than it prevents through
protection. That is no longer
a security problem; it is an
operational failure.
Beyond the security risks, VPN imposes an operational cost that adds
up quietly in help desk tickets, user frustration, patching cycles, and the
workarounds that emerge when the sanctioned access path becomes
the slowest one available.
63% report that users intentionally bypass VPN controls to reach
applications faster. When nearly two-thirds of the workforce
What is the most common complaint your How frequently do users attempt to bypass or work
routes around the security perimeter, every bypassed session flows
users have regarding VPN access today? around VPN access controls to access applications faster?
uninspected and unmonitored. Controls that users consistently route
around do not meaningfully reduce risk.
73%
The bypass has roots in measurable friction. Slow connections top trace to performance 21% 12%
Frequently Unsure
the complaint list at 30%, followed by inconsistent device behavior at
30% Only 7% say users
23% and frequent disconnections at 20%. All three are performance
never bypass
Slow connection speeds
problems, accounting for 73% of complaints. Forty-five percent report
significant or major productivity impact. These are real costs: delayed 23%
63% 7%
projects, missed collaboration windows, frustrated employees working Inconsistent performance across devices/locations
Never
around their own security tools.
20% bypass VPN to
reach apps
Frequent disconnections 18%
Security teams spend more time maintaining VPN than defending what faster Rarely
sits behind it. 73% say VPN demands more operational effort than 15%
modern alternatives. The top drivers: patching complexity (56%) and Authentication difficulties
integration struggles with modern security stacks (50%). As one survey
12%
respondent put it, more time goes to patching the entry point than
Complex VPN setup or configuration
42%
securing the actual data behind it.
Occasionally
Figure 13: What Users Complain About Most Figure 14: 63% of Users Route Around VPN
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 1122

When standard recovery fails and the government orders disconnection, the security
device itself has become the threat – ordered off the network it was purchased
Nation-States to protect.
Inside the Perimeter Against adversaries with nation-state capability, the only viable defense is an
architecture that never exposes the appliance in the first place.
VPN has become a national security concern. The CrowdStrike 2026 Global Threat Report Has your organization experienced a security incident related to VPN vulnerabilities in
The campaigns disclosed in 2024 and 2025 found that 40% of vulnerabilities exploited by the past 12 months?
made that clear. China-nexus actors targeted edge devices such
as VPNs, firewalls, and gateways.¹
Volt Typhoon, confirmed by CISA and
51% 35%
multiple intelligence agencies, targeted In this survey, 51% of organizations reported 51%
No
critical infrastructure across communications, a VPN-related security incident in the past
Yes
energy, transportation, and water sectors, twelve months – a figure that spans every experienced a
14% are not
maintaining access within some networks for sector, not just the critical infrastructure these VPN-related
14% sure — the
security incident
years before discovery.9 Salt Typhoon achieved campaigns targeted. real number
Not sure
in the past
deep penetration of U.S. telecommunications may be higher
12 months
providers, compromising the lawful intercept CISA issued consecutive emergency directives
systems used by law enforcement. The FBI in January 2024 and January 2025, ordering Figure 15: Half Breached in the Past Year
characterized it as one of the largest intelligence federal agencies to disconnect affected
compromises in American history.10 appliances after malware proved capable of
surviving factory resets and firmware updates.¹²
These were not isolated incidents. A China-
The Cadence of Nation-State VPN Exploitation
aligned group designated UAT4356 exploited
three Cisco ASA/FTD zero-days from May
January Early January May–Sep 2024–
through September 2025, targeting government
2024 2025 2025 2025 2025
networks worldwide with firmware-level
persistence that survived reboots and upgrades.¹¹
Additional Chinese state-sponsored groups
exploited Ivanti VPN zero-days throughout early
CISA Emergency Chinese CISA Advisory on UAT4356 Volt Typhoon
2025, deploying malware designed to persist
Directive 24-01 state-sponsored CVE-2025-0282 exploits three and Salt
despite standard remediation. orders Ivanti groups exploit malware survives Cisco ASA/FTD Typhoon
appliance Ivanti VPN factory resets zero-days campaigns
disconnection zero-days targeting confirmed
government across critical
9. CISA, Advisory on Volt Typhoon, multiple releases 2024–2025; confirmed by FBI, NSA, and Five Eyes intelligence partners
10. FBI Director Christopher Wray, Congressional testimony on Salt Typhoon telecommunications compromise, 2024. networks infrastructure
11. Cisco Talos, ArcaneDoor Campaign Disclosure (UAT4356), September 2025. Three ASA/FTD zero-days exploited from May–September 2025.
1. CrowdStrike, 2026 Global Threat Report, February 2026.
12. CISA, Emergency Directive 24-01 (January 2024) and CISA Advisory on CVE-2025-0282 (January 2025).
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 1133

The Clock
Is the Risk
Every finding in this report reduces to one variable: time.
Time to patch, time to detect, time to contain.
Only 6% can patch a critical VPN vulnerability within
24 hours, while 79% say their top AI-driven risk is
attackers weaponizing vulnerabilities faster than patches
can be deployed. The exposure window is structural,
not temporary.
With 38% transitioning and 34% planning zero trust,
6% 29
hybrid access will persist for years. During that
coexistence period, broad network exposure remains
in production. min
The priority is speed of containment: shrinking reachable
surface area, enforcing per-application access, can patch average
and restoring inspection at the point of connection.
within breakout
A CISA-aligned readiness assessment quantifies how
24 hours time
much exposure remains. The decisive question is
whether your access architecture can contain the next
compromise before it spreads.
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 1144

From Reactive
To Resilient
Eliminate broad
network access
32%
flat access
Networks
open
24%
connectivity
Most organizations in our survey placed themselves in the Reactive column These four changes define the shortest path from Reactive to Resilient.
across every dimension. That position is not sustainable when breakout times are Each maps to a CISA zero trust pillar and is ordered by impact.
measured in minutes and AI-enabled attacks are reported by 61% of respondents.
Make authentication
continuous
68% credentials top
ransomware vector
1. First: Eliminate broad network access (Networks): 3. Third: Inspect all traffic inline (Applications & Workloads):
Identity
57%
never audit
32% still grant flat network access after authentication, and 24% provide One-third inspect zero encrypted VPN traffic, and 60% inspect a quarter or
effectively open connectivity. Shifting to an access model that connects less. Without inspection, every session is a potential channel for malware,
each session only to its intended application is both an architecture C2, and exfiltration. Inline inspection at the access layer restores the
change and a segmentation fix in a single step: it collapses blast radius for visibility that encrypted tunnels strip away and makes applications invisible
credential compromise and sharply reduces lateral movement pathways. to unauthorized discovery.
Least-privilege access is foundational, not a later phase. It directly
Inspect all
traffic inline
addresses the risk that 67% cite as their primary reason for adopting
zero trust. 4. Fourth: Automate detection and response (Visibility & Analytics): 33%
inspect zero
Applications
24% deploy AI-powered monitoring today, yet 61% have encountered AI-
& Workloads 60%
inspect ≤25%
enabled attacks. Over half say legacy VPN infrastructure blocks integration
2. Second: Make authentication continuous (Identity): of AI-driven security tools entirely. An access model built for automated
68% identify credentials as the top ransomware entry vector, yet most VPN detection and response removes the integration barriers that keep most
architectures validate identity once and never again. Fifty-seven percent organizations blind to the fastest-moving threats.
do not audit third-party VPN access or are unsure whether audits occur.
Continuous verification that evaluates identity, device posture, and behavior
Automate detection
and response
on every request transforms authentication from a single checkpoint into a
have AI
persistent control – closing the gap that credential-based attacks exploit. 24%
monitoring
Visibility
& Analytics 61% face AI
attacks
None of these changes require perfection across every dimension at once. Each one independently narrows the gap an attacker can exploit, and every week of delay
keeps the full gap open.
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 1155

Is your organization actively transitioning away from VPNs toward a Zero Trust security model?
Zero Trust
The Execution Gap
Only 6%
have no
50% plans
transitioning or completed
12% 38% 21% 13% 10% 6%
The strategic debate over whether Better segmentation at 58% and
No plans to move beyond VPN is effectively ransomware protection at 53%
settled. The hard part now is complete the picture. The alignment
Fully Currently Planning Planning Evaluating,
transitioned transitioning within 12 within 1–2 no firm execution: how fast organizations can between what organizations fear and
months years timeline
transition, and how much exposure what drives their migration to zero
accumulates during coexistence. trust is nearly exact.
84%
Planning or further
VPN usage is declining in 51% of Zero trust is a journey, and most
organizations, and only 10% report an enterprises will operate hybrid
Figure 16: 84% Are Moving Beyond VPN
increase. Half are actively transitioning access environments for years as
to zero trust or report completion, and they migrate high-risk workforce
another 34% are in formal planning. access first while legacy VPN use
Across three consecutive surveys, the cases persist. The practical objective
Steady acceleration across three years
share at least planning zero trust has is to reduce exposure in measurable
grown from 78% to 81% to 84%. steps by shrinking reachable network
2024 2025 2026
Only 6% report no plans. surface area and limiting blast radius
during coexistence.
78% 81% 84%
The drivers map directly to this
report’s findings. Eliminating lateral
movement leads at 67% – the same
threat that 81% identified as a top
Three consecutive surveys
concern and 77% cannot contain.
Operational overhead reduction
follows at 62%.
The contrast is architectural. VPN authenticates once and exposes the network. Zero trust verifies
continuously and connects each session only to a single application, keeping the internal network
unreachable. At its core, it’s the shift from putting users on the network to connecting them only
to the specific app they need.
Zscaler ThreatLabz 2026 VPN Risk Report ©2026 Cybersecurity Insiders. All Rights Reserved. 1166

VPN to Zero Trust:
Zero Trust Readiness Matrix
Readiness Assessment  (aligned to CISA Zero Trust Maturity Model v2.0)
| DIMENSION (CISA Pillar) |                                 | REACTIVE | TRANSITIONING         | RESILIENT              |
| ----------------------- | ------------------------------- | -------- | --------------------- | ---------------------- |
|                         | THE MAJORITY IS HERE            |          | MFA and periodic      | Continuous             |
|                         | Single login grants persistent  |          | reauthentication for  | verification on every  |
AI has compressed attack timelines across every dimension of
|     | access. 68% cite credentials  |     | some applications;  | request; adapts  |
| --- | ----------------------------- | --- | ------------------- | ---------------- |
enterprise security. Credential harvesting, exploitation, east-west
Identity
|     | as top ransomware vector;  |     | third-party access  | to identity, device  |
| --- | -------------------------- | --- | ------------------- | -------------------- |
movement, and exfiltration all operate faster than just twelve months
|     | 57% never audit third-party  |     | audited annually | posture, and behavior |
| --- | ---------------------------- | --- | ---------------- | --------------------- |
ago. The readiness question is whether your infrastructure can
access
operate at the speed these threats now demand.
This assessment is structured around the CISA Zero Trust Maturity
|     | Broad network access post- |     | Zone or role-based  | Each session  |
| --- | -------------------------- | --- | ------------------- | ------------- |
Model v2.0, scoped to the access risks this survey measured. Two
|     | auth; flat topology.  |     | segmentation;  | connects to one  |
| --- | --------------------- | --- | -------------- | ---------------- |
CISA pillars, Devices and Data, fall beyond this survey’s scope;  Networks 56% lack per-app controls;  sessions not yet  application only;
organizations should assess those independently. The three maturity  77% cannot contain lateral  isolated lateral movement
|     | movement |     |     | eliminated by default |
| --- | -------- | --- | --- | --------------------- |
stages align to the progression CISA describes from Traditional
through Optimal. In every dimension, the majority of respondents fall
in the Reactive tier. The lowest-rated dimension typically represents
|     | Little or no encrypted traffic  |     | Some encrypted  | All traffic inspected  |
| --- | ------------------------------- | --- | --------------- | ---------------------- |
the fastest path an attacker will take.
|     | inspection; apps reachable  |     | inspection; manual  | inline in real time;  |
| --- | --------------------------- | --- | ------------------- | --------------------- |
Applications
|     | by anyone on-network.  |     | anomaly review | apps invisible to  |
| --- | ---------------------- | --- | -------------- | ------------------ |
For each dimension, identify which column most closely describes
|     | 60% inspect ≤25% of traffic;  |     |     | unauthorized users |
| --- | ----------------------------- | --- | --- | ------------------ |
& Workloads
your current operational state – not your planned state or your
70% blind to AI threats in
policy, but what is enforced in production today.
VPN
Many organizations will find themselves in the Reactive column
across multiple dimensions. That honest placement is the starting
|     | No automated detection;  |     | Known-pattern  | Automated detection  |
| --- | ------------------------ | --- | -------------- | -------------------- |
point for prioritization.
|     | legacy infra blocks  |     | detection; manual  | and response;  |
| --- | -------------------- | --- | ------------------ | -------------- |
Visibility
|     | modern tools. 76% lack AI  |     | investigation and  | telemetry feeds  |
| --- | -------------------------- | --- | ------------------ | ---------------- |
The next page maps the four changes that move each dimension
& Analytics
|     | monitoring; 51% blocked by  |     | response | continuous policy  |
| --- | --------------------------- | --- | -------- | ------------------ |
from Reactive to Resilient, ordered by impact.
|     | legacy VPN |     |     | refinement |
| --- | ---------- | --- | --- | ---------- |
The lowest-rated dimension typically represents the fastest path an attacker will take.
Zscaler ThreatLabz 2026 VPN Risk Report   ©2026  Cybersecurity Insiders.  All Rights Reserved. 1177

Predictions For
2026 And Beyond
| 1   | 2   | 3   | 4   | 5   |
| --- | --- | --- | --- | --- |
Credential  Attackers optimize  MFA, resets, and  Patch velocity  Defenders shift
theft becomes  for machine-  help desk flows  won’t match  to continuous
a default VPN  speed time-  become the new  exploitation  verification—and
intrusion path.   to-compromise. frontline.  velocity.  away from VPN.

AI will continuously refine  AI-assisted social  AI-assisted scanning  Organizations will move
AI-generated phishing/
social engineering will  exploit targeting and follow- engineering will target  and exploitation will  from “authenticate once”
on actions to compress the  push fatigue, one-time  shorten the time  perimeter trust to per-
outpace exploitation
because “log in” is  window from first contact  codes, device enrollment,  between disclosure and  request checks (identity,
|                       | to valid VPN access—from  | and password reset  | compromise attempts,       |     |
| --------------------- | ------------------------- | ------------------- | -------------------------- | --- |
| faster, quieter, and  |                           |                     | device posture, behavior)  |     |
more reliable than  days to hours, increasingly  workflows as aggressively  widening the gap for  and least-privileged user-
|             | minutes. | as passwords. | organizations with slower            |     |
| ----------- | -------- | ------------- | ------------------------------------ | --- |
| “break in.” |          |               | to-app access to survive             |     |
|             |          |               | patch cycles. machine-speed attacks. |     |
18

How Zscaler Transforms
Secure Access
|                                          |                                   |     | Public | Data   | Legacy |
| ---------------------------------------- | --------------------------------- | --- | ------ | ------ | ------ |
|                                          |                                   |     | Cloud  | Center | Apps   |
| If time is the risk, then secure access  | ZPA supports the broadest set of  |     |        |        |        |
On-Prem
| has to reduce time everywhere it  | private access use cases from managed  |     |     |     |     |
| --------------------------------- | -------------------------------------- | --- | --- | --- | --- |
VCP
VMs (VMware, Nutanix)
| matters: time to expose services, time  | and unmanaged (BYOD) devices to  |     |     |     |     |
| --------------------------------------- | -------------------------------- | --- | --- | --- | --- |
App
Cloud
AC
to move laterally, and time to contain.   in-office users, third-party  Connector AC NC
AWS, Azure, GCP
App-layer access,
| Legacy VPN does the opposite. It  | contractors, and privileged access  |     |     |     |     |
| --------------------------------- | ----------------------------------- | --- | --- | --- | --- |
Container
outbound-only,
| extends the network to the user,  | (RDP, SSH, VNC) without reintroducing  | Docker, KBs, OpenShift |     |     |     |
| --------------------------------- | -------------------------------------- | ---------------------- | --- | --- | --- |
TLS connections
| broadens the attack surface, and turns  | a flat network. Built to deliver Zero   |     |     |     |     |
| --------------------------------------- | --------------------------------------- | --- | --- | --- | --- |
| a single credential compromise into a   | Trust Everywhere at scale, it provides  |     |     |     |     |
Network Connector
pathway for lateral movement.   consistent security and performance  Inside-out tunnel.
IP-to-IP comms - no
| Zscaler Private Access (ZPA), the  | across branch, home, and cloud on a  |     |     |     |     |
| ---------------------------------- | ------------------------------------ | --- | --- | --- | --- |
inbound traffic needed
| industry’s first AI-powered ZTNA,  | unified platform for users, workloads,  |     |     |     |     |
| ---------------------------------- | --------------------------------------- | --- | --- | --- | --- |
replaces network-level access with  and OT devices, backed by 160+  Inline Threat Protection
Zero Trust
direct user-to-application  global data centers. And because  TLS inspection, malware,
Exchange
anomalies, URL filtering,
| connectivity. Applications are made  | fast attacks require fast containment,  |     |     |     |     |
| ------------------------------------ | --------------------------------------- | --- | --- | --- | --- |
sandboxing, IPS, DLP No Public IPs
| invisible behind the Zero Trust  | ZPA adds inline inspection plus  |     |     |     |     |
| -------------------------------- | -------------------------------- | --- | --- | --- | --- |
Business Policy
| Exchange, and Autonomous            | integrated AppProtection, deception,   |     |     |     |     |
| ----------------------------------- | -------------------------------------- | --- | --- | --- | --- |
| User-to-App Segmentation enforces   | and rapid deployment and scaling so    |     |     |     |     |
| least-privilege access by default,  | organizations can reduce exposure and  |     |     |     |     |
Micro Tunnels
| collapsing blast radius and helping  | improve resilience during the hybrid  |     |     |     |     |
| ------------------------------------ | ------------------------------------- | --- | --- | --- | --- |
Specific apps - no
eliminate lateral movement. transition years. lateral movement
Dynamic Policy Evaluation
Identity (SAML/SCIM) and
context (device posture,
ZC
geolocation, etc.)
Remote
Users
ZZssccaalleerr  TThhrreeaattLLaabbzz  22002266  VVPPNN  RRiisskk  RReeppoorrtt   ©2026  Cybersecurity Insiders.  All Rights Reserved. 1199

Key Differentiators Of Zscaler Private Access (ZPA) Why Zscaler Private
Access (ZPA)?
• Built from the ground up for least-privileged access • Accelerate M&A/Divestiture
Connect users to approved apps—not the network— Integrate or separate access quickly—
with policy-based access by default. without merging networks. Minimize Attack Surface
• Minimize the attack surface and lateral movement • Reduce operational complexity Applications are invisible to the network making
Keep apps invisible and contain risk with Replace VPN/VDI/firewalls with a cloud-native them impossible to discover or attack.
user-to-app segmentation. access service.
• Full inline inspection • Automated business continuity
Block threats and protect data with inline inspection Maintain policy-enforced access through Boost Productivity
and integrated DLP. outages and disruptions.
Fast, direct access from 160+ PoPs worldwide with
• Universal ZTNA • Centralized policy enforcement no traffic backhauling.
Deliver consistent access to any app (including legacy) Apply one policy model to all apps for remote
from anywhere. and in-office users.
• Boost workforce productivity • Cloud-delivered solution Reduce Total Cost of Ownership (TCO)
Provide fast, direct access—no backhauling through Connect users directly to apps without routing
the data center. through the data center. Consolidate VPNs, firewalls, and load balancers
into a single cloud-native platform.
• Secure B2B connectivity • 160+ global cloud edge locations
Give partners on-demand, zero-trust access— Deliver secure, local access with consistent
without added infrastructure. performance worldwide.
ZZssccaalleerr TThhrreeaattLLaabbzz 22002266 VVPPNN RRiisskk RReeppoorrtt ©©22002266 CCyybbeerrsseeccuurriittyy IInnssiiddeerrss.. AAllll RRiigghhttss RReesseerrvveedd.. 222000

Methodology &
Demographics
This report is based on a comprehensive survey of 822 IT
and cybersecurity professionals conducted in early 2025 by
Cybersecurity Insiders in partnership with Zscaler ThreatLabz.
The research examines how organizations are addressing the
intersection between AI-accelerated threats and traditional
perimeter-based access, encompassing VPN vulnerability
Career Level
exposure, lateral movement risk, and readiness for zero trust
|     | 24% |     |     | 18% |     | 13% |     | 9%  | 8%  | 6%  | 3%  |     | 19% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
migration. Respondents were screened for direct operational
or strategic responsibility over their organization’s network
| Manager/   |     | Specialist/  |     | Director | Vice      |     | Consultant |     | CTO,CIO,CISO, |     | Founder/CEO/  |     |     | Other |
| ---------- | --- | ------------ | --- | -------- | --------- | --- | ---------- | --- | ------------- | --- | ------------- | --- | --- | ----- |
| Supervisor |     | Coordinator/ |     |          | President |     |            |     | CMO,CFO,COO   |     | President     |     |     |       |
access architecture. Using a stratified sampling approach,
Analyst
the survey achieved a 95% confidence level with a margin
Department of error of +/- 3.4%.
|     |     | 42% |     |     |     |     | 21% |     | 9%  | 7%  | 6%  | 3%  | 12% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IT Security IT Operations Infrastructure Network Engineering Product  Note on terminology: Throughout this report, “AI-enabled attack” refers to
Other
Management adversary activity where responders observed either automation-driven
speed/scale consistent with AI augmentation or direct use of AI-generated
content in social engineering. Confirmed and suspected incidents are
Company Size
reported separately.
|              |     | 38% |     |     |               |     | 36% |     |     |           |     | 26% |     |     |
| ------------ | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
| 1,000-5,000  |     |     |     |     | 5,001-20,000  |     |     |     |     | >20,000   |     |     |     |     |
| employees    |     |     |     |     | employees     |     |     |     |     | employees |     |     |     |     |
©2026 Cybersecurity Insiders. All rights reserved.
Industry
Limited editorial citation (up to 100 words and one unaltered chart) is
permitted with clear attribution to “Cybersecurity Insiders, 2026 VPN Risk
19% 16% 14% 11% 7% 6% 5% 4% 18% Report” and a visible link to cybersecurity-insiders.com.
The report sponsor may reference the findings and use individual charts or
| Computers,  | Financial  |     | Healthcare,  |     | Government | Manufacturing |     | Energy  |     | Professional  |     | Telecommu- |     | Other |
| ----------- | ---------- | --- | ------------ | --- | ---------- | ------------- | --- | ------- | --- | ------------- | --- | ---------- | --- | ----- |
data points in presentations and marketing materials with proper attribution.
| Software,  | Services |     | Pharmaceuticals  |     |     |     |     | & Utilities |     | Services |     | nications |     |     |
| ---------- | -------- | --- | ---------------- | --- | --- | --- | --- | ----------- | --- | -------- | --- | --------- | --- | --- |
The full report, underlying dataset, and research methodology remain the
| Technology |     |     | & Biotech |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
intellectual property of Cybersecurity Insiders and may not be reproduced,
redistributed, or incorporated into derivative research without written
permission.
This report was produced by Cybersecurity Insiders with the support of
Zscaler. Permissions: info@cybersecurity-insiders.com
Zscaler ThreatLabz 2026 VPN Risk Report   ©2026  Cybersecurity Insiders.  All Rights Reserved. 2211

BENCHMARK YOUR SECURITY MATURITY
Independent cybersecurity research revealing the gaps
that shape cybersecurity strategy
Cybersecurity Insiders produces independent research based on
surveys of cybersecurity leaders and practitioners worldwide. Our
reports reveal where security strategies break down in practice —
helping organizations benchmark their maturity, identify capability
gaps, and prioritize the actions needed to close them.
For more information, visit
cybersecurity-insiders.com

Zero Trust Everywhere
About Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so customers can be more agile, efficient, resilient, and
secure. The Zscaler Zero Trust Exchange™ platform protects thousands of customers from cyberattacks and data
loss by securely connecting users, devices, and applications in any location. Distributed across more than 160 data
centers globally, the SSE-based Zero Trust Exchange™ is the world’s largest in-line cloud security platform. Learn
more at zscaler.com or follow us on X @zscaler.
© 2026 Zscaler, Inc. All rights reserved. Zscaler™ and other trademarks listed at zscaler.com/legal/trademarks are either (i) registered
trademarks or service marks or (ii) trademarks or service marks of Zscaler, Inc. in the United States and/or other countries. Any other
trademarks are the properties of their respective owners.
+1 408.533.0288 Zscaler, Inc. (HQ) • 120 Holger Way • San Jose, CA 95134 zscaler.com
Zscaler ThreatLabz 2026 VPN Risk Report March 2026 | Version 2.0 23

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-28", "model": "gemini-3.5-flash-lite"} -->
