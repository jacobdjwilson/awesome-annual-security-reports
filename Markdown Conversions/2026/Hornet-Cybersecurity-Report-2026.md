# Cybersecurity-Report 2026

## Table of Contents
- [About Hornetsecurity](#about-hornetsecurity)
- [What is the Cybersecurity Report?](#what-is-the-cybersecurity-report)
- [What is the Security Lab?](#what-is-the-security-lab)
- [How to Use This Report](#how-to-use-this-report)
- [Chapter 1: Executive Summary](#chapter-1-executive-summary)
- [Chapter 2: The State of Security in the Industry](#chapter-2-the-state-of-security-in-the-industry)
- [Chapter 3: An Analysis of the Major Security Incidents and Cybersecurity News of 2025](#chapter-3-an-analysis-of-the-major-security-incidents-and-cybersecurity-news-of-2025)
- [Chapter 4: Forecasting the Threat Landscape in 2026](#chapter-4-forecasting-the-threat-landscape-in-2026)
- [Chapter 5: References](#chapter-5-references)

---

## About Hornetsecurity
Hornetsecurity empowers companies and organizations of all sizes to focus on their core business by protecting M365 workloads, email communications, securing data, and ensuring business continuity and compliance with next-generation cloud-based solutions.

Our flagship product, 365 Total Protection, is the most comprehensive cloud security solution for Microsoft 365 on the market and includes email security, compliance, governance, and backup.

## What is the Cybersecurity Report?
The Cybersecurity Report by Hornetsecurity is an annual analysis of the current threat landscape based on real-world data collected and studied by Hornetsecurity’s dedicated Security Lab team. Hornetsecurity processes more than 6 billion emails every month. By analyzing the threats identified in these communications, combined with a detailed knowledge of the wider threat landscape, the Security Lab reveals major security trends, threat actor campaigns, and formulates informed projections for the future of Microsoft 365 security threats, enabling businesses to act accordingly. Findings and data from 2025 and projections for 2026 are contained within this report.

## What is the Security Lab?
The Security Lab is a division of Hornetsecurity that conducts forensic analysis of the most current and critical security threats, specializing in email security and the Microsoft 365 ecosystem. This multinational team of security specialists has extensive experience in security research, software engineering, and data science.

An in-depth understanding of the threat landscape established through hands-on examination of real-world phishing attacks, malware, ransomware gangs and more, is critical to developing effective countermeasures. The detailed insights uncovered by the Security Lab serve as the foundation for Hornetsecurity’s next-gen cyber-security solutions.

## How to Use This Report
This report contains five main sections:

- Chapter 1 is the Executive Summary.
- Chapter 2 focuses on the current threat landscape of the Microsoft 365 platform.
- Chapter 3 covers current concerns and discussions regarding the biggest threats and trends from 2025.
- Chapter 4 contains predictions from the Security Lab about cyber-security threats in 2026, along with advice and guidelines to help protect your business.
- Chapter 5 lists all the references and supporting links used in this report.

---

# Chapter 1: Executive Summary

2025 has been a year defined by acceleration. Threat actors embraced automation, artificial intelligence, and social engineering at unprecedented speed, while defenders raced to adapt governance, resilience, and awareness programs to match. What we observed across the Hornetsecurity ecosystem, via our analysis of over 72 billion emails processed, confirms a simple truth: the attack surface is expanding faster than most organizations can secure it.

Email remains the most consistent delivery vector for cyber threats, but tactics have evolved. Malware-laden emails surged by 131% year-over-year, accompanied by a rise in scams (+34.7%) and phishing (+21%). Attackers have traded blunt-force volume for precision evasion, leveraging infrastructure, obfuscated URLs, and stealthy HTML techniques to bypass filters and human visibility alike. Meanwhile, malicious TXT and legacy DOC attachments, once considered to be largely benign or outdated, have re-emerged as primary infection vehicles, highlighting how even “low-risk” file types can no longer be ignored.

Ransomware also made an aggressive comeback in 2025. After several years of relative decline, 24% of organizations reported being victims. This is a 29% increase from the previous year. While immutable backups and improved disaster recovery planning have lowered ransom payment rates to just 13% of cases, attackers have responded by diversifying entry points and objectives. Phishing, compromised credentials, and endpoint exploitation now share equal footing as infiltration paths, and new “Ransomware 3.0” variants are beginning to focus less on encryption and more on data integrity manipulation—corrupting trust itself rather than just availability.

Artificial Intelligence has reshaped both sides of the security equation. CISOs are optimistic but cautious: 61% believe AI has directly increased ransomware risk. CISO concerns around AI are vast. They include things like phishing automation to deepfake impersonation and model poisoning. AI’s potential for misuse has become a defining feature of the threat landscape. Yet the defensive side is catching up, with 68% of organizations investing in AI-powered detection and analytics. The challenge for organizations and security teams in 2026 is governance and working towards harnessing AI’s capabilities without amplifying the risks.

The Hornetsecurity Security Lab forecasts that the coming year will see continued uncontrolled adoption of AI tools across enterprises, often faster than legal or security teams can evaluate. This, paired with the weaponization of agentic AI, will magnify existing vulnerabilities while introducing new ones that defy traditional containment models. Identity, too, remains the primary battlefield: attacker-in-the-middle kits, compromised browser extensions, and OAuth abuse show that credentials and identity continue to be the weak link in modern cloud ecosystems.

Despite this rising complexity, there are reasons for optimism. Organizations are steadily maturing. The adoption of Zero Trust principles, immutable backup technologies, and phishing-resistant MFA are becoming baseline expectations rather than aspirational goals. Security awareness, once a compliance checkbox, is increasingly embedded in company culture. The path forward is clear: resilience, not perfection, is the new metric of success. Those who treat cybersecurity as a core element of business continuity and not just an IT issue will be best positioned to thrive in 2026’s evolving threat landscape.

---

# Chapter 2: The State of Security in the Industry

## Email Security Trends
Email remains the backbone of business communication and, as our data shows, it also continues to be the primary battleground for attackers. 2025’s classification and threat-type shifts reveal two simultaneous realities: attackers are experimenting with new file types and low-effort delivery methods (TXT and legacy DOC surged), and at the same time social engineering remains a consistent lever for compromise.

### Spam, Malware, & Advanced Threat Metrics
The headline numbers are unambiguous: Malware saw the largest relative increase (+130.92%), followed by Scams (+34.70%) and Phishing (+20.97%). Those three categories account for the bulk of the risk that results in operational impact (data theft, encryption, business disruption).

| Category | Adjusted YoY Change 2025 vs. 2024 |
| :--- | :--- |
| Malware | +130.92% |
| Scam | +34.70% |
| Phishing | +20.97% |
| Dirty Commercial Emails | +17.72% |
| Commercial Email | +2.37% |
| Legitimate Messages | +3.38% |
| Transactional | +3.19% |
| Spam | +0.03% |
| Social | -8.05% |
| Suspect / Spear Phishing | -9.75% |
| Pro Commercial Emails | -13.73% |
| Bounce | -18.69% |

## Top 10 Attack Techniques Used in Email Attacks in 2025
1. **Fake From Header Alteration**: Attackers forge the “From” header in emails to impersonate trusted senders.
2. **Fake Spamcause Header Alteration**: Manipulation of spam-related headers to bypass spam filters.
3. **Leverage Legit Hosting Platform to Send Campaign**: Using reputable hosting or email services to distribute phishing or malicious campaigns.
4. **Use of Exotic or Non-Existent TLDs**: Employing unusual or fake top-level domains (e.g., .xyz, .club).
5. **URL Shortening**: Using URL shorteners to hide the true destination of malicious links.
6. **HTML <a> Tag Empty**: Embedding empty anchor tags in HTML emails to confuse spam filters.
7. **Multi-Parted Emails**: Sending emails with multiple MIME parts to evade detection.
8. **URL with Non-ASCII Characters**: Including special or Unicode characters in URLs to create visually deceptive links.
9. **Random Domains / URL Fuzzing**: Generating random or slightly altered domains to bypass domain-based filtering.
10. **ZeroFont Technique**: Inserting zero-size font text in emails to manipulate keyword-based filters.

## Attachment Use and Types in Attacks
![Chart showing file-type growth for malicious payloads in 2025]

- **TXT (+181.39%)** and **DOC (+118.25%)** are the fastest-growing file carriers.
- **ZIP (+29.82%)** remains a vehicle for payload bundling.
- **ICS** and **SHTML** are new entries to the top-ten list.

---

# Chapter 3: An Analysis of the Major Security Incidents and Cybersecurity News of 2025

- **October 2024 – Internet Archive Breach**: 31 million user accounts compromised via an exposed GitLab configuration file.
- **December 2024 – U.S. Treasury Hack**: Chinese APT exploited a supply-chain weakness in BeyondTrust.
- **January 2025 – Ivanti & SonicWall Zero Days**: Critical VPN vulnerabilities exploited for remote code execution.
- **March 2025 – Juniper Networks Router Espionage**: China-nexus APT (UNC3886) exploited Junos OS to implant backdoors.
- **June 2025 – UNFI Ransomware**: Disrupted food supply chain, highlighting cascading risks.
- **July 2025 – Scattered Spider Attacks**: Targeted aviation (Qantas, WestJet) via social engineering of helpdesk staff.
- **July 2025 – Ingram Micro Ransomware**: Global outage caused by the "SafePay" ransomware group.
- **July 2025 – "ToolShell" SharePoint Attacks**: Exploited zero-day vulnerabilities in on-premises SharePoint servers.
- **August 2025 – Salesloft+Drift Compromise**: Supply chain attack via OAuth token theft affecting numerous major tech firms.
- **September 2025 – Jaguar Land Rover Ransomware**: Massive production halt across global factories; estimated £1.9 billion impact.
- **October 2025 – F5 Complete Compromise**: Sophisticated nation-state actor (UNC5221) maintained access for 12 months using "BRICKSTORM" malware.

---

# Chapter 4: Forecasting the Threat Landscape in 2026

## The Security Lab’s 2026 Predictions

### 1. Uncontrolled Adoption of AI Tools
The pace of AI innovation has outstripped the ability of security teams to evaluate implementations. This expands the attack surface, introducing risks like prompt injection and unintended data leakage.

### 2. Weaponization of Agentic AI
Agentic AI systems (autonomous models) are being used to script and launch multi-vector campaigns, lowering the barrier to entry for sophisticated cybercrime.

### 3. Ransomware 3.0: LLM-Driven and Integrity-Focused
Attackers are shifting from simple encryption to data integrity manipulation—altering or falsifying records to destroy trust in data itself.

### 4. Attacker-in-the-Middle (AitM)
The rise of sophisticated phishing kits (like Evilginx) makes phishing-resistant MFA (such as FIDO2/WebAuthn) a mandatory requirement for all organizations.

---

# Chapter 5: References
[^1]: OWASP LLM01:2025 Prompt Injection Guidance.
[^2]: Anthropic, "Detecting and Countering Misuse of AI," August 2025.
[^3]: NYU Tandon School of Engineering, 2025 Study on Autonomous Attack Chains.

---

phishing  emails  or
Teams messages into clicking a link to it. Users
sign  in  to  the  fake  page,  and  their  username,
password,  and  MFA  prompts  are  passed  to  the
legitimate sign in page behind the scenes, while
the attacker steals the resulting token, and can
then access everything the user can, known as
Attacker-in-the-Middle (AiTM).

The ability to manage the MFA prompt is now a
“standard  feature”  in  these  phishing  kits.  The
only  good  defense  is  phishing  resistant  MFA
technologies  such  as  FIDO2  hardware  keys,
Windows  Hello  for  Business,  Certificate  based
Authentication  (CBA)  and  Passkeys,  as  these
are  tied  to  the  legitimate  sign  in  page,  and
won’t work on the fake one, even if the user has
been tricked. However, not only do you need to
deploy  phishing  resistant  MFA,  you  must  also
mandate it as the only sign in method, because
most  phishing  kits  now  will  also  force  a  down-
grade from a stronger MFA method to a less se-
cure one.

PASSKEY ADOPTION WILL BE SLOWED BY
CONFUSING USER EXPERIENCES
While  hardware  FIDO  keys  are  a  great  option
for  phishing  resistant  MFA,  it’s  an  added  cost
for  every  user  to  budget  for.  Passkeys,  where
the  security  chip  in  your  modern  smartphone
is used instead, are an alternative, and we pre-
dicted  that  their  adoption  this  year  would  ac-
celerate, which it has, but not to the extent we
expected.  The  main  reason  for  this  is  a  frag-
mented user experience, it looks differently on
an iPhone, an Android phone or a Windows / Ma-
cOS laptop. Furthermore, there are two flavors,
with consumer ones being “syncable”, meaning

they’re stored in your Apple or Google consum-
er  account  so  you  can  use  them  on  different
devices.  Storing  corporate  credentials  in  end
users’  personal  cloud  accounts  isn’t  accept-
able for most businesses, so they generally en-
force non-syncable passkeys. Those are locked
to  the  smartphone  where  they  were  created,
and in the case of Microsoft 365, the only app
that’s accepted is Microsoft Authenticator. Add
to  this  the  confusing  experience  where  you’re
signing in to a service on your laptop and then
have  to  scan  a  QR  code  with  your  phone,  and
then complete the sign in flow on your phone.
Passkeys  are  the  future  of  phishing  resistant
MFA  but  the  tech  giants  need  to  get  together
and  harmonize  the  overall  experience  for  both
consumer and business users.

IDENTITY VERIFICATION AND RESET
PROCESSES WILL CONTINUE TO
COMPROMISE ORGANIZATIONS
Several  of  the  very  large  breaches  we’ve  seen
recently  were  due  to  (often  outsourced)  help
desk  staff  being  tricked  into  resetting  ac-
counts  for  administrative  user  accounts.  Re-
member,  your  authentication  strength
isn’t
measured  by  which  technology  you  use  when
everything is working normally, but by how hard
it  is  to  subvert  your  enrolment  and  recovery
processes. How do you validate that new hires
are  actually  the  people  you  expect  (and  not  a
North Korean infiltrator) in today’s remote work-
ing  world?  What’s  your  process  for  recovering
accounts  for  users  who  have  lost  their  phone,
FIDO  key,  forgotten  their  password  and  whose
laptop  just  died?  Do  you  have  a  more  secure
process for high privilege accounts? (Including
the  requirement  for  an  in-person  validation  at
a  company  office).  Identity  is  the  new  firewall,
but  you  must  look  holistically  at  mitigating
risks  in  your  entire  identity  workflow,  starting
from when the job offer is made to the last day
of work.

24

CYBER SECURITY REPORT 2026SAAS APPS ARE THE NEW ATTACK SURFACE
Certain  enterprise  compromises  over  the  last
few  years  are  interesting  because  they  com-
pletely  bypass  the  traditional  “compromise
a  normal  user  –  pivot  in  the  internal  network
–  compromise  administrator  accounts”.  As
businesses  become  more  and  more  reliant  on
SaaS  services,  new  types  of  attacks  that  only
compromise  cloud  data  and  identities  are  be-
coming  more  prevalent.  Normal  defenses  such
as  EDR  are  mostly  blind  to  these  attacks,  be-
cause while they’re taking place in the browser,
there’s  no  malicious  files  or  activity  that  end-
point protection can detect. As a matter of fact,
so  much  of  modern  business  computing  now
happens in a browser, which is opaque to EDR,
that  using  an  enterprise  browser  and/or  spe-
cialized software for protection in the browser is
our strong recommendation. Mitre even has an
ATT&CK MATRIX for different SaaS attacks.

BROWSER EXTENSIONS WILL COMPROMISE
MORE BUSINESSES IN THE COMING YEAR
Modern  browsers  are  complex  applications,
almost  like  entire  operating  systems  in  them-
selves, and full of protection that keep us most-
ly safe from dangers on the internet, both in our
personal  life  and  at  work.  But  most  of  us  also
use  browser  extensions,  often  for  productivi-
ty  or  convenience,  but  sometimes  these  come
with  hidden  risks.  In  some  cases,  they’re  vul-
nerable in some way, degrading the protection
of the browser itself, in other cases they’re in-
tentionally  malicious.  This  could  be  by  having
a similar name to a popular add-in, or by crim-
inals  buying  a  previous  benign  extension  and
then weaponizing it.

Make  sure  your  business  has  a  way  of  track-
ing extensions that are installed in your user’s
browsers, easy ways of blocking ones that are
found  to  be  malicious  (Intune  or  AD  GPOs  can
do  this)  and  educating  your  users  about  the
risks.

Estimated likelihood of achieving CRQC

Less likely

More likely

2025

2030

2035

2040

The period of vulnerability for critical
data (with a 10-year lifespan) compro-
mised by ‘harvest now, decrypt later’
attacks before PQC transition.

Create PQC transition plan

Commence PQC transition

Complete PQC transition

INTRODUCTION

CHAPTER 1

CHAPTER 2

CHAPTER 3

CHAPTER 4

CHAPTER 5

PREDICTIONS REGARDING QUANTUM
COMPUTING
Most  threats  we  look  at  in  this  report  are  cur-
rent,  while  the  advent  of  a  Cryptographically
Relevant  Quantum  Computer  (CRQC)  is  still
some years away. This day, known as Q-Day, is
when these types of computers have sufficient
scale (number of Qubits – the equivalent to bits
in  a  classical  computer),  and  low  enough  cost
that  they  can  use  Shor’s  algorithm  to  break
asymmetric  encryption  such  as  RSA  and  Dif-
fie-Hellman. Or Grover’s algorithm to halve the
strength  of  symmetric  cryptography  (AES-128
becomes AES-64).

Many  different  tech  companies,  including  the
usual  suspects  (Google,  IBM,  Microsoft)  are
pouring  millions  into  different  flavors  of  quan-
tum computers, seeing which technological ap-
proach is going to provide enough stable qubits.
The problem is noise, if you have lots of qubits,
but use up most of them for error correction; the
overall number of logical qubits available to run
your calculations are minimized. Quantum com-
puters  will  not  replace  our  current  computers;
instead  they’ll  be  used  for  very  specific  types
of  calculations,  including  breaking  our  current
encryption algorithms.

While  CRCQs  are  still  5  to  15  years  away,  you
can’t  wait  until  they  arrive.  Your  organization
should  start  planning  now,  if  you  store  any
Personally  Identifiable  Information  (PII),  Per-
sonal  Health  Information  (PHI)  and  intend  to
(or  you’re  compelled  to  by  regulation)  to  keep
it  for  longer  than  five  years,  you  need  to  start
using quantum resistant algorithms for the en-
cryption now. This is because several agencies
around  the  world  are  using  Harvest  Now,  De-
crypt Later (HDNL) to store data that they can’t
decrypt now but will be able to with CRCQs. Fur-
thermore,  it’s  a  huge  project;  you  need  to  find
every system, device and part of your network
that  uses  encryption,  which  algorithm  is  used
and what type of data is stored or transmitted.
Sometimes it’ll be easy to add quantum resist-
ant algorithms, in other cases you’ll need to re-
place  the  system  entirely,  or  re-architect  your
processes.

NIST has standardized three quantum resistant
algorithms:

 »

 FIPS 203 defines a cryptographic scheme
called Module-Lattice-Based Key-Encap-
sulation Mechanism (ML-KEM), which is
derived from the CRYSTALS-KYBER sub-
mission.

 »

 »

 FIPS 204 is the Module-Lattice-Based
Digital Signature Algorithm (ML-DSA),
based on the CRYSTAL-Dilithium submis-
sion.

 FIPS 205 specifies the Stateless Hash-
Based Digital Signature Algorithm (SLH-
DSA), which is derived from the SPHINCS+
submission.

They rely on Transport Layer Security (TLS) ver-
sion 1.3 so start by rolling that out everywhere
you can in your environment.

As  for  Operating  Systems,  preview  versions
of  Windows  11  and  Windows  Server  have  up-
dated  versions  of  SymCrypt,  the  same
li-
brary  that’s  used  across  Azure  and  Microsoft
365.  ML-KEM  and  ML-DSA  are  already  availa-
ble  in  SymCrypt,  both  on  Windows  and  Linux.
SymCrypt-OpenSSL  also  offers  the  same  sup-
port  for  OpenSSL.  Apple  is  also  including PQC
in their CryptoKit for developers, and iMessage
in iOS and TLS 1.3 in iOS26 are already incorpo-
rating PQC.

If you write your own applications in-house aim
for crypto agility so that you can swap out ci-
pher suites, or entire algorithms as updates are
delivered.

RISKS FOR ORGANIZATIONS IN 2026

Cybersecurity isn’t a technology problem, it’s a
people  and  process  problem.  As  so  often  hap-
pens when you’re deep into the latest technol-
ogy and seeing rapid developments in GenAI, or
Machine  Learning,  or  Agentic  AI,  the  solutions
you  see  are  tech  based  (“when  you  only  have
a  hammer,  every  problem  looks  like  a  nail”).
But  organizations  rarely  get  breached  based
on  technology  failures  alone,  it’s  more  likely  a
combination  of  people,  process  and  technolo-
gy failures. The Swiss cheese model illustrates
this clearly:

26

CYBER SECURITY REPORT 2026In other words, if you build cyber resiliency into
your organization, through layers of protection
and processes, you’ll be more likely to avoid a
devastating breach.

based Authentication and Passkeys,
which doesn’t allow authentication to fake
login pages, even if the user themselves
has been tricked.

No  matter  the  size  of  your  business,  you  will
be  a  target  of  cyber  security  attacks  in  2026.
As  you  can  see  in  our  data,  being  a  small  or-
ganization / a not-for-profit / “not having any-
thing  worth  attacking”  isn’t  a  defense  against
criminals.  If  your  business  has  sensitive  data
and cash reserves, you are a target. Build a cy-
ber resiliency program based on the Zero Trust
principles:

 »

 »

 »

 Assume breach – obviously you build
strong, layered protections, but they will
eventually fail. At some point the holes
will line up, and a breach will happen. Do
you have detections in place to spot that
quickly? Do you have isolated networks
and only the required permissions as-
signed to minimize the blast radius? Do
you have the people and the processes
in place to react to the alerts and evict
the attackers quickly before they can do
major damage?

 Least privilege – this is possibly the hard-
est thing to get right, give people only the
permissions they need to do their job, and
regularly review them so they don’t accu-
mulate over time.

 Verify each connection – have a strong
policy engine in place (Conditional Access
in Entra ID) that verifies each login and
access to applications, files and other re-
source to ensure that access isn’t allowed
by default, but rather only permitted when
the right conditions are met.

Before  spending  money  on  advanced  security
tools that solve specific problems, start by tak-
ing  care  of  security  hygiene  basics  based  on
the above principles:

 »

 Implement MFA for everyone. Given the
huge increase in Attacker-in-The-Middle
(AiTM) kits having MFA bypass built in,
you need to move to phishing resistant
MFA. This includes hardware OAuth keys,
Windows Hello for Business, Certificate

 »

 »

 »

 »

 Have a strong endpoint protection solu-
tion on all devices where that’s possible,
and integrate that with identity, cloud ap-
plications and an email hygiene solution
for comprehensive eXtended Detection
and Response (XDR).

 Train your users to spot phishing at-
tempts, whether in email, Teams, Zoom or
WhatsApp but more importantly – build a
security culture. Assuming that IT or the
security team is taking care of all cyber
security so everyone else in the business
don’t have to worry about it is like saying
“only the workplace health and safety
staff needs to worry about accidents”. No
– everyone needs to speak up when they
spot something dangerous, whether that’s
balancing precariously on a rickety chair
to replace a light bulb, or someone about
to click on a link that they shouldn’t.

 Patch your software, but unless you want
to double the size of your IT department,
do it in a smart way. Apply Continuous
Threat Exposure Management (CTEM)
principles to protect your business-criti-
cal systems that have exploitable vulner-
abilities first rather than trying to patch
everything, everywhere, which is impossi-
ble.

 Look at your supply chain. Several large
breaches in recent months have been due
to outsourced helpdesk organizations
being socially engineered (hacking people
instead of computer systems). Understand
all your outsourced processes, remem-
bering that you can outsource a function,
but not the risk associated with it. And
investigate all the supply chains that
make your business operate, and build
in resilience for when they are disrupted,
either through cybersecurity attacks or
for other reasons.

INTRODUCTION

CHAPTER 1

CHAPTER 2

CHAPTER 3

CHAPTER 4

CHAPTER 5

A CYBER RESILIENT ORGANIZATION

Because cyber security is a people and process
problem, the solution isn’t more technology, it’s
about changing the culture of your business.

We  can  learn  a  lot  from  the  aviation  industry,
where every incident and accident is thoroughly
investigated, not to assign blame, but to identi-
fy all the different people, process and technol-
ogy factors that contributed to it. And then take
those lessons and incorporate more / different
training, changing processes and technologies
to make sure it doesn’t happen again.

It  starts  with  fostering  a  safety  culture  where
everyone feels safe to speak up when they see
something  that’s  not  right.  This  only  happens
when  people  aren’t  blamed  individually  when
an incident happens – it’s about improving the
processes  so  that  people  aren’t  as  likely  to
make  those  mistakes.  In  turn,  this  means  that
cybersecurity  is  everyone’s  responsibility,  not
just  the  IT  or  security  department  –  because
various  parts  of  the  business  make  technolo-
gy decisions that bring risks that everyone, not
just  IT  needs  to  manage.  We  in  cybersecurity
must  also  do  better  when  it  comes  to  commu-
nicating  with  other  stakeholders,  translating
“geek speak” into business risk language.

As  you  build  resiliency  in  every  part  of  your
business,  keep  up  with  the  changes  in  the
threat landscape as attackers are ever innova-
tive in finding cracks in our systems to exploit.

A HOLISTIC SECURITY STRATEGY

We’ve  mentioned  it  earlier  but  it  bears  repeat-
ing – start with the basics. Foundational cyber
security hygiene processes and technology will
serve your organization’s defenses much better
than  the  latest  cyber  security  point  solution.
You  need  multiple  layers  of  protections  (re-
member the Swiss cheese model):

Next-Gen Spam/Malware detection with ATP
for behavioral analysis to protect against the
contin¬ued barrage of email-based threats we
see in this industry

End-User Security Awareness Training to
train end-users to spot social engineering at-
tacks and spear-phishing attacks

Backup and recovery capabilities for BOTH
on-premises data and data that lives in cloud
services such as M365 for recovery purposes
should a ransomware attack get through

Compliance and governance features that
help protect against accidental data leakage
and ensure that compliance controls are met

Least privilege and sharing control for your
sensitive corporate data stored in SharePoint
and OneDrive for Business

AI powered cyber assistant for Email and
Teams protection, helping every user stay safe

Learn More
Cybersecurity is just one of the many challeng-
es facing businesses today but not prioritizing
it  enough  can  lead  to  catastrophic  outcomes
(just ask Jaguar Land Rover).

Just  as  many  businesses  outsource  parts
of  their  operations  to  specialists
in  that
area  –  take  advantage  of  the  deep  knowledge
and skills we at Hornetsecurity have developed
since  2007. Partner  with  us  to  keep  your  busi-
ness safe.

28

CYBER SECURITY REPORT 2026INTRODUCTION

CHAPTER 1

CHAPTER 2

CHAPTER 3

CHAPTER 4

CHAPTER 5

START YOUR FREE TRIAL

30

CYBER SECURITY REPORT 2026INTRODUCTION

CHAPTER 1

CHAPTER 2

CHAPTER 3

CHAPTER 4

CHAPTER 5

CHAPTER 5
RESOURCES

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

 »

https://www.hornetsecurity.com/en/blog/ransomware-impact-report-2025-press-release/

https://www.hornetsecurity.com/en/blog/ciso-insights/

https://www.hornetsecurity.com/en/blog/sharepoint-vulnerability/

https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-june-2025/

https://www.anthropic.com/news/detecting-countering-misuse-aug-2025

https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/

 https://www.cnbc.com/2025/09/25/judge-anthropic-case-preliminary-ok-to-1point5b-settlement-with-authors.
html

 https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-in-
telligence

 https://www.hornetsecurity.com/en/blog/nis2-directive/

https://www.infosecurity-magazine.com/news/nis2-compliance-strain-budgets/

https://www.infosecurity-magazine.com/news/dora-compliance-costs-soar/

https://ossf.github.io/malicious-packages/stats/

 https://techcommunity.microsoft.com/blog/windowsdriverdev/towards-rust-in-windows-drivers/4449718

https://www.youtube.com/watch?v=uDtMuS7BExE

 https://pentiumsoak.com/the-rise-of-rust-in-the-linux-kernel-transforming-security-stability-in-2025/

 https://medium.com/cybersecurity-and-iot/how-googles-switch-to-rust-programming-is-redefining-android-s-se-
curity-a-52-drop-in-memory-29620cd46e0a

https://security.apple.com/blog/memory-integrity-enforcement/

https://www.aim.security/post/echoleak-blogpost

https://genai.owasp.org/llmrisk/llm01-prompt-injection/

https://arxiv.org/abs/2508.20444v1

https://github.com/kgretzky/evilginx2

 https://www.proofpoint.com/us/blog/threat-insight/dont-phish-let-me-down-fido-authentication-downgrade

https://en.wikipedia.org/wiki/North_Korean_remote_worker_scheme

https://attack.mitre.org/matrices/enterprise/cloud/saas/

https://postquantum.com/post-quantum/crqc/

https://en.wikipedia.org/wiki/Shor%27s_algorithm

https://en.wikipedia.org/wiki/Grover%27s_algorithm

https://github.com/microsoft/SymCrypt-OpenSSL

https://developer.apple.com/videos/play/wwdc2025/314/

https://en.wikipedia.org/wiki/Cryptographic_agility

https://en.wikipedia.org/wiki/Swiss_cheese_model

 https://community.isc2.org/ijoyk78323/attachments/ijoyk78323/industry-news/5604/1/g21f.pdf

https://en.wikipedia.org/wiki/Continuous_Threat_Exposure_Management

https://www.hornetsecurity.com/en/blog/supply-chain-attacks/

https://www.hornetsecurity.com/en/services/advanced-threat-protection/

https://www.hornetsecurity.com/en/services/security-awareness-service/

https://www.hornetsecurity.com/en/services/365-total-backup/

https://www.hornetsecurity.com/en/services/vm-backup/

https://www.hornetsecurity.com/en/services/365-total-protection/

https://www.hornetsecurity.com/en/services/365-permission-manager/

https://www.hornetsecurity.com/en/services/ai-cyber-assistant/

https://www.hornetsecurity.com

32

CYBER SECURITY REPORT 2026INTRODUCTION

CHAPTER 1

CHAPTER 2

CHAPTER 3

CHAPTER 4

CHAPTER 5

ABOUT THE AUTHORS
WRITTEN BY

ANDY SYREWICZE

Andy has over 20 years’ experience in providing technology
solutions across several industry verticals. He specializes in
Infrastructure, Cloud, and the Microsoft 365 Suite.

Andy holds the Microsoft MVP award in Security.

PAUL SCHNACKENBURG

Paul Schnackenburg started in IT when DOS and 286 pro-
cessors were the cutting edge. He runs Expert IT Solutions,
an MSP on the Sunshine Coast in Australia.

Paul is a well-respected technology author and active in
the community, writing in-depth technical articles, focused
on cybersecurity, Microsoft 365 and related cloud services.

He holds MCSE, MCSA, MCT certifications.

34

CYBER SECURITY REPORT 2026