April 2026 | Vol. 7
Phishing Threat
Trends Report

How AI is Redefining
the Phishing Frontier What’s Inside
2026 is off to a relentless start. The threat 03 Opening Stats
landscape is maturing rapidly, bringing new
actors, novel tactics, and classic attacks
05 Attacker Attribution:
supercharged by AI at scale.
Unmasking the Adversary
Our 7th Phishing Threat Trends Report delivers Understand how adversaries operate
actionable intelligence on this evolution. at scale, from trends to specific tactics
Modern phishing has transcended simple social
engineering; today’s attackers ruthlessly exploit
12 Teams Phishing: The Inbox
platform trust and manipulate systems
is No Longer the Only Frontline
to guarantee a return on investment.
How are threat actors exploiting the unique
This report dives deep into the diverse trust gap associated with Microsoft Teams?
approaches of advanced persistent threats
(APTs) and criminal groups. We explore the rise
18 Adversary-in-the-Middle (AiTM):
of multi-channel attacks targeting collaboration
The Stealthy New Standard
tools, and the mainstream adoption of
The sophisticated attack strategy that
Adversary-in-the-Middle (AiTM) and reverse
bypasses MFA to hijack accounts
proxies in criminal toolkits.
The message is clear: phishing in 2026 is
22 The Agentic Shift: Anticipating the
disciplined, persistent, and increasingly AI-
Era of AI-Driven Threats
enabled. We hope these insights help you
Understand how attackers are leveraging
navigate this shifting frontier.
agentic tools to scale high-fidelity threats
Unless otherwise stated, all statistics have
been generated from KnowBe4’s Collaboration
29 Calendar Invites: Infiltrating the
Security products. As always, please reach out
Corporate Schedule
if you have any questions or want to learn more
Attackers have shifted from the scrutinized
about how Knowbe4 stops these threats.
inbox to the quiet sanctuary of the
corporate calendar
32 2026 Intelligence Brief:
Jack Chapman Ask the Experts
Your questions answered about phishing
SVP of Threat Intelligence, KnowBe4
in 2026
35 Wrapping Up: Staying One Step
Ahead in a Shifting Landscape
36 Contributors
Copyright © 2026 KnowBe4 All Rights Reserved. 2

Opening Stats

Opening Stats
(continued)

Attacker Attribution:
Unmasking the Adversary
Cybersecurity professionals often struggle to address two critical
questions: who is attacking my organization, and why?
Answering these questions is the foundation of proactive threat intelligence, allowing defenders to anticipate
campaigns rather than just react to them. Yet, achieving this in the email space is notoriously difficult. Unlike
malware analysis, which leaves concrete forensic artifacts, email is inherently transient. Attackers constantly rotate
spoofed domains, sender IPs, and burner accounts to remain anonymous.
To overcome this, we have moved beyond tracking easily changed indicators and shifted our focus to the
attackers’ actual behaviors. We combine a broad range of unique intelligence and detection data to provide
enhanced visibility into adversary operations, basing our attribution on how these groups operate rather than on
perishable data. This approach provides insight into geographic origins, industry targets, and end-to-end evasion
strategies that bypass traditional defenses.
Applying this attribution methodology to the 2026 landscape brings the modern threat ecosystem into sharp
focus. The following intelligence reveals exactly how adversaries operate at scale — from broad operational trends
down to the precise tactics used by some of 2026’s most active Advanced Persistent Threats (APTs).
Timing Is Everything
Examining these broad trends begins with the realization that modern threat actors operate on standard
corporate schedules. The outdated stereotype of attacks occurring randomly in the middle of the night has
been replaced by calculated precision. Today’s adversaries strategically align their campaign launches with
the natural ebb and flow of the business day.
Attacks Started by Hour of Day - Q1 2026
5k
4k
3k
2k
1k
0
0 5 10 15 20
detratS
skcattA
fo
rebmuN
Peak Attack Volume
17:00
(5:00 PM)
RED ZONE
Hour of Day (24-Hr Clock)
Copyright © 2026 KnowBe4 All Rights Reserved. 5

Ask The Expert
James Dyer
Head of Threat Intelligence
We are often asked, “When do people get attacked?”
X We noticed a distinct increase in the number of attacks starting after lunch, with the volume
beginning to surge around 1:00 PM (13:00) and accelerating rapidly until the peak at 5:00 PM (17:00)
with 4,119 attacks started. The volume then gradually decreases through the late evening and
overnight. This trend supports the insight that attackers are deliberately timing campaigns to target
employees when they are likely fatigued and less scrutinizing as they wrap up their workday.
While launch timing is designed to exploit human fatigue, campaign duration reveals an adversary’s technical
evasion strategy. The 2026 data highlights a clear operational divide: rapid execution versus prolonged,
sustained operations. While over 60% of campaigns attempt to overwhelm initial defenses in under 24 hours,
the most sophisticated APTs are deliberately adopting a sustained approach. By stretching their attacks across
five to ten days, these groups use a drip-feed methodology specifically engineered to bypass volumetric
security filters and exhaust defense teams.
Attack Duration Analysis Q1 2026
5k
Attackers are timing
4k
their strikes for the
3k “End-of-Day Blur,” catching
employees when
2k
cognitive load is highest
1k
and scrutiny is lowest.
0
tnuoC
ngiapmaC
TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
>10 >5 2 1 1-24 <1
days days days days hours hour
Duration Bucket
Copyright © 2026 KnowBe4 All Rights Reserved. 6

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Threat Actor Analysis
The true value of behavioral attribution lies in its ability to separate these sophisticated adversaries from
the background noise. While our researchers actively monitor over 3,000 unique threat actors, applying this
methodology to the 2026 landscape isolates the specific entities driving the macro trends outlined above.
The Threat Actor Table below profiles a curated selection of the most active APTs identified this year.
Highlighting this operational shift are groups like Basalt Harrier and Amber Shearwater. Exhibiting near-perfect
behavioral consistency, these actors demonstrate immense operational maturity. They have moved beyond
manual experimentation, instead aggressively scaling proven, automated models to execute complex use
cases like e-commerce fraud at an industrial scale.
Threat Actor Table Q1 2026
Email TTP Country Top Targeted
Alias Campaigns Attack Type
Volume Consistency of Origin Industries
USA
Generic
Finance,
37224 294 100% E-commerce
Insurance, IT
Basalt Fraud
Harrier
Latvia
Temu
IT, Healthcare,
33450 250 96.8% E-commerce
Finance
Amber Fraud
Shearwater
Nigeria
Real Estate,
BEC + Microsoft
29859 78 100% Healthcare,
Impersonation
Laterite Insurance
Magpie
Vietnam
BEC + Docusign Finance, Real
28491 461 100%
Impersonation Estate, Retail
Tektite
Vulture
Indonesia
BEC + QR Code +
Insurance, IT,
11312 254 100% Company
Finance
Sulphur Impersonation
Kestrel
Understanding an adversary requires seeing their campaigns in motion. The operational timeline below maps
the top five APTs, highlighting a clear operational divide: Amber Shearwater executes high-velocity, short-
duration strikes, whereas Sulphur Kestrel leverages prolonged, sustained operations to silently bypass security
filters. Furthermore, tracking groups like Basalt Harrier reveals densely overlapping campaigns, indicating
access to massive, enterprise-grade infrastructure.
Copyright © 2026 KnowBe4 All Rights Reserved. 7

TPihtlieshing Threat Trends Report   |  April 2026 | Vol. 7
Concurrent Campaign Analysis & Geographical Origin
Basalt
Harrier
| 37,224 msgs |     | 14.8k | 5.1k |     | 4.1k |     | 1.3k |
| ----------- | --- | ----- | ---- | --- | ---- | --- | ---- |
|             |     | 9.7k  |      |     | 2.2k |     |      |
Amber
Shearwater
33,450 msgs
|     | 19.8K |     |     | 10.1K |     |     | 3.5K |
| --- | ----- | --- | --- | ----- | --- | --- | ---- |
Laterite
Magpie
29,859 msgs
|     |     | 24.8k | 4.2k |     |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- | --- |
888
Tektite
Vulture
|     |     | 6.9k |     | 2.1k |     | 931 |     |
| --- | --- | ---- | --- | ---- | --- | --- | --- |
28,491 msgs
481
18.1k
Sulphur
Kestrel
| 11,312 msgs |     | 4k  |     |     | 2.6k |     | 1.3k |
| ----------- | --- | --- | --- | --- | ---- | --- | ---- |
3.5k
|     |     | January |     |     |     | February |     |
| --- | --- | ------- | --- | --- | --- | -------- | --- |
Unmasking APTs: Tektite Vulture and Sulphur Kestrel
To illustrate the distinct tactical differences between high-volume bursts and sustained evasion, we have
detailed the operational playbooks of two highly active APTs on the following two pages.
Copyright © 2026  KnowBe4 All Rights Reserved. 8

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Threat Group Name: Tektite Vulture
Primary Motivation: Financially motivated, Signature Tactics, Techniques,
specifically Credential Harvesting and Invoice and Procedures (TTPs):
Fraud (Business Email Compromise/BEC).
• Social Engineering Hook: Posing as internal
Origin: Vietnam IT support or sending fake DocuSign requests
to exploit “implicit trust” users have in
Targets: Large, indiscriminate, and global internal workflows.
campaign targeting the private sector across
all major geographic regions. • Evasion: Aggressively using link obfuscation
techniques, including a tactic where the entire
Volume and Tempo: Bad actor operating in email is a clickable image to neutralize text-
large, concentrated bursts. One campaign based NLP filters.
accounted for 28% of their total volume
(8,037 emails) in a single day, designed to • Deception: High usage of “Display Name
overwhelm incident response teams. Stuffing” to push the actual sender’s address
off-screen on mobile devices (tracked via
Key Tooling: Validated use of the Typhoon unusually long sender display names and
Phishing Kit, a Phishing-as-a-Service (PhaaS) email prefixes), as displayed in the
toolkit, which allows for highly automated example below.
operations and 100% consistency across
hundreds of campaigns without
manual intervention.
The “Image is a
clickable Link”—
evasion tactic.
The DocuSign
impersonation—
the “Display Name
Stuffing” of the
sender’s long
email address.
This is a real-world example of a phishing email reported in the KnowBe4 Defend platform, part of a campaign
by the threat actor group Tektite Vulture. This phish demonstrates the use of both the “Display Name Stuffing”
deception tactic and the “Image is a clickable Link” evasion tactic.
Copyright © 2026 KnowBe4 All Rights Reserved. 9

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Threat Group Name: Sulphur Kestrel
Primary Motivation: Financially motivated, Signature Tactics, Techniques,
specializing in high-fidelity Microsoft 365 and Procedures (TTPs):
Credential Harvesting and session-based
Multi-Factor Authentication (MFA) bypass. • Social Engineering Hook: Utilizes “Policy
Review” and “Action Required” lures.
Origin: Indonesia/Singapore Frequently employs Calendar Invite Injection
(.ics), which forces email clients to auto-
Targets: Indiscriminate global targeting of process the message as a meeting, triggering
the private sector, specifically focusing on
direct system notifications and bypassing
enterprises using Microsoft 365 and high-
traditional inbox spam filters.
reputation corporate VPN environments.
• Evasion: This threat evades detection by
Volume and Tempo: Sulphur Kestrel utilizes hiding backend servers through geofencing,
a “Just-in-Time” infrastructure, intentionally
JavaScript obfuscation, and Cloudflare
aging batched domains for weeks to evade
tunneling. It further bypasses static analysis
“Newly Registered” security filters.
using split/reverse obfuscation, fragmenting
malicious code to prevent tools from flagging
Key Tooling: Expert utilization of the Greatness
keywords like “password” or “login.”
or NakedPages Phishing-as-a-Service (PhaaS)
kits. These tools are specifically designed for
• Deception: Using Reverse Proxy (AiTM)
reverse proxy operations, allowing the attacker
architecture, this threat mirrors Microsoft login
to act as a live bridge between the victim and
pages with perfect visual accuracy. To evade
the legitimate login portal.
detection, it employs VPN Provider Redirects—
analyzing visitor IPs to reroute security vendors
and corporate VPNs to benign sites like Google.
This is a real-world example of a phishing
email reported in KnowBe4 Defend,
part of a campaign by the threat actor
group Sulphur Kestrel.
Copyright © 2026 KnowBe4 All Rights Reserved. 10

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Conclusion
The data reveals a threat landscape defined by automation, scale, and evasion. As adversaries deploy
sophisticated, multi-day campaigns across disposable infrastructure, relying on easily manipulated indicators
to secure the organization is a losing battle. The ultimate lesson drawn from these APT profiles is that reactive
filtering is no longer sufficient.
To effectively break the cycle and
anticipate the next strike, organizations
must anchor their defenses to the only
metrics attackers don’t change:
their core behaviors, operational tactics,
and fundamental methodologies.
Copyright © 2026 KnowBe4 All Rights Reserved. 11

Monthly Average Number of Teams Attacks Reported
10
8
6
4
2
0
skcattA
fo
rebmuN
Teams Phishing: The Inbox
is No Longer the Only Frontline
While we’ve spent years training our eyes to spot phishing emails, the threat landscape is shifting as social
engineering evolves beyond the inbox. Today’s attackers are increasingly favoring multi-channel campaigns,
a trend already proven effective in smishing and phone-based attacks, to bypass traditional defenses and catch
users off guard. This strategic pivot toward cross-platform innovation is exposing a critical,
often under-protected vulnerability within our organizations: Microsoft Teams.
As Microsoft Teams becomes the central nervous system for global collaboration within organizations, threat
actors are following the action to exploit a unique trust gap. Unlike the formal pace of email, Teams is built for
speed and informality. This high-speed mindset often causes users to prioritize a quick reply and engagement
over a careful security check.
Attackers are banking on this perceived safety, turning our primary collaboration tool into their path of least
resistance. While the primary attack vector remains email, transitioning an attack to Teams allows threat actors
to extend the kill chain and create more avenues for success. These threats are particularly dangerous as Teams
allows an attacker to communicate consistently with a victim over multiple messages. This enables them to build
a rapport and a sense of legitimacy that is much harder to achieve through traditional channels.
The data tells a clear story: as hybrid work cements itself globally, our Threat Research
team has tracked a 41% surge in Teams-based attacks over the last six months
(October 2025 – March 2026), highlighting a critical surface area of risk.
9.2 9.1 9.1
Attackers follow every available
7.5
avenue. While still emerging,
6.7 Microsoft Teams attacks are surging,
6.5
peaking in January 2026. This rise
exploits the “Chat with Anyone”
feature—enabled by default—which
lets users initiate chats with any email
address, regardless of whether the 3.5
recipient has a Teams account.
2.8
2.1 2.3
1.7 1.7 1.8
Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar
Monthly
Copyright © 2026 KnowBe4 All Rights Reserved. 12

TPihtlieshing Threat Trends Report   |  April 2026 | Vol. 7
Social Engineering and Payloads
| Payloads Used |     |     |     | Deepfake Teams calls are an emerging threat,  |
| ------------- | --- | --- | --- | --------------------------------------------- |
currently representing just under 5% of all call-based
attacks. This attack can be conducted through both
| Malicious Links | Fake Calls |     |     |     |
| --------------- | ---------- | --- | --- | --- |
video and audio, with our analysts identifying that
| QR Codes | Malware |     |     |     |
| -------- | ------- | --- | --- | --- |
static audio clips are still representing the majority
|     | 4%  |     |     | of these attacks at 65%, and are primarily utilized  |
| --- | --- | --- | --- | ---------------------------------------------------- |
for VIP impersonation attacks. We are starting to
see more deepfakes occur during pseudo-live calls.
16%
In this scenario, attackers use dynamic, real-time
|     |     | 59% |     | interactions to pressure victims, leaving them little  |
| --- | --- | --- | --- | ------------------------------------------------------ |
time to question the legitimacy of the encounter
before being manipulated into action.
21%
| Attack Length Trend |     |     |     | The average volume of messages per  |
| ------------------- | --- | --- | --- | ----------------------------------- |
|                     |     |     | 7.8 | attack campaign, though small, has  |
| 8                   |     |     | 7.5 |                                     |
7.2
increased by over 450%, rising from
7
6.3
one to nearly eight messages!
segasseM fo rebmuN
6
5.1
This shift shows that attackers are prioritizing
5
|     |     | 4.4 |     | sophisticated social engineering and personalization  |
| --- | --- | --- | --- | ----------------------------------------------------- |
in their attacks. This technique allows the attacks
4
|     | 3.5 |     |     | to establish contact and maintain a rapport before  |
| --- | --- | --- | --- | --------------------------------------------------- |
3.2
|     | 2.8 |     |     | delivering their malicious payload. This heightened  |
| --- | --- | --- | --- | ---------------------------------------------------- |
| 3   | 2.5 |     |     | level of sophistication allows the attacker to       |
2.1
bolster their credibility, significantly increasing the
| 2 1.6 |     |     |     | probability of a successful compromise. |
| ----- | --- | --- | --- | --------------------------------------- |
1.4
1
| raM rpA | yaM nuJ luJ guA peS | tcO voN ceD naJ | beF raM |     |
| ------- | ------------------- | --------------- | ------- | --- |
Months
Copyright © 2026  KnowBe4 All Rights Reserved. 13

TPihtlieshing Threat Trends Report   |  April 2026 | Vol. 7
Social Engineering and Payloads
Social Engineering Techniques Most Common Impersonations
in Teams (2025 - 2026)
Mirrors normal Teams communication  Cybercriminals target roles that carry
(Chat/Pleasantries)  authority or technical necessity to ensure
high-pressure compliance.
Impersonation (targeting IT, HR,
CEO, Finance)
|     |     |     | 1 Information Technology |     |     |
| --- | --- | --- | ------------------------ | --- | --- |
Creation of Urgency (setting deadlines
for negative consequences)
HR (both HR employees
|     |     |     | 2 and HR platforms like  |     |     |
| --- | --- | --- | ------------------------ | --- | --- |
Workday)
Heavy use of social engineering
(due to nature of Teams)
|     |     |     | 3 CEO Impersonation |     |     |
| --- | --- | --- | ------------------- | --- | --- |
Some attacks are a single email
attack, whereas others feature
| longer campaigns |     |     | 4 Finance |     |     |
| ---------------- | --- | --- | --------- | --- | --- |
6-Month Timeline Representing Most Impersonations in Teams Attacks
| AUTOMATED NOTIFICATIONS |     | CEO/EXECUTIVE |     | IT SUPPORT |     |
| ----------------------- | --- | ------------- | --- | ---------- | --- |
Password resets and Exploiting year-end manic  Moving target to live call
 “urgent” system patches schedules and “urgent” requests or software downloads
| October                | November | December             | January | February | March      |
| ---------------------- | -------- | -------------------- | ------- | -------- | ---------- |
| 2025                   |          | 2026                 |         |          |            |
| NEW BUSINESS INQUIRIES |          | HUMAN RESOURCES (HR) |         |          | IT SUPPORT |
High-pressure sales lures using  Capitalizing on new year payroll  Moving target to live call
multi-channel follow-ups updates and promotion news or software downloads
| Most Common Impersonations |     | Tactical Goal |     |     |     |
| -------------------------- | --- | ------------- | --- | --- | --- |
Almost every month is different! This represents how this emerging threat is quickly pivoting depending
on attacker priority and responding to time of year.
Copyright © 2026  KnowBe4 All Rights Reserved. 14

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
The Anatomy of a Multi-Channel Attack
A defining trend is the shift from single-vector attacks to multi-channel orchestration. As email defenses
improve, attackers are using Microsoft Teams alongside email to manufacture credibility. By initiating a
request via email and “following up” via a Teams message, they exploit the platform’s informal nature to
validate their identity across different environments.
This cross-platform movement significantly expands the attack surface. When a request appears in both
an inbox and a chat thread, it creates a false sense of legitimacy that bypasses traditional mental filters
and seamlessly integrates the exploit into the professional workflow.
Step Initial Email: Victim receives
a phishing email asking for
1
something (ex. Payroll update,
urgent IT ticket).
Step Reinforcement on Teams:
Minutes later, a direct message
2
from the same impersonated
entity urging the recipient
to complete the action or
resending the payload.
Nearly 1 in 5 (17.38%) of all Why Multi-Channel Attacks Work
1. Context Switching:
Microsoft Teams attacks are now
Brain resets security filter from email to Teams
multi-channel. These attacks
2. Verification Illusion:
Feeling of verification from seeing the sender
originate in the inbox to set the
on two separate platforms
stage but migrate to Teams to 3. Bypassing Technical Scrutiny:
Attacker bypasses email protection by sending
deliver the final payload.
the payload directly on Teams
Copyright © 2026 KnowBe4 All Rights Reserved. 15

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Case Study 1: IT Impersonation
Leading to a Call and Remote Access Steps an Attacker Takes to Gain
Remote Access And Intercept
This case study demonstrates an impersonation attack the MFA Code
that pivots from a simple chat message to a real-time,
deepfake-assisted voice call to gain remote control X Teams Chat (Urgency)
over a victim’s machine. Coerce a user onto a call by fabricating
an emergency in a Teams chat.
Tactical Methodology: From Social Engineering
to Account Takeover
The attack lifecycle is characterized by four
distinct phases:
• Establishment of Trust: Attackers impersonate
internal IT personnel, utilizing sophisticated social
engineering to bypass initial skepticism.
• Psychological Pressure: The use of manufactured
urgency and negative consequences compels the
recipient toward immediate, reactive behavior.
• Channel Pivot: The transition from text-based
messaging to a live call serves as the campaign’s
most sophisticated element, significantly limiting
the victim’s “think time.”
• AI-Enhanced Exploitation: On the call, the attacker
employs a dynamic deepfake voice, allowing the
attacker to respond to queries in real-time. X Zoom Call
By getting the victim onto a call, the attacker Establish trust and rapport
secures remote access to intercept MFA credentials, by moving the conversation
resulting in a full Microsoft account compromise. to a live video call.
As this is largely an emerging threat, it is worth noting
that Microsoft Teams attacks have the same potential X Screen Share
consequences for the victim as phishing emails: Convince the victim to share
• Download of malware onto the computer their screen to gain visual
access for troubleshooting.
• The attacker connecting the victim’s Microsoft
account to their own device
• Unauthorized access to files and sensitive data X Request for Remote Control
Gain full operational
• Attempting to disable security measures for
control by requesting and
long-term persistence
being granted remote
• Checking the victim’s browser for saved passwords desktop access.
• Deployment of ransomware
• Lateral movement through company network X MFA Intercept
Intercept the critical MFA
Once the Teams account is compromised, the attacker code by viewing it on the
can lay dormant for as long as they want before moving shared screen.
laterally through the company network, exfiltrating
sensitive data and gathering intelligence to fuel further
targeted attacks.
Copyright © 2026 KnowBe4 All Rights Reserved. 16

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Case Study 2: HR Platform Impersonation
This next case is a link-based credential harvesting attack that exploits user trust in a critical,
high-reputation internal system.
Key Tactics of this Attack: Potential Consequences for the Victim:
Platform Impersonation: The attacker Credential Theft: Acquiring the victim’s
impersonates a major HR platform — Workday. actual Workday account credentials, which
This is highly effective because attackers are grant access to a wealth of personal data,
leveraging a widely known platform used by including phone numbers, home addresses,
organizations, leading employees to apply and payroll information.
less scrutiny.
Lateral Movement: Obtaining a reusable
Personalization and Legitimacy: The message username and password that can be tried
is heavily personalized with the Workday logo in other company applications or systems
and a changed display name and follows the (credential reuse).
template of a legitimate Workday notification.
Flexible Payload: The malicious link is versatile
Contextual Timing: The attack is timed for and could be configured to redirect the user
a specific part of the year to target a data to a variety of other credential harvesting
review, exploiting a realistic corporate pages or to download different malicious files.
workflow to increase credibility.
Link-Based Payload: These attacks typically
rely on a link that redirects the user to a
perfect mirror of the login page to steal
their credentials.
Example Below:
With Microsoft Teams and other collaboration software as a new vector, attackers are weaponizing the inherent
trust of the platform against users. Adding collaboration software to attackers’ multi-channel strategy significantly
expands the available attack surface, turning a collaborative safe space into a vulnerability. To reduce the risk that
this attack vector poses to organizations, collaboration attacks need to be treated with the respect they deserve,
with human risk management at the forefront. Though small in volume currently, this emerging threat vector has
already been shown to be profitable for attackers.
Copyright © 2026 KnowBe4 All Rights Reserved. 17

Adversary-in-the-Middle (AiTM):
The Stealthy New Standard
Credential harvesting remains the primary payload of choice for modern adversaries. Currently, 60.13% of all
identified attacks rely exclusively on malicious links, while 90% of malicious attachments incorporate embedded
credential harvesting pages. Threat actors continue to invest heavily in this methodology, increasing technical
sophistication to eliminate traditional indicators of compromise and bypass user detection.
Adversary-in-the-Middle (AiTM) phishing is a technique that uses dedicated tooling to establish a proxy
between a target user and a legitimate login portal for an application.
Imagine pulling up to a five-star hotel. A valet in a crisp uniform takes your keys and gives you a ticket. You watch
him drive your car into the legitimate hotel garage. What you don’t see is that the valet isn’t a hotel employee;
he’s a thief. He still parked your car in the right spot, but he just made a 3D mold of your key and a copy of your
registration while he was in the driver’s seat.
The Attack’s Power Comes From Intercepting the User’s Data Without
Altering Their Experience
The deployment of a malicious proxy ensures that the spoofed login interface appears identical to the authentic
site. This is because the target is, in fact, logging into the legitimate site, but their connection is routed through
an attacker-controlled intermediary.
This approach makes AiTM attacks uniquely effective for three primary reasons. First, the method maintains
total authenticity. Because the login page is a live proxy of the actual service, the interface is indistinguishable
from the real thing, which makes the compromise nearly invisible to the user. Second, it enables silent data
interception. By positioning their system as an intermediary, the attacker observes every interaction in real-time
to harvest credentials and capture the active session ticket. Finally, this leads to an immediate account takeover.
Armed with a stolen session ticket, the attacker can bypass MFA and seize full control of the account without the
user ever realizing they were targeted.
Adversary-in-the-Middle (AiTM) Process
Log in
User
Attacker’s System Legitimate Website
(Reverse Proxy) (Application)
Copyright © 2026 KnowBe4 All Rights Reserved. 18

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Reverse Web Proxy
The malicious proxy is the core component enabling the sophisticated nature of AiTM attacks. This technique sets
up a live proxy between the victim and a legitimate login portal, allowing the attacker to observe all interactions
and steal credentials and the authenticated session cookie. Of the various proxy methods available, the reverse
web proxy is arguably the most scalable and reliable approach from an attacker’s point of view. This method is
highly effective because the victim is interacting with a real site, but instead it directly allows the attacker to
bypass traditional security measures like MFA.
The technique is also accessible due to the availability of open-source tooling, which automates the process
and is leveraged by a wide range of threat actors. Popular tools demonstrating this method include Evilginx,
Modlishka, and Muraena. For instance, the threat group Sulphur Kestrel expertly leverages this AiTM architecture,
utilizing PhaaS kits like Greatness or NakedPages for their reverse proxy operations.
MFA Bypass Attack Process
MFA Response
5
1. Victim sends US/PW
MFA Request
2. Attack capture US/PW 4
as it passes through
reverse proxy
1 2 3
3. Attack relays US/PW
to legitimate site
4. MFA Request: MFA request
is sent to victim by
legitimate site
5. MFA Response: MFA request
Victim Phishing URL Attacker UN/PW Real Site
is approved by victim
6. Legitimate site sends 7 6
authentication cookie back
to attacker’s reverse proxy
7. Attacker sends authentication
cookie backto victim
Authentication Cookie Authentication Cookie
Top Phishing-as-a-Service (PhaaS) Toolkits
Evilginx EvilnoVNC
Kratos Modlishka
Muraena Quantum
Route
Redirect
Starkiller
Copyright © 2026 KnowBe4 All Rights Reserved. 19

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Ask The Expert
James Dyer
Head of Threat Intelligence
Phishing-as-a-Service (PhaaS) Toolkits
X These toolkits automate the entire attack lifecycle, from deploying high-fidelity brand clones to
real-time data exfiltration via the Telegram Bot API. The Kratos toolkit specifically has been noted
for evading bots, where the real malicious payload only activates upon human interaction.
The Impact, the Motivation and the Defense of Reverse Proxy
THE THREAT THE MOTIVATION THE DEFENSE
Reverse Proxy Surge Why Attackers Choose AiTM How to Spot a Reverse Proxy
Ease of Use
Automated
tooling like
Evilginx
Domain Verification:
Check the URL. Phishing
sites often use similar but
slightly altered domains
MFA Bypass
(e.g., micr0soft.com
Steals active instead of microsoft.
session tickets com). This is the most
crucial user-level check.
139.22%
Surge from Looks Real
Sept 2025 – March 2026 Live proxy of the
Network Traffic
real login page
Analysis:
Monitor connections.
Reverse Proxy surge!
Use tools to analyze
This technique is commonly incoming and outgoing
used for attacks, but our threat traffic for signs of a
researchers have spotted a man-in-the-middle
It Works!
large spike in their dataset proxy connection.
where Reverse Proxies are High
now being used more than success rate
ever before.
Copyright © 2026 KnowBe4 All Rights Reserved. 20

Percentage of Link-Based Phish With a Reverse Proxy Payload
25
20
15
10
5
0
Monthly
VPN Detection and Redirection
Attackers often bake additional layers into their attacks to make it convoluted for security professionals to
understand the full picture and scope. This has traditionally been achieved by geolocation checks and abusing
the single-use link approach, voiding the attack being replicated by an interested third party. However, our threat
researchers have found that many attackers are now checking connections originating from top corporate VPN
providers as an additional layer. If a connection is identified as coming from one of these VPNs, the attacker’s
phishing infrastructure will redirect the visitor to a benign site. This technique is used to gather more intelligence
on potential victims and wait until the target accesses the phishing site from a potentially less-secure or
vulnerable internet connection.
The list below showcases a selection of top corporate VPN providers and the corresponding benign sites
to which attackers redirect traffic:
Palo Alto GlobalProtect
tesla.com, forbes.com, quora.com, medium.com, cnn.com, x.com,
walmart.com, disneyplus.com, shopify.com, gitlab.com
Checkpoint Secure Remote Access
stackoverflow.com, twitch.tv, soundcloud.com, dailymotion.com,
paypal.com, gitbucket.org
Citrix Secure Private Access
hulu.com, nytimes.com, washingtonpost.com
OpenVPN Access Server
bbc.com, github.com, wired.com, box.com
Cisco AnyConnect
drive.google.com, onedrive.live.com, soundcloud.com,
slack.com, dropbox.com
hsihP
desaB
kniL
fo
egatnecreP
TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
23.7
20.9
19.9 20.2
17.6
16.8
15.6
14.2
12.0
9.7
9.0
7.8
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
Copyright © 2026 KnowBe4 All Rights Reserved. 21

The Agentic Shift: Anticipating the
Era of AI-Driven Threats
Over the past couple of years, AI has triggered a fundamental shift in how organizations operate, with
worldwide spending on AI forecast by Gartner to reach $2.52 trillion in 2026, a 44% year-over-year increase.
We have moved beyond simple chatbots and reactive assistants into the era of agentic orchestration,
where autonomous AI agents are woven into the fabric of global workflows to summarize, filter, and execute
complex tasks. However, the same efficiency gains benefiting the enterprise are being mirrored by the
adversary. Attackers are now leveraging agentic tools to weaponize reconnaissance and scale high-fidelity
threats that were previously impossible to automate.
We previously predicted that “in the near future,
some form of AI will be used in almost every
phishing attack.” In the past six months alone,
85.8% of phishing attacks were AI driven.
Criminal AI Usage
Reconnaissance
AI has industrialized the reconnaissance phase. By organizing massive datasets to reveal hidden
patterns, attackers can ingest sensitive information and historical breach data at an unprecedented
scale. This automated intelligence gathering facilitates hyper-targeted profiling, where public
documents and social media are harvested to build precise maps of an organization’s internal
projects and supply chain vulnerabilities.
Development
Users are inherently motivated and satisfied by effective personalization; we gravitate toward
experiences that feel tailor-made for us. This is evident in our daily lives through the seamless
convenience of curated shopping recommendations or the personalized “wrapped” summaries
of our digital habits. Cybercriminals understand this psychological pull perfectly and have
weaponized it; by mirroring this same level of relevance in their lures, they exploit our natural
desire for individual attention to bypass our critical judgment.
Copyright © 2026 KnowBe4 All Rights Reserved. 22

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Artificial intelligence scales this into vast, automated attacks, pulling data from the reconnaissance
stage directly to the phish using the following techniques:
• Addressing recipient by name • Impersonating closest social graph relations
• Aligning email to company brand • Timing attack with relevant projects and events
Payload
Polymorphic phishing campaigns consist of a series of almost identical emails, differing only
by a few small details.
AI has supercharged polymorphic attacks, moving beyond simple variations in subject lines to the
automated generation of entirely unique phishing content for every recipient. This allows attackers
to pivot from bulk “spray-and-pray” tactics to deploying thousands of unique and personalized
lures simultaneously. With matured AI toolsets, a single campaign can now instantly generate and
distribute multiple payload formats to further bypass traditional detection.
Common techniques used in polymorphic,
AI-driven phish:
Autogenerated malicious links, often
In the past three years,
combining URL shorteners, obfuscation
techniques, and compromised reputable
we have seen phish using
sites to mask the final destination.
Unique variations of malicious polymorphic elements rise
attachments changing the file’s
signature and content while remaining from 56.9% in 2024 to
personalized to the target victim.
67.3% so far this year.
AI-generated malware, each remodeled
with obfuscated variables and structure
to disrupt signature-based detection.
Execution
The ultimate success of the campaign hinges on the phish itself. By combining insights from the
previous stages, attackers can craft a seemingly legitimate phish, a direct byproduct of social
engineering and high levels of personalization.
To take this sophistication to the next level, the attacker can compromise a business domain to
send their carefully curated attack. Ensuring that authentication passes checks is the final nail in
the coffin to bypass traditional solutions and land their attack in their victims’ inboxes.
Copyright © 2026 KnowBe4 All Rights Reserved. 23

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Polymorphic BEC Phishing Campaign with Elements of Personalization
We estimate that AI-driven attacks are seven times more efficient than
those relying on manual reconnaissance. By automating the research
phase, AI has effectively eliminated the manual labor previously required
to hit high-value targets, allowing attackers to scale sophisticated
campaigns at an unprecedented pace.
Copyright © 2026 KnowBe4 All Rights Reserved. 24

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Diversifying the Payload
AI has transformed the phishing lifecycle from end to end, allowing attackers to abandon static templates in favor
of dynamic, creative payloads. In our digital-first world, the abundance of legitimate audio and video content,
from podcasts and corporate webinars to TikToks, has become a goldmine for exploitation. By harvesting this
data to build precise linguistic profiles and training generative models on the results, threat actors can now clone
executive voices with startling accuracy.
These clones are increasingly deployed in live, “calibrated” scenarios on platforms like Zoom, where attackers
leverage the contextual authority of leadership to manipulate employees. While these tactics sound complicated,
tools like ElevenLabs, Resemble AI, and Voice.ai have significantly lowered the barrier to entry, making
sophisticated deepfake attacks a mainstream threat.
By eliminating language barriers and syntactic red flags, these tools allow attackers to scale high-fidelity,
multi-vector campaigns globally with minimal effort.
MP3 Files in Common Words/Phrases
Phishing Emails Found in MP3 Files
38.1%
Let’s see what the attackers have to say:
Increase in the number
of MP3 files being used
in phishing since the Suspicious login
start of the year
detected
73.3%
Increase in malicious
Urgent
MP3 files as a share of
total MP3 files between
2022 to 2026
72.9% Can you hear
me okay?
Increase in the average Time
size of MP3 files
sensitive
With an average MP3 file length of two
minutes and 13 seconds, attackers need
to balance providing enough audio to be
This is highly
convincing while avoiding red flags that
confidential
could potentially expose them.
Personal
Copyright © 2026 KnowBe4 All Rights Reserved. 25

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Average Size of Attachments
Has Increased
We are witnessing year-on-year growth in
file sizes, a trend driven by the increased 111.8% increase in unique
integration of AI in phishing emails.
Attackers leverage auto-generated content
malware signatures since the
within the file to overwhelm security systems
from scanning the content, effectively
start of 2026 while the size of
obscuring the malicious payload.
these malware samples has
142.2 KB 2023
increased by 9.7%.
2024
144.8 KB
2025
156.7 KB
2026
183.7 KB
How Attackers Are Leveraging AI to Attack Security Vendors Directly
While AI has accelerated the speed and efficiency of phishing, it has also provided cyber criminals with the tools
to systematically undermine traditional security perimeters. By disrupting core detection parameters, such as
NLP and NLU, these AI-driven threats bypass machine defenses, shifting the entire burden of detection to the
human — the final and most vulnerable point of failure.
Common techniques used to bypass security vendors include:
• White-on-white text embedded in documents
• HTML smuggling
• Hidden HTML or markdown instructions in webpage source code
• Zero-pixel images containing malicious metadata
• Microscopic footnotes buried in large documents
• Fake positive signaling to poison data models
• Flood attacks to build trust, preventing anomaly detection and abuses social graphing
Copyright © 2026 KnowBe4 All Rights Reserved. 26

TPihtlieshing Threat Trends Report   |  April 2026 | Vol. 7
Cybercrime-as-a-Service
To get a clear picture on how AI has transformed the threat landscape, our researchers investigated the dark
web to identify the resources currently available to attackers and determine how easily they can be acquired.
To allow the attackers to operate at scale for the above attacks, a mini ecosystem has been established,
where tools for jumping over LLM safeguards and creating malicious agents are a hot commodity.
These methods are now being packaged into Cybercrime-as-a-Service (CaaS) toolkits, enabling even low-
skilled threat actors to execute advanced attacks. The democratization of AI has fueled this thriving CaaS
market on underground forums, posing a persistent challenge to AI safety and governance.
Cybercrime-as-a-Service Toolkits Found on Darkweb
HIGH
|     | Xanthorox AI (Xen) | $3,000 |     |     |     |
| --- | ------------------ | ------ | --- | --- | --- |
Tier
Identity Shadowing:  Agentic Payloads:  Thread Injection:   Visual Intelligence:
3 Mimics target writing  Self-correcting  AI joins existing email  Analyzes screenshots
styles from public/ malware that reacts to  threads with perfect  to extract credentials
$3,000 leaked data. defensive measures. contextual awareness. and network maps.
FraudGPT (Lifetime)
$299
|     | Detection Evasion:                 |     | Dynamic Lures:    | Phishing Kits:       |     |
| --- | ---------------------------------- | --- | ----------------- | -------------------- | --- |
|     | Code obfuscation to bypass static  |     | Context-specific  | End-to-end builders  |     |
Tier AV (antivirus) and EDR (endpoint  emails using industry  for credential-stealing
|     | detection and response) filters. |     | jargon to fool NLP. | landing pages. |     |
| --- | -------------------------------- | --- | ------------------- | -------------- | --- |
2
| noitacitsihpoS noisavE | WormGPT 4 |      |     |     |     |
| ---------------------- | --------- | ---- | --- | --- | --- |
| $220-                  |           | $220 |     |     |     |
$299
|     | VEC/BEC Mastery:         | Ransomware Builder:  |        | Scaffolding:          |     |
| --- | ------------------------ | -------------------- | ------ | --------------------- | --- |
|     | Flawless, grammatically  | Production-ready     |        | Modular Python/       |     |
|     | perfect executive        | encryption scripts   |        | PowerShell scripts    |     |
|     | impersonation.           | and ransom notes.    |        | for lateral movement. |     |
|     | Hacking ChatGPT (2)      |                      |        | Hacking ChatGPT (1)   |     |
|     |                          |                      | $50.96 |                       | $49 |
WormGPT (Lite):  Payload Variety:   Manual Malware:  Standard Lures:
Access to early-gen  250+ scripts for account  Human-directed  Basic invoice/
Tier
uncensored LLM  takeover (ATO) and  generation of simple  urgent-action email
| 1   | output. | carding. |     | keyloggers. | templates. |
| --- | ------- | -------- | --- | ----------- | ---------- |
$4.73-
|     | Unlock ChatGPT | $4.73 |     |     |     |
| --- | -------------- | ----- | --- | --- | --- |
$50.96
|     | Bypass Prompts:         | Basic Phishing:   |     |     |     |
| --- | ----------------------- | ----------------- | --- | --- | --- |
|     | Simple text injections  | High-volume,      |     |     |     |
|     | to remove safety        | generic scam      |     |     |     |
|     | guardrails.             | templates.        |     |     |     |
LOW
Copyright © 2026  KnowBe4 All Rights Reserved. 27

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Ask The Expert
James Dyer
Head of Threat Intelligence
X The above table is a stark illustration of the industrialization of AI-driven
cybercrime through the Cybercrime-as-a-Service (CaaS) ecosystem.
The most interesting trend is the direct correlation between technical abilities
and pricing, which ranges drastically from $4.73 to $3,000. Ultimately, the
data shows that attackers are scaling beyond simple LLM jailbreaks to deploy
integrated, full-spectrum cybercrime campaigns, proving these toolkits are
quickly turning AI manipulation into a mainstream commodity.
The Next Step: Prompt Injection
AI innovation shows no sign of slowing, and as it evolves, so does the creativity of the adversary. In fact, we are
already seeing a new class of threats: emails engineered to manipulate the AI systems they use. By embedding
instructions that are invisible to humans but legible to machines, a technique known as indirect prompt
injection, attackers can hijack an AI’s logic as it processes the data.
Once subverted, a standard AI assistant transforms into a “malgent” — a malicious agent operating with the trusted
permissions of an employee. These agents often have broad access to databases, APIs, and internal comms,
they become the ultimate inadvertent insider threat, executing malicious tasks with the authority of a legitimate
user but without any human oversight.
In this environment, passive defense is no longer viable; staying ahead of the threat requires a proactive,
AI-augmented security posture that matches the speed and sophistication of the modern adversary.
The result is a pivot in the threat landscape:
attackers are no longer just socially engineering
humans; they are socially engineering AI.
Copyright © 2026 KnowBe4 All Rights Reserved. 28

Calendar Invites:
Infiltrating the Corporate Schedule
Modern phishing has found a path of least resistance: the calendar invite. By abusing the .ics file, a universally
trusted, text-based file — attackers bypass standard security solutions that typically categorize these files as a
benign scheduling tool. Unlike traditional phishing, which demands active engagement, this technique leverages
an automatic delivery mechanism: inserting malicious events into a user’s schedule regardless of whether the
initial email is ever opened.
The danger of this attack is rooted in its calculated exploitation of a psychological blind spot. By shifting the field
of play from the scrutinized and busy inbox to the relative sanctuary of the corporate calendar, threat actors bypass
traditional skepticism. In the fast-paced environment of a modern workday, even the most security-conscious
employees operate with an implicit trust in their calendars. For professionals perpetually jumping from meeting
to meeting, the calendar is no longer just a tool, it is a to-do list for their day. This trust is further weaponized when
a system-generated notification triggers a reminder for the event, catching the user in a reactive, high-speed
mindset. Users are far more likely to just join the meeting than verify its origin. This reflexive engagement allows
the attacker to bypass a user’s natural suspicion, transforming a routine calendar alert into a high-consequence
entry point for credential harvesting. By merging technical obfuscation with this “default-to-trust” behavior,
attackers effectively neutralize both automated filters and human intuition in a single, silent stroke.
Calendar Invite Phishing has surged by 49% in the last six
months, confirming this method’s escalating threat.
Common Tactics Calendar Phish Payload Breakdown
Link Calls (social engineering you)
X Sense of urgency
Phone numbers Deepfake (audio or visual)
X Financial linguistics 4%*
(e.g., salary discussion) 11%
X A phone number
(typically a fake support line)
15%
X Impersonation (used as a social
engineering technique to increase 72%
the perceived legitimacy)
X Predominantly link based
*Deepfakes are starting to mature and become more mainstream.
Threat researchers expect this to increase over the next six months.
Copyright © 2026 KnowBe4 All Rights Reserved. 29

TPihtlieshing Threat Trends Report   |  April 2026 | Vol. 7
The Power of Impersonation
A staggering 85% of calendar phish use impersonation tactics to manufacture legitimacy.
Impersonation Types
Brand Impersonation  46%
Approximately half (46%) of
| Company             |      |     | 32%      | impersonations are from well-known,  |
| ------------------- | ---- | --- | -------- | ------------------------------------ |
| Impersonation       |      |     |          | common brands, including:            |
| User Impersonation  |      | 13% |          |                                      |
| VIPs                | 9%   |     |          |                                      |
|                     | 0 10 | 20  | 30 40 50 |                                      |
Beyond malicious links, social engineering, and deep fakes, these attacks serve a scouting function. Attackers are
often notified if an invite is accepted or declined, providing them with confirmation that an email address is active
and identifying high-value targets for future engagement. By placing both an email in a target’s inbox and a meeting
on their calendar, this phishing technique effectively doubles the probability of a successful compromise.
Example Below:
Copyright © 2026  KnowBe4 All Rights Reserved. 30

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
How This Looks in a Calendar:
Technical Analysis: Infrastructure Abuse & Reputation Laundering
• Primary Delivery: The attacker abuses legitimate Google Calendar notifications to ensure DMARC
compliance. This allows the malicious invite to bypass perimeter defenses under the guise of an internal
compliance mandate.
• Redirect Orchestration: The payload is obscured within a multi-stage redirect chain. It leverages a high-
reputation Google tracking URL before pivoting to a compromised Ukrainian (.edu) domain.
• Evasion & Exploitation: By utilizing an open redirect vulnerability on the university site, the attacker
exploits the link’s reputation. This technique ensures the final credential-harvesting destination is hidden
from reputation-based detection during the initial delivery phase.
Conclusion
While using a calendar invite may seem like a minor shift in payload, it introduces a sophisticated social
engineering twist by infiltrating an environment typically perceived as safe and structured. This technique
creates a double-vector attack: the initial email delivery and the persistent calendar event.
The surge in calendar phishing is driven by a simple reality: it works. Traditional defenses often classify
meeting requests as benign, allowing attackers to exploit a specific cognitive bias. Because users are
conditioned to trust their schedules, they are significantly more likely to engage with a calendar notification
than a message in a cluttered inbox. Attackers are banking on “calendar fatigue,” relying on busy employees
who treat their schedule as an absolute source of truth and rarely verify an event’s legitimacy before clicking.
Copyright © 2026 KnowBe4 All Rights Reserved. 31

2026 Intelligence Brief:
Ask the Experts
Through our frequent engagement with readers, we have gained valuable direct insight into the specific
organizational challenges you face. This section is designed to address the most common inquiries we receive
while providing updates on critical shifts in the threat landscape. Our goal is to deliver actionable intelligence
that empowers your organization to better protect its personnel, customers, data and infrastructure.
Q Our current secure email gateway (SEG) seems to be missing more threats than usual.
Are SEGs becoming obsolete?
A They certainly aren’t obsolete; however, they are struggling to keep up with the rising sophistication
of phishing attacks. We have witnessed a 31.4% increase in phishing attacks that are successfully
evading SEGs. Attackers are specifically designing more technical attacks, with 61.2% of phishing
emails coming from compromised business accounts and 64% of attacks now utilizing obfuscation
techniques, such as invisible characters or links obscured within images to specifically disrupt the
detection logic of these gateways.
Q Are attackers really using artificial intelligence within their phishing attacks?
If yes, how much of a problem is it?
A Yes, in the past six months, our data suggests that 85.76% of attacks are using artificial intelligence
in some form within their phishing campaigns. This has increased year on year from 79.9% in 2024
to 84% in 2025. AI has lowered the barrier of entry into cybercrime, making it significantly easier to
create high-quality, heavily personalized phishing emails at a massive scale while simultaneously
extending target surface area.
Q What type of payloads should my team be concerned about? Where should we be
focusing our energy, time, and resources?
A While every organization faces a different threat landscape, in general, malicious hyperlinks remain
a primary vector for attackers, with 60.13% of phishing attempts containing a link. This payload
mechanism offers the versatility to deploy thousands of credential-harvesting sites, implement
CAPTCHAs to evade automated scanning, and extract extensive data beyond basic credentials
as demonstrated in AiTM.
Copyright © 2026 KnowBe4 All Rights Reserved. 32

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Q
Are executable attachments a problem anymore?
A Today 67% of attachment-based payloads are in the form of PDFs, SVGs, and DOCX files, with
executables such as Exe or HTML tumbling down the leaderboard. Researchers have witnessed
attackers pivoting to attachments more commonly used daily in business communications in order
to fly under the radar. Notably, 90% of these attachments are credential harvesting links, not direct
malware. A growing theme shows attackers gaining an initial foothold into a business and then
pushing malicious code organization-wide.
Q What is one payload you think security professionals should be aware of and have security
measures in place to combat?
A Malicious phone numbers have burst onto the scene as an indirect payload to socially engineer victims
outside of email communication. This equates to 7.21% of attacks in 2026 so far to contain a phone
number. Common locations of this malicious content include within the subject, in the first line of the
email, or within the attachment for extra layers of obfuscation.
Q
Are humans writing these malicious emails or is it an LLM now?
A The answer, ultimately, is that it’s a blended approach. The average length of a phishing email has nearly
doubled since 2022, jumping from 497 to 1,011 characters. Attackers are using AI to write longer,
more convincing narratives that build trust, making the social engineering aspect much more potent.
Q We’re seeing a decrease in standard QR code attacks. Does this mean quishing
was just a fad?
A While overall QR usage dipped to 3.79%, the sophistication and obfuscation skyrocketed. As attackers
have moved away from “standard” QR codes within the body of the email, they have transitioned into
inserting 64.51% of QR codes within the attachment. This effectively “nests” the payload to obscure
it from detection by SEGs, which scan the body but will miss a QR code tucked inside a PDF or SVG file.
Copyright © 2026 KnowBe4 All Rights Reserved. 33

TPihtlieshing Threat Trends Report | April 2026 | Vol. 7
Q
Who are the most targeted job roles and industries?
A Threat actors consistently prioritize individuals with the keys to the kingdom, which explains why
senior executives are the most targeted.
The top five most targeted job roles are CEO, CPO, CFO, VP of Finance, and COO. After the top-10
most attacked job roles, there is a wider range of attack targets — from interns to managers — as it
becomes a conversation around individual risk profiles rather than access.
Q How much time do we actually have to train a new employee before they are targeted
by a real phishing attack?
A You have to be on it from the get-go! Our data indicates that the average new starter receives their first
phish in the first month of employment. This suggests that attackers are actively monitoring professional
networks and “new joiner” announcements in real-time to identify fresh targets who may not yet be fully
integrated into the company’s security culture or familiar with standard internal processes.
Q If we block all “new” and “untrusted” domains, will that significantly reduce the number
of phishing emails reaching our users?
A Unfortunately, the data shows that blocking “bad” domains is only a small piece of the puzzle.
Currently, 61.2% of phishing emails that successfully bypass security gateways come from
compromised accounts, with 11.4% of these compromised accounts coming from trusted accounts
within your supply chain!
More than one-quarter (27.6%) come from Webmail providers like Gmail or Outlook, and only 13.6% of
phish are sent from dedicated “phishing domains.” This means 84.4% of all successful phish now pass
DMARC, rendering traditional “identity verification” defenses nearly obsolete.
Q We’ve seen a massive increase in phishing emails that appear to come from trusted services
like Google, Microsoft, and SharePoint. Is this just a coincidence, or is it a specific tactic?
A It is a very deliberate and highly effective tactic. Our latest data indicates that 22% of all phishing
attacks are now sent through a legitimate platform. By using trusted platforms, attackers are
no longer just impersonating these brands; they’re abusing the actual infrastructure of these
trusted providers. This allows their email to bypass standard domain-reputation filters, as all the
authentication results marry up to the legitimate platform and the email lands in your inbox!
Copyright © 2026 KnowBe4 All Rights Reserved. 34

Wrapping Up: Staying One
Step Ahead in a Shifting
Landscape
We hope this edition of the Phishing Threat Trends Report has been an eye-opener.
Our goal is simple: to keep you in the know so you can build a robust defense that
protects your people, your data, and your brand.
If this year’s trends have shown us anything, it’s that attackers are getting bolder and
incredibly creative with how they land their malicious content in an inbox or an app.
By shifting our tracking methodology within email, we have shown that attacker
attribution is the catalyst for transitioning from a reactive defense to a predictive
posture. We focused our efforts in this report to showcase how the inbox is no
longer the only frontline, and your corporate calendar is being infiltrated to exploit
the frantic pace of the digital workday.
Critically, it’s not only your humans being targeted by malicious actors but a shift
into exploiting your agents and tooling. Adversary-in-the-Middle (AiTM) techniques
have dismantled the myth of MFA as a “silver bullet,” proving that even our strongest
safeguards require constant evolution. As we look ahead, the security of AI emerges
as our next frontier, where protecting the integrity of our models is now just as vital
as defending the users who interact with them.
Future-Proofing: The Security Revolution
Relying solely on native security or legacy gateways is no longer a strategy —
it’s a gamble. As cybercriminals pivot and equip their armory with sophisticated
AiTM payload and multi-platform attacks, your security stack needs to be as agile
and adaptive as the adversaries themselves.
By moving toward a holistic ecosystem fueled by deep behavioral analytics and real-
time threat intelligence, your employees become a line of defense. More than a filter,
it is continuous, automated coaching that evolves as fast as the attackers do.
Ready to level up your defense? The KnowBe4 team is here to help you turn these
insights into action. Let’s keep the conversation going and ensure your organization
stays ahead of the curve.
Copyright © 2026 KnowBe4 All Rights Reserved. 35

Contributors
James Dyer Lucy Gee
Head of Threat Intelligence Cyber Security Threat Researcher
James spearheads the Threat Intelligence team at Lucy is passionate about the intersection
KnowBe4, spending his days uncovering the latest of psychology and cybersecurity and the use
phishing threat trends, understanding emerging of behavioral insights to enable people to live and
methodologies, and analyzing the TTPs of the work securely. At KnowBe4, Lucy analyzes the latest
Crime-as-a-Service ecosystem. phishing campaigns and communicates emerging
trends to business stakeholders.
Cameron Sweeney Louis Tiley
Cyber Security Threat Researcher Cyber Security Threat Researcher
Cameron specializes in understanding the Louis researches diverse attack vectors, social
technical aspects of cyberattacks. As a member of engineering tactics, and emerging threats.
the KnowBe4 team, he reverse engineers phishing At KnowBe4, he analyzes phishing campaign
attacks and malware to identify emerging threats, methodologies and builds tools to automate
using statistical analysis to track the evolving threat intelligence gathering to identify industry
threat landscape. trends and shape cybersecurity messaging.
Jack Chapman Dr. Martin J. Krämer
SVP Threat Intelligence CISO Advisor
Jack leverages deep insights of the cyber-threat Martin is a CISO Advisor at KnowBe4. He has more
landscape and his extensive R&D skillset to than 10 years of research and industry experience
oversee threat research and AI development for in cybersecurity with a focus on human-centered
KnowBe4 Defend to stop the advanced phishing computing. Martin held roles in innovation,
attacks that defeat traditional security solutions. research, and technology consulting. He has
Jack maintains close ties with the global cyber worked with both public and private organizations
community, particularly the UK’s intelligence and on information security and data protection.
cyber agency GCHQ.
Copyright © 2026 KnowBe4 All Rights Reserved. 36

About KnowBe4 Defend
An integrated cloud email security solution, Defend delivers AI-powered behavioral-based detection to eliminate
the attacks that get through native security and secure email gateways. Leveraging zero-trust and pre-generative
models, Defend provides the highest efficacy of detection against advanced threats, including zero-day and
emerging attacks, phishing emails sent from compromised accounts, and social engineering. Using dynamic
banners applied to neutralized threats, Defend provides real-time teachable moments that continually “nudge”
employees into good security behaviors to tangibly reduce risk and augment security awareness.
About KnowBe4
KnowBe4 empowers the modern workforce to make smarter security decisions every day. Trusted by more than
70,000 organizations worldwide, KnowBe4 is the pioneer of digital workforce security, securing both AI agents
and humans. The KnowBe4 Platform provides attack simulation and training, collaboration security, and agent
security powered by AIDA (Artificial Intelligence Defense Agents) and a proprietary Risk Score. The platform
leverages 15-years of behavioral data to combat advanced threats including social engineering, prompt injection,
and shadow AI. By securing humans and agents, KnowBe4 leads the industry in workforce trust and defense.
More information at KnowBe4.com.
KnowBe4, Inc. | 33 N Garden Ave, Suite 1200, Clearwater, FL 33755
855-KNOWBE4 (566-9234) | www.KnowBe4.com | Sales@KnowBe4.com
Other product and company names mentioned herein may be trademarks and/or registered trademarks of their respective companies.
Copyright © 2026 KnowBe4 All Rights Reserved.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-31", "model": "gemini-3.5-flash-lite"} -->
