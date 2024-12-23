```markdown
# 2021 NCC Group Annual Research Report

## Table of Contents
- [Executive Summary: Research at NCC Group (2021)](#executive-summary-research-at-ncc-group-2021)
- [Message from the Global Head of Research](#message-from-the-global-head-of-research)
- [Open Source Security Tool & Code Releases](#open-source-security-tool-code-releases)
- [Publicly Reported Security Audits](#publicly-reported-security-audits)
- [Applied Cryptography](#applied-cryptography)
- [Attacking (& Attacking with) Machine Learning Systems](#attacking-attacking-with-machine-learning-systems)
- [Misinformation, Deepfakes, & Synthetic Media](#misinformation-deepfakes-synthetic-media)
- [Reducing Vulnerabilities at Scale & Improving Open Source Security](#reducing-vulnerabilities-at-scale-improving-open-source-security)
- [Virtualization, Emulation, & Containerization](#virtualization-emulation-containerization)
- [Hardware & Embedded Systems](#hardware-embedded-systems)
- [5G Security & Smart Environments](#5g-security-smart-environments)
- [Public Interest Technology](#public-interest-technology)
- [Cloud & CI/CD Pipeline Security](#cloud-ci-cd-pipeline-security)
- [RIFT, Threat intelligence, CIRT, & Honeypots](#rift-threat-intelligence-cirt-honeypots)
- [Managed Detection & Response](#managed-detection-response)
- [Exploit Development Group](#exploit-development-group)
- [Other Research & Speaking](#other-research-speaking)
- [Acknowledgements](#acknowledgements)
- [About Research at NCC Group](#about-research-at-ncc-group)
- [Contact Us](#contact-us)

1
research.nccgroup.com

2021 NCC Group 
Annual Research Report 
Written by Jennifer Fernick
SVP & Global Head of Research, NCC Group

2

## Executive Summary: Research at NCC Group (2021)
In 2021, NCC Group researchers hacked 
drones out of the sky; attacked real-world 
machine learning systems; ironically gained 
RCE against Metasploit; released user-centric 
mobile privacy analysis tooling; advised US 
Congressional staffers about open source and 
supply chain security; asked whether GPT-3 
can generate exploits; reverse engineered 
Intel’s proprietary binary translator which runs 
ARM binaries on x86 to write targeted malware 
that bypasses existing platform analysis 
for platforms used by hundreds of millions; 
shared our expertise in Kubernetes security 
to help improve recommendations made 
by the NSA and CISA; discovered new 
vulnerability classes, and found many critical 
vulnerabilities in high-impact systems. 

We also delivered thousands of dedicated research 
days and over 237 research publications and conference 
presentations, pursuing research in areas including applied 
cryptography, hardware & embedded systems security, 
artificial intelligence, programming languages, operating 
systems, cloud & container security, exploit development, 
threat intelligence, vulnerability research against a range 
of high-impact targets, and beyond. We delivered 139 
research papers, whitepapers, and technical blog posts 
and advisories, at least 30 new open source tools, as well 
as at least 68 conference presentations, in venues including 
Black Hat USA, Toorcon, the Linux Foundation Member 
Summit, Ekoparty, Black Hat Europe, Hardwear.io, 
the ACM/SIGAPP Symposium on Applied Computing, the 
Symposium on Usable Privacy and Security (SOUPS), 
an IETF Internet Architecture Board Workshop, POC 
2021, the International Cryptographic Module 
Conference (ICMC), DEF CON, and many more.

This year, we also began to see our efforts to create 9 
internal Research Working Groups begin to bear fruit, 
through dozens of publications, advisories, and conference 
presentations that we’ll share throughout this report, as well 
as through increased global collaborative research across 
the firm, a stronger research community in which those 
new to research can explore ideas with experienced and 
world-class researchers in a radically open and inclusive 
environment, and a broadened and more interdisciplinary 
approach to security research. Our approach to research 
has been celebrated as a differentiator in the marketplace in 
the Forrester Wave™: European Cybersecurity Consulting 
Providers, Q3 2021 report, where it was noted that “NCC 
dedicates a large proportion of staff time (up to 20%) for 
own research projects, culminating in a lot of specialist 
security research and the development and release of open-
source tools, setting it apart on this dimension in a crowded 
field. NCC excels in its testing work and its research 
capabilities have made demonstrable improvements in 
security beyond its direct work on client projects.”

In 2021, we continued our long-running industry partnership 
with the Centre for Doctoral Training in Data Intensive 
Science at University College London (UCL), where we 
conducted collaborative research in artificial intelligence with 
UCL PhD students. Our research and standardization efforts 
included several contributions to the forthcoming version 
of the C programming language standard (C23), as well 
as contributions to the Center for Internet Security’s CIS 
Benchmarks for Microsoft 365, and IETF Internet Drafts and 
presentations before the IETF Internet Architecture Board. 
We also served on a number of advisory boards including 
the Industrial Advisory Board at King’s College London, the 
Governing Board and Technical Advisory Council of the 
Open Source Security Foundation, the Executive Steering 
Board for Internet of Things Security Foundation (IoTSF), 
the UK’s National Cyber Security Centre (NCSC) Research 
Advisory Panel, among others. We have also had members 
appointed to the Science Advisory Council for the United 
Kingdom’s Home Office. 

From a Commercial Research perspective, 2021 saw 
us deliver thousands of person-days of paid research 
for clients. Besides our Public Reports, that research is 
not covered in this Annual Research Report, aside from 
its mention here. Those engagements included horizon 
scanning on future technologies and their impacts for 
our clients, and research of various defensive techniques 
to help our clients in their risk reduction endeavours. 
We were also part of a winning research consortium for 
UKRI funding (£11.6m) on the topic of the Quantum Data 
Centre of the Future. Over the next 3 years we will provide 
security advice and guidance to the project as it sets out to 
define a blueprint for future secure Quantum Data Centres. 

NCC Group researchers Ross Bradley, Eva Esteban 
Molina, Philip Marsden, & Mark Tedman came in First 
Place at the global “5G Cyber Security Hack’’ competition 
this summer, hosted by by the Finnish Transport and 
Communications Agency, Aalto University, Cisco, Ericsson, 
Nokia, and PwC. Researchers Dale Pavey and Guy Morley 
were named the winners of the Best Ethical Hacker/
Pentester Award at the Security Serious Unsung Heroes 
Awards for their work with independent UK consumer body 
Which?, investigating the safety and security of a range of 
IoT devices, exposing a number of unsafe devices. Jennifer 
Fernick, our Global Head of Research, was named one of 
Canada’s Top 20 Women in Cybersecurity by IT World 
Canada. We also had the privilege to serve as Keynote 
Speakers for events like the Linux Foundation Member 
Summit, and the SANS Pentest Hack Fest, as well as 
serving on the program committees of influential security 
research venues including the USENIX Workshop on 
Offensive Technologies (WOOT), Toorcon, and Black 
Hat USA, among others. 
3

## Message from the Global Head of Research
As our world undergoes rapid social change 
and new norms for our relationship with 
information and with emerging technologies 
are set, I believe it is essential that as 
technologists, we connect with - and 
communicate about - our values, intentions, 
and the big questions that inspire us. It is 
my hope that through this report, readers 
can begin to see and interrogate themes that 
emerged across our wider security research 
program, reflective of the things that matter 
most to individuals across NCC Group. 

From my own view, in the past year, 
we’ve seen a number of themes:
- Time to exploitation of vulnerabilities in the wild 
has rapidly decreased. Industry research aligns with 
what we’re seeing in practice - time to exploitation of a 
vulnerability in the wild after a patch has been released 
has dropped from several weeks as of a few years ago, 
to only a few days now. This is challenging because it 
requires a seriously retooled approach to vulnerability 
management, and because it puts tremendous pressure
to patch on key intermediaries in the software supply 
chain - many of whom are open-source maintainers. 
- Misinformation kills. Much in the way that 2020 taught 
us that election security was hardly about the hardware 
at all, 2021 showed that the health of populations 
depends at least as much on a population’s scientific 
and media literacy as it does on the core scientific 
advancements themselves, and that social media 
companies may be playing potentially even more of 
a role in the health and safety of citizens than those 
individuals’ own democratically-elected leaders.
- Software supply chain security matters. It is no longer 
in the realm of the unusually paranoid to care not only 
about the security of our own code, but also about its 
upstream dependencies and its downstream deployment 
pipeline. Numerous high profile incidents in late 2020 
through 2021 emphasized this point - so much so, 
that U.S. President Biden issued an Executive Order 
largely aimed at remediating it.  
- Ransomware remains an unsolved problem. 
Despite it being a relatively uninteresting topic for most 
security researchers, ransomware is one of the greatest 
threats to digital security as perceived by both the general 
public and countless CISOs alike. Why then, is something 
this impactful being largely overlooked by the research 
community outside of threat intelligence teams? It seems 
like the best advice we have is for IT teams to patch 
everything, faster - but perfection is not a strategy. 
I would like to understand: In a world of limited resources, 
which interventions are the most effective at preventing 
ransomware infections? Sanctions against ransomware 
operators are likely the greatest tool we have, but that 
doesn’t erase the question of what technical solutions 
to this problem look like. 
- Geopolitical power increasingly depends on 
information access, and can swing faster than 
ever before. What does it mean when we put 
internet-enabled sensors into the things that keep 
us alive? What does it mean to put internet-enabled 
sensors into all of the things that make life worth living? 
Does our acceptance of that risk change when we 
imagine highly-skilled foreign adversaries a few 
keystrokes away?  
4

Jennifer Fernick
SVP & Global Head of Research at NCC Group

In 2022 and beyond, we’re going to face
a number of challenges, new and old. 
These include:
- Affective computing, brain-computer interfaces, 
and the broader question of where we draw the line 
as the physical distance between computers and 
human bodies grows increasingly small. With the 
increasing adoption of smart cities, smart buildings, and 
other sensor-rich IoT-connected environments, avoiding 
surveillance in daily life and in physical space becomes 
increasingly difficult, even on one’s own property. 
Compounded with the coming cultural normalization 
of wearable and even implantable sensors for gaming, 
entertainment, and the “metaverse” - not to mention 
the active commercial development of brain-computer 
interfaces - computers keep getting closer and closer to 
our bodies, behaviours, and emotions. I often worry that 
the last bastion of human freedom - one’s own mind - 
is being eroded quickly and quietly in irreparable ways. 
- Full-stack security auditing and defense of real-world 
machine learning systems.  The ubiquitous deployment 
of machine learning systems represents a significant 
and poorly-understood real-world attack surface. This is 
problematic because these systems are too frequently 
granted undue and unchecked autonomy over safety-
critical and socially-critical decisions, and also because 
machine learning models are code. Every enterprise 
AI system that as an industry we fail to secure can put 
the sensitive (and often irrevocable) data of millions or 
even billions of people at risk. Furthermore, insufficiently 
secure systems can open up both individuals and society 
to unjustified machine learning “decisions” that are often 
trusted implicitly - even if the machine that computed them 
is not trustworthy at all. Developing rigorous, full-stack 
threat models and testing frameworks is critical and 
urgent work.
- The rapid advancement of large language models 
in artificial intelligence. Large-scale natural language 
models such as GPT-3 and others have been scaling at 
1-2 orders of magnitude per year, and the generalizable 
performance of transformer models seems to improve 
- even over domain-specific models - with increasing 
scale. While this may not necessarily mean that artificial 
general intelligence is imminent, we would be unwise 
to underestimate the impact that the weaponization of 
large natural language processing models trained on 
a corpus of the world’s source code and vulnerability 
databases could have on software security and the safety 
of the internet. For example, we might ask, could large 
language models like GPT-3 or its’ successors generate 
exploits of software vulnerabilities? Can low-code A.I. 
pair-programming tools create or propagate unsafe code? 
To answer these questions completely requires further 
research, but there are compelling reasons to believe 
that the answer is yes.  
- The relative monoculture of the public cloud’s 
attack surface making the exploitation of singular 
vulnerabilities more socially and economically 
catastrophic. The public cloud made incredible 
computing possible at scale - but with software 
infrastructure of such homogeneity, it also made 
vulnerability exploitation possible at scale, raising 
the intrinsic cost or risk of the existence of individual 
vulnerabilities in these high-value targets. The question 
then becomes: what does this mean for the value of 
vulnerabilities in the global “marketplace,” and how 
might that change how vendors (and researchers) 
approach the security of these systems?
- Decentralized finance (“DeFi”) coupling code and 
money more tightly than ever before, forcing those 
who believe “code is law” to reckon with the fact that 
all software has flaws. Large financial institutions 
each spend hundreds of millions - sometimes even 
billions - per year on cybersecurity, because they 
know that failing to do so may cost them even more. 
Are proportional investments being made in decentralized 
finance applications and cryptocurrencies? Not usually. 
While improvements in cyber resilience today are largely 
driven by regulatory interventions, in the sphere of 
decentralized finance (DeFi), where value is exclusively 
stored digitally and mediated directly by code, a threat 
actor could directly and immediately remove value from a 
company through attacking the underlying infrastructure, 
protocols, or cryptographic implementations. One leaked 
cryptographic key or a single software flaw could lead to 
the collapse of entire organizations.Time will tell whether 
we will see a bottom-up, market-driven push for higher 
assurance systems for serious decentralized finance 
companies, or whether they will become the highest-risk 
value stores on the planet.
- As the COVID-19 pandemic rages on, how do 
we maintain privacy in a world in which we are 
accountable to one another?  In our research this 
year, we conducted wide-ranging research into the 
security & privacy aspects of various jurisdictions’ 
vaccine passports, but other new forms of attestation 
and surveillance - including smart buildings, enhanced 
genomic and health testing, and mobile passports - 
remain under-studied by the security research community. 
Furthermore, the pandemic has breathed new life 
into large tech companies’ VR and augmented reality 
ambitions (“the metaverse”) which will affect not only 
the security and privacy of our devices and homes, 
but invites new kinds of sensors and interfaces (perhaps 
even brain-computer interfaces) which will be perhaps 
more intrinsically connected to our bodies, minds, 
and behaviour that anything we’ve seen before. 
- Finally, we must ask ourselves, what are the grand 
challenges for cybersecurity? What are the problems 
that matter the most to the security & privacy of 
individuals, organizations, and the internet? As an 
industry, we face a reckoning in which I believe that 
we need to elevate ourselves toward taking a more 
“scientific” and rigorous approach to the study of 
information security cause and effect, and let go of the 
unspoken agreements, copycat risk-mitigations, hearsay 
“best practices,” and other unacceptable industry norms. 
While the development of obscure and complex 
exploit chains will always have its place to enable us to 
understand the true frontiers of what we’re up against, 
it is time to prioritize the problems that most meaningfully 
affect the world in which we live. It is my intent that we 
become more methodical in our study of the mitigations 
of specific cybersecurity threats, to move beyond a world 
where companies sometimes feel they have no choice 
but to sink money into the same expensive and at times 
incomplete or misconfigured security products as their 
peers, without a real understanding of their effectiveness, 
and instead to a world where they are empowered 
through an understanding of the actual costs of both 
attack and defense.
5

## Open Source Security Tool & Code Releases
In 2021, we released around 30 open source security tools, major tool updates, implementations, 
or other open-source repositories. Among the security tools released by NCC Group this year are:
- Covenant v0.7: Covenant is an open source .NET 
command and control framework that supports Red Team 
operations, similar in many ways to the well-known Cobalt 
Strike threat emulation software. NCC Group’s Simone 
Salucci and Daniel Lopez Jimenez contributed a number 
of features to the project that they desired while using it. 
Some of those features include: Disabling ETW, Dumping 
Snapshot Processes, Process Injection Tasks, Payload 
Execution Guardrails and Other Pull Requests
- GTFOBLookup: An offline command line lookup utility 
for GTFOBins, LOLBAS, and WADComs, created 
by James Conlan
- KilledProcessCanary: A prototyped a Windows 
Service Canary in order to target parts of the 
ransomware kill chain to minimize impact and overall 
success of operations, created by Ollie Whitehouse. 
The tool was described in his blog post, Deception 
Engineering: exploring the use of Windows Service 
Canaries against ransomware.
- Libptmalloc: Heap analysis tooling for ptmalloc 
(pthreads malloc), and is interesting to those seeking to 
exploit glibc, created by Cedric Halbronn. This was part 
of the work discussed in the blog post, Exploiting the 
Sudo Baron Samedit vulnerability (CVE-2021-3156) 
on VMWare vCenter Server 7.0.  
- Log4j-jndi-be-gone: A simple mitigation for CVE-2021-
44228 (Log4Shell), created to help mitigate the log4j 
vulnerabilities which saw widespread exploitation in 
December 2021, by Jeff Dileo. This tool uses the Byte 
Buddy bytecode manipulation library to modify the at-issue 
log4j class’s method code and short circuit the JNDI 
interpolation handler. It works by effectively hooking the 
at-issue JndiLookup class’ lookup() method that 
Log4Shell exploits to load remote code, and forces it to 
stop early without actually loading the Log4Shell payload 
URL.
- ML-for-RNGs: The Jupyter notebooks underlying 
research exploring the utility of deep learning to predict 
the sequence of the (presumably) random output 
numbers using previously generated numbers without the 
knowledge of the seed for (non-cryptographic) PRNGs 
xorshift128 and Mersenne Twister, by Mostafa Hassan. 
While this research looked at a non-cryptographic 
PRNGs, we are interested, generically, in understanding 
how deep learning-based approaches to finding latent 
patterns within functions presumed to be generating 
random output could work, as a prerequisite to attempting 
to use deep learning to detect previously-unknown 
patterns in cryptographic (P)RNGs. 
- Ndsp-discover: An Nmap script to identify Netgear 
Switch Discovery Protocol (NSDP) on UDP ports 63322 
and 63324, by Manuel Ginés Rodríguez. This tool was 
created in support of Manuel’s extensive vulnerability 
research on the Netgear ProSAFE Plus switches.
- NLAhoney:  Source code to deploy honeypots that 
can capture RDP handshakes, then crack them offline 
in an effort to understand which passwords are being 
sprayed at RDP honeypots we deploy, created by 
Ollie Whitehouse and Ray Lai, as a part of their 
project, Cracking RDP NLA Supplied Credentials 
for Threat Intelligence. 
- Principal Mapper (v1.1.0 Update; v1.1.4 Update):  
Principal Mapper, or PMapper, is a tool and library 
for in-depth analysis with AWS Identity and Access 
Management, as well as AWS Organizations. 
PMapper stores data about AWS accounts and 
organizations, then provides options to query, visualize, 
and analyze that data. The library is written in Python 
and was created by Erik Steringer. 
- Raccoon: is a tool that aims to identify potential 
misconfigurations that could expose sensitive data within 
Salesforce. Specifically, it reveals where access has been 
granted to all records for particular objects of interest, 
by Jerome Smith.
- Reliably-checked String Library Binding: is a library 
binding that uses static array extents to improve 
diagnostics that can help identify memory safety flaws, 
created by Robert Seacord. 
- Ruby-trace: A Low-Level Tracer for Ruby, created by 
Jeff Dileo and originally released to coincide with his DEF 
CON 29 talk on it and parasitic tracing in general. Version 
1.1.0 adds support for the newly released Ruby 3.1 and 
includes a number of improvements, including alternate 
enable/disable hooks. 
- Shouganaiyo-loader: A cross-platform Frida-based 
Node.js command-line tool that forces Java processes 
to load a Java/JVMTI agent regardless of whether or not 
the JVM has disabled the agent attach API, created by 
Jeff Dileo.
- Sigwhatever: For automated exploitation of netntlm hash 
capture via image tags in emails signatures. The tool was 
described in their blog post, Sign over Your Hashes – 
Stealing NetNTLM Hashes via Outlook Signatures 
created by David Cash, Rich Warren, Julian Storr.
- SocksOverRDP:  This tool adds the capability of a 
SOCKS proxy to Terminal Services (or Remote Desktop 
Services) and Citrix (XenApp/XenDesktop). It uses 
6
Dynamic Virtual Channel that enables us to communicate 
over an open RDP/Citrix connection without the need to 
open a new socket, connection or a port on a firewall. 
The author, Balazs Bucsay, presented the tool at the 
Cyber Security Global Summit by Geekle.
- Solitude: Solitude is an open source privacy analysis 
tool that enables you to conduct your own privacy 
investigations into where your private data goes once it 
leaves your web browser or mobile device. Whether a 
curious novice or a more advanced researcher, Solitude 
makes the process of evaluating an app’s privacy 
accessible for everyone, created by Dan Hastings. 
Solitude was featured in media outlets including KitPloit, 
Hacking Land, and Hacking Reviews.
- Squeak: The tool was described in their blog post, 
MSSQL Lateral Movement, created by David Cash. 
This tool supports the work outlined within the blogpost: 
namely, the automation of lateral movement via MSSQL 
CLR without touching disk (besides a DLL being 
temporarily written to disk by the SQL Server process) 
or requiring XP_CMDSHELL.
- UninstalledAppCanary: This project deploys a number 
of canary apps which fire when uninstalled, motivated by 
the idea that certain threat actors uninstall a number of 
products prior to dropping later stages, and was created 
by Ollie Whitehouse. The tool was described in his 
blog post, Deception Engineering: exploring the use of 
Windows Installer Packages against first stage payloads, 
and builds upon prior work discussed in the blog post 
Deception Engineering: exploring the use of Windows 
Service Canaries against ransomware.
- Wubes: is like Qubes (a security-focused operating 
system that aims to provide security through virtualization) 
but for Microsoft Windows. The purpose is to leverage 
the Windows Sandbox technology to spawn applications 
in isolation, so that if you browse a malicious site using 
Wubes, it won’t be able to infect your Windows host 
without additional chained exploits. Currently it supports 
spawning a Windows Sandbox for the Firefox browser but 
other applications can easily be added, and was created 
by Cedric Halbronn.
We also released source code for a variety 
of cryptographic implementations, exploit 
proofs-of-concept, and obfuscation 
reverse-engineering techniques:
- In January 2021, Jeff Dileo released proof-of-concept 
exploit code for his vulnerability, CVE-2020-15257, found 
in containerd - a container runtime underpinning Docker 
and common Kubernetes configurations - which resulted 
in full root container escape for a common container 
configuration. This was discussed in depth in his blog 
post titled, ​ABSTRACT SHIMMER (CVE-2020-15257): 
Host Networking is root-Equivalent, Again. 
- In January 2021, Thomas Pornin published a blog post 
on Double-odd Elliptic Curves, which discussed some 
new elliptic curves he had created for cryptographic 
protocols. These were published on a dedicated 
website, doubleodd.group. He also released a 
complete whitepaper on the IACR ePrint archive, full of 
mathematical demonstrations, and several cryptographic 
implementations of double-odd elliptic curves in Python, 
Go, C, and Assembly. 
- In June 2021, Cedric Halbronn published Exploit 
mitigations: Keeping up with evolving and complex 
software/hardware, seeking to address how it has 
become challenging to follow when certain exploit 
mitigations are added in an update and/or backported to 
some older versions of various software and hardware, 
by creating his mitigations tables which track mitigations 
exploit mitigations available across numerous operating 
systems (Windows, Linux, Android, iOS, OpenBSD, 
FreeBSD), architectures (ARM) and applications and 
versions, including the glibc library, Mozilla Firefox, 
Microsoft Edge, Google Chrome, and Microsoft Office.  
- In September 2021, Eric Schorn released his 
implementations of montgomery multiplication in 
assembly, alongside a blog post titled Optimizing Pairing-
Based Cryptography: Montgomery Multiplication in 
Assembly, which discussed and demonstrated selected 
optimizations found in pairing-based cryptography, 
foundational to the BLS Signatures central to Ethereum 
2.0, zero-knowledge arguments central to Zcash, Filecoin, 
and other blockchain/cryptocurrency projects relying 
upon zk-proofs.  
- In October 2021, Thomas Pornin implemented a 
mathematically-impossible lossless compression 
algorithm, alongside a blog post titled Paradoxical 
Compression with Verifiable Delay Functions, and 
released a paper on the IACR ePrint archive. 
- In October 2021, Nicolas Guigo released tools and 
methods for reversing real-world binary obfuscation, 
through a blog post titled A Look At Some Real-World 
Obfuscation Techniques.
- Outside of research, in late 2021 our Strategic Threat 
Intelligence team created a public github repository, 
Threat-Intelligence-Alerts, where they publish alerts 
about major vulnerabilities, exploits, and mitigations 
on an ongoing basis.  
7

## Publicly Reported Security Audits
For many years, NCC Group has published 
publicly-reported security audits of critical 
components of open source software as well 
as select proprietary systems, including in 
past years for components of important 
systems including OpenSSL, SecureDrop, 
TrueCrypt, Tor, Docker, Keybase, Zcash, 
and many others. 

Of these reports, those labelled “Public 
Report” were developed as a part of a paid 
engagement with an NCC Group client for 
NCC Group to conduct and publish the 
findings of a security audit on in-scope 
components. In 2021, NCC Group delivered 
8 Public Reports across a number of different 
cryptographic implementations, as well as for 
the Google One VPN and WhatsApp End-to-
End Encrypted Backups, among others..
Our 2021 Public Reports include:
- Public Report – BLST Cryptographic Implementation Review (January 2021)
- Public Report – VPN by Google One: Technical Security & Privacy Assessment (April 2021)
- Public Report – Dell Secured Component Verification (May 2021)
- Public Report – Protocol Labs Groth16 Proof Aggregation: Cryptography and Implementation 
Review (June 2021)
- Public Report – WhatsApp End-to-End Encrypted Backups Security Assessment (October 2021)
- Public Report – Zcash NU5 Cryptography Review (November 2021)
- Public Report – Zendoo Proof Verifier Cryptography Review (November 2021)
- Public Report - Whatsapp opaque-ke Cryptographic Implementation Review (December 2021)
8

## Applied Cryptography
- In January 2021, Thomas Pornin published a blog post about his 
recent work on Double-odd Elliptic Curves. Double-odd curves 
are the elliptic curves whose order (number of points on the 
curve) is the double of an odd integer. About 1/4th of all curves 
are double-odd curves: this is a large class of curves, and Such 
curves have nominally been supported by generic standards 
such as ANSI X9.62 (ECDSA signatures over any curve) for 
the last two decades. He notes that the point of double-odd 
elliptic curves is to provide a safe structure, amenable to building 
cryptographic protocols on top of the “prime order group” 
abstraction, but that they also offer performance improvements 
over generic elliptic curves, making them especially useful for 
small embedded systems with severe constraints on power, RAM 
and CPU abilities. There is also a complete whitepaper published 
on the IACR ePrint archive, full of mathematical demonstrations; 
it also specifies the use of do255e and do255s in higher-level 
cryptographic functionalities (key pair generation, key exchange, 
signature, and hash-to-curve). Thomas has also released 
several cryptographic implementations, as well as a geometric 
introduction which helps build mathematical intuition related to 
double-odd curves. 
- In January 2021, our Cryptography Services team (virtually) 
attended the Real-World Cryptography conference, and published 

a blog post in which they shared summaries and insights from 
some of our favourite talks from RWC 2021.
- In January 2021, we published the NCC Group Cryptography 
Services Public Report on the BLST Cryptographic 
Implementation Review. This involved a cryptographic 
implementation review of the BLST library, which implements 
support for the draft IETF specifications on Hashing to Elliptic 
Curves and BLS Signatures. The latter specification uses 
advanced cryptographic-pairing operations to feature aggregation 
properties for secret keys, public keys and signatures, which 
is central to the emerging Ethereum 2.0 Proof-of-Stake 
block-validation mechanism. This report was commissioned 
by Supranational, Protocol Labs and the Ethereum Foundation. 
- In January 2021, Gérald Doussot published Software Verification 
and Analysis Using Z3. This post provided a technical introduction 
on how to leverage the Z3 Theorem Prover to reason about the 
correctness of cryptographic software, protocols and otherwise, 
and to identify potential security vulnerabilities. In this post, 
he covered both: (1) Modeling and analysis of an algorithm 
documented in an old version of the QUIC Transport protocol 
IETF draft, as well as (2) Modeling of specific finite field 
arithmetic operations for elliptic curve cryptography, with integers 
represented using a uniform saturated limb schedule (four limbs of 
64 bits), to prove equivalence with arbitrary-precision arithmetic, 
and for test case generation. In February, researchers from Galois 
published a blog post, “Cryptol as an SMT Frontend,” referencing 
Gérald’s research, in which they checked the implementation of 
part of the QUIC protocol, and built upon this work in June 2021, 
“Cryptographic Assurance with Cryptol,” which they explore an 
optimized implementation of field arithmetic.
- In February 2021, Eli Sohl published Cryptopals: Exploiting CBC 
Padding Oracles. This post - which was the first in a new series 
by Eli which offers educational walkthroughs of the beloved 
Cryptopals cryptography challenges - explored the classic 
padding oracle attack on CBC-mode block ciphers, through the 
lens of Cryptopals challenge #17. 
- In June 2021 we published the NCC Group Cryptography 
Services Public Report on the cryptography and implementation 
review of Protocol Labs Groth16 Proof Aggregation. This was 
a cryptography and implementation review of the Groth16 proof 
aggregation functionality in the bellperson and two other related 
GitHub repositories. This code utilizes inner product arguments to 

efficiently aggregate existing Groth16 proofs while reusing 
existing powers of tau ceremony transcripts. This report was 
commissioned by Protocol Labs. 
- In June 2021, NCC Group’s Thomas Pornin - alongside external 
peers Liz Steininger, isis agora lovecruft, JP Aumasson, and 
Taylor Hornby - spoke on a panel on Auditing Cryptography at the 
Zcash Foundation’s conference, Zcon2lite.
9
- In June 2021, Parnian Alimi published On the Use of 
Pedersen Commitments for Confidential Payments. 
This blog post looked at the Zether protocol, which 
uses ElGamal public key encryption to hide transaction 
amounts and utilizes zero-knowledge proofs to 
demonstrate the validity of a transaction to stakeholders 
in a financial blockchain, namely network validators, 
investors, and auditors. In general, this is important to 
the principle of transaction confidentiality, desirable 
for some financial blockchains, which requires hiding 
investors’ account balances and transaction amounts, 
while enforcing compliance rules and performing validity 
checks on all activities. The post also explains underlying 
cryptographic building blocks including Pedersen 
Commitment, ElGamal Encryption, and Zero-Knowledge 
Proofs, and