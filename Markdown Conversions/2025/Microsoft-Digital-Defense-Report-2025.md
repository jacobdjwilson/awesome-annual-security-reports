# Microsoft Digital Defense Report 2025

## Table of Contents
- [Introduction](#introduction)
- [The threat landscape](#the-threat-landscape)
- [The defense landscape](#the-defense-landscape)
- [Appendix](#appendix)

---

## Introduction

### Introductory statement by Amy Hogan-Burney and Igor Tsyganskiy
**Mobilizing for impact: Cybersecurity leadership in a defining era**

We are living through a defining moment in cybersecurity. As digital transformation accelerates, supercharged by AI, cyber threats increasingly challenge economic stability and individual safety. Cyber threats are rapidly evolving from technical problems affecting business to events impacting all aspects of our society.

For security leaders, the imperative is clear: cybersecurity must be a priority, embedded into the fabric of organizational strategy and addressed regularly as part of risk management. Global partnerships across industry peers and even competitors must be established to coordinate and collaborate on defenses against common adversaries. Traditional perimeter defenses are no longer sufficient. Resilience must be designed into systems, supply chains, processes, and governance. New types of threats will emerge with increasing frequency; being informed and prepared is critical.

**What’s new in this year’s report**

**AI as both a defensive necessity and a target**
We’re witnessing adversaries deploy generative AI for a variety of activities, including scaling social engineering, automating lateral movement, engaging in vulnerability discovery, and even real-time evasion of security controls. Autonomous malware and AI-powered agents are now capable of adapting their tactics on the fly, challenging defenders to move beyond static detection and embrace behavior-based, anticipatory defense.

At the same time, AI systems themselves have become high-value targets, with adversaries amping up use of methods like prompt injection and data poisoning to attack both models and systems, which could lead to unauthorized actions, data leaks, theft, or reputational damage.

**Diverse vectors for initial access**
In today’s world, campaigns rely on multi-stage attack chains that mix tactics and techniques such as social engineering and technical exploits. This year, we saw the widespread adoption of “ClickFix,” a social engineering technique that tricks users into executing malicious code themselves, bypassing traditional phishing protections. We also saw the incorporation of new access methods like device code phishing by both cybercriminal and nation-state actors.

**The pervasive threat of infostealers**
Increasingly, adversaries aren’t breaking in, they’re logging in. In today’s specialized cybercrime economy, access is essential, and infostealers are a way for operators to collect credentials and tokens for sale on the dark web. Follow-on activities by the buyers of compromised credentials can include ransomware, data exfiltration, and/or extortion. Overall, this means that organizations that experience an infostealer infection are at high risk of future breaches.

**Nation-state actors expanding operations**
Geopolitical objectives continue to drive a surge in state-sponsored cyber activity, with a notable expansion in targeting the communications, research, and academia sectors. These expansions are mostly within expected scope and volume, and primarily focused on using cyber espionage against typical targets to complement traditional intelligence operations. Building on a trend we first noted last year, nation states continue to accelerate AI use to evolve their cyber and influence operations, making them more scalable, advanced, and targeted.

We urge you to read this report with a bias toward action. It is not just a reflection of the challenges both past and future; it is a call to mobilize, prepare, and confront. Innovation, resilience, and partnership are the pillars of a secure digital future.

---

### About this report

**Commitment to responsible and ethical practices**
Our approach to cybersecurity is grounded in our core values of responsibility, transparency, and ethical business conduct. We are dedicated to:
- Upholding the highest standards of privacy and data protection.
- Advancing responsible AI and quantum safety initiatives.
- Collaborating across sectors and borders to harmonize standards and share threat intelligence.
- Supporting global efforts to combat cyber mercenaries, safeguard human rights, and foster trust in digital content.

**Our commitment to preserving privacy**
Any and all data included in this report is presented in alignment to our privacy principles. Microsoft is committed to its focus on preserving customers’ control over their data and their ability to make informed choices that protect their privacy. We advocate for strong global privacy and data protection laws requiring companies, including ours, to only collect and use personal data in responsible, accountable ways.

**Report scope**
Microsoft fiscal year 2025 (July 1, 2024–June 30, 2025) unless otherwise stated. Please note that due to rounding, the percentages in some charts may not total 100%.

---

### Our unique vantage point

Our global presence—spanning billions of users, millions of organizations, and a vast network of partners—provides us with an unparalleled perspective on the cybersecurity threat landscape.

**Our breadth and depth of signals**
- **100 trillion**: security signals processed daily.
- **4.5 million**: net new malware file blocks every day.
- **38 million**: identity risk detections analyzed in an average day.
- **15,000+**: Partners in our security ecosystem, making it one of the largest in the world.
- **34,000**: full-time equivalent security engineers employed worldwide.
- **5 billion**: emails screened daily on average to protect users from malware and phishing.

---

### Top 10 recommendations from this report

1. **Manage cyber risk at the boardroom level**: Treat cybersecurity as a business risk on par with financial or legal challenges.
2. **Prioritize protecting identities**: Since identity is the top attack vector, enforce phishing-resistant multifactor authentication across all accounts.
3. **Invest in people, not just tools**: Find ways to upskill your workforce and consider making security part of performance reviews.
4. **Defend your perimeter**: A third of attackers use crude tactics as the easy path into an organization’s exposed footprint.
5. **Know your weaknesses**: Combine knowledge of the organization’s exposure footprint with organizational risk awareness to develop a proactive plan for responding to future breach.
6. **Map and monitor cloud assets**: Conduct an inventory on every cloud workload, API, and identity within the organization.
7. **Build and train for resiliency**: If breaches are all but inevitable, resilience and recovery become key.
8. **Participate in intelligence sharing**: By sharing and receiving real-time threat data with peers, industry groups, and government, we can make it harder for cyber adversaries to achieve their goals.
9. **Prepare for regulatory changes**: Align with emerging laws like the EU Cyber Resilience Act or US critical infrastructure mandates.
10. **Start AI and quantum risk planning now**: Understand both the benefits and risks of AI use within an organization and prepare for a post-quantum cryptography (PQC) world.

---

## The threat landscape

### Key takeaways
1. **Phishing-resistant MFA is the gold standard for security**: MFA blocks over 99% of unauthorized access attempts.
2. **Adversaries are targeting identities that enable access to data**: Government, IT, and research/academic institutions were the most impacted.
3. **Adversaries are using diverse—but well-known—initial access routes**: 28% of breaches were initiated through phishing or social engineering.
4. **Most attacks are for money, not espionage**: More than half of cyberattacks with known motives had financial objectives.
5. **Data exfiltration is the norm**: Data collection was observed in 80% of reactive engagements.
6. **Workload identities are under threat**: Attackers are pivoting to targeting identities and elevated privileges granted to service-to-service workloads.
7. **Adversaries are conducting destructive attacks in the cloud**: We have seen an 87% increase in campaigns aimed at disrupting Azure cloud customer environments.
8. **Adversaries are already using AI as a multiplier**: Adversaries are using AI for automated vulnerability discovery, phishing, and deepfake generation.
9. **Using AI can be both a benefit and a vulnerability**: Organizations should manage the weaknesses of AI, such as prompt injection and data poisoning.
10. **Quantum computing could challenge cybersecurity**: If used by malicious actors, it could threaten the encryption of sensitive data.

---

### How threat actors are shaping the cyber risk environment

Looking back over the past year, we’ve continued to see actors accelerate their development of new and novel techniques to challenge the defenses organizations are implementing to detect and prevent them.

**Most impacted organizations (January–June 2025)**
1. United States: 24.8%
2. United Kingdom: 5.6%
3. Israel: 3.5%
4. Germany: 3.3%
5. Ukraine: 2.8%
6. Canada: 2.6%
7. Japan: 2.6%
8. India: 2.3%
9. United Arab Emirates: 2.0%
10. Australia/Taiwan: 1.8%

**Ten global sectors most impacted by threat actors**
- Government agencies & services: 17%
- Information technology: 17%
- Research and academia: 11%
- Non-governmental organizations: 8%
- Critical manufacturing: 6%
- Transportation systems: 6%
- Consumer retail: 6%
- Communications infrastructure: 5%
- Financial services: 4%
- Healthcare and public health: 4%

---

### Identity, access, and the cybercrime economy

**Identity attacks in perspective**
Modern multifactor authentication still reduces the risk of identity compromise by more than 99%. While attacks against identity infrastructure are still limited in volume, their variety is increasing.

- **Token theft by malware**: 2.4042%
- **AiTM**: 0.2375%
- **Infrastructure**: 0.1692%
- **Attacks on MFA**: 0.0033%
- **Consent phishing**: 0.0005%

More than 97% of identity attacks are password spray or brute force attacks.

---

### Access brokers: The hidden gatekeepers of cybercrime

In the cybercrime economy’s highly specialized and scalable ecosystem, access brokers play a pivotal role. These actors specialize in breaching enterprise environments and selling persistent access to other criminals, including ransomware operators, data extortion groups, and cyber mercenaries.

![Chart showing sectors impacted by access broker activity]

---

## The defense landscape

*(Content regarding AI-powered defense, securing identity in the age of AI, and cloud-scale AI defense is detailed in this section.)*

---

## Appendix

### Glossary
- **AiTM (Adversary-in-the-Middle)**: A type of attack where the attacker intercepts communication between two parties.
- **CaaS (Cybercrime-as-a-Service)**: A business model where cybercriminals sell access or tools to other actors.
- **ClickFix**: A social engineering technique that tricks users into executing malicious code.
- **MFA (Multifactor Authentication)**: A security measure requiring two or more proofs of identity.
- **PQC (Post-Quantum Cryptography)**: Cryptographic algorithms that are thought to be secure against a quantum computer.

### References
1. Microsoft Threat Intelligence, commercial cloud.
2. Atlantic Council, "The Global Cyber Mercenary Market."
3. Intel 471, "Access Broker Activity Report."

[^1]: Footnote content here.

---

nsider access 0.5 E. Victim-owned web infrastructure 4
F. Technology, media, and telecommunications 266 F. Government-owned web infrastructure 2
G. Energy, resources, and agriculture 204 G. Remote access protocol 2
H. Life science and health care 150 H. RMM tools 1
I. Financial services 142
J. Nonprofit sector 84
Source: Intel 471 data Source: Intel 471 data Source: Intel 471 data

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 20
Identity, access, and the cybercrime economy continued
Exploiting vulnerabilities: The persistent threat This year, key vulnerability exploitations that our
“ Recommendations
of unpatched systems Defender Experts observed included:
Vulnerability exploitation remains one of the most
• SimpleHelp RCE chain (CVE-2024-57726/27/28)
reliable, scalable, and silent methods of initial access Vulnerability Patch fast, patch early
• BeyondTrust Privileged Remote Access (PRA)
for threat actors. In the last year, Microsoft Defender exploitation remains Prioritize patching for high-impact CVEs,
and Remote Support (RS) Command Injection
Experts observed a surge in exploitation campaigns especially in internet-facing infrastructure
Vulnerability (CVE-2024-12356) one of the most
targeting known flaws in widely used enterprise and remote access tools.
• Fortinet FortiClient EMS SQL Injection Vulnerability
systems and third-party IT tools. In most cases, reliable, scalable,
(CVE-2023-48788) Isolate management interfaces.
exploitation achieves one of three outcomes:
• Cleo Multiple Products Unrestricted File Upload and silent methods Where possible, restrict RMM tools and
• initial access into protected environments, Vulnerability (CVE-2024-50623) of initial access for administrative consoles to management
• privilege escalation from user to admin • Apache Tomcat Path Equivalence Vulnerability networks or VPN-only access.
threat actors.
• arbitrary code execution to enable lateral (CVE-2025-24813)
Employ exploit detection.
movement or persistence
Effective defense isn’t just patching fast—it’s
Use behavior-based analytics to flag
This activity demonstrates that a strategic pivot expecting gaps and building layers of resilience abnormal post-exploitation behavior
toward infrastructure-level compromise is the new through anomaly detection, behavior-based (for example, Local Security Authority
baseline for initial access. analytics, and hardening high-risk assets. Subsystem Service (LSASS) access, registry
dumping, and outbound tunnelling).
What makes this threat vector especially dangerous
is its lack of dependency on user interaction.
From remote code execution (RCE) in infrastructure
software to logic flaws in authentication mechanisms,
attackers are increasingly skipping phishing and
going straight for the code. Even misconfigurations
in trusted platforms become high-value entry points.
Most of these attacks start with a known Common
Vulnerabilities and Exposures (CVE) exploit and end
in compromise.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 21
Identity, access, and the cybercrime economy continued
Password spray: Anatomy To avoid detection, attackers often employ a “low
Count of IP addresses engaged in high volume password spray attacks by day
of a high-volume attack and slow” strategy, using a single IP address to target
(where count of targeted users is >50)
a small number of identities over extended periods.
Despite their low per-attempt success rate, This chart illustrates how attackers are using more IP addresses as a means to avoid detection.
To reach a larger scale, they automate attacks across
password spray attacks remain a persistent At the same time, advancements in AI are enabling defenders to identify more suspicious
many IP addresses. Cloud-based infrastructure
and high-volume threat. IP addresses. Together, this means more IP addresses are being detected that are involved
is particularly attractive to attackers, as it offers
in password spray attacks.
virtualization, orchestration, and access to a wide
These attacks rely on substantial infrastructure,
range of distinct IP addresses.
allowing adversaries to distribute their activity across
30000
numerous IP addresses (IP).
Learn more on page 72
Autonomous System Numbers (ASNs) are unique
identifiers for collections of IP networks managed
“
25000
by single organizations. While over 50,000 ASNs
carry authentication traffic daily, just 20 ASNs—only
Just 20 ASNs—only 0.04%—
0.04%—account for more than 80% of malicious
password spray activity. This concentration account for more than
20000
underscores the importance of targeted threat
80% of malicious password
intelligence and infrastructure-aware defenses.
spray activity.
Microsoft uses AI to analyze authentication data and
15000
detect subtle patterns of password spray activity
hidden within legitimate traffic. When suspicious
IPs are identified, authentication attempts can be
temporarily blocked, disrupting attacker operations
10000
without affecting legitimate users. This approach
enables real-time protection and adapts to evolving
attacker tactics like automation and rapid IP rotation.
5000
0
Feb 2025 Mar 2025 April 2025 May 2025
Source: Microsoft Digital Crimes Unit

| Microsoft Digital Defense Report 2025  | Contents Introduction |                      |                       |          |     |     |     |     |     |
| -------------------------------------- | --------------------- | -------------------- | --------------------- | -------- | --- | --- | --- | --- | --- |
|                                        |                       | The threat landscape | The defense landscape | Appendix |     |     |     |     | 22  |
Identity, access, and the cybercrime economy continued
|     |     |     |     |     |     |     | Credential abuse patterns  |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
High volume password spray IP   Password spray IP addresses are transient
How a password replay differs from a dictionary attack
An 	analysis	 of	 12.2 	million	 accounts 	in 	a
password 	spray 	attack 	reveals 	the 	following
| 4   |     |     |     | 40%  |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
about cybercriminal login attempts prior to
being	 blocked:
Login attempts using correct
| 3   |     |     |     | 30%                      |     |     |                         |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --- | ----------------------- | --- | --- |
|     |     |     |     |  sPI yarps drowssap fo % |     |     | username and password,  |     |     |
 sserdda PI fo tnuoC
but blocked by multifactor
authentication: only 1.5%
| 2   |     |     |     | 20%  |     |     | This illustrates the limited MFA adoption in   |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ---------------------------------------------- | --- | --- |
this scenario rather than its effectiveness.
Given that modern MFA techniques are
proven to prevent over 99% of identity-
based attacks, expanding MFA usage across
| 1   |     |     |     | 10%  |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
all accounts would dramatically reduce
organizational risk.
| 0   |                     |     |     | 0%                     |     |     |                          |     |     |
| --- | ------------------- | --- | --- | ---------------------- | --- | --- | ------------------------ | --- | --- |
| 0   | 2                   | 4   | 6   | 0                      | 5   | 10  | 15  Incorrect passwords  |     |     |
|     | Count of days seen  |     |     | Number of active days  |     |     |                          |     |     |
for valid usernames:
“wrong password”: 45%
Source: Microsoft Digital Crimes Unit  Source: Microsoft Digital Crimes Unit
This underscores the importance
Most single username/password combination   passwords, this generally represents a low and slow
of avoiding password reuse, since
attempts are used for a single day, attacking from   password spray attack. Multiple attempts at guessing
usernames are commonly recycled.
one IP address. This is generally seen in a replay   a password are made in these attacks, often named
attack, in which a threat actor replays a set of leaked   a “dictionary attack.” If the attacker were to try the
usernames and passwords against Microsoft 365   same username with multiple passwords in close
accounts. When usernames are seen across multiple   succession, the account would be temporarily locked
IP addresses and/or multiple days using multiple   out and easily detected.   Source: Microsoft Threat Intelligence

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 23
Identity, access, and the cybercrime economy continued
Target demographics and exposure
Recommendations
Research and academic environments remain “
disproportionately targeted in password spray
attacks, accounting for 52% of observed spray To reduce the risk and impact of password spray attacks, organizations should adopt On average, each
attempts. Factors contributing to this include a multi-layered identity protection strategy. This includes taking the following measures: compromised
decentralized IT management, high user turnover,
Enforce phishing-resistant MFA for all users Audit and decommission stale accounts username appeared
and inconsistent MFA enforcement—conditions also
observed in other vulnerable sectors such as rural Phishing-resistant MFA remains the most Regularly review and disable inactive accounts, in three separate
effective control against unauthorized access which are often targeted in spray attacks.
healthcare. A May 2025 comparative analysis with
logs, highlighting
using compromised credentials. Even when Ensure that deprovisioned accounts are removed
the Have I Been Pwned database revealed that 85%
attackers possess valid usernames and passwords, from all authentication systems. the magnitude
of usernames targeted in spray attacks appeared
MFA blocks access in over 99% of cases.
in known credential leaks. On average, each of the global
Educate users on credential hygiene
Organizations should monitor for accounts
compromised username appeared in three separate
Promote the use of strong, unique passwords and credential
with valid credentials but unenrolled MFA
logs, highlighting the magnitude of the global
discourage password reuse. Encourage users to
credential leak problem and the importance of users and enforce enrollment policies to close this leak problem.
check their credentials against breach databases
gap. Organizations should also implement
regularly changing passwords.
such as Have I Been Pwned.4
conditional access policies and use risk-based
conditional access to block or challenge sign-ins
Deploy AI-based detection and response
from suspicious IP addresses, geographies, or
Use AI-driven tools to detect anomalous sign-
device types.
in patterns and flag potential spray attacks in
real time.
Monitor and block malicious IP addresses
and ASNs
Continuously monitor authentication logs for error
code 50053 and other indicators of spray activity.
Block IP addresses and ASNs with repeated failed
sign-in attempts or known malicious behavior.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 24
Human-operated attacks and ransomware
Human-operated intrusions:
Infostealer flow chart
From infostealers to ransomware
One of the most concerning trends
this year is the rapid rise in the use of Malvertising / ClickFix / Phishing
infostealers. Traditionally considered
post-exploitation tools, malware families
such as Lumma Stealer, RedLine, Vidar,
Atomic Stealer, and Raccoon Stealer Infostealer deployed
are now increasingly deployed as first-
stage payloads.
These tools, which are typically delivered through
malvertising, search engine optimization (SEO) Credential dump: cookies, passwords, tokens
poisoning, cracked software, and deception
techniques like ClickFix, are designed to collect
credentials, browser session tokens, and system
Sold on forums or access markets
context data at scale.
This shift has elevated infostealers from isolated
threats to foundational components of modern
access campaigns. They enable a division of labor
Used for direct access Purchased by ransomware affiliates
across the cybercriminal ecosystem: initial operators
deploy the malware, access brokers monetize the
stolen data, and users such as ransomware groups
use it to gain footholds in enterprise environments.
As a result, infostealer infections represent more than Initial access Staging of RMM tools, cracked Cobalt Strike, ransomware
just local compromises—they pose a strategic risk of
broader enterprise-wide intrusions.

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  25
Human-operated attacks and ransomware continued
Recommendations
| Top five infostealers  | Windows devices affected by Lumma (March 16-May 16, 2025)  |     |     |     |     |     |
| ---------------------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
Region: Worldwide (Top 20)
Defenders must treat infostealer infections as
50,000
E  precursors to wider compromise, not isolated
D  A
|     | 40,000  |     |     |     |     | malware  events.   |
| --- | ------- | --- | --- | --- | --- | ------------------ |
B
30,000
We recommend:
C
20,000
C
Hunting for loader activity (especially HijackLoader
| A   | D       |     |     |     |     |                                          |
| --- | ------- | --- | --- | --- | --- | ---------------------------------------- |
|     | 10,000  | E F |     |     |     | or Legion) that precedes payloads like   |
G  H I
|     |     |     | J K L M N |       |       |                |
| --- | --- | --- | --------- | ----- | ----- | -------------- |
|     |     |     |           | O P Q | R S T | Lumma Stealer  |
0
Blocking clipboard-to-shell behavior,
|     | A.  India  |     | 44,197  K.  Vietnam  |     | 9,310  |     |
| --- | ---------- | --- | -------------------- | --- | ------ | --- |
B
especially PowerShell scripts from suspicious
|     | B.  Russia  |     | 40,868  L.  Türkiye  |     | 9,292  |     |
| --- | ----------- | --- | -------------------- | --- | ------ | --- |
download paths
|     | C.  Brazil  |     | 21,137  M.  Philippines  |     | 9,008  |     |
| --- | ----------- | --- | ------------------------ | --- | ------ | --- |
D.  United States  15,647  N.  Colombia  8,303  Monitoring for abnormal downloads from GitHub
or Content Delivery Networks (CDN) mimicking
|                    | E.  Indonesia    |     | 14,681  O.  France  |     | 7,314  |                   |
| ------------------ | ---------------- | --- | ------------------- | --- | ------ | ----------------- |
|                    | %  F.  Pakistan  |     | 14,616  P.  Peru    |     | 6,618  | popular software  |
| A.  Lumma Stealer  | 51  G.  Egypt    |     | 12,277  Q.  China   |     | 6,086  |                   |
Limiting password storage and autofill features on
| B.  Atomic  | 21  H.  Spain  |     | 10,598  R.  Bangladesh  |     | 6,083  |     |
| ----------- | -------------- | --- | ----------------------- | --- | ------ | --- |
unmanaged or shared endpoints
C.  Node.js based stealer  16  I.   Argentina  10,486  S.  Poland  5,712
Educating users about deceptive downloads, fake
| D.  Sys01         | 8  J.  Mexico  |     | 9,634  T.  Germany  |     | 5,680  |                                  |
| ----------------- | -------------- | --- | ------------------- | --- | ------ | -------------------------------- |
| E.  Rhadamanthys  | 4              |     |                     |     |        | update pages, and cracked tools  |
Source: Microsoft Threat Intelligence
|     | Lumma Stealer (also known as LummaC2 or      |     | Stealer activity, with campaigns growing in both   |     |     |     |
| --- | -------------------------------------------- | --- | -------------------------------------------------- | --- | --- | --- |
|     | LummaC) was the most prevalent infostealer   |     | frequency and sophistication.                      |     |     |     |
observed in the last year. As a malware-as-a-service
The scale and impact of Lumma Stealer’s
(MaaS) platform, Lumma Stealer is inexpensive,
operations made it a priority target for disruption
feature-rich, and constantly evolving. Its capabilities
for Microsoft—leading to a landmark global
include real-time updates, credential theft, session
intervention by the DCU in May 2025.
hijacking, and crypto wallet draining. In early 2025,
Source: Defender Threat Expert notifications  Microsoft observed a sharp increase in Lumma   Learn more on page 64

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 26
Human-operated attacks and ransomware continued
Lumma Stealer in Latin America
Windows devices affected by Lumma (March 16-May 16, 2025)
Countries such as Brazil, Argentina, Mexico “
Region: Latin America (Top 10)
are frequently targeted by cybercriminals, with
Credential theft has
credential theft, phishing, and ransomware the most
2500
common threats across the Latin America region. become a leading concern
Credential theft has become the leading concern due
in Latin America, due
to increased data breaches and frequent infostealer
malware infections. Between March and May 2025, to increased data breaches
2000 A
Brazil was the third most impacted country in the
and frequent infostealer
world by Lumma Stealer. More broadly, the Latin
malware infections.
America region has been significantly affected by
this infostealer.
1500
To address these threats, Microsoft has strengthened
partnerships with local law enforcement agencies,
Computer Emergency Response Teams (CERT),
and regional security teams. These collaborations
1000
facilitate intelligence sharing, victim notification, B
C
and affirmative disruption actions against
malicious botnets such as Necurs and Trickbot and
D
cybercriminal tools such as “cracked” versions of E
500
Cobalt Strike, which have been linked to over 68 F
ransomware attacks across 19 countries, including
attacks on Latin America’s healthcare sector. J
G H
I
0
A. Brazil 21,137 F. Chile 5,606
B. Argentina 10,486 G. Venezuela 2,617
C. Mexico 9,634 H. Ecuador 2,394
D. Colombia 8,303 I. Dominican Republic 1,918
E. Peru 6,618 J. Bolivia 1,415
Source: Microsoft Threat Intelligence

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 27
Human-operated attacks and ransomware continued
Ransomware’s shifting tactics
Typical human-operated ransomware campaign
The overall ransomware picture this
year did not change significantly from
Access Endpoints Identities Cloud apps Workloads
last year, with organizations worldwide
continuing to face a persistent threat of
attack from a small army of ransomware
actors leveraging both commodity and
custom ransomware strains. Phishing Open Brute force Attacker collects Attacker
mail attachment account reconnaissance and exfiltrates
According to Intel 471’s review of ransomware leak or use stolen configuration data sensitive data
sites, 120 ransomware variants were used against account
71 industries.3 Slightly over half (53%) of the victims credentials
were based in the US, while Canada (6%) and the
United Kingdom (4%) were the next most impacted. Click a URL
Almost half (48%) of organizations whose size is
known had an annual revenue of USD 50 million
or less.
In a continuing shift away from phishing as the Social engineering,
primary means of initial access, ransomware voice phishing, tech
operators are increasingly leveraging social support scams Exploitation Command User Attacker Domain Services Files
and installation and control account is compromises compromised stopped encrypted
engineering to obtain or reset credentials, particularly
compromised a privileged and backups on additional
through vishing or tech support scams. For example, account deleted hosts
this year multiple actors conducted help desk-
themed social engineering, using messaging
platforms such as Teams to communicate with
targets and the Windows utility Quick Assist for
remote access.
Browse to
Learn more on page 67 a website

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  28
Human-operated attacks and ransomware continued
Microsoft also observed several threat actors using   Over 40% of ransomware attacks today
Top ten industries impacted by ransomware  Ransomed organizations by organization   fake software updates or ClickFix techniques to   involve hybrid components. Two years ago,
size in revenue (USD)
convince targets to download malicious software or   less than 5% did.
A
|     |     |     |     | A   | run commands locally on their device.   |
| --- | --- | --- | --- | --- | --------------------------------------- |
B  As in years past, ransomware actors continue to use
Exploitation of public-facing applications also   RMM tools for persistence and further intrusion.
|     |     | C   |     | B   |     |
| --- | --- | --- | --- | --- | --- |
remains a key entry vector. For example, Storm-1175,   Approximately 79% of ransomware cases Microsoft
|     |     | D   |     | C   |     |
| --- | --- | --- | --- | --- | --- |
known for deploying Medusa ransomware, has   observed this year involved at least one RMM tool.
|     | E   |     |     | D   |     |
| --- | --- | --- | --- | --- | --- |
been observed exploiting vulnerabilities in several
Last year, we highlighted that ransomware
E
|     | F   |     |     |     | platforms. These exploits are often chained with   |
| --- | --- | --- | --- | --- | -------------------------------------------------- |
actors were tampering with security solutions
F  credential theft and lateral movement to establish
G  post-compromise. This year, we saw a focus
|     |     |     |     | G   | deeper access.  |
| --- | --- | --- | --- | --- | --------------- |
H  on exploiting antivirus (AV) exclusions to avoid
H  Meanwhile, Octo Tempest, the most sophisticated
I  detection. AV exclusions are typically used by IT or
0  500  100  150  200  ransomware actor, uses advanced social engineering,  security teams to stop AV software from wasting
J
Revenue (USD)
SIM swapping, and identity compromise to access   resources scanning trusted files or directories.
| 0  100  | 200  300  | 400  500  | 600  700  |     |     |
| ------- | --------- | --------- | --------- | --- | --- |
privileged accounts.5 Known for its lateral movement   Attackers seek out misconfigurations such as overly
|     | Count of organizations  |     |     | A.  Over 1 billion  | 239  |
| --- | ----------------------- | --- | --- | ------------------- | ---- |
techniques in cloud, this year the threat actor used   broad exclusions, which they could use to disable
|                                       |     |     |      | B.  500 million – 1 billion  | 124  |
| ------------------------------------- | --- | --- | ---- | ---------------------------- | ---- |
| A.  Industrial products and services  |     |     | 633  |                              |      |
Dragon Force, RansomHub, and Qilin, showing   or sidestep defenses during hands-on-keyboard
|     |     |     |     | C.  100-500 million  | 464  |
| --- | --- | --- | --- | -------------------- | ---- |
B.  Engineering and construction  532  how easy it is for threat actors to move between   intrusions. This year, attackers used exclusions to
|     |     |     |     | D.  50-100 million  | 405  |
| --- | --- | --- | --- | ------------------- | ---- |
C.  Retail, wholesale, and distribution  441  RaaS affiliations. Octo Tempest continues to focus   bypass AV defenses in 30% of observed human-
|     |     |     |     | E.  10-50 million  | 1,739  |
| --- | --- | --- | --- | ------------------ | ------ |
D.  Health care providers and services  376  operated ransomware incidents.
on targeting VMWare ESXi servers, often resulting
|     |     |     |     | F.  5-10 million  | 1,013  |
| --- | --- | --- | --- | ----------------- | ------ |
E.  Technology  281  in high-impact encryption events, particularly in
Despite these evolving threats, attacks reaching the
|                                  |     |     |      | G.  1-5 million  | 4                      |
| -------------------------------- | --- | --- | ---- | ---------------- | ---------------------- |
| F.  IT or technology consulting  |     |     | 252  |                  | hybrid environments.   |
encryption stage have slowed and are now increasing
|     |     |     |     | H.  Revenue not available  | 1,722  |
| --- | --- | --- | --- | -------------------------- | ------ |
G.  Education  251  Overall, targeting hybrid environments is becoming   at a rate of only 7% in 2024-2025 compared to 102%
H.  Law services and consulting  240  more prevalent, with ransomware operators   in 2023-2024, per our incident tracking. EDR solutions
Five most prolific ransomware families
| I.   Transportation  |     |     | 223  |     |     |
| -------------------- | --- | --- | ---- | --- | --- |
leveraging compromised identities and tools like   have proven highly effective at limiting the impact
(percentage of total)
J.  Financial and investment consulting  215  AADInternals to move laterally from on-premises into   of attacks. Improved defense means attackers are
Akira  22%  cloud environments. These techniques allow them   now focused more on data exfiltration—in 82% of
to maintain persistent access, compromise multiple   observed ransomware incidents, we saw large-scale
|     |     |     |     | RansomHub  | 11%  |
| --- | --- | --- | --- | ---------- | ---- |
cloud applications, delete virtual machines (VM) and   data  exfiltration.
|     |     |     |     | Fog  | 11%  |
| --- | --- | --- | --- | ---- | ---- |
backup systems, exfiltrate data from cloud storage,
|     |     |     |     | Qilin  | 7%  |
| --- | --- | --- | --- | ------ | --- |
and encrypt cloud resources.   Learn more on page 67
|     |     |     |     | Play  | 5%  |
| --- | --- | --- | --- | ----- | --- |
Source: Intel 471 data

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 29
Human-operated attacks and ransomware continued
Data exfiltration and impact: To address exfiltration effectively, it’s important to
Data exposure and exfiltration preparedness
Are you prepared? remember that the absence of evidence indicating
data exfiltration does not necessarily mean there’s
At the outset of an incident response Step Purpose
no impact. Understanding the motivations of
engagement, responders generally
the threat actor also provides crucial context.
have to answer two primary questions: Financially motivated threat actors, for example, tend 1 Classify and Identify and label data based on sensitivity, particularly
“How did the threat actors get in?” to be opportunistic, seeking large volumes of data for inventory data crown jewels (most valuable data).
and “What data was stolen?” While extortion or sale. Nation-state affiliated threat actors,
proving exfiltration can be challenging, on the other hand, focus on specific information
it remains a significant concern for such as intellectual property (IP) or state secrets.
customers, regulatory bodies, and In either case, organizations should keep in mind
downstream organizations. the serious consequences that stolen data can pose, 2 Protect Evaluate current protection mechanisms to ensure
like legal risks, impact to industry accreditation, and critical data robust safeguards for sensitive information.
In cases of stolen data, there is clear evidence that
reputational damage.
data has been extracted. In cases of data exposure,
there is evidence that threat actors accessed sensitive
“
data, but the process of exfiltration may not be
visible or may not have occurred. Organizations and
Data collection—which
3
Establish Understand obligations following data exposure/
responders should adhere to zero trust and the
response exfiltration for compliance with legal and regulatory
‘always assume breach’ principles when seeking includes data access and
evidence of access. In the past year, the Microsoft procedures requirements. Understand obligations following data
staging—was noted in exposure/exfiltration for compliance with legal and
Detection and Response Team (DART) observed
exfiltration in 51% of reactive engagements, while 80% of reactive incident regulatory requirements. Establish a business resilience
plan to ensure continuity of operations.
data collection—which includes data access and response engagements.
staging—was noted in 80% of engagements.
4
Maintain visibility Maintain oversight across all environments and
and detection implement rapid response to unusual data access.
capabilities

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  30
Human-operated attacks and ransomware continued
A study in time:
|                      |                     |     | Boxplot of length of threat actor activity by industry  |
| -------------------- | ------------------- | --- | ------------------------------------------------------- |
| What happens when    | Average length of   |     |                                                         |

|     | threat actor activity  |     | 3 years  |
| --- | ---------------------- | --- | -------- |
you hesitate?
|                                    | 58   |     | 2 years  |
| ---------------------------------- | ---- | --- | -------- |
| Time is of the utmost essence in   | Days |     | 1 year   |

cybersecurity. The ability of security
| professionals to respond swiftly,   |     |     | 6 months  |
| ----------------------------------- | --- | --- | --------- |
effectively, and efficiently to early
Average
| signs of a potential breach determines   | dwell time |     | 3 months  |
| ---------------------------------------- | ---------- | --- | --------- |
whether an organization regains control
12
| or falls behind. In some cases, delaying   |     |     | 1 month  |
| ------------------------------------------ | --- | --- | -------- |
Day  s
a response even by one day could have a
significant impact on an organization’s
| ability to fully evict a threat actor and   |                |     | 1 week  |
| ------------------------------------------- | -------------- | --- | ------- |
| rebuild an environment successfully.        | Average time   |     |         |
to engage
The length of threat actor activity is the number
| of days between the earliest identified evidence of   | 9   |     |     |
| ----------------------------------------------------- | --- | --- | --- |
1 day
threat actor activity and the latest. Among attacks
|     | Days    |     |     |
| --- | ------- | --- | --- |
investigated by DART, almost half (39%) lasted
between zero and seven days from earliest to latest
identified threat actor activity, and another 17%
lasted between seven and fourteen days.  Threat
actors are moving faster than ever, making it even   < 1 day  Government  Transportation  Other  Telecommunications  Research and
academia
more important that organizations have the right   Manufacturing  Financial  Energy  Healthcare
mechanisms in place to match that speed.   This chart compares the length of threat actor activity across customer industries over the past year. The horizontal lines
mark median duration in days, and the rectangular boxes indicate the range, where applicable. The research and academia
Learn more on page 68  sector recorded the longest average duration of activity, while the telecommunications sector experienced the shortest.
These differences likely reflect the risk profiles (overall maturity) inherent to each industry and the threat actor goals.
Source: Microsoft Incident Response, Detection and Response Team (DART)

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  31
Human-operated attacks and ransomware continued
As threat actors move faster, they’’re using an
|     | Recommendations for evaluating    | Boxplot of dwell time in days by industry  |     |     |     |     |
| --- | --------------------------------- | ------------------------------------------ | --- | --- | --- | --- |
increasingly aggressive attack chain. As a result,
| dwell times——the length of time in days that a threat   | your incident response posture  |     |     |     |     |     |
| ------------------------------------------------------- | ------------------------------- | --- | --- | --- | --- | --- |
3 years
actor was present in the environment undetected——
2 years
| have become shorter, making early detection         | Does your security budget support your            |     |     |     |     |     |
| --------------------------------------------------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
| crucial. For 46% of our reactive engagements, the   | organization’’s ability to rapidly respond to     |     |     |     |     |     |
1 year
| customer detected the threat actor’’s presence in   | an inevitable cyber incident?  |     |     |     |     |     |
| --------------------------------------------------- | ------------------------------ | --- | --- | --- | --- | --- |
their environment within 48 hours. Most attacks
|     | Do you have clearly defined roles   | 6 months  |     |     |     |     |
| --- | ----------------------------------- | --------- | --- | --- | --- | --- |
(59%) have short dwell times of 7 days or less.
and responsibilities in the case of a
| Attacks with short dwell times are largely   | security incident?   | 3 months  |     |     |     |     |
| -------------------------------------------- | -------------------- | --------- | --- | --- | --- | --- |
conducted by financially motivated actors.
| Threat actors prioritized evading detection and   | Are you supported by a detection or a security   | 1 month  |     |     |     |     |
| ------------------------------------------------- | ------------------------------------------------ | -------- | --- | --- | --- | --- |
operations center (SOC) team?
maintaining access primarily when attacking
government  entities.
Do you conduct proactive threat hunting
1 week
| When it comes to responding, 54% of customers  | supported by threat intelligence?  |     |     |     |     |     |
| ---------------------------------------------- | ---------------------------------- | --- | --- | --- | --- | --- |
engaged DART within three days of detecting a
compromise, and nearly 70% did so within a week.
Learn more
Building an effective incident response plan allows
| organizations to quickly identify workstream leads,   |                                                | 1 day  |     |     |     |     |
| ----------------------------------------------------- | ---------------------------------------------- | ------ | --- | --- | --- | --- |
| establish effective communication, set expectations   | ““Navigating the maze of incident response””   |        |     |     |     |     |
is an evergreen product published by DART
with stakeholders, and call in experts. All of this can
| mean the difference between millions of dollars   | to provide a tactical guide and starting point   |     |     |     |     |     |
| ------------------------------------------------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
for organizations building out their incident
of impact.
response processes who aren’’’t sure where  < 1 day  Government  Transportation  Other  Telecommunications  Research and
academia
|     | to start.  |     | Manufacturing  | Financial  | Energy  | Healthcare  |
| --- | ---------- | --- | -------------- | ---------- | ------- | ----------- |
Navigating the Maze of Incident Response |
This chart compares the average dwell time across customer industries in the past year. The research and academia
Microsoft Security  Blog  sector had the longest average dwell time, indicating that threat actors remained undetected for a significant period.
Conversely, the financial sector had the shortest average dwell time, suggesting quicker detection and response to
threats. Dwell time is a function of attacker motivation in addition to being influenced by attack complexity and an
organization’s threat detection and hunting capabilities.
Source: Microsoft Incident Response, Detection and Response Team (DART)

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 32
Fraud and social engineering
The new age of super-charged fraud Bots themselves are neither good nor bad. They can
Recommendations
and what to do about it be used to automate repetitive tasks, provide instant
access to information, and enhance user experiences
Fraud is as old as commerce itself, rooted in
through personalized, real-time support. Bots can Microsoft recommends organizations implement the following strategies to help identify
the exploitation of trust and information gaps.
improve efficiency, reduce human error, and free up malicious bots and detect bot-assisted cyber fraud:
Throughout history, fraudsters have adapted,
valuable time for more strategic work. Their ability
leveraging new technologies and systems to deceive
to operate 24/7 and scale effortlessly makes them a Residential proxy detection Retrospective remediation
individuals, businesses, and governments.
powerful tool across industries. Integrate third-party proxy intelligence databases. Deactivate accounts or subscriptions identified
Today, we face a pivotal shift: AI is amplifying Build an internal proxy reputation system based on through offline detection.
At the same time, bot-assisted attacks are a rapidly
the scale, speed, and sophistication of fraud and labeled “bot-assisted” transactions.
evolving threat in the digital fraud landscape. Advanced machine learning (ML) approaches
social engineering. While the core tactics remain
More than 90% of the 15.9 billion Microsoft account Customer input pattern analysis Use AI and ML to make sense of complex data—
unchanged—manipulating trust and exploiting
creation requests in the first half of 2025 were from Detect automation by analyzing patterns in user- turning things like email addresses or product
human psychology—the risks are now global,
bad bots. Across the entire year, Microsoft’s anti- submitted data (e.g., names and addresses). descriptions into comparable data points and
immediate, and increasingly targeted.
fraud systems blocked approximately 1.6 million analyzing user actions over time to spot unusual
Behavioral biometrics
Malicious bot protection bot-driven or fake account signup attempts per hour patterns or behaviors.
Monitor mouse movement, click timing,
As ecommerce and digital platforms continue to across its services—an astounding volume indicating
and keystroke dynamics to distinguish bots
scale, so too does the sophistication of fraudsters how attackers are abusing automation and false
from humans.
who exploit automation to bypass traditional identities at scale.
defenses. This is done through bots.
Bots are increasingly used to execute high-speed
credential stuffing, inventory hoarding, fake account
creation, and card testing—often at a scale and
frequency beyond human capability.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 33
Fraud and social engineering continued
The rise of deepfakes and synthetic On platforms like LinkedIn, there may exist fake
identities: How AI is fueling identity Microsoft fraud profiles that use AI-generated portrait photos.6 “
fraud at scale attempts thwarted These fake LinkedIn personas might carry out data
Value of fraud schemes scraping or other abuses like social engineering (for AI-generated IDs are
Using AI, scammers can quickly generate entire fake (many AI-enabled) blocked
example, posing as recruiters or vendors). This not
now often more convincing
websites, profiles, and customer service chats to by Microsoft in one year
only threatens LinkedIn’s integrity but also can spill
(Apr 2024–Apr 2025)
impersonate real businesses or use deepfake voices than real forgeries, growing by
over into direct attacks on Microsoft employees or
and videos to appear as trusted individuals, all at USD 4B partners who might connect with a convincing fake 195% globally in usage.
minimal cost.
profile.7
In the past year, Microsoft thwarted USD 4 billion worth
Synthetic identities are also a rising risk. In the digital
of fraudulent transactions and scams, many likely aided
Automated bot services realm, verifying user identity is a cornerstone
by AI content, and rejected 49,000 bogus enrollment
sign-ups blocked of security. Deepfakes and AI-generated documents
attempts in its partner programs, stopping threat actors
Fake account creation attempts threaten to weaken those verification checkpoints.
who were using fake or stolen identities to pretend to be
(bots/synthetic) blocked on For example, attackers often try to register new
legitimate partners. Microsoft services per hour Microsoft accounts using fake or stolen identities.
Deepfakes involve using AI to create highly realistic 1.6M Their goal might be to obtain free trial resources for
audio and visual content, which can be used for spam/scams or establish throwaway tenant accounts
malicious purposes such as impersonation, fraud, and per hour to launch attacks. Many of these sign-up attempts
misinformation. A deepfake impersonation can lead to use bots—and probably synthetic information Learn more
business email compromise (BEC) or result in leaked (such as random names and AI-generated email
information or the resetting of a password or two-factor addresses)—to get past basic filters. The scale of this AI-powered Deception: Emerging Fraud Threats
authentication (2FA) for an important account. activity indicates a systematic attempt to create fake and Countermeasures | Cyber Signals Issue 9
identities at volume.
Another area where AI deepfakes can be used is in tech
support scams, where fraudsters impersonate a tech AI-generated IDs are now often more convincing
support agent to trick users (often seniors) into paying than real forgeries, growing by 195% globally in
for fake support or installing malware. Traditionally, usage.8 In situations where organizations use selfie
these scams used phone calls, emails, and pop-up checks or document uploads to verify new users,
ads; now threat actors are leveraging AI-modified deepfake techniques can even defeat liveness tests
voices when impersonating support agents for phone (for example, a deepfake video can simulate a person
or video calls. These customer-facing deepfake tech blinking and turning their head).
scams directly impact not only the victims, but the
impersonated company’s reputation and customer trust.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 34
Fraud and social engineering continued
Virtual credit cards and
Growth in single -use credit card sales Recommendations
the shifting fraud landscape
400
Sitting at the crossroads of convenience,
VCCs require a distinct approach to risk
privacy, and security, virtual credit cards 354.7
management. Their unique qualities demand
(VCCs) are reshaping online payments
that merchants treat them as a separate
while simultaneously moving the fraud
payment type—one that calls for agility,
300
battleground for merchants. collaboration, and customer-centric design.
Microsoft recommends the following strategies
The global virtual-card market reached USD 19 billion
to help organizations strengthen defenses while
in 2024 and is projected to expand at a robust 21%
maintaining a smooth customer experience:
Compound Annual Growth Rate (CAGR) through
200
2030 to USD 60 billion.9 This surge is driven by
Adapt billing models and strengthen payment
consumer demand for secure digital payments, the
verification by introducing small validation charges
subscription economy, and strong adoption among
or prepaid options for high-risk customers,
younger demographics. Generated via apps, VCCs
or by requiring backup payment methods for
feature unique details and configurable rules (for
100
larger transactions.
example, limits, merchant category, and lifespan)
designed to reduce card-not-present (CNP) fraud. Enhance fraud detection using velocity monitoring
Businesses, especially in business-to-business and behavioral analytics that go beyond static
(B2B) settings, are also turning to VCCs to improve card data.
payment efficiency. However, the swift adoption 0
of VCCs creates new fraud vulnerabilities and Dec 23 Mar 24 Jun 24 Sep 24 Dec 24 Mar 25 Jun 25 Advocate for industry collaboration by
operational complexities for merchants, necessitating encouraging consistent VCC flagging and
Source: Internal Microsoft commerce telemetry; values indexed to Nov 2023 = 100
strategic adaptation. transparency across card networks.
VCCs often appear like standard cards, making Subscription abuse and refund fraud are rising as Monitor for VCC-specific fraud signals such as
traditional fraud detection rules less effective. Single- bad actors exploit VCCs’ ease of generation and unusually short card lifespans, single-use patterns,
use cards also disrupt recurring billing, causing anonymity. The widespread use of synthetic identities or merchant mismatches
authorization failures. adds further complexity, evading common blocklist
Engage customers proactively with clear
approaches and creating a whack-a-mole effect for
messaging about VCC limitations for
fraud teams.
recurring payments.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 35
Fraud and social engineering continued
Domain impersonation in the age of Beyond these, cybercriminals use AI-driven
AI: Defending against scale and speed adversarial domain generation, such as generative
adversarial networks (GAN), to bypass traditional
Domain impersonation, or cyber-
detection in targeted attacks. The GAN’s generator
squatting, involves registering or using
learns from real domain datasets, like popular
domain names with malicious intent to
brand URLs, and produces convincing lookalike
exploit trademarks or deceive users. domains. Meanwhile, the discriminator evaluates
their authenticity, refining the output until the fake
Domain impersonation has become one of the
domains are nearly indistinguishable from real
fastest-growing online threats due to large-scale, AI-
ones. AI automation allows for the rapid creation of
driven attacks. Common motives include extortion,
thousands of impersonation domains in untargeted
affiliate abuse, phishing, malware distribution, and
attacks, enabling large-scale phishing and scam
cyber-smearing.
campaigns in the space of minutes.
Fraudsters use the following techniques to create
Organizations can reduce domain impersonation
deceptive domain names:
risk by registering their main domain and common
• Typo-squatting: Minor spelling errors (for variations and secure their brand presence by
example, “micorsoft.com”) verifying official social media accounts and
• Homograph-squatting: Using visually similar monitoring fake profiles or fraudulent ads. It is also
characters (such as “rn” for “m”) important to educate employees and customers
• Combo- and level-squatting: Adding extra words to recognize fake URLs, urgent payment requests,
or subdomains to appear legitimate and spoofed emails, and share examples of recent
impersonation attempts to raise awareness.
Having a rapid response plan that includes takedown
procedures with registrars and hosting providers,
as well as playbooks for isolating suspicious emails
and domains quickly, will also aid in the event of an
identified incident.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 36
Social engineering exploits
The rise of ClickFix
Top initial access methods observed Recommendations
Learn more
A particularly notable trend beginning
E
in November 2024 was the rapid surge
Because traditional phishing protections won’t Phishing campaign impersonates Booking.com,
in the use of ClickFix. ClickFix tricks
catch ClickFix, detection must move beyond delivers a suite of credential-stealing malware |
users into copying a command— D static indicators of compromise and focus on Microsoft Security Blog
often embedded in a fake pop-up, job behavioral signals. Microsoft recommends
C Think before you Click(Fix): Analyzing the
application, or support message—and implementing the following:
ClickFix social engineering technique | Microsoft
pasting it into the Windows Run dialog
Security Blog
(Win + R) or a terminal, which then A Awareness training. Teach users that pasting
executes PowerShell or mshta.exe. commands from unknown sources is as risky as
clicking suspicious links.
These commands pull malicious payloads
directly into memory—a clean, fileless
Script block logging. Enable PowerShell
process that is often invisible to B logging and use Constrained Language Mode to
traditional security tools. limit abuse.
ClickFix was the most common initial access Clipboard-to-terminal monitoring. Watch for
method that Microsoft Defender Experts observed unusual clipboard activity followed by shell
in Defender Expert notifications in the last year, launches (cmd.exe, powershell.exe).
accounting for 47% of attacks. ClickFix has been used A. ClickFix 47%
by both cybercriminal and nation-state actors to B. Phishing 35% Browser hardening. Disable clipboard access and
deliver malware, including infostealers, remote access C. Password spray 10% scripting in untrusted zones.
trojans (RATs), and worms. Successful campaigns D. Drive-by compromise and SEO poisoning 7%
Contextual detections. Correlate clipboard usage
have led to credential theft, malware staging, and E. Vulnerability 1%
with downstream execution patterns to catch
persistent access using just a few keystrokes from
suspicious flows.
the user.
Source: Microsoft Defender Experts notifications

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 37
Social engineering exploits continued
Phishing landscape This year, email bombing evolved from being used
as a smokescreen to being used as a first-stage
The most significant change in phishing
attack vector in a broader malware delivery chain.
over the last year is the increase in the
Email bombing is now often used as a precursor to
scale and efficiency of attacks.
vishing or Teams-based impersonation, where the
AI-automated phishing emails achieved 54% attacker contacts the target posing as IT support and
click-through rates compared to 12% for standard offering to resolve the issue. Once trust is established,
attempts—a 4.5x increase. AI enables more targeted targets are guided into installing remote access
phishing and better phishing lures. More concerning, tools, enabling attackers to gain hands-on-keyboard
AI automation has the potential to increase phishing control, deploy malware, and maintain persistence.
profitability by up to 50 times by scaling highly
targeted attacks to thousands of targets at minimal
Recommendations
cost.10 This massive return on investment will
incentivize cyber threat actors who aren’t yet
Filter inbox floods
using AI to add it to their toolbox in the future.
Use rules or heuristics to detect mass sign-up
Email bombing as a precursor to social
emails and alert users or security teams.
engineering attacks
Control Teams exposure
In 2025, one of the most effective social engineering
Restrict external tenant communication and
tactics was email bombing (also called spam
monitor impersonation attempts.
bombing or subscription bombing). In email
bombing, attackers enroll a target’s email account
Educate users
in thousands of newsletters, online services, and
Make employees aware of fake IT support scams,
so on to flood the target’s inbox with hundreds or
especially those asking them to run Quick Assist.
thousands of subscription emails. This is done to hide
critical alerts—for example, MFA prompts, password Limit RMM use
resets, fraud alerts, or transaction notifications— Approve and monitor all remote access tools;
or to create urgency and confusion. block or alert on unauthorized ones through
Windows Defender Application Control (WDAC)
or AppLocker.
Correlate behavior
Flag sequences like inbox flood → Quick Assist →
PowerShell/MSHTA execution.

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  38
Social engineering exploits  continued
BEC: A high-impact threat driven by
Business email compromise by sector (January-June 2025)
identity compromise
While business email compromise
(BEC) represented just 2% of total threats   1.Research and academia 2.Telecommunications 3.Financial   1   Research and academia   49%
services
observed over the past year, its impact
|     |     |     |     | 2   Telecommunications   | 11%  |
| --- | --- | --- | --- | ------------------------ | ---- |
is disproportionately high, particularly
|     |     |     |     | 3   Financial services   | 7%  |
| --- | --- | --- | --- | ------------------------ | --- |
when linked to compromised user
| accounts. In fact, BEC was a more   |     |     |     | 4   Logistics   | 6%  |
| ----------------------------------- | --- | --- | --- | --------------- | --- |
frequent outcome in attacks (21%)
|     |     |     |     | 5   Professional services   | 5%  |
| --- | --- | --- | --- | --------------------------- | --- |
than ransomware (16%), underscoring
|     |     |     |     | 6   Retail and consumer goods   | 5%  |
| --- | --- | --- | --- | ------------------------------- | --- |
the need for organizations to defend
|     |     |     |     | 7   Power and utilities   | 4%  |
| --- | --- | --- | --- | ------------------------- | --- |
against both threat types.
|     | 4.Logistics | 5.Professional   |     | 8    Discrete manufacturing    | 3%  |
| --- | ----------- | ---------------- | --- | ------------------------------ | --- |
BEC attacks are typically initiated through identity
| compromise. Attackers gain initial access through   |     | services |     |                                    |     |
| --------------------------------------------------- | --- | -------- | --- | ---------------------------------- | --- |
|                                                     |     |          |     | 9   Healthcare and public health   | 3%  |
phishing or password spraying, then pivot to BEC-
|     |     |     |     | 10  Hospitality and travel   | 2%  |
| --- | --- | --- | --- | ---------------------------- | --- |
specific activities such as inbox rule manipulation,
unauthorized SharePoint access, internal phishing,   11   Insurance   2%
email thread hijacking, new MFA authentication
|     |     |     |     | 12  Nonprofit   | 2%  |
| --- | --- | --- | --- | --------------- | --- |
method registration, or MFA tampering.
|     | 6.Retail and   | 7.Power and  | 8.Discrete  |     |     |
| --- | -------------- | ------------ | ----------- | --- | --- |
These techniques are used to gain trust, escalate   13  Government   1%
|     | consumer   | utilities | manufact–  |     |     |
| --- | ---------- | --------- | ---------- | --- | --- |
privileges, and ultimately exfiltrate sensitive data
|     | goods |     | uring | 14  Manufacturing   | 1%  |
| --- | ----- | --- | ----- | ------------------- | --- |
or execute financial fraud.
|     |     |         |     | 15  Agriculture, forestry, and fishing   | 0.3%  |
| --- | --- | ------- | --- | ---------------------------------------- | ----- |
|     |     |         |     | 16  Public safety                        | 0.2%  |
|     |     | 10  11  | 12  |                                          |       |
9. Healthcare
and public
|     |     | 13  | 14  |     |     |
| --- | --- | --- | --- | --- | --- |
health
|     |     |     | 15  16  |     |     |
| --- | --- | --- | ------- | --- | --- |

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  39
Social engineering exploits continued
Global BEC hotspots
Active BEC threat groups
BEC activity is not evenly distributed across the
globe. Microsoft telemetry and law enforcement
| 1   | 2   | collaboration have identified regional hotspots where  |
| --- | --- | ------------------------------------------------------ |
BEC operations are particularly active. These areas
Storm-0259  Storm-2502  often serve as hubs for infrastructure setup, money
1  mule recruitment, and laundering operations.
| Operating country:  | Operating country: Nigeria  |     |
| ------------------- | --------------------------- | --- |
Türkiye and TRNC
|                         | Nationality: Nigerian    | Recommendations  |
| ----------------------- | ------------------------ | ---------------- |
| Nationality: Nigerian   | Active: 2021 to present  |                  |
(likely using student visas)
Tactics: International
Active: 2020 to present  Correlate identity-related alerts with suspicious
money laundering, illicit
Tactics: Use of PhaaS for ATO,   cryptocurrency usage, and US  mail flow rules, external forwarding, and
| Email exfiltration, NameCheap  | based mule herding  |     |
| ------------------------------ | ------------------- | --- |
MFA changes.
domains, RedVDS for RDP
Victims: Under assessment
Victims: US, Canadian, UK small
Monitor for unusual sending patterns, especially
and medium businesses
those involving financial requests.
3
2
Audit mailbox access and MFA device
registrations regularly.
| 3   | 4   |     |
| --- | --- | --- |
Educate users on how identity compromise fuels
| Storm-2227           | Storm-2126                       | BEC—not just phishing.  |
| -------------------- | -------------------------------- | ----------------------- |
| Operating country:   | Operating country: South Africa  |                         |
United Arab Emirates
Nationality: Nigerian
Nationality: Nigerian
Active: 2017 to present
Active: 2021 to present
Tactics: Use of ads for phishing,
Tactics: ATO, Email exfiltration,  consumer email targeting,  Learn more
| NameSilo/Hostinger domains,   | GoDaddy domains  |     |
| ----------------------------- | ---------------- | --- |
Azure/RedVDS for RDP
Victims: US real estate, tile
companies and law firms  Understanding business email compromise |
Victims: US construction
| and architecture  |     | Microsoft Security 101  |
| ----------------- | --- | ----------------------- |
4

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 40
Social engineering exploits continued
Device code phishing: The next In device code phishing, attackers exploit the device Device code phishing poses a high risk of data theft
generation of credential theft code authentication flow to capture access and and exfiltration, since it grants threat actors access to *
refresh tokens, which could then be used to access data where the compromised user has permissions,
This year, Microsoft observed a notable
target accounts, data, and other services linked to such as email or cloud storage, without needing a While device code phishing
uptick in threat actors conducting device
the compromised accounts. This technique could also password. In a recent and concerning development,
is not new, most users have
code phishing campaigns worldwide.
enable persistent access or lateral movement as long Microsoft observed a threat actor prompting
not been taught to look for
as the token remains valid. a victim to enter the device code into a Teams
invitation, making it harder for users to identify attacks that target the device
Threat actors exploit the device code authentication
fraudulent activity.
flow by tricking users into entering a device code code flow, and because the
on seemingly legitimate authentication portals Device code phishing poses a considerable threat to
attacker authentication is
that the actor provided in phishing emails or other organizations in all sectors worldwide. Microsoft has
through legitimate codes and
communications. Most threat actors first contact observed nation-state actors from Russia, Iran, and
victims using third-party messaging applications, China as well as cybercriminal groups like Octo tokens, traditional phishing
at times posing as trusted contacts such as an Tempest using this technique to access targets in the
detection tools often miss
administrator or program organizer. Once the user IT sector, NGOs, government agencies, and private
enters the code into the portal, the actor is granted businesses. Ninety-three percent (93%) of the device it, making it a particularly
access and can capture the access and refresh tokens code phishing events that Microsoft observed in the
dangerous phishing evolution.
that are generated. last twelve months occurred in the second half of the
year, indicating the rapid adoption of this technique.
Threat actors have been particularly successful
combining targeted social engineering with out-
of-band communications, which allow these actors
to circumvent antivirus or other detection systems
that would typically identify such activity as spam
or phishing.
Learn more
Storm-2372 conducts device code phishing
campaign | Microsoft Security Blog

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  41
Cloud threat trends
| As organizations accelerate their    | •  A rise in disruptive attack campaigns.   |     |     |     |
| ------------------------------------ | ------------------------------------------- | --- | --- | --- |
*
cloud technology adoption,    There has been an 87% increase in campaigns   Percent increase in some alert notifications
this year (Second 100 days in 2025 compared
| attackers are increasingly targeting    | aimed at disrupting customer environments   |     |     |     |
| --------------------------------------- | ------------------------------------------- | --- | --- | --- |
to first 100 days)  Identity is a primary entry
| cloud environments, leveraging   | through ransomware, mass deletion, or other   |     |     |     |
| -------------------------------- | --------------------------------------------- | --- | --- | --- |
destructive actions.
new tactics and exploiting emerging   A  point for cloud attacks,
•  An escalation in credential theft and data
technologies to compromise assets,    making its protection critical.
disrupt operations, and exfiltrate    exfiltration attempts. Credential and access  B
key theft attempts are up 23%. Attempts to   Enforce MFA and Conditional
sensitive data. Understanding these
C
extract sensitive data from storage accounts and
trends is essential for defenders   Access to block unauthorized
databases increased by 58%.
to prioritize protections and   D  sign-ins, and use Privileged
•  Improved attacker evasion techniques.
respond  effectively.
Threat actors demonstrate a growing awareness  E  Identity Management (PIM)
of cloud defenses and are increasingly employing
Cloud under fire: Escalating attacks   with least-privilege principles
| in cloud environments  | evasion tactics to bypass detection and mitigation.  | F   |     |     |
| ---------------------- | ---------------------------------------------------- | --- | --- | --- |
to tightly control access to
|     |     | 0  20  | 40  60  | 80  100  |
| --- | --- | ------ | ------- | -------- |
Attacks that originate with compromised Entra ID
Recent telemetry from Microsoft Defender for Cloud
identities and escalate into cloud-based activity   sensitive roles.
highlights a significant escalation in the volume
%
within Azure are becoming increasingly prevalent.
and sophistication of attacks targeting Azure cloud
|     | At the same time, the use of service principals for   | A.  Collection  |     | 58  |
| --- | ----------------------------------------------------- | --------------- | --- | --- |
environments. When comparing the first 100 days of
|     |     | B.  Impact  |     | 87  |
| --- | --- | ----------- | --- | --- |
cloud compromise has remained stable or slightly
2025 to the second, trends include:
|     |     | C.  Defense evasion  |     | 57  |
| --- | --- | -------------------- | --- | --- |
decreased, potentially reflecting improved hardening
•  A sharp increase in attack volume. In the number   efforts in this area. Of note, there is a marked rise in   D.  Credential access  23
of observed incidents against Azure-based   Learn more
|                                                 | the use of cloud-native mechanisms—such as Azure   | E.  Run command          |     | 15  |
| ----------------------------------------------- | -------------------------------------------------- | ------------------------ | --- | --- |
| environments, the second 100-day period saw a   | Run Command—for remote code execution (RCE)        |                          |     |     |
|                                                 |                                                    | F.  Attacks by services  |     | 16  |
26% increase in incidents compared to the first   Defending against evolving  attack
within compromised environments.
100 days.  techniques | Microsoft Security  Blog
Learn about AI and advanced defense starting on page 60
Source: Microsoft Defender for Cloud

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 42
Cloud threat trends continued
Container security in focus Containers can be created and taken down quickly,
Cloud threat infection types Median infection time by infection type
but they introduce unique security challenges in
A container is a lightweight, standalone,
cloud-native environments. Microsoft Defender for 100 days January-April 2025 100 days in January-April 2025
executable package of software that
Cloud telemetry reveals that container compromise
includes everything necessary to run 25
often occurs shortly after deployment.
an application.
D
Analysis of container runtime and alert timing
20
over 100 days in January-April 2025, surfaced the
C
following conclusions: C
15
Most compromised containers are attacked within
the first 48 hours of deployment. This emphasizes
B
the critical need for immediate runtime protection. 10
A
B
Cryptomining dominates the attack landscape. A
Cryptojacking is the most prevalent threat in 5 D
Kubernetes environments, exhibiting the fastest
median time to compromise—less than two days
0
post-deployment.
Infection type
Credential theft attacks take longer to manifest.
% Days
These attacks, the second most common type
observed, had the highest median infection A. Crypto miner 58
time, occurring approximately 3.5 days after B. Credential theft 21
container creation. C. Known attack tools 15
D. Web shells 6
Long-tail attacks are a risk. While most attacks
occur early, outliers with significantly delayed
infection highlight the importance of sustained
monitoring beyond initial deployment.
Source: Microsoft Defender for Cloud
syaD
A. Crypto miner 8.7
B. Credential theft 12.7
C. Known attack tools 19.3
D. Web shells 6.8
Source: Microsoft Defender for Cloud

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 43
Nation-state adversary threats
Nation-state cyber activity this year   A minority of attacks, for example against the
prioritized espionage against traditional   Defense Industrial Base, sought to steal proprietary   Most-targeted sectors by nation-state actors
intelligence targets—IT, research and   information for economic advantage. An even
A
academia, government, and think tanks/ smaller number of attacks had other goals, including
B
sabotage and ransom.
NGOs.
CC
A major threat that emerged this year was the
D
discovery of the magnitude of North Korea’s program
EE
to stealthily embed remote workers at organizations
F
around the world. As will be discussed later, this
growing threat has multiple facets, including the   GG
risk of sanctions violation, espionage, extortion,   HH
and sabotage.  I
In line with geopolitical hotspots and longstanding   J
intelligence priorities, the primary geographical   K
targets of nation-state activity this year were in Israel,   L
the United States, and the United Arab Emirates.   00  55  1100  1155  2200  2255 3300
Predictably, Ukraine was also an extreme focus for   PPeerrcceennttaaggee  ooff  ttoottaall
Russian actors.
| % of total                | % of total             |     |
| ------------------------- | ---------------------- | --- |
| A.  IT                    | 26  G.  Transportation | 4   |
| B.  Research and academia | 14  H.  Communications | 4   |
| C.  Government            | 12  I.  Finance        | 3   |
| D.  Think tanks/NGOs      | 7  J.  Health          | 3   |
| E.  Consumer retail       | 7  K.  Defense         | 3   |
| F.  Manufacturing         | 6  L.  EEnneerrggyy    | 33  |
SSoouurrccee::  MMiiccrroossoofftt  TThhrreeaatt  IInntteelllliiggeennccee  nnaattiioonn--ssttaattee  nnoottiifificcaattiioonn  ddaattaa

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  44
Nation-state adversary threats continued
Regional sample of nation-state activity levels observed
Observed event
|     | Americas | Asia & Pacific | Europe | Middle East & Africa |     |     |
| --- | -------- | -------------- | ------ | -------------------- | --- | --- |
activity count
per country
Top activity levels Top activity levels Top activity levels Top activity levels
Over    United States   623  Taiwan     143  Ukraine     277  Israel     603  Kenya     9
200
events  Canada   51  Korea     126  United Kingdom     144  United Arab Emirates     166  Nigeria     8
Brazil   24  India     100  Poland     97  Saudi Arabia     70  Tanzania     5
|          |        | 16  Hong Kong SAR   | 95          | 74          | 70       | 4   |
| -------- | ------ | ------------------- | ----------- | ----------- | -------- | --- |
| 100 ——   | Peru   |                     |   Germany   |   Türkiye   |   Mali   |     |
200
Argentina   11  China     49  France     72  Iraq     67  Namibia     4
50—100  Colombia   10  Australia     47  Spain     61  Jordan     44  Botswana     2
0—50
|     | Mexico   | 9  Thailand   |   39  Russia   |   60  Lebanon   |   39  |     |
| --- | -------- | ------------- | -------------- | --------------- | ----- | --- |
Dominican Republic   5  Japan     38  Italy     51  Egypt     32
|     |         | 4           | 33             | 35       | 27  |     |
| --- | ------- | ----------- | -------------- | -------- | --- | --- |
|     | Chile   | Singapore   |   Azerbaijan   |   Iran   |     |     |
Costa Rica   3  Indonesia     32  Belgium     30  Morocco     26
South Africa     31
Ethiopia    20
Angola     9

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 45
Nation-state adversary threats continued
sseeccuurriittyy,,  ccuussttoommiizzaattiioonn  ooff  ttrraaddeeccrraafftt,,  aanndd
| TTeenn  sseeccttoorrss  mmoosstt  ttaarrggeetteedd  bbyy  CChhiinneessee     |     |     | TTeenn  rreeggiioonnss  mmoosstt  ttaarrggeetteedd  bbyy  CChhiinneessee     |     |     |
| ---------------------------------------------------------------------------- | --- | --- | ---------------------------------------------------------------------------- | --- | --- |
oobbffuussccaattiioonn  ooff  tthheeiirr  eessppiioonnaaggee  ooppeerraattiioonnss..
| tthhrreeaatt  aaccttoorrss  |     |     | tthhrreeaatt  aaccttoorrss  |     |     |
| --------------------------- | --- | --- | --------------------------- | --- | --- |
CChhiinneessee  tthhrreeaatt  aaccttoorrss  rreegguullaarrllyy  rreefifinnee  tthheeiirr
CChhiinnaa  tteecchhnniiqquueess  aass  tthheeyy  aaddaapptt  ttoo  aaddvvaanncceemmeennttss  iinn
sseeccuurriittyy  aanndd  ddeeffeennssiivvee  mmeeaassuurreess..  FFoorr  eexxaammppllee,,
GGlloobbaall  eessppiioonnaaggee  aatt  ssccaallee  tthheeyy  aarree  iinnccrreeaassiinnggllyy  uussiinngg  ccoovveerrtt  nneettwwoorrkkss  ttoo  aavvooiidd
| A B | C D | E F H J | A   | B C | D E F HJ |
| --- | --- | ------- | --- | --- | -------- |
ddeetteeccttiioonn  aanndd  aarree  ffooccuusseedd  oonn  ttaarrggeettiinngg  vvuullnneerraabbllee
TThhee  bbrreeaaddtthh  aanndd  ssccaallee  ooff  CChhiinneessee   G I G I
iinntteerrnneett--ffaacciinngg  ddeevviicceess..  BBeeccaauussee  tthheessee  ddeevviicceess
ttaarrggeettiinngg  ooppeerraattiioonnss  ccoonnttiinnuuee  ttoo  ssttaanndd
aarree  oofftteenn  lleessss  pprrootteecctteedd  aanndd  iinntteeggrraatteedd  wwiitthhiinn  aann
oouutt  ffrroomm  ootthheerr  nnaattiioonn--ssttaattee  aaccttoorrss..
|     |     | %%  ooff  ttoottaall  |     |     | %%  ooff  ttoottaall  |
| --- | --- | --------------------- | --- | --- | --------------------- |
oorrggaanniizzaattiioonn’’ss  sseeccuurriittyy  pprrooggrraammss,,  tthheeyy  ooffffeerr  bbootthh
| AA..  IITT |     | 2233%%  | AA..  UUnniitteedd  SSttaatteess |     | 3355%%  |
| ---------- | --- | ------- | -------------------------------- | --- | ------- |
IInn  lliinnee  wwiitthh  tthheeiirr  eemmpphhaassiiss  oonn  eessppiioonnaaggee  aanndd  tthhee   aann  eennttrryy  ppooiinntt  aanndd  aann  aaddddiittiioonnaall  llaayyeerr  ooff
| BB..  GGoovveerrnnmmeenntt |     | 1100%%  | BB..  TThhaaiillaanndd |     | 1144%%  |
| -------------------------- | --- | ------- | ---------------------- | --- | ------- |
ccoolllleeccttiioonn  ooff  pprroopprriieettaarryy  iinnffoorrmmaattiioonn,,  CChhiinneessee   oobbffuussccaattiioonn  ffoorr  ffuurrtthheerr  aattttaacckkss ..IInn  rreecceenntt
| CC..  TThhiinnkk  ttaannkkss//NNGGOOss |     | 99%%  | CC..  TTaaiiwwaann |     | 1122%%  |
| -------------------------------------- | --- | ----- | ------------------ | --- | ------- |
aaccttoorrss  hhaavvee  pprriimmaarriillyy  ttaarrggeetteedd  oorrggaanniizzaattiioonnss  iinn   yyeeaarrss,,  CChhiinneessee  aaccttoorrss  hhaavvee  bbeeccoommee  ffaasstteerr  aatt
tthhee  IITT  sseeccttoorr,,  iinntteerrnneett  sseerrvviiccee  pprroovviiddeerrss  ((IISSPPss))   ooppeerraattiioonnaalliizziinngg  nneewwllyy  ddiisscclloosseedd  vvuullnneerraabbiilliittiieess,,     DD..  MMaannuuffaaccttuurriinngg 99%%  DD..  KKoorreeaa 88%%
aanndd  tteelleeccoommmmuunniiccaattiioonnss,,  ggoovveerrnnmmeenntt  aaggeenncciieess,,   aa  tthhrreeaatt  ccoommppoouunnddeedd  bbyy  tthhee  ggrroowwiinngg  ccoommpplleexxiittyy   EE..  RReesseeaarrcchh  aanndd  aaccaaddeemmiiaa 66%%  EE..  JJaappaann 44%%
mmiilliittaarryy  aanndd  ddeeffeennssee,,  aanndd  NNGGOOss..  CChhiinneessee  tthhrreeaatt   ooff  ddiiggiittaall  ssuuppppllyy  cchhaaiinnss,,  wwhhiicchh  iinnttrroodduucceess  mmoorree   FF..  CCoonnssuummeerr  rreettaaiill 66%%  FF..  PPhhiilliippppiinneess 33%%
aaccttoorrss’’  ttaarrggeettss  mmoossttllyy  rreessiiddee  iinn  tthhee  UUnniitteedd  SSttaatteess,,   ccoommppoonneennttss  ffoorr  eexxppllooiittaattiioonn..  GG..  CCoommmmuunniiccaattiioonnss 33%%  GG..  UUnniitteedd  KKiinnggddoomm 33%%
AAssiiaa,,  NNoorrtthh  AAffrriiccaa,,  aanndd  LLaattiinn  AAmmeerriiccaa..   HH..  FFiinnaannccee 33%%  HH..  IInnddiiaa 22%%
TThhrroouugghhoouutt  22002244,,  aa  yyeeaarr  wwiitthh  aa  rreeccoorrdd  nnuummbbeerr
CChhiinnaa  uusseess  eessppiioonnaaggee  ooppeerraattiioonnss  aass  aa  kkeeyy  mmeetthhoodd   ooff  eelleeccttiioonnss  wwoorrllddwwiiddee,,  CChhiinneessee  aaccttoorrss  ssppeenntt   II..   TTrraannssppoorrttaattiioonn 22%%  II..   GGeerrmmaannyy 11%%
ooff  ppuurrssuuiinngg  eeccoonnoommiicc  ccoommppeettiittiivvee  aaddvvaannttaaggee..   ssiiggnniifificcaanntt  eeffffoorrtt  ccoolllleeccttiinngg  iinntteelllliiggeennccee  oorr   JJ..  HHeeaalltthh 22%%  JJ..  HHoonngg  KKoonngg  SSAARR 11%%
WWhhiillee  ssttaattee--ssppoonnssoorreedd  aaccttoorrss  ccoonnttiinnuuee  ttoo  ccoonndduucctt   aatttteemmppttiinngg  ttoo  iinnflfluueennccee  tthheeiirr  oouuttccoommeess..
| CChhiinneessee  nnaattiioonn--ssttaattee  tthhrreeaatt  aaccttoorrss  ffooccuusseedd  oonn  IITT,,   |     |     | WWhhiillee  CChhiinneessee  aaccttoorrss  hhaavvee  ppeerrssiisstteennttllyy  ttaarrggeetteedd   |     |     |
| ---------------------------------------------------------------------------------------------------- | --- | --- | ------------------------------------------------------------------------------------------------ | --- | --- |
ooppeerraattiioonnss  bbaasseedd  oonn  tthhiiss  pprriimmaarryy  oobbjjeeccttiivvee,,   TThhrroouugghh  ccoooorrddiinnaatteedd  iinnflfluueennccee  ooppeerraattiioonnss
| ggoovveerrnnmmeenntt,,  aanndd  tthhiinnkk  ttaannkkss  oorr  NNGGOOss  ttoo  ssuuppppoorrtt   |     |     | tthhee  UUnniitteedd  SSttaatteess,,  tthhiiss  yyeeaarr  tthheeyy  ddeemmoonnssttrraatteedd  aann   |     |     |
| ---------------------------------------------------------------------------------------------- | --- | --- | ---------------------------------------------------------------------------------------------------- | --- | --- |
tthheessee  ttaaccttiiccss  aanndd  ooppeerraattiioonnss  oofftteenn  rreellyy  oonn   ccaammppaaiiggnnss,,  aanndd  ccyybbeerr  iinnttrruussiioonnss,,  CChhiinnaa  sseeeekkss  ttoo
| CChhiinnaa’’ss  ggooaall  ooff  rreesshhaappiinngg  tthhee  iinntteerrnnaattiioonnaall  oorrddeerr,,   |     |     | eelleevvaatteedd  ffooccuuss  oonn  TThhaaiillaanndd,,  rreeflfleeccttiinngg  aa  ssttrraatteeggiicc   |     |     |
| ------------------------------------------------------------------------------------------------------ | --- | --- | ------------------------------------------------------------------------------------------------------ | --- | --- |
uunneexxppeecctteedd  ppaarrttnneerrsshhiippss..   uunnddeerrmmiinnee  ddeemmooccrraattiicc  iinnssttiittuuttiioonnss,,  ssooww  ddiissccoorrdd
| eelleevvaattiinngg  CChhiinnaa’’ss  ggeeooppoolliittiiccaall  ssttaannddiinngg,,  aanndd   |     |     | eexxppaannssiioonn  ooff  iinnflfluueennccee  eeffffoorrttss  iinn  SSoouutthheeaasstt  AAssiiaa..  |     |     |
| ------------------------------------------------------------------------------------------ | --- | --- | --------------------------------------------------------------------------------------------------- | --- | --- |
aammoonngg  aalllliieess,,  aanndd  pprroommoottee  nnaarrrraattiivveess  tthhaatt  lleeggiittiimmiizzee
CChhiinneessee  ssttaattee  aaccttoorrss  iinnccrreeaassiinnggllyy  rreellyy  oonn   ccoouunntteerriinngg  WWeesstteerrnn  iinnflfluueennccee  iinn  kkeeyy  rreeggiioonnss..
iittss  ggoovveerrnnaannccee  mmooddeell..  TThhiiss  ppuusshh  rreeflfleeccttss  aanndd  lloonngg--
ppaarrttnneerrsshhiippss  wwiitthh  ppuubblliicc//nnoonn--ggoovveerrnnmmeenntt
tteerrmm  aammbbiittiioonn  ttoo  rreesshhaappee  tthhee  iinntteerrnnaattiioonnaall  oorrddeerr,,
oorrggaanniizzaattiioonnss  ttoo  ccoonndduucctt  vvuullnneerraabbiilliittyy  rreesseeaarrcchh,,
eelleevvaattee  CChhiinnaa’’ss  ggeeooppoolliittiiccaall  ssttaannddiinngg,,  aanndd  ccoouunntteerr
ccrreeaattee  ccuussttoomm  mmaallwwaarree,,  oorr  pprroovviiddee  ccoovveerrtt
WWeesstteerrnn  iinnflfluueennccee  iinn  kkeeyy  rreeggiioonnss..
nneettwwoorrkkss  ttoo  oobbffuussccaattee  ooppeerraattiioonnss..  TThhiiss  bbeehhaavviioorr
rreeflfleeccttss  CChhiinnaa’’ss  lloonnggssttaannddiinngg  ffooccuuss  oonn  ooppeerraattiioonnaall   SSoouurrccee::  MMiiccrroossoofftt  TThhrreeaatt  IInntteelllliiggeennccee  nnaattiioonn--ssttaattee   SSoouurrccee::  MMiiccrroossoofftt  TThhrreeaatt  IInntteelllliiggeennccee  nnaattiioonn--ssttaattee
| nnoottiifificcaattiioonn  ddaattaa  |     |     | nnoottiifificcaattiioonn  ddaattaa |     |     |
| ----------------------------------- | --- | --- | ---------------------------------- | --- | --- |

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 46
Nation-state adversary threats continued
MMiiccrroossoofftt hhaass oobbsseerrvveedd iinnccrreeaasseedd oovveerrllaapp iinn
TTeenn sseeccttoorrss mmoosstt ttaarrggeetteedd bbyy IIrraanniiaann tthhrreeaatt TTeenn rreeggiioonnss mmoosstt ttaarrggeetteedd bbyy IIrraanniiaann tthhrreeaatt
ttaaccttiiccss,, tteecchhnniiqquueess,, aanndd pprroocceedduurreess ((TTTTPPss)) aammoonngg
aaccttoorrss aaccttoorrss
cceerrttaaiinn IIrraanniiaann ssttaattee aaccttoorrss,, ssuuggggeessttiinngg ppoossssiibbllee
ffoorrmmaall oorr iinnffoorrmmaall ccoollllaabboorraattiioonn,, iinncclluuddiinngg sshhaarreedd
IIrraann
rreessoouurrcceess oorr ppeerrssoonnnneell.. TThhiiss ccoonnvveerrggeennccee ccoouulldd
aallssoo rreeflfleecctt cceennttrraalliizzeedd ssttrraatteeggiicc ddiirreeccttiioonn,, sshhaarreedd
PPeerrssiisstteenntt aanndd aaddaappttiivvee
ddeevveellooppmmeenntt ppiippeelliinneess,, tthhiirrdd--ppaarrttyy ccoonnttrraaccttoorr A B C D E F G H J A B C D F HJ
IInn aa yyeeaarr wwhheerree IIrraann wwaass iimmppaacctteedd
ssuuppppoorrtt,, oorr ddeelliibbeerraattee eeffffoorrttss ttoo oobbssccuurree aattttrriibbuuttiioonn.. I E G I
bbyy ccoonnfflliicctt,, IIrraanniiaann ssttaattee aaccttoorrss IInn tthhee llaasstt yyeeaarr,, tthhrreeee IIrraanniiaann aaccttoorrss ttaarrggeetteedd
ccoonnttiinnuueedd ttoo ddiirreecctt bbrrooaadd ccaammppaaiiggnnss sshhiippppiinngg aanndd llooggiissttiiccss ooppeerraattiioonnss aaccrroossss EEuurrooppee %% ooff ttoottaall %% ooff ttoottaall
aaggaaiinnsstt hhiissttoorriicc aaddvveerrssaarriieess,, ttaarrggeettiinngg aanndd tthhee PPeerrssiiaann GGuullff iinn ssoopphhiissttiiccaatteedd ccaammppaaiiggnnss.. AA.. IITT 2211%% AA.. IIssrraaeell 6644%%
oorrggaanniizzaattiioonnss aanndd iinnddiivviidduuaallss TThheessee ccoommpprroommiisseess iinnddiiccaattee aann iinntteenntt ttoo ggaaiinn lloonngg-- BB.. RReesseeaarrcchh aanndd aaccaaddeemmiiaa 1155%% BB.. UUnniitteedd SSttaatteess 66%%
aaccrroossss tthhee MMiiddddllee EEaasstt,, EEuurrooppee,, aanndd tteerrmm aacccceessss ttoo ooppeerraattiioonnaall ssyysstteemmss aanndd sseennssiittiivvee CC.. GGoovveerrnnmmeenntt 88%% CC.. UUnniitteedd AArraabb EEmmiirraatteess 55%%
NNoorrtthh AAmmeerriiccaa.. ccoommmmeerrcciiaall ddaattaa.. AAcccceessss ttoo mmaarriittiimmee ccoommppaanniieess DD.. TTrraannssppoorrttaattiioonn 66%% DD.. IInnddiiaa 22%%
aanndd ddaattaa rraaiisseess ccoonncceerrnnss ggiivveenn iitt ccoouulldd ppootteennttiiaallllyy
EE.. CCoonnssuummeerr rreettaaiill 55%% EE.. GGrreeeeccee 22%%
TThhee vvoolluummee ooff IIrraanniiaann ssttaattee--lliinnkkeedd ccyybbeerr aaccttiivviittyy eennaabbllee eessppiioonnaaggee oorr iinntteerrffeerreennccee wwiitthh ccoommmmeerrcciiaall
FF.. CCoommmmuunniiccaattiioonnss 55%% FF.. AAzzeerrbbaaiijjaann 22%%
rreemmaaiinnss ccoonnssiisstteennttllyy hhiigghh,, wwiitthh ppeerrssiisstteenntt sshhiippppiinngg ooppeerraattiioonnss..
GG.. CCoommmmeerrcciiaall ffaacciilliittiieess 33%% GG.. SSaauuddii AArraabbiiaa 22%%
ccaammppaaiiggnnss oobbsseerrvveedd aaccrroossss ddiivveerrssee iinndduussttrriieess..
IInn llaattee 22002244,, ssoommee nnaattiioonnaall sseeccuurriittyy aaggeenncciieess AA ggrroowwiinngg aanndd ssiiggnniifificcaanntt ttrreenndd aaccrroossss aa ffeeww IIrraanniiaann HH.. MMaannuuffaaccttuurriinngg 33%% HH.. UUnniitteedd KKiinnggddoomm 11%%
tthhrreeaatt aaccttoorrss iiss tthhee aabbuussee ooff cclloouudd iinnffrraassttrruuccttuurree,,
wwaarrnneedd aabboouutt aa ssuurrggee iinn IIrraanniiaann nnaattiioonn-- II.. TThhiinnkk ttaannkkss // NNGGOOss 33%% II.. TTüürrkkiiyyee 11%%
ppaarrttiiccuullaarrllyy MMiiccrroossoofftt AAzzuurree,, ffoorr ccoommmmaanndd aanndd
ssttaattee ccrreeddeennttiiaall hhaarrvveessttiinngg aattttaacckkss,, ttaarrggeettiinngg JJ.. DDeeffeennssee iinndduussttrryy 22%% JJ.. IIrraaqq 11%%
ccoonnttrrooll,, ppeerrssiisstteennccee,, eemmaaiill eexxfifillttrraattiioonn,, aanndd ootthheerr
tthhee hheeaalltthhccaarree,, ggoovveerrnnmmeenntt,, IITT,, eenneerrggyy,, aanndd
mmaalliicciioouuss aaccttiivviittiieess,, oofftteenn uussiinngg ffrraauudduulleennttllyy IIrraann’’ss ffooccuuss oonn tthhee IITT sseeccttoorr sstteemmmmeedd ffrroomm IIrraann vviieewwss IIssrraaeell aass iittss ttoopp rreeggiioonnaall rriivvaall..
eennggiinneeeerriinngg sseeccttoorrss,, rreeflfleeccttiinngg aa ccoonnttiinnuuaattiioonn
ccrreeaatteedd oorr ccoommpprroommiisseedd ssuubbssccrriippttiioonnss.. BByy aabbuussiinngg tthhee sseeccttoorr’’ss uuttiilliittyy iinn eessppiioonnaaggee,, iinnflfluueennccee,, aanndd TTaarrggeettiinngg IIssrraaeell tthhrroouugghh ccyybbeerr ooppeerraattiioonnss
ooff IIrraann’’ss hhiissttoorriiccaallllyy ccoonnssiisstteenntt ffooccuuss oonn ccrriittiiccaall
ssuubbssccrriippttiioonn mmooddeellss ssuucchh aass AAzzuurree ffoorr SSttuuddeennttss aanndd ddiissrruuppttiioonn.. BByy ccoommpprroommiissiinngg IITT pprroovviiddeerrss,, eennaabblleedd IIrraann ttoo ggaatthheerr iinntteelllliiggeennccee,, ddiissrruupptt ccrriittiiccaall
iinnffrraassttrruuccttuurree.. AAtt tthhee ssaammee ttiimmee,, IIrraann’’ss iinntteelllliiggeennccee
ttrriiaall aaccccoouunnttss wwiitthhiinn ccoommpprroommiisseedd tteennaannttss,, tthhrreeaatt IIrraanniiaann nnaattiioonn--ssttaattee tthhrreeaatt aaccttoorrss ggaaiinneedd aacccceessss sseerrvviicceess,, rreettaalliiaattee bbeellooww tthhee lleevveell ooff ooppeenn wwaarr,, aanndd
sseerrvviicceess ccoonnttiinnuuee ttoo ffooccuuss hheeaavviillyy oonn rreeggiioonnaall
aaccttoorrss ccrreeaattee llooww--ccoosstt,, ddiissppoossaabbllee iinnffrraassttrruuccttuurree ttoo sseennssiittiivvee ddaattaa,, ttrruusstteedd ccoommmmuunniiccaattiioonnss,, pprroojjeecctt iiddeeoollooggiiccaall rreessiissttaannccee ffoorr ddoommeessttiicc aanndd
aaddvveerrssaarriieess,, ccoonndduuccttiinngg lloonngg--tteerrmm eessppiioonnaaggee
tthhaatt iiss ddiiffifficcuulltt ttoo ddeetteecctt aanndd ttrraaccee.. aanndd aa ppaatthhwwaayy iinnttoo mmuullttiippllee ddoowwnnssttrreeaamm rreeggiioonnaall aauuddiieenncceess..
aaggaaiinnsstt ccrriittiiccaall iinnffrraassttrruuccttuurree..
sseeccttoorrss ssiimmuullttaanneeoouussllyy..
SSoouurrccee:: MMiiccrroossoofftt TThhrreeaatt IInntteelllliiggeennccee nnaattiioonn--ssttaattee SSoouurrccee:: MMiiccrroossoofftt TThhrreeaatt IInntteelllliiggeennccee nnaattiioonn--ssttaattee
nnoottiifificcaattiioonn ddaattaa nnoottiifificcaattiioonn ddaattaa

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 47
Nation-state adversary threats continued
aanndd ccoonnttiinnuuiinngg ttoo ccoo--oopptt ccyybbeerrccrriimmiinnaall oorr ootthheerr
TTeenn sseeccttoorrss mmoosstt ttaarrggeetteedd bbyy RRuussssiiaann tthhrreeaatt TTeenn rreeggiioonnss mmoosstt ttaarrggeetteedd bbyy RRuussssiiaann tthhrreeaatt
nnaattiioonn--ssttaattee iinnffrraassttrruuccttuurree..
aaccttoorrss aaccttoorrss
TThheessee aaccttoorrss aappppeeaarr ttoo hhaavvee rreedduucceedd tthheeiirr eeffffoorrttss ttoo
RRuussssiiaa ddeevveelloopp bbeessppookkee ooppeerraattiioonnss iinn ffaavvoorr ooff lleevveerraaggiinngg
tthhee ccyybbeerrccrriimmiinnaall eeccoossyysstteemm.. TThhiiss ggrroowwiinngg rreelliiaannccee
EExxppaannddiinngg iittss ttaarrggeett sseett oonn lleessss ssoopphhiissttiiccaatteedd mmeetthhooddss aanndd ccoommmmooddiittyy ttoooollss
bbuutt ssttiillll ffooccuusseedd oonn UUkkrraaiinnee iiss lliikkeellyy aa rreessppoonnssee ttoo eexxppoossuurree bbyy ggoovveerrnnmmeenntt A B C D E F H J A B C D E F G H I J
G I
aaggeenncciieess aanndd ccyybbeerrsseeccuurriittyy fifirrmmss ooff tthheeiirr ttoooollss
RRuussssiiaann ssttaattee aaccttoorrss eexxppaannddeedd tthhee ssccooppee
aanndd tteecchhnniiqquueess.. TThhiiss sshhiifftt iinn TTTTPPss ccoouulldd mmaakkee iitt
ooff tthheeiirr ttaarrggeettiinngg tthhiiss yyeeaarr ttoo iinnffiillttrraattee %% ooff ttoottaall %% ooff ttoottaall
mmoorree ddiiffifficcuulltt ffoorr nneettwwoorrkk ddeeffeennddeerrss ttoo aattttrriibbuuttee
nneettwwoorrkkss aanndd ddeevviicceess pprriimmaarriillyy iinn AA.. GGoovveerrnnmmeenntt 2255%% AA.. UUnniitteedd SSttaatteess 2200%%
ssiimmppllee ooppeerraattiioonnss ttoo ssoopphhiissttiiccaatteedd tthhrreeaatt aaccttoorrss
UUkkrraaiinnee aanndd NNoorrtthh AAttllaannttiicc TTrreeaattyy BB.. RReesseeaarrcchh aanndd aaccaaddeemmiiaa 1133%% BB.. UUnniitteedd KKiinnggddoomm 1122%%
aanndd rreeccooggnniizzee tthhee iimmpplliiccaattiioonnss ooff aa bbrreeaacchh.. AAtt tthhee
OOrrggaanniizzaattiioonn ((NNAATTOO)) mmeemmbbeerr ssttaatteess.. ssaammee ttiimmee,, iitt hhiigghhlliigghhttss tthhee nneeeedd ttoo ddeeffeenndd aaggaaiinnsstt CC.. TThhiinnkk ttaannkkss//NNGGOOss 1133%% CC.. UUkkrraaiinnee 1111%%
kknnoowwnn RRuussssiiaann TTTTPPss.. DD.. IITT 1100%% DD.. GGeerrmmaannyy 66%%
TThhiiss sshhiifftt ttoo aa bbrrooaaddeerr ttaarrggeett sseett——wwhhiillee mmaaiinnttaaiinniinngg
EE.. EEnneerrggyy 55%% EE.. BBeellggiiuumm 55%%
tthhee ssaammee ggeeooggrraapphhiiccaall ffooccuuss——hhaass ppuutt mmoorree MMiiccrroossoofftt sseeppaarraatteellyy ttrraacckkss nnoottiifificcaattiioonnss rreellaatteedd ttoo
FF.. DDeeffeennssee iinndduussttrryy 33%% FF.. IIttaallyy 33%%
oorrggaanniizzaattiioonnss aatt rriisskk ooff ccoommpprroommiissee,, aalltthhoouugghh UUkkrraaiinnee.. TThhiiss ddaattaa sshhoowwss UUkkrraaiinnee aaccccoouunntteedd ffoorr 2255%%
oouuttssiiddee ooff UUkkrraaiinnee tthhaatt rriisskk iiss aallmmoosstt eexxcclluussiivveellyy ffoorr ooff RRuussssiiaa’’ss ccyybbeerr ooppeerraattiioonnss,, mmaakkiinngg iitt tthhee pprriimmaarryy GG.. MMaannuuffaaccttuurriinngg 33%% GG.. EEssttoonniiaa 33%%
ccyybbeerr eessppiioonnaaggee.. ttaarrggeett.. TThheessee aaccttoorrss aappppeeaarr ttoo hhaavvee rreedduucceedd tthheeiirr HH.. TTrraannssppoorrttaattiioonn 33%% HH.. FFrraannccee 33%%
eeffffoorrttss ttoo ddeevveelloopp bbeessppookkee ooppeerraattiioonnss iinn ffaavvoorr ooff II.. FFiinnaannccee 22%% II.. NNeetthheerrllaannddss 33%%
FFoorr eexxaammppllee,, wwee hhaavvee oobbsseerrvveedd aa mmooddeesstt iinnccrreeaassee
lleevveerraaggiinngg tthhee ccyybbeerrccrriimmiinnaall eeccoossyysstteemm.. JJ.. IInntteerr--ggoovveerrnnmmeennttaall oorrggaanniizzaattiioonnss 22%% JJ.. PPoollaanndd 33%%
iinn RRuussssiiaann aaccttoorrss ttaarrggeettiinngg ssmmaalllleerr bbuussiinneesssseess iinn
ccoouunnttrriieess ssuuppppoorrttiinngg UUkkrraaiinnee.. TThhiiss iiss aann eexxppaannssiioonn RRuussssiiaann nnaattiioonn--ssttaattee aaccttoorrss ffooccuusseedd oonn OOuuttssiiddee ooff UUkkrraaiinnee,, tthhee ttoopp tteenn ccoouunnttrriieess mmoosstt
ooff tthheessee aaccttoorrss’’ ssccooppee,, wwhhiicchh pprreevviioouussllyy hhaadd bbeeeenn “ ggoovveerrnnmmeenntt oorrggaanniizzaattiioonnss aanndd tthhiinnkk ttaannkkss oorr aaffffeecctteedd bbyy RRuussssiiaann ccyybbeerr aaccttiivviittyy aallll bbeelloonngg ttoo
mmoossttllyy lliimmiitteedd ttoo ccoonnvveennttiioonnaall ppoolliittiiccaall ttaarrggeettss lliikkee NNGGOOss iinn EEuurrooppee aanndd NNoorrtthh AAmmeerriiccaa,, rreeflfleeccttiinngg NNAATTOO——aa 2255%% iinnccrreeaassee ccoommppaarreedd ttoo llaasstt yyeeaarr..
ggoovveerrnnmmeenntt aaggeenncciieess.. RRuussssiiaann ssttaattee aaccttoorrss mmiigghhtt TThheessee aaccttoorrss aappppeeaarr ttoo hhaavvee tthheeiirr iinntteelllliiggeennccee vvaalluuee ttoo RRuussssiiaa aammiidd tthhee AAlltthhoouugghh UUkkrraaiinnee aappppeeaarrss iinn tthhiirrdd ppllaaccee iinn oouurr
aallssoo vviieeww tthheessee ssmmaalllleerr ttaarrggeettss ooff ooppppoorrttuunniittyy aass rreedduucceedd tthheeiirr eeffffoorrttss ttoo oonnggooiinngg wwaarr.. nnaattiioonn--ssttaattee nnoottiifificcaattiioonn ssyysstteemm,, MMiiccrroossoofftt’’ss
lleessss rreessoouurrccee--iinntteennssiivvee ppiivvoott ppooiinnttss tthheeyy ccaann uussee ttoo ddeeddiiccaatteedd ttrraacckkiinngg ffoorr UUkkrraaiinnee rreevveeaallss iitt wwaass tthhee
ddeevveelloopp bbeessppookkee ooppeerraattiioonnss
aacccceessss llaarrggeerr oorrggaanniizzaattiioonnss.. pprriimmaarryy ffooccuuss ooff RRuussssiiaann ssttaattee aaccttoorrss..
iinn ffaavvoorr ooff lleevveerraaggiinngg tthhee
OOnn tthhee tteecchhnniiccaall ffrroonntt,, RRuussssiiaann ssttaattee aaccttoorrss aarree
ppuurrssuuiinngg ddiiffffeerreenntt aapppprrooaacchheess ttoo aacchhiieevvee tthheeiirr ccyybbeerrccrriimmiinnaall eeccoossyysstteemm..
ggooaallss.. TThhiiss yyeeaarr,, wwee oobbsseerrvveedd nnaattiioonn--ssttaattee aaccttoorrss SSoouurrccee:: MMiiccrroossoofftt TThhrreeaatt IInntteelllliiggeennccee nnaattiioonn--ssttaattee SSoouurrccee:: MMiiccrroossoofftt TThhrreeaatt IInntteelllliiggeennccee nnaattiioonn--ssttaattee
nnoottiifificcaattiioonn ddaattaa nnoottiifificcaattiioonn ddaattaa
oouuttssoouurrcciinngg pprree-- oorr ppoosstt--ccoommpprroommiissee ooppeerraattiioonnss

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 48
Nation-state adversary threats continued
GGlloobbaallllyy,, NNoorrtthh KKoorreeaann tthhrreeaatt aaccttoorrss aarree llaarrggeellyy
TTeenn sseeccttoorrss mmoosstt ttaarrggeetteedd bbyy NNoorrtthh KKoorreeaann TTeenn rreeggiioonnss mmoosstt ttaarrggeetteedd bbyy NNoorrtthh KKoorreeaann
ffooccuusseedd oonn tthhee IITT sseeccttoorr,, aannyy oorrggaanniizzaattiioonn oorr aasssseett
tthhrreeaatt aaccttoorrss tthhrreeaatt aaccttoorrss
aassssoocciiaatteedd wwiitthh bbaannkkiinngg oorr bblloocckkcchhaaiinn tteecchhnnoollooggyy,,
ddeeffeennssee,, aanndd mmaannuuffaaccttuurriinngg.. IInn aaddddiittiioonn,, aannyy eennttiittyy
NNoorrtthh KKoorreeaa
tthhaatt hhaass aa nneexxuuss wwiitthh EEaasstt AAssiiaann ppoolliiccyy,, ffrroomm NNGGOOss
aanndd uunniivveerrssiittiieess ttoo mmiinniissttrriieess ooff ffoorreeiiggnn aaffffaaiirrss,, iiss
RReevveennuuee ggeenneerraattiioonn aanndd
rreemmoottee wwoorrkkeerrss aa pprriioorriittyy ttaarrggeett.. IInn tthhee AAssiiaa--PPaacciifificc ((AAPPAACC)) rreeggiioonn A B C D E F H J A B C D F H J
ssppeecciifificcaallllyy,, NNoorrtthh KKoorreeaann tthhrreeaatt aaccttoorrss aarree iinntteerreesstteedd G I E G I
NNoorrtthh KKoorreeaann ssttaattee aaccttoorrss rreemmaaiinn aa iinn hheeaavvyy mmaannuuffaaccttuurriinngg aanndd aa bbrrooaadd ssppeeccttrruumm ooff
ppeerrssiisstteenntt tthhrreeaatt ttoo aa nnaarrrrooww ttaarrggeett sseett,, oorrggaanniizzaattiioonnss iinn SSoouutthh KKoorreeaa.. %% ooff ttoottaall %% ooff ttoottaall
wwiitthh aa ffeeww eexxcceeppttiioonnss ppuurrssuuiinngg tthhee AA.. IITT 3333%% AA.. UUnniitteedd SSttaatteess 5500%%
TThhiiss yyeeaarr,, aass NNoorrtthh KKoorreeaann ssttaattee aaccttoorrss ppuurrssuueedd
ssaammee sseeccttoorrss aanndd ggeeooggrraapphhiieess uussiinngg BB.. RReesseeaarrcchh aanndd aaccaaddeemmiiaa 1155%% BB.. IIttaallyy 1133%%
aann eevveenn mmoorree aaggggrreessssiivvee aapppprrooaacchh ttoo rreevveennuuee
tthhee ssaammee TTTTPPss yyeeaarr oovveerr yyeeaarr.. ggeenneerraattiioonn,, tthheeyy ddoouubblleedd ddoowwnn oonn ttrraaddiittiioonnaall CC.. TThhiinnkk ttaannkkss//NNGGOOss 88%% CC.. AAuussttrraalliiaa 55%%
aavveennuueess ssuucchh aass ccrryyppttooccuurrrreennccyy tthheefftt aanndd DD.. CCoonnssuummeerr rreettaaiill 77%% DD.. UUnniitteedd KKiinnggddoomm 44%%
AA mmaajjoorr iissssuuee tthhiiss yyeeaarr wwaass tthhee NNoorrtthh KKoorreeaann
rraannssoommwwaarree.. MMiiccrroossoofftt TThhrreeaatt IInntteelllliiggeennccee oobbsseerrvveedd EE.. FFiinnaannccee 55%% EE.. SSwwiittzzeerrllaanndd 22%%
IITT wwoorrkkeerr pprroobblleemm.. FFoorr oovveerr aa ddeeccaaddee,, NNoorrtthh
aa NNoorrtthh KKoorreeaann aaccttoorr ppaarrttiicciippaattiinngg aass aa RRaaaaSS aaffiffilliiaattee FF.. MMaannuuffaaccttuurriinngg 44%% FF.. IInnddiiaa 22%%
KKoorreeaa hhaass rreemmootteellyy sstteeaalltthhiillyy eemmbbeeddddeedd tteennss ooff
tthhoouussaannddss ooff wwoorrkkeerrss aatt oorrggaanniizzaattiioonnss aarroouunndd ffoorr tthhee fifirrsstt ttiimmee.. AA ppiivvoott ttoo RRaaaaSS ppaarrttiicciippaattiioonn GG.. HHeeaalltthh 44%% GG.. GGeerrmmaannyy 22%%
tthhee wwoorrlldd iinn aa ttrreenndd tthhaatt iiss qquuiicckkyy aacccceelleerraattiinngg.. ccoouulldd lleeaadd ttoo mmoorree rraannssoommwwaarree aattttaacckkss aass NNoorrtthh HH.. CCoommmmuunniiccaattiioonnss 22%% HH.. UUnniitteedd AArraabb EEmmiirraatteess 22%%
KKoorreeaa oouuttssoouurrcceess ppaarrttss ooff tthhee rraannssoommwwaarree ccyyccllee,,
AAss ddiissccuusssseedd bbeellooww,, tthhiiss ggrroowwiinngg aarrmmyy ooff wwoorrkkeerrss II.. DDeeffeennssee iinndduussttrryy 22%% II.. FFrraannccee 11%%
ffrreeeeiinngg uupp rreessoouurrcceess ttoo ffooccuuss oonn ccoommpprroommiissiinngg
rreemmiittss hhuunnddrreeddss ooff mmiilllliioonnss ooff ddoollllaarrss aa yyeeaarr ttoo JJ.. CCoommmmeerrcciiaall ffaacciilliittiieess 22%% JJ.. SSoouutthh KKoorreeaa 11%%
ttaarrggeettss.. MMiiccrroossoofftt aallssoo oobbsseerrvveedd aann iinnccrreeaassee iinn
NNoorrtthh KKoorreeaa.. WWhheenn ddiissccoovveerreedd,, ssoommee ooff tthheessee
pphhiisshhiinngg ooppeerraattiioonnss ttoo ccoolllleecctt IIPP aassssoocciiaatteedd wwiitthh NNoorrtthh KKoorreeaann nnaattiioonn--ssttaattee tthhrreeaatt aaccttoorrss ffooccuusseedd TThhee UUnniitteedd SSttaatteess rraannkkss fifirrsstt iinn oouurr nnaattiioonn--ssttaattee
wwoorrkkeerrss hhaavvee ttuurrnneedd ttoo eexxttoorrttiioonn,, aannootthheerr
wweeaappoonnss ssyysstteemmss.. pprriimmaarriillyy oonn oorrggaanniizzaattiioonnss wwiitthh aacccceessss ttoo nnoottiifificcaattiioonn ssyysstteemm ffoorr NNoorrtthh KKoorreeaa dduuee ttoo tthhee
aapppprrooaacchh ttoo bbrriinnggiinngg iinn mmoonneeyy ffoorr tthhee rreeggiimmee..
bblloocckkcchhaaiinn tteecchhnnoollooggyy oorr ccrryyppttooccuurrrreennccyy aanndd hhiigghh vvoolluummee ooff rreemmoottee IITT wwoorrkkeerr aaccttiivviittyy ttaarrggeettiinngg
TThheeyy ccoouulldd aallssoo uussee tthheeiirr eemmppllaacceemmeenntt ffoorr tthhee TThhiiss yyeeaarr,, MMiiccrroossoofftt oobbsseerrvveedd aatt lleeaasstt aa ffeeww uussiinngg
ssoouurrcceess ooff EEaasstt AAssiiaann ppoolliiccyy,, rreeflfleeccttiinngg tthheessee UUSS--bbaasseedd ccoommppaanniieess.. TThheessee wwoorrkkeerrss pprriimmaarriillyy
ddeelliivveerryy ooff mmaallwwaarree lliikkee rraannssoommwwaarree.. WWee ddiissccuussss cclloouudd iinnffrraassttrruuccttuurree ttoo ccoonncceeaall tthheeiirr CC22 iinnffrraassttrruuccttuurree,,
aaccttoorrss’’ mmaannddaatteess ffoorr rreevveennuuee ggeenneerraattiioonn aanndd ppuurrssuuee rroolleess aatt UUSS ccoommppaanniieess bbeeccaauussee tthheeyy oofftteenn
tthhiiss iissssuuee mmoorree iinn--ddeepptthh iinn tthhee iinnssiiddeerr tthhrreeaattss aann iinnccrreeaassee iinn tthheeiirr ssoopphhiissttiiccaattiioonn tthhaatt wwiillll mmaakkee iitt
iinntteelllliiggeennccee ccoolllleeccttiioonn.. ooffffeerr tthhee hhiigghheesstt ssaallaarriieess..
sseeccttiioonn ooff tthhiiss rreeppoorrtt.. hhaarrddeerr ffoorr ddeeffeennddeerrss ttoo ddeetteecctt aanndd bblloocckk aattttaacckkss..
WWhhiillee tthhiiss iiss ssttiillll aa nnaasscceenntt ttrreenndd,, iitt mmaayy bbee aann
iinnddiiccaattoorr ooff NNoorrtthh KKoorreeaann ssttaattee aaccttoorrss eexxpplloorriinngg nneeww
wwaayyss ttoo eevvaaddee ddeeffeennddeerrss..
SSoouurrccee:: MMiiccrroossoofftt TThhrreeaatt IInntteelllliiggeennccee nnaattiioonn--ssttaattee SSoouurrccee:: MMiiccrroossoofftt TThhrreeaatt IInntteelllliiggeennccee nnaattiioonn--ssttaattee
nnoottiifificcaattiioonn ddaattaa nnoottiifificcaattiioonn ddaattaa

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 49
Nation-state adversary threats continued
| Nation-state abuse of AI in influence  | Strategic implications  |     |     |     |
| -------------------------------------- | ----------------------- | --- | --- | --- |
operations: Emerging tactics and  Rapid growth in assessed AI content samples attributed to nation-state adversaries
A critical change, however, is the emergence of
| strategic implications  | AI-first actors—entities that prioritize AI-generated  |     |     |     |
| ----------------------- | ------------------------------------------------------ | --- | --- | --- |
 tnetnoc IA dessessa fo rebmuN 250
content and tools over traditional methods and
| Nation-state actors continue to evolve their cyber  |     |  etats-noitan morf selpmas |     |     |
| --------------------------------------------------- | --- | -------------------------- | --- | --- |
manipulations. These actors are shifting from
200
| and influence operations with the rapid adoption of  |     | spuorg yrasrevda |     |     |
| ---------------------------------------------------- | --- | ---------------- | --- | --- |
spectacle to saturation, flooding the information
| AI, employing more advanced, targeted, and scalable  |     | 150 |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- |
space with synthetic media to desensitize audiences
tactics. This year, the Microsoft Threat Analysis Center
and exhaust detection systems. In some cases, they
100
observed several new trends shaping the landscape
appear to operate semi-independently, drawing
of AI-enabled operations:
|                                                     | from state-aligned narratives while relying on AI to  | 50  |     |     |
| --------------------------------------------------- | ----------------------------------------------------- | --- | --- | --- |
| • AI twinning: the creation of digital replicas of  | maintain volume, speed, and plausible deniability.    |     |     |     |
0
trusted news anchors that deliver state-backed
The shift carries strategic implications. The convergence  Jan 2023 Jul 2023 Jan 2024 Jul 2024 Jan 2025 Jul 2025
narratives with a veneer of credibility.
of AI and cyber operations enables persistent, low-cost,
Date posted on media platform
• Training data poisoning: the attempt to
and scalable influence campaigns. Policymakers and
deliberately insert biased, misleading, or  Source: Microsoft Threat Intelligence
defenders must adapt accordingly—rethinking
manipulative content into the datasets that inform
attribution models, updating content authentication
AI models, with the aim of influencing model
|     | standards, and preparing for influence operations  | Overall sophistication impact by country  |     |     |
| --- | -------------------------------------------------- | ----------------------------------------- | --- | --- |
behavior and output.
where AI is not just a tool, but the core strategy.
• Voice cloning and masking: the use of generative
|     | Learn more on page 66 | 10  | July-Dec 2024 | Jan-June 2025  |
| --- | --------------------- | --- | ------------- | -------------- |
AI audio and visual tools to impersonate individuals
in ways that skirt legal thresholds but challenge
|                                                  |     |                           | China   | China   |
| ------------------------------------------------ | --- | ------------------------- | ------- | ------- |
|                                                  | *   | erocS tcapmI fo egarevA 8 |         |         |
| ethical norms.                                   |     |                           | Iran    | Iran    |
|                                                  |     |                           | Russia  | Russia  |
| The objectives remain consistent: to manipulate  |     | 6                         |         |         |
In the last six months,
public perception and shape conflict narratives.
AI in influence operations   Microsoft evaluates AI-generated content from
The integration of AI tools with conventional cyber
4
techniques—such as phishing, credential harvesting,  nation-state adversaries using a structured impact
has picked up aggressively
framework—assessing the potential stakes of the
and insider recruitment—has made these operations
2
content, its reach, and persistence across media
easier to scale, more effective, and harder to trace.
Attribution will become increasingly challenging as AI  platforms and audiences.
0
blurs the line between state-linked and opportunistic  Learn more  0 2 4 6 8 10
influence campaigns.
Average of Sophistication Score
5 things you need to know about tracking today’s
nation-state threats
Source: Microsoft Threat Intelligence

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 50
Nation-state adversary threats continued
Insider risk in the age of strategic Additionally, many internal cybersecurity tools are not include insider risk in regular risk assessments and • Conduct exit interviews and post-employment
geopolitical competition designed to detect trusted insiders working covertly incorporate insider risk programs information when monitoring. Exit interviews are an effective
with sophisticated external actors. For example, business decisions may impact the workforce. safeguard against insider risk. They provide a final
Insider threats: Emerging dimensions
data loss prevention (DLP) tools that would flag Key recommendations for enterprise leaders include: opportunity to detect warning signs, reinforce
and mitigations
large, suspicious file transfers often miss the slow, confidentiality and data protection obligations,
In an era of increasing geopolitical tensions and • Identify your crown jewels. Pinpoint the data
stealthy exfiltration of an espionage-minded and ensure access to sensitive information is
blurring of public and private sector interests, nation- or technologies that would be most devastating
insider. While zero trust network architecture adds revoked. These conversations also reduce the
state actors have increased their use of insiders to to lose (for example, trade secrets, source code,
protection against unauthorized devices and external risk of disgruntled retaliation, highlight potential
gain access to intelligence. These efforts are often formulas, merger and acquisition plans) and
connections, it requires consistent operationalization process weaknesses, and remind departing staff
long-term operations that are more difficult to detect implement extra safeguards around these assets
on the comprehensive zero trust principles and of their continuing obligations at a time when
than traditional hacks. Nation-states increasingly such as strict need-to-know access, encryption,
security strategy to prevent unauthorized use of a adversarial entities may seek to recruit them (this
use non-state actors—including cyber mercenaries, and monitoring of access logs in real time.
legitimate user account. is more specific to those with security clearances).
criminal syndicates, and front organizations—to • Implement continuous identity verification.
Documenting the exchange creates an audit trail,
conduct insider threat operations that target private According to DTEX Systems and the Ponemon Move beyond one-time sign-ins and use adaptive
demonstrating that the organization has taken
sector entities.11 These proxies obscure attribution Institute, companies take 81 days on average to authentication and behavioral biometrics (like
prudent steps to protect its assets, reputation, and
while enabling scalable, persistent campaigns. contain an identified insider incident.13 This long dwell typing patterns or mouse movements) to
people during workforce transitions.
time gives nation-state actors a persistent foothold continuously verify that the person behind an
China and Russia have both cultivated ecosystems • Engage in holistic insider risk management.
to expand their access, cover their tracks, and even account is the genuine user. If an account starts
to infiltrate corporate environments, often using Effective insider risk management requires a
establish back doors for future use. behaving oddly—for example, a finance employee
academic or professional affiliations to identify and blend of technology, culture, and collaboration.
begins downloading large engineering design
exploit vulnerable insiders.12 The sectors most at Layoffs and workforce reductions across government Deploy behavioral analytics and DLP solutions
files—require immediate re-authentication or
risk—AI, quantum technologies, biotechnology, and and private industry add another dimension to to detect unusual data transfers or privilege
manager approval.
defense—have both economic and military value. the insider landscape. Such workforce adjustments escalations, particularly among highly privileged
• Divide and limit access. Architect your systems
Insider espionage can cause immediate financial loss can inadvertently exacerbate insider threat risks users. Intelligence sharing between government,
on the assumption that an insider might turn
and long-term competitive harm, erasing years of through disgruntled employees or weakened security private industry, and recruiting platforms also helps
malicious. No single individual should be able to
innovation and market advantage through stolen oversight due to budget cuts and staff reductions. expose fake companies and protect organizations
access all critical data. Use segregation of duties
research and development. Malicious insiders can leak sensitive data or redirect from risky potential hires.
and data fragmentation so that even if one
corporate assets to corporate adversaries. Third-party
Most organizations’ cybersecurity frameworks account is compromised, an attacker can’t sweep Additionally, companies can use dedicated insider
suppliers with privileged access might unknowingly
were not initially built with an insider threat in mind. up everything. threat monitoring tools to reduce the overarching
introduce vulnerabilities, making rigorous vetting
Compliance standards and cybersecurity best • Foster a vigilant culture. Employees are often the risk profile. As an example, companies utilizing
and alignment with internal security policies essential
practices traditionally assume that the attacker is first to notice unusual behavior in a peer. Create a Communications Compliance can be notified of
to mitigating insider-driven exposure. Facing this
an outsider trying to break in, but when the threat culture where reporting a concern is encouraged potential talent recruitment outreach.14
threat requires an intentional strategy. For businesses,
actor is an insider with valid access, many of those and rewarded.
the issue of insider risk should be elevated to
measures could be bypassed by default.
the boardroom and C-suite. Executives should

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 51
Nation-state adversary threats continued
Detecting North Korean IT workers • Ensure that the applicant is seen on camera during
North Korea has quietly built a large remote multiple video telecommunication sessions.
employment staffing apparatus that has emplaced • Confirm that the applicant’s contact information
thousands of workers at unwitting companies includes a real phone number, not Voice over
globally. These state sponsored workers, who are Internet Protocol (VoIP), and a residential address.
physically located either in North Korea or abroad,
Once hired, employees should be monitored for
submit tens of thousands of job applications a
the following:
month for software, web development, and other
• Installation of unauthorized software such as RMM
technology/IT positions. This year, we also saw
tools and virtual private networks (VPN), especially
these workers branching into other job types, such
Astrill VPN.
as structural engineering. Because these workers
• Geographical irregularities— for example, a
opportunistically apply to remote job postings, they
supposedly United States-based employee signs
represent a threat to organizations anywhere in the
in from an IP address associated with China, or the
world, in any sector.
employee device engages in impossible travel, in
To help organizations identify potential North Korean which the IP address location changes faster than
state sponsored remote workers, we recommend it would be possible for the employee to travel
the following employment vetting recommendations. between those locations.
For a more extensive discussion, see our blog on • Camera avoidance—the employee creates excuses
Jasper Sleet.15 for why they are never seen on camera.
During the pre-hire stage: In addition to technical monitoring, organizations can
• Check resumes for consistency of names, also use simple, non-technical identity verification
addresses, educational history, and job titles. techniques such as asking employees to turn on
Consider contacting references by phone or their camera periodically and comparing the person
video teleconference. on camera with the one that took delivery of the
• Confirm that the applicant doesn’t have multiple corporate laptop.
social media accounts under different names.
• Scrutinize staffing company employees, since
this is a primary avenue for North Korean state
sponsored workers to land jobs.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 52
AI’s double-edged influence:
Using AI to augment traditional cyberattacks
Defending and disrupting the digital landscape
Automated
spearphishing
Automated
Deepfakes
The AI threat landscape is diverse and Traditional cybersecurity scams
rapidly evolving. The distinctive nature
This category encompasses both cyberattacks Language
of AI-related threats demands that Managing C2 translation
that are amplified using AI and direct attacks
organizations develop new strategies
on AI systems. These threats target underlying Automating
and adaptive approaches to effectively infrastructure and exploit human vulnerabilities. exfil-to-lateral Synthetic
Identifying identity Open-
manage emerging risks. Actors conducting these attacks range from sensitive movement creation source
pipeline
credentials scanning
less-skilled individuals to sophisticated state-
For example, as AI adoption accelerates, so does
sponsored groups.
AI’s access to sensitive data. Whether through
user-supplied inputs, credentialed access to existing Cyberattack augmentation refers to the use of AI
Ransomware
content, or the creation of custom fine-tuned to enhance traditional cyberattacks. The chart on the negotiations AI Reconnaissance
models built on proprietary data, the volume and right highlights the primary areas of augmentation,
sensitivity of data involved continue to grow—which most of which are based in the automation of
means risks associated with the compromise of or previously time-intensive activities.
Cloaking
Researching
unauthorized access to that data are also growing. services
Defenders must counter AI augmentation by Embedded
Bot
AI-associated challenges include both threats to AI fostering a strong cybersecurity culture, training prompt automation
injection
and its users and threats enabled by AI. AI-associated users to recognize manipulation tactics, and
threats can be divided into five major categories: implementing authenticated communication
Code
traditional cybersecurity, malfunction, dangerous channels. AI-driven detection systems that flag Malware generation
capabilities, operational issues, and emerging threats. anomalies in communication patterns or identify Obfuscating generation and
debugging
deepfake content in real time can also serve as or mutating Domain
malware impersonation
critical safeguards, while AI can detect vulnerabilities, payloads
automate patching, and improve threat intelligence.
Tool Exploit
development development

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 53
AI’s double-edged influence: Defending and disrupting the digital landscape continued
Use of generative AI has introduced new layers of Cyberattack automation refers to the use of AI
Generative AI threat map
complexity to the threat landscape. The diagram to enhance traditional cyberattacks. Threat actors
on the left illustrates how risks span across usage, can now automate vulnerability discovery, malware
AI usage User interaction with generative AI-based apps Generative AI-based extended risks application, and platform levels—highlighting issues generation, and data analysis. In response, defenders
security
such as sensitive data exposure, prompt injection, are also leveraging AI to detect vulnerabilities,
insecure plugin design, and foundational threats like automate patching, and improve threat intelligence.
model theft and training data poisoning.
In the realm of social engineering, AI can automate
Sensitive information Shadow IT/harmful third-party
Indirect prompt injection attacks are particularly phishing campaigns, generate deepfakes, and
disclosure LLM-based app or plugin
concerning for developers and organizations that craft highly convincing fraudulent messages.
rely on large language models (LLMs) to process Defenders must counter this AI augmentation by
untrusted or user-generated content. In these attacks, fostering a strong cybersecurity culture, training
malicious instructions are embedded in seemingly users to recognize manipulation tactics, and
AI insider risk, excessive benign data—such as a resume containing hidden implementing authenticated communication
AI agency and overreliance
Generative AI-based app lifecycle text that instructs the AI to favor a candidate. If the channels. AI-driven detection systems that flag
application
security AI is trusted to act autonomously, it might execute anomalies in communication patterns or identify
these hidden commands, leading to biased decisions, deepfake content in real time can also serve as
unauthorized outputs, or even system compromise. critical safeguards.
Prompt injection Data leak, Insecure Defending against these attacks requires both
UPIA/XPIA exfiltration plugin design technical tools—like filters that detect hidden or
malicious text—and strong coordination across
teams. Developers, security experts, and decision-
makers must work together to ensure protections are
built, tested, and enforced consistently.
AI
Fundamental model and training data Model theft involves the unauthorized replication
platform
security of an AI system’s architecture, behavior, or training
data. This can be a result of corporate or nation-
state espionage, especially when the stolen model
is used to develop competing technologies.
Training data poisoning Model theft and model poisoning
Mitigation strategies include access controls,
encryption, threat monitoring, secure development
practices, and coordinated response plans—
shared responsibilities among developers, hosts,
and regulators.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 54
AI’s double-edged influence: Defending and disrupting the digital landscape continued
| Adversarial exploitation   | Information leakage can be exploited by attackers  |     |     |     |     |     |
| -------------------------- | -------------------------------------------------- | --- | --- | --- | --- | --- |
AI creates new attack surfaces
| of inherent risks  | during runtime or from training data, exposing  |     |     |     |     |     |
| ------------------ | ----------------------------------------------- | --- | --- | --- | --- | --- |
sensitive organizational details. AI systems handling
AI malfunctions can overlap with
customer interactions or proprietary data are prime
adversarial threats. Overreliance on
targets—threat actors can extract confidential
AI, information leakage, and agency
|     | information through prompts or vulnerabilities  |     |     |     | N   |     |
| --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
problems are key concerns that affect   in datasets. Strong defenses require strict data  e
w
all users of AI.  governance: enforce data labeling and permission
GenAI   A
AI data and
expiration, encrypt sensitive data, and implement  prompts and   I
Overreliance on AI can be exploited by attackers  orchestration
policies to prevent over-permissioning. You can also  responses a
| who feed manipulated data or craft deceptive  |     |     |     |     |     | t   |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- |
t
use AI preemptively to detect information leakage
| scenarios, seeding false information into systems  |                                                       |     |            |     |     | a   |
| -------------------------------------------------- | ----------------------------------------------------- | --- | ---------- | --- | --- | --- |
|                                                    | by regularly asking your own AI tools to research     |     |            |     |     | c   |
| or even triggering disruptions to operations.      |                                                       |     |            |     |     | k   |
|                                                    | confidential subjects within your organization which  |     | Web data   |     |     |     |
One way to reduce this risk is to treat the AI like  Plugins
|     |     |     | and source   |     | AI models | s   |
| --- | --- | --- | ------------ | --- | --------- | --- |
they shouldn’t be able to access, and securing  and functions u
| a new hire whose work will benefit from review  |     |     | context |     |     |     |
| ----------------------------------------------- | --- | --- | ------- | --- | --- | --- |
any leaks they inadvertently discover and exploit.
| and feedback, not an infallible expert. On the  |     |     |     |     |     | r   |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
f
These measures reduce the risk of adversaries
| development side, this includes designing systems  |                                                     |     |     |     |     | a   |
| -------------------------------------------------- | --------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                    | weaponizing AI to compromise critical information.  |     |     |     |     | c   |
| to be secure by design and default, with human     |                                                     | T   |     |     |     | e   |
oversight. On the deployment side, this means  Agency risks can be exploited by attackers  r s
a
ensuring AI is just one component of a larger  manipulating AI objectives to favor their interests  d Application Cloud Network
| process that you secure. Implementing periodic  | over stakeholders’. For example, adversaries might  | i   |     |     |     |     |
| ----------------------------------------------- | --------------------------------------------------- | --- | --- | --- | --- | --- |
t
i
| audits of AI outputs, establishing review  | inject biased data or influence reward signals so an AI  | o   |     |     |     |     |
| ------------------------------------------ | -------------------------------------------------------- | --- | --- | --- | --- | --- |
n
| protocols, and fostering a culture of questioning  | agent prioritizes advertisers or malicious actors over  |     |     |     |     |     |
| -------------------------------------------------- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
a
AI recommendations are essential strategies for  users, eroding trust and security. Organizations must  l Identity Data

t
| users of AI to mitigate potential overreliance  | counter this with transparency, explainability, and  | h   |     |     |     |     |
| ----------------------------------------------- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
risks. It is critical to treat AI as an augmenting  strong governance. Scenario testing for conflicts  r
e
a
tool rather than an infallible decision-maker.  and embedding ethical safeguards into design are  t
 v
|     | critical to prevent adversarial exploitation of AI goals,  |     | e   | Endpoints |     |     |
| --- | ---------------------------------------------------------- | --- | --- | --------- | --- | --- |
c
|     | especially in autonomous agentic systems.  |     | t   |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- |
o
r
s
Learn more on page 63

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 55
AI’s double-edged influence: Defending and disrupting the digital landscape continued
Dangerous capabilities Operational issues The relative opacity of model files makes compromise Risks from read-write memory include issues such
of a model very difficult to detect after the fact, as data corruption, latent poisoning attacks, and
AI’s powerful capabilities extend to producing Addressing operational issues in AI systems requires
making securing of the build process especially positive-feedback loops. These can erode a system’s
sensitive materials and enhancing skills in ways that, if robust strategies that balance technical precision with
important. Common model-building tools reliability, particularly when it relies on dynamic
misused, pose significant security risks. As a result, it business demands. Issues that might arise during the
should produce dependable artifacts, such as a memory updates, and are a pressing concern for
is essential for developers of AI and policymakers to use of AI include logging and monitoring, ensuring
comprehensive software bill of materials (SBOM) developers and security professionals who manage
establish clear guidelines to ensure appropriate use model integrity, and equipping product teams with
that can be used to verify the authenticity and AI-driven systems. AI developers and platform
while minimizing the risk of misuse. the skills to manage AI-associated risks effectively.
functionality of deployed models. For instance, providers should implement strict data validation, use
Production of sensitive materials refers to the Logging and monitoring of AI use are foundational frequent integrity checks can ensure that no immutable data structures, and employ advanced
generation of content such as manipulated imagery for incident detection, response, and compliance, but unauthorized alterations have been made to the monitoring tools to help mitigate these risks.
or videos that could be used unethically, such as they can also expose sensitive data, create security system, safeguarding against potential breaches.
child sexual abuse material (CSAM). As previously risks, and overwhelm teams with unfiltered or biased
Emerging threats
mentioned, deepfakes also pose serious risks in information. When done correctly, the process of
Learn more
areas like financial fraud, corporate espionage, logging and monitoring involves systematically New threats related to AI and its use are continually
and spreading false information during crises, recording user inputs, system outputs, and internal emerging as AI technology evolves. Current research to Researchers find—and help fix—a hidden
which can cause confusion and hinder emergency behaviors of AI systems to ensure transparency and mitigate these threats includes securing long-running biosecurity threat | Microsoft Signal Blog
responses. Deepfakes can also facilitate identity accountability. At the same time, logging conversations agents and managing risks from read-write memory.
theft and nonconsensual intimate imagery (NCII). might raise privacy concerns. While the volume and
Securing long-running agents involves ensuring
NCII is frequently used to facilitate harassment and sensitivity of this data can pose challenges, solutions
agents remain aligned to their goals and managing
extortion, especially of minors. such as advanced analytics and automated auditing
errors and confusion from hostile data (which might
tools can streamline the process. For example,
Skill uplift through AI can empower individuals to come from external manipulation). This focus area
implementing systems that track anomalies in real
acquire new knowledge, but it does require oversight is particularly relevant for industries relying on
time can help detect fraudulent activities or unusual
to ensure that those skills are not used for malicious automation and AI-based decision-making or for
system behaviors before they escalate.
purposes. For example, bad actors could use AI to companies that use AI agents to automate customer
learn how to develop chemical weapons or plan Model integrity ensures that the AI systems operate service. Corrupted data or adversarial attacks can
mass-casualty attacks. AI should be designed with reliably and as intended over time. However, AI disrupt operational efficiency or lead to a reputational
strict filters and intent detections to block requests models are subject to the same supply-chain risks as loss. Enterprise users of AI can implement strategies
for harmful knowledge, with suspicious queries other software. “Time bomb” attacks, in particular, like continuous goal verification protocols, anomaly-
reviewed by humans. modify the model during training to cause it to detection systems, and adaptive learning algorithms
produce attacker-prescribed outputs when specific which are essential to maintain reliability and enhance
inputs appear, such as when the model is used by a trust in agents.
particular company, past a particular date, or when
an image includes a certain embedded visual trigger.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 56
AI’s double-edged influence: Defending and disrupting the digital landscape continued
Storm-2139: How Microsoft disrupted
A global network of developers, providers, and end users Recommendations for defense
an AI exploitation and abuse ring
Microsoft’s amended complaint in February 2025 named the key developers and providers
Microsoft, together with generative
behind the nefarious tools used to create abusive AI-generated images. Regularly check and update access codes to help
AI technology providers worldwide,
prevent unauthorized use, and set up alerts to
is navigating the challenge of driving
notify you of unusual activity.
AI innovation while staying true to D
Adopt modern authentication methods like
our core principles. Our Digital Crime P
OAuth-based systems and enforce MFA for
Unit’s action against a group we track U
critical accounts.
as Storm-2139 exemplifies how we
can proactively shape the future of Implement advanced monitoring and logging
responsible AI. D P U tools to detect irregular patterns and conduct
periodic security audits.
In July 2024, Microsoft uncovered a global network
exploiting stolen API keys to bypass AI risk and Any evidence of violative images and prompts
governance measures of various popular AI services, Key should be reported to national authorities.
including Azure OpenAI. The developers were
using and selling their nefarious tools, which were D Developers
used to create thousands of abusive AI-generated
Learn more
images, including celebrity deepfakes, sexually
P Providers
explicit imagery, and misogynistic, violent, or hateful
U Users Disrupting a global cybercrime network abusing
synthetic content. By using content provenance tools
generative AI | Microsoft On the Issues
and open-source intelligence, the Digital Crimes Unit
(DCU) was able to trace the origins of this malicious To disrupt the network, the DCU implemented The response from the cybercriminal community Taking legal action to protect the public
behavior. The network we uncovered included the a two-phase approach. In December 2024, the was swift and revealing. Some users went silent, from abusive AI-generated content |
software developers, providers who customized DCU filed a civil complaint to seize and sinkhole while others lashed out—posting warnings, Microsoft On the Issues
and distributed the software, and end users who the primary domain used by Storm-2139 to blaming each other, and even doxing attorneys and
Microsoft files lawsuit against LLMjacking gang
deployed these tools to create synthetic content. communicate and collaborate. This action allowed investigators. Whistleblowers emerged, naming
that bypassed AI safeguards | CSO Online
the DCU to uncover additional evidence, leading key figures and helping the DCU advance its
to an amended complaint in February 2025 that investigation. In March 2025, Microsoft provided How Microsoft is taking down AI hackers who
named the key developers and providers behind extensive criminal referrals to the Department of create harmful images of celebrities and others
the tools. Justice (DOJ), Federal Bureau of Investigation (FBI),
Responsible AI Principles and Approach |
United Kingdom’s National Crime Agency (NCA),
Microsoft AI
and Europol’s European Crime Center (EC3).

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 57
Quantum technologies:
Strategic priority in a new era of competition
Quantum technologies—computing, Commercial companies are driving a significant amount
communications, and sensing—are of current quantum R&D and private enterprise now
foundational to future economic and sits at the epicenter of the global race to develop
national security. quantum technologies. Certain adversaries may also
leverage additional capabilities to strengthen their
Quantum technologies’ potential to accelerate
position through espionage, including the possible
scientific discovery, enable breakthroughs in secure
targeting of Corporate R&D programs, startups,
communications, and disrupt encryption have and academic spin-offs.16 It is therefore imperative
made this technology a high-priority area. Indeed,
to establish robust safeguards and strategic
governments have identified quantum technology as
preparedness now, before quantum technology
a national imperative. Allies and adversaries alike are
becomes widely operational. The stakes are existential:
pursuing quantum capabilities through new national
leadership in quantum could determine not just
research and development (R&D) programs, as well
competitive advantage but the future integrity of secure
as investments to cultivate their own academic and
communications and the global digital economy.
private sector ecosystems. Certain adversaries may
The implications of the race to quantum advantage
also leveraging additional capabilities to strengthen
are sweeping:
their position through espionage.
• Industrial scientific leadership: Quantum
technologies could drive a new wave of innovation
across chemistry and material science discoveries.
For a quantum future that is secure, prosperous, and inclusive, governments
• Impact to cryptography: A sufficiently powerful
and industries must do three things:
quantum computer could break widely used public-
key algorithms, undermining the security of digital
1. Prioritize security while simultaneously embracing innovation.
communications and data.
2. Reshape sectors of the economy to be first movers and capitalize on the quantum future.
• Sensor superiority: Quantum sensors could detect
stealth air or naval assets, eroding strategic deterrence. 3. Work globally to ensure that all humanity benefits through the responsible
and ethical use of transformative technology.
Learn more on page 74

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 58
Part II
The defense
landscape
60 AI and advanced defense
64 Countering nation-state and emerging threats
70 Policy, capacity, and future readiness
76 Strategic vision and global commitments

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 59
Key 3.AI agents can help in threat 6.Cooperation across borders is 9.Governments are moving away
mitigation and incident response crucial to mitigate cyber risks from voluntary compliance toward
takeaways AI agents can help organizations automatically Whether addressing threats like ransomware and cyber cyber requirements
respond to threats, including by suspending suspicious mercenaries or managing emerging technologies like
Across the globe, governments are accelerating
accounts and initiating a password reset, containing AI, cooperation between the public and private sectors
efforts to manage cyber risk through new laws and
a breach before an attacker can conduct further and academia is essential. This includes formulating
regulations. In particular, they are moving from
Insights and actions
malicious activities. Agents can also enforce policies, policy frameworks, establishing protocols, working on
voluntary guidelines to enforceable standards that
for cyber defense monitor credentials and app permissions, and control shared initiatives, intelligence sharing, and engaging
emphasize accountability, risk management, and
employee accesses. in dialogue.
timely incident reporting. At the same time, to
maximize their effectiveness, governments must
Read more on p68 Read more on p67
pursue harmonized, risk-based approaches that
1.Cyber risk is business risk 4.Organizations should implement a 7.Resilience must be woven promote interoperability and reduce duplication
across borders.
As intrusion attempts become the norm, it is essential security framework for AI use in by design
that governing boards and C-suites recognize that When using AI, it’s important to mitigate risks such as Given the persistence of cyber threats, it is Read more on p77
cyber risks are a form of business risk and treat them data leaks or data oversharing, as well as risks to the AI important that systems are designed to anticipate,
accordingly. Solutions to help mitigate this risk include itself such as prompt injections and insecure extensions. withstand, recover from, and adapt to disruptions. 10.Organizations must prepare
conducting security exercises, implementing key This means organizations require a strong security Resilience must be embedded into the very DNA of an for quantum computing
performance indicators tied to cyber hygiene, and framework that helps them: prepare for AI adoption; organization’s infrastructure.
Quantum computing poses a serious threat to current
cross-training teams to build resilience. discover how AI is being used within the organization;
cryptographic systems. As a result, organizations
Read more on p72
protect sensitive data, AI agents, applications and
Read more on p69 should inventory their cryptography (keys, certificates,
models; and govern AI operations.
8.Public-private collaboration is key and protocols) and establish a roadmap to replace
2.AI-powered defense is essential vulnerable algorithms with PQC standards as
Read more on p63 to disrupting cybercrime ecosystems
they become available. Microsoft has established
As adversaries begin to move at the speed of AI, so
must defenders. Microsoft uses AI to conduct threat 5.Deterring cyberattacks requires Successful operations like the Lumma Stealer takedown the Quantum Safe Program to achieve “quantum
demonstrate the power of coordinated legal, technical, readiness” by systematically integrating post-quantum
analytics, identify detection gaps, validate detections, political solutions
and operational strategies across sectors to disrupt cryptographic algorithms into our services.
identify phishing campaigns, automate remediation,
Individual defensive activities aren’t enough to turn malicious infrastructure and protect critical assets.
and shield vulnerable users. the tide of cyber threats from nation states. To protect Read more on p74
Read more on p64
Read more on p60 cyber infrastructure, governments must build
frameworks that signal credible and proportionate
consequences for malicious behavior. This includes
regularizing public attributions, signaling red lines, and
imposing consequences.
Read more on p66

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 60
AI and advanced defense
AI-powered defense: Transforming
AI at every stage of the detection lifecycle
threat detection Microsoft’s investment in AI is transforming
our defense operations and enabling
Threat intel & incidents
Detection Engineering (DE) is a fast-growing
detection engineers to effectively protect
discipline in mature cybersecurity organizations.
AI threat analyst Microsoft and our customers.
Given the increase in the volume and sophistication
of cyberattacks, there is a pressing need for Top threats Threat analysis
dedicated detection teams. While incident There is a large volume of open source and proprietary
responders can write detections during an incident, AI detection gap analyst threat intelligence available, but an organization’s ability
these detections are typically incident-specific and to leverage this information is limited by the speed
narrow. The result is a detection portfolio that is Detection gap and effectiveness of humans at extracting relevant
information. This kind of task is perfectly suited for LLMs,
always one step behind the attacker. DE teams focus
which can sift through threat intelligence and extract
AI telemetry identifier
on strategic, scalable prioritization and development commonalities and kill chains.
of a dynamic, forward-looking detection portfolio.
Relevant telemetry
Identifying detection gaps
At Microsoft, we developed a variety of AI solutions
A common approach for assessing coverage is to map
AI detection author
to help DE teams effectively manage detections
threats prioritized in the previous step to MITRE ATT&CK
throughout their lifecycle. On the right, we give TTPs. We then match the detection portfolio against
Detection
examples of these AI solutions and how they can these TTPs to identify areas that need more coverage.
transform every stage of a detection’s lifecycle. Detection portfolio Filters + logic We use LLMs to map both top threats and existing
modification detections to the chosen attack framework at scale.
AI attack simulator
Detection authoring
A challenge in detection authoring is identifying the
Attacks AI detection evaluator
telemetry that contains information relevant to the
detection. This problem is compounded by the vast
Metrics
amounts and types of telemetry collected by security
information and event management (SIEM) solutions.
Reporting

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 61
AI and advanced defense continued
We are developing AI solutions that create detections Securing identity in the age of AI: AI agents for response and remediation • Credential hygiene agents monitor secrets and
at different levels of sophistication. For basic Proactive and automated protection Beyond using AI to detect identity threats, credentials. If an API key or client secret not used
tests, for example, AI can generate rule-based organizations are increasingly using AI agents to in months still sits in an app configuration, the
AI and machine learning are revolutionizing how
logic that checks for a small set of specific events. respond automatically to threats. These agents can agent might recommend rotating or removing
we detect identity threats by finding subtle patterns
For correlation detections, AI leverages telemetry act in the identity environment with minimal human it to prevent potential abuse. Similarly, this
humans miss. Modern AI-driven identity protection
metadata to identify candidates, then generates guidance—sometimes even on their own. When they agent can monitor for leaked credentials or
systems continuously analyze billions of sign-ins and
the logic that correlates them with malicious either confirm or strongly suspect a threat, they can known compromised passwords and trigger
user signals, learning what normal behavior looks like
activity. For behavioral detections, we use machine act within seconds—far faster than a human can immediate remediation.
for each user and entity so they can spot the early
learning to establish baseline behaviors and identify respond manually. For example, if multiple high-risk • Application risk detection agents keep an eye
signs of an attack. For example, AI can detect a slow
anomalies that can signal malicious activity. signals indicate an account compromise, an AI agent on app permissions and behaviors. Should an app
password spray attack by recognizing a coordinated
can immediately suspend the account, initiate a request higher privileges or exhibit anomalous
Rapid advances in the development of code- pattern of sign-in attempts spaced out over a long
password reset, and notify administrators, containing behavior with user-granted access, the agent
generating LLMs means that whatever the level duration, a pattern that would slip past traditional
the breach before an attacker can escalate their will alert security and preemptively revoke or
of sophistication of the detection logic, we can rate-limit rules. Similarly, AI models evaluate each
access privileges. quarantine the app. This will swiftly reverse
automate its implementation of it in our chosen sign-in against dozens of risk factors (impossible
unauthorized access, nullifying the malicious
coding language. travel, unfamiliar devices, abnormal time of access, AI agents also tackle preventative maintenance,
consent threat vector.
etc.) to assign a risk score in milliseconds. With this working continuously to reduce the attack surface
Detection validation • User lifecycle agents govern access by
information, advanced anomaly detection algorithms and fix security gaps that attackers might exploit.
Detection Engineering must test the artifacts they automatically assigning the right permissions
can instantly flag a threat actor using a stolen token
generate. A simple test injects or executes the events • Policy enforcement agents review identity based on attributes such as role, department,
from an unusual location or attempting to mimic a
or behaviors the detection is intended to catch. configurations and policies like MFA enrollment or group, and certifications. For instance, when
user’s typical location.
This is the DE equivalent of unit tests. conditional access rules and automatically reinforce an employee leaves, the agent revokes all their
While AI is still new, its impact is already significant: any weak spots. After the agent flags users not sessions and removes all access, closing a common
However, attackers use sophisticated multi-stage
thanks to AI-based protections, providers report covered by MFA, it can help enroll them or adjust gap that turns lingering accounts into backdoors.
approaches and decide what to do in later stages
automatically neutralizing the vast majority of identity the policy scope. This ensures security policies If an employee changes roles, the agent could
based on information gained in earlier stages.
attacks. With the assistance of AI, security teams can cover every user and scenario as intended. suggest removing permissions no longer needed,
While unit tests validate individual detections, we
remediate threats before they cause damage, with preventing accumulation of privileges.
need end-to-end testing to ensure the detection
minimal false alarms or missed detections, making
portfolio as a whole is effective. Microsoft has AI-driven agents operate under strict policies, only
defenses both faster and smarter.
developed agentic red teaming approaches where taking well-defined actions and requiring human-in-
autonomous AI agents simulate complex, adaptive the-loop.
multi-stage attacks, enabling effective validation
at scale.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 62
AI and advanced defense continued
Cloud-scale AI defense: A layered defense strategy is essential. At the surface,
Defensive AI systems protecting AI agents
Guardian agents Small Language Models (SLMs) provide lightweight,
highspeed screening of prompts and responses,
As organizations accelerate their
flagging suspicious patterns at scale. Deeper in the Guardian agent
adoption of AI, threat actors target that
funnel, suspicious signals flow from the SLMs into
AI. This demands a new class of defense:
advanced LLMs, combined with context from the
AI systems purpose-built to protect
agent’s internal processes, such as tool invocations,
SLM filter
other AI systems. reasoning traces, and state changes. The LLM
correlates these signals, reconstructs the likely
One of the most pressing challenges is prompt
attack scenario, and issues a verdict: allow, rewrite,
manipulation attacks, including direct and indirect LLM analysis
or block—and raises an alert. This funnel approach
prompt injections, and exploitation through
balances efficiency with depth, ensuring both broad
protocols such as Model Context Protocol (MCP)
coverage and precise decisions.
and Agent2Agent (A2A). The heart of these attacks Decision engine Protective agent
is usually to inject a malicious payload into the AI’s Beyond the model itself, telemetry from orchestration
processing stream which hijacks its behavior and frameworks, APIs, and cloud services play a critical
causes it to run attacker-controlled instructions. role. AI-driven engines baseline normal behavior Action gate
Chain-of-thought
These attacks involve reconnaissance phases, where across these systems and raise alerts when deviations
attackers systematically probe the model to identify occur, such as an agent invoking an unexpected
vulnerabilities before launching targeted operations. function or accessing an untrusted domain.
Tool invocation
Malicious content can be linguistically obfuscated or These signals are then correlated across identities, Output
embedded in seemingly benign files, which defeat endpoints, SaaS applications, and additional
simple keyword and regex filters. Depending on the cloud workloads including containers, serverless
system affected, these attacks may execute read or functions, virtual machines, Kubernetes pods, and
write commands, exfiltrate data, or subtly modify the managed platform services, to reveal coordinated
system’s behavior to suit attacker objectives, such as attack patterns.
by changing the outcome of analyses. Logs and alerts
In this AI-first era, defending AI with AI is not just a
So, defenders deploy intelligent ”guardian agents”— necessity, it’s a strategic advantage. By embedding
dedicated security agents with transparent access to intelligent, adaptive, and context-aware defense
the protected model. This visibility into the model’s mechanisms directly into AI systems, organizations
internal reasoning, tool usage, and decision chains can stay ahead of adversaries and ensure the Security operations center (SOC)
enables real-time detection of malicious behavior integrity of their AI assets.
that would otherwise remain hidden.
Learn more on page 70

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 63
AI and advanced defense continued
Securing AI systems: Safeguarding AI vs. cybercrime: How automation
This framework should *
the enterprise and its innovations is shifting the balance
help organizations
The adoption of generative AI by The DCU is leveraging AI to confront the rapidly
Using innovative
enterprises introduces two security Prepare evolving threat landscape and the increasing
AI-driven tools, the
imperatives: securing the enterprise sophistication of cybercrime. At the heart of the
Anticipate AI adoption by establishing policies,
from risks associated with the enterprise training, and secure foundations before deploying DCU is accelerating DCU’s strategy is a suite of specialized AI tools
that enhance its ability to monitor, investigate, and
AI and securing the enterprise AI itself. AI, including data classification and security, access its impact in the fight
disrupt malicious activity. For example, the DCU has
controls, and zero trust.
The former focuses on mitigating risks posed by against cybercrime. developed a machine learning system that analyzes
how generative AI is used across the workforce— password spray attacks to distinguish between
Discover
for example, data leaks, data oversharing, misuse normal and targeted behavior. This enables the team
of third-party tools, or unintentional sensitive Gain visibility into how AI is used in the to identify high-risk users and proactively protect
information disclosure. The latter addresses organization. Monitor AI applications and agents, vulnerable populations—such as rural hospitals
risks within the AI systems themselves, including detect unsanctioned shadow AI tools, identify and political candidates—before harm occurs.
prompt injections, training data poisoning, and what data is going into and coming out of AI Another powerful tool in the DCU’s arsenal is its
insecure extensions. Per findings from our report, systems, and discover risks and vulnerabilities in AI domain impersonation monitoring system. By using
Secure Employee Access in the Age of AI, 57% apps, agents, and models. AI to detect and track impersonation (or homoglyph)
of organizations have experienced an increase in domains, the DCU can anticipate and block phishing
security incidents linked to AI usage.17 Yet despite Protect campaigns and other malicious activity that rely on
growing awareness of the need for AI controls, Safeguard sensitive data and AI systems. these deceptive URLs.
many organizations may have yet to implement any.
This includes preventing data, defending against
AI also plays a critical role in investigations. The DCU
This creates a gap between adoption and protection
prompt injection attacks, and securing AI apps
uses AI-powered agents to sift through massive
in the enterprise.
and agents.
datasets, extract key indicators of compromise
As generative AI apps and agents become deeply (IOCs), and share them across Microsoft’s security
embedded in business workflows, security teams Govern ecosystem. A reverse engineering plugin powered by
need end-to-end visibility and control. A strong Enforce policies and oversight for AI use. AI further accelerates the analysis of malicious code,
security framework helps organizations: prepare for Retain and audit AI interactions, ensure automating tasks that once took hours or days.
AI adoption; discover how AI is being used within compliance with evolving regulations, and set
the organization; protect sensitive data, AI agents, clear guidelines for AI behavior.
applications, and models; and govern AI operations
with clear policies and safeguards for compliance and
new AI regulations.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 64
Countering nation-state and emerging threats
Disrupting cybercrime ecosystems:
Heat map detailing the global spread of Lumma stealer
Lessons from the Lumma Stealer
takedown
Given Lumma Stealer’s prominence in the
infostealer ecosystem and its role in enabling
broader cybercriminal operations, it became a
high-priority target for disruption this year. In May
2025, the DCU, in collaboration with global law
enforcement and cybersecurity partners, successfully
disrupted the Lumma Stealer infrastructure in a joint
operation exemplifying the power of public-private
collaboration in proactive cyber defense.
Through a US court order and coordinated actions
with the US Department of Justice, Europol, Japan’s
Cybercrime Control Center (JC3), and private sector
partners like ESET, Bitsight, Lumen, CleanDNS, and
GMO Registry, over 2,300 malicious domains were
seized or blocked. These domains formed Lumma
Stealer’s infrastructure backbone.
Red signifies a higher number of
infections and encounters while
blue represents lower.
Source: Lumma pre-disruption data,
Microsoft Digital Crimes Unit

Countering nation-state and emerging threats continued
Worldwide
10000
2024
8000
6000
4000
2000
0
April–June July–Sept Oct–Dec Jan–March April–June July–Sept Oct–Dec Jan–March April–June
2023 2023 2023 2024 2024 2024 2024 2025 2025
stneve
noitceted
2C
Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 65
The disruption not only severed communication Beginning in March 2025 and continuing through
Innovative disruption at scale
between infected devices and Lumma Stealer’s July, DCU telemetry detected a rise in cracked Cobalt
Statutory Automated Disruption program global impact
command centers, but also redirected domain traffic Strike C2 infrastructure, with a pronounced spike in
to Microsoft-controlled sinkholes. This provided China. This pattern aligns with recent cybersecurity
the DCU with enhanced threat intelligence, which it reports of coordinated malware campaigns
monitors, enriches, and shares with external partners 2023 2025 originating from China that leverage cracked
through the Cyber Threat Intelligence Program (CTIP). instances of Cobalt Strike. This activity underscores
The operation highlights how coordinated legal, the importance of persistent, scalable, and cross-
technical, and operational strategies across sectors jurisdictional takedowns of malicious infrastructure.
can significantly disrupt cybercriminal ecosystems Further, Microsoft’s collaboration with Fortra— the
and protect critical infrastructure. cybersecurity software company behind Cobalt
Strike—is central to this effort, as Fortra regularly
These disruption actions were not one-time events,
provides DCU with updated signatures that enhance
but part of a sustained strategy to limit threat
detection systems protecting against emerging C2
actors’ ability to rebuild. By employing innovative
infrastructure. DCU and Fortra continue to add new
techniques—such as court-appointed monitors
sources of intelligence to support the effort.
and DCU’s Statutory Automated Disruption (SAD)
program—the DCU continues to identify and
dismantle new Lumma Stealer infrastructure. Learn more
Although the medium term effect of this operation
has yet to play out, the potential impact of our Disrupting Lumma Stealer: Microsoft leads global
proactive approach to degrading malicious action against favored cybercrime tool | Microsoft
infrastructure is demonstrated by the DCU’s 2023 On the Issues
disruption of cracked Cobalt Strike, a tool widely
Inside Microsoft’s Global Operation to Disrupt
used in ransomware attacks, including those
Lumma Stealer’s 2,300-Domain Malware Network
targeting hospitals.
| The Microsoft Threat Intelligence Podcast
After the initial domain seizures, the DCU issued
Lumma Stealer: Breaking down the delivery
over 238K abuse and takedown notices to hosting
techniques and capabilities of a prolific infostealer
providers globally, resulting in a 68% reduction in
| Microsoft Security Blog
the average number of command and control (C2)
servers and shrinking their average lifespan from 49
days to just 18 days.
Source: DCU Crawler data

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 66
Countering nation-state and emerging threats continued
Deterrence in action: Building • The US administration has issued strong • Prohibit retaliatory cyber operations.
consequences for nation-state actors public statements and indictments tied to cyber Private companies are not in the position to
operations and has publicly attributed cyberattacks independently hack back against malicious nation-
As infrastructure essential to daily life—including
in coordination with allies and partners. state actors, and doing so can risk unintended
water, food, healthcare, communications, and
• The EU is increasingly leveraging its Cyber escalation and harm. While industry can support
transportation systems—becomes increasingly
Diplomacy Toolbox and sanctions regime to hold attributions and partner with government to take
dependent on digital technology, nation-state
bad actors accountable, though implementation action, imposing consequences for internationally
cyber operations targeting these systems cannot
remains uneven. wrongful behavior by states will always need to be
be permissible; in particular those prepositioning
led by governments.
for disruptive or destructive cyberattacks in case of Looking ahead, these are important foundations to
future conflicts. build upon. To further strengthen a cyber deterrence A viable model for cyber deterrence is a necessity
framework, like-minded governments should work to: for the stability of the online world and will require
Defensive actions alone to protect critical
innovations in statecraft and diplomacy in the years
infrastructure are unlikely to deter nation-state threat • Regularize public attributions. States should
ahead. This is why Microsoft is supporting ongoing
adversaries. These are politically motivated activities more consistently issue public attribution
research by the Royal United Services Institute (RUSI)
that must be addressed with political solutions statements, leveraging insights from other
to explore novel approaches to deterring malicious
as well. To protect critical infrastructure, political governments and partners in the private sector
activity online.
institutions, and civilian systems, governments and establishing a more uniform process for doing
must build frameworks that signal credible and so. Such statements should always indicate if
proportionate consequences for malicious activity international laws or norms were violated during a
that violate international rules. cyber incident.
• Signal red lines. States should make clear they
Over the past year, there has been a marked increase
will impose increasingly severe consequences
in recognition of the need for such cyber deterrence,
in response to a spectrum of malicious nation-
with governments and industry aligning more closely
state cyber activity, ranging from espionage to
to response to malicious activity. For example:
prepositioning to disruptive and or destructive
• NATO has advanced coalition-based attribution cyber operations.
frameworks and is exploring collective • Impose diverse consequences. Responses to
countermeasures in response to cyberattacks. nation-state cyberattacks should not be constrained
In July, the alliance released a statement to the cyber domain or prescribed in a one-size-
recognizing and condemning malicious cyber fits-all model. Different threat actors will be deterred
activities attributed to Russia by member states. by different consequences. These could include
economic measures, diplomatic sanctions, naming
and shaming, posturing, or targeted declassification.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 67
Countering nation-state and emerging threats continued
Addressing the geopolitical enablers As a result, addressing ransomware operations Combating cyber mercenaries: which seeks to regulate Commercial Cyber Intrusion
of ransomware operations requires a more coordinated international effort Closing the gaps in global regulation Capabilities (CCIC) with shared frameworks. In April
and political pressure that holds governments 2025, the Pall Mall Process produced a first-of-its-
Many of the most prolific ransomware groups Cyber mercenaries, private firms that sell offensive
accountable for both direct and indirect support of kind Code of Practice for governments to follow in
avoid consequences by targeting victims in other cyber capabilities, operate in legal gray zones, often
ransomware attacks. Designating state sponsors of order to limit harmful impacts of CCICs.20
countries while their own governments turn a blind across borders. Their cross-jurisdictional nature and
ransomware, for example, similar to state sponsors
eye. Whether they are state-affiliated groups or their a lack of oversight make them difficult to trace or Transparency is key. Governments should expose
of terror, with associated stigmas and penalties, is
government simply ignores their activity, the result prosecute, allowing them to act with near impunity. vendors and intermediaries, enforce sanctions, and
one way to incentivize states to confront ransomware
is the existence of “safe haven” states that enable Many also rebrand frequently, shift operations across lead by example by refraining from using cyber
groups operating within their borders.
ransomware attacks abroad and violate international jurisdictions, and use complex financial networks to mercenaries themselves. Meanwhile, industry must
norms of due diligence which oblige governments Other approaches to address escalating further evade detection and regulation. enhance platform security, monitor abuse, and
to take action to prevent illegal cyber activity within ransomware include: act swiftly to disrupt cyber mercenary operations.
To counter this growing threat, governments
their borders. Through due diligence and collaboration, both
• Legal action: Ransomware is a form of extortion and industry must collaborate further to disrupt
sectors can help shrink the space in which cyber
which, in most cases, violates existing laws. the enabling market through intelligence
mercenaries operate—protecting national security,
These should be applied whenever possible. sharing, coordinated responses, and regulation.
human rights, and global digital stability.
By designating state sponsors of ransomware, International norms should also prohibit the use of
civilians might be able to take further legal action cyber mercenaries and close legal loopholes that
against those governments following ransomware allow them to persist. Governments need to put in Learn more
attacks to seek damages in civil courts. place severe limitations—or outright bans—on the
• Public-private partnerships: Encourage industry cyber mercenary market to ensure their products, Protecting users and reaffirming our
partnerships with law enforcement to improve including spyware, cannot be used in violation of commitment to combatting cyber mercenaries |
cooperation against cybercrime. Examples include domestic or international law, human rights, or to Microsoft On the Issues
the International Counter Ransomware Initiative significantly undermine product security.
Protecting the public from abusive
(CRI)18 and the Institute for Security and Technology
Examples already exist of states taking effective AI-generated content across the EU |
(IST) Ransomware Task Force.19
action. The US has placed restrictions on when EU Policy Blog (March 2025)
• Deterrent consequences: Governments should set
federal agencies can solicit the services of cyber
clear expectations around what is responsible state
mercenaries and banned firms that operate
behavior, reinforced by escalating consequences
irresponsibly, meaningfully impacting the bottom
across domains sufficient to deter state-sponsored,
lines of some cyber mercenary firms. Meanwhile,
or enabled, ransomware attacks.
the UK and France have made strides over the past
year in their stewardship of the Pall Mall Process,
an international multistakeholder dialogue that
includes more than 20 government participants and

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  68
Countering nation-state and emerging threats continued
| Intelligent signals: Accelerating   | Organizations can enhance both proactive and   |     |     |     |     |     |     |
| ----------------------------------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
incident response and recovery   reactive detection and response efforts by integrating   Intelligent signals in action
Incident response approach to rapid investigation and recovery
a variety of threat intelligence artifacts holistically.
Threat-informed defense strategies
Understanding the threat landscape, your own
aren’t just for large organizations; all
environment, and how high-quality threat intelligence
organizations can implement threat- Investigation   Triage of anomalous  Threat hunt direction  Intelligence from
can enhance detection and response includes:
|                     |     |             |     | behaviors and  | heavily influenced by  |     | real-world incidents  |
| ------------------- | --- | ----------- | --- | -------------- | ---------------------- | --- | --------------------- |
| informed defense.   |     | workstream  |     |                |                        |     |                       |
|                     |     |             |     | indicators of  | threat actor profiles  |     | lead to improved      |
•  Leveraging diversity in artifacts. Threat intelligence
|                                                  |                                             |     |     | compromise, initial  | (if attributed), attack  |     | detections,      |
| ------------------------------------------------ | ------------------------------------------- | --- | --- | -------------------- | ------------------------ | --- | ---------------- |
| Understanding the threat landscape and curating  | comes in many forms. Atomic indicators of   |     |     |                      |                          |     |                  |
|                                                  |                                             |     |     | hypothesis formed    | campaigns, TTPs,         |     | automation, and  |
relevant operational processes can be a great   compromise and detection signatures should be   the threat landscape,  further protection
start for small organizations to enhance their   paired with research into threat actor behavior.   industry, and  of organizations
victim organization
| security lifecycle. For example, start with the basics:   | Threat hunters can’t only rely on indicator-based   |     |     |     |     |     |     |
| --------------------------------------------------------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
understand the organization’s attack surface and
hunting. Instead, they should have a broad
| most applicable threats first, then build from there.   | understanding of threat actor motivations and TTPs.  |     |     |     |     |     |     |
| ------------------------------------------------------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
•  Being industry and geographically threat
The Microsoft Detection and Response Team (DART),
aware.  Research and build a threat profile for
leverages intelligent signals throughout an entire
the organization, such as its industry position,
investigation to make calculated decisions based
DART
| on the motivations and techniques of threat actor   | geographical location, and size. Use these data   |     |                      |                 |     |                |                    |
| --------------------------------------------------- | ------------------------------------------------- | --- | -------------------- | --------------- | --- | -------------- | ------------------ |
|                                                     |                                                   |     | Suspicious activity  | Investigation   |     | Attack story   | Tactical takeback  |
points to influence security roadmaps and prioritize   detected by customer  and tactical  systematically   complete and
campaigns, intercepting and disrupting threat actor
|     |     |     | & Microsoft  | takeback begins  |     | documented  | threat actor  |
| --- | --- | --- | ------------ | ---------------- | --- | ----------- | ------------- |
implementation of security controls that directly
activity in hours, not days.   IR engaged  in parallel  evicted, strategic
mitigate prevalent threats.
hardening begins
Applying diverse threat intelligence artifacts across
•  Knowing what to protect and where. Document the
multiple workstreams and stages of detection and
organization’s internal security posture and relative
| response heavily influences the direction of threat   | attack surface. Highlight assets of value, those   | Recovery    |     |     |     |     |     |
| ----------------------------------------------------- | -------------------------------------------------- | ----------- | --- | --- | --- | --- | --- |
hunting, tactical takeback efforts, remediation   Recovery approach  Remediation  Hardening strategies
|     | with trust dependencies and privileged pathways.   | workstream  |     |                      |                    |     |                       |
| --- | -------------------------------------------------- | ----------- | --- | -------------------- | ------------------ | --- | --------------------- |
|     |                                                    |             |     | determined based on  | playbook enhanced  |     | catered to immediate  |
activities, and improved detection. Most importantly,
Define a baseline of regular operation to rapidly   initial hypothesis  by rapid blast  and future threats
this approach builds context-aware, tailored
highlight abnormalities should they arise.  radius  identification  common to
recommendations  that  can  influence  organizations’   and attack  organizational
|     |     |     |     |     | surface prioritization  |     | profile  developed  |
| --- | --- | --- | --- | --- | ----------------------- | --- | ------------------- |
strategic security roadmaps and build towards a
more secure future.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 69
Countering nation-state and emerging threats continued
While creating a dedicated threat detection Collaboration as a counter measure: While approaches vary, these developments reflect a
“
and intelligence function is valuable, it can be Breaking down fraud silos growing recognition of the need for more proactive,
costly. Nevertheless, security must be seen coordinated, and enforceable national responses
Cyber fraud is growing more scalable and sophisticated,
as an investment. Cybersecurity risks are Security must be seen to fraud. Looking ahead, we anticipate a significant
outpacing traditional defenses. A key vulnerability
business continuity risks. Building useful threat acceleration in the implementation of these
as an investment.
is the lack of robust, real-time data-sharing across
intelligence artifacts is a cyclical, collaborative legislative frameworks as governments seek to close
Cybersecurity sectors. Fragmented systems and siloed insights
effort. Knowledge sharing and partnerships are the regulatory gaps, enhance consumer protections,
hinder early detection and coordinated response.
of paramount importance. Incident responders risks are business and build a more resilient digital economy.
One of the most effective countermeasures
have a unique viewpoint of an organization’s
continuity risks. is structured collaboration between financial
data—contextual artifacts can be continuously
institutions, technology platforms, regulators, and Learn more
reported back into overall research efforts cyclically.
law enforcement. Sharing fraud signals enables faster
This informs threat hunting, improves detections,
disruption of criminal activity—but it requires more Cross-border collaboration: International
and maintains cross-team awareness of the threat
than isolated partnerships. A unified approach that law enforcement and Microsoft dismantle
landscape. Extending collaboration with external
integrates diverse data sources is essential to expose transnational scam network targeting older
partnerships also builds a stronger, collective defense
abuse patterns and reduce harm. adults | Microsoft On the Issues
against threats.
(June 2025)
Global efforts are gaining momentum. Initiatives like
the Global Signal Exchange21 promote standardized, Disrupting Lumma Stealer: Microsoft
privacy-conscious frameworks for multi-sector leads global action against favored
cooperation. Governments are responding to the cybercrime tool | Microsoft On the Issues
trillions of USD lost to scams with legislation mandating (May 2025)
reporting, liability reform, and stronger public-private
collaboration.22 Australia’s Scam Prevention Framework
Act 2025, for example, introduces sector-specific codes
for fraud prevention.23 The UK’s national strategy,
meanwhile, expands accountability to tech and telecom
sectors and accelerates data-sharing mandates.24
Singapore and Japan are tightening laws to counter
digital payment fraud and cross-border scams.25

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 70
Policy, capacity, and future readiness
Securing the digital frontier: Governments play a pivotal role in fostering As AI is increasingly integrated into national security,
Government’s role in responsible experimentation and mission-driven innovation in the intelligence, and defense operations, its deployment
use of AI in national security and use of AI for cyber defense through public-private must be governed by clear legal framework, such
cyber defense partnerships. The United Kingdom’s Laboratory as NATO’s Principles of Responsible Use and
for AI Security Research (LASR),26 announced in the US Department of Defense’s Responsible AI
As we’ve seen throughout this report, AI gives cyber
November 2024, is an example of one such initiative Framework. Multilateral dialogue and engagements
defenders a significant boost in meeting security
bringing together critical government agencies with with stakeholder groups from industry, academia,
challenges. To fully realize these benefits, especially
academic and other multistakeholder partners to and civil society are essential to promote
in national security contexts, the use of AI must be
advance AI benefits for national cyber resilience. responsible innovation that enhances rather than
guided by robust policy frameworks that allow for a
Microsoft welcomes the recent White House AI endangers global stability. Governments should
sustained commitment to trusted, secure innovation.
Action Plan and the Administration’s commitment set clear expectations for acceptable AI use in
For governments, this includes establishing strong to appropriately balance the dissemination of AI national security, grounded in the United Nations
procurement and security protocols to ensure AI technologies, for example to improve defense (UN) Charter, international humanitarian law
systems are securely designed, developed, deployed, of critical infrastructure, with national security (IHL), and international human rights law (IHRL).
and used, especially when handling sensitive or considerations for Frontier AI. And we continue to Increased international coordination will be needed
classified data. By supporting research, training, and partner closely with the US government to effectively to enforce existing norms and develop new ones that
commercialization—particularly for startups and address security risks to US AI companies, talent, reflect the capabilities and risks of AI, especially as
subject matter experts developing cutting-edge AI intellectual property, and systems. autonomous, agentic systems advance.
and cybersecurity solutions—governments can also
use security as a lever for economic growth.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 71
Policy, capacity, and future readiness continued
Implementing responsible AI in national To stay ahead of evolving regulations such as
security the EU AI Act, Microsoft has taken a layered Learn more
At Microsoft, we expanded our responsible AI tools to approach to compliance, in line with the AI Act’s
better assess and manage adversarial risks in model staggered compliance deadlines. Microsoft has Responsible AI Transparency Report | Microsoft
development and deployment. Microsoft launched undertaken multiple initiatives to promote AI
Securing AI and Cloud with the Zero Day Quest | MSRC Blog | Microsoft Security
our Frontier Governance Framework,27 which serves literacy in accordance with the Act, empowering our
Response Center
as a monitoring function, tracking the emergence of employees, customers, and others to responsibly
new and advanced AI model capabilities that could leverage AI technologies.28 Microsoft also proactively Microsoft commits to skilling one million people for digital skills through Artificial
be misused to threaten national security or pose at- took a layered approach to prepare for compliance Intelligence skilling initiative in South Africa - Source EMEA
scale public safety risks. It also sets out a process for with the Act’s prohibited practices provisions.29 Unlocking data to advance European commerce and culture | Microsoft On the Issues
assessing and mitigating these risks so that frontier AI In July 2025, we signed the General-Purpose AI (July 2025)
models can be deployed in a secure and trustworthy (GPAI) Code of Practice, which includes a set of
Microsoft announces AI skilling opportunities for 2.5 million people in the ASEAN region
way. We are also developing engineering guidance guidelines for compliance with the AI Act’s GPAI
by 2025 | Microsoft Stories Asia
and responsible AI policies to support emerging model provider obligations, which came into effect
agentic systems, as these will play a growing role in in August 2025.30 Microsoft continues to engage Microsoft Elevate: Putting people first | Microsoft On the Issues (July 2025)
AI development and deployment. with the central EU regulator, the AI Office, and other
Unlocking AI’s global potential: progress, productivity, and workforce development |
relevant authorities in EU Member States to share
Microsoft maintains a consistent risk review process Microsoft On the Issues (April 2025)
insights from our AI development, governance, and
across AI releases, including red teaming and pre-
compliance experience, as well as insights we hear Microsoft announces ARC Initiative to strengthen cybersecurity in Kenya | Microsoft On
deployment assessments for high-impact systems.
from our customers. the Issues (May 2025)
This includes all generative AI systems and models,
including Azure OpenAI and Phi family of models to Microsoft also worked with global partners to The Accra Call for Cyber Resilient Development | GC3B
help product teams safely deploy their generative support more consistent governance approaches
Home - The GFCE
AI applications and models. Microsoft’s Sensitive aligned with technical standards, including working
Uses and Emerging Technologies team continues to closely with industry partners in the Frontier Model microsoft/llmail-inject-challenge · Datasets at Hugging Face
advise on high-risk AI and high-impact applications— Forum and the Coalition for Secure AI.
especially in healthcare and science—helping teams
navigate novel risks and shape internal guidance.
To streamline documentation, we introduced an
internal tool that brings together all responsible AI
requirements outlined in the Responsible AI Standard.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 72
Policy, capacity, and future readiness continued
Resilience by design: Strengthening Leaders should shift from a purely defensive posture
Key recommendations for leaders
critical infrastructure for the next to one that embraces resilience as a core design
wave of threats principle. This means building systems that can
continue to operate under duress, recover quickly, Invest in resilience by design
In today’s hyper-connected world, new
and evolve to meet future threats. For leaders, this Encourage the development of infrastructure that is inherently resilient. This includes
vulnerabilities are constantly emerging.
is not just a technical issue—it’s a strategic one. modular systems, redundancy, and fail-safes that allow for graceful degradation and
As a result, cybersecurity expectations, The resilience of our infrastructure directly impacts rapid recovery.
practices, and oversight must evolve to national security, economic stability, and public trust.
Foster public-private collaboration
prioritize resilience.
By embedding resilience into the DNA of an Resilience is a shared responsibility. Governments and industries must work together to
Cyber–physical threats can arise from a variety organization’s infrastructure, we not only protect our set standards, share threat intelligence, and coordinate responses to disruptions.
of sources, including natural disasters, industrial assets but also enhance our ability to compete and
accidents, human error, technical errors, or malicious thrive in a volatile world. Support innovation and workforce development
activities such as cyberattacks, terrorism, or armed Resilience requires cutting-edge technologies and a skilled workforce. Leaders should
Cyber-physical resilience is not just a technical
conflict. These threats have the potential to disrupt champion investments in research and development and education to build
challenge, it’s a leadership imperative.32 CEOs and
the business and operations of critical infrastructures. national capacity.
CFOs must recognize that downtime, data loss, and
Given the interconnected nature of these risks, reputational damage from cyber incidents can have Incentivize resilience through policy and regulation
cyber–physical resilience encompasses both technical profound financial consequences. Simultaneously, Financial and regulatory frameworks should reward organizations that prioritize
and organizational measures. Its goal is to prevent, government leaders must ensure that national resilience, much like how safety and environmental standards are incentivized today.
protect against, respond to, resist, mitigate, absorb, infrastructure can withstand and recover from attacks
Measure and monitor resilience
accommodate, and recover from incidents.31 that could otherwise disrupt societal functions
Establish clear metrics and benchmarks to assess the resilience of critical systems.
at scale. Maintaining a robust defensive posture
Cyberattacks are inevitable. Whether due to Transparency and accountability are essential for continuous improvement.
will be especially important for owners of critical
sophisticated threat actors, human error, or system
infrastructure, many of whom operate with limited
complexity, breaches will occur. The key question is
financial resources.
therefore not if a system will be attacked, but how
well it can withstand attacks and recover. This is the By embedding resilience into the DNA of an
essence of cyber-physical resilience: the ability of organization’s infrastructure, we not only protect our
systems to anticipate, withstand, recover from, and assets but also enhance our ability to compete and
adapt to disruptions—regardless of the cause. thrive in a volatile world.

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  73
Policy, capacity, and future readiness continued
Building resilience in critical infrastructure
Enable
A strategic lifecycle, four core phases…
Stakeholders
Sectors
| Anticipate                  | Withstand             |     |     |     |     |     |     |     |     |     |
| --------------------------- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Identify vulnerabilities    | Design systems with   |     |     |     |     |     |     |     |     |     |
dapt
| and emerging threats  | built-in redundancies  |     |     |     |     |     | A   |     |     |     |
| --------------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                       |                        |     |     |     | A   |     |     | n   |     |     |
t
i
| Conduct risk assessments  | Harden infrastructure    |     |     |     |     |     |     | c   |     |     |
| ------------------------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
|     | against known threats  |     |     |     |     |     |     | p   |     |     |
| --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Model potential disruptions
a
|     |                        |     |     |     |  Building   |     |     | t   |     |     |
| --- | ---------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
|     | Ensure continuity of   |     |     |     |             |     |     |     | e   |     |
R
|          | essential functions  |     |     | e   | Resilience  |        |     |     |       |     |
| -------- | -------------------- | --- | --- | --- | ----------- | ------ | --- | --- | ----- | --- |
|          |                      |     |     | E   |             |        |     |     |       | e   |
|          |                      |     |     | n c |             |        |     |     |       | c   |
|          |                      |     |     | e o |             |        |     |     |       | n   |
|          |                      |     |     | r v |             |        |     |     |       |     |
|          |                      |     |     | g   |             |        |     |     | a     |     |
|          |                      |     |     |     | e           |        |     | d   | n     |     |
|          |                      |     |     | y   | r           |        |     | n   | Fi    |     |
|          |                      |     |     |     |             |        |     | a   |       |     |
|          |                      |     |     | W   |             | Withst |     |     | e     |     |
| Recover  | Adapt                |     |     | a t |             |        |     |     | c a r |     |
 e
|     |     |     |     |  r  |     |     |     |     | h   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |   T |     |     |     | alt |     |     |
R a p id   r e s p o n s e   an d    L e a r n   f ro m  i n c id ents    ransportation   He
|     |     |     |     | G   |     |     |     |     |     | s   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
re s to r a t i o n  p r o t o co l s  a n d   n e a r- m i ss e s   o e
|     |     |     |     | v     |     |     |     |     | ti  |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     | P   |     |  e rn |     |     |     |     | n i | s   |
|     |     | o   |     |       |     |     |     |     | u   | p   |
M i n i m i z e   d o w n t i m e  a n d    U p d a t e   s y s t e m s      lic m m hi
|     |     |     |     | e n |     |     |     | o   | m   | s   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s e r v i c e   d i s r u p t i o n   a n d   p o l i c i e s   y t   P C r
|     |     |     |     |     | ri  | v a t | c to | r    |     | e     |
| --- | --- | --- | --- | --- | --- | ----- | ---- | ---- | --- | ----- |
|     |     |     | In  |     |     | e     | S e  |      |     | art n |
|     |     |     |     | v e |     |       |      |      |     |       |
C o m m u n i c a t e   t r a n s p a re n tly   I n v e s t   i n   i n n o v a t io n  and   s P
|     |     |     |     | t m |     |     |     |     | te   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
|     |     |     |     | e n |     |     |     |     | a    |     |
w i t h   s t a k e h o ld e r s   w o r k f o r c e  t r a in i n g   t  P riv
|     |     |     |     |     | I n n o |             |          | ic - |     |     |
| --- | --- | --- | --- | --- | ------- | ----------- | -------- | ---- | --- | --- |
|     |     |     |     |     |         | v a t i o n |    P u b | l    |     |     |

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 74
Policy, capacity, and future readiness continued
Microsoft’s strategic Quantum computing is novel that can consider many Every organization should inventory its Governments and industries worldwide are actively
path to quantum safety possibilities at once, allowing quantum computers cryptography (keys, certificates, and protocols) preparing for the quantum era by upgrading their
to process complex problems much faster than and establish a roadmap to replace vulnerable cryptographic algorithms to quantum-resistant
Much of modern cryptography relies on
classical systems. algorithms with Post-Quantum Cryptography (PQC) alternatives. Standards bodies like National Institute
mathematical puzzles that are practically
standards as they become available. At Microsoft, of Standards and Technology (NIST) and International
Quantum computing poses a serious threat to
impossible for classical computers
there is a dedicated program to make sure our Organization for Standardization (ISO) have been
current cryptographic systems. While still an
to solve—for instance, cracking the
own products and services—and customers—stay running global competitions to select robust PQC
emerging technology, the expected development
standard encryption behind a secure safe in the quantum era. Microsoft established the algorithms, and international groups are working
of a powerful cryptographically relevant quantum
website or messaging app would take Quantum Safe Program (QSP) to coordinate all its on standards to integrate these algorithms into
computer (CRQC) means that if organizations don’t
millions of years with today’s computers. quantum security efforts across the company and our software so that everyone’s systems can work
update our cryptography in time, we risk a scenario
achieve quantum readiness by gradually integrating together. In everyday terms, it’s like the world has
like the early days of the internet, when websites
PQC algorithms into Microsoft’s services. As part of agreed to upgrade all its locks and keys and is now in
were on unencrypted HTTP and attackers could
our efforts: the process of implementing the change.
eavesdrop on information in transit. In the lead up to
this potential data exposure, Harvest Now, Decrypt • We updated SymCrypt, Microsoft’s core During the last year, multiple governments have also
Later (HNDL) is a real concern: attackers can hoard cryptographic library, to support new post- published guidance and requirements to spur the
encrypted data today so they can decrypt it in the quantum algorithms. SymCrypt is like the engine transition, with most identifying 2035 as the deadline
future with quantum power. that handles encryption under the hood in for completing transition. In the United States,
Windows, Azure, and many Microsoft products. European Union, and Australia, changes to some of
We also enabled PQC support in Windows and the highest risk systems should be made by 2030,
Azure Linux (using SymCrypt OpenSSL). while in Canada and the UK, that date is 2031.
• Microsoft Research has contributed to the design
and analysis of PQC algorithms. Through blogs and
publications, Microsoft shares these developments
with the community, helping to lead the
conversation on how to protect information in the
quantum age.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 75
Policy, capacity, and future readiness continued
Recommendations
Learn more
Governments play a critical role in enabling a quantum-safe future through strong collaboration
with industry and effective policies. To accelerate readiness, we recommend governments take the Post-quantum resilience: building secure
following actions: foundations | Microsoft On the Issues
Quantum-safe security: Progress towards
Establish quantum safety as a national cybersecurity priority. Position quantum-safe cryptography as a
next-generation cryptographyQ uantum-
strategic imperative and embed it into national cybersecurity frameworks.
safe security: Progress towards next-
Align quantum-safe strategies across jurisdictions. Harmonize public policies, standards, and transition generation cryptographyQ uantum-safe
timelines. The G7 should lead by expanding its financial sector post-quantum cryptography workstream to security: Progress towards next-
align G7 members’ broader quantum-safe strategies. generation cryptographyQ uantum-safe security:
Progress towards next-generation cryptography
Adopt international standards. Support global standards development and avoid fragmented, region-
specific approaches that hinder interoperability, innovation, and security. https://quantum.microsoft.com
Set early and progressive timelines. Drive action well before 2030. For instance, the US Committee on
National Security Systems Policy 15 (CNSSP - 15) mandates quantum-safe algorithms in all new products
and services for national security systems by January 2027.
Lead by example with transparent transition plans. Publish and regularly update government transition
roadmaps—including timelines, milestones, and budgets—to foster knowledge sharing and best practices.
Raise awareness and build workforce capacity. Educate the public and critical infrastructure sectors
on quantum risks and readiness. Invest in skilling programs to equip the workforce for a quantum-
safe transition.
Modernize through cloud adoption Promote cloud migration as a strategic enabler. Cloud platforms
can streamline the transition by embedding quantum-safe capabilities, reducing the burden on
individual organizations.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 76
Strategic vision and global commitments
Secure Future Initiative: We continue to deliver product innovations that
“
Progress and priorities translate our internal learnings into customer value, Learn more
across Microsoft Azure, Microsoft 365, Windows,
Microsoft’s Secure Future Initiative (SFI) is our multi-
Transparency and clarity and our security portfolio, including Microsoft
year effort to revolutionize how we design, build, test,
Entra, Defender, and Purview. For instance, Azure’s
remain central to our mission,
and operate our products and services to achieve
integrated Hardware Security Modules (HSMs), Secure Future
the highest security standards. Released in April and through regular reports Initiative (SFI)
Microsoft 365’s Copilot Control System (CCS), and the
2025, the third edition of our public progress report Security above all else.
and additional guidance, widespread deployment of phishing-resistant MFA
continued our tradition of transparency, articulating
reflect our commitment to protecting customers. April 2025 progress report
improvements to Microsoft’s internal security posture we aim to share our learnings
Grounded in our core principles of Secure by Design,
and sharing innovations that help better protect to collectively move our Secure by Default, and Secure Operations, this work Secure Future Initiative | Microsoft Trust Center
customers by design and by default.
ecosystem toward a safer future. reinforces our mission to strengthen security across SFI April 2025 Progress Report
As we highlight in our report, we continue to foster Microsoft and empower customers with solutions
SFI Customer Guidance: Patterns and Practices |
a robust internal security culture. Every Microsoft that are more secure out of the box.
Microsoft Security Blog
employee now has a Security Core Priority within
Our intent in reporting on SFI is not only to share
their performance objectives, fostering personal At the engineering level, progress has been made
progress, but also to offer clear and actionable
accountability and a stronger security mindset. across our twenty-eight aligned objectives covering
guidance through patterns and practices to
To strengthen governance, we’ve established a six engineering pillars, protecting identities, secrets,
customers, partners, and the broader ecosystem.
regulatory governance council of Deputy Chief tenants, and networks, isolating production systems,
Transparency and clarity remain central to
Information Security Officers (dCISO) embedded securing engineering systems, monitoring and
our mission, and through regular reports and
across critical product and business areas, driving risk detecting threats, and accelerating response and
additional guidance, we aim to share our learnings
management alignment, accountability, and resilience remediation. While there will always be more work
to collectively move our ecosystem toward a
at scale. to do, we have made meaningful progress across all
safer future.
areas. This structured approach aligns closely to Zero
Trust architecture, enabling consistent, risk-based
prioritization and continuous improvement.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 77
Strategic vision and global commitments continued
Microsoft’s commitment to These efforts reflect Microsoft’s belief that collective As a global company, Microsoft sees firsthand Microsoft urges governments to prioritize regulatory
strengthening global cybersecurity security is only possible through trusted partnerships how inconsistent cybersecurity regulations harmonization and supports the Organisation for
and shared responsibility. across jurisdictions can hinder resilience. That is Economic Co-operation and Development (OECD)
Microsoft is deeply committed to supporting the
why efforts to establish international regulatory as a key convener in this effort. The organization’s
global effort to counter cyber threats by fostering Global trends: Cybersecurity policies and laws
cooperation, such as the effort led by Germany and multilateral structure and digital security expertise
strong partnerships with governments and As governments accelerate efforts to manage cyber
South Korea, are important. To truly strengthen make it well-positioned to:
advocating for cybersecurity laws and regulations risk through new laws and policies, two key trends
global cybersecurity, governments must pursue
that promote a safer digital ecosystem for all. have emerged: • Develop principles for regulatory alignment.
harmonized, risk-based approaches that promote
• Establish a forum for regulators and experts
A regional focus: Europe’s cybersecurity • Regulatory expansion and enforcement interoperability and reduce duplication.
representing various jurisdictions across the
imperative Governments are shifting from voluntary
Key opportunities for regulatory alignment include: multistakeholder cybersecurity community.
The EU has enacted the Cyber Resilience Act (CRA), guidelines to enforceable standards, emphasizing
• Commission research to map overlaps and gaps in
a landmark regulation poised to become the gold accountability, risk management, and timely • Incident reporting: Standardizing timelines,
global cybersecurity policy.
standard for cybersecurity, much like the General incident reporting. definitions, thresholds, and formats to enable
Data Protection Regulation (GDPR) did for data • Securing the digital supply chain faster, coordinated responses. Earlier this year, Microsoft joined dozens of
privacy. The CRA is expected to elevate global New mandates are driving secure by design • Emerging technologies: Aligning approaches technology leaders in signing an open letter
security standards, influencing how secure products principles, transparency through clearer support to AI and post-quantum cryptography to avoid to the Group of Seven (G7) and OECD, calling
are built even beyond Europe’s borders. lifecycles and forward leaning efforts such as innovation silos. for coordinated action to reduce cyber risk and
encouraging the generation of SBOMs, and • Supply chains and vulnerability management: foster innovation.
But regulation alone isn’t enough. Protecting Europe’s
robust post-market monitoring. Encouraging technology suppliers to inventory
digital infrastructure requires deep collaboration
their supply chain dependencies and strengthen
between governments and industry. Microsoft is While regulatory expansion and enforcement and Learn more
practices of coordinated vulnerability disclosure
actively contributing to this shared mission by: efforts to secure the digital supply chain are well
to improve the identification, communication, and
intended, they can also introduce complexity. Microsoft launches new European Security
• Appointing a European dCISO to its cybersecurity remediation of vulnerabilities across the supply
Fragmented regulatory frameworks can slow down Program | Microsoft On the Issues
governance council. chain promptly.
incident response and ultimately weaken defenses.
• Launching a European Security Program to provide EU Data Resiliency | Microsoft Trust Center
EU governments with real-time threat intelligence
The CyberPeace Institute is helping NGOs defend
and response capabilities.
themselves—before it’s too late (August 2025)
• Contributing guidance to help manufacturers
comply with the CRA—including the development
of harmonized standards by European Standards
Organizations and EU Commission guidance
and supporting legislation through the CRA
Expert Group.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 78
Closing
As global regulatory frameworks evolve and legislative trends
reshape the cybersecurity landscape, one truth remains constant:
security is a shared responsibility.
Governments, industry leaders, civil society, and individual users each
play a vital role in shaping a resilient digital ecosystem. The insights
and data presented throughout this report underscore the urgency of
collaboration—not only across borders but across sectors and disciplines.
Our commitment to lighting the path to a secure future is more than a
campaign theme—it is a call to action. We believe that transparency,
interoperability, and harmonized standards are foundational to progress.
Whether through our threat intelligence, policy advocacy, or engineering
innovations, we aim to empower defenders and decision-makers alike.
Thank you for reading this year’s Microsoft Digital Defense Report. We invite
you to explore our companion resources, share your feedback, and join us in
building a secure, more trustworthy digital world.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 79
Appendix
80 Glossary
82 Contributing teams
84 References

Microsoft Digital Defense Report 2025  Contents  Introduction  The threat landscape  The defense landscape  Appendix  80
Access broker  Container (in cybersecurity context)  Device code phishing
Glossary
A cybercriminal who gains unauthorized access to   A lightweight, standalone package of software    A phishing technique where attackers trick users
organizations and sells that access to other criminals,   that includes everything needed to run an   into entering authentication codes on fake portals,
enabling further attacks such as ransomware or   application. Containers are widely used in cloud   allowing them to hijack accounts.
| data theft.  | environments and can be targeted by attackers    |     |
| ------------ | ------------------------------------------------ | --- |
Endpoint
if not properly secured.
AI deepfake  Any device (such as a computer, smartphone, or
Artificial Intelligence-generated audio, video, or   Credential theft  server) that connects to a network and can be
images that convincingly mimic real people or events   Stealing usernames, passwords, or other   targeted by cyberattacks.
| can be used to impersonate individuals, fabricate   | authentication information to gain unauthorized   | Espionage  |
| --------------------------------------------------- | ------------------------------------------------- | ---------- |
| scenarios, or manipulate public perception—         | access to systems or data.                        |            |
The act of spying to obtain confidential information,
| often contributing to fraud, misinformation,   | Critical infrastructure  |     |
| ---------------------------------------------- | ------------------------ | --- |
often for political, economic, or military advantage.
or disinformation.
Essential systems and assets (energy, water,
Exploit
| Attack surface  | transportation, healthcare, etc.) whose disruption   |     |
| --------------- | ---------------------------------------------------- | --- |
A method or tool used by attackers to take
| The total set of points where an unauthorized user   | would have significant societal impact.  |     |
| ---------------------------------------------------- | ---------------------------------------- | --- |
advantage of vulnerabilities in software or systems.
can try to enter or extract data from an environment.
|                                  | Cyber mercenary                                            | Fraud  |
| -------------------------------- | ---------------------------------------------------------- | ------ |
| BEC (Business Email Compromise)  | A private entity that sells hacking tools or services to   |        |
Deceptive practices intended to gain financial or
| A targeted attack where criminals gain access to   | governments or criminals, often operating in legal   |     |
| -------------------------------------------------- | ---------------------------------------------------- | --- |
personal benefit, often involving manipulation
business email accounts to defraud organizations,   gray zones.  or  impersonation.
often by manipulating financial transactions.
Cyber resilience
Human-operated attack
Botnet
|                                                    | The ability of an organization to anticipate, withstand,        | A cyberattack where humans, rather than automated   |
| -------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------- |
| A network of computers infected with malware and   | recover  from,  and  adapt  to  cyberattacks  or  disruptions.  |                                                     |
tools, actively control the intrusion, often adapting
| controlled as a group to perform malicious activities,   | Cyber-enabled  influence  operations  |     |
| -------------------------------------------------------- | ------------------------------------- | --- |
tactics in real time.
such as launching attacks or sending spam.
Efforts by threat actors to manipulate public opinion
Human-operated ransomware
| Cloud security  | or behavior using digital tools, such as social media,   |     |
| --------------- | -------------------------------------------------------- | --- |
A ransomware attack in which cybercriminals
| Protecting data, applications, and systems hosted   | fake news, or deepfakes.  |     |
| --------------------------------------------------- | ------------------------- | --- |
actively control the intrusion, moving through
in cloud environments. As organizations move to
|     | Data  exfiltration  | networks, stealing data, and manually deploying   |
| --- | ------------------- | ------------------------------------------------- |
the cloud, attackers increasingly target cloud assets   The unauthorized transfer or theft of data from an   ransomware for maximum impact. These attacks
and identities.
|     | organization, often as part of a cyberattack.  | are more targeted and damaging than automated   |
| --- | ---------------------------------------------- | ----------------------------------------------- |
Cloud workload
|     | Data theft  | ransomware, often combining extortion with data   |
| --- | ----------- | ------------------------------------------------- |
Applications, services, or processes running in a cloud   theft or disruption of critical services.
Stealing sensitive or valuable information, such as
environment, which can be targeted by attackers.
intellectual property, personal data, or financial records.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 81
Glossary continued
Identity compromise LLM (Large Language Model) Phishing SLM (Small Language Model)
When an attacker gains control of a user’s digital A type of AI model trained on vast amounts of A cyberattack where attackers impersonate A more compact version of a language model,
identity, allowing unauthorized access to systems text data to understand and generate human-like trusted entities to trick individuals into revealing designed to perform language-related tasks efficiently
or data. language. LLMs can answer questions, summarize sensitive information. with fewer computational resources. SLMs are often
Identity platform documents, and assist with decision-making, but can Post-quantum cryptography (PQC) used for specific, focused applications where speed
also be targeted or manipulated by cyber attackers. and efficiency are important, but they may have more
A system or service that manages digital identities, Encryption methods designed to be secure against
limited capabilities compared to LLMs.
authentication, and access controls for users Malvertising quantum computing attacks.
and devices. Malicious advertising that delivers malware to users Prompt injection Supply chain attack
through deceptive online ads. Targeting less secure elements in an organization’s
Incident response (IR) A type of attack on AI systems where malicious
supply chain (vendors, partners) to gain access to the
A structured approach to managing and mitigating Malware instructions are hidden in user input or data, causing
primary organization.
the impact of cybersecurity incidents. Software designed to disrupt, damage, or gain the AI to behave in unintended or harmful ways.
Infostealer unauthorized access to computer systems. Quantum computing Threat intelligence
Information about current and emerging cyber
Malware designed to collect credentials, tokens, and MFA (multifactor authentication) Advanced computing technology that could
threats, used to inform security strategies and
other sensitive information from infected devices. A security process requiring two or more verification break current encryption methods, requiring new
improve defenses.
factors to access systems or data. security standards.
Influence operations
Token theft
Coordinated efforts to affect public perception or Mule herding Ransomware
Stealing authentication tokens (digital keys) to gain
behavior, often using digital channels and sometimes The recruitment and management of individuals Malicious software that encrypts data and demands
unauthorized access without needing a password.
involving misinformation or manipulation. (“money mules”) who move or launder stolen funds payment for its release.
Infrastructure building on behalf of cybercriminals. Remote access tool Vishing
Voice phishing; using phone calls to trick individuals
A tactic where attackers use compromised systems Nation-state actor Software that allows remote control of a computer,
into revealing sensitive information or performing
to stage further attacks against other targets, often A cyber threat actor sponsored or directed by a often used legitimately but also abused by attackers.
risky actions.
creating a base for future operations. government, often targeting other countries for Resilience by design
espionage, disruption, or influence. Virtual credit card (VCC)
Insider threat Building systems and processes that can
A digital payment card generated for online
A risk posed by individuals within an organization Password spray attack withstand, recover from, and adapt to cyberattacks
transactions, often with unique details and limited
who may intentionally or unintentionally cause harm A technique where attackers try common passwords or disruptions.
lifespan to reduce fraud risk.
by leaking data or facilitating attacks. against many accounts to gain unauthorized access. Social engineering
Workload identities
Manipulating people into performing actions or
Digital identities assigned to applications, services,
divulging confidential information, often used in
or automated processes (not people), which can be
phishing and fraud.
targeted by attackers if not properly secured.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 82
AI Safety and Security Customer Security and Trust Enterprise & Security
Contributing
AI Safety and Security is responsible for all aspects Customer Security and Trust drives continuous Enterprise & Security provides platform technologies
of as well as developing and deploying secure and improvement of customer security in Microsoft and solutions to manage and harden platforms
safe AI, including pre-launch evaluation, incident products and online services. Working with against attacks. The team also empowers company-
teams
response, building safety infrastructure, training, engineering and security teams across the company, wide security initiatives in Zero Trust, secure identity,
research, and policy. the team ensures compliance, enhances security, and secure devices, secure supply chain, and scale
drives transparency to protect customers and the management from cloud.
Central Fraud and Abuse Risk (CFAR)
global ecosystem.
Central Fraud and Abuse Risk detects and responds European Government Affairs
to nation-state actors, criminal syndicates, and Cybersecurity Policy and Diplomacy (CPD) European Government Affairs represents Microsoft’s
common cyber criminals who wish to cause financial Cybersecurity Policy and Diplomacy works on positions towards European political institutions,
and reputational harm to Microsoft, its customers, strengthening global cybersecurity by promoting governments and other political actors. The team
and partners. The team also partners with law responsible industry and state behaviour in oversees a large variety of digital policies across
enforcement, industry affiliates, and customers to cyberspace through sustained diplomatic and policy Europe, including AI, cloud, sustainability and
share fraud insights to make the world safer for all. engagement and multistakeholder partnerships. cybersecurity policy.
Cloud Ecosystem Security Digital Crimes Unit (DCU)
Cloud Ecosystem Security is responsible for the core The Digital Crimes Unit has been fighting cybercrime,
cloud security platform, data security, compliance, protecting individuals and organizations, and
governance, and privacy. The team also leads AI- safeguarding the integrity of Microsoft services
powered threat and data intelligence, as well as AI since 2008, through strategic partnerships and
security research and development. engagements, the seizure of criminal infrastructure,
and the disruption of global cyber threats and
Corporate Standards Group
criminal networks.
Corporate Standards Group represents Microsoft in
multistakeholder organizations that are establishing Digital Security & Resilience
standards on issues such as cybersecurity, AI, Digital Security & Resilience is dedicated to
and data. The team works with governments, civil enabling Microsoft to build the most trusted
society, academia, and industry to create coherent devices and services, while keeping our
international practices that can be used to develop, company and customers protected.
evaluate, and manage trustworthy technology.

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 83
Contributing teams continued
Extended Security Posture Management Microsoft Defender Experts response, and automated disruption capabilities
Extended Security Posture Management builds Microsoft Defender Experts manage Threat Hunting to more than 1 billion devices across all domains
cross-domain pre-breach security solutions for attack and Extended Detection and Response service that (Endpoint, Identity, Office, Cloud, IoT/OT.)
surface management and threat exposure reduction. proactively looks for threats 24/7/365 using Microsoft
National Security Officers
The team brings together posture management Defender data.
National Security Officers advise on best practice
capabilities for devices, identities, cloud, and
Microsoft Incident Response—the Detection cyber guidelines, support driving compliancy and
applications into a set of consolidated products
and Response Team (DART) certification of Microsoft’s services and products in
serving security leaders and their teams.
Microsoft Incident Response—the Detection countries with particular national requirements.
GUARD Detection Engineering team in the and Response Team provides incident hunting,
Office of Responsible AI (ORA)
Cyber Defense Operations (CDO) under the CISO cyber resilience, and threat intelligence services to
Office of Responsible AI (ORA) collaborates with
organization customers. The team maintains strategic partnerships
stakeholders across Microsoft to develop policies,
The Security CTO office mission is to drive innovation, with security organizations, governments, and
practices, and governance systems to uphold our
identify gaps across the security division, and internal Microsoft groups.
AI principles. ORA also helps to shape the new laws
promote opportunities related to organizational
Microsoft Threat Analysis Center needed to ensure that the promise of AI technology
growth and talent. The team identifies systemic
Microsoft Threat Analysis Center identifies and is realized for the benefit of society at large.
opportunities not only in product strategy but also
analyzes nation-state threats and influence
across the division and Microsoft. Office of the Chief Scientific Officer
operations, integrating intelligence with geopolitical
Office of the Chief Scientific Officer leads strategic
Identity & Network Access context to deliver timely insights to Microsoft and its
initiatives at the confluence of the sciences,
Identity & Network Access innovates and builds customers for effective response and protection.
technology, and society, including frontier efforts in AI.
solutions that manage and govern identities and
Microsoft Threat Intelligence Center (MSTIC)
access, including the consumer sign-in experience. US Government Affairs
Microsoft Threat Intelligence Center (MSTIC)
US Government Affairs advances collaborative
Insights, Data Engineering, Analytics, and Systems discovers, tracks, and disrupts sophisticated cyber
discussions with US federal and state government
(IDEAS) and Insights, Data Engineering, and threat actors to protect Microsoft and its customers.
representatives, policymakers, and third-party
Analytics Momentum and Storytelling MSTIC produces actor-centric threat intelligence
groups, as well as the UN and other international
Insights, Data Engineering, Analytics, and Systems and delivers high quality finished intelligence across
organizations. The team oversees a large variety of
(IDEAS) and Insights, Data Engineering, and Microsoft’s security solutions.
policy priorities including AI, cybersecurity, cloud,
Analytics Momentum and Storytelling curates
Microsoft Threat Protection Research sustainability and competition.
metrics used in non-financial public disclosures.
Microsoft Threat Protection Research combines
The team also helps craft the messages around those
the trillions of signals we see daily with world class
metrics, and ensures that the messages align with
security research into highly sophisticated and
Microsoft’s perspectives.
emerging threats to deliver prevention, detection,

Microsoft Digital Defense Report 2025 Contents Introduction The threat landscape The defense landscape Appendix 84
References Part I: The threat landscape 14 Communication Compliance | Microsoft Learn 29 The EU AI Act: Prohibited Practices |
Microsoft (January 2025)
15 Jasper Sleet: North Korean remote IT workers’
1 Cyber Signals: Cyberthreats in K-12 and higher
evolving tactics to infiltrate organizations | Microsoft 30 The General-Purpose AI Code of Practice:
education | Microsoft Security Blog
Security Blog Shaping Europe’s digital future | Microsoft AI
2 Mythical Beasts and where to find them: Mapping Transparency Report
16 Protecting Quantum Science and Technology |
the global spyware market and its threats to national
FBI.gov 31 Cyber–Physical Resilience: Evolution of Concept,
security and human rights | Atlantic Council
Indicators, and Legal Frameworks
3 Intelligence-Driven Cyber Security | Intel 471
32 Fortifying the Resilience of our Critical Infrastructure
4 Have I Been Pwned: Check if your email address has Part II – The defense landscape
been exposed in a data breach
5 Protecting customers from Octo Tempest attacks 17 Secure employee access in the age of AI |
across multiple industries | Microsoft Security Blog Microsoft (2025)
(July 2025)
18 International Counter Ransomware Initiative
6 The latest marketing tactic on LinkedIn: AI-generated
19 Ransomware Task Force (RTF) | Institute for Security
faces | NPR
+Technology
7 Cybersecurity Information Sheet: Contextualizing
20 The Pall Mall Process Code of Practice for States |
Deepfake Threats to Organizations | National
GOV.UK
Security Agency
21 A global clearing house for real-time sharing of scam
8 Synthetic ID document fraud is exploding worldwide
and fraud signals | Global Signal Exchange
thanks entirely to Generative AI: here’s how to stay
safe | TechRadarr 22 International Scammers Steal Over $1 Trillion
in 12 Months in Global State of Scams Report |
9 Grand View Research
Global Anti-Scam Alliance
10 Harvard Kennedy School et al., “Evaluating Large
23 Scams Prevention Framework – Protecting
Language Models’ Capability to Launch Fully
Australians from scams | Treasury.gov.au
Automated Spear Phishing Campaigns: Validated
on Human Subjects,” arXiv preprint, Nov. 30, 2024. 24 APP fraud reimbursement protections | Payment
Study found AI-automated phishing can be up to Systems Regulator
50x more profitable than traditional methods when
25 Combatting Scams | Monetary Authority
targeting large groups
of Singapore
11 States’ use of non-state actors in cyberspace |
26 Mitigating AI Security Risks for UK Prosperity &
Observer Research Foundation
National Resilience | LASR
12 Nation-State Threats | Cybersecurity and
27 Frontier Governance Framework | Microsoft
Infrastructure Security Agency (CISA)
(February 2025)
13 2025 Ponemon Cost of Insider Threats Global Report
28 AI Literacy Starting Guide | Microsoft (June 2025)

Microsoft Digital
Defense Report 2025
Lighting the path to a secure future
For more news on cybersecurity, visit:
https://microsoft.com/corporate--responsibility/cybersecurity
For more report insights, visit:
https://microsoft.com/mddr
For more news on cybersecurity
policy, follow us on LinkedIn:
https://aka.ms/MOILinkedin
For insights and trends for security leaders, visit:
https://www.microsoft.com/security/security-- insider
A Microsoft Threat Intelligence report
October 2025
v2