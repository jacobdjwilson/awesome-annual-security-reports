# Cloudflare Threat Report 2026

## Table of Contents
- [Executive summary](#executive-summary)
- [Key findings for 2026](#key-findings-for-2026)
- [Emerging attack techniques and trends](#emerging-attack-techniques-and-trends)
- [Nation-state analysis](#nation-state-analysis)
- [Cybercrime](#cybercrime)
- [Community and regional perspectives](#community-and-regional-perspectives)
- [Recommendations](#recommendations)

---

## About Cloudforce One
Driven by a mission to help defend the Internet, Cloudforce One leverages telemetry from Cloudflare’s global network — which protects approximately 20% of the web — to drive threat research and operational response, protecting critical systems for millions of organizations worldwide.

## Executive summary
The Internet was built on trust and interoperability, but its architects never anticipated the adversaries who would weaponize those very principles against it.

Every single day, Cloudflare’s network is the first line of defense against more than 230 billion threats. Threat actors are moving with the same speed and sophistication as defenders, leaving no room for error in a neck-and-neck battle for the network.

But Cloudflare doesn’t just react to these threats; we predict and interdict them. By processing over 20% of the world’s Internet traffic, we see the first tremors of an attack before they become a global earthquake and distill patterns across our network to help us anticipate and plan for future disruption. This unmatched visibility allows us to turn raw data into proactive defense.

The 2026 threat landscape is poised to reward the stealthy over the loud, and organizations need to know the threats in order to thwart them. To meet this moment, Cloudforce One has spent the last year translating trillions of network signals and threat actor tactics, techniques, and procedures (TTPs) into the insights and recommendations organizations need to prepare for and execute actionable defense. The inaugural Cloudflare Threat Report is the result of this work.

Our unmatched global telemetry has made the verdict clear: In 2026, we are witnessing the total industrialization of cyber threats, where the barrier to entry has vanished and the “interactive hack” is now a scalable and automated model.

The collapse of the traditional perimeter has turned identity into the primary target, while the explosion of AI and SaaS-to-SaaS complexity has given attackers a force multiplier to move through networks at machine speed. From hyper-volumetric DDoS strikes that paralyze infrastructure to the silent infiltration of corporate payrolls, the 2026 landscape is defined by a shift from brute force to high-trust exploitation.

Our team specializes in turning global signals and critical network interconnections into actionable defense insights, even when direct command and control signals are obscured or unavailable. With the launch of the Cloudflare Threat Report, we’re leveraging this unique visibility of our world-renowned threat researchers to arm security teams with the context they need to make confident decisions for tactical success.

The report provides key perspectives that can make the difference between security and failure at the edge. The adversaries have evolved beyond the network’s original design; our defenses must now do the same.

## Key findings for 2026

### AI is automating high-velocity attacker operations
The primary metric for risk in 2026 is the Measure of Effectiveness — the ratio of attacker effort to operational outcome. The accessibility of generative AI significantly lowers the barrier to entry for highly effective operations, moving the industry beyond technically elegant code to “offense by the system.” By leveraging a victim’s own cloud, software as a service (SaaS), and AI infrastructure to fund and scale missions, adversaries are achieving a level of frictionless scale that traditional risk models fail to capture.

### State-sponsored pre-positioning is compromising critical infrastructure resilience
Chinese threat actors, notably Salt Typhoon and Linen Typhoon, are prioritizing North American telecommunications, government, and IT services for persistent pre-positioning. This strategic targeting suggests a deliberate shift toward preparing for future disruptive events over immediate espionage. By embedding footholds within core infrastructure, adversaries are eroding the foundational resilience of essential public and private sector services, anchoring their presence for long-term geopolitical leverage.

### Over-privileged SaaS integrations are expanding the blast radius of attacks
The security of corporate data is now defined by third-party integrations rather than the traditional network perimeter. In 2026, a single over-privileged SaaS-to-SaaS connection can be weaponized via AI to trigger surgical, multi-tenant breaches across entire ecosystems simultaneously. This structural vulnerability turns the “connective tissue” of modern enterprises into a primary vehicle for widespread and automated operational disruption.

### Adversaries are subverting service ecosystems to mask attacks
Threat actors are weaponizing legitimate cloud ecosystems (SaaS, IaaS, and PaaS) to camouflage malicious actions within benign enterprise operations. In 2026, the use of trusted platforms for encrypted command delivery has matured into a standardized obfuscation layer within broader, multi-stage hybrid infrastructures. This democratization of scalable, high-bandwidth cloud resources allows even low-tier actors to execute sophisticated attacks that bypass traditional egress filtering.

### Deepfake personas are embedding adversarial operatives within Western payrolls
The industrialization of fraudulent identities now allows state-sponsored operatives to embed themselves directly into Western payrolls. These actors leverage deepfake profiles and remote laptop farms to maintain a residency illusion that evades geolocation and identity controls. This infiltration turns the remote workforce into an attack vector, placing malicious insiders within the organization’s most trusted administrative and financial systems.

### Token theft is neutralizing multi-factor authentication
Adversaries are neutralizing standard multi-factor authentication (MFA) by transitioning from “attacking the box” to “attacking the session.” Using infostealers like LummaC2, attackers actively harvest live session tokens to capture already-authenticated states and bypass perimeter controls. This shift has turned ransomware into a simple login event, where attackers exploit fragmented identity estates to move laterally without triggering the credential alerts once relied upon for detection.

### Relay blind spots are enabling internal brand spoofing
Attackers are exploiting a critical blind spot where mail servers fail to reverify a sender’s identity after a message passes through a third-party gateway. Because the traffic arrives from a “trusted” relay, the system incorrectly treats external spoofed messages as internal or safe. This allows phishing-as-a-service bots to bypass standard protection and deliver high-trust brand impersonations directly to user inboxes by abusing fragmented mail authentication.

### Hyper-volumetric strikes are exhausting infrastructure capacity
Hyper-volumetric distributed denial-of-service (DDoS) attacks, fueled by massive botnets like Aisuru, have established a record-breaking 31.4 Tbps baseline that physically exhausts most organizations’ network capacity. These autonomous strikes peak in seconds, effectively closing the window for human intervention and placing an extreme resource tax on local infrastructure.

## Emerging attack techniques and trends
As we look toward the threat landscape of 2026, the industry must undergo a fundamental shift in how it categorizes risk. For decades, the “sophistication” of an adversary — the technical elegance of their code or the novelty of their zero-day — was the primary barometer for danger. Today, that metric is being replaced by a more pragmatic calculation: the Measure of Effectiveness (MOE).

MOE evaluates a threat by the ratio of attacker effort to operational outcome. In layman's terms, it is a measure of “bang for the buck” — where a high-MOE attack achieves maximum disruption with minimum cost. For example, rather than spending millions to develop a custom exploit, a 2026 adversary might use a low-cost GenAI subscription to automate credential harvesting across thousands of targets. This model measures velocity from initial access to exfiltration and the frictionless scale that attackers leverage to target hundreds of victims at once.

### MOE in the SaaS supply chain: Weaponizing connective tissue
Cloudforce One has observed an escalation in attacks targeting the connective tissue of the modern enterprise: the integrations between third-party SaaS platforms. Most notably, through our investigation into the threat actor GRUB1, we have seen how a single compromise of a trusted integration — such as the Salesloft Drift connection to Salesforce — can create a dangerous ripple effect, cascading through entire ecosystems to expose hundreds of corporate tenants simultaneously.

The GRUB1 campaign demonstrates that unsophisticated, individual actors can now execute high-impact breaches by industrializing two key phases of the attack:
- **Automated credential discovery**: Moving from manual guessing to automated scanning of the SaaS supply chain.
- **AI-assisted navigation**: Using large language models (LLMs) to bridge knowledge gaps in specialized software like Salesforce, allowing attackers to locate and exfiltrate sensitive data with surgical precision.

### MOE in AI: From productivity tool to automated exploit vector
The meteoric rise of AI LLMs has introduced a dual-front risk that blurs the line between a productivity tool and a primary threat vector. On one front, there is the unwitting user risk: The unprecedented adoption rate among consumers and enterprises means that vast quantities of proprietary source code, financial details, and personally identifiable information (PII) are being routinely funneled into these systems. On the opposing front is the malicious threat: the reality that this same technology serves as a force multiplier for attackers.

![Deconstructing the OpenCode exploit chain through vulnerability analysis]

### MOE in cloud resources: Living off the XaaS (LotX)
The pervasive adoption of anything-as-a-service (XaaS) — including SaaS, infrastructure-as-a-service (IaaS), and platform-as-a-service (PaaS) — by organizations globally has been mirrored by nearly all threat actors. Cybercriminals, nation-states, and individual hackers now routinely leverage public cloud hyperscaler resources like Amazon Web Services (AWS), Google Cloud Platform (GCP), and SaaS offerings, blending their activities into the massive volume of legitimate cloud traffic.

### The industrialization of insider threats
The Cloudforce One team continues to analyze the critical evolution in state-sponsored insider threats through mapping the industrialization of North Korean remote IT worker schemes. These operatives infiltrate Western organizations by leveraging fraudulent identities and AI-driven deepfakes to bypass video interviews, ultimately funneling hundreds of millions of dollars in revenue back to the regime.

## Nation-state analysis
The modern threat landscape from state and state-aligned actors is increasingly defined by the maturation and tactical synchronization of cyber operations with kinetic and geopolitical objectives. Cloudforce One has observed four primary state actors — Russia, China, North Korea, and Iran — as they continue to refine a toolkit that extends far beyond simple cyber espionage.

### Russia: Blurring the line between digital espionage and operational support
The Russian cyber threat continues to operate under a high-frequency, broad targeting model. Groups like NastyShrew maintain their established practice of leveraging high-reputation cloud services to mask C2 infrastructure and employing geofencing to evade global security scanners.

### China: A sophisticated model of infrastructure pre-positioning and cloud-native stealth
China’s cyber strategy continues to evolve beyond traditional bulk data theft to a sophisticated model of infrastructure pre-positioning and cloud-native stealth. While groups like ClumsyToad maintain high-frequency regional espionage, the broader apparatus increasingly prioritizes the long-term compromise of critical edge devices and telecommunications backbones.

### North Korea: Identity-driven infiltration and analytical parasitism
In 2025, North Korea continued to double down on its established strategy of human-centric operations, augmenting traditional infrastructure exploitation with a more aggressive and industrialized weaponization of identity and trust.

### Iran: High-level credential theft and lateral movement via compromised government infrastructure
In general, Iran tightly integrates digital espionage with kinetic military objectives. By leveraging a human-in-the-loop social engineering model and weaponizing the inherent trust in regional government communications, Iranian actors aim to achieve high-precision intelligence gathering in support of military operations.

## Cybercrime
From record-breaking DDoS attacks peaking at an unprecedented 31.4 Tbps to the identification of over $123 million in explicit financial lures, cybercriminals in 2025 demonstrated a relentless move toward high-velocity, automated exploitation.

### The phishing factory: From low-friction links to industrialized supply chain sabotage
Technical signals from Cloudflare’s Email Security product provide insight into threat actor behavior. We observed that link-based phishing remains the dominant threat vector, favored by both opportunistic criminals and nation-state actors for its extreme economic efficiency.

[^1]: In February and November 2025, several members of this cluster were arrested in Thailand (Phuket) in a joint operation involving US and Thai authorities.
[^2]: Breach of AT&T, Verizon, and Lumen; US House of Representatives; Microsoft SharePoint compromise.
[^3]: PunyToad’s exploitation of F5 and VMware vCenter and ESXi.
[^4]: BRICKSTORM, a Go-based ELF binary, often obfuscated with Garble.

---

g a single laptop compromise into a full-scale
cloud infrastructure breach. In a terrifying shift toward
extortion through destruction, the 2025 variant
contains a dead man’s switch. If the malware detects
that its C2 channels are severed or tokens revoked, it
triggers a wiper payload that deletes the entire home
directory on Linux or %USERPROFILE% on Windows,
punishing the organization for attempting to remediate
the infection.

Nearly

Over

Crucially,

43%of emails

of emails
failed SPF
failed SPF

44%

lacked valid
DKIM signatures

failed
DMARC

46%

Cloudflare | 2026 Cloudflare Threat Report Industrialized PhaaS

Supporting these high-level attacks is the rise of Telegram-
based PhaaS modules, exemplified by the recently disrupted
RaccoonO365 enterprise. These services go beyond simple
spam; they are standardized industrial pipelines marketed as no-
downtime mailer bots that significantly lower the barrier to entry
for cybercriminals. By offering tiered subscription models — such
as $355 for 30 days — these enterprises provide a plug-and-play
marketplace for harvesting credentials, cookies, and data from
Microsoft 365, OneDrive, and SharePoint accounts to enable wide-
scale financial fraud and extortion.

These industrialized pipelines offer 100% inbox delivery
guarantees by using the automated rotation of clean residential
proxies and “warm” IP addresses to bypass reputation-based
filters and security gateways. They also provide turnkey brand
impersonation through high-fidelity, real-time templates for
platforms like Google, Microsoft 365, Kraken, and Gemini that
are virtually indistinguishable from legitimate logins. To maintain
stealth, these kits utilize advanced evasion techniques, including
CAPTCHA-based human verification, browser fingerprinting, and
anti-analysis scripts that actively disable browser consoles to hide
malicious code from security researchers.

Most critically, these bots integrate MFA-bypassing adversary-in-
the-middle (AitM) tech. By acting as a transparent proxy between
the victim and the legitimate service, these kits harvest live
session tokens rather than just static passwords. This effectively
neutralizes standard MFA, as the attacker captures the already-
authenticated session state.

As seen in Cloudforce One’s RaccoonO365 disruption, these
actors often abuse legitimate cloud infrastructure to shield their
backend servers, making the attack appear to originate from a
trusted network. This shift toward automated, destructive extortion
means that traditional perimeter defenses are no longer sufficient;
security must now be as fast and adaptable as the automated
threats it aims to stop.

3636

Advertisement for a PhaaS
mailer bot on Telegram

Cloudflare | 2026 Cloudflare Threat Report 37

The BEC request factory: Intercepting
$123 M in highly targeted financial lures
In 2025 alone, Cloudforce One analysts identified a staggering $123,455,786 in
explicit financial theft attempts. Within this landscape, name impersonation has
proven to be the most lucrative tactic for threat actors, accounting for the vast
majority of these funds. Our data shows that while the financial requests can vary
wildly — with a total range of $5,567,070 between the largest ($5,567,520.00)
and smallest ($450.00) attempts — the sweet spot for attackers is remarkably
consistent. The mean financial theft attempt sits at $49,224.80, nearly mirroring
a median of $48,950.00 and a mode of $49,860.00. These figures suggest
a calculated strategy where fraudsters aim for amounts large enough to be
profitable, yet small enough to potentially bypass more stringent executive
approval thresholds.

The true danger of business email compromise (BEC) lies in thread hijacking,
where an attacker interjects themselves into an existing, legitimate conversation.
This level of intervention is incredibly difficult to detect because it utilizes
legitimate communication channels; to automated systems, these requests
appear as benign, everyday business activity. In one standout instance, our
team intercepted a single hijacked compromise that saved a client $5.5 million,
highlighting the critical reliance on manual intervention and expert analysis by
teams like PhishGuard to prevent catastrophic losses.

As we move into 2026, we expect attackers to use generative tools to automate
thread hijacking at scale, allowing them to maintain this precise ~$49,000
sweet spot across thousands of concurrent conversations without the need for
manual oversight.

Compromise /
spoofing
External
partner’s email is
compromised
or spoofed

Social
engineering
Attackers use
urgency and
emotional
manipulation

Fraudulent
invoice
Fake invoice is
issued for up-front
or “urgent” payment

The reveal
Scam is uncovered
when the real
invoice arrives

BEC lifecycle

Cloudflare | 2026 Cloudflare Threat Report
Pig butchering: How scammers weaponize emotional
trust and wealth personas to drain life savings

38

The Cloudforce One team has observed a number of
“pig butchering” scams in 2025. Pig butchering (known
as shāzhūpán) is a sophisticated long-con investment
scam that originated in the People’s Republic of China
and is a metaphor for the agricultural practice of
fattening up a pig before slaughter; scammers build
intense emotional trust with a victim over weeks or
months (“fattening”) before stealing their life savings
through a fraudulent investment platform (“butchering”).

 1.  A classic “wrong number” introduction
Pig butchering begins with a lure, where scammers
initiate contact via “wrong number” text messages
or social media to build initial rapport. The scammer
often uses a benign “Hey” to bait a response and then
apologizes for the “mistake” to launch a conversation.

4.  Defensive redirection
The example below demonstrates defensive
redirection, as the potential victim successfully
deflects a grooming attempt. The interaction highlights
the strategic ways scammers attempt to integrate
themselves into a victim’s daily schedule.

5.  A fake exchange
Once trust is solidified, the scam moves to the
fraudulent exchange phase. Victims are directed
to deposit cryptocurrency into fake exchanges that
report deceptive, “amazing” gains to encourage further
investment before the victim is ultimately prevented
from withdrawing any funds. Victims that request their
funds will be asked to send in more funds to cover
“fees” or “taxes.”

2.  The “wealth persona” lure
Following this initial contact,
the grooming phase begins.
Our analysts have noted the
use of wealth personas,
where scammers share
photos featuring luxury items
like high-end watches to
establish themselves as
successful investors.

3.   Moving to Telegram
To evade security filters
and deepen the grooming
process, attackers force a
platform migration, moving
victims to unmonitored
messaging apps like Telegram.

Recovering any of the stolen money is difficult, if not
impossible. In some cases, the cryptocurrency can
be traced to an exchange and a legal authority can
compel the exchange to return the funds to a victim.
In most cases, the funds are quickly laundered so
that the legal approach is less effective. Throughout
2026, we anticipate that the grooming phase will
become increasingly automated through LLM-
powered personas. This artificial intimacy allows
a single operative to “fatten” hundreds of victims
simultaneously with highly personalized, AI-generated
emotional lures that are virtually indistinguishable from
human interaction.

Cloudflare | 2026 Cloudflare Threat Report 3939

The infostealer engine: How stolen logs
fuel the global ransomware pipeline

The Cloudforce One team emphasizes that an infostealer infection must be treated with the same urgency
as a live network intrusion. These tools have evolved far beyond nuisance malware; they now serve as the
primary engine for a transactional criminal supply chain fueled by initial access brokers (IABs). This pipeline
begins when IABs purchase logs — bulk collections of stolen data — from infostealer operators, validate the
credentials, and auction off high-value corporate access to ransomware cartels.

This evolution has led to staggering corporate exposure; according to Verizon’s 2025 Data Breach Investigations
Report, 54% of all ransomware attacks in 2025 traced back to infostealer-enabled credential theft.5 A critical
case in point occurred in early 2025 when the HellCat ransomware group successfully breached major global
organizations, including Jaguar Land Rover and Telefónica, specifically by leveraging Jira credentials and session
tokens sourced directly from infostealer logs.

The Lumma disruption and the path ahead

In May 2025, our team participated in a high-impact, coordinated global operation to disrupt Lumma
Stealer (LummaC2), a premier example of the malware-as-a-service (MaaS) model. Lumma represents the
industrialization of data theft, providing criminals with customized malware builds and professional-grade
dashboards to manage stolen data. Its primary effectiveness stems from the exfiltration of session tokens
and active cookies, which neutralizes standard MFA and allows attackers to log in rather than break in.

Cloudforce One’s role in this disruption included deploying Turnstile-enabled interstitial warning pages across
malicious C2 domains to prevent malware bypass and taking direct action against the accounts used to configure
this infrastructure.

While our 2025 focus remained on disrupting these established MaaS giants, the 2026 landscape will be defined
by their successors — variants we predict will move toward fully automated token-rotation-bypass to collapse the
time between initial infection and full ransomware deployment into a matter of hours.

Cloudforce One is already tracking the emergence of vacuum-fillers and new MaaS variants attempting to reclaim
this market share. We plan to continue these aggressive disruption efforts.

Cloudflare | 2026 Cloudflare Threat Report 40

Ransomware 2.0: Weaponizing authorized
access and human-in-the-loop sabotage
Cloudforce One observes that the modern extortion landscape has shifted from a
purely technical encryption challenge into a high-fidelity identity and access crisis. The
weaponization of authorized credentials and internal collaborators has become the primary
path for high-impact breaches, signaling a move beyond traditional malware toward the
exploitation of legitimate access.

This evolution is driven by a sophisticated infostealer-to-extortion pipeline, which in 2026
may transition from an emerging threat to the standard operational baseline for throughput
and speed in the ransomware ecosystem. Attack chains frequently begin with malware like
LummaC2 harvesting credentials for Citrix, Microsoft RDWeb, and browser-based VPNs.
These high-value targets are then handed off to ransomware groups who bypass the difficult
intrusion phase entirely, focusing their efforts on data theft and direct extortion. This cycle is
being further compressed by AI-accelerated attack cycles; GenAI has shrunk timelines from
days to minutes, as threat actors leverage LLMs in real time to rewrite code that bypasses
EDR and to map complex network topologies for rapid lateral movement.

The targeting of “critical continuity” has also intensified, with manufacturing and critical
infrastructure now representing over 50% of all targeted attacks.6 Attackers prioritize
these sectors because the immense cost of operational downtime creates a desperate and
immediate incentive for high-value payouts. This strategy is often supported by human-
in-the-loop access, where attackers recruit remote workers in lower-income regions for as
little as $50 to provide initial access to billion-dollar networks, essentially turning the trusted
interior into an active attack vector.

Lastly, in a majority of observed cases, exfiltrated data is used as leverage for ransom while
bypassing traditional backup-and-restore defenses that organizations typically rely on to
recover from a standard encryption attack. In other words, pure extortion has become the
new standard in the ransomware ecosystem.

Cloudflare | 2026 Cloudflare Threat Report Cloudflare | 2026 Cloudflare Threat Report

41

Case study

The authorized insider investigation
and unmasking

A recent Cloudforce One REACT incident response
investigation provides a definitive example of ransomware’s
shift to high-fidelity identity and access crisis. In this
instance, a company’s trusted employee with high-level
permissions leaked sensitive client metadata and source
code following a personal grievance and launched a high-
value extortion campaign. This quiet crime scene left no
traditional malware signatures; instead, investigators had
to map a “shadow path” where the insider staged data over
several weeks using legitimate production access during
standard working hours.

To unmask the threat actor, the team launched a response
and investigation rooted in both threat and psychological
intelligence indicators. For example, investigators poked
the insider in internal communications by downplaying
the attacker’s skill. This provoked a defensive response in
the next ransom email, where the actor used linguistic slips
that mirrored the investigators’ recent internal comments,
narrowing the suspect pool to those with access to
specific logs.

By merging technical logs with behavioral science — using
sentiment analysis on internal employee communications to
match the tone and linguistic patterns of the ransom notes —
the team identified a specific individual correlated to threat
indicators. Once the company had this forensic evidence in
hand, they were able to partner with law enforcement to
intercept the employee as they attempted to flee the country.
Accounting for human risk is now just as vital as patching
software vulnerabilities.

Cloudflare | 2026 Cloudflare Threat Report
42

The triple-threat bot chain: From identity breach
to host compromise to disruption

The sheer scale of automated traffic is a pervasive
threat to organizations globally, with approximately 30%
of all HTTP traffic Cloudflare observes originating from
bots. While some of this is benign — such as search
engine crawlers — a significant portion is dedicated to
a high-speed attack chain that bridges identity theft,
host compromise, and service disruption.

Bot vs. human

Bot (automated) vs. human HTTP
requests distribution

Bot
29.9%

Human
70.1%

Cloudforce One tracks these malicious bots not as
isolated scanners, but as a continuous lifecycle. This
chain relies on massive, distributed botnets — such
as Aisuru and its successor Kimwolf — which mask
the source of attacks by tunneling through residential

proxy services. This makes malicious traffic look like it
is originating from legitimate users, allowing attackers
to systematically test defenses from the network layer
up to the application layer while remaining below the
radar of traditional filters.

Heading into 2026, we expect the use of successor
networks like Kimwolf to continue expanding, making
this residential-proxy tunneling the default operational
baseline for evading IP-based filters.

Bots as the engine of
identity exploitation

The chain begins with automated account takeover
(ATO), where bots weaponize compromised credentials
at industrial scale. This process is fed by a circular
ecosystem of harvesting sites and infostealers like
Qakbot and Emotet. These bots do not simply look
for vulnerabilities in the traditional sense; they exploit
human behavior, specifically the fact that 63% of all
human logins involve credentials that have already
been compromised elsewhere.

Attackers use bots to test stolen username and
password pairs across thousands of sites per second.
The scale is staggering, as Cloudflare data shows
that 94% of all login attempts originate from bots.
To bypass modern detection, attackers use tools
like Selenium and Puppeteer to mimic human mouse
movements and realistic scrolling, allowing them
to bypass traditional session intelligence during a
credential stuffing assault.

30% of all HTTP

traffic Cloudflare
observes
originates
from bots

63% of all human logins

involve credentials
that have already
been compromised
elsewhere

94%

of all login
attempts
originate
from bots

Cloudflare | 2026 Cloudflare Threat Report 43

Escalating to host compromise and automated harvesting

Once a bot secures a foothold through credential exploitation, the objective shifts to host
compromise and the systematic extraction of data. Infrastructure for this stage is provided by
botnets like the dismantled 911 S5 or the high-compute Mantis botnet, which utilizes hijacked
virtual machines to launch attacks.

This stage of the chain increasingly targets the interfaces of LLMs. These sophisticated bots
are designed to interact with LLMs in ways that exploit vulnerabilities in their input handling
or output generation, systematically extracting sensitive or proprietary information that was
used in the model’s training or has been generated by the model itself. This novel form of data
theft bypasses traditional network security measures by leveraging the public-facing nature
of LLM interfaces, posing a substantial risk to organizations that deploy or rely on these
advanced AI systems.

Bot-driven infrastructure disruption and exhaustion

The final link in the chain is the transition to availability threats, where the botnet power used
for access is turned into a weapon of destruction. Denial-of-service (DoS) attacks are the
most visible expressions of this power, designed to destroy business continuity. In late 2025,
the Aisuru botnet reached record-shattering peaks, demonstrating how residential botnets
can cripple major digital properties.

By utilizing botnets like Kimwolf, which recently saw over 550 C2 nodes null-routed in early
2026, attackers hide their attacks within legitimate residential traffic to bypass IP-based
blocking. Beyond volumetric floods, modern bots target specific high-cost application
functions, such as complex search queries, to exhaust a server’s CPU and memory and take
a site offline with minimal traffic.

This pivot from stealthy exploitation to massive infrastructure bombardment marks a shift in
the threat actor’s endgame: When access is no longer enough, they weaponize the entire bot
chain to achieve total operational blackout. This industrialization of disruption is reflected in
the staggering surge of hyper-volumetric activity observed by Cloudforce One.

Cloudflare | 2026 Cloudflare Threat Report 44

DDoS attacks by year and type

HTTP DDoS attacks              Network-layer DDoS attacks

50.0 M

40.0 M

30.0 M

20.0 M

10.0 M

0.0 M

s
k
c
a
t
t
a
S
o
D
D

47.1 M

12.7 M

34.4 M

2025

14.0 M

5.2 M

8.7 M

2023

21.3 M

9.9 M

11.4 M

2024

Year

DDoS attacks observed by Cloudflare

In 2025, the total number of DDoS attacks observed by Cloudflare more than doubled to an
astonishing 47.1 million. The most substantial growth was in network-layer DDoS attacks,
which more than tripled year over year.

Once viewed mostly as a nuisance, DDoS attacks have become powerful weapons for
external actors seeking to disrupt operations and undermine business continuity. On average,
Cloudflare mitigated 5,376 DDoS attacks every hour: 3,925 network-layer DDoS attacks and
1,451 HTTP DDoS attacks.

The year was defined by the rise of hyper-volumetric attacks, largely fueled by the
emergence of the Aisuru and Kimwolf botnets, which control an estimated 1 to 4 million
infected hosts. Hyper-volumetric attacks are now occurring with routine frequency, with
Cloudforce One observing 19 new world record attacks in 2025. The current record holder, a
31.4 Tbps attack in November, was a massive UDP flood launched by the Aisuru botnet. This
attack was nearly six times the peak volume of 2024’s largest attack.

In 2025, the total number of DDoS attacks
observed by Cloudflare more than doubled.

Cloudflare | 2026 Cloudflare Threat Report
World record DDoS attacks

45

h
t
n
o
M

September 2024

October 2024

October 2024

April 2025

May 2025

August 2025

August 2025

August 2025

August 2025

August 2025

September 2025

September 2025

September 2025

September 2025

September 2025

September 2025

September 2025

September 2025

September 2025

October 2025

October 2025

November 2025

3.8 Tbps

4.2 Tbps

5.6 Tbps

6.5 Tbps

7.3 Tbps

7.7 Tbps

8.4 Tbps

9.9 Tbps

10.7 Tbps

11.5 Tbps

11.9 Tbps

12.0 Tbps

12.5 Tbps

15.1 Tbps

17.0 Tbps

17.8 Tbps

19.7 Tbps

22.2 Tbps

25.8 Tbps

29.4 Tbps

29.7 Tbps

31.4 Tbps

0.0 Tbps

10.0 Tbps

20.0 Tbps

30.0 Tbps

40.0 Tbps

Max rate (Tbps)

Hyper-volumetric DDoS attacks continue to grow in size and frequency

Heading into 2026, multi-terabit attacks are likely to become the new baseline for targeted
campaigns. The democratization of massive botnets like Aisuru means that even mid-tier
threat actors can now launch hyper-volumetric attacks that were once the sole province
of nation-states.

Organizations must shift from reactive to proactive, autonomous defense postures, as the
window for human intervention has effectively closed — most 2025 attacks lasted less than
10 minutes, far too fast for manual mitigation. Furthermore, as geopolitical tensions continue
to influence cyber activity, industries like automotive and mining should expect to be caught
in the crossfire of state-aligned DDoS campaigns.

For a deeper dive into the current DDoS landscape,
explore Cloudforce One’s quarterly DDoS threat reports.

Cloudflare | 2026 Cloudflare Threat Report Community
and regional
perspectives

While many threat actors operate globally, regional
targeting is often driven by local geopolitical tensions and
specific economic assets. The following highlights the
primary threat actors and key concerns for the Americas,
EMEA (Europe, Middle East, and Africa), and APAC (Asia-
Pacific) regions. The actors listed in each region below
were chosen for their operational gravity in those areas,
based on analyses of where they exert the most pressure,
maintain the most specialized infrastructure, or pursue
their primary strategic objectives.

IV.Primary actors

4747

LAYOUT
OPTION 1

Key concerns

Identity-first intrusions
Identity abuse has now
superseded network exploitation
as the primary vector for initial
access. Threat actors have moved
away from “attacking the box” and
are now focused on “attacking the
session,” prioritizing credential
theft, session hijacking, and the
systematic bypassing of MFA.
By weaponizing compromised
identities, attackers can navigate
cloud environments and enterprise
systems with the appearance of
legitimacy, bypassing the need for
traditional malware.

Infrastructure pre-positioning
The shift from data theft to
operational persistence in critical
utilities suggests attackers are
preparing for disruptive events
rather than just espionage.

Ransomware service maturity
The professionalization of
ransomware-as-a-service (RaaS)
means even lower-tier affiliates
can execute high-impact attacks
using sophisticated playbooks.

Americas
The Americas, particularly the United States, remains the most targeted
region globally by volume. Threat activity in the Americas is primarily
characterized by highly sophisticated state-sponsored pre-positioning
and a pervasive, industrial-scale ransomware ecosystem.

Primary threat actors

CallowDuck

Alias / AKA:
Scattered Spider

SleezyShrew

Alias / AKA:
APT29

Focus: Identity and access
management (IAM) abuse

Context: They are the premier
example of the shift from malware
to identity abuse. They utilize
sophisticated social engineering
(vishing) and MFA fatigue to
compromise cloud environments.
They are highly disruptive to major
US enterprise and hospitality sectors
(e.g., MGM / Caesars).

Focus: Government, think tanks,
and cloud service providers

Context: This group has shifted
heavily toward cloud-based targets,
utilizing sophisticated session
hijacking and token theft to maintain
access to sensitive communications.
They focus on long-term persistence
(e.g., in Microsoft 365 environments)
and supply chain compromises (e.g.,
SolarWinds).

FrumpyToad

Alias / AKA:
APT41

Focus: State espionage and private
financial gain

Context: Known for software supply
chain attacks, they target US
healthcare, tech, and retail sectors
for both intellectual property and
personal profit.

CloyingKrill

Alias / AKA:
APT33

Focus: Aerospace, defense,
and petrochemical sectors

Context: A primary arm of Iranian
state-sponsored activity. They
target defense contractors to narrow
military technology gaps and gather
regional intelligence.

DazedToad

Alias / AKA:
Volt Typhoon

Focus: Critical infrastructure
(energy, water, communications,
transportation)

Context: Unlike traditional espionage,
this group focuses on pre-positioning
for potential future sabotage. They
are masters of LotL, using built-in
network tools to maintain long-
term persistence without triggering
traditional malware alerts.

Qilin, Akira, and Play

Ransomware proliferation

Focus: Financial extortion through
double extortion (data theft and
encryption); leads attacks on the
telecom and healthcare sectors

Context: These groups represent
the industrialized wing of
cybercrime. Akira and Play often
exploit unpatched VPNs, while Qilin
is known for aggressive name-and-
shame tactics.

Cloudflare | 2026 Cloudflare Threat Report

Europe, Middle East,
and Africa (EMEA)
Europe is the second most targeted region, with 22% of global extortion
victims located there. The EMEA landscape remains the primary theater
for disruptive cyber operations linked to the war in Ukraine and shifting
power dynamics in Eastern Europe and the Middle East.

Primary threat actors

ZapoyShrew

Alias / AKA:
APT44

MuddyKrill

Alias / AKA:
MuddyWater

Focus: Destructive operations and
critical infrastructure sabotage

Focus: Regional geopolitics and
telecommunications

Context: This group is responsible
for grid attacks in Europe and the
widespread use of high-profile
wiper malware.

Context: This group targets
government and private sectors
across the Middle East (Israel, Saudi
Arabia, UAE) and Southern Europe
for espionage and regional influence.

IncoherentShrew

Alias / AKA:
APT28

Focus: Political and military
espionage

Context: Heavily involved in
disinformation campaigns and leak
sites (hack-and-leak) targeting
European parliaments and NATO-
aligned entities.

RuntZander

Alias / AKA:
White Lynx

Focus: Information operations (IO)
and hack-and-leak campaigns aimed
at neighbors of Belarus, including
Poland, Germany, Latvia, and
Lithuania, with targeting focused
on government and media

Context: Closely aligned with
Belarusian and Russian interests,
this group specializes in stealing
and leaking sensitive data to
influence local elections or damage
political figures.

48

Key concerns

Targeted critical infrastructure
Organizations in energy, finance,
or logistics face an elevated risk of
being targeted as part of broader
geopolitical pressure campaigns.

Wiper malware spillover
Destructive tools intended for
regional conflicts often possess
self-propagating capabilities that
can inadvertently impact global
supply chains.

Political hacktivism
Hacktivists are responsible for
almost 80% of recorded incidents
in the EU, primarily using
DDoS attacks to target public
administration and banking.

Industrial extortion
Ransomware accounts for over
38% of incidents in the EU
transport sector.

Weaponized disinformation
The combination of data leaks
and AI-enhanced disinformation
makes it increasingly difficult
for organizations to defend
their brand reputation during
regional crises.

Cloudflare | 2026 Cloudflare Threat Report

49

Key concerns

Network backbone compromise
The targeting of ISPs and network
edge devices (Salt Typhoon)
means that traffic thought to be
secure could be intercepted before
it even reaches its destination.

Economic and maritime espionage
High-tech manufacturing and
maritime industries are at extreme
risk of IP theft aimed at closing
competitive gaps in regional
industrial capabilities.

Supply chain and IT targeting
The information technology and
semiconductor sectors are the
most targeted industries in
the region.

Stealthy persistence (LotL)
The widespread use of LotL
techniques makes it exceptionally
difficult to differentiate between
a legitimate administrator and a
state-sponsored actor.

Summit espionage
Major 2026 diplomatic events
(ASEAN in the Philippines, APEC in
China) are prime targets for state-
backed intelligence gathering.

Asia-Pacific (APAC)
The APAC region faces a unique blend of high-tech espionage and
large-scale financial theft. Threat activity in APAC is also dominated by
actors supporting the Belt and Road Initiative and territorial claims in
the South China Sea. There is a heavy focus on maritime intelligence
and compromise of core network infrastructure to enable broad-scale
monitoring and pre-positioning for future conflicts.

Primary threat actors

DazedToad

Alias / AKA:
Volt Typhoon

WorthlessSlug

Alias / AKA:
Diamond Sleet

Focus: Critical infrastructure and
OT pre-positioning

Focus: Cryptocurrency and
financial systems

Context: Utilizes LotL techniques
to maintain long-term, undetected
access to regional military and
utility infrastructure.

Context: While global, their activity
in APAC is intense, targeting
regional exchanges and financial
hubs (Singapore / Japan) to
generate hard currency for the
North Korean regime.

SoggyToad

Alias / AKA:
APT40

Focus: Maritime and naval technology

Context: This group focuses
specifically on targets in the
APAC region that have strategic
relevance to the South China Sea,
including regional governments and
engineering firms.

ClumsyToad

Alias / AKA:
Mustang Panda

Focus: Southeast Asian
governments and
international nonprofits

Context: Focuses on entities involved
in South China Sea policy, often using
lure documents related to regional
summits and diplomatic events.

WimpyToad

Alias / AKA:
Salt Typhoon

Focus: Telecommunications
infrastructure and service providers

Context: Specializes in
compromising the core of the
Internet — ISP routers and telecom
switches — to intercept vast
amounts of data at the source.

Cloudflare | 2026 Cloudflare Threat Report

Cloudflare | 2026 Cloudflare Threat Report

5050

Drivers of regional overlap
The concept of a regionally isolated threat is becoming more and more scarce. While intent is
often regional, the infrastructure and target selection frequently cross continental boundaries.
The question of regional overlap in the threat landscape is a core challenge in cyber threat
intelligence. While many threat actors are geographically focused for political or cultural
reasons, the modern threat landscape shows significant and increasing overlap across the
Americas, EMEA, and APAC regions.

We can categorize this overlap into three distinct drivers: geopolitical and state-sponsored
campaigns, cybercrime, and the technology supply chain. Below are examples of these
regional overlaps and the actor behaviors that drive them.

Geopolitical and state-sponsored overlap

The most sophisticated actors (typically Tier 1 nation-states and threat actors aligned with
those states) do not respect regional boundaries because their interests are global.

The big four (China, Russia, Iran, North Korea): These actors maintain distinct “desks” for
each region.

•  China-aligned actors (e.g., FrumpyToad, DazedToad): While heavily focused on APAC

(Taiwan / South China Sea), they simultaneously target Americas and EMEA for intellectual
property theft and pre-positioning in critical infrastructure.

•  Russia-aligned actors (e.g., IncoherentShrew, SleezyShrew): Historically focused
on EMEA and the Americas, they increasingly overlap into APAC to monitor shifting
diplomatic alliances.

Cybercrime big game hunting

Cybercriminal syndicates (RaaS) are almost entirely region-agnostic. They target revenue,
not geography.

•  Overlap pattern: A ransomware group might hit a logistics firm in Germany (EMEA) on

Monday and an insurance provider in Brazil (Americas) on Tuesday.

•  IABs: These actors sell access to networks globally. An IAB based in Eastern Europe might
sell access to a Japanese manufacturing plant (APAC) to a ransomware affiliate based in
the Americas.

Supply chain and shared technology stacks

Because many global enterprises use the same software (Microsoft Office, Salesforce CRM,
vSphere, etc.), a single vulnerability creates a global overlap.

The vulnerability sprint: When a zero-day is released (e.g., React2Shell), actors across all
regions rush to scan the global IP space, often with the help of attack surface management
tools which are typically helping attackers more than defenders. This creates a noise floor of
activity that overlaps every region simultaneously.

5151

Specific examples of regional overlap

Several advanced persistent threat (APT) groups serve as primary examples of adversaries with a global reach,
systematically targeting organizations across the Americas, EMEA, and APAC regions. These groups often align
their operations with geopolitical objectives or large-scale financial theft.

Key exemplars of multi-regional threat actors include:

NervousToad

Lazarus group

ClumsyToad

Alias / AKA:
APT27

A prominent group that consistently
targets headquarters worldwide. Its
operations span North and South
America, Europe, and the Middle
East, focusing on sectors such
as aerospace, government, and high
tech to conduct long-term espionage.

Alias / AKA:
Hidden Cobra

Alias / AKA:
Mustang Panda

A sophisticated group of actors
known for their immense geographic
reach and diverse motives,
including financial gain through
cryptocurrency theft and strategic
sabotage. It maintains an active
presence in North America, Europe,
and Asia.

Highly active group that utilizes
diverse techniques like spear-
phishing and DLL sideloading across
a vast geographic footprint. In 2026,
its activity was noted in the United
States, Europe, and extensively
across APAC countries including
Australia, India, Japan, and Vietnam.

SleezyShrew

CloyingKrill

Alias / AKA:
APT29

A group that operates globally to
support Russian foreign policy. It
targets government and diplomatic
entities across North America,
Europe, and other regions opposing
Russian interests.

Alias / AKA:
APT33

An actor that illustrates a broad
operational scope, targeting critical
infrastructure in the United States
(Americas), Saudi Arabia (Middle
East / EMEA), and South Korea
(APAC), with a specific focus on the
energy and aviation sectors.

LockBit and
similar ransomware
syndicates

While often criminal rather than
state-sponsored, these groups
function as enterprise cybercriminals
with global reach. They target
large-scale enterprises across every
major economic region, including
the Americas, EMEA, and APAC,
prioritizing high-value critical
infrastructure for double and
triple extortion.

Cloudflare | 2026 Cloudflare Threat Report

Cloudflare | 2026 Cloudflare Threat Report

52

The strategic hub phenomenon

Cloudforce One observes certain strategic hubs where regional and global threat interests
converge, creating an exceptionally high-density threat environment.

Israel

Global cybersecurity and geopolitical nexus

As a primary theater for both regional conflict and global cybersecurity innovation, Israel
faces tri-regional pressure. It is targeted by EMEA-based adversarial neighbors for
destabilization, Americas-based stakeholders for geopolitical monitoring, and APAC-based
actors seeking to exfiltrate world-class defensive technology and military IP.

Singapore

Financial and logistical nexus

Acting as the pivotal gateway for trade and finance between the APAC and Americas
regions, Singapore serves as a global listening post. It attracts the full spectrum of
intelligence activity, ranging from state-sponsored financial espionage (seeking insights
into global markets) to advanced cybercriminal syndicates targeting its high concentration
of liquid capital.

Taiwan

Semiconductor and cross-strait tensions

As the global epicenter for advanced semiconductor manufacturing and a focal point of
maritime territorial disputes, Taiwan represents a critical silicon shield. It is under constant
pressure from APAC-based actors (China-nexus) focused on technological exfiltration
and pre-positioning for potential future blockade scenarios. Simultaneously, it attracts
Americas- and EMEA-based stakeholders monitoring regional stability and the integrity of
the global hardware supply chain.

Ukraine

Kinetic-digital proving ground

Serving as the frontline for modern hybrid warfare, Ukraine is the world’s most active
theater for destructive cyber operations. It is relentlessly targeted by EMEA-based state
actors (Russia- / Belarus-nexus) for critical infrastructure sabotage and psychological
operations. Concurrently, it serves as a primary intelligence collection point for Americas
and European allies seeking to analyze the evolution of state-sponsored tactical
coordination and new wiper malware variants.

53

Analytical implications

The regional overlaps detailed in this report have three critical implications for global
threat analysis:

•  Cross-regional lateral movement: A local incident is rarely isolated. Adversaries frequently

utilize a breach in an EMEA or APAC branch as a low-friction testing ground or staging
point for lateral movement into an Americas-based headquarters. Security teams must
adopt a unified global response model to prevent cross-regional escalation.

•  Strategic infrastructure proxying: Threat actors increasingly utilize geographic proxying
to complicate attribution and circumvent geofencing. We frequently observe Americas-
based actors leasing EMEA-based VPS infrastructure to target APAC entities. Effective
tracking now requires monitoring cross-regional routing patterns rather than relying on
simple IP-origin telemetry.

•  Temporal vulnerability exploitation (time-zone arbitrage): Adversaries strategically

leverage regional blind spots by conducting high-intensity activity during the weekends
or national holidays of the target region. By initiating operations when local defensive
capacity is reduced but the attacker’s home region is in a standard business day, they
significantly maximize their dwell time and operational success rate.

Cloudflare | 2026 Cloudflare Threat Report Recommendations
A roadmap for strategic resilience and
an identity-centric enterprise model

The key findings in this report signal that the 2026 threat
landscape is defined by the weaponization of identity, the
industrialization of SaaS supply chain vulnerabilities, and the
emergence of hyper-volumetric, autonomous DDoS strikes
that outpace human intervention.

To thrive in this environment, organizations must pivot from
reactive, infrastructure-centric defense to a proactive,
identity-centric resilience model. The following
recommendations provide a high-level roadmap for neutralizing
these emerging force multipliers and securing the modern, AI-
integrated enterprise.

V.1

2

55

Focus AI security efforts on
securing workforce AI usage

Transition from MFA to identity-
first zero trust

Prioritize securing how employees interact
with LLMs to prevent AI-assisted navigation by
attackers. Implement strict data loss prevention
(DLP) for AI prompts and deploy browser-
isolated environments for generative AI tools
to ensure corporate keys to the kingdom aren’t
inadvertently leaked into model training sets or
captured by infostealers.

Since infostealers like LummaC2 now harvest
session tokens to bypass MFA, organizations
must move beyond simple one-time codes.
Implement phishing-resistant MFA (FIDO2
/ passkeys) and continuous monitoring that
invalidates sessions instantly if impossible
travel or suspicious device fingerprints (like
mouse-jiggling software) are detected.

3

Harden the SaaS-to-SaaS connective tissue

The GRUB1 campaign proves that a single compromise of a trusted
integration can create a dangerous ripple effect. Conduct an
immediate audit of all SaaS API permissions. Apply the principle
of least privilege to integrations, specifically looking for over-
privileged read / write tokens in tools like Salesforce, Slack, and
GitHub that could allow an attacker to pivot between clouds.

4

5

Implement human-in-the-loop
verification for remote hiring

Adopt autonomous, hyper-
volumetric DDoS defenses

To counter the industrialized North Korean insider
threat, move away from purely digital onboarding.
Use zero trust biometric verification for all remote
video interviews and enforce strict hardware-
based geofencing. Corporate laptops should be
cryptographically paired to the user’s physical
location to neutralize “laptop farm” facilitators.

With the Aisuru botnet pushing attacks
to a 31.4 Tbps new baseline, the window
for human intervention has closed.
Organizations must shift to automated,
edge-based mitigation that can respond in
seconds. Legacy scrubbing center models
are no longer sufficient for attacks that
peak and conclude within 10 minutes.

6

Isolate peripheral infrastructure
to contain exposure

Eliminate email blind spots with
AI-first security

To establish a robust defensive posture,
organizations must implement a strategic
shift in how they manage IaaS and SaaS
dependencies. Specifically, subsidiary
and supporting services should operate
independently, utilizing dedicated domain
names, unique IP addresses, and, where
feasible, distinct autonomous system
numbers (ASNs).

PhaaS bots can rapidly bombard organizations
with emails leveraging polymorphic tactics
that bypass legacy secure email gateways.
Organizations must adopt AI-first email security
capable of interpreting these shifting variables
and adapting to both incoming and lateral
threats. By utilizing signals beyond the email
inbox, these systems can better identify and
neutralize internal compromised accounts in
real time.

7

Cloudflare | 2026 Cloudflare Threat Report Cloudforce One overview

56

Threat intelligence

Managed defense

Gain access to Cloudflareʼs
global threat visibility with
a powerful package of
threat intelligence tooling
and expertise to make your
organization smarter, more
responsive, and more secure.

Receive 24 / 7 expert
monitoring and proactive
threat detection across your
Cloudflare stack, ensuring
continuous protection and
rapid response to issues.

Cyber response
and readiness

Deploy hands-on experts
to neutralize active threats,
conduct forensic analysis, and
minimize operational impact.

Learn more

Learn more

Learn more

Contact Cloudforce One security experts

Subscribe to our threat research

Cloudflare | 2026 Cloudflare Threat Report Modernize your security with Cloudflare

One security platform. Network to cloud. Apps to Al.

57

App to network layer

•  Web App 8, API

protection (WAAP)

•  Security service

edge (SSE)

•  DDoS Protection

Al-powered protection

•  Email Security

•  Bot Management

•  Platform simplified

with Al agents

Cloudflare’s one security platform scales seamlessly from network to
cloud, and protects all users and data across applications and Al. It
leverages an intelligent and programmable global cloud network to unify
a range of diverse technologies, harnesses Al-powered threat intelligence
to deliver low-touch, high-efficacy protection, and Al-powered data loss
prevention detections to distributed organizations of all sizes.

Secure inbound and outbound traffic from network to application
layer, to increase consistency and coverage across distributed IT
environments with existing teams and budget.

Secure Al workloads from models to inference, to increase Al
adoption with secure, reliable inference and protected, clean
data for trusted Al models.

Al-powered protection and observability fueled by our global
network scale reduces the mean time to detect, respond, and
mitigate future critical incidents.

Cloudflare offers an integrated approach to security modernization,
simplifying deployment, enhancing visibility, and reducing the TCO
while eliminating the multiple vendors and tools required with traditional,
fragmented solutions. By delivering security close to the end user and
requested resource, Cloudflare ensures resiliency and broad protection
against evolving threats.

The result: One security platform. Network to cloud. Apps to Al.

Inbound and outbound

•  Secure access service

edge (SASE)

•  Network as a service
(NaaS) and multicloud

•  Network Interconnect

Secure Al workloads

•  Al Gateway

•  Firewall for Al

•  Critical infrastructure

trusted to run Al

With Cloudflare,
customers can realize:

24%

breach risk reduction
across the enterprise

35%

time savings on security
and DNS management

250

hours of avoided downtime

227%

ROI of Cloudflare over
three years

Source: Forester TEI study

Cloudflare | 2026 Cloudflare Threat Report

5858

Endnotes

1.  https://www.nhpr.org/2025-11-21/russian-hacking-suspect-wanted-by-the-fbi-arrested-

on-thai-resort-island

https://therecord.media/russian-arrested-thailand-allegedly-void-blizzard-apt-member

2.  https://hackread.com/us-telecom-breaches-firms-chinese-salt-typhoon-hackers/

https://www.reuters.com/world/asia-pacific/china-hacked-email-systems-us-
congressional-committee-staff-ft-reports-2026-01-08/

https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-
exploitation-of-on-premises-sharepoint-vulnerabilities/

3.  https://my.f5.com/manage/s/article/K000154696

https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign

4.  https://dev.to/lovestaco/go-undercover-code-obfuscation-with-garble-1ld6

5.  https://www.verizon.com/business/resources/reports/dbir/

6.  https://industrialcyber.co/reports/half-of-2025-ransomware-attacks-hit-critical-sectors-

as-manufacturing-healthcare-and-energy-top-global-targets/

Cloudflare | 2026 Cloudflare Threat Report

Partner Network Logo

59

Get in touch with us to learn how
to modernize your security.

1 888 99 FLARE

enterprise@cloudflare.com

www.cloudflare.com

Cloudflare | 2026 Cloudflare Threat Report This document is for informational purposes only and is the property of Cloudflare.
This document does not create any commitments or assurances from Cloudflare or its
affiliates to you. You are responsible for making your own independent assessment of
the information in this document. The information in this document is subject to change
and does not purport to be all inclusive or to contain all the information that you may
need. The responsibilities and liabilities of Cloudflare to its customers are controlled by
separate agreements, and this document is not part of, nor does it modify, any agreement
between Cloudflare and its customers. Cloudflare services are provided “as is” without
warranties, representations, or conditions of any kind, whether express or implied.

© 2026 Cloudflare, Inc. All rights reserved. CLOUDFLARE® and the Cloudflare logo
are trademarks of Cloudflare. All other company and product names and logos may
be trademarks of the respective companies with which they are associated.

1 888 99 FLARE | enterprise@cloudflare.com | Cloudflare.com

REV:BDES-8830.2026MARCH2