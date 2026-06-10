# Cloudflare Threat Report 2026

## Table of Contents
- [Executive summary](#executive-summary)
- [Key findings for 2026](#key-findings-for-2026)
- [I. Emerging attack techniques and trends](#i-emerging-attack-techniques-and-trends)
  - [MOE in the SaaS supply chain: Weaponizing connective tissue](#moe-in-the-saas-supply-chain-weaponizing-connective-tissue)
  - [MOE in AI: From productivity tool to automated exploit vector](#moe-in-ai-from-productivity-tool-to-automated-exploit-vector)
  - [Case study: Deconstructing the OpenCode exploit chain through vulnerability analysis](#case-study-deconstructing-the-opencode-exploit-chain-through-vulnerability-analysis)
  - [MOE in cloud resources: Living off the XaaS (LotX)](#moe-in-cloud-resources-living-off-the-xaas-lotx)
  - [Key LotX findings across tracked threat actor groups](#key-lotx-findings-across-tracked-threat-actor-groups)
  - [The industrialization of insider threats](#the-industrialization-of-insider-threats)
- [II. Nation-state analysis](#ii-nation-state-analysis)
  - [Russia: Blurring the line between digital espionage and operational support](#russia-blurring-the-line-between-digital-espionage-and-operational-support)
  - [China: A sophisticated model of infrastructure pre-positioning and cloud-native stealth](#china-a-sophisticated-model-of-infrastructure-pre-positioning-and-cloud-native-stealth)
  - [North Korea: Identity-driven infiltration and analytical parasitism](#north-korea-identity-driven-infiltration-and-analytical-parasitism)
  - [Iran: High-level credential theft and lateral movement via compromised government infrastructure](#iran-high-level-credential-theft-and-lateral-movement-via-compromised-government-infrastructure)
- [III. Cybercrime](#iii-cybercrime)
  - [The phishing factory: From low-friction links to industrialized supply chain sabotage](#the-phishing-factory-from-low-friction-links-to-industrialized-supply-chain-sabotage)

---

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

- **AI is automating high-velocity attacker operations**: The primary metric for risk in 2026 is the Measure of Effectiveness — the ratio of attacker effort to operational outcome. The accessibility of generative AI significantly lowers the barrier to entry for highly effective operations.
- **State-sponsored pre-positioning is compromising critical infrastructure resilience**: Chinese threat actors, notably Salt Typhoon and Linen Typhoon, are prioritizing North American telecommunications, government, and IT services for persistent pre-positioning.
- **Over-privileged SaaS integrations are expanding the blast radius of attacks**: In 2026, a single over-privileged SaaS-to-SaaS connection can be weaponized via AI to trigger surgical, multi-tenant breaches across entire ecosystems simultaneously.
- **Adversaries are subverting service ecosystems to mask attacks**: Threat actors are weaponizing legitimate cloud ecosystems (SaaS, IaaS, and PaaS) to camouflage malicious actions within benign enterprise operations.
- **Deepfake personas are embedding adversarial operatives within Western payrolls**: The industrialization of fraudulent identities now allows state-sponsored operatives to embed themselves directly into Western payrolls.
- **Token theft is neutralizing multi-factor authentication**: Adversaries are neutralizing standard multi-factor authentication (MFA) by transitioning from “attacking the box” to “attacking the session.”
- **Relay blind spots are enabling internal brand spoofing**: Attackers are exploiting a critical blind spot where mail servers fail to reverify a sender’s identity after a message passes through a third-party gateway.
- **Hyper-volumetric strikes are exhausting infrastructure capacity**: Hyper-volumetric distributed denial-of-service (DDoS) attacks, fueled by massive botnets like Aisuru, have established a record-breaking 31.4 Tbps baseline.

## I. Emerging attack techniques and trends

As we look toward the threat landscape of 2026, the industry must undergo a fundamental shift in how it categorizes risk. For decades, the “sophistication” of an adversary was the primary barometer for danger. Today, that metric is being replaced by a more pragmatic calculation: the Measure of Effectiveness (MOE).

MOE evaluates a threat by the ratio of attacker effort to operational outcome. This approach exploits a profound resource asymmetry, repurposing a victim’s own cloud, SaaS, and AI infrastructure to fund and execute the mission.

### MOE in the SaaS supply chain: Weaponizing connective tissue

Cloudforce One has observed an escalation in attacks targeting the integrations between third-party SaaS platforms. Through our investigation into the threat actor **GRUB1**, we have seen how a single compromise of a trusted integration — such as the Salesloft Drift connection to Salesforce — can create a dangerous ripple effect.

The GRUB1 campaign demonstrates that unsophisticated, individual actors can now execute high-impact breaches by industrializing two key phases:
1. **Automated credential discovery**: Moving from manual guessing to automated scanning of the SaaS supply chain.
2. **AI-assisted navigation**: Using large language models (LLMs) to bridge knowledge gaps in specialized software like Salesforce.

### MOE in AI: From productivity tool to automated exploit vector

The meteoric rise of AI LLMs has introduced a dual-front risk:
- **Unwitting user risk**: Vast quantities of proprietary source code, financial details, and PII are being routinely funneled into these systems, creating a "data gravity" effect.
- **Malicious threat**: This technology serves as a force multiplier for attackers, allowing them to automate the discovery and weaponization of "weird machines" in a supply chain.

### Case study: Deconstructing the OpenCode exploit chain through vulnerability analysis

![Diagram of the OpenCode exploit chain showing the interaction between the web UI, the /pty/ API, and the server URL override parameter.]

Cloudflare’s product security team conducted a vulnerability analysis of OpenCode, identifying that a malicious website could abuse the server URL override feature to achieve cross-site scripting (XSS) on `http://localhost:4096`. This, combined with the OpenCode API’s `/pty/` endpoints for spawning arbitrary local processes, allowed for remote code execution on the local system.

### MOE in cloud resources: Living off the XaaS (LotX)

The pervasive adoption of anything-as-a-service (XaaS) has been mirrored by nearly all threat actors. Cybercriminals and nation-states now routinely leverage public cloud hyperscaler resources (AWS, GCP, Azure) to blend their activities into the massive volume of legitimate cloud traffic.

**Scalability and elasticity as a weapon**:
- **Resource hijacking**: Actors exploit service quotas to spin up hundreds of high-performance GPU instances for cryptomining or as high-bandwidth jump boxes.
- **Metadata abuse**: Attackers can escalate privileges from a single vulnerable instance to full administrative control of a cloud tenant.

### Key LotX findings across tracked threat actor groups

- **FrumpyToad (Logic-based C2)**: Weaponizes Google Calendar for its cloud-to-cloud C2 loop.
- **PunyToad (Encrypted tunneling)**: Utilizes legitimate developer tools to bypass egress filtering.
- **NastyShrew (Paste site dead drop resolvers)**: Uses public “paste” sites to coordinate shifting infrastructure.
- **PatheticSlug (PaaS-ing the perimeter)**: Exploits the “reputation shield” of cloud ecosystems to mask malicious delivery.
- **CrustyKrill (SaaS-hosted phishing)**: Blends credential harvesting into common cloud hosting.

### The industrialization of insider threats

The Cloudforce One team continues to analyze the critical evolution in state-sponsored insider threats through mapping the industrialization of North Korean remote IT worker schemes. These operatives infiltrate Western organizations by leveraging fraudulent identities and AI-driven deepfakes to bypass video interviews.

## II. Nation-state analysis

The modern threat landscape from state and state-aligned actors is increasingly defined by the maturation and tactical synchronization of cyber operations with kinetic and geopolitical objectives.

### Russia: Blurring the line between digital espionage and operational support

Russian cyber threats operate under a high-frequency, broad targeting model.
- **NastyShrew**: Focused on high-frequency persistence and the disruption of Ukrainian critical infrastructure.
- **StainedShrew**: Highly active in targeting events of perceived geopolitical importance (e.g., NATO summits).
- **RottenShrew**: Functions as a specialized reconnaissance unit, geolocating military personnel likely to be followed by kinetic action.

### China: A sophisticated model of infrastructure pre-positioning and cloud-native stealth

Chinese actors are prioritizing the long-term compromise of critical edge devices and telecommunications backbones.
- **ClumsyToad**: High-frequency regional espionage using localized lures and USB-borne worms like SnakeDisk.
- **PunyToad**: Specializes in the exploitation of edge network appliances (F5 BIG-IP, VMware vCenter) for persistent pre-positioning.
- **FrumpyToad**: Utilizes LotX tactics to blend C2 traffic into legitimate enterprise ecosystems.

### North Korea: Identity-driven infiltration and analytical parasitism

North Korea has industrialized the use of generative AI, deepfakes, and analytical parasitism.
- **PutridSlug**: Uses deepfake video and audio to impersonate executives and deploys trojanized coding challenges.
- **PatheticSlug**: Focuses on analytical parasitism, posing as journalists to gather off-the-record insights.
- **FoolishSlug**: The most tactically aggressive group, utilizing an espionage-ransomware hybrid model to fund the regime.

### Iran: High-level credential theft and lateral movement via compromised government infrastructure

Iranian actors integrate digital espionage with kinetic military objectives.
- **MuddyKrill**: Integrates digital reconnaissance with physical targeting, including hijacked CCTV surveillance.
- **ConvolutedKrill**: Credential-theft specialist that leverages compromised government accounts to exploit regional trust.
- **CrustyKrill**: Uses high-touch social engineering and recruitment lures to compromise victims.

## III. Cybercrime

From record-breaking DDoS attacks peaking at an unprecedented 31.4 Tbps to the identification of over $123 million in explicit financial lures, cybercriminals in 2025 demonstrated a relentless move toward high-velocity, automated exploitation.

### The phishing factory: From low-friction links to industrialized supply chain sabotage

Link-based phishing remains the dominant threat vector. Our analysis of 450 million emails reveals that nearly 43% failed SPF, over 44% lacked valid DKIM signatures, and 46% failed DMARC.

**The Shai-Hulud 2.0 supply chain campaign**:
This campaign weaponized the Node package manager (npm) ecosystem through a single phished developer. By gaining access to a maintainer’s tokens, attackers deployed a self-replicating worm that injects malicious preinstall scripts into every package the victim maintains, creating a massive ripple effect across the software supply chain.

[^1]: Joint operation involving US and Thai authorities, February and November 2025.
[^2]: Breach of AT&T, Verizon, Lumen, and the July 2025 Microsoft SharePoint compromise.
[^3]: PunyToad exploitation of F5 and VMware vCenter and ESXi.
[^4]: BRICKSTORM malware, often obfuscated with Garble.

---

Threat Report 3366
Industrialized PhaaS
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
Advertisement for a PhaaS
mailer bot on Telegram

Cloudflare | 2026 Cloudflare Threat Report 37
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
Compromise / Social Fraudulent The reveal
spoofing engineering invoice
Scam is uncovered
External Attackers use Fake invoice is when the real
partner’s email is urgency and issued for up-front invoice arrives
compromised emotional or “urgent” payment
or spoofed manipulation
BEC lifecycle

Cloudflare | 2026 Cloudflare Threat Report 38
Pig butchering: How scammers weaponize emotional
trust and wealth personas to drain life savings
The Cloudforce One team has observed a number of
4.
Defensive redirection
“pig butchering” scams in 2025. Pig butchering (known
as shāzhūpán) is a sophisticated long-con investment
The example below demonstrates defensive
scam that originated in the People’s Republic of China
redirection, as the potential victim successfully
and is a metaphor for the agricultural practice of
deflects a grooming attempt. The interaction highlights
fattening up a pig before slaughter; scammers build
the strategic ways scammers attempt to integrate
intense emotional trust with a victim over weeks or
themselves into a victim’s daily schedule.
months (“fattening”) before stealing their life savings
through a fraudulent investment platform (“butchering”).
1.
A classic “wrong number” introduction
Pig butchering begins with a lure, where scammers
initiate contact via “wrong number” text messages
or social media to build initial rapport. The scammer
often uses a benign “Hey” to bait a response and then 5. A fake exchange
apologizes for the “mistake” to launch a conversation.
Once trust is solidified, the scam moves to the
fraudulent exchange phase. Victims are directed
to deposit cryptocurrency into fake exchanges that
report deceptive, “amazing” gains to encourage further
investment before the victim is ultimately prevented
from withdrawing any funds. Victims that request their
funds will be asked to send in more funds to cover
“fees” or “taxes.”
2.
The “wealth persona” lure
Following this initial contact,
the grooming phase begins.
Our analysts have noted the
use of wealth personas,
where scammers share
photos featuring luxury items
like high-end watches to
establish themselves as
successful investors.
Recovering any of the stolen money is difficult, if not
impossible. In some cases, the cryptocurrency can
be traced to an exchange and a legal authority can
3. M oving to Telegram compel the exchange to return the funds to a victim.
In most cases, the funds are quickly laundered so
To evade security filters that the legal approach is less effective. Throughout
and deepen the grooming 2026, we anticipate that the grooming phase will
process, attackers force a become increasingly automated through LLM-
platform migration, moving powered personas. This artificial intimacy allows
victims to unmonitored a single operative to “fatten” hundreds of victims
messaging apps like Telegram. simultaneously with highly personalized, AI-generated
emotional lures that are virtually indistinguishable from
human interaction.

Cloudflare | 2026 Cloudflare Threat Report 3399
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

Cloudflare | 2026 Cloudflare Threat Report 40
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

CClloouuddffllaarree || 22002266 CClloouuddffllaarree TThhrreeaatt RReeppoorrtt 41
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

Cloudflare | 2026 Cloudflare Threat Report 42
The triple-threat bot chain: From identity breach
to host compromise to disruption
The sheer scale of automated traffic is a pervasive proxy services. This makes malicious traffic look like it
threat to organizations globally, with approximately 30% is originating from legitimate users, allowing attackers
of all HTTP traffic Cloudflare observes originating from to systematically test defenses from the network layer
bots. While some of this is benign — such as search up to the application layer while remaining below the
engine crawlers — a significant portion is dedicated to radar of traditional filters.
a high-speed attack chain that bridges identity theft,
host compromise, and service disruption. Heading into 2026, we expect the use of successor
networks like Kimwolf to continue expanding, making
this residential-proxy tunneling the default operational
Bot vs. human baseline for evading IP-based filters.
Bot (automated) vs. human HTTP
Bots as the engine of
requests distribution
identity exploitation
The chain begins with automated account takeover
Bot
(ATO), where bots weaponize compromised credentials
29.9%
at industrial scale. This process is fed by a circular
ecosystem of harvesting sites and infostealers like
Qakbot and Emotet. These bots do not simply look
for vulnerabilities in the traditional sense; they exploit
human behavior, specifically the fact that 63% of all
Human
70.1% human logins involve credentials that have already
been compromised elsewhere.
Attackers use bots to test stolen username and
password pairs across thousands of sites per second.
The scale is staggering, as Cloudflare data shows
that 94% of all login attempts originate from bots.
Cloudforce One tracks these malicious bots not as To bypass modern detection, attackers use tools
isolated scanners, but as a continuous lifecycle. This like Selenium and Puppeteer to mimic human mouse
chain relies on massive, distributed botnets — such movements and realistic scrolling, allowing them
as Aisuru and its successor Kimwolf — which mask to bypass traditional session intelligence during a
the source of attacks by tunneling through residential credential stuffing assault.
of all HTTP of all human logins of all login
30% 63% 94%
traffic Cloudflare involve credentials attempts
observes that have already originate
originates been compromised from bots
from bots elsewhere

Cloudflare | 2026 Cloudflare Threat Report 43
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

Cloudflare | 2026 Cloudflare Threat Report 44
DDoS attacks by year and type
50.0 M
40.0 M
30.0 M
20.0 M
10.0 M
0.0 M
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
skcatta
SoDD
HTTP DDoS attacks Network-layer DDoS attacks
47.1 M
12.7 M
34.4 M
21.3 M
9.9 M
14.0 M
5.2 M
11.4 M
8.7 M
2023 2024 2025
Year
In 2025, the total number of DDoS attacks
observed by Cloudflare more than doubled.

Cloudflare | 2026 Cloudflare Threat Report 45
World record DDoS attacks
September 2024 3.8 Tbps
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
Hyper-volumetric DDoS attacks continue to grow in size and frequency
htnoM
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
0.0 Tbps 10.0 Tbps 20.0 Tbps 30.0 Tbps 40.0 Tbps
Max rate (Tbps)
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

Community
IV.
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

Cloudflare | 2026 Cloudflare Threat Report  4477
LAYOUT
Americas
OPTION 1
The Americas, particularly the United States, remains the most targeted
region globally by volume. Threat activity in the Americas is primarily
characterized by highly sophisticated state-sponsored pre-positioning
and a pervasive, industrial-scale ransomware ecosystem.
Primary actors
Primary threat actors
Key concerns
| C  allowDuck | S  leezyShrew |     |
| ------------ | ------------- | --- |

| Alias / AKA:   | Alias / AKA:   |     |
| -------------- | -------------- | --- |
Identity-first intrusions
| Scattered Spider  | APT29 |     |
| ----------------- | ----- | --- |
Identity abuse has now
Focus: Identity and access  Focus: Government, think tanks,   superseded network exploitation
management (IAM) abuse and cloud service providers as the primary vector for initial
access. Threat actors have moved
| Context: They are the premier  | Context: This group has shifted  |     |
| ------------------------------ | -------------------------------- | --- |
away from “attacking the box” and
| example of the shift from malware  | heavily toward cloud-based targets,  |     |
| ---------------------------------- | ------------------------------------ | --- |
are now focused on “attacking the
| to identity abuse. They utilize  | utilizing sophisticated session  |     |
| -------------------------------- | -------------------------------- | --- |
sophisticated social engineering  hijacking and token theft to maintain  session,” prioritizing credential
(vishing) and MFA fatigue to  access to sensitive communications.  theft, session hijacking, and the
compromise cloud environments.  They focus on long-term persistence  systematic bypassing of MFA.
They are highly disruptive to major  (e.g., in Microsoft 365 environments)  By weaponizing compromised
US enterprise and hospitality sectors  and supply chain compromises (e.g.,  identities, attackers can navigate
(e.g., MGM / Caesars). SolarWinds). cloud environments and enterprise
systems with the appearance of
legitimacy, bypassing the need for
traditional malware.
F  rumpyToad
|     | DazedToad | Infrastructure pre-positioning   |
| --- | --------- | -------------------------------- |
The shift from data theft to

Alias / AKA:   Alias / AKA:   operational persistence in critical
| APT41 | Volt Typhoon | utilities suggests attackers are  |
| ----- | ------------ | --------------------------------- |
preparing for disruptive events
Focus: State espionage and private  Focus: Critical infrastructure  rather than just espionage.
| financial gain | (energy, water, communications,  |                              |
| -------------- | -------------------------------- | ---------------------------- |
|                | transportation)                  | Ransomware service maturity  |
Context: Known for software supply
chain attacks, they target US  Context: Unlike traditional espionage,  The professionalization of
healthcare, tech, and retail sectors  this group focuses on pre-positioning  ransomware-as-a-service (RaaS)
for both intellectual property and  for potential future sabotage. They  means even lower-tier affiliates
personal profit. are masters of LotL, using built-in  can execute high-impact attacks
|     | network tools to maintain long- | using sophisticated playbooks. |
| --- | ------------------------------- | ------------------------------ |
term persistence without triggering
traditional malware alerts.
| C  loyingKrill | Q  ilin, Akira, and Play |     |
| -------------- | ------------------------ | --- |
|                |                          |     |
| Alias / AKA:   | Ransomware proliferation |     |
APT33
Focus: Financial extortion through
| Focus: Aerospace, defense,   | double extortion (data theft and   |     |
| ---------------------------- | ---------------------------------- | --- |
| and petrochemical sectors    | encryption); leads attacks on the  |     |
telecom and healthcare sectors
Context: A primary arm of Iranian
| state-sponsored activity. They        | Context: These groups represent      |     |
| ------------------------------------- | ------------------------------------ | --- |
| target defense contractors to narrow  | the industrialized wing of           |     |
| military technology gaps and gather   | cybercrime. Akira and Play often     |     |
| regional intelligence.                | exploit unpatched VPNs, while Qilin  |     |
is known for aggressive name-and-
shame tactics.

Cloudflare | 2026 Cloudflare Threat Report  48
Europe, Middle East,
and Africa (EMEA)
Europe is the second most targeted region, with 22% of global extortion
victims located there. The EMEA landscape remains the primary theater
for disruptive cyber operations linked to the war in Ukraine and shifting
power dynamics in Eastern Europe and the Middle East.
Primary threat actors
| Z  apoyShrew | M  uddyKrill |     |
| ------------ | ------------ | --- |
Key concerns
|               |               |     |
| ------------- | ------------- | --- |
| Alias / AKA:  | Alias / AKA:  |     |
Targeted critical infrastructure
| APT44 | MuddyWater |     |
| ----- | ---------- | --- |
Organizations in energy, finance,
Focus: Destructive operations and  Focus: Regional geopolitics and  or logistics face an elevated risk of
critical infrastructure sabotage telecommunications being targeted as part of broader
geopolitical pressure campaigns.
| Context: This group is responsible  | Context: This group targets     |     |
| ----------------------------------- | ------------------------------- | --- |
| for grid attacks in Europe and the  | government and private sectors  |     |
Wiper malware spillover
| widespread use of high-profile   | across the Middle East (Israel, Saudi  |     |
| -------------------------------- | -------------------------------------- | --- |
Destructive tools intended for
| wiper malware. | Arabia, UAE) and Southern Europe  |     |
| -------------- | --------------------------------- | --- |
regional conflicts often possess
for espionage and regional influence.
self-propagating capabilities that
can inadvertently impact global
supply chains.
Political hacktivism
Hacktivists are responsible for
almost 80% of recorded incidents
in the EU, primarily using
| I ncoherentShrew | R  untZander | DDoS attacks to target public  |
| ---------------- | ------------ | ------------------------------ |
administration and banking.
|               |                |     |
| ------------- | -------------- | --- |
| Alias / AKA:  | Alias / AKA:   |     |
Industrial extortion
| APT28 | White Lynx |     |
| ----- | ---------- | --- |
Ransomware accounts for over
Focus: Political and military  Focus: Information operations (IO)  38% of incidents in the EU
espionage and hack-and-leak campaigns aimed  transport sector.
at neighbors of Belarus, including
Context: Heavily involved in
|     | Poland, Germany, Latvia, and  | Weaponized disinformation   |
| --- | ----------------------------- | --------------------------- |
disinformation campaigns and leak
|                                  | Lithuania, with targeting focused   | The combination of data leaks  |
| -------------------------------- | ----------------------------------- | ------------------------------ |
| sites (hack-and-leak) targeting  | on government and media             |                                |
and AI-enhanced disinformation
European parliaments and NATO-
makes it increasingly difficult
| aligned entities. | Context: Closely aligned with  |     |
| ----------------- | ------------------------------ | --- |
for organizations to defend
Belarusian and Russian interests,
their brand reputation during
this group specializes in stealing
regional crises.
and leaking sensitive data to
influence local elections or damage
political figures.

Cloudflare | 2026 Cloudflare Threat Report  49
Asia-Pacific (APAC)
The APAC region faces a unique blend of high-tech espionage and
large-scale financial theft. Threat activity in APAC is also dominated by
actors supporting the Belt and Road Initiative and territorial claims in
the South China Sea. There is a heavy focus on maritime intelligence
and compromise of core network infrastructure to enable broad-scale
monitoring and pre-positioning for future conflicts.
Primary threat actors
| DazedToad | WorthlessSlug | Key concerns |
| --------- | ------------- | ------------ |

|               |               |                             |
| ------------- | ------------- | --------------------------- |
| Alias / AKA:  | Alias / AKA:  | Network backbone compromise |
Volt Typhoon Diamond Sleet The targeting of ISPs and network
edge devices (Salt Typhoon)
Focus: Critical infrastructure and   Focus: Cryptocurrency and   means that traffic thought to be
OT pre-positioning financial systems secure could be intercepted before
it even reaches its destination.
| Context: Utilizes LotL techniques  | Context: While global, their activity  |     |
| ---------------------------------- | -------------------------------------- | --- |
| to maintain long-term, undetected  | in APAC is intense, targeting          |     |
access to regional military and   regional exchanges and financial  Economic and maritime espionage
utility infrastructure. hubs (Singapore / Japan) to  High-tech manufacturing and
generate hard currency for the   maritime industries are at extreme
|     | North Korean regime. | risk of IP theft aimed at closing  |
| --- | -------------------- | ---------------------------------- |
competitive gaps in regional
industrial capabilities.
| SoggyToad | ClumsyToad  |     |
| --------- | ----------- | --- |
Supply chain and IT targeting
|                |               | The information technology and  |
| -------------- | ------------- | ------------------------------- |
| Alias / AKA:   | Alias / AKA:  | semiconductor sectors are the   |
| APT40          | Mustang Panda | most targeted industries in     |
the region.
| Focus: Maritime and naval technology | Focus: Southeast Asian  |                               |
| ------------------------------------ | ----------------------- | ----------------------------- |
|                                      | governments and         | Stealthy persistence (LotL)   |
Context: This group focuses
|     | international nonprofits | The widespread use of LotL  |
| --- | ------------------------ | --------------------------- |
specifically on targets in the
APAC region that have strategic  Context: Focuses on entities involved  techniques makes it exceptionally
relevance to the South China Sea,  in South China Sea policy, often using  difficult to differentiate between
including regional governments and  lure documents related to regional  a legitimate administrator and a
engineering firms. summits and diplomatic events. state-sponsored actor.
Summit espionage
Major 2026 diplomatic events
(ASEAN in the Philippines, APEC in
W  impyToad
China) are prime targets for state-
|     |     | backed intelligence gathering. |
| --- | --- | ------------------------------ |

Alias / AKA:
Salt Typhoon
Focus: Telecommunications
infrastructure and service providers
Context: Specializes in
compromising the core of the
Internet — ISP routers and telecom
switches — to intercept vast
amounts of data at the source.

Cloudflare | 2026 Cloudflare Threat Report 5500
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
• China-aligned actors (e.g., FrumpyToad, DazedToad): While heavily focused on APAC
(Taiwan / South China Sea), they simultaneously target Americas and EMEA for intellectual
property theft and pre-positioning in critical infrastructure.
• Russia-aligned actors (e.g., IncoherentShrew, SleezyShrew): Historically focused
on EMEA and the Americas, they increasingly overlap into APAC to monitor shifting
diplomatic alliances.
Cybercrime big game hunting
Cybercriminal syndicates (RaaS) are almost entirely region-agnostic. They target revenue,
not geography.
• Overlap pattern: A ransomware group might hit a logistics firm in Germany (EMEA) on
Monday and an insurance provider in Brazil (Americas) on Tuesday.
• IABs: These actors sell access to networks globally. An IAB based in Eastern Europe might
sell access to a Japanese manufacturing plant (APAC) to a ransomware affiliate based in
the Americas.
Supply chain and shared technology stacks
Because many global enterprises use the same software (Microsoft Office, Salesforce CRM,
vSphere, etc.), a single vulnerability creates a global overlap.
The vulnerability sprint: When a zero-day is released (e.g., React2Shell), actors across all
regions rush to scan the global IP space, often with the help of attack surface management
tools which are typically helping attackers more than defenders. This creates a noise floor of
activity that overlaps every region simultaneously.

Cloudflare | 2026 Cloudflare Threat Report  5511
Specific examples of regional overlap
Several advanced persistent threat (APT) groups serve as primary examples of adversaries with a global reach,
systematically targeting organizations across the Americas, EMEA, and APAC regions. These groups often align
their operations with geopolitical objectives or large-scale financial theft.
Key exemplars of multi-regional threat actors include:
| N  ervousToad   | L azarus group  | C  lumsyToad   |
| --------------- | --------------- | -------------- |
|                 |                 |                |

|     |     |     |
| --- | --- | --- |
Alias / AKA:
|        | Alias / AKA:  | Alias / AKA:   |
| ------ | ------------- | -------------- |
| APT27  | Hidden Cobra  | Mustang Panda  |
A prominent group that consistently  A sophisticated group of actors  Highly active group that utilizes
targets headquarters worldwide. Its  known for their immense geographic  diverse techniques like spear-
operations span North and South  reach and diverse motives,  phishing and DLL sideloading across
America, Europe, and the Middle  including financial gain through  a vast geographic footprint. In 2026,
East, focusing on sectors such   cryptocurrency theft and strategic  its activity was noted in the United
| as aerospace, government, and high   | sabotage. It maintains an active  |     |
| ------------------------------------ | --------------------------------- | --- |
States, Europe, and extensively
tech to conduct long-term espionage.
|              | presence in North America, Europe,  | across APAC countries including       |
| ------------ | ----------------------------------- | ------------------------------------- |
|              | and Asia.                           | Australia, India, Japan, and Vietnam. |
| SleezyShrew  | C  loyingKrill                      | L  ockBit and                         |
|              |                                     |                                       |
|              |                                     | similar ransomware                    |
|              |                                     |                                       |

s yndicates
| Alias / AKA:  | Alias / AKA:  |     |
| ------------- | ------------- | --- |

| APT29  | APT33  |     |
| ------ | ------ | --- |
While often criminal rather than
| A group that operates globally to  | An actor that illustrates a broad  |     |
| ---------------------------------- | ---------------------------------- | --- |
state-sponsored, these groups
| support Russian foreign policy. It  | operational scope, targeting critical  |     |
| ----------------------------------- | -------------------------------------- | --- |
function as enterprise cybercriminals
| targets government and diplomatic  | infrastructure in the United States  |     |
| ---------------------------------- | ------------------------------------ | --- |
with global reach. They target
| entities across North America,  | (Americas), Saudi Arabia (Middle  |     |
| ------------------------------- | --------------------------------- | --- |
large-scale enterprises across every
| Europe, and other regions opposing  | East / EMEA), and South Korea  |     |
| ----------------------------------- | ------------------------------ | --- |
major economic region, including
| Russian interests. | (APAC), with a specific focus on the  |     |
| ------------------ | ------------------------------------- | --- |
the Americas, EMEA, and APAC,
energy and aviation sectors.
prioritizing high-value critical
infrastructure for double and
triple extortion.

Cloudflare | 2026 Cloudflare Threat Report 52
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

Cloudflare | 2026 Cloudflare Threat Report 53
Analytical implications
The regional overlaps detailed in this report have three critical implications for global
threat analysis:
• Cross-regional lateral movement: A local incident is rarely isolated. Adversaries frequently
utilize a breach in an EMEA or APAC branch as a low-friction testing ground or staging
point for lateral movement into an Americas-based headquarters. Security teams must
adopt a unified global response model to prevent cross-regional escalation.
• Strategic infrastructure proxying: Threat actors increasingly utilize geographic proxying
to complicate attribution and circumvent geofencing. We frequently observe Americas-
based actors leasing EMEA-based VPS infrastructure to target APAC entities. Effective
tracking now requires monitoring cross-regional routing patterns rather than relying on
simple IP-origin telemetry.
• Temporal vulnerability exploitation (time-zone arbitrage): Adversaries strategically
leverage regional blind spots by conducting high-intensity activity during the weekends
or national holidays of the target region. By initiating operations when local defensive
capacity is reduced but the attacker’s home region is in a standard business day, they
significantly maximize their dwell time and operational success rate.

Recommendations
V.
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

Cloudflare | 2026 Cloudflare Threat Report 55
1 2
Focus AI security efforts on Transition from MFA to identity-
securing workforce AI usage first zero trust
Prioritize securing how employees interact Since infostealers like LummaC2 now harvest
with LLMs to prevent AI-assisted navigation by session tokens to bypass MFA, organizations
attackers. Implement strict data loss prevention must move beyond simple one-time codes.
(DLP) for AI prompts and deploy browser- Implement phishing-resistant MFA (FIDO2
isolated environments for generative AI tools / passkeys) and continuous monitoring that
to ensure corporate keys to the kingdom aren’t invalidates sessions instantly if impossible
inadvertently leaked into model training sets or travel or suspicious device fingerprints (like
captured by infostealers. mouse-jiggling software) are detected.
3 Harden the SaaS-to-SaaS connective tissue
The GRUB1 campaign proves that a single compromise of a trusted
integration can create a dangerous ripple effect. Conduct an
immediate audit of all SaaS API permissions. Apply the principle
of least privilege to integrations, specifically looking for over-
privileged read / write tokens in tools like Salesforce, Slack, and
GitHub that could allow an attacker to pivot between clouds.
4 5
Implement human-in-the-loop Adopt autonomous, hyper-
verification for remote hiring volumetric DDoS defenses
To counter the industrialized North Korean insider With the Aisuru botnet pushing attacks
threat, move away from purely digital onboarding. to a 31.4 Tbps new baseline, the window
Use zero trust biometric verification for all remote for human intervention has closed.
video interviews and enforce strict hardware- Organizations must shift to automated,
based geofencing. Corporate laptops should be edge-based mitigation that can respond in
cryptographically paired to the user’s physical seconds. Legacy scrubbing center models
location to neutralize “laptop farm” facilitators. are no longer sufficient for attacks that
peak and conclude within 10 minutes.
Isolate peripheral infrastructure Eliminate email blind spots with
6
to contain exposure AI-first security
To establish a robust defensive posture, PhaaS bots can rapidly bombard organizations
organizations must implement a strategic with emails leveraging polymorphic tactics
shift in how they manage IaaS and SaaS that bypass legacy secure email gateways.
dependencies. Specifically, subsidiary Organizations must adopt AI-first email security
and supporting services should operate capable of interpreting these shifting variables
independently, utilizing dedicated domain and adapting to both incoming and lateral
names, unique IP addresses, and, where threats. By utilizing signals beyond the email
feasible, distinct autonomous system inbox, these systems can better identify and
numbers (ASNs). neutralize internal compromised accounts in
real time.
7

Cloudflare | 2026 Cloudflare Threat Report  56
Cloudforce One overview
| Threat intelligence | Managed defense | Cyber response   |
| ------------------- | --------------- | ---------------- |
and readiness
| Gain access to Cloudflareʼs  | Receive 24 / 7 expert  |     |
| ---------------------------- | ---------------------- | --- |
global threat visibility with  monitoring and proactive  Deploy hands-on experts
| a powerful package of  | threat detection across your  |     |
| ---------------------- | ----------------------------- | --- |
to neutralize active threats,
threat intelligence tooling  Cloudflare stack, ensuring  conduct forensic analysis, and
and expertise to make your  continuous protection and  minimize operational impact.
| organization smarter, more  | rapid response to issues. |     |
| --------------------------- | ------------------------- | --- |
responsive, and more secure.
| Learn more | Learn more | Learn more |
| ---------- | ---------- | ---------- |
Contact Cloudforce One security experts
Subscribe to our threat research

Cloudflare | 2026 Cloudflare Threat Report 57
Modernize your security with Cloudflare
One security platform. Network to cloud. Apps to Al.
App to network layer Inbound and outbound
• Web App 8, API • Secure access service
protection (WAAP) edge (SASE)
• Security service • Network as a service
edge (SSE) (NaaS) and multicloud
• DDoS Protection • Network Interconnect
Al-powered protection Secure Al workloads
• Email Security • Al Gateway
• Bot Management • Firewall for Al
• Platform simplified • Critical infrastructure
with Al agents trusted to run Al
Cloudflare’s one security platform scales seamlessly from network to
cloud, and protects all users and data across applications and Al. It
With Cloudflare,
leverages an intelligent and programmable global cloud network to unify
customers can realize:
a range of diverse technologies, harnesses Al-powered threat intelligence
to deliver low-touch, high-efficacy protection, and Al-powered data loss
prevention detections to distributed organizations of all sizes. 24%
Secure inbound and outbound traffic from network to application breach risk reduction
layer, to increase consistency and coverage across distributed IT across the enterprise
environments with existing teams and budget.
Secure Al workloads from models to inference, to increase Al 35%
adoption with secure, reliable inference and protected, clean
time savings on security
data for trusted Al models.
and DNS management
Al-powered protection and observability fueled by our global
network scale reduces the mean time to detect, respond, and
250
mitigate future critical incidents.
Cloudflare offers an integrated approach to security modernization, hours of avoided downtime
simplifying deployment, enhancing visibility, and reducing the TCO
while eliminating the multiple vendors and tools required with traditional,
227%
fragmented solutions. By delivering security close to the end user and
requested resource, Cloudflare ensures resiliency and broad protection
ROI of Cloudflare over
against evolving threats.
three years
The result: One security platform. Network to cloud. Apps to Al.
Source: Forester TEI study

Cloudflare | 2026 Cloudflare Threat Report 5588
Endnotes
1. https://www.nhpr.org/2025-11-21/russian-hacking-suspect-wanted-by-the-fbi-arrested-
on-thai-resort-island
https://therecord.media/russian-arrested-thailand-allegedly-void-blizzard-apt-member
2. https://hackread.com/us-telecom-breaches-firms-chinese-salt-typhoon-hackers/
https://www.reuters.com/world/asia-pacific/china-hacked-email-systems-us-
congressional-committee-staff-ft-reports-2026-01-08/
https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-
exploitation-of-on-premises-sharepoint-vulnerabilities/
3. https://my.f5.com/manage/s/article/K000154696
https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign
4. https://dev.to/lovestaco/go-undercover-code-obfuscation-with-garble-1ld6
5. https://www.verizon.com/business/resources/reports/dbir/
6. https://industrialcyber.co/reports/half-of-2025-ransomware-attacks-hit-critical-sectors-
as-manufacturing-healthcare-and-energy-top-global-targets/

Cloudflare | 2026 Cloudflare Threat Report 59
Partner Network Logo
Get in touch with us to learn how
to modernize your security.
1 888 99 FLARE
enterprise@cloudflare.com
www.cloudflare.com

This document is for informational purposes only and is the property of Cloudflare.
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
1 888 99 FLARE | enterprise@cloudflare.com | Cloudflare.com REV:BDES-8830.2026MARCH2